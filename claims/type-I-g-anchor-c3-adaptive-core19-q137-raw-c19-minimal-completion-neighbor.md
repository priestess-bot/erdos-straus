---
kind: claim
claim_id: type-I-g-anchor-c3-adaptive-core19-q137-raw-c19-minimal-completion-neighbor
title: q=137 raw C=19 的最小双 raw 因子完成与正规形纤维近邻
statement: 在 q=137 actual raw family p(w)=193+772716168w 的固定 candidate N=p+16 中，任何含 raw endpoint 19 且满足 target 条件 h=-1 (mod 8) 的因子唯一写成 h=19r、r=5 (mod 8)。它在该 affine family 上可实现当且仅当 gcd(r,40669272)=1；此时唯一参数类为 w=-11*40669272^(-1) (mod r)。故最小完成是 r=5、h=95、w=2 (mod 5)，而既有 h=247 是 r=13 的同一分类实例。进一步限制 w=27+25u，则每个 prime parameter 都有 actual raw word 137;5;Fac(Q/5) 到达 endpoint 19，且 N=95(219614071+203346360u) 满足 v_5(N)=v_19(N)=1。因此 actual raw 5-edge 和 actual raw 19-endpoint 无条件单射到同一 (D,a)=(2,2) candidate fiber 的两个不同 layer-one factor token，target h=95 正是它们的乘积。其直接 Type II 因子生成器 (A,B,C,K)=(2,B_u,1,12) 经 gcd(A,B_u)=2 规范化为 (1,B_u/2,4,6)，保持 N、h、m、x、d 和单位分数证书，并把模数 8 送到 16。新商 C=4 非平方自由，故该 8->16 映射仅是严格的 factor-normal-form 纤维近邻，不是 admissible source-switch fiber、Fourier demand、容量或 selector edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-c3-adaptive-core19-q137-first-entry-family
  - type-I-g-anchor-c3-adaptive-core19-q137-raw-c19-same-fiber-owner
  - type-II-coprime-factor-normal-form
  - type-II-same-modulus-source-switch-crt-criterion
topics:
  - type-I
  - type-II
  - q137
  - core19
  - raw-source
  - source-owner
  - target-factor
  - target-fiber-neighbor
  - normal-form
  - CRT
  - terminal-first
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_c3_adaptive_core19_q137_raw_c19_minimal_completion.py
    role: minimal completion classification, actual two-atom raw control, and normalization-neighbor certificate
visibility: public
last_checked: '2026-08-08'
---

# q=137 raw (C=19) 的最小双 raw 因子完成与正规形纤维近邻

此前的 [q=137 raw (C=19) 同纤维 owner 控制](type-I-g-anchor-c3-adaptive-core19-q137-raw-c19-same-fiber-owner.md)
取补因子 (13)，得到 target (247=19\cdot13)。这里证明：在同一个

\[
N(w)=p(w)+16
\tag{1}
\]

candidate 中，含 raw endpoint (19) 的最小可行 target 实际是

\[
\boxed{95=19\cdot5}.
\tag{2}
\]

它不仅更小，补因子 (5) 还是同一条 actual raw transcript 的真实边标签。结果因而
给出两个不同 raw 原子到同一 candidate factor layer 的算术 owner 映射。它也暴露一个
必要边界：这张 Type II 证书的互素规范化会把模数 (8) 移到 (16)，而新的 quotient
不是 squarefree；所以该近邻不能被记为 source-switch 或容量边。

## 1. 固定 (N=p+16) 中所有 19-target completion 的精确分类

q=137 actual raw family 是

\[
p(w)=193+772716168w,
\qquad
772716168=19\cdot40669272.
\tag{3}
\]

在 ((D,a,c,M)=(2,2,1,8)) candidate fiber 中，

\[
N(w)=p(w)+aM=p(w)+16
=19\bigl(11+40669272w\bigr).
\tag{4}
\]

考虑一个确实包含 raw endpoint (19) 的 target 因子 (h=19r)。同模数
source-switch 的 target parity 是

\[
h\equiv-1\pmod8.
\tag{5}
\]

因 (19\equiv3\pmod8)，这等价于

\[
r\equiv5\pmod8.
\tag{6}
\]

另一方面，由 (4)，

\[
19r\mid N(w)
\Longleftrightarrow
r\mid11+40669272w.
\tag{7}
\]

令 (g=(r,40669272))。线性同余 (7) 可解当且仅当 (g\mid11)。而

\[
(11,40669272)=1,
\tag{8}
\]

所以得到精确的、无搜索的分类：

\[
\boxed{
\begin{aligned}
19r\mid N(w)\ \text{for some }w
&\Longleftrightarrow (r,40669272)=1,\\
w&\equiv-11\,(40669272)^{-1}\pmod r.
\end{aligned}}
\tag{9}
\]

这里仍须联用 (6)。最小正 (r\equiv5\pmod8) 是 (5)，且

\[
(5,40669272)=1,
\qquad
w\equiv2\pmod5.
\tag{10}
\]

故 (2) 是此 fixed candidate fiber 中的最小 (19)-containing target。作为交叉检查，
(r=13) 时 (9) 给 (w\equiv4\pmod {13})，恰好恢复此前的
(247=19\cdot13) 控制。相反，(r=21) 时
((21,40669272)=21\nmid11)，给出一张严格的 target-tuning 空回执。

## 2. 最小完成的 exact-height raw 子射线

为同时冻结 (5) 和 (19) 的 candidate height，进一步取

\[
w=27+25u,
\qquad u\ge0.
\tag{11}
\]

则

\[
\begin{aligned}
p_u&=20863336729+19317904200u,\\
N_u=p_u+16
&=95\bigl(219614071+203346360u\bigr).
\end{aligned}
\tag{12}
\]

括号内分别恒为 (1\pmod5) 与 (6\pmod {19})，所以

\[
v_5(N_u)=v_{19}(N_u)=1.
\tag{13}
\]

初项与步长互素，且为 (1,0\pmod {24})。Dirichlet 定理给出无穷多个 prime
parameters；它们都仍在既有 q=137 actual raw family 内。

在同一子射线上，已有 raw block 的尾因子为

\[
Q_u=4723572715+4373678400u
=5\bigl(944714543+874735680u\bigr),
\tag{14}
\]

而括号恒为 (3\pmod5)。既有 q=137 family 已经证明
((Q_u,K_uR_u)=1)；故对每个 prime parameter，实际 raw word 可以固定以

\[
137;\ 5;\ \operatorname{Fac}(Q_u/5)
\tag{15}
\]

开始，并到达 endpoint (19)。这里 (5) 是一条 exact-height actual raw edge，
(19) 是 exact-height actual raw endpoint。

在 (u=0)，

\[
p=20863336729,
\qquad Q/5=944714543
\tag{16}
\]

均被复现器认证为 prime（前者通过两层 Pocklington：
(66869669-1=2^2\cdot3701\cdot4517)，
(p-1=2^3\cdot3\cdot13\cdot66869669)）。所以

\[
(1,137),(1,5),(0,944714543)
\tag{17}
\]

给出一条完全展开的 actual primitive control 到 ((19,R-19,1))。

定义两个不同的 occurrence atom：

\[
\begin{aligned}
\alpha_u(\omega_{5,u},1)&=((D,a),5,1),\\
\alpha_u(\omega_{19,u},1)&=((D,a),19,1),
\qquad (D,a)=(2,2).
\end{aligned}
\tag{18}
\]

式 (13) 使其成为到同一 candidate (N_u) 的两个不同 layer-one token 的单射。
并且

\[
\{1,5\}\{1,19\}
=\{1,5\}\{1,3\}=U(8),
\qquad5\cdot19\equiv-1\pmod8.
\tag{19}
\]

因此 (2) 是两个实际 raw 因子共同进入同一 target product 的控制，而不是一个
endpoint 与任意补因子的数值重合。

## 3. 直接 Type II 终端

取

\[
(A,C,K)=(2,1,12),
\qquad h=4ACK-1=95,
\tag{20}
\]

并令

\[
B_u=2635368850+2440156320u
=12\bigl(219614071+203346360u\bigr)-2.
\tag{21}
\]

有 (95B_u=12p_u+2)，以及

\[
m_u=\frac{2+B_u}{12}=\frac{N_u}{95},
\quad
x_u=2B_u,
\quad d=4.
\tag{22}
\]

于是每个 prime (p_u) 都有

\[
\boxed{
\frac4{p_u}
=\frac1{2B_u}
+\frac1{24p_u}
+\frac1{12B_up_u}.}
\tag{23}
\]

特别地 (u=0) 给出

\[
\frac4{20863336729}
=\frac1{5270737700}
+\frac1{500720081496}
+\frac1{659791052672009899800}.
\tag{24}
\]

## 4. 一般的规范化纤维近邻引理

下面的代数说明为什么 (23) 不能被粗暴登记为原 (M=8) source-switch fiber 的
互素 normal form。

**规范化近邻引理。** 设一张 Type II 因子表示满足

\[
p=4ABC-m,
\qquad m=\frac{A+B}{K},
\qquad 0<m<p,
\tag{25}
\]

但暂不要求 ((A,B)=1)。令 (g=(A,B))，写

\[
A'=A/g,\quad B'=B/g,\quad C'=g^2C,\quad K'=K/g.
\tag{26}
\]

则 (g\mid K)，而 (26) 是同一张证书的唯一互素正规形：

\[
\begin{aligned}
p&=4A'B'C'-m, & m&=\frac{A'+B'}{K'},\\
A^2C&=A'^2C', & ABC&=A'B'C',\\
4ACK-1&=4A'C'K'-1.
\end{aligned}
\tag{27}
\]

若把 factor representation 写成 source-switch 参数

\[
D=AC,\quad a=A,\quad M=4D,
\tag{28}
\]

则正规化后的参数为

\[
D'=A'C'=gD,\quad a'=A/g,\quad M'=gM,
\qquad aD=a'D'=A^2C,
\tag{29}
\]

并且 (h+1=MK=M'K')。所以两边共享完全相同的 candidate integer
(p+4aD)、target factor、缺口、除子与 Type II identity；它们是一个严格的
normal-form target-fiber neighbor。

为证明 (g\mid K)，令 (A=ga,B=gb)。由 (p=4ABC-m) 和
(0<m<p) 可知 ((m,ABC)=1)。又 Type II 条件给

\[
m\mid ABC+A^2C=g^2aC(a+b).
\tag{30}
\]

故 (m\mid a+b)，从而 (K=g(a+b)/m) 被 (g) 整除。其余各式直接代入即得。

对于 (20)--(21)，恒有 (g=(2,B_u)=2)，所以

\[
(A',B',C',K')=(1,B_u/2,4,6),
\tag{31}
\]

并得到

\[
(D,a,M)=(2,2,8)
\longmapsto(D',a',M')=(4,1,16).
\tag{32}
\]

这里新 quotient (D'/a'=4) 非 squarefree。因而 (32) 是 target 的
normal-form 邻接，不是同模数 source-switch 的 admissible fiber，也没有生成任何
严格递降。

## 5. 边界

本卡推进的是两个明确而有限的对象：最小 (19)-containing target completion 的完整
算术分类，以及两个 actual raw atom 的同 candidate owner 映射。它仍未建立：

* F/G fixed layer、源差分群或 canonical Fourier role；
* independent typed Fourier/source demand；
* Hall request、demand-to-slot injection、Kneser price 或容量 surplus；
* admissible (8\to16) source-switch、全称 owner functor、selector edge 或递降。

窄复现：

```bash
python3 reproductions/type_i_c3_adaptive_core19_q137_raw_c19_minimal_completion.py --verify
```
