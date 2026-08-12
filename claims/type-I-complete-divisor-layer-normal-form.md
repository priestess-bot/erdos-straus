---
kind: claim
claim_id: type-I-complete-divisor-layer-normal-form
title: 完整 d 整除 x 的 Type I 层的规范因子正规形
statement: 对核心素数 p=24h+1，全部合法 m=24c-1 缺口上满足 d|x=(p+m)/4 的 Type I 证书，与唯一数据 (lambda,r,t) 一一对应：lambda|6、r|h+c、t=(h+c)/r、gcd(r,6/lambda)=1，且 24c-1|6pt+lambda；此时 d=lambda r。该层严格扩大此前 lambda=2 的 d=2r 终端族。p=2137 是 R=3 G 且四路 residual，旧 d=2r 层未命中，但新层以 (m,d)=(23,45) 直接终止。双 G 七路 residual p=2521 在此更大的完整 d|x 层仍无命中，故该层也不能单独构成全称出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - short-certificate-equivalence
  - type-I-24c-minus-one-adaptive-divisor-terminal-family
  - type-I-adaptive-d2r-global-family-boundary
topics:
  - type-I
  - adaptive-divisor
  - divisor-normal-form
  - terminal-first
  - R3-G
  - double-G
  - strict-counterexample
  - proof-boundary
sources:
  - claim: short-certificate-equivalence
    role: Type-I-divisor-reconstruction
  - claim: type-I-24c-minus-one-adaptive-divisor-terminal-family
    role: lambda-equals-two-subfamily
  - claim: type-I-adaptive-d2r-global-family-boundary
    role: previous-smaller-layer-boundary
  - reproduction: reproductions/type_i_complete_divisor_layer_normal_form.py
    role: exact-layer-equality-and-controls
visibility: public
last_checked: '2026-08-12'
---

# 完整 \(d\mid x\) Type I 层的规范因子正规形

## 1. 精确参数化

令

\[
p=24h+1,
\qquad
1\le c\le h,
\qquad
m=24c-1,
\qquad
s=h+c,
\qquad
x=\frac{p+m}{4}=6s.
\tag{1}
\]

考虑该 gap 上完整的 **\(d\mid x\) Type I 层**。也就是说，只限制

\[
d\mid x,
\qquad
m\mid px+d,
\tag{2}
\]

不讨论 \(d\mid x^2\) 但 \(d\nmid x\) 的其余 Type I 证书。

**定理。** (2) 的每个 \(d\) 唯一写成

\[
\boxed{
d=\lambda r,
\quad
\lambda\mid6,
\quad
r\mid s,
\quad
t=s/r,
\quad
\gcd(r,6/\lambda)=1,}
\tag{3}
\]

且其 Type I 条件精确为

\[
\boxed{
24c-1\mid6pt+\lambda.}
\tag{4}
\]

反过来，(3)--(4) 的每一组数据都给出 (2)，从而恢复标准 Type I certificate。

**证明。** 对任意 \(d\mid6s\)，定义

\[
\lambda=(d,6),
\qquad
r=d/\lambda.
\tag{5}
\]

则 \(\lambda\mid6\)。对每个素数幂，\(d\) 中未被 \(\lambda\) 吸收的部分必须来自
\(s\)，故 \(r\mid s\)；而 \((r,6/\lambda)=1\) 恰保证 (5) 不会漏掉
\(d\) 的 \(2,3\)-进部分。反过来，这三个条件显然给出
\(\lambda r\mid6rt=6s\)。因此 (3) 是 \(d\mid x\) 的唯一正规形。

又 \(p=24s-m\)，所以

\[
px+d
=6ps+\lambda r
=r(6pt+\lambda).
\tag{6}
\]

由 \(m<p\)、\(p\) 为素数以及 \(p\equiv24s\pmod m\)，有 \((s,m)=1\)，
故 \((r,m)=1\)。于是 (6) 中 \(m\mid px+d\) 当且仅当 (4) 成立。证毕。

\(\lambda=2\) 正好恢复此前 \(d=2r\) 的完整自适应终端族；(3) 说明
\(\lambda\in\{1,3,6\}\) 是该层此前没有读取的仅有新方向。

## 2. R=3 G 中的严格新增 terminal

取

\[
p=2137,
\qquad
h=89,
\qquad
c=1,
\qquad
m=23,
\qquad
s=90.
\tag{7}
\]

选择

\[
\lambda=3,
\qquad
r=15,
\qquad
t=6,
\qquad
d=45.
\tag{8}
\]

有 \((r,2)=1\)，且

\[
23\mid6\cdot2137\cdot6+3.
\tag{9}
\]

故这是一张直接 Type I certificate，明确为

\[
\boxed{
\frac4{2137}
=\frac1{540}+\frac1{50175}+\frac1{1286687700}.}
\tag{10}
\]

同时

\[
\frac{3p+1}{4}=1603=7\cdot229,
\tag{11}
\]

其素因子均为 \(1\pmod3\)，所以 \(p\) 是 \(R=3\) G。既有四路 dispatch 仍在
此点返回 residual；完整 \(\lambda=2\) 层也无命中。故 (10) 是本正规形相对于旧层
的实际新增 terminal，而非符号重写。

## 3. 更大层的严格边界

双 G 控制

\[
p=2521,
\qquad h=105
\tag{12}
\]

在所有 \(1\le c\le105\)、全部 \(\lambda\mid6\) 与 (3) 允许的 \(r\mid h+c\)
中都不满足 (4)。也就是说，

\[
\boxed{
p=2521\text{ 在完整 }d\mid x\text{ Type I 层没有 certificate}.}
\tag{13}
\]

该点也是当前七路 terminal dispatch 的 residual。因此，即使将 \(d=2r\) 扩大到
完整 \(d\mid x\) 层，仍不能得到 R=3 G 或全局出口的全称 selector。这里不否定
\(p=2521\) 的 gap-23 Type II 严格递降；恰恰说明全局论证必须在该层失败时切换到
Type II 或另一条可提升递降。

复现命令：`python3 reproductions/type_i_complete_divisor_layer_normal_form.py --verify`
