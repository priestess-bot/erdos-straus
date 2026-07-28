---
kind: claim
claim_id: type-I-linear-full-spectrum-bgt1-200
title: 首次一般 B 大于一压力层的二百点完整线性谱审计
statement: 在冻结的1964个普通Type II p减一遗漏点中，选出首次线性一般B证书的B大于一层200点；对每点完整枚举所有线性源模数R及K平方除子目标谱。共检查10292个R和18074个定向源状态，得到1018个目标命中、2752个有限指数F障碍和6522个子群/角色G障碍；200点均至少有一个命中，且每点同时保留F和G状态。3209个R满足端点t=3 mod4的二残数注入条件，其中351个还满足-1属于<2 mod R>而排除G；这351个中129个已命中、222个为F、没有G。该结果是分层有限审计，不是全称选择器。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- linear-source
- general-b
- full-spectrum
- subgroup-character
- finite-exponent
- two-adic-support
- pressure-set
- mixed-selector
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-and-terminal-bridge-context
visibility: public
last_checked: '2026-07-29'
---

# 首次一般 (B>1) 压力层的二百点完整线性谱审计

## 审计对象

已有的 1,964 个普通 Type II (p-1) 双尾遗漏点中，先按既有“首次命中”程序选出首次线性一般
(B>1) 的 200 个核心素数。这个选择只定义压力层，不宣称随机性，也不改变线性源的完整枚举：
对每个选中素数，重新穷尽

\[
p=a+s+asR,
\qquad s\text{ 奇数},
\qquad R\equiv3\pmod4,
\]

的全部状态，并按 (R) 去重。

对每个状态令

\[
K=\frac{pR+1}{4},
\qquad
\mathcal C_R(K)=\{dK^{-1}:d\mid K^2\}.
\]

程序穷尽所有 (d\mid K^2) 且 (d\equiv-K\pmod R)。无命中时，再用 (K) 的素因子支撑子群
精确判定 (-1) 是否属于该子群，从而区分有限指数 (F) 障碍和子群/角色 (G) 障碍。

## 结果

| 项目 | 数量 |
| --- | ---: |
| 选中核心素数 | 200 |
| 完整线性模数 (R) | 10,292 |
| 定向线性源状态 | 18,074 |
| 目标谱命中 | 1,018 |
| 有限指数 (F) 障碍 | 2,752 |
| 子群/角色 (G) 障碍 | 6,522 |

每一个选中素数都有至少一个命中，单点命中数在 1--11 之间；同时每一个点都保留至少一个
(F) 状态和一个 (G) 状态。因此，首次 (B>1) 证书不是孤立现象，但“某个状态从 (G)
逃逸”仍不能推出终端命中，(F) 是独立的第二层障碍。

在 10,292 个去重后的 (R) 中，有 3,209 个满足某个端点 (t\equiv3\pmod4)，因而可用
半块二残数注入引理。只有其中 351 个进一步满足
(-1\in\langle2\bmod R\rangle)，可以用该引理排除 (G)；这 351 个状态的分类为：

| 二残数且循环子群逃逸状态 | 数量 |
| --- | ---: |
| 已命中 | 129 |
| (F) 障碍 | 222 |
| (G) 障碍 | 0 |

这验证了二残数引理在完整谱上的作用边界：它确实排除了 (G)，但不能消除有限指数盒缺口。

## 数学含义与边界

该审计把路线复核中“首次命中数据不能代表完整障碍谱”的问题，推进到一个可复现的分层压力层。
它支持两个工作假设：

1. 目标命中应按状态谱的多重性研究，而不是只记录第一张证书；
2. 证明全称混合选择器必须同时处理 (G\to F) 的角色逃逸和 (F\to\) 命中的有限指数增长。

它不证明所有核心素数都有命中，也不证明这 200 点之外的谱具有相同分布；尤其不能把
(1018/(1018+2752+6522)) 解读为密度或概率。

## 复现

```bash
python3 reproductions/type_i_linear_full_spectrum_bgt1_200.py \
  --output reproductions/type-i-linear-full-spectrum-bgt1-200-results.json
python3 -m unittest tests/test_type_i_linear_full_spectrum_bgt1_200.py -q
```

结果文件：[type-i-linear-full-spectrum-bgt1-200-results.json](../reproductions/type-i-linear-full-spectrum-bgt1-200-results.json)
