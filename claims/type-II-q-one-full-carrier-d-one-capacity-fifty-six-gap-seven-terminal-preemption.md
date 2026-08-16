---
kind: claim
claim_id: type-II-q-one-full-carrier-d-one-capacity-fifty-six-gap-seven-terminal-preemption
title: q=1 full-carrier 零 k 容量五十六的 gap-7 Type II 前缀排除
statement: >-
  在 ordinary q=1 G full-carrier 的 even t=2s 固定-n 宏的零 k 容量分类中，若
  immediate d=1 receiver 的 residual capacity 为 c=56，则 (j,g)=(11,7)，故
  7 divides (24s+1) 并强制 s=2 (mod 7)。原始核心素数 p=48s+1 因而在宏之前已有
  显式 gap-7 Type II 终端：取 x=12s+2、A=1、B=6s+1、C=2，得到
  4/p=1/x+1/y+1/z，其中 y=p(x+2)/7、z=p(x+x^2/2)/7。由于 q=1 phase root
  只接收 terminal-first 未命中的 endpoint，c=56 不可能是合法 persistent receiver。
  这里的特定 (A,B,C)=(1,6s+1,2) 模板不关闭 c=8：其 (j,g)=(11,1) 与 s=2 (mod 7)
  不相容。实际 c=8 控制 p=157393 另有 gap-7 Type I 与 h=107 | p+4 的 Type II
  终端，但这不是 c=8 射线的全称结论。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-full-carrier-phase-root-entry
  - type-II-q-one-full-carrier-d-one-zero-k-capacity-ray-classification
  - type-II-q-one-full-carrier-second-anchor-fixed-n-macro
  - denominator-escape-state-contract
topics:
  - type-II
  - q-one
  - full-carrier
  - type-I
  - d-one
  - residual-capacity
  - c-fifty-six
  - terminal-first
  - fixed-gap
  - proof-boundary
sources:
  - claim: type-II-q-one-full-carrier-phase-root-entry
    role: terminal-first-admission-before-the-full-carrier-root
  - claim: type-II-q-one-full-carrier-d-one-zero-k-capacity-ray-classification
    role: c-fifty-six-shape-and-g-seven-congruence
  - reproduction: reproductions/type_ii_q_one_full_carrier_d_one_capacity_fifty_six_terminal_preemption.py
    role: exact-gap-seven-construction-and-two-macro-controls
visibility: public
last_checked: '2026-08-17'
---

# q=1 full-carrier 零 \(k\) 容量五十六的 gap-7 Type II 前缀排除

## 1. 终端优先的精确位置

令 ordinary \(q=1\) Type II G endpoint 的核心素数为

\[
p=24t+1.
\]

进入 full-carrier Type I root 的规则只适用于已经通过 terminal-first 分派、仍需非终端
处理的 endpoint。故只要对原始 \(p\) 给出直接 Type I/II 证书，就不能把它继续登记为
该 root 的 persistent 宏输入；这不是在 macro target 上把一个偶前驱误写成解。

现在进入偶支 \(t=2s\)，即

\[
p=48s+1.
\tag{1}
\]

零 \(k\) 容量图的 \(c=56\) 行已经精确给出

\[
(c,j,g)=(56,11,7),
\qquad g\mid24s+1.
\tag{2}
\]

因此

\[
24s+1\equiv0\pmod7
\quad\Longrightarrow\quad
\boxed{s\equiv2\pmod7}.
\tag{3}
\]

这里不需再使用 \(q_\star=103\) 或 \(s\equiv86\pmod{721}\)：\(g=7\) 已足够触发
原始 endpoint 的 terminal-first 前缀。

## 2. 固定 gap-7 的直接 Type II 证书

固定 (1)、(3)，令

\[
h=7,
\qquad
x=\frac{p+h}{4}=12s+2=2(6s+1).
\tag{4}
\]

写

\[
(A,B,C)=(1,6s+1,2).
\tag{5}
\]

则 \(x=ABC\)、\(A\le B\)、\((A,B)=1\)，且由 (3)

\[
A+B=6s+2\equiv0\pmod7.
\tag{6}
\]

所以这正是 gap \(7\) 的 Type II normal form，除子为 \(A^2C=2\)。其三分母写成

\[
\boxed{
\begin{aligned}
x&=12s+2,\\
y&=\frac{p(x+2)}7=\frac{4p(3s+1)}7,\\
z&=\frac{p(x+x^2/2)}7
  =\frac{4p(6s+1)(3s+1)}7.
\end{aligned}}
\tag{7}
\]

式 (3) 使 \(y,z\) 为正整数。正规形恒等式，或直接通分，给出

\[
\boxed{\frac4p=\frac1x+\frac1y+\frac1z.}
\tag{8}
\]

在这里 \(7\le p-2\)：零 \(k\) 的 \(c=56\) 相位已至少有
\(s\equiv86\pmod{721}\)，特别 \(p\ge4129\)。故 (7) 是合法、有界 gap 的直接
Type II certificate。

结合第 1 节的准入优先级，得到

\[
\boxed{c=56\text{ 不可能出现在 terminal-first 之后的 persistent q=1 receiver 中}.}
\tag{9}
\]

这排除的是整个 \(c=56\) 算术相位作为实际队列状态，不是说其 macro 恒等式不存在。

## 3. 两个 \(q_\star=103\) 实际控制

先前 \(c=56\) 的 ordinary \(q=1\) macro 控制为 \(s=86,p=4129\)。式 (7) 给出

\[
(x,y,z)=(1034,611092,315934564),
\qquad
\frac4{4129}=\frac1{1034}+\frac1{611092}+\frac1{315934564}.
\tag{10}
\]

因此这行是有效的 macro arithmetic receipt，但不再是一个可进入 persistent selector 的
障碍控制。

为避免把这个结论误扩展到 \(c=8\)，注意该行有

\[
(c,j,g)=(8,11,1).
\tag{11}
\]

若它同时满足 \(s\equiv2\pmod7\)，则

\[
24s+1\equiv66s+1\equiv0\pmod7,
\]

从而 \(7\mid g\)，与 (11) 矛盾。因此上面的固定 gap-7 构造与 \(c=8\) 形状
完全不相交。这里的“不相交”只针对 (5) 的特定 gap-7 Type II 正规形，并不排除
其他 gap-7 终端。

现有 \(c=8\) 控制 \(p=157393,s=3279\) 已由既有 \(p\equiv5\pmod7\) 的 gap-7
Type I 规则抢占；它还恰好有一个不同的 terminal：

\[
p+4=157397=107\cdot1471,
\qquad107\equiv3\pmod4,
\]

故标准 \(p+4\) Type II 公式给出

\[
\frac4{157393}
=\frac1{39375}+\frac1{57920624}+\frac1{2280624570000}.
\tag{12}
\]

式 (12) 只抢占这一个实际控制点；它没有证明所有 \(c=8\) 的 \(q_\star=103\) 射线
都终止。

## 4. 作用域

本卡新增了一个全称 terminal-first 排除：零 \(k\) 的 \(c=56\) 容量形状只能作为
postmacro 算术影子存在，不能进入合法 persistent queue。剩余的零 \(k\) 103 通道只有
\(c=8,j=11,g=1\)，且仍需要一个与其 \(g=1\) 条件相容的 terminal 或 E1--E5
strict edge。其确定性的第二 complete-excess continuation 已知会增大 capacity，故不能
重复这条 bundle 路线。这里没有声称这个剩余通道已经覆盖，更没有声称 G/Type I global exit。

聚焦复核：

~~~bash
python3 reproductions/type_ii_q_one_full_carrier_d_one_capacity_fifty_six_terminal_preemption.py --verify
~~~

复现器仅重放 \(c=56\Rightarrow s\equiv2\pmod7\) 的固定 gap-7 证书、\(c=8\) 的
不相交性及两个已知 macro 控制；不做 prime-range 或 terminal-range 搜索。
