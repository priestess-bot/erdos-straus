---
kind: claim
claim_id: type-I-fg-qprefix-block-bound-first-overflow-terminal
title: F 请求的 candidate-fiber q-prefix 绑定与首个越界短缺口分派
statement: >-
  typed Q-PREFIX 的前置对象是 CANDIDATE_FIBER_QBLOCK_BOUND，而不是已经包含目标
  残数命中、B'>A 和完整因子积的终局 FIBER_REALIZED。固定一个实际 F 请求、带名边、
  target/source labels、层 J 和深度 d 后，target/deep-source 的共同规范数据、估值差
  和逐幂整除先给出 candidate binding；实际 source edge、prescribed elementary
  role、整数 source map 及 fresh/replay occurrence 账本再把它升级为 typed prefix。
  这两个连续回执有一个有限联合充要门；通过后只产生一个 lineage
  {1,q,...,q^d}。p=557281,R=199 的真实 F 指数盒在显式 target-odd 正角色
  digest 下产生一个 q=3 请求；同一 p 上的 rows 19838,138866 与 target 182
  依次通过 candidate binding 与 typed admission，得到 full-C3 prefix {1,3,9}，但 N=558009
  的全部因子均不为 -1 mod 728，故终局 FIBER_REALIZED 仍失败。这给出门序不可倒置的
  严格反例。相反，p=73 的实际 q=3 边虽形成 candidate binding，全部 depth-2
  typed upgrades 都在共同 canonical source base 前失败，且 U(8) 无 3-primary
  物理方向。
  对任意 p=1 mod4、奇 M>=3 且 (p,M)=1，首个越过严格 owner 窗口的 M-prefix
  标签唯一对应 m=3 mod4、m=-2p mod M、0<m<4M；若 p 还是核心素数且 m<p，可把
  这个 m 送入完整 Bradford Type I/II 菜单。p=557281,M=27 在 m=79 处给出 d=16 的 Type II
  终端，而 p=73,M=27 在 m=43 处完整菜单为空。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fg-fourier-to-type-II-role-demand-bridge
  - type-I-f-target-involution-fourier-phase-collapse
  - type-I-fg-qprefix-request-depth-admission
  - type-I-source-lattice-qheight-exclusive-tail-kernel-relay
  - type-I-owner-profile-canonical-base-target-slot-capacity
  - type-I-raw-certified-q-layer-charge-key-nonreuse
  - type-II-source-fiber-shared-q-ledger
  - type-II-hall-matching-fiber-realization-gate
  - short-certificate-equivalence
  - two-denominator-lift-criterion
topics:
  - type-I
  - type-II
  - F-state
  - q-prefix
  - candidate-fiber
  - gate-order
  - owner-overflow
  - short-certificate
  - strict-obstruction
  - terminal
  - capacity-map
sources:
  - claim: type-I-raw-certified-q-layer-charge-key-nonreuse
    role: three-level-candidate-typed-terminal-admission-order
  - claim: type-I-f-target-involution-fourier-phase-collapse
    role: target-odd-Fourier-charge-threshold
  - claim: type-II-hall-matching-fiber-realization-gate
    role: terminal-full-product-fiber-realization-definition
  - claim: short-certificate-equivalence
    role: complete-Bradford-Type-I-II-gap-menu
  - claim: two-denominator-lift-criterion
    role: exact-two-denominator-preserving-one-coordinate-lift-gate
  - reproduction: reproductions/type_i_fg_qprefix_block_bound_first_overflow.py
    role: actual-F-role-block-bound-p73-no-go-and-overflow-controls
visibility: public
last_checked: '2026-08-10'
---

# F 请求的 candidate-fiber q-prefix 绑定与首个越界短缺口分派

## 1. 三层门序

终局 `FIBER_REALIZED(A)` 已经要求：选出的完整因子积 \(h_A\) 整除同一个
\(N_A=p+4s_A\)，满足

\[
h_A\equiv-1\pmod {4D_A},
\qquad B_A>A_A,
\tag{1}
\]

并保留整数来源。它是 Type II 命中或跨状态 Kneser surplus 的门，不能作为寻找
\(h_A\) 之前的 Q-PREFIX 前提。无环顺序必须是

~~~text
CANDIDATE_FIBER_QBLOCK_BOUND
  -> TYPED_QPREFIX_REALIZED
  -> full product / target residue / B'>A
  -> FIBER_REALIZED or a typed target-miss relay
~~~

第一层只说明一条带来源的 q 幂链被绑定到同一个候选 target numerator；第二层才把
它分配给独立 typed demand；最后一层才检查完整积是否命中目标。

## 2. candidate binding 与 typed prefix 的联合有限充要门

固定核心素数 \(p\)、奇素数 \(q\nmid p\)、层 \(J\ge1\)、深度 \(d\ge1\)、target
\(x\) 和 deep source \(s_0\)。约定 \(v_q(0)=\infty\)。第一层
`CANDIDATE_FIBER_QBLOCK_BOUND` 只要求：

1. \(0<4x,4s_0<p\)，且
   \(D_*=D(x)\mid D_0=D(s_0)\)、\(q\nmid4D_*\)；
2.
   \[
   \min\{v_q(p+4s_0),v_q(x-s_0),v_q(p+4x)\}\ge J+d,
   \tag{2}
   \]
   并在 target ledger 逐项验证
   \(q^r\mid p+4x\)（\(0\le r\le d\)）。

这两项只把带来源的候选块

\[
B_d=\{1,q,\ldots,q^d\}
\tag{3}
\]

绑定到同一个 target numerator；不需要 typed demand、shallow edge、角色、
occurrence assignment 或目标残数。

现在另固定一个已独立存在的 typed F request \(\mathfrak r\)。令其带名源边为
\(e=(z_0,z_1)\)，差向量 \(\delta=z_1-z_0\)，prescribed elementary role 为
\(c\in\mathbb F_q^\times\)，并固定 shallow source \(s_1\)。把上述 candidate
binding 升级为 `TYPED_QPREFIX_REALIZED`，还必须且只须：

3. \(0<4s_1<p\)、\(D(s_1)=D_0\)、\(v_q(p+4s_1)=J\)，且带 provenance 的整数
   仿射 source map \(\mathcal L\) 把 \(z_0,z_1\) 送到 \(s_0,s_1\)，通过
   joint-SNF/content 门，并在固定规范下满足
   \[
   \frac{s_1-s_0}{q^J}\equiv c\pmod q;
   \tag{4}
   \]
   若请求合同允许单位重标，则 (4) 同步使用其记录的 normalization unit；
4. prescribed \(\eta\)/SNF map 把 \(q\bmod4D_*\) 送到请求指定的非零
   elementary role；
5. 一个 `block_lineage_id` 把相对层 \(r=1,\ldots,d\) 单射映到同一 charge 的
   连续前缀；\((\mathsf S,s_0,q,J+r)\) 与
   \((\mathsf T,x,q,J+r)\) 均 fresh，或是同一 assignment 的完整 replay，shallow
   occurrence 也有容量。

因此，在固定 canonical-owner universe、一个 named request 和一个 lineage 中，
depth-\(d\) typed prefix 存在，当且仅当先有第 1--2 项的 candidate receipt，再有
第 3--5 项的 typed admission receipt。必要性由任一 typed receipt 投影到 canonical
profiles、估值、source map、角色和 owner ledger 得到；充分性由两层数据依次构造
(3) 并分配给 \(\mathfrak r\)。最终输出只有一个 request、一个 elementary role
direction 和一个 lineage；深度 \(d\) 不生成 \(d\) 个请求。

这里允许 \(x=s_0\)：此时 \(v_q(x-s_0)=\infty\)，是 identity self-binding。若 source
与 target 的 state id 不同，即使整数值相同，occurrence keys 仍不同；若 state id 和
值都相同，同一请求的同一 key 只收费一次。只有另一个 assignment 再占用同一 unit
key 才构成冲突。

上述充要门不含目标 \(-1\)、完整积、\(B'>A\) 或 `FIBER_REALIZED`。这些条件若提前
出现，就会用待构造的积来证明积的候选块存在，形成定义环。

## 3. 同一实际 F 状态上的 full-\(C_3\) 正控制

取

\[
p=557281,\qquad R=199,\qquad
K=\frac{pR+1}{4}=2\cdot5\cdot11^3\cdot2083.
\tag{5}
\]

\(3\) 是模 \(199\) 的本原根；在 \(C_{198}\) 的离散对数坐标中

\[
(\log_3 2,\log_3 5,\log_3 11,\log_3 2083)
=(106,138,189,165).
\tag{6}
\]

对称指数盒 \([-1,1]\times[-1,1]\times[-3,3]\times[-1,1]\) 有 \(189\) 个带重数
点和 \(129\) 个不同像，目标 \(-1\) 的坐标 \(99\) 不在像中。事实上若

\[
106a+138b+189c+165d\equiv99\pmod {198},
\tag{7}
\]

模 \(3\) 先迫使 \(a=0\)，模 \(9\) 再迫使 \(d=-b\)；除以 \(9\) 后得到
\(21c-3b\equiv11\pmod {22}\)，模 \(3\) 矛盾。另一方面
\(\gcd(198,106,138,189,165)=1\)，所以源像生成整个 \(C_{198}\)：这是实际 F 状态，
不是 G 支撑外分离。

固定 state-local digest `EXPLICIT_TARGET_ODD_INDEX_43`，选择 \(j=43\)。因为
\(\chi_{43}(-1)=-1\)，它是 target-odd；四个 Dirichlet 因子的对称 residue 为
\((4,-6,9,-33)\)。相应的 anti-target 值为

\[
-\Re\!\left(
 \overline{\chi_{43}(-1)}
 \sum_{z\in\mathcal B}\chi_{43}(\phi(z))
\right),
\tag{8}
\]

它精确分解为

\[
\left(1+2\cos\frac{4\pi}{99}\right)\!
\left(1+2\cos\frac{2\pi}{33}\right)\!
\frac{\sin(7\pi/22)}{\sin(\pi/22)}\!
\left(1+2\cos\frac{\pi}{3}\right)>0.
\tag{8a}
\]

前两角都小于 \(\pi/3\)，故前两因子各大于 \(2\)；又
\(0<\pi/22<7\pi/22<\pi/2\)，第三因子大于 \(1\)，末项等于 \(2\)。所以 (8a)
严格大于 \(8\)。这个盒在 identity 处恰有 \(c(1)=3\) 个表示，且普通 Fourier
阈值为 \(189/(198-1)<1\)，从而

\[
A(\chi_{43})>8>c(1)=3>\frac{189}{197}.
\tag{8b}
\]

因此它满足 target-odd certificate 的收费阈值，而不只是任意正角色；这里也不依赖
浮点最大值或 tie tolerance。这个显式 digest 必须随请求保存，只认证本控制中的一个
合法角色，不声称是仓库其它 Fourier 排序下的全局 canonical maximum。

\(j=43\) 的 3-primary 投影为 index \(154\)，阶为 \(9\)。四个素因子方向在
\(C_9\) 中的相位为

\[
(4,3,0,3).
\tag{9}
\]

因此 factor-\(2\) 带名边 \(0\to e_{(2)}\) 的完整相位为 \(4\bmod9\)，初等相位为
\(1\bmod3\)，产生一个 `SOURCE_RANK_DEMAND(3)`。

在同一个 \(p\) 上取

\[
(D_*,A_*,x)=(182,1,182),\qquad
D_0=19838,\qquad(s_0,s_1)=(19838,138866).
\tag{10}
\]

其中 \(D_*=2\cdot7\cdot13\)、\(D_0=D_*\cdot109\)，两个 source rows 的 canonical
base 都是 \(D_0\)，且

\[
\bigl(v_3(p+4x),v_3(p+4s_0),v_3(p+4s_1)\bigr)=(4,3,1),
\quad v_3(s_0-x)=3.
\tag{11}
\]

整数 source line

\[
\mathcal L(z)=19838+119028z_{(2)}
\tag{12}
\]

把实际 factor-\(2\) edge 送到 \(s_0,s_1\)，且
\((s_1-s_0)/3\equiv1\pmod3\)。以 \(\beta_1=2\) 定义

\[
\tau(s)=\frac{s-2}{3}\pmod9,
\tag{13}
\]

则 \((\tau(x),\tau(s_0),\tau(s_1))=(6,6,1)\)，精确对齐 target phase \(0\) 和
chosen edge phase \(4\) 的共同偏移 \(6\)。这个 order-\(9\) 检查只覆盖 target 与
chosen edge；其它素因子方向只在 elementary \(C_3\) 降阶后相容，不能申报
full-\(C_9\) ambient lift。

target modulus 和 numerator 为

\[
4D_*=728,\qquad N_x=p+4x=558009=3^4\cdot83^2.
\tag{14}
\]

故 \(\{1,3,9\}\) 逐项整除 \(N_x\)。又
\(\operatorname{ord}_{728}(3)=6\)，而

\[
\eta:U(728)\to C_3,\qquad
\eta(u)=(u\bmod13)^4
\tag{15}
\]

把 \((1,3,9)\) 送到 \((1,3,9)\)。取一个 fresh lineage 和相对层 \(1,2\)，第 2 节
全部门通过，得到

\[
\boxed{\texttt{ACTUAL\_F\_REQUEST\_CANDIDATE\_FIBER\_DEPTH2\_BLOCK\_BOUND}}
\tag{16}
\]

以及一个 typed full-\(C_3\) prefix。

但 \(N_x\) 的十五个因子 \(3^a83^b\)（\(0\le a\le4,0\le b\le2\)）模 \(728\) 的
残数是

\[
\{1,3,9,19,27,57,81,83,121,171,249,283,337,361,363\},
\tag{17}
\]

不含 \(727=-1\)。所以此 target fiber 的终局 `FIBER_REALIZED` 为假。对
\(w=-1\)，(15) 的核大小为 \(96\)，截面

\[
S_w=\{k\in\ker\eta:wk\in\{1,3,9\}\}=\{727\}
\tag{18}
\]

具有 Fourier 能量 \(1(96-1)=95\)。式 (16)--(18) 是“typed prefix 在先、target
miss relay 在后”的严格门序反例。

## 4. \(p=73\) 的实际 F 局部 no-go

对 \(p=73,R=27,K=17\cdot29\)，取仓库中的反向实际边
\((0,1)\to(0,0)\)。规范角色

\[
\rho(a,b)=2(15a+b)\pmod3
\tag{19}
\]

在差向量 \((0,-1)\) 上取值 \(1\)。仿射映射
\(\Phi(z)=5-3z_2\) 把 endpoints 送到 \(2,5\)，并给出高度
\((4,4,1)\)，所以角色、范围、仿射和深度二的基本算术门都通过。

然而 \(4s<p\) 与 (2)--(4) 的完整枚举只有

\[
(J,x,s_0,s_1)=(1,2,2,5),(1,2,2,14),(2,2,2,11).
\tag{20}
\]

三项的 source canonical bases 分别是 \((2,5),(2,14),(2,11)\)，全部不相等。
更高 \(J\) 由 \(3^{J+2}<2p\) 排除。因此即使允许合法的 \(x=s_0\)，仍得到

\[
\boxed{\texttt{CANONICAL\_COMMON\_SOURCE\_BASE\_PROFILE\_EMPTY}}.
\tag{21}
\]

此外 target \(x=2\) 的单位群为 \(U(8)\)，
\(\operatorname{ord}_8(3)=2\)，没有 3-primary 物理方向；
\(\{3^e\bmod8\}=\{1,3\}\) 也不含目标 \(7\)。这是独立的

\[
\boxed{\texttt{TARGET\_PHYSICAL\_Q\_DIRECTION\_PRIMARY\_RANK\_ZERO}}.
\tag{22}
\]

式 (21)--(22) 只关闭这个 actual-F \(q=3\)、depth-\(2\) 同 target-fiber 入口。
\(p=73\) 在其它路径已有 Type II 终端，因此不是猜想反例。

## 5. 首个越界标签的 CRT defect map

令 \(p\equiv1\pmod4\)，\(M\ge3\) 为奇数且 \((p,M)=1\)。唯一取
\(b\in[1,M-1]\) 使 \(M\mid p+4b\)。严格 owner 窗口中这个 residue class 的标签为

\[
b+kM,\qquad k\ge0,\qquad4(b+kM)<p,
\tag{23}
\]

其数量精确为

\[
C_M(p)=\max\!\left(0,
\left\lceil\frac{p-4b}{4M}\right\rceil\right).
\tag{24}
\]

令 \(y=b+C_M(p)M\) 为首个越界标签，并定义 \(m=4y-p\)。由 CRT，\(m\) 是区间
\([1,4M-1]\) 内唯一满足

\[
m\equiv3\pmod4,\qquad m\equiv-2p\pmod M
\tag{25}
\]

的整数；反之 (25) 唯一恢复 \(y=(p+m)/4\)。于是

\[
\frac p4<y<\frac p4+M,\qquad
M\mid p+4y,\qquad
\gcd(M,y)=1.
\tag{26}
\]

再令

\[
n_M(p)=\frac{p+4y}{M}=\frac{2p+m}{M}.
\tag{27}
\]

则 \(n_M(p)\) 为奇数；对核心范围 \(p\ge73,M\ge3\)，还有 \(0<n_M(p)<p\)。这只是
一个严格变小的数值势，不是解可提升的 E4 递降。

还可以严格关闭一个窄提升类。设
\((a,b,c)\in\operatorname{Sol}(n)\)、\(2\le n<p\)，保持其中两个分母不变，只把
坐标 \(a\) 替换成 \(a'>0\)。既有精确判据的正性分子为

\[
D_p(n,a)=np-4(p-n)a.
\tag{27a}
\]

任一源解坐标满足 \(a>n/4\)，故
\(a\ge a_0=\lfloor n/4\rfloor+1\)。由于 (27a) 随 \(a\) 严格递减，令
\(W_p(n)=D_p(n,a_0)\)，则

\[
W_p(n)\le0
\Longrightarrow
\text{全部二分母保留的一项替换提升都因正性失败}.
\tag{27b}
\]

对奇 \(n\)，闭式为

\[
W_p(n)=
\begin{cases}
n^2+3n-3p,&n\equiv1\pmod4,\\
n^2+n-p,&n\equiv3\pmod4.
\end{cases}
\tag{27c}
\]

这不排除保留一个分母并重组另外两项的提升，更不排除一般 E4；\(W_p(n)>0\) 也只表示
正性尚未排除，仍须源解坐标和整除门。

若 \(p\) 同时为核心素数且 \(m<p\)，则 \(3\le m\le p-2\) 正好进入 Bradford
自然范围。枚举
\(d\mid y^2\) 后，完整分派是

\[
\begin{aligned}
\mathrm{Type\ I}:&\quad m\mid py+d;\\
\mathrm{Type\ II}:&\quad d\le y,\quad m\mid y+d.
\end{aligned}
\tag{28}
\]

命中即给短终端；全空则输出
`FIRST_OVERFLOW_SHORT_GAP_MENU_EMPTY`。后者只严格关闭这个 defect map，不能由
\(n_M(p)<p\) 冒充可提升递降。

## 6. 两个 overflow 控制与选择器接线

对 \(p=73,M=27\)，有

\[
(m,y,n_M)=(43,29,7).
\tag{29}
\]

\(y^2=29^2\) 的全部除子在 (28) 中均失败，所以得到菜单空回执。它与 (21)--(22)
组成同一请求的两侧局部障碍。这里 \(n_M=7\) 且
\(W_{73}(7)=7^2+7-73=-17\)，所以连全部二分母保留的一项替换提升也由 (27b)
关闭；例如源解 \((2,28,28)\) 的三个标记坐标都失败。但这仍不排除 \(p=73\) 的其它
终端或更一般提升。

对 \(p=557281,M=27\)，有

\[
(m,y,n_M)=(79,139340,41283).
\tag{30}
\]

\(d=16\mid y^2\)、\(d\le y\)，且 \(79\mid y+16\)，所以 (28) 给出 Type II 解

\[
\boxed{
\frac4{557281}
=\frac1{139340}
+\frac1{983043684}
+\frac1{8561081683035}.}
\tag{31}
\]

因此第 3 节的 actual-F positive control 是 terminal-preempted calibration；它证明
实际 F 请求到 candidate-fiber full-\(C_3\) 的入口存在，但不提供未决素数上的普遍
终端。

选择器新增的局部分派为

~~~text
one actual typed F request + one named edge
  -> finite candidate-fiber binding gate
       fail: exact target/deep binding obstruction
       pass:
         -> typed source-map/role/lineage/occurrence admission
              pass: one typed Q-PREFIX lineage
                    -> full product target hit: FIBER_REALIZED / TYPE_II_TERMINAL
                    -> target miss: FULL_CQ_PREFIX_TARGET_OR_KERNEL_SECTION
              fail: exact common-base/role/occurrence obstruction
       either local obstruction:
         -> first excluded q^(J+d)-owner label
              core prime + m < p + Bradford hit: TYPE_I_OR_II_TERMINAL
              menu empty: FIRST_OVERFLOW_SHORT_GAP_MENU_EMPTY
              numerical quotient n_M < p: no descent charge without E4
~~~

这张分派第一次在同一个 actual F 状态上闭合了“一个请求 \(\to\) full-\(C_3\)
candidate block”，并把一个 owner-window 失败送入确定的 \(<4M\) 短缺口菜单。尚未
证明的是：每个未终止 actual F 请求都依次通过 candidate binding 与 typed
admission，或每个 overflow 菜单空回执都能形成 exact successor、全解提升 E4 和
不可重置 E5。

## 聚焦验证

~~~bash
python3 reproductions/type_i_fg_qprefix_block_bound_first_overflow.py --verify
~~~

验证器只核对 (5)--(31) 的离散对数、有限 Fourier selector、canonical profiles、
估值、source line、typed keys、target 因子残数、\(p=73\) 完整局部候选和两个 overflow
菜单；不运行历史扫描。
