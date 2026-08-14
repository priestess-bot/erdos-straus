---
kind: claim
claim_id: type-I-root-capacity-stutter-transverse-pminusone-root-quotient-orientation
title: p 减一 complete-excess 横向素因子的 root-quotient 定向饱和
statement: >-
  对核心素数 p≡1 mod24 的 actual proper-root stutter receipt，令
  u=h/3、v=(p^2+p+1)/h、w=(2r+1)/u。若 q|(E,D*,m+2,p-1) 是
  p-1,h+1 complete-excess overlap 素数，b=v_q(p-1)、t=v_q(D)-b，
  则 q^b||(v+3)，且 q^(b+1)|(w+9)。因此此前的 root-quotient 二分
  实际有固定方向：cyclotomic quotient v 在基准 q^b 饱和，root-index quotient w
  至少保留一个额外 q。该容量图不构造短证书、解提升、已注册递降边或全局出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-transverse-overlap-receipt-relay
  - type-I-root-capacity-stutter-transverse-pminusone-root-quotient-offset-saturation
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
    role: receipt-quotient-and-p-minus-one-overlap-valuations
  - claim: type-I-root-capacity-stutter-transverse-pminusone-root-quotient-offset-saturation
    role: root-quotient-identity-and-unoriented-saturation
  - reproduction: reproductions/type_i_root_capacity_stutter_transverse_pminusone_root_quotient_orientation.py
    role: fixed-root-and-receipt-q-primary-orientation-control
visibility: public
last_checked: '2026-08-14'
---

# \(p-1\) complete-excess 横向素因子的 root-quotient 定向饱和

## 1. 输入赋值

固定核心素数 \(p\equiv1\pmod {24}\) 的 actual proper-root stutter receipt，写

\[
u=\frac h3,\qquad
v=\frac{p^2+p+1}{h},\qquad
w=\frac{2r+1}{u}.
\tag{1}
\]

设 \(q\mid(E,D_*,m+2,p-1)\) 是 \(p-1,h+1\) complete-excess overlap 素数，
并令

\[
b=v_q(p-1),\qquad t=v_q(D)-b>0,\qquad Q=q^b.
\tag{2}
\]

已有 receipt relay 给出

\[
v_q(h+1)=v_q(r-1)=v_q(e)=b,
\qquad
v_q(T)=b+t,
\tag{3}
\]

以及

\[
v_q(ph+1)=2b+t.
\tag{4}
\]

式 (4) 也直接来自 \(ph+1=eD\)：其中 \(v_q(e)=b\)、
\(v_q(D)=b+t\)。因为 \(q\mid D_*\) 且 \(3\mid h\)，有 \(q\ne3\)，
故所有下列以 \(2,3\) 作单位的比较均合法。

写三个 \(q\)-单位

\[
P=\frac{p-1}{Q},\qquad
H=\frac{h+1}{Q},\qquad
R=\frac{r-1}{Q}.
\tag{5}
\]

## 2. receipt 与 T 的一阶定向

将 \(p=1+QP\)、\(h=-1+QH\) 代入 (4) 的整数，得到

\[
ph+1=Q\bigl(H-P+QPH\bigr).
\tag{6}
\]

由 \(v_q(ph+1)=2b+t>b\)，可知

\[
H\equiv P\pmod q.
\tag{7}
\]

另一方面，\(r=1+QR\) 给出

\[
2T
=Q\left(2R+3P+Q(2P^2+4PR)+2Q^2P^2R\right).
\tag{8}
\]

由 \(v_q(T)=b+t>b\)，得到

\[
2R+3P\equiv0\pmod q.
\tag{9}
\]

## 3. quotient 定向

先由 \(h(v+3)=p^2+p+1+3h\) 与 (5) 得到

\[
h\frac{v+3}{Q}=3(P+H)+QP^2.
\tag{10}
\]

按 (7) 模 \(q\) 化简，右侧为 \(6P\)，而 \(h\equiv-1\pmod q\)。因为
\(q\ne2,3\) 且 \(P\) 是 \(q\)-单位，故

\[
\frac{v+3}{Q}\equiv-6P\not\equiv0\pmod q.
\tag{11}
\]

所以

\[
\boxed{v_q(v+3)=b.}
\tag{12}
\]

再由 \(u(w+9)=2r+1+3h\) 得

\[
u\frac{w+9}{Q}=2R+3H.
\tag{13}
\]

联用 (7) 与 (9)，右端模 \(q\) 为 \(-3P+3P=0\)。又 \(q\nmid u\)，于是

\[
\boxed{v_q(w+9)\ge b+1.}
\tag{14}
\]

这不仅推出先前的
\(\min\{v_q(v+3),v_q(w+9)\}=b\)，还给出哪一侧必须在基准处饱和。

## 4. 边界

式 (12)--(14) 是 actual receipt 与 proper-root 共同产生的容量图。它把未来
`transverse_residual_provenance_adapter` 的根层输入定向为：\(v+3\) 提供恰好
\(q^b\) 的 cyclotomic quotient 因子，\(w+9\) 至少保留 \(q^{b+1}\)。当前
没有已验证的 Type I/II terminal menu 或全域 lift 可直接消耗这对偏移；因此它仍不是
global exit。

## 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_stutter_transverse_pminusone_root_quotient_orientation.py --verify
```

复现器使用 \((p,h,q,r)=(8641,39,5,266)\) 的固定 root/receipt-q-primary 控制，
核对 (3)--(4)、root quotient 公式以及 (12)--(14)。该控制不被声称为完整 actual
stutter receipt，也不扫描范围。
