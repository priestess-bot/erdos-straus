---
kind: claim
claim_id: type-I-f-c78-raw-root-fixture-p73-r79
title: p=73, R=79 的最小 F-C78 universal raw-source 终端预先截断控制
statement: 在限定域 p 为 1 mod 24 素数、p<R、R 为 3 mod 4，且固定层稳定子商要求为 C78 时，(p,R,K)=(73,79,1442=2*7*103) 是字典序最小的 F 型数值控制例。其原始指数盒 [-1,1]^3 不命中 -1，最小 l1 后字典序的无界目标见证为 (0,0,-3)；J={2^a 7^b:a,b in [-1,1]} 的稳定子平凡，商为 C78。target-odd 角色 chi_1 非零，完整 target-odd Parseval 能量为 1053，且 chi_1 的 3-primary 目标/残余坐标为 0/2 mod 3。同一图表有实际 universal p-source raw 边 (73,5615,72)->(1,78,1)，但该固定 J 满足 J cap 73J=empty，故此 raw 边不能给出 canonical native row-to-anchor assignment。p=73 又已有 Type II 终端叶 4/73=1/20+1/292+1/730。因此此例严格是 terminal-preempted control，不是递归边；它没有共同仿射律、carry、E2 或解提升。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-f-g-fourier-obstruction-certificate
  - type-I-fixed-layer-stabilizer-defect-reduction
  - type-I-f-target-involution-fourier-phase-collapse
  - type-I-raw-universal-p-parent-root-policy-boundary
topics:
  - type-I
  - F-state
  - fixed-layer
  - C78
  - finite-fourier
  - target-involution
  - raw-source
  - terminal-first
  - proof-boundary
sources:
  - claim: type-I-f-g-fourier-obstruction-certificate
    role: F-box-and-Fourier-semantics
  - claim: type-I-f-target-involution-fourier-phase-collapse
    role: target-odd-energy-and-q-primary-semantics
  - claim: type-I-raw-universal-p-parent-root-policy-boundary
    role: universal-p-source-raw-edge-semantics
visibility: public
last_checked: '2026-08-07'
---

# \(p=73,R=79\) 的最小 F-C78 universal raw-source 终端预先截断控制

## 1. 范围与最小性

本卡固定

\[
p=73,\qquad R=79,\qquad K=\frac{pR+1}{4}=1442=2\cdot7\cdot103.
\tag{1}
\]

这里的“最小”只针对下列明确的控制族：

\[
p\equiv1\pmod {24},\qquad p<R,\qquad R\equiv3\pmod4,
\qquad H/\operatorname{Stab}_H(J)\cong C_{78}.
\tag{2}
\]

在 \(73\) 以下没有 \(1\pmod {24}\) 的素数，因此 \(p=73\) 是该核心域的最小素数。
另一方面，最后一个条件蕴含 \(\varphi(R)\ge78\)。对任意 \(1<R<79\)，
\(\varphi(R)\le R-1<78\)，故 \(R\ge79\)；本例以 \(R=79\) 达到该下界。
这不是对所有 F 状态、所有 raw 图表或原猜想的最小性断言。

## 2. F 盒与无界见证

以 \(3\) 为 \(U(79)\) 的生成元，精确离散坐标为

\[
2=3^4,\qquad 7=3^{53},\qquad103=3^{13},\qquad-1=3^{39}\pmod {79}.
\tag{3}
\]

令

\[
\phi(a,b,c)=2^a7^b103^c\pmod {79},\qquad
\mathcal B=[-1,1]^3\cap\mathbb Z^3.
\tag{4}
\]

于是目标方程等价于

\[
4a+53b+13c\equiv39\pmod {78}.
\tag{5}
\]

对 \(\mathcal B\) 的全部 27 个向量逐一检查给出

\[
-1\notin\phi(\mathcal B).
\tag{6}
\]

故这是一个 F 型有限指数盒缺失。按“最小 \(\ell_1\) 范数、再字典序”的固定规则，
无界目标纤维的规范见证是

\[
z_\ast=(0,0,-3),\qquad
13(-3)\equiv39\pmod {78}.
\tag{7}
\]

不存在 \(\ell_1<3\) 的目标见证；\((0,0,3)\) 是同一长度的另一解，故在该规则下
排在 \(z_\ast\) 之后。式 (7) 明确在原盒外，不能被误记为 Type I 命中。

## 3. 固定层、C78 商与 target-odd Fourier 回执

把 \(2,7\) 固定为一层，而 \(103\) 作为残余块，令

\[
J=\{2^a7^b:a,b\in[-1,1]\}
=\{1,2,7,14,17,34,40,43,68\}\pmod {79}.
\tag{8}
\]

支撑 \(\{2,7,103\}\) 生成整个 \(U(79)\cong C_{78}\)，并且直接计算得到

\[
\operatorname{Stab}_{U(79)}(J)=\{1\}.
\tag{9}
\]

因此本例没有被稳定子缩小：\(H/\operatorname{Stab}_H(J)\cong C_{78}\)。令 \(c_x\) 是 (4) 的
27 个盒内表示在这个循环商坐标 \(x\in\mathbb Z/78\mathbb Z\) 的计数，
\(C_s=\sum_xc_xc_{x-s}\)。本例的盒映射实际上无碰撞，且

\[
c_{39}=0,\qquad C_0=27,\qquad C_{39}=0.
\tag{10}
\]

取 \(\zeta=\zeta_{78}\)，\(\chi_1(3)=\zeta\)。它是 target-odd，因为

\[
\chi_1(-1)=\zeta^{39}=-1.
\tag{11}
\]

其 Fourier 系数不为零：

\[
A_1=D_1(\zeta^4)D_1(\zeta^{53})D_1(\zeta^{13})\ne0.
\tag{12}
\]

这里三个根的阶依次为 \(39,78,6\)，而 \(D_1(w)=w^{-1}+1+w\) 对根单位恰在
\(w\) 阶为 \(3\) 时为零。注意 (12) 只是指明一个 target-odd 非零角色；它不把
\(\chi_1\) 说成唯一或最大谱角色。

全部 target-odd 角色的精确 Parseval 能量为

\[
E^-:=\sum_{\substack{1\le k<78\\ k\ \mathrm{odd}}}|A_k|^2
=\frac{78}{2}(C_0-C_{39})
=39\cdot27
=1053.
\tag{13}
\]

这是状态内有限群能量，尚不是 q 进高度、载体数量或跨状态容量需求。

对 \(\chi_1\) 的三进主分量，坐标 \(a\in\mathbb Z/78\mathbb Z\) 投影为
\(26a\pmod3\)。因此目标和残余 \(103\) 分别满足

\[
39\longmapsto0\pmod3,\qquad13\longmapsto2\pmod3.
\tag{14}
\]

式 (14) 是直接 Fourier 相位坐标：奇素数目标对合塌缩到零，而 residual 块仍非平凡。
它没有提供从该坐标到整数标签的 source map。

## 4. 同图表的 actual raw source

该图表有标准 universal \(p\)-source

\[
\mathsf S=(p,R(p-1)-p,p-1)=(73,5615,72).
\tag{15}
\]

它是本原 formal raw node，且 \(v_{73}(73)=1>v_{73}(K)=0\)。选择第一坐标并取
\(q=73\) 时，shift 为

\[
s=-72\equiv1\pmod {73}.
\tag{16}
\]

未约分的下一行已经本原，故有一条实际 raw 边

\[
(73,5615,72)
\xrightarrow[\gcd\ \mathrm{reduction}=1]{q=73,\ s=1}
(1,78,1).
\tag{17}
\]

这只证明同一图表中的 raw source/path 回执。它不等于 E1--E5 所需的已接纳 selector
root，也不把 (17) 注册为递归边。

### 此固定层的 canonical row-to-anchor assignment 已被排除

沿 (17) 的 selected-coordinate lineage，归一化相位为

\[
\Phi_{\mathsf S}=-73^{-1}=66,
\qquad
\Phi_{\rm dst}=-1^{-1}=78,
\qquad
\Phi_{\rm dst}\Phi_{\mathsf S}^{-1}=73\pmod {79}.
\tag{18}
\]

现在只取本卡已经固定的 \(H=U(79)\)、平凡稳定子和 (8) 中的 \(J\)。直接计算

\[
\boxed{J\cap73J=\varnothing.}
\tag{19}
\]

若存在一个固定 anchor \(\theta\) 和两个 \(j_{\mathsf S},j_{\rm dst}\in J\)，使

\[
\Phi_v=\theta j_v^{-1}\qquad(v=\mathsf S,\mathrm{dst}),
\tag{20}
\]

则 (18) 强制 \(73=j_{\mathsf S}j_{\rm dst}^{-1}\)，即
\(j_{\mathsf S}\in J\cap73J\)，与 (19) 矛盾。故“同一 F Fourier 图表中有 raw
edge”不能被误读成已有 row-to-anchor map。这个结论只针对已固定的 \(J\) 和 native
\(H=U(79)\) assignment；不排除另一个 layer、另一个 chart 或独立 source-to-F map。

## 5. terminal-first 截断

同一个核心素数已有直接 Type II 叶。取

\[
(A,B,C,\kappa)=(2,5,2,1),\qquad
p=4ABC-7,
\tag{21}
\]

得到精确单位分数恒等式

\[
\boxed{
\frac4{73}=\frac1{20}+\frac1{292}+\frac1{730}.
}
\tag{22}
\]

因此 terminal-first 语义必须先输出 (22)，而不是把 (17) 送进递归队列。该卡的正确状态是
`terminal-preempted control`，调度结果为 `direct_Type_II_terminal`，并且
`recursive_edge_eligible = false`。

## 6. 明确未闭合的接口

本控制例没有给出 row-to-anchor map、跨行共同 affine law、carry contract、E2 验证、
或解提升。它也没有把 (14) 提升为整数 q-adic 标签，没有建立 E4 state identity 或 E5
严格下降。上述项目是未提供的接口，不应被理解为已反证；但在它们分别被证明并接入前，
本卡既不是递归边，也不推进 Erd\H{o}s--Straus 猜想的全称闭合。

复现：

~~~bash
python3 reproductions/type_i_f_c78_raw_root_fixture_p73_r79.py --verify
~~~
