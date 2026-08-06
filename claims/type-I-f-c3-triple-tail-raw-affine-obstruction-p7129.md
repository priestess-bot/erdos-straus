---
kind: claim
claim_id: type-I-f-c3-triple-tail-raw-affine-obstruction-p7129
title: p=7129 F 型 c=3 三尾 raw-to-affine 的两个窄障碍
statement: 对 p=7129、R=30879、K=55034098 的真实 F 型 c=3 even-tail control，三条带精确尾 nu=4,2,1 的同一 determinant 行由两条实际 raw 2-边 4->2->1 连接。其自然 raw 相位 Theta_nu=-13nu^(-1) 分别为 23156、15433、30866，阶分别为 1656、552、1656，均同时含 3 与 23。因此仅在未约化的自然候选模型 H=U(R)、P=1 中，不能把这三个自然 raw phase 中的任一个作为 q=3 或 q=23 的 AAL q-coprime anchor a。另对 identity tail 方案 j_nu=s_nu=nu，由本卡显式构造的 q=3、23 阶恰为 q 且在 2 上非平凡的角色，都与共同仿射律 s_nu=c+u gamma(j_nu) 不相容：由 nu=1,2,4 强制 4=3 mod q。此例严格只排除上述未约化自然 anchor 和 identity abstract-label ansatz；不对任意稳定子商 H/P 量化，不排除另一个 q-coprime anchor、非 identity row-to-anchor map、额外物理标记或跨图表 map，且不构造 selector edge、E4/E5 或全局无解结论。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-c3-even-tail-root-entry-admission-boundary
  - type-I-anchored-affine-phase-tree-capacity
  - type-I-raw-factor-action-affine-preflight
topics:
  - type-I
  - F-state
  - c3
  - raw-transition
  - even-tail
  - affine-phase
  - q-primary
  - anchor-obstruction
  - row-to-anchor
  - proof-boundary
sources:
  - claim: type-I-g-anchor-c3-even-tail-root-entry-admission-boundary
    role: c3-even-tail-physical-row-and-root-receipt-interface
  - claim: type-I-anchored-affine-phase-tree-capacity
    role: q-coprime-anchor-and-common-affine-law-contract
  - reproduction: reproductions/type_i_f_c3_triple_tail_raw_affine_obstruction_p7129.py
    role: bounded-physical-row-group-and-affine-obstruction-verifier
visibility: public
last_checked: '2026-08-07'
---

# p=7129 F 型 c=3 三尾 raw-to-affine 的两个窄障碍

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

## 6. 边界与下一接口

本控制已经核验 F witness、三条 physical row、raw 方向、角色可用性与两个明确的
raw-to-affine 失败点；它仍没有以下内容：

```text
nonidentity_row_to_anchor_map = not_constructed
common_affine_chart           = not_constructed
physical_label_interval       = not_constructed
anchor_membership_a_jinv      = not_checked
row_to_anchor_provenance      = not_constructed
terminal_first_status          = not_evaluated
carry/E2                      = not_used_for_an_edge
E4/E5                         = not_constructed
selector_edge                 = false
```

尤其 (21) 不排除重选 q-coprime anchor，(27) 不排除以额外 raw/physical 字段定义的
非 identity map，也不排除跨 chart 的 affine construction。这个 F 例子只把下一步收紧为：
任何在未约化 \(H=U(R),P=1\) 模型中企图复用 \(\Theta_\nu\) 或 identity abstract-label ansatz 的
构造必须先绕开上述已证障碍，随后才有资格进入 raw-factor compatibility、physical carry
与容量接口；稳定子约化本身仍是独立待证接口。

窄复现：

```bash
python3 reproductions/type_i_f_c3_triple_tail_raw_affine_obstruction_p7129.py --verify
```
