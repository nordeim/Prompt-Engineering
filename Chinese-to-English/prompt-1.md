Please meticulously plan to translate the following into English while preserving the content, its nuances, structure and layout.

Below is a meticulous translation plan designed to preserve **meaning, technical precision, rhetorical style, document hierarchy, formatting, and emphasis** before performing the actual translation.

## Translation Objectives

The English translation should preserve:

1. **Every factual claim** without omission or interpretation.
2. **Technical terminology** using industry-standard English terminology.
3. **Document hierarchy** (headings, subheadings, blockquotes, tables, separators).
4. **Evaluation tone**, which is formal, analytical, and evidence-based.
5. **Strength of certainty** (e.g. "成立" → "Confirmed", not merely "Likely").
6. **Markdown formatting** exactly where practical.

The result should read as though it were originally written by an experienced English technical analyst rather than as a literal translation.

---

# Overall Style

The Chinese document is written in the style of a professional technical verification report.

The English should therefore adopt:

* formal technical English
* concise but complete wording
* documentation/report style
* neutral and objective voice
* evidence-oriented language

Avoid adding commentary or explanatory notes that do not exist in the source.

---

# Document Structure

The following structure should remain unchanged.

```
Title

Executive Summary

horizontal rule

Verification Details

1.
quotation
verification result
analysis

2.
quotation
...

...

Summary

Markdown table

Final Conclusion
```

The numbering should remain exactly the same.

---

# Heading Translation

Translate headings using natural technical English rather than literal word-for-word translation.

Examples:

> 执行摘要

→

**Executive Summary**

---

> 声明验证详情

→

**Detailed Verification of Claims**

or

**Claim Verification Details**

(The latter is slightly closer to the original.)

---

> 总结

→

**Summary**

---

# Verification Labels

The repeated phrase

> 验证结果：✅ 成立

should become consistently

> **Verification Result:** ✅ Confirmed

Do **not** alternate between

* Valid
* True
* Correct
* Verified

Consistency is preferable.

---

# Quoted Claims

Every quoted claim should remain inside Markdown blockquotes.

Example

```
> Original claim...
```

should remain

```
> Original claim...
```

without changing formatting.

---

# Technical Terminology

Use established English terminology.

| Chinese    | English                |
| ---------- | ---------------------- |
| 执行环境       | execution environment  |
| 硬件隔离       | hardware isolation     |
| 内核逃逸       | kernel escape          |
| MicroVM    | MicroVM                |
| 冷启动        | cold start             |
| 常驻内存       | resident memory        |
| 快照         | snapshot               |
| 回滚         | rollback               |
| 克隆         | clone                  |
| 写时复制       | copy-on-write (CoW)    |
| 生命周期       | lifecycle              |
| 挂起         | suspend                |
| 恢复         | resume                 |
| 沙箱         | sandbox                |
| 裸金属服务器     | bare-metal server      |
| 宿主机        | host machine           |
| Guest OS   | guest OS               |
| Hypervisor | hypervisor             |
| 页表         | page table             |
| 嵌套虚拟化      | nested virtualization  |
| 文件系统       | filesystem             |
| 自动化安装      | automated installation |
| 一键安装       | one-click installation |

---

# Product Names

Never translate product names.

Keep exactly:

* CubeSandbox
* CubeCoW
* RustVMM
* KVM
* PVM
* AutoPause
* AutoResume
* E2B
* GitHub
* README.md
* Ubuntu
* XFS
* Ext4
* reflink
* FICLONE
* vmlinux

---

# Performance Numbers

Preserve every numerical expression exactly.

Examples

```
<60ms

<5MB

32GB

96-core server

2000+

67ms

P95 90ms

P99 137ms
```

Do not convert units.

---

# Chinese Evaluation Language

Translate with equivalent confidence.

Examples

---

成立

→

Confirmed

---

准确描述了

→

accurately describes

---

多个来源证实

→

confirmed by multiple sources

---

官方文档

→

official documentation

---

新闻稿

→

press releases

---

第三方评测

→

third-party evaluations

---

广泛讨论

→

widely discussed

---

一致确认

→

consistently confirmed

---

交叉验证

→

cross-validated

---

# Tone Preservation

The report intentionally sounds authoritative.

Avoid overly enthusiastic wording.

For example

Chinese:

> 具有高度可信度

Prefer

> is highly credible

instead of

> is unquestionably true

---

# Paragraph Style

Maintain paragraph boundaries.

Do not merge paragraphs.

Do not split paragraphs unnecessarily.

---

# Bullet Lists

Preserve bullet nesting exactly.

Example

```
* Ownership
* Technology Stack
* Core Capabilities
```

should remain identical.

---

# Horizontal Rules

Retain

```
---
```

exactly.

---

# Table

Preserve Markdown table formatting.

Recommended translation:

| Claim Category | Core Claim | Verification Result | Key Evidence Sources |
| -------------- | ---------- | ------------------- | -------------------- |

Translate only the contents.

Keep the checkmarks.

---

# Final Conclusion

Translate

> 最终结论

as

**Final Conclusion**

Maintain the same strength:

> The guide's descriptions of CubeSandbox's architecture, performance characteristics, and deployment methodology are accurate and well supported by publicly available evidence. All key technical claims can be cross-validated through official documentation, published benchmark data, and independent third-party technical analyses.

This preserves both the wording and the evidential emphasis without strengthening or weakening the original claim.

---

# Consistency Rules

Throughout the translation, ensure consistent rendering of recurring phrases:

| Chinese | English                |
| ------- | ---------------------- |
| 声明      | claim                  |
| 核心声明    | core claim             |
| 核心能力    | core capability        |
| 核心特性    | core feature           |
| 技术方案    | technical architecture |
| 技术路径    | technical approach     |
| 官方文档    | official documentation |
| 官方仓库    | official repository    |
| 发布说明    | release notes          |
| 更新日志    | changelog              |
| 部署指南    | deployment guide       |
| 快速开始指南  | quick start guide      |
| 性能报告    | performance report     |
| 安全分析文章  | security analysis      |

---

# Quality Assurance Checklist

Before considering the translation complete, verify that:

* Every heading is preserved.
* Every blockquote remains a blockquote.
* Every bullet list is retained.
* Every Markdown table is preserved.
* Every checkmark (✅) is retained.
* Every product name remains untranslated.
* Every version number is unchanged.
* Every filesystem name is unchanged.
* Every latency and memory figure is unchanged.
* Every occurrence of "Verification Result: ✅ Confirmed" is rendered consistently.
* No factual additions, omissions, or reinterpretations have been introduced.
* The English reads naturally while remaining faithful to the original structure, nuance, and evidential tone.
