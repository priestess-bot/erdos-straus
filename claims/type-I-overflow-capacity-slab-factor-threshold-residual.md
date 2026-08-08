---
kind: claim
claim_id: type-I-overflow-capacity-slab-factor-threshold-residual
title: 高载体容量层的因子阈值残余二分
statement: 设核心素数 p=1 (mod 24) 的 verified overflow 满足 pn=4Md+1、B_p=(p-1)^2/4<M<2B_p，且 c=(p-1)/4<=A<=B_p、A|M。写 b=M/A。则必有完整 E1--E5 递降，除非 1<b<=d 且 d*spf(b)>=p：若 b>p，L=b 满足 outer-rank 条件并由固定-n 商模 p 折叠给出后继；若 b<p 且 b>d，余因子交换给出后继；若 b<=d 且 d*spf(b)<p，最小素因子转移给出后继。b=p 不可能。故 d^2<p 时容量层完全闭合。边界 (p,d,n,M,A,b)=(73,11,789,1309,187,7) 显示因子阈值残余在当前菜单中非空；它不是猜想反例，也不否定 fixed-s、终端或其它 alternate。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-cofactor-factor-exchange-carrier-descent
  - type-I-overflow-fixed-n-quotient-fold-descent
topics:
  - type-I
  - overflow
  - high-carrier
  - capacity-window
  - cofactor
  - factor-threshold
  - residual
  - quotient-fold
  - well-founded-descent
  - proof-boundary
sources:
  - claim: type-I-overflow-cofactor-factor-exchange-carrier-descent
    role: small-cofactor-transfer-and-exchange
  - claim: type-I-overflow-fixed-n-quotient-fold-descent
    role: large-cofactor-folded-reset
  - reproduction: reproductions/type_i_overflow_capacity_slab_factor_threshold_residual.py
    role: focused-four-route-receipt
visibility: public
last_checked: '2026-08-08'
---

# 高载体容量层的因子阈值残余二分

## 定理

设 \(p\equiv1\pmod {24}\) 为素数，并记

\[
B_p=\frac{(p-1)^2}{4},
\qquad c=\frac{p-1}{4}.
\]

设一个已有 source/path/node 回执的 verified overflow 满足

\[
pn=4Md+1,
\qquad B_p<M<2B_p,
\qquad 1\le d<p,
\qquad c\le A\le B_p,
\qquad A\mid M.
\tag{1}
\]

写 \(b=M/A>1\)。则以下三类构造已经覆盖除

\[
\boxed{\quad 1<b\le d,
\qquad d\,\operatorname{spf}(b)\ge p\quad}
\tag{2}

以外的全部状态：

\[
\begin{array}{c|c|c}
\text{条件}&\text{构造}&\text{E5}\\ \hline
b>p&L=b\text{ 的 fixed-}n\text{ 商模 }p\text{ 折叠}&\text{outer support rank}\\
b<p,\ b>d&(M,d)=(Ab,d)\mapsto(Ad,b)&(\lfloor B_p/A\rfloor,M)\\
b\le d,\ d\,\operatorname{spf}(b)<p&g=\operatorname{spf}(b)\text{ 的因子转移}&(\lfloor B_p/A\rfloor,M)
\end{array}
\tag{3}
\]

每一行均为完整 E1--E5 边；(2) 只是当前三种构造的精确残余，不排除 fixed-\(s\)、
Type I/II 终端或其它 alternate。

## 证明

由 (1)，

\[
b=\frac MA\le\frac Mc<\frac{2B_p}{c}=2(p-1).
\tag{4}
\]

并且 \(p\nmid M\)，所以 \(b=p\) 不可能。

若 \(b>p\)，则

\[
A=\frac Mb<\frac{2B_p}{p}=\frac{(p-1)^2}{2p}<\frac p2<b,
\]

故 \(b>2A\)。再由 (4) 和 \(p\ge73\)，有 \(b<2(p-1)<B_p\)，从而

\[
A<b\le B_p,
\qquad
\left\lfloor\frac{B_p}{b}\right\rfloor
\le\left\lfloor\frac{B_p}{2A}\right\rfloor
<\left\lfloor\frac{B_p}{A}\right\rfloor.
\tag{5}
\]

因为 \(b\mid M\mid Md\)，取 \(L=b\) 并调用 fixed-\(n\) 商折叠给出第一行。

现在设 \(b<p\)。若 \(b>d\)，余因子交换的条件 \(d<b<p\) 成立，给出第二行。
若 \(b\le d\) 且 \(d\operatorname{spf}(b)<p\)，最小素因子
\(g=\operatorname{spf}(b)\) 是可移因子，给出第三行。故仅在 (2) 时这三条规则
同时不适用，证明完毕。

## 平方阈值推论与精确边界

若 \(d^2<p\)，则 (2) 不可能：其中
\(\operatorname{spf}(b)\le b\le d\)，故

\[
d\operatorname{spf}(b)\le d^2<p.
\]

所以整个容量层在 \(d^2<p\) 时完全闭合。

边界例

\[
(p,d,n,M,A,b)=(73,11,789,1309,187,7)
\]

满足 \(B_{73}=1296<M<2B_{73}\)、\(A\ge c=18\)，而

\[
1<b=7\le11=d,
\qquad d\operatorname{spf}(b)=11\cdot7=77\ge73.
\]

它精确落在 (2)。这只表明当前因子转移、交换和 \(L=b\) 折叠菜单没有自动出口，
不表示该行没有其它合法递降或直接证书。

## 聚焦复现

```bash
python3 reproductions/type_i_overflow_capacity_slab_factor_threshold_residual.py --verify
```

四条精确回执覆盖大余因子的折叠、\(b>d\) 的交换、低于阈值的因子转移和 (2) 的
严格边界；不做历史范围扫描。
