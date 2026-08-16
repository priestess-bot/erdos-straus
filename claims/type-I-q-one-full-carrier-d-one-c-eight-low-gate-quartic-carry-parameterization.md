---
kind: claim
claim_id: type-I-q-one-full-carrier-d-one-c-eight-low-gate-quartic-carry-parameterization
title: q=1 容量八 low gate 的四次 carry 商参数化
statement: >-
  在 c=8 high-q source 中，令 D_s=gcd(V,M)，并设实际 V-side prime q 的 direct
  capacity 为 c in {1,...,7}。则 carry quotient
  lambda=(32D_s q+79c)/p 是正整数、q 不整除 lambda、lambda=-c mod16，且
  q 整除显式四次式
  G_c(lambda)=lambda^4-4c lambda^3-27334c^2 lambda^2+
  2471436c^3 lambda-59657719c^4。反之，在 D_s 已按 source residue table 固定，
  p lambda=32D_s q+79c、q>2(p-1) 且 q 整除 G_c(lambda) 的 high-q 数据会强制
  q 整除 V，并恢复该 c 的 direct low gate。因而 low-gate 问题可等价转写为四次
  carry 多项式的素因子与线性 p reconstruction 的耦合；lambda 无全局上界，故这不是
  对 seven-gate residual 的排空、terminal 或 E5 证明。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-q-one-full-carrier-d-one-c-eight-high-q-shared-defect-rigidity
  - type-I-q-one-full-carrier-d-one-c-eight-v-side-direct-m-one-capacity-map
topics:
  - type-I
  - q-one
  - full-carrier
  - c-eight
  - low-gate
  - quartic
  - carry-parameterization
  - source-support
  - proof-boundary
sources:
  - claim: type-I-q-one-full-carrier-d-one-c-eight-high-q-shared-defect-rigidity
    role: fixed-source-defect-D_s
  - claim: type-I-q-one-full-carrier-d-one-c-eight-v-side-direct-m-one-capacity-map
    role: linear-low-capacity-congruence
  - reproduction: reproductions/type_i_q_one_full_carrier_d_one_c_eight_low_gate_quartic_carry_parameterization.py
    role: quartic-identity-and-actual-high-q-control
visibility: public
last_checked: '2026-08-17'
---

# q=1 容量八 low gate 的四次 carry 商参数化

## 1. 从模 \(p\) gate 提取整数 carry 商

保留容量八 high-\(R\) source

\[
p=48s+1,\qquad K=8M,\qquad
V=R(p-1)-p,
\tag{1}
\]

并令

\[
D_s=(V,M).
\tag{2}
\]

设 \(q>2(p-1)\) 是一个实际 \(V\)-side strict raw prime。由
[共享缺陷刚性](type-I-q-one-full-carrier-d-one-c-eight-high-q-shared-defect-rigidity.md)，
endpoint \(a=V/q\) 满足 \((a,M)=D_s\)。若 a-side direct capacity 落在 low gate，
写它为

\[
1\le c\le7.
\tag{3}
\]

已有线性 capacity 式给出

\[
79c+32D_s q\equiv0\pmod p.
\tag{4}
\]

所以可定义唯一正整数

\[
\boxed{
\lambda=\frac{32D_s q+79c}{p}.
}
\tag{5}
\]

这不是另一个自由参数：它精确记录 (4) 的整商。因为 \(p\equiv1\pmod {16}\)，
\(32D_sq\equiv0\pmod {16}\)，从 (5) 还立即有

\[
\boxed{\lambda\equiv-c\pmod {16}.}
\tag{6}
\]

此外，若 \(q\mid\lambda\)，则 (5) 会给 \(q\mid79c\)，但
\(q>2(p-1)\ge8256>79c\)。故

\[
\boxed{(q,\lambda)=1.}
\tag{7}
\]

## 2. source 多项式的四次化

把 \(s=(p-1)/48\) 代入 source-side \(V\) 的闭式，得到

\[
\boxed{
4V=P(p):=
121p^4-396p^3+346p^2+4p-79.
}
\tag{8}
\]

令 \(a_c=79c\)。将 \(p\lambda\equiv a_c\pmod q\) 代入 \(P(p)\lambda^4\)，有

\[
\begin{aligned}
P(p)\lambda^4
&\equiv
121a_c^4-396a_c^3\lambda
+346a_c^2\lambda^2+4a_c\lambda^3-79\lambda^4\\
&=-79G_c(\lambda)
\pmod q,
\end{aligned}
\tag{9}
\]

其中

\[
\boxed{
G_c(X)=
X^4-4cX^3-27334c^2X^2
+2471436c^3X-59657719c^4.
}
\tag{10}
\]

式 (9) 是一个精确多项式恒等式，不依赖 \(D_s\) 或 source 因子分解。

## 3. 正反向等价

在 actual high-\(q\) low-gate 输入上，\(q\mid V\)，故 \(q\mid P(p)\)。由 (7)、(9)
和 \(q\ne79\)，得到

\[
\boxed{q\mid G_c(\lambda).}
\tag{11}
\]

反过来，固定一个 source 参数 \(s\) 及其按 residue table 重算的 \(D_s\)，并假设

\[
p=48s+1,\qquad
p\lambda=32D_s q+79c,
\tag{12}
\]

\[
1\le c\le7,\qquad
q>2(p-1),\qquad
q\text{ 为素数},\qquad
q\mid G_c(\lambda).
\tag{13}
\]

由于 (12)--(13) 同样保证 \(q\nmid\lambda\)、\(q\ne79\)，(9) 反向给出

\[
q\mid P(p)=4V.
\tag{14}
\]

而 \(q\) 是奇素数，故 \(q\mid V\)。high-\(q\) 以及 \(D_s\mid11\cdot41\cdot149\)
排除 \(q\mid M\)，所以 \(v_q(V)>v_q(K)\)，确实恢复一个 strict \(V\)-side label。
最后 (12) 就是 (4)，而 direct capacity 在 \(1,\ldots,p-1\) 中唯一，故它正是
\(c\)。

因此 (11)--(13) 给出 low gate 的正确反向参数化：对每个

\[
c\in\{1,\ldots,7\},\qquad
\lambda\equiv-c\pmod {16},
\tag{15}
\]

先分解 \(G_c(\lambda)\) 的素因子，再以 (12) 重建 \(p\) 并检查 source residue、
roughness、terminal-first 与 typed guards。每个固定 \(\lambda\) 的候选菜单有限；
但 \(\lambda\) 没有在本卡中得到全局上界。

在真实 \(q_\star=103\) rough 域另有 \(p\equiv9\pmod {103}\)，故 (12) 还给

\[
32D_sq+79c\equiv9\lambda\pmod {103}.
\tag{16}
\]

这是一条额外筛核，不是对 (11) 的矛盾。

## 4. 实际非 low-gate 控制

取 high-\(q\) source 的非平凡 defect control

\[
s=116,\quad p=5569,\quad D_s=11,\quad q=578581.
\tag{17}
\]

它的实际 direct capacity 是 \(c=4202\)，不是 (3) 的 low gate；但 (5)、(8)--(10)
对任意 positive capacity 都成立。这里

\[
\lambda=\frac{32\cdot11\cdot578581+79\cdot4202}{5569}=36630,
\tag{18}
\]

并且直接验证

\[
q\mid G_{4202}(36630),
\qquad
36630\equiv-4202\pmod {16}.
\tag{19}
\]

该控制只检验 polynomial transport 和反向整除，不把一个 non-low endpoint 冒充成
low-gate 反例或 E5 edge。

## 5. 边界

本卡没有证明 \(G_c(\lambda)\) 的所有高素因子都不能满足 (12)，也没有构造一条满足
真实 \(q_\star=103\) roughness 的 low-gate endpoint。因此它没有关闭当前 seven-gate
residual，也没有证明 terminal、strict split capacity、typed state admission 或
G/Type I global exit。

它的作用是把“\(q\) 是巨大 \(V\) 的一个因子且命中一个小模 \(p\) 残余”改写为一张
可独立研究的四次因子--线性重建问题。后续若要证明 gate 为空、构造 gate endpoint，
或把 gate 映到 \(c_\Sigma<8\)，都必须使用 (12) 的额外算术，而不能只重复
\(q\bmod p\) 的七项菜单。

聚焦复核：

~~~bash
PYTHONPATH=reproductions python3 \
  reproductions/type_i_q_one_full_carrier_d_one_c_eight_low_gate_quartic_carry_parameterization.py --verify
~~~

复现器重放四次恒等式、(6)、(11) 和一个已有 non-low high-\(q\) raw control；
不扫描参数射线、素数、V 的因子或历史 certificate。
