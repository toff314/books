#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_book.py — 把某一章的翻译产物构建为 Markdown / HTML / PDF（中文 + 中英对照）。

前置：该章的 translated.json 已由 pdf-translate 流水线产出，位于 build/<slug>/。

用法:
    python3 scripts/build_book.py --slug 01-introduction --title "第 1 章 绪论" --dual
产出:
    zh/md/<slug>.md              中文 Markdown
    zh/md/<slug>.dual.md         中英对照 Markdown（--dual）
    zh/html/<slug>.html          在线阅读 HTML
    zh/pdf/<slug>-zh.pdf         中文 PDF
    zh/dual/<slug>-dual.pdf      中英对照 PDF（--dual）

依赖 pdf-translate 技能（路径可用环境变量 PDF_TRANSLATE_SKILL 覆盖）。
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent
REPO = BOOK.parent
SKILL = Path(os.environ.get("PDF_TRANSLATE_SKILL", "/home/yuanwu/zhihu-wiki/skills/pdf-translate"))
PY = SKILL / ".venv" / "bin" / "python"


def run(cmd: list) -> None:
    print("  $", " ".join(str(c) for c in cmd))
    subprocess.run([str(c) for c in cmd], check=True)


def build(slug: str, title: str, dual: bool, out_pdf: bool) -> None:
    work = BOOK / "build" / slug
    translated = work / "translated.json"
    if not translated.is_file():
        sys.exit(f"[ERROR] 找不到 {translated}，请先跑完 pdf-translate 的 extract/plan/merge")

    md_dir = BOOK / "zh" / "md"
    html_dir = BOOK / "zh" / "html"
    pdf_dir = BOOK / "zh" / "pdf"
    dual_dir = BOOK / "zh" / "dual"
    for d in (md_dir, html_dir, pdf_dir, dual_dir):
        d.mkdir(parents=True, exist_ok=True)

    # 1. Markdown（中文 + 可选对照）
    md_cmd = [PY, SKILL / "scripts" / "build_markdown.py", translated, "-o", md_dir,
              "--slug", slug, "--title", title, "--img-subdir", slug]
    if dual:
        md_cmd.append("--bilingual")
    run(md_cmd)

    # 2. HTML（在线直读）——图片直接引用 md/images，不重复拷贝
    nav = (f'<div class="nav"><a href="../../index.html">← 返回书目</a>'
           f'<a href="../md/{slug}.md">Markdown 源文件</a></div>')
    img_prefix = "" if html_dir == md_dir else "../md/"
    run(["python3", REPO / "scripts" / "md2html.py", md_dir / f"{slug}.md",
         "-o", html_dir, "--title", title, "--nav", nav, "--img-prefix", img_prefix])
    if dual:
        run(["python3", REPO / "scripts" / "md2html.py", md_dir / f"{slug}.dual.md",
             "-o", html_dir, "--title", f"{title}（中英对照）", "--nav", nav,
             "--img-prefix", img_prefix])

    if not out_pdf:
        return

    # 3. PDF（中文 / 对照）
    run([PY, SKILL / "scripts" / "build_html.py", translated, "-o", work, "--mode", "both"])
    run([PY, SKILL / "scripts" / "render_pdf.py", work / "mono.html",
         "-o", pdf_dir / f"{slug}-zh.pdf"])
    if dual:
        run([PY, SKILL / "scripts" / "render_pdf.py", work / "dual.html",
             "-o", dual_dir / f"{slug}-dual.pdf"])


def main() -> int:
    ap = argparse.ArgumentParser(description="章节构建：translated.json → md / html（默认不渲染分章 PDF）")
    ap.add_argument("--slug", required=True, help="章节 slug，如 01-introduction")
    ap.add_argument("--title", default="", help="中文标题")
    ap.add_argument("--dual", action="store_true", help="同时产出中英对照版")
    ap.add_argument("--pdf", action="store_true",
                    help="额外逐章渲染 PDF（默认不渲染；整本 PDF 用 scripts/build_pdf_book.py 产出）")
    args = ap.parse_args()

    build(args.slug, args.title or args.slug, args.dual, args.pdf)
    print("[OK] 构建完成")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
