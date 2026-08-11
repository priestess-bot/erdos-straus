---
kind: claim
claim_id: type-II-p-minus-one-jacobi-source-localization-collision-capacity
title: p-1 因子 Type II 的 Jacobi 源因子定位、奇偶门与跨 q 碰撞容量
statement: >-
  设 p=4U+1=4qr+1 为素数，m=4q-1，x=U+q=q(r+1)。模 m 的
  Jacobi 角色在 q 的每个素因子上恒为 +1，而在 r+1 的每个素因子 ell
  上恰等于 Kronecker 符号 (p/ell)。因此所有 Jacobi 负方向都来自严格递降源
  n=r+1；Type II signed-box 命中必须在这些负源素数上的总指数为奇数。
  负源集为空时立即得到规范 G 证书；若单位群循环且阶为 2 乘奇数，则负源集
  非空又等价于目标 -1 已在源支撑群中。固定 U 跨 q 时，同一负源素数 ell
  只能出现在 q 同余于 -U mod ell 的状态，故任意区间 [A,B] 中的出现次数至多
  floor((B-A)/ell)+1。这给出从 Jacobi 角色到真实 r+1 整数素因子候选槽的规范
  owner 映射和碰撞容量，但不自动证明 physical source-column 实现、源关系格独立、
  Hall--Rado 可行或 E4/E5 递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - short-certificate-equivalence
  - type-II-two-tail-deflation-descent
  - type-II-p-minus-one-endpoint-envelope-large-prime-allocation
  - type-II-p-minus-one-divisor-downset-prime-power-allocation
  - type-I-fg-fourier-to-type-II-role-demand-bridge
topics:
  - type-II
  - p-minus-one
  - Jacobi-character
  - quadratic-reciprocity
  - source-factor
  - source-localization
  - parity-gate
  - cross-state-capacity
  - collision-bound
  - F-G-state
  - selector
sources:
  - claim: type-II-two-tail-deflation-descent
    role: exact-p-minus-one-source-and-lift
  - claim: type-II-p-minus-one-endpoint-envelope-large-prime-allocation
    role: signed-box-F-G-fibers-and-p67369-dispatch
  - claim: type-II-p-minus-one-divisor-downset-prime-power-allocation
    role: canonical-allowed-q-domain
  - claim: type-I-fg-fourier-to-type-II-role-demand-bridge
    role: role-to-integer-source-factor-and-physical-column-boundary
  - reproduction: reproductions/type_ii_p_minus_one_jacobi_source_localization.py
    role: focused-reciprocity-parity-incidence-and-control-verifier
visibility: public
last_checked: '2026-08-11'
---

# \(p-1\) 因子 Type II 的 Jacobi 源因子定位、奇偶门与跨 \(q\) 碰撞容量

## 1. 设置与主定理

设

\[
p=4U+1=4qr+1
\tag{1}
\]

为素数，其中 \(q,r\ge1\)。对应的 \(p-1\) 因子 Type II 图表为

\[
m=4q-1,
\qquad
x=\frac{p+m}{4}=U+q=q(r+1),
\qquad
n=r+1.
\tag{2}
\]

这里 \(n\) 正是双尾递降后的严格较小源。已有正规形给出

\[
(m,x)=1.
\tag{3}
\]

在单位群 \((\mathbb Z/m\mathbb Z)^\times\) 上定义 Jacobi 角色

\[
\chi_m(a)=\left(\frac{a}{m}\right).
\tag{4}
\]

对素数 \(\ell\) 再记

\[
\varepsilon_p(\ell)=\left(\frac{p}{\ell}\right)_{\!K},
\tag{5}
\]

其中下标 \(K\) 表示在 \(\ell=2\) 时使用 Kronecker 符号。则有

\[
\boxed{
\ell\mid q\Longrightarrow\chi_m(\ell)=1,}
\tag{6}
\]

\[
\boxed{
\ell\mid r+1\Longrightarrow
\chi_m(\ell)=\varepsilon_p(\ell).}
\tag{7}
\]

所以负 Jacobi 源集可规范定义为

\[
\boxed{
\mathcal N_q(p)=
\{\ell\text{ 为素数}:\ell\mid r+1,\quad
\varepsilon_p(\ell)=-1\}.}
\tag{8}
\]

式 (6)--(7) 说明：抽象的负二次角色没有藏在载体 \(q\) 中，而是逐个定位到
严格递降源 \(n=r+1\) 的真实素因子。

## 2. 载体 \(q\) 的 Jacobi 中性

先取奇素数 \(\ell\mid q\)。因为

\[
m=4q-1\equiv-1\pmod\ell,
\qquad
m\equiv3\pmod4,
\]

Jacobi 二次互反律给出

\[
\begin{aligned}
\left(\frac{\ell}{m}\right)
&=(-1)^{\frac{\ell-1}{2}\frac{m-1}{2}}
  \left(\frac{m}{\ell}\right)\\
&=\left(\frac{-1}{\ell}\right)
  \left(\frac{-1}{\ell}\right)
=1.
\end{aligned}
\tag{9}
\]

这里不要求 \(m\) 为素数；奇分母的 Jacobi 互反律已经足够。

若 \(2\mid q\)，则 \(m\equiv7\pmod8\)，从而

\[
\left(\frac2m\right)=1.
\tag{10}
\]

这就证明 (6)。特别地，\(q\) 的任意素数次幂都只贡献平凡角色。

## 3. \(r+1\) 上的源互反公式

先取奇素数 \(\ell\mid r+1\)。由 \(r\equiv-1\pmod\ell\)，

\[
p=4qr+1\equiv1-4q=-m\pmod\ell.
\tag{11}
\]

再次使用 \(m\equiv3\pmod4\) 和二次互反律，

\[
\begin{aligned}
\left(\frac{\ell}{m}\right)
&=\left(\frac{-1}{\ell}\right)
  \left(\frac{m}{\ell}\right)\\
&=\left(\frac{-m}{\ell}\right)
=\left(\frac{p}{\ell}\right).
\end{aligned}
\tag{12}
\]

若 \(\ell=2\)，则 \(r\) 为奇数。此时只有两种情形：

\[
\begin{array}{c|c|c}
q\bmod2&m\bmod8&p\bmod8\\ \hline
0&7&1\\
1&3&5.
\end{array}
\tag{13}
\]

两行分别给出

\[
\left(\frac2m\right)
=\left(\frac p2\right)_{\!K}
=1
\quad\text{或}\quad
\left(\frac2m\right)
=\left(\frac p2\right)_{\!K}
=-1.
\]

故 (7) 对 \(\ell=2\) 也成立。

若某个素数同时整除 \(q\) 与 \(r+1\)，则 (6)--(7) 迫使

\[
\varepsilon_p(\ell)=1.
\tag{14}
\]

因此

\[
\boxed{\mathcal N_q(p)\cap\{\ell:\ell\mid q\}=\varnothing.}
\tag{15}
\]

每个负角色因子都确实属于源 \(r+1\)，不会与 \(q\)-载体重名。

## 4. signed box 的负源奇偶门

对 \(x\) 的每个素因子 \(\ell\) 取整数指数 \(z_\ell\)，并在模 \(m\) 的单位群中写

\[
\rho(z)=\prod_{\ell\mid x}\ell^{z_\ell}.
\tag{16}
\]

由 (6)--(8)，负指数按单位群逆元解释时仍有

\[
\boxed{
\chi_m(\rho(z))
=(-1)^{\sum_{\ell\in\mathcal N_q(p)}z_\ell}.}
\tag{17}
\]

具体地，对任意 \(d\mid x^2\)，令

\[
z_\ell=v_\ell(d)-v_\ell(x),
\qquad
-v_\ell(x)\le z_\ell\le v_\ell(x).
\tag{18}
\]

则 \(\rho(z)\equiv d/x\pmod m\)，而 Type II 目标同余正是

\[
\rho(z)\equiv-1\pmod m.
\tag{19}
\]

因为 \(m\equiv3\pmod4\)，

\[
\chi_m(-1)=-1.
\tag{20}
\]

所以每张 Type II 命中都必须满足严格奇偶门

\[
\boxed{
\sum_{\ell\in\mathcal N_q(p)}
\bigl(v_\ell(d)-v_\ell(x)\bigr)
\equiv1\pmod2.}
\tag{21}
\]

这不仅适用于有界盒；任何由 \(x\) 的素因子生成的无界目标关系也必须使用至少一个
真实负源因子。

若 \(\mathcal N_q(p)=\varnothing\)，则源支撑群全部落入
\(\ker\chi_m\)，而 \(-1\) 在核外。因此立即得到

\[
\boxed{
\mathcal N_q(p)=\varnothing
\Longrightarrow
\text{\(q\)-纤维有规范 Jacobi G 证书}.}
\tag{22}
\]

反向一般不能只凭 Jacobi 角色断言。设

\[
H_q=\langle\ell\bmod m:\ell\mid x\rangle.
\tag{23}
\]

若单位群循环且

\[
\varphi(m)=2s,\qquad s\text{ 为奇数},
\tag{24}
\]

则单位群只有一个二阶元 \(-1\)。任何满足
\(\chi_m(a)=-1\) 的元素都有偶阶，其生成子群必包含该唯一二阶元。于是此时有精确判据

\[
\boxed{
\mathcal N_q(p)=\varnothing
\iff -1\notin H_q,
\qquad
\mathcal N_q(p)\ne\varnothing
\iff -1\in H_q.}
\tag{25}
\]

特别地，\(m\) 为素数时总满足 (24)。在 (25) 的第二支中，有界 signed box
若仍 miss，才可称为 F；负源非空本身不证明有界命中。若 \(m\) 为一般合数，单位群
可能有多个二阶元，负源非空也不保证 \(-1\in H_q\)，仍须执行完整支撑群测试。

## 5. 跨 \(q\) 的真实源因子碰撞容量

现在固定 \(p=4U+1\)，让 \(q\) 在 \(U\) 的某个有限因子域
\(\mathcal D\subseteq\{q:q\mid U\}\) 中变化。对任意素数 \(\ell\)，有更直接的
入射刻画

\[
\boxed{
\ell\in\mathcal N_q(p)
\iff
\ell\mid U+q
\quad\text{且}\quad
\varepsilon_p(\ell)=-1.}
\tag{26}
\]

正向由 \(U+q=q(r+1)\) 立即得到。反向中，若 \(\ell\mid q\)，则
\(\ell\mid U\) 且 \(p=4U+1\) 在 \(\ell\) 上的 Kronecker 符号为 \(+1\)，与
假设矛盾；故 \(\ell\nmid q\)，从 \(\ell\mid q(r+1)\) 可约去 \(q\)，得到
\(\ell\mid r+1\)。

因此若同一负源素数出现在两个状态 \(q_i,q_j\)，则

\[
q_i\equiv q_j\equiv-U\pmod\ell
\]

并且

\[
\boxed{\ell\mid(q_i-q_j).}
\tag{27}
\]

定义真实出现度

\[
\deg_{\mathcal D}(\ell)
=\#\{q\in\mathcal D:\ell\in\mathcal N_q(p)\}.
\tag{28}
\]

若 \(\mathcal D\subseteq[A,B]\)，同一剩余类在该区间至多出现
\(\lfloor(B-A)/\ell\rfloor+1\) 次，故

\[
\boxed{
\deg_{\mathcal D}(\ell)
\le
\left\lfloor\frac{B-A}{\ell}\right\rfloor+1.}
\tag{29}
\]

特别地，\(\ell>B-A\) 时该负源槽是私有槽。对核心素数
\(p\equiv1\pmod{24}\)，有

\[
\varepsilon_p(2)=\varepsilon_p(3)=1,
\tag{30}
\]

所以所有负源素数均至少为 \(5\)。

对每个非空负源集可取规范 owner

\[
o(q)=\min\mathcal N_q(p).
\tag{31}
\]

这给出一个完全由整数因子决定的映射

\[
q\longmapsto
\operatorname{SOURCE\_QUADRATIC\_FACTOR\_SLOT}(o(q)),
\tag{32}
\]

且任一 \(\ell\) 的 owner 负载不超过 (29)。相反，任何声称把多于
\(\deg_{\mathcal D}(\ell)\) 个状态分配给同一 \(\ell\)-槽的方案，都有严格回执

\[
\operatorname{SOURCE\_PRIME\_COLLISION\_CAPACITY\_DEFICIT}.
\tag{33}
\]

式 (29) 计数的是源分母 \(r+1\) 中同一个真实素数的跨状态出现，不是抽象角色维数。

## 6. 三组控制

### 6.1 \(p=73\)：奇偶门确实约束 Type II 命中

这里 \(U=18\)。四个状态的负源集包括

\[
\mathcal N_1(73)=\varnothing,
\qquad
\mathcal N_2(73)=\{5\},
\qquad
\mathcal N_3(73)=\{7\},
\qquad
\mathcal N_6(73)=\varnothing.
\tag{34}
\]

对 \(q=2\)，有 \(m=7,x=20\)，而 \(d=1\) 是 Type II 命中。其 \(5\)-指数差为

\[
v_5(1)-v_5(20)=-1,
\]

恰为奇数，验证 (21)。

### 6.2 \(p=337\)：允许域内的碰撞界取等

这里 \(U=84\)，两个端点允许状态 \(q=1,6\) 都含负源素数 \(5\)：

\[
5\mid85=U+1,
\qquad
5\mid90=U+6.
\tag{35}
\]

二者之差恰为 \(5\)。在区间 \([1,6]\) 中，

\[
\deg_{\{1,6\}}(5)=2
=\left\lfloor\frac{6-1}{5}\right\rfloor+1,
\tag{36}
\]

所以 (29) 可取等。对 \(q=6\)，\(m=23,x=90,d=2\) 又是实际 Type II 命中，
其唯一负源 \(5\) 的指数差为 \(-1\)。

### 6.3 \(p=67369\)：五张 G 与三张 F 的源侧解释

已有端点反链把允许域压成 \(q\mid42\)。新公式给出

\[
\begin{array}{c|c}
q&\mathcal N_q(67369)\\ \hline
1&\varnothing\\
2&\varnothing\\
3&\varnothing\\
6&\varnothing\\
7&\{29,83\}\\
14&\varnothing\\
21&\{73\}\\
42&\{67\}.
\end{array}
\tag{37}
\]

因此旧分类中的五张 G 证书不再只是逐行符号表，而统一来自 (22)。余下三个模数

\[
m_7=27,\qquad m_{21}=83,\qquad m_{42}=167
\]

的单位群都循环且阶分别为 \(18,82,166\)，故 (25) 证明目标 \(-1\) 已在源支撑群中；
结合已有有界盒 miss，它们严格属于 F。式 (37) 还把三张 F 的角色分别落实为

\[
\{29,83\},\qquad\{73\},\qquad\{67\}
\]

这些 \(r+1\) 的真实素因子，而不是无来源的 Fourier 标签。

## 7. 选择器接口与严格边界

在端点禁止反链先把 \(q\) 压到下闭允许域 \(\mathcal C_U\) 后，选择器可逐状态执行：

\[
\boxed{
\begin{array}{ll}
\mathcal N_q(p)=\varnothing
&\Rightarrow
\operatorname{JACOBI\_G\_SOURCE\_TRIVIAL},\\[2mm]
\mathcal N_q(p)\ne\varnothing
&\Rightarrow
\text{登记整数源因子候选 }
\operatorname{SOURCE\_QUADRATIC\_FACTOR\_SLOT}(\ell)
\text{ 及奇偶门 (21)}.
\end{array}}
\tag{38}
\]

第一支只是支撑分离，不应收取 Type II source-rank 或 \(q\)-height 容量。第二支已经
解决角色的 integer source-factor provenance，并由 (29) 给出跨状态 occurrence
容量；physical source-column realization 仍是后续门。

本定理仍没有证明以下任何一步：

1. 不同 \(\ell\)-槽在整数源关系格或 SNF 商中独立；
2. 带角色需求满足 Hall--Rado 匹配；
3. 某个 F miss 自动产生 Type I/II 终端；
4. owner 槽自动满足统一边合同 E4 的全域提升与 E5 的严格良基下降。

所以 (38) 是从 F/G 对偶证书到整数源因子 occurrence 账本的必要算术提升，不是把
analysis evidence 误升级成 verified edge。下一决定性对象是：在
\(\mathcal N_q(p)\ne\varnothing\) 的允许状态上先实现 physical source columns，
再计算源关系格的实际评价矩阵，并证明
其满配、容量缺口或可提升递降三分。

聚焦验证：

~~~bash
python3 reproductions/type_ii_p_minus_one_jacobi_source_localization.py --verify
~~~

验证器只检查本定理的互反恒等式、命中奇偶、碰撞取等及 \(p=67369\) 的源集合；
不重复运行既有有界盒或历史素数范围测试。
