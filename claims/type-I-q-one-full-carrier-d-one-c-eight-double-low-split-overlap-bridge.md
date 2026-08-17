---
kind: claim
claim_id: type-I-q-one-full-carrier-d-one-c-eight-double-low-split-overlap-bridge
title: q=1 容量八双低容量 split 的线性互补重叠桥
statement: >-
  在真实 q_star=103 的 c=8 high-q low-gate endpoint 中，若 a-side direct
  capacity c 与 atomic-split capacity c_Sigma 都在 {1,...,7}，令
  D=gcd(V,M)、g_b=gcd(b,M)、epsilon in {0,1,2,3} 为互补二进修正、
  u=2^epsilon*g_b，则 (79c-32D)c_Sigma=4u c^2 (mod p)。q_star=103
  的八个 D-CRT 下界使左侧绝对值严格小于 p，故存在唯一 k>=0 使
  4u c^2=(79c-32D)c_Sigma+kp。k=0 的唯一算术可能是
  (D,c,c_Sigma,u)=(1,1,4,47)，并强制 epsilon=0、g_b=47；其余所有
  double-low branch 都满足
  g_b>=(p-7|79c-32D|)/(32c^2)，特别地
  p<=1568g_b+15052023。因而除了该固定 marker 外，任何 split 再次降到
  c_Sigma<8 的路径都必须携带随 p 线性增长的互补旧支撑重叠。此结论不证明
  double-low branch 存在、terminal、typed admission、E1--E5 或全局 exit。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-q-one-full-carrier-d-one-c-eight-high-q-shared-defect-rigidity
  - type-I-q-one-full-carrier-d-one-c-eight-low-gate-complement-pfree-split-interface
  - type-I-q-one-full-carrier-d-one-c-eight-qstar-103-low-gate-odd-carry-rays
topics:
  - type-I
  - q-one
  - full-carrier
  - c-eight
  - q-star-103
  - low-gate
  - atomic-split
  - complement-overlap
  - capacity-map
  - proof-boundary
sources:
  - claim: type-I-q-one-full-carrier-d-one-c-eight-low-gate-complement-pfree-split-interface
    role: p-free-two-sided-payload-and-complement-multiplier
  - claim: type-I-q-one-full-carrier-d-one-c-eight-high-q-shared-defect-rigidity
    role: fixed-source-defect-and-disjointness
  - claim: type-I-q-one-full-carrier-d-one-c-eight-qstar-103-low-gate-odd-carry-rays
    role: eight-defect-CRT-lower-thresholds
  - reproduction: reproductions/type_i_q_one_full_carrier_d_one_c_eight_double_low_split_overlap_bridge.py
    role: bridge-identity-fixed-quotient-menu-and-two-raw-controls
visibility: public
last_checked: '2026-08-17'
---

# q=1 容量八双低容量 split 的线性互补重叠桥

## 1. 输入与目标

保留真实 \(q_\star=103\) 的容量八 high-\(q\) source：

\[
p=48s+1,\qquad K=8M,\qquad pR+1=4K.
\tag{1}
\]

取一条实际 \(V\)-side strict raw prime \(q>2(p-1)\)，其 \(m=1\) endpoint 为

\[
(a,b)=\left(\frac Vq,R-\frac Vq\right).
\tag{2}
\]

写

\[
D=(V,M)=(a,M),\qquad
g_b=(b,M),
\tag{3}
\]

并令 \(\epsilon\in\{0,1,2,3\}\) 是已有双侧 split 正规形中的二进修正：

\[
T_b=\frac{b}{2^\epsilon g_b}.
\tag{4}
\]

这里 \((D,g_b)=1\)。设 a-side direct capacity 和 split canonical capacity 分别为

\[
c=\left\langle8(a/D)^{-1}\right\rangle_p,
\qquad
C=c_\Sigma=\left\langle8(T_aT_b)^{-1}\right\rangle_p.
\tag{5}
\]

本卡只研究最窄、也最有希望产生 E5 的 double-low 子域：

\[
1\le c\le7,\qquad1\le C\le7.
\tag{6}
\]

令

\[
u:=2^\epsilon g_b.
\tag{7}
\]

目标不是声称 (6) 必然发生，而是精确量化：一旦它发生，互补旧支撑重叠 \(g_b\) 还剩多少自由度。

## 2. 线性重叠--容量桥

已有 a-side low-gate 与双侧 split 容量式分别为

\[
79c+32Dq\equiv0\pmod p,
\tag{8}
\]

\[
79T_bC+32Dq\equiv0\pmod p.
\tag{9}
\]

相减并使用 \(p\ne79\)，得到

\[
T_bC\equiv c\pmod p.
\tag{10}
\]

另一方面，\(qa=V\equiv-R\pmod p\) 且 \(b=R-a\)，所以

\[
qb\equiv R(q+1)\pmod p.
\tag{11}
\]

容量八 source 还有 \(4R\equiv79\pmod p\)。将 (4)、(10)--(11) 合并，先得

\[
79(q+1)C\equiv4ucq\pmod p.
\tag{12}
\]

再用 (8) 消去 \(q\)，即得本卡的核心恒等式：

\[
\boxed{(79c-32D)C\equiv4uc^2\pmod p.}
\tag{13}
\]

这比此前的二次 \(q\)-容量式更适合研究 double-low：它完全消去了 raw prime \(q\)、大端点
\(a,b\) 和 \(T_b\)，只留下固定 defect、两个小容量与可解释的互补重叠 \(u\)。

## 3. q-star=103 的小整数提升

实际 \(q_\star=103\) source 的 defect 只可能为

\[
\mathcal D=\{1,11,41,149,451,1639,6109,67199\}.
\tag{14}
\]

odd-carry-ray 的 CRT 阈值给出每个 \(D\) 的 \(p\) 下界。对 (6) 中的全部 49 个
\((c,C)\)，令

\[
A_{D,c,C}=(79c-32D)C.
\tag{15}
\]

逐个 \(D\) 的精确最大值如下：

| \(D\) | actual \(p\) 的下界 | \(\max_{1\le c,C\le7}|A_{D,c,C}|\) |
|---:|---:|---:|
| 1 | 4,129 | 3,647 |
| 11 | 14,017 | 1,911 |
| 41 | 58,513 | 8,631 |
| 149 | 632,017 | 32,823 |
| 451 | 666,625 | 100,471 |
| 1,639 | 2,841,985 | 366,583 |
| 6,109 | 4,315,297 | 1,367,863 |
| 67,199 | 245,938,465 | 15,052,023 |

所以所有 actual double-low input 都满足

\[
\boxed{|A_{D,c,C}|<p.}
\tag{16}
\]

式 (13) 因而不再只是模 \(p\) 条件：存在唯一整数 \(k\) 使

\[
\boxed{4uc^2=A_{D,c,C}+kp.}
\tag{17}
\]

左侧为正且 (16) 成立，故 \(k\ge0\)。

## 4. 唯一零 carry marker

若 \(k=0\)，则 \(A_{D,c,C}>0\) 且

\[
4c^2\mid A_{D,c,C},
\qquad
u=\frac{A_{D,c,C}}{4c^2}.
\tag{18}
\]

这只是八个 \(D\)、七个 \(c\)、七个 \(C\) 的固定常数表；它不是参数扫描。直接逐项约化得到

\[
\boxed{
k=0
\Longrightarrow
(D,c,C,u)=(1,1,4,47).}
\tag{19}
\]

反向代入确有

\[
(79-32)\cdot4=188=4\cdot47.
\tag{20}
\]

因为 \(u=2^\epsilon g_b=47\) 且 \(47\) 为奇数，(19) 还强制

\[
\boxed{\epsilon=0,\qquad g_b=47.}
\tag{21}
\]

重要的是，(19) 是一个剩余 marker，不是实际 endpoint 存在性结论。它仅说明：
若 bounded-overlap double-low 想避开宏观重叠，必须精确落在这一个
\((D,c,C,\epsilon,g_b)=(1,1,4,0,47)\) 分支。

## 5. 非异常分支必须有宏观互补重叠

在 (19) 以外，\(k\ge1\)。由 (17)、(15) 与 \(2^\epsilon\le8\)，有

\[
\begin{aligned}
4uc^2&\ge p-|A_{D,c,C}|,\\
g_b
&\ge
\frac{p-7|79c-32D|}{32c^2}.
\end{aligned}
\tag{22}
\]

这给出一个可直接用于后续因子分配的必要条件。特别地，因
\(c^2\le49\)，并由表中的全局最大值，

\[
\boxed{
p\le32c^2g_b+7|79c-32D|
\le1568g_b+15\,052\,023.}
\tag{23}
\]

因此，除唯一 marker (21) 外，若 \(g_b\) 被固定常数或任何严格次线性候选策略限制，
它至多覆盖一个显式有界的 \(p\) 区间。对无界 source，split 再次降到
\(C<8\) 必须伴随至少线性尺度的 \(g_b=(b,M)\)。

这把下一步从“继续筛 seven carry rays”改为两个互斥且可核查的数学对象：

1. 分析单一 \(D=1,c=1,C=4,g_b=47\) marker 是否能实际满足 quartic ray、typed
   admission 和 priority；
2. 对非异常 branch，按 \(M=9s(176s+5)(3168s^2+24s-1)\) 的大因子研究宏观
   \(g_b\) 是否强制 terminal、另一条 lift，或更强的良基下降。

## 6. 边界

本卡没有证明任何 actual high-\(q\) endpoint 命中 a-side low gate 或 split low gate；
更没有把 (13) 自动提升为 verified_edge。终端优先、typed state、source/path receipt、
全域解提升和 E1--E5 仍需独立支付。

它已排除的只是一个不充分的全域设想：不能期待由 bounded complementary overlap 的普通
double-low split 自动解决容量八残余。除 (21) 这个显式 marker 外，任何该类候选都必须
解释一个随 \(p\) 增长的旧支撑重叠。

聚焦复核：

~~~bash
PYTHONPATH=reproductions python3 \
  reproductions/type_i_q_one_full_carrier_d_one_c_eight_double_low_split_overlap_bridge.py \
  --verify
~~~

复现器只检查八行 CRT 常数、392 个固定小整数量词、桥恒等式和两个既有 actual raw
controls；不扫描 source 参数、素数、\(V\) 的因子或历史 certificate。
