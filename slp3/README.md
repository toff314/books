# Speech and Language Processing（第三版）· 中文翻译

Daniel Jurafsky & James H. Martin 著《Speech and Language Processing》第三版（2026 年 8 月版）的开源中文翻译。

- **原名**：Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition (Third Edition)
- **原书**：[ed3book_aug26.pdf](source/ed3book_aug26.pdf)（646 页 / 27 章）
- **原文版权**归原作者所有，本项目仅提供翻译与排版，供学习交流使用。

## 在线阅读

从 [`index.html`](index.html) 进入书目页，可在线阅读中文 Markdown。

## 目录结构

```
slp3/
├── source/            英文原版 PDF
├── zh/
│   ├── md/            中文 Markdown（按章）
│   ├── html/          中文 HTML（在线直读）
│   ├── pdf/           中文 PDF（按章 + 合订）
│   └── dual/          中英对照 PDF
├── scripts/           本书的构建脚本
└── build/             中间产物（不入库）
```

## 交付形态

| 形态 | 说明 |
|---|---|
| 中文 Markdown | `zh/md/NN-*.md`，按章组织，便于校对与二次加工 |
| 中文 HTML | `zh/html/NN-*.html`，浏览器直接阅读 |
| 中文 PDF | `zh/pdf/NN-*-zh.pdf`，保留图片与表格的重新排版 |
| 中英对照 PDF | `zh/dual/NN-*-dual.pdf`，段段对照，便于核校 |
| 英文原版 | `source/ed3book_aug26.pdf` |

## 章节进度

见 [`SUMMARY.md`](SUMMARY.md)。

## 构建方式

翻译流水线来自 `pdf-translate` 技能（结构提取 → 多 agent 并发翻译 → 中英重排 → Chromium 渲染）。
本书的构建脚本位于 [`scripts/`](scripts/)。

```bash
# 1. 结构提取（需要 pdf-translate 技能的 venv）
# 2. 分片并并发翻译
# 3. 合并 → 生成 Markdown / HTML / PDF
python3 scripts/build_book.py --chapter 01
```
