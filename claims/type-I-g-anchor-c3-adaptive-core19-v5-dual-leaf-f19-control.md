---
kind: claim
claim_id: type-I-g-anchor-c3-adaptive-core19-v5-dual-leaf-f19-control
title: c=3 adaptive core-19 首个素数点的双叶、F 型固定层与 q=19 控制
statement: 在 adaptive core-19 ambient-19 ray 的首个素数参数 v=5 上，p=1202376916441 的同一个 high-R universal source 有两条共享 (p,5) 前缀的 actual primitive raw word，分别到达 C0=p-3 与 C1=19。两行共享 A=19 的 E2/carry core 19。其 centered fixed layer J=C_R(1)={1} 是 F 型：完整 1215 点指数盒不含 -1，而 31641497801^105942250765=-1 mod R。由 191|R 与 4K=pR+1，eta(a)=a^10 mod191 在实际 K-support group 上有精确 19 阶，且因 P=Stab_H(J)=1 在固定层商中存活；其归一化相位向量为 (9,11,9,3,13,2)。但 eta 是 target-even，且该点有 (m,d)=(3,11) 的直接 Type II terminal，故该控制不是 root、odd/mixed entry 或 selector edge。更一般地，该 affine ray 的每个 prime parameter 点上，eta 的限制在 K-support group 中都非平凡。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-c3-adaptive-core19-ambient19-terminal-screen
  - type-I-g-anchor-c3-adaptive-divisor-factor-block-normal-form
  - type-I-fg-raw-transcript-persistent-ledger-carry-core
  - type-I-ordered-raw-lineage-normalized-phase-rigidity
  - type-I-fixed-layer-stabilizer-defect-reduction
  - type-I-f-g-fourier-obstruction-certificate
topics:
  - type-I
  - c3
  - core19
  - raw-source
  - dual-leaf
  - mixed-side
  - F-state
  - fixed-layer
  - stabilizer
  - Fourier
  - q-primary
  - terminal-first
  - Type-II
  - proof-boundary
sources:
  - claim: type-I-g-anchor-c3-adaptive-core19-ambient19-terminal-screen
    role: affine candidate ray and ambient conductor
  - claim: type-I-g-anchor-c3-adaptive-divisor-factor-block-normal-form
    role: C0 actual factor-block word
  - claim: type-I-fixed-layer-stabilizer-defect-reduction
    role: fixed-layer quotient and character descent criterion
  - reproduction: reproductions/type_i_c3_adaptive_core19_v5_dual_leaf_f19_control.py
    role: exact prime, raw, F-box, q=19, carry, and terminal control
visibility: public
last_checked: '2026-08-07'
---

# Adaptive core-19 的首个素数双叶控制

## 1. 参数点与范围

考虑已有 affine ray

\[
\begin{aligned}
h(v)&=7572510960+8505305445v,\\
p(v)&=181740263041+204127330680v,\\
R(v)&=104h(v)-9,
\qquad K(v)=(26h(v)+1)(p(v)-3).
\end{aligned}
\tag{1}
\]

其首个非负素数参数为

\[
v=5,
\quad h=50099038185,
\quad p=1202376916441,
\quad R=5210299971231.
\tag{2}
\]

这里的“首个”只指 \(v=0,1,2,3,4\) 分别已有因子
\(23,1459,61,283,29\)。本卡不据此作任何范围性素数分布断言。对 (2)，复现器以两层
Pocklington 链而不是概率测试检查素性：

\[
\begin{aligned}
p-1&=2^3\,3^2\,5\,7\cdot477133697,\\
477133697-1&=2^7\cdot13\cdot17\cdot101\cdot167.
\end{aligned}
\tag{3}
\]

标准 \(c=3\) 行为

\[
\begin{aligned}
M_0&=1302574992811, & C_0&=p-3=1202376916438,\\
K&=M_0C_0
=2\cdot19^2\cdot193\cdot5351\cdot66383\cdot31641497801.
\end{aligned}
\tag{4}
\]

以下是一个固定点控制，不是整条 ray 的统一 raw word，也不是 terminal-free root。

## 2. 同源双叶 raw tree

声明的 high-\(R\) universal source 为

\[
\mathsf S=(p,R(p-1)-p,p-1).
\tag{5}
\]

两支先共享两个实际 raw step：

\[
\mathsf S\xrightarrow{(0,p)}(1,R-1,1)
\xrightarrow{(1,5)}(1042059994246,4168239976985,1).
\tag{6}
\]

第一支是既有 adaptive factor-block normal form 的逐素因子展开；其共同前缀后的
side/label word 是

\[
(1,7),(1,2),(0,2),(0,2),(0,2),(0,72106829959),(1,13),(1,2),(0,2),
\tag{7}
\]

并到达 \((C_0,R-C_0,1)\)。

第二支是独立的 mixed-side word：

\[
\begin{aligned}
(1042059994246,4168239976985)
&\xrightarrow{(0,92660501)}(11246,5210299959985)\\
&\xrightarrow{(1,5)}(1042059991997,4168239979234)\\
&\xrightarrow{(1,10798549169)}(386,5210299970845)\\
&\xrightarrow{(1,5)}(1042059994169,4168239977062)\\
&\xrightarrow{(0,54845262851)}(19,R-19).
\end{aligned}
\tag{8}
\]

所有 (6)--(8) 的标签都是素数；逐边有严格容量、unit condition 和
`gcd_reduction=1`。特别地，最后一步使用

\[
1042059994169=19\cdot54845262851,
\tag{9}
\]

因此它是到奇 cofactor 的实际 raw leaf，而不是把 \(C_0\) 的偶尾重命名为 \(C_1\)。

令

\[
M_1=K/19=82430847541333694617222,
\quad d_1=p-19,
\quad n_1=4M_1-R=329723390160124478497657.
\tag{10}
\]

有序谱系给出两条不同的 physical-tail 读法：

\[
\begin{array}{c|c|c|c}
\text{leaf}&\text{orientation}&\text{coordinate}&\text{normalized phase}\\ \hline
C_0&-1&R-C_0&13\\
C_1&+1&19&-n_1=4387621028405\pmod R.
\end{array}
\tag{11}
\]

这完成了这个实际点的同源 mixed-side raw provenance；它没有建立 odd/mixed
root-entry adapter、source-to-F map 或完整 selector transcript。

## 3. 两行 carry 与支撑可见的 19 方向

两行

\[
(M_0,C_0,d_0,n_0)=(M_0,C_0,3,13),
\qquad
(M_1,C_1,d_1,n_1)
\tag{12}
\]

都满足 determinant，且取 \(A=19\) 时均通过 E2。若行集和 E2 集都是
\(\{0,1\}\)，则

\[
\operatorname{CarryCore}=19.
\tag{13}
\]

更重要的是，(1) 对每个参数都给出 \(191\mid R\)。由

\[
4K=pR+1
\tag{14}
\]

得到

\[
K\equiv4^{-1}\equiv48\pmod {191},
\qquad
48^{10}\equiv150\ne1\pmod {191}.
\tag{15}
\]

因为 \(U(191)\) 为 \(190\) 阶循环群，映射

\[
\eta:U(R)\longrightarrow U(191)[19],
\qquad \eta(a)=a^{10}\pmod {191}
\tag{16}
\]

的核在 \(U(191)\) 中恰为唯一的 \(10\) 阶子群。令

\[
H=\langle q\bmod R:q\mid K\rangle.
\tag{17}
\]

由于 \(K\in H\) 且 \(\eta(K)=150\ne1\)，有

\[
\boxed{\eta|_H\text{ 的阶恰为 }19.}
\tag{18}
\]

这把“ambient 角色存在”加强为：每个 prime parameter point 的实际 \(K\)-support
group 都已经带有非平凡的 \(19\)-primary 方向。

对任意固定层 \(J\subseteq H\)、\(P=\operatorname{Stab}_H(J)\)，这个指定方向在
固定层商中存活的充要条件是

\[
\boxed{
\eta\text{ descends nontrivially to }H/P
\Longleftrightarrow P\subseteq\ker(\eta|_H).}
\tag{19}
\]

因为 \(\eta|_H\) 的像是素数阶群，若某个 \(s\in P\) 满足
\(s^{10}\not\equiv1\pmod {191}\)，则 \(P\) 的像已为整个 \(19\) 阶群，指定角色恰被杀掉。
所以 (19) 也是一个逐稳定子生成元的有限判据。

## 4. 一个实际 F 型固定层与规范化 q=19 mode

在本点取中心化固定层 \(N=1\)，即

\[
J=\mathcal C_R(1)=\{1\},
\qquad P=\operatorname{Stab}_H(J)=\{1\}.
\tag{20}
\]

完整 centered exponent box 的大小为

\[
3\cdot5\cdot3^4=1215.
\tag{21}
\]

复现器逐一枚举这些向量，得到 \(1215\) 个不同 residue，且不含 \(-1\)。另一方面

\[
31641497801^{105942250765}\equiv-1\pmod R.
\tag{22}
\]

故 \(-1\in H\) 但 \(-1\notin\mathcal C_R(K)\)，这是一个实际的 F 型目标缺失；
不是 G 型支撑外障碍。由 (20)，(19) 在这里无条件通过。

取 \(\zeta=150\)，它在 \(U(191)\) 中有精确 \(19\) 阶。按 (4) 的因子顺序，

\[
\eta(q_i)=\zeta^{a_i},
\qquad
(a_i)=(9,11,9,3,13,2).
\tag{23}
\]

并且带重数的相位和为 \(1\pmod {19}\)，与 \(\eta(K)=\zeta\) 一致。每个
Dirichlet block 的宽度为 \(3\) 或 \(5\)，均小于 \(19\)，故

\[
\prod_i\sum_{z=-\nu_i}^{\nu_i}\zeta^{a_i z}\ne0.
\tag{24}
\]

这给出一个明确、归一化并在 \(H/P\) 存活的 \(q=19\) Fourier mode。它不是 F 缺失
强制选出的 target-odd mode，因为

\[
\eta(-1)=1.
\tag{25}
\]

因此 (23)--(24) 仍未提供跨状态的 q-adic carrier mapping 或 `demand_to_slot`。

## 5. terminal-first 截断与保留缺口

该控制点不能进入 root dispatcher。取

\[
m=3,
\quad d=11,
\quad x=\frac{p+3}{4}=300594229111
=11\cdot387839\cdot70459.
\tag{26}
\]

则 \(d\mid x^2\)、\(d\le x\)、\(3\mid x+d\)，从而

\[
\frac4p=
\frac1{300594229111}
+\frac1{120475854103889934264934}
+\frac1{3292213317349827317887300015390334}.
\tag{27}
\]

所以 terminal-first 规则必须在 raw/Fourier 分支之前输出 (27)。这也解释了为什么本卡
只能作接口正控制，不是 selector root。

仍未解决的决定性问题是：构造一个把 (8) 绑定为 fresh top-level state 的
odd/mixed-side entry，证明非 terminal 点上的完整 physical transcript，并将这样的
mode 接到实际 q-adic capacity 或严格可提升下降。现有 even-tail entry 硬编码
\(C=p-3,d=3,n=13\)，不能接纳 \(C_1=19\)。

复现：

```bash
python3 reproductions/type_i_c3_adaptive_core19_v5_dual_leaf_f19_control.py --verify
```
