---
kind: claim
claim_id: type-I-linear-multi-active-fourier-carrier-vector
title: 线性多活跃 G/F 角色的载体向量提取
statement: 对任意线性状态及其有限阶规范内部角色（F 型角色或 H 内部非平凡商角色），角色的非平凡素因子支撑可从两块 U=sR+1、V=aR+1 的精确素指数中提取为带颜色的载体向量。每个活跃素数都有一个高度至少为 ceil((v_q(K)+2*1_{q=2})/2) 的高载体块；同一核心素数的不同坐标块之间，这些高度的最低幂严格整除标签差或同标签模数差，因此可按素数和块颜色输入单方向或带颜色的 q 进容量定理。外部 G 型分离角色在 H 上恒等、支撑为空，不属于本卡；本卡也不保证不同状态选择同一素数/颜色或同一联合高度，不产生全局容量矛盾。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- linear-source
- f-state
- g-state
- finite-fourier
- relation-lattice
- multi-active
- q-adic
- capacity
- cross-state
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-linear-normal-form-context
visibility: public
last_checked: '2026-07-30'
---

# 线性多活跃 G/F 角色的载体向量提取

## 线性块与规范角色

固定核心素数 \(p\equiv1\pmod {24}\) 的线性状态

\[
p=a+s+asR,
\qquad s\ \mathrm{odd},
\qquad R\equiv3\pmod4,
\]

并令

\[
K=\frac{pR+1}{4},
\qquad U=sR+1,
\qquad V=aR+1,
\qquad UV=4K.
\]

写

\[
H=\mathcal H_R(K),
\qquad
\Lambda=\ker\!\left(\phi:\mathbb Z^r\to H\right),
\qquad
\phi(z)=\prod_{i=1}^r q_i^{z_i},
\]

其中 \(q_1<\cdots<q_r\) 是 \(K\) 的不同素因子。规范内部角色由有限相位向量

\[
\theta_i=\frac{a_i}{m}\pmod1
\]

编码，满足 \(La\equiv0\pmod m\)（\(L\) 是关系格基矩阵）。定义活跃支撑

\[
\mathcal I(\theta)=\{q_i:a_i\not\equiv0\pmod m\}
=\{q_i:\chi(q_i)\ne1\}.
\]

若内部角色非平凡，则 \(\mathcal I(\theta)\ne\varnothing\)。F 型目标缺失角色和
\(H\) 内部的非平凡商角色都属于这一有限可验证编码；外部 G 型分离角色限制到 \(H\)
后恒等，\(\mathcal I(\theta)=\varnothing\)，因此由支撑/角色证书分支处理，不送入本卡。
本卡只处理已选内部角色的载体提取，不重新选择角色。

## 载体向量

对每个线性块 \(B(t,R)=tR+1\)，定义其相对于 \(K\) 的载体向量

\[
\boldsymbol\beta(t,R)
=\bigl(v_q(B(t,R))\bigr)_{q\mid K}.
\tag{1}
\]

因为 \(B(t,R)\in\{U,V\}\) 且 \(UV=4K\)，每个坐标满足

\[
v_q(U)+v_q(V)=
\begin{cases}
v_q(K),&q\ne2,\\
v_2(K)+2,&q=2\mid K.
\end{cases}
\tag{2}
\]

若 \(q\in\mathcal I(\theta)\)，则 \(q\mid K\)，从而 (2) 保证

\[
\max\{v_q(U),v_q(V)\}
\ge
\left\lceil\frac{v_q(K)+2\mathbf 1_{q=2}}2\right\rceil.
\tag{3}
\]

因此可以定义高度优先的规范载体：在 \(sR+1\)、\(aR+1\) 中选择
\(v_q(tR+1)\) 较大的块，平手时取 \(s\prec a\)。该载体对每个活跃 \(q\) 都有显式
正高度下界。把块的标签 \(t\)
作为颜色；同一标签的不同模数 \(R\) 形成同色纤维。一个规范多活跃载体证书可写为

\[
\mathsf{MC}(\theta)=
\left(
m,(a_1,\ldots,a_r),
\{(q,\mathrm{color}(t),v_q(tR+1)):
q\in\mathcal I(\theta),\ v_q(tR+1)>0\}
\right),
\tag{4}
\]

并按角色阶、相位分子、素数和块标签的字典序规范化。验证器只需检查角色的关系格同余、
块因数分解和 (1)--(3)。高度优先规则不保证不同状态选出相同颜色；颜色分裂必须交给
带颜色容量或双颜色交集主张。

## 角色—块的精确相位载荷

令

\[
\widetilde B(t,R)=\frac{B(t,R)}{2^{v_2(B(t,R))}},
\]

则 \(\widetilde B(t,R)\mid K\)，因而它的角色值完全由载体向量给出：

\[
\chi\!\left(\widetilde B(t,R)\right)
=
\exp\!\left(
2\pi i\sum_{q\mid K}
v_q\!\left(\widetilde B(t,R)\right)\,\theta_q
\right).
\tag{5}
\]

这是一条精确可验证的“角色—块”接口，不要求 \(2\in H\)。若 \(2\in H\)，还可以把
\(2\)-进块指数加入相位方程；若 \(2\notin H\)，则使用奇部 \(\widetilde B\) 已经避免了
非法地评价角色在 \(2\) 上的值。

因此，规范 Fourier/格角色不再只是一个抽象相位向量：它同时带有一组实际整数块和
其全部 \(q\)-进载荷。注意 (5) 是相位一致性条件，不把相位分母误读成
\(v_q(B)\)；二者是不同的证书字段。

## 跨状态整除链

固定同一核心素数 \(p\)，取两个去重后的不同坐标块
\((t_i,R_i)\)、\((t_j,R_j)\)，并令

\[
h_i(q)=v_q(t_iR_i+1),
\qquad
h_j(q)=v_q(t_jR_j+1).
\]

若 \(h_i(q),h_j(q)>0\)，则

\[
q^{\min(h_i(q),h_j(q))}
\mid
\gcd(t_iR_i+1,t_jR_j+1).
\tag{6}
\]

线性块的标签—模数刚性进一步给出

\[
q^{\min(h_i(q),h_j(q))}
\mid
\begin{cases}
|t_i-t_j|,&t_i\ne t_j,\\
|R_i-R_j|,&t_i=t_j.
\end{cases}
\tag{7}
\]

所以载体证书具有天然的颜色分流：

- 不同标签的同一 \(q\) 进入标签差容量；
- 相同标签的同一 \(q\) 进入模数差容量；
- 若同一状态的多个 \(q\) 同时被记录，则只有在它们落入同一坐标差时，才能调用
  多活跃向量容量；跨不同颜色未经证明不能把容量相乘。

式 (6)--(7) 只依赖完整线性源谱的块刚性，不依赖角色阶、角色幅度或单活跃假设。

## 规范载体选择的全局容量不等式

现在把载体映射固定为一个可计算的规范规则。令 \(\mathcal S\) 是同一核心素数的去重
线性状态集合（同一 \(R\) 只保留一个状态，不同状态取不同 \(R\)），并为每个纳入本卡的状态选其规范内部角色。对每个状态：

1. 取活跃支撑中的最小素数 \(q_s\)；
2. 按固定的块顺序 \(s\prec a\)，在 \(U=sR+1\)、\(V=aR+1\) 中取第一个满足
   \(v_{q_s}(tR+1)>0\) 的块标签 \(t_s\)；
3. 令 \(x_s=(t_s,R_s)\)，并写 \(h_s=v_{q_s}(t_sR_s+1)\ge1\)。

由于不同状态的 \(R_s\) 已去重，\((q_s,x_s)\) 在状态之间不重复。按选出的素数分组，
令

\[
\mathcal X_q=\{x_s:q_s=q\},
\qquad
B_x:=B(t,R)=tR+1\quad(x=(t,R)),
\qquad
H_q=\max_{x\in\mathcal X_q}v_q(B_x),
\]

空组的 \(H_q\) 约定为 \(0\)。对非空组取

\[
M_t(q)=\max_{(t,R)\in\mathcal X_q}t-\min_{(t,R)\in\mathcal X_q}t,
\qquad
M_R(q)=\max_{(t,R)\in\mathcal X_q}R-\min_{(t,R)\in\mathcal X_q}R.
\]

线性载体块的混合容量定理逐组给出

\[
|\mathcal X_q|
\le
\sum_{x\in\mathcal X_q}v_q(B_x)
\le
\frac{M_t(q)M_R(q)}{q^2-1}
+\frac{M_t(q)+M_R(q)}{q-1}
+H_q.
\tag{8}
\]

因而，若同一核心素数的所有 \(|\mathcal S|\) 个纳入状态均携带这种内部角色，则必须满足可执行的全局
容量不等式

\[
\boxed{
|\mathcal S|
\le
\sum_{q\in\mathcal Q_*}
\left(
\frac{M_t(q)M_R(q)}{q^2-1}
+\frac{M_t(q)+M_R(q)}{q-1}
+H_q
\right),
}
\tag{9}
\]

其中 \(\mathcal Q_*=\{q_s:s\in\mathcal S\}\)。如果完整状态数据违反 (9)，则至少一个状态
不能同时保持当前内部证书类型；它必须进入目标命中、偶终端或其它已定义出口。

不等式 (9) 是有限全局排除检验，不是无条件的普适容量常数：右端的素数分组和坐标
宽度依赖被审计的完整状态集合，且当前数据上右端可能远大于左端。它的价值在于把
“是否存在统一容量矛盾”变成一个不需要重新枚举平方除子、只需验证角色支撑和载体块的
明确判据。

## 对统一选择器的实际进展

对每个携带内部角色的状态，现有规范角色证书现在可以扩充为

\[
\mathsf{dual}
\longmapsto
\mathsf{MC}(\theta)
\longmapsto
\{\text{素数 }q,\text{块颜色},\text{正高度}\}.
\]

这解决了跨状态容量接口中的第一项缺口：证书确实能产生可验证的正载体高度。对同一
\((q,\mathrm{color})\) 分组后，可直接应用[跨状态嵌套 q 进证书的容量上界](type-I-cross-state-q-adic-capacity-bound.md)
及[线性载体块的标签—模数混合 q 进容量](type-I-linear-hybrid-label-modulus-q-adic-capacity.md)。

剩余缺口被精确化为三项：

1. 规范角色的活跃支撑可能分散到多个 \(q\)，不同状态的规范选择也可能使用不同 \(q\)；
2. 高度优先载体的颜色可能在“不同标签”和“同标签模数”之间切换，必须按颜色分组
   或建立联合容量；
3. Fourier 近角色预算不决定哪个 \(q\) 或哪个颜色在跨状态中重复，因此尚不能由
   单纯数量统计推出容量超载。

因此，本卡把“对偶证书到载体映射”从开放定义推进为已证明的有限数据结构和整除链，
但没有把条件性容量界误写成跨状态全称选择器。
