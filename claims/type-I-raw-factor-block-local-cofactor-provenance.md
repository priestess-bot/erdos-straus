---
kind: claim
claim_id: type-I-raw-factor-block-local-cofactor-provenance
title: 单首标签因子轨道的局部 raw-to-cofactor provenance
statement: 设同一 Type I raw 图表的 canonical anchor 为 (1,R-1,1)。若首素标签 lambda 整除 R-1 且 v_lambda(R-1)>v_lambda(K)，写 b=(R-1)/lambda；若 H 整除 S=R-b，L=S/H，且对每个 ell|L 有 v_ell(H)>=v_ell(K)，则 lambda;Fac(L) 是一条 actual primitive raw receipt，终点为 (H,R-H,1)。若再有 H|N_A=p+4DA、gcd(H,4D)=1、A|D、D/A 平方自由和 4AD<p，则该 transcript 与因子整除共同构成 state-local raw-to-cofactor receipt。它不自动给 target-odd、slot、capacity 或 selector edge。在 v=5、D=6303 的完整八个 A 候选格中，三个合法首标签 lambda=5,5623,92660501 与全部 N_A 的 24 个交集只有 (lambda,A,gcd(S_lambda,N_A))=(5,11,7) 非平凡；该唯一 H=7 正控制有 actual receipt。特别地 A=573 的四个 C38 同 phase candidate 全部不能由此一首边+单侧 factor-block 拓扑到达。q=137 family 在 w=7666 有实际 endpoint H=19*53*3671，但同点 H 不整除 N_573；沿该 family，U=53*3671|Q(w) 与 U|N_573(w) 的两个 CRT 类不相交。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-marked-raw-peeling-calculus
  - type-I-g-anchor-c3-adaptive-core19-q137-first-entry-family
  - type-I-g-anchor-c3-adaptive-core19-v5-dual-leaf-f19-control
  - type-I-g-anchor-c3-adaptive-core19-v5-d6303-complete-fiber-boundary
  - type-I-g-anchor-c3-adaptive-core19-v5-phase-provenance-boundary
topics:
  - type-I
  - raw-source
  - factor-block
  - factor-provenance
  - candidate-fiber
  - c3
  - core19
  - q137
  - q19
  - CRT
  - terminal-first
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_raw_factor_block_local_cofactor_provenance.py
    role: local factor-orbit replays, v=5 complete first-edge incidence table, and q=137 CRT controls
visibility: public
last_checked: '2026-08-08'
---

# 单首标签因子轨道的局部 raw-to-cofactor provenance

这张卡给出一个严格的、可重放的 raw-to-cofactor 最小接口。它把 raw transcript 的
实际终点 \(H\) 与同一素数的 Type II candidate record 中的整除式 \(H\mid N_A\)
绑在一起。这个接口比 character phase 强，因为 \(H\) 是逐边 raw word 保留的整数；
但它仍只是局部 incidence，不能替代 target residue、独立 slot 或递归下降。

## 1. 单首标签因子轨道引理

固定一个同一图表

\[
4K=pR+1
\]

的 canonical raw anchor \((1,R-1,1)\)。令 \(\lambda\) 是素数，满足

\[
\lambda\mid R-1,
\qquad
v_\lambda(R-1)>v_\lambda(K),
\qquad
b=\frac{R-1}{\lambda},
\qquad
S=R-b.
\tag{1}
\]

再取正整数 \(H,L\)，使

\[
S=HL,
\qquad
v_\ell(H)\ge v_\ell(K)\quad\text{对每个素数 }\ell\mid L.
\tag{2}
\]

**引理。** 在 (1)--(2) 下，

\[
(1,R-1,1)
\xrightarrow{(1,\lambda)}
(b,S,1)
\xRightarrow{\operatorname{Fac}(L)}
(H,R-H,1)
\tag{3}
\]

是一条 actual primitive raw receipt。首条 \(L\)-边选择第二坐标；此后每次选择
raw step 写在第一坐标的商。所有边的 gcd reduction 都为 \(1\)。

**证明。** 首边的严格容量正是 (1)。因为
\((R-1,R)=1\)，有 \((b,R)=(S,R)=1\)。若某一步当前被选坐标为
\(H L'\)，其中 \(\ell\mid L'\)，则其 \(\ell\)-高度至少为
\(v_\ell(H)+1>v_\ell(K)\)，故严格容量成立。源节点的另一坐标为
\(R-HL'\)；因 \(\ell\mid HL'\) 而 \(\ell\nmid R\)，它不被 \(\ell\) 整除，
所以 unit condition 成立。raw step 的直接算术是

\[
(R-HL')+\!R(\ell-1)=\ell\left(R-\frac{HL'}{\ell}\right),
\]

因而每步把 \(HL'\) 替换为 \(HL'/\ell\)，保持层 \(m=1\)。两个坐标互素，因为它们
的和为 \(R\) 且被选坐标与 \(R\) 互素，所以不会产生 gcd reduction。逐个剥离
\(\operatorname{Fac}(L)\) 即得 (3)。证毕。

这也给出一个 order-independent 的局部轨道：对每个 \(E\mid L\)，选择 \(L/E\)
的任意素因子顺序都到达

\[
N_R(HE)=(HE,R-HE,1).
\tag{4}
\]

## 2. 从 raw endpoint 到 candidate cofactor

固定 \(D,A\)，令

\[
N_A=p+4DA.
\tag{5}
\]

若 (3) 的 endpoint 还满足

\[
A\mid D,\qquad D/A\text{ 平方自由},\qquad 4AD<p,\qquad
(H,4D)=1,\qquad H\mid N_A,
\tag{6}
\]

则定义

\[
\mathcal I=(p,R,K;\ \text{raw digest},\lambda,b,H,L;\
D,A,N_A,H\mid N_A).
\tag{7}
\]

为一个 **state-local raw-to-cofactor receipt**。其中 raw digest 是 (3) 的逐边
ordered transcript；它防止把相同的 phase 或未标记 endpoint 当成同一 occurrence。

(7) 只证明同一个 fixed state 内的两件事实：raw 的确到达 \(H\)，且该整数的确整除
该 state 的 candidate record。它没有给出

\[
H\equiv-1\pmod {4D},
\qquad
\text{occurrence}\longmapsto\text{typed request},
\qquad
\text{request}\hookrightarrow\text{physical slots}.
\tag{8}
\]

因此 (7) 不是 Type II terminal，也不是 capacity 注入或 selector edge。

## 3. v=5 的完整一首边分类

取 v=5 的实际 core-19 state：

\[
\begin{aligned}
p&=1202376916441,\\
R&=5210299971231,\\
K&=2\cdot19^2\cdot193\cdot5351\cdot66383\cdot31641497801,
\end{aligned}
\tag{9}
\]

并固定 \(D=6303\)。有

\[
R-1=2\cdot5\cdot5623\cdot92660501.
\tag{10}
\]

\(\lambda=2\) 不可用，因为
\(v_2(R-1)=v_2(K)=1\)。其余全部合法的首标签及相应 \(S_\lambda\) 是

\[
\begin{array}{c|r|l}
\lambda&S_\lambda=R-(R-1)/\lambda&\text{因式分解}\\ \hline
5&4168239976985&5\cdot7\cdot119092570771\\
5623&5209373366221&41\cdot101\cdot127\cdot1423\cdot6961\\
92660501&5210299915001&1213\cdot7603\cdot564959.
\end{array}
\tag{11}
\]

对所有八个 \(A\mid6303\)，完整地计算

\[
\gcd(S_\lambda,N_A),
\qquad N_A=p+4\cdot6303A,
\tag{12}
\]

得到 24 个格中唯一的非平凡值

\[
\boxed{(\lambda,A,\gcd(S_\lambda,N_A))=(5,11,7).}
\tag{13}
\]

它给出真正的正控制：

\[
\begin{aligned}
L&=S_5/7=595462853855=5\cdot119092570771,\\
N_{11}&=1202377193773=7^2\cdot347\cdot70715591.
\end{aligned}
\tag{14}
\]

两个 \(L\) 标签均是 \(K R\)-unit。接在既有的 universal \((0,p)\) raw edge 后，
(3) 给出实际 word

\[
(0,p),(1,5),(1,5),(0,119092570771)
\tag{15}
\]

到达 \((7,R-7,1)\)，且 \(7\mid N_{11}\)。所以 (15) 是一个同状态的非平凡
raw-to-cofactor receipt。

另一方面，\(A=573\) 的 record 是

\[
N_{573}=1202391362917
=17\cdot19^3\cdot53^2\cdot3671.
\tag{16}
\]

其 C38 phase 对应的四个同标签候选为

\[
19,\quad1014049,\quad3307571,\quad1334507617.
\tag{17}
\]

对 (11) 的每一个 \(S_\lambda\) 和 (17) 的每一个数，gcd 均为 \(1\)。因此
这四个 candidate cofactor 都不能通过当前的“一首边 + 单侧 factor-block”拓扑取得
raw endpoint provenance。这个结论只排除该精确定义的局部拓扑，不排除更长或混侧的
raw word。

还可从三条现有 physical occurrence 得到无歧义但很弱的 resource incidence：

\[
\gcd(p-3,N_{573})=\gcd(19,N_{573})=\gcd(38,N_{573})=19.
\tag{18}
\]

它说明三条 occurrence 都碰到同一 shared-\(19\) resource；不能把这一个 gcd
自动拆成三份 source rank、prefix request 或 physical slot。

v=5 已有 \((m,d)=(3,11)\) 的直接 Type II terminal。因此 (13)--(18) 都只能作为
terminal-preempted interface evidence。

## 4. q=137 的正控制与 CRT 不相容

q=137 actual raw family 给

\[
\begin{aligned}
p(w)&=193+772716168w,\\
Q(w)&=43+174947136w,\\
R-b&=19Q(w).
\end{aligned}
\tag{19}
\]

对每个 \(w\ge1\) 的 prime parameter，既有 \(137;\operatorname{Fac}(Q)\) transcript
本身已经到达 \(H=19\)。又 \(19\mid N_{573}(w)\)、\(D/573=11\) 平方自由且
\(4\cdot6303\cdot573<p(w)\)，所以这是一条全族的 local \(H=19\) incidence。
它只使用一个 \(19\)-层，既不是 target factor，也不能提供 \(U\) 的 q-free
provenance。

令

\[
U=53\cdot3671=194563,
\qquad
H_1=19U=3696697.
\tag{20}
\]

在 \(w=7666\)，有一个实际素数控制

\[
\begin{aligned}
p&=5923642144081,\\
Q&=1341144744619=53\cdot113\cdot3671\cdot61001=U(113\cdot61001).
\end{aligned}
\tag{21}
\]

接在既有 universal \((0,p)\) edge 后，只剥离 \(L=113\cdot61001\)，(3) 给出
actual word

\[
(0,p),(1,137),(1,113),(0,61001)
\tag{22}
\]

到 \(H_1\)。这说明 endpoint 的完整整数因子确实能提供超出 character phase 的
raw provenance。

但令同一素数的 \(D=6303,A=573\) record 为

\[
N_{573}(w)=14446669+772716168w.
\tag{23}
\]

在 (21) 的点，

\[
N_{573}(7666)\equiv2777211\not\equiv0\pmod {H_1}.
\tag{24}
\]

更一般地，\(U\) 与两条仿射步长都互素，精确 CRT 类是

\[
\begin{aligned}
U\mid Q(w)&\Longleftrightarrow w\equiv7666\pmod U,\\
U\mid N_{573}(w)&\Longleftrightarrow w\equiv92963\pmod U.
\end{aligned}
\tag{25}
\]

它们不相交。并且

\[
Q(w)\equiv5\pmod {19},
\qquad
N_{573}(w)\equiv171\pmod {19^2},
\tag{26}
\]

故 \(R-b=19Q(w)\) 与 \(N_{573}(w)\) 都不能承载
\(19^3U\)。所以这个 actual q=137 orbit 虽能精确保留 \(H_1\)，却不能在同一参数点
成为 \(A=573\) target record 的 factor receipt。

q=137 family 和 v=5 也不是同一个 state：v=5 满足
\((R-1)\equiv43\pmod {137}\)，没有 q=137 的首 raw edge。不能把 (22) 跨素数
移植为 v=5 的 slot 或 candidate label。

## 5. 范围

本卡新增的是：

1. 一个可重放的 raw endpoint \(H\) 到 candidate divisibility \(H\mid N_A\) 的局部接口；
2. v=5 固定 \(D=6303\) 的完整一首边 incidence 分类及唯一 \(H=7\) 正控制；
3. q=137 中实际保留 \(19U\) 与 candidate-record CRT 对齐失败的精确边界。

它没有构造 raw occurrence 到 \((D,A,b,H,\text{slot})\) 的全 functor，也没有给出
shared-\(q\) ledger、demand-to-slot 单射、E1--E5 或全局良基势。特别是相同
candidate record 内的 nested cofactors 仍不能被重复收费为独立 capacity。

窄复现：

~~~
python3 reproductions/type_i_raw_factor_block_local_cofactor_provenance.py --verify
~~~
