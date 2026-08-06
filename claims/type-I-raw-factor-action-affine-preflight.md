---
kind: claim
claim_id: type-I-raw-factor-action-affine-preflight
title: raw 因子作用到共同仿射相位图的可积性门
statement: 对一个由实际 raw 因子边组成的连通物理菜单，若 row-to-anchor 映射要以同一个因子作用承载共同仿射标签，则锚定相位差必须是 raw 因子自由群同态的一维势；这当且仅当该因子作用杀死所有有符号闭路词。特别地，同因子菱形的离散曲率必须为零，偏移 c 和单位斜率 u 都不能修复非零曲率。p=5281 的 Jacobi-odd 物理菱形中，单独用 tail t 的 7、13、29-primary 相位曲率分别为 2、11、28，故严格排除 tail-only 的 factor-local affine map；派生组合相位 M t^(-1) K^(-1)=delta 则给出一个可积的抽象 anchor 图，但不替代物理行的 (M,t) 账本。该结论为使用 raw transition 证明 source-map 的必要门，不提供 F 锚点、物理整数标签、E2、E4、E5 或 selector edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-jacobi-odd-p5281-physical-row-ledger
  - type-I-g-anchor-marked-raw-peeling-calculus
  - type-I-anchored-affine-phase-tree-capacity
  - type-I-f-target-involution-fourier-phase-collapse
topics:
  - type-I
  - G-state
  - source-map
  - raw-transition
  - affine-phase
  - q-primary
  - cocycle
  - row-to-anchor
  - proof-boundary
sources:
  - claim: type-I-g-anchor-jacobi-odd-p5281-physical-row-ledger
    role: physical-raw-diamond-and-marked-rows
  - claim: type-I-anchored-affine-phase-tree-capacity
    role: conditional-affine-capacity-interface
  - reproduction: reproductions/type_i_raw_factor_action_affine_preflight.py
    role: raw-factor-curvature-and-integrability-control
visibility: public
last_checked: '2026-08-07'
---

# raw 因子作用到共同仿射相位图的可积性门

## 1. Raw-compatible affine map

令 \(\Gamma\) 是一个弱连通的有向 physical raw 图，顶点集为 \(V\)，边

\[
e:v\longrightarrow w
\]

带 raw 素因子标签 \(r(e)\)。反向走边记为 \(-[r(e)]\)。令

\[
F_\Gamma=\mathbb Z^{\{\mathrm{raw\ factors}\}}
\]

是因子的自由加法群，\(L_\Gamma\subset F_\Gamma\) 是所有无向闭路的带符号因子词
生成的 cycle lattice。固定 \(A=\mathbb Z/q^k\mathbb Z\)。

单有逐行 AAL 数据

\[
j(v)\in J_t,\qquad
s_v\equiv c+u\gamma_{j(v),k}\pmod {q^k}
\tag{1}
\]

并未约束 raw 图；若 \(j(v)\) 可逐行任意选择，边和菱形没有信息。若要以 raw
transition 作为 `row_to_anchor_map` 的 source 证据，必须额外存在

\[
\alpha\in\operatorname{Hom}(F_\Gamma,A)
\tag{2}
\]

使每条边满足

\[
\boxed{
\gamma_{j(w),k}-\gamma_{j(v),k}
=\alpha([r(e)])\pmod {q^k}.
}
\tag{3}
\]

于是 \(s_w-s_v\equiv u\alpha([r(e)])\pmod {q^k}\)。称 (3) 为
`raw_factor_action_compatibility`。它是使用 raw 图论证共同仿射 source map 的附加门，
不改变不使用 raw 动作语义的纯容量不等式。

## 2. 可积性定理

给定 (2)，存在顶点势

\[
\beta:V\longrightarrow A,\qquad
\beta(w)-\beta(v)=\alpha([r(e)])
\tag{4}
\]

当且仅当

\[
\boxed{\alpha(L_\Gamma)=0.}
\tag{5}
\]

**证明。** 若 (4) 成立，沿闭路求和左侧望远镜相消，故 (5) 必要。反之任选根
\(v_0\) 与 \(\beta(v_0)\)，按任一路径的有向因子词积分定义 \(\beta(v)\)。两条
路径之差属于 \(L_\Gamma\)，故 (5) 保证定义无关；逐边延长即得 (4)。证毕。

特别地，对菱形

\[
v_0\xrightarrow{a}v_a\xrightarrow{b}v_{ab},\qquad
v_0\xrightarrow{b}v_b\xrightarrow{a}v_{ab},
\tag{6}
\]

必须有

\[
\boxed{
\kappa_\beta=
\beta(v_{ab})-\beta(v_b)-\beta(v_a)+\beta(v_0)=0.
}
\tag{7}
\]

这等价于两条同因子 \(a\) 边有同一个相位增量。对 (1)，
\(\kappa_s=u\kappa_\beta\)：\(c\) 消失且 \(u\) 是单位，均不能修复非零曲率。

## 3. p=5281 的 tail-only 曲率证书

采用已有 physical ledger

\[
p=5281,\quad R=5279,\quad K=6969600,\quad
Q=2639=7\cdot13\cdot29,
\tag{8}
\]

其菜单和完整 menu 内 raw 菱形是

\[
\mathcal D^-=\{7,91,203,2639\},
\qquad
7\xrightarrow{13}91\xrightarrow{29}2639,
\quad
7\xrightarrow{29}203\xrightarrow{13}2639.
\tag{9}
\]

四条 row 的必要标记为

\[
\begin{array}{c|rrrr}
\delta&7&91&203&2639\\ \hline
M_\delta&278784&6969600&2323200&2323200\\
t_\delta&181&5221&1751&1759.
\end{array}
\tag{10}
\]

这里 \(7\) 是 \(U(5279)\) 的本原根，
\(5278=2\cdot7\cdot13\cdot29\)。令
\(\eta_\ell(7^z)=z\pmod\ell\)，其中
\(\ell\in\{7,13,29\}\)。若只用 tail 相位

\[
\beta_t(\delta)=\eta_\ell(t_\delta),
\tag{11}
\]

则

\[
\begin{aligned}
D_t
&=t_{2639}t_7(t_{91}t_{203})^{-1}
\equiv1267\equiv7^{492}\pmod {5279},\\
\kappa_{\beta_t}&=492\pmod\ell.
\end{aligned}
\tag{12}
\]

故

\[
\boxed{
\kappa_{\beta_t}\equiv2\pmod7,\qquad
11\pmod{13},\qquad
28\pmod{29}.
}
\tag{13}
\]

三层均非零。因此不存在由 \(t\bmod R\) 的非平凡 \(7\)、\(13\) 或
\(29\)-primary 角色得到的 factor-local raw affine map；这不是换 \(c,u\) 或
同阶角色可以修复的缺数据问题。

## 4. 组合 factor phase 的可积修复

该账本还严格满足

\[
M_\delta t_\delta^{-1}\equiv K\delta\pmod R.
\tag{14}
\]

所以派生的组合相位

\[
\vartheta_\delta=M_\delta t_\delta^{-1}K^{-1}\equiv\delta\pmod R
\tag{15}
\]

给出

\[
\beta_{\rm full}(\delta)=\eta_\ell(\vartheta_\delta)
=\eta_\ell(\delta),
\qquad
\beta_{\rm full}(q\delta)-\beta_{\rm full}(\delta)=\eta_\ell(q)
\tag{16}
\]

于每条 (9) 的边。故 (5) 成立，菱形曲率为零。

这是一个明确的**抽象** anchor realization：取

\[
H=U(5279),\quad\operatorname{im}\phi=H,\quad t_0=1,
\quad J=\{\delta^{-1}:\delta\in\mathcal D^-\},
\tag{17}
\]

并把 row \(\delta\) 送至 \(j_\delta=\delta^{-1}\)。对
\(\psi_\ell(7)=\zeta_\ell\)，有

\[
\psi_\ell(j_\delta)=\zeta_\ell^{-\eta_\ell(\delta)},
\qquad
\gamma_{j_\delta,1}=\eta_\ell(\delta).
\tag{18}
\]

所以 \(c=0,u=1\) 的有限群仿射式与 raw factors 相容。\(\vartheta\) 只是通过
factor-action 门所需的组合相位投影：它不能替代无损 physical row 的 \((M,t)\)、因子
分解或 carry 账本。现有菜单中 \(\vartheta=\delta\) 可作为一个派生标记使用，但未来
表只有在已证明可从保存编码恢复 raw transition 和物理 row 时，才可作同样压缩。

## 5. 选择器边界

(17)--(18) 只是 marked-row 群论构造。这个控制仍是 G/Jacobi 二次菜单、
`terminal_preempted`，没有实际 F 型 q-primary anchor、物理整数标签区间、carry、
E4 或 E5。因此其状态仍为

```text
raw_factor_action_compatibility = verified (full mark only)
tail_only_status                = obstructed
aal_status                      = ANCHORED_PHASE_MAP_UNCLOSED
recursive_edge_eligible         = false
```

未来若用 raw paths 论证 F/奇 \(q\) 的 `row_to_anchor_map`，须先通过 (5) 并保留
完整 marked row。它不排除独立、不使用 raw 动作的 source-map；但后者不能从 raw
菜单的边完整性推出。

窄复现：

```bash
python3 reproductions/type_i_raw_factor_action_affine_preflight.py --verify
```
