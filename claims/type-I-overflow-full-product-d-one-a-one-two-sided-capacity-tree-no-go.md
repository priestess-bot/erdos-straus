---
kind: claim
claim_id: type-I-overflow-full-product-d-one-a-one-two-sided-capacity-tree-no-go
title: 完整乘积 d=1 的 a=1 双侧容量树 no-go 与 split-carrier 合同边界
statement: >-
  在完整乘积 d=1 的 a=1 族中，若容量锚 u≡1 (mod p)、u|K 且
  p||(R-u)，真实剥离 p 后令 y=(R-u)/p、x=R-y，则两侧容量精确为
  gcd(y,K)=gcd(pu+1,K) 与 gcd(x,K)=gcd(pu-p+1,K)。对任意有限深度 N，
  可用同一个 CRT 参数 r 使从 u0=p+1 出发、逐层同时迭代
  P(u)=pu+1 和 M(u)=pu-p+1 得到的完整二叉树全部整除 K；每条边都是先做
  一个真实 p-raw edge、再做容量剥离，且宏内没有 bottom Type I terminal。因此任何只在这两个 side
  projection 上搜索固定深度的局部退出策略均不成立。该 no-go 不排除中间 raw
  路径之外的 Type I/II terminal-first 证书或跨图表宏。进一步地，peeled node 两侧都超容量时，现有单侧
  complete-excess receipt 两种定向都全称不准入；把两侧完整块合并虽给出
  split-carrier 的规范目标算术，但缺少 E1/E3 来源合同，而且固定 p=73,r=50
  的联合 multiplier 为 1 (mod p)，故即使新增合同也仍需单列 carry stutter。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-full-product-d-one-a-one-p-primary-chain-no-go
  - type-I-universal-p-source-capacity-anchor-orbit
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
  - denominator-escape-state-contract
topics:
  - type-I
  - overflow
  - full-product
  - d-one
  - a-one
  - p-primary-peeling
  - two-sided-capacity
  - binary-tree
  - crt-obstruction
  - split-carrier
  - source-provenance
  - strict-counterexample
sources:
  - claim: type-I-overflow-full-product-d-one-a-one-p-primary-chain-no-go
    role: one-sided-chain-no-go-and-normal-form
  - claim: type-I-universal-p-source-capacity-anchor-orbit
    role: actual-capacity-peeling-semantics
  - claim: type-I-bottom-sink-scc-complete-excess-bundle-selector
    role: current-single-side-bundle-admission-contract
  - concept: denominator-escape-state-contract
    role: e1-e5-persistent-edge-contract
  - reproduction: reproductions/type_i_overflow_d_one_a_one_two_sided_capacity_tree_no_go.py
    role: focused-binary-tree-and-split-boundary-receipts
visibility: public
last_checked: '2026-08-12'
---

# 完整乘积 \(d=1\) 的 \(a=1\) 双侧容量树 no-go 与 split-carrier 合同边界

## 1. 设置

固定核心素数 \(p\equiv1\pmod {24}\)。沿上一张卡留下的 \(a=1\) 边界写

\[
g=\frac{p+1}{2},
\qquad
b=2pr-1,
\qquad
n=(p+1)b-1,
\tag{1}
\]

\[
A=\frac{pn-1}{4},
\qquad
R=(p-1)n-1,
\qquad
K=A(p-1).
\tag{2}
\]

再令

\[
C=\frac{p^2-1}{2},
\qquad
T=p^2r-g.
\tag{3}
\]

直接代入有

\[
A=gT,
\qquad
K=CT,
\qquad
4K=pR+1,
\tag{4}
\]

以及

\[
R\equiv1-p(2r+1)\pmod {p^2}.
\tag{5}
\]

本卡研究真实 bottom 容量锚

\[
u\mid K,
\qquad
u\equiv1\pmod p,
\qquad
p\parallel R-u.
\tag{6}
\]

## 2. 一次 \(p\)-剥离后的精确双侧容量

从 \(\{u,R-u\}\) 的第二侧做一个真实 \(q=p\) raw edge。因为 \(p\nmid K\) 且
\((u,R)=1\)，该步无 gcd reduction，得到

\[
y=\frac{R-u}{p},
\qquad
x=R-y.
\tag{7}
\]

定义两个整数变换

\[
P(u)=pu+1,
\qquad
M(u)=pu-p+1=p(u-1)+1.
\tag{8}
\]

### 定理 1（精确双侧容量公式）

式 (6)--(8) 全称满足

\[
\boxed{
(y,K)=(P(u),K),
\qquad
(x,K)=(M(u),K).}
\tag{9}
\]

**证明。** 由 \(pR=4K-1\) 直接得到

\[
p^2y=p(R-u)=4K-P(u),
\tag{10}
\]

以及

\[
p^2x=p^2R-p(R-u)=4(p-1)K+M(u).
\tag{11}
\]

又 \(p\nmid K\)，所以乘上 \(p^2\) 不改变与 \(K\) 的 gcd。分别在 (10)、(11)
中模 \(K\) 读取 gcd，即得 (9)。\(\square\)

两个候选后继还满足

\[
P(u)\equiv M(u)\equiv1\pmod p,
\qquad
(P(u),M(u))=1,
\tag{12}
\]

因为二者之差为 \(p\)，而它们都不被 \(p\) 整除。因此若 \(P(u),M(u)\mid K\)，
则 peeled node 的两侧分别沿真实容量剥离精确到达这两个互素锚，并有
\(P(u)M(u)\mid K\)。

对 repunit 锚 \(H_j=1+p+\cdots+p^j\)，互补多项式尤其是

\[
B_j=M(H_j)=1+p^2+p^3+\cdots+p^{j+1}.
\tag{13}
\]

固定底座 \(C\) 对它的贡献精确为

\[
\boxed{
(B_j,C)=(j+1,p-1).}
\tag{14}
\]

事实上 \(C=(p-1)(p+1)/2\)，两因子互素；模 \(p-1\) 有
\(B_j\equiv j+1\)。模 \(p+1\) 令 \(p\equiv-1\)：\(B_j\) 按 \(j\) 的奇偶分别
同余 1 或 2，而 \((p+1)/2\) 为奇数，故后一因子的 gcd 恒为 1，得到 (14)。这说明
二叉大容量主要来自可调因子 \(T\)，不是固定底座自动提供的退出。

## 3. 任意有限深度的完整二叉容量树

取根

\[
u_0=p+1.
\tag{15}
\]

对给定 \(N\ge1\)，令 \(\mathcal S_N\) 是从 \(u_0\) 开始、对每个深度小于 \(N\)
的节点同时应用 \(P,M\) 所得的有限完整二叉树。归纳地每个
\(u\in\mathcal S_N\) 都满足 \(u\equiv1\pmod p\)。

### 定理 2（有限完整二叉 CRT no-go）

对每个 \(N\ge1\)，存在正整数 \(r\)，使：

1. 每个 \(u\in\mathcal S_N\) 都整除 \(K\)；
2. 每个非叶节点满足 \(p\parallel R-u\)；
3. 它的两条 \(P/M\) 边都是“一个真实 \(p\)-raw edge + 一段真实容量剥离”；
4. 树内所有 departure node 及两侧容量宏路径都没有 bottom Type I terminal。

**证明。** 对每个 \(u\in\mathcal S_N\) 定义

\[
d_u=\frac{u}{(u,C)},
\qquad
L_N=\operatorname{lcm}_{u\in\mathcal S_N}d_u.
\tag{16}
\]

逐素数比较估值可知

\[
u\mid CT
\quad\Longleftrightarrow\quad
d_u\mid T.
\tag{17}
\]

所有树节点都是 \(p\)-单位，所以 \((L_N,p)=1\)。选择

\[
p^2r\equiv g\pmod {L_N},
\tag{18}
\]

便有 \(L_N\mid T\)，从而全树节点都整除 \(K=CT\)。再由 CRT 指定一个模 \(p\)
的类，同时避开

\[
r\equiv-\frac12,-1\pmod p.
\tag{19}
\]

每个树节点模 \(p^2\) 只有两类：

\[
M(u)\equiv1\pmod {p^2},
\qquad
P(u)\equiv1+p\pmod {p^2}.
\tag{20}
\]

结合 (5)，式 (19) 分别保证这两类节点的 \(R-u\) 都恰被 \(p\) 除一次。定理 1 与
全树整除随即把 peeled 两侧容量精确识别为 \(P(u),M(u)\)；通用容量剥离定理把 gcd
等式实现成真实 raw 路径。

departure side 含 \(p\nmid K\)，所以起点不是 terminal；容量剥离中只要还有超容量
素数也不可能 terminal。到达子锚后，另一侧 \(R-P(u)\) 或 \(R-M(u)\) 仍含
\(p\nmid K\)，所以终点也不是 terminal。最后可在同一 CRT 类中取足够大的正代表，
确保所有坐标为正。定理得证。\(\square\)

量词必须写成

\[
\boxed{\forall N\ \exists r,}
\tag{21}
\]

不能写成一个固定 \(r\) 支撑无限树。固定 \(K\) 的因子有限，而树节点增长无界。
不过 (21) 已严格否定任何仅在 \(P/M\) side projections 上检查统一固定深度、并期待
至少一侧强制退出的局部策略。

作为固定回执，\(p=73,N=3\) 可取

\[
r=32\,150\,457\,426\,076\,906\,549\,030\,965\,202\,251\,906\,656\,011\,250\,208\,523\,768\,862\,218\,456\,903.
\tag{22}
\]

四层节点数依次为 \(1,2,4,8\)，脚本固定核对全部 14 条真实双侧容量边。较小的一层
控制 \(p=73,r=4\,796\,963,u_0=74\) 给出

\[
74\longmapsto\{5403,5330\};
\tag{23}
\]

它是一张较紧凑的同时强制两侧完整后继的控制，不主张对一般参数的最小性。

## 4. 为什么现有 complete-excess 合同不能当场截断

对任一真实 primitive bottom node

\[
x+y=R,
\qquad
(x,y)=1,
\tag{24}
\]

分别按 \(K\) 容量写完整超额分解

\[
x=Q_x\beta_x,
\qquad
y=Q_y\beta_y.
\tag{25}
\]

这里 \(Q_x\) 是所有满足 \(v_q(x)>v_q(K)\) 的完整 \(q^{v_q(x)}\) 块之积，另一侧
同理。于是四个因子两两互素，且

\[
\beta_x\beta_y\mid K.
\tag{26}
\]

但在 \(Q_x>1\) 且其它来源条件固定时，现有 path-anchored 单侧 receipt 若选择
\(x\) 侧的 \(Q_x\)，其 residual-divisibility gate 精确要求

\[
y\beta_x\mid K.
\tag{27}
\]

因为 \((y,\beta_x)=1\) 且 \(\beta_x\mid K\)，有严格等价

\[
y\beta_x\mid K
\quad\Longleftrightarrow\quad
y\mid K
\quad\Longleftrightarrow\quad
Q_y=1.
\tag{28}
\]

对称地，在 \(Q_y>1\) 且其它来源条件固定时，\(y\) 侧的 residual-divisibility
gate 通过当且仅当 \(Q_x=1\)。完整 support-switch 还须另验所选块 \(p\)-free、
source/path 等其余合同条件。特别地：

\[
\boxed{
Q_x,Q_y>1
\Longrightarrow
\text{两种单侧 complete-excess 定向都因 residual gate 不满足现有 E1/E3。}}
\tag{29}
\]

这不是目标模逆或 E5 障碍，而是来源合同全称不准入。也不能把两块静态地顺序剥离：
若先对 \(q\mid x\) 做 raw edge，另一侧变成

\[
y'=y+(q-1)x/q,
\tag{30}
\]

并且 \(Q_y\mid y'\) 当且仅当 \(Q_y\mid q-1\)；后一个条件不由 (24)--(25) 推出。

## 5. split-carrier 的算术闭包及两道严格边界

虽然 (29) 排除现有接口，(25)--(26) 仍给出一个新的纯算术对象：

\[
Q_\Sigma=Q_xQ_y,
\qquad
\beta_\Sigma=\beta_x\beta_y,
\qquad
xy=Q_\Sigma\beta_\Sigma,
\tag{31}
\]

\[
\beta_\Sigma\mid K,
\qquad
(Q_\Sigma,\beta_\Sigma)=1.
\tag{32}
\]

若 \(p\nmid Q_\Sigma\)，则可在算术上定义

\[
M=\operatorname{lcm}(A,Q_x,Q_y)
\tag{33}
\]

及其唯一 canonical chart。但 \(Q_\Sigma\) 跨越加法节点的两侧，不满足现有
\(u+Q\beta=R\) 的同侧来源语法；所以 (31)--(33) 只能称为
`split_carrier_arithmetic_closure`，尚不是一条 E1--E5 边。

### 边界 A：即使目标严格，现有来源仍不合法

取 \(p=73,r=1\)。从 anchor \(\{1,R-1\}\) 做一个真实 \(p\)-edge 后得到

\[
(A,R,K)=(195804,772487,14097888),
\qquad
\{x,y\}=\{761905,10582\},
\tag{34}
\]

\[
(Q_x,\beta_x)=(761905,1),
\qquad
(Q_y,\beta_y)=(143,74).
\tag{35}
\]

虽然 \(\beta_x\beta_y=74\mid K\)，但两个单侧 residual gate 都失败。联合算术 support

\[
M=21\,333\,318\,666\,660
\tag{36}
\]

的 canonical cofactor 为 \(67<72=K/A\)。因此，对应 E2 的 canonical arithmetic、
对应 E4 的 identity-lift candidate 和 E5 rank inequality 都成立；但单侧 E1 premise
已经失败，且尚无 split E3 normal-form verifier，所以不能登记为 edge。

### 边界 B：新增联合合同也不会自动严格

取 \(p=73,r=50\)，并从 \(u=74\) 的 departure side 做一次真实 \(p\)-edge。此时

\[
(A,R,K)=(9857281,38888999,709724232),
\tag{37}
\]

\[
y=532725=177575\cdot3,
\qquad
x=38356274=19178137\cdot2.
\tag{38}
\]

两侧完整超额块为 \(Q_y=177575,Q_x=19178137\)，都与 \(A\) 互素且不被 73 整除。
但联合 multiplier

\[
L=\frac{\operatorname{lcm}(A,Q_x,Q_y)}A
=Q_xQ_y
=3\,405\,557\,677\,775
\equiv1\pmod {73}.
\tag{39}
\]

因此 canonical cofactor 仍为 72，和 parent 相等。故即使以后建立新的 split 来源与
恒等提升合同，也仍必须把 \(L\not\equiv1\pmod p\) 的严格 carry 与 \(L\equiv1\)
的 stutter 分开处理。

## 6. 结论与下一精确余项

本卡严格排除了两条看似自然的补丁：

1. 加深固定层数的双侧 \(p\)-capacity 搜索；
2. 把 peeled node 的两侧超额块无条件当成现有单 bundle，或假定联合 bundle 自动严格。

它没有排除完整 selector，因为所选容量宏之外的 raw 分支或独立 terminal-first
检查仍可能给出 Type I/II 证书，且 split-carrier 还可能形成新的合法跨图表宏。当前最小的新接口是带颜色的
`path_anchored_split_complete_excess_bundle_v1`：它必须保留 \((Q_x,Q_y)\) 两侧来源、
证明联合收费的 E1/E3 合法性，并在高支撑分派

\[
L\not\equiv1\pmod p
\quad\text{与}\quad
L\equiv1\pmod p
\tag{40}
\]

两类。后一类还需要新的 carry 下降、直接短证书或另一种 terminal-first 分派。

后续的
[双侧载荷正规形、stutter 继电与无限族严格旁路](type-I-overflow-full-product-d-one-a-one-split-carrier-stutter-relay.md)
已经把这一步继续压缩：它给出唯一的双色来源恒等式，但确认现有单侧 E1/E3 尚不能推出
原子 split 收费；同时把条件性 stutter 继电到下一条 \(d=1\) 剩余类，并证明
\(p=73,r=50+kW\) 的整条无限 stutter 族都有同一路径的 \(h=3\) 单侧严格候选 carry。
对已 persistent 且完成 typed-target 重分类的实例，它给出严格出口；因此本卡的固定
stutter 是真实算术边界，却不是已知的持久算术余项。

## 7. 聚焦回执

```bash
python3 reproductions/type_i_overflow_d_one_a_one_two_sided_capacity_tree_no_go.py --verify
```

脚本固定核对 \(p=73,N=3\) 的 15 个树节点和 14 条双侧宏公式，以及 (34)--(39)
两个 split-carrier 边界；不扫描素数、分母、一般深度、历史 selector 或完整 Reach。
