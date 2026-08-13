---
kind: claim
claim_id: type-I-overflow-full-product-d-one-a-one-s-one-saturated-provenance-exclusion
title: a=1 的 s=1 饱和端点反向闭包与现有具名源排除
statement: >-
  固定任意 primitive m=1 raw bottom 节点 N_x={x,R-x}。其全部带素数标签的 m=1
  前驱恰为 N_y，其中 y=min(qx,R-qx)，且 qx<R、q 不整除 R、
  v_q(x)>=v_q(K)；所以每个节点的反向入度有限。对 p=73 的既有 s=1 静态饱和
  endpoint h=451141437368，这个公式给出完整的 23 节点、23 边反向可达闭包。
  universal p-source 与最小互素素数 q_*=5 source 的全部首 raw 后继都在 m=1 层且与
  该闭包不交，故从这两个固定具名源出发的任意 raw path 均不能到达 h。该静态控制还被
  直接 Type II 证书 4/73=1/20+1/219+1/4380 抢占。因此它不再是 admitted 饱和障碍；
  结论不排除未来不同的 target-independent source family，也不关闭一般 s=1 provenance
  问题。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-formal-full-excess-cycle-or-hit-reduction
  - type-I-universal-p-source-capacity-anchor-orbit
  - type-I-chart-least-coprime-prime-anchor-source
  - type-I-unified-terminal-first-selector-contract
topics:
  - type-I
  - overflow
  - full-product
  - d-one
  - a-one
  - raw-path
  - reverse-reach
  - finite-closure
  - source-provenance
  - terminal-first
  - saturation
  - proof-boundary
sources:
  - claim: type-I-formal-full-excess-cycle-or-hit-reduction
    role: complete-raw-transition-semantics
  - claim: type-I-chart-least-coprime-prime-anchor-source
    role: second-target-independent-named-source-family
  - claim: type-I-overflow-full-product-d-one-a-one-regeneration-return-digit-normal-form
    role: static-s-one-saturated-endpoint-receipt
  - reproduction: reproductions/type_i_s_one_saturated_endpoint_provenance_exclusion.py
    role: exact-reverse-closure-source-menu-and-terminal-intercept
visibility: public
last_checked: '2026-08-13'
---

# \(a=1\) 的 \(s=1\) 饱和端点反向闭包与现有具名源排除

## 1. \(m=1\) raw 图的完整反向前驱公式

固定一张图表

\[
R\ge3,
\qquad K\ge1,
\tag{1}
\]

并把 primitive bottom node 写成无序对

\[
N_x=\{x,R-x\},
\qquad 1\le x<\frac R2,
\qquad (x,R)=1.
\tag{2}
\]

raw 图保留素数标签，所以这里讨论的是带标签的有向多重图；一般图表可以有自环，也可能
有不同标签落到同一节点。

**定理 1（完整反向前驱公式）。** 所有满足

\[
N_y\xrightarrow{q}N_x
\tag{3}
\]

的 \(m=1\) raw 前驱与下列素数 \(q\) 一一对应：

\[
\boxed{
qx<R,
\qquad q\nmid R,
\qquad \nu_q(x)\ge\nu_q(K).}
\tag{4}
\]

对应前驱为

\[
\boxed{y=\min(qx,R-qx).}
\tag{5}
\]

特别地，固定 \(N_x\) 的标签菜单满足

\[
q\le\left\lfloor\frac{R-1}{x}\right\rfloor,
\tag{6}
\]

所以反向入度可显式有限枚举。

**证明。** 假设 (3) 成立，并把源上被 \(q\) 除的坐标记为 \(C\)，另一坐标为
\(R-C\)。因为源层数为 1，唯一 shift 是 \(q-1\)。未约分输出恰为

\[
\left\{\frac Cq,\ R-\frac Cq\right\}.
\tag{7}
\]

源 primitive 给出 \((C,R)=1\)，所以

\[
\gcd\left(\frac Cq,R-\frac Cq\right)
=\gcd\left(\frac Cq,R\right)=1.
\tag{8}
\]

因此 (7) 不会发生 gcd reduction。若 \(C/q=R-x>R/2\)，则
\(C=q(R-x)>R\)，与源坐标 \(C<R\) 矛盾；故必有 \(C/q=x\)，即 \(C=qx<R\)。
超容量条件等价于

\[
\nu_q(qx)>\nu_q(K)
\Longleftrightarrow
\nu_q(x)\ge\nu_q(K).
\tag{9}
\]

又因 \((x,R)=1\)，源 primitive 条件 \((qx,R)=1\) 恰等价于 \(q\nmid R\)。这证明
必要性及 (5)。反过来，若 (4) 成立，则
\(\{qx,R-qx\}\) 为正 primitive bottom node，\(q\) 超容量；以 shift \(q-1\)
执行 raw 边，(7) 无约分地返回 \(N_x\)。故条件也充分。\(\square\)

这个定理与“给任意目标临时制造 formal \(p\)-parent”不同：它完整列出了底层 raw 图中
所有实际入边，因而可用于证明一个**事先固定**源族到指定 endpoint 的不可达性。

## 2. \(p=73\) 的静态 \(s=1\) 饱和回执

沿用 regeneration return 控制

\[
p=73,
\qquad r_0=21\,164\,451,
\tag{10}
\]

得到

\[
b=3\,090\,009\,845,
\qquad n=228\,660\,728\,529,
\tag{11}
\]

\[
A=4\,173\,058\,295\,654,
\quad
R=16\,463\,572\,454\,087,
\quad
K=300\,460\,197\,287\,088.
\tag{12}
\]

静态 endpoint 为

\[
h=451\,141\,437\,368,
\tag{13}
\]

而对侧的完整超额分解为

\[
R-h
=3\cdot5\,337\,477\,005\,573,
\tag{14}
\]

\[
(A,5\,337\,477\,005\,573)=1,
\qquad 3h\mid K.
\tag{15}
\]

其 canonical multiplier 满足

\[
5\,337\,477\,005\,573
=1+73\bigl(1+73\cdot1\,001\,590\,731\bigr).
\tag{16}
\]

所以这是 \(s\equiv1\pmod p\) checkpoint。一次 regeneration 后首位
\(\omega=-1\)，返回 \(p\)-free 根接口，且根容量为

\[
73^2+73+1=5403.
\tag{17}
\]

这些等式只说明静态算术相容；endpoint 是否来自已声明源，必须由 raw Reach 独立判断。

## 3. 反向可达闭包恰有 23 点

从 (13) 开始反复应用定理 1。按到 endpoint 的最短反向距离分层，得到：

| 层 | 节点的小坐标 \(x\) |
|---:|---|
| 0 | 451141437368 |
| 1 | 2255707186840, 2478187895679, 3157990061576, 3380470770415, 5864838685784, 6087319394623, 7669404435256 |
| 2 | 673622146207, 4072632975692, 5185036519887, 7434563687037 |
| 3 | 970263091326, 3368110731035, 4715355023449, 5011995968568, 7706484553396 |
| 4 | 1427584548383, 3850152266849, 4851315456630, 6791841639282 |
| 5 | 6470480615406, 7137922741915 |

第 5 层没有新前驱。完整的带标签边可压缩为下列 predecessor 表；记号
\(y_q\) 表示 \(N_y\xrightarrow qN_x\)：

| target \(x\) | 全部 \((q,y)\) |
|---:|---|
| 451141437368 | (5,2255707186840), (7,3157990061576), (13,5864838685784), (17,7669404435256), (23,6087319394623), (29,3380470770415), (31,2478187895679) |
| 2255707186840 | (5,5185036519887), (7,673622146207) |
| 2478187895679 | (3,7434563687037), (5,4072632975692) |
| 3157990061576 | (5,673622146207) |
| 673622146207 | (5,3368110731035), (7,4715355023449), (13,7706484553396), (17,5011995968568), (23,970263091326) |
| 970263091326 | (5,4851315456630), (7,6791841639282), (13,3850152266849) |
| 5011995968568 | (3,1427584548383) |
| 1427584548383 | (5,7137922741915), (7,6470480615406) |

表中未列出的闭包节点没有前驱。逐行使用 (4) 的有限素数菜单，不只是 BFS 生成树，得到

\[
\boxed{23\text{ 个节点},\qquad23\text{ 条带标签边}.}
\tag{18}
\]

因此这 23 点是完整的 \(m=1\) 反向可达闭包。

## 4. 两类现有具名源的全部首步均被排除

### 4.1 Universal \(p\)-source

该图表的固定 universal source 为

\[
(U,V,m)
=(73,1\,185\,377\,216\,694\,191,72),
\tag{19}
\]

其中

\[
V=521\cdot2\,275\,196\,193\,271.
\tag{20}
\]

三个素因子相对 \(K\) 都超容量，且完整首后继菜单为

\[
\begin{array}{c|ccc}
q&73&521&2\,275\,196\,193\,271\\ \hline
\text{后继小坐标}&1&2\,275\,196\,193\,271&521.
\end{array}
\tag{21}
\]

每个后继的层数都恰为 1。

### 4.2 最小互素素数源

这里不整除 \(RK(R-1)\) 的最小素数为 \(q_\star=5\)，对应固定源

\[
(U,V,m)=(5,65\,854\,289\,816\,343,4),
\tag{22}
\]

且

\[
V=3^2\cdot7\cdot5641\cdot5717\cdot32413.
\tag{23}
\]

由于 \(\nu_3(V)=\nu_3(K)=2\)，标签 3 不超容量；其余五个标签给出完整菜单

\[
\begin{array}{c|ccccc}
q&5&7&5641&5717&32413\\ \hline
\text{后继小坐标}
&1&7\,055\,816\,766\,038&11\,674\,222\,623&11\,519\,029\,179&2\,031\,724\,611.
\end{array}
\tag{24}
\]

这些后继也全部位于 \(m=1\) 层。(21)、(24) 共给出八条首边、七个不同的小坐标
（两类源共享 \(x=1\)），并且它们与 (18) 的闭包完全不交。\(m=1\) raw 边保持层数
1，所以得到严格结论

\[
\boxed{
\text{从当前两个固定具名源的任意首边出发，任意后续 raw path 都不能到达 }h.}
\tag{25}
\]

这比“规范 anchor 轨道不经过 \(h\)”更强；它穷尽了两个源三元组的全部首步选择，而
不是只检查默认 anchor 边。

## 5. Terminal-first 抢占与合同结论

同一个核心素数已有直接 Type II 证书

\[
\boxed{
\frac4{73}=\frac1{20}+\frac1{219}+\frac1{4380}.}
\tag{26}
\]

因此按现有 terminal-first 合同，选择器在生成该深层静态候选之前已经停止。对 (13)--(17)
这一个控制，准确账本是：

| 合同项 | 结论 |
|---|---|
| E1 | 对 universal \(p\)-source 与 \(q_\star\)-source 完整失败，见 (25)；target-dependent formal parent 不计来源。 |
| E2 | 静态 determinant、complete-excess、checkpoint 与饱和 return 算术均通过。 |
| E3 | 被 (26) 的 terminal-first priority 抢占，不产生递归 edge。 |
| E4 | 未调用。 |
| E5 | 未支付；静态 return 本身仍饱和。 |

所以这个 \(p=73\) 例子不再能承担“已获准路径可能饱和”的反例角色。它同时遭到来源排除
和终端抢占。

结论的量词必须保持精确：(25) 只排除当前两类 target-independent named source
families。未来若提出第三类合法源，仍可检查其首后继是否进入 (18)；本卡没有证明任意
可能源都不可达，也没有证明所有核心素数的 \(s=1\) return 都被终端覆盖。

## 6. 聚焦回执

```bash
python3 reproductions/type_i_s_one_saturated_endpoint_provenance_exclusion.py --verify
```

脚本从定理 1 重新生成全部反向层和边，完整分解两个具名源的坐标并回放每条首边，同时
重算静态饱和 return 与 (26)。它不扫描素数范围、分母范围、selector history 或历史
测试结果。
