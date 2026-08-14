---
kind: claim
claim_id: type-I-root-capacity-stutter-transverse-root-residue-low-gap-descent
title: 横向 stutter 根余数的低缺口 Type II 终端与严格两尾递降
statement: >-
  对核心素数 p≡1 mod24 的 terminal-first 后 actual proper-root stutter receipt，令
  D=mp+1-h、D|ph+1、D*=D/gcd(D,h^2-1)，并取奇素数 q|D*。对任意
  p+3 的奇除数 A 且 q∤A，令 K=<Ah>_q 为 Ah 模 q 的最小正剩余。若 K>A、K 为偶数、
  gcd(A,K)=1、K|(q+A)，且 s=(q+A)/K 属于 {3,7,11,23} 并满足
  s≡3 mod4A，则已有一般 A 型二次移位的正支自动命中，
  C=(p+s)/(4Aq) 为正整数，且
  4/p=1/(AqC)+1/(pACK)+1/(pqCK)。更强地，n=(p+s)/(s+1)<p，
  4/n=1/(AqC)+1/(ACK)+1/(qCK)，后两尾乘 p 恰恢复目标证书。这是一张
  actual transverse residual 到有界 gap 的直接 terminal 与显式 marked two-tail
  lift 的条件性适配器。特别地 A=1 的低 gap 条件精确等价于
  q|gcd(D*,sh-1) 且 q=-1 mod 2s，无需再选择 K；它不证明每个 residual
  必满足该 source-factor gate。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-finite-curve-constraint
  - type-I-root-capacity-stutter-transverse-general-quadratic-type-II-fan
  - type-II-factor-pair-carrier-strict-descent
  - short-certificate-equivalence
topics:
  - type-I
  - type-II
  - root-capacity
  - stutter
  - transverse-residual
  - root-residue
  - source-factor-gate
  - bounded-gap
  - strict-descent
  - marked-lift
  - terminal-dispatch
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-finite-curve-constraint
    role: actual-stutter-curve-identity
  - claim: type-I-root-capacity-stutter-transverse-general-quadratic-type-II-fan
    role: general-A-positive-branch-terminal-chart
  - claim: type-II-factor-pair-carrier-strict-descent
    role: factor-pair-two-tail-strict-lift
  - claim: short-certificate-equivalence
    role: direct-Type-II-certificate-verifier
  - reproduction: reproductions/type_i_root_capacity_stutter_transverse_root_residue_low_gap_descent.py
    role: q-local-root-residue-factor-gate-and-two-tail-lift-controls
visibility: public
last_checked: '2026-08-14'
---

# 横向 stutter 根余数的低缺口 Type II 终端与严格两尾递降

## 1. 目标和设置

固定核心素数

\[
p\equiv1\pmod {24}.
\]

terminal-first 后，设一个 actual proper-root stutter receipt 存在。沿用

\[
D=mp+1-h,
\qquad
D\mid ph+1,
\qquad
(D,h)=1,
\qquad
D_*=\frac{D}{(D,h^2-1)}.
\tag{1}
\]

有限曲线约束还给出某个正整数 \(a\) 使

\[
Da=m+h(h-1).
\tag{2}
\]

取一个奇素数

\[
q\mid D_*,
\tag{3}

\]

以及 \(p+3\) 的奇除数 \(A\)，并假设 \(q\nmid A\)。由于 \((q,h)=1\)，

\[
K=\langle Ah\rangle_q\in\{1,\ldots,q-1\}
\tag{4}

\]

定义良好。这里 \(\langle\cdot\rangle_q\) 表示最小正剩余。

本卡研究这一实际来源固定的根余数是否触发一个**有界缺口**的 Type II exit。令

\[
\mathcal G=\{3,7,11,23\}.
\tag{5}
\]

它恰是满足 \(s\equiv3\pmod4\) 且 \(s+1\mid24\) 的正缺口。因此，对每个
\(s\in\mathcal G\)，都有 \(s+1\mid p-1\)。

## 2. 根余数使一般二次移位和正支自动成立

由 \(q\mid D\)、(1) 和 (2)，分别有

\[
ph+1\equiv0\pmod q,
\qquad
m+h(h-1)\equiv0\pmod q.
\tag{6}
\]

定义 (4) 给出 \(K\equiv Ah\pmod q\)，故

\[
\begin{aligned}
mA^2+K(K-A)
&\equiv A^2\bigl(m+h(h-1)\bigr)\\
&\equiv0\pmod q,
\end{aligned}
\tag{7}
\]

并且

\[
Kp+A\equiv A(ph+1)\equiv0\pmod q.
\tag{8}
\]

所以现有一般 \(A\) 型二次扇中原本需要单独测试的二次移位和正支，在实际
\(K=\langle Ah\rangle_q\) 上同时自动命中。这并没有创造一张新的任意参数
Type II 图表；它把已有图表精确接回 actual transverse residual 的根高度。

## 3. 低缺口 dispatch 与证书

再假设

\[
K>A,
\qquad
K\equiv0\pmod2,
\qquad
(A,K)=1,
\tag{9}
\]

且

\[
K\mid q+A,
\qquad
s=\frac{q+A}{K}\in\mathcal G,
\qquad
s\equiv3\pmod {4A}.
\tag{10}
\]

因 \(s\ge3\) 和 \(K>A\)，有

\[
q=sK-A>K,
\tag{11}
\]

故 \(q>A\) 且 \((q,K)=1\)。又 \(p\ge73\)、\(s\in\mathcal G\)，所以
\(3\le s\le23<p-2\)。把 \(Ks=q+A\) 与 (8) 相加，得到

\[
K(p+s)=Kp+q+A\equiv0\pmod q,
\]

从而

\[
q\mid p+s.
\tag{12}
\]

另一方面，\(A\) 是奇数且 \(A\mid p+3\)，所以

\[
4A\mid p+3.
\tag{13}
\]

再由 (10)，\(4A\mid s-3\)。由于 \((q,4A)=1\)，(12)--(13) 给出

\[
C=\frac{p+s}{4Aq}\in\mathbb Z_{>0}.
\tag{14}
\]

令

\[
x=AqC,
\qquad
d=A^2C.
\tag{15}
\]

则 \(d\mid x^2\)、\(d\le x\)，且

\[
x+d=AC(q+A)=ACKs.
\tag{16}
\]

故 \((s,d)\) 是 Type II 除子证书，并恢复为

\[
\boxed{
\frac4p=
\frac1{AqC}+
\frac1{pACK}+
\frac1{pqCK}.}
\tag{17}
\]

这也是一般 \(A\) 型扇的正支：由 \(q=Ks-A\) 和 (10)，

\[
q\equiv3K-A\pmod {4AK}.
\tag{18}
\]

所以 (7)--(10) 是此前一般扇的一条 source-aware、root-residue 参数化，而不是对
其中的命中条件作无根据的放松。

## 4. 同一命中自动给出严格两尾递降

由 (5) 和 \(p\equiv1\pmod {24}\)，定义

\[
n=\frac{p+s}{s+1}\in\mathbb Z_{>0}.
\tag{19}
\]

显然 \(n<p\)。式 (16) 给出

\[
\begin{aligned}
\frac1{ACK}+\frac1{qCK}
 &=\frac{A+q}{AqCK}\\
 &=\frac{s}{AqC}.
\end{aligned}
\tag{20}
\]

因此有一对精确恒等式

\[
\boxed{
\frac4n=
\frac1{AqC}+
\frac1{ACK}+
\frac1{qCK},}
\tag{21}
\]

\[
\boxed{
\frac4p=
\frac1{AqC}+
\frac1{pACK}+
\frac1{pqCK}.}
\tag{22}
\]

也就是说，保留 (21) 的首分母、将后两尾乘以 \(p\)，正好恢复 (22)。这是一张
singleton marked two-tail lift：它只声称所写出的 \(4/n\) 解可提升，而不把任意
\(\operatorname{Sol}(n)\) 的解误作都可按同一公式提升。

## 5. 有界缺口的实际条件表

条件 \(s\equiv3\pmod {4A}\) 在 (5) 上没有隐含的无限案例：

| \(s\) | 允许的奇 \(A\) | 严格较小分母 \(n\) |
| ---: | --- | --- |
| \(3\) | 任意 \(A\) | \((p+3)/4\) |
| \(7\) | \(A=1\) | \((p+7)/8\) |
| \(11\) | \(A=1\) | \((p+11)/12\) |
| \(23\) | \(A\in\{1,5\}\) | \((p+23)/24\) |

表中还须保留 (9)--(10) 的实际根余数条件。它不是固定有限射线覆盖：例如
\(s=3\) 时 \(A\) 仍可以随 \(p+3\) 的奇因子变化；这里“有界”仅指 gap
\(s\le23\)，而不是声称所有分母或所有参数有绝对界。

## 6. \(A=1\) 的无选择 source-factor gate

对 \(A=1\)，第 3 节的 \(K\) 不必再作为一个待搜索参数。对任意
\(s\in\mathcal G\)，以下两组条件等价：

\[
\begin{aligned}
&K=\langle h\rangle_q,\quad K>1,\quad K\equiv0\pmod2,\quad
K\mid q+1,\quad \frac{q+1}{K}=s; \tag{23}\\
\Longleftrightarrow\quad
&q\mid sh-1,\qquad q\equiv-1\pmod {2s}. \tag{24}
\end{aligned}
\]

**证明。** 若 (23) 成立，\(q+1=sK\) 且 \(K\equiv h\pmod q\)，故
\(sh\equiv1\pmod q\)；又 \(K\) 为偶数，所以 \(2s\mid q+1\)。

反过来，若 (24) 成立，令

\[
K=\frac{q+1}{s}.
\tag{25}
\]

由于 \(q\equiv-1\pmod {2s}\)，\(K\) 是偶数。又 \(s\ge3\)，所以

\[
1<K<q.
\tag{26}
\]

式 \(sh\equiv1\equiv sK\pmod q\) 给出 \(K=\langle h\rangle_q\)，并且
\(q+1=sK\)，恢复 (23)。证毕。

因此定义完全由 actual receipt 数据给出的有限因子菜单

\[
\mathcal Q_s^{(1)}(D_*,h)
=\left\{
q:\ q\text{ 为奇素数},\
q\mid(D_*,sh-1),\
q\equiv-1\pmod {2s}
\right\}.
\tag{27}
\]

每个 \(q\in\mathcal Q_s^{(1)}(D_*,h)\) 都给出第 4 节的严格两尾递降，参数为

\[
K=\frac{q+1}{s},\qquad
C=\frac{p+s}{4q},\qquad
n=\frac{p+s}{s+1}.
\tag{28}
\]

这里不需要选择 \(A\)、\(K\) 或二次移位；只需分解四个固定整数
\(\gcd(D_*,sh-1)\)。此外，actual stutter 曲线给出可用的必要容量过滤：

\[
q\in\mathcal Q_s^{(1)}(D_*,h)
\Longrightarrow
q\mid ms^2-s+1.
\tag{29}
\]

确实，\(h\equiv s^{-1}\pmod q\) 与 \(m+h(h-1)\equiv0\pmod q\) 相乘以
\(s^2\) 即得 (29)。因此 (27) 是从 \(D_*,h\) 到 terminal/descent 的 exact
source-factor gate，而 (29) 为它与 stutter 参数 \(m\) 的独立交叉检查。

这不是另一张 Type II 家族：它只是将本卡的 \(A=1\) low-gap slice 完全压缩为
actual residual 的因子和剩余类条件。它也没有说明 \(\mathcal Q_s^{(1)}\) 对任意
actual receipt 必非空。

## 7. 三个 q-local 算术控制

第一个控制为 \(s=3\) 的无选择因子门：

\[
(p,q,h,m,K,s,C,n)=(337,17,6,4,6,3,5,85).
\tag{30}
\]

它给出

\[
\frac4{85}=\frac1{85}+\frac1{30}+\frac1{510},
\qquad
\frac4{337}=\frac1{85}+\frac1{10110}+\frac1{171870}.
\tag{31}
\]

第二个控制为 \(s=7\) 的同一因子门：

\[
(p,q,h,m,K,s,C,n)=(97,13,15,11,2,7,2,13).
\tag{32}
\]

它给出

\[
\frac4{13}=\frac1{26}+\frac14+\frac1{52},
\qquad
\frac4{97}=\frac1{26}+\frac1{388}+\frac1{5044}.
\tag{33}
\]

第三个控制使用 \(A>1\) 的一般根余数行：

\[
(p,A,q,h,m,K,s,C,n)=(1297,5,13,9,6,6,3,5,325),
\tag{34}
\]

于是

\[
\frac4{325}=\frac1{325}+\frac1{150}+\frac1{390},
\qquad
\frac4{1297}=\frac1{325}+\frac1{194550}+\frac1{505830}.
\tag{35}
\]

三个控制都只核对 \(q\)-local stutter 同余、根余数、低缺口和两尾恒等式；它们**不**
把局部算术元组冒充 actual root receipt。

## 8. 边界

本适配器实质上补上了“实际横向 residual 命中后，如何得到一个明确的严格小分母解及其
反向两尾提升”这一段；它没有补上全称选择器。尤其没有证明：

* 每个 actual \(D_*\) 都有奇素因子 \(q\)；
* 任意这样的 \(q\) 都使 \(K=\langle Ah\rangle_q\) 满足 (9)--(10)；
* 低缺口未命中时必存在另一张 Type I/II 证书或可登记的跨状态递降；
* 这些 singleton lifts 已满足 G/Type I 状态合同所需的完整 source lineage、
  target reclassification 与全局良基势。

因此它是一个条件性 `transverse_residual_provenance_adapter`，为命中状态提供直接
terminal 和严格数值势 \(p\mapsto n<p\)，但不是 Erdős--Straus 猜想、G/Type I
global exit 或全称短证书/递降引理的证明。

## 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_stutter_transverse_root_residue_low_gap_descent.py --verify
```

脚本只重放 (30)、(32)、(34) 的 q-local 算术和精确 two-tail lift，不扫描素数、根层、
分母或 selector 历史。
