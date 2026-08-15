---
kind: claim
claim_id: type-I-normal-chart-height-bound
title: Type I 正规图表的二次高度上界
statement: >-
  对任意核心素数 p 的标准 Type I 正规形
  p=4ABC-m、mR=4B^2C+1，其中 3<=m<=p-2，恒有
  mR-1=B(p+m)/A<=(p+m)^2/4，进而
  R<=floor(((p+3)^2+4)/12)，并有相应的 K 上界
  floor((p*floor(((p+3)^2+4)/12)+1)/4)。因此，若一个候选 typed reclassification 保留
  (p,R,K) 且其 R 或 K 超过相应界，它不可能是标准 Type I 正规形。这是同图表重分类的必要条件，
  不排除改变 R、K 的重图表、Type II 路径或其它递降机制。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-coprime-factor-normal-form
topics:
  - type-I
  - normal-form
  - chart-height
  - same-chart-no-go
  - reclassification
  - proof-boundary
sources:
  - claim: type-I-coprime-factor-normal-form
    role: standard-normal-form-coordinates
  - reproduction: reproductions/type_i_normal_chart_height_boundary.py
    role: positive-normal-form-controls
visibility: public
last_checked: '2026-08-15'
---

# Type I 正规图表的二次高度上界

设 \(p\equiv1\pmod {24}\) 是核心素数，且一张标准 Type I 正规形为

\[
p=4ABC-m,
\qquad
mR=4B^2C+1,
\qquad
(A,B)=1,
\tag{1}
\]

其中 \(A,B,C\) 为正整数，且 \(m\equiv3\pmod4\)、\(3\le m\le p-2\)。这里
置 \(H=AR-B\)、\(K=BCH\)；标准正规形恒等式给出
\(4K=pR+1\)，其中 \(R\) 是该图表余因子。

## 定理

令

\[
D=mR-1.
\tag{2}
\]

则任何这样的正规形都满足

\[
\boxed{
D=\frac{B(p+m)}{A}\le\frac{(p+m)^2}{4}.}
\tag{3}
\]

特别地，

\[
\boxed{
R\le\left\lfloor\frac{(p+3)^2+4}{12}\right\rfloor.}
\tag{4}
\]

写

\[
U_R(p)=\left\lfloor\frac{(p+3)^2+4}{12}\right\rfloor.
\tag{5}
\]

由于 \(K=(pR+1)/4\) 随 \(R\) 单调，(4) 还给出可直接检索的伴随界

\[
\boxed{
K\le U_K(p):=\left\lfloor\frac{pU_R(p)+1}{4}\right\rfloor.}
\tag{6}
\]

因此，固定 \(p,R,K\) 的候选图表若违反 (4) 或 (6)，就不可能被 typed reclassification
实现为一张**标准 Type I 正规形**。这里 \(K\) 不是额外自由度，因为同一图表恒有
\(4K=pR+1\)。

## 证明

由 (1)，

\[
D=4B^2C,
\qquad
p+m=4ABC.
\tag{7}
\]

消去 (4BC) 得到精确恒等式

\[
DA=B(p+m).
\tag{8}
\]

又 \(C\ge1\)，所以 \(D=4B^2C\ge4B^2\)，即

\[
B\le\frac{\sqrt D}{2}.
\tag{9}
\]

而 \(A\ge1\) 与 (8) 给出 \(D\le B(p+m)\)。代入 (9) 并除以正数
\(\sqrt D\)，便有

\[
\sqrt D\le\frac{p+m}{2},
\]

这正是 (3)。于是

\[
R=\frac{D+1}{m}
\le\frac{(p+m)^2+4}{4m}.
\tag{10}
\]

右端作为实变量 \(m\in[3,p-2]\) 的函数可写为

\[
\frac{p^2+4}{4m}+\frac p2+\frac m4.
\tag{11}
\]

其导数的符号由 \(m^2-(p^2+4)\) 决定，在这个区间内严格为负。因此 (10) 的最大值
在 \(m=3\) 处取得，给出 (4)；将该界代入 \(K=(pR+1)/4\) 即得 (6)。证毕。

## 两个独立正规形控制

* \(p=193\)、\((m,A,B,C,R)=(15,2,1,26,7)\) 时，
  \(D=104\le10816=(p+m)^2/4\)。
* \(p=2377\)、\((m,A,B,C,R)=(71,3,2,102,23)\) 时，
  \(D=1632\le1498176=(p+m)^2/4\)。

第二个控制含 \(B=2\)，所以该边界不是 \(B=1\) 外部源子类的偶然性质。

## 范围

本卡只给出 Type I 正规形的必要高度条件。它不构造任意 \(p\) 的正规形、终端证书或
严格源，也不排除通过改变 \(R,K\) 的换图表进入 Type I，或进入 Type II 的路径。

Focused verification:

```bash
python3 reproductions/type_i_normal_chart_height_boundary.py --verify
```
