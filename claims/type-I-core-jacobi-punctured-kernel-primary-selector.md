---
kind: claim
claim_id: type-I-core-jacobi-punctured-kernel-primary-selector
title: 核心 Jacobi 饱和陪集的删点容量、成对 Fourier 与主分派选择器
statement: >-
  设 p≡1 (mod 24)、4K=pR+1，并对 K 的全部素因子采用 N=1 的规范指数盒。
  若 -1 属于生成群 H，令 chi=(./R)、L=ker chi、d=|L|。Jacobi-negative
  记录经 s_z=-Phi(z) 平移为 L 上的反演对称多重集 m；精确 Type I 目标缺失
  等价于 m(1)=0。若同时没有同符号 H-像碰撞，则删去目标点后每盒至多占
  d-1 个像，并有 C<=Theta_ord-|A union S| 及偶性收紧，其中 A 是大小至少 d
  的盒、S 是 Jacobi special boxes。当 |H|>2 时，任意 F 状态还强制一个规范
  Jacobi 成对 Fourier 对比至少为 4C/(|H|-2)；|H|=2 时 F 不可能。高穿孔
  密度时所有非平凡核角色都有负对比。
  将 L=T times O 分成 2-Sylow 与奇 Hall 部分后，要么 O-单位纤维给出非零
  2^a 缩放核关系，并由精确非对称二进盒判定终端或盒外残差；要么 O 投影仍缺失
  目标，产生非恒奇阶全局 Fourier 角色及带条件掩码的奇素数阶源秩旗标。一般旗标
  尚无保持原记录来源的完整整数 owner/source-map；p=97 的 11 阶旗标已有反演对
  owner 圆柱横向秩映射、C_11 关联格 SNF 及来源保持的规范边 token，其精确源秩
  容量为 1，同纤维横向 lift 已被排除。一般非相邻边若有唯一 q^(j+1) deep
  endpoint 且目标继承该层，则已有 {1,q} arithmetic-ready block；只有来源边合格且
  source/target 两个全局 occurrence key 均未占用时才成为 verified physical
  source-class lift。固定 q=3 的三张模板覆盖全部充分大核心素数；任意奇 source
  prime 还有 residue-optimal matched menu；任意 rank-one named edge 还有精确的
  最小 q-height 对偶。已绑定层的旗标只能在原层准入或输出严格 obstruction；只有
  尚未绑定层的请求才能在 owner 窗口可容纳时选择 valuation-shifted carrier 构造
  新层的 source-line 仿射 provenance，否则给出严格窗口阻碍。但其范围/target-state 门、
  完整 kernel source box 与全局 E5 仍未证明。奇主阶记录若在某个完整 CRT
  素数幂分量上为 1，则现可直接进入图表无关标记与不可逆 CRT_DESCENT 的严格
  降 R 重图表；只有全分量非平凡的记录仍转交 odd-owner/source-map。多个独立角色的纯代数层容量已有
  障碍商短正合列和精确上尾 Hall 判据；真实物理边仍需范围、标签与 occurrence 门。
  纯二进盒外关系则可由半幂对合规范分裂 R，并在终端门失败时
  进入图表无关标记与不可逆 phase 支付的严格降 R 重图表；故只剩奇阶支仍未闭合。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-core-jacobi-ordered-capacity-strict-slack-terminal
  - type-I-fixed-layer-qprimary-representation-dual-capacity-selector
  - type-I-target-fiber-primary-filtered-support-source-dichotomy
  - type-I-generalized-dyadic-exact-relation-capacity
  - type-I-pure-dyadic-half-power-crt-rechart-descent
  - type-I-odd-primary-component-kernel-crt-rechart-descent
  - type-II-source-fiber-finite-abelian-composition-relay
  - type-I-odd-owner-nonadjacent-common-base-next-layer-lift
  - type-I-odd-owner-prime-matched-affine-carrier-fourier-descent-boundary
  - type-I-source-lattice-qheight-dual-valuation-shift-carrier
  - type-I-source-lattice-filtered-dual-tail-hall-capacity
topics:
  - type-I
  - core-prime
  - Jacobi-character
  - punctured-capacity
  - finite-fourier
  - q-primary
  - source-rank
  - generalized-dyadic
  - selector
  - proof-program
sources:
  - claim: type-I-core-jacobi-ordered-capacity-strict-slack-terminal
    role: core-Jacobi-sign-box-input
  - claim: type-I-target-fiber-primary-filtered-support-source-dichotomy
    role: source-difference-rank-semantics
  - claim: type-I-generalized-dyadic-exact-relation-capacity
    role: exact-dyadic-box-admission
  - claim: type-I-pure-dyadic-half-power-crt-rechart-descent
    role: outside-box-half-power-terminal-or-strict-rechart
  - claim: type-I-odd-owner-nonadjacent-common-base-next-layer-lift
    role: nonadjacent-exclusive-next-q-layer-physical-source-class-lift
  - claim: type-I-odd-owner-prime-matched-affine-carrier-fourier-descent-boundary
    role: prime-matched-affine-admission-and-kernel-fourier-boundary
  - claim: type-I-source-lattice-qheight-dual-valuation-shift-carrier
    role: minimal-qheight-dual-and-nonambient-rank-one-carrier
  - claim: type-I-source-lattice-filtered-dual-tail-hall-capacity
    role: multi-role-obstruction-filtration-and-tail-capacity
  - reproduction: reproductions/type_i_core_jacobi_punctured_kernel_primary_selector.py
    role: focused-capacity-Fourier-Sylow-and-boundary-controls
visibility: public
last_checked: '2026-08-10'
---

# 核心 Jacobi 饱和陪集的删点容量、成对 Fourier 与主分派选择器

## 1. 核心压缩

设

\[
p\equiv1\pmod {24},\qquad 4K=pR+1,\qquad
K=\prod_{i=1}^r q_i^{\nu_i},\qquad \nu_i\ge1,
\tag{1}
\]

并令

\[
H=\langle q_1,\ldots,q_r\rangle\le U(R),\qquad -1\in H,
\qquad \chi(h)=\left(\frac hR\right).
\tag{2}
\]

核心同余给出 \(R\equiv3\pmod4\)，故 \(\chi(-1)=-1\)。因此

\[
L=\ker(\chi|_H),\qquad d=|L|=|H|/2,
\qquad H=L\times\langle-1\rangle.
\tag{3}
\]

在对称指数盒

\[
B_\nu=\prod_i[-\nu_i,\nu_i]\cap\mathbb Z^r,
\qquad \Phi(z)=\prod_iq_i^{z_i}\pmod R
\tag{4}
\]

中定义 Jacobi-negative 记录和规范平移

\[
S^-:=\{z\in B_\nu:\chi(\Phi(z))=-1\},
\qquad s_z:=-\Phi(z)\in L,
\tag{5}
\]

\[
m(x):=\#\{z\in S^-:s_z=x\},\qquad
C:=\sum_{x\in L}m(x).
\tag{6}
\]

令 \(I=\{i:\chi(q_i)=-1\}\)。已有核心奇偶约束说明 \(I\ne\varnothing\)，并且

\[
V:=|B_\nu|=\prod_i(2\nu_i+1),
\qquad
A_0:=\prod_{i\notin I}(2\nu_i+1),
\qquad
\boxed{C=\frac{V-A_0}{2}>0.}
\tag{7}
\]

精确目标 \(\Phi(z)=-1\) 等价于 \(s_z=1\)。所以规范 \(N=1\) 图表的 F 状态
恰好满足

\[
\boxed{m(1)=0.}
\tag{8}
\]

取反 \(z\mapsto-z\) 保持 \(S^-\)，并把 \(s_z\) 送到 \(s_z^{-1}\)，故

\[
\boxed{m(x)=m(x^{-1}).}
\tag{9}
\]

零向量不在 \(S^-\)，所以取反没有固定指数记录。特别地，\(C\) 为正偶数；若
\(x=x^{-1}\)，则 \(m(x)\) 也为偶数。

## 2. 删去目标点后的严格有序容量

沿用核心 Jacobi 有序容量中的符号盒 \(B_\sigma\)、大小 \(b_\sigma\)、字符和
\(D_\sigma\) 与 filtered 计数

\[
c_\sigma=\#(S^-\cap B_\sigma)
=\frac{b_\sigma-D_\sigma}{2}.
\tag{10}
\]

令

\[
\Theta_{\rm ord}=\sum_\sigma\min(b_\sigma,d),
\qquad
\mathcal A=\{\sigma:b_\sigma\ge d\},
\qquad
\mathcal S=\{\sigma:D_\sigma>0\}.
\tag{11}
\]

其中 \(\mathcal S\) 正是已有的 special boxes，且
\(|\mathcal S|=2^{r-|I|}\)。假设既没有精确目标命中，也没有同一符号盒内的
两个不同指数点具有相同 \(H\)-像。此时

\[
\Phi:S^-\cap B_\sigma\hookrightarrow(-L)\setminus\{-1\},
\tag{12}
\]

而右侧只有 \(d-1\) 个元素。因此

\[
\boxed{c_\sigma\le\min(b_\sigma,d-1),}
\qquad
\boxed{C\le\Theta_{\rm punct}:=
\sum_\sigma\min(b_\sigma,d-1)\le(d-1)2^r.}
\tag{13}
\]

式 (13) 对每个大盒 \(\sigma\in\mathcal A\) 相对 \(\Theta_{\rm ord}\) 至少节省一格。
另一方面，已有 Jacobi special-box 正字符和对每个
\(\sigma\in\mathcal S\) 至少节省一格。同一个盒的两种理由不能重复收费，故准确合并为

\[
\boxed{
C\le\Theta_{\rm ord}-|\mathcal A\cup\mathcal S|.}
\tag{14}
\]

再用 \(C\) 的偶性，得到本节最强的整数门

\[
\boxed{
C\le2\left\lfloor
\frac{\Theta_{\rm ord}-|\mathcal A\cup\mathcal S|}{2}
\right\rfloor.}
\tag{15}
\]

因此 (13)--(15) 任一违反都强制以下至少一项：

1. \(\Phi(z)=-1\)，从 \(z,-z\) 中定向后得到 \(e<K\)、
   \(e\mid K^2\)、\(e\equiv-K\pmod R\) 的直接 Type I 除子；
2. 同符号 \(H\)-像碰撞，差向量落在原指数预算内，并产生已有的短关系偶前驱。

逐盒还可写成

\[
\boxed{b_\sigma-D_\sigma\le |H|-2,}
\qquad
b_\sigma\le\min\{|H|,|H|-2+D_\sigma\}.
\tag{16}
\]

这里的碰撞终端只构造较小偶数；除非第二层 marked fiber 非空或另有 E1--E5，不能把它
误写成已经可提升的递降。

## 3. Jacobi 核上的规范成对 Fourier

定义规范收缩同态

\[
\rho:H\longrightarrow L,
\qquad
\rho(h)=
\begin{cases}
h,&\chi(h)=1,\\
-h,&\chi(h)=-1.
\end{cases}
\tag{17}
\]

其核为 \(\langle-1\rangle\)。对 \(\eta\in\widehat L\)，令

\[
\psi_\eta:=\eta\circ\rho.
\tag{18}
\]

这是 \(\eta\) 到 \(H\) 的唯一满足 \(\psi_\eta(-1)=1\) 的延拓；另一个延拓为
\(\chi\psi_\eta\)。定义原盒 Fourier 和

\[
F(\psi)=\sum_{z\in B_\nu}\psi(\Phi(z))
\tag{19}
\]

以及核多重集的未归一化 Fourier 变换

\[
\widehat m(\eta)=\sum_{x\in L}m(x)\eta(x).
\tag{20}
\]

由 negative 指示函数 \((1-\chi)/2\) 直接得到

\[
\boxed{
\widehat m(\eta)
=\frac12\bigl(F(\psi_\eta)-F(\chi\psi_\eta)\bigr).}
\tag{21}
\]

式 (9) 说明所有 \(\widehat m(\eta)\) 都为实数；对称盒也使 (21) 右侧两个原盒
Fourier 和分别为实数。角色正交性给出

\[
\sum_{\eta\in\widehat L}\widehat m(\eta)=d\,m(1).
\tag{22}
\]

在 F 状态中，平凡项为 \(C\)，其余项之和为 \(-C\)。若 \(d>1\)，存在
\(\eta\ne1\) 满足

\[
\boxed{
\widehat m(\eta)\le-\frac C{d-1},}
\tag{23}
\]

为得到确定性证书，固定由有序素因子坐标诱导的 SNF 角色编码，并在所有非平凡角色中
依次按 \(\widehat m(\eta)\) 最小、角色阶最小、相位分子字典序最小选择
\(\eta_*\)。平均值证明说明 \(\eta_*\) 必满足 (23)；下文的 \(\eta\) 可统一取
\(\eta_*\)。这里的“规范”与任意有限阿贝尔群的抽象自同构无关，而是相对于已冻结的
图表坐标和 SNF 编码。

等价地

\[
\boxed{
F(\chi\psi_\eta)-F(\psi_\eta)
\ge\frac{2C}{d-1}
=\frac{4C}{|H|-2}.}
\tag{24}
\]

两角色均不属于 \(\{1,\chi\}\)。至少一个角色还满足

\[
|F(\theta)|\ge\frac C{d-1}=\frac{2C}{|H|-2}.
\tag{25}
\]

因此普通近角色预算可在该角色上收紧为

\[
\sum_i\min\{1,\nu_i^2\|\theta_i\|^2\}
\le60\log\frac{V(|H|-2)}{2C}.
\tag{26}
\]

它严格优于普通 \(60\log(|H|-1)\) 的充要比较条件是

\[
\boxed{V>(|H|-1)A_0.}
\tag{27}
\]

Parseval 还给出精确的成对对比能量

\[
\sum_{\eta\ne1}
\bigl(F(\psi_\eta)-F(\chi\psi_\eta)\bigr)^2
=4d\sum_{x\in L}m(x)^2-4C^2.
\tag{28}
\]

若 \(|H|=2\)，则 \(L=\{1\}\)。由 \(C>0\) 得 \(m(1)>0\)，所以 F 状态不可能，
已经存在精确 Type I 命中。

## 4. 高穿孔密度使全部核角色同时为负

若每个非目标残基的重数满足 \(m(x)\le M\)，令

\[
E_{\rm def}:=M(d-1)-C.
\tag{29}
\]

对任意 \(\eta\ne1\)，利用 \(\sum_{x\ne1}\eta(x)=-1\) 有

\[
\widehat m(\eta)
=-M-\sum_{x\ne1}(M-m(x))\eta(x),
\tag{30}
\]

故

\[
\boxed{|\widehat m(\eta)+M|\le E_{\rm def}.}
\tag{31}
\]

特别地，若

\[
\boxed{C>M(d-2),}
\tag{32}
\]

则每个非平凡 \(L\)-角色都满足

\[
\widehat m(\eta)\le-\bigl(C-M(d-2)\bigr)<0.
\tag{33}
\]

没有同符号碰撞时，同一归一化残基在每个符号盒至多出现一次，所以可取
\(M=2^r\)。于是

\[
C>2^r(d-2)
\Longrightarrow
\text{每个非平凡 q-primary 核角色都有负 Jacobi 成对对比}.
\tag{34}
\]

这是真正的全 q-primary 分支；若 (34) 不成立，则低密度区进一步收紧为
\(C\le2^r(d-2)\)。若 \(L\) 本身是 q-group，(23) 选出的角色无需 (34) 也已经
是 q-primary。

## 5. Sylow--Hall 主分派

把 Jacobi 核规范分解为

\[
L=T\times O,
\qquad T=L_{(2)},\qquad O=L_{\rm odd}.
\tag{35}
\]

令

\[
C_T:=\sum_{t\in T}m(t,1_O).
\tag{36}
\]

### 5.1 纯二进纤维：精确缩放关系与二进盒准入

若 \(C_T>0\)，选择一条记录 \(z\) 使

\[
s_z=(t,1_O),\qquad t\in T\setminus\{1\}.
\tag{37}
\]

写 \(\operatorname{ord}(t)=2^a\)，其中 \(a\ge1\)。因为
\(\Phi(z)=-s_z\)，有

\[
\boxed{\lambda=2^a z\ne0,
\qquad\Phi(\lambda)=1.}
\tag{38}
\]

为避免与 (17) 的群收缩同态混淆，记有理高度为

\[
\mathfrak h(\lambda):=\prod_iq_i^{\lambda_i}.
\]

由不同素数的唯一分解，\(\mathfrak h(\lambda)\ne1\)。取唯一方向
\(\varepsilon\in\{\pm1\}\) 使 \(\mathfrak h(\varepsilon\lambda)<1\)。式 (38) 进入已有
广义二进终端的充要盒条件是

\[
|\varepsilon2^az_q|\le\nu_q\quad(q\ne2),
\qquad
-\nu_2-1\le\varepsilon2^az_2\le\nu_2.
\tag{39}
\]

若 \(2\nmid K\)，这里按广义二进关系盒的约定补入零二进坐标
\(z_2=\nu_2=\lambda_2=0\)。

若二进坐标也满足对称界，它只是已有短关系；唯一新增的广义二进外层是
\(\varepsilon2^az_2=-\nu_2-1\)。若 (39) 失败，规范回执必须是

```text
SCALED_RELATION_OUTSIDE_DYADIC_BOX
```

并保存逐坐标 overflow。该标签只说明**原图表**的关系盒准入失败，不能在这里直接
称为终端。后续半幂定理取

\[
\omega=\Phi(2^{a-1}z)
\]

并以 \(\gcd(R,\omega\mp1)\) 把 \(R\) 分成互素真因子。唯一
\(3\pmod4\) 因子 \(R_*<R\) 给出新中心 \(K_*=(pR_*+1)/4\)：半幂进入新目标盒
或关系盒时返回相应终端回执，\(R_*\mid p+4\) 时直接 Type II；否则在
\(W=\operatorname{Sol}(4,p)\) 与不可逆 CRT_DESCENT phase 中返回完整 E1--E5 的
严格 \(R\to R_*\) 重图表边。若调用方使用图表依赖 marking 或允许 phase 回退，
该后继仍只能是 candidate transition。

### 5.2 奇 Hall 目标缺失：全局非恒角色

若 \(C_T=0\)，定义投影多重集

\[
m_O(o)=\sum_{t\in T}m(t,o).
\tag{40}
\]

则 \(m_O(1)=0\)、总质量仍为 \(C\)，且 \(m_O(o)=m_O(o^{-1})\)。所以 \(O\ne1\)，
并存在非平凡奇阶角色 \(\eta\in\widehat O\) 满足

\[
\boxed{\widehat m_O(\eta)\le-\frac C{|O|-1}.}
\tag{41}
\]

该角色不可能在实际记录上恒相位：若相位常为 \(u\)，反演对称给出 \(u=u^{-1}\)；
奇阶根单位中只有 \(u=1\)，这会使 Fourier 系数等于 \(C>0\)，与 (41) 矛盾。
定义实际记录的奇部源差分群

\[
\Delta:=\left\langle
o_zo_w^{-1}:z,w\in S^-
\right\rangle\le O,
\qquad s_z=(t_z,o_z)\in T\times O.
\]

于是 \(\eta|_\Delta\) 非平凡；取其像阶的任一素因子并投影到相应 primary 分量，
得到某个奇素数 \(\ell\) 满足

\[
\boxed{\dim_{\mathbb F_\ell}(\Delta/\ell\Delta)\ge1.}
\tag{42}
\]

这一步无需整数 source-map：\(\Delta\) 直接由原指数记录之差产生。但 \(\ell\) 仍只是
有限残余群的素因子，(42) 尚未把它映射到一个物理 \(\ell\)-owner 或整数高度。

### 5.3 带 SNF 标记的素层 Fourier 旗标

为了把 (42) 规范化到一个素数阶相位，固定 \(O\) 的有序群表示和确定性的 SNF
素指数链

\[
O=O_0\supsetneq O_1\supsetneq\cdots\supsetneq O_s=\{1\},
\qquad [O_j:O_{j+1}]=\ell_j.
\tag{43}
\]

令

\[
M_j=\sum_{o\in O_j}m_O(o),
\tag{44}
\]

并取首个 \(M_{j+1}=0<M_j\) 的层。商
\(Q_j=O_j/O_{j+1}\simeq C_{\ell_j}\) 上的条件直方图 \(a(u)\) 满足

\[
a(0)=0,\qquad \sum_ua(u)=M_j,\qquad a(u)=a(-u).
\tag{45}
\]

因此存在阶恰为奇素数 \(\ell_j\) 的局部角色 \(\kappa\)，使

\[
\boxed{\widehat a(\kappa)\le-\frac{M_j}{\ell_j-1}.}
\tag{46}
\]

任取支撑相位 \(u\ne0\)，反演给出 \(-u\) 也在支撑中；因 \(\ell_j\) 为奇数，
\(u\ne-u\)，且差分相位 \(2u\ne0\)。所以 (46) 不是纯锚点，源差分像满射
\(C_{\ell_j}\)。

必须保留两个边界。首先，“规范”是相对于固定 SNF 标记而言；抽象群本身可能没有
自同构不变的合成链。其次，(46) 是带 \(O_j\) 条件掩码的局部 Fourier 系数。局部
角色虽可延拓为 \(O\) 上的 \(\ell_j\)-primary 角色，但全局阶可能升高，且 (46) 不能
删去条件掩码后冒充原始 \(F(\psi)\) 的单项。

## 6. q-primary 投影不可直接继承负号

基本成对负系数不保证其某个 q-primary 分量仍为负。取加法群

\[
H=C_6\times C_2,\qquad -1=(0,1),\qquad
q_1=(2,1),\quad q_2=(3,1),\quad \nu_1=\nu_2=1.
\tag{47}
\]

令 \(\chi(x,\epsilon)=(-1)^\epsilon\)。Jacobi-negative 盒压缩到
\(L=C_6\) 后有

\[
m(2)=m(4)=1,\qquad m(3)=2,\qquad m(0)=0.
\tag{48}

对 \(\eta_k(x)=e^{2\pi ikx/6}\)，精确系数为

\[
(\widehat m(\eta_1),\ldots,\widehat m(\eta_5))
=(-3,1,0,1,-3).
\tag{49}

所以全部负系数都具有复合阶 6；阶 2 与阶 3 的 q-primary 系数分别为零和正数。
这严格排除“先取 (23) 的角色，再任取一个 primary 分量并保留负号”的错误步骤。
正确出口是 (34) 的高密度全角色门，或 (43)--(46) 的条件素层旗标。

同一模型的纯二进记录给出 \(\lambda=(0,\pm2)\)，超出第二坐标预算 \(1\)，也说明
式 (38) 不能跳过 (39)。

## 7. 三个核心控制

### 7.1 \(p=97\)：低密度区仍有全局 11 阶证书

取

\[
(p,R,K)=(97,67,5^3\cdot13).
\tag{50}
\]

模 67 的原根 2 给出 \(L=\langle4\rangle\simeq C_{33}\)。十条 negative 记录的
规范坐标各出现一次：

\[
\{6,7,8,9,11,22,24,25,26,27\}\subset C_{33}.
\tag{51}
\]

阶 11 角色 \(\eta(k)=e^{2\pi ik/11}\) 满足

\[
\widehat m(\eta)
=1-2\cos\frac{2\pi}{11}
< -\frac5{16}
=-\frac C{d-1}.
\tag{52}
\]

最后一个严格不等式可由
\(2\pi/11<\pi/5\) 和
\(\cos(\pi/5)=(1+\sqrt5)/4>21/32\) 直接验证。故旧有序容量未触发的
\(p=97\) 状态已经从“弱 Jacobi 商饱和”推进为显式全局 11 阶核 Fourier 证书。
角色阶本身仍不等于物理 11-owner；但后续的 owner 圆柱横向数字引理已经为其中一对
反演记录构造了两个真实 11-prefix owner，见下段。该新增映射仍不能据此宣称 Type II
或递降。

若选 SNF 链 \(C_{33}\supset3C_{33}\supset0\)，条件质量为
\((10,4,0)\)，末层 \(C_{11}\) 的相位支撑为 \(\{2,3,8,9\}\)，给出同一状态的
局部 11 阶源秩旗标。

更具体地，全局角色在反演记录 \(z_+=(1,0)\)、\(z_-=(-1,0)\) 上的相位为
\(2,9\pmod {11}\)。两条记录的有理单项式为 \(5,1/5\)，共同无向整数
\(\sigma=5+1=6\)。由于

\[
97+4\cdot6=11^2,
\qquad
97+4\cdot17=3\cdot5\cdot11,
\]

标准范围内的两个 11-owner \(6,17\) 在第一层 owner 圆柱内的横向数字为 \(0,1\)，
并满足

\[
\tau_1(s_z)=8\gamma(z)+6\pmod {11}.
\]

所以该反演对真实保存一个 \(\mathbb F_{11}\) 差分方向。另一方面，这两个 owner 分属
\(U(24)\) 与 \(U(68)\)，二者都没有 11-primary 单位群方向，也都没有当前路线内的
Type II 命中或严格 source-switch。固定 \((D,A)\) 纤维又必然固定 owner 标签
\(s=AD\)，所以同纤维横向秩一般恒为零；正确载体是 \(D=6,17\) 两个参数顶点的
增广关联格，商为 \(C_{11}\)。故准确回执是跨纤维
OWNER_CYLINDER_TRANSVERSE_RANK_ONE 加 FIBER_INCIDENCE_SNF，而不是单纤维
source-map。

该二点映射的来源门现在也可关闭。把带名记录
\((z_+,z_-)\)、有理反演对 \((5/1,1/5)\) 及整数规则
\[
\mathcal L_{\rm inv}(z_+,z_-)=(6,17)
\]
登记为一个有向边 token；其余因子为 \(N_6=11,N_{17}=15\)。以共同仿射斜率
\(a=8\) 归一化后，
\[
\frac{\Theta_1(e_6-e_{17})}{8(2-9)}
=\frac{11-15}{4\cdot8(2-9)}
=1\pmod {11}.
\]
因此该 token 的来源签名和整数余因子 realization 同时固定，一个 q-rank 请求的
incidence-token 流、关联槽流及 Rado rank 都等于 1；若复制为两个独立请求，则严格
得到 rank \(1<2\)。这只把此前的 partial-pair provenance 升级为
source-preserving additive rank-one 资源，不提供
\(h\equiv-1\pmod {4D}\) 的因子积；结合 \(|U(24)|=8\)、\(|U(68)|=32\) 和
\(|U(408)|=128\)，从 \(C_{11}\) 到当前 endpoint 乘法 source 环境的直接 lift
严格为零。相邻边固定基定理又证明 \(6,17\) 互素，故共同算术行基只能为 1；唯一
除子格目标 \(x=1\) 与所需残数 \(6\pmod {11}\) 不符，当前 fixed-base physical
lift 在 E2 严格阻塞。该 no-go 仍不排除异质源基、非相邻边或换状态的外部物理 token。
详见
[奇阶 Fourier 源差分到 owner 圆柱横向数字的秩容量映射](type-I-odd-fourier-owner-cylinder-transverse-rank-map.md)
、[奇阶 owner 横向数字的跨纤维关联格源映射与同纤维 no-go](type-I-odd-owner-fiber-incidence-lattice-source-map.md)
、[奇阶 owner 关联边的来源保持规范化与精确一维秩容量](type-I-odd-owner-incidence-edge-source-preserving-capacity.md)
与[奇阶相邻 owner 边的共同固定基塌缩、终端与源秩障碍](type-I-odd-owner-adjacent-edge-fixed-base-physical-lift-dichotomy.md)。

### 7.2 \(p=73,R=63\)：盒外残差经半幂 CRT 命中 Type II

取

\[
(p,R,K)=(73,63,1150),\qquad K=2\cdot5^2\cdot23.
\tag{53}
\]

这里 \(|H|=36\)、\(|L|=18\)、\(C=18\)，精确目标为空且没有同符号碰撞。
记录

\[
z=(0,1,-1),\qquad s_z=8\pmod {63},\qquad\operatorname{ord}(s_z)=2
\tag{54}
\]

落在纯二进纤维。式 (38) 给出

\[
\lambda=(0,2,-2),\qquad \Phi(\lambda)=1,
\qquad \mathfrak h(\lambda)=(5/23)^2<1.
\tag{55}
\]

它只在 \(23\) 坐标超出原预算一层，所以回执是
`SCALED_RELATION_OUTSIDE_DYADIC_BOX`，而不是原图表的广义二进终端。但半幂相位
就是 \(55\)，并给出

\[
(R_+,R_-)=(9,7),\qquad
(R_*,K_*)=(7,128).
\]

旧关系的 \(5,23\) 支撑不能进入 \(K_*\)，可是 \(R_*=7\mid73+4\)。因此
\(D=1\) Type II 门直接给出

\[
\boxed{
\frac4{73}
=\frac1{20}+\frac1{219}+\frac1{4380}.}
\tag{55a}
\]

所以这个原本的真实 admission 边界现已被 terminal-first 闭合；它不再是纯二进支的
未决控制。

### 7.3 \(p=433\)：删点门的无条件终端侧

取

\[
(p,R,K)=(433,15,1624),\qquad |H|=8,\qquad d=4.
\tag{56}
\]

此时 \(C=28>\Theta_{\rm punct}=24\)，所以 (13) 的逆否必须触发。该状态同时有
精确目标命中和同符号碰撞：\(z=(0,0,-1)\) 给出 Type I 除子 \(e=56\)，而

\[
(0,0,1),\ (1,1,0)
\tag{57}
\]

具有相同的模 15 像，产生 \((E,n)=(3136,224)\)。因此它验证的是无条件的
“hit 或 collision”分派，不是 F 内的纯碰撞例。

## 8. 选择器增量与未闭合边界

本引理严格细化了既有
`Q_PRIMARY_QUOTIENT_SATURATED`：对核心 \(X=\{1,\chi\}\)，饱和的 negative
陪集不再停在一个弱商关系，而是先删去精确目标，再进入 \(L\) 内部的容量与 Fourier
选择器。规范输出顺序为

```text
EXACT_TYPE_I_HIT
  or SAME_SIGN_KERNEL_TERMINAL
  or PUNCTURED_JACOBI_CAPACITY
       -> PURE_2_PRIMARY_SCALED_RELATION
            -> DYADIC_TERMINAL
            -> SCALED_RELATION_OUTSIDE_DYADIC_BOX
                 -> HALF_POWER_CRT_TERMINAL
                 -> STRICT_CRT_RECHART
       -> ODD_HALL_FOURIER_SOURCE_RANK
            -> ODD_PRIMARY_COMPONENT_KERNEL_CRT_RECHART
            -> FULL_COMPONENT_P_PLUS_ONE_TERMINAL
            -> ODD_PRIMARY_FULL_COMPONENT_RESIDUAL
                -> MASKED_PRIME_LAYER_FLAG
```

这里真正新增的是：核心 Jacobi 饱和陪集内部的目标删点、规范角色对、全角色高密度门，
以及反演对称自动排除奇素数纯锚点。有限阿贝尔合成列本身不是新的群论机制。

owner 圆柱横向数字已经给出正确的嵌套相位中心，参数纤维关联格也给出
规范 \(C_q\) source-SNF，并严格排除了同纤维横向 lift。对 \(p=97\) 的反演 pair，
来源保持边、规范源列和一个请求的 incidence flow--Rado 门已经闭合；一般 phase
lift 的带名整数来源边现有更一般的仿射 content 判据。对已经来源合格的非相邻边，若恰有唯一 endpoint 进入
\(q^{j+1}\) 且目标继承该层，则独占下一层已构成真实 \(\{1,q\}\) physical
source-class arithmetic-ready block；在可自由选择 cyclic q-primary 角色时，存在
不杀掉实际 q 类的角色恰当且仅当 \(q\mid\operatorname{ord}_{4D_*}(q)\)，而既定
\(J\)/anchor/labels 仍需联合 SNF/\(\eta\)。固定 \(q=3\) 的三张模板覆盖全部
\(p>2600\) 核心素数；进一步对任意奇 source prime 已有 residue-optimal matched
menu；rank-one 带名记录对的 source-lattice 角色还有一个由 Smith 正规形计算的
最小实现深度。对已经登记 \(J\) 的 MASKED_PRIME_LAYER_FLAG，只能在同一 \(J\)
判定：\(J<d_q\) 时输出严格对偶阻碍，\(J\ge d_q\) 时也必须在原层通过全部物理门。
只有尚未绑定层的 rank-one 请求才能另选
\(J\ge\max(1,d_q)\) 使用 valuation-shifted carrier；若该层超过 owner 窗口则有
全窗口严格 no-go。该 carrier 在精确范围门通过时只关闭一个新层 named source line
的代数 provenance；没有 layer-relay/retyping 时不能回填旧旗标。单个
carrier 的秩仍为 1。对多个独立角色，令
\(O_J=(F_J+qL)/qL\)；障碍短正合列精确计算角色子空间 \(W\) 在各层的可实现秩。
已绑定层的角色子空间只能用 \(W\cap V_{J_{\rm req}}\) 在原层判定，不能借过滤移层。
对尚未绑定层的请求，若角色合同允许换基，则所有上尾商维数不超过对应上尾容量，
恰当且仅当存在过滤适配基分派；不可换名角色则由各自最小深度的上尾 Hall 计数判定。
这个预筛给出严格的
代数容量缺口，但通过后仍必须为每条边验证 range/label/occurrence/source-switch 并运行
物理 Hall/Rado。详见
[源格障碍过滤的短正合列与上尾 Hall 容量](type-I-source-lattice-filtered-dual-tail-hall-capacity.md)。而单个
\(\{1,q\}\) 块的稳定子平凡，严格降模只能先输出显式
kernel Fourier；该输出在预设标签下仍可能阻塞，且尚未给出完整核来源盒、跨状态
target closure 或全局 E5。该关联格另有尺度二分：
\(p>4q^{j+1}\) 时 owner 数字全覆盖；
\(p<4q^{j+1}\) 时每个深 owner 的余因子缩为 \(k\in\{1,3,5,7\}\)，可先运行完整
Type II 小余因子菜单。纯二进缩放关系在 (39) 外时则已有规范
半幂 CRT 真因子、精确共享支撑界和严格重图表 adapter。故 odd-Hall 分支仍保持

```text
selector_status = analysis_evidence
recursive_edge_eligible = false
```

奇主阶记录现在也先按完整素数幂分量检查：存在非平凡 component kernel 时，
由 \(R\to R_*<R\) 的严格 CRT 边退出；full-component 情形若
\(\ell\equiv3\pmod4\)、\(\ell\nmid R\) 且 \(\ell\mid K\)，则转入 \(p+1\)
短终端；仅 `ODD_PRIMARY_FULL_COMPONENT_RESIDUAL` 保留给 owner/source-map。
纯二进盒外分支在图表无关 marking 和不可逆 CRT_DESCENT phase 均登记后可使用

```text
selector_status = verified_edge
recursive_edge_eligible = true
```

若这两个适配条件缺失，它仍降回 candidate transition。详见
[纯二进盒外关系的半幂 CRT 分裂、终端准入与严格重图表递降](type-I-pure-dyadic-half-power-crt-rechart-descent.md)
、[非相邻 owner 的共同基平方菜单、余因子碰撞与下一层物理 q-toggle](type-I-odd-owner-nonadjacent-common-base-next-layer-lift.md)
、[奇素数 source 匹配的仿射载体、显式核 Fourier 与良基递降边界](type-I-odd-owner-prime-matched-affine-carrier-fourier-descent-boundary.md)
、[源格角色的最小 q 层对偶与 content 估值移位载体](type-I-source-lattice-qheight-dual-valuation-shift-carrier.md)
与[源格障碍过滤的短正合列与上尾 Hall 容量](type-I-source-lattice-filtered-dual-tail-hall-capacity.md)。

## 聚焦验证

~~~bash
python3 reproductions/type_i_core_jacobi_punctured_kernel_primary_selector.py --verify
~~~

该验证只重算三个核心控制、一个有限群反例、Fourier 恒等式和准入边界，不运行历史扫描。
