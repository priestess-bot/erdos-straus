---
kind: claim
claim_id: type-I-linear-three-label-reselection-conjecture
title: 线性一般 B 的三标签层重选终端选择猜想
statement: 对每个核心素数p，要么存在普通Type II p-1双尾证书，要么存在完整线性源谱中的状态p=a+s+asR，使K=(pR+1)/4的源碰撞、源私有、仿射碰撞、仿射私有四层中某个至多三层的子积N满足-1属于C_R(N)。该条件推出一般B目标平方除子命中和E=sR+1的偶 Type I 终端桥，因而严格蕴含原混合终端选择引理。三千万有限剖面支持该命题，两个完整单点表明“两层”不能替代“三层”。
claim_status: open
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- type-II
- linear-source
- general-b
- target-square-divisor
- coordinate-label
- reselection
- finite-product
- terminal-bridge
- conjecture
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 线性一般 B 的三标签层重选终端选择猜想

固定核心素数 \(p\)。其完整线性源谱由全部

\[
p=a+s+asR,
\qquad s\equiv1\pmod2,
\qquad R\equiv3\pmod4 \tag{1}
\]

组成；平方根界保证此谱对每个固定 \(p\) 有限。对一个有向状态，按
[坐标标签碰撞分解](type-I-linear-block-label-collision.md)与
[标签层支撑剖面](type-I-linear-label-layer-support-profile.md)定义

\[
K=G_cG_pL_cL_p, \tag{2}
\]

其中四项依次是源碰撞、源私有、仿射碰撞、仿射私有层。对层子集 \(I\)，记其乘积为
\(N_I\)。

## 猜想

\[
\boxed{
\begin{aligned}
&\text{每个核心素数 \(p\) 都有普通 Type II \(p-1\) 双尾证书，}\
&\quad\text{或存在 (1) 的一个状态与 } I\subseteq
\{G_c,G_p,L_c,L_p\},\\
&\quad |I|\le3,
\qquad -1\in\mathcal C_R(N_I).
\end{aligned}} \tag{3}
\]

这里

\[
\mathcal C_R(N)=
\left\{\prod_{q\mid N}q^{z_q}\bmod R:
-\nu_q(N)\le z_q\le\nu_q(N)\right\}. \tag{4}
\]

若 (3) 的第二分支成立，则 \(N_I\mid K\) 给出 \(-1\in\mathcal C_R(K)\)，因此存在
\(d\mid K^2\) 满足 \(4d\equiv-1\pmod R\)。线性源的

\[
E=sR+1,\qquad n=p-s=aE \tag{5}
\]

又满足

\[
2\mid E,\qquad E\mid4K^2,\qquad E\equiv1\pmod R,\qquad
E\le4K-2R. \tag{6}
\]

所以 (3) 的第二分支给出一般 \(B\) Type I 正规形与原混合终端选择引理所需的偶桥。
这证明本猜想严格蕴含[原目标选择器](type-I-target-divisor-even-terminal-selector.md)。

## 有限证据与尖锐性

[三千一百万重选剖面](type-I-linear-label-reselection-profile-31m.md)完整枚举了200个普通双尾
遗漏的全部线性源谱；每一点都有 \(|I|\le3\) 的重选，且分布为

\[
185_{|I|=1}+13_{|I|=2}+2_{|I|=3}. \tag{7}
\]

两点

\[
p=13{,}782{,}409,\qquad p=26{,}034{,}649 \tag{8}
\]

各自只有一张完整谱目标命中，且最小层数为三。因此不能把 (3) 的三层界替换为两层。

固定状态不应与重选混淆：[372409 的四层边界](type-I-linear-four-label-layer-boundary-372409.md)
给出两张必须全四层的成功状态；但同一个素数的其它线性源可重选到较小支撑。这正是 (3)
把量词放在“存在一个状态”而非“每个状态”的原因。

## 真正缺口

有限证据并不排除某个更大的尾遗漏具有下列任一情形：

- 所有线性目标命中均需要四层；
- 完整线性源谱根本没有目标命中；
- 普通 Type II 双尾和线性源两分支同时失败。

证明 (3) 需要比较不同 \(R\) 的完整四层素因子与角色/有限指数障碍，而不是对一个固定
状态应用 Kneser 型饱和。现有[跨模数公因子刚性](type-I-linear-cross-modulus-gcd-rigidity.md)
和[混合障碍剖面](type-I-linear-general-b-obstruction-mixture-profile-600m.md)提供了这种比较的
精确输入，但尚未给出全称相交定理。
