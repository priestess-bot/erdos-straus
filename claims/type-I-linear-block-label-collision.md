---
kind: claim
claim_id: type-I-linear-block-label-collision
title: 线性源双因子块的坐标标签碰撞分解
statement: 对同一核心素数 p 的有限个线性源 p=a+s+asR，令 E=sR+1 与 F=aR+1。E 整除 p-s，F 整除 p-a；故任意两个坐标标签不同的块的公因子整除标签差。对有限标签集，逐块剥离其与所有其它标签差最小公倍数的公因子后，不同标签的私有层两两互素。七个完整线性压力谱的490个有向源、980个块和73,135个跨标签块对逐项重放该分解。这是跨源素因子碰撞的精确有限状态化，不保证任何目标平方除子命中。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- linear-source
- source-square
- factorization
- collision
- private-factors
- general-b
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 线性源双因子块的坐标标签碰撞分解

## 定理

固定核心素数 \(p\)，并取有限个线性源状态

\[
p=a_i+s_i+a_is_iR_i,
\qquad s_i\equiv1\pmod2,
\qquad R_i\equiv3\pmod4. \tag{1}
\]

定义两类带标签因子块

\[
E_i=s_iR_i+1,\quad \lambda(E_i)=s_i;
\qquad
F_i=a_iR_i+1,\quad \lambda(F_i)=a_i. \tag{2}
\]

它们满足

\[
E_i\mid p-s_i,\qquad F_i\mid p-a_i,
\qquad E_iF_i=pR_i+1=4K_i. \tag{3}
\]

因此，对任意两个标签不同的块 \(B,C\)，有

\[
\boxed{\gcd(B,C)\mid\lvert\lambda(B)-\lambda(C)\rvert.} \tag{4}
\]

令 \(\mathcal T\) 为全部标签的有限集合，且

\[
J_t=\operatorname{lcm}_{u\in\mathcal T,\ u\ne t}|t-u|,
\qquad
S_B=\gcd(B,J_{\lambda(B)}),\qquad P_B=B/S_B. \tag{5}
\]

则所有标签不同的块满足

\[
\boxed{\gcd(P_B,P_C)=1.} \tag{6}
\]

标签相同的块属于同一坐标纤维；(4)--(6) 对它们不作互素断言。

## 证明

若 \(B=E_i\)，则 \(B\mid p-s_i\)；若 \(B=F_i\)，则 \(B\mid p-a_i\)。所以
\(B\mid p-\lambda(B)\)。两个块的公因子因而同时整除

\[
p-\lambda(B),\qquad p-\lambda(C),
\]

从而整除二者之差，得到 (4)。

为证 (6)，设素数 \(q\) 同时整除 \(P_B,P_C\)，并令
\(e=\min(v_q(B),v_q(C))\)。由 (4)，

\[
e\le v_q(|\lambda(B)-\lambda(C)|)
\le v_q(J_{\lambda(B)}),\ v_q(J_{\lambda(C)}).
\]

因此 \(q^e\) 已在两个块的碰撞层中出现，不能同时留在两个私有层，矛盾。故 (6) 成立。

## 有限审计与边界

在七个既有完整线性压力谱

\[
p\in\{214729,878089,2210569,13782409,64214329,105295129,536944489\}
\]

中，程序完整恢复 490 个有向 \((a,s,R)\) 状态，构造 980 个 \(E,F\) 块，并逐项检查
全部 73,135 个跨标签块对。原始块公因子在 47,449 个对中非平凡；(4) 与 (6) 对每一对均
成立。因而该分解并不依赖“因子通常互素”的启发式。

该结果只把跨源共享因子压缩到有限的标签差碰撞层，尚不比较不同 \(R\) 的目标单位群，
也不推出 \(-1\) 命中中心化平方除子谱。它与[线性源模数之间的公因子刚性](type-I-linear-cross-modulus-gcd-rigidity.md)互补：后者控制完整 \(K_R\) 的共享指数，本页保留每个 \(K_R\) 内源块和仿射块的坐标来源。

可复现：

~~~bash
python3 reproductions/type_i_linear_block_label_collision.py
python3 -m unittest tests.test_type_i_linear_block_label_collision -v
~~~
