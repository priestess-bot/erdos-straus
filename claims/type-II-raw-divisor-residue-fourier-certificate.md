---
kind: claim
claim_id: type-II-raw-divisor-residue-fourier-certificate
title: Type II raw 空集的平方除子残数 Fourier 证书
statement: 设 L=(h+1)/4，且 h=-1 (mod 4D_0)、h 整除 p+4D_0a_0。raw Type II 三元组存在当且仅当目标残数 D_0a_0 (mod h) 命中一个由 A^2C、AC|L 和序条件确定的有限残数集。若未命中，则该有限集合与目标的锚定指示函数有一个显式非平凡 Fourier 频率，Parseval 给出幅度下界；频率通过源关系格仿射相容性后可升级为 F/G 对偶证书；若允许阶投影能量为零且 e>1，则必有一个严格较小的核参数 Fourier relay，再按相容容量或 lift-obstructed 三分处理。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-arithmetic-lift-raw-factor-fallback
  - type-II-kernel-fourier-source-relation-compatibility
  - type-II-kernel-fourier-energy-role-capacity-dispatch
topics:
  - type-II
  - raw-ray
  - divisor-residue
  - Fourier
  - source-relation
  - lift-compatibility
  - dual-certificate
  - proof-boundary
sources:
  - claim: type-II-arithmetic-lift-raw-factor-fallback
    role: raw-factorization-equivalence
  - claim: type-II-kernel-fourier-source-relation-compatibility
    role: source-character-lift-gate
  - claim: type-II-kernel-fourier-energy-role-capacity-dispatch
    role: kernel-compatible-energy-dispatch
visibility: public
last_checked: '2026-08-05'
---

# Type II raw 空集的平方除子残数 Fourier 证书

## 1. raw 候选的除子残数等价

设

\[
h>1,\qquad h\equiv-1\pmod{4D_0},\qquad
h\mid p+4D_0a_0,
\]

并令

\[
L=\frac{h+1}{4},\qquad t_0\equiv D_0a_0\pmod h.
\tag{1}
\]

把 \(d=AC\) 作为中间除子。对每个 \(d\mid L\) 和 \(A\mid d\)，令

\[
C=\frac dA,\qquad K=\frac Ld,\qquad s=A^2C=Ad.
\tag{2}
\]

定义满足 raw 序条件的有限残数集

\[
\mathcal S_{L,p}^{\rm ord}
=
\left\{
Ad\bmod h:
\ d\mid L,\ A\mid d,\
\frac Ld\bigl(p-4Ad\bigr)+2A\ge0
\right\}
\subseteq\mathbb Z/h\mathbb Z.
\tag{3}
\]

这里的最后一个不等式正好是

\[
A\le\frac{Kp+A}{h},
\tag{4}
\]

因为

\[
\frac{Kp+A}{h}-A
=\frac{K(p-4A^2C)+2A}{h}
=\frac{\frac Ld(p-4Ad)+2A}{h}.
\]

对 \(ACK=L\) 的任意三元组，有

\[
h\mid Kp+A
\iff
A\equiv4D_0Ka_0\pmod h
\iff
A^2C\equiv D_0a_0\pmod h.
\tag{5}
\]

最后一个等价式使用 \(4D_0KAC=4D_0L=D_0(h+1)\equiv D_0\pmod h\)。
因此得到精确命中判据

\[
\boxed{
\mathscr R_{\rm raw}(h;p)\ne\varnothing
\iff
t_0\in\mathcal S_{L,p}^{\rm ord}.
}
\tag{6}
\]

这把 raw 三元组枚举压缩成一个有限的平方除子残数命中问题。

## 2. 未命中的锚定 Fourier 证书

假设 \(t_0\notin\mathcal S_{L,p}^{\rm ord}\)。在循环加法群
\(G_h=\mathbb Z/h\mathbb Z\) 上令

\[
f=1_{\mathcal S_{L,p}^{\rm ord}}-\delta_{t_0},
\]

并用未归一化 Fourier 变换

\[
\widehat f(j)
=\sum_{x\in G_h}f(x)e^{-2\pi ijx/h},
\qquad 0\le j<h.
\tag{7}
\]

由于目标不在残数集，支持不相交，故

\[
\widehat f(0)=|\mathcal S_{L,p}^{\rm ord}|-1,
\qquad
\sum_{j=0}^{h-1}|\widehat f(j)|^2
=h\bigl(|\mathcal S_{L,p}^{\rm ord}|+1\bigr).
\]

从而非平凡频率的总能量为

\[
\boxed{
\sum_{j=1}^{h-1}|\widehat f(j)|^2
=
h\bigl(|\mathcal S_{L,p}^{\rm ord}|+1\bigr)
-\bigl(|\mathcal S_{L,p}^{\rm ord}|-1\bigr)^2.
}
\tag{8}
\]

对 \(0\le|\mathcal S_{L,p}^{\rm ord}|\le h-1\)，右端严格为正。因此存在
\(1\le j<h\) 使

\[
\boxed{
|\widehat f(j)|
\ge
\sqrt{
\frac{
h\bigl(|\mathcal S_{L,p}^{\rm ord}|+1\bigr)
-\bigl(|\mathcal S_{L,p}^{\rm ord}|-1\bigr)^2
}{h-1}
}.
}
\tag{9}
\]

该系数的具体形式是

\[
\widehat f(j)
=\sum_{s\in\mathcal S_{L,p}^{\rm ord}}
e^{-2\pi ijs/h}
-e^{-2\pi ijt_0/h},
\tag{10}
\]

所以它同时记录所有 raw 候选残数与目标残数的相位差。式 (9) 是
RAW_DIVISOR_FOURIER 的规范幅度下界；它不是把 raw 空集误写成 Type II 命中。

## 3. 向 F/G 源关系的提升门

频率 \(j\) 首先只是参数群 \(G_h\) 上的加法角色
\(\eta_j(x)=e^{-2\pi ijx/h}\)。要把 (10) 解释成真实 F/G 或单位群 Fourier
证书，还必须提供一个带来源的关系映射

\[
\varphi:\text{source relation quotient}\longrightarrow G_h
\]

使每个实际源指数的 \(A^2C\) 残数与 \(\varphi\) 的像一致，并且锚点
\(t_0\) 的关系恒等式得到保持。等价地，候选参数角色必须满足已有源关系格的
仿射相容性判据。若相容，则

\[
\chi=\eta_j\circ\varphi
\]

给出一个真实的 SOURCE_RELATION_FOURIER 负证书，可送入 F/G 的相位或容量接口；
若相容性失败，则该 \(j\) 必须输出 LIFT_OBSTRUCTED，不能计入乘法 Kneser 容量。

还有一个无需求解完整关系格的必要阶筛。若指定的源角色定义在有限群 \(H\) 上，记
\(E=\exp(H)\)，则任何 \(\chi\in\widehat H\) 的阶都整除 \(E\)。因此参数频率
\(\eta_j\) 要求

\[
\boxed{
\frac h{\gcd(h,j)}\mid E.
}
\tag{11}
\]

若 (11) 失败，该频率不可能通过任何到 \(H\) 的源关系提升，直接输出
LIFT_OBSTRUCTED；无需把它送入 q-height 容量。该阶筛只是必要条件，(11) 成立仍需
继续检查源关系格和锚点的仿射相容性。

这个阶筛可以一次性压缩为一个有限商。令

\[
e=\gcd(h,E),\qquad \pi_e:\mathbb Z/h\mathbb Z\to\mathbb Z/e\mathbb Z,
\]

并定义投影重数

\[
m(y)=\#\{s\in\mathcal S_{L,p}^{\rm ord}:\pi_e(s)=y\},
\qquad
g_e(y)=m(y)-\mathbf1_{y=\pi_e(t_0)}.
\tag{12}
\]

所有阶整除 \(E\) 的参数角色恰好是 \(\mathbb Z/e\mathbb Z\) 上角色的拉回。对
\(g_e\) 应用 Parseval，得到可提升阶部分的精确能量

\[
\boxed{
\sum_{\substack{\xi\in\widehat{\mathbb Z/e\mathbb Z}\\\xi\ne1}}
|\widehat{g_e}(\xi)|^2
=
e\sum_y|g_e(y)|^2-(|\mathcal S_{L,p}^{\rm ord}|-1)^2.
}
\tag{13}
\]

若右端为正，则存在一个阶整除 \(E\) 的非平凡参数频率；它仍需通过源关系格
相容性，成功后才可成为 F/G 证书。若右端为零，则 \(g_e\) 在
\(\mathbb Z/e\mathbb Z\) 上为常数，所有源群阶允许的非平凡角色都看不见这个
raw 空集；此时继续枚举同一源群角色不能产生新的对偶信息，必须转向另一条
Type I/II 射线或良基递降。

### 3a. 零投影能量的核 Fourier relay

设 \(e>1\) 且 (13) 右端为零。令
\[
y_0=\pi_e(t_0),\qquad
c=\frac{|\mathcal S_{L,p}^{\rm ord}|-1}{e}.
\tag{14}
\]
由 \(g_e\) 为常数，必有 \(c\in\mathbb Z_{\ge0}\) 且
\[
m(y)=c+\mathbf 1_{y=y_0}\quad(y\in\mathbb Z/e\mathbb Z).
\tag{15}
\]
因此 \(y_0\in\pi_e(\mathcal S_{L,p}^{\rm ord})\)。令
\[
K_e=\ker\pi_e
=\{0,e,2e,\ldots,h-e\}\le\mathbb Z/h\mathbb Z,
\qquad
\mathcal S^{\ker}_{t_0}
=\{k\in K_e:t_0+k\in\mathcal S_{L,p}^{\rm ord}\}.
\tag{16}
\]
则
\[
1\le n_{\ker}:=|\mathcal S^{\ker}_{t_0}|=c+1<|K_e|.
\tag{17}
\]
左端来自 (15)，右端来自 \(t_0\notin\mathcal S_{L,p}^{\rm ord}\)：若
\(\mathcal S^{\ker}_{t_0}=K_e\)，则 \(k=0\) 会给出 \(t_0\in\mathcal S\)。
特别地，零投影能量在 \(e=h\) 时不可能发生，因为此时 \(K_e=\{0\}\)。

对 \(K_e\) 的未归一化 Fourier 变换，有精确核能量
\[
\boxed{
\sum_{\substack{\psi\in\widehat K_e\\\psi\ne1}}
\left|\sum_{k\in\mathcal S^{\ker}_{t_0}}\overline{\psi(k)}\right|^2
=n_{\ker}\bigl(|K_e|-n_{\ker}\bigr)>0.
}
\tag{18}
\]
取幅度最大的最小频率 \(\psi_\ast\)，得到规范回执
\[
\mathrm{RAW\_PARAMETER\_KERNEL\_FOURIER}
=(h,e,t_0,K_e,\mathcal S^{\ker}_{t_0},\psi_\ast).
\tag{19}
\]
这是一个严格的加法参数 relay：环境规模从 \(h\) 降到
\(|K_e|=h/e<h\)。若 \(\psi_\ast\) 通过源关系格和标签 SNF，则升级为
\(\mathrm{SOURCE\_RELATION\_FOURIER}\)；若不能提升，则记录
\(\mathrm{KERNEL\_FOURIER\_LIFT\_OBSTRUCTED}\)，但不再把原始零能量分支误记为
“没有对偶信息”。

### 3b. 构造性小例子

在 \(G=\mathbb Z/12\mathbb Z\) 中取 \(e=4\)、\(\mathcal S=\{0\}\)、\(t_0=4\)。
投影到 \(\mathbb Z/4\mathbb Z\) 后 \(g_e\equiv0\)，所以允许阶部分的能量确为零；
但 \(K_e=\{0,4,8\}\)，且
\[
\mathcal S^{\ker}_{t_0}=\{8\},
\qquad
n_{\ker}(|K_e|-n_{\ker})=1\cdot(3-1)=2.
\]
因此“允许角色看不见”并不等于“目标没有结构”：结构被推到更小的核参数层。

### 3c. 核 relay 的相容角色—容量三分

令 \(\mathcal X_{\mathrm{comp}}\subseteq\widehat K_e\) 是通过
源关系格、锚点和标签 SNF 的核角色集合，并令
\[
F_{\ker}(\psi)
=\sum_{k\in\mathcal S^{\ker}_{t_0}}\overline{\psi(k)}.
\tag{20}
\]
则由 (18) 有精确分解
\[
n_{\ker}(|K_e|-n_{\ker})
=
\sum_{\substack{\psi\in\mathcal X_{\mathrm{comp}}\\\psi\ne1}}
|F_{\ker}(\psi)|^2
+
\sum_{\psi\notin\mathcal X_{\mathrm{comp}}}|F_{\ker}(\psi)|^2.
\tag{21}
\]
因此核 relay 的规范三分为：

1. 若第二项为正，取最小阶且幅度最大的不可提升角色，输出
   \(\mathrm{RAW\_PARAMETER\_KERNEL\_LIFT\_OBSTRUCTED}\)，并保存其非零系数；
2. 若第二项为零，第一项必为正，按最小相容角色阶进入
   \(\ell\)-初等 Rado/Hall、较高 \(2^j\) 或混合 primary 分支；独立源列匹配
   通过后才可进入 F/G/Kneser 容量；
3. 若相容角色给出真实容量缺口，输出
   \(\mathrm{RAW\_PARAMETER\_KERNEL\_CAPACITY\_DEFICIT}\)，并把该缺口交给
   Hall/annihilator 闭包；若容量已超过缺口，则得到 Type II 目标纤维命中。

这正是核 Fourier 能量分派定理在 raw 参数 relay 上的专门推论。它把
\(\mathrm{RAW\_PARAMETER\_KERNEL\_FOURIER}\) 从单纯的加法证书接入真实的
F/G 角色账本，同时保留不可提升能量，禁止把它伪计为容量。

因此 raw 空集的严格分派为：

1. \(t_0\in\mathcal S_{L,p}^{\rm ord}\)：直接 Type II；
2. \(t_0\notin\mathcal S_{L,p}^{\rm ord}\)，且某个锚定频率通过关系格提升：
   F/G 对偶证书；
3. 所有选定频率均不相容：RAW_DIVISOR_FOURIER/LIFT_OBSTRUCTED，转交其它
   Type I/II 射线或良基递降。

当选定源关系商是循环群时，第 2--3 步可化为有限的一元算术检查。把每个 raw
候选残数和锚点写成参数标签 \(\lambda_j\)，把对应源单位写成 \(g^{c_j}\)，对
频率 \(k\) 求解

\[
e c_j s-mk\lambda_j\equiv0\pmod{em}.
\]

逐行除性失败或广义 CRT 的不相容对给出有限的
LIFT_OBSTRUCTED/SOURCE_RELATION_FOURIER 回执；系统有解时则构造实际源角色
\(\chi_s\)。完整约化公式见
[Type II raw 参数频率的循环源商提升矩阵](../claims/type-II-raw-cyclic-source-lift-matrix.md)。
若源关系商不是循环群，则把同一检查写成
\(H=\bigoplus_\nu C_{m_\nu}\) 上的整数线性系统，并用 Smith 正规形给出整除失败
行或显式角色；不能把非循环商压成一个离散对数。完整的一般接口见
[Type II raw 参数频率的有限阿贝尔源商 SNF 提升](../claims/type-II-raw-finite-abelian-source-lift-snf.md)。
若参数来自多个两两互素的局部 CRT 块，则局部标签必须先经 CRT 幂等元合并；
把 \(a_i\bmod h_i\) 直接当成共同 \(\mathbb Z/h\mathbb Z\) 元素，在两个以上非平凡
块时只有零频率与代表选择无关。规范的局部相位和 \(p=97\) 的
\(h_1=11,h_2=13\) 边界见
[Type II CRT 局部标签到全局 Fourier 的幂等元桥](../claims/type-II-crt-local-label-idempotent-phase-bridge.md)。

## 4. \(p=97\) 的显式边界

取

\[
p=97,\qquad D_0=6,\qquad a_0=133,\qquad h=143,\qquad L=36.
\]

此时

\[
t_0\equiv6\cdot133\equiv83\pmod{143},
\]

而满足序条件的残数集为

\[
\mathcal S_{36,97}^{\rm ord}
=\{1,2,3,4,6,8,9,12,16,18,24\}.
\]

目标 \(83\) 不在其中，故 raw 集为空。式 (8) 的非平凡能量为

\[
143(11+1)-(11-1)^2=1616,
\]

所以至少有一个 \(j\in\{1,\ldots,142\}\) 满足

\[
|\widehat f(j)|\ge\sqrt{1616/142}.
\]

直接取 \(j=1\) 时系数幅度约为 \(11.478\)，但它只有在通过源关系格提升后才是
F/G 证书。若指定源群为 \(U(24)\)，其指数为 \(2\)，而所有非平凡频率的阶只能是
\(11,13\) 或 \(143\)，均不整除 2；所以这整个 raw Fourier 分支都严格
LIFT_OBSTRUCTED，而不是低模数 Type II 命中。

## 5. 研究边界

该引理现在把 raw 空集转成三层分派：直接残数命中、可提升的原始/核 Fourier，
或明确的源关系/算术障碍。零投影能量且 \(e>1\) 的分支已得到严格加法模数
下降 \(h\to h/e\)；仍没有证明该参数 relay 总能回译为原猜想的较小 Type I/II
实例，也没有证明所有不可提升的核角色必产生原整数下降。仅有加法残数 Fourier
仍不能替代这一步。
