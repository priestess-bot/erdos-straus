---
kind: claim
claim_id: type-I-pure-dyadic-half-power-crt-rechart-descent
title: 纯二进盒外关系的半幂 CRT 分裂、终端准入与严格重图表递降
statement: >-
  设核心图表 4K=pR+1 的 Jacobi F 状态含纯二进记录 z，令
  s=-Phi(z) 的阶为 2^a。完整缩放 2^a z 若落在广义二进盒外，仍可取半幂
  omega=Phi(2^(a-1)z)：它是既非 1 也非 -1 的对合元，并把
  R 规范分解为互素真因子 R_+=gcd(R,omega-1) 与
  R_-=gcd(R,omega+1)。其中唯一 3 mod 4 因子 R_* 给出严格更小中心图表
  K_*=(pR_*+1)/4；写 c=R/R_*，则
  K=cK_*-(c-1)/4 且 gcd(K,K_*)=gcd(K_*,(c-1)/4)。
  半幂若能进入 K_* 的目标盒或二进关系盒，分别直接产生 Type I 或一个规范的
  广义二进算术终端回执；后者只有 marked 提升通过时才终止递归。
  R_*|p+4 时另有 D=1 Type II 终端。否则上述 gcd 恒等式给出精确来源支撑障碍。
  对图表无关标记集 Sol(4,p)，把目标 hit/F/G 独立重算并进入不可逆
  CRT_DESCENT 调度后，恒等解提升与 (phase,R) 良基势把 R->R_* 升级为完整
  E1--E5 重图表边。该边关闭纯二进盒外残差的结构分派，但不证明下降后的 F/G
  状态必终端。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-core-jacobi-punctured-kernel-primary-selector
  - type-I-generalized-dyadic-exact-relation-capacity
  - type-I-short-relation-even-terminal
  - type-i-target-odd-d1-menu-typeii-terminal
  - type-I-f-g-fourier-obstruction-certificate
  - type-I-canonical-complete-support-rechart-g-obstruction
  - denominator-escape-state-contract
topics:
  - type-I
  - pure-dyadic
  - scaled-relation
  - CRT
  - involution
  - support-switch
  - rechart
  - generalized-dyadic
  - well-founded-descent
  - E1-E5
  - proof-program
sources:
  - claim: type-I-core-jacobi-punctured-kernel-primary-selector
    role: pure-2-primary-scaled-relation-input
  - claim: type-I-generalized-dyadic-exact-relation-capacity
    role: target-relation-box-and-even-terminal
  - claim: type-I-canonical-complete-support-rechart-g-obstruction
    role: chart-independent-marking-and-irreversible-support-switch-precedent
  - reproduction: reproductions/type_i_pure_dyadic_half_power_crt_rechart_descent.py
    role: focused-split-support-terminal-and-rechart-controls
visibility: public
last_checked: '2026-08-09'
---

# 纯二进盒外关系的半幂 CRT 分裂、终端准入与严格重图表递降

## 1. 半幂对合给出规范 CRT 分裂

先给出不依赖 Jacobi 来源的算术形式。设

\[
p\equiv1\pmod {24},\qquad R\equiv3\pmod4,\qquad
4K=pR+1,
\tag{1}
\]

并令 \(u\in U(R)\) 的精确阶为 \(2^a\)，其中 \(a\ge1\)。假设

\[
\omega:=u^{2^{a-1}}\notin\{1,-1\}\pmod R.
\tag{2}
\]

定义

\[
R_+=\gcd(R,\omega-1),\qquad
R_-=\gcd(R,\omega+1).
\tag{3}
\]

因为 \(\omega^2\equiv1\pmod R\)，每个奇素数幂
\(\ell^e\Vert R\) 整除 \(\omega-1\) 或 \(\omega+1\)。两者之差为 2，
故一个奇素数幂不可能同时整除二者。因此

\[
\boxed{R_+R_-=R,\qquad (R_+,R_-)=1.}
\tag{4}
\]

式 (2) 又说明 \(R_+,R_->1\)，所以二者都是 \(R\) 的真因子。由于
\(R\equiv3\pmod4\)，互素奇因子 \(R_+,R_-\) 中恰有一个为
\(3\pmod4\)，另一个为 \(1\pmod4\)。记

\[
\boxed{
R_*=\text{\(R_+,R_-\) 中唯一的 \(3\pmod4\) 因子},
\qquad c=\frac R{R_*}.}
\tag{5}
\]

于是

\[
1<R_*<R,\qquad c>1,\qquad c\equiv1\pmod4.
\tag{6}
\]

若 \(R_*=R_+\)，则 \(\omega\equiv1\pmod {R_*}\) 且
\(\omega\equiv-1\pmod c\)；若 \(R_*=R_-\)，两个符号反过来。因而半幂不是
一个未定位的二阶角色，而是同时携带一个规范 kernel 端和一个规范 target 端。

## 2. 核心 Jacobi 纯二进记录自动满足非平凡假设

沿用核心 Jacobi 选择器的记号

\[
H=L\times\langle-1\rangle,\qquad
L=\ker\chi_R,\qquad -1\notin L.
\tag{7}
\]

取 F 状态中的 Jacobi-negative 记录 \(z\)，写

\[
\Phi(z)=-s_z,\qquad s_z\in L,\qquad
\operatorname{ord}(s_z)=2^a,\quad a\ge1.
\tag{8}
\]

F 状态的精确目标被删去，所以 \(s_z\ne1\)。令

\[
u=\Phi(z)=-s_z.
\tag{9}
\]

由于 \(-1\) 与 \(L\) 是直积方向，\(u\) 的精确阶同样为 \(2^a\)。若 \(a>1\)，

\[
u^{2^{a-1}}=s_z^{2^{a-1}}\in L
\]

是非平凡对合，故既不为 1，也不可能等于 \(L\) 外的 \(-1\)。若 \(a=1\)，
\(u=-1\) 将迫使 \(s_z=1\)，同样与目标删点矛盾。因此

\[
\boxed{
\omega=\Phi(2^{a-1}z)
\text{ 总满足式 (2)。}}
\tag{10}
\]

特别地，即使完整关系

\[
\lambda=2^az,\qquad \Phi(\lambda)=1
\tag{11}
\]

超出原广义二进关系盒，半幂 (10) 仍给出 (3)--(6) 的规范真因子分裂。这不是把
盒外向量伪装成原图表终端；它把失败转成一个不同的、更小中心图表候选。

## 3. 新中心图表与精确共享支撑界

由 \(R_*\equiv3\pmod4\)，定义

\[
K_*=\frac{pR_*+1}{4}\in\mathbb N.
\tag{12}
\]

将 \(R=cR_*\) 代入 (1)，得到

\[
\boxed{
K=cK_*-\frac{c-1}{4}.}
\tag{13}
\]

记

\[
d_c=\frac{c-1}{4}.
\tag{14}
\]

从 \(K=cK_*-d_c\) 立即得到

\[
\boxed{
\gcd(K,K_*)=\gcd(K_*,d_c).}
\tag{15}
\]

所以新旧中心支撑的交集并不由半幂相位自动保留；它完全受小整数 \(d_c\) 控制。
若半幂向量

\[
\mu=2^{a-1}z
\tag{16}
\]

能在新中心图表中由 \(K_*\) 的素数指数表示，则每个
\(\mu_q\ne0\) 的素数 \(q\) 同时整除 \(K\) 与 \(K_*\)，因而

\[
\boxed{
\operatorname{rad}\!\left(\prod_{\mu_q\ne0}q\right)
\mid\gcd(K_*,d_c).}
\tag{17}
\]

式 (17) 是中心目标盒和普通关系盒的必要支撑门。通过它仍不够；还必须逐素数检查
\(K_*\) 的指数预算。广义二进盒有且只有一个形式例外：当 \(2\nmid K_*\) 时允许
定向关系使用外层指数 \(\mu_2=-1\)。但若这是唯一非零坐标，则
\(\rho(\mu)=1/2\not\equiv1\pmod {R_*}\)，因为 \(R_*>1\)；所以一个实际
kernel-sign 半幂仍必须使用至少一个来自 \(\gcd(K,K_*)\) 的活跃素数。
因此当 \(\gcd(K_*,d_c)=1\) 时，任何非零半幂向量都不能命中新目标盒或新关系盒。
这给出可独立复核的

\[
\text{HALF\_POWER\_CRT\_SOURCE\_SUPPORT\_OBSTRUCTED}
\tag{18}
\]

而不是含混的 source-map 未找到。

## 4. 两个终端准入门

写

\[
\varepsilon_*=
\begin{cases}
+1,&R_*=R_+,\\
-1,&R_*=R_-.
\end{cases}
\qquad
\omega\equiv\varepsilon_*\pmod {R_*}.
\tag{19}
\]

### 4.1 半幂进入新指数盒

分解 \(K_*=\prod_qq^{\nu_q^*}\)，并把旧支撑外的坐标预算解释为零。

若 \(\varepsilon_*=-1\) 且

\[
|\mu_q|\le\nu_q^*\qquad(\text{全部 }q),
\tag{20}
\]

则 \(\mu\) 是新图表中心指数盒中的精确目标点。定向
\(\rho(\mu)=\prod q^{\mu_q}<1\) 后，

\[
e=K_*\rho(\mu)
\]

是整数，满足

\[
0<e<K_*,\qquad e\mid K_*^2,\qquad
e\equiv-K_*\pmod {R_*}.
\tag{21}
\]

所以 (20) 已是原素数 \(p\) 的直接中心 Type I 终端。

若 \(\varepsilon_*=+1\)，先取唯一方向使 \(\rho(\mu)<1\)。若该方向落在
\(K_*\) 的非对称二进关系盒

\[
-\nu_2^*-1\le\mu_2\le\nu_2^*,
\qquad
|\mu_q|\le\nu_q^*\quad(q\ne2),
\tag{22}
\]

则 \(\mu\) 是新图表的合法广义二进关系点。已有精确关系容量定理给出

\[
E=4K_*\rho(\mu),\qquad
n=\frac{4K_*-E}{R_*},
\qquad 0<n<p,\quad2\mid n,
\tag{23}
\]

并产生规范的广义二进偶前驱回执。这里 (20)--(22) 使用的是新中心 \(K_*\) 的预算，
不能沿用旧 \(K\) 的盒。按照现有广义二进合同，(23) 只完成 arithmetic terminal：
只有第二层 marked fiber 非空或其它 E4 适配器通过时，它才终止原 \(p\) 的递归；
若标记提升为空，选择器仍继续使用第 5 节的严格 CRT rechart，不能停在 (23)。

### 4.2 \(D=1\) Type II 短路

独立地，若

\[
\boxed{R_*\mid p+4,}
\tag{24}
\]

则 \(h=R_*\equiv-1\pmod4\) 是已有 \(D=1\) 菜单的真实因子。令

\[
x=\frac{p+R_*}{4},
\quad
y=\frac{p(x+1)}{R_*},
\quad
z=\frac{px(x+1)}{R_*},
\tag{25}
\]

便有

\[
\boxed{\frac4p=\frac1x+\frac1y+\frac1z.}
\tag{26}
\]

式 (24) 不是半幂 CRT 分裂的自动结论；下面的 \(p=73,R=95\) 控制严格否定这种
错误推广。

## 5. 盒准入失败后的完整 E1--E5 重图表边

当直接 Type I、Type II 和已经通过 marked 提升的广义二进终端都未命中时，
(5)、(12) 仍给出严格更小的合法中心图表；这包括 (22) 只产生未提升算术前驱的情形。
要把它用于递归，必须显式采用图表无关标记，而不能继承旧中心目标纤维。定义

\[
W_S=W_T=\operatorname{Sol}(4,p),
\tag{27}
\]

并令 target \(T\) 的中心 hit/F/G 类型、因子分解、目标纤维和对偶角色全部从
\((p,R_*,K_*)\) 独立重算。边适配器记为

\[
\text{core\_half\_power\_crt\_rechart\_v1}.
\tag{28}
\]

其 E1--E5 为：

| 门 | 证明数据 |
|---|---|
| E1 | 原图表恒等式、Jacobi-negative 记录 \(z\)、\(s_z\) 的精确 \(2^a\) 阶、盒外向量及半幂 |
| E2 | 式 (3)--(6)、(12) 确定唯一 \(R_*,K_*\)，并显式替换全部中心支撑 |
| E3 | 具名 verifier 从整数重算阶、CRT 因子、式 (13)--(15)、新因子分解及 hit/F/G 类型 |
| E4 | \(\Phi_{T\to S}(w)=w\) 是 (27) 上的恒等映射 |
| E5 | 下述不可逆 phase--\(R\) 势严格下降 |

为防止换支撑后无成本回到增大 \(R\) 的旧图表，预先定义

\[
\Pi_{\rm CRT}(X)=
\bigl(\epsilon_{\rm CRT}(X),R_X\bigr)
\in\{0,1\}\times\mathbb N,
\tag{29}
\]

其中进入本菜单前 \(\epsilon_{\rm CRT}=1\)，提交后为 0。第一次边把第一坐标
从 1 降到 0；已经处于 CRT_DESCENT 的状态再次调用本边时，由
\(R_*<R\) 降低第二坐标。提交后只允许：

1. 直接终端；
2. 另一条严格降低 \(R\) 的 CRT 因子边；
3. 由放在 (29) 之前的其它已证明全局秩支付的边。

禁止无成本返回 \(\epsilon_{\rm CRT}=1\)，也禁止在同一 phase 中调用增大 \(R\)
而没有更早秩付款的重图表。字典序 \(\{0,1\}\times\mathbb N\) 良基，所以
(29) 是预定义的全域 E5，而不是对有限图事后编号。

因此盒准入失败时的准确状态不是 analysis-only：

\[
\boxed{
\text{PURE\_2\_SCALED\_RELATION\_OUTSIDE\_BOX}
\Longrightarrow
\text{terminal 或严格可提升 CRT rechart}.}
\tag{30}
\]

式 (30) 的 recursive edge 资格只在 (27)--(29) 的封闭调度内成立。若调用方坚持
使用图表依赖中心标记集，或允许 CRT phase 返回旧 phase，则 E4 或 E5 失效，必须降回
candidate transition。

## 6. 四个聚焦控制

### 6.1 \(p=73,R=63\)：支撑失败但 \(D=1\) 终端

\[
(p,R,K)=(73,63,1150),\qquad
K=2\cdot5^2\cdot23.
\]

记录 \(z=(0,1,-1)\) 的相位为 \(55\)，阶为 2。半幂就是自身，且

\[
(R_+,R_-)=(9,7),\qquad
(R_*,c,K_*)=(7,9,128).
\]

新旧支撑交只有

\[
\gcd(1150,128)=2
=\gcd\left(128,\frac{9-1}{4}\right),
\]

所以 \(5/23\) 不能进入新目标盒。不过 \(7\mid73+4\)，式 (25) 给出

\[
\frac4{73}
=\frac1{20}+\frac1{219}+\frac1{4380}.
\tag{31}
\]

### 6.2 \(p=73,R=95\)：target-sign 的严格双失败

\[
(p,R,K)=(73,95,1734),\qquad
K=2\cdot3\cdot17^2.
\]

取 \(z=(1,0,-1)\)。其相位 \(56\) 为非平凡对合，

\[
(R_+,R_-)=(5,19),\qquad
(R_*,c,K_*)=(19,5,347).
\tag{32}
\]

这里

\[
\gcd(1734,347)=1,
\qquad 19\nmid77.
\tag{33}
\]

所以半幂虽在模 19 上等于 \(-1\)，既不能进入 \(K_*=347\) 的目标盒，也没有
\(D=1\) 短路。这严格否定“target-sign CRT 因子自动终端”。新图表的支撑由
\(347\equiv5\pmod {19}\) 生成奇阶子群，故独立重算为 G 状态；(30) 给出
\(R:95\to19\) 的严格重图表边。

### 6.3 \(p=97,R=55\)：kernel-sign 的严格支撑失败

\[
(p,R,K)=(97,55,1334),\qquad
K=2\cdot23\cdot29.
\]

取 \(z=(0,1,0)\)。原相位阶为 4，半幂相位为

\[
23^2\equiv34\pmod {55},
\qquad
(R_+,R_-)=(11,5).
\]

所以

\[
(R_*,c,K_*)=(11,5,267),
\qquad
\gcd(1334,267)=1.
\tag{34}
\]

半幂在模 11 上是 kernel 关系，却不能进入 \(K_*=3\cdot89\) 的关系盒；
\(11\nmid101\)，也无 \(D=1\) 短路。目标同样独立重算为 G，得到
\(R:55\to11\) 的严格边。这说明 kernel-sign 与 target-sign 两侧都必须保留
支撑门 (15)--(17)。

### 6.4 算术准入正控制

取

\[
(p,R,K)=(337,255,21484),\qquad u=2,
\quad\operatorname{ord}_{255}(2)=8.
\]

半幂为 \(2^4=16\)，并有

\[
(R_+,R_-)=(15,17),\qquad
(R_*,K_*)=(15,1264),\qquad1264=2^4\cdot79.
\]

所以半幂真实进入新关系盒，取方向 \(2^{-4}\) 后

\[
E=4\cdot1264/16=316,\qquad
n=(4\cdot1264-316)/15=316<337.
\tag{35}
\]

该控制只验证第 4.1 节的一般算术准入，不声称它来自核心 Jacobi-negative 分支。

## 7. 对统一选择器的增量与边界

纯二进分支现在可按以下顺序分派：

    PURE_2_PRIMARY_RECORD
      -> full scaled relation inside dyadic box: existing terminal
      -> full scaled relation outside dyadic box
           -> canonical half-power CRT split
                -> target-box admission: Type I
                -> relation-box admission: generalized dyadic receipt
                     -> marked lift: terminal
                     -> unlifted: continue to CRT rechart
                -> R_* divides p+4: D=1 Type II
                -> source support obstruction
                     -> irreversible strict CRT rechart

这完成了此前缺失的盒外关系回收：盒外不再只是一个逐坐标 overflow 标签，而是有
规范真因子、精确共享支撑界和可提升严格后继。它没有证明下降后的 G/F sink 必有
短证书，也没有处理 odd-Hall Fourier 旗标；后者仍需同纤维 source-map 或另一条
良基下降。因此本结果推进的是纯二进分支的递归接口，不是 Erdős--Straus 猜想的
全称闭合。

## 聚焦验证

    python3 reproductions/type_i_pure_dyadic_half_power_crt_rechart_descent.py --verify

该 verifier 只重算四个控制中的相位阶、CRT 因子、中心恒等式、共享支撑、终端和
目标 hit/F/G 类型，不运行历史扫描。
