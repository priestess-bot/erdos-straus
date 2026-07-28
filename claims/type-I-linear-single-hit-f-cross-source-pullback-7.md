---
kind: claim
claim_id: type-I-linear-single-hit-f-cross-source-pullback-7
title: 七个单命中压力点的 F 型跨源拉回与指数预算边界
statement: 在完整线性谱中仅有一个一般B目标命中的七个压力点上，共有71个有限指数F状态和110个有向源。对每个状态按同一核心素数的全部264个线性模数定义共享层 S_R=gcd(K_R,lcm_{R'!=R}|R-R'|/4)，共享层拉回在7个方向产生34个原始残类，其中5个方向的16个残类进入仿射块生成子群，但进入实际有限指数盒的仍为0。16个子群可见残类的最小额外指数预算分布为delta=1:6、2:4、6:2、7:2、8:2；因此该扩展样本仍只显示预算缺口，不提供统一转移或递降。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- linear-source
- general-b
- finite-exponent
- cross-modulus
- shared-layer
- centered-spectrum
- exponent-budget
- single-hit
- negative-boundary
- mixed-selector
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-29'
---

# 七个单命中压力点的 F 型跨源拉回与指数预算边界

## 审计对象

从 200 点完整谱中选出一般 \(B\) 目标恰有一个命中的七个核心素数

\[
67369, 878089, 13782409, 26034649, 57399241, 152498329, 283319689.
\]

对每个核心素数的全部线性模数集合 \(\mathcal R_p\)，令

\[
K_R=\frac{pR+1}{4},
J_R=\operatorname{lcm}_{R'\in\mathcal R_p,\,R'\ne R}
\frac{|R-R'|}{4},
S_R=\gcd(K_R,J_R).
\]

对有向源分解 \(K_R=\gamma L\)，计算

\[
D_R(X)=\mathcal A_R(X)\mathcal A_R(X)^{-1},
T_\gamma=\{-x^{-1}:x\in D_R(\gamma)\},
H_L=\langle D_R(L)\rangle.
\]

分别记录

\[
P_{\rm raw}=D_R(S_R)\cap T_\gamma,
\quad
P_{\rm sub}=P_{\rm raw}\cap H_L,
\quad
P_{\rm finite}=P_{\rm raw}\cap D_R(L).
\]

这里的 \(\mathcal R_p\) 是该核心素数的完整线性谱，而不是只保留 \(F\) 状态的模数；这样共享层
确实包含同一素数的命中、G 和 F 源之间可能共享的指数层。

## 结果

七个谱共含 264 个不同 \(R\)，其中 71 个 \(F\) 状态、110 个有向 \(F\) 源。对每个核心素数的
全部源模数逐项验证跨模数恒等式，共复核 5542 个模数对。

| 层级 | 非空有向源数 | 残类总数 |
| --- | ---: | ---: |
| \(P_{\rm raw}\) | 7 | 34 |
| \(P_{\rm sub}\) | 5 | 16 |
| \(P_{\rm finite}\) | 0 | 0 |

按核心素数分组：

| \(p\) | \(F\) 状态数 | 有向源数 | 原始方向 | 子群方向 |
| ---: | ---: | ---: | ---: | ---: |
| 67,369 | 5 | 6 | 0 | 0 |
| 878,089 | 2 | 4 | 0 | 0 |
| 13,782,409 | 9 | 17 | 1 | 1 |
| 26,034,649 | 6 | 8 | 2 | 1 |
| 57,399,241 | 24 | 36 | 3 | 2 |
| 152,498,329 | 12 | 18 | 0 | 0 |
| 283,319,689 | 13 | 21 | 1 | 1 |

所有 110 个方向均满足

\[
D_R(L)\cap T_\gamma=\varnothing,
\]

而且所有 16 个 \(P_{\rm sub}\) 残类仍在有限指数盒之外。

## 指数预算缺口

对每个 \(t\in P_{\rm sub}\)，令 \(\delta(t)\) 为用仿射块素因子表示 \(t\) 所需的最小
额外指数预算，即最小的非负整数满足

\[
|z_q|\le v_q(L)+\delta(t)
\]

的指数向量存在。精确分布为

\[
\begin{array}{c|ccccc}
\delta&1&2&6&7&8\\ \hline
\text{残类数}&6&4&2&2&2
\end{array}
\]

最小缺口为 1，最大缺口为 8。新出现的单命中谱边界包括

\[
(p,R,a,s)=(13782409,335,2165,19),
\]

其中两个子群可见类的缺口均为 2；其余非空方向给出缺口
\(1,6,7,8\)，与先前四核心审计的缺口集合一致。

## 结论边界

这次扩展没有发现“共享层进入 \(H_L\) 后必然只需一个坐标补偿”的规律。它反而把已有
负边界推广到七个真正的单命中压力点：共享层有时能产生目标拉回，甚至把目标拉回送进
仿射块生成子群，但有限指数盒仍完全不相交。

因此当前尚无可用的“预算转移”或“严格递降”引理。后续若要推进混合终端选择器，必须
额外证明以下至少一项：

1. 缺口 \(\delta(t)\) 能沿某条合法源重选边严格下降；
2. 某个缺口类可以转化为新的 \(R'\) 或普通 Type II 证书；
3. 共享层与私有层的联合积集在另一状态中强制产生反足点。

本页是七个有限完整谱上的负边界，不是全称反例，也不证明 Erdős--Straus 猜想。

## 复现

```bash
python3 reproductions/type_i_linear_single_hit_f_cross_source_pullback_7.py
python3 -m unittest tests/test_type_i_linear_single_hit_f_cross_source_pullback_7.py -q
```

结果文件：
[type-i-linear-single-hit-f-cross-source-pullback-7-results.json](../reproductions/type-i-linear-single-hit-f-cross-source-pullback-7-results.json)

规范记录摘要为
`3b1795047f79a13cac70abddaa5b4ed2930fc17de1af18f3ebbd76017a1676a8`。
