---
kind: claim
claim_id: type-I-path-anchored-atomic-split-total-typed-rechart
title: 双侧完整超额原子目标的全定义 hit/F/G 重图与 terminal-first 分派
statement: >-
  对任何已经满足 path_anchored_atomic_split_complete_excess_v1 算术输入条件的
  canonical atomic target，存在不读取未知 Egyptian-fraction 解的有限、确定性
  terminal-first 分派。它先在全部 Bradford 合法缺口与平方除子上穷尽直接 Type I/II
  证书；若该有限屏为空，则从 target 的整数 K_T 完整分解、中心指数盒和有限单位群中
  canonical 地得到互斥且穷尽的 hit/F/G 三分：hit 序列化为直接 centered Type I
  terminal，F 取最短再字典序最小的无界指数见证及 D-/D+，G 取有限商的 canonical
  separating character。故原子 split 条件 E1--E4 表示定理中“target typed fields、
  terminal priority 与 classification serializer”这一个数学子条件可由有限重算支付；
  原始 source/path provenance、state normal-form validator、scope/receipt serializer
  和 E5 strict rank 仍是独立 guards，不能由本分派自动支付。对 actual H4 clean q-bridge，
  在已有严格 parent-macro capacity 和其余 source guards 均被接受的条件下，本卡消除
  target-local typed/priority 的未指定余项，但不宣称 H4-Closure 或全局猜想已经证明。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-path-anchored-atomic-split-complete-excess-admission
  - type-I-overflow-total-cofactor-typed-projection-dispatch
  - type-I-factorization-free-centered-hit-terminal-serializer
  - denominator-escape-state-contract
topics:
  - type-I
  - atomic-split
  - target-rechart
  - terminal-first
  - direct-certificate
  - hit
  - F-state
  - G-state
  - separating-character
  - solution-lift
  - proof-boundary
sources:
  - claim: type-I-path-anchored-atomic-split-complete-excess-admission
    role: canonical-atomic-source-target-and-E5-gate
  - claim: type-I-overflow-total-cofactor-typed-projection-dispatch
    role: finite-hit-F-G-classifier-precedent
  - claim: type-I-factorization-free-centered-hit-terminal-serializer
    role: hit-to-direct-Type-I-terminal
  - concept: denominator-escape-state-contract
    role: typed-fiber-defect-and-E1-to-E5-contract
  - paper: bradford2024
    locator: Type-I-and-Type-II-square-divisor-parametrizations
    role: direct-gap-divisor-terminal-screen
  - reproduction: reproductions/type_i_atomic_split_total_typed_rechart.py
    role: focused-total-classifier-direct-screen-and-atomic-F-control
visibility: public
last_checked: '2026-08-17'
---

# 双侧完整超额原子目标的全定义 typed 重图

## 1. 范围：补的是 target 分派，不是 source admission

固定核心素数

\[
p\equiv1\pmod {24}.
\tag{1}
\]

考虑已经通过
'path_anchored_atomic_split_complete_excess_v1' 的**算术输入**的一个候选：它有一个
已指定 source/path occurrence、其 canonical complete-excess payload

\[
x=Q_x\beta_x,\qquad y=Q_y\beta_y,
\qquad Q_x,Q_y>1,\qquad p\nmid Q_xQ_y,
\tag{2}
\]

以及由该 payload 唯一确定的

\[
M=\operatorname{lcm}(A,Q_x,Q_y),\qquad
c=\langle(4M)^{-1}\rangle_p,
\tag{3}
\]

\[
K_T=Mc,\qquad R_T=\frac{4K_T-1}{p}.
\tag{4}
\]

已有原子 split 定理已经支付 (2)--(4) 的 canonicality，并给出 E5 的精确门；它刻意把
target 的 F/G/hit 类型、terminal-first priority 和 typed serializer 留作外部条件。本卡
只关闭这个**target-local、有限**的条件。特别地，它不构造一个未给出的 source/path，
不把 'candidate_transition' 写成 'verified_edge'，也不把条件性 normal-form validator
当作已接入的全局 registry。

由 (4)

\[
pR_T+1=4K_T,\qquad (K_T,R_T)=1,\qquad R_T\equiv3\pmod4.
\tag{5}
\]

下文每一项都只由 \(p\) 与 (2) 的有限整数 payload 重算；不会读取
\(\operatorname{Sol}(p)\) 的未知成员。

## 2. 完备的直接终端优先屏

对每个允许缺口 \(m\) 定义

\[
3\le m\le p-2,\qquad m\equiv3\pmod4,\qquad x_m=\frac{p+m}{4}.
\tag{6}
\]

令下面两组有限 receipt 为

\[
\begin{aligned}
\mathcal D_p^{\rm I}
 &=\{(m,d):d\mid x_m^2,\ m\mid px_m+d\},\\
\mathcal D_p^{\rm II}
 &=\{(m,d):d\mid x_m^2,\ d\le x_m,\ m\mid x_m+d\}.
\end{aligned}
\tag{7}
\]

以 \((m,\mathbf1_{\rm II},d)\) 的字典序固定一个规范优先级：较小缺口优先，同一缺口中
Type I 先于 Type II，再取较小 \(d\)。因此

\[
\mathcal D_p=\mathcal D_p^{\rm I}\cup\mathcal D_p^{\rm II}
\tag{8}
\]

是一个有限且不依赖 target 的 terminal-first screen。

若 \((m,d)\in\mathcal D_p^{\rm I}\)，令

\[
y=\frac{px_m+d}{m},\qquad z=\frac{px_my}{d}.
\tag{9}
\]

若 \((m,d)\in\mathcal D_p^{\rm II}\)，令

\[
y=\frac{p(x_m+d)}m,\qquad z=\frac{x_my}{d}.
\tag{10}
\]

这些表达式都是整数。事实上 \(m<p\) 给出 \((m,p)=1\)，而
\((x_m,m)=(x_m,p)=1\)。在 Type I 情形，\(d\equiv-px_m\pmod m\)，所以
\((d,m)=1\)；将 \(my=px_m+d\) 乘以 \(x_m\)，再用 \(d\mid x_m^2\)，得到
\(d\mid x_my\)。Type II 的同一论证从 \(my=p(x_m+d)\) 开始。

直接代入并使用 \(4x_m=p+m\)，两种情形都给出

\[
\frac4p=\frac1{x_m}+\frac1y+\frac1z.
\tag{11}
\]

所以 \(\mathcal D_p\ne\varnothing\) 时，规范最小元素是一个可重算的 terminal leaf；
此时选择器不应构造 (3)--(4) 的递归 target。这里的“complete”只指 (7) 所定义的
全部 Bradford 缺口--平方除子参数化，并不声称已经穷尽 Erd\H{o}s--Straus 的每种可能
证书。

## 3. 无直接终端时的 total hit/F/G classifier

以下假定 \(\mathcal D_p=\varnothing\)。对 (4) 的完整素因子分解写为

\[
K_T=\prod_{i=1}^r q_i^{\nu_i},\qquad
H_T=\langle q_1,\ldots,q_r\rangle\le U(R_T),
\tag{12}
\]

并令中心盒

\[
B_\nu=\prod_{i=1}^r[-\nu_i,\nu_i]\cap\mathbb Z^r.
\tag{13}
\]

分类器定义为

\[
\begin{array}{c|l}
\texttt{hit}
 &\exists z\in B_\nu:\prod_iq_i^{z_i}\equiv-1\pmod {R_T},\\
\texttt{F}
 &-1\in H_T\ \text{且没有盒内 hit},\\
\texttt{G}
 &-1\notin H_T.
\end{array}
\tag{14}
\]

这是互斥且穷尽的三分。它是有限的：盒 (13) 有有限体积，\(U(R_T)\) 也有限，故可用
有限乘法表先计算 \(H_T\)，再判定 \(-1\) 的成员资格。完整分解在这里是 verifier 的
数学输入；本结论不承诺对任意巨大 \(K_T\) 存在实用的快速分解算法。

### 3.1 'hit'：直接终端而非新递归 state

令 \(z\in B_\nu\) 是先按 \(\ell_1\) 长度、再按字典序最小的 hit，并取

\[
u=\prod_iq_i^{(z_i)_+},\qquad
v=\prod_iq_i^{(-z_i)_+}.
\tag{15}
\]

则

\[
(u,v)=1,\qquad uv\mid K_T,\qquad u+v\equiv0\pmod {R_T}.
\tag{16}
\]

由 (5)、(16) 和既有 centered-pair serializer，'hit' 是直接 Type I terminal，不可被
误登记为一个 F/G 后继。

### 3.2 'F'：规范无界见证及 signed defects

设

\[
\mathcal W_T=\left\{z\in\mathbb Z^r:
\prod_iq_i^{z_i}\equiv-1\pmod {R_T}\right\}.
\tag{17}
\]

F 情形中该集合非空。选择

\[
z_T=\min_{z\in\mathcal W_T}(\|z\|_1,z_1,\ldots,z_r).
\tag{18}
\]

式 (18) 是有效的有限选择，而不只是存在性符号。以 \(q_i^{\pm1}\) 为边的 Cayley 图
在有限群 \(H_T\) 上连通；到 \(-1\) 的一个 simple path 至多有
\(|H_T|-1\) 条边。因此某个 \(z\in\mathcal W_T\) 满足
\(\|z\|_1\le |H_T|-1\)，只需在该有限半径内枚举便能实现 (18)。

相对 (12) 重算全局定向缺陷

\[
d_i^-(z_T)=(-z_{T,i}-\nu_i)_+,\qquad
d_i^+(z_T)=(z_{T,i}-\nu_i)_+.
\tag{19}
\]

故 F target 的 typed payload 为 'target_fiber.status=nonempty'、见证 \(z_T\) 和
有定义的 \((D^-,D^+)\)；它不继承 source 的见证或缺陷。

### 3.3 'G'：有限、规范的 separating character

设 \(N=\exp U(R_T)\)。枚举 \(U(R_T)\) 的自然剩余类顺序及所有函数

\[
\chi:U(R_T)\longrightarrow\mathbb Z/N\mathbb Z,
\tag{20}
\]

以其值表的字典序选择第一个满足

\[
\chi(ab)=\chi(a)+\chi(b),\qquad
\chi(q_i)=0\ (1\le i\le r),\qquad
\chi(-1)\ne0
\tag{21}
\]

的函数。这个笨重的定义仅用于证明 totality；实际 verifier 可以以同一固定顺序的
CRT/SNF 分解压缩它。

式 (21) 一定有解：在有限阿贝尔商 \(U(R_T)/H_T\) 中，\(-1H_T\ne H_T\)，而有限
阿贝尔群的 \(\mathbb Z/N\mathbb Z\)-对偶分离非单位元。于是 G target 的 typed payload
为 'target_fiber.status=empty'、上述 canonical \(\chi\)，并将
'signed_defect.status=not_applicable' 连同 G 原因写入 receipt；它不能伪造数值零缺陷。

## 4. 条件性 E1--E5 后果

### 定理（原子 target 的 total typed rechart）

给定 (2) 的 canonical atomic payload，按以下顺序执行：

1. 枚举 (7)；若非空，输出其规范直接 Type I/II terminal；
2. 否则构造 (3)--(4)，完整分解 \(K_T\)，执行 (14)；
3. 'hit' 输出 (15)--(16) 的 terminal；F 或 G 以 (18)--(21) 生成 target typed fields。

该过程对每个合法整数 payload 都终止且决定唯一分派。它不读取未知解，故可作为原子
adapter 的 target classification、terminal priority 与 classification serializer 的完整
算术部分。

若既有原子 split 卡所要求的 persistent source/path provenance、scope continuity、
source/target normal-form validator、content-addressed receipt serializer 均独立接受，
则上述过程补足其 E2/E3 中 target type 的重算项；两端仍取

\[
W_S=W_T=\operatorname{Sol}(p),\qquad \Phi_{T\to S}(w)=w,
\tag{22}
\]

所以既有 E4 恒等 lift 不变。F/G 非终端 target 是否能进入递归，仍且仅受原子 split
卡的 E5 门

\[
A\le\frac{(p-1)^2}{4}
\quad\text{或}\quad
A>\frac{(p-1)^2}{4}\ \text{且}\ c<C
\tag{23}
\]

以及全部 source/receipt guards 约束。本定理没有从一个裸的 raw node 推出 E1，也没有把
有限的 target classifier 误当作全局良基势。

## 5. 对 actual H4 clean q-bridge 的受限作用

在 actual H4 clean \(q\)-bridge 的双侧、p-free endpoint 中，已有 bridge 给出 canonical
raw word、atomic payload 和同一 persistent parent 的严格容量比较

\[
\Lambda_p^\sharp(P)=(0,p-1)>(0,c_q)
\quad\text{当 }c_q\le p-2.
\tag{24}
\]

因此，在 H4 prefix、source state、scope、owner 和 normal-form guard 都被实际 receipt
接受的条件下，(7)--(21) 给出以下完整 target-local dispatch：

\[
\text{direct Bradford terminal}
\ \lor\
\text{centered-hit terminal}
\ \lor\
\text{typed F target}
\ \lor\
\text{typed G target}.
\tag{25}
\]

若落在后两项且 (24) 与其余 E1--E3 receipt 均通过，才得到 H4 parent-to-target 的
'verified_edge' 候选。故 (25) 消除了“target 的类型、优先级或序列化尚未定义”这个
数学空位；它仍未构造项目尚无的统一 verifier，也没有证明每个 H4 source 真的通过其余
guards。H4-Closure 及全局 G/Type I exit 仍是开放命题。

## 6. 聚焦严格 atomic 控制

复现器固定 'type_i_atomic_split_s_zero_endpoint_boundary' 的 \(p=73,r=1\) 原子算术
fixture。它的 target 为

\[
M=21\,333\,318\,666\,660,
\]

\[
K_T=1\,429\,332\,350\,666\,220,\qquad
R_T=78\,319\,580\,858\,423,
\tag{26}
\]

且

\[
K_T=2^2 3^3\cdot5\cdot7^2\cdot11\cdot13\cdot37\cdot67\cdot152381.
\tag{27}
\]

其 \(127575\) 个中心盒指数均不命中，而

\[
z=(111621836,4010792179018,3,0,0,0,0,0,0)
\tag{28}
\]

直接满足

\[
\prod_iq_i^{z_i}\equiv-1\pmod {R_T}.
\tag{29}
\]

故这个严格 target 是 F，且 (19) 给出

\[
D^-=(0,0,0,0,0,0,0,0,0),
\]

\[
D^+=(111621834,4010792179015,2,0,0,0,0,0,0).
\tag{30}
\]

同一个 \(p=73\) 先被 (7) 的 Type I \((m,d)=(7,10)\) 直接证书截断；因此 (26)--(30)
只是强制重图的算术控制，**不是**实际 persistent H4 edge，也不应绕过 terminal-first
priority。复现器还核对该 Type I 证书和同缺口 Type II \((7,1)\) 的三个分母恒等式。

~~~bash
python3 reproductions/type_i_atomic_split_total_typed_rechart.py --verify
~~~
