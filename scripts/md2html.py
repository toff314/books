#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
md2html.py — 把本书生成的 Markdown 转成可直接在线阅读的 HTML（零第三方依赖）。

只支持本项目 build_markdown.py 产出的 Markdown 子集：
标题 / 段落 / 无序列表 / 表格 / 图片 / 引用块(页边注) / 粗体 / 斜体 / 行内代码。

用法:
    python3 scripts/md2html.py slp3/zh/md/01-introduction.md -o slp3/zh/html --title "第 1 章 绪论"
"""
from __future__ import annotations

import argparse
import html as H
import re
import sys
from pathlib import Path

CSS = """
:root { --ink:#1b1b1b; --muted:#6b7280; --line:#e5e7eb; --accent:#0b5fa5; --bg:#ffffff; }
* { box-sizing: border-box; }
body { margin:0; background:#f6f7f9; color:var(--ink);
  font-family:-apple-system,"PingFang SC","Microsoft YaHei","WenQuanYi Micro Hei",sans-serif;
  line-height:1.85; font-size:16px; }
.wrap { max-width:860px; margin:0 auto; background:var(--bg); min-height:100vh;
  padding:48px 56px 120px; box-shadow:0 0 24px rgba(0,0,0,.06); }
h1,h2,h3,h4 { line-height:1.35; margin:1.4em 0 .6em; }
h1 { font-size:28px; border-bottom:2px solid var(--line); padding-bottom:.3em; }
h2 { font-size:22px; } h3 { font-size:18px; } h4 { font-size:16px; }
p { margin:0 0 .9em; text-align:justify; }
ul { margin:.4em 0 1em 1.4em; } li { margin:.25em 0; }
img { max-width:100%; height:auto; display:block; margin:1.2em auto; }
blockquote { margin:.8em 0; padding:.5em 1em; background:#f7f8fa;
  border-left:3px solid #c9d2dd; color:#4a4a4a; font-size:14px; }
blockquote p { margin:.2em 0; }
.term { margin:.8em 0; padding:.5em 1em; background:#f7f8fa;
  border-left:3px solid #b9c4d0; color:#4a4a4a; font-size:14px; }
.term code { background:none; color:var(--accent); margin-right:.5em; }
.term-zh { color:#333; margin-right:.5em; }
.term-explain { color:#4a4a4a; }
table { border-collapse:collapse; width:100%; margin:1em 0; font-size:14px; }
th,td { border:1px solid var(--line); padding:7px 10px; text-align:left; vertical-align:top; }
th { background:#f3f5f7; font-weight:600; }
code { background:#f0f2f5; padding:.1em .35em; border-radius:3px; font-size:.9em; }
.caption { font-size:14px; color:#4a4a4a; margin:.2em 0 1.3em; text-align:center; }
.figbox { border:2.5px solid #1d3f9e; border-radius:3px; padding:.6em .95em;
  margin:1.2em 0; background:#fff; }
.figbox p { margin:.4em 0; }
.figbox blockquote { background:transparent; border-left:0; padding:0; margin:.4em 0;
  color:#333; font-size:15px; }
hr { border:0; border-top:1px solid var(--line); margin:2em 0; }
.nav { margin-bottom:1.5em; font-size:14px; color:var(--muted); }
.nav a { color:var(--accent); text-decoration:none; margin-right:1em; }
footer { margin-top:3em; padding-top:1em; border-top:1px solid var(--line);
  font-size:13px; color:var(--muted); }
"""


def inline(text: str) -> str:
    # 表格单元格里的 <br> 是 build_markdown 生成的换行标记：先还原、再统一转成真实换行，
    # 否则会被 escape 成字面 "&lt;br&gt;" 显示给读者。
    text = (text or "").replace("<br>", "\n")
    text = H.escape(text)
    text = text.replace("\n", "<br>")
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)
    return text


IMG_PREFIX = ""

# 页边术语块（build_markdown 产出）：首行 `原词`（译名），其后一行 “释义：…”。
TERM_HEAD = re.compile(r"^`([^`]+)`(?:（(.*)）)?$")


def term_block(block: list[str]) -> str | None:
    """把页边术语引用块渲染为 <aside class="term">（含 term-explain），非术语块返回 None。"""
    if not block:
        return None
    m = TERM_HEAD.match(block[0].strip())
    if not m:
        return None
    explain = ""
    for x in block[1:]:
        if x.startswith("释义："):
            explain = x[len("释义："):].strip()
            break
    if not explain:
        return None
    parts = [f"<code>{H.escape(m.group(1))}</code>"]
    if m.group(2):
        parts.append(f'<span class="term-zh">{H.escape(m.group(2))}</span>')
    parts.append(f'<span class="term-explain">{inline(explain)}</span>')
    return f'<aside class="term">{"".join(parts)}</aside>'


def image(line: str) -> str:
    m = re.match(r"^!\[[^\]]*\]\(([^)]+)\)$", line.strip())
    if not m:
        return ""
    src = m.group(1)
    if IMG_PREFIX and not src.startswith(("http://", "https://", "/")):
        src = IMG_PREFIX + src
    return f'<img src="{H.escape(src, quote=True)}" alt="">'


def table(block: list[str]) -> str:
    rows = []
    for i, line in enumerate(block):
        if i == 1 and set(line.replace("|", "").strip()) <= {"-", " "}:
            continue  # 分隔行
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        rows.append(cells)
    if not rows:
        return ""
    out = ["<table>"]
    for ri, cells in enumerate(rows):
        tag = "th" if ri == 0 else "td"
        out.append("<tr>" + "".join(f"<{tag}>{inline(c)}</{tag}>" for c in cells) + "</tr>")
    out.append("</table>")
    return "".join(out)


def join_lines(lines: list[str]) -> str:
    """合并同一段落的软换行：拉丁文之间补空格，中文之间不补。"""
    out = ""
    for s in lines:
        if not out:
            out = s
            continue
        if out[-1:].isascii() and s[:1].isascii():
            out += " " + s
        else:
            out += s
    return out


def convert(md: str) -> str:
    lines = md.split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        # 彩色边框文本框（build_markdown 产出的显式标记）：成组包一层带边框的容器
        if stripped == "<!--figbox-->":
            out.append('<div class="figbox">')
            i += 1
            continue
        if stripped == "<!--/figbox-->":
            out.append("</div>")
            i += 1
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m:
            lv = len(m.group(1))
            out.append(f"<h{lv}>{inline(m.group(2))}</h{lv}>")
            i += 1
            continue

        if stripped == "---":
            out.append("<hr>")
            i += 1
            continue

        if image(stripped):
            out.append(image(stripped))
            i += 1
            continue

        if stripped.startswith("|"):
            block = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                block.append(lines[i])
                i += 1
            out.append(table(block))
            continue

        if stripped.startswith(">"):
            block = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                block.append(lines[i].strip()[1:].strip())
                i += 1
            term_html = term_block(block)
            if term_html is not None:
                out.append(term_html)
                continue
            inner = "".join(f"<p>{inline(x)}</p>" for x in block if x)
            out.append(f"<blockquote>{inner}</blockquote>")
            continue

        if re.match(r"^[-*]\s+", stripped):
            items = []
            while i < len(lines) and re.match(r"^[-*]\s+", lines[i].strip()):
                items.append(re.sub(r"^[-*]\s+", "", lines[i].strip()))
                i += 1
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>")
            continue

        # 图注：build_markdown 产出的独立斜体行 `*图 X.Y …*`（* 后无空格，非列表项）
        mc = re.match(r"^\*([^*].*?)\*$", stripped)
        if mc:
            out.append(f'<p class="caption">{inline(mc.group(1))}</p>')
            i += 1
            continue

        # 普通段落（连续非空行合并）
        para = []
        while i < len(lines):
            s = lines[i].strip()
            # `*` 仅在作为列表标记（`* ` 后跟空格）时才是块起点；否则是斜体行/图注
            if not s or s.startswith(("#", ">", "|", "!", "<")) or re.match(r"^[-*]\s+", s):
                break
            para.append(s)
            i += 1
        if para:
            out.append("<p>" + inline(join_lines(para)) + "</p>")
        else:
            i += 1
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description="Markdown → 在线阅读 HTML")
    ap.add_argument("md", nargs="?", help="输入 Markdown（省略时读 stdin）")
    ap.add_argument("-o", "--out", required=True, help="输出目录")
    ap.add_argument("--title", default="", help="页面标题")
    ap.add_argument("--name", default="", help="输出文件名（不含扩展名）")
    ap.add_argument("--nav", default="", help="顶部导航 HTML 片段")
    ap.add_argument("--img-prefix", default="", help="图片路径前缀（如 ../md/images/）")
    args = ap.parse_args()

    global IMG_PREFIX
    IMG_PREFIX = args.img_prefix

    if args.md:
        src = Path(args.md)
        text = src.read_text(encoding="utf-8")
        name = args.name or src.stem
    else:
        text = sys.stdin.read()
        name = args.name or "index"

    title = args.title or name
    doc = f"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{H.escape(title)}</title>
<style>{CSS}</style>
</head><body><div class="wrap">
{args.nav}
{convert(text)}
</div></body></html>
"""
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    p = out_dir / f"{name}.html"
    p.write_text(doc, encoding="utf-8")
    print(f"[OK] {p}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
