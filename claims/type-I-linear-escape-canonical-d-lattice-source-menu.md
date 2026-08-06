---
kind: claim
claim_id: type-I-linear-escape-canonical-d-lattice-source-menu
title: 线性 escape 的 canonical D-格来源菜单与纤维残余回执
statement: 固定核心素数 p 和 D。对标准 Type II 来源格 A_D={a|D:D/a 平方自由,4aD<p} 与目标格 L_D={(D',A):D'|D,A|D',D'/A 平方自由,4AD'<p}，对每个同时整除 N_a=p+4Da 和 N'_{D',A}=p+4AD' 的素数保留唯一最大 q-进高度，得到有限 canonical 菜单 E_D^can(p)；profile 只能从该容量选择一个前缀，不能把 q,q^2 等重复成独立行。若 A_D 非空，则每个菜单素数都与 4D 互素，因此自动是每个目标 U(4D') 的单位。该菜单对“一跳、保持来源、D-格 Type II source-switch” universe 完备；shared-q ledger 后所有该 universe 中的真实原子来源都出现于菜单。对每个目标纤维，若 canonical unit-source 子群仍不含线性 block escape 目标，则商角色给出 CANONICAL_D_LATTICE_ESCAPE_OBSTRUCTED。该结论不覆盖 raw、外部 F/G alternate 或下一递归层来源。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-linear-escape-primary-source-switch-finite-dispatch
  - type-II-source-fiber-shared-q-ledger
  - type-II-q-prefix-source-crt-fiber-concentration
  - type-II-same-modulus-source-switch-crt-criterion
topics:
- type-I
- linear-source
- escape
- Type-II
- source-switch
- divisor-lattice
- source-complete
- finite-menu
- shared-q
- residual-obstruction
- proof-program
sources:
  - claim: type-II-source-fiber-shared-q-ledger
    role: repeated-q-realization
  - claim: type-II-q-prefix-source-crt-fiber-concentration
    role: common-target-fiber
  - claim: type-II-same-modulus-source-switch-crt-criterion
    role: D-lattice-source-switch-normal-form
  - reproduction: reproductions/type_i_linear_escape_canonical_d_lattice_fixture.py
    role: fixed-D residual scope fixture
visibility: public
last_checked: '2026-08-05'
---

# 线性 escape 的 canonical D-格来源菜单与纤维残余回执

## 1. 声明的 universe

固定核心素数 \(p\) 和正整数 \(D\)，定义标准来源格

\[
\mathcal A_D(p)=
\left\{
a:a\mid D,\quad D/a\text{ 平方自由},\quad 4aD<p
\right\},
\tag{1}
\]

以及一跳目标格

\[
\mathcal L_D(p)=
\left\{
(D',A):
D'\mid D,\quad A\mid D',\quad D'/A\text{ 平方自由},\quad
4AD'<p
\right\}.
\tag{2}
\]

令

\[
N_a=p+4Da,
\qquad
N'_{D',A}=p+4AD'.
\tag{3}
\]

本卡的 universe \(\mathfrak U_D^{(1)}\) 仅包含下列对象：

1. 来源标签来自 \(a\in\mathcal A_D(p)\)；
2. 目标参数来自 \((D',A)\in\mathcal L_D(p)\)；
3. 每个来源因子是 \(N_a\) 的因子，并经 shared-q ledger 合成为整除
   \(N'_{D',A}\) 的实际整数幂块；
4. 直接 Type II 正规形先要求混合因子
   \(h\equiv-1\pmod {4D'}\)；若还需要保持旧 \(D\) 的来源语义，再额外检查
   \(h\equiv-1\pmod {4D}\)。

它不包括 raw Type II 因子、未由 (1) 产生的外部 F/G alternate，或递归后继上的新来源。
这些分支仍必须由各自的终端或菜单处理。

## 2. 规范原子菜单和单位引理

对每条来源—纤维—素数 route 定义其最大可用高度

\[
e_{a,D',A,q}=
\min\{v_q(N_a),v_q(N'_{D',A})\}.
\tag{4}
\]

只保留 \(e_{a,D',A,q}\ge1\) 的 route，得到 canonical 原子菜单

\[
\mathcal E_D^{\mathrm{can}}(p)=
\left\{
(a,D',A,q,e_{a,D',A,q}):
\begin{array}{l}
a\in\mathcal A_D(p),\quad (D',A)\in\mathcal L_D(p),\\
q\text{ 为素数},\quad e_{a,D',A,q}\ge1
\end{array}
\right\}.
\tag{5}
\]

对固定的 \((a,D',A,q)\)，菜单恰有一个 route。profile 至多从它选择一个前缀
\[
1\le m\le e_{a,D',A,q};
\tag{6}
\]
不能同时把 \(q,q^2,\ldots,q^e\) 当作独立块。多个来源的同一 q 再由 shared-q
ledger 合并。

若 \(\mathcal A_D(p)\ne\varnothing\)，则

\[
\boxed{\gcd(N_a,4D)=1\quad(a\in\mathcal A_D(p)).}
\tag{7}
\]

事实上，(1) 给出 \(D<p/4\)。\(N_a\) 为奇数；若 \(r\mid D\) 为素数，则

\[
N_a\equiv p\not\equiv0\pmod r,
\tag{8}
\]

因为 \(r\le D<p\) 而 \(p\) 是素数。于是 (7) 成立。特别地，(5) 中所有 \(q\)
都不整除 \(4D\)，故也不整除任意 \(4D'\)。canonical 菜单中没有
\(\mathrm{SOURCE\_UNIT\_GROUP\_NONUNIT}\) 行；该回执只可能来自外部、未闭合来源。

菜单有限。更精确地，

\[
|\mathcal A_D(p)|\le\tau(D),
\qquad
|\mathcal L_D(p)|\le\sum_{D'\mid D}\tau(D')\le\tau(D)^2,
\tag{9}
\]

而 \(N_a<2p\)，所以

\[
\boxed{
|\mathcal E_D^{\mathrm{can}}(p)|
\le \tau(D)^3\lfloor\log_2(2p)\rfloor.
}
\tag{10}
\]

这个上界甚至把每个 route 的所有可选前缀高度都计入；实际菜单每个
\((a,D',A,q)\) 只保留一个最大高度。

## 3. 一跳 D-格的 source-completeness

设一个 \(\mathfrak U_D^{(1)}\) source-switch 使用来源
\((a_i,q_i^{m_i})\)，并在目标 \(f=(D',A)\) 上回译为实际混合因子 \(h\)。由定义，

\[
q_i^{m_i}\mid N_{a_i},
\qquad
q_i^{m_i}\mid h\mid N'_{D',A}.
\tag{11}
\]

令
\[
e_i=e_{a_i,D',A,q_i}.
\]
由 (11) 得 \(m_i\le e_i\)，故

\[
1\le m_i\le
\min\{v_{q_i}(N_{a_i}),v_{q_i}(N'_{D',A})\}=e_i,
\tag{12}
\]

故 \((a_i,D',A,q_i,e_i)\in\mathcal E_D^{\mathrm{can}}(p)\)，而 \(m_i\) 是该
route 的一个合法前缀。这证明每个真实原子来源行都在菜单中。

反过来，菜单行已经精确保存了来源、目标纤维、素数和最大合法前缀。选定行组后，
shared-q ledger 决定每个 q 的真实可用高度；通过 CRT、范围、平方自由、同一纤维、
\(h\equiv-1\pmod {4D'}\) 和正规形门的行组，正是 \(\mathfrak U_D^{(1)}\) 中可回译的
source-switch。故

\[
\boxed{
\mathcal E_D^{\mathrm{can}}(p)
\text{ 对 }\mathfrak U_D^{(1)}
\text{ 是有限且 source-complete 的。}
}
\tag{13}
\]

“complete”在 (13) 中只量化 (1)--(3) 的 D-格 universe；它不能删除外部来源的
\(\mathrm{SOURCE\_UNCLOSED}\) 回执，也不能跳过 raw fallback。

## 4. 每纤维 residual escape 回执

设一个线性 escaped state 已给出单位群 \(G_R=U(R)\)、两块子群
\(L_{\rm blk}\le G_R\)，以及 escape 目标
\(\Delta_Q\in G_R\)。对每个 \(f=(D_f,A_f)\in\mathcal L_D(p)\)，令

\[
J_f=
\left\langle
L_{\rm blk},\
q\bmod R:
(a,D_f,A_f,q,e)\in\mathcal E_D^{\mathrm{can}}(p),\
q\nmid R
\right\rangle
\le G_R.
\tag{14}
\]

每个能映入 \(U(R)\) 的 canonical D-格来源积都落在 \(J_f\)；\(J_f\) 是该纤维内
可实现来源子群的一个显式上界。因此若

\[
\Delta_Q\notin J_f,
\tag{15}
\]

有限阿贝尔商 \(G_R/J_f\) 上存在一个角色在 \(\Delta_Q\) 的像上非平凡、在该纤维
所有 canonical source 上平凡。记录

\[
\mathrm{CANONICAL\_D\_LATTICE\_ESCAPE\_OBSTRUCTED}
=(f,J_f,\Delta_Q,\chi_f).
\tag{16}
\]

若 (15) 对所有 \(f\in\mathcal L_D(p)\) 成立，则整个
\(\mathfrak U_D^{(1)}\) 被严格排除为当前 escape 的支付来源。这个回执不排除其它
\(D\)、raw、Type I 或外部 F/G source。

## 5. 固定原始 D 层不必支付 escape

下面给出一个严格的固定层边界，而不是递归 no-go。取

\[
p=57{,}399{,}241,\qquad R=59,\qquad D=41.
\tag{17}
\]

在线性状态 \(a=956{,}654,s=1\) 中，

\[
U^\circ=15,\qquad
V^\circ=56{,}442{,}587=2693\cdot20959,
\]
\[
K=846{,}638{,}805=3\cdot5\cdot2693\cdot20959.
\tag{18}
\]

\(\langle15\rangle\) 是 \(\mathbb F_{59}^{\times}\) 的 29 阶二次剩余子群，而
\(2693\equiv38\) 和 \(20959\equiv14\pmod {59}\) 都在非剩余陪集。因此对声明的
\(C_2=\mathbb F_{59}^{\times}/\langle15\rangle\) 秩一需求，可取
\(\delta=38\langle15\rangle\) 作为非平凡代表。

这里

\[
\mathcal A_{41}(p)=\{1,41\},
\]
\[
N_1=57{,}399{,}405=3\cdot5\cdot7\cdot546661,
\qquad
N_{41}=57{,}405{,}965=5\cdot2861\cdot4013.
\tag{19}
\]

(19) 的所有带标签素因子在模 \(59\) 下都是二次剩余。因此以这些原始
\(D=41\) 来源构成的每个 canonical 菜单行都在 \(\langle15\rangle\) 中，固定层菜单
对 \(\delta\) 的像秩为零，不能支付该声明的秩一需求。

这不能升级为整个递归 D-格失败：在下一层 \(D'=A=1\) 上，

\[
p+4=57{,}399{,}245=5\cdot11{,}479{,}849,
\qquad
11{,}479{,}849\equiv42\pmod {59},
\tag{20}
\]

且后一个因子为二次非剩余。它是下层新来源，不属于 (19) 的一跳原始
\(D=41\) source universe。故 (17) 反驳的只是“任一固定原始 D 菜单自动覆盖
escape”的推断；它不排除下一层、raw、Type I 或其它 \(D\)。

常数规模复现见
[固定 D canonical source residual fixture](../reproductions/type_i_linear_escape_canonical_d_lattice_fixture.py)。

## 6. 研究边界

(13) 消除了固定 D、一跳 D-格分派中的“来源未枚举”缺口；(16) 还会把不能覆盖的
情形转成明确的有限角色/SNF 残余，而不是含糊的失败。决定性的剩余问题是证明真实
linear escape 总能落在某个可提升的 D-格 universe，或为 D-格 residual 建立一个
不同的 Type I/II、raw 或严格 E1--E5 出口。
