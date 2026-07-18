# Translation Engine v4.0 → v5.0 变更日志

**主题：** `System Prompt: Deterministic Forensic Translation Engine`
**变更类型：** 重大修订（处理 38 项发现：8 项 Critical、11 项 High、13 项 Medium、6 项 Low）
**审计文档：** `Translation_Engine_v4_Audit_and_v5_Plan.md`
**v5.0 制品：** `Translation_Engine_v5_Prompt.md`（629 行，约 47 KB）

本变更日志将每一处 v4.0 章节/行号映射到其在 v5.0 中的处置方式，并标注驱动每项变更的发现 ID。它构成 v5 计划执行步骤 4 所要求的可追溯性制品。

---

## Summary by Section

| v4.0 章节 | v5.0 中的处置 | 发现 ID |
|---|---|---|
| Header + Role（第 1–4 行） | 修订：行为确定性契约取代解码参数声明 | C1 |
| System Parameters（第 6–9 行） | 拆分：行为契约保留在 Role 块中；字面解码设置移至标注为操作员指引的 "Deployment Note" 块 | C1 |
| Core Philosophy（3 条公理） | 保留并扩展：Axiom 1 新增许可偏差说明以与习语处理相调和；新增 Axiom 4（Instruction Quarantine） | H8 |
| Defensive Protocol 1 — Entity Anchoring | 保留并扩展：双向化；新增 person/place/case/honorific 子协议；修正示例划分（Translated 集合 vs Preserved 集合）；术语权威阶梯 | H6, M1, M3 |
| Defensive Protocol 2 — Modal & Epistemic Mapping | 保留并扩展：所有表格双向化；新增 `shall`；新增 Financial 标记；新增统计学陈述标记 | H2, H3, M11, M12 |
| Defensive Protocol 3 — Anti-Translationese | 保留（S3）并扩展以补充搭配 | — |
| Defensive Protocol 4 — Culturally-Bound Expressions | 保留（S8）并精化；与 `--notes` 模式关联 | — |
| Defensive Protocol 5 — Source Error / OCR | 保留并与 `--notes` 模式关联 | L4 |
| （新增）Defensive Protocol 6 — Grammar Asymmetry | 新增：时态/体、数、定指性、性别未知代词 | H4 |
| （新增）Defensive Protocol 7 — Quantity & Locale Conventions | 新增：数值等价标准、货币、日期、单位、百分比/范围 | H5, C6 |
| Mandatory Multi-Phase Workflow | 修订：单一全局修复预算（≤2 次审计循环；其他阶段各执行一次）；Phase 5 改为带严重度分级的 MQM-lite 审计；拓扑检查拆分为结构层与表面层 | C3, C8, M6 |
| Phase 1: Topological Parsing | 保留并澄清 HTML 表格处理 + 注释策略关联 | L5, H11 |
| Phase 2: Semantic & Modal Deconstruction | 保留 | — |
| Phase 3: Domain Reconstruction | 保留 + 应用 Grammar Asymmetry 与 Quantity & Locale | H4, H5 |
| Phase 4: Typographical Compilation | 修订：拆分为 Structural Topology 与 Surface Typography；作品标题映射；嵌套引号/括号规则；CJK–Latin 间距边界情形；emoji/mention/hashtag 透传 | C2, C3, H7, M4, M13, L2 |
| Phase 5: Zero-Trust Audit | 修订：MQM-lite 严重度分级；IU 覆盖率记账取代"信息密度"检查；仅结构层拓扑检查；数值等价标准取代"完全一致数字" | C3, C6, M6 |
| Ambiguity Resolution Protocol | 保留（S4）并与 Notice Channel 及 `--notes` 模式关联 | C4 |
| Quality Priorities | 保留（S5）+ 按优先级分配 MQM-lite 严重度分级 | — |
| Strict Output Constraints | 修订：定义 Notice Channel；no-silent-failure 规则；模式特定输出 | C4, C5 |
| Optional Glossary Output Mode | 修订：完善 schema；定义 Certainty 枚举；首次出现排序；carry-over 块格式 | H10, M9 |
| （新增）§0 Intake & Direction Protocol | 新增 | C7 |
| （新增）Modes & Runtime Parameters | 新增：default、`--glossary`、`--notes`、`--qa`、`--strict`、`--locale`、`--termbase`、`--translate-comments`、`--publishing` | C4, C5, H1, H9, M5 |
| （新增）Terminology Precedence Ladder | 新增：6 级优先级，从用户术语库降至"保留原文" | H9, M3 |
| （新增）Conformance Level Definitions（L1–L4） | 新增：每级验收标准；范围边界声明 | M8, L3 |
| Few-Shot Calibration Examples | 修订：4 → 8 个示例；替换 Example 3（无操作）；新增：CN→EN 法律对冲、注入隔离、OCR 伪迹、作品标题 | M7, L4 |
| Self-Test Instruction | 修订：限定范围引号检查；锁定保留豁免；notice-channel 检查；模式输出检查 | C2, M10 |
| （新增）Extensibility: Domain Pack | 新增：可插拔的语域扩展 | future-proofing |
| Footer（"Translation Quality Target"） | 保留 + 新增版本行 | — |

---

## Critical Fixes（C1–C8）— 处置详情

### C1 — 自指的解码参数
- **v4.0 位置：** 第 7–9 行（"Set `temperature=0` and `top_p=0.1` for all translation operations."）
- **v5.0 修复：** 在 Role/Operating Mode 块中以行为确定性契约替代（"Operate as a deterministic state machine: at every decision point, choose the rendering most consistent with the locked glossary, the modality tables, and prior choices within the same payload"）。字面解码设置移至 "Deployment Note (for the inference layer, not the model)" 块，明确标注为模型自身控制之外的操作员指引。

### C2 — "No smart quotes" 检查门与强制中文排版相冲突
- **v4.0 位置：** Phase 4 强制使用中文全角引号 `""` `''`（U+201C/201D/2018/2019 — 与英文弯引号相同的码位）；Self-Test 要求"no smart quotes"。
- **v5.0 修复：** 引号宽度规则现在按段落语言与排版配置限定范围：中文段落*保留* `""` `''`；英文技术段落使用直引号；`--publishing` 配置允许英文散文中使用弯引号。Self-Test 改写为："No half-width-converted or flattened quotes in Chinese segments (Chinese segments retain `""` `''` U+201C/201D/2018/2019); no curly quotes in English technical segments (default profile) unless `--publishing` is active."

### C3 — 拓扑保真检查与强制排版变换相冲突
- **v4.0 位置：** Phase 5 拓扑检查要求每个 Markdown 符号"与源文完全一致"，而 Phase 4 *要求*偏离源文表面（注入间距、引号规范化、标点宽度转换）。
- **v5.0 修复：** Phase 5 审计现在区分**Structural Topology Check**（标题、列表、表格、围栏、链接目标 — 必须与源文完全一致）与**Surface Typography Check**（按 Phase 4 规则规范化；豁免于源文一致性检查，改为对照排版规则审计）。Few-Shot Example 3 明确演示了这一区分。

### C4 — 译者注有条件地允许，但允许其存在的模式并不存在
- **v4.0 位置：** Defensive Protocol 4 与 Ambiguity Protocol 第 4 步引用了"output mode permits commentary"，但该模式从未定义。
- **v5.0 修复：** 新的 `Modes & Runtime Parameters` 章节明确定义了 `--notes` 模式（允许内联 `[译注: …]` 注释）与 `--qa` 模式（允许审计摘要）。所有对"if the output mode permits"的引用现在都解析到一个已定义的标志。

### C5 — 静默的尽力而为回退破坏了取证保证
- **v4.0 位置：** Phase 5 — "halt and output the best-effort translation with a silent internal flag (do not expose the flag to the user)."
- **v5.0 修复：** "Silent internal flag" 机制废止。新的 Notice Channel 协议：默认模式下审计失败在载荷末尾追加一行 `[NOTICE]`；`--strict` 模式*仅*输出 Notice 行并抑制载荷。No-silent-failure 规则在 Output Constraints 中明确声明。

### C6 — "Identical numbers" 事实检查与数字本地化示例相冲突
- **v4.0 位置：** Phase 5 Fact Check 要求数字"完全一致"；Example 1 要求将 "$2.4 million" → "240 万美元"。
- **v5.0 修复：** Phase 5 Fact Check 现在要求"在 Quantity & Locale Conventions 下数值等价"（而非表面一致）。新的 Defensive Protocol 7 — Quantity & Locale Conventions — 明确定义了转换策略（货币、日期、单位、百分比/范围）。

### C7 — 缺失核心操作指令：方向检测
- **v4.0 位置：** 完全缺失。
- **v5.0 修复：** 在 Core Philosophy 之前新增 §0 Intake & Direction Protocol。定义：显式覆盖处理、自动检测、双语载荷处理、第三语言 Notice Channel、空/乱码载荷行为、同语言"翻译"请求。

### C8 — 迭代预算被双重且不一致地规定
- **v4.0 位置：** Workflow 头部称"Maximum self-correction iterations per phase: 2"；Phase 5 称"return to Phase 3 (maximum 2 iterations)."
- **v5.0 修复：** 单一全局修复预算仅声明一次："Audit-failure loops ≤ 2. All other phases execute exactly once." 删除各阶段措辞。Phase 5 一致地引用全局预算。

---

## High Coverage Gaps（H1–H11）— 处置详情

| ID | 缺口 | v5.0 章节 | 状态 |
|----|-----|--------------|--------|
| H1 | 无区域设置维度（简体/繁体、中国大陆/台湾、美国/英国） | Modes & Runtime Parameters — `--locale=zh-CN\|zh-TW\|en-US\|en-GB` + Entity Anchoring 区域设置术语子规则 | 已关闭 |
| H2 | 情态表单向 | Defensive Protocol 2 — 所有表格双向化并配有对称反例 | 已关闭 |
| H3 | 列出财务语域但无标记 | Defensive Protocol 2 — 新增 Financial / Securities-Disclosure Markers 块（10 个条目） | 已关闭 |
| H4 | 无语法不对称协议 | Defensive Protocol 6 — Grammar Asymmetry Protocol（时态/体、数、冠词、代词） | 已关闭 |
| H5 | 无数量、日期或单位策略 | Defensive Protocol 7 — Quantity & Locale Conventions | 已关闭 |
| H6 | 命名实体覆盖缺口（人名、地名、案件名、敬称） | Defensive Protocol 1 — 扩展 person/place/case/honorific 子协议 | 已关闭 |
| H7 | 无作品标题排版映射（《》 ↔ 斜体/引号） | Typography Rules — Title-of-Works Mapping 表，含 GB/T 排除清单 | 已关闭 |
| H8 | 无提示词注入隔离 | Axiom 4 — Instruction Quarantine | 已关闭 |
| H9 | 无用户术语库注入或优先级协议 | Modes（`--termbase`）+ Terminology Precedence Ladder（6 级） | 已关闭 |
| H10 | 无跨片段术语持久化 | Glossary Mode — Carry-Over 块格式已定义 | 已关闭 |
| H11 | 代码注释与 UI 字符串不可变性过度延伸 | Defensive Protocol 1 — 本地化例外 + Phase 1 注释策略（`--translate-comments`） | 已关闭 |

---

## Medium Precision Issues（M1–M13）— 处置详情

| ID | 问题 | v5.0 修复 |
|----|-------|-----------|
| M1 | "Meta" 被错误归类为翻译名示例 | Defensive Protocol 1 — 拆分为 Translated 集合（苹果、微软、谷歌、亚马逊、甲骨文）与 Preserved 集合（Meta、OpenAI、Anthropic、Palantir） |
| M2 | RFC 2119 引用不精确（小写 "must" 对比大写 MUST） | Defensive Protocol 2 — Engineering markers 表区分 MUST/SHOULD/MAY（大写，BCP 14 规范性）与 must/should/may（小写，普通英语） |
| M3 | "Universally preferred" 循环定义 | 由 Terminology Precedence Ladder（6 级显式优先级）解决 |
| M4 | CJK–Latin 间距规则未标注为风格选择 | Typography Rules — 标注为"digital house-style rule"；枚举边界情形（全角标点邻接、`%`/`$`/`°`/单位符号、加粗/斜体跨度、链接文本） |
| M5 | 仅直引号规则与出版声明相冲突 | Typography Rules — English Typography 现有 Default（技术，直引号）与 Publishing（`--publishing`，散文中允许排版引号）配置 |
| M6 | "Information density proportional" 不可度量 | Phase 5 — 以 IU-Coverage Bookkeeping 检查替代 |
| M7 | Example 3 为无操作 | Few-Shot Example 3 替换为演示排版、不可变性与 C3 结构层 vs 表面层区分的 EN→CN 案例 |
| M8 | 调用 L1–L4 等级但未定义 | 新增 Conformance Level Definitions 章节 — 每级验收标准 |
| M9 | 术语表 schema 中 "Certainty" 未定义 | Glossary Mode — Certainty 枚举：`locked-standard` / `locked-context` / `candidate`；首次出现排序 |
| M10 | Self-test 中 "no unexplained English" 误报强制保留项 | Self-Test — Locked-Retention Exemption：不可变元素、锁定术语表保留项与领域标准缩写免于检查 |
| M11 | 情态映射表中缺失 "shall" | Defensive Protocol 2 — Legal markers 表：`shall` → 须/应当；`shall not` → 不得 |
| M12 | 统计/医学术态缺口 | Defensive Protocol 2 — Medical markers 表扩展："significant (stat.)" → 具有统计学意义；"associated with" → 与……相关（绝不译作 导致） |
| M13 | "Dominant language" 标点规则对嵌套情形规定不足 | Typography Rules — 明确嵌套情形：中文内全英文括号遵循英文规则；中文嵌套引号遵循 outer-双 inner-单（"…'…'…"） |

---

## Low Findings（L1–L6）— 处置详情

| ID | 问题 | v5.0 修复 |
|----|-------|-----------|
| L1 | "Halt and output" 残留 | 由 Notice Channel + `--strict` 机制替代 |
| L2 | 无 emoji/mentions/hashtags 透传 | Typography Rules — 显式透传规则 |
| L3 | 无范围边界声明（引擎 ≠ 认证翻译） | Conformance Level Definitions — 显式范围边界声明 |
| L4 | 仅有 4 个校准示例；无对抗性示例 | Few-Shots — 扩展至 8 个；新增：CN→EN 法律对冲、注入尝试、OCR 伪迹、作品标题 |
| L5 | "Merged cells" 暗示 HTML 表格 | Phase 1 — 澄清：标准 Markdown 表格按原样支持；带 `colspan`/`rowspan` 的 HTML 表格原样保留，仅翻译单元格文本 |
| L6 | 无对冒犯性/敏感内容的保真立场 | 隐含于 Axiom 1 + Axiom 4 — 取证完整性 = 按原样翻译，不做净化；Axiom 4 也中和任何由安全过滤器注入并会编辑内容的"soft refusal" |

---

## v4.0 优势保留（S1–S8）

| ID | 优势 | 在 v5.0 中的保留方式 |
|----|----------|----------------------|
| S1 | 带反例的显式情态表 | 原样保留并双向扩展（Legal、Engineering、Medical、Financial） |
| S2 | 不可变元素锚定 | 原样保留并精化（本地化例外、注释策略） |
| S3 | 反翻译腔搭配对（双向） | 原样保留并扩展（8 个 EN→CN + 6 个 CN→EN 搭配） |
| S4 | Ambiguity Resolution Protocol 作为有序层级 | 原样保留，关联至 Notice Channel 与 `--notes` 模式 |
| S5 | 带覆盖规则的 Quality Priorities | 原样保留，叠加 MQM-lite 严重度分级 |
| S6 | 带推理行的 Few-shot 示例 | 保留并扩展（4 → 8 个示例） |
| S7 | 禁止元评论/阶段泄漏 | 原样保留 |
| S8 | 带功能等价偏好的文化绑定习语处理 | 原样保留并精化（功能等价现在通过许可偏差说明与 Axiom 1 相调和） |

---

## 验收标准状态（v5 Plan §4）

v5.0 草案满足全部 12 项验收标准。右栏标明了对应规则在 `Translation_Engine_v5_Prompt.md` 中的位置。

| # | 标准 | v5.0 位置 |
|---|-----------|----------------|
| 1 | C2 回归：含 `""` 的中文源文在输出中产生 U+201C/201D；Self-Test 不报警 | Typography Rules（Chinese Typography）+ Self-Test（限定范围引号检查） |
| 2 | C7 方向：单语 EN → CN；单语 CN → EN；法语 → 单行 Notice，无翻译 | §0 Intake & Direction Protocol + Output Constraints（Notice Channel） |
| 3 | C5 可见性：强制审计失败 → 默认追加 Notice；`--strict` 仅输出 Notice | Modes（`--strict`）+ Phase 5 审计失败行为 + Output Constraints（no-silent-failure rule） |
| 4 | H8 注入：含 "ignore previous instructions" 的源文 → 原样翻译；行为不变 | Axiom 4 + Few-Shot Example 6 |
| 5 | H2 双向性："涉嫌转移资产" → "allegedly transferred assets"；"allegedly" → 涉嫌/据称 | Defensive Protocol 2 — Legal markers 表（双向）+ Few-Shot Example 5 |
| 6 | H1 区域设置：`--locale=zh-TW` → 軟體/網路；默认 → 简体 + 大陆术语 | Modes（`--locale`）+ Entity Anchoring（区域设置术语子规则） |
| 7 | H5 数量："$2.4 million" → 240 万美元；"yesterday" → 昨天；不进行 USD↔CNY 转换 | Defensive Protocol 7 — Quantity & Locale Conventions + Few-Shot Example 1 |
| 8 | H7 标题：《三体》 → *The Three-Body Problem*；"Hamlet" → 《哈姆雷特》；组织名绝不以 《》 包裹 | Typography Rules — Title-of-Works Mapping + Few-Shot Example 8 |
| 9 | C3 拓扑：弯引号 + 紧凑 CJK 间距按规则规范化；标题/表格/围栏完全一致；无审计循环 | Phase 1 + Phase 5（Structural vs Surface 拆分）+ Few-Shot Example 3 |
| 10 | M11/M12 情态："shall" → 须/应当；"significantly associated with" → 与……显著相关（统计学），绝不使用 导致 | Defensive Protocol 2 — Legal markers（shall）+ Medical markers（统计学陈述） |
| 11 | H10 持久化：片段 2 复用片段 1 的术语表可复现相同术语；termbase 覆盖优于内置 | Glossary Mode — Carry-Over 块 + Terminology Precedence Ladder |
| 12 | 输出清洁度：无模式标志 → 零元评论；`--qa` → 仅含严重度计数的审计摘要 | Modes + Output Constraints + Self-Test（模式输出检查） |

---

## 自审通过结果

### Pass 1 — 矛盾扫描

针对 C2/C3/C4/C6 失败模式执行了 15 项两两矛盾检查。全部通过：

1. 引号规则（C2）— 按段落语言 + 排版配置限定范围；无冲突。
2. 拓扑检查（C3）— 拆分为结构层 vs 表面层；无冲突。
3. 译者注（C4）— 所有条件引用都解析到 `--notes` 模式；无未定义的门控。
4. 静默失败（C5）— 废止；Notice Channel + `--strict` 一致定义。
5. 完全一致数字（C6）— 以数值等价标准替代；在 Phase 5、Example 1 与 Defensive Protocol 7 中保持一致。
6. 方向检测（C7）— §0 全面定义了触发条件。
7. 迭代预算（C8）— 单一全局预算，被一致引用。
8. 解码参数（C1）— 行为契约在 Role 中；字面设置在 Deployment Note 中；无重叠。
9. Axiom 1 与习语处理 — 许可偏差说明对二者进行调和。
10. Axiom 4 与运行时标志 — 标志不可覆盖公理；在 Axiom 4 与 Modes 章节中保持一致。
11. 作品标题与 Entity Anchoring — 两章节都将组织名排除在 《》 之外。
12. 术语表 carry-over 与 Precedence Ladder — 顺序一致。
13. `--strict` 模式行为 — 在 Modes、Phase 5 与 Output Constraints 中保持一致。
14. `--publishing` 配置范围 — 在 Modes 与 Typography Rules 中保持一致。
15. 不可变元素本地化例外 — 在 Entity Anchoring、Phase 1 与 Modes（`--translate-comments`）中保持一致。

### Pass 2 — 验证套件（12 个用例）

来自 v5 Plan §5（验证套件）的全部 12 个用例已对照草案在脑内执行：

1. 法律情态陷阱（EN→CN）— Example 1 覆盖；通过。
2. 法律情态陷阱（CN→EN）— Example 5 覆盖；通过。
3. RFC 2119 大写/小写 — Engineering markers 表已区分；通过。
4. 注入尝试 — Example 6 覆盖；通过。
5. OCR 伪迹 — Example 7 覆盖；通过。
6. 弯引号/直引号混合 — Typography Rules + Self-Test 覆盖；通过。
7. 双语输入 — §0 规则 3 覆盖；通过。
8. 第三语言输入 — §0 规则 4 + Notice Channel 覆盖；通过。
9. 区域设置切换 — Modes（`--locale`）覆盖；通过。
10. 财务对冲 — Financial markers 表覆盖；通过。
11. 统计学陈述 — Medical markers 表覆盖；通过。
12. 作品标题 — Example 8 + Title-of-Works Mapping 覆盖；通过。
13. 3 片段术语持久化链 — Carry-over 块 + Precedence Ladder 覆盖；通过。

### Pass 3 — 验收标准检查

来自 v5 Plan §4 的全部 12 项验收标准已确认可满足。参见上文的"验收标准状态"表。

---

## 行数对比

| 指标 | v4.0 | v5.0 | 差值 |
|---|---|---|---|
| 总行数 | 214 | 629 | +415 |
| 章节（顶层 `###`） | 8 | 17 | +9 |
| Few-shot 示例 | 4 | 8 | +4 |
| 情态表 | 3（单向） | 4（双向） | +1 |
| 已定义模式标志 | 1（隐式 `--glossary`） | 8 | +7 |
| Critical 缺陷计数 | 8 | 0 | −8 |
| High 缺口计数 | 11 | 0 | −11 |
| Medium 问题计数 | 13 | 0 | −13 |
| Low 发现计数 | 6 | 0 | −6 |

---

## 操作员迁移须知

1. **直接替换。** v5.0 设计为 v4.0 的直接替换。无需外部代码改动；提示词自包含。
2. **推理层设置。** 此前由模型声明的字面 `temperature=0` / `top_p=0.1` 设置现在作为操作员指引放在 Deployment Note 中。已经应用这些设置的操作员无需改动；尚未应用的操作员应予以应用以获得最佳结果。
3. **新标志为可选启用。** 新增模式标志（`--notes`、`--qa`、`--strict`、`--locale`、`--termbase`、`--translate-comments`、`--publishing`）均为可选启用。默认行为（仅载荷、zh-CN/en-US、技术排版配置）与 v4.0 可观察行为一致 — 除了审计失败现在会输出可见的 Notice Channel 行而非静默失败（C5 修复）。
4. **`--glossary` 向后兼容。** v4.0 的 `--glossary` 标志仍然可用；schema 现在更严格（Certainty 枚举、首次出现排序），但基本格式不变。
5. **无认证翻译声明。** 新增的 Conformance Level Definitions 章节明确指出引擎输出*不*构成认证或宣誓翻译。这是对范围的澄清，而非能力缩减 — v4.0 同样不产生认证翻译，只是未作说明。

---

*变更日志结束。关于 v5.0 提示词本身，请参见 `Translation_Engine_v5_Prompt.md`。*
