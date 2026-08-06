---
kind: claim
claim_id: type-I-fixed-layer-stabilizer-defect-reduction
title: 固定层稳定子缺陷约化
statement: 设 H 为有限单位子群且固定层 J subset H 含单位元，P=Stab_H(J)。则 P subset J、pi(J) 无周期，并且任意残余乘积 J product_i S_i 在 H/P 中保持精确成员关系、固定目标表示数和 Fourier 系数的稳定子约化。当 J=C_R(N) 是中心化固定层时，该乘积就是 C_R(K)，故 F 缺失可限制到 quotient characters，并把非平凡谱阈值从 |H|-1 收紧为 |H/P|-1。若 -1 不属于 H，应先分出 G 型支撑障碍。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- general-b
- fixed-layer
- stabilizer
- Kneser
- finite-abelian-groups
- F-state
- G-state
- proof-program
sources:
- paper: grynkiewicz_marchan_ordaz2009
  locator: Theorem C
  role: finite-sumset-growth-context
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-terminal-selector-context
visibility: public
last_checked: '2026-08-07'
---

# 固定层稳定子缺陷约化

## 设置

先给出任意固定层的有限群版本。设 $R$ 为奇数，

\[
H\le(\mathbb Z/R\mathbb Z)^\times,
\qquad 1\in J\subseteq H,
\qquad S_i^{\pm}=\{q_i^z:-b_i\le z\le b_i\}\subseteq H,
\]

并令

\[
\mathcal P_J=J\prod_{i=1}^{k}S_i^{\pm}.
\tag{1}
\]

中心化 Type I 应用是下列特殊情形：

\[
K=N\prod_{i=1}^{k}q_i^{b_i},
\qquad
H=\left\langle q:q\mid K\right\rangle,
\qquad
J=\mathcal C_R(N).
\]

此时 $q_i$ 是固定层 $N$ 以外的不同素数，并且

\[
\mathcal C_R(K)=\mathcal P_J.
\]

这里不假设 $J$ 是子群；通常它只是含单位元的对称有限子集。

## 稳定子约化定理

令

\[
P=\operatorname{Stab}_H(J)=\{h\in H:hJ=J\},
\qquad
\pi:H\to H/P.
\]

则：

1. $P\subseteq J$，因而 $JP=J$；
2. $\pi(J)$ 在 $H/P$ 中无周期，即
   $\operatorname{Stab}_{H/P}(\pi(J))=\{P\}$；
3. 投影保持积集恒等式：
   \[
   \boxed{\pi(\mathcal P_J)
   =\pi(J)\prod_i\pi(S_i^{\pm}).}
   \]
4. 若 $-1\in H$，则目标成员关系精确保留：
   \[
   \boxed{
   -1\in\mathcal P_J
   \Longleftrightarrow
   \pi(-1)\in\pi(J)\prod_i\pi(S_i^{\pm}).}
   \]

在中心化应用 $J=\mathcal C_R(N)$ 中，第三、四项的 $\mathcal P_J$ 可分别替换为
$\mathcal C_R(K)$。

若 $-1\notin H$，第四项不适用；该状态先归入 G 型支撑障碍，不能在商群中写成
一个不存在的 $\pi(-1)$。

### 证明

因为 $1\in J$，若 $x\in P$，则
$x=x\cdot1\in xJ=J$，故 $P\subseteq J$。稳定子定义也给出 $JP=J$。

对第三项直接投影积集恒等式即可。若 $xP$ 稳定 $\pi(J)$，则
\[
\pi(xJ)=xP\,\pi(J)=\pi(J),
\]
所以 $xJP=JP$。使用 $JP=J$ 得 $xJ=J$，即 $x\in P$。
因此投影后的固定层无周期，第二项成立。

最后，
\(\mathcal P_J=J\prod_iS_i^{\pm}\) 是 $P$-周期集，因为 $P$ 稳定 $J$。
一个元素是否属于该集合完全由它在 $H/P$ 中的像决定，故得到第四项。
证毕。

## 稳定子约化的 Fourier 精确接口

把

\[
\bar H=H/P,\qquad \bar J=\pi(J),\qquad
\bar N(\bar t)=\#\{(\bar j,z):\bar j\in\bar J,
\ -b_i\le z_i\le b_i,\ \bar j\prod_i\pi(q_i)^{z_i}=\bar t\}
\]

作为商群中的表示数。因为 \(P\subseteq J\)，\(J\) 是 \(P\)-coset 的不交并；对固定
的 \(t\in H\)，每个满足商群方程的 \((\bar j,z)\) 在原群中恰有一个 \(j\in J\) 使
\(j\prod_iq_i^{z_i}=t\)。因此有精确恒等式

\[
\boxed{N_J(t)=\bar N(\pi(t)).}
\tag{7}
\]

若把目标在整个 coset \(tP\) 上求和，才得到
\(\sum_{u\in tP}N_J(u)=|P|\,\bar N(\pi(t))\)。这一区分避免把稳定子大小错误地
重复计入固定目标的表示数。

令
\[
P^\perp=\{\chi\in\widehat H:\chi|_P=1\}\cong\widehat{\bar H}.
\]

对固定层 Fourier 系数
\[
A_J(\chi)=\left(\sum_{j\in J}\chi(j)\right)
\prod_iD_{b_i}(\chi(q_i))
\]
有两种互补情形：若 \(\chi\notin P^\perp\)，则按 \(P\)-coset 求和得到
\(A_J(\chi)=0\)；若 \(\chi=\bar\chi\circ\pi\in P^\perp\)，则

\[
\boxed{A_J(\chi)=|P|\,A_{\bar J}(\bar\chi).}
\tag{8}
\]

将 (7) 的商群表示数作角色展开，若 \(\bar N(\bar t)=0\)，则 \(|\bar H|>1\)，并且存在
\(1\ne\bar\chi\in\widehat{\bar H}\) 使

\[
\boxed{
|A_{\bar J}(\bar\chi)|\ge
\frac{|\bar J|\prod_i(2b_i+1)}{|\bar H|-1}.}
\tag{9}
\]

提升回 \(H\) 后，规范 F 证书可以限制在 \(P^\perp\setminus\{1\}\)，并满足更强的

\[
\boxed{
|A_J(\chi)|\ge
\frac{|J|\prod_i(2b_i+1)}{|H/P|-1}.}
\tag{10}
\]

相比未约化的 \(|H|-1\) 分母，(10) 在 \(|P|>1\) 时严格收紧角色幅度下界；同时
\(\bar J\) 已无周期，所以后续 Kneser/Fourier 处理不再重复支付固定层的周期部分。
若 \(|\bar H|=1\)，则商群目标必被零指数命中，不存在 F 缺失。

因此可把稳定子约化后的规范证书编码为

\[
\mathsf{SF}=\bigl(|H/P|,\operatorname{ord}(\bar\chi),
-|A_J(\chi)|,\operatorname{phase}(\bar\chi)\bigr),
\]

按商群阶、角色阶、谱幅度和相位分子作字典序选择。它把固定层的稳定子信息直接
接入规范 Fourier/关系格对象，而不是只登记一个群商。该证书仍是状态内对偶对象；
跨状态容量或解可提升递降仍需额外的 \(q\)-进拉回。

### 聚焦算术回执

下面先记录一个**一侧固定层切片**的有限群控制，而不是把它误作中心化固定层的回执。对

\[
(p,R,K)=(193,63,3040),\qquad K=608\cdot5,\qquad
J=\mathcal A_{63}(608):=\{d\bmod63:d\mid608\},\qquad P=\{1,2,4,8,16,32\},
\]

有 \(|H|=36\)、\(|H/P|=6\)、\(|J|=12\)、\(|\bar J|=2\)。取 residual block
\(q=5,\ b=1\)，则 \(-1\notin\mathcal C_{63}(K)\)，但 \(-1\in H\)；商群目标坐标为
\(3\)，且规范 quotient Fourier 角色的最大幅度为 \(2\sqrt3\)，超过阈值
\(2\cdot3/(6-1)=6/5\)。提升后的阈值为 \(12\cdot3/5=36/5\)，而幅度乘
\(|P|=6\) 后仍严格超过该值。

回执由

~~~bash
python3 reproductions/type_i_fixed_layer_stabilizer_fourier.py --verify
~~~

生成；它逐个目标元素核验 (7)、商群无周期和该切片的目标缺失/Fourier 下界。因为
\(\mathcal A_{63}(608)\prod\{5^{-1},1,5\}\subsetneq\mathcal C_{63}(3040)\)，该脚本的
`J`、计数向量和阈值**不能**被引用为中心化分解 \(\mathcal C_R(K)=J\prod S_i^{\pm}\) 的
数值回执；它是一个实际 F 状态上的 slice-local 对偶控制。

同一 $p=193$ 的中心化控制可取
\(J=\mathcal C_{63}(608)\)，得到 \(|J|=18\)、商表示向量
\((3,2,1,0,1,2)\) 和目标计数零。该完整中心化实例及其 target-odd 能量由
`reproductions/type_i_f_target_involution_fourier.py --verify` 单独重算，详见
[F 型目标对合的 target-odd Fourier 能量与 q-primary 相位塌缩](type-I-f-target-involution-fourier-phase-collapse.md)。

## 统一选择器中的 typed 对偶回执

固定层商 Fourier 不另造一个递归边类型，而是写入状态的
`certificate_context`，其最小字段为

```text
certificate_type = fixed_layer_quotient_fourier
selector_status = analysis_evidence
state_class = F 或 G
phase = DUAL_CERTIFICATE
quotient_order = |H/P|
stabilizer_order = |P|
character_order = ord(chi_bar)
amplitude_squared = |A_J(chi)|^2
threshold_fraction = [|bar J| product_i(2 b_i + 1), |H/P|-1]
lifted_threshold_fraction = [|J| product_i(2 b_i + 1), |H/P|-1]
recursive_edge_eligible = false
```

`amplitude_squared` 和两个阈值分数优先于浮点幅度保存；规范字典序使用
\((|H/P|,\operatorname{ord}(\bar\chi),-|A_J(\chi)|^2,
\operatorname{phase}(\bar\chi))\)。因此该回执能作为 F/G 的规范表示—对偶证书，
但不能单独进入递归图。只有后续另行通过 E1--E5、给出全域解提升和严格势下降，才可
把它连接到 `support_switch`、`q_adic_lift` 或 `verified_edge`。

在上述一侧切片控制中，typed 载荷为

```text
certificate_type = fixed_layer_quotient_fourier
selector_status = analysis_evidence
state_class = F
quotient_order = 6
stabilizer_order = 6
character_order = 6
amplitude_squared = 12
threshold_fraction = [6, 5]
lifted_threshold_fraction = [36, 5]
recursive_edge_eligible = false
```

这一区分是统一选择器的类型安全边界：固定目标计数恒等式是状态内算术事实，商谱
幅度是对偶事实，二者都不能被误写成跨状态容量或解可提升递降。

## 商角色阶债务：连接 Fourier 与容量的中间字段

对残余块指数 \(b_i\)，令所选商角色满足

\[
\bar\chi(\pi(q_i))=e^{2\pi i\theta_i},
\qquad
\delta_i=\|\theta_i\|_{\mathbb R/\mathbb Z}.
\]

记归一化 Dirichlet 因子为

\[
\rho_b(\delta)=\frac1{2b+1}
\left|\sum_{z=-b}^{b}e^{2\pi iz\delta}\right|.
\]

对所有整数 \(b\ge1\) 和 \(0\le\delta\le1/2\)，有初等界

\[
-\log\rho_b(\delta)\ge
\frac1{60}\min\{1,b^2\delta^2\},
\tag{11a}
\]

其中 \(\rho_b(\delta)=0\) 时左侧按 \(+\infty\) 解释。证明可按
\(b\delta\le1/4\)、\(1/4<b\delta<1\) 和 \(b\delta\ge1\) 三段处理：第一段把
指数视为均匀变量并用 \(1-\cos u\ge2u^2/\pi^2\)，第二段用
\(|\sin x|\le1\) 及正弦凹性给出 \(\rho_b\le4/5\)，第三段用
\(|\sin((2b+1)\pi\delta)|\le1\)、\(\sin(\pi\delta)\ge2\delta\) 给出
\(\rho_b\le1/4\)。

由 (9) 的商群角色展开，若目标在商群中缺失，则某个非平凡角色满足
\(\prod_i\rho_{b_i}(\delta_i)\ge1/(|H/P|-1)\)，故

\[
\boxed{
\sum_i\min\{1,b_i^2\delta_i^2\}
\le 60\log(|H/P|-1).}
\tag{11}
\]

若 \(d_i=\operatorname{ord}(\bar\chi(\pi(q_i)))\)，则非平凡坐标满足

\[
\delta_i\ge\frac1{d_i},
\]

从而得到可离散记录的角色阶债务

\[
\boxed{
\mathsf D_{\rm ord}(\bar\chi)=
\sum_{\bar\chi(\pi(q_i))\ne1}
\min\left\{1,\left(\frac{b_i}{d_i}\right)^2\right\}
\le60\log(|H/P|-1).}
\tag{12}
\]

\(\mathsf D_{\rm ord}\) 是表示—对偶侧的有限字段：它可以按
\((q_i,d_i,b_i)\) 跨状态分组，但不能直接改写成 \(v_{q_i}(tR+1)\) 或其它算术高度。
只有另行证明角色阶、线性块颜色和 \(q_i\)-进载荷之间的映射，(12) 才能作为容量需求；
否则它仍是 `analysis_evidence`。这一区分避免把“角色阶小”错误解释为“载体高度大”，
也把下一步的跨状态桥明确成一个可检验的映射命题。

在一侧切片回执 \((p,R,K)=(193,63,3040)\) 中，所选原始角色的商阶为
\(d_5=6\)、\(b_5=1\)，因而

\[
\mathsf D_{\rm ord}=\min\{1,(1/6)^2\}=\frac1{36}.
\]

该数值与相位债务同为 \([1,36]\)，但 `carrier_mapping_status` 仍为
`unproved`，不承担任何跨状态容量结论。现在可以把这一步精确分成 q-primary
phase-lift 三分：有独立标签映射才进入相位树容量，局部无标签或联合 Hall 缺口则保留
对应阻碍回执，详见
[Fourier q-primary 相位到算术载体的有限提升—容量二分](type-I-fourier-qprimary-phase-lift-capacity-dichotomy.md)。

## 研究作用与边界

这条定理把“固定层必须恰好是子群”的特殊假设改成稳定子约化。约化后的
\(\pi(J)\) 是无周期缺陷因子，可直接作为 Kneser、Kemperman 或 Pollard 型论证的第一层。
但它只降低有限群表示的周期，不降低 $p$、$R$、缺口或任何算术势函数；因此输出仍是
**商群压缩**，不是算术下降，也不单独给出全称选择器。
