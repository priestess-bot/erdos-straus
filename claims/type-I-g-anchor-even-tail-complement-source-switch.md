---
kind: claim
claim_id: type-I-g-anchor-even-tail-complement-source-switch
title: G-anchor 补余 seed 的偶侧 raw 编码与跨图表 source-switch 候选
statement: 对任意 p=1 (mod 4) 的 Type I 图表，现有 m=1 raw 编码若固定读取奇侧，则其 physical cofactor 必为奇数，因而不能读取 full-Q 补余 seed 的偶 cofactor。读取偶侧的带方向编码 (C,M,t)=((x,K),K/(x,K),x/(x,K)) 是严格无损的 primitive m=1 raw-node 编码；在额外 4M>R（等价 C<p）时才给出 physical determinant 行。两类补余 seed 都是其 t=1 像。更强地，在 c=3 分支，旧 G-anchor 的 canonical node (p-3,1) 经仿射 source-switch Phi_{80h-8} 直接送到该偶侧 seed node，并随后由 d-dual 代数上落入 (R,K;A)=(11,3(22h+1);3)。这给出一个明确的跨图表 adapter 候选，但 Phi 和偶侧方向尚未写入现有 E1/E3 合同，故不是已登记递归边。c=9 的相应前像为 (p-9,7)；p=193 是正控制，而 p=337 的完整 universal-source raw Reach 不含该点，故该简单模式不全称。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-marked-raw-peeling-calculus
  - type-I-g-anchor-fixed-chart-affine-complement-overflow-torsor
  - type-I-g-anchor-torsor-source-adapter-boundary
  - type-I-g-anchor-full-q-complement-r11-reset-boundary
  - type-I-overflow-a-one-dual-outer-rank-reset
  - denominator-escape-state-contract
topics:
  - type-I
  - G-anchor
  - full-Q
  - raw-path
  - marked-embedding
  - even-tail
  - source-switch
  - complement-torsor
  - R-11
  - proof-boundary
sources:
  - claim: type-I-g-anchor-marked-raw-peeling-calculus
    role: odd-tail-m1-raw-encoding
  - claim: type-I-g-anchor-fixed-chart-affine-complement-overflow-torsor
    role: complement-seed-families
  - claim: type-I-overflow-a-one-dual-outer-rank-reset
    role: conditional-R11-reset
visibility: public
last_checked: '2026-08-06'
---

# G-anchor 补余 seed 的偶侧 raw 编码与跨图表 source-switch 候选

## 1. 奇侧投影的奇偶边界

固定一个合法图表

\[
4K=pR+1,
\qquad
p\equiv1\pmod4.
\tag{1}
\]

于是 \(R\equiv3\pmod4\)，特别地 \(R\) 为奇数。现有扩展 \(m=1\) raw
编码把 primitive 节点定向为

\[
x\in2\mathbb N,
\qquad
y=R-x\in2\mathbb N+1,
\qquad
(x,y)=1,
\tag{2}
\]

并读取奇侧

\[
C=(y,K),
\qquad
M=K/C.
\tag{3}
\]

所以该投影的整个像都满足

\[
\boxed{C\text{ 为奇数}.}
\tag{4}
\]

full-\(Q\) 补余 seed 的新缺量为 \(d\in\{3,9\}\)，故其 physical
cofactor 是

\[
C^\vee=p-d,
\tag{5}
\]

必为偶数。因此它不属于任何 target chart 的既有 odd-tail \(m=1\)
projection 像。这排除了以任意长 target raw word、但仍沿用既有投影语义的
nonlocal 替换；它不说明 seed 本身不是 raw primitive node。

## 2. 无损的偶侧编码

对 (2) 改为读取偶侧，定义

\[
C=(x,K),
\qquad
M=\frac KC,
\qquad
t=\frac xC.
\tag{6}
\]

**定理（偶侧 raw-node 编码）。** 式 (6) 是 primitive \(m=1\) raw node 与

\[
\mathcal E^{\rm raw}_{p,R}=
\left\{(M,t):
\begin{array}{l}
M\mid K,\ C=K/M,\ 0<Ct<R,\ 2\mid Ct,\\
(t,M)=1,\ (R-Ct,R)=1
\end{array}
\right\}
\tag{7}
\]

之间的双射。逆映射为

\[
(M,t)\longmapsto\{Ct,R-Ct\}.
\tag{8}
\]

**证明。** 对 (6)，有

\[
(Ct,K)=C(t,M)=C,
\qquad
(Ct,R-Ct)=(Ct,R)=1.
\tag{9}
\]

所以 (7) 的所有条件成立。反过来，(7) 的互素条件使 (8) 是 primitive
node，而 (9) 反向恢复 \(C=(Ct,K)\)、\(M=K/C\) 与 \(t=Ct/C\)。证毕。

这个结论首先是 raw-node 编码，不是自动 determinant 编码。其 physical
determinant 子像恰需附加

\[
4M>R
\quad\Longleftrightarrow\quad
C<p.
\tag{10}
\]

在旧 G 图表 \(R=p-2<p\) 中，(10) 对每个 raw node 自动成立；在高图表中不成立。
例如 \((p,R,K)=(73,303,5530)\) 的 primitive node \(\{158,145\}\) 给

\[
(C,M,t)=(158,35,1),
\qquad
4M=140<303.
\tag{11}
\]

因而它是合法 raw node，却不是 determinant 行。

## 3. 补余 seed 正是偶侧 \(t=1\) 节点

令 \(p=24h+1\)。两类补余 target 的偶侧数据为

\[
\begin{array}{c|c|c|c|c|c}
d&M&R&C=x&y=R-x\\ \hline
3&26h+1&104h-9&24h-2&80h-7\\
9&(50h+2)/3&(200h-67)/3&24h-8&(128h-43)/3
\end{array}
\tag{12}
\]

两行均有

\[
(x,K)=x,
\qquad
t=1,
\qquad
4M-R\in\{13,25\}.
\tag{13}
\]

primitive 性也可不靠枚举地验证。第一行满足

\[
y-3x=8h-1,
\qquad
x-3(8h-1)=1;
\tag{14}
\]

第二行满足

\[
3y-5x=8h-3,
\qquad
x-3(8h-3)=1.
\tag{15}
\]

所以两行确实给出 target high chart 中的 primitive raw node。它们是否有
source/path provenance 是另一个问题。

## 4. \(d=3\) 的显式 anchor-level source switch

现在取 \(h\not\equiv2\pmod3\)。旧 G 图表为

\[
R_0=p-2=24h-1,
\qquad
K_0=144h^2.
\tag{16}
\]

其 universal \(p\)-source 经实际 \(q=p,t=1\) 边到达 canonical anchor
\(\{1,p-3\}\)。将其定向为 \((p-3,1,1)\)。令

\[
\Delta=(104h-9)-R_0=80h-8,
\qquad
\Phi_\Delta(U,V,m)=(U,V+\Delta m,m).
\tag{17}
\]

则

\[
\Phi_\Delta(p-3,1,1)
=(24h-2,80h-7,1).
\tag{18}
\]

右端正是 (12) 的第一行。故偶侧投影把它读为

\[
(M,C,d,n)=(26h+1,24h-2,3,13).
\tag{19}
\]

随后的 \(d\)-dual 代数上给出

\[
(R_d,K_d;A')=(11,3(22h+1);3).
\tag{20}
\]

这产生一个非常具体的候选宏：

\[
\text{old G source}
\xrightarrow{q=p}
\{p-3,1\}
\xrightarrow{\Phi_{80h-8}}
\{24h-2,80h-7\}
\xrightarrow{\text{even-tail}}
\text{seed}
\xrightarrow{d\text{-dual}}
R=11.
\tag{21}
\]

第一箭头是已有 actual raw edge，末箭头在 seed 有 verified provenance 时是已有
\(A=1\) dual-RESET。中间 \(\Phi\) 与 even-tail direction 则是本卡新构造的
source-switch 数据，而不是已有 raw transition。

这里有两个不能省略的障碍。以 \(p\) 放在第一坐标的既有 \(p\)-边实际给出

\[
\Phi_\Delta(1,p-3,1)=(1,R_T-1,1),
\tag{21a}
\]

即 target canonical anchor；(18) 先交换了旧 anchor 的坐标，而 \(\Phi\) 是不对称的，
所以它不能同时成为该有序 \(p\)-边的 action-preserving 像。更强地，令

\[
Q_0=\frac{p-3}{2}.
\tag{21b}
\]

对每个 \(q\mid Q_0\)，旧图表有 \(v_q(p-3)>v_q(K_0)=0\)，但 target 满足

\[
K_T=(26h+1)(p-3),
\qquad
v_q(p-3)\le v_q(K_T).
\tag{21c}
\]

因此 \(\Phi\) 把旧 full-\(Q_0\) 的外部容量直接变成 target 的已饱和容量；它不能保存
任何同一条 \(q\)-raw edge。若要采用 (21)，必须为这种“定向仿射尾饱和”提供新的
账本与 phase 语义，不能把它伪写成 ordinary raw peeling。

因此 (21) 的 E1--E5 状态如下：

| 项 | 已有或新需要的内容 |
|---|---|
| E1 | 旧 universal source 与首个 \(p\)-边已回放；但 (21a)--(21c) 表明 \(\Phi\) 尚不是已注册的 source/path action。 |
| E2 | (19)--(20) 给出 \(A'=3\mid3(22h+1)\)；偶侧 raw mark 到 verified overflow normal form 仍须新定义。 |
| E3 | 需要 verifier 重算 \(\Delta\)、有序方向、容量饱和、primitive node、补余 seed、dual chart 与 scope 传播。 |
| E4 | 可候选取图表无关的 \(\operatorname{Sol}(p)\) 恒等 lift，但新 \(\Phi\)+projection 段尚无 marked-set/state lift。 |
| E5 | dual-RESET 半段由 \(1\to3\) 严格支撑秩支付；整个宏还须把新 phase 纳入 terminal-first 调度。 |

所以 (21) 是全 \(d=3\) 分支的明确 **adapter candidate**，而非当前合同下的
`verified_edge`。还需定向仿射尾饱和的账本规则、source-tree scope 的跨图表传播、
target typed classification 与 terminal-first 优先门，才能把它登记为递归宏。

## 5. \(d=9\) 的局部控制与反例

当 \(h\equiv2\pmod3\) 时，类似计算给出

\[
\Delta=\frac{128h-64}{3},
\qquad
\Phi_\Delta(p-9,7,1)
=\left(24h-8,\frac{128h-43}{3},1\right).
\tag{22}
\]

因此只要旧 G raw Reach 包含 \(\{7,p-9\}\)，并将它重定向为 \((p-9,7)\)，就有相同的偶侧 source-switch
候选，并可再走 \(d=9\) dual 到 (20) 的 \(A'=9\) 版本。

这不是全称事实。\(p=193\) 是正控制：旧 G anchor 有实际路径

\[
\begin{aligned}
\{1,190\}&\xrightarrow5\{38,153\}
\xrightarrow{17}\{9,182\}
\xrightarrow7\{26,165\}\\
&\xrightarrow{11}\{15,176\}
\xrightarrow{11}\{16,175\}
\xrightarrow5\{35,156\}
\xrightarrow5\{7,184\}.
\end{aligned}
\tag{23}
\]

但 \(p=337\) 的完整 universal-source raw Reach 恰为

\[
\begin{aligned}
(337,112223,336)&\longrightarrow(1,334,1)\\
&\xrightarrow{167}(2,333,1)
\xrightarrow{37}(9,326,1)
\xrightarrow{163}(2,333,1),
\end{aligned}
\tag{24}
\]

其中不含 \(\{7,328\}\)。故 (22) 不能以同一指定 universal root 覆盖整个
\(d=9\) 分支。

此外，\(d=9\) target 的 canonical \(m=1\) anchor tree 甚至不能自行补齐这个缺口。
令 \(x=p-9\)，则

\[
2x<R<3x,
\qquad
M=K/x=\frac{50h+2}{3}\ \text{为偶数}.
\tag{25}
\]

一个 \(m=1\) 前驱若进入 \(\{x,R-x\}\)，唯一可能的素数为 \(q=2\)，但

\[
v_2(2x)\le v_2(K),
\tag{26}
\]

不满足 raw 超容量条件。因此该 seed 在 target 的 \(m=1\) bottom 图中无入边。
这不排除 \(m>1\) 的形式前驱，也不排除新的 source root；例如 \(p=193\) 中确有
\((736,797,3)\) 经 \(q=2\) 和 gcd 约分到该 seed node。

## 6. 边界与下一步

偶侧编码消除了“补余 seed 没有 raw node”这一假障碍，却没有自动生成跨图表
action。随后得到的 [\(m=1\) raw interface 刚性](type-I-g-anchor-complement-seed-m1-interface-rigidity.md)
进一步表明：(21) 不能由 source-preserving 的 \(q=p\) action intertwiner 证明；\(c=3\)
只能把 target 到达性缩至一个带相位 \(\pm M\) 的 \(t=4\) gate，而 \(c=9\) 在整个
\(m=1\) 图中无入边。因而当前最窄的正向任务是把 target source 的 raw receipt 升格为带版本、
可验证的 source macro，并证明其 source-tree scope、typed classification、terminal-first 与 E5
宏调度可在全 \(d=3\) 分支兼容。
[affine-prime target-source 模板](type-I-g-anchor-c3-affine-prime-target-source-template.md)
及其 [双中间节点推广](type-I-g-anchor-c3-two-intermediate-target-source-template.md)
已经给出多条条件性的 \(d=3\) target-chart raw path，但尚未完成这层合同。\(d=9\) 则需要一个
覆盖 (24) 反例的新 source family、\(m>1\) 接口或不同的非线性 action；
[二进高层前驱卡](type-I-g-anchor-c9-dyadic-high-layer-predecessor.md) 只提供局部前驱，不能替代
该 source receipt。

在进入上述 provenance 难题之前，选择器还应优先运行
[\(n-2\) 直接终端筛](type-I-g-anchor-complement-seed-n-minus-two-terminal-sieves.md)：它已经
从两类补余常数提取出 gap-11、gap-23 Type II 子族和一条 \(R=11\) gap-7 Type I 射线；
更一般的 [\(p+12/p+36\) 因子 terminal fan](type-II-p-plus-12-36-divisor-terminal-fan.md)
把这两条特例扩展为可按因子检索的直接 Type II 扇。这些都是原始 \(p\) 的 direct terminal，
不需要 source-switch。

本卡不把 raw node、source switch 或 \(\operatorname{Sol}(p)\) 的恒等映射单独冒充为
E1--E5 递归边，也不声称 Erdos--Straus 猜想已被解决。
