---
kind: claim
claim_id: type-I-g-anchor-c3-factor-block-terminal-preemption
title: c=3 factor-block actual raw rays 的 terminal-first 整条截断
statement: 已证明实际 factor-block raw provenance 的五条 c=3 Dirichlet ray，以及其 h=8 mod19 的 core-19 交集 ray，分别都有对整条 affine 参数族成立的 Type II 平方因子终端。对每个素数参数点，终端同时给出一个严格更小实例的双尾解，因此 terminal-first 必须在任何 raw root 之前截断这些 ray。该结果不否定其它 c=3 raw path，也不证明完整 Type II 选择器；它把现有 factor-block positive families 从候选 root 列表中准确移除。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-c3-factor-block-raw-source-receipts
  - type-II-factor-square-tail-descent-family
  - type-II-small-shared-gap-explicit-fan
topics:
  - type-I
  - c3
  - raw-source
  - Dirichlet-ray
  - terminal-first
  - Type-II
  - strict-descent
  - proof-boundary
sources:
  - claim: type-I-g-anchor-c3-factor-block-raw-source-receipts
    role: actual-raw-ray-provenance
  - claim: type-II-factor-square-tail-descent-family
    role: Type-II-square-tail-and-lift-law
  - claim: type-II-small-shared-gap-explicit-fan
    role: gap-seven-terminal-context
  - reproduction: reproductions/type_i_c3_factor_block_terminal_preemption.py
    role: symbolic-affine-preemption-controls
visibility: public
last_checked: '2026-08-07'
---

# \(c=3\) factor-block actual raw rays 的 terminal-first 截断

## 1. 方形因子终端模板

先记一个已有 Type II 双尾递降族的直接形式。令

\[
p=4QT+1,
\qquad m=4Q-1,
\qquad d\mid Q^2,
\tag{1}
\]

并假设

\[
T\equiv-4d-1\pmod m,
\qquad 6\mid QT,
\qquad d\le Q(T+1).
\tag{2}
\]

设 \(x=Q(T+1)=(p+m)/4\)。则 \(d\mid x^2\)、\(m\mid x+d\)，因而

\[
\frac4p
=\frac1x
+\frac1{p(x+d)/m}
+\frac1{p(x+x^2/d)/m}.
\tag{3}
\]

两条带 \(p\) 的尾同时去掉 \(p\) 后，得到严格较小的实例

\[
\frac4{T+1}
=\frac1x
+\frac1{(x+d)/m}
+\frac1{(x+x^2/d)/m},
\qquad T+1<p.
\tag{4}
\]

这里 (3) 是 terminal-first 的直接输出；(4) 是同一数据的算术可提升严格递降，
不是尚未建立的 selector state edge。

## 2. 五条既有 raw Dirichlet ray 全部被截断

`type-I-g-anchor-c3-factor-block-raw-source-receipts` 已分别给出下表前五行的 actual
factor-block raw receipt，只要其仿射 \(p(s)\) 为素数。每一行写成
\(p(s)=4Q T(s)+1\)，并满足 (1)--(2)：

\[
\begin{array}{c|c|c|c|c}
\text{raw family}&p(s)&Q&(m,d)&T(s)\\ \hline
\text{compact }(7,2)&73+720720s&2&(7,1)&9+90090s\\
\text{class }3,(7,2)&73+5045040s&2&(7,1)&9+630630s\\
\text{class }1,(7,46)&1033+135944368560s&3&(11,3)&86+11328697380s\\
\text{class }0,(79,202)&3313+5335268223383280s&9&(35,3)&92+148201895093980s\\
\text{class }4,(15,2)&26737+22604400s&6&(23,3)&1114+941850s.
\end{array}
\tag{5}
\]

例如首行有 \(T\equiv2=-4\cdot1-1\pmod7\)，其余行同样由表中的常数项
直接验证；每条 \(T\) 的步长都被对应的 \(m\) 整除，且 \(6\mid QT\) 沿整条
参数线保持。因此，只要 (5) 的 \(p(s)\) 是素数，(3) 和 (4) 均成立。

这给出一个严格的调度结论：这些实际 raw receipt 不是新的 root 候选。terminal-first
必须在读取 raw word 前输出 (3)，故不能把“无穷多个 actual raw source”误写成
“无穷多个待递归 selector seed”。

## 3. core-19 raw ray 也被 \(m=7\) 截断

固定 \((a,b)=(7,2)\) 的精确容量条件与 \(h\equiv8\pmod {19}\) 相交后，取

\[
t=18+40755u.
\tag{6}
\]

它保留所有必要的 factor-block 条件

\[
t\equiv0\pmod3,
\qquad
t\not\equiv4\pmod5,
\qquad
t\not\equiv3\pmod{11},
\qquad
t\not\equiv9\pmod{13},
\tag{7}
\]

并给出已证明 actual raw receipt 的无穷 Dirichlet ray

\[
h=255+570570u,
\qquad
p=6121+13693680u,
\qquad
h\equiv8\pmod {19}.
\tag{8}
\]

这里 \((6121,13693680)=1\)，故有无穷多个素数参数点；但是

\[
p\equiv3\pmod7.
\tag{9}
\]

令

\[
Q=2,
\qquad m=7,
\qquad d=1,
\qquad
T=\frac{p-1}{8}=765+1711710u.
\tag{10}
\]

则 (1)--(2) 成立，故每个素数参数点均有 (3) 的 direct Type II terminal，
并由 (4) 严格降至 \(T+1=(p+7)/8\)。基点 \(p=6121\) 的显式终端见
`type-I-g-anchor-c3-core19-dual-leaf-raw-tree-p6121`。

因此 core-19 条件、actual raw source 及同图表双行 carry 算术本身并不足以进入
q-primary selector：这条最自然的交集 ray 在 terminal-first 之前已经结束。

## 4. 固定 Type II 模板的有限整条筛

这一截断也给出筛选下一条 affine substrate 的精确工具。设

\[
p(v)=P+Dv,
\qquad D\equiv0\pmod4,
\qquad
X_m(v)=\frac{p(v)+m}{4}=X_m(0)+\frac D4v,
\tag{11}
\]

其中 \(m\equiv3\pmod4\) 固定。一个固定正整数 \(d\) 在整条 ray 上都满足 Type II
的整除同余部分

\[
d\mid X_m(v)^2,
\qquad m\mid X_m(v)+d
\qquad(v\ge0)
\tag{12}
\]

当且仅当

\[
\boxed{
m\mid D,
\qquad
d\mid E_m^2,
\qquad
m\mid P+4d,
\qquad
E_m=\gcd\left(\frac{P+m}{4},\frac D4\right).
}
\tag{13}
\]

还须另验 \(d\le X_m(v)\) 的正性/高度条件。证明只用
\(\gcd_{v\ge0}X_m(v)=E_m\)：第一条整除等价于 \(d\mid E_m^2\)，第二条在
系数和常数项上分别等价于 \(m\mid D\) 与 \(m\mid P+4d\)。

(13) 是有限因子检查，适合排除“整条 affine ray 的固定 \((m,d)\) terminal”；
它不排除随参数变化的因子、单点 terminal 或其它 Type I/II 证书。因此不能将
未命中有限固定模板误称为 terminal-free。

## 5. 边界与下一步

本卡的推进是负向但结构性的：现有 factor-block positive families 已被从 root 候选中
精确剔除。它不否定 adaptive factor-block topology、mixed-side raw path，或任意点的
其它 Type II/Type I 出口。

下一条候选 substrate 应同时满足：actual raw receipt、\(h\equiv8\pmod {19}\)、
terminal residual，以及 \(R\) 含 \(1\pmod {19}\) 的因子。随后仍须独立构造
mixed-side 双叶来源、证明角色未被 fixed-layer stabilizer 杀掉，并完成 terminal-first、
phase/ledger 与 E4/E5 接口；本卡没有完成其中任何一项。

复现：

```bash
python3 reproductions/type_i_c3_factor_block_terminal_preemption.py --verify
```
