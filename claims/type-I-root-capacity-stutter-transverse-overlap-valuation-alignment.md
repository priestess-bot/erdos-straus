---
kind: claim
claim_id: type-I-root-capacity-stutter-transverse-overlap-valuation-alignment
title: 横向 stutter overlap 残余的三重赋值对齐与 T 余量
statement: >-
  对核心素数 p≡1 mod24 的 actual proper-root stutter receipt，令
  D*=D/gcd(D,h^2-1)、C=(p^2-1)/2、D_T=D/gcd(D,C)。若奇素数 q|D* 且 q|m，
  则 b=v_q(m)=v_q(p+1)=v_q(h-1)<v_q(D)。若 q|D*、q|m+2 且 q|p-1，
  则 b=v_q(m+2)=v_q(p-1)=v_q(h+1)<v_q(D)。在两种情形中令
  t=v_q(D)-b，则 q^t||D*=q^t||D_T 且 q^t|T。故所有未由局部 terminal
  分流关闭的 p±1 overlap 残余，都由同步的基准 q-赋值之上的 T-side excess 承载；
  该结构本身不构造证书、解提升或全局递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-transverse-residual-capacity-map
  - type-I-root-capacity-stutter-transverse-residual-local-terminal-dispatch
  - type-I-root-capacity-stutter-receipt-factor-split
topics:
  - type-I
  - root-capacity
  - stutter
  - transverse-residual
  - valuations
  - overlap
  - t-residual
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-transverse-residual-capacity-map
    role: D-star-transverse-input-and-D-star-divides-T
  - claim: type-I-root-capacity-stutter-transverse-residual-local-terminal-dispatch
    role: p-plus-one-and-p-minus-one-overlap-branches
  - claim: type-I-root-capacity-stutter-receipt-factor-split
    role: C-T-capacity-split
  - reproduction: reproductions/type_i_root_capacity_stutter_transverse_overlap_valuation_alignment.py
    role: fixed-overlap-valuation-controls
visibility: public
last_checked: '2026-08-14'
---

# 横向 stutter overlap 残余的三重赋值对齐与 \(T\) 余量

## 1. 设置

固定核心素数 \(p\equiv1\pmod {24}\) 的 actual proper-root stutter receipt。沿用
根容量数据

\[
M_0=\frac{p^2+p+1}{3},\qquad
u=(2r+1,M_0),\qquad h=3u,\qquad
T=p^2r-\frac{p+1}{2},
\]

并写

\[
D=mp+1-h,\qquad D\mid ph+1,
\tag{1}
\]

\[
H=h^2-1,\qquad D_*=\frac{D}{(D,H)},\qquad
C=\frac{p^2-1}{2},\qquad D_T=\frac{D}{(D,C)}.
\tag{2}
\]

取奇素数 \(q\mid D_*\)。由 \(D\mid ph+1\) 可知 \((D,h)=1\)，故
\((D_*,h)=1\)；再由 \(3\mid h\)，有 \(q\ne3\)。此前的局部终端分流表明：

\[
q\mid m\Longrightarrow q\mid p+1,\ q\mid h-1,
\tag{3}
\]

而当 \(q\mid m+2\) 且落在尚未处理的 \(p-1\) 分支时，

\[
q\mid p-1,\ q\mid h+1.
\tag{4}
\]

下面的结论只分析这两个 \(p\pm1\) overlap；\(q\mid m+2,2p+1\) 的横向
分支不满足 \(q\mid h^2-1\)，不属于本卡。

## 2. \(p+1,h-1,m\) 的赋值同步

设 \(q\mid m\)，并记

\[
\alpha=v_q(m),\qquad
\beta=v_q(h-1),\qquad
\gamma=v_q(p+1),\qquad
\delta=v_q(D).
\tag{5}
\]

由于 \(q\) 是奇数且 \(q\mid h-1\)，有 \(v_q(H)=\beta\)。又 \(q\mid D_*\)
恰给出

\[
\delta>\beta.
\tag{6}
\]

由 (1) 的第一式

\[
D=mp-(h-1).
\tag{7}
\]

若 \(\alpha<\beta\)，右侧两项的赋值不同，故 \(v_q(D)=\alpha<\beta\)；若
\(\alpha>\beta\)，则 \(v_q(D)=\beta\)。两者都与 (6) 矛盾。因此

\[
\alpha=\beta.
\tag{8}
\]

再由 \(D\mid ph+1\) 和

\[
ph+1=p(h-1)+(p+1),
\tag{9}
\]

可知 \(v_q(ph+1)\ge\delta>\beta\)。若 \(\gamma\ne\beta\)，(9) 右侧的赋值
不同，其和的赋值至多为 \(\beta\)，矛盾。故 \(\gamma=\beta\)。综上，

\[
\boxed{
q\mid(D_*,m)
\Longrightarrow
v_q(m)=v_q(p+1)=v_q(h-1)<v_q(D).}
\tag{10}
\]

## 3. \(p-1,h+1,m+2\) 的赋值同步

现在设 \(q\mid m+2\) 且 \(q\mid p-1\)，并记

\[
\alpha=v_q(m+2),\qquad
\beta=v_q(h+1),\qquad
\gamma=v_q(p-1),\qquad
\delta=v_q(D).
\tag{11}
\]

由 (4) 和 \(q\mid D_*\)，仍有 \(v_q(H)=\beta\) 与 \(\delta>\beta\)。先使用

\[
ph+1=p(h+1)-(p-1).
\tag{12}
\]

和 \(D\mid ph+1\)。与第 2 节同样的不同赋值论证给出

\[
\gamma=\beta.
\tag{13}
\]

把 (1) 重写为

\[
D=(m+2)p-(h+1)-2(p-1).
\tag{14}
\]

若 \(\alpha<\beta\)，(14) 的第一项具有严格较小的赋值，强制
\(v_q(D)=\alpha<\beta\)，矛盾。若 \(\alpha>\beta\)，把 (12) 与 (14) 分别除以
\(q^\beta\) 再模 \(q\) 化简。设

\[
P=\frac{p-1}{q^\beta},\qquad
U=\frac{h+1}{q^\beta};
\]

它们都是模 \(q\) 的单位。由 \(\delta>\beta\) 得

\[
U-P\equiv0\pmod q,
\qquad
U+2P\equiv0\pmod q.
\tag{15}
\]

于是 \(3P\equiv0\pmod q\)，与 \(q\ne3\) 及 \(q\nmid P\) 矛盾。因此
\(\alpha=\beta\)，并得到

\[
\boxed{
q\mid(D_*,m+2),\ q\mid p-1
\Longrightarrow
v_q(m+2)=v_q(p-1)=v_q(h+1)<v_q(D).}
\tag{16}
\]

## 4. 同步基准之上的 \(T\)-side excess

在 (10) 或 (16) 的任一情形，记共同的基准赋值为 \(b\)，并置

\[
t=v_q(D)-b>0.
\tag{17}
\]

由于 \(q\) 为奇数，且在各自情形中它只整除 \(p^2-1\) 的一个线性因子，

\[
v_q(C)=b,\qquad v_q(H)=b.
\tag{18}
\]

所以

\[
\boxed{
v_q(D_*)=v_q(D_T)=t.}
\tag{19}
\]

已有的约化残余与 \(C/T\) 因子分裂给出 \(D_*\mid T\) 及 \(D_T\mid T\)，从而

\[
\boxed{q^t\mid T.}
\tag{20}
\]

因此 overlap 情形不是任意的 \(p\pm1\) 因子重合：\(m\) 或 \(m+2\)、相应
\(p\pm1\)、相应 \(h\mp1\) 必先以完全相同的 \(q\)-赋值对齐，而真正留在
\(D_*\) 中的 \(q^t\) 是一个 \(T\)-side excess。

## 5. 边界

本引理没有上界 \(t\)，也不保证 \(q\mid m\) 或 \(q\mid m+2\) 发生。它尤其不能从
\(q^t\mid T\) 推出容量素因子 \(q\mid u\)、external-source 菜单命中、Type I/II
证书或解提升。它只将上一张局部分流卡剩下的 \(p-1,h+1\) 支路，连同 \(p+1,h-1\)
的 nonterminal 子支，压缩为一个可以与 actual \(T\)-赋值和 complete-excess provenance
继续联立的同步 valuation 约束。

## 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_stutter_transverse_overlap_valuation_alignment.py --verify
```

脚本只重放两个固定抽象 stutter 算术控制：一个 \(p+1,h-1,m\) overlap，一个
\(p-1,h+1,m+2\) overlap。两者都明确不冒充 actual root receipt；它们用于核对
(10)、(16)、(19) 的纯整数赋值关系，不执行范围扫描。
