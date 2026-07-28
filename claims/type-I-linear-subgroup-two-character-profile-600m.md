---
kind: claim
claim_id: type-I-linear-subgroup-two-character-profile-600m
title: 七点线性 G 型状态的二残数与角色阶剖面
statement: 对七个完整线性压力谱的190个子群角色G型状态，43个状态的某个有向源端点t=3 mod 4，故半块机制把2注入其K的生成子群；33个状态满足-1属于<2 mod R>，但两类状态不相交，否则将与G型矛盾。最小分离二幂角色阶在189个状态为2，仅(p,R)=(536944489,8859)需要4。因此二次互反拉回覆盖本有限压力集中的绝大多数G型障碍，但高阶角色不能忽略，二残数机制本身也不足以关闭任一已存G型状态。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- linear-source
- general-b
- subgroup-character
- quadratic-character
- higher-order-character
- residue-class
- obstruction
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 七点线性 G 型状态的二残数与角色阶剖面

## 审计对象

输入为[七点全线性目标谱的角色与有限指数混合剖面](type-I-linear-general-b-obstruction-mixture-profile-600m.md)
冻结的全部 190 个 G 型状态：

\[
-1\notin\mathcal H_R(K),
\qquad K=\frac{pR+1}{4}. \tag{1}
\]

对每个状态，完整重建该 \(R\) 的有向线性源，检查是否存在端点
\(t\equiv3\pmod4\)。这样的端点给出

\[
\frac{tR+1}{2}\equiv2^{-1}\pmod R,
\qquad 2\in\mathcal H_R(K). \tag{2}
\]

另直接计算 \(2\) 在 \((\mathbb Z/R\mathbb Z)^\times\) 中的阶，以判断
\(-1\in\langle2\bmod R\rangle\)。最后从单位群离散对数格证书计算能分离 \(-1\) 的最小
二幂角色阶。

## 结果

总计结果为

| 项目 | 状态数 |
| --- | ---: |
| G 型状态 | 190 |
| 具有半块二残数注入 | 43 |
| 满足 (-1inlangle2angle) | 33 |
| 同时满足这两项 | 0 |
| 有二阶分离角色 | 189 |
| 需要四阶分离角色 | 1 |

前两类不相交不是偶然的计数现象。若某个 G 型状态同时有 (2) 且
\(-1\in\langle2\rangle\)，则 \(-1\in\mathcal H_R(K)\)，与 (1) 矛盾。
这也验证了[半块二残数逃逸](type-I-linear-half-block-two-residue-escape.md)的精确适用边界：
它是排除候选 G 型的必要结构，而不是让已存在 G 型自动命中的工具。

唯一最小分离二幂角色阶为四的状态是

\[
p=536{,}944{,}489,
\qquad R=8{,}859,
\qquad K=1{,}189{,}197{,}807{,}013. \tag{3}
\]

它没有 \(t\equiv3\pmod4\) 的有向端点，且 \(-1\notin\langle2\bmod R\rangle\)。

## 含义与边界

189/190 的二阶覆盖支持把[二次互反拉回](type-I-linear-quadratic-obstruction-reciprocity-pullback.md)
作为 G 型跨源比较的主坐标：绝大多数障碍可以转述为 \(K\) 的实际素因子在
\(\mathbb Q(\sqrt{pR/m})\) 中的分裂条件。

但 (3) 说明纯二次路线不能成为无例外的证明。另一方面，43 个半块注入状态仍全部是 G 型，
说明只知道 \(2\in\mathcal H_R(K)\) 也不够。全称选择器仍需跨不同 \(R\) 比较二次分裂条件，
并为高阶角色状态提供替代源或更高阶互反机制。

## 复现

~~~bash
python3 reproductions/type_i_linear_subgroup_two_character_profile_600m.py
python3 -m unittest tests.test_type_i_linear_subgroup_two_character_profile_600m -v
~~~
