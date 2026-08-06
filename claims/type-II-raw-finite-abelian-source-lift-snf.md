---
kind: claim
claim_id: type-II-raw-finite-abelian-source-lift-snf
title: Type II raw 参数频率的有限阿贝尔源商 SNF 提升
statement: 对任意有限阿贝尔真实源关系商，将源单位与锚点的参数角色提升问题精确化为一个整数线性同余系统；其 Smith 正规形给出角色存在的充要整除条件、显式构造以及失败时的有限关系矛盾证书。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-raw-cyclic-source-lift-matrix
  - type-II-kernel-fourier-source-relation-compatibility
topics:
  - type-II
  - raw-ray
  - finite-abelian-source-quotient
  - Fourier
  - SNF
  - congruence
  - lift-compatibility
  - certificate
sources:
  - claim: type-II-raw-cyclic-source-lift-matrix
    role: cyclic-special-case
  - claim: type-II-kernel-fourier-source-relation-compatibility
    role: affine-source-relation-gate
visibility: public
last_checked: '2026-08-05'
---

# Type II raw 参数频率的有限阿贝尔源商 SNF 提升

## 1. 一般源商与参数标签

令真实源关系商分解为

\[
H=\bigoplus_{\nu=1}^{d} C_{m_\nu},
\qquad
C_{m_\nu}=\langle g_\nu\rangle.
\tag{1}
\]

给定 \(r\) 个源单位和一个目标锚点，写成

\[
u_j=\sum_{\nu=1}^{d}c_{j\nu}g_\nu\quad(1\le j\le r),
\qquad
\alpha=\sum_{\nu=1}^{d}c_{0\nu}g_\nu,
\tag{2}
\]

其中 \(c_{j\nu}\in\mathbb Z/m_\nu\mathbb Z\)。把它们通过带来源的 raw 标记送入
\(\mathbb Z/e\mathbb Z\)，记标签为

\[
\lambda_j,\lambda_0\in\mathbb Z/e\mathbb Z.
\tag{3}
\]

对频率 \(k\in\mathbb Z/e\mathbb Z\)，目标参数相位仍为

\[
\eta_k(x)=\exp\!\left(\frac{2\pi i kx}{e}\right).
\tag{4}
\]

标签只是待检验的相位数据，不自动构成从 \(H\) 到 \(\mathbb Z/e\mathbb Z\) 的群同态。

## 2. 整数同余系统

每个 \(H\) 的角色由 \(s=(s_1,\ldots,s_d)\) 参数化，其中
\(s_\nu\in\mathbb Z/m_\nu\mathbb Z\)，且

\[
\chi_s\!\left(\sum_\nu x_\nu g_\nu\right)
=
\exp\!\left(
2\pi i\sum_{\nu=1}^{d}\frac{s_\nu x_\nu}{m_\nu}
\right).
\tag{5}
\]

取

\[
L=\operatorname{lcm}(e,m_1,\ldots,m_d),
\qquad
A_{j\nu}=L\frac{c_{j\nu}}{m_\nu}\in\mathbb Z,
\qquad
b_j=L\frac{k\lambda_j}{e}\in\mathbb Z,
\tag{6}
\]

其中 \(c_{j\nu}\) 和 \(\lambda_j\) 取任意整数代表。要求源单位和锚点的角色分别等于
\(\eta_k(\lambda_j)\) 与 \(\eta_k(\lambda_0)\)，等价于

\[
\sum_{\nu=1}^{d}A_{j\nu}s_\nu\equiv b_j\pmod L,
\qquad
j=0,1,\ldots,r.
\tag{7}
\]

这是一个 \(t=r+1\) 行、\(d\) 个角色变量的有限同余系统。改变
\(s_\nu\) 为 \(s_\nu+m_\nu\) 会使左侧改变 \(L c_{j\nu}\)，所以 (7) 与
\(s_\nu\pmod{m_\nu}\) 无关。

把 \(A\) 视为 \(t\times d\) 矩阵，定义整数增广矩阵

\[
B=[\,A\mid -L I_t\,],
\qquad
x=(s_1,\ldots,s_d,z_0,\ldots,z_r)^{\mathsf T}.
\tag{8}
\]

那么 (7) 等价于一个整数线性方程

\[
Bx=b.
\tag{9}
\]

因此，raw 频率 \(k\) 可提升为真实源角色，当且仅当 (9) 有整数解。

## 3. Smith 正规形的充要判据

取 \(B\) 的 Smith 正规形

\[
U B V
=
\operatorname{diag}(\delta_1,\ldots,\delta_\rho,0,\ldots,0),
\qquad
\delta_i>0,\quad
\delta_i\mid\delta_{i+1},
\tag{10}
\]

其中 \(U,V\) 为整系数可逆矩阵。令 \(b'=Ub\)，则有精确判据

\[
\boxed{
(9)\text{ 有解}
\iff
\delta_i\mid b'_i\ (1\le i\le\rho),
\quad
b'_i=0\ (\rho<i\le t).
}
\tag{11}
\]

若 (11) 成立，取

\[
y_i=b'_i/\delta_i\quad(1\le i\le\rho),
\qquad
y_i=0\quad(i>\rho),
\qquad
x=Vy,
\tag{12}
\]

则 \(x\) 的前 \(d\) 个分量给出角色参数 \(s_\nu\)，从而显式构造
\(\chi_s\)。按 \(m_\nu\) 约化这些分量不会改变 (7)。

若 (11) 失败，则有两种有限回执：

* 某个 \(i\le\rho\) 使 \(\delta_i\nmid b'_i\)。第 \(i\) 行是一个整除关系障碍；
* 某个 \(i>\rho\) 使 \(b'_i\ne0\)。第 \(i\) 行说明 \(b\) 不在 \(B\) 的整数像中。

将第 \(i\) 行乘以 \(U\) 的对应行，可得到一个明确的源单位—锚点关系线性组合；
左侧对所有角色变量都落在 \(\delta_i\mathbb Z\)（或恒为零），而右侧为
\(b'_i\)，故该行是可独立复核的
SOURCE_RELATION_FOURIER/LIFT_OBSTRUCTED 证书。

## 4. 与有限群角色和阶筛的对应

方程 (7) 直接展开为

\[
\sum_{\nu=1}^{d}\frac{s_\nu c_{j\nu}}{m_\nu}
-\frac{k\lambda_j}{e}\in\mathbb Z,
\tag{13}
\]

所以它同时包含所有源关系、源单位自身的阶关系和锚点的绝对相位关系。若取任意
整数关系向量 \(v=(v_0,\ldots,v_r)\) 使

\[
\sum_{j=0}^{r}v_j c_{j\nu}\equiv0\pmod{m_\nu}
\quad\text{对每个 }\nu,
\tag{14}
\]

则 (13) 必然推出

\[
k\sum_{j=0}^{r}v_j\lambda_j\equiv0\pmod e.
\tag{15}
\]

因此 SNF 失败行可回译为源关系格上的相位矛盾；反过来，所有关系向量满足 (15)
时，(9) 必有解。这是抽象仿射相容性判据在一般有限阿贝尔源商上的有限矩阵实现。

此外，任何可提升频率都满足

\[
\operatorname{ord}(\eta_k)
=\frac e{\gcd(e,k)}
\mid \operatorname{exp}(H)
=\operatorname{lcm}(m_1,\ldots,m_d).
\tag{16}
\]

指数阶筛是 (11) 的廉价必要条件；通过阶筛并不替代 SNF 的来源和锚点检查。

## 5. 两个校验

### 非循环源商中的成功提升

取

\[
H=C_2\oplus C_3,\qquad e=6,\qquad k=1,
\]

并取三行（锚点、两个源单位）

\[
(c_{0,1},c_{0,2})=(1,1),\quad \lambda_0=5,
\]
\[
(c_{1,1},c_{1,2})=(1,0),\quad \lambda_1=3,
\qquad
(c_{2,1},c_{2,2})=(0,1),\quad \lambda_2=2.
\]

角色参数 \(s=(1,1)\) 给出相位 \(5/6,1/2,1/3\)，恰分别等于
\(\eta_1(5),\eta_1(3),\eta_1(2)\)。因此 SNF 系统有解并构造真实源角色。

### 非循环源商中的失败提升

取 \(H=C_2\oplus C_2\)、\(e=4\)、\(k=1\)，只取源单位
\(u_1=(1,0)\) 及标签 \(\lambda_1=1\)。此行要求一个阶为 2 的源元素承载阶为 4
的相位。这里 \(L=4\)，该行的系数为 \(A=(2,0)\)，右端为 \(b_1=1\)；增广行的
系数最大公因子为 2，不整除右端 1，SNF 立即给出
LIFT_OBSTRUCTED。

### 阶筛通过但关系冲突

取 \(H=C_2=\langle g\rangle\)、\(e=2\)、\(k=1\)，并给同一个源单位
\(u_1=u_2=g\) 赋予两个标签
\(\lambda_1=0,\lambda_2=1\)。两个单行的相位阶都为 2，因而通过 (16)，但它们要求
\(\chi(g)=1\) 和 \(\chi(g)=-1\) 同时成立。此时 \(L=2\)，两行同为 \(A=1\)，
右端分别为 \(b_1=0,b_2=1\)；增广矩阵的差分零行在 \(Ub\) 上留下非零项，SNF
给出一个纯关系型的 LIFT_OBSTRUCTED。这个例子说明指数阶筛只是必要条件，不能
替代来源关系检查。

## 6. 接入 raw 空集分派

对 raw 残数 Fourier 选出的频率 \(k\)，先用 (16) 删除阶不可能的频率，再构造
(6)--(9)。若 SNF 通过，输出显式 \(\chi_s\) 及锚点相位，才允许将 raw Fourier
系数送入 F/G 的 q-height 或 Kneser 容量账本；若 SNF 失败，保留失败行的整除或零
关系回执，转向另一源商、另一条 Type I/II 射线或严格良基递降。参数 Fourier 的
Parseval 能量本身仍不能替代这个来源门。

## 研究边界

本引理解决任意已给定有限阿贝尔源商和 raw 标签的角色提升，但不构造标签映射，也
不证明 SNF 成功后的 Fourier 角色必产生统一有界 Type II 证书。剩余的决定性缺口是
建立 raw 除子残数到源商标签的有界构造，或证明所有 SNF 失败行都能回译成更小且
可提升的 Type I/II 实例。
