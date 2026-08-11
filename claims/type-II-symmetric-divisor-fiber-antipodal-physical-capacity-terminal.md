---
kind: claim
claim_id: type-II-symmetric-divisor-fiber-antipodal-physical-capacity-terminal
title: Type II 对称除子纤维的反足物理容量与逐奇核模式终端
statement: >-
  设 m>=3、(m,x)=1，写 x=prod_i ell_i^e_i，并令 d(z)=prod_i
  ell_i^(e_i+z_i)，其中 -e_i<=z_i<=e_i。若目标纤维满足
  d(z)/x=-1 mod m，则 z->-z 是无固定点对合，且
  d(z)d(-z)=x^2；每个反足对恰有一个成员满足 d<x。因此完整 signed
  box 命中在合法 m=4x-p Type II 状态中当且仅当存在真实 Type II 短证书，
  命中纤维中恰有一半是合法小除子。
  在循环 Jacobi C2 剥离中，该对合保持每个奇 parity 模式 delta，并在约化坐标上为
  u_i->-u_i-delta_i、z_j->-z_j；故每个非空奇核仿射盒自身已经产生 Type II
  terminal，不需要另做范围分派。该结论只用目标 -1 的二阶性与指数盒对称性，因而
  同样适用于一般有限阿贝尔源群；空盒后的 Type I/E1--E5 转交仍未由本定理解决。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - short-certificate-equivalence
  - type-II-p-minus-one-jacobi-source-localization-collision-capacity
topics:
  - type-II
  - symmetric-divisor-box
  - antipodal-involution
  - physical-capacity
  - range-gate
  - Jacobi-character
  - odd-kernel
  - affine-box
  - terminal
  - finite-abelian-group
  - selector
sources:
  - claim: short-certificate-equivalence
    role: Type-II-divisor-certificate-and-reconstruction
  - claim: type-II-p-minus-one-jacobi-source-localization-collision-capacity
    role: signed-box-and-negative-source-parity
  - reproduction: reproductions/type_ii_symmetric_divisor_fiber_antipodal_physical_capacity.py
    role: exact-antipodal-pairing-mode-count-and-noncyclic-control-verifier
visibility: public
last_checked: '2026-08-12'
---

# Type II 对称除子纤维的反足物理容量与逐奇核模式终端

## 1. 对称除子纤维

设

\[
m\ge3,\qquad (m,x)=1,
\qquad
x=\prod_{i=1}^t\ell_i^{e_i},\quad e_i\ge1,
\tag{1}
\]

其中 \(\ell_i\) 两两不同。定义对称指数盒

\[
\mathcal Z=\prod_{i=1}^t[-e_i,e_i]\cap\mathbb Z^t
\tag{2}
\]

以及它的真实除子回译

\[
d(z)=\prod_{i=1}^t\ell_i^{e_i+z_i}\mid x^2.
\tag{3}
\]

Type II 目标纤维为

\[
\mathcal F^-_{m,x}
=\left\{z\in\mathcal Z:
d(z)x^{-1}\equiv-1\pmod m\right\}.
\tag{4}
\]

式 (3) 不是形式 source column：令

\[
y_i=e_i+z_i\in\{0,1,\ldots,2e_i\},
\tag{5}
\]

则 \(y_i\) 正是 \(x^2\) 中素因子 \(\ell_i\) 被选取的真实 occurrence 数。
唯一分解给出

\[
\prod_i\{0,\ldots,2e_i\}
\longleftrightarrow
\{d:d\mid x^2\}
\tag{6}
\]

的双射，所以这里不存在 owner 重名、source-column 冲突或 Hall 匹配缺口。

## 2. 反足物理容量定理

定义

\[
\iota(z)=-z.
\tag{7}
\]

若 \(z\in\mathcal F^-_{m,x}\)，则

\[
\prod_i\ell_i^{-z_i}
\equiv(-1)^{-1}
\equiv-1\pmod m,
\tag{8}
\]

故 \(-z\in\mathcal F^-_{m,x}\)。在 occurrence 坐标中，(7) 恰为逐素因子补集

\[
y_i\longmapsto y_i^*=2e_i-y_i.
\tag{9}
\]

相应两个真实除子满足

\[
\boxed{d(z)d(-z)=x^2.}
\tag{10}
\]

该对合没有固定点。事实上，固定点只能是 \(z=0\)，但此时
\(d(0)x^{-1}=1\)，而 \(m\ge3\) 保证 \(1\not\equiv-1\pmod m\)。等价地，
目标纤维中不可能有 \(d=x\)。

由 (10)，每一对 \(\{z,-z\}\) 中恰有一个成员满足

\[
d(z)<x,
\tag{11}
\]

另一个满足 \(d(-z)>x\)。因此

\[
\boxed{
|\{z\in\mathcal F^-_{m,x}:d(z)<x\}|
=\frac12|\mathcal F^-_{m,x}|.}
\tag{12}
\]

也可以用中心化精确权

\[
\mathsf w(z)=\log\frac{d(z)}x
=\sum_i z_i\log\ell_i
\tag{13}
\]

表述同一结论。唯一分解保证 \(\mathsf w(z)=0\) 只可能发生在 \(z=0\)，而

\[
\mathsf w(-z)=-\mathsf w(z).
\tag{14}
\]

所以目标纤维的物理权严格成正负对，不需要另建最小乘积松弛或浮点比较。

## 3. Type II 终端的充要性

进一步设 \(p\) 为奇素数，且 \(m=4x-p\) 是合法 Type II 缺口：

\[
3\le m\le p-2,
\qquad
m\equiv3\pmod4.
\]

由短证书判据，Type II 除子要求

\[
d\mid x^2,\qquad d\le x,\qquad d\equiv-x\pmod m.
\tag{15}
\]

在 (1) 下 \(d=x\) 不可能满足最后一个同余，故大小门等价于 \(d<x\)。
式 (3)--(4) 与反足定理于是给出

\[
\boxed{
\mathcal F^-_{m,x}\ne\varnothing
\iff
\exists d\mid x^2:\ d<x,\ d\equiv-x\pmod m
\iff
\text{该状态有 Type II 短证书}.}
\tag{16}
\]

若搜索先返回 \(d>x\)，无需重新搜索：直接取

\[
d^*=\frac{x^2}{d}<x
\tag{17}
\]

即可。由 \((m,d)=1\) 及 \(d/x\equiv-1\pmod m\)，有

\[
\frac{d^*}{x}=\frac xd\equiv-1\pmod m.
\tag{18}
\]

再按 Type II 恢复式构造

\[
Y=\frac{p(x+d^*)}{m},
\qquad
Z=\frac{p(x+x^2/d^*)}{m},
\tag{19}
\]

便得到直接 terminal。这里没有跨状态 E4：目标分解已经在当前状态内完成。

## 4. 每个奇核 parity 模式内部闭合

现在进入循环 Jacobi 状态。设源群阶为 \(2s\)，其中 \(s\) 为奇数；对生成元
取离散对数

\[
a_i=2b_i+\beta_i,
\qquad
\beta_i\in\{0,1\},
\tag{20}
\]

负源集合为 \(\mathcal N=\{i:\beta_i=1\}\)。固定奇 parity 模式

\[
\delta=(\delta_i)_{i\in\mathcal N},
\qquad
D_\delta=\sum_{i\in\mathcal N}\delta_i\equiv1\pmod2,
\tag{21}
\]

并写

\[
z_i=\delta_i+2u_i\quad(i\in\mathcal N).
\tag{22}
\]

对应奇核仿射盒为

\[
\sum_{i\in\mathcal N}a_i u_i
+\sum_{i\notin\mathcal N}b_i z_i
\equiv C_\delta\pmod s,
\tag{23}
\]

其中

\[
C_\delta=
\frac{s-1}{2}
-\sum_{i\in\mathcal N}b_i\delta_i
-\frac{D_\delta-1}{2}.
\tag{24}
\]

反足对合在约化坐标上为

\[
\boxed{
u_i\longmapsto-u_i-\delta_i\quad(i\in\mathcal N),
\qquad
z_i\longmapsto-z_i\quad(i\notin\mathcal N).}
\tag{25}
\]

它保持每个变量的原有限区间，并且保持同一个 \(\delta\)，因为
\(-z_i\equiv z_i\equiv\delta_i\pmod2\)。它也直接保持 (23)：其左端变为

\[
-C_\delta-\sum_{i\in\mathcal N}a_i\delta_i,
\]

而 (20)、(21)、(24) 给出

\[
2C_\delta+
\sum_{i\in\mathcal N}a_i\delta_i
=s\equiv0\pmod s.
\tag{26}
\]

因此每个奇 parity 模式的解集自身就是无固定点反足对的并，而不是只有全部模式的并
才具有该性质。结合 (12)，对每个 \(\delta\) 都有

\[
\boxed{
|\{v\in\operatorname{Sol}_s(\delta):d(v)<x\}|
=\frac12|\operatorname{Sol}_s(\delta)|.}
\tag{27}
\]

特别地，任意一个非空奇核仿射盒都直接产生 Type II terminal。选择器无需先从该模式
挑一个解、再运行独立的 \(d<x\) 范围门。

## 5. 一般有限阿贝尔源群

上述核心论证不依赖循环离散对数。令 \(H\) 为任意有限阿贝尔群，

\[
\phi:\mathbb Z^t\to H
\]

为真实素因子指数映射，\(B=\prod_i[-e_i,e_i]\)，并令目标 \(\tau\in H\)
满足

\[
\tau^2=1,
\qquad
\tau\ne1.
\tag{28}
\]

则

\[
\phi(z)=\tau
\Longrightarrow
\phi(-z)=\tau^{-1}=\tau.
\tag{29}
\]

只要物理回译仍为 (3)，式 (9)--(14) 原样成立。故对 Type II 的
\(\tau=-1\)，一般有限阿贝尔源群的**命中分支**已经具有同样的物理 occurrence、
指数预算和大小门闭合。循环假设只用于把 miss 压成单个模 \(s\) 的仿射盒；它不用于
把命中升级为 terminal。

## 6. 控制例

对 \(p-1\) Type II 状态：

\[
\begin{array}{c|c|c|c}
(p,q)&x&|\mathcal F^-|&d<x\text{ 与 }d>x\text{ 的数量}\\ \hline
(73,2)&20&4&2+2\\
(337,6)&90&4&2+2\\
(67369,7),(67369,21),(67369,42)&-&0&0+0
\end{array}
\tag{30}
\]

前两行都只有一个奇 parity 模式，且模式内部由 (25) 配对。后三行是原有的奇核空盒，
所以本定理不会伪造 terminal。

另取真实 Type II 状态

\[
p=41,\qquad m=15,\qquad x=14=2\cdot7.
\]

其源支撑群

\[
\langle2,7\rangle=U(15)\simeq C_4\times C_2
\]

非循环，但目标纤维仍恰为

\[
(z_2,z_7)=(-1,-1),(1,1),
\qquad
d=1,196.
\tag{31}
\]

这给出一般有限阿贝尔版本的最小正控制。

## 7. 选择器边界

当前分支的精确分派可以收紧为

\[
\boxed{
\begin{array}{ll}
\text{signed/奇核盒非空}
&\longrightarrow\text{直接 Type II terminal},\\
\text{signed/奇核盒为空}
&\longrightarrow\text{精确同纤维 Type II no-go}.
\end{array}}
\tag{32}
\]

式 (32) 完成的是同一除子纤维内的 physical occurrence、指数预算和范围门；它没有
证明每个核心素数至少有一个非空纤维。空盒到普通端点状态的后续转交现已由自然尾关系
Reach 与 \(q\)-owned gcd shadow 完成：关系图无终端时，任一底层节点都产生 \(q\) 的
真因子端点，并以 \(\operatorname{Sol}(p)\) 恒等映射和严格 \(q\) 下降支付 E4--E5；
\(q=1\) 的 F-empty 基例不可能。见
[Type II 关系 Reach 的 \(q\)-owned gcd shadow 全称端点递降](type-II-relation-reach-gcd-shadow-endpoint-descent.md)。

这关闭的是普通 F/odd-kernel endpoint phase；它不自动证明任意非平凡标记集的短证书
成员资格，也不替代 G 状态后续的 Type I selector。
自然物理权最小溢出并不自动提供这条边：已有端点状态会把全部最小权放在 Jacobi
中性载体而非负源上，且局部共享缺口和直接载体删除同时失败。见
[\(p-1\) Type II 奇核空盒的物理权最小溢出与中性载体 no-go](type-II-p-minus-one-jacobi-weighted-minimum-overflow-neutral-carrier-no-go.md)。

聚焦验证：

~~~bash
python3 reproductions/type_ii_symmetric_divisor_fiber_antipodal_physical_capacity.py --verify
~~~
