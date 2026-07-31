---
kind: claim
claim_id: type-I-formal-linear-chart-p-transience-large-slab-anchor
title: 线性图表中 p 边的有限瞬态与 large-slab 三锚点压缩
statement: 对真正线性图表 p=a+s+asR，恒有 R<=p-2；formal Reach 保持 R，故任一 m=1 节点都不可能含 q=p 出边，所有 p 边只在 m>1 严格降层并且不属于周期。若 m=1 的单外部 slab 写成 X=q^e alpha、Y=beta、alpha beta|K、q不整除K 且 q^e>R/4，则 alpha只能为1、2、3，q不等于p；对全部 Q|M|Q alpha beta，存在降 R 的 M 当且仅当 M=Q 已经下降，扩大保留容量无补救作用。规范 q-peeling 路径到达锚点 {alpha,R-alpha}；除可能的第一步外，这一 peeling 段全部严格降 min，第一步只可能降 min、降 max 或成为唯一的 R=3 二进自环。锚点若非 Type I 汇点，当时的全部剩余超额集中在 R-alpha。三个 alpha 分支均有现有碰撞与容量吸收菜单全 miss 的线性例子，因此该压缩尚不是全称终端或合法 E4 递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-formal-full-excess-cycle-or-hit-reduction
  - type-I-formal-ranked-pruning-and-external-gap-selector
  - type-I-formal-external-slab-collision-absorption-rechart
topics:
  - type-I
  - formal-target-pair
  - linear-source
  - q-adic
  - external-slab
  - large-slab
  - cycle
  - well-founded-pruning
  - proof-boundary
sources:
  - claim: type-I-formal-full-excess-cycle-or-hit-reduction
    role: complete-formal-graph-and-cycle-interface
  - claim: type-I-formal-ranked-pruning-and-external-gap-selector
    role: exact-formal-transition
  - claim: type-I-formal-external-slab-collision-absorption-rechart
    role: large-slab-input-and-existing-terminal-menu
visibility: public
last_checked: '2026-07-31'
---

# 线性图表中 \(p\) 边的有限瞬态与 large-slab 三锚点压缩

## 1. 线性可实现性给出的 \(R<p\)

设核心素数的一张真正线性图表满足

\[
p=a_0+s_0+a_0s_0R,
\qquad a_0,s_0>0,
\qquad R\equiv3\pmod4,
\tag{1}
\]

并令

\[
4K=pR+1.
\tag{2}
\]

则

\[
R\le a_0s_0R=p-a_0-s_0\le p-2.
\]

所以

\[
\boxed{R\le p-2.}
\tag{3}
\]

formal transition 始终保持同一个 \(R\)：每个后继仍满足

\[
A'+B'=Rm'.
\tag{4}
\]

所以 (3) 沿固定线性图表的完整 formal Reach 自动保持，不是额外的归纳假设。

## 2. \(q=p\) 只可能是严格降层的有限瞬态

由 (2) 有 \(v_p(K)=0\)。任一 \(m=1\) 节点满足

\[
A+B=R<p,
\]

故 \(1\le A,B<p\)，从而 \(p\nmid AB\)。因此

\[
\boxed{
q=p\text{ 不可能标记任何 }m=1\text{ 出边，因而不属于底层周期或汇 SCC}.}
\tag{5}
\]

高层中的 \(p\) 边仍可精确描述。若被选坐标为 \(C=pC_0\)，另一坐标为 \(D\)，并写

\[
m=up+r_0,
\qquad1\le r_0<p,
\tag{6}
\]

则 formal shift 为 \(t=p-r_0\)。未正规化后继为

\[
\left(C_0,\ R(u+1)-C_0,\ u+1\right).
\tag{7}
\]

原节点互素给出 \((C_0,R)=1\)，所以正规公因子精确为

\[
g=(C_0,u+1).
\tag{8}
\]

于是

\[
\boxed{
m'=\frac{u+1}{g}
\le\left\lceil\frac mp\right\rceil<m.}
\tag{9}
\]

即使路径中夹杂其它同样降低 \(m\) 的边，从层 \(m_0>1\) 出发也至多出现

\[
\left\lceil\log_p m_0\right\rceil
\tag{10}
\]

条 \(p\)-标记边；\(m_0=1\) 时该数为零。这个结论只把 \(q=p\) 从最终周期障碍中
删除，不是完整路径的总边数界。formal 边本身仍未给出合法 equation target 或 E4
解提升。

### 2.1 \(R<p\) 不可跨图表继承

若离开线性可实现域，结论立即失败。取

\[
p=73,\qquad R=75,\qquad K=1369=37^2.
\]

完整 \(m=1\) 图中有真实三周期

\[
\{2,73\}
\xrightarrow{73}
\{1,74\}
\xrightarrow{2}
\{37,38\}
\xrightarrow{19}
\{2,73\}.
\tag{11}
\]

所以不能把 (5) 偷换成任意静态图表上的命题，也不能在 rechart 后不重新验证 \(R<p\)。

另一方面，真实线性图表的高层确实会出现 \(p\) 边。对

\[
p=73=18+1+18\cdot1\cdot3,
\qquad (R,K)=(3,55),
\]

有形式路径

\[
(1,11^7,6495724)
\xrightarrow{11}
(2,1771561,590521)
\xrightarrow{2}
(1,885782,295261)
\xrightarrow{73}
(1,12134,4045).
\tag{12}
\]

这说明 \(p\) 边不能从整个 Reach 删除，只能按 \(m\) 把它视为有限瞬态。

## 3. large-slab 的三锚点压缩

现在位于 \(m=1\) 层，并取单外部 slab

\[
X=Q\alpha,
\qquad Y=\beta,
\qquad Q=q^e,
\qquad e\ge1,
\tag{13}
\]

满足

\[
X+Y=R,\qquad
(X,Y)=1,\qquad
\alpha\beta\mid K,\qquad
q\nmid K,\qquad
Q>\frac R4.
\tag{14}
\]

因为 \(X<R\)，有

\[
1\le\alpha<\frac RQ<4,
\]

所以

\[
\boxed{\alpha\in\{1,2,3\}.}
\tag{15}
\]

式 (5) 还给出 \(q\ne p\)。又因 \(q\nmid\alpha\)，可依次取 \(q\)-边：

\[
S_j=
\left(\{q^j\alpha,R-q^j\alpha\},1\right),
\qquad j=e,e-1,\ldots,0.
\tag{16}
\]

每一步

\[
S_j\xrightarrow q S_{j-1}
\tag{17}
\]

都是完整超高图中的合法形式迁移，因为所选坐标仍有正 \(q\)-指数，而
\(v_q(K)=0\)。原始互素性给出 \((q\alpha,R)=1\)，所以各步无需额外正规约分。
最终到达

\[
\boxed{S_0=(\{\alpha,R-\alpha\},1),\qquad\alpha\in\{1,2,3\}.}
\tag{18}
\]

## 4. 扩大 \(M\) 不能补救 \(M=Q\) 的不下降

任取 \(d\mid\alpha\beta\)，并令 \(M=Qd\)。由于 \(q\nmid K\) 且
\(\alpha\beta\mid K\)，有 \((Q,d)=1\)，并且每个满足

\[
Q\mid M\mid Q\alpha\beta
\]

的 \(M\) 都唯一如此表示。先只比较规范代表。模 \(4Q\) 约化
\(R_{Qd}\) 的定义同余，得到

\[
\boxed{R_{Qd}=R_Q+4Q\kappa_d\ge R_Q}
\qquad(0\le\kappa_d<d).
\tag{19}
\]

更显式地，若

\[
c=\frac{pR_Q+1}{4Q},
\]

则 \(\kappa_d\) 是区间 \(0\le\kappa_d<d\) 中满足

\[
\kappa_d\equiv-cp^{-1}\pmod d
\]

的唯一整数。这里 \(p^{-1}\pmod d\) 存在，因为 \(d\mid K\) 且 \(p\nmid K\)。
因此不需要枚举整条容量梯：

\[
\boxed{
\exists\,Q\mid M\mid Q\alpha\beta:\ R_M<R
\iff R_Q<R.}
\tag{20}
\]

正向蕴含来自 \(R_Q\le R_M<R\)，反向则直接取 \(M=Q\)。这个容量支配结论实际上
不需要 large-slab 不等式；只要 \(M=Qd\)、\((Q,d)=1\) 且规范图表有定义就成立。

在当前 \(R<4Q\) 的 large-slab 中，还可以把各代表相对旧 \(R\) 写成闭式。定义
\(1\le\rho_d<Q\) 为

\[
p\rho_d\equiv\frac Kd\pmod Q.
\tag{21}
\]

规范容量图表的模数有精确公式

\[
\boxed{
R_{Qd}=
\begin{cases}
R-4d\rho_d,&4d\rho_d<R,\\
R+4d(Q-\rho_d),&4d\rho_d>R.
\end{cases}}
\tag{22}
\]

事实上，\(d\mid K\) 先给出 \(pR\equiv-1\pmod {4d}\)，而 (21) 说明

\[
p(R-4d\rho_d)\equiv-1\pmod {4Qd}.
\]

若该代表为正，它因 \(R<4Q\le4Qd\) 已在规范区间内；若为负，加上 \(4Qd\) 就得到
(22) 的第二行。等号 \(4d\rho_d=R\) 因 \(R\) 为奇数不可能发生。

再令 \(\rho_1\) 对应 \(d=1\)。模 \(Q\) 有

\[
d\rho_d\equiv\rho_1\pmod Q,
\]

故某个 \(j\ge0\) 满足

\[
d\rho_d=\rho_1+jQ.
\tag{23}
\]

由于 \(4Q>R\)，若 \(j\ge1\) 则不可能有 \(4d\rho_d<R\)；这也从旧 \(R\) 的
坐标再次验证了 (20)。所以若 \(R_Q>R\)，加入任意旧容量因子
\(d\mid\alpha\beta\) 都不能重新获得降 \(R\)。

## 5. peeling 段只有一次方向切换

因为

\[
q^{e-1}\alpha=\frac Xq<\frac R2,
\tag{24}
\]

所以除第一步外，(17) 的每一步都严格降低小坐标：

\[
\min S_{j-1}=q^{j-1}\alpha<q^j\alpha=\min S_j
\qquad(1\le j<e).
\tag{25}
\]

第一步也只有三种可能：

1. 若 \(X\le R/2\)，或 \(X/q<Y\)，则严格降低 \(\min\)；
2. 若 \(X>R/2\) 且 \(X/q>Y\)，则严格降低 \(\max\)；
3. 若 \(X/q=Y\)，由 \((X,Y)=1\) 得 \(Y=1,X=q\)，再由 \(R=q+1\) 为奇数得到
   唯一边界

   \[
   (R,q,e,\alpha,\beta)=(3,2,1,1,1),
   \tag{26}
   \]

   即已知的 \(\{1,2\}\) 二进自环。

所以除唯一自环外，这一 peeling 段先至多走一步 \(\max\) 边，随后只走 \(\min\)
边，并落到三个一侧锚点之一。但这是一条 formal 候选路径，不是 E4 已验真的跨状态递降。

这里的结论严格限定于 (16)--(17) 的这 \(e\) 步。到达锚点后，\(q\) 可能在
\(R-\alpha\) 中重新出现；例如 \((p,R,K)=(73,7,128)\) 有

\[
\{3,4\}\xrightarrow3\{1,6\}\xrightarrow3\{2,5\},
\]

第二条已经降低 \(\max\)，不属于原 peeling 段。

## 6. 锚点当时的全部超额位于另一侧

由 (14) 有 \(\alpha\mid K\)，且

\[
(\alpha,R-\alpha)=1.
\]

若

\[
\alpha(R-\alpha)\mid K,
\tag{27}
\]

则 (18) 是完整超高图的汇点，已有 cycle-or-hit 定理直接恢复同状态 Type I 证书。
若 (27) 失败，则任何满足

\[
v_\ell(\alpha(R-\alpha))>v_\ell(K)
\]

的剩余超额素数 \(\ell\) 必全部来自 \(R-\alpha\) 一侧。于是 large-slab 的锚点余项
被压缩成

\[
\boxed{
\alpha\in\{1,2,3\},\qquad
\text{overflow support at }S_0
\subseteq\operatorname{supp}(R-\alpha).}
\tag{28}
\]

式 (28) 只描述锚点当时所有可触发 formal 边的赋值超额；它不声称只有一个超额素数，
也不声称后续迁移后仍保持同侧集中。

还有一个自动的二进分流。因 \(p\equiv1\pmod8\)：

- 若 \(q=2\)，则 \(K\) 为奇数、\(R\equiv3\pmod8\)，且
  \(\alpha,\beta\) 都为奇数，所以 \(\alpha\in\{1,3\}\)；
- 若 \(q\) 为奇数，则 \(\alpha,\beta\) 奇偶相反，故 \(K\) 为偶数、
  \(R\equiv7\pmod8\)。

## 7. 三个系数分支都不会被现有菜单自动闭合

下面三例都来自真正线性图表，满足 (13)--(15)。对每个 \(T\mid R\)，两类 slab
碰撞均失败；对每个 \(Q\mid M\mid Q\alpha\beta\)，规范图表也都满足 \(R_M>R\)。

| \(\alpha\) | \((p,R,K)\) | \((Q,\beta)\) | 一张线性源 \((a_0,s_0)\) | 全部 \(R_M\) |
|---:|---:|---:|---:|---|
| 1 | \((241,7,422)\) | \((5,2)\) | \((30,1)\) | \(R_5=19,R_{10}=39\) |
| 2 | \((193,15,724)\) | \((7,1)\) | \((12,1)\) | \(R_7=19,R_{14}=47\) |
| 3 | \((337,23,1938)\) | \((7,2)\) | \((14,1)\) | \(R_7=27,R_{14}=55,R_{21}=83,R_{42}=167\) |

这些例子不是 Erdos--Straus 反例，也不声称对应 slab 必然属于某个指定缺陷见证的
源可达域。它们严格否定的是：仅凭 \(\alpha=1,2,3\) 和现有双碰撞/部分容量吸收条件，
就能逐分支推出直接终端或降 \(R\)。下一步必须利用 slab 的来源关系、锚点
\(R-\alpha\) 的额外因子结构，或构造改变 equation target 的合法状态边。

## 8. 聚焦复现

~~~bash
python3 reproductions/type_i_formal_linear_chart_slab_boundaries.py
python3 reproductions/type_i_formal_linear_chart_slab_boundaries.py --verify
~~~

结果文件：

~~~text
reproductions/type-i-formal-linear-chart-slab-boundaries-results.json
~~~
