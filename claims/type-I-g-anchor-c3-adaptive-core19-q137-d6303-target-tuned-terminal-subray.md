---
kind: claim
claim_id: type-I-g-anchor-c3-adaptive-core19-q137-d6303-target-tuned-terminal-subray
title: q=137 实际 raw 族的 D=6303 target-tuned Type II 终端子射线
statement: 在 q=137 actual raw family p(w)=193+772716168w 中，固定 D_star=6303、M_star=4D_star=25212、A=K=1 和 target factor h=M_star-1=25211。唯一同余 w=21771 (mod 25211) 使 h|p(w)+M_star；写 w=21771+25211t、t>=0，则 p=p0+19480947311448t，p0=16822803693721，且 gcd(p0,19480947311448)=1。因此该子射线有无穷 prime parameter，且每个 prime parameter 保留 q=137 actual raw receipt。对每个这样的 prime，B=(p+1)/25211、m=B+1、x=6303B、d=6303 给出 A=1,C=6303,K=1 的直接 Type II 证书。t=2 的 p=55784698316617 由四层 Pocklington 链认证为素数。这是一个显式 target-tuned terminal family，不是 raw-to-fiber adapter、capacity 或 terminal-free selector edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-c3-adaptive-core19-q137-first-entry-family
  - type-II-coprime-factor-normal-form
  - type-II-same-modulus-source-switch-crt-criterion
topics:
  - type-I
  - Type-II
  - c3
  - core19
  - raw-source
  - q137
  - affine-family
  - target-tuning
  - CRT
  - D6303
  - constructive-certificate
  - terminal-first
  - Dirichlet
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_c3_adaptive_core19_q137_first_entry_family.py
    role: target congruence, Pocklington prime control, and Type II normal-form certificates
visibility: public
last_checked: '2026-08-07'
---

# q=137 实际 raw 族的 \(D_\ast=6303\) target-tuned 终端子射线

这是一条正向的整数 target 构造：不从 character phase 猜测 cofactor，而是在已有
actual raw affine family 的参数上直接调谐一个合法 Type II target factor。它证明
target residue 与 raw admission 可以在同一无穷子射线上同时实现，但该子射线因此被
terminal-first 关闭，不能作为 selector 的 terminal-free 分支。

## 1. Target 与参数同余

已有 q=137 raw family 是

\[
p(w)=P+\Delta w,\qquad
P=193,\qquad
\Delta=772716168.
\tag{1}
\]

取

\[
D_\ast=6303=3\cdot11\cdot191,\qquad
M_\ast=4D_\ast=25212,\qquad
h=M_\ast-1=25211.
\tag{2}
\]

于是 \(h\equiv-1\pmod {M_\ast}\)、\((h,M_\ast)=1\)，且 \((\Delta,h)=1\)。
又 \(D_\ast/A=6303\) 平方自由。解

\[
\Delta w\equiv-(P+AM_\ast)\pmod h
\tag{3}
\]

得到唯一最小非负代表

\[
w_0=21771.
\tag{4}
\]

所以

\[
w=w_0+ht,\qquad t\ge0
\Longrightarrow
h\mid p(w)+AM_\ast.
\tag{5}
\]

写

\[
\begin{aligned}
p_t&=16822803693721+19480947311448t,\\
w_t&=21771+25211t.
\end{aligned}
\tag{6}
\]

有

\[
(16822803693721,19480947311448)=1,\qquad
p_0\equiv1\pmod {24},\qquad
19480947311448\equiv0\pmod {24}.
\tag{7}
\]

特别地 \(AM_\ast<p_0\)，所以 \(A=1\) 是同模数 source-switch 判据中的 admissible
参数。

故 Dirichlet 定理给出无穷多个 prime \(p_t\)。由于 \(w_t\ge0\)，每个这些 prime
parameter 同时属于既有 q=137 actual raw family，保留其 actual primitive
\(137;\operatorname{Fac}(Q)\) receipt。

## 2. 直接 Type II normal form

令

\[
A=1,\qquad C=D_\ast=6303,\qquad K=1,\qquad
B_t=\frac{p_t+1}{h}.
\tag{8}
\]

由 \(M_\ast=h+1\)，(5) 等价于

\[
p_t+M_\ast=h(B_t+1).
\tag{9}
\]

因此

\[
q=4ACK-1=25211=h,\qquad q\mid Kp_t+A,
\tag{10}
\]

且 \(B_t\ge A\)。互素因子正规形立刻给出

\[
m_t=A+B_t=B_t+1,\qquad
x_t=AB_tC=6303B_t,\qquad
d=A^2C=6303.
\tag{11}
\]

所以对每个 prime \(p_t\)，有直接证书

\[
\boxed{
\frac4{p_t}
=\frac1{x_t}
+\frac1{6303p_t}
+\frac1{6303B_tp_t}.}
\tag{12}
\]

这里 \(h\) 是真正的 target factor：它既整除 \(p_t+4AD_\ast\)，又满足
\(h\equiv-1\pmod {4D_\ast}\)。这正是同模数 source-switch 判据中的完整算术
target，而不是仅有相位兼容的余因子。

## 3. 一个实际 prime/raw/terminal 控制

取 \(t=2\)，得到

\[
\begin{aligned}
w&=72193,\\
p&=55784698316617,\\
B&=2212712638,\\
m&=2212712639,\\
x&=13946727757314.
\end{aligned}
\tag{13}
\]

该 \(p\) 的 Pocklington 链为

\[
\begin{aligned}
21003781-1&=2^2\cdot3\cdot5\cdot7\cdot43\cdot1163,\\
252045373-1&=2^2\cdot3\cdot21003781,\\
43855894903-1&=2\cdot3\cdot29\cdot252045373,\\
p-1&=2^3\cdot3\cdot53\cdot43855894903.
\end{aligned}
\tag{14}
\]

复现器以 bases \((10,2,2,2)\) 验证每层 Pocklington 条件。因此该控制点同时有
actual q=137 raw receipt 和 (12) 的 Type II certificate：

\[
\frac4{55784698316617}
=\frac1{13946727757314}
+\frac1{351610953489636951}
+\frac1{778014000445749883509486738}.
\tag{15}
\]

## 4. 范围

这条构造展示了如何把一个 target residue 通过参数 CRT 调回实际 raw family；它不从
v=5 的 phase 数据导出 \(H\)，也没有为任意给定 raw occurrence 构造 target。所有
prime terms 都已有短证书，故它只能作为 raw-to-integer terminal 的正控制，而不能
充当 capacity、递降或 selector edge。

窄复现：

    python3 reproductions/type_i_c3_adaptive_core19_q137_first_entry_family.py --verify
