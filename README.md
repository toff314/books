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
| Speech and Language Processing（第三版） | [`slp3/`](slp3/) | 646 页 / 26 章 | 1 章 |

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

## 版权

各书原文版权归原作者与出版社所有。本仓库仅提供翻译与排版，供学习交流使用；如涉版权问题请联系删除。
