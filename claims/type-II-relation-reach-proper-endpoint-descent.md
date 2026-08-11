---
kind: claim
claim_id: type-II-relation-reach-proper-endpoint-descent
title: Type II 关系图可达底层的真因子端点递降与终端优先边界
statement: >-
  设 p=4U+1 为核心素数，q 属于 p-1 Type II 的端点允许下闭域，
  m=4q-1、x=U+q。由任一真实整数目标原像构造完整自然尾关系 Reach，并依次
  检查自然尾、fresh quotient 和边标签终端。若 Reach 仍无终端，且某个
  source-reachable kappa=1 节点 {a,m-a} 满足 a|q、a<q，则 q'=a 仍在端点
  允许域。重建 m'=4a-1、x'=U+a 后，若新端点有短证书或 signed box 命中，
  则直接得到 Type I/II 终端；否则得到合法 G/F 空状态。后者以 Sol(p) 的恒等
  映射完成 E4，并以预先定义的自然数势 q'<q 完成 E5，因而是完整 E1--E5
  端点递降。p=6529,q=48 证明必须限制到 source-reachable 子图；p=20857,q=66
  证明边标签终端必须先运行；p=9601,q=40 证明不能只检查 sink-SCC 最小点。
  本定理的整坐标存在性本身未证；后续 q-owned gcd-shadow 定理已用
  q'=gcd(a,q) 或 gcd(m-a,q) 的规范投影删除该全称前提。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-odd-kernel-overflow-natural-tail-relation-graph
  - type-II-p-minus-one-divisor-downset-prime-power-allocation
  - type-II-symmetric-divisor-fiber-antipodal-physical-capacity-terminal
  - denominator-escape-state-contract
topics:
  - type-II
  - p-minus-one
  - odd-kernel
  - relation-graph
  - kappa-one
  - source-reachable
  - endpoint-descent
  - identity-lift
  - well-founded-rank
  - E1-E5
  - selector
sources:
  - claim: type-II-odd-kernel-overflow-natural-tail-relation-graph
    role: terminal-first finite relation reach
  - claim: type-II-p-minus-one-divisor-downset-prime-power-allocation
    role: endpoint downset closure
  - claim: type-II-symmetric-divisor-fiber-antipodal-physical-capacity-terminal
    role: nonempty target endpoint gives a d-less-than-x Type-II terminal
  - concept: concepts/denominator-escape-state-contract.md
    role: E1-E5 state and edge contract
  - reproduction: reproductions/type_ii_relation_scc_proper_endpoint_descent.py
    role: focused edge-terminal-and-boundary verifier
visibility: public
last_checked: '2026-08-12'
---

# Type II 关系图可达底层的真因子端点递降

## 1. 设置与终端优先 Reach

固定

\[
p=4U+1\equiv1\pmod {24},
\qquad
q\mid U,
\qquad
m=4q-1,
\qquad
x=U+q,
\tag{1}
\]

并假设 \(q\) 属于已证明的端点允许下闭域

\[
\mathcal C_U
=\{d\mid U:d\le Q(U/d)\}.
\tag{2}
\]

取奇核空盒的一个真实整数目标原像，按正负部分约成

\[
A+B=m\kappa,
\qquad
(A,B)=1.
\tag{3}
\]

在完整关系 Reach 中按固定顺序运行：

\[
AB\mid px
\longrightarrow
h\mid\kappa
\longrightarrow
\text{over-capacity edge label}
\longrightarrow
\text{relation transition}.
\tag{4}
\]

前三项分别检查自然尾、fresh-quotient 与边标签 Type I/II 终端。以下只研究
这些终端全部不存在时由 (3) source-reachable 的底层节点，不使用整个抽象底层图中
不可达的节点。

## 2. 真因子端点适配器

设终端自由 Reach 含有一个底层节点

\[
\{a,m-a\},
\qquad
1\le a<m-a,
\tag{5}
\]

并且它通过真因子门

\[
\boxed{a\mid q,\qquad a<q.}
\tag{6}
\]

定义新端点

\[
q'=a,
\qquad
m'=4a-1,
\qquad
x'=U+a.
\tag{7}
\]

因为 \(a\mid q\mid U\)，新端点仍是 \(p-1\) 因子 Type II 状态。又由
\(q\in\mathcal C_U\) 及端点域的因子下闭性，

\[
\boxed{a\in\mathcal C_U.}
\tag{8}
\]

同时

\[
4x'=4U+4a=p+m',
\tag{9}
\]

若写 \(U=ar'\)，则 \(x'=a(r'+1)\) 且
\(p=4ar'+1=4a(r'+1)-m'\)。所以 \((x',m')\) 的任一公因子也整除素数 \(p\)；
又 \(m'<p\)，故 \((x',m')=1\)。

所以 (7) 确实重建了同一个素数 \(p\) 的合法 Type II 端点，而不是只给出一个
较小模数。

在该端点上重新执行统一短证书与 signed-box verifier：

1. 若 gap \(m'\) 有 Type I/II 证书，直接输出终端；
2. 若 signed box 非空，反足物理容量定理从同一目标纤维选出 \(d<x'\) 的成员，
   直接输出 Type II 终端；
3. 否则按完整源子群测试重建 G 或 F 空状态 \(T(p,a)\)。

第三支不是分析证据，而是合法后继。其 E1--E5 为：

| 合同 | 可复核内容 |
|---|---|
| E1 | 原端点、真实整数原像、完整 terminal-first Reach、节点 (5) 及真因子门 (6) |
| E2 | 由 (7) 确定性重建 \(q',m',x'\)、素因子表、signed box 与 G/F/hit 分类 |
| E3 | 重算 \(a\mid U\)、\(a\le Q(U/a)\)、\((x',m')=1\) 及 (9) |
| E4 | 两状态都取 \(W=\operatorname{Sol}(p)\)，故 \(\Phi(u)=u\) 是全域恒等提升 |
| E5 | 在不可重入的 `p_minus_one_endpoint_descent` phase 中取 \(\Pi=q\)，由 (6) 得 \(\Pi(T)=a<q=\Pi(S)\) |

因此得到条件性但完整的递降定理：

\[
\boxed{
\text{source-reachable bottom }a\mid q, a<q
\Longrightarrow
\text{Type I/II terminal 或 verified endpoint descent}.}
\tag{10}
\]

E4 的结论适用于解集标记恰为 \(\operatorname{Sol}(p)\) 的普通端点状态；若来源状态
另带非平凡标记，必须另外证明该标记在恒等映射下保持，不能直接调用本定理。

这里使用的是预先定义在正整数上的势 \(q\)，不是对有限图事后编号。任何随后允许
\(q\) 增大的重图表都必须退出该 phase，并由独立外层秩付款；本定理不授权无代价 reset。

## 3. 两条真实递降与两条终端

### 3.1 \(p=1201,q=3\)

此时

\[
U=300,\qquad m=11,\qquad x=303,\qquad
(A,B,\kappa)=(9,101,10).
\]

完整关系 Reach 无自然尾、商因子或边标签终端，底层五周期含
\(\{1,10\}\)。取 \(a=1\mid3\)，得到

\[
q'=1,\qquad m'=3,\qquad x'=301=7\cdot43.
\]

模 \(3\) 的两个源因子都等于 \(1\)，所以新端点是规范 G 空状态。回执以
\(3\to1\) 支付 E5，并以 \(\operatorname{Sol}(1201)\) 恒等映射支付 E4。

### 3.2 \(p=31249,q=42\)

这里

\[
(m,x)=(167,7854),\qquad(A,B,\kappa)=(14,153,1).
\]

source-reachable 底层含 \(\{1,166\}\)，故 \(q'=1\) 再次给出 G 空状态，且
\(42\to1\) 是严格端点势下降。唯一 sink-SCC 的最小点其实是 \(\{2,165\}\)；
这说明适配器可以在进入最终 SCC 前退出，不需要把周期本身伪装成递降。

### 3.3 \(p=3433,q=22\) 与 \(p=9601,q=40\)

第一例的可达节点 \(\{2,85\}\) 给出 \(q'=2\)、gap \(7\)，并重建 Type II 证书

\[
(x',d,y,z)=(860,1,422259,363142740).
\]

第二例的完整关系 Reach 有唯一 sink-SCC
\(\{1,158\}\leftrightarrow\{2,157\}\)，其最小点只会转交到 G；但进入该 sink
之前的可达节点 \(\{5,154\}\) 已给出 \(q'=5\)、gap \(19\) 的 Type II 证书

\[
(x',d,y,z)=(2405,65,1248130,46180810).
\]

所以完整菜单必须扫描所有 source-reachable 底层节点并执行 terminal-first，不能只
查看 sink-SCC 最小点。

## 4. 两个必要边界

### 4.1 不可使用整个抽象底层图

对

\[
p=6529,\qquad q=48,\qquad(m,x)=(191,1680),
\]

最小源关系 \((A,B)=(16,175)\) 的完整 Reach 只进入以 \(\{1,190\}\) 为最小点的
汇 SCC。整个抽象底层图另有以 \(\{5,186\}\) 为最小点的汇 SCC，但它不从该真实源
关系可达，而且 \(5\nmid48\)。因此若删除 source-reach provenance，真因子门会被
一个无关 SCC 伪造为失败。

### 4.2 边标签终端必须先于重图表

对

\[
p=20857,\qquad q=66,\qquad(m,x)=(263,5280),
\]

最小源关系为 \((A,B,\kappa)=(81,1760,7)\)。其第一层载体 \(3\) 已给出 gap \(3\) Type I
终端。若忽略该终端继续查看底层结构，会遇到不满足简单真因子模式的节点；这不能
反驳 (10)，因为正确 selector 已在 (4) 的边标签层结束。

## 5. 原条件的存在性边界

式 (10) 已经删除了 E2、E4 和 E5 三个旧缺口；剩余问题不再是“得到真因子坐标后
如何递降”，而是纯存在性命题：

\[
\boxed{
\text{每个终端自由的真实 Reach 是否必含某个 }a\mid q,\ a<q\text{？}}
\tag{11}
\]

当前聚焦样本支持 (11)，但有限搜索不是证明。若 (11) 为假，反例必须同时满足：

1. 原 signed box 为空且目标位于完整源子群；
2. 完整关系 Reach 没有三类优先终端；
3. 每个 source-reachable 底层节点的较小坐标都不是 \(q\) 的真因子。

这三个条件曾定义整坐标加强命题的精确反例域。任意不可达 SCC、已被边标签抢占的关系或
非最小抽象底层节点都不能充当 (11) 的反例。

不过全称转交已经不再需要证明 (11)。对任意可达底层节点
\(\{a,b\}\)，集合

\[
\{(a,q),(b,q)\}\setminus\{q\}
\]

必非空；其中每个元素都是 \(q\) 的真因子。后续的 gcd-shadow 定理用这个物理
\(q\)-owned 投影重建端点，并保留本卡的 E2--E5 证明。因此 (11) 只保留为一个更强的
关系图结构问题，不再是空盒转交的决定性缺口。见
[Type II 关系 Reach 的 \(q\)-owned gcd shadow 全称端点递降](type-II-relation-reach-gcd-shadow-endpoint-descent.md)。

聚焦验证：

```bash
python3 reproductions/type_ii_relation_scc_proper_endpoint_descent.py --verify
```

验证器只重放上述两条 verified edge、两条 Type II terminal 与两个边界，不运行
历史素数范围测试。
