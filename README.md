# Books · 外文技术书中文翻译

一个「多书书架」仓库：每本书一个子目录，统一提供**中文 Markdown 在线阅读、中文 PDF、中英对照 PDF**，并保留英文原版。

## 站点

| 入口 | 地址 |
|---|---|
| 书架首页 | `http://<host>:17000/` |
| 书目页 | `http://<host>:17000/<book>/` |

部署方式：`docker compose up -d`（Caddy 静态托管 + 目录浏览，见 [`docker-compose.yaml`](docker-compose.yaml) 与 [`Caddyfile`](Caddyfile)）。

## 已收录

| 书 | 目录 | 原书 | 进度 |
|---|---|---|---|
| Speech and Language Processing（第三版） | [`slp3/`](slp3/) | 646 页 / 26 章 | 26 / 26 章 |

## 目录约定

```
books/
├── index.html              # 书架首页
├── docker-compose.yaml     # Caddy 部署
├── Caddyfile
├── scripts/
│   └── md2html.py          # Markdown → 在线可读 HTML（零依赖）
└── <book-slug>/            # 每本书
    ├── README.md           # 书目说明
    ├── SUMMARY.md          # 章节目录与进度
    ├── index.html          # 书目页
    ├── source/             # 英文原版 PDF
    ├── zh/
    │   ├── md/             # 中文 Markdown（按章）
    │   ├── html/           # 中文 HTML（在线阅读）
    │   ├── pdf/            # 中文 PDF
    │   └── dual/           # 中英对照 PDF
    ├── scripts/            # 本书构建脚本
    └── build/              # 中间产物（不入库）
```

## 新增一本书

1. 建 `<book-slug>/`，放原书 PDF 到 `source/`；
2. 复制 `slp3/scripts/build_book.py`，用 `--slug` 指定章节；
3. 走翻译流水线（`pdf-translate` 技能）产出 `build/<slug>/translated.json`；
4. `python3 scripts/build_book.py --slug <slug> --title "第 N 章 …" --dual`；
5. 更新本书 `SUMMARY.md`、`index.html` 与根 `index.html` 的书架列表。

## 翻译流水线

翻译由 [`pdf-translate`](../../zhihu-wiki/skills/pdf-translate) 技能完成：

```
PDF 结构提取 → 多 subagent 并发翻译 → 合并机检 → 中英重排 → Chromium 渲染 PDF
```

排版为**内容等价的重新排版**（页数与原书不同）；图片、表格、标题层级保留。

### 与其他翻译方案的区别

| 方案 | 结果 |
|---|---|
| 通用机翻（Google / DeepL 等在线传 PDF） | 只得到连续文本：**图片、表格、标题层级全丢**；无术语一致性约束 |
| 直接丢给对话式 LLM | 长书必须分段，**跨段术语漂移**；图/表无法保留；没有独立译审 |
| 覆盖式重排工具（PDFMathTranslate / BabelDOC 一类） | 保留原版式，但中文按原栏宽硬塞，**行内错位、断行难看**；质量完全依赖原布局 |
| **本项目（pdf-translate 流水线）** | 结构化重排 + 独立译审 + 版式修订，见下 |

### 本项目的做法与优势

1. **结构先于文字**：先把 PDF 拆成 `doc.json`（页 → 块：标题/段落/表格/图注/页边术语/插图）。插图按**页面区域栅格化**（矢量 + 位图一并保留，不会漏掉矢量图）；
   文字型 figure（彩色示例框）**不烤进图片**，而是打组后在渲染时加框 —— 所以框内的英文也能被翻译。
2. **翻译有术语与一致性约束**：先定稿术语表注入每个分片 → 多 subagent 并发翻译 →
   机检（遗漏 / 空译 / 结构错位）+ **独立译审**（与翻译员上下文隔离，专查漏译、语义反向、数字与单位、
   术语漂移、幻觉增删）→ REVISE 定点回修，最多 3 轮收敛。
3. **图表有专检**：`check_figures.py` 逐项核对插图落盘 / 空块、图注↔图表配对、
   产物 `<img>` 与 `.figbox` 计数、bbox 畸形 —— 把“图注在、图丢了”“表格被降级成文字”
   这类**静默丢失**挡在交付前。
4. **可读性优先**：内容等价重排（不追求与原书逐页一致），中文按 A4 重新排版、补图注、加术语旁注；
   同时提供**中英对照 PDF**逐段核校。
5. **可复现、可增量、可审计**：`doc.json` 单一数据源；中间产物（`chunks/`、`translated.json`、
   `translation_report.json`、`verify_report.json`、`figures_report.json`）全部留档，可定位到 block id 定点返修；
   按章流水线可并行推进。
6. **一份译文、四种产物**：Markdown（可二次加工）/ 在线阅读 HTML / 中文 PDF / 中英对照 PDF。

### 已知限制（如实告知）

- 不做**像素级还原**：产出是内容等价的重新排版，页数、行位置与原书不同；需要“与原版一模一样”请改用覆盖式工具。
- **扫描件 / 纯图片 PDF 不支持**，需先 OCR。
- 数学公式按文本原样保留，不做 LaTeX 重排。
- 图表与排版个别处仍可能有瑕疵（如折行术语被拆开、个别表被降级为文字）—— 本仓库持续用上述机检 + 译审回归发现并修复。

## 版权

各书原文版权归原作者与出版社所有。本仓库仅提供翻译与排版，供学习交流使用；如涉版权问题请联系删除。
