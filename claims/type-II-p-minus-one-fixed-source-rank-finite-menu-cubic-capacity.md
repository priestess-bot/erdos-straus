---
kind: claim
claim_id: type-II-p-minus-one-fixed-source-rank-finite-menu-cubic-capacity
title: p-1 因子 Type II 递降的固定源秩有限菜单与三次容量界
statement: >-
  设 p=4qr+1 为素数，m=4q-1，x=q(r+1)，于是 m+1|p-1，兼容的
  Type II 双尾递降源为 n=r+1。固定 r 后，全部这类 Type II 除子证书与有限
  (k,d) 菜单一一对应：ceil((r+2)/4)<=k<=K_r=floor((2r+1)/3)，
  d|k^2，a=4k-r-1>0，a|d+k，q=(d+k)/a，且 d<q(r+1)。
  因而 q<=K_r(K_r+1)、p-1<=4rK_r(K_r+1)，菜单容量至多为
  sum_{k=ceil((r+2)/4)}^{K_r} tau(k^2)。特别地，任何把源秩 n 限制在
  固定上界内的 p-1 因子 Type II 策略都只能覆盖有界多个 p；对核心素数，
  r<=5 全空，r=6 恰有 p=73、97 两个素数目标。这是全称容量 no-go，
  不是有限范围覆盖外推。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - short-certificate-equivalence
  - type-II-two-tail-deflation-descent
  - type-II-linear-square-gcd-allocation-core-gap-cutoff
topics:
  - type-II
  - p-minus-one
  - two-tail-descent
  - fixed-source-rank
  - finite-menu
  - exact-capacity
  - cubic-bound
  - bounded-rank-no-go
  - selector
sources:
  - claim: type-II-two-tail-deflation-descent
    role: exact-p-minus-one-compatible-two-tail-lift
  - claim: type-II-linear-square-gcd-allocation-core-gap-cutoff
    role: linear-square-divisor-bijection
  - reproduction: reproductions/type_ii_p_minus_one_fixed_source_rank_finite_menu.py
    role: symbolic-menu-and-small-rank-control-verifier
visibility: public
last_checked: '2026-08-11'
---

# \(p-1\) 因子 Type II 递降的固定源秩有限菜单与三次容量界

## 1. 定理

设

\[
p=4qr+1
\tag{1}
\]

为素数，其中 \(q,r\in\mathbb N\)。取与因子 \(4q\mid p-1\) 对应的缺口和
首分母

\[
m=4q-1,
\qquad
x=\frac{p+m}{4}=q(r+1).
\tag{2}
\]

因为 \(m+1=4q\mid p-1\)，任何该缺口的 Type II 证书都可沿两条
\(p\)-尾严格递降到

\[
n=\frac{p+m}{m+1}=r+1.
\tag{3}
\]

固定 \(r\)，定义

\[
k_-(r)=\left\lceil\frac{r+2}{4}\right\rceil,
\qquad
K_r=\left\lfloor\frac{2r+1}{3}\right\rfloor,
\qquad
a_{r,k}=4k-r-1.
\tag{4}
\]

再令 \(\mathcal M_r\) 为全部满足下列条件的正整数对 \((k,d)\)：

\[
\begin{aligned}
&k_-(r)\le k\le K_r,\\
&d\mid k^2,\\
&a_{r,k}>0,\qquad a_{r,k}\mid d+k,\\
&q_{r,k,d}:=\frac{d+k}{a_{r,k}}\in\mathbb N,\\
&d<q_{r,k,d}(r+1),\\
&p_{r,k,d}:=4q_{r,k,d}r+1\text{ 为素数}.
\end{aligned}
\tag{5}
\]

则有精确双射

\[
\boxed{
\begin{array}{c}
\text{源秩 }n=r+1\text{ 的全部 }p-1\text{ 因子 Type II 递降证书}\\
\longleftrightarrow
\mathcal M_r.
\end{array}}
\tag{6}
\]

正向中 \(k=(x+d)/m\)；反向中由 (5) 恢复
\[
q=q_{r,k,d},\quad p=p_{r,k,d},\quad m=4q-1,\quad x=q(r+1).
\]

因此固定源秩的原本无界 \(q\) 已被压成一个只枚举 \(k^2\) 除子的有限菜单。

## 2. 从 Type II 证书到线性平方坐标

Type II 的完整除子条件为

\[
d\mid x^2,
\qquad
0<d\le x,
\qquad
m\mid x+d.
\tag{7}
\]

定义

\[
k=\frac{x+d}{m}.
\tag{8}
\]

先注意 \(d=x\) 不可能：否则 \(m\mid2x\)，而 \((m,x)=1\)、\(m\ge3\)
会给出矛盾。因此 \(1\le d<x\)，并得到精确窗口

\[
x+1\le km<2x.
\tag{9}
\]

同时

\[
\begin{aligned}
d
&=km-x\\
&=k(4q-1)-q(r+1)\\
&=q(4k-r-1)-k\\
&=q\,a_{r,k}-k.
\end{aligned}
\tag{10}
\]

线性平方参数化给出

\[
\boxed{d\mid x^2\iff d\mid k^2.}
\tag{11}
\]

这里没有丢失互素条件。由 \(p\) 为素数可得 \((m,x)=1\)：若素数
\(\ell\mid(m,x)\)，则 \(4q\equiv1\pmod\ell\) 且
\(\ell\mid r+1\)，从而

\[
p=4qr+1\equiv r+1\equiv0\pmod\ell;
\]

但 \(\ell\le m<p\)，矛盾。若 \(d\mid x^2\)，则 \((m,d)=1\)，由
\(x\equiv km\pmod d\) 可约去 \(m^2\)，得到 \(d\mid k^2\)。反之若
\(d\mid k^2\)，同一同余立即给出 \(x^2\equiv k^2m^2\equiv0\pmod d\)。这就逐向证明
(11)，没有循环使用待证条件。

式 (10) 及 \(d>0\) 强制

\[
a_{r,k}=4k-r-1\ge1,
\]

即

\[
k\ge k_-(r).
\tag{12}
\]

另一方面，由 \(m=4q-1\ge3q\) 和 (9) 得

\[
3qk\le km<2q(r+1),
\]

所以 \(3k<2(r+1)\)，即

\[
k\le K_r.
\tag{13}
\]

最后，(10) 给出

\[
a_{r,k}\mid d+k,
\qquad
q=\frac{d+k}{a_{r,k}}.
\tag{14}
\]

这证明每张证书唯一进入 (5)。

## 3. 反向完备性

反过来，取任意 \((k,d)\in\mathcal M_r\)，并按 (5) 定义 \(q,p\)，再按 (2)
定义 \(m,x\)。由

\[
q(4k-r-1)=d+k
\]

立即得到

\[
km-x=d.
\tag{15}
\]

所以 \(m\mid x+d\)。又因 \(d\mid k^2\) 且

\[
x\equiv km\pmod d,
\]

有 \(d\mid x^2\)。条件 \(d<q(r+1)=x\) 给出 Type II 的大小门。
因此 (7) 全部成立，短证书恢复公式产生

\[
\frac4p
=
\frac1x
+\frac1{p(x+d)/m}
+\frac1{p(x+x^2/d)/m}.
\tag{16}
\]

把后两项的分母除以 \(p\)，便由 (3) 得到源解

\[
\frac4{r+1}
=
\frac1x
+\frac1{(x+d)/m}
+\frac1{(x+x^2/d)/m}.
\tag{17}
\]

式 (16)--(17) 也给出全域解提升：把源解的后两个分母同乘 \(p\) 即恢复目标。
故 (5) 没有混入只满足必要条件的伪候选，双射 (6) 得证。

## 4. 精确容量与三次界

对 \((k,d)\in\mathcal M_r\)，由 \(d\mid k^2\) 有

\[
1\le d\le k^2.
\]

结合 (14) 和 \(a_{r,k}\ge1\)，得到

\[
q=\frac{d+k}{a_{r,k}}
\le d+k
\le k^2+k
\le K_r(K_r+1).
\tag{18}
\]

因此

\[
\boxed{
q\le K_r(K_r+1),
\qquad
p-1=4qr\le4rK_r(K_r+1).}
\tag{19}
\]

在枚举层面，每个 \(k\) 只需检查 \(k^2\) 的正除子，所以带重数的候选容量满足

\[
\boxed{
|\mathcal M_r|
\le
\sum_{k=k_-(r)}^{K_r}\tau(k^2).}
\tag{20}
\]

式 (19) 还给出不含取整函数的三次界。由

\[
K_r\le\frac{2r+1}{3},
\qquad
K_r+1\le\frac{2r+4}{3},
\]

可得

\[
\boxed{
9(p-1)\le8r(2r+1)(r+2).}
\tag{21}
\]

若选择器只允许源秩

\[
n=r+1\le N,
\]

则右端至多为 \(8(N-1)(2N-1)(N+1)\)。所以

\[
\boxed{
p>1+\frac89(N-1)(2N-1)(N+1)
\Longrightarrow
\text{不存在源秩至多 }N\text{ 的这类 Type II 递降}.}
\tag{22}
\]

这是一条无样本的 bounded-source-rank no-go。任何企图用有限个固定较小源实例
覆盖全部核心素数的 \(p-1\) 因子 Type II 策略都会失败；源秩至少必须按三次容量
尺度随 \(p\) 增长。

## 5. 核心素数的小秩边界

若再要求

\[
p\equiv1\pmod {24},
\]

则 (1) 等价于 \(6\mid qr\)。对 \(1\le r\le6\) 完整运行 (5)，去重后的
\((q,p)\) 为

\[
\begin{array}{c|c|c}
r&[k_-(r),K_r]&\text{通过素数门的 }(q,p)\\ \hline
1&[1,1]&(1,5)\\
2&[1,1]&(2,17)\\
3&[2,2]&(1,13)\\
4&[2,3]&(1,17)\\
5&[2,3]&(2,41),(3,61)\\
6&[2,4]&(3,73),(4,97)
\end{array}
\tag{23}
\]

同一 \((q,p)\) 可能有多张不同 \((k,d)\) 证书；表中已按 \((q,p)\) 去重。
其中属于核心素数的只有

\[
\boxed{r=6,\qquad p=73,97.}
\tag{24}
\]

两张对应的正控制分别是

\[
\begin{aligned}
p=73:\quad &(q,m,x,k,d)=(3,11,21,2,1),\\
&\left(21,146,3066\right)\in\operatorname{Sol}(73),\\
&\left(21,2,42\right)\in\operatorname{Sol}(7);
\end{aligned}
\tag{25}
\]

\[
\begin{aligned}
p=97:\quad &(q,m,x,k,d)=(4,15,28,2,2),\\
&\left(28,194,2716\right)\in\operatorname{Sol}(97),\\
&\left(28,2,28\right)\in\operatorname{Sol}(7).
\end{aligned}
\tag{26}
\]

因此 \(r\le5\) 在核心域严格为空；\(r=6\) 的两个命中也已经是直接终端兼严格
双尾递降，不是新的未分类状态。

## 6. 对统一选择器的含义

本定理没有证明每个核心素数都存在 \(p-1\) 因子 Type II 递降。它完成的是另一项
必要的容量收紧：

1. 固定源秩不再是无界残数搜索，而是 (5) 的有限除子菜单；
2. 菜单非空时立即得到直接 Type II 终端和严格可提升递降；
3. 菜单为空时得到该源秩的完备 no-go，而不是搜索深度不足；
4. 任意全称策略必须允许 \(r\) 无界增长，并满足 (19)--(22) 的三次容量门。

所以后续不应继续寻找一个固定的小偶源作为全称出口。真正可能闭合的 Type II
\(p-1\) 选择器必须在 \(U=(p-1)/4\) 的因子分解 \(U=qr\) 上自适应选择增长的
\(r\)，再把 (5) 的局部除子菜单与 Fourier、格或加法组合容量证书耦合。

聚焦验证：

~~~bash
python3 reproductions/type_ii_p_minus_one_fixed_source_rank_finite_menu.py --verify
~~~

验证器核对恒等式、固定 \(r\) 菜单与原 Type II 条件的双向一致、式
(18)--(22) 以及 (23)--(26)；不运行历史范围扫描。
