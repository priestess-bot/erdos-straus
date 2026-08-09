---
kind: claim
claim_id: type-I-overflow-high-capacity-small-d-residual-cone
title: 高容量小 d overflow 的精确容量壳/余因子残余锥
statement: >-
  设 p≡1 (mod 24) 的 verified overflow 满足 pn=4Md+1、2B_p≤M、d^2<p，且携带
  c=(p−1)/4≤A≤B_p、A|M 以及 source/path、Sol(p)、E1--E5 合同。令
  M=kp+r、P=rd、b=M/A，并令 Π_p(A)=floor(B_p/A)、
  Θ_p(A)=floor(B_p/Π_p(A))+1。该 Θ_p(A) 是严格降低外层秩的最小有界载体，
  且 A<Θ_p(A)≤2A。若 P≥Θ_p(A)，则 L=P 给出完整 fixed-s 严格外层秩递降；
  若 P<Θ_p(A)，则余因子 dispatcher 依次给出 dg<p 的因子转移、d<b<p 的交换，或
  b 的某个壳除子 t（Θ_p(A)≤t≤B_p）的 fixed-n 商模 p 折叠。因 d^2<p，所有
  未分流状态必满足 P<Θ_p(A)、b>p、每个 q|b 有 dq≥p，并且 b 在闭区间
  [Θ_p(A),B_p] 没有除子；特别地 b<Θ_p(A) 或 b>B_p，前一类还强制
  A>(p−1)/2。Π_p(A)=1 时 Θ_p(A)=B_p+1，明确记录为无 bounded-support
  reset 的顶层容量壳。该二分严格收紧旧的 2A 充分门，但不声称余项已经有
  Type I/II 终端或全局递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-small-d-dual-saturation-composition
  - type-I-overflow-fixed-s-bounded-divisor-saturation
  - type-I-overflow-cofactor-factor-exchange-carrier-descent
  - type-I-overflow-fixed-n-quotient-fold-descent
topics:
  - type-I
  - overflow
  - high-capacity
  - small-d
  - fixed-s
  - cofactor
  - floor-shell
  - outer-rank
  - residual-cone
  - well-founded-descent
  - proof-boundary
sources:
  - claim: type-I-overflow-fixed-s-bounded-divisor-saturation
    role: fixed-s-product-saturation-edge
  - claim: type-I-overflow-cofactor-factor-exchange-carrier-descent
    role: factor-transfer-and-exchange-edges
  - claim: type-I-overflow-fixed-n-quotient-fold-descent
    role: high-cofactor-fold-edge
  - reproduction: reproductions/type_i_overflow_high_capacity_small_d_residual_cone.py
    role: focused-route-and-residual-receipts
visibility: public
last_checked: '2026-08-09'
---

# 高容量小 \(d\) overflow 的精确容量壳/余因子残余锥

## 设置

令

\[
B_p=\frac{(p-1)^2}{4},
\qquad
c=\frac{p-1}{4}.
\]

考虑一个已有 source/path/node 回执的 verified overflow

\[
pn=4Md+1,
\qquad 2B_p\le M,
\qquad 1\le d<p,
\qquad d^2<p,
\tag{1}
\]

并令 charged support 满足

\[
c\le A\le B_p,
\qquad A\mid M.
\tag{2}
\]

写

\[
M=kp+r,
\qquad 1\le r<p,
\qquad P=rd,
\qquad b=\frac MA.
\tag{3}
\]

模 \(p\) 的行列式恒等式给出

\[
s:=\frac{4rd+1}{p}\in\mathbb Z_{>0},
\qquad 1\le s\le4d-1,
\qquad 4P+1=sp.
\tag{4}
\]

## 精确外层势壳

记

\[
\Pi_p(A):=\left\lfloor\frac{B_p}{A}\right\rfloor,
\qquad
\Theta_p(A):=\left\lfloor\frac{B_p}{\Pi_p(A)}\right\rfloor+1.
\tag{5}
\]

这是严格 outer-rank 下降的精确整数阈值：对任何整数 \(L\) 都有

\[
A<L\le B_p,
\qquad
\Pi_p(L)<\Pi_p(A)
\quad\Longleftrightarrow\quad
\Theta_p(A)\le L\le B_p.
\tag{6}
\]

事实上，令 \(u=\Pi_p(A)\)。不等式
\(\lfloor B_p/L\rfloor<u\) 等价于 \(B_p/L<u\)，也即

\[
L>\frac{B_p}{u}.
\]

对整数 \(L\) 这恰为 \(L\ge\lfloor B_p/u\rfloor+1=\Theta_p(A)\)。又

\[
B_p\ge Au,
\qquad
\frac{B_p}{A}<u+1\le2u,
\]

所以

\[
A<\Theta_p(A)\le2A.
\tag{7}
\]

若 \(\Pi_p(A)=1\)，则 \(A>B_p/2\) 且

\[
\Theta_p(A)=B_p+1;
\tag{8}
\]

因而任何 \(L\le B_p\) 都不能支付一次 strict outer-rank reset。若
\(\Pi_p(A)\ge2\)，则 \(\Theta_p(A)\le B_p\)，故它是真正落在容量盒内的首个
可支付载体。

## 精确 fixed-\(s\) 饱和出口

由 \(d^2<p\) 有 \(d<\sqrt p\)，而 \(p\ge73\) 时

\[
4\sqrt p<p-1.
\]

因而

\[
4P=4rd<4(p-1)\sqrt p<(p-1)^2=4B_p.
\tag{9}
\]

另一方面，\(s\ge1\) 和 (4) 给出 \(P\ge c\)。所以

\[
c\le P<B_p.
\tag{10}
\]

若 \(P\ge\Theta_p(A)\)，取 \(L=P\)。由 (6)，此时
\(A<L\le B_p\)、\(\Pi_p(P)<\Pi_p(A)\)，且 \(L\mid rd\)。再有

\[
s<4P,
\qquad
K_L=P(p-1)>0,
\qquad
R_L=4P-s>0,
\tag{11}
\]

\[
pR_L+1=4K_L.
\tag{12}
\]

既有 fixed-\(s\) 有界除子合同遂给出完整 E1--E5 的外层秩递降；\(R_L<p\) 时
登记为 marked absorb，\(R_L>p\) 时仍是 overflow 后继。此处不要求 \(A\mid P\)：
若支撑不被包含，(6) 直接支付 support reset。

## 余因子 dispatcher

下面假设 \(P<\Theta_p(A)\)。由 \(M>B_p\ge A\) 有 \(b>1\)。余因子因子转移集合为

\[
\mathcal G(M,d;A)=\{g:g\mid b,\ 1<g,\ dg<p\}.
\tag{13}
\]

若该集合非空，取其中规范的最大 \(g\)，则

\[
(M,d;A)\longmapsto(M/g,dg;A)
\tag{14}
\]

由已有因子转移合同给出完整 E1--E5，并严格降低
\(\Lambda=(\lfloor B_p/A\rfloor,M)\)。特别地，当 \(b\le d\) 时可取
\(g=\operatorname{spf}(b)\)，因为

\[
d\,\operatorname{spf}(b)\le d^2<p.
\tag{15}
\]

若 \(\mathcal G\) 为空但 \(d<b<p\)，余因子交换

\[
(M,d;A)=(Ab,d;A)\longmapsto(Ad,b;A)
\tag{16}
\]

同样给出完整 E1--E5 和相同势的严格下降。

定义余因子精确容量壳除子集

\[
\mathcal D_b^{\Theta}(A):=
\{t:t\mid b,\ \Theta_p(A)\le t\le B_p\}.
\tag{17}
\]

若 \(\mathcal D_b^{\Theta}(A)\ne\varnothing\)，令 \(t_*\) 为其中最大的除子，并取
\(L=t_*\)。由于 \(t_*\mid b\mid M\mid Md\)，有

\[
A<L\le B_p,
\qquad
\left\lfloor\frac{B_p}{L}\right\rfloor
<\left\lfloor\frac{B_p}{A}\right\rfloor.
\tag{18}
\]

固定-\(n\) 商模 \(p\) 折叠合同把 \(Md/L\) 写成

\[
\frac{Md}{L}=ph+\delta,
\qquad h\ge0,
\qquad1\le\delta<p,
\tag{19}
\]

并给出

\[
M_T=L,\qquad d_T=\delta,\qquad n_T=n-4Lh,\qquad A_T=L
\tag{20}
\]

的完整 E1--E5 后继。这里 \(L\) 不要求等于 \(b\)，也不要求是素数；它可以是
\(b\) 的任意壳内复合除子。又不需要另加 \(4L>n\)，因为长商由折叠恒等式处理。

## 残余锥

若上述三类路由都没有被选中，因 (15) 可排除 \(b\le d\)。又
\(b\ne p\)，否则 \(p\mid M\) 与 (1) 矛盾；若 \(b<p\)，则 \(d<b<p\) 会触发
(16) 的交换。因此必有

\[
P<\Theta_p(A),
\qquad b>p,
\qquad \mathcal D_b^{\Theta}(A)=\varnothing,
\qquad d q\ge p\quad(q\mid b\text{ 为素数}).
\tag{21}
\]

因为 \(b\) 本身是其除子，\(\mathcal D_b^{\Theta}(A)=\varnothing\) 必然推出

\[
b<\Theta_p(A)\qquad\text{或}\qquad b>B_p.
\tag{22}
\]

这是一个穷尽的算术二分。由 (7)，第一种分支还给出高支撑必要条件：若
\(b<\Theta_p(A)\)，则

\[
2B_p\le M=Ab<2A^2,
\qquad
A>\sqrt{B_p}=\frac{p-1}{2}.
\tag{23}
\]

因此真正未由本菜单处理的高容量小 \(d\) 状态只落在：

1. \(P<\Theta_p(A)\)、\(p<b<\Theta_p(A)\)、\(A>(p-1)/2\) 的
   prethreshold 高支撑余项；或
2. \(P<\Theta_p(A)\)、\(b>B_p\)，且 \(b\) 的全部除子都避开
   \([\Theta_p(A),B_p]\) 的精确超容量壳缺口。

当 \(\Pi_p(A)=1\) 时，(8) 表明第一类允许 \(b\le B_p\)，但这不是一个遗漏的
bounded-divisor：outer rank 已经等于一，任何 \(L\le B_p\) 都没有 E5 支付。
两类都只表示当前 Type I 载体选择器的精确边界，不表示没有其它 Type I/II 表示，
也不表示 Erdos--Straus 反例。尤其不能把第二类错误简化为“\(b\) 必为素数”：
下面给出一个复合余因子的精确壳缺口控制。下一步应对这两个锥分别接入
generalized \(2^j\)、q-adic capacity 或直接 Type II 终端，而不是把 (21) 当作负定理。

## 聚焦回执

算术回执脚本覆盖以下十一种状态：

\[
\begin{array}{c|c}
\text{回执}&\text{分类}\\ \hline
(73,1129,5151,4,51)&P\ge2A\text{ 的 fixed-}s\\
(73,28361,129397,4,83)&\Theta_p(A)=87\le P=164<2A=166\text{ 的精确 fixed-}s\\
(73,145,2646,1,49)&\text{因子转移}\\
(73,337,3075,2,75)&\text{余因子交换}\\
(73,161,2938,1,26)&b\text{ 本身的 fixed-}n\text{ 折叠}\\
(73,27505,501966,1,18)&t=353\mid b=79\cdot353\text{ 的壳除子折叠}\\
(73,317,5785,1,65)&\Theta_p(A)=69\le b=89<2A\text{ 的壳除子折叠}\\
(73,23381,426703,1,53)&t=97\mid b=83\cdot97,\ \Theta_p(A)=55\text{ 的壳除子折叠}\\
(73,645,11771,1,149)&p<b=79<\Theta_p(A)=163\text{ 的 prethreshold 残余}\\
(73,1585,28926,1,18)&\text{素数超容量残余}\\
(73,37617,686510,1,110)&b=79^2\text{ 的复合精确壳缺口残余}
\end{array}
\]

其中五元组顺序为 \((p,n,M,d,A)\)。这些控制只验证算术分类、规范图表和势支付。
第 2、7、8 条分别说明：精确阈值能关闭 \(P<2A\) 的 fixed-\(s\) 行，以及
旧 \(2A\) 门遗漏的单一和复合余因子折叠。第 11 条的
\(\operatorname{Div}(b)=\{1,79,6241\}\) 与
\([\Theta_p(A),B_{73}]=[118,1296]\) 不相交，严格否定“精确壳余项余因子必为素数”的
错误缩约。第 9 条保留真实的 \(b<\Theta_p(A)\) 边界。所有控制都不提供新的
source/path 可达性，也不替代全局 F/G 选择器。

复现命令：

```bash
python3 reproductions/type_i_overflow_high_capacity_small_d_residual_cone.py --verify
```
