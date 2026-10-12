#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_tampered.py — 修复被 subagent 篡改的原文。

以 doc.json 为准恢复分片中的 text / items / rows，并同步调整译文数组长度，
保证译文结构与原文严格一致（多出的行合并、缺失的行补空）。

用法:
    python3 scripts/fix_tampered.py <slug> [slug...]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent


def _merge_extra_rows(zh: list, keep_n: int) -> list:
    """译文行数多于原文时，把多出的行合并到末行。"""
    keep = zh[: keep_n - 1]
    tail = zh[keep_n - 1 :]
    width = max((len(r) for r in tail), default=0)
    merged = []
    for ci in range(width):
        parts = [(r[ci] if ci < len(r) else "").strip() for r in tail]
        merged.append("".join(p for p in parts if p))
    keep.append(merged)
    return keep


def fix(slug: str) -> list[str]:
    work = BOOK / "build" / slug
    doc = json.loads((work / "doc.json").read_text(encoding="utf-8"))
    src = {b["id"]: b for p in doc["pages"] for b in p.get("blocks", []) if b.get("id")}

    touched: list[str] = []
    for f in sorted((work / "chunks").glob("chunk_*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        changed = False
        for it in d["items"]:
            s = src.get(it.get("id"))
            if not s:
                continue
            kind = s.get("block_type") or s.get("type")

            if kind == "table":
                if it.get("rows") != s.get("rows"):
                    it["rows"] = s.get("rows") or []
                    changed = True
                zh = list(it.get("zh_rows") or [])
                n = len(it["rows"])
                if n and len(zh) > n:
                    zh = _merge_extra_rows(zh, n)
                elif n and len(zh) < n:
                    width = len(it["rows"][0]) if it["rows"] else 1
                    zh += [[""] * width for _ in range(n - len(zh))]
                if zh != it.get("zh_rows"):
                    it["zh_rows"] = zh
                    changed = True

            elif kind == "list":
                if it.get("items") != (s.get("items") or []):
                    it["items"] = s.get("items") or []
                    changed = True
                zi = list(it.get("zh_items") or [])
                n = len(it["items"])
                if len(zi) > n:
                    zi = zi[:n]
                elif len(zi) < n:
                    zi += [""] * (n - len(zi))
                if zi != it.get("zh_items"):
                    it["zh_items"] = zi
                    changed = True

            else:
                if it.get("text") != (s.get("text") or ""):
                    it["text"] = s.get("text") or ""
                    changed = True

        if changed:
            f.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
            touched.append(f.name)
    return touched


def main() -> int:
    if len(sys.argv) < 2:
        print("用法: fix_tampered.py <slug> [slug...]")
        return 2
    for slug in sys.argv[1:]:
        t = fix(slug)
        print(f"  {slug}: 修复 {len(t)} 个分片 {t if t else ''}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
