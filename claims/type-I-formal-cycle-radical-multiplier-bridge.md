---
kind: claim
claim_id: type-I-formal-cycle-radical-multiplier-bridge
title: 周期平方自由支撑的三目标乘子桥与首个直接反例
statement: 设 R>=3、gcd(K,R)=1、4K=1(mod R)，S 是 K 支撑的子集，B=prod_{q in S}q。若 S 的带符号平方自由立方命中 -1、-4B 或 -(4B)^(-1) 中任一目标，则 K 的完整中心指数盒必命中 -1；在核心状态 4K=pR+1 中，这进一步产生同状态 Type I 证书。原先更强的“R=7(mod8) 的每个通用周期都直接命中 -1”命题为假：首个模数反例是 R=30031 的五周期 (31,6000,1200,240,961)，其 25357 个立方残数不含 -1，但同时命中另外两个乘子目标。该周期因含素数 3 而与核心 K 支撑不相容；所以它否定直接 radical 猜想，但不否定核心周期必终端的更弱命题。
claim_status: established
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-I-core-formal-cycle-radical-cube-boundary
  - type-I-general-b-centered-square-spectrum
  - type-I-formal-cycle-representation-lattice-capacity
topics:
  - type-I
  - formal-target-pair
  - support-preserving-cycle
  - radical-cube
  - multiplier-bridge
  - centered-spectrum
  - counterexample-boundary
  - finite-verification
sources:
  - claim: type-I-core-formal-cycle-radical-cube-boundary
    role: direct-radical-conjecture-and-finite-prefix
  - claim: type-I-general-b-centered-square-spectrum
    role: centered-box-terminal
visibility: public
last_checked: '2026-07-31'
---

# 周期平方自由支撑的三目标乘子桥与首个直接反例

## 1. 三目标乘子桥

令

\[
(K,R)=1,
\qquad R\ge3,
\qquad 4K\equiv1\pmod R,
\tag{1}
\]

并取任意有限集合

\[
S\subseteq\operatorname{Supp}(K),
\qquad
B=\prod_{q\in S}q.
\tag{2}
\]

对每个符号向量 \(\varepsilon=(\varepsilon_q)_{q\in S}\in\{-1,0,1\}^S\)，分别记

\[
c_\varepsilon=\prod_{q\in S}q^{\varepsilon_q}\in\mathbb Q_{>0},
\qquad
\bar c_\varepsilon=\prod_{q\in S}q^{\varepsilon_q}\pmod R,
\qquad
\mathcal C_S=\{\bar c_\varepsilon:\varepsilon\in\{-1,0,1\}^S\}.
\tag{3}
\]

这里 \(c_\varepsilon\) 是正有理单项式，\(\bar c_\varepsilon\) 才是它在
\((\mathbb Z/R\mathbb Z)^\times\) 中的剩余类；后文构造整数除子时使用前者，判断目标命中时
使用后者。

则有充分条件

\[
\boxed{
\mathcal C_S\cap
\left\{-1,-4B,-(4B)^{-1}\right\}\neq\varnothing
\quad\Longrightarrow\quad
-1\in\mathcal C_R(K).}
\tag{4}
\]

这里所有逆元都在模 \(R\) 下取；(1)--(2) 保证它们存在。

## 2. 直接中心除子证明与两目标等价式

固定一个命中 (4) 中某个目标的符号向量 \(\varepsilon\)。三个目标各自给出一个显式中心
除子：

\[
D_\varepsilon=
\begin{cases}
Kc_\varepsilon,&\bar c_\varepsilon=-1,\\
B/c_\varepsilon,&\bar c_\varepsilon=-4B,\\
Bc_\varepsilon,&\bar c_\varepsilon=-(4B)^{-1}.
\end{cases}
\tag{5}
\]

第一行在 \(q\in S\) 的指数为 \(v_q(K)+\varepsilon_q\)，介于 0 与 \(2v_q(K)\)
之间；后两行的指数分别为 \(1-\varepsilon_q\) 与 \(1+\varepsilon_q\)，介于 0 与 2
之间。因此三种情形都满足

\[
D_\varepsilon\mid K^2.
\tag{6}
\]

由 \(4K\equiv1\pmod R\)，三行又统一给出

\[
D_\varepsilon\equiv-K\pmod R.
\tag{7}
\]

这直接证明 (4)：中心因子互补后可取 \(D<K\)，因而得到中心盒命中。进一步，若处于核心
状态

\[
p\equiv1\pmod{24},
\qquad R\ge3,
\qquad 4K=pR+1,
\tag{8}
\]

则可按中心谱定理恢复同状态 Type I 证书；仅有 (1) 时不能把一般中心命中直接称为
Erdős--Straus Type I 证书。注意 \(\mathcal C_S\) 对取逆封闭，而

\[
(-4B)^{-1}=-(4B)^{-1}.
\tag{9}
\]

所以后两个目标的**存在性完全等价**。更紧凑地，(4) 等价于下面的二目标平方除子条件：

\[
\boxed{
\exists D\mid B^2:
\quad
D\equiv-B\pmod R
\quad\text{或}\quad
4D\equiv-1\pmod R.}
\tag{10}

第一支就是 direct radical hit，第二支就是乘子桥。具体地，当
\(\bar c_\varepsilon=-1\) 时也可改取
\(D=Bc_\varepsilon\mid B^2\)，得到 \(D\equiv-B\)；反向从任意
\(D\mid B^2\) 取有理单项式 \(c_\varepsilon=D/B\)，其指数均在
\(\{-1,0,1\}\) 中。两条同余分别还原 (4) 的 \(-1\) 与
\(-(4B)^{-1}\) 目标。

## 3. 直接 radical 猜想的首个反例

取

\[
R=30031=59\cdot509.
\tag{11}
\]

通用一层图 \(U_R\) 有五周期

\[
\{31,30000\}
\to\{6000,24031\}
\to\{1200,28831\}
\to\{240,29791\}
\to\{961,29070\}
\to\{31,30000\},
\tag{12}
\]

所选坐标与边素数依次为

\[
(30000,5),\ (6000,5),\ (1200,5),\ (29791,31),\ (961,31).
\tag{13}
\]

每项都满足 \(q^2\) 整除所选坐标。周期坐标的素因子支撑是

\[
S=\{2,3,5,7,11,17,19,31,2621,3433\},
\tag{14}
\]

其平方自由积为

\[
B=208121535026790.
\tag{15}
\]

完整生成 (3) 得到 25357 个不同残数，但

\[
-1\notin\mathcal C_S.
\tag{16}
\]

因此先前提出的全称命题

\[
R\equiv7\pmod8
\Longrightarrow
U_R\text{ 的每个周期支撑直接命中 }-1
\tag{17}
\]

是假的。按 \(R\) 递增的完整前缀扫描表明，(11) 是 \(R\equiv7\pmod8\) 中第一个出现
这种 direct radical miss 的模数。

## 4. 同一反例由乘子桥修复

在模 \(R\) 下有

\[
B\equiv5420,
\qquad
4B\equiv21680,
\qquad
(4B)^{-1}\equiv2395.
\tag{18}
\]

两组显式平方自由见证为

\[
\frac{155}{4493797}
=\frac{5\cdot31}{7\cdot11\cdot17\cdot3433}
\equiv8351=-4B\pmod R,
\tag{19}
\]

以及其倒数

\[
\frac{4493797}{155}
\equiv27636=-(4B)^{-1}\pmod R.
\tag{20}
\]

所以 (4) 的另外两个目标同时命中。只要某个 \(K\) 满足 (1) 且包含 (14) 的全部支撑，
式 (6) 的后两行给出同一个中心除子

\[
D=\frac{B\cdot4493797}{155}
=6033909224121185946
\mid B^2,
\qquad
4D\equiv-1\pmod {30031}.
\tag{21}
\]

但该通用周期不能成为核心状态的真实 \(K\) 支撑周期。因为

\[
R\equiv1\pmod3,
\qquad p\equiv1\pmod3
\tag{22}
\]

推出

\[
K=\frac{pR+1}{4}\equiv2\pmod3,
\tag{23}
\]

而 (14) 含素数 3。故 (16) 只否定放大图上的 direct radical 猜想，不给出实际核心
\(K\) 支撑周期的反例。

## 5. \(R<100000\) 的完整三目标扫描

新的高性能复现程序对全部

\[
7\le R<100000,
\qquad R\equiv7\pmod8
\tag{24}
\]

共 12500 个模数构造 \(U_R\)。它先求强连通分量，再使用两层安全剪枝：若单节点支撑
已经 direct 命中 \(-1\)，任何包含该节点的周期支撑超集也命中；在简单路径 DFS 中，若
当前累计支撑已命中，任何后续扩张同样命中。对剩余诱导 SCC，按周期最小节点锚定枚举
全部仍可能 miss 的简单周期。因此剪枝不会删除 direct miss 或 multiplier miss。

精确结果为

\[
\begin{array}{c|r}
\text{含周期的模数}&511\\
\text{循环 SCC}&807\\
\text{循环节点}&9809\\
\text{direct radical miss 周期}&1\\
\text{multiplier bridge miss 周期}&0.
\end{array}
\tag{25}
\]

唯一 direct miss 正是 (11)--(16)，所以它也是该完整前缀中的首个反例。式 (25) 是有限
验证，不是 (4) 或下面开放命题的全称证明。复现入口和锁定结果分别为
`reproductions/type_i_core_formal_cycle_multiplier_scan.cpp` 与
`reproductions/type-i-core-formal-cycle-multiplier-scan-results.json`。

## 6. 新的正确研究对象

原三目标中的 \(-1\) 是旧 radical-cube 判据，另外两个互逆目标直接构造
\(D\mid B^2\) 且 \(4D\equiv-1\pmod R\)。所以比继续扩大 direct \(-1\) 扫描更贴近
中心盒本身的开放命题是

\[
\boxed{
R\equiv7\pmod8,
\quad\mathcal Z\text{ 是 }U_R\text{ 的有向简单周期},
\quad B=\prod_{q\in S(\mathcal Z)}q
\Longrightarrow
\exists D\mid B^2:
D\equiv-B\ \text{或}\ 4D\equiv-1\pmod R.}
\tag{26}
\]

等价地，可以把 \(\lambda=4B\pmod R\) 看作一个虚拟生成元，并问

\[
-1\in
\left\{\bar c\lambda^e:\bar c\in\mathcal C_S, e\in\{-1,0,1\}\right\}.
\tag{27}
\]

这个虚拟坐标只用于表述乘子桥，不代表 \(4B\) 是新的素因子或可复用容量。

在本次 \(R<100000\) 的完整扫描中，没有发现 \(R\equiv7\pmod8\) 的三目标反例；全域是否
存在反例仍未知，(26) 也尚无全称证明。旧的非核心 \(R=7219\) 周期对三个目标全部 miss，
所以 (26) 中的同余条件不能删除。对实际核心 \(K\) 支撑周期，还可以退到更一般的周期
表示格与 \(K\) 容量盒相交命题。
固定反例、两个乘子见证及核心不相容性由
`reproductions/type_i_formal_cycle_multiplier_boundary.py` 独立核验；它不把有限前缀证据
升级成全称证明。
