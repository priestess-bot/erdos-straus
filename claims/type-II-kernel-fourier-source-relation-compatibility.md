---
kind: claim
claim_id: type-II-kernel-fourier-source-relation-compatibility
title: Type II 核 Fourier 与源关系格的仿射相容性判据
statement: 对有限阿贝尔单位群中的源指数盒，目标伪命中陪集的核 Fourier 系数可以精确写成真实乘法碰撞商上的仿射关系格 Fourier 和。给定相对频率 theta 与目标锚点 a，它们可提升为同一个核角色当且仅当在源关系格与锚点关系上同时满足恒等关系；失败时得到严格的 LIFT_OBSTRUCTED 回执。该判据消除了把 CRT 加法频率直接计入 Type II 容量的逻辑漏洞，但不自动把相容角色升级为 Type II 命中或算术递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-congruence-kernel-split-fourier-certificate
  - type-II-source-fiber-qheight-kneser-bridge
  - type-II-same-modulus-source-switch-crt-criterion
topics:
- type-II
- kernel-fourier
- source-relation-lattice
- affine-fourier
- lift-compatibility
- source-switch
- capacity
- descent-interface
- proof-program
sources:
  - claim: type-II-congruence-kernel-split-fourier-certificate
    role: target-coset-kernel-Fourier
  - claim: type-II-source-fiber-qheight-kneser-bridge
    role: source-exponent-box-and-q-height
  - claim: type-II-same-modulus-source-switch-crt-criterion
    role: labelled-CRT-lift-obstruction
visibility: public
last_checked: '2026-08-04'
---

# Type II 核 Fourier 与源关系格的仿射相容性判据

## 源盒、目标陪集与真实碰撞商

令 \(G\) 为有限阿贝尔群，\(K\le G\)，\(\pi:G\to G/K\) 为商映射。给定源单位
\(u_1,\ldots,u_r\in G\) 和有限指数盒

\[
\mathcal Z=\prod_{i=1}^r\{0,1,\ldots,d_i\},
\qquad
\phi(z)=\prod_i u_i^{z_i},
\qquad
P=\phi(\mathcal Z).
\tag{1}
\]

固定目标 \(t\in G\)，并假设

\[
t\notin P,
\qquad
\pi(t)\in\pi(P).
\tag{2}
\]

目标陪集中的源指数为

\[
\mathcal E_t=\{z\in\mathcal Z:\pi(\phi(z))=\pi(t)\}.
\tag{3}
\]

不能直接按 \(\mathcal E_t\) 计数，因为不同指数可能给出同一个单位。定义真实碰撞关系

\[
z\sim_G z'\iff \phi(z)=\phi(z'),
\tag{4}
\]

并令 \(\widetilde{\mathcal E}_t=\mathcal E_t/\!\sim_G\)。对每个碰撞类定义

\[
\kappa([z])=t^{-1}\phi(z)\in K.
\tag{5}
\]

则目标截面正好是

\[
S_t=\{\kappa([z]):[z]\in\widetilde{\mathcal E}_t\}
 =\{k\in K:tk\in P\}.
\tag{6}
\]

因为 \(t\notin P\)，有 \(1\notin S_t\)，而 (2) 保证 \(S_t\ne\varnothing\)。因此，
对任意 \(\chi\in\widehat K\)，核 Fourier 系数有精确的无重数公式

\[
\boxed{
\widehat{1_{S_t}}(\chi)
 =\sum_{[z]\in\widetilde{\mathcal E}_t}
   \overline{\chi\!\left(t^{-1}\phi(z)\right)}.
}
\tag{7}
\]

这一步是必要的：若直接对指数盒求和，源关系格中的碰撞会被重复收费，所得幅度
不再是目标截面的 Fourier 证书。

## 仿射关系格分解

定义两个源关系格

\[
L_\pi=\{n\in\mathbb Z^r:\pi(\phi(n))=1\},
\qquad
L_G=\{n\in\mathbb Z^r:\phi(n)=1\}.
\tag{8}
\]

显然 \(L_G\subseteq L_\pi\)，且第一同构定理给出

\[
L_\pi/L_G\ \simeq\ H_\pi:=\phi(L_\pi)\le K.
\tag{9}
\]

取一个基类 \([z_0]\in\widetilde{\mathcal E}_t\)，写

\[
\alpha=t^{-1}\phi(z_0)\in K,
\tag{10}
\]

并令

\[
Q_t=\{[z-z_0]_{L_G}: [z]\in\widetilde{\mathcal E}_t\}
\subseteq L_\pi/L_G.
\tag{11}
\]

由 \(\phi(z-z_0)\in K\) 及 (9)，有

\[
S_t=\alpha\,\phi(Q_t).
\tag{12}
\]

于是 (7) 等价于仿射关系格 Fourier 和

\[
\boxed{
\widehat{1_{S_t}}(\chi)
 =\overline{\chi(\alpha)}
   \sum_{\bar n\in Q_t}\overline{\chi(\phi(n))}.
}
\tag{13}
\]

式 (13) 把核分裂的两个部分分开：

* \(Q_t\) 是源关系格上的相对频率支撑；
* \(\alpha\) 是目标伪命中的绝对锚点相位。

只有相对关系而没有锚点相位的加法 Fourier 证书，不能自动代表 (13)。

## 相容性定理

设 \(\theta:L_\pi\to\mathbb C^\times\) 是一个候选相对相位群同态，\(a\in\mathbb C^\times\)
是候选锚点相位。要求它们来自某个核角色 \(\chi\in\widehat K\)：

\[
\theta(n)=\chi(\phi(n))\quad(n\in L_\pi),
\qquad
a=\chi(\alpha).
\tag{14}
\]

定义仿射关系集

\[
\mathcal R_\alpha
 =\{(n,m)\in L_\pi\times\mathbb Z:
      \phi(n)\alpha^m=1\}.
\tag{15}
\]

则存在满足 (14) 的核角色 \(\chi\) 当且仅当

\[
\boxed{
\theta(n)=1\quad(n\in L_G),
\qquad
\theta(n)a^m=1\quad((n,m)\in\mathcal R_\alpha).
}
\tag{16}
\]

### 证明

必要性直接来自 \(\phi(n)=1\)（当 \(n\in L_G\)）以及

\[
1=\chi(\phi(n)\alpha^m)=\theta(n)a^m.
\]

反过来，在 \(H_0=\langle H_\pi,\alpha\rangle\le K\) 上定义

\[
\psi(\phi(n))=\theta(n),
\qquad
\psi(\alpha)=a.
\tag{17}
\]

若同一元素有两种表示，商去两种表示得到一个 \((n,m)\in\mathcal R_\alpha\)，
或得到 \(n\in L_G\)；(16) 保证 (17) 与表示无关。因此 \(\psi\) 是 \(H_0\) 上的
群角色。有限阿贝尔群子群上的复角色可延拓到整个 \(K\)，得到
\(\chi\in\widehat K\)。证毕。

把 (16) 用 Smith 正规形作用于 \(L_\pi\) 的整数基和有限群 \(K\) 的分解，便得到
一个有限且可复核的 SOURCE_RELATION_FOURIER 载荷。

## 对容量与递降的严格含义

给定实际核字符 \(\chi\)，取

\[
\theta_\chi(n)=\chi(\phi(n)),
\qquad
a_\chi=\chi(\alpha).
\tag{18}
\]

则 (16) 自动成立，且 (13) 是一个真正可提升到 \(K\) 的源关系格 Fourier 证书。
这关闭了“核字符是否真的来自源块”的隐藏逻辑缺口，但仍不等于 Type II 命中。

反过来，若从 CRT 参数集合或其它加法模型得到候选 \((\theta,a)\)，而 (16) 失败，
则该频率不能进入 \(U(4D_*)\) 的 Kneser 容量账本，必须标记
LIFT_OBSTRUCTED。失败的具体关系 \((n,m)\) 是一个有限的反证回执，而不是
“跨状态容量已经支付”的理由。

因此，未吸收核分支现在有严格的两层分派：

1. 先用 Parseval 选出非平凡核角色，再用 (13) 记录其源关系格支撑；
2. 对任何外部频率先过 (16)，失败即停止乘法提升，成功才允许交给 q-height/Kneser
   账本。

这一步把剩余的全称缺口精确缩小为：如何从一个**相容**的
SOURCE_RELATION_FOURIER 证书证明 q 进容量超载、构造 Type II 目标命中，或给出
携带标记集的严格良基递降。关系格相容性本身已经不再是未区分的黑箱。

## \(p=97\) 的两类边界

### 真正的核角色：相容

取 \(G=U(24)\)、\(K=\{1,5,13,17\}\)、\(t=23\)、\(P=\{1,11\}\)。
源盒为 \(z\in\{0,1\}\)、\(\phi(z)=11^z\)。目标陪集只有 \(z_0=1\)，并且

\[
\alpha=23^{-1}11\equiv13\pmod{24},
\qquad
L_\pi=L_G=2\mathbb Z,
\qquad
Q_t=\{0\}.
\]

因此 (13) 退化为 \(\widehat{1_{S_t}}(\chi)=\overline{\chi(13)}\)。
取核角色 \(\chi(13)=-1\)，得到此前的系数 \(-1\)；这里没有任何加法—乘法错配。

### CRT 加法频率：不相容

同一个 \(p=97,D=6\) 的伪池化使用标签

\[
(x_1,x_2)=(1,3)\pmod{143},
\qquad
(u_1,u_2)=(11,13)\pmod{24}.
\]

对频率 \(t=1\)，向量 \(n=(3,-1)\) 满足

\[
3x_1-x_2=0\pmod{143},
\qquad
u_1^3u_2^{-1}\equiv23\not\equiv1\pmod{24}.
\]

所以第一条关系条件失败；该 CRT 频率是严格的
LIFT_OBSTRUCTED，不能把 \(11\cdot13\equiv-1\pmod{24}\) 充当一个带来源的
Type II 证书。这与参数纤维为空的直接计算一致。

## 研究边界

本引理完成的是“核 Fourier 证书 ↔ 源关系格”的精确接线和不可提升反证，尚未证明
相容 Fourier 角色必然产生 Type I/II 短证书或核心素数下降。后续若要闭合统一选择器，
必须在 (13) 的 \(Q_t\) 上证明一个真实 q-height/载体成本下界，或者构造保持来源标记的
商递降；不能把 (16) 本身误称为容量矛盾。
