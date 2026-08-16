---
kind: claim
claim_id: type-I-q-one-full-carrier-d-one-c-eight-low-gate-complement-pfree-split-interface
title: q=1 容量八低容量 gate 的互补 p-free 排除与双侧 split 接口
statement: >-
  在真实 q_star=103 的 c=8 high-R source 上，设一条实际 V-side strict raw prime
  q>2(p-1) 到达 (a,b,1)=(V/q,R-V/q,1)，令 h=gcd(a,M)，并令 a-side canonical
  capacity c_a<8。则 p 不整除 b；所以 a,b 的完整 excess block 都 p-free，且 c_a<8
  强制 Q_a>1。若 Q_b=1，则 b+Q_a beta_a=R、b beta_a|K 构成 actual
  path-anchored 单侧 complete-excess payload，canonical target 的 capacity 正是
  c_a<8。若 Q_b>1，则同一 actual raw receipt 满足双侧 atomic split 的所有
  source/p-free 算术前提；写 T_i=lcm(M,Q_i)/M，L=T_aT_b，split target capacity
  c_Sigma 满足 79 T_b c_Sigma+32 hq=0 (mod p)。因此低 gate 的 p-primary
  complement 不是未支付障碍：余下分支精确缩为单侧 target typed/priority 准入，或双侧
  split 的 independent capacity 与 typed/priority 准入。本结论不将任一候选自动升级为
  terminal 或 E1--E5 edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-q-one-full-carrier-d-one-c-eight-v-side-direct-m-one-capacity-map
  - type-I-q-one-full-carrier-d-one-c-eight-universal-source-non-p-separation
  - type-I-path-anchored-atomic-split-complete-excess-admission
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
  - type-I-high-support-bundle-carry-capacity-terminal-dispatch
  - denominator-escape-state-contract
topics:
  - type-I
  - q-one
  - full-carrier
  - c-eight
  - source-lineage
  - complete-excess
  - p-free
  - atomic-split
  - capacity-map
  - proof-boundary
sources:
  - claim: type-I-q-one-full-carrier-d-one-c-eight-v-side-direct-m-one-capacity-map
    role: direct-m-one-low-capacity-gate
  - claim: type-I-q-one-full-carrier-d-one-c-eight-universal-source-non-p-separation
    role: primitive-V-side-source-and-shared-support
  - claim: type-I-path-anchored-atomic-split-complete-excess-admission
    role: two-sided-payload-admission-schema
  - claim: type-I-bottom-sink-scc-complete-excess-bundle-selector
    role: one-sided-complete-excess-normal-form
  - reproduction: reproductions/type_i_q_one_full_carrier_d_one_c_eight_low_gate_complement_pfree_split_interface.py
    role: finite-p-primary-exclusion-and-two-sided-raw-control
visibility: public
last_checked: '2026-08-17'
---

# q=1 容量八低容量 gate 的互补 \(p\)-free 排除与双侧 split 接口

## 1. 输入与记号

保留容量八 \(q_\star=103\) 的 normal form：

\[
p=48s+1,\qquad
s\equiv86\pmod {103},\qquad
K=8M,\qquad
pR+1=4K.
\tag{1}
\]

这里 \(M\) 是已由前一条 strict relay 支付的 charged support；特别地
\(M>B_p=(p-1)^2/4\)，当前 high-support capacity 为 \(8\)。取一个实际 \(V\)-side
strict raw prime \(q>2(p-1)\)。已有 source receipt 给出无约分 endpoint

\[
(p,V,p-1)\xrightarrow q(a,b,1),\qquad
a=\frac Vq,\qquad b=R-a,\qquad (a,b)=1.
\tag{2}
\]

令

\[
h=(a,M),\qquad
T_a=\frac a h,\qquad
c_a=\langle8T_a^{-1}\rangle_p.
\tag{3}
\]

direct \(m=1\) capacity map 已经证明

\[
79c_a+32hq\equiv0\pmod p.
\tag{4}
\]

本卡只处理真正命中低容量 gate 的情形 \(1\le c_a\le7\)。对
\(v\in\{a,b\}\)，记相对于当前 \(K\) 的完整 excess 分解为

\[
v=Q_v\beta_v,\qquad Q_v=Q_K(v).
\tag{5}
\]

## 2. 低 gate 排除互补坐标的 \(p\)-primary

**引理。** 在 (1)--(4) 与 \(1\le c_a\le7\) 下，

\[
\boxed{p\nmid b.}
\tag{6}
\]

**证明。** 因为 \(qa=V\equiv-R\pmod p\) 且 \(b=R-a\)，

\[
p\mid b
\Longleftrightarrow a\equiv R\pmod p
\Longleftrightarrow q\equiv-1\pmod p.
\tag{7}
\]

若 (7) 成立，(4) 强制

\[
p\mid32h-79c_a.
\tag{8}
\]

已有 source-side 支撑分离给出 \(h\mid67199=11\cdot41\cdot149\)。因此只剩八个
\(h\) 与七个 \(c_a\) 的 56 个固定整数。精确因子分解显示，满足

\[
p\ge4129,\qquad p\equiv1\pmod {48},\qquad p\mid32h-79c_a
\tag{9}
\]

的唯一候选为

\[
(h,c_a,p)=(1639,1,52369).
\tag{10}
\]

但此时

\[
s=\frac{52369-1}{48}=1091\equiv61\pmod {103},
\tag{11}
\]

矛盾于 (1)。故 (6) 成立。这里没有扫描 \(s\)、素数或 endpoint；(10) 是 56 个小常数
的有限因子证书。 \(\square\)

source-side 分离本已有 \(p\nmid a\)，所以

\[
\boxed{p\nmid Q_aQ_b.}
\tag{12}
\]

这关闭的是 low gate 上 canonical rechart 的互补 \(p\)-primary，不把 raw edge 本身
误记为递降。

## 3. 完整 excess 的 source 分支

由 complete-excess lcm 正规化，

\[
\frac{\operatorname{lcm}(M,Q_a)}M=T_a.
\tag{13}
\]

若 \(Q_a=1\)，上式给出 \(T_a=1\)，从而 (3) 强制 \(c_a=8\)，与低 gate 矛盾。于是

\[
\boxed{Q_a>1.}
\tag{14}
\]

低 gate 没有“a-side 没有可收费完整块”的遗漏，剩余只有两种互斥情形。

### 3.1 单侧分支：\(Q_b=1\)

此时 \(b\mid K\)。又 \(\beta_a\mid K\)，且 \((b,\beta_a)=1\)，所以

\[
\boxed{b+Q_a\beta_a=R,\quad b\beta_a\mid K,\quad
(Q_a,b\beta_a)=1,\quad p\nmid Q_a.}
\tag{15}
\]

这正是 actual direct raw path 上的单侧 complete-excess payload。其 canonical support
为

\[
M_a=\operatorname{lcm}(M,Q_a)=MT_a,
\tag{16}
\]

而 target capacity 正是 \(c_a\)。故 high-support rank 的算术部分严格为

\[
\Lambda_p^\sharp:(0,8)\longmapsto(0,c_a),\qquad c_a<8.
\tag{17}
\]

也就是说，source/path、maximal block、p-free charge 与 E5 的算术条件已经支付。
若 source 的 persistent receipt、一个不借用 sink 假设的 one-sided adapter/normal-form
verifier、target 的独立 typed classifier，以及 terminal/alternate priority prefix 都通过，
才可将 (15)--(17) 升为完整 E1--E5 edge；本卡不跳过这些回执。

### 3.2 双侧分支：\(Q_b>1\)

由 (2)、(5)、(12)，

\[
(Q_a,Q_b)=1,\qquad \beta_a\beta_b\mid K,\qquad p\nmid Q_aQ_b.
\tag{18}
\]

所以同一个 source/path receipt 满足 atomic split schema 的完整 payload 前提。令

\[
T_b=\frac{\operatorname{lcm}(M,Q_b)}M,\qquad
L=\frac{\operatorname{lcm}(M,Q_a,Q_b)}M.
\tag{19}
\]

两个完整块互素，逐素数比较给出

\[
L=T_aT_b.
\tag{20}
\]

令 split canonical target 的 capacity 为

\[
c_\Sigma=\langle8L^{-1}\rangle_p.
\tag{21}
\]

由 \(T_ac_a\equiv8\) 和 (20)，\(c_a\equiv T_bc_\Sigma\pmod p\)。代入 (4)：

\[
\boxed{79T_bc_\Sigma+32hq\equiv0\pmod p.}
\tag{22}
\]

因此 a-side 命中低 gate 并不自动使 atomic split 的 \(c_\Sigma<8\)；互补完整块
\(T_b\) 必须单独进入容量比较。这不是 source 缺口： (18) 已支付双侧 payload 的
\(p\)-free 与 source 算术条件。余下的决定性问题是 (21) 的 strict capacity、目标 typed
reclassification 与 priority receipt。

## 4. 精确控制

已有 terminal-preempted c=8 控制 \(s=3279,p=157393\)，取 \(q=5963047\) 时，actual
raw endpoint 同时有两个完整 block：

\[
Q_a=3113076331159817,\qquad
Q_b=19138464436332689.
\tag{23}
\]

它们都与旧 support 互素，因此

\[
T_a=Q_a,\qquad T_b=Q_b,\qquad
L=T_aT_b=59579500651491202538305440357913.
\tag{24}
\]

该控制不命中 low gate；它给出

\[
c_a=11230,\qquad c_\Sigma=38261,
\tag{25}
\]

并直接满足 (4)、(22)。它只复核双侧公式和 raw payload，不作为 persistent
counterexample 或 selector edge。

## 5. 收紧后的边界

本卡没有证明每个容量八 source 都命中低 gate，也没有保证 (21) 严格下降。它新增的是：

- 对任何实际 low-gate endpoint，互补 \(p\)-primary 已被全称排除；
- 单侧时 E5 的算术支付已经完成，剩下的是 one-sided adapter、typed/priority 准入；
- 双侧时 source/p-free payload 已完整，唯一新增算术门是 (21) 的 capacity，而不是
  无来源的 formal rechart。

下一条有价值的对象是：对双侧分支，将 (22) 与 \(T_b\) 的可控结构连接到
\(c_\Sigma<8\)、terminal，或另一条全域可提升的严格势；不能再把 \(p\mid b\) 当作
开放 source-lineage 障碍。

聚焦复核：

~~~bash
python3 reproductions/type_i_q_one_full_carrier_d_one_c_eight_low_gate_complement_pfree_split_interface.py --verify
~~~

复现器只分解 56 个小常数 \(32h-79c\)，并重放一个既有 raw control；不扫描参数射线、
素数、factor target 或历史证书。
