---
kind: claim
claim_id: type-I-overflow-full-product-d-one-a-one-all-core-dual-saturation-s-zero-tree-no-go
title: a=1 共同根的全核心双容量饱和与 s=0 任意深树 no-go
statement: >-
  对每个核心素数 p≡1 mod24 和每个固定有限深度 d，都存在无穷多个 a=1,d=1
  参数 r，使共同根 h=p+1 的一次真实 p-peel 两侧容量同时饱和到 W=p^2+1 与
  N=p^2+p+1；两侧完整超额块 Q_x,Q_y 均与 K 互素，规范 atomic-split multiplier
  L=Q_xQ_y 精确满足 nu_p(L-1)=2。同时，从 h=p+1 迭代
  P(h)=ph+1、M(h)=ph-p+1 的预定深度 d 完整二叉容量树全部真实存在，且树内宏没有
  bottom Type I terminal。根容量一般公式为
  gcd(x,K)=2gcd(r+(p+1)/2,(p^2+1)/2) 与
  gcd(y,K)=3gcd(2r+1,(p^2+p+1)/3)。该结果把既有 p=73 控制提升到所有核心素数，
  排除任何声称双根容量、s=0 位数与 P/M 树三项中至少一项会在统一固定深度内必然改善
  的局部出口策略；它不排除独立 Type I/II terminal-first，也不把 chart-local root
  receipt 自动升级为 persistent admitted lineage。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-full-product-d-one-a-one-two-sided-capacity-tree-no-go
  - type-I-path-anchored-atomic-split-complete-excess-admission
  - type-I-universal-p-source-capacity-anchor-orbit
topics:
  - type-I
  - overflow
  - full-product
  - d-one
  - a-one
  - common-root
  - dual-saturation
  - split-stutter
  - p-adic
  - hensel
  - binary-tree
  - crt-obstruction
  - proof-boundary
sources:
  - claim: type-I-overflow-full-product-d-one-a-one-two-sided-capacity-tree-no-go
    role: p-m-tree-and-actual-capacity-macro-semantics
  - claim: type-I-path-anchored-atomic-split-complete-excess-admission
    role: canonical-colored-split-multiplier
  - reproduction: reproductions/type_i_all_core_dual_saturation_s_zero_tree_no_go.py
    role: fresh-crt-dual-saturation-exact-height-and-depth-two-receipt
visibility: public
last_checked: '2026-08-13'
---

# \(a=1\) 共同根的全核心双容量饱和与 \(s=0\) 任意深树 no-go

## 1. 共同根与两侧 peeled 坐标

固定核心素数

\[
p\equiv1\pmod {24},
\tag{1}
\]

并沿用 \(a=1,d=1\) 图表

\[
g=\frac{p+1}{2},
\qquad C=\frac{p^2-1}{2},
\qquad T=p^2r-g,
\tag{2}
\]

\[
A=gT,
\qquad K=CT,
\qquad
R=2p^3r-p^2-2pr-p+1.
\tag{3}
\]

于是 \(4K=pR+1\)。根锚 \(u_0=p+1\) 整除 \(C\)，且

\[
R-(p+1)=py,
\tag{4}
\]

其中

\[
\boxed{y=2(p^2-1)r-p-2,}
\tag{5}
\]

\[
\boxed{x=R-y
=2p^3r-2p^2r-p^2-2pr+2r+3.}
\tag{6}
\]

当 \(p\nmid y\) 时，从 \(\{p+1,R-p-1\}\) 选择 departure side 的 raw
\(p\)-边恰做一次、无 gcd reduction，并到达 primitive bottom node \(\{x,y\}\)。

记

\[
W=p^2+1,
\qquad N=p^2+p+1.
\tag{7}
\]

既有双侧容量公式在 \(u=p+1\) 上先给

\[
(x,K)=(W,K),
\qquad (y,K)=(N,K).
\tag{8}
\]

## 2. 全称的共同根容量映射

### 定理 1（两侧根容量的 \(r\)-gcd 公式）

对每个 (1)--(7) 的整数参数，

\[
\boxed{
(x,K)=2\gcd\left(r+g,\frac W2\right),}
\tag{9}
\]

\[
\boxed{
(y,K)=3\gcd\left(2r+1,\frac N3\right).}
\tag{10}
\]

**证明。** 首先

\[
(W,C)=2,
\qquad
\left(\frac W2,\frac C2\right)=1.
\tag{11}
\]

模 \(W/2\) 有 \(p^2\equiv-1\)，故

\[
T\equiv-(r+g)\pmod {W/2}.
\tag{12}
\]

又 \(W\) 恰含一层 2，而 \(K\) 至少含这层 2，结合 (8)、(11)--(12) 得 (9)。

同理，

\[
(N,C)=3,
\qquad
\left(\frac N3,\frac C3\right)=1.
\tag{13}
\]

模 \(N/3\) 有

\[
2T\equiv-(p+1)(2r+1).
\tag{14}
\]

而 \(2(p+1)\) 在模 \(N/3\) 下可逆，所以 (8)、(13)--(14) 给出 (10)。
\(\square\)

因此两侧分别饱和的充要同余为

\[
(x,K)=W
\Longleftrightarrow
r\equiv-g\pmod {W/2},
\tag{15}
\]

\[
(y,K)=N
\Longleftrightarrow
2r+1\equiv0\pmod {N/3}.
\tag{16}
\]

而

\[
\left(\frac W2,\frac N3\right)=1,
\tag{17}
\]

所以双饱和同余对每个核心素数都兼容。下面采用更强的 \(T\)-整除，一并固定完整超额
块的 maximality 与任意有限容量树。

## 3. 同时装入任意固定深度的容量树

定义

\[
P(u)=pu+1,
\qquad M(u)=pu-p+1.
\tag{18}
\]

给定 \(d\ge0\)，令 \(\mathcal S_d\) 是从 \(p+1\) 开始、对所有深度小于 \(d\)
的节点同时应用 \(P,M\) 得到的完整二叉树。置

\[
\boxed{
\mathcal M_d=
\operatorname{lcm}\left(
 (WN)^2,
 \left\{\frac{u}{(u,C)}:u\in\mathcal S_d\right\}
\right).}
\tag{19}
\]

每个树节点都同余 \(1\pmod p\)，所以

\[
(p,\mathcal M_d)=1.
\tag{20}
\]

要求

\[
\boxed{T\equiv0\pmod {\mathcal M_d}.}
\tag{21}
\]

等价于 \(r\) 的唯一模 \(\mathcal M_d\) 类，因为 \(p^2\) 可逆。由

\[
u\mid CT
\Longleftrightarrow
\frac{u}{(u,C)}\mid T,
\tag{22}
\]

式 (21) 使 \(\mathcal S_d\) 的每个节点都整除 \(K\)。它还蕴含

\[
W^2N^2\mid T.
\tag{23}
\]

结合定理 1，(23) 给两侧容量饱和

\[
(x,K)=W,
\qquad (y,K)=N.
\tag{24}

而且 \(K\) 在 \(W,N\) 每个素因子上的容量严格高于 endpoint 本身。由
\((x,K)=W\)、\((y,K)=N\) 逐素数反推，存在唯一整数

\[
x=Q_xW,
\qquad y=Q_yN,
\tag{25}
\]

满足

\[
\boxed{(Q_xQ_y,K)=1.}
\tag{26}

因此 \(Q_x,Q_y\) 恰为两侧相对 \(K\) 的 maximal complete-excess blocks；它们还
因 \((x,y)=1\) 而彼此互素。规范 atomic-split multiplier 简化为

\[
\boxed{L=Q_xQ_y=\frac{xy}{WN}.}
\tag{27}

## 4. 每个核心素数都有两个 \(s=0\) Hensel 类

定义

\[
F_p(r)=xy-WN.
\tag{28}

从 (5)--(7) 展开并只保留模 \(p^2\)，得到

\[
\boxed{
F_p(r)\equiv
-(4r^2+10r+7)+p(4r^2+2r-4)
\pmod {p^2}.}
\tag{29}

令

\[
q(r)=4r^2+10r+7.
\tag{30}

其判别式为

\[
\Delta=10^2-4\cdot4\cdot7=-12.
\tag{31}

因 \(p\equiv1\pmod {24}\)，有 \(p\equiv1\pmod3\)，从而
\((-3/p)=1\)。所以 (30) 在模 \(p\) 下有两个不同根；\(p\nmid12\) 说明两根都
是单根。又

\[
F_p'(r)\equiv-q'(r)\pmod p,
\tag{32}

所以每个根都唯一 Hensel 提升为一个

\[
\rho_\pm\pmod {p^2}
\tag{33}

使 \(F_p(\rho_\pm)\equiv0\pmod {p^2}\)。由 (27)--(28) 及 \(p\nmid WN\)，

\[
F_p(r)\equiv0\pmod {p^2}
\Longleftrightarrow
L\equiv1\pmod {p^2}.
\tag{34}

这正是 split relay 的 \(s\equiv0\pmod p\) 类。

这些 Hensel 类还自动通过实际根路径所需的三个 \(p\)-门：

\[
q(-1)=1,
\qquad q(-3/2)=1,
\qquad q(-1/2)=3.
\tag{35}

其中 \(r\equiv-1\pmod p\) 会破坏根锚以及 \(1+p\pmod {p^2}\) 树节点的
departure 精确一层条件，\(r\equiv-1/2\pmod p\) 会破坏
\(1\pmod {p^2}\) 树节点的对应条件，而 \(r\equiv-3/2\pmod p\) 会使 peeled
坐标 \(x\) 含 \(p\)。式 (35) 逐一排除这三个坏类；所以根 departure
\(R-(p+1)\) 恰含一层 \(p\)，两个 peeled 坐标都 \(p\)-free，且两类树节点的
departure 都恰含一层 \(p\)。这里不涉及 ordinary root multiplier；在 \(a=1\) 行它本来
就属于既有 \(p\)-free failure 分支。

## 5. CRT 合并及精确二阶高度

由 (20)，(21) 的模 \(\mathcal M_d\) 类可与任一 (33) 用 CRT 合并。故对每个
\(p,d\)，存在无穷多个正 \(r\) 同时满足：

\[
T\equiv0\pmod {\mathcal M_d},
\qquad
r\equiv\rho_\pm\pmod {p^2}.
\tag{36}

还可把 \(L-1\) 的高度固定为恰好 2。先取 (36) 的一个代表 \(r_0\)，再写

\[
r=r_0+p^2\mathcal M_d k.
\tag{37}

模 \(p^3\) 的 Taylor 展开为

\[
F_p(r)
\equiv F_p(r_0)+p^2\mathcal M_dkF_p'(r_0)
\pmod {p^3}.
\tag{38}

式 (20)、(32) 说明 \(\mathcal M_dF_p'(r_0)\not\equiv0\pmod p\)。因此
\(k\pmod p\) 中恰有一个值让 (38) 继续被 \(p^3\) 整除；其余 \(p-1\) 个值全部满足

\[
\nu_p(F_p(r))=2.
\tag{39}

固定其中任一值，再加任意 \(p^3\mathcal M_d\) 的正倍数，得到无穷多个参数。取其中
充分大的正代表，还可同时保证有限树中每次 peeled 坐标都严格大于对应的
\(P(u),M(u)\)，所以所用容量都是真正的超容量而不是等号边界。由 (27)--(28) 及
\(p\nmid WN\)，

\[
\boxed{\nu_p(L-1)=2.}
\tag{40}

## 6. 树中每条边都是真实容量宏

每个 \(u\in\mathcal S_d\) 在模 \(p^2\) 下只能属于

\[
u\equiv1
\quad\text{或}\quad
u\equiv1+p.
\tag{41}

而

\[
R\equiv1-p(2r+1)\pmod {p^2}.
\tag{42}

式 (35) 排除 \(r\equiv-1/2,-1\pmod p\)，故每个树节点都满足

\[
p\parallel R-u.
\tag{43}

由 (21)--(22)，\(u,P(u),M(u)\) 全部整除 \(K\)。双侧容量定理于是把每条树边实现为

\[
\text{一次实际 raw }p\text{-edge}
\quad+\quad
\text{一段实际 capacity peeling}.
\tag{44}

departure side 含 \(p\nmid K\)，容量剥离的中间节点仍有超容量素数，而子锚的对侧
\(R-P(u)\) 或 \(R-M(u)\) 又由 (43) 含 \(p\)。所以 (44) 的宏内部没有 bottom
Type I sink。

综合以上得到主结论：

\[
\boxed{
\forall p\equiv1\pmod {24}\text{ prime}\ \forall d\ge0
\exists^\infty r>0:
\begin{array}{l}
(x,K)=p^2+1,\ (y,K)=p^2+p+1,\\
(Q_xQ_y,K)=1,\ \nu_p(L-1)=2,\\
\mathcal S_d\text{ 的全部容量宏真实存在且宏内无 bottom Type I sink}.
\end{array}}
\tag{45}
\]

## 7. 证明边界与研究后果

式 (45) 同时保持了三种此前看似可用的局部资源：

1. 两侧共同根容量都不是真因子，而是分别饱和到 \(p^2+1\)、\(p^2+p+1\)；
2. split multiplier 不只是 \(1\pmod p\)，而是精确落在 \(1\pmod {p^2}\) 的 hard 类；
3. 任意在证明前固定的 \(P/M\) 搜索深度都可以完整不退出。

所以任何仅依赖这三项，并断言其中至少一项会在统一固定深度内必然严格改善的局部势，
都不可能单独证明全局出口。

这里没有声称一条固定 \(r\) 支撑无限树；量词是 \(\forall d\,\exists^\infty r\)。也没有
排除树外 raw 分支、跨图表动作或独立 Type I/II terminal-first。更重要的是，(45) 从
共同根 node 开始提供 chart-local actual raw receipts，但没有凭空制造 persistent parent；
只有调用方已经把该根绑定到 admitted lineage 时，才能谈后续 E1--E5。因而本卡是对
局部势与固定菜单的全称 no-go，不是 Erdős--Straus 反例，也不是 admitted cycle。

## 8. 聚焦回执

```bash
python3 reproductions/type_i_all_core_dual_saturation_s_zero_tree_no_go.py --verify
```

脚本固定 \(p=73,d=2\)，从 (19)、(21)、(29)、(33) 现场 CRT 构造一个新参数；随后
重算七个树节点、六个容量宏、双侧饱和、两侧 maximal complete-excess blocks 及
\(\nu_{73}(L-1)=2\)。它不扫描素数范围、分母范围、selector history 或历史结果。
