---
kind: claim
claim_id: type-I-overflow-full-product-d-one-a-one-single-endpoint-stutter-guarded-relay
title: a=1 单侧端点 stutter 的因子对正规形与条件 guarded relay
statement: >-
  在完整乘积 d=1 的 a=1 hard state 中，设真实 path 到达 primitive capacity endpoint
  h|K，且对侧 z=R-h 的完整超额单侧 receipt 为 z=Q beta。令
  g_A=gcd(A,Q)、E_0=Q/g_A、D=beta g_A。若 E_0=1 (mod p)，则 D|ph+1；当
  2<=h<p 时，唯一存在正整数 m,k 使 D=mp+1-h、kD=ph+1，并且
  p+k | mk^2-k+1。该条件还等价于显式二元因子正规形，但 m,k 本身不提供较小分母
  lift。写 E_0=1+ps 后，canonical checkpoint 仍为 a=1,d=1，其下一 ordinary
  complete-excess multiplier E_1 满足 E_1≡s (mod p)。因此 s 不同于 0,1,-1 时下一
  carry 严格；s=-1 时最小互素素数源给 capacity 1；s=1 时进入有限 p-adic
  regeneration，除非末端落入 p-free failure；s=0 立即返回 p-free failure。只有 suffix
  最终得到 c<=p-2 且完整 persistent/typed/terminal-first 合同通过时，原 endpoint
  stutter 才可作为不入队 checkpoint 包进 guarded E1--E5 宏。p=97,r=6618 的真实
  五步 raw path 到达 h=58，给出 (m,k,D)=(4,17,331) 与 E_0=1+97*376206；它严格
  反驳“所有真实大非 1 (mod p) endpoint 的 canonical carry 一步严格”，但下一 ordinary
  multiplier 为 40 (mod 97)，故候选 capacity 为 80；只有上述 guards 全部通过后，
  才可登记宏并实现 96->80。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-full-product-d-one-a-one-s-zero-endpoint-boundary
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
  - type-I-overflow-full-product-d-one-complete-excess-capacity-map
  - type-I-overflow-full-product-d-one-p-adic-regeneration-countdown
  - type-I-chart-least-coprime-prime-anchor-source
  - type-I-overflow-full-product-d-one-p-block-peeling-obstruction
  - type-I-overflow-unbounded-same-chart-promotion-persistence-boundary
  - type-I-path-anchored-atomic-split-complete-excess-admission
  - type-I-unified-terminal-first-selector-contract
  - denominator-escape-state-contract
topics:
  - type-I
  - overflow
  - full-product
  - d-one
  - a-one
  - capacity-endpoint
  - complete-excess-bundle
  - carry-stutter
  - p-adic-regeneration
  - guarded-macro
  - strict-counterexample
  - proof-boundary
sources:
  - claim: type-I-overflow-full-product-d-one-a-one-s-zero-endpoint-boundary
    role: endpoint-capacity-map-and-single-side-receipt
  - claim: type-I-overflow-full-product-d-one-p-adic-regeneration-countdown
    role: canonical-d-one-regeneration-arithmetic-and-countdown
  - claim: type-I-chart-least-coprime-prime-anchor-source
    role: raw-p-failure-alternate-source
  - claim: type-I-path-anchored-atomic-split-complete-excess-admission
    role: guarded-checkpoint-composition-pattern
  - reproduction: reproductions/type_i_single_endpoint_stutter_guarded_relay.py
    role: two-reachable-endpoint-stutters-no-descent-obstruction-and-strict-relay-candidate
visibility: public
last_checked: '2026-08-13'
---

# \(a=1\) 单侧端点 stutter 的因子对正规形与条件 guarded relay

## 1. 设置

固定核心素数 \(p\equiv1\pmod {24}\)，并取一个已经入队、内容寻址且具有合法
origin/parent receipt 的 \(a=1,d=1\) hard state

\[
S=(p,R,K;A,\sigma).
\tag{1}
\]

沿用正规形

\[
b=2pr-1,\qquad n=(p+1)b-1,
\tag{2}
\]

\[
A=\frac{pn-1}{4},\qquad K=A(p-1),\qquad R=(p-1)n-1.
\tag{3}
\]

特别地，\(b\equiv-1\pmod p\)，而 \(A>B_p=(p-1)^2/4\)。设一条绑定于
`S.state_id` 的真实 raw path 到达定向 primitive node

\[
h+z=R,
\qquad (h,z)=1,
\qquad h\mid K.
\tag{4}
\]

按 \(K\) 的完整容量唯一分解

\[
z=Q\beta,
\qquad
Q=\prod_{\nu_q(z)>\nu_q(K)}q^{\nu_q(z)},
\tag{5}
\]

并假设

\[
Q>1,\qquad p\nmid Q,\qquad h\beta\mid K.
\tag{6}
\]

定义

\[
g_A=(A,Q),\qquad E_0=\frac Q{g_A},\qquad
D=\beta g_A,\qquad M=\operatorname{lcm}(A,Q)=AE_0.
\tag{7}
\]

由 primitive 性，\(h,\beta,g_A\) 两两互素；结合它们都整除 \(K\)，有

\[
hD\mid K,\qquad z=E_0D.
\tag{8}
\]

以下把 \(E_0\equiv1\pmod p\) 称为这张单侧 endpoint receipt 的 canonical
stutter。这里 \(E_0\) 是 endpoint multiplier，不要与 target 的下一 ordinary
multiplier 混淆。

## 2. Stutter 的整数因子对正规形

由 \(4K=pR+1\) 和 \(hD\mid K\)，令

\[
w=\frac K{hD},
\qquad
k=\frac{ph+1}{D}.
\tag{9}
\]

式 (9) 中的 \(k\) 是正整数：既有 endpoint 容量映射给出
\(D\mid ph+1\)。此外

\[
\boxed{k+pE_0=4hw.}
\tag{10}
\]

这只是把
\(4K=p(h+E_0D)+1\) 除以 \(D\)；它同时保留了 endpoint、charged residual 和
完整超额 multiplier。

现在额外设

\[
2\le h<p,
\qquad E_0\equiv1\pmod p.
\tag{11}
\]

因为 \(E_0D=z\equiv1-h\pmod p\)，有唯一 \(m\ge1\) 使

\[
\boxed{D=mp+1-h.}
\tag{12}
\]

由 \(D\le ph+1\) 得 \(m\le h\)。把 \(Dk=ph+1\) 与 (12) 联立，可得到

\[
\boxed{
D=\frac{mp^2+p+1}{p+k},
\qquad
h=\frac{mpk+k-1}{p+k}.}
\tag{13}
\]

所以必要整除条件精确为

\[
\boxed{p+k\mid mk^2-k+1.}
\tag{14}
\]

反过来，给定正整数 \(m,k\)，若 (14) 成立，并令

\[
\ell=\frac{mk^2-k+1}{p+k},
\qquad
h=mk-\ell,
\qquad
D=m(p-k)+\ell+1,
\tag{15}
\]

则 (13) 与 \(Dk=ph+1\) 成立。若所得 \(2\le h<p\)、\(D>0\)，并且 \(D\) 确实
等于真实 receipt 的 \(\beta(A,Q)\)，就恢复 endpoint stutter。最后这个 receipt
识别条件不可删除；(14) 单独只是一张二元整数候选表。

还有一个对小 endpoint 定理有用的精确式。令

\[
a=mk-h.
\tag{16}
\]

由 (12)--(13) 直接得到

\[
\boxed{
p a=k(h-1)+1,
\qquad
D a=m+h(h-1).}
\tag{17}
\]

所以 \(a\ge1\)，并且

\[
D\le m+h(h-1),
\qquad
m(p-1)\le h^2-1.
\tag{18}
\]

特别地，\(h^2<p\) 时 (18) 不可能成立。这把旧的小 endpoint 条件
\(h^2+h-1<p\) 加强为 \(h^2<p\)。

## 3. 为什么 \(m,k\) 不是自动递降

式 (18) 确实给出 \(m<p\)，但它没有给出 \(4/m\) 的标记解，也没有把该解提升到
\(4/p\) 的公式。现有 one-/two-denominator lift 都必须读取源解的实际分母坐标；
(12)--(18) 不含这些数据。

这个障碍不是措辞问题。存在真实可达 endpoint stutter

\[
p=97,\qquad r=36,\qquad h=95,
\tag{19}
\]

其参数为

\[
(m,k,D)=(1,3072,3).
\tag{20}
\]

其七步 raw path 的小侧序列与标签为

\[
\begin{aligned}
1&\xrightarrow{97}677\,278
\xrightarrow{6911}98
\xrightarrow{3}21\,898\,623
\xrightarrow{37}1\,183\,712\\
&\xrightarrow{71}16\,672
\xrightarrow{11}5\,970\,845
\xrightarrow{62\,851}95.
\end{aligned}
\tag{20a}
\]

每个标签都是素数，选中侧比 \(K\) 恰多一层该素数，shift 为 \(q-1\)，且 gcd
reduction 为 1。终点完整分解为

\[
R-95=65\,695\,872=21\,898\,624\cdot3,
\qquad E_0=21\,898\,624\equiv1\pmod {97}.
\tag{20b}
\]

这里尤其要区分

\[
D=3,\qquad (R-95,K)=96.
\tag{20c}
\]

一般的 \(D=\beta(A,Q)\) 不是 endpoint 总容量 gcd。

这里 \(m=1<p\)，但三个正单位分数之和至多为 3，所以 \(4/1\) 没有三项正单位分数
解；同时 \(k>p\)。因此“取 \(m\) 或 \(k\) 作较小源分母”在真实 path 上已经失败。
这一张真实反例已经足以否定全称自动递降；\(m,k\) 只保留为 stutter 索引，不登记为
descent，除非另行提供源解、全域 lift 和严格势回执。

## 4. 任意单侧 endpoint stutter 的二阶 relay

现在不再假设 \(h<p\)，只使用 (1)--(8)。设

\[
E_0=1+ps,
\qquad s>0.
\tag{21}
\]

endpoint carry 的 canonical target cofactor 仍为 \(p-1\)。定义 macro-local
checkpoint \(U\) 的参数

\[
\boxed{
n_1=E_0n-s,
\qquad
b_1=bE_0-s.}
\tag{22}
\]

因为 \(E_0=1+ps\)，有

\[
4M=(pn-1)E_0=p(E_0n-s)-1,
\tag{23}
\]

以及

\[
n_1=(p+1)b_1-1.
\tag{24}
\]

所以 \(U\) 仍是 \(a=1,d=1\) 状态：

\[
M=\frac{pn_1-1}{4},\qquad
R_1=(p-1)n_1-1,\qquad
K_1=M(p-1).
\tag{25}
\]

式 (22) 又给

\[
b_1\equiv-1-s\pmod p.
\tag{26}
\]

因此 \(U\) 的 ordinary complete-excess multiplier

\[
E_1=(p-1)b_1-1
\tag{27}
\]

满足核心继电式

\[
\boxed{E_1\equiv s\pmod p.}
\tag{28}
\]

式 (22)--(28) 只使用 canonical \(d=1\) 算术，不依赖 \(E_0\) 来自根 anchor、单侧
endpoint 还是获准的 atomic split。因此既有 regeneration 定理可以从这个 endpoint
checkpoint 继续使用；新的内容是把它与真实 path-anchored endpoint receipt 和最终宏
合同明确组合。

## 5. 精确四分派

由 ordinary \(d=1\) action 的两条 \(p\)-门和 (26)--(28)，得到：

\[
\begin{array}{c|l}
s\pmod p & \text{checkpoint }U\text{ 的规范 suffix}\\ \hline
0 & E_1\equiv0:\ p\text{-free failure，保留真实 }p\text{-peel Reach};\\
1 & E_1\equiv1:\ \text{进入有限 }p\text{-adic regeneration};\\
-1 & b_1\equiv0:\ \text{raw }p\text{-source failure，改用 }q_\star\text{ source};\\
\text{其它} & c=\langle-s^{-1}\rangle_p\le p-2\text{，严格 carry}.
\end{array}
\tag{29}
\]

最后一行的标准写法是

\[
c=\langle-s^{-1}\rangle_p.
\tag{30}
\]

当 \(s\equiv-1\) 时，ordinary source 本身不合法；最小互素素数源到达同一 anchor，
而 \(a=1\) 使其 target capacity 精确为 1。当 \(s\equiv1\) 时，既有倒计时给

\[
\nu_p(E_{i+1}-1)=\nu_p(E_i-1)-1.
\tag{31}
\]

若首个非 regeneration 行为 ordinary strict 或 raw-source failure，则分别由 (30) 或
\(q_\star\) 得到最终 \(c\le p-2\)。若首个非 regeneration 行是 p-free failure，则
不能产生这张宏；它返回同一个 \(a=1\) hard branch。故真正未闭合的不是所有 endpoint
stutter，而精确是：

\[
\boxed{
s\equiv0\pmod p,
\quad\text{或}\quad
s\equiv1\pmod p\text{ 的 regeneration 最终落入 p-free failure}.}
\tag{32}
\]

## 6. 条件 guarded E1--E5 宏

### 定理 1（单侧 endpoint stutter guarded relay）

在 (1)--(8)、(21) 下，若 (29) 的规范 suffix 最终到达 residual capacity
\(c\le p-2\)，且途中没有落入 (32)，则从真实 persistent \(S\) 一次连续重放到最终
target \(V\) 可条件性组成 guarded E1--E5 宏，前提是以下回执全部通过：

1. **E1：** 重放 \(S\) 的 origin/parent、完整 raw source/path、定向 node occurrence、
   (5) 的 maximality、(6)--(8) 的 residual gate、owner 与 scope；suffix 必须从
   `U.checkpoint_id` 连续重放，\(U\) 不获得独立 root 或 persistent 权限；
2. **E2：** 从原始整数唯一重算 \(U\)、每个 regeneration checkpoint 与 \(V\) 的
   support、\(R,K\)、\(a=1,d=1\) normal form 及合法 target；
3. **E3：** 对每个状态独立执行 `verify_state` 与 F/G/hit 重分类，保存 adapter/verifier
   version、state/path/owner/ledger digest 和同一 \(\sigma\)；最终 \(V\) 标记
   `pending_dispatch`；
4. **E4：** 全部标记集均为图表无关的 \(\operatorname{Sol}(4,p)\)，宏 lift 是各段
   identity 的全域复合；
5. **E5：** 所有 checkpoint 都不入队，只比较真实 parent 与最终 target。由
   \(A>B_p\)、\(M>A\) 及 \(c\le p-2\)，
   \[
   \Lambda_p^\sharp(S)=(0,p-1)>(0,c)=\Lambda_p^\sharp(V).
   \tag{33}
   \]

\(s\equiv1\) 时的估值 (31) 只证明宏内部 suffix 有限，不能替代 (33)。此外，必须对
\(S\)、策略暴露的 raw node、\(U\)、每个 regeneration checkpoint 和 \(V\) 重放
版本化 terminal/alternate prefix；只有已由具名 verifier 闭合的 direct terminal 才立即返回
terminal leaf。alternate 命中必须按其自身 typed contract 分派；未获 E1--E5 或 terminal
资格时只保留 `analysis_evidence`，当前 endpoint 宏不生成后继。

这是一条条件组合定理，不声称统一 serializer/adapter/registry 已实现。对 (29) 的一般
类、\(-1\) 类和最终非 p-free 的 \(1\) 类，整数算术、identity lift 与最终 rank 已经
齐备；实现缺口是 checkpoint schema、内容 hash、typed classifier、priority receipt 与
registry 集成。式 (32) 则仍是实质算术余项，不能归入“只差实现”。

## 7. 真实可达的一步 stutter 反例与二阶严格出口

取

\[
p=97,\qquad r=6618.
\tag{34}
\]

相应状态为

\[
\begin{aligned}
b&=1\,283\,891,& n&=125\,821\,317,\\
A&=3\,051\,166\,937,& K&=292\,912\,025\,952,\\
R&=12\,078\,846\,431.&&
\end{aligned}
\tag{35}
\]

从 canonical anchor \(\{1,R-1\}\) 出发，以下五条实际 raw 边到达 \(h=58\)：

\[
\begin{aligned}
1&\xrightarrow{5}2\,415\,769\,286
\xrightarrow{67}36\,056\,258
\xrightarrow{3793}9\,506\\
&\xrightarrow{5393}2\,239\,725
\xrightarrow{208\,217\,357}58.
\end{aligned}
\tag{36}
\]

每一步都选中含标签素数的一侧，标签在该侧指数为 1、在 \(K\) 中指数为 0，shift 为
\(q-1\)，且 gcd reduction 为 1。终点有

\[
z=R-58=12\,078\,846\,373
=36\,491\,983\cdot331,
\tag{37}
\]

\[
Q=36\,491\,983,\qquad \beta=D=331,\qquad (A,Q)=1,
\tag{38}
\]

\[
58\cdot331\mid K,\qquad
97\cdot58+1=17\cdot331.
\tag{39}
\]

因此 (12)--(14) 的参数为

\[
(m,k,D)=(4,17,331),
\qquad 97+17\mid4\cdot17^2-17+1.
\tag{40}
\]

关键是

\[
E_0=Q=36\,491\,983=1+97\cdot376\,206.
\tag{41}
\]

所以这是一张真实可达、\(h\not\equiv1\pmod p\)、不命中该 endpoint 的 direct
bottom Type I terminal，且 canonical carry 不严格的 one-shot stutter。它严格反驳
“所有大的非 \(1\bmod p\) endpoint 的 canonical carry 一步严格”，也反驳仅含
direct bottom Type I 与该 carry 的二分；它不声称旁路的完整 Type I/II 菜单为空。

但 \(s=376\,206\equiv40\pmod {97}\)，落入 (29) 的一般类。checkpoint 参数为

\[
\begin{aligned}
n_1&=4\,591\,469\,360\,625\,405,\\
b_1&=46\,851\,728\,169\,647,\\
M&=111\,343\,131\,995\,166\,071,\\
R_1&=440\,781\,058\,620\,038\,879,\\
K_1&=10\,688\,940\,671\,535\,942\,816.
\end{aligned}
\tag{42}
\]

下一 ordinary multiplier 为

\[
E_1=4\,497\,765\,904\,286\,111\equiv40\pmod {97},
\tag{43}
\]

两条 \(p\)-门都通过，且

\[
c=-40^{-1}\equiv80<96\pmod {97}.
\tag{44}
\]

所以该反例否定的是单步引理，不是否定 guarded relay；在 (33) 的最终比较下，它给出
\((0,96)\to(0,80)\) 的严格算术候选。只有定理 1 的全部回执通过后，该候选才成为合法宏。

## 8. 当前边界

本卡没有证明每个大 endpoint 都产生 stutter 或 terminal，也没有关闭 (32)。它把旧的
“大非 \(1\bmod p\) endpoint 必须一步严格”改成了正确的两层目标：

1. 非 stutter endpoint 给出当步严格算术 cofactor；
2. stutter endpoint 除 (32) 外都有最终 \(c\le p-2\) 的严格算术 suffix；只有连续
   lineage、typed reclassification、priority prefix、identity lift 和 E5 全部通过时，
   才升格为 guarded strict macro，否则仍是 candidate。

下一项决定性数学工作因此应专门研究 endpoint multiplier 的
\(E_0\equiv1\pmod {p^2}\) 类，以及 regeneration 落入 p-free failure 后的真实
\(p\)-block Reach；不再把 \(m,k\) 当作无标记较小分母，也不再尝试证明已经被 (34)--(41)
否定的 one-shot 命题。

## 9. 聚焦回执

```bash
python3 reproductions/type_i_single_endpoint_stutter_guarded_relay.py --verify
```

脚本只重放 (19)--(20c) 的七条 raw 边与 (34)--(44) 的五条 raw 边，核对完整超额
分解、因子对正规形、\(D\) 与总 gcd 的区分以及下一 strict capacity。它不扫描素数、
分母、selector history、完整 terminal 菜单或历史测试。
