---
kind: claim
claim_id: type-I-formal-target-pair-descent-cycle-boundary
title: 形式目标因子对转移的 m 等于一支撑内循环边界
statement: 对互素正整数形式目标对 A+B=Rm，若 q|K、v_q(A)>v_q(K)，则题设 q 进转移在 m=1 时把无序对 {A,R-A} 精确送到 {A/q,R-A/q}，约分因子恒为 1。核心素数 p=6415417、线性源 (a,s,R)=(8,17017,47) 给出 K=75381150=2*3*5^2*13*29*31*43；其 K 支撑上的五个形式目标对 {45,2},{15,32},{16,31},{8,39},{4,43} 沿 q=3,2,2,2,2 构成严格超高循环，且每个节点只有一个可转移超高坐标。因此不存在一个在未增广形式对状态上沿全部此类边严格下降的良基势。五个循环因子对本身均不触发 Type I、端点 Type II 或广义二进终端，但同一 (p,R,K) 另有独立 Type I、Type II 与二进终端；故该反例只否定把全部形式迁移边无条件登记为递降，不否定先检测终端、剪去部分边或在增广合法状态上使用其它势函数的选择器。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-f-overflow-rational-gap-denominator
  - type-I-f-qadic-numerator-lift-rigidity-and-gcd-reduction
  - type-I-coprime-factor-normal-form
  - type-II-coprime-factor-normal-form
  - type-I-general-dyadic-terminal-transfer
  - type-I-dyadic-p-minus-one-factor-pair-selector
  - type-I-pminusone-b12-divisor-residue-selector
topics:
  - type-I
  - type-II
  - formal-target-pair
  - q-adic
  - support-preserving-cycle
  - well-founded-descent
  - dyadic-terminal
  - counterexample-boundary
  - proof-program
sources:
  - claim: type-I-f-overflow-rational-gap-denominator
    role: formal-target-pair-and-denominator-defect-interface
  - claim: type-I-f-qadic-numerator-lift-rigidity-and-gcd-reduction
    role: q-adic-gcd-reduction-boundary
  - claim: type-I-coprime-factor-normal-form
    role: direct-type-I-normal-form-verifier
  - claim: type-II-coprime-factor-normal-form
    role: endpoint-type-II-normal-form-verifier
  - claim: type-I-general-dyadic-terminal-transfer
    role: same-state-dyadic-terminal-verifier
  - claim: type-I-dyadic-p-minus-one-factor-pair-selector
    role: independent-p-minus-one-terminal-verifier
  - claim: type-I-pminusone-b12-divisor-residue-selector
    role: same-R-p-minus-one-terminal-verifier
visibility: public
last_checked: '2026-07-30'
---

# 形式目标因子对转移的 \(m=1\) 支撑内循环边界

## 1. 形式转移在 \(m=1\) 时的精确化简

设

\[
A+B=Rm,
\qquad
\gcd(A,B)=1,
\qquad
4K=pR+1,
\tag{1}
\]

并令素数 \(q\mid K\) 满足

\[
v_q(A)>v_q(K).
\tag{2}
\]

由 \(q\mid A\)、\((A,B)=1\) 得 \(q\nmid B\)；由 \(q\mid K\) 和
\(4K=pR+1\) 得 \(q\nmid R\)。因此 (1) 模 \(q\) 还给出 \(q\nmid m\)，从而存在
唯一的

\[
t\in\{1,\ldots,q-1\},
\qquad
t\equiv-m\pmod q.
\tag{3}
\]

题设的原始形式转移为

\[
\widetilde T_q(A,B,m)=
\left(
\frac Aq,
\frac{B+Rt}{q},
\frac{m+t}{q}
\right),
\tag{4}
\]

随后同时除以三个坐标允许的最大公因子。若 \(m=1\)，则 \(t=q-1\) 且 \(B=R-A\)，
所以 (4) 精确化为

\[
\boxed{
\widetilde T_q(A,R-A,1)
=
\left(
\frac Aq,
R-\frac Aq,
1
\right).
}
\tag{5}
\]

此时

\[
\gcd\!\left(\frac Aq,R-\frac Aq\right)
=\gcd\!\left(\frac Aq,R\right)=1,
\tag{6}
\]

故后置约分因子恒为 \(1\)。若允许在下一步把两个全局方向交换，则在无序对记号下，
(5) 就是

\[
\boxed{
\{C,R-C\}\longmapsto
\left\{\frac Cq,R-\frac Cq\right\}.
}
\tag{7}
\]

式 (7) 保持正性、互素性、\(m=1\) 和目标合同

\[
\frac AB\equiv-1\pmod R.
\tag{8}
\]

它没有在这些形式性质中留下自动严格下降的坐标。

## 2. 一个完整 \(K\) 支撑内的线性源反例

取

\[
\boxed{p=6{,}415{,}417,\qquad R=47.}
\tag{9}
\]

### 2.1 素性与线性源核验

这个 \(p\) 是素数。一个独立的 Lucas 素性证书为

\[
p-1=2^3\cdot3^3\cdot7\cdot4243,
\tag{10}
\]

其中 \(4243\) 为素数；以 \(19\) 为见证，有

\[
19^{p-1}\equiv1\pmod p,
\tag{11}
\]

并且对 \(r\in\{2,3,7,4243\}\)，数
\(19^{(p-1)/r}\bmod p\) 依次为

\[
6{,}415{,}416,\quad
4{,}235{,}574,\quad
2{,}588{,}861,\quad
4{,}593{,}057,
\tag{12}
\]

它们减 \(1\) 后与 \(p\) 的最大公因子均为 \(1\)。Lucas 判据遂证明 (9) 的素性。
另外 \(p\equiv1\pmod {24}\)。

该点还是一个完整线性源：

\[
p=8+17017+8\cdot17017\cdot47.
\tag{13}
\]

相应两块为

\[
8R+1=377=13\cdot29,
\tag{14}
\]

\[
17017R+1
=799800
=2^3\cdot3\cdot5^2\cdot31\cdot43.
\tag{15}
\]

所以

\[
\begin{aligned}
4K&=pR+1=(8R+1)(17017R+1)=301{,}524{,}600,\\
K&=75{,}381{,}150
=2\cdot3\cdot5^2\cdot13\cdot29\cdot31\cdot43.
\end{aligned}
\tag{16}
\]

特别地，\(\nu_2=v_2(K)=1\)、\(\nu_3=v_3(K)=1\)，且
\(\gcd(K,R)=1\)。

### 2.2 五节点循环

考虑以下无序形式目标对；每个坐标的全部素因子都属于 \(\operatorname{Supp}(K)\)：

| 节点 | 无序对 | 唯一超高坐标 | 所用素数 | 超高量 |
|---|---:|---:|---:|---:|
| \(S_0\) | \(\{45,2\}=\{3^2\cdot5,2\}\) | \(45\) | \(3\) | \(2-\nu_3=1\) |
| \(S_1\) | \(\{15,32\}=\{3\cdot5,2^5\}\) | \(32\) | \(2\) | \(5-\nu_2=4\) |
| \(S_2\) | \(\{16,31\}=\{2^4,31\}\) | \(16\) | \(2\) | \(4-\nu_2=3\) |
| \(S_3\) | \(\{8,39\}=\{2^3,3\cdot13\}\) | \(8\) | \(2\) | \(3-\nu_2=2\) |
| \(S_4\) | \(\{4,43\}=\{2^2,43\}\) | \(4\) | \(2\) | \(2-\nu_2=1\) |

每对之和都是 \(47\)，故 \(m=1\)；由于 \(47\) 为素数且所有坐标都在
\(\{1,\ldots,46\}\) 中，每对互素，并满足 (8)。表中的另一个坐标在 \(K\) 的逐素数
指数盒内，因此列出的超高坐标和素数在每个节点都是唯一的。

按 (4) 逐步计算，得到

\[
\begin{aligned}
(45,2,1)&\xrightarrow[q=3,\ t=2]{}
\left(15,\frac{2+47\cdot2}{3},1\right)=(15,32,1),\\
(32,15,1)&\xrightarrow[q=2,\ t=1]{}
\left(16,\frac{15+47}{2},1\right)=(16,31,1),\\
(16,31,1)&\xrightarrow[q=2,\ t=1]{}(8,39,1),\\
(8,39,1)&\xrightarrow[q=2,\ t=1]{}(4,43,1),\\
(4,43,1)&\xrightarrow[q=2,\ t=1]{}(2,45,1).
\end{aligned}
\tag{17}
\]

最后一个有序对是第一个有序对的交换。因此，在允许全局换向的无序形式状态上，

\[
\boxed{
S_0\longrightarrow S_1\longrightarrow S_2
\longrightarrow S_3\longrightarrow S_4\longrightarrow S_0
}
\tag{18}
\]

是一个五周期。所有边都满足题设的真实严格超高条件，并且整个周期不离开
\(\operatorname{Supp}(K)\)。这不是由新素因子偶然进入所造成的伪循环。

## 3. 对全边良基势的否定

设 \((W,\prec)\) 是任意良基严格序，且假设存在只依赖未增广形式状态的势函数

\[
\Phi:\{(p,R,K,\{A,B\},m)\}\longrightarrow W
\tag{19}
\]

使每一条满足题设条件的形式转移边都严格下降。对 (18) 连用五次便得到

\[
\Phi(S_0)\succ\Phi(S_1)\succ\Phi(S_2)
\succ\Phi(S_3)\succ\Phi(S_4)\succ\Phi(S_0),
\tag{20}
\]

与严格序的非自反性矛盾。因此：

\[
\boxed{
\text{不存在沿全部未剪枝形式转移边严格下降的状态内良基势。}
}
\tag{21}
\]

这比排除某个简单的 \(L^1\)、\(m+A+B\) 或字典序势更强；它排除所有以同一个无序形式
状态为自变量、并要求每条原始边都严格下降的势。

若把方向保留为有序标签，则 (17) 中的换向必须作为允许的零成本操作处理。一个势若在
换向时可以任意增大，就不能证明允许换向的算法终止；若要求换向不增，则同一周期仍给出
(20)。

## 4. 循环节点不是因子对终端，但同一状态已有独立终端

必须区分“循环中的这一个因子对产生终端”与“同一 \((p,R,K)\) 存在另一个终端”。
本例精确展示了两者不同。

### 4.1 五个循环因子对均不直接产生 Type I

对互素的 \(K\)-支撑目标对，落在原 \(K\) 指数盒内等价于 \(AB\mid K\)。五个节点的
乘积依次为

\[
90,\quad480,\quad496,\quad312,\quad172.
\tag{22}
\]

它们分别在 \(3\) 或 \(2\) 上超过 (16) 的指数，故都不整除 \(K\)。所以五个形式对
本身都不是原盒中的 Type I 目标命中。

### 4.2 五个循环因子对均不直接产生端点 Type II

若把节点的互素两坐标作为 Type II 正规形的前两项，则合法缺口 \(h\) 必须整除
\(A+B=47\)。在自然范围内唯一可能的是 \(h=47\)，而

\[
x_{47}=\frac{p+47}{4}=1{,}603{,}866.
\tag{23}
\]

用 (22) 中五个乘积除 (23)，余数依次为

\[
66,\quad186,\quad298,\quad186,\quad138.
\tag{24}
\]

故没有一个节点满足端点 Type II 的必要充分条件 \(AB\mid x_{47}\)。

### 4.3 五个循环因子对均不直接产生广义二进终端

每个节点都满足 \(A/B\equiv-1\pmod {47}\)。但

\[
\operatorname{ord}_{47}(2)=23
\tag{25}
\]

是奇数，所以 \(-1\notin\langle2\rangle\subset(\mathbb Z/47\mathbb Z)^\times\)。
因此任意 \(j\ge1\) 都不可能使该节点的两个坐标满足

\[
A\equiv2^jB\pmod {47}
\tag{26}
\]

或其反向。五个循环因子对本身都不能调用广义二进终端判据。

### 4.4 同一 \((p,R,K)\) 的独立终端

尽管循环因子对自身均不终止，同一状态并不是 F-box miss，也不是 Erdős--Straus
反例。它至少有以下三类独立出口。

**Type I。** 取合法缺口 \(h=11\)、

\[
x=\frac{p+11}{4}=1{,}603{,}857,
\qquad e=129=3\cdot43.
\tag{27}
\]

则

\[
4e+1=11\cdot47,
\qquad
K=xR-e,
\qquad
e\mid x.
\tag{28}
\]

对应的 Bradford Type I 证书除子为

\[
d=\frac{x^2}{e}=19{,}940{,}754{,}081,
\tag{29}
\]

其互素正规形为

\[
(A_I,B_I,C_I)=(12{,}433,1,129).
\tag{30}
\]

这里 \(x=A_IB_IC_I\)、\(d=A_I^2C_I\)，并且
\(B_Ip+A_I=p+12{,}433=11\cdot584{,}350\)，所以 Type I 正规形条件全部成立。
直接恢复得到

\[
\frac4p
=\frac1{1{,}603{,}857}
+\frac1{937{,}213{,}837{,}950}
+\frac1{483{,}601{,}511{,}189{,}550}.
\tag{31}
\]

**Type II。** 取缺口 \(h=3\)、

\[
x=\frac{p+3}{4}=1{,}603{,}855,
\qquad d=5.
\tag{32}
\]

则 \(d\mid x^2\)、\(d\le x\)、\(3\mid x+d\)，其互素正规形为

\[
(A_{II},B_{II},C_{II})=(1,320{,}771,5),
\tag{33}
\]

因为 \(3\mid A_{II}+B_{II}=320{,}772\)。

**广义二进终端。** 令 \(L=2K=150{,}762{,}300\)，取

\[
(a_d,b_d,j)=(1,435,2),
\qquad 435=3\cdot5\cdot29.
\tag{34}
\]

则 \(a_d,b_d\mid L\)、\((a_d,b_d)=1\)，且

\[
1\equiv2^2\cdot435\pmod {47},
\qquad
1<2^2\cdot435.
\tag{35}
\]

这里 \(v_2(L)=2\)，所以 \(j=2\) 用尽但不超过二进预算。对应

\[
E_2=2^{-1}L\frac1{435}=173{,}290,
\qquad
n=\frac{2L-E_2}{47}=6{,}411{,}730,
\tag{36}
\]

其中 \(n\) 是严格小于 \(p\) 的正偶数。

仓库原有冻结档案还给出了两个更直接的 \(p-1\) 终端记录：

- [B1/B2 菜单一千万范围档案](../reproductions/type-i-pminusone-b12-menu-profile-10m-results.json)
  保存
  \[
  (E,B,C,H,h,n)=(48,1,129,584350,11,p-1).
  \tag{37}
  \]
  这里 \(E-1=47\)，所以它正是同一 \(R=47\) 状态，并把 (27)--(30) 的缺口
  \(11\) Type I 证书桥到偶源 \(p-1\)。
- [二幂 p 减一的一千万范围档案](../reproductions/type-i-dyadic-pminusone-profile-10m-results.json)
  另存
  \[
  (\text{exponent},B,C,h,n)=(2,1,281,375,p-1),
  \tag{38}
  \]
  给出不依赖本循环因子对的另一张二幂 \(p-1\) 终端。

因此一个先调用正规形 verifier 的选择器会在进入 (18) 前直接停机；这个 \(p\) 也不属于
需要由形式迁移闭合的选择器余核或猜想困难实例。循环只会击中“忽略已有终端并把每一条
形式超高转移都当作递降”的规则。

## 5. 不能直接升级为合法 Erdős--Straus 解提升

形式转移 (4) 确实保持一个同余关系，但它没有提供

\[
\Phi_{T\to S}:W_T\longrightarrow W_S
\tag{39}
\]

这样的标记解提升映射。更具体地：

1. \(m\) 是辅助关系 \(A+B=Rm\) 的商，不是 Erdős--Straus 方程的源分母；即使
   \(m>1\) 时下降，也没有降低根目标分母 \(p\)。
2. 形式后继默认没有独立定义的 equation target、marked solution set 和正规形；只保留
   (8) 不能把它登记为新的算术状态。
3. 本例在 \(m=1\) 处回到同一个形式状态，直接否定原始全边系统的 strict decrease
   义务。
4. 即使某条轨道最终落入 \(AB\mid K\) 的盒内，那也是为同一 \(p\) 直接重建一张
   Type I 证书，而不是从较小实例的任意解提升回 \(p\)。

所以 (4) 当前至多是目标表示搜索中的 analysis_evidence。要把某个剪枝后的子族升级为
合法边，仍必须另行给出合法后继状态、正规形 verifier、全域解提升和一个在该实际选定
边集上严格下降的良基势。

## 6. 精确边界

本反例证明的是：

\[
\boxed{
\text{全部形式超高边}\not\subseteq
\text{一个未增广状态上的严格递降关系。}
}
\tag{40}
\]

它不证明以下更强的否定命题：

- 不存在先检查 Type I/II/二进终端、再选择边的算法；
- 不存在删去至少一条循环边后的规范选择器；
- 不存在把方向、已用资源、合法标记或其它算术秩加入状态后的其它势函数；
- 不存在完全不同的 support switch、Type II 旁路或解提升机制。

不过，任何这样的修复都必须明确改变边集或状态合同。仅仅给原循环事后赋予一个有限图
拓扑编号，或允许势在无成本换向时上升，不能恢复对原始全边系统的终止证明。
