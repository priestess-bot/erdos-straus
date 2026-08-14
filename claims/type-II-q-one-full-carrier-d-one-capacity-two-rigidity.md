---
kind: claim
claim_id: type-II-q-one-full-carrier-d-one-capacity-two-rigidity
title: q=1 full-carrier 的 d=1 容量二刚性入口与 19 相位分离
statement: >-
  设 ordinary q=1 G full-carrier root 的第二-anchor fixed-n 宏已产生 persistent
  d=1 receiver，并令其 p-free complete-excess canonical target 的 residual capacity
  为 c。则 c=2 当且仅当宏在偶 t=2s 分支满足 g=gcd((p+1)/2,(n+1)/2)=1、j=8；
  奇 t 分支不可能有 c=2。此时 n=2p-1、q_*=19、p=912u+769，初始 raw p-source
  门失败而 p-free 门通过，故实际 relay 必使用既有 least-coprime source repair。若
  A=(pn-1)/4、E=(2p^2-3p-1)/2、M=AE，则 c=2 target 是一个 high C=2 chart；
  M 是 19 的倍数，而最小 high C=2 support A_2=(p-1)(2p-1)/8 是 19-unit。写
  M=A_2+ph，则 h>0 且 h=15 (mod 19)。因此 q=1 路径进入 C=2 的唯一方式被压缩为
  一个严格的 19-phase 高支持子族；它不能与最小 C=2 边界同一化，也不由该最小边界的
  bundle/dyadic no-go 自动关闭。该结论是容量映射，不构造该高相位子族的全称终端或递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-full-carrier-d-one-p-free-gate-exclusion-relay
  - type-II-q-one-full-carrier-second-anchor-fixed-n-macro
  - type-I-overflow-full-product-d-one-complete-excess-capacity-map
  - type-I-high-support-c2-boundary-carry-dyadic-capacity-transduction
  - type-I-high-support-c2-centered-vieta-antipodal-no-go
  - denominator-escape-state-contract
topics:
  - type-II
  - q-one
  - full-carrier
  - type-I
  - d-one
  - complete-excess
  - residual-capacity
  - c-two
  - high-support
  - phase-separation
  - source-repair
  - proof-boundary
sources:
  - claim: type-II-q-one-full-carrier-d-one-p-free-gate-exclusion-relay
    role: immediate-p-free-admission-and-least-coprime-source-repair
  - claim: type-I-high-support-c2-boundary-carry-dyadic-capacity-transduction
    role: minimal-c-two-boundary-and-its-limited-scope
  - reproduction: reproductions/type_ii_q_one_full_carrier_d_one_capacity_two_rigidity.py
    role: exact-odd-boundary-and-even-c-two-phase-receipt
visibility: public
last_checked: '2026-08-15'
---

# q=1 full-carrier 的 d=1 容量二刚性入口与 19 相位分离

## 1. 要分类的容量面

固定 ordinary q=1 G full-carrier root 的第二-anchor fixed-(n) 宏产生的 immediate
postmacro \(d=1\) receiver。沿用已有卡的记号：

\[
A=\frac{pn-1}{4},\qquad
R=(p-1)n-1,\qquad
K=A(p-1),
\tag{1}
\]

\[
\alpha=\frac{p+1}{2}=ga,\qquad
v=\frac{n+1}{2}=gb,\qquad
E=(p-1)b-a.
\tag{2}
\]

前卡已证明这个 immediate receiver 的 p-free 门总通过。因此其 complete-excess
carrier \(M=AE\) 有唯一 canonical target；记其 residual capacity 为

\[
c=\frac{K_M}{M}\in\{1,\ldots,p-1\},
\qquad c\equiv-E^{-1}\pmod p.
\tag{3}
\]

再生正是 \(c=p-1\)，且已被单独收口。本卡只分类最小、也是现有高支撑机制中最刚性的
非再生容量面：

\[
\boxed{c=2.}
\tag{4}
\]

## 2. 奇支不可能进入 \(c=2\)

在奇 \(t\) 分支，已有闭式为

\[
p=24t+1,\qquad
14\delta+3=jp,\qquad 1\le j\le13,
\tag{5}
\]

\[
21n=5jp+7j-15,\qquad
3(7v)-5j\alpha=j+3.
\tag{6}
\]

所以 \(g\mid j+3\)。另一方面，直接由 (6) 消去 \(t\)，得到

\[
42(\alpha+v)=(5j+21)p+(7j+27).
\tag{7}
\]

结合 \(E\equiv-(\alpha+v)/g\pmod p\)，容量公式 (3) 化为

\[
c(7j+27)\equiv42g\pmod p.
\tag{8}
\]

若 \(c=2\)，则

\[
p\mid T:=7j+27-21g.
\tag{9}
\]

由 \(1\le j\le13\) 及 \(1\le g\le j+3\)，有

\[
-218\le T\le97.
\tag{10}
\]

并且 \(T\not=0\)，因为 \(T\equiv27\equiv6\pmod7\)。故 (9) 强制
\(p\le218\)。奇支有 \(t\ge3\)，于是唯一可能的核心素数是

\[
p=73,\qquad t=3.
\tag{11}
\]

式 (5) 给出 \(j=1\)，再由 (6) 得 \(n=17,g=1\)，从而 \(T=13\)，与
\(73\mid T\) 矛盾。因此

\[
\boxed{\text{奇 }t\text{ 的 q=1 immediate receiver 从不有 }c=2.}
\tag{12}
\]

## 3. 偶支的 \(c=2\) 刚性

令 \(t=2s\)。宏的强制 excess prime \(q_\star\) 满足

\[
p=48s+1,\qquad q_\star\mid6s-1,
\tag{13}
\]

并有唯一 \(j\) 满足

\[
3q_\star\delta-4=jp,\qquad
1\le j<3q_\star<p,\qquad j\equiv2\pmod3,
\tag{14}
\]

\[
4n=jp+4-j,\qquad
\alpha=24s+1,\qquad v=6js+1.
\tag{15}
\]

于是

\[
4v-j\alpha=4-j,\qquad g\mid j-4,
\tag{16}
\]

以及

\[
8(\alpha+v)=(j+4)p+(12-j).
\tag{17}
\]

所以 (3) 给出精确容量同余

\[
c(12-j)\equiv8g\pmod p.
\tag{18}
\]

令 \(c=2\)。式 (18) 等价于

\[
j+4g\equiv12\pmod p.
\tag{19}
\]

若 \(j=2\)，则 \(g=1\) 且左端为 \(6\)，不可能满足 (19)。若 \(j\ge5\)，由
\(g\mid j-4\) 和 \(j<3q_\star\le18s-3\)，有

\[
0<j+4g\le5j-16<90s-31<2p.
\tag{20}
\]

故 (19) 只可能给出 \(j+4g=12\) 或 \(j+4g=p+12\)。后一个等式会使

\[
g\mid j-4=p+8,\qquad g\mid\alpha\mid p+1,
\tag{21}
\]

故 \(g\mid7\)。若 \(g=1\)，则 \(j=p+8>p\)；若 \(g=7\)，则
\(j=p-16=48s-15\)，这与 \(j<18s-3\) 矛盾。于是只能有

\[
j+4g=12.
\tag{22}
\]

因 \(g\) 为奇数且 \(j\equiv2\pmod3\)，(22) 强制

\[
\boxed{g=1,\qquad j=8,\qquad n=2p-1.}
\tag{23}
\]

把 (23) 代回 determinant \(pn=4(9s q_\star)\delta+1\)，得到

\[
q_\star\delta=4(32s+1).
\tag{24}
\]

由于 \(q_\star\) 是奇素数且 \(q_\star\mid6s-1\)，它也整除 \(32s+1\)。但

\[
16(6s-1)-3(32s+1)=-19,
\tag{25}
\]

故

\[
\boxed{q_\star=19.}
\tag{26}
\]

反过来，偶支的 \(g=1,j=8\) 代回 (18) 给出 \(4c\equiv8\pmod p\)，而
\(1\le c<p\)，所以 \(c=2\)。因此 (12)、(23) 给出精确分类，而不只是必要条件。

## 4. raw source 修复与 19 相位

由 (23)，

\[
R=(p-1)(2p-1)-1=p(2p-3),
\tag{27}
\]

所以 immediate receiver 的 universal raw \(p\)-source 不 primitive。另一方面
\(n\equiv-1\pmod p\)，并不等于 \(-2\pmod p\)，故 p-free 门通过。于是当
terminal-first 没有更早退出时，已有的最小互素素数 source repair 是这里唯一的规范
anchor source；不能把 \(p\)-source 误写为可用。

式 (13)、(26) 给出

\[
s\equiv16\pmod{19},\qquad
\boxed{p=912u+769\quad(u\ge0).}
\tag{28}
\]

现在 \(a=(p+1)/2\)、\(b=p\)，所以

\[
E=\frac{2p^2-3p-1}{2},
\qquad
A=\frac{p(2p-1)-1}{4},
\qquad M=AE.
\tag{29}
\]

由 \(p\equiv9\pmod{19}\)、\(n\equiv17\pmod{19}\)，有

\[
4A=pn-1\equiv9\cdot17-1\equiv0\pmod{19},
\qquad 19\mid M.
\tag{30}
\]

令同一 \(p\) 的最小 high \(C=2\) support 为

\[
A_2=\frac{(p-1)(2p-1)}8.
\tag{31}
\]

它满足 \(A_2\equiv17\pmod{19}\)，所以 \(M\ne A_2\)。又已有 complete-excess
下界给出 \(M>p^2>A_2\)，故唯一写成

\[
M=A_2+ph,\qquad h>0.
\tag{32}
\]

将 (30)--(32) 模 \(19\) 化简，使用 \(p^{-1}\equiv17\pmod{19}\)，得到

\[
\boxed{h\equiv15\pmod{19}.}
\tag{33}
\]

因此 target 的坐标为

\[
K_2=2M,\qquad
R_2=2p-3+8h,
\tag{34}
\]

并满足 \(19\mid K_2\)、\(R_2\equiv2\pmod{19}\)。这精确区分了 q=1 路径的
容量二 target 与最小 \(C=2\) 图表：两者的 support 相差一个非零的、固定同余类的
high phase。

## 5. 作用域

本卡把 q=1 路径进入最难 \(C=2\) 容量面的入口压缩为单一 \(q_\star=19\) 高相位子族，
并记录了 raw \(p\)-source 失败与 charged support 的 19-归属。它不构造该子族的
Type I/II 短证书，也不把最小 \(C=2\) 图表的 complete-excess 或 dyadic no-go 扩展到
所有 high phase。下一条有效路线必须利用 (28)、(33) 的额外 19 相位信息，或给出独立的
terminal/strict edge；不能把最小边界的结论直接外推。

聚焦重放：

```bash
python3 reproductions/type_ii_q_one_full_carrier_d_one_capacity_two_rigidity.py --verify
```

它只重放奇支强制的 \(p=73\) 边界和偶支 \(p=769\) 的 \(q_\star=19\) 完整容量二
receipt；不做素数范围扫描或终端枚举。
