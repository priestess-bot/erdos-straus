---
kind: claim
claim_id: type-I-odd-primary-component-torsion-rank-collapse
title: 奇主阶相位的完整分量秩坍缩与严格重图表
statement: >-
  在核心 Type I Jacobi F 图表中，对固定奇素数 ell，把所有 Jacobi-negative
  记录规范抽取出的精确 ell 阶相位生成 F_ell 空间 V_ell<=U(R)[ell]。
  对 R 的每个完整素数幂 q^e，局部 ell-torsion U(q^e)[ell] 的维数至多一。
  因而 dim_Fell(V_ell)>=2 时，任取一个完整分量的投影都有非零核；该核中的
  相位由原记录的显式整数线性组合给出，且在该完整分量上为 1。它触发
  component-kernel 的严格 R 降低重图表，并沿既有 CRT_DESCENT 势通过 E1--E5。
  所以所有 terminal-first 后未由 component rechart 消解的 odd-primary full-component
  分支都必须满足 V_ell 为一维，且其唯一非零相位在每个完整分量上均非平凡。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-odd-primary-component-kernel-crt-rechart-descent
  - type-I-core-jacobi-punctured-kernel-primary-selector
  - denominator-escape-state-contract
topics:
  - type-I
  - jacobi
  - odd-primary
  - torsion-rank
  - CRT
  - rechart
  - well-founded-descent
  - E1-E5
  - proof-program
sources:
  - claim: type-I-odd-primary-component-kernel-crt-rechart-descent
    role: exact-primary-extraction-and-component-rechart
  - reproduction: reproductions/type_i_odd_primary_component_torsion_rank_collapse.py
    role: focused-rank-two-combination-and-rechart-control
visibility: public
last_checked: '2026-08-12'
---

# 奇主阶相位的完整分量秩坍缩与严格重图表

## 1. 带来源的 ell-torsion 空间

设核心图表满足

\[
p\equiv1\pmod {24},\qquad R\equiv3\pmod4,\qquad4K=pR+1,
\tag{1}
\]

并固定一个奇素数 \(\ell\)。对每条 Jacobi-negative 记录 \(z\)，写

\[
\Phi(z)=-s_z,\qquad s_z\in\ker\chi_R,
\qquad\ell^{a_z}\Vert\operatorname{ord}(s_z),
\tag{2}
\]

只保留 \(\ell\mid\operatorname{ord}(s_z)\) 的记录。令

\[
k_z=\frac{\operatorname{ord}(s_z)}{\ell^{a_z}},\qquad
\delta_z=
\begin{cases}
1,&2\mid k_z,\\
2,&2\nmid k_z,
\end{cases}
\tag{3}
\]

并定义带来源的相位向量与其核关系

\[
\mu_z=\delta_z\ell^{a_z-1}k_z z,\qquad
\omega_z=\Phi(\mu_z),\qquad
\lambda_z=\ell\mu_z.
\tag{4}
\]

既有奇主阶提取给出

\[
\operatorname{ord}_R(\omega_z)=\ell,\qquad
\Phi(\lambda_z)=1.
\tag{5}
\]

因此所有 \(\omega_z\) 位于

\[
U(R)[\ell]:=\{u\in U(R):u^\ell=1\}.
\tag{6}
\]

这个群的乘法可以按 \(\mathbb F_\ell\) 加法书写。定义由**实际记录**生成的
相位空间

\[
\boxed{V_\ell=\langle\omega_z:\ell\mid\operatorname{ord}(s_z)\rangle
\le U(R)[\ell].}
\tag{7}
\]

式 (7) 不是抽象角色空间：若

\[
\omega=\prod_z\omega_z^{c_z}\ne1,\qquad c_z\in\{0,\ldots,\ell-1\},
\tag{8}
\]

则明示的整数向量

\[
\mu=\sum_zc_z\mu_z,\qquad\lambda=\ell\mu
\tag{9}
\]

满足 \(\Phi(\mu)=\omega\) 与 \(\Phi(\lambda)=1\)。这就是组合相位的 E1
来源回执；即使 \(\mu\) 落在原指数盒外，它也不是无来源的单位群元素。

## 2. 每个完整分量最多容纳一维 ell-torsion

写

\[
R=\prod_{i=1}^tq_i^{e_i}.
\tag{10}
\]

CRT 投影限制为

\[
\pi_i:V_\ell\longrightarrow U(q_i^{e_i})[\ell].
\tag{11}
\]

对奇素数幂 \(q^e\)，\(U(q^e)\) 是循环群，故其 \(\ell\)-torsion 要么平凡，
要么同构于 \(C_\ell\)。所以

\[
\boxed{\dim_{\mathbb F_\ell}U(q_i^{e_i})[\ell]\le1.}
\tag{12}
\]

若 \(\dim_{\mathbb F_\ell}V_\ell\ge2\)，则由秩—零化度，对任意固定 \(i\)

\[
\dim\ker\pi_i
\ge\dim V_\ell-1
\ge1.
\tag{13}
\]

选取 \(1\ne\omega\in\ker\pi_i\)。它在全局仍有精确 \(\ell\) 阶，却满足

\[
\omega\equiv1\pmod {q_i^{e_i}}.
\tag{14}
\]

因此 (8)--(9) 给出的 \(\mu,\lambda\) 不但保留显式来源，还让 \(R\) 的完整
component-kernel 至少含 \(q_i^{e_i}>1\)。

## 3. 组合相位触发严格重图表

对 (14) 的 \(\omega\)，定义

\[
R_0=\prod_{q^e\Vert R,\ \omega\equiv1\ (\bmod q^e)}q^e,
\qquad R_1=R/R_0.
\tag{15}
\]

于是 \(R_0>1\)、\((R_0,R_1)=1\)，且 \(R_1>1\)，因为 \(\omega\ne1\pmod R\)。
唯一满足 \(R_*\equiv3\pmod4\) 的因子 \(R_*\in\{R_0,R_1\}\) 满足

\[
1<R_*<R,\qquad
K_*=\frac{pR_*+1}{4},\qquad
K=\frac R{R_*}K_*-\frac{R/R_*-1}{4}.
\tag{16}
\]

回执采用

```text
core_odd_primary_component_torsion_rank_rechart_v1
```

并由下列数据通过状态合同：

| 门 | 证明数据 |
|---|---|
| E1 | 所有参与的负记录、\(c_z\)、式 (4)、(8)--(9) 与 \(\operatorname{ord}(\omega)=\ell\) |
| E2 | 式 (14)--(16) 的完整分量核、\(R_*\) 与 \(K_*\) |
| E3 | 从整数重算组合相位、局部分量、目标因子分解和 hit/F/G 类型 |
| E4 | \(W_S=W_T=\operatorname{Sol}(4,p)\)，\(w\mapsto w\) |
| E5 | 已有不可逆 `CRT_DESCENT` phase 中 \((\epsilon_{\rm CRT},R)\) 的严格下降 |

所以

\[
\boxed{\dim_{\mathbb F_\ell}V_\ell\ge2
\quad\Longrightarrow\quad
\text{terminal 或严格可提升的 }R\text{ 下降}.}
\tag{17}
\]

取逆否命题可得当前 odd-primary 的精确残余约束：在 terminal-first 后，若所有
component-kernel、torsion-square-peel 和 \(p+1\) 出口都没有命中，则每个仍活跃的
\(\ell\) 都必须满足

\[
\boxed{
\dim_{\mathbb F_\ell}V_\ell=1,
\quad\ell\nmid R,
\quad\text{其每个非零元在每个完整 }q^e\Vert R\text{ 上都非平凡}.}
\tag{18}
\]

最后一项并不是“无解”断言；它精确说明任何后续 owner/source-map 或 adaptive-gap
构造只能处理单一、全分量可见的 \(\ell\)-方向。

## 4. 真实秩二控制：\(p=73,R=63,\ell=3\)

\[
K=1150=2\cdot5^2\cdot23.
\]

下列两条负记录各自都在 \(9\) 和 \(7\) 两个完整分量上非平凡：

\[
\begin{array}{c|c|c|c|c}
z&\Phi(z)&s_z&\mu_z&\omega_z\\
\hline
(0,1,0)&5&58&(0,2,0)&25\\
(1,1,-1)&47&16&(2,2,-2)&4
\end{array}
\tag{19}
\]

在 \(U(9)[3]\times U(7)[3]\) 中，以最小非平凡根为局部基，二者的坐标为

\[
(2,2),\qquad(1,2)\in\mathbb F_3^2,
\tag{20}
\]

所以已经张成二维空间。取其差，得到

\[
\mu=(-2,0,2),\qquad
\omega=25\cdot4^{-1}=22\pmod {63},\qquad
\Phi(3\mu)=1.
\tag{21}
\]

这里 \(22\equiv1\pmod7\)、\(22\not\equiv1\pmod9\)，故

\[
R_0=7,\qquad R_1=9,\qquad R_*=7,\qquad K_*=128.
\tag{22}
\]

这给出由两个 individually full-support 记录组合而来的严格 \(63\to7\) 重图表。
它验证的是秩坍缩的新增路径，而非重复使用一个原本已有 component-kernel 的单记录。

## 聚焦验证

```bash
python3 reproductions/type_i_odd_primary_component_torsion_rank_collapse.py --verify
```

验证器只重算上述真实 F 状态的两条记录、局部 \(3\)-torsion 坐标、秩二、组合相位、
核关系和 \(63\to7\) 的中心恒等式；不运行历史扫描。
