---
kind: claim
claim_id: type-I-g-anchor-c3-affine-prime-target-source-template
title: c=3 补余 seed 的 affine-prime target-source raw 模板
statement: 令 u>=0、h=3+42u，并设 p=1008u+73、alpha=2184u+151、beta=624u+43、gamma=546u+37 均为素数，且 u 不等于 3 (mod 13)。则 c=3 补余 target chart (R,K)=(4368u+303,(1092u+79)(1008u+70)) 有一条从其自身 canonical p-source 出发的实际 raw 路径：p、alpha、beta、2、gamma、13、2、2 依次把 source 送至 complement seed {x,R-x}，其中 x=1008u+70。anchor 到 t=4 node 的标签积 W=2 alpha beta gamma 13 满足 W=-M (mod R)，全 anchor-word 积为 -13 (mod R)，恰过 determinant--raw endpoint gate。该构造是条件性的 fresh target-source raw provenance，不是 old G chart 的 transport，也尚未定义 even-tail mark 的 E3 verifier、全域解提升或 E5 宏调度；因而不是 verified_edge。反过来，任何标签积为固定常数的 anchor word 都不能在这一无界族上到达 t=4 node，故统一模板必须使用随 h 变化的标签或无界的词复杂度。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-complement-seed-m1-interface-rigidity
  - type-I-g-anchor-even-tail-complement-source-switch
  - type-I-g-anchor-full-q-complement-r11-reset-boundary
  - type-I-g-anchor-marked-raw-peeling-calculus
  - type-I-universal-p-source-capacity-anchor-orbit
  - denominator-escape-state-contract
topics:
  - type-I
  - G-anchor
  - complement-torsor
  - c3
  - target-source
  - raw-path
  - affine-prime
  - phase
  - even-tail
  - no-go
  - proof-boundary
sources:
  - claim: type-I-g-anchor-complement-seed-m1-interface-rigidity
    role: endpoint-phase-gate-and-even-tail
  - claim: type-I-g-anchor-even-tail-complement-source-switch
    role: c3-complement-seed-and-even-side-encoding
  - claim: type-I-g-anchor-full-q-complement-r11-reset-boundary
    role: conditional-R11-reset-after-verified-receipt
  - claim: type-I-g-anchor-marked-raw-peeling-calculus
    role: raw-transition-semantics
  - claim: type-I-universal-p-source-capacity-anchor-orbit
    role: canonical-p-source-formula
  - concept: denominator-escape-state-contract
    role: E1-E5-admission-boundary
visibility: public
last_checked: '2026-08-06'
---

# \(c=3\) 补余 seed 的 affine-prime target-source raw 模板

## 1. 条件族与 target chart

令

\[
u\in\mathbb N_0,
\qquad
h=3+42u,
\tag{1}
\]

并定义四个仿射数

\[
\begin{aligned}
p&=24h+1=1008u+73,\\
\alpha&=2184u+151,\\
\beta&=624u+43,\\
\gamma&=546u+37.
\end{aligned}
\tag{2}
\]

本卡的前提是 (2) 中四个数都是素数，且

\[
u\not\equiv3\pmod {13}.
\tag{3}
\]

这里不声称满足这些素数条件的 \(u\) 有无穷多个；下文只是给出一个可逐项验证的
条件性 raw 模板。由 \(h\equiv0\pmod3\)，这属于 full-\(Q\) 补余构造的
\(c=3\) 分支。它现在是更一般的
[双中间节点 target-source 模板](type-I-g-anchor-c3-two-intermediate-target-source-template.md)
在 \((a,b)=(7,2)\) 下的特例；保留本卡是为了记录该最短骨架及其显式 affine 标签。
写其 target 数据为

\[
\begin{aligned}
R&=104h-9=4368u+303,\\
M&=26h+1=1092u+79,\\
x&=p-3=24h-2=1008u+70,\\
y&=R-x=3360u+233,\\
K&=Mx,
\qquad n=13.
\end{aligned}
\tag{4}
\]

直接有

\[
pR+1=4Mx=4K,
\qquad
R=4M-13,
\qquad
13x=3R+1.
\tag{5}
\]

所以 \(\{x,y\}\) 是现有补余构造给出的 physical determinant seed；其偶侧
编码为 \(t=1\)。下文要补的是它在 target 图表内的一个条件性 raw source path，
而不是把它当作旧 G 图表路径的像。

## 2. 从 target canonical source 到 seed 的显式词

对本图表自身，取有序形式源

\[
\mathsf S_T=
\bigl(p,\ R(p-1)-p,\ p-1\bigr).
\tag{6}
\]

这条首边也满足完整的 raw unit 条件。因为
\(R-4p=8h-13\) 且 \(0<8h-13<p\)，有 \((p,R)=1\)。又
\(M=p+2h\)、\(x=p-3\)，所以 \(p\nmid K=Mx\)，从而
\(v_p(p)>v_p(K)\)。并且
\(\bigl(p,R(p-1)-p\bigr)=1\)，故 source node primitive，\(q=p\) 也与
\(R(p-1)\bigl(R(p-1)-p\bigr)\) 互素。其 raw 边的 shift 为 \(1\)，且没有 gcd 约分：

\[
\mathsf S_T
\xrightarrow{p}
(1,R-1,1)=N_R(1).
\tag{7}
\]

以下五个恒等式指定其后的 anchor word：

\[
\begin{aligned}
R-1&=2\alpha, & R-2&=7\beta,\\
R-7&=8\gamma, & R-4&=13(8h-1),\\
R-(8h-1)&=4x.
\end{aligned}
\tag{8}
\]

因而，逐步选择等号左侧相应的坐标，可得完整的 \(m=1\) raw 路径

\[
\begin{aligned}
N_R(1)
&\xrightarrow{\alpha}N_R(2)
\xrightarrow{\beta}N_R(7)
\xrightarrow{2}N_R(4\gamma)\\
&\xrightarrow{\gamma}N_R(4)
\xrightarrow{13}N_R(8h-1)=N_R(4x)\\
&\xrightarrow{2}N_R(2x)
\xrightarrow{2}N_R(x).
\end{aligned}
\tag{9}
\]

等式 \(N_R(8h-1)=N_R(4x)\) 表示同一个无序节点：它的两坐标正是
\(8h-1\) 和 \(4x\)。为避免该无序记号掩盖实际 raw 操作，(9) 的中段可写成

\[
\begin{aligned}
(4,R-4,1)
&\xrightarrow{13}(8h-1,4x,1)\\
&\xrightarrow{2}(2x,R-2x,1)
\xrightarrow{2}(x,R-x,1).
\end{aligned}
\tag{10}
\]

每一步都遵循标准 raw 公式：若当前 \(m=1\) 且选择坐标 \(U\) 的素因子 \(q\)，
则 shift 是 \(q-1\)，输出为

\[
\left(\frac Uq,\frac{V+R(q-1)}q,1\right).
\tag{11}
\]

在 (9) 中，所选坐标依次为

\[
R-1,\quad R-2,\quad R-7,\quad4\gamma,\quad
R-4,\quad4x,\quad2x.
\tag{12}
\]

由 (8) 和起点 \((1,R-1)=1\)，每个输出节点均保持 primitive，故 (9) 的
gcd reduction 始终为 \(1\)。

## 3. 容量与单位条件

该路径不是只在模 \(R\) 中的形式连线。下面逐项检查 raw 超容量条件。
首先

\[
M\text{ 为奇数},
\qquad
x=2(504u+35),
\qquad
v_2(K)=1,
\tag{13}
\]

而 \(\gamma\) 为奇数。因此 (8) 和 (13) 给出三条 \(q=2\) 边的有效高度：

\[
v_2(R-7)=3>1,
\qquad
v_2(4x)=3>1,
\qquad
v_2(2x)=2>1.
\tag{14}
\]

对三个随 \(u\) 变化的素数标签，以下恒等式排除它们进入 \(K=Mx\)：

\[
\begin{array}{c|cc}
q & \text{排除 }q\mid M & \text{排除 }q\mid x\\ \hline
\alpha & 2M=\alpha+7 & 13x=6\alpha+4\\
\beta & 4M=7\beta+15 & 13x=21\beta+7\\
\gamma & M=2\gamma+5 & 13x=24\gamma+22
\end{array}
\tag{15}
\]

因为 \(\alpha\ge151\)、\(\beta\ge43\)、\(\gamma\ge37\)，(15) 蕴含

\[
\alpha\nmid K,
\qquad
\beta\nmid K,
\qquad
\gamma\nmid K.
\tag{16}
\]

最后，\(M\equiv1\pmod {13}\)，并且

\[
x\equiv7u+5\pmod {13}.
\tag{17}
\]

故条件 (3) 恰好保证 \(13\nmid K\)。这证明 (9) 中每个奇素数标签都具有
严格超过 \(v_q(K)=0\) 的高度。各标签与 \(R\) 也互素：这对
\(\alpha,\beta,\gamma,13\) 分别由 (8) 的余数 \(1,2,7,4\) 给出，对 \(2\)
由 \(R\) 为奇数给出。于是每步的 unit、shift 和容量条件都成立。

## 4. 精确相位与接口门

令从 anchor 到 \(N_R(4x)\) 的前缀标签积为

\[
W=\alpha\beta\cdot2\cdot\gamma\cdot13.
\tag{18}
\]

逐步按 (11) 跟踪有序坐标，或直接连续使用 (8)，得到

\[
W(8h-1)\equiv1\pmod R.
\tag{19}
\]

另一方面，(4) 给出恒等式

\[
M(8h-1)=2hR-1.
\tag{20}
\]

所以

\[
\boxed{W\equiv-M\pmod R.}
\tag{21}
\]

末端两条 \(2\)-边把标签积再乘 \(4\)。由 \(4M=R+13\)，完整 anchor word
满足

\[
\boxed{
\alpha\beta\cdot2\cdot\gamma\cdot13\cdot2\cdot2
=4W\equiv-13\pmod R.
}
\tag{22}
\]

这正好满足 determinant--raw endpoint gate：到 seed \(N_R(x)\) 的任何
\(m=1\) word 都必须有标签积 \(\pm13\pmod R\)。更强地，因
\(N_R(4x)\) 是精确 even-tail 的 \(t=4\) 层，它的前缀积必须是
\(\pm M\pmod R\)；(21) 给出了所需的负相位。

因此，(7)--(9) 不只是终点碰巧重合，而是在 source、容量、精确尾和 endpoint
phase 四个 raw 字段上同时闭合。

## 5. 三个控制实例

下表列出三个满足前提的控制点。表中只列 anchor 之后的标签；首个 \(p\)-边由
(7) 固定。

\[
\begin{array}{c|c|c|c|c|c|c|c}
u&p&R&M&x&\alpha&\beta&\gamma\\ \hline
0&73&303&79&70&151&43&37\\
2&2089&9039&2263&2086&4519&1291&1129\\
5&5113&22143&5539&5110&11071&3163&2767
\end{array}
\tag{23}
\]

例如 \(u=0\) 时，(9) 展开为

\[
\begin{aligned}
\{1,302\}
&\xrightarrow{151}\{2,301\}
\xrightarrow{43}\{7,296\}
\xrightarrow{2}\{148,155\}\\
&\xrightarrow{37}\{4,299\}
\xrightarrow{13}\{23,280\}
\xrightarrow{2}\{140,163\}
\xrightarrow{2}\{70,233\}.
\end{aligned}
\tag{24}
\]

其 anchor-word 积为 \(-13\pmod {303}\)，而到 \(\{23,280\}=N_R(4x)\)
的前缀积为 \(-79\pmod {303}\)，分别与 (22)、(21) 一致。\(u=2,5\) 的
四个仿射数同样都是素数，故给出独立的非最小控制点，而不只是 \(p=73\) 的偶然例子。

## 6. 固定常数标签词的 no-go

这一正例的标签必须随 \(h\) 变化。更精确地，考虑任何与 \(h\) 无关的 literal
anchor word，令其正标签积为常数 \(\Theta\)。若它到达 \(N_R(4x)\)，endpoint
gate 强制

\[
\Theta\equiv\pm M\pmod R,
\qquad
M=26h+1,
\qquad
R=104h-9.
\tag{25}
\]

当

\[
h>
\max\left\{
\frac{\Theta-1}{26},\
\frac{\Theta+10}{78}
\right\},
\tag{26}
\]

有 \(0<M-\Theta<R\)，故 \(\Theta\not\equiv M\pmod R\)；同时
\(0<\Theta+M<R\)，故 \(\Theta\not\equiv-M\pmod R\)。于是这样的词不能
到达 \(t=4\) node，更不可能接上末端的 \(2,2\) tail。

作为推论，若一个统一方案只允许固定有限标签表并把词长一致地限制在某个常数，
则它只有有限多个可能的 \(\Theta\)，因而至多覆盖有限多个本族参数。该 no-go 不排除
本卡的仿射标签，也不排除随 \(h\) 增长的词长或其它非局部 source macro。

## 7. 合同边界

这条路径从 **target 图表自身** 的 \(\mathsf S_T\) 出发。它不是旧
\(R_0=p-2\) 的 G-anchor word 的 transport：此前的 source-preserving \(p\)-edge
intertwiner no-go 仍然有效，不能被 (7) 绕过。这里得到的是一个独立的、条件性的
fresh target-source raw receipt，而不是 old G 到 complement seed 的 adapter。

把它升级为递归宏仍缺少合同层的内容：

| 项 | 当前结论 | 仍缺内容 |
|---|---|---|
| E1 | (6)--(9) 给出条件性的 raw source/path 数据。 | 把高 \(R\) fresh source 的 scope、root-entry 与 typed receipt 写入选择器。 |
| E2 | (4)--(5) 给出实际 determinant seed，且其 \(d=3\) dual 代数上落在 \(R=11\)。 | 将偶侧 \(t=1\) raw mark 注册为 verified overflow normal form。 |
| E3 | 每步 raw 算术已显式。 | 需要重算素数前提、方向、容量、相位、primitive 性、dual chart 与 scope 的 verifier。 |
| E4 | 若 seed 已有完整 receipt，现有 \(R=11\) RESET 可使用图表无关的 \(\operatorname{Sol}(p)\) 恒等 lift。 | 本卡的 raw/even-tail 段没有 marked-set 或全域解提升。 |
| E5 | (21)--(22) 提供可检查的 phase 数据。 | 尚无把该 phase、tail 与 terminal-first 调度相容的严格宏势支付。 |

因此本卡既不把 raw node 冒充为 short certificate，也不把这条条件路径称为
`verified_edge` 或完整 E1--E5 边。它把 \(c=3\) 的剩余问题收紧为：如何为这类
target-source receipt 定义可验证的 even-tail/source scope 接口，并证明相应的 lift 与
良基宏调度。
