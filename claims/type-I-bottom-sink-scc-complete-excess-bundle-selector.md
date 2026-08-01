---
kind: claim
claim_id: type-I-bottom-sink-scc-complete-excess-bundle-selector
title: 底层汇 SCC 的完整超额 bundle 选择器与线性源 overflow 收缩
statement: 对合法核心图表 4K=pR+1 的任一来源可达完整 raw formal Reach，汇点直接给 Type I；否则任取 bottom sink-SCC，在其中选小坐标最小节点 {x,y}，必有 x|K。把 y 中所有超过 K 指数容量的完整素数幂块打包为 Q，并写 y=Q beta，则 Q>1、x beta|K、(Q,x beta)=1、Q不整除K。对 absorbed support A|K，规范容量并不是一般的 AQ，而是 M=lcm(A,Q)；它满足 M/A>=2。若规范 R_M<p，则以 M 为新 absorbed support、Sol(p) 为共同标记集和恒等提升得到完整 E1--E5 边；若 R_M>p，则得到 pn=4Md+1 的 bundle overflow。因此 competing-excess 不再是独立 sink-SCC 余项，每个 F 状态都严格分流为 bundle marked absorb 或 bundle overflow。若初始 A=1 且图表有线性源 p=a+s+asR，则 overflow 强制 as<4/alpha；as=1 的整族由 Jacobi 角色严格属于 G，故线性 F overflow 只能有 alpha=1 且 as属于{2,3}。在更窄的 source-anchored clean single-external alpha=1 子类中，q-peeling 到 anchor 后关闭全部 as=3，并把 as=2 收缩到必要类 p congruent to 169 modulo 240。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-formal-full-excess-cycle-or-hit-reduction
  - type-I-formal-cycle-representation-lattice-capacity
  - type-I-target-fiber-joint-capacity-signed-carrier-dictionary
  - type-I-bottom-external-static-carrier-support-fork
  - type-I-marked-support-accumulation-rechart-saturation
  - two-denominator-lift-same-one-mod-four-no-go
  - denominator-escape-state-contract
topics:
  - type-I
  - F-state
  - formal-target-pair
  - bottom-SCC
  - competing-excess
  - q-adic-capacity
  - composite-carrier
  - complete-excess-bundle
  - path-anchored-receipt
  - absorbed-support
  - marked-descent
  - overflow
  - linear-source
  - Jacobi-character
sources:
  - claim: type-I-formal-full-excess-cycle-or-hit-reduction
    role: finite-complete-reach-and-bottom-cycle-reduction
  - claim: type-I-target-fiber-joint-capacity-signed-carrier-dictionary
    role: signed-node-overflow-carrier
  - claim: type-I-bottom-external-static-carrier-support-fork
    role: prime-power-clean-versus-competing-boundary
  - claim: type-I-marked-support-accumulation-rechart-saturation
    role: identity-lift-state-and-well-founded-potential
  - claim: two-denominator-lift-same-one-mod-four-no-go
    role: conditional-rejection-of-smaller-same-class-d-only-successors
  - claim: denominator-escape-state-contract
    role: marked-edge-and-path-anchored-receipt-contract
visibility: public
last_checked: '2026-08-01'
---

# 底层汇 SCC 的完整超额 bundle 选择器与线性源 overflow 收缩

## 1. 完整 Reach 与汇 SCC

固定核心素数和合法线性图表状态

\[
p\equiv1\pmod {24},
\qquad
4K=pR+1,
\qquad
3\le R\le p-2,
\tag{1}
\]

并允许状态携带

\[
A\mid K
\tag{2}
\]

作为 absorbed support。取任一已经验真的形式源

\[
U+V=Rm,
\qquad
(U,V)=1.
\tag{3}
\]

在完整、未剪枝 raw formal Reach 中，对每个满足

\[
v_q(UV)>v_q(K)
\tag{4}
\]

的素数保留正规迁移。已有完整超高图定理证明：可达图有限；每条 \(m>1\) 边严格
降低 \(m\)；无出边节点精确满足 \(UV\mid K\)，并直接恢复原 \(p\) 的 Type I
证书。因此任一没有直接汇点的 sink-SCC 都位于

\[
m=1,
\qquad
X+Y=R,
\qquad
(X,Y)=1.
\tag{5}
\]

以下证明只使用完整出边集和 sink 性，不依赖路径 tie-break、周期词选择或有限样本上界。

## 2. 最小小坐标必已落入 K 容量

令 \(\mathcal C\) 是 (5) 中的一个 sink-SCC。在 \(\mathcal C\) 中选择小坐标最小的
节点，并定向为

\[
\{x,y\},
\qquad
x<y,
\qquad
x+y=R.
\tag{6}
\]

若存在素数 \(q\) 满足

\[
v_q(x)>v_q(K),
\tag{7}
\]

则完整 raw 图含边

\[
\{x,y\}\xrightarrow q
\left\{\frac xq,R-\frac xq\right\}.
\tag{8}
\]

因为 \(x/q<x<R/2\)，后继的规范小坐标恰为 \(x/q\)。又因 \(\mathcal C\) 是
sink-SCC，(8) 的后继仍必须属于 \(\mathcal C\)，这与 (6) 的最小性矛盾。因此

\[
\boxed{x\mid K.}
\tag{9}
\]

若再有 \(y\mid K\)，由 \((x,y)=1\) 得 \(xy\mid K\)。该节点没有 raw 出边，并由
已有汇点正规形给出直接 Type I。因此以下只需研究

\[
y\nmid K.
\tag{10}
\]

## 3. 规范 complete-excess bundle

写

\[
y=\prod_q q^{e_q},
\qquad
\nu_q=v_q(K),
\tag{11}
\]

并定义全部超容量素数集合和完整幂块 bundle

\[
E=\{q:e_q>\nu_q\},
\qquad
Q=\prod_{q\in E}q^{e_q},
\qquad
\beta=\frac yQ.
\tag{12}
\]

由 (10)，\(E\ne\varnothing\)，所以 \(Q>1\)。定义 (12) 时取的是每个 offending
素数在 \(y\) 中的**完整素数幂块**，不是只取超出的 \(e_q-\nu_q\) 层。因此

\[
(Q,\beta)=1.
\tag{13}
\]

再由 \((x,y)=1\) 得 \((Q,x\beta)=1\)。对 \(q\mid\beta\)，定义保证
\(v_q(\beta)\le\nu_q\)；对 \(q\mid x\)，式 (9) 给出同样的容量界，而
\((x,\beta)=1\)。故

\[
\boxed{
Q>1,
\qquad
x\beta\mid K,
\qquad
(Q,x\beta)=1,
\qquad
Q\nmid K,
\qquad
Q<R<p.}
\tag{14}
\]

最后一项来自 \(Q\mid y<R\)。于是最小节点规范写成

\[
\boxed{x+Q\beta=R,\qquad x\beta\mid K.}
\tag{15}
\]

这就是 `complete_excess_bundle` receipt。旧的 clean single-external slab 只是
\(E=\{q\}\)、\(q\nmid K\) 时的特例。一般 \(E\) 可以含多个素数，也可以含
\(q\mid K\) 但 \(e_q>v_q(K)\) 的完整块。

若把节点定向指数向量写成

\[
z_q=v_q(y)-v_q(x),
\tag{16}
\]

则由于两侧互素，(12) 还可写成

\[
E=\operatorname{supp}\operatorname{ov}_{\nu}(z),
\qquad
Q=\prod_{q\in E}q^{|z_q|}.
\tag{17}
\]

所以 \(Q\) 不是任意重图表模数：它正是带符号容量字典在同一实际整数侧给出的全部
超额载体之并。

## 4. 容量账本必须用 lcm 合并

旧 prime-power 边因 \(q\nmid K\) 自动有 \((A,Q)=1\)，所以写成 \(AQ\)。对 (12)
的一般 bundle，这个互素性可以失败。规范容量并必须定义为

\[
\boxed{M=\operatorname{lcm}(A,Q),}
\tag{18}
\]

不能无条件写成 \(AQ\)。事实上，对每个 \(q\mid Q\)，

\[
v_q(Q)=e_q>v_q(K)\ge v_q(A).
\tag{19}
\]

因此

\[
A\mid M,
\qquad
Q\mid M,
\qquad
\frac MA=
\prod_{q\mid Q}q^{e_q-v_q(A)}\ge2,
\qquad
M\nmid K.
\tag{20}
\]

式 (18) 逐素数取旧承诺与新完整块的最大指数。若在 \((A,Q)>1\) 时误取 \(AQ\)，共同
素数的指数会被无依据地相加；相应模同余即使成立，也只是 unanchored rechart，不能由
该 bundle receipt 通过 E1 来源核验。

## 5. bundle marked edge 或 overflow

由 \(A\mid K\)、\(Q<R<p\) 得 \((p,4M)=1\)。定义唯一规范代表

\[
1\le R_M<4M,
\qquad
pR_M\equiv-1\pmod {4M},
\qquad
K_M=\frac{pR_M+1}{4}.
\tag{21}
\]

于是

\[
R_M\equiv3\pmod4,
\qquad
M\mid K_M.
\tag{22}
\]

还有

\[
\boxed{R_M\ne R.}
\tag{23}
\]

若 \(R\ge4M\)，(23) 来自规范范围；若 \(R<4M\) 且 \(R_M=R\)，则
\(4M\mid pR+1=4K\)，即 \(M\mid K\)，与 (20) 矛盾。又因
\(R_M\equiv3\pmod4\)、\(p\equiv1\pmod4\)，\(R_M\ne p\)。所以只有以下二分。

### 5.1 \(R_M<p\)：完整 E1--E5 marked edge

若

\[
R_M<p,
\tag{24}
\]

则 \(3\le R_M\le p-2\)，并定义后继

\[
\mathsf T=(p,R_M,K_M;M).
\tag{25}
\]

两端均取

\[
W_{\mathsf S}=W_{\mathsf T}=\operatorname{Sol}(p),
\tag{26}
\]

解提升为恒等映射。令

\[
B_p=\frac{(p-1)^2}{4},
\qquad
\Phi(\mathsf S)=\left\lfloor\frac{B_p}{A}\right\rfloor.
\tag{27}
\]

由 (22)、(24) 有 \(M\mid K_M\le B_p\)，而 (20) 给出 \(M\ge2A\)。所以

\[
\boxed{
\left\lfloor\frac{B_p}{M}\right\rfloor
<
\left\lfloor\frac{B_p}{A}\right\rfloor.}
\tag{28}
\]

规范边型 `marked_complete_excess_bundle_edge_v1` 的合同为：

| 合同项 | 核验内容 |
|---|---|
| E1 | 重放来源路径；sink-minimum 型再重放完整 SCC 与最小节点，path-anchored 型直接重算 (14)--(20) |
| E2 | 由 (21)、(25) 重算全部后继字段和 F/G/hit 分类 |
| E3 | 同时验证源状态、目标状态、bundle receipt 与 lcm 更新 |
| E4 | (26) 的恒等提升 |
| E5 | (27)--(28) 的 absorbed-support 势严格下降 |

这里给出的是可执行 verifier 应满足的规范合同；当前聚焦脚本重放代表性 receipt，尚未
实现同名的通用状态 verifier。边的 established 状态由上述整数证明承担，而不是由四个
样例外推。

该边允许同一素数在以后以更高完整块再次出现；每次只有当新指数严格超过当前
\(K\) 容量时，lcm 账本才会增长。因而它不依赖“素数永不重入”，而依赖可重算的
逐素数容量并和数值势。

### 5.2 \(R_M>p\)：bundle overflow

若

\[
R_M>p,
\tag{29}
\]

则 \(M>p/4\)。写 \(K_M=MC\)，并置

\[
n=4M-R_M,
\qquad
d=p-C.
\tag{30}
\]

与 prime-power 情形完全相同，(21) 给出

\[
\boxed{
pn=4Md+1,
\qquad
(M,pn)=1.}
\tag{31}
\]

这里 \(n\ge1\)。若 \(d\le0\)，右端至多为 \(1\)，而左端至少为 \(p>1\)，矛盾；
所以 \(d>0\) 也由同一恒等式自动得到。

这是 `complete_excess_bundle_overflow` receipt，不是 E4 后继。若额外满足
\(2\le n<p\)，此前对同 \(1\pmod4\) 的 D-only 空纤维定理仍适用；一般 bundle
overflow 并不保证 \(n<p\)，所以不能无条件调用该 no-go。(31) 的下一出口必须换载体、
直接终端或改变尾数据。

## 6. 完整 sink-SCC 与 F 状态的选择器结论

综合第 1--5 节，对任一来源可达完整 formal Reach 有

\[
\boxed{
\text{DIRECT TYPE I}
\quad\lor\quad
\text{BUNDLE MARKED ABSORB}
\quad\lor\quad
\text{BUNDLE OVERFLOW}.}
\tag{32}
\]

算法上先检查完整 Reach 的直接终端；若无终端，就把每个 sink-SCC 的节点按
\((\min(X,Y),\max(X,Y))\) 排序，并选择排序列表字典序最小的 sink，再取其中最小
小坐标，(12) 唯一确定 \(Q\)。所以 (32) 不含路径选择量词。

特别地，每个 F 状态的规范无界目标纤维见证 \(z\) 都显式给出

\[
U=\prod_q q^{(z_q)_+},
\qquad
V=\prod_q q^{(-z_q)_+},
\qquad
m=\frac{U+V}{R}.
\]

目标同余保证 \(m\in\mathbb N\)，正负支撑分离保证 \((U,V)=1\)，故这是 (3) 的
形式源。若 Reach 中出现 \(UV\mid K\)，它会直接产生盒内 Type I，与 F 分类矛盾。
因此 F 状态无条件满足

\[
\boxed{
F
\Longrightarrow
\text{BUNDLE MARKED ABSORB}
\quad\lor\quad
\text{BUNDLE OVERFLOW}.}
\tag{33}
\]

这首次把 F 的表示/格证书接到合法跨状态宏边：格或 Fourier 证书负责给出规范形式源；
完整 raw Reach 负责到达 sink；带符号容量在最小节点打包成实际整数载体；(18)、(28)
负责跨状态容量账本与良基性。

G 状态确实没有只用 \(K\) 支撑的形式源，但后续的通用源定理给出

\[
(U,V,m)=\bigl(p,R(p-1)-p,p-1\bigr)
\xrightarrow{q=p,t=1}
(1,R-1,1).
\tag{33a}
\]

因此按当前允许外部超容量素数的 raw 合同，裸 G 也有实际 source；(32) 对每个合法
F/G/hit 图表都可调用。这是本卡第 1--5 节之后的下游加强，不参与其原证明。严格证明见
[通用 \(p\) 源与容量锚点轨道](type-I-universal-p-source-capacity-anchor-orbit.md)。

## 7. 线性源的初始 overflow 只剩三条窄射线

再假设当前是初始状态 \(A=1\)，图表具有真正线性源

\[
p=a+s+asR,
\qquad
a,s\in\mathbb N,
\tag{34}
\]

把 (15) 暂写为

\[
R=x+Q\eta,
\qquad
x\eta\mid K.
\tag{35}
\]

进入真 overflow \(R_Q>p\) 后，由初始 \(A=1\) 得 \(M=Q\)，并有

\[
Q>\frac p4>\frac R4.
\]

再定义

\[
\alpha:=\eta,
\qquad
\beta:=x.
\]

由于 \(\alpha Q<R\)，上述不等式才推出 \(\alpha<4\)，所以

\[
R=\alpha Q+\beta,
\qquad
\alpha\beta\mid K,
\qquad
\alpha\in\{1,2,3\}.
\tag{36}
\]

线性源同时给出

\[
asR<p<R_Q<4Q<\frac{4R}{\alpha}.
\tag{37}
\]

因此

\[
\boxed{as<\frac4\alpha.}
\tag{38}
\]

于是 \(\alpha=2,3\) 都强制 \(as=1\)；\(\alpha=1\) 只允许
\(as\in\{1,2,3\}\)。但 \(as=1\) 时必有 \(a=s=1\)，从而

\[
p=R+2,
\qquad
R\equiv23\pmod {24},
\qquad
K=\left(\frac{R+1}{2}\right)^2.
\tag{39}
\]

定义单位群上的 Jacobi 角色

\[
\chi(u)=\left(\frac uR\right).
\]

因 \(R\equiv7\pmod8\)，有 \(\chi(2)=1\)。若奇素数 \(q\mid K\)，则
\(q\mid R+1\)，所以 \(R\equiv-1\pmod q\)。Jacobi 二次互反给出

\[
\left(\frac qR\right)
\left(\frac Rq\right)
=(-1)^{\frac{q-1}{2}\frac{R-1}{2}},
\qquad
\left(\frac Rq\right)=
\left(\frac{-1}q\right).
\tag{40}
\]

由于 \((R-1)/2\) 为奇数，两项符号相消，故 \(\chi(q)=1\)。另一方面

\[
\chi(-1)=(-1)^{(R-1)/2}=-1.
\tag{41}
\]

所以 \(\chi\) 在全部 \(K\) 支撑生成元上平凡，却分离目标 \(-1\)。这严格证明

\[
\boxed{as=1\Longrightarrow\text{state is G}.}
\tag{42}
\]

结合 (38)，线性 F 状态的初始 bundle overflow 只能满足

\[
\boxed{
\alpha=1,
\qquad
as\in\{2,3\}.}
\tag{43}
\]

在通常取 \(s\) 为奇数的有向线性源规范中，(43) 只剩

\[
(a,s)=(2,1),(3,1),(1,3).
\tag{44}
\]

式 (43) 只覆盖初始、具有线性源的 F 图表；它不覆盖 \(A>1\) 的累积图表或没有线性源
的普通 bundle overflow。

## 8. clean single-external 的 \(\alpha=1\) 条件闭合

本节增加一个范围更窄但更强的结论。除第 7 节前提外，假设 overflow 来自一条已经有
source/path/node 回执的 **clean single-external** bottom slab

\[
\{Q,b\},
\qquad
R=Q+b,
\qquad
Q=q^e,
\qquad
q\nmid K,
\qquad
b\mid K,
\qquad
R_Q>p.
\]

这里 \(\alpha=1\)，且绝不把一般 composite complete-excess bundle 偷换成 clean
prime power。对

\[
V_j=\{q^{e-j},R-q^{e-j}\},
\qquad 0\le j\le e,
\]

当 \(j<e\) 时，所选侧仍有正 \(q\)-指数，而 \(v_q(K)=0\)，所以完整 raw 图含边
\(V_j\to V_{j+1}\)。因此原回执可严格延伸到 anchor

\[
\boxed{\{1,R-1\}.}
\]

若原 slab 在 sink-SCC 中，sink 性还保证整段留在同一 SCC；若它只是一般 Reach 节点，
则使用 `path_anchored_complete_excess_bundle` 来源回执，而不能冒充 sink-minimum
回执。后续 lcm、恒等提升和势证明不变。

令

\[
S=\frac{R-1}{2},
\qquad
\{1,R-1\}=\{1,2S\}.
\]

### 8.1 \(as=3\) 全部吸收

此时 \(p=3R+4\)、\(R\equiv7\pmod8\)，并且

\[
K=\frac{(R+1)(3R+1)}4.
\]

\(S\) 为奇数。对任意素数 \(\ell\mid S\)，有 \(R\equiv1\pmod\ell\)，两个分子块
分别同余 \(2,4\)，故 \((S,K)=1\)。另一方面 \(v_2(K)\ge2\)，所以 anchor 的规范
complete-excess bundle 恰为

\[
Q_*=S,
\qquad
\beta_*=2.
\]

它给出 \(M=S\)，且

\[
R_S<4S=2R-2<p=3R+4.
\]

因此 clean \(\alpha=1,\ as=3\) 整支都产生 path-anchored bundle marked edge。

### 8.2 \(as=2\) 只剩一个必要模类

此时 \(p=2R+3\)、\(R\equiv11\pmod{12}\)，且

\[
K=\frac{(R+1)(2R+1)}4,
\qquad
S\equiv5\pmod6,
\qquad
(S,K)=1.
\]

若 \(K\) 为偶数，等价于 \(p\equiv1\pmod{48}\)，anchor bundle 仍是
\((Q_*,\beta_*)=(S,2)\)，并由 \(R_S<2R-2<p\) 吸收。

若 \(K\) 为奇数，等价于 \(p\equiv25\pmod{48}\)，则 \(2\) 也超容量，anchor bundle
变为

\[
Q_*=M=R-1,
\qquad
\beta_*=1,
\qquad
p=2M+5.
\]

写 \(5R_M+1=\kappa M\)。由规范模 \(4M\) 条件、\(R_M\equiv3\pmod4\) 和
\(0<R_M<4M\) 得 \(\kappa\equiv2\pmod4\) 且 \(0<\kappa<20\)。又因
\(p=2M+5>5\) 为素数，有 \(5\nmid M\)；同余 \(\kappa M\equiv1\pmod5\) 排除
\(\kappa=10\)。所以

\[
\kappa\in\{2,6,14,18\},
\]

而 \(M\bmod5=1,2,3,4\) 分别对应 \(\kappa=6,18,2,14\)。由
\(R_M=(\kappa M-1)/5\) 和本分支 \(M\ge34\)，因此
\(M\bmod5\in\{1,3\}\) 时吸收，\(M\bmod5\in\{2,4\}\) 时 overflow。与
\(p\equiv25\pmod{48}\) 合并后，素数情形只有

\[
p\equiv73,169\pmod{240}
\]

仍 overflow；\(121,217\pmod{240}\) 已吸收，而 \(25\pmod{240}\) 被素性排除。

对 \(p\equiv73\pmod{240}\)，令

\[
x=\frac{p+7}{4},
\qquad
d=\frac{x^2}{5}.
\]

此时 \(5\mid x\)、\(d\mid x^2\)，并由 \(p=4x-7\) 得

\[
px+d=7\left(\frac{3x^2}{5}-x\right).
\]

所以 gap \(7\) 的 Type I 判据直接命中。最终得到条件性无样本收缩

\[
\boxed{
\text{source-anchored clean }\alpha=1\text{ overflow}
\Longrightarrow
\text{terminal/marked edge}
\quad\lor\quad
\bigl(as=2,\ p\equiv169\pmod{240}\bigr).}
\]

这里 \(p\ge73\)，所以 gap \(7\) 也处在合法范围。这不是对一般 bundle overflow 的
结论。例 \(p=673,R=335\) 的 \(\alpha=1\)
complete-excess 节点 \(\{7,328\}\) 有 \(Q=328=2^3\cdot41\) 且
\((Q,K)=4\)，所以 clean \(q\)-peeling 前提失败。本卡也没有证明
\(169\bmod240\) 的严格 source-Reach 分支非空；这里只声称它是尚未关闭的必要类。

## 9. 精确边界

### 9.1 单素数 clean 强化为假，复合 bundle 为真

取

\[
(p,R,K)=(21169,19,100553),
\qquad
K=193\cdot521.
\tag{45}
\]

该状态为 F；一个规范形式源是

\[
(521^3,1,7443198).
\tag{46}
\]

一条精确 raw 路径为

\[
\begin{aligned}
(1,141420761,7443198)
&\xrightarrow{521}(12,271441,14287)\\
&\xrightarrow{521}(11,521,28)\\
&\xrightarrow{11}(1,56,3)\\
&\xrightarrow7(8,11,1).
\end{aligned}
\tag{47}
\]

底层 \(q=2\) 九循环覆盖全部九个节点。该 sink-SCC 没有任何 clean
single-external prime-power slab，但最小点 \(\{1,18\}\) 给出

\[
Q=18,
\qquad
\beta=1,
\qquad
R_{18}=71<p,
\tag{48}
\]

所以复合 bundle 给出合法 marked edge。该素数另有全局 gap \(31\) Type I；(45)--(48)
反驳的是“sink-SCC 必含单素数 clean slab”，不是猜想反例。

### 9.2 共享 K 素数时必须使用 lcm

对

\[
(p,R,K;A)=(409,51,5215;5),
\tag{49}
\]

sink 最小点为 \(\{1,50\}\)，且

\[
Q=50=2\cdot5^2,
\qquad
v_5(K)=1,
\qquad
(A,Q)=5.
\tag{50}
\]

规范并为 \(M=\operatorname{lcm}(5,50)=50\)，不是 \(250\)。它给出

\[
R_M=111<p
\tag{51}
\]

的 marked edge。相同机制在 \((p,R,K;A)=(409,251,25665;5)\) 给出

\[
Q=M=250,
\qquad
R_M=511>p,
\tag{52}
\]

以及

\[
409\cdot489=4\cdot250\cdot200+1.
\tag{53}
\]

这说明 (32) 不能加强为“必进入 marked edge”。

### 9.3 二进自环被 bundle edge 合法关闭

旧边界

\[
(p,R,K)=(1009,3,757)
\tag{54}
\]

的 \(\{1,2\}\) 自环在本定理中给出 \(Q=2\)、\(R_2=7<p\)。因此该 raw 自环仍不是
逐边递降，但整个 sink-SCC 已有合法 marked 宏边。

### 9.4 线性 F overflow 的幸存射线

取

\[
(p,R,K)=(241,79,4760),
\qquad
(a,s)=(3,1).
\tag{55}
\]

该状态为 \(\Psi_0=1\) 的 F 状态，实际 Reach 含

\[
(Q,\alpha,\beta)=(71,1,8),
\qquad
R_{71}=251>p.
\tag{56}
\]

这说明 (43) 的 \(as=3\) 支不是空形式。原 \(q=71\) clean slab 一步 peeling 已到
\(\{1,78\}\)，第 8.1 节的规范 anchor bundle 为

\[
Q_*=39,\qquad \beta_*=2,\qquad R_{39}=11<p.
\]

所以该例已经由全称 clean-\(\alpha=1\) 子定理退出。相同 Reach 还另有

\[
(Q',\alpha',\beta')=(37,2,5),
\qquad
R_{37}=35<p,
\tag{57}
\]

式 (57) 给出另一个 alternate carrier；它不是第 8.1 节证明所需的载体。

## 10. 证明边界与下一目标

本定理及其两个下游加强完成四项此前开放的接口：

1. `COMPETING_EXCESS` 不再是 bottom sink-SCC 的独立余项；多素数和 K 内超指数都由
   规范 bundle 一次打包；
2. 每个 F 状态的规范表示证书都能产生合法 marked edge 或显式 overflow，而不再只
   输出 formal cycle/Pareto miss；
3. `universal_p_source_v1` 把同一结论扩展到裸 G，不再要求 \(K\)-支撑形式源；
4. 初始 \(A=1\) 的每个 bundle overflow 都由 determinant 派生出合法 charged-support
   identity edge。

它没有关闭：

- \(A>1\) 累积图表的 overflow；
- 累积层中保持旧支撑的 source/path/node alternate、直接终端或外层 support reset。

在更窄的 source-anchored clean single-external \(\alpha=1\) 子类中，第 8 节已经关闭
全部 \(as=3\) 和除 \(p\equiv169\pmod{240}\) 外的 \(as=2\)；该结论不能推广到一般
complete-excess bundle。

因此下一目标已经从“competing-excess SCC 是否到达 clean 单素数 slab”严格收缩为：

\[
\boxed{
\text{对每个递归可达的 }A>1\text{ overflow，构造保持 }A\text{ 的严格边或直接终端；}
\text{否则以独立外层秩支付 support reset。}
\tag{58}
\]

第 7--8 节的线性射线和模 \(240\) 分类仍是有用的局部结构，但初始 overflow 已有统一
下一边，故它们不再是独立递归余项。固定层格/Fourier 证书仍用于选择 alternate 和保存
overflow miss；它不再需要承担裸 G source 或单素数 clean 强制。下游定理及精确反例见
[overflow 固定 \(n\) 对偶图谱](type-I-overflow-determinant-fixed-n-dual-support-conflict.md)。

## 11. 聚焦复现

~~~bash
python3 reproductions/type_i_bottom_sink_scc_complete_excess_bundle.py
python3 reproductions/type_i_bottom_sink_scc_complete_excess_bundle.py --verify
~~~

结果文件为

~~~text
reproductions/type-i-bottom-sink-scc-complete-excess-bundle-results.json
~~~

对应 SHA-256 为

~~~text
1407e23353804cef2995aa0fd0b85b14abb8fc6f70b8ade60fdd49cdc268fc1a  reproductions/type_i_bottom_sink_scc_complete_excess_bundle.py
92458fe092c86a8db3ce1d693bd2234c87ab66094c1a80ad6d53cb3f4e8c583b  reproductions/type-i-bottom-sink-scc-complete-excess-bundle-results.json
~~~

该脚本只复核四个 bundle receipt、一个实际 F-source 路径、lcm 重叠、一个 overflow、
二进自环、Jacobi G 边界，以及一条线性 F overflow 的 clean-anchor/alternate-carrier
路径；它不重跑历史状态普查。全称结论由第 2--8 节的整数证明承担。
