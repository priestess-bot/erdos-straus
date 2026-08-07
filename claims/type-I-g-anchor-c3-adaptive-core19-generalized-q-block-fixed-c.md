---
kind: claim
claim_id: type-I-g-anchor-c3-adaptive-core19-generalized-q-block-fixed-c
title: c=3 core-19 的广义 q 三段 raw 语言与 C=19^2 固定 RESET 实际族
statement: 设 high-R chart 的 swapped canonical anchor 满足 q 与 KR 互素、c|K，且 R-1=q bQ1、(q-1)R+b=q aQ2、R-a=qcQ3。若每个 Qi 的素因子都是 R-unit，且对其相应 endpoint b、a、c 保留严格 K-capacity，则 side schedule q;Fac(Q1);q;Fac(Q2);q;Fac(Q3) 是到 (c,R-c,1) 的 actual primitive raw word。该统一 q=5 的既有 C=19 grammar。对 ambient core-19 ray，取 c=361、q=5、b=11246、a=386，三式同时成立当且仅当 v=1085244 (mod 20619541)。进一步限制 v=1085244+20619541*1090735887676059709266*t 后，有限 determinant-prime set 强制全部 Qi 与 K、R 互素；因而该 primitive progression 的每个 prime parameter 都有 actual C=361 raw receipt，并固定 reset 到 R=747。该无穷实际族尚无 terminal-free point 或 E1--E5 selector edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-c3-adaptive-core19-c19-atomic-reset
  - type-I-overflow-a-one-dual-outer-rank-reset
  - type-I-g-anchor-c3-adaptive-core19-ambient19-terminal-screen
topics:
  - type-I
  - c3
  - core19
  - raw-source
  - factor-block
  - fixed-c
  - dual-reset
  - infinite-family
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_c3_adaptive_core19_generalized_q_block_fixed_c.py
    role: generalized q-block congruences and reserve-stable C=19^2 ray
visibility: public
last_checked: '2026-08-07'
---

# 广义 q 三段 raw 语言与 C=19^2 实际族

本卡把现有 `C=19` 的三个 \(5\)-block 提升为一个固定 \(c\) 的 raw language，
并给出第一个不只是 \(c=19\) 的实际核心-19 prime family。它不是 selector
覆盖定理。

## 1. 广义 q-block 引理

设

\[
pR+1=4K,\qquad (q,KR)=1,\qquad c\mid K,
\tag{1}
\]

其中 \(q\) 为素数。取正整数 \(a,b,Q_1,Q_2,Q_3\)，满足

\[
R-1=qbQ_1,
\qquad (q-1)R+b=qaQ_2,
\qquad R-a=qcQ_3.
\tag{2}
\]

对每个 \(Q_i\) 的素因子 \(\ell\)，要求它是 \(R\)-unit，并保留相应 endpoint
的 strict capacity：

\[
\begin{aligned}
\ell\mid Q_1&\Longrightarrow v_\ell(b)\ge v_\ell(K),\\
\ell\mid Q_2&\Longrightarrow v_\ell(a)\ge v_\ell(K),\\
\ell\mid Q_3&\Longrightarrow v_\ell(c)\ge v_\ell(K).
\end{aligned}
\tag{3}
\]

从 swapped anchor \((R-1,1,1)\) 出发，采用如下 side schedule：先在左侧做
\(q;\operatorname{Fac}(Q_1)\)，再在右侧做 \(q;\operatorname{Fac}(Q_2)\)，
最后在右侧做 \(q\)，然后在左侧做 \(\operatorname{Fac}(Q_3)\)。则它到达

\[
(c,R-c,1).
\tag{4}
\]

确实，第一段把 \(R-1\) 化到 \(b\)。第二个 \(q\)-step 后，互补坐标是

\[
R-\frac{R-b}{q}=\frac{(q-1)R+b}{q}=aQ_2,
\]

所以第二个 factor block 到达 \((a,R-a,1)\)。最后一个 \(q\)-step 的被除坐标为

\[
\frac{R-a}{q}=cQ_3,
\]

第三个 block 因而到达 (4)。式 (3) 是每一段末次剥离的容量条件；\(R\)-unit
条件和 \((q,KR)=1\) 给 unit condition，所有步骤都保持 \(m=1\)，故没有
gcd reduction。反向 replay 也强制 (2)--(3)，所以这给出指定 side topology 的
完整刻画。

一旦 (4) 是已解码 raw leaf，固定-\(c\) RESET 引理适用：令

\[
1\le\rho<4c,\qquad \rho p\equiv-1\pmod {4c},
\tag{5}
\]

则 r-side target 是

\[
\boxed{(R_\rho,K_\rho)=\left(\rho,\frac{\rho p+1}{4}\right).}
\tag{6}
\]

## 2. C=19^2 的同余射线

保留既有 ambient core-19 ray

\[
\begin{aligned}
p(v)&=181740263041+204127330680v,\\
R(v)&=787541139831+884551766280v.
\end{aligned}
\tag{7}
\]

在 (2) 中取

\[
q=5,\qquad c=361,\qquad b=11246,\qquad a=386.
\tag{8}
\]

前两个整除条件分别给

\[
v\equiv5\pmod {5623},\qquad v\equiv5\pmod {193},
\tag{9}
\]

而最后一个条件 \(R-a\equiv0\pmod {5\cdot361}\) 给

\[
v\equiv2\pmod {19}.
\tag{10}
\]

CRT 因而给出唯一 progression

\[
\boxed{v\equiv1085244\pmod {20619541}.}
\tag{11}
\]

在这个 progression 上 \(h\equiv160\pmod {361}\)。此时 \(26h+1\) 与
\(p-3\) 各含一个 \(19\) 因子，所以 \(361\mid K\)。同时

\[
747p\equiv-1\pmod {1444},
\]

故 (6) 固定为

\[
\boxed{(R_\rho,K_\rho)=\left(747,\frac{747p+1}{4}\right).}
\tag{12}

第一个 parameter 的

\[
p=221528142596748961
=2579\cdot282413\cdot304153543
\tag{13}
\]

不是素数。以下证明一个更细的 CRT 限制会同时关闭所有 factor-reserve 和 unit gate。

## 3. reserve-stable 实际 raw 子族

写

\[
v=1085244+20619541z.
\tag{14}
\]

在这个参数中，\(p,M=26h+1,x=p-3\) 和三个 block 都是 affine form：

\[
\begin{aligned}
p&=221528142596748961+4209011864176817880z,\\
M&=239988821146478041+4559762852858219370z,\\
x=p-3&=221528142596748958+4209011864176817880z,\\
Q_1&=17071941749705+324365132694876z,\\
Q_2&=1989544631266145+37801142821622544z,\\
Q_3&=531831182596073+10104737624062536z.
\end{aligned}
\tag{15}
\]

对任意两条 affine form \(A_0+A_1z,B_0+B_1z\)，其公共素因子必整除
\(A_0B_1-A_1B_0\)。应用到六对 \((Q_i,M)\)、\((Q_i,x)\) 后，其 determinant
的所有素因子都落在

\[
\mathcal S=
\{2,3,7,13,17,19,29,61,101,167,191,193,5623\}.
\tag{16}
\]

这里不是只记录 radical：复现器逐一检查六个 determinant 的完整素因子分解。令

\[
\mathcal L=\prod_{\ell\in\mathcal S}\ell
=1090735887676059709266,
\qquad z=\mathcal Lt.
\tag{17}
\]

三个常数项 \(Q_i(0)\) 都不被 \(\mathcal S\) 中的任何素数整除，而
\(Q_i(\mathcal Lt)\equiv Q_i(0)\pmod\ell\) 对每个 \(\ell\in\mathcal S\) 成立。
determinant 引理因而给出

\[
\gcd(Q_1Q_2Q_3,Mx)=1
\quad\text{for every }t\ge0.
\tag{18}
\]

这正是 (3) 的三段 reserve。unit gate 也同时关闭：\(Q_1\mid R-1\)；
若 \(Q_2\) 与 \(R\) 有公共素因子，它除 \(b=2\cdot5623\)；若 \(Q_3\) 与
\(R\) 有公共素因子，它除 \(a=2\cdot193\)。式 (17) 已使三个 \(Q_i\) 避开
这些素数，且 \(R\equiv1\pmod5\)、\(5\nmid K\)。故所有 raw edge 的
strict capacity、unit condition 和 gcd-reduction gate 都成立。

因此对

\[
\boxed{
v=1085244+20619541\cdot1090735887676059709266\,t
}
\tag{19}
\]

的每一个 prime parameter，完整 raw word

\[
p;\ 5;\operatorname{Fac}(Q_1);\ 5;\operatorname{Fac}(Q_2);\
5;\operatorname{Fac}(Q_3)
\tag{20}
\]

实际到达 \((361,R-361,1)\)，随后由 (12) 做 atomic \(r\)-RESET 到 \(R=747\)。
这里 \(p(t)\) 的首项与步长互素；Dirichlet 定理因此给出无穷多个 prime parameter。

这个结论只建立了一个无限的 actual raw/reset family。它尚无一个已确认
terminal-free 的 prime parameter，也没有 canonical F/G、完整 source adapter 或
E1--E5 receipt，所以不能登记 selector edge。

在 v=5 的既有 q=5 三段 topology 中，第三段的 \(19\)-进容量已经饱和：它不能
直接提升到 \(c=361\)，也不能产生 \(c=38\) 或 \(722\)。这只是该 topology 的
局部障碍，不是所有 C=19^2 raw path 的 no-go。
