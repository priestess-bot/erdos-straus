---
kind: claim
claim_id: type-I-q-one-full-carrier-d-one-c-eight-low-gate-complement-pfree-split-interface
title: q=1 容量八低容量 gate 的互补 p-free 排除与双侧 split 接口
statement: >-
  在真实 q_star=103 的 c=8 high-R source 上，设一条实际 V-side strict raw prime
  q>2(p-1) 到达 (a,b,1)=(V/q,R-V/q,1)，令 h=gcd(a,M)，并令 a-side canonical
  capacity c_a<8。事实上，对每个这样的 high q endpoint 都有 b 不整除 K，故 Q_b>1；
  而 low gate 还强制 p 不整除 b、Q_a>1。因此同一 actual raw receipt 必满足双侧
  atomic split 的所有 source/p-free 算术前提；写 T_i=lcm(M,Q_i)/M，L=T_aT_b，
  split target capacity
  c_Sigma 满足 79 T_b c_Sigma+32 hq=0 (mod p)。更精确地，
  T_b=b/(2^epsilon*gcd(M,p^2+p-1-q))，其中 epsilon 只可能为 0,1,2,3；
  所以 split capacity 还满足一个无需分解 b 的二次 q-同余。低 gate 的 p-primary
  complement 不是未支付障碍：余下分支精确缩为双侧 split 的 independent capacity 与
  typed/priority 准入。本结论不将任一候选自动升级为
  terminal 或 E1--E5 edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-q-one-full-carrier-d-one-c-eight-v-side-direct-m-one-capacity-map
  - type-I-q-one-full-carrier-d-one-c-eight-universal-source-non-p-separation
  - type-I-path-anchored-atomic-split-complete-excess-admission
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

## 2. 高 \(q\) endpoint 的互补坐标永不饱和

**引理。** 在 (1)--(2) 的任意实际 \(q>2(p-1)\) endpoint 上，

\[
\boxed{b\nmid K,\qquad Q_b>1.}
\tag{5a}
\]

**证明。** 若 \(b\mid K\)，写 \(w=K/b\)。由 \(pR+1=4K\) 与 \(R=a+b\)，

\[
pa+1=b(4w-p).
\tag{5b}
\]

令 \(d=4w-p\)。它为正整数。又 \(a<R/2<b\)，所以

\[
d=\frac{pa+1}{b}<p+\frac1a<p+1.
\tag{5c}
\]

由于 \(d\equiv-p\equiv3\pmod4\) 而 \(p\equiv1\pmod4\)，必有
\(1\le d\le p-1\)。将 \(b=(pa+1)/d\)、\(R=a+b\) 代入
\(qa=R(p-1)-p\)，得到整数恒等式

\[
\bigl((p+d)(p-1)-dq\bigr)a=p(d-1)+1.
\tag{5d}
\]

右边正，故左侧括号是正整数，从而

\[
a\le p(d-1)+1\le(p-1)^2.
\tag{5e}
\]

另一方面，容量八闭式直接给出

\[
R-2(p^3+1)
=3124224s^3+36864s^2-1680s-5>0
\qquad(s\ge1).
\tag{5f}
\]

于是 (5b)、(5e) 和 \(b>R/2\) 导致

\[
1\le d=\frac{pa+1}{b}
<\frac{2\bigl(p(p-1)^2+1\bigr)}R
<1,
\tag{5g}
\]

矛盾。因此 \(b\nmid K\)。按 complete-excess 的定义，\(Q_b=1\) 当且仅当
\(b\mid K\)，故第二个结论也成立。 \(\square\)

## 3. 低 gate 排除互补坐标的 \(p\)-primary

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

## 4. 低 gate 的强制双侧完整 excess payload

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

低 gate 没有“a-side 没有可收费完整块”的遗漏，而第 2 节已经排除
\(Q_b=1\)。所以它被强制送入双侧 payload。由 (2)、(5)、(12) 及 (5a)，

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

这里的互补乘子也有一个不需要分解 \(b\) 的精确正规形。令

\[
g_b=(b,M),\qquad
e_b=v_2(b),\qquad e_M=v_2(M),
\tag{23}
\]

并定义

\[
\epsilon=
\begin{cases}
e_b-e_M,&1\le e_b-e_M\le3,\\
0,&\text{其它情形}.
\end{cases}
\tag{24}
\]

因为 \(q>2(p-1)\)，而 \((V,M)\mid67199\)，有 \((q,M)=1\)；又
\((p,M)=1\)。从 \(qb=p+R(q-p+1)\) 乘以 \(p\)，并使用
\(pR\equiv-1\pmod M\)，得到

\[
pq\,b\equiv p^2+p-1-q\pmod M.
\tag{25}
\]

两边的乘子都是 \(M\)-unit，故

\[
\boxed{g_b=(M,p^2+p-1-q).}
\tag{26}
\]

对 odd prime，complete-excess 只在 \(v_\ell(b)>v_\ell(M)\) 时带出
\(v_\ell(b)-v_\ell(M)\) 个指数；对 \(2\)，旧 capacity 额外有 \(2^3\)。逐素数比较
遂给出

\[
\boxed{T_b=\frac{b}{2^\epsilon g_b}.}
\tag{27}
\]

因此 (20) 也可写成

\[
L=\frac{ab}{h\,2^\epsilon g_b}.
\tag{28}
\]

模 \(p\) 下有 \(a\equiv-Rq^{-1}\)、\(b\equiv R(q+1)q^{-1}\)，且
\(4R\equiv79\)。将它们代入 \(Lc_\Sigma\equiv8\) 得到无需分解 \(b\) 的二次容量式：

\[
\boxed{
79^2(q+1)c_\Sigma+
128h\,2^\epsilon g_bq^2\equiv0\pmod p.
}
\tag{29}
\]

因此 a-side 命中低 gate 并不自动使 atomic split 的 \(c_\Sigma<8\)；互补完整块
\(T_b\) 必须单独进入容量比较。不过 (26)--(29) 已把这项比较压为 gcd、二进估值和
模运算，而不是 \(b\) 的一般因式分解。这不是 source 缺口： (18) 已支付双侧 payload 的
\(p\)-free 与 source 算术条件。余下的决定性问题是 (21) 的 strict capacity、目标 typed
reclassification 与 priority receipt。

## 5. 精确控制

已有 terminal-preempted c=8 控制 \(s=3279,p=157393\)，取 \(q=5963047\) 时，actual
raw endpoint 同时有两个完整 block：

\[
Q_a=3113076331159817,\qquad
Q_b=19138464436332689.
\tag{30}
\]

它们都与旧 support 互素，因此

\[
T_a=Q_a,\qquad T_b=Q_b,\qquad
L=T_aT_b=59579500651491202538305440357913.
\tag{31}
\]

在这里 \(g_b=3,\epsilon=1\)，故 (27) 直接重建 \(T_b\)。

该控制不命中 low gate；它给出

\[
c_a=11230,\qquad c_\Sigma=38261,
\tag{32}
\]

并直接满足 (4)、(22)、(29)。它只复核双侧公式和 raw payload，不作为 persistent
counterexample 或 selector edge。

## 6. 收紧后的边界

本卡没有证明每个容量八 source 都命中低 gate，也没有保证 (21) 严格下降。它新增的是：

- 对任何实际 low-gate endpoint，互补 \(p\)-primary 已被全称排除；
- 对每个高 \(q\) direct endpoint，\(Q_b>1\) 已全称成立，low gate 因而没有单侧
  adapter 分支；
- 双侧 source/p-free payload 已完整，(26)--(29) 使其容量只需 gcd、二进估值和模
  运算；唯一新增算术门仍是 (21) 的 capacity，而不是无来源的 formal rechart。

下一条有价值的对象是：对双侧分支，将 (29) 与 \(g_b\) 的可控结构连接到
\(c_\Sigma<8\)、terminal，或另一条全域可提升的严格势；不能再把 \(Q_b=1\) 或
\(p\mid b\) 当作开放 source-lineage 障碍。

聚焦复核：

~~~bash
python3 reproductions/type_i_q_one_full_carrier_d_one_c_eight_low_gate_complement_pfree_split_interface.py --verify
~~~

复现器只分解 56 个小常数 \(32h-79c\)，并重放一个既有 raw control；不扫描参数射线、
素数、factor target 或历史证书。
