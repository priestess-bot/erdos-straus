---
kind: claim
claim_id: type-I-first-overflow-common-denominator-marked-lift
title: 首个 overflow 商的公共分母双因子门、quotient-multiple 终端与 proper marked lift
statement: >-
  对 q>=2 与分母 c，令 R_q(c)=4c-q、S_q(c)=qc，并以 S_q(c)^2 的因子同余定义
  E_q(c)。则 c 出现在 Sol(q) 中当且仅当 E_q(c) 非空；因此 n<p 的一分母保留
  marked lift 恰由 n、p 两侧的双因子门刻画，并在准确的 proper marked set 上给出
  全域映射。对 first-overflow 数据 (p,M,y,m,n)，自然分母 y 的目标门恰等价于 gap m
  的完整 Bradford 菜单，所以菜单空时保留 y 严格不可能。另一方面，对
  p<4kn<=2p，r_k=4kn-p 与 d=n 给出 Type I 证书当且仅当 r_k|(kp+1)；first-overflow
  时只需检查少于 M/4 个 k。控制 (p,M,y,m,n)=(73,27,29,43,7) 的自然 y 与全部
  二分母保留提升都失败，但 k=3 给出 gap 11 的 alternate Type I 终端，且规范
  非降序解空间中的精确一分母 marked state 为 {(2,21,42),(2,15,210)}，通过
  c=21 或 210 全域提升到 Sol(73)。规范 Sol_le(7) 中又有一条全部坐标不大于 p/4
  的解，故任何定义在全规范解空间上的自适应一分母保留映射均不存在。该 lift 已有
  完整数学映射与严格秩下降，但尚未生成统一 selector 的 E2/E3 状态回执。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fg-qprefix-block-bound-first-overflow-terminal
  - one-denominator-lift-factor-criterion
  - marked-solution-descent-closure
  - short-certificate-equivalence
topics:
  - type-I
  - first-overflow
  - common-denominator
  - marked-solution
  - solution-lift
  - alternate-terminal
  - divisor-factorization
  - strict-descent
  - strict-obstruction
  - candidate-transition
  - proof-program
sources:
  - claim: one-denominator-lift-factor-criterion
    role: exact-target-side-factor-gate
  - claim: marked-solution-descent-closure
    role: proper-marked-state-induction-contract
  - claim: short-certificate-equivalence
    role: quotient-multiple-Type-I-reconstruction
  - reproduction: reproductions/type_i_first_overflow_common_denominator_marked_lift.py
    role: focused-natural-y-alternate-menu-and-p73-marked-state-verification
visibility: public
last_checked: '2026-08-10'
---

# 首个 overflow 商的公共分母双因子门、quotient-multiple 终端与 proper marked lift

## 1. 公共分母的精确双因子门

对整数 \(q\ge2,c\ge1\)，置

\[
R_q(c)=4c-q,
\qquad S_q(c)=qc,
\tag{1}
\]

并定义

\[
\mathcal E_q(c)=
\left\{e\in\mathbb N:
\begin{array}{l}
R_q(c)>0,\ e\mid S_q(c)^2,\\
R_q(c)\mid S_q(c)+e,\\
R_q(c)\mid S_q(c)+S_q(c)^2/e
\end{array}
\right\}.
\tag{2}
\]

令 \(\operatorname{Den}(q)\) 是 \(\operatorname{Sol}(q)\) 全部三元组中出现过的分母
集合。为消除置换重复，另记

\[
\operatorname{Sol}_{\le}(q)
=\{(a,b,c)\in\operatorname{Sol}(q):a\le b\le c\}.
\]

则

\[
\boxed{
c\in\operatorname{Den}(q)
\quad\Longleftrightarrow\quad
\mathcal E_q(c)\ne\varnothing.}
\tag{3}
\]

任一解中的单项 \(1/c\) 必严格小于 \(4/q\)，所以 \(R_q(c)>0\)。余下两项满足

\[
\frac1u+\frac1v
=\frac4q-\frac1c
=\frac{R_q(c)}{S_q(c)}.
\]

标准因子恒等式

\[
(R_q(c)u-S_q(c))(R_q(c)v-S_q(c))=S_q(c)^2
\tag{4}
\]

立即给出 (2)--(3)，并从任意 \(e\in\mathcal E_q(c)\) 恢复

\[
u=\frac{S_q(c)+e}{R_q(c)},
\qquad
v=\frac{S_q(c)+S_q(c)^2/e}{R_q(c)}.
\tag{5}
\]

固定 \(2\le n<p\)。对每个规范源解 \(z\in\operatorname{Sol}_{\le}(n)\)，按“最小坐标值、
最小坐标位置、最小 \(e\)”选择一个满足
\(c\in z\) 且 \(e\in\mathcal E_p(c)\) 的 pair，并定义

\[
W^{[1]}_{p\leftarrow n}
=\{z\in\operatorname{Sol}_{\le}(n):
\text{这样的 }(c,e)\text{ 存在}\}.
\tag{6}
\]

式 (5) 给出确定的全域映射

\[
\boxed{
\Phi_{p\leftarrow n}(z)
=\operatorname{sort}\left(
c,
\frac{pc+e}{4c-p},
\frac{pc+p^2c^2/e}{4c-p}
\right)
\in\operatorname{Sol}_{\le}(p)\subseteq\operatorname{Sol}(p).}
\tag{7}
\]

因此

\[
W^{[1]}_{p\leftarrow n}\ne\varnothing
\quad\Longleftrightarrow\quad
\exists c:
\mathcal E_n(c)\ne\varnothing,
\ \mathcal E_p(c)\ne\varnothing.
\tag{8}
\]

这是保留一个坐标、重组两尾的精确双因子交条件。式 (7) 在 (6) 的**全部**输入上
定义，且 \(\rho=n<p\) 支付良基下降，所以它给出 marked-solution closure 所需的
全域提升与严格秩下降。它们是统一选择器 E4/E5 的数学分量；要升级为 selector
`verified_edge`，仍须另行构造并验证完整的 source/target state、E2/E3 与 edge
normal-form 回执。没有必要也通常不可能把定义域扩大到整个
\(\operatorname{Sol}_{\le}(n)\)。

## 2. first-overflow 自然分母 \(y\) 的等价障碍

取 first-overflow 数据

\[
m=4y-p,
\qquad
n=\frac{p+4y}{M}<p,
\qquad
3\le m\le p-2,
\tag{9}
\]

其中 \(p\) 为核心素数、\(M\ge3\) 为奇数、\((p,M)=1\)。既有 CRT defect map 给出
\((M,y)=1\)。由 \(nM=p+4y\)、\(0<y<p\) 得

\[
(n,y)=1.
\tag{10}
\]

令 \(r=4y-n\)。因为 \(M\ge3\) 且 \(p<4y\)，有 \(r>0\)。又 \(n\) 为奇数，故

\[
\gcd(r,ny)=1,
\qquad
\gcd(m,py)=1.
\tag{11}
\]

于是 (2) 的第二个同余由第一个自动推出，得到

\[
y\in\operatorname{Den}(n)
\quad\Longleftrightarrow\quad
\exists f\mid n^2y^2:
f\equiv-ny\pmod r,
\tag{12}
\]

\[
\mathcal E_p(y)\ne\varnothing
\quad\Longleftrightarrow\quad
\exists e\mid p^2y^2:
e\equiv-py\pmod m.
\tag{13}
\]

因 \(p/4<y<p/2\)，式 (13) 正是首分母 \(y\)、缺口 \(m\) 的两项余式可分解条件。
由 Bradford Type I/II 完备性，

\[
\boxed{
\mathcal E_p(y)\ne\varnothing
\quad\Longleftrightarrow\quad
\text{gap }m\text{ 的完整 Type I/II 菜单命中}.}
\tag{14}
\]

所以 `FIRST_OVERFLOW_SHORT_GAP_MENU_EMPTY` 已经严格关闭了保留自然 \(y\) 的全部
一分母 lifts。下一分支必须换成 \(c\ne y\)，不能在同一个 \(y\) 上重复调用另一种
因子语言。

## 3. quotient-multiple alternate Type I 终端

first-overflow 商 \(n\) 还规范地产生一个不依赖 \(y\) 的短菜单。对任意

\[
k\in\mathcal K(p,n)
=\{k\in\mathbb N:p<4kn\le2p\},
\tag{15}
\]

令

\[
x_k=kn,
\qquad
r_k=4kn-p.
\tag{16}
\]

则 \(3\le r_k\le p-2\)、\(r_k\equiv3\pmod4\)，而 \(d=n\mid x_k^2\)。又

\[
\gcd(r_k,n)=\gcd(p,n)=1,
\]

所以 Type I 条件精确化为

\[
\boxed{
(r_k,d=n)\text{ 是 Type I 证书}
\quad\Longleftrightarrow\quad
r_k\mid kp+1.}
\tag{17}
\]

若写 \(\ell=(kp+1)/r_k\)，恢复出的有序解为

\[
\boxed{
\frac4p
=\frac1{kn}
 +\frac1{n\ell}
 +\frac1{pkn\ell}.}
\tag{18}
\]

式 (15) 保证 \(n\ell\ge kn\)，所以 \(kn\) 确是首分母。对
\(n=(2p+m)/M\)，有 \(n>2p/M\)，故

\[
k\le\frac p{2n}<\frac M4.
\tag{19}
\]

因此这个 alternate 只需检查少于 \(M/4\) 个 \(k\)，而不是重新枚举全部自然缺口。
它是由 overflow quotient 生成的有界 Type I 子菜单；全空时仍须进入 (6) 的其它
source coordinates 或别的 exact successor。

## 4. \(p=73,M=27\)：菜单空之后的严格 marked-lift 控制

这里

\[
(p,M,y,m,n)=(73,27,29,43,7),
\qquad r=4y-n=109.
\tag{20}
\]

自然 \(y\) 的 source 门要求

\[
f\mid 203^2,\qquad f\equiv15\pmod{109},
\]

但全部除子残数只有

\[
\{1,4,7,29,49,78,94\}.
\tag{21}
\]

目标门要求

\[
e\mid 2117^2,\qquad e\equiv33\pmod{43},
\]

而全部除子残数为

\[
\{1,10,14,24,29,30,32,40,42\}.
\tag{22}
\]

所以 \(y=29\) 两侧都失败。另一方面，
\(\mathcal K(73,7)=\{3,4,5\}\)。取 \(k=3\)，有

\[
r_3=11,\qquad 11\mid3\cdot73+1,
\]

故 (17) 给出 alternate Type I 证书

\[
(m',x,d)=(11,21,7)
\tag{23}
\]

及第一条目标解

\[
\frac4{73}=\frac1{21}+\frac1{140}+\frac1{30660}.
\tag{24}
\]

更强地，\(\operatorname{Sol}_{\le}(7)\) 的全部规范非降序解恰为

\[
\begin{aligned}
\{&(2,15,210),(2,16,112),(2,18,63),(2,21,42),\\
  &(2,28,28),(3,6,14),(4,4,14)\}.
\end{aligned}
\tag{25}
\]

逐坐标应用 (2) 得到精确 proper marked state

\[
\boxed{
W^{[1]}_{73\leftarrow7}
=\{(2,15,210),(2,21,42)\}.}
\tag{26}
\]

两条规范映射为

\[
\frac47=\frac12+\frac1{21}+\frac1{42}
\xrightarrow[c=21,\ e=7]{\Phi_{73\leftarrow7}}
\frac4{73}=\frac1{21}+\frac1{140}+\frac1{30660},
\tag{27}
\]

\[
\frac47=\frac12+\frac1{15}+\frac1{210}
\xrightarrow[c=210,\ e=10]{\Phi_{73\leftarrow7}}
\frac4{73}=\frac1{20}+\frac1{210}+\frac1{30660}.
\tag{28}
\]

其余满足 \(4c>73\) 的源坐标 \(c=28,42,63,112\) 分别要求模
\(39,95,179,375\) 的除子残数 \(23,69,55,74\)，全部失败。于是 (26) 不是只展示
两个正例，而是完整 marked-set 分类。

源解 \((3,6,14)\) 的全部坐标都不超过 \(73/4\)。保留其中任何坐标都会使
\(4c-73\le0\)，故不存在定义在整个 \(\operatorname{Sol}_{\le}(7)\) 上、即使允许逐解
自适应选坐标的一分母保留映射。这是

\[
\boxed{
\texttt{FULL\_CANONICAL\_SOL7\_ADAPTIVE\_ONE\_DENOMINATOR\_LIFT\_EMPTY}}
\tag{29}
\]

的单解见证，并严格说明 proper marking 是必要的。式 (26)--(28) 已显式给出非空
source marked set、每项因子见证、在全部两项输入上的提升公式和严格分母秩
\(7<73\)，所以它是 marked-solution closure 下的完整数学 lift control。当前 artifact
尚未构造 denominator-escape state contract 要求的内容寻址 source/target states，
也未运行 `verify_state(S/T)` 与 edge normal-form verifier；因此在统一 selector
账本中只能登记为 `candidate_transition`，不能登记为完整 E1--E5 或
`verified_edge`。\(p=73\) 的既有直接终端仍按 terminal-first 预占。

## 5. 两条规范 source-tail 充分族

式 (8) 还可以由源实例的规范尾部直接供应。若 \(n\equiv7\pmod8\)，令

\[
T=\frac{n(n+1)}4,
\qquad c_1=\frac{3T}{2}.
\]

则

\[
\frac4n
=\frac1{(n+1)/4}+\frac1{c_1}+\frac1{3T}.
\tag{30}
\]

若 \(p\nmid c_1\)，且

\[
R=4c_1-p>0,
\qquad R\mid4c_1^2+n,
\tag{31}
\]

则取 \(e=n\mid(pc_1)^2\)。因 \(p\equiv4c_1\pmod R\)，式 (31) 等价于
\(R\mid pc_1+n\)；互素化简给出 \(e\in\mathcal E_p(c_1)\)，从而产生 (7)。

若 \(n\equiv3\pmod4\)，仍令 \(T=n(n+1)/4\)，并取

\[
c_2=T(T+1).
\]

恒有

\[
\frac4n
=\frac1{(n+1)/4}+\frac1{T+1}+\frac1{c_2}.
\tag{32}
\]

假设 \(p\nmid c_2\)。任意 \(e\mid c_2^2\) 若满足

\[
4c_2-p>0,
\qquad
4c_2-p\mid4c_2^2+e,
\tag{33}
\]

便给出 \(e\in\mathcal E_p(c_2)\)。对 \(p=73,n=7\)，(30)--(31) 取
\(c_1=21,e=7\)，(32)--(33) 取 \(c_2=210,e=10\)，正好恢复 (27)--(28)。

这两族把下一全称缺口压成明确的 divisor-residue 命题：对 menu-empty overflow
quotient，证明 quotient-multiple 菜单或至少一个规范 source tail 命中；若全部失败，
才转向 Fourier/kernel exact successor。它们不是对所有核心素数已经覆盖的断言。

## 聚焦验证

~~~bash
python3 reproductions/type_i_first_overflow_common_denominator_marked_lift.py --verify
~~~

验证器只重算 (20)--(33) 的两个自然 \(y\) 门、三个 quotient-multiple 候选、
\(\operatorname{Sol}_{\le}(7)\) 规范完整表、精确 marked set 与两条映射；不运行历史扫描。
