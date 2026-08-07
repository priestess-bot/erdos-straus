---
kind: claim
claim_id: type-I-g-anchor-c3-adaptive-core19-q137-first-entry-family
title: c=3 core-19 的 q=137 首标签 C=19 实际 raw 家族
statement: 在 c=3 chart 中取 h=8+2603v，则 p=193+62472v、R=823+270712v，且 q=137 的首 raw edge 后可由 Q=43+14144v 到达 C=19。精确 gcd gate 是 v 不等于 1 (mod 3)、5 (mod 7)、16 (mod 19)、14 (mod 31)。因此在 v=12369w 上，每一个 prime p=193+772716168w 都有 actual primitive word 137;Fac(Q) 到达 (19,R-19,1)，从而有固定 R=63 的 C=19 RESET。这个 raw family 避开 q=23 首标签的自动 terminal；固定 pair Type II 筛在该 affine subray 的 36 个 m 和 144 个 d 候选上均无命中。但它不排除按参数移动的 terminal：w=0 有 (m,d)=(7,20)，而 w=1+1319t 的每个 prime 参数都有 (m,d)=(1319,1) 的直接 Type II 证书。该 terminal 子射线必须 terminal-first 关闭；它不为原始 raw receipt 登记 selector edge，也不分类其余 w。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-c3-adaptive-core19-c19-atomic-reset
  - type-I-g-anchor-c3-adaptive-core19-q23-first-entry-terminal-obstruction
  - type-I-g-anchor-c3-adaptive-core19-ambient19-terminal-screen
topics:
  - type-I
  - type-II
  - c3
  - core19
  - raw-source
  - factor-block
  - infinite-family
  - terminal-first
  - terminal-subray
  - fixed-pair-screen
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_c3_adaptive_core19_q137_first_entry_family.py
    role: q=137 raw controls, capacity sieve, fixed-pair screen, and terminal subray
visibility: public
last_checked: '2026-08-07'
---

# q=137 首标签的 C=19 实际 raw 家族

本卡给出第二条与既有 q=5 和 q=23 语言不同的无限 C=19 raw family。它避开
q=23 的首标签 terminal 定理，但没有把有限固定-pair 筛误报成 terminal-free；
其中一条精确参数子射线反而有统一的直接 Type II 终端。

## 1. 两段 q=137 language

在 c=3 chart

\[
p=24h+1,\qquad R=104h-9
\tag{1}
\]

中联立 \(h\equiv8\pmod {19}\) 与 \(137\mid R-1\)，得到

\[
h=8+2603v.
\tag{2}
\]

因此

\[
\begin{aligned}
p&=193+62472v,&R&=823+270712v,\\
b&=\frac{R-1}{137}=6+1976v,
&Q&=\frac{R-b}{19}=43+14144v.
\end{aligned}
\tag{3}
\]

沿此 ray，\(137\nmid K\)、\(R\equiv1\pmod {137}\)。若
\(\gcd(Q,KR)=1\)，则

\[
(1,137);\quad (1,\operatorname{Fac}(Q))
\tag{4}
\]

从 \((1,R-1,1)\) 先到 \((b,R-b,1)\)，再到 \((19,R-19,1)\)。其中第一个
\(Q\)-factor 选右侧，之后选左侧；因而 (4) 是一个 actual primitive raw word。

## 2. exact capacity sieve

对 (3) 中的 \(Q, M=26h+1, x=p-3, R\) 取 affine determinant，得到

\[
\operatorname{rad}\Delta(Q,M)\subseteq\{2,3,13,19,31\},
\quad
\operatorname{rad}\Delta(Q,x)\subseteq\{2,7,19\},
\quad
\operatorname{rad}\Delta(Q,R)\subseteq\{2,13\}.
\tag{5}
\]

逐素数解线性同余得到精确 gate

\[
\gcd(Q,KR)=1
\Longleftrightarrow
v\not\equiv1\pmod3,\quad
v\not\equiv5\pmod7,\quad
v\not\equiv16\pmod{19},\quad
v\not\equiv14\pmod{31}.
\tag{6}
\]

令

\[
v=12369w,\qquad 12369=3\cdot7\cdot19\cdot31.
\tag{7}
\]

四个被排除的剩余类都不为零，所以 (6) 对所有 \(w\ge0\) 成立。于是

\[
\boxed{p(w)=193+772716168w}
\tag{8}
\]

的每一个 prime parameter 都有 (4) 的 actual raw receipt。首项 \(193\) 与步长
互素，故 Dirichlet 定理给出无穷多个这样的 prime parameter。每条 leaf 再由既有
固定 \(c=19\) RESET 落到 \(R=63\)：这里 \(63p(w)+1\equiv0\pmod {76}\)
对所有 \(w\) 保持成立。复现器同时检查 \(M,x,R\) 对 \(v\) 的三个斜率皆为
\(137\) 的倍数，因此首标签 \(137\) 在整个子射线上始终是 \(KR\)-unit。

## 3. 固定 pair terminal 的精确边界

对 affine ray \(p(w)=P+Dw\)，固定 \(m\equiv3\pmod4\)、\(d>0\) 的 Type II
factor-pair template 在整条 ray 上成立，当且仅当

\[
m\mid D,\qquad
d\mid E_m^2,\qquad
m\mid P+4d,
\qquad
d\le\frac{P+m}{4},
\qquad
E_m=\gcd\left(\frac{P+m}{4},\frac D4\right).
\tag{9}
\]

最后一个范围条件因 \(D>0\) 而对整条 ray 等价于其 \(w=0\) 版本。对 (8)，\(D\)
有 36 个 \(3\pmod4\) 因子；所有 \(d\mid E_m^2\) 合计只有 144 个。逐一应用
(9) 给出零命中。故这个 actual raw family 不携带一个
uniform fixed-pair terminal。特别地，下面的 \(m=1319\) 不整除 \(D\)，所以它只在
一个参数子射线上成立，并不与这个固定模板结论矛盾。

## 4. 两个控制

\(w=0\) 给

\[
p=193,\quad R=823,\quad Q=43,
\]

并有 word \((1,137),(1,43)\)，但 \((m,d)=(7,20)\) 是直接 Type II terminal。

\(w=1\) 是一个 prime control：

\[
\begin{aligned}
p&=772716361,& R&=3348437551,\\
Q&=174947179=11\cdot181\cdot87869.
\end{aligned}
\]

其 word

\[
(1,137),(1,11),(0,181),(0,87869)
\]

逐边满足 strict capacity、unit condition 和 gcd-reduction \(=1\)，并到达
\((19,R-19,1)\)。但它有直接 Type II 终端：

\[
\begin{aligned}
p+4&=772716365=1319\cdot585835,\\
m&=1319\equiv3\pmod4,\qquad
x=\frac{p+m}{4}=193179420,\\
x+1&=1319\cdot146459.
\end{aligned}
\tag{10}
\]

取 \(d=1\)。则 \(d\mid x^2\)、\(d\le x\)、\(m\mid x+d\)，故

\[
\frac4p
=\frac1{193179420}
+\frac1{113171265515699}
+\frac1{21862359432988733714580}.
\tag{11}
\]

所以这个 control 必须由 terminal-first 分派关闭；其 raw receipt 和 \(R=63\)
RESET 仍是正确的原始结构事实，但不能记为 selector edge。

## 5. \(m=1319,d=1\) 的无穷 terminal 子射线

令 \(D=772716168\)。有

\[
D\equiv-197\pmod {1319},
\qquad
\gcd(197,1319)=1.
\tag{12}
\]

因此对 (8) 的任意参数，

\[
1319\mid p(w)+4
\Longleftrightarrow
w\equiv1\pmod {1319}.
\tag{13}
\]

写 \(w=1+1319t\)，则

\[
\begin{aligned}
p_t&=772716361+1019212625592t,\\
p_t+4&=1319(585835+772716168t),\\
K_t&=146459+193179042t,\\
x_t&=1319K_t-1.
\end{aligned}
\tag{14}
\]

这里 \(4K_t-1=(p_t+4)/1319\)、\(4x_t=p_t+1319\)。所以对每个 prime
\(p_t\)，取 \(m=1319,d=1\) 有

\[
\boxed{
\frac4{p_t}
=\frac1{x_t}
+\frac1{p_tK_t}
+\frac1{p_tK_tx_t}.}
\tag{15}
\]

\(\gcd(772716361,1019212625592)=1\)，而初项和步长分别为 \(1\) 与
\(0\pmod {24}\)。Dirichlet 定理因此给出无穷多个核心 prime 参数。由第 2 节，
这些 prime 同时保留 actual \(137;\operatorname{Fac}(Q)\) raw receipt；但 (15)
优先终止它们。这个结论只覆盖 \(w\equiv1\pmod {1319}\)，不声称其余参数没有
moving terminal。
