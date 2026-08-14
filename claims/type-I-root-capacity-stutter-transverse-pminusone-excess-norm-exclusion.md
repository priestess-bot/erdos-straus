---
kind: claim
claim_id: type-I-root-capacity-stutter-transverse-pminusone-excess-norm-exclusion
title: p 减一 complete-excess 横向素因子的 Eisenstein 范数排除
statement: >-
  对核心素数 p≡1 mod24 的 actual proper-root stutter receipt，设
  q|(E,D*,m+2,p-1) 是 p-1,h+1 overlap 中的 complete-excess 奇素数，且
  e=(ph+1)/D、a=em-h、N=a^2-a(e-1)+(e-1)^2。则 q!=3 且
  N≡3 mod q，故 v_q(N)=0。因而这个 complete-excess q 不能作为现有
  Eisenstein 范数或范数商的素因子进入根容量 source provenance；该排除不提供
  Type I/II 证书、p-1 source tail、已注册递降边或全局出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-transverse-overlap-receipt-relay
  - type-I-root-capacity-stutter-eisenstein-support
topics:
  - type-I
  - root-capacity
  - stutter
  - transverse-residual
  - complete-excess
  - p-minus-one
  - eisenstein-norm
  - provenance
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-transverse-overlap-receipt-relay
    role: actual-p-minus-one-complete-excess-receipt-valuations
  - claim: type-I-root-capacity-stutter-eisenstein-support
    role: norm-and-existing-source-provenance-interface
  - reproduction: reproductions/type_i_root_capacity_stutter_transverse_overlap_receipt_relay.py
    role: fixed-local-q-primary-norm-exclusion-control
visibility: public
last_checked: '2026-08-14'
---

# \(p-1\) complete-excess 横向素因子的 Eisenstein 范数排除

## 1. 设置

固定核心素数

\[
p\equiv1\pmod {24}
\]

的一个 actual proper-root stutter receipt。沿用

\[
D_*=\frac{D}{(D,h^2-1)},\qquad
e=\frac{ph+1}{D},\qquad
a=em-h,
\tag{1}
\]

以及 stutter Eisenstein 范数

\[
N=a^2-a(e-1)+(e-1)^2.
\tag{2}
\]

设奇素数 \(q\) 落在横向 \(p-1,h+1\) overlap 的 actual complete-excess
支路，即

\[
q\mid(E,D_*,m+2,p-1).
\tag{3}
\]

这里 \(q\ne3\)：因为 \(3\mid h\)，而 actual 横向商已有
\((D_*,h)=1\)。

## 2. 范数排除

receipt/checkpoint relay 对 (3) 给出

\[
q\mid e,\qquad a=em-h\equiv1\pmod q.
\tag{4}
\]

第二个同余也可直接由 \(q\mid m+2\)、\(q\mid h+1\) 和 \(q\mid e\) 看出。
于是

\[
e-1\equiv-1\pmod q.
\tag{5}
\]

代入 (2)，得到不依赖任何估计的固定余数：

\[
\begin{aligned}
N
&\equiv 1^2-1(-1)+(-1)^2\\
&\equiv3\pmod q.
\end{aligned}
\tag{6}
\]

由于 \(q\ne3\)，故

\[
\boxed{v_q(N)=0.}
\tag{7}
\]

这比仅有 \(q\nmid h\) 更强：该 \(q\) 不但不是 \(h\)-支撑容量因子，也根本不在
stutter Eisenstein 范数 \(N\) 或范数商 \(N/h\) 中。

## 3. 对 provenance 的含义

现有 Eisenstein provenance 分派从 \(q\mid N\) 开始：若该因子也在 \(h\) 中，
它可被识别为 root-capacity source；若不在 \(h\) 中，则仍须另建 quotient-only
adapter。式 (7) 表明 (3) 中的 complete-excess \(q\) 不会进入这两种范数分派的
任一种。

因此，不能把 \(q\mid E\)、\(q\mid E_1+1\) 或 \(q\mid e\) 重命名为
``Eisenstein norm factor''，并借用已有 norm-to-source 菜单。任何后续
`transverse_residual_provenance_adapter` 若要消耗该 \(q\)，必须使用
receipt/checkpoint relay 之外的新输入，例如直接的 \(p-1\) source-tail 构造、独立
短证书，或带全域 identity lift 的严格递降。

## 4. 边界与聚焦复现

式 (7) 是对一类 provenance 的严格排除，不是 \(p-1\) source descent 的失败证明。
它既不说明所有 \(p-1\) source tail 都为空，也不排除未来使用 \(q\) 的非范数
构造，更不产生 Type I/II 证书或 E1--E5 recursive edge。

```bash
python3 reproductions/type_i_root_capacity_stutter_transverse_overlap_receipt_relay.py --verify
```

该复现器在固定的局部 \(p-1\) complete-excess receipt 控制上重算 (4)--(7)；控制
不被冒充为 actual root receipt，正文的全称结论仅使用 (1)--(5) 的 actual 前提。
