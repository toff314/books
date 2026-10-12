#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
update_site.py — 按 zh/ 实际产出重新生成 SUMMARY.md 与书目页 index.html。

用法:
    python3 scripts/update_site.py
"""
from __future__ import annotations

import html
import re
from pathlib import Path

from prepare_chapters import CHAPTERS

BOOK = Path(__file__).resolve().parent.parent
REPO = BOOK.parent

PARTS = [
    ("第一部分 · 大语言模型（Large Language Models）", 1, 8),
    ("第二部分 · 高级 LLM 主题与工具（Advanced LLM Topics and Tools）", 9, 17),
    ("第三部分 · 标注语言结构（Annotating Linguistic Structure）", 18, 26),
]


def status_of(num: str, name: str) -> dict:
    slug = f"{num}-{name}"
    md = BOOK / "zh" / "md" / f"{slug}.md"
    html_f = BOOK / "zh" / "html" / f"{slug}.html"
    pdf = BOOK / "zh" / "pdf" / f"{slug}-zh.pdf"
    dual = BOOK / "zh" / "dual" / f"{slug}-dual.pdf"
    return {
        "md": md.is_file(), "html": html_f.is_file(),
        "pdf": pdf.is_file(), "dual": dual.is_file(),
        "done": html_f.is_file() and pdf.is_file(),
    }


def build_summary() -> str:
    done_cnt = sum(1 for n, nm, _t, _a, _b in CHAPTERS if status_of(n, nm)["done"])
    lines = [
        "# 目录 · SUMMARY",
        "",
        "**Speech and Language Processing（第三版）** — Daniel Jurafsky & James H. Martin，2026 年 8 月版，646 页 / 26 章。",
        "",
        f"图例：✅ 已完成 · 🚧 进行中 · ⬜ 待翻译　　**进度：{done_cnt} / {len(CHAPTERS)} 章**",
        "",
    ]
    for part_title, lo, hi in PARTS:
        lines.append(f"## {part_title}")
        lines.append("")
        lines.append("| # | 章节 | 原书页 | 中文 |")
        lines.append("|---|---|---|---|")
        for num, name, title, first, _last in CHAPTERS:
            n = int(num)
            if not (lo <= n <= hi):
                continue
            st = status_of(num, name)
            slug = f"{num}-{name}"
            if st["done"]:
                zh = (f"[在线阅读](zh/html/{slug}.html) · [对照](zh/html/{slug}.dual.html) · "
                      f"[PDF](zh/pdf/{slug}-zh.pdf) · [对照PDF](zh/dual/{slug}-dual.pdf) · "
                      f"[MD](zh/md/{slug}.md)")
                mark = "✅"
            elif st["html"] or st["md"]:
                zh, mark = "🚧 构建中", "🚧"
            else:
                zh, mark = "待翻译", "⬜"
            short = re.sub(r"^第\s*\d+\s*章\s*", "", title)
            lines.append(f"| {n} | {short} | {first} | {mark} {zh} |")
        lines.append("")
    lines += [
        "## 附录",
        "",
        "| 内容 | 原书页 |",
        "|---|---|",
        "| Bibliography（参考文献） | 607 |",
        "| Subject Index（主题索引） | 638 |",
        "",
    ]
    return "\n".join(lines)


def build_book_index() -> str:
    done_cnt = sum(1 for n, nm, _t, _a, _b in CHAPTERS if status_of(n, nm)["done"])
    rows = []
    for part_title, lo, hi in PARTS:
        rows.append(f"  <h2>{html.escape(part_title)}</h2>")
        rows.append('  <table>')
        rows.append('    <tr><th class="no">#</th><th>章节</th><th class="pg">原书页</th><th class="zh">中文</th></tr>')
        for num, name, title, first, _last in CHAPTERS:
            n = int(num)
            if not (lo <= n <= hi):
                continue
            st = status_of(num, name)
            slug = f"{num}-{name}"
            if st["done"]:
                cell = (f'<a href="zh/html/{slug}.html">在线阅读</a>'
                        f'<a href="zh/html/{slug}.dual.html">对照</a>'
                        f'<a href="zh/pdf/{slug}-zh.pdf">PDF</a>'
                        f'<a href="zh/dual/{slug}-dual.pdf">对照PDF</a>')
                cls = "done"
            else:
                cell, cls = "待翻译", "wait"
            short = re.sub(r"^第\s*\d+\s*章\s*", "", title)
            rows.append(f'    <tr><td class="no">{n}</td><td>{html.escape(short)}</td>'
                        f'<td class="pg">{first}</td><td class="zh {cls}">{cell}</td></tr>')
        rows.append('  </table>')
    body = "\n".join(rows)

    first_done = next((f"{n}-{nm}" for n, nm, _t, _a, _b in CHAPTERS if status_of(n, nm)["done"]), None)
    leads = []
    if first_done:
        leads = [
            f'<a href="zh/html/{first_done}.html">中文在线阅读</a> ·',
            f'<a href="zh/pdf/{first_done}-zh.pdf">中文 PDF</a> ·',
            f'<a href="zh/dual/{first_done}-dual.pdf">中英对照 PDF</a> ·',
        ]
    leads.append('<a href="source/ed3book_aug26.pdf">英文原版 PDF</a>')

    css = """  :root { --ink:#1b1b1b; --muted:#6b7280; --line:#e5e7eb; --accent:#0b5fa5; }
  * { box-sizing:border-box; }
  body { margin:0; background:#f6f7f9; color:var(--ink); line-height:1.8;
    font-family:-apple-system,"PingFang SC","Microsoft YaHei","WenQuanYi Micro Hei",sans-serif; }
  .wrap { max-width:980px; margin:0 auto; padding:56px 32px 100px; }
  .back { font-size:14px; margin-bottom:1.6em; }
  .back a { color:var(--accent); text-decoration:none; }
  h1 { font-size:30px; margin:0 0 .15em; }
  .en { color:var(--muted); font-size:15px; margin:0 0 1.2em; }
  .lead { background:#fff; border:1px solid var(--line); border-radius:12px;
    padding:20px 24px; margin:0 0 2em; font-size:15px; }
  .lead a { color:var(--accent); }
  h2 { font-size:20px; margin:2em 0 .6em; padding-bottom:.3em; border-bottom:1px solid var(--line); }
  table { border-collapse:collapse; width:100%; background:#fff; font-size:14px;
    border:1px solid var(--line); border-radius:10px; overflow:hidden; }
  th,td { padding:10px 12px; text-align:left; border-bottom:1px solid var(--line); }
  th { background:#f3f5f7; font-weight:600; font-size:13px; color:#374151; }
  tr:last-child td { border-bottom:none; }
  td.no { color:var(--muted); width:44px; }
  td.pg { color:var(--muted); width:64px; }
  td.zh { width:250px; white-space:nowrap; }
  td.zh a { color:var(--accent); text-decoration:none; margin-right:8px; font-size:13px; }
  td.zh a:hover { text-decoration:underline; }
  .done { color:#047857; font-weight:600; }
  .wait { color:#9ca3af; }
  footer { margin-top:3em; font-size:13px; color:var(--muted); }
  footer a { color:var(--accent); }"""

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Speech and Language Processing（第三版）· 中文翻译</title>
<style>
{css}
</style>
</head>
<body>
<div class="wrap">
  <div class="back"><a href="../index.html">← 返回书架</a></div>
  <h1>Speech and Language Processing（第三版）</h1>
  <p class="en">Daniel Jurafsky &amp; James H. Martin · 2026 年 8 月版 · 646 页 / 26 章 · 已完成 {done_cnt} 章</p>
  <div class="lead">
    <strong>交付形态：</strong>
    {" ".join(leads)}
  </div>
{body}
  <footer>
    原文版权归 Daniel Jurafsky 与 James H. Martin 所有 · 本页提供中文翻译与排版，供学习交流使用<br>
    <a href="SUMMARY.md">SUMMARY.md</a> · <a href="README.md">README</a>
  </footer>
</div>
</body>
</html>
"""


def main() -> int:
    (BOOK / "SUMMARY.md").write_text(build_summary(), encoding="utf-8")
    (BOOK / "index.html").write_text(build_book_index(), encoding="utf-8")

    done_cnt = sum(1 for n, nm, _t, _a, _b in CHAPTERS if status_of(n, nm)["done"])
    root = (REPO / "index.html")
    if root.is_file():
        text = root.read_text(encoding="utf-8")
        text = re.sub(r"翻译进度：\d+ / \d+ 章", f"翻译进度：{done_cnt} / {len(CHAPTERS)} 章", text)
        root.write_text(text, encoding="utf-8")

    print(f"[OK] SUMMARY.md / index.html 已更新（完成 {done_cnt}/{len(CHAPTERS)} 章）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
