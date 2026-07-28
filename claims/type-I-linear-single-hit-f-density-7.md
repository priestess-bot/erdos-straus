---
kind: claim
claim_id: type-I-linear-single-hit-f-density-7
title: 七个单命中压力点的 F 型反足点密度缺口
statement: 在完整线性谱仅有一个一般B目标命中的七个压力点上，共有71个有限指数F状态；逐项计算单边除子谱A_R(K)与素因子支撑子群H_R(K)，全部满足严格不等式2|A_R(K)|<|H_R(K)|，没有半密度等号状态。最小缺口为6，出现在(p,R)=(67369,27)；最大缺口为130762696，出现在(p,R)=(283319689,141659843)。该结果排除仅靠单状态半密度统一闭合的路线，但不构成跨状态定理。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- linear-source
- general-b
- finite-exponent
- antipodal-density
- single-hit
- pressure-set
- mixed-selector
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-29'
---

# 七个单命中压力点的 (F) 型反足点密度缺口

## 审计对象

取完整线性谱中目标平方除子恰有一个命中的七个压力点：

\[
67369,\ 878089,\ 13782409,\ 26034649,\ 57399241,\ 152498329,\ 283319689.
\]

对每个有限指数状态

\[
-1\in\mathcal H_R(K)\setminus\mathcal C_R(K),
\qquad K=\frac{pR+1}{4},
\]

直接构造

\[
\mathcal A_R(K)=\{d\bmod R:d\mid K\},
\]

并从单位群对数格证书恢复 (|\mathcal H_R(K)|)。程序还独立验证

\[
\mathcal A_R(K)\cap-\mathcal A_R(K)=\varnothing,
\qquad
2|\mathcal A_R(K)|\le|\mathcal H_R(K)|.
\]

## 结果

| (p) | F 状态数 | 最小缺口 | 最大缺口 |
| ---: | ---: | ---: | ---: |
| 67,369 | 5 | 6 | 30,968 |
| 878,089 | 2 | 146 | 424 |
| 13,782,409 | 9 | 210 | 462,354 |
| 26,034,649 | 6 | 60 | 11,833,864 |
| 57,399,241 | 24 | 34 | 25,875,264 |
| 152,498,329 | 12 | 30 | 180,476 |
| 283,319,689 | 13 | 100 | 130,762,696 |
| **合计** | **71** | **6** | **130,762,696** |

71 个状态全部是严格 F 型：没有一个达到

\[
2|\mathcal A_R(K)|=|\mathcal H_R(K)|.
\]

最接近半密度的是

\[
(p,R)=(67369,27),
\qquad
|\mathcal H_R(K)|-2|\mathcal A_R(K)|=6.
\]

最大缺口为

\[
(p,R)=(283319689,141659843),
\qquad
|\mathcal H_R(K)|-2|\mathcal A_R(K)|=130762696.
\]

## 研究含义

该压力层没有显示“F 状态靠近半密度边界”的统一规律：同一层同时出现极小和极大的缺口。
因此，证明混合终端选择器不能只证明某个固定 (R) 的半密度充分条件，也不能假定指数盒
会自然增长到半群的一半。

更具体的下一步是把

\[
\mathcal A_R(K)=\mathcal A_R(S_R)\mathcal A_R(P_R)
\]

的共享层 (S_R) 和剩余层 (P_R) 放回这些 F 状态，研究多个 (R) 之间的私有层是否必然
使某一个状态跨过反足点；这比继续扩大单状态密度统计更接近全称证明。

## 边界与复现

本页只覆盖七个单命中压力点的 71 个 F 状态，不证明其它素数或其它状态的统一性质。

```bash
python3 reproductions/type_i_linear_single_hit_f_density_7.py \
  --output reproductions/type-i-linear-single-hit-f-density-7-results.json
python3 -m unittest tests/test_type_i_linear_single_hit_f_density_7.py -q
```

结果文件：[type-i-linear-single-hit-f-density-7-results.json](../reproductions/type-i-linear-single-hit-f-density-7-results.json)
