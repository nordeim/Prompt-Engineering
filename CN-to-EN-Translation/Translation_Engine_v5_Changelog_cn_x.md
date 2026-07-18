# 翻译计划：《Translation Engine v4.0 → v5.0 Changelog》EN→CN

---

## 一、文档概况分析

**文档类型：** 技术变更日志（changelog），属于工程/技术写作体裁，兼具文档管理与质量审计属性。

**篇幅：** 约 214 行（v4.0 原始行数），内容包含大量结构化表格、编号列表、引用代码标识、内联代码（如标志名称 `--strict`、文件名 `Translation_Engine_v5_Prompt.md`）、以及跨多个维度的交叉引用。

**语域（register）：** 工程技术文档 + 质量审计报告。混合了以下子语域：
- 软件工程（版本管理、配置参数、部署说明）
- 翻译行业（术语管理、翻译质量评估、MQM 框架）
- 质量审计（发现项分类、严重性等级、验收标准、回归验证）

---

## 二、翻译方向与区域设定

| 参数 | 设定 |
|------|------|
| 源语言 | English (EN) |
| 目标语言 | 简体中文 (zh-CN) |
| 术语体系 | 大陆术语（软件、网络、程序、默认） |
| 标点规范 | 中文段落使用全角标点；英文代码/标识符段落保留半角标点 |
| CJK-Latin 间距 | 中文字符与相邻拉丁字母/阿拉伯数字之间插入半角空格 |

---

## 三、术语锁定表（核心）

以下为文档中高频出现且必须全文一致的核心术语对。按出现频率和重要性排列。

### 3.1 版本与文档管理术语

| 英文 | 中文 | 备注 |
|------|------|------|
| changelog | 变更日志 | |
| major revision | 重大修订 | |
| finding | 发现项 | 审计语境 |
| Critical / High / Medium / Low | 严重 / 高 / 中 / 低 | 严重性等级，四档一致 |
| disposition | 处置方式 | 审计发现项的处理结果 |
| traceability artifact | 可追溯性工件 | |
| audit document | 审计文档 | |
| acceptance criteria | 验收标准 | |
| regression | 回归 | 质量验证语境 |
| scope boundary | 范围边界 | |
| backward compatibility | 向后兼容 | |
| drop-in replacement | 直接替换 | |

### 3.2 引擎架构术语

| 英文 | 中文 | 备注 |
|------|------|------|
| deterministic state machine | 确定性状态机 | |
| behavioral-determinism contract | 行为确定性契约 | |
| decoding parameters | 解码参数 | |
| deployment note | 部署说明 | |
| inference layer | 推理层 | |
| axiom | 公理 | |
| Instruction Quarantine | 指令隔离 | 固定译法 |
| Defensive Protocol | 防御协议 | 固定译法 |
| Entity Anchoring | 实体锚定 | 固定译法 |
| Modal & Epistemic Mapping | 模态与认知映射 | 固定译法 |
| Anti-Translationese | 反翻译腔 | 固定译法 |
| Grammar Asymmetry Protocol | 语法不对称协议 | 固定译法 |
| Quantity & Locale Conventions | 数量与区域惯例 | 固定译法 |
| Terminology Precedence Ladder | 术语优先级阶梯 | 固定译法 |
| Notice Channel | 通知通道 | 固定译法 |
| self-referential | 自指 | C1 语境 |
| prompt injection | 提示注入 | |
| licensed deviation | 许可偏差 | |

### 3.3 翻译行业术语

| 英文 | 中文 | 备注 |
|------|------|------|
| locked glossary | 锁定术语表 | |
| locked-standard | 锁定-标准 | Certainty 枚举值，保留英文标识 |
| locked-context | 锁定-上下文 | 同上 |
| candidate | 候选 | 同上 |
| carry-over glossary | 承接术语表 | |
| domain pack | 领域包 | |
| termbase | 术语库 | |
| modality tables | 模态映射表 | |
| collocation pairs | 搭配对 | |
| few-shot calibration examples | 少样本校准示例 | |
| culturally-bound expressions | 文化绑定表达 | |
| functional equivalence | 功能对等 | |

### 3.4 质量评估术语

| 英文 | 中文 | 备注 |
|------|------|------|
| MQM-lite audit | MQM-lite 审计 | MQM 为专有框架名，保留原文 |
| severity class | 严重性等级 | |
| IU-Coverage Bookkeeping | 信息单元覆盖记账 | IU = Information Unit |
| Structural Topology | 结构拓扑 | |
| Surface Typography | 表面排版 | |
| Zero-Trust Audit | 零信任审计 | |
| self-correction iteration | 自校正迭代 | |
| repair budget | 修复预算 | |
| audit loop | 审计循环 | |

### 3.5 标记与配置项（不可变元素）

以下元素在翻译中**保持原文不变**，不翻译：

- 所有 Finding ID：C1–C8, H1–H11, M1–M13, L1–L6
- 所有运行时标志：`--glossary`, `--notes`, `--qa`, `--strict`, `--locale`, `--termbase`, `--translate-comments`, `--publishing`
- 文件名：`Translation_Engine_v5_Prompt.md`, `Translation_Engine_v4_Audit_and_v5_Plan.md`
- 版本号：v4.0, v5.0
- 推理层参数：`temperature=0`, `top_p=0.1`
- RFC/BCP 编号：RFC 2119, RFC 8174, BCP 14
- 国标编号：GB/T 28039-2011, GB/T 15834-2011
- Unicode 码位：U+201C, U+201D, U+2018, U+2019
- Markdown 语法标记示例：`#`, `##`, `###`, `` ` ` ``
- 行号引用：lines 1–4, lines 6–9, 等

---

## 四、结构拓扑保留清单

文档包含以下结构元素，翻译时必须逐一保留：

| 结构类型 | 数量（约） | 保留要求 |
|----------|-----------|----------|
| 一级标题 (`#`) | 1 | 层级、标记、顺序完全一致 |
| 二级标题 (`##`) | ~10 | 同上 |
| 三级标题 (`###`) | ~8 | 同上 |
| 表格（标准 Markdown） | ~15 | 列数、行数、对齐标记完全一致；表头翻译，内容翻译 |
| 编号列表 | ~12 | 编号层级与缩进一致 |
| 无序列表 | ~30 | 嵌套层级一致 |
| 行内代码 | ~40+ | 内容不变（标志名、文件名、参数值等） |
| 粗体标记 | ~20+ | 范围对应 |
| 加粗+代码混合 | 多处 | 如 **v4.0 location:** → **v4.0 位置：** |
| 分隔线 (`---`) | ~3 | 保留 |

---

## 五、难点与关键决策

### 5.1 表格单元格的翻译策略

文档中约 15 个表格是核心信息载体。表格单元格翻译需注意：
- **短语级条目**（如 "Self-referential decoding parameters"）→ 译为对应中文短语（"自指解码参数"）
- **代码/ID 引用**（如 "C1", "H8", "S3"）→ 不翻译
- **v5.0 section 列**（如 "Modes & Runtime Parameters"）→ 与 v5.0 正文中对应章节标题一致
- **Status 列**（"Closed"）→ 统一译为"已关闭"
- **Preservation 列**（"Preserved verbatim"）→ 统一译为"原文保留"

### 5.2 多层嵌套列表

v5.0 Changelog 中大量使用嵌套列表（如"Acceptance Criteria Status"表的右列包含较长描述），翻译时需确保：
- 缩进层级准确还原
- 长描述行在中文中保持简洁，不溢出破坏排版

### 5.3 混合语域句子的处理

部分句子同时包含技术描述和审计评价，例如：

> "All 12 acceptance criteria are satisfied by the v5.0 draft."

翻译策略：技术语言为主导语域，使用工程/审计中文表达习惯：
→ "v5.0 草案满足全部 12 项验收标准。"

### 5.4 Finding ID 的引用格式

原文中 Finding ID 以多种形式出现：
- 表格单元格内：`C1`, `H8`, `M3`, `L4`
- 多个 ID 并列：`H2, H3, M11, M12`
- 标题中：`C1 — Self-referential decoding parameters`
- 列表中：`1. C1 — Self-referential decoding parameters`

**决策：** Finding ID 全部保留英文原文不翻译。标题中的描述性部分翻译。

→ `C1 — 自指解码参数`

### 5.5 "Disposition" 一词的翻译

该词在文档中高频出现（约 15 次），且在不同上下文中含义略有差异：
- "Disposition in v5.0" → "在 v5.0 中的处置方式"
- "Disposition Detail"（二级标题）→ "处置详情"
- "Status" 列中的 "Closed" → 该列本身即为 disposition 的简化表达

**决策：** 统一译为"处置"，搭配词灵活处理。

### 5.6 长标题的翻译节奏

部分二级标题较长，如：
> "C1 — Self-referential decoding parameters"

中文需保持技术文档标题的简洁感：
→ `C1 — 自指解码参数`

> "M6 — 'Information density proportional' unmeasurable"

→ `M6 — "信息密度成比例"不可测量`

### 5.7 引号的特殊处理

文档中含有多处语言学讨论中需要保留原文引号的场景，例如：
- 讨论中文引号 `""` `''` (U+201C/201D/2018/2019) 时，这些引号本身是讨论对象，需用代码标记或明确标注
- 讨论英文直引号 vs 弯引号时同理

**决策：** 引号作为代码讨论对象时，使用行内代码标记（`` `""` ``）或明确标注 Unicode 码位，确保中文译文不产生歧义。

---

## 六、翻译执行计划（分阶段）

### Phase 1：拓扑解析与不可变元素锁定

- 逐行扫描文档，标记所有 Markdown 结构元素（标题层级、表格、列表、行内代码、粗体）
- 锁定全部不可变元素（Finding ID、标志名、文件名、版本号、Unicode 码位、行号引用、RFC/BCP/GB 标准号）
- 记录表格的列数、行数、对齐方式

**产出：** 结构拓扑蓝图 + 不可变元素清单

### Phase 2：语义解构与模态标注

- 将文档拆分为信息单元（IU）
- 标注每个 IU 的语域（技术/审计/管理）
- 标注逻辑连接词（因果、转折、条件、递进、时序）
- 识别跨段落的术语一致性需求

**产出：** IU 列表 + 语域/模态标注

### Phase 3：领域重构与翻译执行

按文档自然顺序逐节翻译，确保：
- 术语表全文一致
- 中文表达符合技术文档习惯（避免翻译腔）
- 数字、百分比、版本号等精确对应
- 格式标记（Finding ID 引用方式、表格状态值）统一

**翻译顺序：**
1. 标题块（Subject / Change type / Audit document / v5.0 artifact）
2. "Summary by Section" 表
3. "Critical Fixes" 小节（C1–C8）
4. "High Coverage Gaps" 小节（H1–H11 表 + 展开段落）
5. "Medium Precision Issues" 小节（M1–M13）
6. "Low Findings" 小节（L1–L6）
7. "v4.0 Strengths Preserved" 小节（S1–S8）
8. "Acceptance Criteria Status" 小节
9. "Self-Review Pass Results" 小节
10. "Line-Count Comparison" 表
11. "Migration Notes for Operators" 小节
12. 页脚声明

### Phase 4：排版编译

- 中文段落：全角标点（，。！？；：""''（））
- 中文与拉丁字母/数字之间：半角空格
- 行内代码前后：半角空格
- 表格对齐：与原文一致
- 粗体标记范围：与原文 IU 对应

### Phase 5：零信任审计

逐项核查：
- **事实核查：** 所有 Finding ID、数量（12 项验收标准、15 次矛盾检查、214 行/629 行等）、文件名、版本号精确无误
- **模态核查：** 无升降级（如 "designed as" → "设计为"，不译为"保证"）
- **结构拓扑核查：** 标题层级、表格行列、列表嵌套完全一致
- **术语一致性核查：** 全文同一术语译法一致
- **信息覆盖核查：** 无遗漏 IU，无添加原文未提及的信息

---

## 七、风险预判

| 风险 | 等级 | 应对策略 |
|------|------|----------|
| 表格列宽导致中文译文溢出 | 中 | 使用更简洁的中文表达；必要时适当缩短同义表述 |
| Finding ID 引用密度极高，易遗漏 | 中 | Phase 5 逐一核对每个 ID 的出现 |
| 同一英文术语在不同小节中语境略有差异 | 低 | 根据术语表统一译法，仅在搭配层面灵活调整 |
| "verbatim"、"preserved" 等词的精确传达 | 低 | "verbatim" → "原文"/"逐字"；"preserved" → "保留"；区分使用 |
| 技术与审计双语域的自然切换 | 低 | 以工程/技术文档中文规范为主，审计用语辅助 |

---

## 八、质量目标

| 维度 | 目标 |
|------|------|
| 事实保真 | 100% — 所有 Finding ID、数字、文件名、版本号零误差 |
| 术语一致性 | 100% — 全文同一术语同一译法 |
| 结构完整性 | 100% — 标题、表格、列表层级完全对应 |
| 表面排版 | ≥ 98% — CJK-Latin 间距、标点全角/半角符合规范 |
| 可读性 | 自然流畅的中文技术文档风格，无翻译腔 |

---

以上为完整的翻译执行计划。如确认无误，可进入执行阶段（Phase 3）开始逐节翻译。
