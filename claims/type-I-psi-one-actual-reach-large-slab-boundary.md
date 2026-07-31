---
kind: claim
claim_id: type-I-psi-one-actual-reach-large-slab-boundary
title: Psi 一层 F 状态源见证锚定的完整 formal Reach large-slab 边界
statement: 在哈希冻结的483个Psi_0=1有限指数F状态和1615条正见证上，源见证锚定的完整未剪枝formal Reach共有520559个节点、1874407条带标签边，并产生1412个large-slab记录，覆盖282态；双秩范围只看到其中638个。两类slab碰撞各命中2个，完整formal Reach新增774个slab没有新增碰撞；加入节点external-affine终端、三锚点external-affine终端和规范R_Q<R吸收后仍有566个strong miss，覆盖198态且alpha=1,2,3各有实例。只按碰撞或容量吸收分类时有581个local good和831个local miss；后者中761个存在至少一条formal路径到达good single-slab，仍有70个slab记录、45态在完整formal后继图中没有该候选。最小后继残余为(p,R)=(5596369,35)的{3,32}。这些是有限候选生成边界；formal边没有E4，任何miss都不是Erdos-Straus反例。
claim_status: computationally_reproduced
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-I-psi-one-source-word-large-slab-constraint
  - type-I-formal-natural-tail-integrality-rigidity
  - type-I-formal-external-slab-collision-absorption-rechart
  - type-I-formal-full-excess-cycle-or-hit-reduction
  - type-I-psi-one-affine-boundary-terminal-profile
topics:
  - type-I
  - F-state
  - psi-one
  - formal-reach
  - external-slab
  - large-slab
  - q-adic
  - capacity
  - computation
  - proof-boundary
sources:
  - claim: type-I-psi-one-source-word-large-slab-constraint
    role: source-path-necessary-conditions
  - claim: type-I-formal-natural-tail-integrality-rigidity
    role: natural-lift-obstruction
  - claim: type-I-formal-external-slab-collision-absorption-rechart
    role: collision-and-capacity-menu
  - claim: type-I-formal-full-excess-cycle-or-hit-reduction
    role: finite-formal-closure-interface
  - claim: type-I-psi-one-affine-boundary-terminal-profile
    role: affine-terminal-menu
visibility: public
last_checked: '2026-07-31'
---

# Psi 一层 F 状态源见证锚定的完整 formal Reach large-slab 边界

## 1. 审计对象与判据

输入固定为完整 \(\Psi_0=1\) 终端审计中的

\[
483\text{ 个有限指数 F 状态},
\qquad1615\text{ 条正见证}.
\]

对每态从全部正见证重建未剪枝 `raw_transitions` 闭包。这里“完整”有明确的有限性
含义。若源见证最大层为 \(m_{\max}\)，则每条 \(m>1\) 边严格降层、\(m=1\) 边保持
层数；每层无序正坐标对至多有 \(\lfloor(Rm-1)/2\rfloor\) 个，所以整个闭包包含于

\[
\sum_{m=1}^{m_{\max}}\left\lfloor\frac{Rm-1}{2}\right\rfloor
\]

个候选节点。程序对两个坐标和每个满足
\(v_q(\text{coordinate})>v_q(K)\) 的素数都调用 `raw_transitions`，直到 frontier 为空，
没有深度、秩或节点数截断。因此“完整”只指相对于这些冻结源见证和这套 formal 边定义
的闭包，不代表已经验证了真实状态边。节点总数按 483 个逐态图求和；边数是带标签的
transition occurrence 总数。

节点
\((A,B,m)\) 只有在 \(m=1\) 且可定向为

\[
A=Q\alpha,
\qquad B=\beta,
\qquad Q=q^e,
\qquad q\nmid K,
\qquad \alpha\beta\mid K
\tag{1}
\]

时才记为 single-external slab；再加 \(4Q>R\) 才记为 large-slab。由已证明的
large-slab 压缩，后者自动满足

\[
\alpha\in\{1,2,3\}.
\tag{2}
\]

本卡使用两组互补分类。

第一组 `strong miss` 菜单逐个检查：

1. \(T\mid R\) 上的 Type II 碰撞 \(4AB\mid p+T\)；
2. \(T\mid R\) 上的跨图表中心 Type I 碰撞 \(4AB\mid pT+1\)；
3. 当前节点坐标 \(A,B\) 的 external-affine gap 终端：只枚举坐标因子
   \(h\mid A\) 或 \(h\mid B\)，并要求 \(3\le h\le p-2\)、\(h\equiv3\pmod4\) 且
   \(h/(h,K)>1\)，再完整检查该 gap 的 Type I/II 平方除子证书；
4. peeling 锚点 \(\{\alpha,R-\alpha\}\) 的同一 external-affine 菜单；
5. 规范容量图表 \(R_Q<R\)。

前四项全空且第五项不下降，才称为本卡的 `strong miss`。

第二组用于研究后继释放。`basic good single-slab` 只要求两类碰撞之一成立，或
\(R_Q<R\)；它不要求 (2)，所以 small-slab 也可成为后继出口。对每态完整图的全部
good single-slab 作反向多源搜索，从而一次性判断每个起始 large-slab 是否存在至少一条
formal 路径到达这种候选。这里的 formal 路径本身仍不满足 E4。

## 2. 完整 formal Reach 严格大于双秩范围

源见证锚定的完整 formal 审计得到

\[
\boxed{
520559\text{ 个节点},
\qquad1874407\text{ 条边}.
}
\tag{3}
\]

其中有

\[
\boxed{1412\text{ 个 large-slab，覆盖 }282\text{ 态}.}
\tag{4}
\]

此前 \((m,\min(A,B))\) 与 \((m,\max(A,B))\) 双秩的 accepted 闭包加一步 rejected
lookahead 只包含

\[
638\text{ 个 large-slab，覆盖 }256\text{ 态}.
\tag{5}
\]

完整 formal Reach 因而新增 774 个 slab，并新增 26 个“双秩范围完全看不到 slab”的状态。
所以双秩闭包足以生成很多直接终端，却不是 slab 来源的完备替代品。

三个系数分支的分布为

| 范围 | \(\alpha=1\) | \(\alpha=2\) | \(\alpha=3\) | 合计 |
|---|---:|---:|---:|---:|
| 完整 formal Reach | 899 | 368 | 145 | 1412 |
| 双秩范围 | 378 | 202 | 58 | 638 |

外部指数以一层为主，但并非全是一层：\(e=1\) 有 1349 个，\(e>1\) 有 63 个，最大
\(e=13\)；其中 \(q=2\) 有 36 个。

## 3. 现有局部菜单的精确覆盖

两类 slab 碰撞极少：

| 通道 | 命中数 | 精确记录 |
|---|---:|---|
| Type II 碰撞 | 2 | \((178790089,111,\{10,101\},T=111)\)、\((508542169,103,\{2,101\},T=103)\) |
| 跨图表 Type I 碰撞 | 2 | \((266080369,63,\{1,62\},T=7)\)、\((452110129,63,\{1,62\},T=7)\) |

完整 formal Reach 新增的 774 个 slab 没有增加一个碰撞命中。当前节点
external-affine 菜单命中 86 个 slab 记录，锚点菜单命中 397 个记录，两者重叠 21 个
记录。两碰撞及两个 external-affine 菜单全部失败的有 948 个记录；全体 1412 个记录中
共有 581 个规范容量吸收，其中 382 个落在这 948 个预吸收 miss 内，故加入吸收后仍有

\[
\boxed{566\text{ 个 strong miss，覆盖 }198\text{ 态}.}
\tag{6}
\]

其 \(\alpha\) 分布为

\[
420,\quad126,\quad20.
\tag{7}
\]

即三个锚点分支各自都有源见证锚定的 formal strong-miss 实例，不再只是人为构造的
线性局部例子。
双秩范围内部也仍有 247 个 strong miss、150 态，分布为 \(172,67,8\)。

完整 formal Reach 中按 \(p\) 最小的 strong miss 是

\[
(p,R,K)=(214729,391,20989760),
\]

\[
\{A,B\}=\{5,386\},
\qquad(Q,\alpha,\beta)=(193,2,5),
\qquad R_Q=731>391.
\tag{8}
\]

它不在双秩范围。双秩范围内最小者是

\[
(p,R)=(5596369,35),
\qquad\{A,B\}=\{3,32\},
\qquad(Q,\alpha,\beta)=(32,1,3),
\qquad R_Q=79.
\tag{9}
\]

\(\alpha=3\) 的最小双秩 strong miss 为

\[
(p,R)=(24738289,455),
\qquad\{A,B\}=\{2,453\},
\qquad(Q,\alpha,\beta)=(151,3,2),
\qquad R_Q=523.
\tag{10}
\]

从 (10) 出发的完整后继图有 20 个节点、43 条边，其中只有三张 single-external slab：

\[
(Q,\alpha,\beta,R_Q)
=(227,2,1,531),\ (151,3,2,523),\ (449,1,6,1563).
\]

三张的两类碰撞和容量下降全部失败。它是 (13) 中唯一的 \(\alpha=3\) 完整后继残余，
所以后继搜索也没有消去第三个锚点分支。

## 4. 沿完整 formal 后继图的候选可达与 70 个残余

若暂时只把两碰撞或 \(R_Q<R\) 称为 `basic good`，则 1412 个起始 large-slab 中

\[
581\text{ local good},
\qquad831\text{ local miss}.
\tag{11}
\]

四个碰撞节点在本样本中都已经包含于 581 个容量下降节点，所以碰撞没有增加并集大小。
对每个 local miss 询问是否存在至少一条完整 formal 路径到达 good single-slab，得到

\[
\boxed{
761\text{ 个存在候选路径},
\qquad70\text{ 个没有该候选}.
}
\tag{12}
\]

70 个残余分属 45 态，按起始 \(\alpha=1,2,3\) 的分布为

\[
53,\quad16,\quad1.
\tag{13}
\]

最小例正是 (9)。它来自线性源 \((a,s)=(331,483)\) 和唯一正见证
\((1,2,-1,0)\)，有精确路径

\[
(107,18723,538)
\xrightarrow{79}
(8,237,7)
\xrightarrow{2,\ g=4}
(1,34,1)
\xrightarrow{17}
(2,33,1)
\xrightarrow{11}
(3,32,1).
\tag{14}
\]

从终点 (9) 出发的完整后继图有 12 个节点、26 条边，唯一 single-external slab 就是
它自身，且不是 basic good。路径标签乘积为 29546，但包含正规公因子的路径字乘积为

\[
79\cdot(2\cdot4)\cdot17\cdot11=118184.
\tag{15}
\]

source-word 定理从首条强制边后的 \((8,237,7)\) 开始计字，因此相应后缀的纯标签乘积
是 \(2\cdot17\cdot11=374\)，而

\[
\Theta=(2\cdot4)\cdot17\cdot11=1496.
\]

取 \(U_1=237\)、\(\varepsilon=1\)、\(u=1361\)，可逐式核验

\[
1496\cdot32=237+35\cdot1361,
\qquad
1496\cdot3=-237+35(1496-1361).
\]

所以 118184 是含首边的全路径正规乘积，1496 才是该定理中的 \(\Theta\)；二者都验证了
纯标签乘积不足以恢复路径同余。

## 5. 一个源见证锚定的 formal \(\alpha=3\) 四周期

取

\[
(p,R,K)=(212973049,215,11447301384),
\]

\[
K=2^3\cdot3^2\cdot293\cdot431\cdot1259,
\qquad(a,s)=(2,494137).
\]

正见证 \((-1,-2,-1,-1,2)\) 给出

\[
(1585081,2273094,17945)
\xrightarrow{1259}
(1259,1966,15)
\xrightarrow{983}
(2,213,1).
\tag{16}
\]

末节点是 \((Q,\alpha,\beta)=(71,3,2)\) 的 strong miss，且进入确定性四周期

\[
\{2,213\}
\xrightarrow{71}\{3,212\}
\xrightarrow{53}\{4,211\}
\xrightarrow{211}\{1,214\}
\xrightarrow{107}\{2,213\}.
\tag{17}
\]

这个局部 strong miss 随后仍会遇到 basic good：\(\{3,212\}\) 可写成
\((Q,\alpha,\beta)=(53,4,3)\)，有 \(R_{53}=171<215\)；\(\{1,214\}\) 可写成
\((107,2,1)\)，有 \(R_{107}=55<215\)。所以 (17) 支持研究“peeling 后的有界组合再
吸收”，却也显示仅证明锚点本身终端并非必要。

该状态原本另有 gap 431 的直接 Type I 证书。因此 (17) 既不是原猜想反例，也不是
无解状态；它只反驳“源见证关系会使当前 large-slab/锚点菜单逐点自动闭合”。

## 6. 自然尾与自然端点仍未给出新出口

对每个 slab 取好尾首分母 \(x=K/\beta\)，自然候选 gap 为

\[
h=4x-p=\frac{pQ\alpha+1}{\beta}.
\tag{18}
\]

完整 1412 个 slab 中只有 14 个 \(h\) 落入合法 gap 范围，双秩 638 个中有 11 个；
对这些 gap 完整枚举首分母平方除子后，Type I/II 命中均为零。这是有限负结果，不是
普遍不可能定理。真正普遍的结论是：固定 \(pK\) 与自然好尾后，另一尾在非汇点上不是
整数，见[自然双尾整数性刚性](type-I-formal-natural-tail-integrality-rigidity.md)。

## 7. 结论边界与下一接口

本审计改变了下一步的优先级：

1. 继续增加 \(\operatorname{Div}(R)\) 上的两类 slab 碰撞没有数据支持；完整 formal Reach
   新增 774 个 slab 而零新增碰撞。
2. 单纯加入来源同余也不能关闭三个 \(\alpha\) 分支；每个分支都有满足这些必要条件的
   strong-miss 记录。
3. 761/831 的 formal 后继候选可达说明“peeling 后寻找 small/large single-slab 容量
   吸收”值得保留，但它仍缺每条路径的 E4。
4. 70 个完整后继残余迫使选择器再加入 slab 之外的高层仿射量、多个节点的有界组合，
   或真正改变根尾数据的 marked lift。

例如原四个状态局部残余中的

\[
(p,R)=(78268369,8895),
\qquad\{A,B\}=\{652,8243\}
\]

在 slab 与锚点菜单中全部失败、\(R_{8243}=10395>R\)，但源高层节点
\((326,1787569,201)\) 的

\[
|326-R|=8569=19\cdot451
\]

给出 gap 19 的直接 Type I 终端。下一选择器因此应把“高层仿射边界量”与
“single-slab 容量”放在同一个来源路径证书中，而不是只在 \(m=1\) 锚点上扩菜单。

所有 formal 边仍标记为 `analysis_evidence_not_verified_edge`。孤立的 \(R_Q<R\) 可在现有
不可逆 ABSORB 阶段中作为合法容量下降，但一条在它之前的 formal 路径仍没有 E4。因此
(12) 的 761 个候选可达不能计作合法递降；同理，70 个残余也不能计作
Erdős--Straus 反例。

## 8. 聚焦复现

```bash
python3 reproductions/type_i_psi_one_large_slab_reach_boundary.py
python3 reproductions/type_i_psi_one_large_slab_reach_boundary.py --verify
```

结果文件：

```text
reproductions/type-i-psi-one-large-slab-reach-boundary-results.json
```

输入和 formal transition 实现都由脚本中的固定 SHA-256 校验；结果只保存汇总、碰撞
正例、代表性 strong miss 与精确路径，不复制 520559 个中间节点。
