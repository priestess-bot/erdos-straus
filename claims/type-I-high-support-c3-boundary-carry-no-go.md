---
kind: claim
claim_id: type-I-high-support-c3-boundary-carry-no-go
title: 最小 C=3 高支撑边界的严格 complete-excess carry no-go
statement: 对每个核心素数 p=1 (mod 24)，越过 B_p=(p-1)^2/4 的最小 canonical C=3 支撑是 A_3=(p-1)(3p-1)/12，其图表为 (R_3,K_3;A_3)=(3p-4,(p-1)(3p-1)/4;A_3)。在该图表的任意合法 bottom complete-excess 候选上，canonical target cofactor c 都严格大于 3；因此该宏族既不能下降也不能 stutter。证明穷尽 c=1,2,3 的八个可能 multiplier 类：五类被 full-block 的 2/3-adic 门排除，另三类分别迫使 4h-1|20、8h-3|87 或 6h-1|21（p=24h+1），与 h>=3 的必要同余和大小矛盾。该结论与 C=2 边界的 strict carry no-go 相邻，但不声称任意高支撑状态、也不声称 C=3 图表本身必有 source/path 或 F/G provenance。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-high-support-bundle-carry-capacity-terminal-dispatch
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
  - type-I-overflow-total-cofactor-canonical-projection-persistence-rank
  - denominator-escape-state-contract
topics:
  - type-I
  - high-support
  - c3-boundary
  - complete-excess
  - carry-capacity
  - strict-no-go
  - well-founded-descent
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_high_support_c3_boundary_carry_no_go.py
    role: closed-form-gates-and-focused-sink-controls
visibility: public
last_checked: '2026-08-12'
---

# 最小 (C=3) 高支撑边界的严格 complete-excess carry no-go

## 1. 闭式边界

固定核心素数

\[
p=24h+1,
\qquad h\ge3,
\qquad B_p=\frac{(p-1)^2}{4}.
\tag{1}
\]

在 canonical 高支撑图表中取余因子 (C=3)，即

\[
12A\equiv1\pmod p,
\qquad A>B_p.
\tag{2}
\]

**引理 1（最小 (C=3) 图表）。** 满足 (2) 的最小支撑为

\[
\boxed{
A_3=\frac{(p-1)(3p-1)}{12}=4h(36h+1).}
\tag{3}
\]

对应图表是

\[
\boxed{
R_3=3p-4=72h-1,
\qquad
K_3=3A_3=12h(36h+1),}
\tag{4}
\]

并满足

\[
12A_3=pR_3+1,
\qquad
4K_3=pR_3+1,
\qquad
K_3/A_3=3.
\tag{5}
\]

**证明。** 直接展开

\[
12A_3=(p-1)(3p-1)=p(3p-4)+1.
\tag{6}
\]

又有

\[
A_3-B_p=\frac{p-1}{6}<p.
\tag{7}
\]

同余 (2) 的各正解相差 (p)，而 (A_3-p<B_p<A_3)，故 (3) 是第一个越过
(B_p) 的解。其余公式由 (3) 与 (K_3=3A_3) 立即给出。\(\square\)

## 2. 低余因子只能落在八个类中

设一个合法 complete-excess receipt 在该图表上取完整 offending block (Q)，剩余
(\beta)，并满足

\[
y=Q\beta<R_3,
\qquad x\beta\mid K_3,
\qquad (Q,x\beta)=1,
\qquad M=\operatorname{lcm}(A_3,Q)=A_3L.
\tag{8}
\]

其 canonical target 余因子 (c\in\{1,\ldots,p-1\}) 满足

\[
c\equiv3L^{-1}\pmod p.
\tag{9}
\]

若 (c\le3)，且 (2\le L<R_3)，则 (9) 穷尽给出

\[
\begin{array}{c|c}
c&L\\ \hline
1&3,\ p+3,\ 2p+3\\
2&(p+3)/2,\ 3(p+1)/2,\ (5p+3)/2\\
3&p+1,\ 2p+1.
\end{array}
\tag{10}
\]

这八个数没有遗漏：对每个 (c\in\{1,2,3\})，先解 (9) 的唯一模 (p) 剩余类，
再截取区间 ([2,3p-5]\)。

这里 full-block 语法提供两个关键门。由于

\[
v_2(K_3)=v_2(A_3)=2+v_2(h),
\qquad
v_3(K_3)=v_3(A_3)+1,
\tag{11}
\]

故

\[
2\mid L\Longrightarrow 2^{v_2(A_3)}L\mid Q,
\qquad
3\mid L\Longrightarrow9\mid L.
\tag{12}
\]

第二式是因为 (Q) 中的 (3)-block 必须超过 (v_3(K_3))，而从 (Q) 到
(L=Q/(A_3,Q)) 会减去至多 (v_3(A_3)) 层。

## 3. 八类的统一排除

**定理 2（(C=3) strict carry no-go）。** 对每个满足 (1) 的图表 (4)，任何满足
(8) 的合法 complete-excess 候选都满足

\[
\boxed{c>3.}
\tag{13}
\]

因此其 canonical high-support rank 不会下降，也不会保持不变。

**证明。** 逐类使用 (10)。

1. (L=3) 及 (L=3(p+1)/2=3(12h+1)) 都恰有一层 (3)，违反 (12)。

2. 对

\[
L\in\left\{p+3,\ \frac{5p+3}{2},\ p+1\right\},
\tag{14}
\]

式 (12) 给出 (Q\ge4L>R_3)，违反 (8)。

3. 设 (L=(p+3)/2=12h+2)。若 (h) 为偶数，则
(2^{v_2(A_3)}\ge8)，故 (Q\ge8L>R_3)。若 (h) 为奇数，
(2^{v_2(A_3)}=4)，且

\[
4L\le Q<R_3<8L,
\tag{15}
\]

所以 (Q=4L=48h+8>R_3/2)，必有 (\beta=1)。于是

\[
x=R_3-Q=3(8h-3)
\tag{16}
\]

整除 (x\mid K_3) 给出 (d=8h-3\mid4K_3/3)。但

\[
\frac{4K_3}{3}=16h(36h+1)\equiv87\pmod d.
\tag{17}
\]

这里 (d\ge21) 且 (d\equiv5\pmod{16})，而 (87) 的正因子没有这样的因子，矛盾。

4. 设 (L=2p+3=48h+5)。它大于 (R_3/2)，故 (8) 强制
(Q=L,\beta=1)。于是

\[
x=R_3-Q=6(4h-1).
\tag{18}
\]

令 (d=4h-1\)。从 (x\mid K_3) 得 (d\mid K_3/6)，但

\[
\frac{K_3}{6}=2h(36h+1)\equiv5\pmod d.
\tag{19}
\]

而 (d\ge11>5)，矛盾。

5. 最后设 (L=2p+1=3(16h+1))。若 (v_3(L)=1)，已由 (12) 排除。否则
(L>R_3/2) 强制 (Q=L,\beta=1)，并且 (3\mid16h+1)，即
(h\equiv2\pmod3)。现有

\[
x=R_3-Q=4(6h-1).
\tag{20}
\]

令 (d=6h-1\)。从 (x\mid K_3) 得 (d\mid K_3/4)，而

\[
\frac{K_3}{4}=3h(36h+1)\equiv\frac72\pmod d.
\tag{21}
\]

故 (d\mid7)。但 (d\ge17>7)，矛盾。

这穷尽 (10)，证明 (13)。若 (c=3) 则高支撑的第二秩坐标保持，若 (c>3) 则上升；
二者都不能支付严格的 canonical complete-excess E5。\(\square\)

## 4. 两个定向控制

上述证明不需要枚举 bottom graph。作为两个独立的有限控制，完整 bottom sink 上的合法
候选为

\[
\begin{array}{c|c|c|c}
p&(R_3,K_3;A_3)&\#\text{ sink nodes}&(\#\text{ candidates},\min c)\\ \hline
73&(215,3924;1308)&4&(4,27)\\
193&(575,27744;9248)&15&(7,19).
\end{array}
\tag{22}
\]

这些控制只检验通用 gate 与完整有限 receipt 枚举相容；它们不是 (13) 的证明前提。

## 5. 边界

定理 2 仅排除最小 (C=3) 图表上的 complete-excess macro。它既不证明图表必然来自
一个实际 F/G source，也不构造 terminal，更不处理 (C\ge4) 或一般 (A>1) 溢出状态。
它的作用是把全局出口缺口再明确一层：任何处理这张边界图表的全称路线必须使用
terminal、不同的带 lift 递降，或一种不被当前 full-block 语法覆盖的 paid reset。

## 6. 聚焦复核

```bash
python3 reproductions/type_i_high_support_c3_boundary_carry_no_go.py --verify
```
