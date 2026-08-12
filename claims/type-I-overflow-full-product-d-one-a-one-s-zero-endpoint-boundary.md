---
kind: claim
claim_id: type-I-overflow-full-product-d-one-a-one-s-zero-endpoint-boundary
title: a=1 的 s=0 二阶回返、小容量端点出口与固定深度 no-go
statement: >-
  在完整乘积 d=1 的 a=1 图表中，任一实际 primitive capacity endpoint h|K 满足精确
  容量映射 gcd(R-h,K)=gcd(ph+1,K)。若 2<=h<p 且 h^2<p，则要么
  R-h|K 直接给 Type I terminal，要么 R-h 的完整超额单侧 receipt p-free 且 canonical
  carry 严格降到 c<=p-2；特别地，所有核心素数上的 h=2,3 都闭合。另一方面，
  h=1 (mod p) 时 R-h 的完整超额块必含 p，故 p-free gate 强制失败并继续 p-peel。
  对条件性 atomic split stutter，s=(L-1)/p 的 hard 类精确等价于 L=1 (mod p^2)；
  写 L=1+p^2 t，则 target 仍为 a=1,d=1，参数满足 r'=r+tT、T'=LT，但根 departure
  的 p 进层数可以升高，不能视为原容量树原样重启。固定 p=73,r=95979 给出层数
  1->2 后再由 h=3 严格降到 c=2；而 r=21944065678 给出根 s=0、两端点
  5330=p^2+1 与 5403=p^2+p+1，两个 immediate endpoint receipt 的完整块都含 73。
  更强地，对每个固定深度 N，CRT 可同时保持该根 s=0 cell 与深度 N 的完整 P/M
  容量树。因此任何仅以 P/M endpoint projection 是否在固定深度内退出为判据的策略都
  不能关闭 s=0；本卡留下的决定性余项是大非 1 (mod p) endpoint 的严格动作，
  或跨整棵 p-block 树的全局良基势/终端。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-path-anchored-atomic-split-complete-excess-admission
  - type-I-overflow-full-product-d-one-a-one-split-carrier-stutter-relay
  - type-I-overflow-full-product-d-one-a-one-two-sided-capacity-tree-no-go
  - type-I-universal-p-source-capacity-anchor-orbit
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
topics:
  - type-I
  - overflow
  - full-product
  - d-one
  - a-one
  - split-stutter
  - p-adic
  - capacity-endpoint
  - complete-excess-bundle
  - strict-carry
  - binary-tree
  - crt-obstruction
  - proof-boundary
sources:
  - claim: type-I-path-anchored-atomic-split-complete-excess-admission
    role: atomic-split-admission-and-stutter-boundary
  - claim: type-I-overflow-full-product-d-one-a-one-split-carrier-stutter-relay
    role: s-relay-and-minimal-receipt-cell
  - claim: type-I-overflow-full-product-d-one-a-one-two-sided-capacity-tree-no-go
    role: p-m-capacity-tree-and-crt-semantics
  - claim: type-I-universal-p-source-capacity-anchor-orbit
    role: actual-capacity-endpoint-peeling
  - claim: type-I-bottom-sink-scc-complete-excess-bundle-selector
    role: single-side-complete-excess-receipt
  - reproduction: reproductions/type_i_atomic_split_s_zero_endpoint_boundary.py
    role: focused-small-endpoint-restart-dual-p-block-and-depth-three-controls
visibility: public
last_checked: '2026-08-13'
---

# \(a=1\) 的 \(s=0\) 二阶回返、小容量端点出口与固定深度 no-go

## 1. 设置与结论分层

固定核心素数 \(p\equiv1\pmod {24}\)，在 \(a=1,d=1\) 图表中写

\[
g=\frac{p+1}{2},\qquad b=2pr-1,\qquad n=(p+1)b-1,
\tag{1}
\]

\[
T=p^2r-g,\qquad A=gT,\qquad
K=\frac{p^2-1}{2}T=A(p-1),
\tag{2}
\]

\[
R=(p-1)n-1,\qquad 4K=pR+1.
\tag{3}
\]

本卡有两类互补结论：

1. 第 2--3 节建立任意 endpoint 的精确容量映射，并以强化后的 \(h^2<p\) 阈值全称
   关闭平方根尺度的小 endpoint；
2. 第 4--7 节证明任意 \(p^f\)-peel 的双侧容量映射，及 \(s=0\) 可以提升根
   \(p\)-进层数、与任意固定深度的完整容量树共存，所以不能把小 endpoint 引理外推成
   全覆盖。

这里的 split target 只有在
`path_anchored_atomic_split_complete_excess_v1` 已通过 E1--E4 时才是合法
checkpoint；若 E5 stutter，它本身仍不是入队边。

## 2. 任意 capacity endpoint 的精确映射

设 \(\{h,R-h\}\) 是一条真实路径上的 primitive node，且

\[
h\mid K.
\tag{4}
\]

令 \(z=R-h\)。由 (3)，

\[
pz=pR-ph=4K-(ph+1).
\tag{5}
\]

又 \(p\nmid K\)，故乘 \(z\) 以 \(p\) 不改变它与 \(K\) 的 gcd。于是

\[
\boxed{(R-h,K)=(ph+1,K).}
\tag{6}
\]

这比只给一个依赖 \(p,h\) 的上界更强：它是可以逐点重算的精确容量映射。

若 \(z\nmid K\)，按 \(K\) 的完整容量唯一分解

\[
z=Q\beta,\qquad
Q=\prod_{\nu_q(z)>\nu_q(K)}q^{\nu_q(z)}.
\tag{7}
\]

令

\[
g_A=(A,Q),\qquad E=Q/g_A,\qquad D=\beta g_A.
\tag{8}
\]

由 \((Q,\beta)=1\) 得 \((g_A,\beta)=1\)。又 \(\beta\mid K\)、\(g_A\mid A\mid K\)，
所以

\[
D\mid K,\qquad ED=z.
\tag{9}
\]

特别地，\(D\mid z\) 与 (6) 给出

\[
\boxed{D\mid ph+1.}
\tag{10}
\]

另一方面，primitive 条件给出 \((h,\beta)=1\)；结合 \(h,\beta\mid K\) 得

\[
h\beta\mid K.
\tag{11}
\]

所以 (7) 确实是现有单侧 path-anchored complete-excess receipt，而不是静态重分块。
其规范 support 与 multiplier 为

\[
M=\operatorname{lcm}(A,Q)=AE.
\tag{12}
\]

## 3. 小容量 endpoint 的全称严格出口

### 定理 1（小 endpoint terminal-or-strict）

若

\[
2\le h<p,\qquad h^2<p,
\tag{13}
\]

则以下二者必有其一：

1. \(R-h\mid K\)，于是 \(h(R-h)\mid K\)，直接给 bottom Type I terminal；
2. (7)--(12) 给出 \(p\)-free 单侧 receipt，且其 target cofactor
   \(c=\langle-E^{-1}\rangle_p\) 满足 \(1\le c\le p-2\)。

**证明。** 若 \(z\mid K\)，由 \((h,z)=1\) 和 (4) 即得第 1 项。以下设
\(z\nmid K\)。因 \(h\ne1\pmod p\) 且 \(R\equiv1\pmod p\)，有 \(p\nmid z\)，故
\(p\nmid Q\)，receipt 的 p-free 门通过。

parent cofactor 为 \(p-1\)。唯一可能不严格的情形是 \(E\equiv1\pmod p\)。由
\(ED=z\equiv1-h\pmod p\)，这会强制

\[
D\equiv1-h\pmod p.
\tag{14}
\]

因 \(D>0\)、\(2\le h<p\)，存在 \(m\ge1\) 使

\[
D=mp+1-h.
\tag{15}
\]

式 (10) 给 \(D\le ph+1\)，故 \(m\le h\)。再次用 (10)：

\[
D\mid m(ph+1)-hD=m+h(h-1).
\tag{16}
\]

右端为正，故 \(D\le m+h(h-1)\)。与 (15) 比较得到

\[
m(p-1)\le h^2-1<p-1,
\tag{17}
\]

与 \(m\ge1\) 矛盾。因此 \(E\not\equiv1\pmod p\)，canonical cofactor 不是 \(p-1\)，只能
落在 \(1,\ldots,p-2\)。\(\square\)

令

\[
H_p=\max\{h\in\mathbb N:h^2<p\}.
\tag{18}
\]

所有 \(2\le h\le H_p\) 都被定理 1 关闭。对核心素数 \(p\ge73\)，特别有
\(h=2,3\) 无条件闭合；\(p=73\) 时覆盖 \(2\le h\le8\)。

这个强化后的半径仍不能由同一整除论证推广到全部 \(h\)。例如

\[
p=73,\qquad h=19,\qquad D=347=5p+1-h
\]

满足 \(D\mid ph+1=1388\)。这不必是一个真实 state，却足以说明 (10)、(14) 单独不能
排除大 endpoint stutter。

## 4. Endpoint 的模 \(p\) 二分

式 (3) 给 \(R\equiv1\pmod p\)。因此：

1. 若 \(h\equiv1\pmod p\)，则 \(p\mid R-h\)。因为 \(p\nmid K\)，式 (7) 的完整
   超额块 \(Q\) 必含 \(R-h\) 的全部 \(p\)-block，故该单侧 complete-excess carry 被
   p-free gate 排除；沿此 complement 的规范 continuation 是继续真实 \(p\)-peeling。
   这不排除 priority terminal 或另一侧的其它合法动作。
2. 若 \(h\not\equiv1\pmod p\)，则 \(p\nmid Q\) 自动成立；若再有 (13)，定理 1
   给 terminal 或 strict carry。

所以 endpoint-first 的精确未知域不是“所有 endpoint”，而是：

\[
\boxed{
h\equiv1\pmod p\text{ 的继续 }p\text{-tree}
\quad\text{或}\quad
h\not\equiv1\pmod p\text{ 的大 endpoint}.}
\tag{19}
\]

### 4.1 任意 \(p^f\)-peel 的双侧容量映射

前述 gcd 映射不只适用于一层。设 \(f\ge1\) 且
\(p^f\mid R-h\)，定义

\[
y=\frac{R-h}{p^f},
\qquad
x=R-y.
\tag{19a}
\]

则直接由 \(4K=pR+1\) 得

\[
\boxed{
p^{f+1}y=4K-(ph+1),\qquad
p^{f+1}x=4(p^f-1)K+(ph-p^f+1).}
\tag{19b}
\]

由于 \(p\nmid K\)，两式模 \(K\) 精确给出

\[
\boxed{
(y,K)=(ph+1,K),\qquad
(x,K)=(ph-p^f+1,K).}
\tag{19c}
\]

这些代数恒等式只需 \(p^f\mid R-h\)，不需要 \(h\mid K\)；条件
\(p^f\parallel R-h\) 只在把 \(f\) 解释为剥尽的 \(p\)-block 高度时需要。条件
\(h\mid K\)、正性、primitive/path receipt 和 terminal-first gate 则属于实际容量宏的
准入语义，不能由 (19b)--(19c) 代替。

当 \(f=1\) 时两个容量标签（也是完整子锚候选）为

\[
P(h)=ph+1,\qquad M(h)=p(h-1)+1.
\tag{19d}
\]

它们的实际容量分别是 \((P(h),K)\) 与 \((M(h),K)\)；只有候选本身整除
\(K\) 时，才是完整子锚。

固定同一个 \(K\)，若 \(h>1\)、\(h\mid K\)，且
\(h'\in\{P(h),M(h)\}\) 本身整除 \(K\)，则 \(h'>h\)，故

\[
\rho_K(h')=\frac K{h'}<\frac K h=\rho_K(h).
\tag{19e}
\]

这是一个真实的固定图表局部良基量，但不是全局势。首先，若“child”只指
\((P(h),K)\) 或 \((M(h),K)\)，它可能小于 \(h\)，(19e) 不成立；其次，合法
canonical target 一般是 \(K_M=ALc_M\)，并不总是 \(LK\)。只对已通过 E1--E4 的
\(a=1,d=1\) split stutter checkpoint，有 \(c_M=p-1\)，从而
\(K_M=AL(p-1)=LK\)，同一锚上的预算才重置为
\(\rho_{K_M}(h)=L\rho_K(h)\)。特别是 \(s\equiv0\pmod p\) 时
\(L=1+p^2t\)，同时 \(R\) 也改变，旧 departure/path 未必可以重放。故后面的
fixed-depth no-go 与 (19e) 并不矛盾：前者的量词是“每个 \(N\) 存在一个随 \(N\)
增长的 \(K_N\)”，后者只是“每个固定 \(K\) 的完整子锚路径有限”。

## 5. \(s=0\) 的二阶正规形

设一个已获 E1--E4 准入的 atomic split 满足 carry stutter

\[
L\equiv1\pmod p,\qquad s=\frac{L-1}{p}.
\tag{20}
\]

已有 relay 把 target 写成

\[
n'=Ln-s,\qquad b'=Lb-s.
\tag{21}
\]

真正返回 \(p\)-free-failure hard 类的条件为

\[
\boxed{s\equiv0\pmod p\Longleftrightarrow L\equiv1\pmod {p^2}.}
\tag{22}
\]

写

\[
L=1+p^2t,\qquad s=pt.
\tag{23}
\]

由 \(b=2pr-1\) 与 (21)，

\[
\begin{aligned}
b'
&=(2pr-1)L-pt\\
&=2p(rL-gt)-1.
\end{aligned}
\tag{24}
\]

因此 target 仍在 \(a=1,d=1\) 正规形，且新参数精确为

\[
\boxed{r'=rL-gt=r+t(p^2r-g)=r+tT.}
\tag{25}
\]

于是

\[
\boxed{T'=p^2r'-g=LT.}
\tag{26}
\]

式 (25) 还给出

\[
r'\equiv r-gt\pmod p.
\tag{27}
\]

所以 \(s=0\) 并不保证 root departure 的 \(p\)-进层数不变；\(t\) 的下一位会改变新的
\(r'\pmod p\)。

### 5.1 原样重启的严格反例

取

\[
p=73,\qquad r=95\,979.
\tag{28}
\]

根 \(u=74\) 一次 \(p\)-peel 后得到

\[
x=73\,638\,154\,802,\qquad y=1\,022\,752\,149,
\]

\[
(Q_x,\beta_x,g_x)=(36\,819\,077\,401,2,1),
\qquad
(Q_y,\beta_y,g_y)=(340\,917\,383,3,1).
\tag{29}
\]

联合倍率为

\[
L=12\,552\,263\,512\,023\,361\,583,
\qquad \nu_{73}(L-1)=2,
\tag{30}
\]

且

\[
t=\frac{L-1}{73^2}
=2\,355\,463\,222\,372\,558\equiv43\pmod {73}.
\tag{31}
\]

由 (25)，target 参数满足

\[
r'=1\,204\,753\,612\,468\,350\,993\,590\,111
\equiv-1\pmod {73}.
\tag{32}
\]

所以 root departure 的估值从

\[
\nu_{73}(R-74)=1
\]

升为

\[
\nu_{73}(R'-74)=2.
\tag{33}
\]

这严格否定“\(s=0\) 后同一 root \(p\)-edge 原样重启”。不过完整 \(p^2\)-peel 后两侧
容量为 \((74,3)\)，其 \(h=3\) endpoint 满足

\[
R'-3=4Q_3,\qquad
Q_3=234\,290\,844\,523\,945\,154\,425\,456\,065\,041,
\]

\[
(A',Q_3)=1,\qquad Q_3\equiv36\pmod {73},
\tag{34}
\]

所以定理 1 给出的 canonical capacity 精确为 \(2\)。这张控制说明层数可以改变，但小
endpoint 一旦出现仍会严格退出。

## 6. 双 immediate endpoint 同时 p-free 失败

小 endpoint 并非每个 \(s=0\) root 都会出现。取

\[
p=73,\qquad r=21\,944\,065\,678.
\tag{35}
\]

对应

\[
\begin{aligned}
T&=116\,939\,925\,998\,025,\\
A&=4\,326\,777\,261\,926\,925,\\
K&=311\,527\,962\,858\,738\,600,\\
R&=17\,070\,025\,362\,122\,663.
\end{aligned}
\tag{36}
\]

根 peeled pair 为

\[
x=16\,836\,189\,398\,257\,970,
\qquad
y=233\,835\,963\,864\,693,
\tag{37}
\]

其完整 split 分解是

\[
x=3\,158\,759\,737\,009\cdot5\,330,
\qquad
y=43\,278\,912\,431\cdot5\,403.
\tag{38}
\]

两个完整块都与 \(A,K\) 互素，且

\[
L=136\,707\,686\,048\,581\,100\,858\,879,
\qquad \nu_{73}(L-1)=2.
\tag{39}
\]

因此这是一个真实 \(s=0\) root，而两侧实际 capacity endpoint 精确为

\[
h_x=5\,330=p^2+1,\qquad
h_y=5\,403=p^2+p+1.
\tag{40}
\]

它们都同余 \(1\pmod {73}\)。两个 immediate endpoint 的合法单侧 receipt 分别为

\[
R-h_x
=5\,690\,008\,454\,039\,111\cdot3,
\tag{41}
\]

\[
R-h_y
=43\,278\,802\,703\cdot394\,420.
\tag{42}
\]

但

\[
5\,690\,008\,454\,039\,111
=73\cdot77\,945\,321\,288\,207,
\]

\[
43\,278\,802\,703
=73\cdot592\,860\,311.
\tag{43}
\]

两张 receipt 的 residual gate、互素和 maximality 都成立；失败的精确字段只是
\(p\nmid Q\)。所以它们必须继续 \(p\)-peel，不能登记 strict canonical carry。这是对
“一层 endpoint-first 必闭合 \(s=0\)”的真实严格反例，不是否定后续路径可能退出。

## 7. \(s=0\) 与任意固定深度容量树共存

定义根 \(u_0=p+1\)，并对每个 endpoint 迭代

\[
P(u)=pu+1,\qquad M(u)=pu-p+1.
\tag{44}
\]

记 \(\mathcal S_N\) 为深度 \(N\) 的完整 \(P/M\) 树，并令

\[
C=\frac{p^2-1}{2},\qquad
L_N=\operatorname{lcm}_{u\in\mathcal S_N}\frac{u}{(u,C)}.
\tag{45}
\]

上一张容量树定理已经证明：若 \(L_N\mid T\)，且 \(r\pmod p\) 避开两个 departure
退化类，则整棵树都给真实的“一次 \(p\)-peel + 容量剥离”边。

### 定理 2（固定深度 \(s=0\) 容量树 no-go）

对 \(p=73\) 及每个有限 \(N\ge1\)，存在参数 \(r_N\)，使：

1. 根 split 的完整残量为 \((\beta_x,\beta_y)=(5330,5403)\)；
2. 根联合倍率满足 \(L\equiv1\pmod {73^2}\)；
3. \(\mathcal S_N\) 的每个 endpoint 都整除 \(K\)，每个非叶 departure 恰含一层
   超容量 \(73\)；
4. 树内相应容量宏没有 bottom Type I terminal；所以任何仅以固定深度 \(P/M\)
   endpoint projection 是否退出为判据的策略都不能强迫退出。

**证明。** 对根两侧的线性式，消元恒等式为

\[
p^2x-2(p-1)(p^2-1)T=p^2+1,
\]

\[
p^2y-2(p^2-1)T=-(p^2+p+1).
\tag{46}
\]

令

\[
D_0=\operatorname{lcm}\left(
\frac{p^2+1}{(p^2+1,C)},
\frac{p^2+p+1}{(p^2+p+1,C)}
\right).
\tag{47}
\]

在 \(p=73\) 时

\[
D_0=\operatorname{lcm}(2665,1801)=4\,799\,665.
\tag{48}
\]

这里

\[
D_0=5\cdot13\cdot41\cdot1801
\tag{49}
\]

是 squarefree，且 \((C,D_0)=1\)。令

\[
M_N=\operatorname{lcm}(L_N,D_0^2),
\qquad M_N\mid T.
\tag{50}
\]

再同时固定

\[
r_N\equiv396\pmod {73^2}.
\tag{51}
\]

这个剩余类避开树节点两种模 \(p^2\) departure class 对应的两个 \(r\bmod p\) 退化类；
特别地 \(p\parallel R-(p+1)\)。由 \(D_0\mid T\) 与 \(2\cdot3\mid C\) 得
\(p^2+1=5330\mid K\)、\(p^2+p+1=5403\mid K\)。上一张容量树定理的精确双侧
公式于是给

\[
(x,K)=5330,\qquad(y,K)=5403.
\tag{52}
\]

还需证明 endpoint 的一次素数层全部留在 residual。对
\(q\mid D_0\)，式 (49) 表明对应 endpoint 常数在 \(q\) 上恰有一层，而 (50) 给
\(\nu_q(K)=\nu_q(T)\ge2\)。结合 (52)，对应坐标的 \(q\)-估值恰为 1。对 \(x\)
中的 2 与 \(y\) 中的 3，

\[
\nu_2(C)=3>\nu_2(5330)=1,\qquad
\nu_3(C)=2>\nu_3(5403)=1.
\tag{53}
\]

结合 (52)，这证明 endpoint 的每个素数都留在 residual。若坐标还有与 \(K\) 共有的
其它素数，它会出现在 (52) 的 gcd 中，矛盾；所以其余坐标素数都不整除 \(K\)，并完整
进入超额块。因此完整分解精确为

\[
\boxed{
(\beta_x,\beta_y)=(5330,5403),\qquad
(Q_xQ_y,K)=1,\qquad(g_x,g_y)=(1,1).}
\tag{54}
\]

在满足 endpoint 整除的这个 CRT 子格上，两个 quotient 可显式写成

\[
Q_x=\frac{383616r-2663}{2665},\qquad
Q_y=\frac{3552r-25}{1801}.
\tag{55}
\]

令 \(r_0=21\,944\,065\,678\) 为 (35) 的控制点。直接计算

\[
\begin{aligned}
r_0&\equiv396\pmod {73^2},\\
73^2r_0-37&\equiv0\pmod {D_0}.
\end{aligned}
\tag{56}
\]

任一满足 (50)--(51) 的 \(r_N\) 也有
\(73^2r_N-37\equiv0\pmod {D_0}\)。由于 \(73^2\) 在模 \(D_0\) 下可逆，
(51)、(56) 给

\[
r_N-r_0\equiv0\pmod {73^2D_0}.
\tag{57}
\]

因 \(2665,1801\mid D_0\)，把 (57) 代入 (55) 后
\(Q_x(r_N)-Q_x(r_0)\) 与 \(Q_y(r_N)-Q_y(r_0)\) 都被 \(73^2\) 整除。因此两商模
\(73^2\) 与控制点 (35) 相同；再由 (38)--(39) 与 (54)，canonical 联合倍率
\(L=Q_xQ_y\) 仍满足

\[
L\equiv1\pmod {73^2}.
\tag{58}
\]

最后，所有 \(P/M\) tree endpoint 都同余 \(1\pmod {73}\)，且 \(D_0\) 为 73-free，故
\((M_N,73^2)=1\)。所以 (50)--(51) 可由 CRT 同时满足；取足够大的正代表保证全部坐标
为正。(51) 还避开上述两个 departure 退化类，所以树内每条 \(p\)-edge 恰为一层。
引用上一张容量树定理的第 3--4 项，每条 \(P/M\) 宏都真实，且
宏内没有 bottom Type I terminal。每个叶 endpoint 也满足 \(h\equiv1\pmod {73}\)，
所以第 4 节的 p-free gate 排除其 immediate single-side complete-excess carry，并把该
projection 继续送往 \(p\)-peel；这给出本定理第 3--4 项。\(\square\)

固定 \(N=3\) 的 verifier 控制参数为

\[
r_3=
3\,081\,303\,956\,325\,088\,557\,376\,553\,319\,788\,046\,874\,862\,151\,069\,359\,244\,625\,807\,615\,652\,961\,464\,503.
\tag{59}
\]

脚本重算 15 个 endpoint、14 条容量宏、根 \((5330,5403)\) 与 \(L\equiv1\pmod {73^2}\)。
一般 \(N\) 由 (45)--(58) 的 CRT 证明承担。该 no-go 只针对固定深度的 \(P/M\)
endpoint 投影；同层其它 raw branch、独立 Type I/II terminal-first 或跨图表宏仍可能
提前退出。

## 8. 新的决定性余项

本卡证明“只观察 fixed-depth \(P/M\) endpoint projection”不是全局方法。后续
[单侧 endpoint stutter guarded relay](type-I-overflow-full-product-d-one-a-one-single-endpoint-stutter-guarded-relay.md)
又把大 endpoint 的旧余项进一步压缩。对已通过 source、residual 和 p-free gate
的单侧 endpoint receipt，若 multiplier \(E_0\not\equiv1\pmod p\)，其算术 carry
当步严格；若 \(E_0=1+ps\)，则

\[
E_1\equiv s\pmod p.
\tag{60}
\]

因此 \(s\not\equiv0,1,-1\) 时下一 ordinary suffix 有严格算术 cofactor，
\(s\equiv-1\) 时 alternate source 的算术 capacity 为 1，\(s\equiv1\) 时进入有限
regeneration。这些 suffix 只有在 persistent/typed/terminal-first 与 E1--E5 回执全部通过后
才能升格为合法宏。在这个 p-free stutter 子域内，真正未闭合的算术类只剩

\[
\boxed{
E_0\equiv1\pmod {p^2},
\quad\text{或}\quad
E_0\equiv1+p\pmod {p^2}\text{ 且 regeneration 最终落入 p-free failure}.}
\tag{61}
\]

另外，\(h\equiv1\pmod p\) 时 \(p\mid E_0\)，p-free gate 失败，必须保留为独立的
p-block continuation，不属于 (61)。而且 \(p=97,r=6618,h=58\) 是真实可达的
一步 stutter；(60) 给出下一 ordinary suffix 的算术候选 capacity \(80<96\)，
只有所有 E1--E5 guards 通过后才能登记为宏。所以不能再把旧目标写成
“所有大非 \(1\bmod p\) endpoint 一步 strict”。

势函数方向也有两个新的硬边界。固定 \(K\) 时，完整 \(P/M\) 子锚确实由 (19e)
严格消耗 \(K/h\)；但已获 E1--E4 准入的 stutter checkpoint 会把这个量乘以
\(L\)，故它不是仅由该算术 checkpoint 控制的全局势。更强地，
[Hensel 高度 no-go](type-I-overflow-full-product-d-one-a-one-s-zero-hensel-height-no-go.md)
在一个固定完整超额胞中构造出任意大的条件 rechart 算术 target 根
\(p\)-进高度；它排除仅从这个 normal form 推出统一高度界，但不排除 admission gate
对合法边施加额外限制。因此下一步不应继续机械加深投影、只从算术 normal form
给 \(p\)-block 深度设统一上界，或使用单步 endpoint rank；应在
以下两个对象中建立全称定理：

1. **任意高度的 p-free return 出口：** 对 (61) 的两类，利用 (19b)--(19c) 的精确
   双侧容量、同层其它 raw branch 或 Type I/II 菜单，构造 terminal 或最终
   capacity \(<p-1\) 的 guarded macro；
2. **可跨 rechart 的树级资源：** 给 \(p\)-block continuation 一个不会被
   \(K\mapsto LK\)、alternate source 或 split checkpoint 重置的良基量，并证明每次
   无 terminal 的完整宏都严格消耗它。

任何只承诺“再看固定若干层 \(P/M\) endpoint projection”的选择器都被定理 2 排除；
中间 raw node 的 Type I/II、其它 branch 或跨图表动作不在该 no-go 的量词内。当前结果
仍未证明所有 \(s=0\) 状态退出，也没有证明 Erdos--Straus 猜想。

## 9. 聚焦回执

运行 `python3 reproductions/type_i_atomic_split_s_zero_endpoint_boundary.py --verify`。

脚本只重放 \(r=57\) 的两个小 endpoint、(28) 的二阶 root-restart、(35) 的双
immediate p-block 失败和 (51) 的深度 3 控制；不扫描素数、分母、历史 selector、完整
证书菜单或一般深度。
