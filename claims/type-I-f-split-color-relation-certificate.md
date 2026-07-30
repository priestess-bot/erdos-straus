---
kind: claim
claim_id: type-I-f-split-color-relation-certificate
title: 分色 F 状态的关系格多角色盒空缺证书
statement: 对冻结完整线性谱中 291 个无法同色承载两个活跃方向的 F 状态，完整关系格的贪心独立对偶基约束均可把有限指数盒排空；每个状态因此获得一份可复查的多角色关系格证书。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- F-state
- relation-lattice
- finite-fourier
- bounded-certificate
- split-color
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-target-context
visibility: public
last_checked: '2026-07-30'
depends_on:
  - type-I-f-split-color-phase-projection-boundary
  - type-I-f-relation-lattice-certificate-reconstruction
---

# 分色 F 状态的关系格多角色盒空缺证书

## 主张

对分色容量分支中 291 个状态，完整重建关系格 (Lambda) 和目标仿射原像后，在有限
指数盒内逐点验证，并从 (Lambda^*) 的基字符中贪心选择能最大幅度削减剩余盒的约束。
对每个状态，所选独立关系约束的交集最终为空，因此得到明确的 F 型盒空缺证书。该
证书不是单一 Fourier 角色，而是一组相互配合的格对偶角色。

## 口径

这是有限状态的证书重建，不声称贪心长度最小，也不把多角色证书自动解释成跨状态容量
需求。它把 251 个非空二维相位投影状态与 40 个空投影状态统一放回完整关系格框架，
下一步仍需研究如何从这些多角色的支撑、相位和载体颜色中提取可比较的全局需求。

## 复现

```text
python3 reproductions/type_i_f_split_color_relation_certificate.py
```

结果文件：

```text
reproductions/type-i-f-split-color-relation-certificate-results.json
```
