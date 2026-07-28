---
kind: claim
claim_id: type-I-linear-adversarial-core-f-cross-source-pullback-audit-600m
title: 对抗核心 F 状态的跨源共享层拉回审计
statement: 对四个真实对抗核心的45个有限指数F状态和69个有向源，令 S_R=gcd(K_R,lcm_{R'!=R}|R-R'|/4)，并比较 D_R(S_R) 与块目标拉回 T_gamma={-x^(-1):x属于D_R(gamma)}。原始共享层拉回只出现在6个方向共32个残类，进入仿射块子群 H_L 的只有4个方向共14个残类，而进入实际有限指数盒 D_R(L) 的为0；因此共享层不能在该有限全集中直接完成缺失目标对齐，但仅凭共享层的子群可见性也不足以证明普适选择器。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- linear-source
- cross-modulus
- shared-layer
- finite-exponent
- centered-spectrum
- block-alignment
- adversarial-core
- negative-boundary
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-29'
---

# 对抗核心 F 状态的跨源共享层拉回审计

## 审计对象

固定核心素数 (p)，令 (mathcal R_p) 是当前完整线性源谱中出现的全部不同模数，并写

\[
K_R=\frac{pR+1}{4}.
\]

由跨模数公因子刚性，任意两个不同源模数满足

\[
\gcd(K_R,K_{R'})
=\gcd\!\left(K_R,\frac{|R-R'|}{4}\right).
\]

因此定义

\[
J_R=\operatorname{lcm}_{R'\in\mathcal R_p,\,R'\ne R}
\frac{|R-R'|}{4},
\qquad
S_R=\gcd(K_R,J_R).
\]

(S_R) 恰好是 (K_R) 中可能与同一核心素数的其它线性源共享的最高指数层。对一个
有向线性源分解 (K_R=\gamma L)，定义

\[
D_R(X)=\mathcal A_R(X)\mathcal A_R(X)^{-1},
\qquad
T_\gamma=\{-x^{-1}:x\in D_R(\gamma)\},
\qquad
H_L=\langle D_R(L)\rangle.
\]

我们区分三种逐层拉回：

\[
P_{\rm raw}=D_R(S_R)\cap T_\gamma,
\]

\[
P_{\rm sub}=D_R(S_R)\cap T_\gamma\cap H_L,
\]

\[
P_{\rm finite}=D_R(S_R)\cap T_\gamma\cap D_R(L).
\]

(P_{\rm raw}) 表示共享层在单位群中产生了所需类，(P_{\rm sub}) 表示这些类至少落在
仿射块所生成的子群内，而 (P_{\rm finite}) 才是真正能由有限指数盒直接完成块对齐的类。

## 完整有限结果

输入是四个真实对抗核心的完整 F 状态集合：

\[
(p,R)\in\{878089,26034649,57399241,283319689\},
\]

共 45 个 F 型模数状态、69 个有向源。对全部 \(3882\) 个跨模数源对逐项复核上面的
\(\gcd\) 恒等式，并对每个有向源精确枚举共享层的中心化差集。

| 层级 | 非空有向源数 | 残类总数 |
| --- | ---: | ---: |
| (P_{\rm raw}) | 6 | 32 |
| (P_{\rm sub}) | 4 | 14 |
| (P_{\rm finite}) | 0 | 0 |

所有 69 个方向的完整块审计仍满足

\[
D_R(L)\cap T_\gamma=\varnothing,
\]

与 F 型状态的目标缺失一致。四个能进入 (H_L) 但仍不在 (D_R(L)) 中的潜在边界为：

| (p) | (R) | ((a,s)) | (P_{\rm raw}) | (P_{\rm sub}) |
| ---: | ---: | ---: | --- | --- |
| 26,034,649 | 375 | \((73,951)\) | \(\{86,266\}\) | \(\{86,266\}\) |
| 57,399,241 | 155 | \((1755,211)\) | \(\{23,27,37,44,67,74,81,88,111,118,128,132\}\) | \(\{128,132\}\) |
| 57,399,241 | 567 | \((101055,1)\) | \(\{248,496,551,559\}\) | \(\{248,496,551,559\}\) |
| 283,319,689 | 1247 | \((93,2443)\) | \(\{237,275,762,905,984,1229\}\) | 同左 |

例如 \(p=26{,}034{,}649,R=375,(a,s)=(73,951)\) 的共享层为

\[
S_R=232696=2^3\cdot17\cdot29\cdot59,
\]

它在 \(H_L\) 中产生两个目标拉回类 86 和 266，但这两个类都不属于实际
\(D_R(L)\)，所以没有形成 \(-1\) 的有限指数见证。

## 指数预算缺口

对每个 \(t\in P_{\rm sub}\)，令 \(\delta(t)\) 是表示

\[
t=\prod_{q\mid L}q^{z_q}\pmod R
\]

时所需的最小额外指数预算：即要求

\[
|z_q|\le v_q(L)+\delta(t)
\]

的最小非负整数 \(\delta(t)\)。因为 \(t\notin D_R(L)\)，所有这些 \(\delta(t)\) 都严格为正。本次 14 个
潜在残类的精确分布为

\[
\begin{array}{c|ccccc}
\delta & 1&2&6&7&8\\ \hline
\text{残类数}&6&2&2&2&2
\end{array}
\]

最小预算缺口为 1，最大为 8。例如：

- `p=26034649, R=375` 的类 86 需要仿射因子 `(2,29,59)` 上的指数向量
  `(2,1,-2)`，比原盒多出一个单位；
- `p=57399241, R=155` 的类 128 只有一条仿射素因子，最小表示为指数 `-7`，比原盒
  多出 6 个单位；
- `p=283319689, R=1247` 的类 762 的一个最小表示为 `(4,8,-9)`，预算缺口为 8。

因此“共享层把类送入 \(H_L\)”与“共享层只需补一个坐标”之间存在可量化的指数距离。
后续若要证明跨源选择器，至少需要一个能控制该距离的指数转移或递降引理。

## 结论与边界

这张审计排除了一个具体的跨源加强方案：

> 只要某个 F 状态的共享指数层在仿射块子群 \(H_L\) 中产生目标拉回类，就能完成
> Type I 目标。

四个潜在行直接反驳了这个说法。共享层确实可能把目标拉回送入 (H_L)，但仍然缺少
有限指数盒中的实际坐标；因此下一步必须控制指数预算、块标签或跨模数之间的共同坐标，
不能只做子群层面的角色判断。

这是一项四个核心上的完整有限负边界，不是全称选择器的反例，也不证明 Erdős--Straus
猜想。它把跨源路线的剩余问题精确缩小为：能否利用共享层的**指数分配**控制上述预算
缺口，强制某个方向的 \(P_{\rm finite}\) 非空，或者把该失败状态递降到更小实例。

## 复现

```bash
python3 reproductions/type_i_linear_adversarial_core_f_cross_source_pullback_audit_600m.py
python3 -m unittest tests.test_type_i_linear_adversarial_core_f_cross_source_pullback_audit_600m -q
```

结果文件：
[`type-i-linear-adversarial-core-f-cross-source-pullback-audit-600m-results.json`](../reproductions/type-i-linear-adversarial-core-f-cross-source-pullback-audit-600m-results.json)

规范记录摘要为
`3fb5de592e621f446e1a227e820b18ad0b12528683e18e8ad1cfc0c7bc9ab845`。
