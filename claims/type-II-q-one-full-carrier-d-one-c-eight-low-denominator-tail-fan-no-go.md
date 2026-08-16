---
kind: claim
claim_id: type-II-q-one-full-carrier-d-one-c-eight-low-denominator-tail-fan-no-go
title: q=1 容量八低分母 p-1 Type II 尾扇无路
statement: >-
  设 p=48s+1 是核心素数且 s>=86。对 r=2,3,4,6，令
  m_r=(p-1)/r-1；这些都是合法的 3 mod 4 Bradford gap，若有 Type II
  证书便会以 ordinary two-tail deflation 严格降到分母 r+1=3,4,5,7。事实上
  这四个 gap 都没有 Type II 证书。若 s 为偶数，额外的 q_star-bearing gap
  m_8=(p-1)/8-1=6s-1 也没有 Type II 证书；它原本会降到分母 9。证明只用
  Type II 除子条件压出的有限常数整除表；r=6 的唯一 s>=86 必要候选是
  s=99，但 48*99+1=7*679 不是素数。故这些低分母 p-1 尾不能关闭 c=8
  的 terminal-first 残余，但结论不排除其它 gap、Type I 证书、atomic split
  或一般递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - gap-residue-reachability
  - type-II-q-one-full-carrier-d-one-c-eight-second-full-excess-carry-obstruction
topics:
  - type-II
  - q-one
  - full-carrier
  - c-eight
  - terminal-first
  - p-minus-one-tail
  - strict-descent
  - low-denominator
  - proof-boundary
sources:
  - claim: gap-residue-reachability
    role: exact-Type-II-gap-divisor-criterion
  - claim: type-II-q-one-full-carrier-d-one-c-eight-second-full-excess-carry-obstruction
    role: c-eight-high-R-and-terminal-first-context
  - reproduction: reproductions/type_ii_q_one_full_carrier_d_one_c_eight_low_denominator_tail_fan_no_go.py
    role: finite-constant-divisor-receipt
visibility: public
last_checked: '2026-08-17'
---

# q=1 容量八低分母 \(p-1\) Type II 尾扇无路

## 1. 自然尾扇及其本应给出的严格下降

容量八 high-\(R\) normal form 的根素数满足

\[
p=48s+1,\qquad s\ge86.
\tag{1}
\]

对 \(r\in\{2,3,4,6\}\)，定义 \(p-1\) 索引的 gap

\[
m_r=\frac{p-1}{r}-1=\frac{48s}{r}-1,
\qquad
x_r=\frac{p+m_r}{4}.
\tag{2}
\]

每个 \(m_r\equiv3\pmod4\)，且 \(3\le m_r\le p-2\)。若它有 ordinary
Type II certificate，则 \(m_r+1\mid p-1\)，两条 \(p\)-divisible tail 可同时
deflate，所得分母是

\[
n_r=\frac{p+m_r}{m_r+1}=r+1<p.
\tag{3}
\]

所以这四个 gap 分别会把根直接送到已经可解的

\[
n_r\in\{3,4,5,7\}.
\tag{4}
\]

若 \(s\) 为偶数，写 \(s=2t\)。还有与实际 \(q_\star=103\) rough 因子同形的

\[
m_8=\frac{p-1}{8}-1=6s-1=12t-1,
\qquad
x_8=\frac{p+m_8}{4}=27t,
\tag{5}
\]

它也满足 \(m_8\equiv3\pmod4\)，且若有 Type II certificate 则会严格降到

\[
n_8=\frac{p+m_8}{m_8+1}=9.
\tag{6}
\]

这里研究的是这些非常具体的 terminal-first 候选，而不是所有 \(p-1\) tail。

## 2. 统一的必要除子条件

固定一个合法 gap \(m\) 和 \(x=(p+m)/4\)。Type II certificate 必须含有

\[
d\mid x^2,\qquad 1\le d\le x,\qquad m\mid x+d.
\tag{7}
\]

在 (1) 的低分母尾扇中，\(x+d\) 的大小只有一到两个可能的 \(m\)-倍数。因此
(7) 会强制一个显式线性 \(d\)，再把 \(d\mid x^2\) 化为固定常数整除。这一步只使用
[固定 gap 的精确除子残数判据](gap-residue-reachability.md)中的 Type II 必要条件；
若必要条件已矛盾，当然不会有 certificate。

## 3. \(r=2,3,4\) 的常数矛盾

### \(r=2\): 本应降到 \(3\)

此时

\[
m_2=24s-1,\qquad x_2=18s.
\tag{8}
\]

因为 \(0<x_2+d<2m_2\)，(7) 强制

\[
d=m_2-x_2=6s-1.
\tag{9}
\]

由 \(d\mid324s^2\) 和 \(6s\equiv1\pmod d\)，得到

\[
d\mid324.
\tag{10}
\]

但 \(d\equiv-1\pmod6\)，与 \(d\mid324=2^2 3^4\) 合并只可能 \(d=1\)，
这与 \(s\ge86\) 矛盾。

### \(r=3\): 本应降到 \(4\)

这里

\[
m_3=16s-1,\qquad x_3=16s=m_3+1.
\tag{11}
\]

由于 \(m_3<x_3+d<3m_3\)，只能有

\[
d=2m_3-x_3=16s-2=2(8s-1).
\tag{12}
\]

从 \(d\mid256s^2\) 得

\[
8s-1\mid128s^2.
\tag{13}
\]

而 \((8s-1,s)=1\)，故 \(8s-1\mid128\)。左侧为大于 \(1\) 的奇数，右侧
只有二因子，矛盾。

### \(r=4\): 本应降到 \(5\)

此时

\[
m_4=12s-1,\qquad x_4=15s.
\tag{14}
\]

条件 \(m_4<x_4+d<3m_4\) 强制

\[
d=2m_4-x_4=9s-2.
\tag{15}
\]

若 \(d\mid225s^2\)，则由 \(9s\equiv2\pmod d\) 有

\[
d\mid900.
\tag{16}
\]

又 \(d\equiv1\pmod3\)，所以 \(d\mid100\)；再由 \(d\equiv7\pmod9\)，在
\(100=2^2 5^2\) 的有限除子表中唯一可能是 \(d=25\)。这给出 \(s=3\)，
与 \(s\ge86\) 矛盾。

## 4. \(r=6\): 唯一高参数必要候选不是素数

现在

\[
m_6=8s-1,\qquad x_6=14s.
\tag{17}
\]

对 \(s\ge86\)，有

\[
m_6<x_6+d<4m_6,
\]

故 (7) 只允许两种情形：

\[
d=2m_6-x_6=2(s-1),
\tag{18}
\]

或

\[
d=3m_6-x_6=10s-3.
\tag{19}
\]

在 (18) 中，\(d\mid196s^2\) 给出

\[
s-1\mid98.
\tag{20}
\]

当 \(s\ge86\) 时唯一可能为 \(s=99\)，但

\[
48\cdot99+1=4753=7\cdot679
\tag{21}
\]

不是素数。

在 (19) 中，由 \(10s\equiv3\pmod d\) 得

\[
d\mid1764=2^2 3^2 7^2.
\tag{22}
\]

再加上 \(d\equiv7\pmod {10}\)，该常数的除子中只有

\[
d\in\{7,147\},
\tag{23}
\]

对应 \(s\in\{1,15\}\)，均不在 (1) 的范围。因此 \(r=6\) 也没有可用 certificate。

## 5. 偶 \(s\) 的 \(q_\star\)-bearing \(r=8\) gap

令 \(s=2t\)，其中 \(t\ge43\)。由 (5) 和 \(1\le d\le x_8\)，有

\[
2m_8<x_8+d<5m_8,
\]

所以只剩

\[
d=3m_8-x_8=9t-3=3(3t-1),
\tag{24}
\]

或

\[
d=4m_8-x_8=21t-4.
\tag{25}
\]

若 (24) 整除 \(x_8^2=729t^2\)，则 \(3t-1\) 与 \(3t\) 互素，因而

\[
3t-1\mid3^6.
\tag{26}
\]

左侧为 \(2\pmod3\)，而 \(3^6\) 的正除子要么为 \(1\)，要么可被 \(3\) 整除，
矛盾。

若 (25) 整除 \(729t^2\)，利用 \(21t\equiv4\pmod d\) 得

\[
d\mid16\cdot729=11664.
\tag{27}
\]

又 \(d\equiv2\pmod3\)，故 \(d\mid16\)；但 \(d=21t-4\ge899\)，矛盾。

因此真实 103 rough 域的偶 \(s\) 子域不能把 \(N=6s-1\) 直接当成一个
Type II gap 来获得分母 \(9\) 的尾递降。

## 6. 结论与边界

对容量八的 \(s\ge86\) 域，下列最自然的 \(p-1\)-indexed Type II tail terminal 均已
排除：

\[
\begin{array}{c|c|c}
r&m_r&\text{本应得到的 source denominator}\\ \hline
2&24s-1&3\\
3&16s-1&4\\
4&12s-1&5\\
6&8s-1&7\\
8\ (s\ \text{even})&6s-1&9
\end{array}
\tag{28}
\]

这是一张 terminal-first **no-go**，不是对 Erdős--Straus 猜想的负结论，也没有缩小
其余 direct Type I/II gap、Type I normal-form bridge、\(V\)-side atomic split 或
全局势的可行性。它的实际作用是：不能把“从 \(p-1\) 取最小几个自然因子，下降到一个
已知小分母”当成 \(c=8\) 残余的未支付出口。

聚焦复核：

~~~bash
python3 reproductions/type_ii_q_one_full_carrier_d_one_c_eight_low_denominator_tail_fan_no_go.py --verify
~~~

复现器只重放 (2)--(27) 中的固定常数因子表与 \(s=99\) 的合数控制；不扫描素数、
gap、分母或历史 target。
