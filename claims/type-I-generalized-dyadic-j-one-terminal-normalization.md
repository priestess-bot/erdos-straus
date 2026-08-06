---
kind: claim
claim_id: type-I-generalized-dyadic-j-one-terminal-normalization
title: 广义二进偶终端的唯一 j=1 归一化与二进盒外边界
statement: 设 L=2K。每个满足互素除子、二进预算、同余和定向条件的广义 2^j 偶终端 (A,B,j) 都唯一归一为一个满足 j=1 的互素 L-除子对 (A#,B#)，并保留完全相同的终端数据 (E,n)。因此在自由除子对的终端层，j>1 不扩张任何终端集合，只可保留 source-label provenance。相应关系向量恰有一层可能位于目标指数盒的二进负侧外；该层等价于 v_2(E)=1，不能来自目标纤维近邻对。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-general-dyadic-terminal-transfer
  - type-I-target-fiber-neighbor-terminal
  - type-I-target-fiber-neighbor-dyadic-normalization
topics:
  - type-I
  - generalized-dyadic
  - terminal-normalization
  - two-adic
  - target-fiber
  - relation-lattice
  - terminal-first
  - proof-program
sources:
  - claim: type-I-general-dyadic-terminal-transfer
    role: generalized-dyadic-terminal-legality
  - claim: type-I-target-fiber-neighbor-terminal
    role: near-pair-terminal-boundary
  - claim: type-I-target-fiber-neighbor-dyadic-normalization
    role: target-fiber-relation-lens
visibility: public
last_checked: '2026-08-07'
---

# 广义二进偶终端的唯一 \(j=1\) 归一化与二进盒外边界

## 1. 自由除子对的设置

令

\[
4K=pR+1,
\qquad L=2K,
\]

其中 \(R\) 为奇数。考虑一般二进传输的一个合法自由除子对

\[
(A,B)=1,
\qquad A,B\mid L,
\qquad A\equiv2^jB\pmod R,
\tag{1}
\]

其中 \(j\ge1\) 满足精确二进预算和定向条件

\[
1\le j\le v_2(L)+v_2(A)-v_2(B),
\qquad A<2^jB.
\tag{2}
\]

对应的偶终端数据是

\[
E_j=2^{1-j}L\frac AB,
\qquad
n_j=\frac{2L-E_j}{R}.
\tag{3}
\]

这里讨论的是没有额外 source label 的终端层。若 \((A,B,j)\) 还携带一个必须保留的
来源标签，下面的归一化不删除该标签，只说明它不会给出新的 \((E,n)\)。

## 2. \(j=1\) 归一化定理

令既约正分数

\[
\frac{A^\sharp}{B^\sharp}
=2^{1-j}\frac AB,
\qquad (A^\sharp,B^\sharp)=1.
\tag{4}
\]

则有

\[
\boxed{
\begin{gathered}
A^\sharp,B^\sharp\mid L,
\qquad A^\sharp\equiv2B^\sharp\pmod R,
\qquad A^\sharp<2B^\sharp,\\
1\le v_2(L)+v_2(A^\sharp)-v_2(B^\sharp),\\
L\frac{A^\sharp}{B^\sharp}=E_j,
\qquad n_1=n_j.
\end{gathered}}
\tag{5}
\]

因此 \((A^\sharp,B^\sharp,1)\) 是合法的一阶二进见证。反过来，既约化使
\((A^\sharp,B^\sharp)\) 唯一，故每个自由除子对终端 \((E,n)\) 有唯一的 \(j=1\)
正规形。

### 证明

置

\[
\lambda=v_2(L),
\qquad \alpha=v_2(A),
\qquad \beta=v_2(B),
\qquad s=1-j+\alpha-\beta.
\tag{6}
\]

由 (2)，

\[
1-\lambda\le s.
\tag{7}
\]

又因 \((A,B)=1\)，二进赋值 \(\alpha,\beta\) 至少一个为零。若 \(s>0\)，必有
\(\beta=0\)，从而 \(s\le\alpha\le\lambda\)；若 \(s=0\)，二进部分不变；若
\(s<0\)，(7) 给出 \(-s\le\lambda-1\)。所以 (4) 约分后的二进分子或分母都整除 \(L\)。对每个奇素数，
\(A,B\) 的互素性和 \(A,B\mid L\) 已经给出同样的结论，故
\(A^\sharp,B^\sharp\mid L\)。

由 (1)，在模 \(R\) 的单位群中有

\[
\frac{A^\sharp}{B^\sharp}
\equiv2^{1-j}\frac AB
\equiv2\pmod R,
\]

即得同余；定向不等式也在两边同乘正数 \(2^{1-j}/B\) 后变为
\(A^\sharp<2B^\sharp\)。此外

\[
v_2\!\left(L\frac{A^\sharp}{B^\sharp}\right)
=\lambda+s
=\lambda+1-j+\alpha-\beta
\ge1.
\tag{8}
\]

所以 \((A^\sharp,B^\sharp,1)\) 满足一阶二进预算；(3)--(4) 直接给出
\(E_1=E_j\) 和 \(n_1=n_j\)。证毕。

## 3. 目标纤维的精确二进边界

写 \(K=2^{\nu_2}\prod_{q\in Q_{\rm odd}}q^{\nu_q}\)，其中
\(\nu_2=v_2(K)=\lambda-1\)。令 \(Q_K=\{q:q\mid K\}\) 与
\(Q_L=Q_K\cup\{2\}\)。原目标纤维
\(\mathcal Z^-_{R,K}\subseteq\mathbb Z^{Q_K}\) 已在 \(2\mid K\) 时包含二进坐标；
定义其到 \(L\)-支撑坐标的自然嵌入

\[
\widetilde{\mathcal Z}^-_{R,K}:=\iota_K\bigl(\mathcal Z^-_{R,K}\bigr)
\subseteq\mathbb Z^{Q_L}.
\tag{9}
\]

这里 \(\iota_K\) 在 \(2\mid K\) 时为恒等嵌入；仅在 \(K\) 为奇数时补入值为零的
二进坐标。相应的扩展目标指数盒为

\[
\qquad
\widetilde{\mathcal B}_{K}:=[-\nu_2,\nu_2]\times
\prod_{q\in Q_{\rm odd}}[-\nu_q,\nu_q]
\subseteq\mathbb Z^{Q_L}.
\tag{10}
\]

在此扩展坐标中定义关系向量

\[
\ell=v(A)-v(B)-j e_2
=v(A^\sharp)-v(B^\sharp)-e_2.
\tag{11}
\]

式 (1) 说明 \(\ell\) 属于模 \(R\) 的乘法关系格。奇素数坐标自动落在
\([ -\nu_q,\nu_q]\)，而二进坐标满足

\[
-\nu_2-1\le\ell_2\le\nu_2,
\qquad
v_2(E_j)=\lambda+\ell_2+1.
\tag{12}
\]

下界就是 (2)；上界由 \(j\ge1\)、\(\beta\ge0\) 及 \(\alpha\le\lambda\) 给出
\(\ell_2=\alpha-\beta-j\le\lambda-1=\nu_2\)。

所以有精确二分

\[
\boxed{
v_2(E_j)=1
\Longleftrightarrow
\ell_2=-\nu_2-1.}
\tag{13}
\]

这是唯一可能位于扩展目标指数盒 \(\widetilde{\mathcal B}_{K}\) 外的一层二进负侧。
它不可能来自目标纤维近邻对，因为近邻构造总给出 \(E=4U\)，故 \(4\mid E\) 且
\(n\equiv0\pmod4\)。

若 \(4\mid E_j\)（等价于 \(\ell\in\widetilde{\mathcal B}_{K}\)），则 \(\ell\) 已落入
扩展目标指数盒；但这仍不自动给出近邻 provenance。在这一前提下，精确的额外条件是
相应目标纤维透镜非空：

\[
\widetilde{\mathcal Z}^-_{R,K}\cap
\bigl(\widetilde{\mathcal Z}^-_{R,K}+\ell\bigr)\ne\varnothing.
\tag{14}
\]

因此 \(j=1\) 归一化压缩了终端搜索维度，却不把独立 divisor-ratio 终端伪装成目标纤维
近邻或可提升递降。

## 4. 一个外层且非近邻的控制

取

\[
p=673,
\qquad R=83,
\qquad K=13965=3\cdot5\cdot7^2\cdot19,
\qquad L=27930.
\tag{15}
\]

则 \(4K=pR+1\)。一阶见证

\[
(A,B,j)=(15,49,1)
\tag{16}
\]

满足 \(15\equiv2\cdot49\pmod{83}\) 和 \(15<98\)，并给出

\[
E=8550,
\qquad n=570.
\tag{17}
\]

这里 \(v_2(E)=1\)、\(n\equiv2\pmod4\)，关系向量（按
\((2,3,5,7,19)\)）为

\[
\ell=(-1,1,1,-2,0).
\tag{18}
\]

它正好处在 (13) 的唯一盒外层。相同终端也可写为 \((A,B,j)=(30,49,2)\)，而 (4)
唯一归一回 (14)。另一方面，该状态的目标纤维仅有

\[
(-1,0,-2,1),
\qquad (1,0,2,-1)
\tag{19}
\]

两点；在扩展坐标中它们分别嵌入为 \((0,-1,0,-2,1)\) 与
\((0,1,0,2,-1)\)。它们的奇部差 \((2,0,4,-2)\) 超过预算 \((1,1,2,1)\)，
故不存在近邻对。
这是“非近邻不等于无 dyadic 终端”的严格控制，不是 Erdős--Straus 反例。

窄复现：

```bash
python3 reproductions/type_i_generalized_dyadic_j_one_normalization.py --verify
```

## 5. 对选择器的影响

终端优先分派在自由除子对层只需搜索 \(j=1\)；原始 \(j>1\) 三元组可作为
`source_provenance` 保存。真正尚未闭合的部分是：

1. \(4\mid E\) 时的目标纤维透镜是否被占据；
2. 外层 \(v_2(E)=1\) 偶前驱的非自然标记提升；
3. 任意偶前驱到原素数解的 E4 全域提升与 E5 良基下降。
