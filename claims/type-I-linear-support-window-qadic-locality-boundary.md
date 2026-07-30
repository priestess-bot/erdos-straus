---
kind: claim
claim_id: type-I-linear-support-window-qadic-locality-boundary
title: 线性源因子支撑窗口的 q 进局部性边界
statement: 固定线性源 p=a+s+asR，令 U=aR+1、V=sR+1、K_R=UV/4。对满足 q|K_R 的奇素数 q，令 k=v_q(K_R)，则 k=v_q(U)+v_q(V)，并分别推出 q 进块高度、标签同余和同标签模数差同余；固定标签和有限 R 窗口内的载体数可由 (p-t)/q^j 的除子注入精确上界。但这些同余不排除窗口外载体，也不赋予离开窗口的额外 q 进成本；p=3001 的显式单坐标 F-box 溢出给出反例。q=2 需先扣除 UV 中的固定 4 因子。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-linear-block-divisor-q-adic-capacity
  - type-I-linear-block-label-collision
  - type-I-f-overflow-cross-state-qadic-capacity
topics:
- type-I
- linear-source
- q-adic
- support-window
- overflow
- cross-state
- capacity
- counterexample
- proof-program
sources:
- claim: type-I-linear-block-divisor-q-adic-capacity
  role: fixed-label-divisor-capacity
- claim: type-I-linear-block-label-collision
  role: label-collision-congruence
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-linear-normal-form-context
visibility: public
last_checked: '2026-07-30'
---

# 线性源因子支撑窗口的 \(q\) 进局部性边界

## 线性块与指数分拆

固定核心素数 \(p\)，取一个线性源状态

\[
p=a+s+asR,\qquad R\equiv3\pmod4,
\]

并令

\[
U=aR+1,\qquad V=sR+1,\qquad
K_R=\frac{UV}{4}=\frac{pR+1}{4}.
\tag{1}
\]

两个块满足

\[
U\mid p-a,\qquad V\mid p-s,\qquad
U\equiv V\equiv1\pmod R.
\tag{2}
\]

设 \(q\) 为满足 \(q\mid K_R\) 的奇素数。由于 \(q\nmid R\)，写

\[
r_q=v_q(U),\qquad \ell_q=v_q(V),\qquad
\nu_q=v_q(K_R).
\]

除以 4 不改变奇素数指数，故有精确恒等式

\[
\boxed{\nu_q=r_q+\ell_q.}
\tag{3}
\]

同时 \(4\) 在模 \(q^k\) 下可逆，所以对任意 \(k\le\nu_q\) 有全局同余链

\[
q^k\mid K_R
\Longrightarrow
q^k\mid pR+1
\Longrightarrow
pR\equiv-1\pmod{q^k}
\Longrightarrow
R\equiv-p^{-1}\pmod{q^k}.
\tag{3a}
\]

这里 \(q\nmid p\) 由 \(pR\equiv-1\pmod q\) 自动推出。式 (3a) 只给出总支撑的
一个剩余类；它不能决定 \(q^k\) 是否集中在 \(U\)、\(V\) 的一个块中，这正是
式 (3) 的分拆信息不可省略的原因。

因此 \(q^k\mid K_R\) 只说明 \(k\le r_q+\ell_q\)；它不自动说明
\(q^k\) 全部落在 \(U\) 或 \(V\) 的一个颜色中。若 \(r_q>0\) 或 \(\ell_q>0\)，分别有

\[
\begin{aligned}
q^{r_q}\mid U
&\Longrightarrow
aR\equiv-1\pmod{q^{r_q}}
\Longrightarrow
R\equiv-a^{-1}\pmod{q^{r_q}},\\
q^{\ell_q}\mid V
&\Longrightarrow
sR\equiv-1\pmod{q^{\ell_q}}
\Longrightarrow
R\equiv-s^{-1}\pmod{q^{\ell_q}}.
\end{aligned}
\tag{4}
\]

这里的逆元存在，因为 \(q\mid aR+1\) 或 \(q\mid sR+1\) 时分别有
\(q\nmid a\) 或 \(q\nmid s\)。结合 (2)，同一链还给出

\[
\boxed{
\begin{aligned}
q^{r_q}&\mid p-a,\\
q^{\ell_q}&\mid p-s.
\end{aligned}}
\tag{5}
\]

式 (3)--(5) 是从 \(q^k\mid K_R\) 能无条件得到的精确 \(q\)-进代数信息：
它记录了总指数、两个颜色的分拆、模数剩余类和对应端点标签除性。

## 同标签的模数差与窗口内除子注入

用 \(\tau\in\{a,s\}\) 统一记一个块标签，写

\[
B_{\tau,R}=\tau R+1.
\]

若同一标签 \(\tau\) 的两个状态在 \(R,R'\) 上分别具有
\(q^j\mid B_{\tau,R}\) 和 \(q^h\mid B_{\tau,R'}\)，令
\(d=\min(j,h)\)。相减得到

\[
q^d\mid \tau(R'-R).
\]

而 \(q\nmid\tau\)，所以

\[
\boxed{q^{\min(j,h)}\mid R'-R.}
\tag{6}
\]

若标签不同，设 \(q^j\mid B_{\tau,R}\)、\(q^h\mid B_{\sigma,R'}\)，则由
\(B_{\tau,R}\mid p-\tau\)、\(B_{\sigma,R'}\mid p-\sigma\) 得

\[
\boxed{q^{\min(j,h)}\mid \tau-\sigma.}
\tag{7}
\]

式 (6) 才是可以称为“\(R\)-窗口局部性”的部分：固定同一标签和同一层 \(q^j\)
时，所有载体模数位于一个模 \(q^j\) 的剩余类中。对有限区间
\(I=[R_{\min},R_{\max}]\cap\mathbb Z\)，定义

\[
\mathcal C_{\tau,j}(p;I)
=\{R'\in I:q^j\mid B_{\tau,R'},\ B_{\tau,R'}\mid p-\tau\}.
\]

取

\[
d'=\frac{B_{\tau,R'}}{q^j}.
\]

则有一个不依赖选择顺序的单射

\[
\begin{aligned}
d'&\mid\frac{p-\tau}{q^j},\\
q^jd'&\equiv1\pmod\tau,\\
R'&=\frac{q^jd'-1}{\tau}.
\end{aligned}
\tag{8}
\]

从而

\[
\boxed{
|\mathcal C_{\tau,j}(p;I)|
\le
\min\left\{
\left\lfloor\frac{R_{\max}-R_{\min}}{q^j}\right\rfloor+1,\,
\tau_{\mathrm{div}}\left(\frac{p-\tau}{q^j}\right)
\right\},
}
\tag{9}
\]

其中 \(\tau_{\mathrm{div}}(n)\) 表示正除子数，且 \(q^j\nmid p-\tau\) 时第二项按 0 解释。
式 (9) 是严格的窗口内容量界，
与已有同标签除子容量卡相同；它没有对 \(I\) 外的 \(R'\) 作断言。

## \(q=2\) 的固定因子修正

若 \(q=2\)，必须保留 (1) 中的除数 4。令

\[
\alpha=v_2(U),\qquad \beta=v_2(V),\qquad
\nu_2=v_2(K_R),
\]

则

\[
\boxed{\alpha+\beta=\nu_2+2.}
\tag{10}
\]

因此不能把 \(\nu_2\) 直接等同于单一块的二进高度。对任一实际块高度
\(\alpha\) 或 \(\beta\)，(4)--(9) 仍可逐层使用；但把 \(2^k\mid K_R\)
转换为载体需求时，必须先说明 \(k+2\) 个 \(UV\) 指数如何在两块和固定因子 4
之间分配。忽略这一点会把二进容量高估两层。

## 结构性窗口外反例族

上述局部性不能从线性恒等式升级为与 \(p\) 无关的统一绝对窗口。给定奇素数
\(q\)、整数 \(k\ge1\) 和 \(T\ge1\)，取

\[
R_1=4q^k-1,\qquad
R_2=4q^k(T+1)-1,\qquad
M=\operatorname{lcm}\!\left(24,\,4q^k(T+1)\right).
\tag{11}
\]

选择一个满足 \(p\equiv1\pmod M\) 且 \(p>R_2+1\) 的素数；这样的素数由
Dirichlet 定理存在无穷多个。对这个**固定的 \(p\)**，令

\[
s_1=s_2=1,\qquad
a_i=\frac{p-1}{R_i+1}\quad(i=1,2).
\tag{12}
\]

因为 \(R_i+1\mid M\)，两组参数都满足

\[
p=a_i+1+a_iR_i,\qquad
R_i\equiv3\pmod4,
\]

并且

\[
q^k\mid R_i+1,\qquad q^k\mid K_{R_i}
\tag{13}
\]

两状态的模数距离为

\[
R_2-R_1=4q^kT.
\tag{14}
\]

若 \(q\nmid T\)，则 \(v_q(R_2-R_1)=k\)，所以即使距离按 \(T\) 任意放大，
也没有增加超过共享层的 \(q\)-进差价。这里 \(T\) 变化时为构造方便而重新选择
\(p\)；每个实例内部的 \(p\) 是固定的。因此该族只排除一个不依赖 \(p\) 的统一
Archimedean \(R\)-窗口，不声称对某个固定 \(p\) 存在无限多个状态。

最小易读实例取 \(q=3,k=1,T=5\)，则 \(M=72\)、\(p=73\)，并得到

\[
(a_1,s_1,R_1)=(6,1,11),\qquad
(a_2,s_2,R_2)=(1,1,71),
\]

\[
K_{R_1}=201=3\cdot67,\qquad
K_{R_2}=1296=2^4\cdot3^4,\qquad
R_2-R_1=60.
\tag{15}
\]

这只是共同 \(q\)-支撑和远距离线性合法性的结构性反例；它不声称两个状态都是
F-box miss。下一节的 \(p=3001\) 例则同时满足单坐标 F-box 溢出。

## 窗口外没有自动额外收费：显式反例

下面给出一个完全可手算复核的奇素数反例。取素数

\[
p=3001\equiv1\pmod {24},\qquad (a,s,R)=(30,1,99).
\]

则

\[
3001=30+1+30\cdot1\cdot99,\qquad
U=2971,\qquad V=100,
\]

以及

\[
K_R=\frac{2971\cdot100}{4}=74275=5^2\cdot2971.
\tag{16}
\]

取真因子 \(t=9\mid R\)，有 \(t\equiv1\pmod4\)。因为

\[
2971\equiv1\pmod9,\qquad
5^{-3}\equiv2^3\equiv8\equiv-1\pmod9,
\]

向量

\[
z=(-3,0)
\]

（坐标顺序 \(5,2971\)）属于目标纤维。另一方面，指数盒
\(|z_5|\le2,\ |z_{2971}|\le1\) 内，第二坐标恒为 1 模 9，而

\[
\{5^e\bmod9:-2\le e\le2\}
=\{1,2,4,5,7\}
\]

不含 \(-1\equiv8\)。所以这是一个单坐标 F-box miss，且 \(5\)-坐标溢出一层：
\(|z_5|-\nu_5=3-2=1\)。

现在看同一核心素数的另一个合法线性源

\[
(a',s',R')=(1,1,2999),\qquad
3001=1+1+1\cdot1\cdot2999.
\]

它使用同一标签 \(s'=1\)，并且

\[
B_{1,2999}=1\cdot2999+1=3000=5^3\cdot24.
\tag{17}
\]

所以 \(R'=2999\) 的同标签块恰好提供需求所需的三层 \(5\)-进高度。若把当前支撑
窗口取为一个包含 \(R=99\) 的有限窗口（例如 \(I=[3,215]\)），则 \(R'\notin I\)，
但没有产生额外的 \(5\)-进层：需求是三层，(12) 正好提供三层。与此同时

\[
R'-R=2900=5^2\cdot116,\qquad
v_5(R'-R)=2=\nu_5(K_R),
\tag{18}
\]

说明 (6) 只保留了原有的两层共享同余；离开窗口的距离没有强制增加一层或更多
\(5\)-进收费。这也展示了为什么必须区分“窗口内除子容量”和“全谱载体迁移”。

## 结论边界与缺失条件

因此，下列强命题是假的：

\[
\text{“所有 \(q\)-进溢出需求都必须由因子支撑的有限 \(R\)-窗口支付。”}
\]

从线性恒等式无条件成立的只是：

1. 奇素数总指数按 (3) 在两个块颜色之间分拆；
2. 同标签同层满足 (6)，异标签共享层满足 (7)；
3. 固定有限窗口内的载体数满足除子上界 (9)；
4. 二进方向必须使用修正后的指数关系 (10)。

要把 (9) 升级为选择器所需的全局收费或严格递降，至少还需一个额外算术条件：

1. **载体映射条件**：每个关系格溢出层 \(e_q\) 映射到某个确定标签 \(\tau\) 和除子
   \(B_{\tau,R'}\)，且不同需求的映射在 (8) 的除子账本中不重复；
2. **窗口闭合条件**：所有满足该映射的除子都证明 \(R'\in I\)，或窗口外的
   \(R'\) 带有一个可加的势函数并产生严格下降；
3. **标签迁移排除条件**：对 \(\tau\ne\sigma\) 的载体，利用 (7) 排除
   \(q^{\min(j,h)}\mid\tau-\sigma\)，否则需求可跨标签转移；
4. **二进分配条件**：对 \(q=2\) 明确分配 (10) 中的固定两层，不能把
   \(v_2(K_R)\) 当作单块高度。

在没有这些条件前，“因子支撑 \(R\)-窗口”只能作为局部容量账本，不能作为
盒外层必付费或必递降的全称定理。
