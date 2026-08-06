---
kind: claim
claim_id: type-II-c2-quotient-one-escape-factor-terminal
title: Type II C2 商的单逃逸因子精确终端门
statement: 在一个已通过来源标签、同纤维、CRT、范围和 shared-q 门的 Type II 目标纤维中，设完整的 source-only 物理积集在某个将 -1 分离的 C2 商上恒等。则 source-only 积不可能给出 h=-1 mod 4D' 的 raw Type II 终端。若 N'=p+4AD' 中另有一个未复用的实际奇素因子 q 在该商上非平凡，则它与一个物理可用的 source-only 积 R_I 形成终端当且仅当 R_I=(-1)q^(-1) mod 4D'；该命中给出一张 raw Type II 短证书。故此商分离并不产生虚假的容量：它把 one-escape-factor 模式压缩为一个精确、有限且带物理来源的核内残类测试。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-raw-ray-certificate
  - type-II-annihilator-congruence-fiber-lift-criterion
  - type-II-filtered-composition-source-slot-terminal
topics:
  - type-II
  - raw-ray
  - source-map
  - quotient
  - C2
  - relay
  - escape-factor
  - terminal
  - proof-program
sources:
  - claim: type-II-raw-ray-certificate
    role: raw-Type-II-certificate
  - claim: type-II-annihilator-congruence-fiber-lift-criterion
    role: labeled-fiber-lift-gate
  - claim: type-II-filtered-composition-source-slot-terminal
    role: physical-source-slot-accounting
visibility: public
last_checked: '2026-08-06'
---

# Type II \(C_2\) 商的单逃逸因子精确终端门

## 1. 已关闭的来源纤维

令 \(p\equiv1\pmod4\) 为素数，并固定一个 Type II 目标参数

\[
A\mid D',\qquad C=\frac{D'}A,\qquad 4AD'<p,
\tag{1}
\]

以及

\[
M'=4D',\qquad N'=p+4AD'.
\tag{2}
\]

考虑一个已经通过来源标签、同纤维、CRT、范围、互素和 shared-\(q\) 门的
有限 source-only universe。将其中可独立选择的原子物理块记为

\[
\mathcal H=\{h_1,\ldots,h_t\},\qquad h_i\mid N',
\tag{3}
\]

并要求每个允许的 source-only 混合因子恰为一组未复用块的积。记其实际整数积集及
对应的残数集为

\[
\mathscr R=\left\{R_I=\prod_{i\in I}h_i:
 I\text{ 是允许的未复用选择，且 }R_I\mid N'\right\},
\qquad
\overline{\mathcal P}=\{R_I\bmod M':R_I\in\mathscr R\}
\subseteq U(M') .
\tag{4}
\]

这里“完整”只量化这个已经声明的 source-only universe：若实际允许拆分 \(h_i\)、
重用素数幂或加入外部来源，则这些选择必须先纳入 (3)--(4)，不能引用本卡的
source-only 障碍。

假设有满射群同态

\[
\eta:U(M')\twoheadrightarrow C_2,\qquad \eta(-1)\ne1,
\tag{5}
\]

并且全部固定物理块均被湮灭：

\[
\eta(h_i)=1\qquad(1\le i\le t).
\tag{6}
\]

## 2. source-only 的严格障碍

由 (6) 的乘法性，

\[
\eta(\overline r)=1\qquad(\overline r\in\overline{\mathcal P}).
\tag{7}
\]

另一方面 \(\eta(-1)\ne1\)，所以

\[
\boxed{-1\notin\overline{\mathcal P}.}
\tag{8}
\]

因而在这个完整 source-only universe 中，没有由 \(\mathscr R\) 给出的允许
source-only 物理积 \(h\) 能同时满足

\[
h\equiv-1\pmod {M'}.
\tag{9}
\]

选择器应在此处输出

\[
\mathrm{C2\_SOURCE\_ONLY\_TERMINAL\_IMPOSSIBLE},
\tag{10}
\]

而不是把同一个商角色重复记为容量或原猜想的递降。

## 3. 一个真实逃逸因子的充要终端门

令 \(q\) 是 \(N'\) 的一个未复用奇素因子。对每个实际 source-only 积
\(R_I\in\mathscr R\)，要求其有可用的物理因子账本，即

\[
qR_I\mid N'.
\tag{11}
\]

等价地，对每个素数 \(\ell\) 必须有

\[
v_\ell(R_I)+\mathbf 1_{\ell=q}\le v_\ell(N').
\tag{12}
\]

因为 (1) 蕴含 \(\gcd(N',M')=1\)，\(q\in U(M')\)。再假设

\[
\eta(q)\ne1.
\tag{13}
\]

令 \(\overline r=R_I\bmod M'\)。则对带有 (11) 物理见证的
\(\overline r\in\overline{\mathcal P}\)，有精确等价式

\[
\boxed{
qR_I\equiv-1\pmod {M'}
\quad\Longleftrightarrow\quad
\overline r\equiv(-1)q^{-1}\pmod {M'}.
}
\tag{14}
\]

右式是唯一的核内校正残类；(13) 只说明它位于 \(\ker\eta\)，并不保证它属于
实际物理残数集 \(\overline{\mathcal P}\)。因此失败时的正确回执是

\[
\mathrm{C2\_ONE\_ESCAPE\_KERNEL\_CORRECTION\_MISSING},
\tag{15}
\]

而不是“商角色已经给出 Type II”。

若 (14) 命中，令 \(h=qR_I\)、

\[
K=\frac{h+1}{4D'},\qquad
B=\frac{Kp+A}{h}.
\tag{16}
\]

由 \(h\mid N'\) 和 \(4D'K=h+1\)，

\[
K N'=Kp+4AD'K\equiv Kp+A\pmod h,
\tag{17}
\]

所以 \(B\) 是正整数。并且

\[
B-A=\frac{K(p-4AD')+2A}{h}>0
\tag{18}
\]

由 (1) 成立。又

\[
h=4ACK-1.
\tag{19}
\]

因此 raw-ray 定理给出一个实际 Type II 短证书。更明确地，令

\[
m=\frac{A+B}{K},\qquad x=ABC,\qquad d=A^2C,
\tag{20}
\]

则 \(0<m<p\)、\(d\mid x^2\)、\(d\le x\)、\(m\mid x+d\)，以及

\[
\frac4p
=\frac1x
+\frac1{p(x+d)/m}
+\frac1{px(x+d)/(md)}.
\tag{21}
\]

这就是带一个外部实际因子的 terminal-first 回执。

## 4. 完整性范围

在 (3)--(4) 所声明的物理 source-only universe 中，任何恰有一个外部因子 \(q\)
的 raw 因子都写作 \(h=qR_I\)。所以 (14) 不只是充分条件，也是该
one-escape-factor 模式的必要条件。它不排除两个或更多外部因子、另一目标纤维、
未纳入 (3) 的来源拆分，或已通过严格整数回译门的商递降。

## 5. 定点证书

取

\[
p=2473,\qquad D=6,\qquad a=3,\qquad D'=3,\qquad A=1.
\tag{22}
\]

此时 \(p\equiv1\pmod{24}\)，来源 \(a=3\) 的因子 \(5\) 同时满足

\[
5\mid p+4Da=2545,\qquad
5\mid N'=p+4AD'=2485,\qquad
AD'=3\equiv18=Da\pmod5.
\tag{23}
\]

在 \(U(12)\) 上取模 \(4\) 的 \(C_2\) 商。它满足

\[
\eta(5)=1,\qquad \eta(-1)\ne1,\qquad
\mathscr R=\{1,5\},\qquad \overline{\mathcal P}=\{1,5\}.
\tag{24}
\]

所以 source-only 积不能命中 \(-1\equiv11\pmod{12}\)。但未复用的真实因子

\[
q=7\mid2485,\qquad \eta(7)\ne1,\qquad
(-1)7^{-1}\equiv5\pmod{12}
\tag{25}
\]

命中 (14)。故 \(h=5\cdot7=35\)、\(K=3\)、\(C=3\)、\(B=212\)。由 (20)，

\[
(m,x,d)=(71,636,3),
\tag{26}
\]

并得到显式证书

\[
\boxed{
\frac4{2473}
=\frac1{636}
+\frac1{22257}
+\frac1{4718484}.
}
\tag{27}
\]

这一实例只演示已闭合局部纤维的 source-only 障碍和单逃逸因子终端，不把它外推为
所有 \(C_2\) 商或所有 F/G 状态的全称闭合。
