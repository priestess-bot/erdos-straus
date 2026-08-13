---
kind: claim
claim_id: type-I-root-capacity-proper-endpoint-stutter-exclusion
title: 根容量 proper endpoint 在 h 小于 p 时排除实际 stutter
statement: >-
  对核心素数 p≡1 mod24 的实际 root-capacity receipt，令
  M0=(p^2+p+1)/3、u=gcd(2r+1,M0)、h=3u，并取
  R-h=E D、D|K 的 maximal complete-excess 归一化。若 u<M0 且 h<p，
  则实际 canonical cofactor c=<D(h−1)^(-1)>p 满足 c≤p−2；等价地，
  唯一可能的 stutter 门 D≡1−h (mod p) 不发生。因而 proper-root 的实际
  stutter 只能出现在 h>p 的端点层；h=p 由 h|(p^2+p+1) 不可能。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-general-endpoint-divisor-gate
  - type-I-root-capacity-stutter-receipt-factor-split
topics:
  - type-I
  - root-capacity
  - proper-root
  - stutter
  - complete-excess
  - divisor-gate
  - strict-carry
  - global-exit
  - proof-boundary
sources:
  - claim: type-I-root-capacity-general-endpoint-divisor-gate
    role: actual-receipt-divisor-gate-and-canonical-cofactor
  - claim: type-I-root-capacity-stutter-receipt-factor-split
    role: cyclotomic-exclusion-and-p-plus-one-gcd-control
  - reproduction: reproductions/type_i_root_capacity_proper_endpoint_stutter_exclusion.py
    role: symbolic-and-fixed-receipt-checks
visibility: public
last_checked: '2026-08-13'
---

# 根容量 proper endpoint 在 h < p 时排除实际 stutter

## 设置

固定核心素数 \(p\equiv1\pmod{24}\)，令

\[
M_0=\frac{p^2+p+1}{3},
\qquad
u=\gcd(2r+1,M_0),
\qquad
h=3u.
\]

取一个真实 root-capacity endpoint 的 maximal complete-excess receipt，并按既有正规形写成

\[
z=R-h=E D,
\qquad D\mid K,
\qquad D\mid ph+1,
\qquad (h,z)=1.
\tag{1}
\]

由 \(u\mid M_0\) 还知道 \(h\mid p^2+p+1\)。实际因子分裂引理另外给出
\(\gcd(D,M_0)=1\)，而 \(D\mid z\) 与 \(\gcd(h,z)=1\) 给出 \(3\nmid D\)。

假设是 proper-root \(u<M_0\)，所以 \(p\nmid E\)，且规范 cofactor 为

\[
c=\left\langle D(h-1)^{-1}\right\rangle_p.
\tag{2}
\]

需要排除的唯一非严格情形是

\[
D\equiv1-h\pmod p.
\tag{3}
\]

## 定理

若 \(h<p\)，则 (3) 不可能成立。因此

\[
\boxed{h<p\Longrightarrow c\le p-2.}
\tag{4}
\]

### 证明

现在反设 (3) 成立。由于 \(0<h<p\)、\(D>0\)，存在唯一整数 \(m\ge1\) 使

\[
D=mp+1-h.
\tag{6}
\]

由 \(D\mid ph+1\) 和 (6)，有

\[
D\mid(ph+1)+pD=mp^2+p+1.
\tag{7}
\]

用 \(m(p^2+p+1)\) 减去右侧，得到

\[
\boxed{D\mid(m-1)(p+1).}
\tag{8}
\]

令 \(g_+=\gcd(D,p+1)\)。由 (8)，

\[
\frac D{g_+}\mid m-1.
\tag{9}
\]

若 \(m=1\)，则 (7) 直接给出 \(D\mid p^2+p+1=3M_0\)。结合
\(\gcd(D,M_0)=1\) 和 \(3\nmid D\)，只能有 \(D=1\)；但
\(D=p+1-h\ge2\)，矛盾。

以下设 \(m\ge2\)。此时 (9) 的右端为正，故可以取大小估计。

另一方面，\(g_+\mid p+1\) 且 \(g_+\mid D\mid ph+1\)，在模 \(g_+\) 下有

\[
0\equiv ph+1\equiv1-h,
\]

所以

\[
g_+\mid h-1.
\tag{10}
\]

结合 (9)--(10)，得到

\[
D\le(m-1)(h-1).
\tag{11}
\]

但由 (6) 直接计算

\[
D-(m-1)(h-1)
=mp+1-h-(mh-m-h+1)
=m(p-h+1)>0,
\tag{12}
\]

与 (11) 矛盾。故 (3) 不成立，(4) 得证。

最后，proper-root 端点满足 \(h\mid p^2+p+1\)，而

\[
p^2+p+1\equiv1\pmod p,
\]

所以 \(h=p\) 本身不可能。由此实际 proper-root stutter 若存在只能满足

\[
\boxed{h>p.}
\tag{13}
\]

证毕。

## 对全局出口目标的增量

这条定理把一般 root hard box 从“任意 \(h\)”压缩为唯一高端余项：

* \(h^2<p\) 的旧小 endpoint 条件不再需要；所有 \(h<p\) 都有严格 arithmetic carry；
* \(u=M_0\) 的饱和 root 仍须先执行真实 \(p\)-peel，本定理只处理 proper-root；
* 剩余 proper-root stutter 必须在 \(h>p\) 上与 endpoint priority、source provenance
  或高端容量递降联立，不能再从小端点抽象除数门出发。

特别地，这不是把抽象 \(ph+1\) 除数误当成 actual receipt：\(m\ge2\) 分支只使用了
\(D\mid ph+1\)、\(D>0\) 和 \(h<p\)；边界 \(m=1\) 使用实际 receipt 的
cyclotomic-free 条件 \(\gcd(D,M_0)=1\) 与 \(3\nmid D\)。

该定理本身尚未处理 \(h>p\) 的 stutter，也没有给出跨分母解提升；所以全局
“短证书或递降”目标仍未闭合，但其 proper-root 余项已明确降维。

## 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_proper_endpoint_stutter_exclusion.py --verify
```

复现脚本只核验定理中的整除链、互素链和两个固定 proper-root 严格 receipt；不做范围扫描。
