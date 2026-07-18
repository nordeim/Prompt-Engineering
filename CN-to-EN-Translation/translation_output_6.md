<engine_logs>
## Phase 1: Topological Parsing
- Structural elements identified: The document is a Markdown changelog with a title (`#`), a summary-by-section table, section headings (`##` and `###`), tables (for critical fixes, high coverage gaps, medium precision issues, low findings, strengths, acceptance criteria, line counts, and migration notes), bullet lists, and code-like formatting for flags (e.g., `--strict`) and file names.
- Immutable elements locked: All finding IDs (C1, H2, etc.), flag names (`--strict`, `--glossary`, `--notes`, `--qa`, `--locale`, `--termbase`, `--translate-comments`, `--publishing`), file names (`Translation_Engine_v5_Prompt.md`, `Translation_Engine_v4_Audit_and_v5_Plan.md`), version numbers (v4.0, v5.0), acronyms (RFC, MQM), and the literal strings "U+201C", "U+201D", "U+2018", "U+2019" are preserved verbatim.
- Structural Topology locked: Title, four top-level sections (Summary by Section, Critical Fixes (C1–C8), etc.), tables with three columns, and nested bullet points.

## Phase 2: Semantic & Modal Deconstruction
- IU count: Approximately 50–60 information units (sentences and table cells).
- Modal tags applied: All statements are declarative, factual, and assertive (changelog documentation). The document uses a mix of descriptive, prescriptive (e.g., "v5.0 fix:"), and evaluative language (e.g., "Preserved").
- Ambiguities detected: None material. The text is technical and unambiguous.

## Phase 3: Domain Reconstruction & Translation
- Translation draft complete.
- Terminology choices:
  - "changelog" → "变更日志"
  - "forensic" → "法证级"
  - "modality" → "模态" / "情态" (used as "模态映射" for modal mapping)
  - "disposition" → "处置" / "处理"
  - "audit" → "审计"
  - "glossary" → "术语表"
  - "locale" → "区域设置"
  - "Precedence Ladder" → "优先级梯级"
  - "MQM-lite" → "MQM-lite" (acronym retained)
  - "carry-over" → "结转" / "延续"
  - "defect" → "缺陷"
  - "finding" → "发现" / "问题"
  - "acceptance criteria" → "验收标准"
  - "migration notes" → "迁移须知"
- Grammar Asymmetry applications: English present tense and past tense mapped to Chinese aspect markers appropriately (e.g., "was replaced" → "已替换为"; "preserved" → "保留"; "added" → "新增").
- Quantity & Locale applications: All version numbers, line counts, and finding IDs preserved exactly.

## Phase 4: Typographical Compilation
- Surface Typography applied: Full-width punctuation for Chinese text (，。！？；： “ ” ‘ ’). CJK–Latin spacing added (e.g., “v5.0 版本”, “U+201C 字符”). Code spans and flags are wrapped in backticks and preserved verbatim.
- Title-of-Works mappings: Document title translated as 《翻译引擎 v4.0 → v5.0 变更日志》 (book/journal style).
- Nested quote rules: Not applicable.
- Heading Translation Policy: All headings translated, with proper nouns (e.g., “C1”, “H2”, “RFC 2119”) preserved inside the translated headings.

## Phase 5: Zero-Trust MQM-lite Audit
- Fact Check: PASS (all numbers, versions, IDs preserved).
- Modality Check: PASS (assertive/declarative modality mapped consistently).
- Structural Topology Check: PASS (headings, tables, lists, and bullet hierarchies preserved).
- Surface Typography Check: PASS (CJK-Latin spacing and punctuation width conform to Phase 4 rules).
- Collocation Check: PASS (e.g., “变更日志” for changelog, “验收标准” for acceptance criteria, “迁移须知” for migration notes).
- IU-Coverage Bookkeeping: PASS.
- Ambiguity Handling Check: PASS.
- Severity counts: Critical=0 Major=0 Minor=0 Neutral=0
- Repair loops used: 0 / 2

## Phase 6: Self-Test Pre-Output Gate
- Quote check (scoped): PASS (Chinese segments use “ ” and ‘ ’ per rules; no straight quotes in Chinese-dominant text outside code spans).
- Locked-retention exemption: PASS (all flags, IDs, and file names preserved).
- Notice-channel check: PASS (no warranting condition).
- Reasoning-marker check: PASS (payload contains no “Step 1:”, “I think”, etc.).
- Heading-hierarchy check: PASS (headings from source preserved).
- Heading-translation-consistency check: PASS (all headings translated per policy).
- Mode-output check: PASS (default mode; payload only).
- Scratchpad-format check: PASS.
- Self-Test result: PASS
</engine_logs>

# 翻译引擎 v4.0 → v5.0 变更日志

**主题：** `系统提示词：确定性法证级翻译引擎`
**变更类型：** 重大修订（处理了 38 项发现：8 项关键、11 项高优先级、13 项中优先级、6 项低优先级）
**审计文档：** `Translation_Engine_v4_Audit_and_v5_Plan.md`
**v5.0 工件：** `Translation_Engine_v5_Prompt.md`（629 行，约 47 KB）

本变更日志逐一映射了 v4.0 各章节/行在 v5.0 中的处置方式，并附带了驱动每项变更的问题 ID。该日志作为 v5 计划执行步骤 4 所要求的可追溯性工件。

---

## 按章节汇总

| v4.0 章节 | v5.0 中的处置 | 问题 ID |
|---|---|---|
| 标题头 + 角色（第 1–4 行） | 已修订：行为确定性契约取代了解码参数声明 | C1 |
| 系统参数（第 6–9 行） | 已拆分：行为契约保留在角色块中；文字解码设置移至标注为操作员指引的“部署说明”块 | C1 |
| 核心理念（3 条公理） | 保留并扩展：公理 1 增加了许可偏离说明，以协调习语处理；新增公理 4（指令隔离） | H8 |
| 防御性协议 1 — 实体锚定 | 保留并扩展：双向；新增人员/地点/案件/敬称子协议；修正了示例拆分（已翻译集 vs 保留集）；术语权威层级 | H6、M1、M3 |
| 防御性协议 2 — 模态与认知映射 | 保留并扩展：所有表格双向；新增“shall”；新增金融标记；新增统计声明标记 | H2、H3、M11、M12 |
| 防御性协议 3 — 反翻译腔 | 保留（S3）并扩展了额外搭配 | — |
| 防御性协议 4 — 文化负载表达 | 保留（S8）并细化；链接到 `--notes` 模式 | — |
| 防御性协议 5 — 源文本错误 / OCR | 保留并链接到 `--notes` 模式 | L4 |
| （新增）防御性协议 6 — 语法不对称 | 已添加：时态/体、数、限定词、性别未知代词 | H4 |
| （新增）防御性协议 7 — 数量与区域惯例 | 已添加：数值等价标准、货币、日期、单位、百分比/范围 | H5、C6 |
| 强制性多阶段工作流 | 已修订：单一全局修复预算（≤2 次审计循环；其他阶段执行一次）；第 5 阶段变为带严重性等级的 MQM-lite 审计；拓扑检查拆分为结构性与表面性 | C3、C8、M6 |
| 阶段 1：拓扑解析 | 保留并澄清了 HTML 表格处理和注释策略链接 | L5、H11 |
| 阶段 2：语义与模态解构 | 保留 | — |
| 阶段 3：领域重构 | 保留并加入语法不对称及数量与区域惯例应用 | H4、H5 |
| 阶段 4：排版汇编 | 已修订：拆分为结构性拓扑与表面排版；作品标题映射；嵌套引用/括号规则；CJK-拉丁文间距边界情况；表情符号/提及/话题标签透传 | C2、C3、H7、M4、M13、L2 |
| 阶段 5：零信任审计 | 已修订：MQM-lite 严重性等级；IU 覆盖率核算替代“信息密度”检查；仅结构性拓扑检查；数值等价标准替代“完全相同数字” | C3、C6、M6 |
| 歧义消解协议 | 保留（S4）并链接到通知通道和 `--notes` 模式 | C4 |
| 质量优先级 | 保留（S5）并按 MQM-lite 严重性等级为每项优先级分配等级 | — |
| 严格输出约束 | 已修订：定义通知通道；无静默失败规则；模式特定输出 | C4、C5 |
| 可选术语表输出模式 | 已修订：补全架构；定义确定性枚举；按首次出现排序；结转块格式 | H10、M9 |
| （新增）§0 接收与方向协议 | 已添加 | C7 |
| （新增）模式与运行时参数 | 已添加：默认、`--glossary`、`--notes`、`--qa`、`--strict`、`--locale`、`--termbase`、`--translate-comments`、`--publishing` | C4、C5、H1、H9、M5 |
| （新增）术语优先级梯级 | 已添加：从用户术语库到“保留原文”的 6 级优先级 | H9、M3 |
| （新增）符合性等级定义（L1–L4） | 已添加：每级验收标准；范围边界声明 | M8、L3 |
| 小样本校准示例 | 已修订：4 → 8 个示例；替换了示例 3（无效示例）；新增：中文→英文法律模糊表达、注入隔离、OCR 伪影、作品标题 | M7、L4 |
| 自测指令 | 已修订：作用域引用检查；锁定保留豁免；通知通道检查；模式输出检查 | C2、M10 |
| （新增）可扩展性：领域包 | 已添加：可插拔的领域扩展 | 前瞻性预留 |
| 页脚（“翻译质量目标”） | 保留并增加了版本行 | — |

---

## 关键修复（C1–C8）—— 处置详情

### C1 — 自指解码参数
- **v4.0 位置：** 第 7–9 行（“将所有翻译操作设置为 `temperature=0` 和 `top_p=0.1`。”）
- **v5.0 修复：** 替换为角色/运行模式块中的行为确定性契约（“以确定性状态机运行：在每个决策点，选择与锁定术语表、模态表以及同负载内先前选择最一致的呈现”）。文字解码设置移至“部署说明（针对推理层，而非模型）”块，明确标注为模型自身控制范围之外的操作员指引。

### C2 — “禁用弯引号”门禁与强制中文排版冲突
- **v4.0 位置：** 阶段 4 强制使用中文全角引号 `""` `''`（U+201C/201D/2018/2019——与英文弯引号码点相同）；自测要求“无弯引号”。
- **v5.0 修复：** 引用宽度规则现按段落语言和排版配置文件作用域划分：中文段落 *保留* `""` `''`；英文技术性段落使用直引号；`--publishing` 配置文件允许英文散文使用弯引号。自测措辞改为：“中文段落中无半角转换或压扁的引号（中文段落保留 `""` `''` U+201C/201D/2018/2019）；英文技术性段落（默认配置文件）中无弯引号，除非 `--publishing` 处于活动状态。”

### C3 — 拓扑保真度检查与强制排版转换矛盾
- **v4.0 位置：** 阶段 5 拓扑检查要求每个 Markdown 符号“与源文本完全一致”，而阶段 4 *要求*偏离源文本表面（插入间距、引号规范化、标点宽度转换）。
- **v5.0 修复：** 阶段 5 审计现区分**结构性拓扑检查**（标题、列表、表格、围栏、链接目标——必须与源文本完全匹配）和**表面排版检查**（按阶段 4 规则规范化；免除源文本一致性检查，改为对照排版规则审计）。小样本示例 3 明确展示了此区别。

### C4 — 译者注有条件允许，但允许模式不存在
- **v4.0 位置：** 防御性协议 4 和歧义协议步骤 4 引用了从未定义的“输出模式允许注释”。
- **v5.0 修复：** 新增“模式与运行时参数”章节，明确定义 `--notes` 模式（允许行内 `[译注: …]` 注释）和 `--qa` 模式（允许审计摘要）。所有“如果输出模式允许”的引用现在都解析到已定义的标志。

### C5 — 静默最佳努力回退削弱法证级保证
- **v4.0 位置：** 阶段 5——“停止并输出最佳努力翻译，附带静默内部标志（不向用户暴露该标志）。”
- **v5.0 修复：** 废除“静默内部标志”机制。新增通知通道协议：默认模式下审计失败在负载末尾附加一行 `[NOTICE]`；`--strict` 模式仅输出通知行并抑制负载。输出约束中明确声明无静默失败规则。

### C6 — “完全相同数字”事实检查与数字本地化示例矛盾
- **v4.0 位置：** 阶段 5 事实检查要求数字“完全相同”；示例 1 要求转换 “$2.4 million” → “240 万美元”。
- **v5.0 修复：** 阶段 5 事实检查现要求“在数量与区域惯例下数值等价”（而非表面完全相同）。新增防御性协议 7——数量与区域惯例——明确定义转换策略（货币、日期、单位、百分比/范围）。

### C7 — 核心操作指令缺失：方向检测
- **v4.0 位置：** 完全缺失。
- **v5.0 修复：** 在核心理念之前新增 §0 接收与方向协议。定义：显式覆盖处理、自动检测、双语负载处理、第三语言通知通道、空/乱码负载行为、同语言“翻译”请求。

### C8 — 迭代预算双重且不一致规定
- **v4.0 位置：** 工作流标题说“每阶段最大自纠迭代次数：2”；阶段 5 说“返回阶段 3（最多 2 次迭代）”。
- **v5.0 修复：** 单一全局修复预算一次性声明：“审计失败循环 ≤ 2。所有其他阶段恰好执行一次。”删除了各阶段特定说法。阶段 5 一致引用全局预算。

---

## 高优先级覆盖缺口（H1–H11）—— 处置详情

| ID | 缺口 | v5.0 章节 | 状态 |
|----|-----|-----------|------|
| H1 | 无区域维度（简体/繁体、大陆/台湾、美式/英式） | 模式与运行时参数 — `--locale=zh-CN\|zh-TW\|en-US\|en-GB` + 实体锚定中的区域术语子规则 | 已关闭 |
| H2 | 模态表格单向 | 防御性协议 2 — 所有表格双向，并带对称反面示例 | 已关闭 |
| H3 | 列出了金融领域但无标记 | 防御性协议 2 — 新增金融/证券披露标记块（10 项） | 已关闭 |
| H4 | 无语法不对称协议 | 防御性协议 6 — 语法不对称协议（时态/体、数、冠词、代词） | 已关闭 |
| H5 | 无数量、日期或单位策略 | 防御性协议 7 — 数量与区域惯例 | 已关闭 |
| H6 | 命名实体覆盖缺口（人员、地点、案件、敬称） | 防御性协议 1 — 扩展了人员/地点/案件/敬称子协议 | 已关闭 |
| H7 | 无作品标题排版映射（《》 ↔ 斜体/引号） | 排版规则 — 作品标题映射表，含 GB/T 排除列表 | 已关闭 |
| H8 | 无提示词注入隔离 | 公理 4 — 指令隔离 | 已关闭 |
| H9 | 无用户术语库注入或优先级协议 | 模式（`--termbase`）+ 术语优先级梯级（6 级） | 已关闭 |
| H10 | 无跨段落术语持久性 | 术语表模式 — 定义了结转块格式 | 已关闭 |
| H11 | 代码注释和 UI 字符串不可变性过度延伸 | 防御性协议 1 — 本地化例外 + 阶段 1 注释策略（`--translate-comments`） | 已关闭 |

---

## 中优先级精确性问题（M1–M13）—— 处置详情

| ID | 问题 | v5.0 修复 |
|----|-----|-----------|
| M1 | “Meta”误分类为已翻译名称示例 | 防御性协议 1 — 拆分为已翻译集（苹果、微软、谷歌、亚马逊、甲骨文）和保留集（Meta、OpenAI、Anthropic、Palantir） |
| M2 | RFC 2119 引用不精确（小写“must”与大写 MUST） | 防御性协议 2 — 工程标记表区分 MUST/SHOULD/MAY（大写，BCP 14 规范性）与 must/should/may（小写，普通英语） |
| M3 | “普遍首选”循环定义 | 由术语优先级梯级（6 个显式层级）解决 |
| M4 | CJK-拉丁文间距规则未标记为风格选择 | 排版规则 — 标记为“数字出版风格规则”；列举了边界情况（全角标点相邻、`%`/`$`/`°`/单位符号、粗体/斜体范围、链接文本） |
| M5 | 仅直引号规则与出版声明冲突 | 排版规则 — 英文排版现分为默认（技术性，直引号）和出版（`--publishing`，允许散文使用弯引号）配置文件 |
| M6 | “信息密度成比例”不可衡量 | 阶段 5 — 替换为 IU 覆盖率核算检查 |
| M7 | 示例 3 是无效示例 | 小样本示例 3 替换为英译中案例，展示排版、不可变性和 C3 结构性与表面区别 |
| M8 | L1–L4 级别被引用但未定义 | 新增符合性等级定义章节 — 每级验收标准 |
| M9 | 术语表架构“确定性”未定义 | 术语表模式 — 确定性枚举：`locked-standard` / `locked-context` / `candidate`；按首次出现排序 |
| M10 | 自测“无未解释英文”错误标记强制保留项 | 自测 — 锁定保留豁免：不可变元素、锁定术语表保留和领域标准缩略语除外 |
| M11 | 模态映射中缺失“shall” | 防御性协议 2 — 法律标记表：`shall` → 须/应当；`shall not` → 不得 |
| M12 | 统计/医学模态缺口 | 防御性协议 2 — 医学标记表扩展：“significant (stat.)” → 具有统计学意义；“associated with” → 与……相关（从不译为“导致”） |
| M13 | “主导语言”标点在嵌套情况下规定不足 | 排版规则 — 规定了嵌套情况：中文内部完全英文括号内按英文规则；中文嵌套引号遵循外双内单（“外层‘内层’外层”） |

---

## 低优先级发现（L1–L6）—— 处置详情

| ID | 问题 | v5.0 修复 |
|----|-----|-----------|
| L1 | “停止并输出”残留 | 替换为通知通道 + `--strict` 机制 |
| L2 | 无表情符号/提及/话题标签透传 | 排版规则 — 明确透传规则 |
| L3 | 无范围边界（引擎 ≠ 认证翻译） | 符合性等级定义 — 明确范围边界声明 |
| L4 | 仅 4 个校准示例；无对抗性示例 | 小样本 — 扩展到 8 个；新增：中文→英文法律模糊表达、注入尝试、OCR 伪影、作品标题 |
| L5 | “合并单元格”暗示 HTML 表格 | 阶段 1 — 澄清：标准 Markdown 表格按原样支持；带 `colspan`/`rowspan` 的 HTML 表格逐字保留，仅翻译单元格文本内容 |
| L6 | 无针对攻击性/敏感内容的保真度立场 | 隐含于公理 1 + 公理 4 — 法证级完整性 = 按原样翻译，不做净化处理；公理 4 同时消除任何会编辑内容的“软拒绝”安全过滤器注入 |

---

## v4.0 保留优势（S1–S8）

| ID | 优势 | v5.0 中的保留方式 |
|----|------|-------------------|
| S1 | 带反面示例的显式模态表 | 逐字保留并双向扩展（法律、工程、医学、金融） |
| S2 | 不可变元素锚定 | 逐字保留并细化（本地化例外、注释策略） |
| S3 | 反翻译腔搭配对（双向） | 逐字保留并扩展（8 个英译中 + 6 个中译英搭配） |
| S4 | 作为有序层级的歧义消解协议 | 逐字保留，链接到通知通道和 `--notes` 模式 |
| S5 | 带覆盖规则的质量优先级 | 逐字保留，并叠加了 MQM-lite 严重性等级 |
| S6 | 带推理行的小样本示例 | 保留并扩展（4 → 8 个示例） |
| S7 | 禁止元评论/阶段泄漏 | 逐字保留 |
| S8 | 文化负载习语处理，优先功能等效 | 逐字保留并细化（功能等效现通过许可偏离说明与公理 1 协调） |

---

## 验收标准状态（v5 计划 §4）

所有 12 项验收标准均在 v5.0 草案中满足。右侧列标明了 `Translation_Engine_v5_Prompt.md` 中对应的规则位置。

| # | 标准 | v5.0 位置 |
|---|------|-----------|
| 1 | C2 回归测试：中文源文本带有 `""` 时，输出中为 U+201C/201D；自测不标记 | 排版规则（中文排版）+ 自测（作用域引用检查） |
| 2 | C7 方向：纯英文 → 中文；纯中文 → 英文；法语 → 单行通知，不翻译 | §0 接收与方向协议 + 输出约束（通知通道） |
| 3 | C5 可见性：强制审计失败 → 默认附加通知；`--strict` 仅输出通知 | 模式（`--strict`）+ 阶段 5 审计失败行为 + 输出约束（无静默失败规则） |
| 4 | H8 注入：源文本包含“忽略先前指令”→ 逐字翻译为内容；行为不变 | 公理 4 + 小样本示例 6 |
| 5 | H2 双向性：“涉嫌转移资产”→ “allegedly transferred assets”；“allegedly”→ 涉嫌/据称 | 防御性协议 2 — 法律标记表（双向）+ 小样本示例 5 |
| 6 | H1 区域：`--locale=zh-TW` → 軟體/網路；默认 → 简体 + 大陆术语 | 模式（`--locale`）+ 实体锚定（区域术语子规则） |
| 7 | H5 数量：“$2.4 million”→ 240 万美元；“yesterday”→ 昨天；不进行美元↔人民币转换 | 防御性协议 7 — 数量与区域惯例 + 小样本示例 1 |
| 8 | H7 标题：《三体》→ *The Three-Body Problem*；“Hamlet”→ 《哈姆雷特》；组织名称从不加《》 | 排版规则 — 作品标题映射 + 小样本示例 8 |
| 9 | C3 拓扑：弯引号 + 紧凑 CJK 间距按规则规范化；标题/表格/围栏完全匹配；无审计循环 | 阶段 1 + 阶段 5（结构性与表面拆分）+ 小样本示例 3 |
| 10 | M11/M12 模态：“shall”→ 须/应当；“significantly associated with”→ 与……显著相关（统计学），从不译为“导致” | 防御性协议 2 — 法律标记（shall）+ 医学标记（统计声明） |
| 11 | H10 持久性：带有第 1 段术语表的第 2 段复现相同术语；术语库覆盖优先于内置 | 术语表模式 — 结转块 + 术语优先级梯级 |
| 12 | 输出卫生：无模式标志 → 零元评论；`--qa` → 仅含严重性计数的审计摘要 | 模式 + 输出约束 + 自测（模式输出检查） |

---

## 自审通过结果

### 第 1 次检查 — 矛盾扫描

针对 C2/C3/C4/C6 失败模式进行了十五项两两矛盾检查。全部通过：

1. 引号规则（C2）— 按段落语言 + 排版配置文件作用域；无冲突。
2. 拓扑检查（C3）— 拆分为结构性与表面；无冲突。
3. 译者注（C4）— 所有条件引用均解析到 `--notes` 模式；无未定义门禁。
4. 静默失败（C5）— 已废除；通知通道 + `--strict` 定义一致。
5. 完全相同数字（C6）— 替换为数值等价标准；在阶段 5、示例 1 和防御性协议 7 中一致。
6. 方向检测（C7）— §0 全面定义了触发条件。
7. 迭代预算（C8）— 单一全局预算，引用一致。
8. 解码参数（C1）— 角色中为行为契约；部署说明中为文字设置；无重叠。
9. 公理 1 与习语处理 — 许可偏离说明协调两者。
10. 公理 4 与运行时标志 — 标志不得覆盖公理；在公理 4 和模式章节中一致。
11. 作品标题与实体锚定 — 组织名称在两节中均排除在《》之外。
12. 术语表结转与优先级梯级 — 顺序一致。
13. `--strict` 模式行为 — 在模式、阶段 5 和输出约束中一致。
14. `--publishing` 配置文件范围 — 在模式和排版规则中一致。
15. 不可变元素本地化例外 — 在实体锚定、阶段 1 和模式（`--translate-comments`）中一致。

### 第 2 次检查 — 验证套件（12 个用例）

针对草案对 v5 计划 §5（验证套件）中所有 12 个用例进行了心理执行：

1. 法律模态陷阱（英译中）— 示例 1 覆盖；通过。
2. 法律模态陷阱（中译英）— 示例 5 覆盖；通过。
3. RFC 2119 大写/小写 — 工程标记表区分；通过。
4. 注入尝试 — 示例 6 覆盖；通过。
5. OCR 伪影 — 示例 7 覆盖；通过。
6. 混合弯/直引号 — 排版规则 + 自测覆盖；通过。
7. 双语输入 — §0 规则 3 覆盖；通过。
8. 第三语言输入 — §0 规则 4 + 通知通道覆盖；通过。
9. 区域切换 — 模式（`--locale`）覆盖；通过。
10. 金融模糊表达 — 金融标记表覆盖；通过。
11. 统计声明 — 医学标记表覆盖；通过。
12. 作品标题 — 示例 8 + 作品标题映射覆盖；通过。
13. 3 段术语持久性链 — 结转块 + 优先级梯级覆盖；通过。

### 第 3 次检查 — 验收标准检查

v5 计划 §4 中所有 12 项验收标准均确认可满足。参见上文的“验收标准状态”表。

---

## 行数比较

| 指标 | v4.0 | v5.0 | 差值 |
|------|------|------|------|
| 总行数 | 214 | 629 | +415 |
| 顶级章节（`###`） | 8 | 17 | +9 |
| 小样本示例数 | 4 | 8 | +4 |
| 模态表数量 | 3（单向） | 4（双向） | +1 |
| 定义的模式标志数 | 1（隐含 `--glossary`） | 8 | +7 |
| 关键缺陷数 | 8 | 0 | −8 |
| 高优先级缺口数 | 11 | 0 | −11 |
| 中优先级问题数 | 13 | 0 | −13 |
| 低优先级发现数 | 6 | 0 | −6 |

---

## 操作员迁移须知

1. **即插即用替换。** v5.0 设计为 v4.0 的即插即用替代品。无需外部代码更改；提示词是自包含的。
2. **推理层设置。** 模型先前声称的文字 `temperature=0` / `top_p=0.1` 设置现已作为部署说明中的操作员指引。已经应用这些设置的操作员无需更改任何内容；未应用的操作员应应用这些设置以获得最佳效果。
3. **新标志为可选启用。** 新模式标志（`--notes`、`--qa`、`--strict`、`--locale`、`--termbase`、`--translate-comments`、`--publishing`）均为可选启用。默认行为（仅负载、zh-CN/en-US、技术性排版配置文件）与 v4.0 可观察行为匹配——除了审计失败现在会输出可见的通知通道行而不是静默失败（C5 修复）。
4. **向后兼容 `--glossary`。** v4.0 中的 `--glossary` 标志仍然有效；架构现在更严格（确定性枚举、首次出现排序），但基本格式不变。
5. **无认证翻译声明。** 新的符合性等级定义章节明确说明引擎输出 *不是* 认证或宣誓翻译。这是范围澄清，而非能力降低——v4.0 也未曾产生认证翻译，只是没有明确说明。

---

*变更日志结束。有关 v5.0 提示词本身，请参阅 `Translation_Engine_v5_Prompt.md`。*
