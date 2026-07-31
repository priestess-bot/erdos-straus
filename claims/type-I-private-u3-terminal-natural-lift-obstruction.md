---
kind: claim
claim_id: type-I-private-u3-terminal-natural-lift-obstruction
title: 私有 u=3 偶终端的自然提升障碍与 q-free 因子三分
statement: 设私有 u=3 族满足 p=2ht+3、K=qh、E=4h^2、n=2h(t-3)。自然 E 标记源的标记分母为 q(t-3)/2，其非空性等价于原 R 状态已有 Type I，且它不含平凡偶源解 (n/2,n,n)。保留平凡解两个坐标的提升恒不可能；把 E 用作保留 n/2 或 n 的一分母提升因子也分别被模 4 与模 3 障碍排除。其余标准一分母提升精确归约为 h^2、(n/2)^2 或 n^2 上的三个 q-free 除子筛，而不是由偶终端自动给出的递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-private-u3-carrier-dyadic-terminal-q-free-type-II
  - type-I-normal-source-state-realization
  - type-I-normal-reverse-two-tail-selector
  - one-denominator-lift-factor-criterion
  - middle-coordinate-lift-certificate-equivalence
  - even-predecessor-two-denominator-lift-obstruction
topics:
  - type-I
  - type-II
  - private-carrier
  - dyadic-terminal
  - even-source
  - solution-lift
  - obstruction
  - divisor-residues
  - support-exit
  - proof-program
sources:
  - claim: type-I-private-u3-carrier-dyadic-terminal-q-free-type-II
    role: private-family-and-terminal-identities
  - claim: type-I-normal-source-state-realization
    role: marked-Type-I-source-realization
  - claim: one-denominator-lift-factor-criterion
    role: exact-one-coordinate-lift-factorization
  - claim: even-predecessor-two-denominator-lift-obstruction
    role: two-coordinate-standard-source-obstruction
visibility: public
last_checked: '2026-07-31'
---

# 私有 \(u=3\) 偶终端的自然提升障碍与 \(q\)-free 因子三分

## 设置

沿用[私有载体族](type-I-private-u3-carrier-dyadic-terminal-q-free-type-II.md)的条件：
\(p,q\) 为素数，\(p\equiv1\pmod {24}\)，且

\[
p=t+3+3tR,
\qquad tR+1=2q,
\qquad t>6,
\qquad R>3.
\tag{1}
\]

令

\[
h=\frac{3R+1}{2}.
\]

已有结论给出

\[
t\equiv7\pmod {12},
\quad R\equiv3\pmod8,
\quad h\equiv5\pmod {12},
\quad p=2ht+3,
\quad K=qh,
\tag{2}
\]

以及广义二进终端

\[
E=4h^2,
\qquad n=2h(t-3),
\qquad p-n=6h+3.
\tag{3}
\]

本卡回答一个更窄的问题：式 (3) 是否能从偶数 \(n\) 的平凡解自动提升回 \(p\)。

## 自然 \(E\) 标记纤维没有新增目标

记 \(c=p-n=6h+3\)。由 \(2h=3R+1\) 直接计算得

\[
E-1=4h^2-1=cR,
\qquad
E\mid\frac{n^2}{4}.
\tag{4}
\]

所以 \((p,n,E)\) 满足 Type I 源状态实现判据的桥因子前提。自然源中的标记分母是

\[
\alpha=\frac{nK}{E}=\frac{q(t-3)}2.
\tag{5}
\]

而且

\[
\frac4n-\frac1\alpha
=\frac RK
=\frac4p-\frac1{pK}.
\tag{6}
\]

因此，若能把 \(R/K\) 分成两个正单位分数，就可保持这两个尾项并把
\(\alpha\) 替换为 \(pK\)。但二项因子分解和 Type I 源状态实现判据说明，这个标记纤维
非空当且仅当原 \((R,K)\) 状态已有 Type I 中心除子。结合私有族的目标消元式，条件恰为

\[
\boxed{
\exists d\mid h^2:\ d\equiv-1\pmod R
\quad\text{或}\quad
d\equiv-h\pmod R.}
\tag{7}
\]

故自然 \(E\) 桥只是同状态 Type I 的等价标记形式，不是 Type I 失败后的新出口。

它也不包含平凡偶源解。事实上，\(\alpha=n/2\) 会要求 \(q=2h\)，但

\[
q-2h=\frac{(t-6)R-1}{2}>0.
\]

而 \(\alpha=n\) 会要求 \(q=4h\)，进而给出 \((t-12)R=3\)，与 \(R>3\) 矛盾。
所以不能以 \((n/2,n,n)\) 冒充式 (5) 的标记源。

## 平凡偶源的两坐标保留全部失败

距离 \(p-n=6h+3\) 是正奇数。因而
[邻近偶数源的两分母保留障碍](even-predecessor-two-denominator-lift-obstruction.md)
可直接应用：从

\[
\frac4n=\frac1{n/2}+\frac1n+\frac1n
\tag{8}
\]

保留任意两个分母、只替换第三个分母，都不可能得到 \(4/p\) 的正整数解。

这排除了最直接的全域提升；剩下的标准源尝试只能保留一个坐标并同时重组另外两个。

## 保留 \(x=n/2\) 时 \(E\) 必失败

置

\[
x=\frac n2=h(t-3),
\qquad
\mu=4x-p=2h(t-6)-3.
\tag{9}
\]

由 \(t\ge7\) 可知 \(p/4<x<p/2\)，且 \(\mu>1\)。一分母提升因子式使用
\(S=px\)；因 \(t-3\) 被 4 整除，\(E=4h^2\mid x^2\mid S^2\)。若试图取
\(e=E\)，必要同余为

\[
\mu\mid px+E.
\tag{10}
\]

模 \(\mu\) 有 \(p\equiv4x\)。又因 \(h\not\equiv0\pmod3\)，

\[
\gcd(\mu,4h^2)=1.
\]

故 (10) 等价于

\[
\mu\mid(t-3)^2+1.
\tag{11}
\]

但 \(h,t-6\) 都是奇数，所以 \(\mu\equiv3\pmod4\)。任意
\(3\pmod4\) 的正整数都有一个 \(3\pmod4\) 素因子出现奇数次，因而 \(-1\) 不可能是
模 \(\mu\) 的平方；(11) 矛盾。这里 \(0<x<p\)、\(p\) 为素数，故
\((p,x)=1\)，进而

\[
\gcd(\mu,S)=\gcd(4x-p,px)=1.
\]

因此 \((e,S^2/e)\) 的两个因子同余互相等价，互补因子 \(S^2/E\) 也失败。

## 保留 \(n\) 时 \(E\) 也必失败

再置

\[
\Delta=4n-p=6h(t-4)-3.
\tag{12}
\]

此时一分母提升使用 \(S=np\)。若取 \(e=E\)，必要条件为

\[
\Delta\mid np+E.
\tag{13}
\]

模 \(\Delta\) 有 \(p\equiv4n\)，而
\(\gcd(\Delta,4h^2)=1\)，所以 (13) 等价于

\[
\Delta\mid4(t-3)^2+1.
\tag{14}
\]

式 (12) 表明 \(3\mid\Delta\)，但 \(t-3\equiv1\pmod3\)，故 (14) 右端模 3 为
2，矛盾。又因 \(0<n<p\)、\(p\) 为素数，

\[
\gcd(\Delta,S)=\gcd(4n-p,np)=1.
\]

因子配对同余再次等价，所以互补因子 \(S^2/E\) 同样失败。

## 剩余的三个 \(q\)-free 因子筛

上述否定不排除其它因子。它把平凡偶源的一分母提升精确压缩成以下三类有限筛。

第一类是原状态 Type I，即式 (7) 的两个 \(h^2\) 剩余类。

第二类保留 \(x=n/2\)。因 \(p\) 为素数且 \((p,x)=1\)，把一分母因子唯一写成
\(e=p^a d\)、\(d\mid x^2\)。排序条件 \(e\le px\) 排除 \(a=2\)，于是只剩

\[
\boxed{
\begin{array}{ll}
a=0:& d\mid x^2,\quad \mu\mid4x^2+d,\\
a=1:& d\mid x^2,\quad d\le x,\quad \mu\mid x+d.
\end{array}}
\tag{15}
\]

它们分别正是缺口 \(\mu=4x-p\) 的 Type I 与 Type II 证书条件；按中间分母等价定理，
源 \(n\) 没有降低这项直接目标难度。

第三类保留 \(n\)。同样写 \(e=p^a f\)、\(f\mid n^2\)，排序排除 \(a=2\)，并得到

\[
\boxed{
\begin{array}{ll}
a=0:& f\mid n^2,\quad \Delta\mid4n^2+f,\\
a=1:& f\mid n^2,\quad f\le n,\quad \Delta\mid n+f.
\end{array}}
\tag{16}
\]

最后，\(R\ge11\) 给出 \(q>5t\)，而 \((q,h)=1\)。故

\[
q\nmid h(t-3),
\qquad q\nmid x,
\qquad q\nmid n.
\tag{17}
\]

式 (7)、(15)、(16) 的全部搜索空间都不含私有素数 \(q\)。这与任意 Type II 首分母
满足 \(q\nmid x\) 的先前定理一致：真正可能的出口必须读取 \(h,t-3\) 的因子结构，
而不是继续消耗增长的私有载体。

## 结论边界

本卡没有证明三个 \(q\)-free 因子筛之一必命中。它证明的是更严格的研究排除：

1. 广义二进终端本身不等于可提升递降；
2. 自然 \(E\) 标记纤维在 Type I miss 时为空；
3. 平凡偶源不能通过两坐标保留启动；
4. 终端因子 \(E\) 不能通过两个最自然的一分母通道循环使用。

因此下一步应研究式 (15)--(16) 的联合剩余类容量，或构造改变全部三个分母的新标记状态；
继续尝试直接复用 \(E=4h^2\) 不会闭合该族。
