---
kind: claim
claim_id: type-II-raw-cyclic-source-lift-matrix
title: Type II raw 参数频率的循环源商提升矩阵
statement: 设真实源关系商 H 为循环群，且已给出源单位与锚点在参数循环群 Z/eZ 中的标签。每个参数频率 k 是否能提升为 H 的真实角色，等价于一个一元线性同余系统；逐行可除性失败或广义 CRT 不相容时，给出有限的 LIFT_OBSTRUCTED 关系证书；相容时显式构造源角色并保留锚点相位。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-raw-divisor-residue-fourier-certificate
  - type-II-kernel-fourier-source-relation-compatibility
topics:
  - type-II
  - raw-ray
  - cyclic-source-quotient
  - Fourier
  - congruence
  - CRT
  - lift-compatibility
  - certificate
sources:
  - claim: type-II-raw-divisor-residue-fourier-certificate
    role: raw-parameter-frequency
  - claim: type-II-kernel-fourier-source-relation-compatibility
    role: affine-source-relation-gate
visibility: public
last_checked: '2026-08-05'
---

# Type II raw 参数频率的循环源商提升矩阵

## 1. 有限循环源商模型

令真实源关系商为循环群

\[
H=\langle g\rangle\simeq C_m,
\]

并选定一组实际源单位及一个目标锚点

\[
u_i=g^{c_i}\quad(1\le i\le r),
\qquad
\alpha=g^{c_0},
\qquad c_i,c_0\in\mathbb Z/m\mathbb Z.
\tag{1}
\]

设 raw 残数已经通过一个带来源的参数标记送入
\(\mathbb Z/e\mathbb Z\)，其中 \(e\ge1\)。记

\[
\lambda_i,\lambda_0\in\mathbb Z/e\mathbb Z
\tag{2}
\]

为 \(u_i\) 与 \(\alpha\) 的标签。对频率 \(k\in\mathbb Z/e\mathbb Z\)，参数角色为

\[
\eta_k(x)=\exp\!\left(\frac{2\pi i kx}{e}\right).
\tag{3}
\]

这里的标签并不自动构成群同态；它们只表示待检验的 raw 参数相位。是否存在真实
源角色，必须由下面的同余系统决定。若源商不是循环群，应先在 Smith 分解的一个
循环因子上应用本引理，不能把非循环群强行写成单个离散对数。

## 2. 一元提升矩阵

所有 \(H\) 的角色都可写成

\[
\chi_s(g)=\exp\!\left(\frac{2\pi i s}{m}\right),
\qquad s\in\mathbb Z/m\mathbb Z.
\tag{4}
\]

要求 \(\chi_s\) 在源单位和锚点上分别等于 raw 参数角色，即

\[
\chi_s(u_i)=\eta_k(\lambda_i),
\qquad
\chi_s(\alpha)=\eta_k(\lambda_0).
\tag{5}
\]

由 (1)--(4)，(5) 等价于对 \(j=0,1,\ldots,r\) 同时满足

\[
e c_j s-mk\lambda_j\equiv0\pmod{em},
\tag{6}
\]

其中 \((c_j,\lambda_j)=(c_0,\lambda_0)\) 当 \(j=0\)，否则采用源单位的对应
数据。称 (6) 为循环源提升矩阵；它只有一个未知量 \(s\)，但包含所有源关系和锚点
关系。

### 逐行约化

令

\[
g_j=\gcd(c_j,m),
\qquad n_j=\frac m{g_j}.
\tag{7}
\]

因为 \(\gcd(ec_j,em)=e g_j\)，第 \(j\) 行 (6) 有解当且仅当

\[
e g_j\mid m k\lambda_j.
\tag{8}
\]

满足 (8) 后，用 \(c_j/g_j\) 在 \(\mathbb Z/n_j\mathbb Z\) 中的逆元约化出

\[
s\equiv\rho_j
 :=\left(\frac{c_j}{g_j}\right)^{-1}
   \frac{m k\lambda_j}{e g_j}
 \pmod{n_j}.
\tag{9}
\]

这里 \(\gcd(c_j/g_j,n_j)=1\)，故逆元确实存在；若 \(n_j=1\)，该行没有额外
约束。

### 广义 CRT 判据

在所有非平凡行上得到 (9) 后，系统 (6) 有解当且仅当

\[
\rho_i\equiv\rho_j
\pmod{\gcd(n_i,n_j)}
\qquad\text{对所有 }i,j.
\tag{10}
\]

这是广义中国剩余定理。若 (10) 成立，CRT 给出唯一的 \(s\pmod N\)，其中

\[
N=\operatorname{lcm}(n_0,n_1,\ldots,n_r)\mid m;
\tag{11}
\]

取其在 \(\mathbb Z/m\mathbb Z\) 中的任一代表，便得到显式源角色
\(\chi_s\)。因此有精确二分：

\[
\boxed{
\text{raw 频率 }k\text{ 可提升到 }H
\iff
\text{(8) 对每行成立且 (10) 对每对行成立}.
}
\tag{12}
\]

逐行条件 (8) 失败时，行 \(j\) 本身就是一个不可整除的关系证书；若 (8) 全部
成立而 (10) 失败，任意不相容行对 \((i,j)\) 给出

\[
s\equiv\rho_i\pmod{n_i},
\qquad
s\equiv\rho_j\pmod{n_j},
\qquad
\rho_i\not\equiv\rho_j\pmod{\gcd(n_i,n_j)},
\tag{13}
\]

这是一份有限的 SOURCE_RELATION_FOURIER/LIFT_OBSTRUCTED 回执，而不是未定位的
“角色不存在”。

## 3. 与源关系格判据的等价

若 \(z\mapsto\phi(z)\) 是源指数映射，式 (6) 也可按关系向量直接读取。任意
整数关系 \(v=(v_0,\ldots,v_r)\) 满足

\[
\sum_j c_jv_j\equiv0\pmod m
\]

时，(5) 要求

\[
k\sum_j\lambda_jv_j\equiv0\pmod e.
\tag{14}
\]

因此 (8)/(10) 的失败必然产生一个源关系格向量，使 (14) 失败；反之，所有关系
向量都满足 (14) 时，一元 CRT 系统相容并给出 (4) 的源角色。该等价把抽象的
\(L_G\) 与仿射锚点关系压缩为一张可枚举的循环矩阵。特别地，锚点行 \(j=0\) 不能
省略；只检查相对源关系会遗漏式 (13) 中的绝对相位冲突。

如果 \(e\nmid m\)，则某些频率可能仍通过 (6) 以较小阶出现，但必满足

\[
\operatorname{ord}(\eta_k)=\frac e{\gcd(e,k)}\mid m.
\tag{15}
\]

式 (15) 是先前指数阶筛的循环特例；系统 (8)--(10) 比它严格，因为它还检查了
每个来源标签和锚点的关系。

## 4. 成功与失败的研究分派

将 raw 空集的 Fourier 频率 \(k\) 投影到一个循环源商后，按以下顺序处理：

1. 先按 (15) 删除阶不可能的频率；
2. 对剩余频率构造 (6)，逐行检查 (8)；
3. 用 (10) 做锚点—源关系的 CRT 检查；
4. 成功时输出显式 \(\chi_s\)，其 Fourier 系数可以进入真实 F/G 容量账本；
5. 失败时保留 (8) 或 (13) 的最小回执，转向另一源商、另一条 Type I/II 射线或
   严格良基递降。

这一步不会把参数 Fourier 能量本身当作乘法容量。只有在成功得到 \(\chi_s\) 后，
raw 残数系数才满足源关系格仿射相容性，才允许调用已有的 q-height/Kneser 证书。

## 5. 两个小型校验

### 可提升样例

取 \(m=6\)、\(e=3\)、\(k=1\)，并令

\[
(c_0,c_1,c_2)=(1,2,3),
\qquad
(\lambda_0,\lambda_1,\lambda_2)=(1,2,0).
\]

此时 \(s=2\) 满足每一行 (6)：
\(3\cdot1\cdot2-6\cdot1=0\)、
\(3\cdot2\cdot2-6\cdot2=0\)、以及
\(3\cdot3\cdot2-6\cdot0=18\)。所以
\(\chi_2(g)=\exp(2\pi i/3)\) 是真实的源提升角色。

### 不可提升样例

取 \(m=2\)、\(e=3\)、\(k=1\)，只取一条源行

\[
c_0=1,
\qquad
\lambda_0=1.
\]

式 (6) 变成 \(3s-2\equiv0\pmod6\)，但左侧模 3 为零而右侧模 3 为一，故
(8) 失败。这里参数角色的阶为 3，而源群指数为 2；逐行除性证书直接给出
LIFT_OBSTRUCTED。

## 6. 对 \(p=97\) raw 边界的含义

在 \(p=97,h=143\) 的 raw 空集例中，指定源群 \(H=U(24)\) 的指数为 2，而
\(\mathbb Z/143\mathbb Z\) 的所有非平凡频率阶为 11、13 或 143。它们先由
(15) 全部排除，因此无需伪造循环离散对数或把 CRT 频率写成单位群角色。

若以后从另一条源射线得到循环商 \(C_m\) 且 \(e\mid m\)，则本矩阵提供了下一步
的实际算法：对 raw 残数标签和目标锚点逐行建立 (6)，成功便得到可计入容量的角色，
失败便得到明确关系向量或 CRT 不相容对。这样，raw 空集分支不再停留在抽象的
LIFT_OBSTRUCTED，而有一个有限、可复核、可自动化的源提升接口。

## 研究边界

本引理只解决循环源商上的角色提升，不证明任意 raw 参数标签都存在带来源的标记，
也不证明相容角色必然造成 q-height 超载。非循环源商需要对 Smith 的每个循环因子
分别求解并检查因子间的锚点相容性；成功的角色仍需进入已有的 F/G 容量或递降证明。
