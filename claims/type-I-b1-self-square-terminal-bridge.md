---
kind: claim
claim_id: type-I-b1-self-square-terminal-bridge
title: B 等于一正规形的自平方终端桥
statement: 设核心素数 p 具有 B=1 的 Type I 正规形 mR=4C+1、p=4AC-m、H=AR-1、K=CH。若 H 为偶数且 H>4C，则 E=16C^2 是一个偶终端因子，给出 n=(4K-E)/R=4C(H-4C)/R 的 Type I 源解。更精确地，该源处于上半区当且仅当 H>8C。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- b1
- terminal-bridge
- self-square
- even-source
- upper-half
- normal-form
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# \(B=1\) 正规形的自平方终端桥

设 \(p\equiv1\pmod {24}\) 是核心素数，并且已有一个 \(B=1\) 的 Type I 正规形。为避免
把本引理误读成正规形的存在定理，以下将其参数显式写出：

\[
mR=4C+1,\qquad p=4AC-m,\qquad H=AR-1,\qquad K=CH, \tag{1}
\]

其中 \(m,A,C\) 为正整数，\(m\equiv3\pmod4\)。于是 \(R\equiv3\pmod4\)，特别 \(R\ge3\)，并有

\[
4K=pR+1,
\qquad
\frac4p=\frac1{AC}+\frac1{ACH}+\frac1{pK}. \tag{2}
\]

**定理。** 若 \(H\) 为偶数且 \(H>4C\)，令

\[
E=16C^2,
\qquad
j=\frac{H-4C}{R},
\qquad
n=4Cj=\frac{4K-E}{R}. \tag{3}
\]

则 \(E\) 是满足

\[
E\mid4K^2,\qquad E\equiv1\pmod R,\qquad E\le4K-2R \tag{4}
\]

的偶因子；\(n\) 是 \(2\le n<p\) 的偶数，且

\[
\frac4n=\frac1{jH/4}+\frac1{AC}+\frac1{ACH}. \tag{5}
\]

因此 (3) 是一张从该目标正规形反向得到的 Type I 偶源终端证书。它只断言“已有的 \(B=1\)
正规形满足一个可检验条件时”可以闭合；并不选择每个核心素数的正规形。

**证明。** 由 \(mR=4C+1\) 及 \(m\equiv3\pmod4\)，知 \(R\equiv3\pmod4\)。又

\[
4CH=4C(AR-1)=pR+(mR-4C)=pR+1,
\]

给出 (2)。条件 \(H>4C\) 使 \(j\) 为正整数；而 \(H\) 与 \(4C\) 都是偶数、\(R\) 是奇数，故
\(j\) 也是偶数。于是 \(n=4Cj\) 为偶数，且 \(jH/4\) 为整数。

由 \(4C\equiv-1\pmod R\)，有

\[
E=16C^2\equiv1\pmod R. \tag{6}
\]

同时 \(K=CH\) 且 \(H\) 为偶数，故

\[
\frac{4K^2}{E}=\frac{H^2}{4}\in\mathbb Z. \tag{7}
\]

再由 \(H-4C=Rj\)，得到 \(4K-E=4C(H-4C)=4CRj\)，故 (3) 的最后等式成立。
因为 \(j\ge2\)，有 \(4K-E\ge8CR\ge2R\)，这给出 (4) 的上界；\(E>1\) 还给出 \(n<p\)。
最后，使用 \(H+1=AR\) 与 \(H-4C=Rj\)，有

\[
\frac1{jH/4}+\frac1{AC}+\frac1{ACH}
=\frac4{jH}+\frac{H+1}{ACH}
=\frac4{jH}+\frac R{CH}
=\frac{4C+Rj}{CjH}
=\frac1{Cj}=\frac4n,
\]

即得 (5)。

## 上半区的精确界

直接相减可得

\[
2n-(p+1)=\frac{4C(H-8C)+1-R}{R}. \tag{8}
\]

这里 \(H\not=8C\)：模 \(R\) 时左边两项分别为 \(-1\) 与 \(-2\)。若 \(H>8C\)，
分子至少为 \(4C+1-R=(m-1)R>0\)；若 \(H<8C\)，分子至多为 \(-4C+1-R<0\)。所以

\[
n\ge\frac{p+1}{2}\quad\Longleftrightarrow\quad H>8C. \tag{9}
\]

可复算的有限压力剖面见 [自平方终端桥剖面](type-I-b1-self-square-terminal-bridge-profile-600m.md)。
最小示例为 \(p=337\)、\((A,C,H,R,K)=(17,5,118,7,590)\)：此时
\((E,n,jH/4)=(400,280,413)\)。

~~~bash
python3 -m unittest tests.test_type_i_b1_self_square_terminal_bridge_profile_600m -q
~~~
