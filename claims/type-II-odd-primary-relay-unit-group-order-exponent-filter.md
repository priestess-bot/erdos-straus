---
kind: claim
claim_id: type-II-odd-primary-relay-unit-group-order-exponent-filter
title: 奇主压缩 relay 的单位群阶—指数必要过滤器
statement: 设奇主压缩得到 O=pi^(-1)((H/<R>)_(2))，并考虑严格较小模数 D' 上保持目标与来源标签的满射 eta:U(4D')->O。则 |O|=|H|/|(H/<R>)_(odd)| 必须整除 phi(4D')，且 exp(O) 必须整除 Carmichael 指数 lambda(4D')；每个固定来源像 u_i 的阶还必须整除 lambda(4D')。任一条件失败都给出无需完整 SNF 的 G1 阶/指数负证书；条件全部通过仍不保证满射，必须继续执行联合目标同余与 SNF。对所有 D'|D 的前筛为空时，得到该奇主 relay 沿低模数 Type II source-switch 的有限完备负证书。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-odd-primary-annihilator-compression-two-primary-terminal
  - type-II-annihilator-unit-group-target-map-snf-criterion
  - type-II-annihilator-congruence-fiber-lift-criterion
topics:
- type-II
- odd-primary
- arithmetic-lift
- unit-group
- group-order
- exponent
- Carmichael
- SNF
- source-switch
- obstruction
- proof-program
sources:
  - claim: type-II-odd-primary-annihilator-compression-two-primary-terminal
    role: compressed-relay-group
  - claim: type-II-annihilator-unit-group-target-map-snf-criterion
    role: full-surjection-SNF
  - claim: type-II-annihilator-congruence-fiber-lift-criterion
    role: finite-source-switch-menu
visibility: public
last_checked: '2026-08-05'
---

# 奇主压缩 relay 的单位群阶—指数必要过滤器

## 1. 输入与候选回译

沿用奇主压缩设置。令 \(H\) 是有限阿贝尔群，\(R\subseteq H\) 含单位元，
\(L=\langle R\rangle\)，并令

\[
Q=H/L=Q_{(2)}\times Q_{\mathrm{odd}},
\qquad
O=\pi^{-1}(Q_{(2)}).
\tag{1}
\]

于是

\[
|O|=\frac{|H|}{|Q_{\mathrm{odd}}|},
\qquad
O/L\simeq Q_{(2)}.
\tag{2}
\]

假设 \(O\) 已作为一个 Type II relay 的目标群嵌入原始单位群，并尝试在
\(D'\mid D\)、\(D'<D\) 的较小模数上构造保持目标和来源标签的同态

\[
\eta:U(4D')\twoheadrightarrow O,
\qquad
\eta(-1)=-1_O.
\tag{3}
\]

这里还要同时满足既有的 \(A\mid D'\)、\(D'/A\) 平方自由、
\(4AD'<p\)、来源 CRT 和 \(B'>A\) 条件；本引理只提取 (3) 必须满足的群论不变量。

记

\[
\Lambda_{D'}=\lambda(4D')
\]

为 \(U(4D')\) 的 Carmichael 指数，记 \(\exp(O)\) 为 \(O\) 的群指数。

## 2. 阶—指数必要定理

**定理。** 若 (3) 存在，则必有

\[
\boxed{|O|\mid\varphi(4D')}
\tag{4}
\]

以及

\[
\boxed{\exp(O)\mid\Lambda_{D'}.}
\tag{5}
\]

若固定来源因子 \(h_i\) 在低模数中满足 \((h_i,4D')=1\)，并记

\[
u_i=\eta(h_i\bmod 4D'),
\]

则进一步有

\[
\boxed{\operatorname{ord}(u_i)\mid\Lambda_{D'}.}
\tag{6}
\]

因此可定义三个互斥的最小失败回执：

\[
\begin{array}{ll}
\mathrm{G1\_ORDER\_OBSTRUCTED}:&
|O|\nmid\varphi(4D');\\
\mathrm{G1\_EXPONENT\_OBSTRUCTED}:&
|O|\mid\varphi(4D')\text{ 但 }\exp(O)\nmid\Lambda_{D'};\\
\mathrm{G2\_SOURCE\_ORDER\_OBSTRUCTED}:&
\text{某个固定来源像 }u_i\text{ 的阶不整除 }\Lambda_{D'}.
\end{array}
\tag{7}
\]

当 (4)--(6) 全部通过时，只能记为
\(\mathrm{G1\_INVARIANT\_PREFILTER\_PASSED}\)，不能据此声称
\(\eta\) 存在；仍需运行联合目标同余和满射 SNF。

### 证明

有限群满射的阶由拉格朗日定理给出
\[
|O|=|U(4D')|/|\ker\eta|,
\]
而 \(|U(4D')|=\varphi(4D')\)，故 (4) 成立。

任取 \(x\in U(4D')\)。由 Carmichael 定理
\(x^{\Lambda_{D'}}=1\)。应用同态 \(\eta\) 得
\[
\eta(x)^{\Lambda_{D'}}=1.
\]
所以 \(O=\eta(U(4D'))\) 的每个元素阶都整除 \(\Lambda_{D'}\)，即
\(\exp(O)\mid\Lambda_{D'}\)，得到 (5)。对固定来源像 \(u_i=\eta(h_i)\) 直接得到
(6)。证毕。

## 3. 有限低模数前筛的完备负证书

固定原始 \(D\)，定义奇主 relay 的不变量候选集

\[
\mathscr D_{\mathrm{inv}}(O;D)
=
\left\{
D'\mid D:
D'<D,\quad
|O|\mid\varphi(4D'),\quad
\exp(O)\mid\lambda(4D')
\right\}.
\tag{8}
\]

若还固定来源像阶 \(d_i=\operatorname{ord}(u_i)\)，定义加强候选集

\[
\mathscr D_{\mathrm{src}}(O;D,\mathbf d)
=
\left\{
D'\in\mathscr D_{\mathrm{inv}}:
d_i\mid\lambda(4D')\ \text{对所有 }i
\right\}.
\tag{9}
\]

于是有精确的有限分派：

\[
\boxed{
\mathscr D_{\mathrm{src}}(O;D,\mathbf d)=\varnothing
\Longrightarrow
\text{不存在任何满足 (3) 的低模数 source-switch 满射}.}
\tag{10}
\]

证明是逐候选应用 (4)--(6) 的逆否命题；\(D\) 的正因子集有限，所以
(10) 是一个有限、完备且不依赖枚举顺序的 G1/G2 负证书。其规范载荷可以取

\[
\mathsf{OF}_{\mathrm{odd}}=
\bigl(
|O|,\exp(O),D,
\{(D',\mathrm{failed\_factor}) : D'\mid D,\ D'<D\}
\bigr),
\tag{11}
\]

其中 failed_factor 是
\(|O|\) 在 \(\varphi(4D')\) 中的缺失因子、\(\exp(O)\) 在
\(\lambda(4D')\) 中的缺失因子，或某个 \(d_i\) 的缺失因子。

这个负证书只排除“该 relay 的低模数满射回译”；它不排除原模数直接 Type II、
另一来源子列表、Type I 或其它严格下降。

## 4. 与完整 SNF 菜单的严格关系

把 (8)--(9) 接入现有的
[单位群—目标带像满射 SNF 判据](type-II-annihilator-unit-group-target-map-snf-criterion.md)
和[带来源同余纤维提升菜单](type-II-annihilator-congruence-fiber-lift-criterion.md)：

1. 先对每个 \(D'\mid D\) 做阶、指数和来源像阶前筛；
2. 只有 \(D'\in\mathscr D_{\mathrm{src}}\) 才枚举 \(A\)、统一来源 CRT 和目标映射
   \(Y\)；
3. 对通过前筛的 \(Y\) 执行联合目标同余 SNF，再执行满射商 SNF；
4. 若 \(Y\) 通过，继续检查 \(A\mid D'\)、平方自由、范围、\(B'>A\) 和直接
   Type II 子列表命中。

因此前筛与 SNF 的逻辑关系是

\[
\boxed{
\text{满射 SNF 通过}
\Longrightarrow
\text{阶/指数前筛通过},
}
\tag{12}
\]

但反向蕴含一般不成立。前筛把 G1/G2 的失败分成廉价不变量障碍，
SNF 才负责处理 invariant-factor、目标 \(-1\) 像和多来源联合相容性。

## 5. 构造性边界例子

### 阶障碍：\(U(28)\) 的奇主压缩不能降到 \(U(4)\)

取 \(H=U(28)\)，\(R=\{1\}\)，\(L=\{1\}\)。有
\[
|H|=\varphi(28)=12,
\qquad
H\simeq C_6\times C_2.
\]

其 2-Sylow 原像为
\[
O=\{1,13,15,27\},
\qquad
|O|=4,
\qquad
Q_{\mathrm{odd}}\simeq C_3,
\]
并且目标 \(-1=27\in O\)。若尝试 \(D'=1\)，则
\[
|U(4)|=\varphi(4)=2,
\]
所以 \(|O|=4\nmid2\)。无论来源标签如何选择，都不存在
\(U(4)\twoheadrightarrow O\)；这是 G1_ORDER_OBSTRUCTED，不需要枚举 SNF 矩阵。

### 指数障碍的独立边界

抽象 relay \(J=C_4\) 与候选源群 \(U(8)\simeq C_2\times C_2\) 都有阶 4，
但
\[
\exp(J)=4,\qquad \lambda(8)=2.
\]
所以不存在 \(U(8)\twoheadrightarrow C_4\)，尽管阶整除条件通过；这给出
G1_EXPONENT_OBSTRUCTED 而非阶障碍。它说明只检查群阶会漏掉
invariant-factor 失败。

## 6. 对统一选择器的作用与边界

奇主压缩后，若 \(\mathscr D_{\mathrm{src}}\) 非空，仍需执行完整 source-switch/SNF；
若为空，则可立即输出有限的
\(\mathrm{ODD\_PRIMARY\_LOWER\_MODULUS\_INVARIANT\_OBSTRUCTION}\)，并把状态转给
Type I/F/G 或其它 Type II 子列表。若某个 \(D'\) 通过前筛和 SNF，且参数纤维、
来源合同和 \(B'>A\) 均通过，则 \(D'<D\) 支付良基势，成为真正的
verified_edge。

该引理没有声称所有奇主 relay 都能降模；它把剩余缺口从抽象“群映射未知”收紧为：

\[
\text{阶/指数前筛通过}
\;\longrightarrow\;
\text{联合 SNF/CRT}
\;\longrightarrow\;
\text{Type II 参数与 E1--E5}.
\]

如果这三层都失败，失败类型已经可区分，不能再通过重复 Fourier 或容量计数掩盖。
