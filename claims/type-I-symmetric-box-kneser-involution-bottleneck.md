---
kind: claim
claim_id: type-I-symmetric-box-kneser-involution-bottleneck
title: 中心化指数盒的 Kneser 对合瓶颈
statement: 对有限阿贝尔群 H 中的非空基集 A_0（应用于目标纤维时可取对称）和中心化幂块 B_i={g_i^z:-e_i<=z<=e_i}，令 P=A_0 B_1...B_r、T=Stab_H(P)，并令 o_i 为 g_iT 在 H/T 中的阶。则 |P|>=|A_0T|+|T| sum_i lambda_i，其中 lambda_i=min(2e_i,o_i-1)。若目标 t 不在 P，则 sum_i lambda_i<=floor((|H|-1-|A_0T|)/|T|)。因此被稳定子吸收的方向收费 0，非平凡二阶方向收费 1，阶至少 3 的活跃方向收费至少 2；在 Type I 中心化私有盒的无周期商上，F 型未命中只能保留有限的二阶/吸收方向预算。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-private-quotient-box-saturation
  - type-I-linear-single-active-cross-state-exit-trichotomy
topics:
- type-I
- F-state
- symmetric-box
- Kneser
- stabilizer-quotient
- involution
- dyadic
- capacity
- proof-program
sources:
  - claim: type-I-private-quotient-box-saturation
    role: central-symmetric-box-input
visibility: public
last_checked: '2026-08-04'
---

# 中心化指数盒的 Kneser 对合瓶颈

## 有限群引理

令 \(H\) 为有限阿贝尔群，\(A_0\subset H\) 为非空集合，且令

\[
B_i=\{g_i^z:-e_i\le z\le e_i\},\qquad e_i\ge0.
\]

置

\[
P=A_0B_1\cdots B_r,\qquad T=\operatorname{Stab}_H(P).
\]

把 \(\bar g_i=g_iT\) 视为商群 \(H/T\) 中的元素，记其阶为
\(o_i=\operatorname{ord}(\bar g_i)\)。定义

\[
\lambda_i
  =|B_iT/T|-1
  =\min(2e_i+1,o_i)-1
  =\min(2e_i,o_i-1).
\tag{1}
\]

则

\[
\boxed{
|P|\ge |A_0T|+|T|\sum_{i=1}^r\lambda_i.
}
\tag{2}
\]

若目标 \(t\in H\) 不属于 \(P\)，则

\[
\boxed{
\sum_{i=1}^r\lambda_i
\le
\left\lfloor
\frac{|H|-1-|A_0T|}{|T|}
\right\rfloor.
}
\tag{3}
\]

因此

\[
\begin{array}{c|c|c}
\text{商群中方向} & o_i & \lambda_i\quad(e_i\ge1)\\ \hline
\text{被稳定子吸收} & 1 & 0\\
\text{非平凡对合方向} & 2 & 1\\
\text{非对合方向} & o_i\ge3 & \lambda_i\ge2
\end{array}
\tag{4}
\]

更精确地，非对合方向的收费是
\(\min(2e_i,o_i-1)\)，所以当指数盒变宽时，收费会继续增长直到绕满
\(\langle\bar g_i\rangle\)。

### 证明

在商群 \(H/T\) 中，

\[
B_iT/T=\{\bar g_i^z:-e_i\le z\le e_i\}.
\]

这是一个循环子群中的连续指数段，因而恰有
\(\min(2e_i+1,o_i)\) 个元素，得到 (1)。
对 \(A_0,B_1,\ldots,B_r\) 应用多集合 Kneser 不等式，并取最终积集的稳定子
\(T\)，得到

\[
\begin{aligned}
|P|
&\ge |A_0T|+\sum_i|B_iT|-r|T|\\
&=|A_0T|+|T|\sum_i\bigl(|B_iT/T|-1\bigr),
\end{aligned}
\]

即 (2)。若 \(t\notin P\)，则 \(|P|\le |H|-1\)，代入 (2) 即得 (3)。
最后，\(o_i=1\) 时 \(\lambda_i=0\)；\(o_i=2\) 且 \(e_i\ge1\) 时
\(\lambda_i=1\)；\(o_i\ge3\) 且 \(e_i\ge1\) 时
\(\lambda_i\ge2\)。证毕。

## Type I 中心化盒的直接形式

沿用[Type I 多私有因子商群指数盒的饱和判据](type-I-private-quotient-box-saturation.md)
的中心化设置。设 \(J\) 是固定层子群，\(Q=H/J\)，并写

\[
S_i^\pm=\{(q_iJ)^z:-b_i\le z\le b_i\},
\qquad
B^\pm=S_1^\pm\cdots S_k^\pm.
\]

令 \(T=\operatorname{Stab}_Q(B^\pm)\)，并令
\(o_i=\operatorname{ord}(q_iJT)\) 是 \(q_iJ\) 在 \(Q/T\) 中的阶。把 \(A_0=\{1\}\)
代入 (3)，若目标 \(-1\) 的商类不在 \(B^\pm\)，则

\[
\boxed{
\sum_{i=1}^k\min(2b_i,o_i-1)
\le |Q/T|-2.
}
\tag{5}
\]

这里使用了 \(|A_0T|=|T|\) 和
\[
\left\lfloor\frac{|Q|-1-|T|}{|T|}\right\rfloor=|Q/T|-2.
\]

所以 Type I F 型中心化盒未命中时，任何不被 \(T\) 吸收且在商群中阶至少
3 的私有素因子方向都要消耗至少两个单位；只有商群对合方向可以只消耗一个单位。
若 \(Q/T\) 为奇数阶，则不存在非平凡对合，因而

\[
\boxed{
2\,\#\{i:q_iJT\ne T,\ o_i\ge3\}
\le |Q/T|-2.
}
\tag{6}
\]

还有一个纯 dyadic 的闭合。若所有未被 \(T\) 吸收的方向都满足
\(o_i\le2\)，且每个非吸收方向有 \(b_i\ge1\)，则

\[
\boxed{
B^\pm/T=\left\langle q_iJT:q_iJT\ne T\right\rangle=Q/T.
}
\tag{7}
\]

这里最后一个等号使用 \(Q=\langle q_iJ\rangle\)。所以在
\(-1\in H\) 的 Type I 状态中，纯 dyadic 分支必命中
\(-1\in\mathcal C_R(K)\)；若目标不在总支撑群 \(H\)，则它是 G 型支撑逃逸，而不是
一个新的 F 型容量缺口。换言之，真正的 F 型未命中且 \(-1\in H\) 时，至少存在一个
商阶 \(o_i\ge3\) 的非对合方向，且该方向至少贡献两个 \(\lambda\)-单位。

### (7) 的证明

当 \(o_i=1\) 时，块在商群中是 \(\{1\}\)；当 \(o_i=2\) 且 \(b_i\ge1\) 时，
\[
\{(q_iJ)^z:-b_i\le z\le b_i\}=\{1,q_iJ\}.
\]
这些二元块的乘积恰是它们生成的初等二群。所有非吸收方向的像生成 \(Q/T\)，故
得到 (7)。因为 \(T\subset B^\pm\)，目标的商类属于 \(B^\pm/T\) 当且仅当目标属于
\(B^\pm\)，从而得到上述命中/支撑逃逸二分。

这个结论比逐块只记“至少增长一个 \(T\)-块”的预算严格一倍，并把未命中分支
明确压缩为：

1. 方向被 \(T\) 吸收，必须转入更小稳定子商；
2. 方向在 \(Q/T\) 中是二阶元，进入广义 \(2^j\)/dyadic 分支；
3. 其余非对合方向的总指数预算不超过 (5)。

若 (5) 的反向严格不等式成立，则 \(B^\pm=Q\)，从而目标商类被命中；在线性
Type I 状态中再结合已有偶因子提升即可得到混合终端。这里的“反向”只指有限盒
饱和充分条件，不把该命中自动升级为跨状态递降。

## 与单活跃退出和 Type II 容量的接线

单活跃循环商退出后，新的多活跃状态通常给出中心化指数盒而不是单向幂段。
式 (5) 提供一个不依赖角色选择的第一层分流：如果非对合方向的真实指数预算已经
超过 \(|Q/T|-2\)，则目标必在盒内；否则剩余方向只能是稳定子吸收或二阶商方向。
前者与稳定子商递降相容，后者正好是广义 \(2^j\) 字符/对称距离问题。

这也解释了 Type II 规范扇中高阶二幂深度的作用：二阶商方向不应继续按普通
奇素数容量重复计费，而应单独记录其二幂深度；非对合方向则可使用 (5) 的至少
二单位容量。该接线仍是状态级结构定理，尚未给出从 Type II 移位 q 进高度到
\(\lambda_i\) 的算术单射。

## 逻辑边界

本卡只证明有限群乘积集的精确容量与对合分层。它不证明：

1. 每个盒外 Fourier/Pareto 需求都对应一个不同的 \(q_i\) 方向；
2. Type II 移位的共同素因子幂自动产生 \(Q/T\) 中的非对合方向；
3. 稳定子商递降一定能提升为更小的核心素数实例；
4. 二阶方向一定给出 Type I/II 短证书。

因此它把当前第三分支进一步压缩为两个明确问题：证明真实算术载体能注入
\(\lambda_i\) 预算，或在二阶/吸收分支建立可提升的良基下降。没有这两个输入，
(5) 仍是精确的容量必要条件而非猜想的全称证明。
