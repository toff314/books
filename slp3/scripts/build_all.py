#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_all.py — 扫描所有章节，对「翻译已完整」的章节批量构建 md/HTML/PDF，并更新站点导航。

用法:
    python3 scripts/build_all.py                 # 构建所有已翻译完整的章节
    python3 scripts/build_all.py --only 02 03    # 只构建指定章
    python3 scripts/build_all.py --stage         # 只看状态，不构建
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

from prepare_chapters import CHAPTERS

BOOK = Path(__file__).resolve().parent.parent
SKILL = Path(os.environ.get("PDF_TRANSLATE_SKILL", "/home/yuanwu/zhihu-wiki/skills/pdf-translate"))
PY = SKILL / ".venv" / "bin" / "python"


def chunk_status(slug: str) -> tuple[int, int]:
    """返回 (已填满的分片数, 总分片数)。"""
    r = subprocess.run([str(PY), str(SKILL / "scripts" / "check_chunks.py"),
                        str(BOOK / "build" / slug / "chunks")],
                       capture_output=True, text=True)
    out = r.stdout.strip()
    if out.startswith("[OK]"):
        import re
        m = re.search(r"(\d+) 个分片", out)
        n = int(m.group(1)) if m else 0
        return n, n
    import re
    m = re.search(r"(\d+)/(\d+) 个分片", out)
    if m:
        bad, tot = int(m.group(1)), int(m.group(2))
        return tot - bad, tot
    return 0, 0


def main() -> int:
    ap = argparse.ArgumentParser(description="批量构建已翻译完整的章节")
    ap.add_argument("--only", nargs="*", default=None)
    ap.add_argument("--stage", action="store_true", help="只报告状态")
    ap.add_argument("--dual", action="store_true", default=True)
    args = ap.parse_args()

    targets = [c for c in CHAPTERS if not args.only or c[0] in args.only]
    ready = []
    print(f"{'章':<4}{'标题':<32}{'分片进度':<14}{'状态'}")
    for num, name, title, _f, _l in targets:
        slug = f"{num}-{name}"
        if not (BOOK / "build" / slug / "chunks").is_dir():
            print(f"{num:<4}{title:<32}{'-':<14}未准备")
            continue
        ok, total = chunk_status(slug)
        state = "✅就绪" if total and ok == total else f"⏳ {ok}/{total}"
        print(f"{num:<4}{title:<32}{f'{ok}/{total}':<14}{state}")
        if total and ok == total:
            ready.append((num, name, title))

    if args.stage:
        return 0

    print(f"\n开始构建 {len(ready)} 章…")
    for num, name, title in ready:
        slug = f"{num}-{name}"
        work = BOOK / "build" / slug
        r = subprocess.run([str(PY), str(SKILL / "scripts" / "merge_chunks.py"),
                            str(work / "doc.json"), "-o", str(work)],
                           capture_output=True, text=True)
        if r.returncode != 0:
            print(f"  [{num}] merge 未通过：{r.stdout.strip().splitlines()[-1] if r.stdout else ''}")
            continue
        r2 = subprocess.run([sys.executable, str(BOOK / "scripts" / "build_book.py"),
                             "--slug", slug, "--title", title, "--dual"],
                            capture_output=True, text=True)
        ok = "构建完成" in r2.stdout
        print(f"  [{num}] {title} — {'✅ 构建完成' if ok else '❌ 失败'}")

    subprocess.run([sys.executable, str(BOOK / "scripts" / "update_site.py")])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
