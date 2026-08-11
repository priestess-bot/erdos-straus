---
kind: claim
claim_id: type-II-p-minus-one-jacobi-odd-kernel-affine-box-relay
title: p-1 因子 Type II 的 Jacobi C2 剥离与奇核有界仿射盒
statement: >-
  设 p=4qr+1、m=4q-1，且 H=<ell mod m: ell|x> 为循环单位子群，|H|=2s、
  s 为奇数，Jacobi 负源非空并且 -1 属于 H。选 H 的生成元 g，写
  ell_i=g^(a_i)、beta_i=a_i mod 2、b_i=(a_i-beta_i)/2。则任意 signed-box
  Type II 目标命中等价于一个奇数 parity 模式 delta 和模 s 的有界线性同余：
  对负源坐标 z_i=delta_i+2u_i、非负源坐标保留 z_i，满足
  sum_(negative) a_i u_i + sum_(positive) b_i z_i =
  (s-1)/2 - sum_(negative) b_i delta_i - (sum delta_i-1)/2 mod s。
  Jacobi C2 投影在负源非空时自动饱和为 {0,1}，所以剩余 F miss 是奇核/完整关系
  的精确 affine-box 障碍；若所有模式盒为空，得到构造性
  JACOBI_ODD_KERNEL_BOX_EMPTY，而不是 SNF 失败或重复的 C2 容量需求。
  p=67369 的 q=7,21,42 三张 F 盒分别在模 9,41,83 上为空。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-p-minus-one-jacobi-source-snf-rank-one-anchor-dichotomy
  - type-II-p-minus-one-jacobi-source-localization-collision-capacity
  - type-II-odd-primary-annihilator-compression-two-primary-terminal
  - type-II-source-fiber-cyclic-primary-digit-terminal
  - type-II-kernel-fourier-source-relation-compatibility
topics:
  - type-II
  - p-minus-one
  - Jacobi-character
  - C2-quotient
  - odd-primary
  - affine-box
  - discrete-log
  - F-state
  - constructive-no-go
  - capacity
  - selector
sources:
  - claim: type-II-p-minus-one-jacobi-source-snf-rank-one-anchor-dichotomy
    role: rank-one-Jacobi-source-and-anchor-compatibility
  - claim: type-II-p-minus-one-jacobi-source-localization-collision-capacity
    role: negative-source-factor-and-signed-box-parity
  - claim: type-II-odd-primary-annihilator-compression-two-primary-terminal
    role: odd-primary-kernel-and-2-primary-interface
  - claim: type-II-source-fiber-cyclic-primary-digit-terminal
    role: primary-box-capacity-boundary
  - reproduction: reproductions/type_ii_p_minus_one_jacobi_odd_kernel_affine_box.py
    role: reduced-odd-box-equivalence-and-p67369-empty-verifier
visibility: public
last_checked: '2026-08-11'
---

# \(p-1\) 因子 Type II 的 Jacobi \(C_2\) 剥离与奇核有界仿射盒

## 1. 循环 Jacobi 状态

设

\[
p=4qr+1,\qquad
m=4q-1,\qquad
x=q(r+1),
\tag{1}
\]

并令

\[
H=\langle \ell\bmod m:\ell\text{ 为 }x\text{ 的素因子}\rangle
\le(\mathbb Z/m\mathbb Z)^\times.
\tag{2}
\]

假设 \(H\) 循环、\(|H|=2s\) 且 \(s\) 为奇数，并且 Jacobi 负源非空。由
rank-one 源 SNF 引理，\(-1\in H\) 时 Jacobi 角色在 \(H\) 上是非平凡同态，
其唯一二阶元正是 \(-1\)。取 \(H\) 的生成元 \(g\)，对 \(x\) 的不同素因子
\(\ell_i\) 写

\[
\ell_i\equiv g^{a_i}\pmod m,
\qquad
0\le a_i<2s.
\tag{3}
\]

由于 Jacobi 角色在 \(g\) 上取 \(-1\)，有

\[
\beta_i=a_i\bmod2\in\{0,1\},
\qquad
b_i=\frac{a_i-\beta_i}{2}\in\mathbb Z.
\tag{4}
\]

负源集合正是

\[
\mathcal N=\{i:\beta_i=1\}.
\tag{5}
\]

令 \(e_i=v_{\ell_i}(x)\)，signed exponent box 为

\[
\mathcal Z=
\prod_i[-e_i,e_i]\cap\mathbb Z.
\tag{6}
\]

向量 \(z\in\mathcal Z\) 对应除子

\[
d(z)=\prod_i\ell_i^{e_i+z_i},
\qquad d(z)\mid x^2.
\tag{7}
\]

## 2. \(C_2\) 剥离定理

Type II 目标同余

\[
d(z)x^{-1}\equiv-1\pmod m
\tag{8}
\]

等价于离散对数同余

\[
\sum_i a_i z_i\equiv s\pmod{2s}.
\tag{9}
\]

令

\[
B(z)=\sum_{i\in\mathcal N}z_i.
\tag{10}
\]

由于 \(a_i=2b_i+\beta_i\)，式 (9) 的左侧为

\[
2\sum_i b_i z_i+B(z).
\tag{11}
\]

目标右侧 \(s\) 为奇数，所以 (9) 必然要求

\[
B(z)\equiv1\pmod2.
\tag{12}
\]

反过来，在 (12) 下令

\[
T(z)=\frac{B(z)-1}{2}\in\mathbb Z.
\tag{13}
\]

由 (9)--(11)，目标同余精确等价于

\[
\boxed{
\sum_i b_i z_i+T(z)
\equiv\frac{s-1}{2}\pmod s.}
\tag{14}
\]

证明只需把 (11) 写成
\[
2\left(\sum_i b_i z_i+T(z)\right)+1
\equiv s\pmod{2s},
\]
再约去因子 2。反向代回同样成立。证毕。

式 (14) 是把已闭合的 Jacobi \(C_2\) 方向剥离后的精确奇核方程；它不是把
Jacobi 角色重新作为一个额外容量收费。

## 3. 奇偶模式到普通奇模有界盒

固定一个奇偶模式

\[
\boldsymbol\delta=(\delta_i)_{i\in\mathcal N}
\in\{0,1\}^{\mathcal N},
\qquad
D_\delta=\sum_{i\in\mathcal N}\delta_i
\text{ 为奇数}.
\tag{15}
\]

对每个负源坐标写

\[
z_i=\delta_i+2u_i,
\qquad
u_i\in
W_i(\delta_i):=
\{u\in\mathbb Z:-e_i\le\delta_i+2u\le e_i\}.
\tag{16}
\]

对 \(i\notin\mathcal N\) 保留

\[
z_i\in[-e_i,e_i]\cap\mathbb Z.
\tag{17}
\]

此时

\[
T(z)=\frac{D_\delta-1}{2}+\sum_{i\in\mathcal N}u_i,
\tag{18}
\]

所以 (14) 化为普通模 \(s\) 的线性盒：

\[
\boxed{
\sum_{i\in\mathcal N}a_i u_i
\;+\!
\sum_{i\notin\mathcal N}b_i z_i
\equiv
C_\delta\pmod s,}
\tag{19}
\]

其中

\[
\boxed{
C_\delta=
\frac{s-1}{2}
-\sum_{i\in\mathcal N}b_i\delta_i
-\frac{D_\delta-1}{2}.}
\tag{20}
\]

于是得到精确有限并：

\[
\boxed{
\{z\in\mathcal Z:d(z)x^{-1}\equiv-1\}
\longleftrightarrow
\bigsqcup_{\substack{\boldsymbol\delta\in\{0,1\}^{\mathcal N}\\
D_\delta\ {\rm odd}}}
\operatorname{Sol}_s(\boldsymbol\delta),}
\tag{21}
\]

其中 \(\operatorname{Sol}_s(\boldsymbol\delta)\) 是 (19) 在 (16)--(17) 边界下的
整数解集。

每个 \(i\in\mathcal N\) 都有 \(e_i\ge1\)，故 Jacobi \(C_2\) 投影本身满足

\[
\{\sum_{i\in\mathcal N}z_i\bmod2:z\in\mathcal Z\}
=\{0,1\}.
\tag{22}
\]

因此负源非空时，空集只能来自奇模盒 (19) 的全部模式均无解，而不能来自
二进制投影不足。

## 4. F 空盒与可构造回执

假设所有奇偶模式的解集为空：

\[
\operatorname{Sol}_s(\boldsymbol\delta)=\varnothing
\quad\text{对每个奇模式 }\boldsymbol\delta.
\tag{23}
\]

则由 (21) 得到完整 signed box 目标 miss，并可输出

\[
\boxed{
\operatorname{JACOBI\_ODD\_KERNEL\_BOX\_EMPTY}
\left(
m,s,\mathcal N,
\{C_\delta,W_i(\delta_i),\operatorname{Sol}_s(\delta)\}
\right).}
\tag{24}
\]

该回执严格排除所有 \(d\mid x^2\) 的目标同余，因而当然排除 \(d<x\) 的
Type II 短证书。它不是 source-SNF 失败：源标签角色已经显式相容；也不是
Jacobi \(C_2\) 容量缺口：式 (22) 已饱和。它是 Jacobi 核内的奇模有限盒 no-go。

若某个模式有解，(16)--(17) 恢复 \(z\)，再由 (7) 构造 \(d(z)\)。若

\[
d(z)<x,
\tag{25}
\]

则 (8) 给出 Type II 短证书；若 \(d(z)\ge x\)，该命中只通过完整 signed-box
门，仍须重新选择 \(d\) 或转交范围分派。故 (19) 的命中是构造性候选，不自动
跳过 Type II 大小门。

## 5. 三组控制

### 5.1 \(p=73,q=2\)：奇核方程有真实命中

取

\[
m=7,\quad H=U(7)=\langle3\rangle,\quad s=3,
\]

\[
\log_3(2)=2,\qquad
\log_3(5)=5.
\]

负源只有 \(5\)，其模式为 \(\delta_5=1\)，式 (19) 为

\[
2u_5+z_2\equiv2\pmod3,
\qquad
u_5\in\{-1,0\},\quad z_2\in[-2,2].
\tag{26}
\]

\(z_2=-2,z_5=-1\)（即 \(d=1\)）给出解并恢复已有 Type II 命中。

### 5.2 \(p=337,q=6\)：跨状态碰撞下仍有命中

取 \(m=23\)、生成元 \(g=5\)、\(s=11\)，并有

\[
\log_5(2)=2,\quad
\log_5(3)=16,\quad
\log_5(5)=1.
\]

负源为 \(5\)，奇核方程为

\[
u_5+z_2+8z_3\equiv5\pmod{11},
\qquad
u_5\in\{-1,0\},
\quad z_2\in[-1,1],\quad z_3\in[-2,2].
\tag{27}
\]

\(z_2=0,z_3=-2,z_5=-1\) 给出 \(d=2\) 的 Type II 命中。

### 5.3 \(p=67369\)：三张 F 的奇核空盒

端点下闭域已经把状态压为 \(q\mid42\)。三个负源可见状态的 reduced boxes 为：

\[
\begin{array}{c|c|c}
q&(m,s)&\text{奇核方程}\\ \hline
7&(27,9)&
u_{29}+u_{83}+8z_7\equiv4\pmod9,\\
21&(83,41)&
28u_{73}+36z_3+4z_7+12z_{11}\equiv27\pmod{41},\\
42&(167,83)&
82u_{67}+20z_2+47z_3+59z_7\equiv42\pmod{83}.
\end{array}
\tag{28}
\]

边界分别为

\[
\begin{array}{c|c}
q&\text{变量范围}\\ \hline
7&
u_{29},u_{83}\in\{-1,0\},\quad z_7\in[-1,1],\\
21&
u_{73}\in\{-1,0\},\quad z_3,z_7,z_{11}\in[-1,1],\\
42&
u_{67}\in\{-1,0\},\quad
z_2,z_3\in[-2,2],\quad z_7\in[-1,1].
\end{array}
\tag{29}
\]

三个有限解集均为空。因此这三张 F 不是 Jacobi C2/SNF 失败，而是明确的
\(\operatorname{JACOBI\_ODD\_KERNEL\_BOX\_EMPTY}\)。结合已有的 gap-\(31\)
Type I terminal，\(p=67369\) 的 terminal-first 分派不变；本引理新增的是
F 空盒的奇核坐标和可复核空证书。

## 6. 选择器接口与边界

对循环 Jacobi 状态，选择器现在可使用如下顺序：

\[
\begin{array}{ll}
\mathcal N=\varnothing
&\longrightarrow \operatorname{JACOBI\_G\_SOURCE\_TRIVIAL},\\
\mathcal N\ne\varnothing,\ -1\notin H
&\longrightarrow \operatorname{JACOBI\_RANK\_ONE\_ANCHOR\_OUTSIDE},\\
\mathcal N\ne\varnothing,\ -1\in H,
\exists\boldsymbol\delta:\operatorname{Sol}_s(\boldsymbol\delta)\ne\varnothing
&\longrightarrow \text{范围门后 Type II candidate/terminal},\\
\mathcal N\ne\varnothing,\ -1\in H,
\forall\boldsymbol\delta:\operatorname{Sol}_s(\boldsymbol\delta)=\varnothing
&\longrightarrow \operatorname{JACOBI\_ODD\_KERNEL\_BOX\_EMPTY}.
\end{array}
\tag{30}
\]

最后一支只能作为 F/odd-kernel 算术负证书，不能自动声称 Type I 或递降。若
odd-kernel 空盒在跨状态 owner 流中产生候选需求，仍需执行真实 source-column
实现、SNF 去重和 E4/E5；本引理只关闭 Jacobi \(C_2\) 与循环奇核的算术描述。

聚焦验证：

~~~bash
python3 reproductions/type_ii_p_minus_one_jacobi_odd_kernel_affine_box.py --verify
~~~

验证器检查公式 (14)--(21) 的逐向量等价、\(p=73,337\) 的命中和
\(p=67369\) 三个 reduced-box 空集，不运行历史范围测试。
