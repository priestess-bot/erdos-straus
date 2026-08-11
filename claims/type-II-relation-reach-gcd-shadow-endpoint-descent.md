---
kind: claim
claim_id: type-II-relation-reach-gcd-shadow-endpoint-descent
title: Type II 关系 Reach 的 q-owned gcd shadow 全称端点递降
statement: >-
  设 p=4U+1 为核心素数，q>1 属于 p-1 Type II 的端点允许下闭域，
  m=4q-1、x=U+q。任一 terminal-first 后仍存活的真实整数关系 Reach 必进入
  kappa=1 底层。对任一 source-reachable 底层节点 {a,b}，令
  D_q(a,b)={gcd(a,q),gcd(b,q)} 去掉 q；因 a+b=4q-1，D_q(a,b) 必非空，
  且每个 q' 属于 D_q(a,b) 都满足 q'|q、q'<q。以 q' 重建
  m'=4q'-1、x'=U+q' 后，端点下闭性保证状态合法；新端点命中时直接产生
  Type I/II 短证书，否则以 Sol(p) 恒等映射和 q'<q 得到完整 E1--E5
  递降。q=1 时模数为 3；若目标 -1 位于源像，则某个源生成元模 3 为 -1，
  单位指数已在 signed box 内命中，故 F-empty 基例不存在。于是普通 Type II
  F-empty 端点相位必在有限次 q 因子递降内终止或转交 G/Type I，底层关系周期
  不再构成循环障碍。该论证不使用循环离散对数，并推广到一般有限阿贝尔源群；
  非平凡 marked_solution_set 的终端成员资格仍须另证。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-odd-kernel-overflow-natural-tail-relation-graph
  - type-II-relation-reach-proper-endpoint-descent
  - type-II-p-minus-one-divisor-downset-prime-power-allocation
  - type-II-symmetric-divisor-fiber-antipodal-physical-capacity-terminal
  - denominator-escape-state-contract
topics:
  - type-II
  - p-minus-one
  - odd-kernel
  - relation-graph
  - gcd-shadow
  - physical-capacity
  - endpoint-descent
  - identity-lift
  - well-founded-rank
  - E1-E5
  - finite-abelian-groups
  - selector
sources:
  - claim: type-II-odd-kernel-overflow-natural-tail-relation-graph
    role: terminal-first finite relation reach and kappa-one bottom existence
  - claim: type-II-relation-reach-proper-endpoint-descent
    role: endpoint reconstruction and E1-E5 contract for exact divisor coordinates
  - claim: type-II-p-minus-one-divisor-downset-prime-power-allocation
    role: endpoint divisor-downset closure
  - claim: type-II-symmetric-divisor-fiber-antipodal-physical-capacity-terminal
    role: signed-box hit gives physical d-less-than-x Type-II terminal
  - concept: concepts/denominator-escape-state-contract.md
    role: E1-E5 state and edge contract
  - reproduction: reproductions/type_ii_relation_reach_gcd_shadow_endpoint_descent.py
    role: focused gcd-shadow endpoint and q-one-base verifier
visibility: public
last_checked: '2026-08-12'
---

# Type II 关系 Reach 的 \(q\)-owned gcd shadow 全称端点递降

## 1. 从物理空盒到终端自由底层

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

并假设 \(q\) 属于端点允许下闭域。奇核盒非空时，反足物理容量定理已经从同一
目标纤维构造 \(d<x\) 的 Type II terminal。以下只研究目标位于完整源像、但有限
signed box 为空的 F/odd-kernel 状态。

任取一个真实整数目标原像，写成

\[
A+B=m\kappa,
\qquad
(A,B)=1.
\tag{2}
\]

自然尾容量定理把指数预算精确写成 \(AB\mid px\)：成立时直接得到 Type I/II；
不成立时依次检查 \(\kappa\) 的 fresh quotient 和超容量边标签。若均无终端，完整
关系 Reach 必进入一个 source-reachable 的底层节点

\[
\{a,b\},
\qquad
a+b=m=4q-1,
\qquad
(a,b)=1.
\tag{3}
\]

旧适配器要求 \(a\) 或 \(b\) 本身是 \(q\) 的真因子。下面证明不需要这个额外
存在性量词。

## 2. \(q\)-owned gcd shadow 引理

对底层节点 (3) 定义其 \(q\)-owned shadows：

\[
\mathcal D_q(a,b)
=\{(a,q),(b,q)\}\setminus\{q\}.
\tag{4}
\]

这里集合去重。每个未被删除的元素当然是 \(q\) 的正因子并且小于 \(q\)。关键是
它不可能为空。

若 (4) 为空，则 \(q\mid a\) 且 \(q\mid b\)。于是
\(q\mid a+b=4q-1\)，即 \(q\mid1\)，与 \(q>1\) 矛盾。因此

\[
\boxed{
q>1
\Longrightarrow
\varnothing\ne\mathcal D_q(a,b)
\subseteq\{d:d\mid q,\ d<q\}.}
\tag{5}
\]

式 (4) 是一个确定的物理容量投影。由于 \(q\mid x\)，\((a,q)\) 与
\((b,q)\) 分别保留当前关系坐标中由端点 \(q\) 实际拥有的 occurrence，并删除
\(r+1\) 侧或关系迁移新引入的外部载体。

## 3. shadow 端点的 E1--E5 适配器

从 (4) 任选一个规范元素 \(q'\)。选择器可以先对全部 shadow 检查终端；若均无终端，
再取最小 \(q'\)。定义

\[
m'=4q'-1,
\qquad
x'=U+q'.
\tag{6}
\]

由 \(q'\mid q\mid U\)，且端点允许域沿整除向下封闭，\(q'\) 仍是合法端点。又有

\[
4x'=p+m'.
\tag{7}
\]

若 \(U=q'r'\)，则 \(x'=q'(r'+1)\)，且

\[
p=4q'r'+1=4q'(r'+1)-m'.
\]

所以 \((x',m')=1\)。从原始整数重新分解 \(x'\)，重算完整源子群和 signed box：

1. 若统一短证书 verifier 在 gap \(m'\) 命中，直接输出 Type I/II terminal；
2. 若 signed box 命中，反足物理容量定理直接输出 \(d<x'\) 的 Type II terminal；
3. 否则重建合法 G 或 F 空状态 \(T(p,q')\)。

第三支对普通状态 \(W_S=W_T=\operatorname{Sol}(p)\) 的 E1--E5 为：

| 合同 | 可复核内容 |
|---|---|
| E1 | 原端点、真实整数原像、terminal-first source path、底层节点 (3) 和 gcd 见证 (4) |
| E2 | 由 \(q'=(a,q)\) 或 \(q'=(b,q)\) 确定性重建 (6)、分解、source subgroup 与 G/F/hit 分类 |
| E3 | 重算 \(q'\mid q\mid U\)、端点下闭性、\((x',m')=1\) 与 (7) |
| E4 | 两状态均取 \(W=\operatorname{Sol}(p)\)，故恒等映射 \(u\mapsto u\) 全域可提升 |
| E5 | 在不可重入的 p-minus-one endpoint phase 中，势从 \(q\) 严降到 \(q'\) |

因此

\[
\boxed{
q>1\text{ 且 Reach terminal-free}
\Longrightarrow
\text{Type I/II terminal 或 verified endpoint descent}.}
\tag{8}
\]

式 (5) 对每个底层节点成立，所以 (8) 不再依赖“Reach 中碰巧出现整坐标
\(a\mid q\)”的未证猜想。

## 4. \(q=1\) 的精确基例

当 \(q=1\) 时，

\[
m=3,
\qquad
x=U+1.
\tag{9}
\]

核心条件给出 \(6\mid U\)，所以 \(x\equiv1\pmod3\)，所有 \(x\) 的素因子都是模
\(3\) 的单位。写 \(x=\prod_i\ell_i^{e_i}\)，其中 \(e_i\ge1\)。

模 \(3\) 单位群只有 \(\{1,-1\}\)。若目标 \(-1\) 位于 \(\ell_i\) 生成的源像，
则至少一个生成元满足

\[
\ell_j\equiv-1\pmod3.
\]

取指数向量 \(z_j=1\)、其余坐标为零；因 \(e_j\ge1\)，它已经位于原 signed box，
并命中 \(-1\)。所以

\[
\boxed{q=1\Longrightarrow\text{hit 或 G；F-empty 不可能}.}
\tag{10}
\]

对本定理的 F/odd-kernel 输入，G 已被“目标在源像内”排除，故 \(q=1\) 必为 Type II
terminal。这是 endpoint descent 的基例，而不是有限扫描观察。

## 5. 循环闭合

每条非终端 shadow 边满足

\[
q'\mid q,
\qquad
q'<q.
\tag{11}
\]

因此 F 状态之间只能形成严格下降的正整数因子链。链若到达 \(q=1\)，由 (10) 命中；
若中途重算为 G，则退出 Type II endpoint phase，转交已有 G/Type I selector。该
phase 禁止重新进入更大的 \(q\)，所以底层 relation SCC 不再产生递归循环。

## 6. 一般有限阿贝尔源群

式 (2)--(8) 只使用真实整数原像、gcd、端点下闭性和同一方程 \(4/p\)，不使用循环
离散对数。更精确地，允许任意有限阿贝尔源群 \(H\) 配备真实剩余类同态

\[
\phi:\mathbb Z^t\longrightarrow H\longrightarrow U(m),
\]

其中坐标生成元来自 \(x\) 的物理素因子，二阶目标映到模 \(m\) 的 \(-1\)。任取目标
的整数原像，仍可按正负部分得到 (2)，所以自然尾容量、关系 Reach 和 gcd-shadow
适配器原样成立。这里不要求 \(H\) 或其像循环。

基例也不要求源群循环。任意源生成系到
\(U(3)\simeq C_2\) 的像若含非平凡目标，至少一个生成元的像非平凡；对应单位指数
就在对称盒内。结合一般有限阿贝尔版本的反足物理容量定理，命中仍自动给出一个
\(d<x\) 的 Type II terminal。因此循环假设只用于把某些中间 miss 写成离散对数
仿射盒，不用于空盒转交、大小门或 endpoint descent。

## 7. 控制与严格边界

聚焦验证包括：

- \(p=7057,q=36\) 的真实 terminal-free Reach 最小坐标为 \(2\)，严格否定
  “每个 Reach 都到达坐标 \(1\)”；其 gcd shadows 仍含 \(q'=1\)，并在 gap \(3\)
  直接命中；
- \(p=47713,q=142\) 的来源节点含整坐标 \(q\)，另一坐标仍给出真 shadow，完整
  Reach 的 \(q'=2\) 在 gap \(7\) 终止；
- \(p=1201,q=3\) 与 \(p=31249,q=42\) 分别给出 \(3\to1\)、\(42\to1\) 的 G
  verified edge；
- \(p=73,q=1\) 是 G 基例，\(p=97,q=1\) 是 hit 基例，二者复现 (10) 的两侧。

非平凡 marked_solution_set 是本定理的明确边界。若状态携带
\(W_S\subsetneq\operatorname{Sol}(p)\)，非终端边可以在目标状态逐字保留同一个谓词，
使恒等映射仍成立；但新端点的一张普通短证书未必属于 \(W_S\)。因此除非另行验证
terminal 的 mark membership，不得把普通终端升级为 marked terminal。

另一个边界是这条边降低端点势 \(q\)，而不是方程分母 \(p\)。它之所以是有效的
良基 chart descent，依赖两项同时成立：endpoint phase 禁止回到更大的 \(q\)，并且
\(q=1\) 的 F-empty 基例由 (10) 真正关闭。若外层选择器允许无付款 reset 到较大
\(q\)，式 (11) 不能充当全局 E5；本定理也不单独证明 Erdős--Straus 猜想或退出后的
G/Type I 分支。

聚焦验证：

~~~bash
python3 reproductions/type_ii_relation_reach_gcd_shadow_endpoint_descent.py --verify
~~~

验证器不运行历史素数范围测试。
