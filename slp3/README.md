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
│   ├── pdf/           中文整本 PDF（slp3-zh.pdf）
│   └── dual/          中英对照整本 PDF（slp3-dual.pdf）
├── scripts/           本书的构建脚本
└── build/             中间产物（不入库）
```

## 交付形态

| 形态 | 说明 |
|---|---|
| 中文 Markdown | `zh/md/NN-*.md`，按章组织，便于校对与二次加工 |
| 中文 HTML | `zh/html/NN-*.html`，浏览器直接阅读 |
| 中文整本 PDF | `zh/pdf/slp3-zh.pdf`，**全书合成一份**，保留图片与表格的重新排版 |
| 中英对照整本 PDF | `zh/dual/slp3-dual.pdf`，**全书合成一份**，段段对照便于核校 |
| 英文原版 | `source/ed3book_aug26.pdf` |

## 章节进度

见 [`SUMMARY.md`](SUMMARY.md)。

## 为什么用这套流水线

与“在线传 PDF 翻译 / 直接丢给对话式 LLM / 覆盖式重排工具”相比，本项目的差异在四点：

- **结构先于文字**：先拆成 `doc.json`（标题/段落/表格/图注/页边术语/插图逐块），插图按页区域栅格化、
  文字型示例框不烤进图片而是成组加框 —— 图、表、标题层级都能保留，框内英文也照样翻译。
- **有译审，不是一遍过**：术语表先注入每个分片，分片并发翻译后跑机检 + **独立译审**
  （与翻译员上下文隔离，专查漏译 / 语义反向 / 数字单位 / 术语漂移 / 幻觉增删），REVISE 定点回修、最多 3 轮收敛。
- **图表有专检**：`check_figures.py` 核对插图落盘、图注↔图表配对、产物 `<img>`/`.figbox` 计数，
  把“图注在、图丢了”“表格被降级成文字”这类静默丢失挡在交付前。
- **可复现可增量**：中间产物全部留档，可定位到 block id 定点返修；按章流水线可并行推进；
  同一份译文出 Markdown / 在线阅读 / 中文 PDF / **中英对照 PDF** 四种形态。

代价是**不做像素级还原**（产出是内容等价的重新排版，页数与原书不同），扫描件 / 纯图片 PDF 也不支持（需先 OCR）。
详见根 [`README.md`](../README.md)。

## 构建方式

翻译流水线来自 `pdf-translate` 技能（结构提取 → 多 agent 并发翻译 → 中英重排 → Chromium 渲染）。
本书的构建脚本位于 [`scripts/`](scripts/)。```bash
# 1. 结构提取（需要 pdf-translate 技能的 venv）
# 2. 分片并并发翻译
# 3. 逐章 → Markdown / HTML（在线阅读用）
python3 scripts/build_book.py --slug 01-introduction --title "第 1 章 引言" --dual
# 4. 全书 → 一份中文整本 PDF + 一份中英对照整本 PDF（只渲染一次）
python3 scripts/build_pdf_book.py
```
