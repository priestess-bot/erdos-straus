---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-carry-overlap-boundary
title: q=1 高 C=2 19 相位 H4 carry-overlap、条件 p减一高度边界与有限标签边界
statement: >-
  在 q=1 high C=2 19 相位每个未被 H3 terminal 抢占、经最大 complete-excess
  构造到 H4 的状态中，令 L=M4/M3、c4 为 H4 canonical capacity，并定义唯一第四 carry
  s4=(L*c4-c3)/p。则 0<=s4<L，且 H4 p-anchor 的精确 overlap 为
  gcd(R4-1,K4)=2*gcd((p+1)/2,c3-s4)。所以该 gcd 的任一 3 (mod 4) 素因子给出
  可直接核验的 Type II raw-ray 证书，但同一素因子已经给出根级 p+1 Type I 证书；故在
  p+1 terminal-first 后，该 H4 gate 不增加全局 terminal 覆盖。同时 L(c4-c3)=p*s4-c3(L-1)
  精确判定本地 capacity 势方向。若未来 typed reclassification 将同一 H4 图表实现为 Type I
  正规形并保留最大尾，则其 p-1 标准最大尾桥必因图表高度超过桥的平方容量而不可能成立。
  这是一条条件性图表边界，不声称 H4 本身已有 Type I 正规形。然而 H4 overlap 与该势方向都不由此前的有限 H3 标签
  (u mod 119,a,g,lambda) 决定：p=184993 与 p=727633 均有
  (u,a,g,lambda)=(83,1723,1,1) 且 H3 clean，但 H4 的奇 overlap 分别为 1 与 17。
  另有 p=448561 与 p=665617 共享 (u,a,g,lambda)=(15,431,1,1)，但前者 c4>c3、
  后者 c4<c3。因此不能把 H3 的有限 mask 直接当作 H4 全域 selector 或势下降证明；
  任何继续该路线的 selector 至少必须携带 s4（或等价的实际 H4 carry）信息。该结果没有证明
  H4 总能终端或递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
  - type-II-q-one-c-two-19-phase-fourth-anchor-terminal-gate
  - type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
  - type-II-raw-ray-certificate
  - p-plus-one-sqrt-certificate
  - type-I-normal-pminusone-upper-half-bridge
  - type-I-universal-p-source-capacity-anchor-orbit
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - carry-capacity
  - terminal-first
  - short-certificate
  - strict-counterexample
  - selector-boundary
  - terminal-preemption
  - p-minus-one
  - conditional-height-boundary
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
    role: H3-to-H4-maximal-excess-construction
  - claim: type-II-q-one-c-two-19-phase-fourth-anchor-terminal-gate
    role: H3-coprime-support-and-terminal-dispatch
  - claim: type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
    role: high-H3-capacity-lower-bound
  - claim: type-II-raw-ray-certificate
    role: overlap-factor-to-Type-II-certificate
  - claim: p-plus-one-sqrt-certificate
    role: root-level-terminal-preemption
  - claim: type-I-normal-pminusone-upper-half-bridge
    role: same-chart-pminusone-bridge-criterion
  - concept: denominator-escape-state-contract
    role: named-normal-form requirement for a legal recursive state
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_carry_overlap_boundary.py
    role: exact-carry-identity-and-label-boundary-controls
visibility: public
last_checked: '2026-08-15'
---

# q=1 high \(C=2\) 19-phase 的 H4 carry-overlap 公式与有限标签边界

## 1. H4 的缺失状态变量

保留最大 complete-excess H3 \(\Rightarrow\) H4 构造的记号。令

\[
w=\frac{p+1}{2},
\qquad
M_4=M_3L,
\qquad
K_4=M_4c_4,
\qquad
pR_4+1=4K_4,
\tag{1}
\]

其中 \(L=M_4/M_3>1\)，并且 \(c_4\) 是唯一满足

\[
c_4\equiv c_3L^{-1}\pmod p,
\qquad 1\le c_4\le p-2
\tag{2}
\]

的 canonical capacity。因此有唯一整数

\[
\boxed{s_4=\frac{Lc_4-c_3}{p}.}
\tag{3}
\]

它不是可忽略的记账量。由于 \(L\ge2\) 且 \(1\le c_3,c_4\le p-2\)，

\[
-p<Lc_4-c_3<Lp.
\]

左式又是 \(p\) 的倍数，故

\[
\boxed{0\le s_4<L.}
\tag{4}
\]

这是 H4 canonicalization 的真实 carry，而非新的自由选择。

## 2. 精确 H4 anchor-overlap 恒等式

此前 H3 的精确计算给出

\[
p\equiv1\pmod {16},
\qquad (w,M_3)=1,
\tag{5}
\]

并且 \(M_3\) 为偶数。最大超额块和其与 \(M_3\) 的 overlap 都为奇数，故 \(L\)
为奇数、\(K_4\) 为偶数，且 \(p\nmid K_4\)。从 (1) 得

\[
\begin{aligned}
(R_4-1,K_4)
&=(p+1,K_4)\\
&=2(w,K_4)\\
&=2(w,Lc_4).
\end{aligned}
\tag{6}
\]

另一方面，(3) 和 \(p\equiv-1\pmod w\) 给出

\[
Lc_4=c_3+ps_4\equiv c_3-s_4\pmod w.
\tag{7}
\]

合并 (6)--(7)，得到所需的完整公式

\[
\boxed{(R_4-1,K_4)=2\,(w,c_3-s_4).}
\tag{8}
\]

因此 H4 的 complete-excess/anchor selector 不应只继承 H3 的 \(g=(w,c_3)\)：
它需要实际 carry residual \(c_3-s_4\)。

同一个 carry 也精确支付容量变化：由 (3)，

\[
\boxed{L(c_4-c_3)=ps_4-c_3(L-1).}
\tag{9}
\]

所以 \(c_4<c_3\) 当且仅当右端为负。这个判据不把 H3 \(\Rightarrow\) H4 自动
称为 local capacity descent；先前的 persistent 宏只比较其终点与 \(P\) 的 \(p-1\)
容量。

## 3. 状态局部的 Type II terminal 与根级预先截断

设 \(\ell\equiv3\pmod4\) 是 \((w,c_3-s_4)\) 的一个素因子。则
\(\ell\mid p+1\)。取

\[
A=1,
\qquad C=\frac{\ell+1}{4},
\qquad k=1,
\qquad B=\frac{p+1}{\ell}.
\tag{10}
\]

有 \(4ACk-1=\ell\mid kp+A\)，故 raw-ray 公式给出一张合法 Type II
证书。这是一个可核验的 H4 terminal gate；它没有声称 \(\ell\) 在所有状态存在，
也没有声称 \(C\) 有统一常数上界。

但这个 gate 不能为根级 terminal-first selector 增加新的覆盖。事实上，\(\ell\mid w\)
且 \(\ell\equiv3\pmod4\)。直接令

\[
x=\frac{p+\ell}{4},
\qquad d=x,
\qquad y=\frac{x(p+1)}{\ell},
\qquad z=py.
\tag{11}
\]

则 \(\ell\mid px+d=x(p+1)\)，并且 \(d=x\mid x^2\)，所以 \((\ell,d)\)
是根素数 \(p\) 的直接 Type I 除子证书。这正是
[\(p+1\) 平方根证书](p-plus-one-sqrt-certificate.md)的同一构造；取最小的
\(3\pmod4\) 因子时还得到其平方根界。

因此有严格包含关系

\[
\boxed{
 \{p:\text{H4 overlap gate 有 }3\pmod4\text{ 因子}\}
 \subseteq
 \{p:\text{\(p+1\) Type I terminal 存在}\}.}
\tag{12}
\]

特别地，若根级 selector 已先检查并排除了 \(p+1\) terminal，则 \(w\) 的每个素因子
都是 \(1\pmod4\)。因为 \((w,c_3-s_4)\mid w\)，H4 overlap gate 在这一全局残余上
必为空。它仍可作为**状态局部**的 Type II 证书，但不能被当作尚未覆盖根素数的新增出口。

作为正控制，\(p=114769\) 在 H3 clean 分支上到达 H4，且

\[
(w,c_3-s_4)=23.
\]

取 \((A,C,k)=(1,6,1)\) 得

\[
\frac4{114769}
=\frac1{29940}+\frac1{688614}+\frac1{3436183860}.
\tag{13}
\]

同一个 \(\ell=23\) 也给出被预先选择的根级 Type I 证书：

\[
\frac4{114769}
=\frac1{28698}+\frac1{143203020}+\frac1{16435267402380}.
\tag{14}
\]

## 4. 同图表 Type I 正规形的条件 \(p-1\) 最大尾桥高度边界

H4 目前是 complete-excess 的 canonical capacity target，而不是已经附有三分母
Type I `normal_form` verifier 的状态。因而不能从图表恒等式直接断言 H4 有一个可被
\(p-1\) 桥检验的“前两项”。不过 H4 的图表高度仍给出一个严格的条件边界：

> 若后续 typed reclassification 将**同一** \((p,R_4,K_4)\) 实现为 Type I 正规形，
> 并且该正规形的最大尾满足
> \(R_4=4r_4-1\)，则保持该正规形前两项、取源 \(n=p-1\) 的标准最大尾桥不可能存在。

写

\[
R_4=4r_4-1,
\qquad
t=\frac{p-1}{4}.
\tag{15}
\]

[Type I 正规形的 \(p-1\) 桥判据](type-I-normal-pminusone-upper-half-bridge.md)应用于上述
**条件性的 Type I 正规形**时说明，该同图表最大尾桥存在当且仅当

\[
r_4\mid t^2.
\tag{16}
\]

H4 的高度使这一整除式不可能。三 anchor 宏的首个高容量为

\[
M_0=\frac{(p-1)(2p+1)(2p^2-3p-1)}8.
\tag{17}
\]

对 \(p\ge73\)，三个因子分别严格大于 \(p/2\)、\(2p\)、\(p^2\)，故

\[
M_3>M_0>\frac{p^4}{8}.
\tag{18}
\]

另一方面，H4 有 \(M_4=M_3L\)、\(L>1\)、\(c_4\ge1\)，所以
\(K_4=M_4c_4>M_0\)。由 \(pR_4+1=4K_4\) 和 (15)，

\[
K_4=pr_4-t,
\qquad
r_4=\frac{K_4+t}{p}
>\frac{p^3}{8}
>\frac{p^2}{16}
>t^2.
\tag{19}
\]

这与 (16) 矛盾。因此

\[
\boxed{\begin{gathered}
\text{任何保留 H4 图表的未来 Type I 正规形，均不存在以 }n=p-1\\
\text{为源、保持其前两项的标准最大尾偶桥。}
\end{gathered}}
\tag{20}
\]

这是图表尺度的条件 no-go，不是 H4 的 typed transition。它不建立 H4 的 Type I 正规形、
不排除根素数在另一张低 \(R\) 图表中有 \(p-1\) 终端，也不排除其它 \(n<p\) 的提升。

## 5. H3 有限标签不足的严格反例

下面两点都通过 H3 clean 分支，且有相同的 H3 有限标签：

| \(p\) | \(u\) | \(a\) | \(g\) | \(\lambda\) | \(c_4\) | \((w,c_3-s_4)\) |
|---:|---:|---:|---:|---:|---:|---:|
| \(184993\) | \(83\) | \(1723\) | \(1\) | \(1\) | \(178654\) | \(1\) |
| \(727633\) | \(83\) | \(1723\) | \(1\) | \(1\) | \(594031\) | \(17\) |

所以不存在一个只读取 \((u,a,g,\lambda)\) 的函数，能够给出 H4 的精确
odd overlap \((w,c_3-s_4)\)。这不是从两个点外推整体行为，而是对该特定
有限标签 selector 的直接反例：同一输入标签被要求同时输出 \(1\) 和 \(17\)。
此前的 hard \(q=1\) mask 控制 \(p=14449\) 也满足 (8)，其
\((w,c_3-s_4)=1\)；所以该公式同时覆盖 clean 与原 mask 两类 H3 前身。

同样的有限标签也不能确定 (9) 的符号：

| \(p\) | \(u\) | \(a\) | \(g\) | \(\lambda\) | \(c_3\) | \(c_4\) | 方向 |
|---:|---:|---:|---:|---:|---:|---:|---|
| \(448561\) | \(15\) | \(431\) | \(1\) | \(1\) | \(85507\) | \(423624\) | 上升 |
| \(665617\) | \(15\) | \(431\) | \(1\) | \(1\) | \(126883\) | \(20388\) | 下降 |

故不可能仅从该 H3 标签宣布 H3 \(\Rightarrow\) H4 是严格容量递降；需要实际 \(s_4\)
或等价的 carry gate。

## 6. 边界与下一接口

式 (8) 把 H4 的状态局部 terminal 输入压缩为一个明确的 carry residual，并给出它命中时的
构造性证书；但 (12) 证明该终端在根级已被 \(p+1\) 分支预先截断。故在真正的全局残余上，
不能再试图从 \((w,c_3-s_4)\) 的 \(3\pmod4\) 因子获得新出口；(20) 进一步规定了：
任何保留该图表的 Type I 重分类不能把 \(p-1\) 标准最大尾桥当作下一出口。H4 的下一条有效
研究接口必须先给出 typed reclassification，再利用 \(s_4\) 构造不同的可提升 \(n<p\) 递降，
或给出一个不经 \(p+1\) 因子的短证书；它也不能只重复 H3 的 \((u,\lambda)\) 有限 mask。

Focused verification:

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_carry_overlap_boundary.py --verify
```
