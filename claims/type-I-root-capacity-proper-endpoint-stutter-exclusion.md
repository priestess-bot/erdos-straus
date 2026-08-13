---
kind: claim
claim_id: type-I-root-capacity-proper-endpoint-stutter-exclusion
title: 根容量 proper endpoint 的 stutter 门审计（原低端排除已撤回）
statement: >-
  对核心素数 p≡1 mod24 的实际 root-capacity receipt，令
  M0=(p^2+p+1)/3、u=gcd(2r+1,M0)、h=3u，并取
  R-h=E D、D|K 的 maximal complete-excess 归一化。proper-root 中的唯一
  非严格同余门仍是 D≡1−h (mod p) 且 D|ph+1。此前试图由该门推出
  h<p 时矛盾的证明错误地假设 D|m(p^2+p+1)，现已撤回；低端门是否为空仍是开放问题。
claim_status: retracted
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

# 根容量 proper endpoint 的 stutter 门审计（原低端排除已撤回）

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

## 已验证的有效内容

proper-root 的实际回执满足

\[
D\mid ph+1,qquad c=\left\langle D(h-1)^{-1}\right\rangle_p,qquad
\text{stutter}\Longleftrightarrow D\equiv1-h\pmod p.
\]

### 原低端排除证明的错误

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

但是不能从 (7) 减去 \(m(p^2+p+1)\)：当前假设没有给出
\(D\mid p^2+p+1\) 或 \(D\mid m(p^2+p+1)\)。例如抽象整数
\(p=5,h=3,m=2,D=8\) 满足 \(D\mid mp^2+p+1\)，却不满足
\(D\mid m(p^2+p+1)\)。因此旧稿中的
\(D\mid(m-1)(p+1)\) 及其大小矛盾不成立，不能据此排除任何 \(h\) 区间。

最后，proper-root 端点满足 \(h\mid p^2+p+1\)，而

\[
p^2+p+1\equiv1\pmod p,
\]

所以 \(h=p\) 本身不可能；但这并不排除任何其余端点的 stutter。

## 对全局出口目标的增量

因此不能声称一般 root hard box 已压缩为唯一高端余项：

* \(h^2<p\) 的旧小 endpoint 论证暂时无效，不能宣称所有 \(h<p\) 都严格；
* \(u=M_0\) 的饱和 root 仍须先执行真实 \(p\)-peel，本定理只处理 proper-root；
* 必须重新处理所有 proper-root stutter，并与 endpoint priority、source provenance
  或容量递降联立。

这是纠错记录，而不是新的全局出口定理。全局“短证书或递降”目标仍未闭合。

## 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_proper_endpoint_stutter_exclusion.py --verify
```

复现脚本只核验实际回执的已知整除门和抽象反例，不把错误的大小矛盾当作验证结果。
