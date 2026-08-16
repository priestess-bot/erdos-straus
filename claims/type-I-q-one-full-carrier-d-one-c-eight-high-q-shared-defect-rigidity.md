---
kind: claim
claim_id: type-I-q-one-full-carrier-d-one-c-eight-high-q-shared-defect-rigidity
title: q=1 容量八 high-q endpoint 的共享缺陷刚性
statement: >-
  在 c=8 high-R source S=(p,V,p-1) 中，令 p=48s+1、s>=86、K=8M，
  D_s=gcd(V,M)=gcd(V,K)。对任意实际 V-side strict raw prime q>2(p-1)，
  其 m=1 endpoint 为 (a,b)=(V/q,R-V/q)，并满足
  gcd(a,M)=D_s、gcd(D_s,gcd(b,M))=1。精确地，
  D_s 是 11、41、149 中满足 s=6 mod11、s=30 mod41、s=55 mod149 的素数之积。
  因此 a-side capacity low gate 对每个固定 source 只有七个 q mod p 残余类，
  而非可独立选择的八个 h-defect 和七个 capacity 的 56 个混合 gate；双侧 split
  公式中的 h 也可唯一替换为 D_s。结论不保证任一残余类空、c_Sigma<8、terminal
  或 E1--E5 edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-q-one-full-carrier-d-one-c-eight-universal-source-non-p-separation
  - type-I-q-one-full-carrier-d-one-c-eight-v-side-direct-m-one-capacity-map
  - type-I-q-one-full-carrier-d-one-c-eight-low-gate-complement-pfree-split-interface
topics:
  - type-I
  - q-one
  - full-carrier
  - c-eight
  - high-q
  - source-support
  - capacity-map
  - atomic-split
  - proof-boundary
sources:
  - claim: type-I-q-one-full-carrier-d-one-c-eight-universal-source-non-p-separation
    role: exact-shared-support-table-and-actual-raw-source
  - claim: type-I-q-one-full-carrier-d-one-c-eight-v-side-direct-m-one-capacity-map
    role: direct-capacity-congruence
  - claim: type-I-q-one-full-carrier-d-one-c-eight-low-gate-complement-pfree-split-interface
    role: split-capacity-and-complementary-overlap-formula
  - reproduction: reproductions/type_i_q_one_full_carrier_d_one_c_eight_high_q_shared_defect_rigidity.py
    role: residue-defect-table-and-nontrivial-high-q-control
visibility: public
last_checked: '2026-08-17'
---

# q=1 容量八 high-\(q\) endpoint 的共享缺陷刚性

## 1. 固定 source 的缺陷不是一项选择变量

保留容量八 high-\(R\) source 的记号

\[
p=48s+1,\qquad s\ge86,\qquad K=8M,
\]

\[
pR+1=4K,\qquad V=R(p-1)-p.
\tag{1}
\]

定义 source 的共享缺陷

\[
D_s=(V,M).
\tag{2}
\]

由于 \(V\) 为奇数，(1) 立即给出

\[
D_s=(V,K).
\tag{3}
\]

已有 source-side 支撑分离证明 \(D_s\mid11\cdot41\cdot149\)，并给出每个素数
出现的充要剩余。故不是只知道一个上界，而是有精确式

\[
\boxed{
D_s=
11^{[s\equiv6\ (11)]}
41^{[s\equiv30\ (41)]}
149^{[s\equiv55\ (149)]}.
}
\tag{4}
\]

这里 \([P]\) 为命题 \(P\) 的 \(0/1\) 指示数。因 (4) 的每个指数至多一，
\(D_s\) 是由根参数 \(s\) 单独决定的八值量，不依赖随后选择哪一个 raw prime。

## 2. high-\(q\) raw edge 保留全部 source 缺陷

取任意实际 \(V\)-side strict raw prime

\[
q\mid V,\qquad v_q(V)>v_q(K),\qquad q>2(p-1),
\tag{5}
\]

并写

\[
a=\frac Vq,\qquad b=R-a.
\tag{6}
\]

它的 raw receipt 无 gcd reduction 地到达 \((a,b,1)\)，所以 \((a,b)=1\)。

若 \(q\mid M\)，由 \(q\mid V\) 可得 \(q\mid D_s\)。但 (4) 的素因子仅为
\(11,41,149\)，而

\[
q>2(p-1)\ge8256.
\tag{7}
\]

这是矛盾。因此

\[
(q,M)=1.
\tag{8}
\]

逐素数比较 (6)、(8) 的估值，得到

\[
\boxed{
(a,M)=\left(\frac Vq,M\right)=(V,M)=D_s.
}
\tag{9}
\]

这说明已有容量图中写作 \(h=(a,M)\) 的量，在 fixed source 的 high-\(q\) 子域内
不是一项 endpoint defect，而是预先确定的 source invariant。

令

\[
g_b=(b,M).
\tag{10}
\]

由 \(D_s\mid a\)、\((a,b)=1\) 和 \(g_b\mid b\)，还得到

\[
\boxed{(D_s,g_b)=1.}
\tag{11}
\]

所以 a-side 的全部旧 support overlap 与 b-side 的旧 support overlap 也不共享
\(11,41,149\) 的 defect token。

## 3. 每个实际 source 只有七个 direct low gates

令

\[
T_a=\frac a{D_s},
\qquad
c_a=\langle8T_a^{-1}\rangle_p.
\tag{12}
\]

已有 direct \(m=1\) capacity map 的线性式现在成为

\[
\boxed{79c_a+32D_s q\equiv0\pmod p.}
\tag{13}
\]

因此，对固定的 \(s\)，定义

\[
\mathcal C_p(D_s)=
\left\{
-79r(32D_s)^{-1}\pmod p:1\le r\le7
\right\}.
\tag{14}
\]

因为 \(p\ge4129\)，(14) 中七个残余彼此不同，且

\[
\boxed{
c_a<8
\Longleftrightarrow
q\bmod p\in\mathcal C_p(D_s).
}
\tag{15}
\]

原先的 \(\{h\mid67199\}\times\{1,\ldots,7\}\) 给出的是整个参数族的
\(8\cdot7\) 个可能式；(9) 证明一个实际 root source 只落在其中一个 \(h=D_s\)
fiber。故任何后续试图排除或命中 low gate 的论证只需处理该 source 的七个 residue
classes，不能再把 \(h\) 当作与 \(q\) 独立的 selector choice。

进一步地，[low gate 的四次 carry 商参数化](type-I-q-one-full-carrier-d-one-c-eight-low-gate-quartic-carry-parameterization.md)
把这七类中的 \(q\mid V\) 条件精确改写为固定四次式的素因子条件和 \(p\) 的线性
重建。该参数化仍有无界 carry 商，因而不是本节 seven-gate 菜单的排空证明。

## 4. 对 atomic split 的精确影响

在 low gate 上，已有双侧 payload 给出

\[
79T_b c_\Sigma+32hq\equiv0\pmod p,
\]

\[
T_b=\frac{b}{2^\epsilon g_b}.
\tag{16}
\]

由 (9)--(11)，它可唯一重写为

\[
\boxed{
79T_b c_\Sigma+32D_s q\equiv0\pmod p,
\qquad
(D_s,g_b)=1.
}
\tag{17}
\]

这消除了 split capacity 式中一项表面上的 source/endpoint 混合自由度，但没有控制
\(g_b\) 的其余素因子，也没有推出 \(c_\Sigma<8\)。所以 (17) 是下一步的精确输入，
不是一条已经支付 E5 的 edge。

## 5. 非平凡控制

取

\[
s=116,\qquad p=5569,\qquad D_s=11.
\tag{18}
\]

这里 \(q=578581\) 是一个实际 strict \(V\)-side raw prime，且

\[
(p,V,p-1)\xrightarrow q
(50259113795,5172256748028,1).
\tag{19}
\]

直接重算给出

\[
(q,M)=1,\quad (a,M)=11,\quad (b,M)=12,\quad (11,12)=1,
\tag{20}
\]

并且

\[
c_a=4202,\qquad79c_a+32\cdot11\cdot578581\equiv0\pmod{5569}.
\tag{21}
\]

这个控制不命中 low gate，也不声称 \(p=5569\) 是 persistent root；它只检验
非平凡 \(D_s\) 时 (9)、(11)、(13) 的实际 raw 算术。

## 6. 边界

本引理没有证明下列任何更强结论：

- \(\mathcal C_p(D_s)\) 在真实 \(q_\star=103\) rough 域中为空；
- 某个实际 \(V\) 因子一定命中 (14)；
- low-gate atomic split 的 \(c_\Sigma<8\)，或其 target 已有 typed E1--E5 admission；
- G/Type I global exit。

它只把当前决定性门从一个表面上的 \(56\) 格 mixed-defect 菜单，压成每个实际 source
的 \(7\) 格 \(q\)-residue 问题，并证明互补 overlap 不会重新携带同一 defect。

聚焦复核：

~~~bash
PYTHONPATH=reproductions python3 \
  reproductions/type_i_q_one_full_carrier_d_one_c_eight_high_q_shared_defect_rigidity.py --verify
~~~

复现器只重放 (4)、(9)、(11)、(13) 的固定 residue table 和一个 nontrivial raw receipt；
不扫描参数、素数、endpoint 或 certificate menu。
