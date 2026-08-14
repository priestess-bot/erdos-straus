---
kind: claim
claim_id: type-I-root-capacity-stutter-transverse-pminusone-root-quotient-offset-saturation
title: p 减一 complete-excess 横向素因子的 root-quotient 偏移饱和
statement: >-
  对核心素数 p≡1 mod24 的 actual proper-root stutter receipt，令
  u=h/3、v=(p^2+p+1)/h、w=(2r+1)/u。若 q|(E,D*,m+2,p-1) 是
  p-1,h+1 complete-excess overlap 素数，b=v_q(p-1)、t=v_q(D)-b，
  则 q^b|(v+3,w+9)，且
  v_q(p^2(w+9)-3(v+3))=b；所以
  min(v_q(v+3),v_q(w+9))=b。该 root-quotient 二分容量图只限制
  complete-excess q 的来源，尚不构造证书、已注册递降边或全局出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-transverse-overlap-receipt-relay
  - type-I-root-capacity-stutter-transverse-residual-capacity-map
topics:
  - type-I
  - root-capacity
  - stutter
  - transverse-residual
  - complete-excess
  - p-minus-one
  - root-quotient
  - valuations
  - capacity-map
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-transverse-overlap-receipt-relay
    role: p-minus-one-overlap-base-valuations-and-T-excess
  - claim: type-I-root-capacity-stutter-transverse-residual-capacity-map
    role: root-quotients-and-exact-T-identity
  - reproduction: reproductions/type_i_root_capacity_stutter_transverse_pminusone_root_quotient_offsets.py
    role: fixed-proper-root-q-primary-offset-control
visibility: public
last_checked: '2026-08-14'
---

# \(p-1\) complete-excess 横向素因子的 root-quotient 偏移饱和

## 1. 设置

固定一个核心素数 \(p\equiv1\pmod {24}\) 的 actual proper-root stutter receipt。
写

\[
u=\frac h3,\qquad
v=\frac{p^2+p+1}{h},\qquad
w=\frac{2r+1}{u}.
\tag{1}
\]

这些是 root capacity 的两个互素商，并有精确恒等式

\[
\frac{2T}{u}=p^2w-3v.
\tag{2}
\]

设 \(q\mid(E,D_*,m+2,p-1)\) 是 \(p-1,h+1\) overlap 中的
complete-excess 奇素数。令

\[
b=v_q(p-1),\qquad t=v_q(D)-b>0.
\tag{3}
\]

此前的 actual relay 已给出

\[
v_q(h+1)=v_q(r-1)=b,\qquad v_q(T)=b+t,\qquad q\ne3.
\tag{4}
\]

特别地 \(q\nmid h\) 和 \(q\nmid u\)。

## 2. 两个偏移的共同基准

由 (1) 有

\[
h(v+3)=p^2+p+1+3h.
\tag{5}
\]

将 \(p\equiv1\pmod {q^b}\)、\(h\equiv-1\pmod {q^b}\) 代入右侧，得到

\[
q^b\mid v+3.
\tag{6}
\]

同样地，利用 \(u(w+9)=2r+1+9u=2r+1+3h\)，(4) 给出

\[
q^b\mid w+9.
\tag{7}
\]

这两个偏移是 actual proper-root 条件的产物；它们不能从只保留
receipt/checkpoint 局部同余的控制中恢复。

## 3. 不可同时高于基准

从 (2) 直接得到

\[
\begin{aligned}
p^2(w+9)-3(v+3)
&=\frac{2T}{u}+9(p^2-1).
\end{aligned}
\tag{8}
\]

因为 \(q\nmid u\)，(4) 的第一项赋值为 \(b+t>b\)。又 \(q\ne3\) 且
\(q\mid p-1\)、\(q\nmid p+1\)，所以第二项满足

\[
v_q\bigl(9(p^2-1)\bigr)=b.
\tag{9}
\]

非阿基米德比较由 (8)--(9) 强制

\[
\boxed{
v_q\bigl(p^2(w+9)-3(v+3)\bigr)=b.}
\tag{10}
\]

结合 (6)--(7)，若 \(v+3\) 和 \(w+9\) 都被 \(q^{b+1}\) 整除，则 (10) 左侧
也会被 \(q^{b+1}\) 整除，矛盾。因此得到 root-quotient 二分容量图：

\[
\boxed{
\min\{v_q(v+3),v_q(w+9)\}=b.}
\tag{11}
\]

换言之，complete-excess 的原始高 \(q\)-幂不会在两个 proper-root quotient
offset 中同时保留；至少一个坐标恰在 overlap 基准处饱和。

## 4. 边界

式 (11) 是 actual-root-only 的来源压缩。它把后续
`transverse_residual_provenance_adapter` 分成可检验的 \(v+3\) 或 \(w+9\)
饱和两支，但当前没有已验证 terminal menu 消耗这两个偏移。因此它不推出
Type I/II 证书、source-tail witness、全域 identity lift 或 E1--E5 edge。

## 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_stutter_transverse_pminusone_root_quotient_offsets.py --verify
```

复现器使用 \((p,h,q,r)=(1009,111,7,351)\) 的固定 proper-root q-primary
控制，核对 \(u=(2r+1,(p^2+p+1)/3)=37\)、(2) 及 (6)--(11)。它不宣称该控制
为完整 actual stutter receipt，也不扫描根层或素数。
