# CLAUDE.md — 霖楓學苑 (Lam Fung Academy)

## 專案定位

香港小學數學補習教材生產系統
- Python + Node.js 混合工具鏈 (SVG/MathJax/OCR)
- 70+ 份 P5/P6 HTML 講義, 自行開發幾何 SVG 庫
- 教育內容+營運文件+市場研究三合一

## 🔴 強制基礎設施規則

- **本專案目前無 Git 版本控制 — 這是首要風險**
- 立即初始化 Git repo: `git init && git add . && git commit -m "初始提交"`
- 創建 `.gitignore` 排除 `node_modules/`, `__pycache__/`, `.ipynb_checkpoints/`
- 創建 `requirements.txt` 記錄 Python 依賴 (matplotlib 等)
- 商業機密文件 (最高機密標記) 需確認是否應納入版本控制

## 技能綁定 (自動調用)

| 場景 | 技能 |
|------|------|
| 🔴 **每次對話開始** | `using-superpowers` |
| Python 工具開發 | `python-patterns`, `python-testing` |
| 前端/HTML 模板 | `frontend-design`, `design-system` |
| 內容生產自動化 | `content-engine` |
| 文件生成 (PDF/DOCX) | `pdf`, `docx` |
| 品牌設計 | `brand-guidelines`, `theme-factory` |
| 除錯/報錯 | `systematic-debugging` |
| 規劃新功能 | `writing-plans`, `brainstorming` |
| 程式碼重整 | `coding-standards`, `simplify` |
| 安全檢查 | `security-review` |
| 行銷文案 | `copywriter`, `writing-skills` |
| 市場研究 | `market-research` |
| 教育/課程設計 | `course-designer` (若有) |
| Git 初始化 | `git-workflow` |
| Token 壓縮 | `caveman`, `caveman-commit` |

## 專案架構

```
lam-fung-academy/
├── _tools/                  # Python 生產工具
│   ├── svg_geometry.py      # SVG 幾何庫 v2.3
│   ├── render_math.py       # LaTeX→PNG 渲染
│   ├── build_demo.py        # 講義建構器
│   └── replace_*.py         # 批次替換工具
├── _templates/              # HTML 模板
├── 講義/                    # 所有講義
│   ├── P5/                  # P5 (40課 + SSPA模擬)
│   └── P6/                  # P6 (20+課)
├── _ocr_pages/              # 掃描課本頁面
├── _ocr_text/               # OCR 輸出
├── ocr_batch.cjs            # 批次 OCR 腳本
└── *.md                     # 營運文件 (市場研究, 課綱, 銷售手冊)
```

## 關鍵限制

- 無版本控制 — 修改前先 git init
- 無 requirements.txt — Python 依賴安裝在全局環境
- 硬編碼路徑 `G:\lam-fung-academy\_tools` 在多個腳本中
- HTML 講義為自包含格式 (SVG 內嵌, base64 圖片), 無外部依賴
- MathJax v4.1.2 CDN 載入 (需網路), PDF 輸出為離線版本
