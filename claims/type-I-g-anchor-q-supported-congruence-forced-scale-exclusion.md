---
kind: claim
claim_id: type-I-g-anchor-q-supported-congruence-forced-scale-exclusion
title: G-anchor 的同余强制尺度束不能全域覆盖 Q-supported 外部源
statement: >-
  对每个核心素数 p=1 (mod 24)，尺度 k=1,2,3,6 都由同余强制可选。存在无穷多个
  核心素数 p=1 (mod 14280)，且在这些四个尺度中的任一个上均不存在 Q-supported 的
  完整平方因子 external-source witness。因而仅依赖所有核心素数共同拥有的固定尺度束
  不能给出 G/Type I 全域出口；必须使用随 p 变化的尺度，或另一类短证书/递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-q-supported-power-external-source-ray
topics:
  - type-I
  - G-state
  - G-anchor
  - external-source
  - q-supported
  - scale-selection
  - capacity-map
  - counterexample-family
  - proof-boundary
sources:
  - claim: type-I-g-anchor-q-supported-power-external-source-ray
    role: exact-Q-supported-support-and-residue-classification
  - reproduction: reproductions/type_i_g_anchor_q_supported_congruence_forced_scale_exclusion.py
    role: fixed-four-scale-exclusion-control
visibility: public
last_checked: '2026-08-16'
---

# G-anchor 的同余强制尺度束不能全域覆盖 \(Q\)-supported 外部源

## 定理

令 \(p\equiv1\pmod{24}\) 为核心素数，并令

\[
H=\frac{p-1}{4}.
\]

于是 \(6\mid H\)，所以

\[
\mathcal U=\{1,2,3,6\}
\]

中的每个尺度都可取为 \(k\mid H\)。对每个这样的 \(k\)，按通常方式定义

\[
q=4k-1,\qquad
n=\frac{qp+1}{q+1},\qquad
M=kn,\qquad
Q=\frac{p-3}{2}.
\]

若进一步

\[
p\equiv1\pmod{14280}
\qquad
(14280=24\cdot5\cdot7\cdot17),
\tag{1}
\]

则对所有 \(k\in\mathcal U\)，不存在正整数 \(e\) 满足

\[
\operatorname{rad}(e)\mid Q,\qquad
e\mid M^2,\qquad
e\le M,\qquad
e\equiv-M\pmod q.
\tag{2}
\]

换言之，在四个由核心同余统一保证的尺度上，没有 \(Q\)-supported 的完整平方因子
external-source witness。由 Dirichlet 定理，(1) 中有无穷多个素数 \(p\)。

## 证明

type-I-g-anchor-q-supported-power-external-source-ray 的逆向完备性给出：若 (2) 成立，
则 \(e\) 的每个素因子都整除 \(6k-1\)，并且

\[
e\equiv-k\pmod{4k-1}.
\tag{3}
\]

若 \(e=1\)，则由 \(M\equiv k\pmod q\) 得 \(1\equiv-k\pmod q\)，但
\(-k\not\equiv1\pmod{4k-1}\)，故可只考虑 \(e>1\)。

对 \(k=1\)，唯一可能的支撑素数为 \(5\)。而 (1) 给出
\(Q\equiv-1\pmod5\)，所以 \(5\nmid Q\)，矛盾。

对 \(k=2\)，唯一可能的支撑素数为 \(11\)，但模 \(q=7\) 时

\[
\langle11\bmod7\rangle=\langle4\rangle=\{1,2,4\},
\qquad
-2\equiv5\pmod7.
\]

这与 (3) 矛盾。

对 \(k=3\)，唯一可能的支撑素数为 \(17\)。由 (1) 有
\(Q\equiv-1\pmod{17}\)，所以 \(17\nmid Q\)，矛盾。

最后，对 \(k=6\)，唯一可能的支撑素数来自 \(\{5,7\}\)。由 (1) 同时有

\[
Q\equiv-1\pmod5,
\qquad
Q\equiv-1\pmod7,
\]

故 \(Q\) 不含任何允许的支撑素数，仍然矛盾。这覆盖全部 \(\mathcal U\)。

因为 \(\gcd(1,14280)=1\)，Dirichlet 定理给出无穷多个
\(p\equiv1\pmod{14280}\) 的素数。\(\square\)

## 作用域与后果

这个定理排除的是由核心同余统一提供的四尺度束上的 **\(Q\)-supported 平方因子外源**
接口，不排除：

- 随 \(p\) 的附加因子变化的其他 \(k\mid H\)；
- 不使用 \(Q\)-supported 外源的 Type I 或 Type II 证书；
- 其他严格可提升的 source。

因此它不是猜想的反例，也不是对全体 Type I 终端的否定。它的严格结论是：一个全称
G/Type I 选择器若要依赖该外源机制，不能只在 \(\{1,2,3,6\}\) 中固定选择；必须给出
变量尺度的覆盖定理，或切换到别的证书/递降分支。

## 聚焦回执

~~~bash
python3 reproductions/type_i_g_anchor_q_supported_congruence_forced_scale_exclusion.py --verify
~~~

回执只检查固定核心素数 \(p=14281\equiv1\pmod{14280}\) 的四个尺度，重算
\((q,n,M,\gcd(Q,M))\) 与 \(k=2\) 的有限群排除；它不扫描素数、分母或历史状态。
