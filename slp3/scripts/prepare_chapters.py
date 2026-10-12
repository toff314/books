#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
prepare_chapters.py — 按书签批量切分章节 PDF，并跑结构提取 + 分片。

用法:
    python3 scripts/prepare_chapters.py                # 全部章节
    python3 scripts/prepare_chapters.py --only 02 03   # 只跑指定章
    python3 scripts/prepare_chapters.py --skip-existing
产出:
    build/<slug>-en.pdf       单章英文 PDF
    build/<slug>/doc.json     结构提取结果
    build/<slug>/chunks/*.json 翻译分片
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
import time
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent
SRC = BOOK / "source" / "ed3book_aug26.pdf"
SKILL = Path(os.environ.get("PDF_TRANSLATE_SKILL", "/home/yuanwu/zhihu-wiki/skills/pdf-translate"))
PY = SKILL / ".venv" / "bin" / "python"

# (序号, slug, 中文标题, 起始物理页, 结束物理页)  —— 页码取自 PDF 书签
CHAPTERS = [
    ("01", "introduction", "第 1 章 引言", 11, 40),
    ("02", "words-and-tokens", "第 2 章 词与词元", 41, 75),
    ("03", "ngram-language-models", "第 3 章 N-gram 语言模型", 76, 99),
    ("04", "logistic-regression", "第 4 章 逻辑回归", 100, 134),
    ("05", "embeddings", "第 5 章 嵌入", 135, 158),
    ("06", "neural-networks", "第 6 章 神经网络", 159, 184),
    ("07", "transformers-and-pretraining", "第 7 章 Transformer 与预训练", 185, 216),
    ("08", "post-training", "第 8 章 后训练", 217, 232),
    ("09", "masked-language-models", "第 9 章 掩码语言模型", 235, 250),
    ("10", "interpretability", "第 10 章 可解释性", 251, 259),
    ("11", "retrieval-based-models", "第 11 章 基于检索的模型", 260, 282),
    ("12", "agents", "第 12 章 智能体", 283, 283),
    ("13", "machine-translation", "第 13 章 机器翻译", 284, 309),
    ("14", "rnns-and-lstms", "第 14 章 RNN 与 LSTM", 310, 335),
    ("15", "phonetics-and-speech", "第 15 章 语音学与语音特征提取", 336, 364),
    ("16", "speech-recognition", "第 16 章 自动语音识别", 365, 390),
    ("17", "text-to-speech", "第 17 章 文本转语音", 391, 404),
    ("18", "sequence-labeling", "第 18 章 词性与命名实体的序列标注", 408, 432),
    ("19", "cfg-and-parsing", "第 19 章 上下文无关文法与成分句法分析", 433, 456),
    ("20", "dependency-parsing", "第 20 章 依存句法分析", 457, 480),
    ("21", "information-extraction", "第 21 章 信息抽取：关系、事件与时间", 481, 506),
    ("22", "semantic-role-labeling", "第 22 章 语义角色标注", 507, 526),
    ("23", "lexicons-sentiment", "第 23 章 情感、态度与内涵词表", 527, 546),
    ("24", "coreference-entity-linking", "第 24 章 共指消解与实体链接", 547, 576),
    ("25", "discourse-coherence", "第 25 章 篇章连贯", 577, 598),
    ("26", "conversation-structure", "第 26 章 会话及其结构", 599, 606),
]


def slug_of(num: str, name: str) -> str:
    return f"{num}-{name}"


def split_one(num: str, name: str, first: int, last: int) -> Path:
    """切出单章 PDF（幂等）。"""
    out = BOOK / "build" / f"{slug_of(num, name)}-en.pdf"
    if out.is_file() and out.stat().st_size > 0:
        return out
    code = (
        "import pymupdf,sys;"
        f"s=pymupdf.open(r'{SRC}');o=pymupdf.open();"
        f"o.insert_pdf(s, from_page={first - 1}, to_page={last - 1});"
        f"o.set_metadata({{'title':'SLP3 {num} {name}'}});"
        f"o.save(r'{out}');print(o.page_count)"
    )
    subprocess.run([str(PY), "-c", code], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="批量切章 + 结构提取 + 分片")
    ap.add_argument("--only", nargs="*", default=None, help="只处理这些章号，如 02 03")
    ap.add_argument("--skip-existing", action="store_true", help="已有 chunks 的章节跳过")
    ap.add_argument("--size", type=int, default=40, help="每片最大块数")
    ap.add_argument("--max-chars", type=int, default=8000, help="每片最大字符数")
    args = ap.parse_args()

    targets = [c for c in CHAPTERS if not args.only or c[0] in args.only]
    print(f"待处理章节: {len(targets)}")

    for num, name, title, first, last in targets:
        slug = slug_of(num, name)
        work = BOOK / "build" / slug
        chunks = work / "chunks"

        if args.skip_existing and chunks.is_dir() and any(chunks.glob("chunk_*.json")):
            print(f"  [{num}] {title} — 已存在分片，跳过")
            continue

        t0 = time.time()
        pdf = split_one(num, name, first, last)
        r1 = subprocess.run([str(PY), str(SKILL / "scripts" / "extract_pdf.py"), str(pdf), "-o", str(work)],
                            capture_output=True, text=True)
        if r1.returncode != 0:
            print(f"  [{num}] {title} — 提取失败: {r1.stderr.strip()[:200]}")
            continue
        r2 = subprocess.run([str(PY), str(SKILL / "scripts" / "plan_chunks.py"),
                             str(work / "doc.json"), "-o", str(work),
                             "--size", str(args.size), "--max-chars", str(args.max_chars)],
                            capture_output=True, text=True)
        if r2.returncode != 0:
            print(f"  [{num}] {title} — 分片失败: {r2.stderr.strip()[:200]}")
            continue

        n_chunks = len(list(chunks.glob("chunk_*.json")))
        info = [l for l in r1.stdout.split("\n") if "可译块" in l]
        print(f"  [{num}] {title} — {n_chunks} 分片  {info[0].strip() if info else ''}  ({time.time()-t0:.1f}s)")

    print("完成。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
