---
kind: claim
claim_id: type-I-g-anchor-c3-adaptive-core19-v5-signed-marked-source-groupoid
title: v=5 C0/C1 的 signed marked-tail 非 native raw-source groupoid
statement: 设一个带方向的 m=1 raw leaf 有 z=epsilon*C*t、C=K/M，则 mu=-epsilon*K^(-1)*M*t^(-1)=-z^(-1) (mod R)。raw edge qg*z_next=z_prev 精确诱导 mu_next=(qg)*mu_prev；保持 tracked coordinate 的 frame morphism token 为 1，故在每个连通分量固定一个初始 mark 后，有限带 frame source graph 的 mark 存在当且仅当每个闭路的 token holonomy 为 1。v=5 的两条 declared primitive raw path 加一个 coordinate-frame swap 满足该条件，形成有限 nonnative signed marked-source groupoid；其两叶在 H_row/<mu1*mu0^(-1)> 中相同，且 eta(a)=a^10 (mod 191) 给出相对精确 19 阶方向 eta(mu1/mu0)=zeta^11。这只证明一个有限 raw-source relation 的非零 19-初等商；它不构成完整 Type II 参数纤维、整数 q-height、capacity 或递降边。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-c3-adaptive-core19-v5-dual-leaf-f19-control
  - type-I-ordered-raw-lineage-normalized-phase-rigidity
  - type-II-source-fiber-elementary-rank-qheight-injection
topics:
  - type-I
  - c3
  - core19
  - raw-source
  - coordinate-frame
  - signed-tail
  - source-groupoid
  - holonomy
  - q-primary
  - source-rank
  - analysis-evidence
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_c3_adaptive_core19_v5_signed_marked_source_groupoid.py
    role: frame-aware raw groupoid, q=19 relation, and integer-lift boundary
visibility: public
last_checked: '2026-08-07'
---

# v=5 signed marked-tail raw-source groupoid

这张卡回答一个窄而关键的问题：centered fixed-layer 的 no-go 以后，是否仍可对两条
raw 谱系建立一个不丢失相位的共同表示？答案是可以，但它只是有限、显式声明的
non-native raw-source presentation，不能直接冒充 Type II source fiber。

## 1. 带方向的最小 raw mark

设

\[
4K=pR+1,\qquad z=\epsilon Ct,\qquad C=K/M,\qquad \epsilon\in\{\pm1\},
\tag{1}
\]

其中 \(z\) 是一条 \(m=1\) raw leaf 上被跟踪的物理坐标，\(t\) 是其正尾。
定义

\[
\boxed{
\mu(M,t,\epsilon):=-\epsilon K^{-1}Mt^{-1}\pmod R.
}
\tag{2}
\]

由于 \(K=MC\)，且 \(\epsilon^{-1}=\epsilon\)，有

\[
\mu=-\epsilon C^{-1}t^{-1}=-z^{-1}\pmod R.
\tag{3}
\]

所以它无损保留了 physical coordinate 的符号。只保留旧的 \((M,t)\) 不够：
\(z=Ct\) 与 \(z=-Ct\) 有相同 \((M,t)\)，却有相反的 phase。

若一条 raw edge 的实际 gcd reduction 为 \(g\)，并且被追踪坐标满足

\[
qg z_{\mathrm{next}}=z_{\mathrm{prev}}\pmod R,
\tag{4}
\]

则反演 (4) 得到严格的传播律

\[
\boxed{\mu_{\mathrm{next}}=(qg)\mu_{\mathrm{prev}}\pmod R.}
\tag{5}
\]

若一个 frame morphism 同时运输 tracked-coordinate index，它不是 raw division，
token 定义为 \(1\)。因此给定带 frame 的有限 source multigraph，在每个连通分量选定
一个初始 mark 后，mark 可一致传播的充要条件为每个有向闭路满足

\[
\prod_{e\text{ on loop}}\operatorname{token}(e)^{\pm1}=1\pmod R.
\tag{6}
\]

这只是 token 1-cocycle 的精确 holonomy 条件。它授权 phase merge，不授权物理
row 或 Type II parameter merge。

## 2. v=5 的 frame diamond 与两条 branch

在 v=5，令 \(S\) 为 universal \(p\)-source，\(A=(1,R-1,1)\)，并显式写

\[
A^\sigma=(R-1,1,1),\qquad
Q=(1042059994246,4168239976985,1).
\]

universal \(p\)-edge 给 \(S\to A\)。随后 C0 路径先作 frame swap
\(A\to A^\sigma\)，再在左侧取 \(q=5\)；C1 路径在原 frame 的右侧取
\(q=5\)。它们到达同一个 \(Q\)，但不是同一 ordered raw edge。唯一有意引入的
diamond 有

\[
5\cdot1\cdot5^{-1}=1\pmod R,
\tag{7}
\]

故满足 (6)。初始到共同点的 marks 为

\[
\mu_S=390772497842,\qquad
\mu_A=R-1,\qquad
\mu_Q=R-5.
\tag{8}
\]

之后所有 declared edge 的 \(g=1\)。两个 branch token word 分别是

\[
\begin{aligned}
w_0&=(7,2,2,2,2,72106829959,13,2,2),\\
w_1&=(92660501,5,10798549169,5,54845262851),
\end{aligned}
\tag{9}
\]

它们在 \(R\) 中的积为

\[
\gamma_0=3126179982736,\qquad
\gamma_1=4332775765550.
\tag{10}
\]

两条 signed tail 及终点 mark 是

\[
\begin{array}{c|c|c}
\text{leaf}&(C,M,t,\epsilon)&\mu\\ \hline
C_0&(1202376916438,1302574992811,1,-1)&13\\
C_1&(19,82430847541333694617222,1,+1)&4387621028405.
\end{array}
\tag{11}
\]

复现器逐边回放 primitive raw receipt，并验证

\[
\mu_Q\gamma_0=13,\qquad
\mu_Q\gamma_1=4387621028405\pmod R.
\tag{12}
\]

因此 (8)--(12) 在声明的有限 universe 内闭合。它不反驳
[centered mixed-source fiber no-go](type-I-g-anchor-c3-adaptive-core19-v5-centered-mixed-source-fiber-no-go.md)：
这里刻意不要求 marks 落在 \(\mathcal C_R(K)\) 的 centered layer。

## 3. 抽象 q=19 relation 与严格边界

写

\[
u=\mu_1\mu_0^{-1}=5147016975629.
\tag{13}
\]

令 \(H_{\rm row}=\langle\mu_0,\mu_1\rangle\subset U(R)\)，并令
\(\phi:\mathbb Z^2\to H_{\rm row}\) 将 \(e_i\) 映到 \(\mu_i\)。最小的
abstract common-fiber quotient 是

\[
\pi_{\rm rel}:H_{\rm row}\longrightarrow H_{\rm row}/\langle u\rangle.
\tag{14}
\]

它使两叶相同，且 \(e_1-e_0\in\ker(\pi_{\rm rel}\phi)\) 的像为 \(u\)。取
\(\eta(a)=a^{10}\pmod{191}\)、\(\zeta=150\)，有

\[
\eta(\mu_0)=\zeta^{16},\qquad
\eta(\mu_1)=\zeta^8,\qquad
\eta(u)=\zeta^{11}.
\tag{15}
\]

所以如果 \(A_\pi=\phi(\ker(\pi_{\rm rel}\phi))\)，则

\[
u\in A_\pi,\qquad
u\notin A_\pi^{19},\qquad
\boxed{A_\pi/A_\pi^{19}\ne0.}
\tag{16}
\]

这是一个精确的有限 Abelian/SNF 型 \(19\)-初等方向，而不是 Type II capacity。
目前没有\(D_*,A\)、\(b_i\)、完整 parameter fiber、CRT/prefix 或
`demand_to_slot`。直接采用已有 E2 余数也不行：

\[
\begin{array}{c|c|c|c}
&r=M\bmod p&4r<p&v_{19}(p+4r)\\ \hline
C_0&100198076370&\text{是}&0\\
C_1&996707180734&\text{否}&2.
\end{array}
\tag{17}
\]

它们无法同时提供 Type II 所需的 range 与 \(19\)-height。这只排除当前自然整数
coordinate，未排除全新的 integer source map。

## 4. 可检验的合同状态

本卡的结果必须保持

```text
certificate_type = nonnative_signed_marked_source_tree_v1
source_universe = two declared raw paths' prefix vertices + explicit frame arrow
vertex_mark = (ordered tuple, frame id, tracked index, z, M, t, epsilon, mu)
raw_edge = (source, selected index, q, gcd reduction, destination, token=q*g)
frame_edge = (source frame, destination frame, tracked-index transport, token=1)
merge_rule = no implicit physical merges; every declared merge needs holonomy
status = analysis_evidence_only
```

将它升级为 capacity 或 selector edge 前，必须独立给出完整 transition/source universe、
occurrence projection 与有限 parameter fiber、保留 (15) 的整数
\((\mu,\epsilon,t,\text{digest})\mapsto(D_*,A,b)\) map、physical slots、E4/E5 和
terminal-first clearance。v=5 本身还有 \((m,d)=(3,11)\) terminal，且 source F
witness 不是 canonical Fourier input；两项均禁止当前控制成为 selector edge。

窄复现：

    python3 reproductions/type_i_c3_adaptive_core19_v5_signed_marked_source_groupoid.py --verify
