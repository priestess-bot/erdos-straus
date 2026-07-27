---
kind: claim
claim_id: type-I-normal-even-source-small-side-simplification
title: Type I 偶源桥的小侧普通除子对可免除大小预算
statement: 对核心素数的 Type I 正规形偶源桥，令 L=2K 并既约化 E/L=a/b。则 a=b 不可能。若 a<b，则 E<L<2L-2R，故桥的大小条件自动成立；此时 E 为偶数当且仅当 2 整除 a 或 b 整除 L/2。并且 a<b 当且仅当源 n=(2L-E)/R 满足 n≥(p+1)/2；因 p=1 mod24 且 n 为偶数，等价于 n≥(p+3)/2。反之，任意满足 E<L 的偶源桥都给出这样的 a<b 普通除子对。因此小侧终端选择只需强制互素除子 a,b 整除 L、a=2b 模 R 与这个显式偶性条件。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- normal-form
- terminal-bridge
- even-source
- divisor-pairs
- factorization
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-and-divisor-certificate-context
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization-context
visibility: public
last_checked: '2026-07-28'
---

# Type I 偶源桥的小侧普通除子对可免除大小预算

沿用[偶源桥的比二普通除子对等价](type-I-normal-even-source-ratio-two-pair.md)的记号。令

\[
L=2K,\qquad \frac EL=\frac ab,\qquad (a,b)=1,
\]

其中 \(a,b\mid L\) 且 \(a\equiv2b\pmod R\)。

## 定理

对任意核心素数 \(p\equiv1\pmod{24}\) 的 Type I 正规形偶源桥：

\[
a\ne b. \tag{1}
\]

若 \(a<b\)，则

\[
E=\frac{La}{b}<L<2L-2R, \tag{2}
\]

所以终端桥的大小条件 \(E\le2L-2R\) 自动成立。此外，在 \(a<b\) 的情形，

\[
2\mid E
\quad\Longleftrightarrow\quad
2\mid a\ \text{或}\ b\mid\frac L2. \tag{3}
\]

因此，小侧 \(a<b\) 中的桥存在性精确等价于

\[
a,b\mid L,\quad (a,b)=1,\quad a<b,\quad a\equiv2b\pmod R,
\quad\left(2\mid a\ \text{或}\ b\mid\frac L2\right). \tag{4}
\]

反过来，任何已有偶源桥若满足 \(E<L\)，其既约对必满足 \(a<b\)，因而落入 (4)。

令桥的源为

\[
n=\frac{2L-E}{R}.
\]

则小侧条件还有精确的源深度表达：

\[
a<b
\quad\Longleftrightarrow\quad
E<L
\quad\Longleftrightarrow\quad
n\ge\frac{p+1}{2}. \tag{5}
\]

因为 \(p\equiv1\pmod {24}\) 使 \((p+1)/2\) 为奇数，而偶桥强制 \(n\) 为偶数，(5)
在本问题中也等价于 \(n\ge(p+3)/2\)。

## 证明

由正规形关系 \(4K=pR+1\) 可知 \((L,R)=1\)。又

\[
L-2R=\frac{(p-4)R+1}{2}>0. \tag{6}
\]

若 \(a=b\)，互素性迫使 \(a=b=1\)。而 \(a\equiv2b\pmod R\) 则给出
\(1\equiv2\pmod R\)，这与正规形中 \(R\equiv3\pmod4\)、\(R\ge3\) 矛盾，故 (1) 成立。

若 \(a<b\)，则 \(E=La/b<L\)。式 (6) 给出 \(L<2L-2R\)，于是 (2) 成立。

由 \(a\ne b\) 及 \(E/L=a/b\)，有 \(a<b\) 当且仅当 \(E<L\)。另一方面

\[
E<L
\quad\Longleftrightarrow\quad
nR>L=\frac{pR+1}{2}
\quad\Longleftrightarrow\quad
n>\frac p2+\frac1{2R}.
\]

其中 \(p\) 为奇数而 \(R\ge3\)，故对整数 \(n\) 此条件恰为
\(n\ge(p+1)/2\)，证明 (5)。

最后，\((a,b)=1\) 意味着若 \(a\) 为偶数则 \(b\) 为奇数，因而 \(E=La/b\) 为偶数。
若 \(a\) 为奇数，则 \(E\) 为偶数当且仅当 \(L/b\) 为偶数，等价于
\(b\mid L/2\)。这证明 (3)。将 (2)--(3) 代回已有的比二普通除子对等价，便得 (4)。

## 含义

此引理没有选择 \(L,R\) 或 \(a,b\)，故不证明全称混合终端选择引理；它只将其中一类
终端状态的大小预算完全删除。后续逐点选择可先攻击 (4) 的普通除子残数问题，把无法找到
小侧对的状态单独保留为真正的大侧指数残余。

五亿完整普通双尾遗漏的终端记录中，
[小侧剖面](type-I-tail-reverse-even-source-small-side-profile-500m.md)显示 1,717 条里有 1,622 条
在同一 \((L,R)\) 状态下拥有小侧桥；剩余 95 条只是同一状态内的大侧残余。
它们在同一有限 Type I 盒的其它正规形中均有小侧替代，见
[替代正规形剖面](type-I-tail-reverse-even-source-small-side-alternative-profile-500m.md)。
五亿至六亿连续区间的 247 条普通双尾遗漏也全部可重选为小侧桥，见
[连续区间小侧剖面](type-I-mixed-terminal-dense-small-side-profile-600m.md)。
