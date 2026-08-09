---
kind: claim
claim_id: type-I-overflow-high-capacity-small-d-residual-cone
title: 高容量小 d overflow 的固定-s/余因子残余锥
statement: >-
  设 p≡1 (mod 24) 的 verified overflow 满足 pn=4Md+1、2B_p≤M、d^2<p，且携带
  c=(p−1)/4≤A≤B_p、A|M 以及 source/path、Sol(p)、E1--E5 合同。令
  M=kp+r、P=rd、b=M/A。若 P≥2A，则 L=P 给出完整 fixed-s 严格外层秩递降；
  若 P<2A，则余因子 dispatcher 依次给出 dg<p 的因子转移、d<b<p 的交换，或
  b>p、b≤B_p、b≥2A 时的 fixed-n 商模 p 折叠。因 d^2<p，剩余状态必满足
  P<2A、b>p，且 b<2A 或 b>B_p；前一类还强制 A>(p−1)/2。该二分把
  M≥2B_p、A≥c 的小 d 边界压缩为高支撑或超容量余项，但不声称余项已经有
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

# 高容量小 \(d\) overflow 的固定-\(s\)/余因子残余锥

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

## 固定-\(s\) 饱和出口

由 \(d^2<p\) 有 \(d<\sqrt p\)，而 \(p\ge73\) 时

\[
4\sqrt p<p-1.
\]

因而

\[
4P=4rd<4(p-1)\sqrt p<(p-1)^2=4B_p.
\tag{5}
\]

另一方面，\(s\ge1\) 和 (4) 给出 \(P\ge c\)。所以

\[
c\le P<B_p.
\tag{6}
\]

若 \(P\ge2A\)，取 \(L=P\)。则 \(A<L\le B_p\)、\(L\mid rd\)，并且

\[
s<4P,
\qquad
K_L=P(p-1)>0,
\qquad
R_L=4P-s>0,
\tag{7}
\]

\[
pR_L+1=4K_L.
\tag{8}
\]

对 \(x=B_p/A\ge1\)，恒有

\[
\left\lfloor\frac{x}{2}\right\rfloor<\lfloor x\rfloor;
\]

因此 \(P\ge2A\) 蕴含

\[
\left\lfloor\frac{B_p}{P}\right\rfloor
<\left\lfloor\frac{B_p}{A}\right\rfloor.
\tag{9}
\]

既有 fixed-\(s\) 有界除子合同遂给出完整 E1--E5 的外层秩递降；\(R_L<p\) 时
登记为 marked absorb，\(R_L>p\) 时仍是 overflow 后继。此处不要求 \(A\mid P\)：
若支撑不被包含，(9) 直接支付 support reset。

## 余因子 dispatcher

下面假设 \(P<2A\)。由 \(M>B_p\ge A\) 有 \(b>1\)。余因子因子转移集合为

\[
\mathcal G(M,d;A)=\{g:g\mid b,\ 1<g,\ dg<p\}.
\tag{10}
\]

若该集合非空，取其中规范的最大 \(g\)，则

\[
(M,d;A)\longmapsto(M/g,dg;A)
\tag{11}
\]

由已有因子转移合同给出完整 E1--E5，并严格降低
\(\Lambda=(\lfloor B_p/A\rfloor,M)\)。特别地，当 \(b\le d\) 时可取
\(g=\operatorname{spf}(b)\)，因为

\[
d\,\operatorname{spf}(b)\le d^2<p.
\tag{12}
\]

若 \(\mathcal G\) 为空但 \(d<b<p\)，余因子交换

\[
(M,d;A)=(Ab,d;A)\longmapsto(Ad,b;A)
\tag{13}
\]

同样给出完整 E1--E5 和相同势的严格下降。

最后设 \(b>p\)。注意 \(b\ne p\)：否则 \(p\mid M\)，与
\(4Md+1\equiv-1\pmod p\) 矛盾。若再满足

\[
b\le B_p,
\qquad b\ge2A,
\tag{14}
\]

取 \(L=b\mid Md\)。有 \(A<L\le B_p\)，且

\[
\left\lfloor\frac{B_p}{b}\right\rfloor
<\left\lfloor\frac{B_p}{A}\right\rfloor.
\tag{15}
\]

固定-\(n\) 商模 \(p\) 折叠合同把 \(Md/b=Ad\) 写成 \(ph+\delta\)，其中
\(1\le\delta<p\)，并给出

\[
M_T=b,\qquad d_T=\delta,\qquad n_T=n-4bh,\qquad A_T=b.
\tag{16}
\]
\]

的完整 E1--E5 后继。这里不需要另加 \(4b>n\)；长商由折叠恒等式处理。

## 残余锥

若上述三类余因子路由都没有被选中，因 (12) 可排除 \(b\le d\)，因而必有

\[
P<2A,
\qquad b>p,
\qquad b>B_p\ \text{或}\ b<2A.
\tag{17}
\]

这是一个穷尽的算术二分。第二个分支还给出高支撑必要条件：若 \(b<2A\)，则

\[
2B_p\le M=Ab<2A^2,
\qquad
A>\sqrt{B_p}=\frac{p-1}{2}.
\tag{18}
\]

因此真正未由本菜单处理的高容量小 \(d\) 状态只落在：

1. \(P<2A\)、\(p<b<2A\)、\(A>(p-1)/2\) 的高支撑余项；或
2. \(P<2A\)、\(b\ge2A>B_p\) 的超容量余项。

两类都只表示当前 Type I 载体选择器的精确边界，不表示没有其它 Type I/II 表示，
也不表示 Erdos--Straus 反例。下一步应对这两个锥分别接入 generalized \(2^j\)、
q-adic capacity 或直接 Type II 终端，而不是把 (17) 当作负定理。

## 聚焦回执

算术回执脚本覆盖以下六种状态：

\[
\begin{array}{c|c}
\text{回执}&\text{分类}\\ \hline
(73,1129,5151,4,51)&P\ge2A\text{ 的 fixed-}s\\
(73,145,2646,1,49)&\text{因子转移}\\
(73,337,3075,2,75)&\text{余因子交换}\\
(73,161,2938,1,26)&b\text{ 的 fixed-}n\text{ 折叠}\\
(73,317,5785,1,65)&\text{高支撑残余}\\
(73,1585,28926,1,18)&\text{超容量残余}
\end{array}
\]

其中四元组顺序为 ((p,n,M,d,A))。这些控制只验证算术分类、规范图表和势支付；
它们不提供新的 source/path 可达性，也不替代全局 F/G 选择器。

复现命令：

```bash
python3 reproductions/type_i_overflow_high_capacity_small_d_residual_cone.py --verify
```
