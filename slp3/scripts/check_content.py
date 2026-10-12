#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_content.py — 译文内容质量门禁（不只看"翻没翻"，还看"翻得对不对、干不干净"）。

检测项：
  H1 页眉/页脚残留        —— 文本形如 "1.1 • 标题 5"、"4 第 1 章 • 引言"
  H2 页眉内联污染          —— 正文段落中间夹杂页眉片段
  H3 图注被误检为表格      —— 表格含全空列 / `<br>` 堆叠 / 超长单元格
  H4 段落被切碎            —— 过短段落（跨页断开）
  H5 图片引用缺失          —— md 引用的图片文件不存在
  H6 空译 / 重复块

用法:
    python3 scripts/check_content.py <slug> [slug...]
    python3 scripts/check_content.py --all
"""
from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent

# "1.1 • 什么是大型语言模型？ 5" 或 "4 第 1 章 • 引言"
HEADER_PATTERNS = [
    re.compile(r"^\s*\d+(\.\d+)*\s*•.{0,70}?\s*\d+\s*$"),
    re.compile(r"^\s*\d+\s+第\s*\d+\s*章\s*•"),
    re.compile(r"第\s*\d+\s*章\s*•.{0,40}\s+\d+\s*$"),
]
HEADER_INLINE = re.compile(r"[^。；\n]{6,40}?\s\d{1,3}\s第\s\d+\s章\s*•\s[^ ]{1,20}\s[^。；\n]{6,40}")
CJK = re.compile(r"[\u4e00-\u9fff]")
SENT_END = ("。", "！", "？", "…", "”", '"', ".", "!", "?", "：", "；", ":", ";")


def _is_header(text: str) -> bool:
    t = (text or "").strip()
    if not t or len(t) > 90:
        return False
    return any(p.search(t) for p in HEADER_PATTERNS)


def check(slug: str) -> dict:
    work = BOOK / "build" / slug
    md = BOOK / "zh" / "md" / f"{slug}.md"
    issues: dict[str, list] = {k: [] for k in ("H1", "H2", "H3", "H4", "H5", "H6")}

    tj = work / "translated.json"
    if tj.is_file():
        doc = json.loads(tj.read_text(encoding="utf-8"))
        seen = set()
        prev_kind = None
        prev_text = ""
        for p in doc.get("pages", []):
            for b in p.get("blocks", []):
                kind = b.get("block_type") or b.get("type")
                zh = (b.get("zh") or "").strip()
                src = (b.get("text") or "").strip()

                if kind in ("heading", "paragraph", "note", "caption") and zh:
                    if _is_header(zh) or _is_header(src):
                        issues["H1"].append(f'{b.get("id")} :: {zh[:50]}')
                    if HEADER_INLINE.search(zh):
                        issues["H2"].append(f'{b.get("id")} :: …{HEADER_INLINE.search(zh).group()[:60]}…')
                    if zh in seen and kind != "note":
                        issues["H6"].append(f'{b.get("id")} :: 重复段落 {zh[:30]}')
                    seen.add(zh)
                prev_kind, prev_text = kind, zh

                if kind == "table":
                    rows = b.get("zh_rows") or b.get("rows") or []
                    if not rows:
                        continue
                    width = max(len(r) for r in rows)
                    empty_col = any(
                        all(not ((r[c] if c < len(r) else "").strip()) for r in rows)
                        for c in range(width)
                    )
                    longest = max((len(str(c)) for r in rows for c in r), default=0)
                    brs = sum(str(c).count("<br>") for r in rows for c in r)
                    if empty_col or longest > 200 or brs >= 3:
                        issues["H3"].append(
                            f'{b.get("id")} :: 空列={empty_col} 最长单元格={longest} <br>数={brs}'
                        )

    if md.is_file():
        text = md.read_text(encoding="utf-8")
        # H4：以最终 Markdown 为准——真正的版面切断会让段落不以句末标点结束
        for para in (p.strip() for p in text.split("\n\n")):
            if not para or para.startswith(("#", "!", "|", ">", "*", "-")):
                continue
            if CJK.search(para) and not para.endswith(SENT_END):
                issues["H4"].append(f"md :: …{para[-28:]}")
        for ref in set(re.findall(r"!\[\]\(([^)]+)\)", text)):
            if not (md.parent / ref).exists():
                issues["H5"].append(ref)

    total = sum(len(v) for v in issues.values())
    return {"slug": slug, "issues": issues, "total": total}


def main() -> int:
    ap = argparse.ArgumentParser(description="译文内容质量检查")
    ap.add_argument("slugs", nargs="*")
    ap.add_argument("--all", action="store_true", help="检查所有已构建章节")
    ap.add_argument("--show", type=int, default=4)
    args = ap.parse_args()

    slugs = args.slugs
    if args.all:
        slugs = [p.name.replace(".md", "") for p in sorted((BOOK / "zh" / "md").glob("*.md"))
                 if not p.name.endswith(".dual.md")]

    labels = {
        "H1": "页眉/页脚残留", "H2": "页眉内联污染", "H3": "图注误检为表格",
        "H4": "段落被切碎", "H5": "图片引用缺失", "H6": "重复/异常块",
    }
    bad = 0
    for slug in slugs:
        r = check(slug)
        flag = "OK" if r["total"] == 0 else "ISSUES"
        print(f"[{flag}] {slug}  问题合计={r['total']}")
        for k, v in r["issues"].items():
            if v:
                bad += 1
                print(f"    {k} {labels[k]}: {len(v)}")
                for item in v[: args.show]:
                    print(f"       - {item}")
                if len(v) > args.show:
                    print(f"       … 其余 {len(v) - args.show} 条")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
