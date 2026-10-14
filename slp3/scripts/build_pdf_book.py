#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_pdf_book.py — 把全书各章合成**一份** PDF（中文整本 / 中英对照整本）。

设计：书籍层只渲染一次，而不是逐章渲染 26×2 份 PDF。
流程：各章 build/<slug>/{mono,dual}.html 的 <body> 拼接成一份「书级 HTML」
      （封面 + 目录 + 每章分页）→ pdf-translate 技能的 render_pdf.py 渲染 → 一份 PDF。

用法:
    python3 scripts/build_pdf_book.py              # 中文整本 + 对照整本
    python3 scripts/build_pdf_book.py --mode mono  # 只要中文整本
产出:
    build/_book/mono.html / dual.html   （中间产物）
    zh/pdf/slp3-zh.pdf                  中文整本
    zh/dual/slp3-dual.pdf               中英对照整本
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent
SKILL = Path(os.environ.get("PDF_TRANSLATE_SKILL", "/home/yuanwu/zhihu-wiki/skills/pdf-translate"))
PY = SKILL / ".venv/bin/python"


def chapters() -> list[tuple[str, str]]:
    """按 SUMMARY.md 的顺序返回 [(slug, 中文标题)]，只取已有 translated.json 的章。"""
    txt = (BOOK / "SUMMARY.md").read_text(encoding="utf-8")
    out, seen = [], set()
    for m in re.finditer(r"\(zh/html/([0-9][0-9a-z-]*)\.html\)", txt):
        slug = m.group(1)
        if slug in seen:
            continue
        seen.add(slug)
        line = txt[:m.start()].rsplit("\n", 1)[-1]
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        title = cells[1] if len(cells) >= 2 else slug
        if (BOOK / "build" / slug / "translated.json").is_file():
            out.append((slug, title))
    return out


def extract(html: str) -> tuple[str, str]:
    """取出 <style>…</style> 与 <body …>…</body> 内部 HTML。"""
    style = "".join(re.findall(r"<style[^>]*>(.*?)</style>", html, re.S))
    body = re.search(r"<body[^>]*>(.*?)</body>", html, re.S)
    return style, (body.group(1) if body else html)


def build(mode: str, chs: list[tuple[str, str]], title: str) -> Path:
    parts, style = [], ""
    toc = ["<div class='bookcover'>",
           f"<h1>{title}</h1>",
           "<p class='bk-author'>Daniel Jurafsky &amp; James H. Martin</p>",
           "<p class='bk-note'>开源中文翻译 · 内容等价的重新排版（页数与英文原版不同）</p>",
           "</div>",
           "<div class='booktoc'><h2>目录</h2><ol>"]
    for slug, zh_title in chs:
        src = BOOK / "build" / slug / f"{mode}.html"
        if not src.is_file():
            print(f"  [skip] 缺少 {src}")
            continue
        s, b = extract(src.read_text(encoding="utf-8"))
        if not style:
            style = s
        # 图片引用：build/<slug>/images/x → build/_book/../<slug>/images/x
        b = b.replace('src="images/', f'src="../{slug}/images/')
        parts.append(f"<div class='bookchap'>{b}</div>")
        toc.append(f"<li><a href='#{slug}'>{zh_title}</a></li>")
    toc.append("</ol></div>")
    if not parts:
        sys.exit("[ERROR] 没有可合并的章节（先跑 build_html.py 产出 mono/dual.html）")
    mj_src = BOOK.parent / "vendor" / "mathjax" / "tex-svg.js"
    mj = ""
    if mj_src.is_file():
        mj = ("<script>MathJax={tex:{inlineMath:[['$','$']],displayMath:[['$$','$$']]},"
              "svg:{fontCache:'global'}};</script>\n"
              f'<script id="MathJax-script" src="{mj_src.as_uri()}"></script>\n')
    head = f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">
<title>{title}</title>
{mj}<style>{style}
.bookcover {{ page-break-after: always; text-align: center; padding-top: 30%; }}
.bookcover h1 {{ font-size: 25pt; border: 0; }}
.bk-author {{ font-size: 12pt; color: #555; }}
.bk-note {{ font-size: 10pt; color: #888; margin-top: 2em; }}
.booktoc {{ page-break-after: always; }}
.booktoc ol {{ line-height: 2; font-size: 11.5pt; }}
.bookchap {{ page-break-before: always; }}
</style></head><body>"""
    out_dir = BOOK / "build" / "_book"
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / f"{mode}.html"
    dest.write_text(head + "\n".join(toc) + "\n".join(parts) + "</body></html>", encoding="utf-8")
    print(f"  [OK] {dest}（{len(parts)} 章）")
    return dest


def main() -> int:
    ap = argparse.ArgumentParser(description="全书合成一份 PDF")
    ap.add_argument("--mode", choices=["mono", "dual", "both"], default="both")
    args = ap.parse_args()
    chs = chapters()
    print(f"章节数：{len(chs)}")
    jobs = []
    if args.mode in ("mono", "both"):
        jobs.append(("mono", BOOK / "zh/pdf/slp3-zh.pdf",
                     "Speech and Language Processing（第三版）· 中文翻译"))
    if args.mode in ("dual", "both"):
        jobs.append(("dual", BOOK / "zh/dual/slp3-dual.pdf",
                     "Speech and Language Processing（第三版）· 中英对照"))
    for mode, pdf, title in jobs:
        html = build(mode, chs, title)
        pdf.parent.mkdir(parents=True, exist_ok=True)
        env = dict(os.environ)
        subprocess.run([str(PY), str(SKILL / "scripts" / "render_pdf.py"), str(html), "-o", str(pdf)],
                       check=True, env=env)
        print(f"  [OK] {pdf}（{pdf.stat().st_size // 1024} KB）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
