---
kind: claim
claim_id: type-i-empty-target-fiber-gf-source-dispatch
title: 固定 Type I 空目标纤维的规范 G/F/源差分三分
statement: 对固定合法 Type I 图表，若目标指数纤维为空，则先由目标是否属于源子群给出规范 G 支撑分离；若目标属于源子群，则规范 Fourier 缺口角色按其在盒像差分子群上的限制，唯一分成支撑湮灭的 F 对偶证书或至少一个独立 q 源差分请求。该请求只能进入已闭合的 Type-II source admission；空纤维本身不计作 q 容量或递降。p=73 的 R=27 给出真实 F 空纤维，p=241 的 R=3、7 给出 G 空纤维并由独立 Type-II 正规形救援。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-f-g-fourier-obstruction-certificate
  - type-I-target-fiber-primary-filtered-support-source-dichotomy
  - type-i-ii-source-universe-admission-expansion-relay
  - type-I-r3-r7-chart-fan-coverage-counterexample
topics:
  - type-I
  - F-state
  - G-state
  - empty-target-fiber
  - Fourier
  - source-difference
  - q-primary
  - Type-II
  - cross-chart
  - proof-program
sources:
  - claim: type-I-f-g-fourier-obstruction-certificate
    role: empty-fiber-Fourier-deficit
  - claim: type-I-target-fiber-primary-filtered-support-source-dichotomy
    role: support-annihilator-versus-q-demand
  - claim: type-i-ii-source-universe-admission-expansion-relay
    role: q-demand-to-Type-II-admission
  - reproduction: reproductions/type_i_empty_target_fiber_gf_source_dispatch.py
    role: p73-F-and-p241-G-controls
visibility: public
last_checked: '2026-08-09'
---

# 固定 Type I 空目标纤维的规范 G/F/源差分三分

## 设置

设 \(p\equiv1\pmod {24}\) 为核心素数，\(R\equiv3\pmod4\)，并令

\[
K=\frac{pR+1}{4}=\prod_{i=1}^{r}q_i^{\nu_i}.
\]

把 \(H=\langle q_1,\ldots,q_r\rangle\leq U(R)\) 写成乘法群，令

\[
\mathcal B=\prod_{i=1}^{r}[-\nu_i,\nu_i]\cap\mathbb Z^r,\qquad
\phi(z)=\prod_iq_i^{z_i},\qquad t=-1\pmod R.
\]

目标指数纤维和盒像分别是

\[
\mathcal Z_t=\{z\in\mathcal B:\phi(z)=t\},\qquad
S=\phi(\mathcal B).
\]

本卡只处理 \(\mathcal Z_t=\varnothing\)。令

\[
D_B=\langle ss'^{-1}:s,s'\in S\rangle\leq H
\]

为盒像差分子群，并记

\[
\widehat{\mathcal B}(\chi)=\sum_{z\in\mathcal B}\chi(\phi(z)),
\qquad V=|\mathcal B|.
\]

## 规范三分定理

### A. 目标在源子群外：G 支撑分离

若 \(t\notin H\)，有限阿贝尔对偶性给出角色

\[
\chi_G\in\widehat{U(R)},\qquad
\chi_G|_H=1,\qquad \chi_G(t)\neq1.
\]

按角色阶、CRT 坐标和相位向量的固定字典序选最小角色，输出

\[
\mathrm{G\_SUPPORT\_SEPARATION}.
\]

这是精确的不可达证书：所有盒点的相位都是 \(1\)，而目标相位不是 \(1\)。
它不产生 Type-II q 需求。即使同一个 \(p\) 存在另一张图表或 Type-II 短证书，
该证书也必须作为独立的跨图表 admission 边记录。

### B. 目标在源子群内：规范 Fourier 缺口

若 \(t\in H\) 且 \(\mathcal Z_t=\varnothing\)，对非平凡
\(\chi\in\widehat H\) 定义

\[
\sigma(\chi)=-\operatorname{Re}\!
\left(\overline{\chi(t)}\,\widehat{\mathcal B}(\chi)\right).
\]

由有限群正交性

\[
\sum_{\chi\ne1}\sigma(\chi)=V,
\]

故存在 \(\chi_*\ne1\) 满足

\[
\sigma(\chi_*)\geq\frac{V}{|H|-1}>0.
\tag{1}
\]

取最大 \(\sigma\)、再按角色阶和群坐标字典序的规范 \(\chi_*\)。

#### B1. 盒像差分被湮灭

若

\[
\chi_*|_{D_B}=1,
\]

则存在常数 \(c\) 使 \(\chi_*(s)=c\) 对所有 \(s\in S\) 成立。因而

\[
\widehat{\mathcal B}(\chi_*)=Vc,\qquad
-V\operatorname{Re}(\overline{\chi_*(t)}c)
\geq\frac{V}{|H|-1}>0.
\tag{2}
\]

目标与整个盒像位于不同的角色相位层，输出

\[
\mathrm{F\_SUPPORT\_ANNIHILATOR}
\]

及 \((\chi_*,D_B,c,t,\sigma(\chi_*))\) 载荷。这是 F 状态的有限对偶证书，
但不计 Type-II q 容量。

#### B2. 盒像差分含有 q 初等方向

若 \(\chi_*|_{D_B}\) 非平凡，取

\[
q_*=\min\{q:\ q\text{ 为 }|\chi_*(D_B)|\text{ 的素因子}\}.
\]

则 \(D_{B,q_*}/q_*D_{B,q_*}\neq0\)，从而

\[
r_{q_*}(B)=
\dim_{\mathbb F_{q_*}}\!
\left(D_{B,q_*}/q_*D_{B,q_*}\right)\geq1.
\tag{3}
\]

若 \(\mathcal L_B=\langle z-z':z,z'\in\mathcal B\rangle\)，则

\[
\frac{\mathcal L_B}
{\mathcal L_B\cap\ker\phi+q_*\mathcal L_B}
\cong
\frac{D_B}{q_*D_B},
\tag{4}
\]

所以 (3) 是真实源差分格至少一个独立 q 方向的需求，而不是把角色阶当作
整数 q-height。输出

\[
\mathrm{F\_SOURCE\_DIFFERENCE\_Q\_DEMAND}
(q_*,r_{q_*},\chi_*|_{D_B}).
\]

只有在 source contract、source-map、CRT/SNF、范围和 E1--E5 全部通过后，
该请求才可送入 Type-II source admission；否则分别保留
\(\mathrm{FOURIER\_ROLE\_NO\_ARITHMETIC\_LIFT}\)、
\(\mathrm{SOURCE\_UNIVERSE\_MENU\_ESCAPE}\) 或
\(\mathrm{SOURCE\_ADMISSION\_EXACTNESS\_UNPROVED}\)。

## 证明

若 \(t\notin H\)，\(tH\) 是 \(U(R)/H\) 的非单位陪集，有限阿贝尔群对偶分离
直接给出 A。

现设 \(t\in H\) 且 \(\mathcal Z_t=\varnothing\)。目标计数恒等式为

\[
0=\frac1{|H|}\sum_{\chi\in\widehat H}
\overline{\chi(t)}\,\widehat{\mathcal B}(\chi).
\]

平凡角色项为 \(V\)，故非平凡项的实部总和为 \(-V\)，即
\(\sum_{\chi\ne1}\sigma(\chi)=V\)，得到 (1)。

若 \(\chi_*\) 在 \(D_B\) 上恒等，对任意 \(s,s'\in S\) 有
\(\chi_*(s)\chi_*(s')^{-1}=1\)，所以支撑相位为常数 \(c\)，代入 (1) 得
(2)，并且 \(\chi_*(t)\neq c\)。这是 B1。

若 \(\chi_*\) 在 \(D_B\) 上非恒等，则其像是非平凡有限循环群。取
\(q_*\mid|\chi_*(D_B)|\)，\(D_B\) 的 q-primary 部分非平凡，有限 q 群的
Frattini 商给出 (3)。\(\phi\) 限制在 \(\mathcal L_B\) 上满射到 \(D_B\)，
第一同构定理及 \(\phi(q\mathcal L_B)=qD_B\) 给出 (4)。这证明 B2。

A、B1、B2 互斥且穷尽；空纤维没有第四种“容量已支付”解释。证毕。

## 具体控制与跨图表边界

### \(p=241\) 的两个 G 空图表

\[
R=3,\quad K=181,\quad H=\{1\},\qquad
R=7,\quad K=422=2\cdot211,\quad H=\{1,2,4\}.
\]

两个目标 \(-1\) 都不在 \(H\)，所以都输出 G 支撑分离；其盒像分别是
\(\{1\}\) 与 \(\{1,2,4\}\)，目标均不在对应源像中。不能把两个空纤维合并成一个
q 容量缺口。

同一个 \(p=241\) 另有独立 Type-II 正规形

\[
(A,C,K_{\mathrm{II}},B,h)=(1,1,2,69,7),
\]

满足

\[
h=4ACK_{\mathrm{II}}-1,\quad
h\mid p+4A^2C,\quad
h\mid K_{\mathrm{II}}p+A,\quad B>A.
\]

因此正确的跨路线记录是

\[
\mathrm{G\_SUPPORT\_SEPARATION}
\longrightarrow
\mathrm{TYPE\_II\_ADMISSION}(p=241,h=7),
\]

而不是“R=3/7 的空纤维已经构成递降”。

### \(p=73,\ R=27\) 的真实 F 空纤维

\[
K=493=17\cdot29,\qquad H=U(27),\qquad
\mathcal B=\{-1,0,1\}^2.
\]

以 \(2\) 为 \(U(27)\) 的生成元时，

\[
17\equiv2^{15},\qquad29\equiv2,
\]

盒像指数正好为 \(\{-4,-3,\ldots,4\}\pmod {18}\)，而
\(-1\equiv2^9\) 不在盒像中。于是 \(t\in H\) 但目标纤维为空，属于 B 分支。
盒像含有相邻元素，故 \(D_B=H\)，规范角色在 \(D_B\) 上非平凡；最小素因子
\(q_*=2\)，并且 \(r_2(B)=1\)。该实例输出一个真实的
\(\mathrm{F\_SOURCE\_DIFFERENCE\_Q\_DEMAND}(2,1)\)，而不是 G 分离。

## 选择器后果

对每个固定 Type-I 图表，空目标纤维现在有一个可执行的顺序：

\[
\text{目标在 }H\text{ 外}
\to\mathrm{G\_SUPPORT\_SEPARATION};
\]

\[
\text{目标在 }H\text{ 内}
\to
\begin{cases}
\mathrm{F\_SUPPORT\_ANNIHILATOR},\\
\mathrm{F\_SOURCE\_DIFFERENCE\_Q\_DEMAND}.
\end{cases}
\]

第一条不会制造 Type-II 容量，第二条也只制造一个有限源秩请求。只有 source
admission 完备并通过整数提升，才可得到短证书或严格可提升递降；否则保留精确
的 Fourier/算术障碍。该三分把“空图表扇区”接回统一选择器，但还没有证明所有
核心素数的某条图表一定通过 Type-II admission 或拥有严格后继。

## 聚焦复现

~~~bash
python3 reproductions/type_i_empty_target_fiber_gf_source_dispatch.py --verify
~~~
