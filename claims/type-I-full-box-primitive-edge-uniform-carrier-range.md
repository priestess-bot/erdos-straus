---
kind: claim
claim_id: type-I-full-box-primitive-edge-uniform-carrier-range
title: 完整指数盒的原始坐标边与统一 q-载体范围阈值
statement: >-
  设一个 exact F source contract 保留完整指数盒 B_nu 的每条坐标边 0->e_i，
  且非零 q-初等 source role gamma:Z^r->F_q 在该盒差分格上可见。则按固定
  坐标顺序存在一条带名原始边 e_i，满足 gamma(e_i)!=0、content(e_i)=1 及最小
  q-height 对偶深度为零。故对尚未绑定层的单请求可固定 J=1、d=q-1，并消去
  content 所导致的载体范围增长。对每个奇素数 q，由有限个 (beta_q(p),gamma(e_i))
  残数确定的 canonical cyclotomic carrier 阈值 T_q 有限；当核心素数 p>T_q 时，
  此原始边有一个 full-C_q candidate q-prefix arithmetic carrier。特别地 q=3 时
  T_3=484778372；所以 p>T_3 的任何完整盒 3-可见请求都通过该 carrier 的纯算术
  范围门。该结论只给 candidate/source-line arithmetic provenance；它不证明
  prescribed target state、joint SNF、occurrence、FIBER_REALIZED、解提升或 E5。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-source-lattice-qheight-dual-valuation-shift-carrier
  - type-I-source-lattice-qheight-exclusive-tail-kernel-relay
  - type-I-fg-qprefix-request-depth-admission
  - type-I-fg-qprefix-block-bound-first-overflow-terminal
topics:
  - type-I
  - type-II
  - F-state
  - source-lattice
  - full-exponent-box
  - primitive-edge
  - q-adic
  - q-prefix
  - carrier
  - range-bound
  - strict-obstruction
  - proof-program
sources:
  - claim: type-I-source-lattice-qheight-dual-valuation-shift-carrier
    role: rank-one-depth-and-matched-carrier
  - claim: type-I-source-lattice-qheight-exclusive-tail-kernel-relay
    role: full-Cq-prefix-boundary
  - claim: type-I-fg-qprefix-request-depth-admission
    role: one-request-one-lineage-and-coordinate-edge-control
  - claim: type-I-fg-qprefix-block-bound-first-overflow-terminal
    role: actual-F-full-box-control
  - reproduction: reproductions/type_i_full_box_primitive_edge_uniform_carrier_range.py
    role: primitive-edge-and-q3-threshold-controls
visibility: public
last_checked: '2026-08-12'
---

# 完整指数盒的原始坐标边与统一 \(q\)-载体范围阈值

## 1. 适用的 source contract

设

\[
\mathcal B_\nu=\prod_{i=1}^r[-\nu_i,\nu_i]\cap\mathbb Z^r,
\qquad \nu_i\ge1,
\tag{1}
\]

并且当前的 exact source contract 已明确保留每条带名坐标边

\[
0\longrightarrow e_i\qquad(1\le i\le r)
\tag{2}
\]

作为合法 source relation。这是一个实质前提：若 contract 已经过滤了某条边，不能
仅由它仍在抽象指数盒中把它重新收费为 physical source。

令奇素数 \(q\) 的 source-visible elementary role 为

\[
\gamma:\mathbb Z^r\longrightarrow\mathbb F_q,
\qquad \gamma\ne0.
\tag{3}
\]

这里把 role 写在完整差分格上，是指其已通过当前 contract 所要求的 relation/SNF
准入；本卡不把盒外角色或 anchor-only 角色改写为 (3)。

## 2. 原始坐标边引理

按固定坐标顺序取最小的 \(i\) 使

\[
c:=\gamma(e_i)\ne0.
\tag{4}
\]

这样的 \(i\) 必存在，否则 (3) 在 \(\mathbb Z^r\) 的标准基上全为零。令

\[
\delta=e_i.
\tag{5}
\]

则 \(0,e_i\in\mathcal B_\nu\)，所以 (2) 给出一条真实带名边；并且

\[
\boxed{
\operatorname{content}(\delta)=1,
\qquad
d_q(\mathbb Z\delta,\gamma|_{\mathbb Z\delta})=0.}
\tag{6}
\]

第一式直接来自 \(e_i\) 的坐标。第二式是 rank-one depth 公式：\(q\) 不整除
\(\operatorname{content}(e_i)\)，故其 \(q\)-进赋值为零。于是这个请求可在不改变
原 source edge 的情况下固定使用

\[
J=1,
\qquad d=q-1.
\tag{7}
\]

这严格消除了 content \(g\) 随状态增长而推高最小层或 carrier 大小的分支；它没有
消除 source/target 发生额外过滤、共同 canonical base、标签或 occurrence 的门。

## 3. 只依赖 \(q\) 的 canonical 范围阈值

令

\[
m=q^q,
\qquad b=\beta_q(p)=-p4^{-1}\pmod m.
\tag{8}
\]

固定 cyclotomic 素数 \(r_q\) 为满足

\[
\operatorname{ord}_{r_q}(q)=q,
\qquad v_q(r_q-1)=1
\tag{9}
\]

的最小素数。令
\(\mathcal B_q^{\rm core}=\{\beta_q(p):p\text{ 是核心素数}\}\subseteq U(m)\)。
当 \(q=3\) 时它是所有 \(2\pmod3\) 的单位残数；当 \(q\ge5\) 时，CRT 与
Dirichlet 定理给出 \(\mathcal B_q^{\rm core}=U(m)\)。对每个

\[
b\in\mathcal B_q^{\rm core},\qquad c\in\mathbb F_q^\times,
\tag{10}
\]

定义 \(\alpha=c(b\bmod q)^{-1}\)。以下每一步均在满足所列同余和避让条件的
素数中取最小者：

\[
\begin{aligned}
u_{b,c}&\equiv1+\alpha q\pmod m,&u_{b,c}&\ne r_q,\\
v_{b,c}&\equiv1\pmod m,&v_{b,c}&\notin\{r_q,u_{b,c}\},\\
\lambda_{b,c}&\equiv b(r_qu_{b,c})^{-1}\pmod m,&
\lambda_{b,c}&\notin\{r_q,u_{b,c},v_{b,c}\}.
\end{aligned}
\tag{11}
\]

各剩余类都是 \(m\) 的单位，Dirichlet 定理保证这些确定化选择存在。定义

\[
\begin{aligned}
x_{b,c}&=r_qu_{b,c}\lambda_{b,c},\\
D_{*,b,c}&=x_{b,c},\qquad D_{0,b,c}=x_{b,c}v_{b,c},\\
s_{0,b,c}&=x_{b,c}v_{b,c},\qquad
s_{1,b,c}=x_{b,c}u_{b,c}v_{b,c},\\
T_q&=\max_{b\in\mathcal B_q^{\rm core},\ c\ne0}
4r_qu_{b,c}^{\,2}v_{b,c}\lambda_{b,c}.
\end{aligned}
\tag{12}
\]

这是有限最大值，故 \(T_q<\infty\)。若 \(p>T_q\)，则对由 (4) 选出的 \(b,c\)
有

\[
4s_{1,b,c}<p.
\tag{13}
\]

且

\[
\begin{aligned}
v_q(p+4x_{b,c})&\ge q,\\
v_q(p+4s_{0,b,c})&\ge q,\\
v_q(p+4s_{1,b,c})&=1,\\
\frac{s_{1,b,c}-s_{0,b,c}}q&\equiv c\pmod q.
\end{aligned}
\tag{14}
\]

目标取 \((D_*,A,C)=(x_{b,c},1,x_{b,c})\)，两条 source rows 取
\((D_0,1)\)、\((D_0,u_{b,c})\)。它们全部 canonical，且整数仿射式

\[
\mathcal L(z)=s_{0,b,c}+(s_{1,b,c}-s_{0,b,c})z_i
\tag{15}
\]

在带名边 \(0\to e_i\) 上实现 (4)。因此已有估值移位与 q-prefix 定理给出一个
depth \(q-1\) 的 arithmetic candidate；其 cyclotomic quotient 中 \([q]\) 的像
生成 \(C_q\)。

这里的量词只覆盖 **算术 carrier 的范围门**。要把它升级为 typed prefix，仍必须逐项
验证 candidate-fiber binding、prescribed role/SNF、source-switch、fresh occurrence
和完整 target state；即使 full \(C_q\) prefix 已 typed-realized，target miss 的
kernel slice 仍不是 E4/E5。

## 4. \(q=3\) 的精确统一阈值

核心素数满足 \(p\equiv1\pmod3\)，故 (8) 的允许残数恰为

\[
b\in\{2,5,8,11,14,17,20,23,26\}\pmod{27}.
\tag{16}
\]

这里 \(r_3=13\)。当 \(c=1\) 时 \(u=7\)；当 \(c=2\) 时 \(u=31\)。两种情况的
最小 \(v\) 都是 \(109\)。枚举 (16) 与 \(c\in\{1,2\}\) 的 18 个确定性值给出

\[
\boxed{
T_3=4\cdot13\cdot31^2\cdot109\cdot89
=484778372,}
\tag{17}
\]

最大值在 \((b,c)=(11,2)\) 取得。于是对任意 \(p>T_3\) 的核心素数，只要一个
完整盒 source contract 产生 source-visible 的 3-角色，就存在一条 content-one
coordinate edge 通过 full-\(C_3\) carrier 的纯算术范围门。

作为低于统一阈值但实际通过的控制，\(p=557281\) 有 \(b=20,c=1\)，由 (11) 得

\[
(r,u,v,\lambda)=(13,7,109,2),
\qquad
4r u^2v\lambda=555464<p.
\tag{18}
\]

它正是实际 F 指数盒中 factor-\(2\) coordinate edge 的既有 full-\(C_3\) candidate。
该控制的完整因子积仍不命中 \(-1\)，所以它同时防止把本引理误读成终端定理。

## 5. 选择器分派

~~~text
full exponent-box source contract + source-visible q role
  -> first nonzero coordinate edge 0 -> e_i
  -> content = 1, minimal q-depth = 0
  -> p > T_q:
       canonical full-C_q arithmetic carrier range passes
       -> run candidate binding / SNF / occurrence / target-state gates
  -> p <= T_q:
       no range conclusion from this lemma
  -> filtered coordinate edge or non-full source contract:
       FULL_BOX_PRIMITIVE_EDGE_ADMISSION_UNPROVED
~~~

本引理只压缩“content 造成的 range obstruction”。它既不证明每个 F/G 状态拥有完整
指数盒 source contract，也不为 G 支撑分离制造虚假的 q 请求，更不提供全局短证书或
严格可提升递降。

## 聚焦验证

~~~bash
PYTHONPATH=reproductions python3 \
  reproductions/type_i_full_box_primitive_edge_uniform_carrier_range.py --verify
~~~

验证器只检查坐标边的 content/depth、\(q=3\) 的 18 个 canonical threshold cases、
最大值以及 \(p=557281\) 的实际 full-box factor-\(2\) 控制；不进行历史扫描。
