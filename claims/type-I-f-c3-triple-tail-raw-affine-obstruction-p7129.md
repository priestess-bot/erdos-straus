---
kind: claim
claim_id: type-I-f-c3-triple-tail-raw-affine-obstruction-p7129
title: p=7129 F 型 c=3 三尾的 suffix 正控制、source-root p-edge 门与窄障碍
statement: 对 p=7129、R=30879、K=55034098 的真实 F 型 c=3 even-tail control，三条带精确尾 nu=4,2,1 的同一 determinant 行由两条实际 raw 2-边连接。完整中心层 J_full={2^a7^b509^c7723^d:a,b,c,d in [-1,1]} 有 |J_full|=81、平凡稳定子；取 theta=-1 时，j_4=4C、j_2=2C、j_1=C 给出 q=3、23 上的 suffix-local 正 q-affine 控制。可是，既有 declared source-root raw tree 的首条 p=7129 边强制 J_full 与 pJ_full 相交，而有限 CRT 差分证书给出该交为空。另 p=7129 已有直接 Type II 终端 4/7129=1/2037+1/14258+1/29043546，故 selector 状态为 terminal_preempted。原有两个窄负结论仍成立：仅在未约化 H=U(R)、P=1 中，自然 raw phase 不能作 q=3 或 23 的 q-coprime anchor，且 identity abstract-label ansatz j_nu=s_nu=nu 不满足共同仿射律。本卡不构造 integer labels、carry/E2、E4/E5、selector edge 或全局无解结论，也不排除另一 source word、root policy、fixed layer、稳定子商或跨图表 map。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-c3-even-tail-root-entry-admission-boundary
  - type-I-anchored-affine-phase-tree-capacity
  - type-I-raw-factor-action-affine-preflight
  - type-I-fg-raw-transcript-persistent-ledger-carry-core
topics:
  - type-I
  - F-state
  - c3
  - raw-transition
  - even-tail
  - affine-phase
  - q-primary
  - centered-fixed-layer
  - source-root-membership
  - terminal-first
  - carry-core
  - anchor-obstruction
  - row-to-anchor
  - proof-boundary
sources:
  - claim: type-I-g-anchor-c3-even-tail-root-entry-admission-boundary
    role: c3-even-tail-physical-row-and-root-receipt-interface
  - claim: type-I-anchored-affine-phase-tree-capacity
    role: q-coprime-anchor-and-common-affine-law-contract
  - claim: type-I-fg-raw-transcript-persistent-ledger-carry-core
    role: local-single-row-carry-core-boundary
  - reproduction: reproductions/type_i_f_c3_triple_tail_raw_affine_obstruction_p7129.py
    role: bounded-physical-row-fixed-layer-terminal-and-affine-verifier
visibility: public
last_checked: '2026-08-07'
---

# p=7129 F 型 c=3 三尾的 suffix 正控制、source-root p-edge 门与窄障碍

## 1. 固定的 F 型 physical control

取

\[
p=7129,
\qquad R=30879,
\qquad M=7723,
\qquad C=7126,
\qquad K=MC=55034098.
\tag{1}
\]

它满足

\[
p\equiv1\pmod {24},\qquad
R=4M-13,
\qquad pR+1=4K,
\tag{2}
\]

以及 c=3 determinant

\[
d=p-C=3,
\qquad n=4M-R=13,
\qquad pn=4Md+1.
\tag{3}
\]

这里

\[
K=2\cdot7\cdot509\cdot7723.
\tag{4}
\]

在由 (4) 的因子指数 \([-1,1]^4\) 给出的有限中心盒中，\(-1\) 没有表示；但

\[
2^{-2}7^0 509^{-5}7723^8\equiv-1\pmod R.
\tag{5}
\]

故经有限盒逐项复核，此 control 是 F 型，且一个盒外 witness 是

\[
(-2,0,-5,8).
\tag{6}
\]

本卡只研究 (1) 的三个 exact-tail mark，既不把 F witness 解释成 raw source map，
也不把它当作 selector 的充分条件。

## 2. 三条真实 determinant 行与两条 raw 边

对每个 \(\nu\in\{4,2,1\}\)，在有序 m=1 节点中选择 \(\nu C\) 一侧，并保留

\[
(C,M,\nu,d,n)=(7126,7723,\nu,3,13).
\tag{7}
\]

这是实际 physical row：

\[
(\nu C,K)=C,
\qquad K/C=M,
\tag{8}
\]

而 (3) 对三行都成立。相应节点和 raw 边为

\[
\begin{aligned}
(R-4C,4C,1)&=(2375,28504,1)
 \xrightarrow{\,2\,}(14252,16627,1)=(2C,R-2C,1),\\
(2C,R-2C,1)&=(14252,16627,1)
 \xrightarrow{\,2\,}(7126,23753,1)=(C,R-C,1).
\end{aligned}
\tag{9}
\]

两步的 shift 都是 \(1\)，gcd reduction 都是 \(1\)。更具体地，

\[
v_2(4C)=3>v_2(K)=1,
\qquad v_2(2C)=2>v_2(K)=1,
\tag{10}
\]

且每步的非选坐标及 \(R\) 都与 \(2\) 互素。因此 (9) 是实际的严格容量、unit
condition 均成立的 ordered raw transcript，而不是由 endpoint 倒推的形式尾链。

## 3. 单位群与可用的奇 primary 层

有

\[
R=3^2\cdot47\cdot73,
\qquad
U(R)\cong C_6\times C_{46}\times C_{72},
\tag{11}
\]

其中可分别取 \(2\bmod9\)、\(5\bmod47\)、\(5\bmod73\) 为三个循环因子生成元。
实际 F 支撑并非只投影到这些因子：验证器检查了三个隔离 CRT 生成元的短词

\[
\begin{array}{c|c|c}
\text{support word in }(2,7,509,7723)&\text{CRT components modulo }(9,47,73)&\text{residue modulo }R\\ \hline
(1,10,10,2)&(2,1,1)&17156\\
(9,0,3,12)&(1,5,1)&28252\\
(6,3,0,10)&(1,1,5)&26650.
\end{array}
\tag{12}
\]

因此

\[
H:=\langle2,7,509,7723\rangle=U(R).
\tag{13}
\]

特别地，

\[
|U(R)|=19872=2^5\cdot3^3\cdot23.
\tag{14}
\]

所以 \(q=3\) 与 \(q=23\) 都有 primary 角色，且都可选成在 raw factor \(2\)
上非平凡。一个明确的指数写法是

\[
\eta_3(u)=\log_2(u\bmod9)\pmod3,
\qquad
\eta_{23}(u)=\log_5(u\bmod47)\pmod{23}.
\tag{15}
\]

验证器给出

\[
\eta_3(2)=1\pmod3,
\qquad
\eta_{23}(2)=18\pmod{23},
\tag{16}
\]

故二者都满足 \(\psi_q(2)\ne1\)。这只建立该 F control 中可使用的角色层，
不建立任何 source map。

## 4. 未约化自然 raw phase 不能充当 q-coprime anchor

由于 \(R=4M-13\)，从 (9) 的 c=3 tail 自然得到的 phase mark 可写为

\[
\Theta_\nu=-13\nu^{-1}\pmod R.
\tag{17}
\]

它完全由 fixed raw tail 与 determinant 归一化给出：

\[
\begin{array}{c|c|c}
\nu&\Theta_\nu&\operatorname{ord}_{U(R)}(\Theta_\nu)\\ \hline
4&23156=-M&1656=2^3\cdot3^2\cdot23\\
2&15433=-2M&552=2^3\cdot3\cdot23\\
1&30866=-13&1656=2^3\cdot3^2\cdot23.
\end{array}
\tag{18}
\]

并且 raw \(2\)-边正好给出

\[
\Theta_2\equiv2\Theta_4,
\qquad
\Theta_1\equiv2\Theta_2\pmod R.
\tag{19}
\]

现在只固定未约化的自然候选模型

\[
H=U(R),\qquad P=\{1\}.
\tag{20}
\]

以 \(a\) 表示 AAL anchor，避免与 physical tail \(\nu\) 混淆。锚定仿射相位
合同要求 \(\operatorname{ord}_H(a)\) 与所用奇素数 \(q\) 互素。若尝试取
\(a=\Theta_\nu\)，则 (18) 对 \(q=3\) 和 \(q=23\) 都违反该必要条件。因此得到的是
一个严格限定的候选锚点障碍：

\[
\boxed{H=U(R),\ P=1:\quad \Theta_\nu\text{ 不能作为 }q\in\{3,23\}\text{ 的 q-coprime AAL anchor }a.}
\tag{21}
\]

它不表示不存在别的 q-coprime anchor，也不表示 \(\Theta_\nu\) 不能作为带完整
provenance 的 raw mark 保存。更重要的是，本卡**不**把 (18) 的 \(U(R)\) 元阶直接
推到任意稳定子商 \(H/P\)：商可以杀掉相关 q-primary 部分，故这类 quotient model
仍须独立检查。

## 5. Identity abstract-label ansatz 的共同仿射矛盾

另单独考察最直接、但过强的选择

\[
j_\nu=s_\nu=\nu\in\{1,2,4\}.
\tag{22}
\]

本节仍只在 \(H=U(R),P=1\) 的未约化模型中作一个**抽象标签**测试：假设某个尚未
构造的 anchor set \(J\) 含 \(\{1,2,4\}\)，并取 \(j_\nu=\nu\)。这里 \(s_\nu\) 是
尝试满足共同仿射律的整数标签；本节不验证 \(a j_\nu^{-1}\in\operatorname{im}\phi\)、
physical label interval、multiplicity 或 row-to-anchor provenance。现在只令
\(q\in\{3,23\}\)，并取 (15) 中由 \(\eta_q\) 给出的**阶恰为 \(q\)** 的角色
\(\psi_q\)；(16) 已验证 \(\psi_q(2)\ne1\)。用

\[
\psi_q(j_\nu)=\zeta_q^{-\gamma_\nu}
\tag{23}
\]

定义相位指数。由 \(j_\nu=\nu\) 有

\[
\gamma_1=0,
\qquad \gamma_4=2\gamma_2\pmod q.
\tag{24}
\]

若存在共同的 \(c\in\mathbb Z/q\mathbb Z\) 与单位
\(u\in(\mathbb Z/q\mathbb Z)^\times\) 使

\[
s_\nu\equiv c+u\gamma_\nu\pmod q
\qquad(\nu=1,2,4),
\tag{25}
\]

则 \(\nu=1\) 给出 \(c=1\)，\(\nu=2\) 给出 \(u\gamma_2=1\)，而 \(\nu=4\) 给出

\[
4\equiv1+2u\gamma_2\equiv3\pmod q,
\tag{26}
\]

矛盾。由 (15)--(16)，这特别适用于 \(q=3\) 和 \(q=23\)。因此

\[
\boxed{H=U(R),\ P=1:\quad j_\nu=s_\nu=\nu\text{ 这一 identity abstract-label ansatz 无法通过共同奇 }q\text{-仿射同余门}.}
\tag{27}
\]

这一步没有构造或验证任何 AAL 的 anchor-membership 条件，也没有把三条 tail 的未标记
determinant 行合并。它仅排除 \(j_\nu=s_\nu=\nu\) 这一自然 abstract-label 尝试；
它不对任意 row-to-anchor map 或稳定子商中的标签关系作出结论。

## 6. 完整中心层上的 suffix-local 正控制

现在使用完整的固定中心层

\[
J_{\mathrm{full}}
=\left\{2^a7^b509^c7723^d:\ a,b,c,d\in[-1,1]\right\}.
\tag{28}
\]

复现器逐项枚举得到

\[
|J_{\mathrm{full}}|=81,
\qquad
\operatorname{Stab}_H(J_{\mathrm{full}})=\{1\}.
\tag{29}
\]

故这里的稳定子商仍为 \(H\)。由 (12)--(13)，完整 support 指数映射的像也是
\(H=U(R)\)，从而在相应的 \(J_\theta\) 记号下有
\(J_\theta=J_{\mathrm{full}}\)。取

\[
\theta=-1\pmod R,
\qquad \operatorname{ord}_H(\theta)=2,
\tag{30}
\]

它同时与 \(q=3,23\) 互素。对 (9) 的三个真实尾点，定义

\[
\Phi_\nu=-(\nu C)^{-1}=-13\nu^{-1}pmod R.
\tag{31}
\]

则有一个完全由实际 tail 坐标给出的固定层表示：

\[
\Phi_\nu=\theta j_\nu^{-1},
\qquad
\begin{array}{c|c|c}
\nu&j_\nu=\nu C\pmod R&(2,7,509,7723)\text{ 指数}\\ \hline
4&28504=7723^{-1}&(0,0,0,-1)\\
2&14252=2^{-1}7723^{-1}&(-1,0,0,-1)\\
1&7126=2\cdot7\cdot509&(1,1,1,0).
\end{array}
\tag{32}
\]

这不是 (22) 的 identity abstract-label 尝试：这里的 anchor 是 \(\theta=-1\)，
而 \(j_\nu\) 是实际的 \(\nu C\)，尚未给出共同整数标签 \(s_\nu\)。

沿用 (15) 的角色并用

\[
\psi_q(j_\nu)=\zeta_q^{-\gamma_\nu}
\tag{33}
\]

定义相位指数，精确数据为

\[
\begin{array}{c|ccc|cc}
q&\gamma_4&\gamma_2&\gamma_1&
\gamma_2-\gamma_4&\gamma_1-\gamma_2\\ \hline
3&0&1&2&1&1\\
23&21&16&11&18&18.
\end{array}
\tag{34}
\]

两列 edge increment 分别等于 (16) 的 \(\eta_q(2)\)，正好对应两条 raw
\(2\)-边。因此这是一个明确的正结论：三点 suffix 在 \(q=3\) 和 \(q=23\) 的
factor-local 相位兼容。

它的边界同样明确：该控制没有预先声明 source root、root policy、共同整数标签、
carry/E2、E4/E5 或递归边；所以不能把它提升为完整 ancestry 的 AAL admission。

## 7. 已声明 source-root 的首条 \(p\)-边被固定层门阻断

既有 factor-block source receipt 的首条实际 raw 边是

\[
S=(p,R(p-1)-p,p-1)=(7129,220098383,7128)
\xrightarrow{\,7129\,}(1,30878,1).
\tag{35}
\]

复现器同时检查此边 strict capacity、unit condition 与 gcd reduction=1。若同一固定
\(\theta\) 覆盖这条边，记 source 为 \(v\)、destination 为 \(w\)，则

\[
\Phi_w=p\Phi_v,
\qquad \Phi_x=\theta j_x^{-1}
\quad\Longrightarrow\quad
j_v=pj_w.
\tag{36}
\]

因此必须有 \(J_{\mathrm{full}}\cap pJ_{\mathrm{full}}\ne\varnothing\)。这里存在一个
不依赖大范围搜索的有限 CRT 差分证书。对 (11) 的坐标记号，四个 support factor 与
\(p\) 的坐标为

\[
\begin{array}{c|c}
u&\ell(u)\in C_6\times C_{46}\times C_{72}\\ \hline
2&(1,18,8)\\
7&(4,32,33)\\
509&(5,31,44)\\
7723&(0,21,43)\\ \hline
7129&(0,44,38).
\end{array}
\tag{37}
\]

若 \(p=j_vj_w^{-1}\)，两端的中心盒指数差 \(e\in[-2,2]^4\)。前两个坐标同余仅留下

\[
e=(-2,0,-2,-2),\qquad e=(1,1,-1,-1),
\tag{38}
\]

而二者第三坐标都是 \(26\pmod {72}\)，不是 \(38\pmod {72}\)。所以

\[
\boxed{J_{\mathrm{full}}\cap7129J_{\mathrm{full}}=\varnothing.}
\tag{39}
\]

这也排除同一中心指数约束下的删因子子层，因为它们均包含于
\(J_{\mathrm{full}}\)。其量词仅为 (35) 这条已声明 source-root \(p\)-边和该标准
fixed layer；它不排除另一个 source word、root policy 或 fixed layer。这个失败门比
q-coprime 或 q-phase 更早，但不与第 6 节的 suffix 正控制矛盾。

## 8. terminal-first 状态与局部 CarryCore

在尝试任何 root/raw 递归前，\(p=7129\) 已有直接的 Type II 终端：

\[
A=C=1,\quad k=2,\quad h=4ACk-1=7,
\qquad 2p+1=14259=7\cdot2037.
\tag{40}
\]

取 \(B=2037\)、\(m=(A+B)/k=1019\)、\(x=ABC=2037\)、\(d=A^2C=1\)，有
\(m\mid x+d=2038\) 且 \(m\equiv3\pmod4\)，并且整数交叉相乘严格验证

\[
\boxed{\frac4{7129}=
\frac1{2037}+\frac1{14258}+\frac1{29043546}.}
\tag{41}
\]

故本例的 selector 语义为

```text
terminal_first_status = DIRECT_TYPE_II_TERMINAL_VERIFIED
selector_status       = terminal_preempted
recursive_edge        = ineligible
```

(35)--(39) 只保留为对入口接口的诊断性证书，不能把 raw tree 放入递归队列。

此外，三条 tail occurrence 的未标记 determinant row 都是同一行
\((C,M,d,n)=(7126,7723,3,13)\)，不是三条独立 physical row。令
\(r=M\bmod p=594\)，当前 transcript 的局部 ledger 量为

\[
\operatorname{CarryCore}=\gcd(M,Cr)
=\gcd(7723,7126\cdot594)=1.
\tag{42}
\]

它只说明此 transcript 中可持续保留的 \(A\) 只能是 \(1\)；并不证明 carry/E2
lift，也不因三个 marked occurrence 而把 physical-row 计数为三。

## 9. 边界与下一接口

本控制已经核验 F witness、三条 marked occurrence、raw 方向、角色可用性、一个
suffix-local 正控制、一个 source-root fixed-layer 门、两个明确的 raw-to-affine 窄障碍
与直接终端；它仍没有以下内容：

```text
suffix_row_to_anchor_assignment = verified_for_t4_t2_t1_only
full_source_rooted_assignment  = obstructed_at_p_edge_J_full_membership
common_affine_chart           = not_constructed
physical_label_interval       = not_constructed
anchor_membership_a_jinv      = verified_for_suffix_only
row_to_anchor_provenance      = suffix_only_not_full_source_rooted
terminal_first_status         = DIRECT_TYPE_II_TERMINAL_VERIFIED
carry/E2                      = not_lifted
E4/E5                         = not_constructed
selector_edge                 = false (terminal_preempted)
```

尤其 (21) 不排除重选 q-coprime anchor，(27) 不排除以额外 raw/physical 字段定义的
非 identity map，(39) 不排除另一个 source word、root policy 或 fixed layer，也不排除
跨 chart 的 affine construction。第 6 节说明仅看后缀时 factor-local 相位并无矛盾；第 7 节
定位了已声明完整 ancestry 在最早 \(p\)-边的 fixed-layer membership 失败；第 8 节则规定
此 \(p\) 已终端，不应转化成 selector 递归实例。稳定子约化、完整 row-to-anchor provenance
和 carry/E2/E4/E5 仍是独立待证接口。

窄复现：

```bash
python3 reproductions/type_i_f_c3_triple_tail_raw_affine_obstruction_p7129.py --verify
```
