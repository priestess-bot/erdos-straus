---
kind: claim
claim_id: type-i-empty-fiber-target-odd-source-demand
title: 空 F 纤维的 target-odd 支撑分离—源差分二分
statement: 对目标 t=-1 属于源子群 H 但有界指数纤维为空的 Type I 状态，盒像的反演对称性保证存在规范 target-odd 角色 chi(t)=-1，其 Fourier 实部至少为单位元盒重数 c(1)。按该角色在盒像差分子群上的限制，空 F 纤维严格分成目标奇支撑分离或至少一个独立 q 初等源差分请求；前者不收费容量，后者才可送入 Type-II source admission。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-i-empty-target-fiber-gf-source-dispatch
  - type-I-f-target-involution-fourier-phase-collapse
  - type-I-fg-fourier-to-type-II-role-demand-bridge
topics:
  - type-I
  - F-state
  - target-odd
  - Fourier
  - source-difference
  - q-primary
  - capacity
  - Type-II
  - constructive-certificate
  - proof-program
sources:
  - claim: type-i-empty-target-fiber-gf-source-dispatch
    role: empty-fiber-G-F-dispatch
  - claim: type-I-f-target-involution-fourier-phase-collapse
    role: target-odd-energy-identity
  - reproduction: reproductions/type_i_empty_target_fiber_gf_source_dispatch.py
    role: p73-target-odd-q-demand-control
visibility: public
last_checked: '2026-08-09'
---

# 空 F 纤维的 target-odd 支撑分离—源差分二分

## 设置

固定 Type I 图表

\[
K=\frac{pR+1}{4}=\prod_iq_i^{\nu_i},\qquad
H=\langle q_i\bmod R\rangle\le U(R),
\]

以及指数盒和像映射

\[
\mathcal B=\prod_i[-\nu_i,\nu_i]\cap\mathbb Z^r,\qquad
\phi(z)=\prod_iq_i^{z_i}.
\]

设目标 \(t=-1\in H\)，但

\[
\mathcal Z_t=\{z\in\mathcal B:\phi(z)=t\}=\varnothing.
\]

令 \(c(x)=|\{z\in\mathcal B:\phi(z)=x\}|\)，
\(S=\operatorname{supp}(c)\)，
\(D_B=\langle ss'^{-1}:s,s'\in S\rangle\)，并令

\[
A(\chi)=\sum_{x\in H}c(x)\chi(x)
\]

为未归一化盒 Fourier 系数。

## Target-odd 能量引理

由于 \(\mathcal B=-\mathcal B\)，有

\[
c(x)=c(x^{-1}).
\tag{1}
\]

目标 \(t=-1\) 是非平凡对合，且 \(c(t)=0\)，而零指数给出 \(c(1)\ge1\)。定义

\[
X^-=\{\chi\in\widehat H:\chi(t)=-1\}.
\]

则每个 \(A(\chi)\) 对 \(\chi\in X^-\) 都是实数，并且

\[
\boxed{
\sum_{\chi\in X^-}A(\chi)
=\frac{|H|}{2}\bigl(c(1)-c(t)\bigr)
=\frac{|H|}{2}c(1).
}
\tag{2}
\]

因此存在一个规范选择的 \(\chi_-\in X^-\)，使

\[
\boxed{
A(\chi_-)\ge c(1)\ge1,\qquad \chi_-(t)=-1.
}
\tag{3}
\]

规范规则是先最大化实数 \(A(\chi)\)，再按角色阶和固定群坐标字典序最小化。
这比在全部非平凡角色中任取一个负 Fourier 项更强：角色被强制保留目标对合的
相位信息。

## 源差分二分

对 \(\chi_-\) 运行同一个有限源差分门。

### 1. Target-odd 支撑分离

若

\[
\chi_-|_{D_B}=1,
\]

则因为 \(1\in S\)，有 \(\chi_-(s)=1\) 对所有 \(s\in S\)，而
\(\chi_-(t)=-1\)。故得到构造性证书

\[
\mathrm{TARGET\_ODD\_SUPPORT\_SEPARATION}
\]

及载荷 \((\chi_-,D_B,S,t,A(\chi_-))\)。其盒支撑全部在
\(\ker\chi_-\) 中，目标在相反相位层；不产生 Type-II q 需求，也不应计入跨状态
容量。

### 2. Target-odd 源差分 q 请求

若 \(\chi_-|_{D_B}\) 非平凡，取

\[
q_*=\min\{q:q\text{ 是 }|\chi_-(D_B)|\text{ 的素因子}\}.
\]

则

\[
\boxed{
r_{q_*}(B)=
\dim_{\mathbb F_{q_*}}
\left(D_{B,q_*}/q_*D_{B,q_*}\right)\ge1.
}
\tag{4}
\]

若 \(\mathcal L_B=\langle z-z':z,z'\in\mathcal B\rangle\)，则

\[
\boxed{
\frac{\mathcal L_B}
{\mathcal L_B\cap\ker\phi+q_*\mathcal L_B}
\cong
\frac{D_B}{q_*D_B}.
}
\tag{5}
\]

所以输出

\[
\mathrm{TARGET\_ODD\_SOURCE\_DIFFERENCE\_Q\_DEMAND}
(q_*,r_{q_*},\chi_-|_{D_B}).
\]

这至少是一个真实源关系方向，而不是角色阶、Fourier 幅度或目标对合相位的重复
收费。只有独立 source-map、整数相位提升、物理 owner、容量和 E1--E5 通过后，
它才可以进入 Type-II 短证书或严格可提升递降。

## 证明

由有限阿贝尔角色正交性，

\[
\sum_{\chi:\chi(t)=-1}\chi(x)
=\frac{|H|}{2}
\bigl(\mathbf 1_{x=1}-\mathbf 1_{x=t}\bigr).
\tag{6}
\]

将 (6) 乘以 \(c(x)\) 求和，得到 (2)。式 (1) 还给出
\(A(\chi)=\overline{A(\chi)}\)：将 \(x\mapsto x^{-1}\) 代换即可。因此平均值至少
\(c(1)\)，得到 (3)。

若 \(\chi_-\) 在 \(D_B\) 上恒等，则它在 \(S\) 上是常数；因为 \(1\in S\)，该
常数只能是 \(1\)，于是得到分支 1。

若 \(\chi_-\) 在 \(D_B\) 上非恒等，其像是非平凡有限循环群，故某个
\(q_*\)-primary 部分非平凡，\(D_{B,q_*}/q_*D_{B,q_*}\) 非零，得到 (4)。
\(\phi\) 限制在 \(\mathcal L_B\) 上满射到 \(D_B\)，第一同构定理和
\(\phi(q_*\mathcal L_B)=q_*D_B\) 给出 (5)。两支互斥且穷尽。证毕。

## 实例：\(p=73,\ R=27\)

\[
K=493=17\cdot29,\qquad H=U(27),\qquad
\mathcal B=\{-1,0,1\}^2.
\]

取 \(2\) 为 \(U(27)\) 的生成元，则

\[
17=2^{15},\qquad29=2,\qquad-1=2^9\pmod {27}.
\]

盒像指数是 \(\{-4,-3,\ldots,4\}\pmod {18}\)，故目标纤维为空而 \(t\in H\)。
规范 target-odd 角色可取 \(\chi_-(2)=e^{2\pi i/18}\)，其角色指标为 \(1\)，
且

\[
A(\chi_-)
=1+2\sum_{j=1}^{4}\cos\frac{\pi j}{9}
\approx5.758770483144
\ge c(1)=1.
\]

盒像含有 \(1,2\)，所以 \(D_B=H\)，角色在差分群上非平凡。其最小素数
方向为 \(q_*=2\)，且 \(r_2(B)=1\)。因此该实例严格输出
\(\mathrm{TARGET\_ODD\_SOURCE\_DIFFERENCE\_Q\_DEMAND}(2,1)\)，而不是
\(\mathrm{TARGET\_ODD\_SUPPORT\_SEPARATION}\)。

## 选择器意义与边界

对于空 F 纤维，target-odd 角色把“目标对合缺失”与“源差分 q 需求”绑定：

\[
\text{empty F fiber}
\to
\begin{cases}
\text{target-odd support separation},\\
\text{target-odd source q demand}.
\end{cases}
\]

第一支是免费的对偶负证书；第二支才进入已有 source-label SNF、物理 q 流和
Type-II admission。该引理没有证明 q 请求必有整数提升，也没有证明跨状态容量必超载；
它把全局缺口进一步缩小为 source-map/owner/E1--E5 的具体承接问题。

## 聚焦复现

~~~bash
python3 reproductions/type_i_empty_target_fiber_gf_source_dispatch.py --verify
~~~

