---
kind: claim
claim_id: type-I-root-capacity-strict-carry-eisenstein-precofactor-quotient
title: 严格 root carry 的 Eisenstein 前 cofactor 商范数门
statement: >-
  对核心素数 p≡1 mod24 的 actual strict proper-root carry，令 h|p^2+p+1、
  c=<D(h-1)^(-1)>_p，并把 c 规范成 canonical even complement n 与距离
  delta=p-n。令 tau=1（c 奇）或 -1（c 偶），以及
  s=(D-tau delta(h-1))/p、v=(p^2+p+1)/h。则
  t=v s^2+tau(2p+1)s delta+h delta^2 是正的 Eisenstein 范数：存在
  beta∈Z[omega] 使 N(beta)=t。更精确地，alpha=D+tau delta-s omega 属于
  范数为 h 的理想 (h,omega-p)，故 alpha=gamma beta、N(gamma)=h。于是每个
  q≡2 mod3 在 t 中的赋值为偶数；并且 q|t 当且仅当 q 同时整除 D、delta、s。
  这给 strict carry 在进入固定 cofactor tail fiber 之前增加了一个 exact Eisenstein
  quotient coordinate；它不自动给出短证书或全局递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-general-endpoint-divisor-gate
  - type-I-root-capacity-strict-carry-complement-even-source-gate
  - type-I-root-capacity-stutter-receipt-factor-split
topics:
  - type-I
  - root-capacity
  - strict-carry
  - pre-cofactor
  - eisenstein-integers
  - norm
  - complete-excess
  - capacity-map
  - proof-boundary
sources:
  - claim: type-I-root-capacity-general-endpoint-divisor-gate
    role: actual-root-receipt-and-canonical-cofactor
  - claim: type-I-root-capacity-strict-carry-complement-even-source-gate
    role: canonical-even-complement-and-distance
  - claim: type-I-root-capacity-stutter-receipt-factor-split
    role: actual-D-and-cyclotomic-support-split
  - reproduction: reproductions/type_i_root_capacity_strict_carry_eisenstein_precofactor_quotient.py
    role: fixed-actual-receipt-ideal-quotient-controls
visibility: public
last_checked: '2026-08-14'
---

# 严格 root carry 的 Eisenstein 前 cofactor 商范数门

## 1. 设置

固定一个核心素数

\[
p\equiv1\pmod {24}
\]

的 actual strict proper-root carry。沿用真实 maximal complete-excess receipt

\[
h\mid p^2+p+1,
\qquad
D\mid ph+1,
\qquad
c=\left\langle D(h-1)^{-1}\right\rangle_p,
\qquad 1\le c\le p-2.
\tag{1}
\]

把 \(c\) 变成 canonical even complement

\[
n=
\begin{cases}
c,&2\mid c,\\
p-c,&2\nmid c,
\end{cases}
\qquad
\delta=p-n,
\qquad
\tau=
\begin{cases}
 1,&2\nmid c,\\
-1,&2\mid c.
\end{cases}
\tag{2}
\]

于是 \(n\) 为偶数、\(\delta\) 为奇数，且

\[
c\equiv\tau\delta\pmod p.
\tag{3}
\]

由 (1) 定义

\[
\boxed{
s=\frac{D-\tau\delta(h-1)}p\in\mathbb Z,
\qquad
v=\frac{p^2+p+1}{h}\in\mathbb Z_{>0}.}
\tag{4}
\]

这里的 \(s\) 是 carry 在 canonical parity 规范下的前 cofactor 坐标；它不是
tail selector 的任意 auxiliary variable。

## 2. 范数理想与精确商

令 \(\omega^2+\omega+1=0\)，并在 Eisenstein 环

\[
\mathcal E=\mathbb Z[\omega]
\]

中使用

\[
N(a+b\omega)=a^2-ab+b^2.
\tag{5}
\]

由于 \(h\mid p^2+p+1\)，评价映射

\[
\varphi_{p,h}:\mathcal E\longrightarrow\mathbb Z/h\mathbb Z,
\qquad
a+b\omega\longmapsto a+bp\pmod h
\tag{6}
\]

是良定义且满射的环同态。其核为

\[
\mathfrak h_{p,h}=(h,\omega-p),
\qquad
\#(\mathcal E/\mathfrak h_{p,h})=h.
\tag{7}
\]

置

\[
\alpha=D+\tau\delta-s\omega.
\tag{8}
\]

由 (4) 有

\[
D+\tau\delta=ps+\tau h\delta,
\tag{9}
\]

故 \(\varphi_{p,h}(\alpha)=\tau h\delta\equiv0\pmod h\)，即

\[
\boxed{\alpha\in\mathfrak h_{p,h}.}
\tag{10}
\]

\(\mathcal E\) 是关于 (5) 的 Euclidean 环，所以 (7) 的理想有一个生成元
\(\gamma_{p,h}\)，满足

\[
(\gamma_{p,h})=\mathfrak h_{p,h},
\qquad N(\gamma_{p,h})=h.
\tag{11}
\]

从 (10) 得到一个实际的整 Eisenstein 商

\[
\boxed{\alpha=\gamma_{p,h}\beta,\qquad\beta\in\mathcal E.}
\tag{12}
\]

这不是抽象的有理范数等式：\(\beta\) 的整性由 carry 的 exact congruence
\(D\equiv\tau\delta(h-1)\pmod p\) 和 \(h\mid p^2+p+1\) 强制。

## 3. 商范数公式

按 (5)、(8)--(9) 展开，得到

\[
\begin{aligned}
N(\alpha)
&=(D+\tau\delta)^2+(D+\tau\delta)s+s^2\\
&=(p^2+p+1)s^2+\tau h(2p+1)s\delta+h^2\delta^2\\
&=h\bigl(vs^2+\tau(2p+1)s\delta+h\delta^2\bigr).
\end{aligned}
\tag{13}
\]

因此定义

\[
\boxed{
t=vs^2+\tau(2p+1)s\delta+h\delta^2=N(\beta)>0.}
\tag{14}
\]

这里 \(\alpha\ne0\)：\(\tau=1\) 时其实部 \(D+\delta\) 为正；\(\tau=-1\)
时若 \(\alpha=0\)，则 \(s=0\) 且 \(D=\delta\)，但 (4) 会给出
\(D=-\delta(h-1)<0\)，矛盾。

等价地，完成平方给出

\[
\boxed{
4vt=\bigl(2vs+\tau(2p+1)\delta\bigr)^2+3\delta^2.}
\tag{15}
\]

式 (15) 单独只显示正定性；(10)--(14) 更强，因为它给出 \(t\) 的整
Eisenstein 商，而不只是一个二元二次型值。

## 4. Inert 素因子的精确位置

令 \(q\equiv2\pmod3\) 为任意有理素数，包括 \(q=2\)。先注意

\[
q\nmid h.
\tag{16}
\]

事实上 \(q\mid h\) 会使 \(q\mid p^2+p+1\)。若 \(q\ne3\)，则 \(p\) 在
\(\mathbb F_q^\times\) 中有阶 \(3\)，迫使 \(q\equiv1\pmod3\)；\(q=2\) 也不整除
\(p^2+p+1\)，矛盾。

在 \(\mathcal E\) 中，这样的 \(q\) 保持为素理想。由 (12)、(16)，有

\[
q\mid t=N(\beta)
\Longrightarrow q\mid\beta
\Longrightarrow q\mid\alpha.
\tag{17}
\]

后一个整除表示 \(q\mid s\) 与 \(q\mid D+\tau\delta\)。再由 (9) 和
\(q\nmid h\)，得到 \(q\mid\delta\)，继而 \(q\mid D\)。反向地，若
\(q\mid D,\delta,s\)，则 \(q\mid\alpha\)，所以 \(q^2\mid N(\alpha)=ht\)，再用
(16) 得 \(q\mid t\)。故有精确的来源定位

\[
\boxed{
q\equiv2\pmod3
\quad\Longrightarrow\quad
q\mid t\ \Longleftrightarrow\ q\mid\gcd(D,\delta,s).}
\tag{18}
\]

特别地，所有 \(q\equiv2\pmod3\) 都以偶数赋值出现于 \(t\)：

\[
\boxed{q\equiv2\pmod3\Longrightarrow v_q(t)\equiv0\pmod2.}
\tag{19}
\]

确实，若 \(q^j\Vert\beta\) 于 \(\mathcal E\)，则 \(N(\beta)\) 中恰含
\(q^{2j}\)；这里利用 \((q)\) 在 \(\mathcal E\) 中保持为素。

这把 inert 素因子从一个没有来源的范数余项，收紧成 actual receipt divisor、
canonical complement distance 与前 cofactor 坐标的三重公共因子。它可与既有的
\(D_C\mid h^2-1\)、\(D_T\mid h^2-h-2r\) 分裂联立；但在尚未给出这一联立必命中
terminal 的证明前，不能把 (18) 当作全局出口。

## 5. 两个 sharp controls

真实 high-half control

\[
p=313,\quad r=271,\quad h=543,\quad D=8,\quad c=n=298
\]

给出

\[
\delta=15,\quad\tau=-1,\quad s=26,\quad v=181,\quad t=1.
\]

可以取

\[
\gamma=-7-26\omega=\alpha,
\qquad\beta=1.
\tag{20}
\]

故这个困难 high-half receipt 位于理想商范数的单位纤维；这解释了为什么仅从
\(t\) 的素因子无法强制它的 tail selector 命中。

另一方面，取实际 strict control

\[
p=193,\quad r=3,\quad h=21,\quad D=2,\quad c=n=58,
\]

有

\[
\delta=135,\quad\tau=-1,\quad s=14,\quad t=763=7\cdot109,
\qquad (h,t)=7.
\tag{21}
\]

例如 \(\gamma=-1-5\omega\)、\(\beta=-22-31\omega\)。所以不能把 (14)
错误强化为 \((h,t)=1\)。另一个 actual control

\[
(p,r,h,D,c,\delta,s,t)=(577,66,57,10,62,515,50,4075)
\tag{22}
\]

满足 \(4075=5^2\cdot163\)，并且 inert prime \(5\) 的确同时整除
\(D,\delta,s\)，验证 (18) 的非空边界。

## 6. 对 global-exit 目标的作用与边界

这个结论发生在 fixed \((p,c)\) tail fiber 之前：它把 actual strict receipt 的
\((D,h,c)\) 字段压成固定范数 \(h\) 的 Eisenstein quotient coordinate \(\beta)，并精确
标出 inert residual 只能从哪里进入。它提供了把 actual \(D\) 的因子分裂接回
pre-cofactor 分类的一个新接口。

它尚未证明坏 cofactor 不可达，也没有构造 Type I/II terminal、\(n<p\) 的解提升或
E1--E5 已注册递归边。特别地，(20) 表明任何只依赖 \(t\) 非平凡素因子的方案都不能
覆盖全部 strict carries；下一步必须使用 \(\beta\) 的完整坐标，或把 (18) 与 actual
\(D_C/D_T\) 分裂和 external-source menu 做联合分流。

## 聚焦复现

~~~bash
python3 reproductions/type_i_root_capacity_strict_carry_eisenstein_precofactor_quotient.py --verify
~~~

脚本只重放四个 actual strict receipts、构造范数为 \(h\) 的 Eisenstein ideal generator、
验证整商与 inert 素因子定位，并保留两个 sharp boundary；不执行素数、分母或 selector
范围搜索。
