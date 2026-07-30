---
kind: claim
claim_id: type-I-linear-single-active-fourier-carrier-bridge
title: 线性单活跃循环商的 Fourier—载体素数桥接
statement: 在 R=3 mod 8 的线性 F 型状态中，若稳定子商为 C_{2m}，且只有一个奇素数 q 在商中非平凡、qT 生成商群、目标像为 q^mT，则 primitive quotient character 的相位分母为 2m，F 型恰等价于 e=v_q(K)<m。该同一 q 的指数 e 可由线性块 tR+1 提取为正 q 进载荷，并满足跨状态标签差/模数差整除约束；因此这类对偶证书可直接输入线性混合 q 进容量界。该桥接是单活跃分支的严格结果，不覆盖多活跃 F 状态，也不声称一般 Fourier 证书自动选择出 q。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- linear-source
- f-state
- finite-fourier
- relation-lattice
- single-active
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

# 线性单活跃循环商的 Fourier—载体素数桥接

## 设置与范围

固定一个核心素数 \(p\equiv1\pmod {24}\)，取线性源

\[
p=a+s+asR,
\qquad s\ \mathrm{odd},
\qquad R\equiv3\pmod8,
\]

并令

\[
K=\frac{pR+1}{4},
\qquad U=sR+1,
\qquad V=aR+1.
\]

于是

\[
UV=4K,
\qquad U\equiv V\equiv1\pmod R,
\qquad K\ \mathrm{odd}.
\]

写

\[
H=\mathcal H_R(K),
\qquad A=\mathcal A_R(K),
\qquad C=AA^{-1},
\qquad T=\operatorname{Stab}_H(A),
\qquad Q=H/T.
\]

假设状态为 F 型：

\[
-1\in H\setminus C.
\]

本卡只处理以下明确的低复杂度分支：

1. \(Q\cong C_{2m}\)；
2. 存在奇素数 \(q\mid K\)，其像 \(\bar q=qT\) 生成 \(Q\)；
3. 其它素因子 \(r\mid K\) 的像均在 \(T\) 中；
4. 目标像满足 \(\overline{-1}=\bar q^{\,m}\)，即它是 \(Q\) 的非平凡阶二元。

条件 4 排除了目标已经落入固定层的情形；若该条件失败，应转入固定层缺陷或一般多活跃
对偶分支，而不能套用本卡。

## 商群、目标缺口与 primitive Fourier 字符

令

\[
e=v_q(K).
\]

由于 \(T\subseteq A\)，且其它素因子在 \(T\) 中，除子谱在商群中的像精确为

\[
\bar A=\{\bar q^{\,j}:0\le j\le e\},
\qquad
\bar C=\{\bar q^{\,z}:-e\le z\le e\}.
\]

目标 \(\bar q^m\) 属于 \(\bar C\) 当且仅当区间 \([-e,e]\) 含有一个与 \(m\)
模 \(2m\) 同余的整数。因 F 型目标缺失，得到精确等价式

\[
\boxed{
\text{F 型单活跃循环商}
\quad\Longleftrightarrow\quad
e<m.
}
\tag{1}
\]

反过来 \(e\ge m\) 时，指数 \(z=m\) 直接给出目标命中。这是有限盒边界，而不是
仅仅生成子群边界。

选择由 \(\bar q\) 确定的 primitive quotient character

\[
\chi_q(\bar q)=\exp\!\left(\frac{2\pi i}{2m}\right),
\]

并将其从 \(Q\) 拉回 \(H\)。则

\[
\chi_q(-1)=-1,
\qquad
\operatorname{ord}(\chi_q)=2m,
\qquad
\|\theta_q\|=\frac1{2m},
\]

其中 \(\theta_q\) 是活跃坐标的中心化相位。故单活跃分支中存在一个规范的、目标定向
的有限 Fourier/对偶证书

\[
\boxed{
\bigl(Q\cong C_{2m},\ qT\mapsto1/(2m),\ e<m\bigr).
}
\tag{2}
\]

这里的 primitive character 是按已选生成元 \(qT\) 定义的目标定向载荷；它不声称一定
等于一般 Fourier 证书中按最大谱幅度选出的角色。后者可能选择一个不同的奇指数角色，
但仍位于同一有限循环商。这个区别避免把“可规范提取的载体角色”误写成“全局最强角色”。

在关系格语言中，活跃坐标的对偶分量为

\[
y_q=\frac1{2m},
\]

其有限阶分母为 \(2m\)，而 (1) 给出

\[
e<\frac{\operatorname{den}(y_q)}2.
\tag{3}
\]

因此该分支首次实现了“对偶分母—有限指数预算”的精确字典；它仍只适用于已经识别出
单活跃商方向的状态。

## 载体素数的线性块提取

因为 \(R\equiv3\pmod8\)，有 \(K\) 奇且 \(UV=4K\)。令

\[
r=v_q(U),
\qquad e-r=v_q(V).
\]

已有的 \(3\pmod8\) 块分配恒等式给出：

\[
\boxed{
\begin{array}{c|c|c}
\text{条件}&(v_q(U),v_q(V))&\text{载体块}\\ \hline
a\text{ 偶}&(e,0)&sR+1\\
a\text{ 奇}&(e/2,e/2)&sR+1\text{ 与 }aR+1
\end{array}}
\tag{4}
\]

在第二行 \(e\) 必为偶数。定义每个块标签的载荷

\[
\rho(t)=
\begin{cases}
e,&t=s,\\
e/2,&t\in\{s,a\}\text{ 且 }a\text{ 奇},\\
0,&\text{其它块}.
\end{cases}
\tag{5}
\]

则 \(q^{\rho(t)}\mid tR+1\)。这一步把 (2) 中的商群活跃方向变成一个实际整数块上的
正 \(q\)-进高度；其依据是
[3 mod 8 线性 F 型单一活跃素因子的幂级碰撞约束](type-I-linear-single-active-prime-power-collision-3mod8.md)，
不是一般角色相位可以单独推出的结论。

## 跨状态兼容性与容量输入

取同一核心素数的两个单活跃状态 \(i,j\)，且它们提取出同一个活跃素数 \(q\)。对任意
相应载体块标签 \(t_i,t_j\)，已有块刚性给出

\[
q^{\min(\rho_i(t_i),\rho_j(t_j))}
\mid
\gcd(t_iR_i+1,t_jR_j+1).
\tag{6}
\]

于是

\[
q^{\min(\rho_i(t_i),\rho_j(t_j))}
\mid
\begin{cases}
|t_i-t_j|,&t_i\ne t_j,\\
|R_i-R_j|,&t_i=t_j.
\end{cases}
\tag{7}
\]

同时，\(K_i-K_j=p(R_i-R_j)/4\) 给出总指数约束

\[
q^{\min(e_i,e_j)}
\mid\frac{|R_i-R_j|}{4}.
\tag{8}
\]

因此，每个单活跃 F 型对偶证书都可携带一个明确的载荷记录

\[
\mathsf{carrier}(i,q)=
\bigl(q,\ 2m_i,\ e_i,\ \{(t,\rho_i(t))\}\bigr).
\tag{9}
\]

并满足线性载体块的标签—模数混合容量定理的输入条件。特别地，若一组状态的证书
都要求某个指定块族载荷至少为 \(h_0\)，而其坐标块落在宽度

\[
(M_t,M_R),
\]

则该组不能超过

\[
\frac{M_tM_R}{q^2-1}
 +\frac{M_t+M_R}{q-1}+H_{\max}
\tag{10}
\]

的总载荷（其中 \(H_{\max}\) 是该族最大高度）。若状态数乘以 \(h_0\) 超过 (10)，则至少有
一个状态离开该单活跃 F 型分支，进入多活跃、G、hit 或终端分支。

## 证明边界与下一桥梁

式 (1)--(3) 只使用单活跃循环商的有限指数结构和 primitive character；式 (4)--(8)
使用线性源的块分解与已建立的公因子刚性。因此这是一个完整的受限桥接定理，而不是
经验相关性。

它仍不能完成统一选择器，原因有三：

1. 当前四个真实对抗核心的 45 个 F 状态都至少有三个活跃方向，单活跃分支在该数据上
   只是排除性模型；
2. 一般规范 Fourier 角色的分母不自动指定某个载体素数，更不能自动给出正的
   \(q\)-进高度；
3. 多活跃状态需要把多个载荷向量同时拉回共同标签或模数差，现有容量界只在这些
   整除链已验证时适用。

所以本卡完成的是统一目标中的一个严格接口：

\[
\boxed{
\text{单活跃对偶证书}
\Longrightarrow
\text{载体素数/正高度}
\Longrightarrow
\text{跨状态容量约束}.
}
\]

下一步必须处理多活跃对偶证书的载体提取，或证明稀疏多活跃结构能产生严格可提升的
算术下降；不能把本卡外推为所有 F/G 状态的全称结论。
