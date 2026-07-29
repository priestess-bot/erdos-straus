---
kind: claim
claim_id: type-I-linear-single-active-prime-power-collision-3mod8
title: 3 模 8 线性 F 型单一活跃素因子的幂级碰撞约束
statement: 设 p=1 mod24，线性状态的 R=3 mod8，且 F 型商 H_R(K)/T 为 C_{2m}；除一个奇素数 q 外的所有奇素因子落在 T 中，qT 生成商群。令 e=v_q(K)。若 a 为偶数，则 q^e 全部落在源块 sR+1；若 a 为奇数，则 e 必为偶数且 q^(e/2) 同时整除两个块。因而同一 q 在两个此类状态中重复时，按各块承担的指数，q 的相应幂必须整除标签差或模数差。这是跨状态 F 缺口的幂级必要条件，不是全称选择器。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- linear-source
- f-obstruction
- cyclic-quotient
- active-prime
- odd-k
- 3-mod-8
- power-collision
- label-collision
- cross-modulus
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-linear-normal-form-context
visibility: public
last_checked: '2026-07-29'
---

# \(3\bmod8\) 线性 F 型单一活跃素因子的幂级碰撞约束

## 设置

固定核心素数 \(p\equiv1\pmod {24}\)，取线性源状态

$$
p=a+s+asR,\qquad s\equiv1\pmod2,\qquad R\equiv3\pmod8,
$$

并令

$$
K=\frac{pR+1}{4},\qquad
U=sR+1,\qquad V=aR+1,\qquad UV=4K. \tag{1}
$$

因为 \(p\equiv1\pmod8\)、\(R\equiv3\pmod8\)，有

$$
K\equiv1\pmod2. \tag{2}
$$

设

$$
-1\in\mathcal H_R(K)\setminus\mathcal C_R(K),\qquad
\mathcal H_R(K)/T\cong C_{2m},\qquad
T=\operatorname{Stab}_{\mathcal H_R(K)}(\mathcal A_R(K)), \tag{3}
$$

并假设除一个奇素数 \(q\mid K\) 外的所有奇素数在 \(T\) 中，\(qT\) 生成商群。记

$$
e=v_q(K). \tag{4}
$$

F 型商的反足点不相交性给出

$$
e<m. \tag{5}
$$

## 单状态的幂级分配

对源块和仿射块分别记

$$
U=sR+1,\qquad V=aR+1.
$$

则有以下精确分叉：

$$
\boxed{
\begin{array}{c|c|c}
\text{条件}&q\text{ 在 }U,V\text{ 中的指数}&\text{结论}\\ \hline
a\text{ 偶}&v_q(U)=e,\quad v_q(V)=0&q^e\mid U\\
a\text{ 奇}&v_q(U)=v_q(V)=e/2&e\text{ 为偶数}
\end{array}} \tag{6}
$$

在第二行，\(q^{e/2}\) 同时整除 \(U\) 与 \(V\)。

## 跨状态幂级碰撞

取同一核心素数的两个不同状态 \(i,j\)，均满足上面的 \(3\bmod8\) 一奇素数模型，且
\(q_i=q_j=q\)。定义块承担指数

$$
\rho_i(t)=
\begin{cases}
e_i,&t=s_i,\ a_i\text{ 偶},\\
e_i/2,&t\in\{s_i,a_i\},\ a_i\text{ 奇}.
\end{cases} \tag{7}
$$

未列出的块承担指数为 \(0\)。则任意两个坐标块满足

$$
q^{\min(\rho_i(t),\rho_j(u))}
\mid\gcd(tR_i+1,uR_j+1). \tag{8}
$$

因此

$$
q^{\min(\rho_i(t),\rho_j(u))}
\mid
\begin{cases}
|t-u|,&t\ne u,\\
|R_i-R_j|,&t=u,
\end{cases} \tag{9}
$$

同时跨模数恒等式给出更强的总指数约束

$$
q^{\min(e_i,e_j)}
\mid\frac{|R_i-R_j|}{4}. \tag{10}
$$

所以一个重复的活跃 q 若指数较大，就必须在完整源谱的标签差或模数差中留下同样大的
\(q\)-进预算；它不能作为两个状态之间的“无结构共享因子”。

## 证明

先证 (2)。有

$$
pR+1\equiv1\cdot3+1\equiv4\pmod8,
$$

故 \(4K=pR+1\) 恰好给出 \(K\) 为奇数。

若 \(a\) 偶，则 \(V=aR+1\) 为奇数。由 \(UV=4K\) 与 \(K\) 奇，得到
\(v_2(U)=2\)。令 \(U_{\mathrm o}=U/4\)，则 \(U_{\mathrm o}\mid K\)。
在商群中 \(K\) 的残数为 \(q^eT\)，而 \(4K\equiv1\pmod R\)，所以

$$
4T=(qT)^{-e}. \tag{11}
$$

另一方面 \(U\equiv1\pmod R\) 给出
\(U_{\mathrm o}\equiv4^{-1}\pmod R\)，故
\(U_{\mathrm o}T=(qT)^e\)。但 \(U_{\mathrm o}\) 的唯一非平凡商群贡献是
\(q^{v_q(U)}\)，从而 \(v_q(U)\equiv e\pmod{2m}\)。由
\(0\le v_q(U)\le e<m\)，得到 \(v_q(U)=e\)，并由 \(UV=4K\) 得
\(v_q(V)=0\)。

若 \(a\) 奇，则 \(U,V\) 都为偶数。由于 \(K\) 奇且 \(UV=4K\)，必有
\(v_2(U)=v_2(V)=1\)。于是 \(U/2,V/2\mid K\)，且
\(2\in\mathcal H_R(K)\)。写 \(2T=(qT)^\alpha\)，令
\(r=v_q(U)\)。块同余分别给出

$$
r+\alpha\equiv0\pmod{2m},\qquad
(e-r)+\alpha\equiv0\pmod{2m}. \tag{12}
$$

相减得 \(e-2r\equiv0\pmod{2m}\)。由
\(|e-2r|\le e<m\)，得到 \(e=2r\)，证明第二行。

最后，(6) 保证相应的 q 幂分别整除坐标块。不同标签的块公因子整除标签差，
相同标签的块公因子整除模数差，得到 (8)--(9)；(10) 是
\(\gcd(K_i,K_j)=\gcd(K_i,|R_i-R_j|/4)\) 的 \(q\)-进形式。证毕。

## 对原选择器的作用

这条定理把 \(3\bmod8\) 的一奇素因子 F 残余压缩为两个可追踪的方向：

- \(a\) 偶时，全部指数只能沿源块 \(sR+1\) 走；
- \(a\) 奇时，指数必须平分到两个块，因而 \(e\) 必为偶数。

跨状态时，幂级碰撞 (9) 与总模数预算 (10) 必须同时成立。若完整源谱中不存在承载这些
\(q\)-进幂的标签/模数差，则该重复活跃方向被排除；若存在，则其位置已经被明确标记，
可与二进最近剩余缺口、标签层 Kneser 判据联合。

本卡仍不处理多个奇活跃素因子、非 \(3\bmod8\) 模数或高阶角色，也不证明原混合终端
选择引理；它提供的是一个比单素因子相容性更强的跨状态必要条件。
