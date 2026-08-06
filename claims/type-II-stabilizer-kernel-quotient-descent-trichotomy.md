---
kind: claim
claim_id: type-II-stabilizer-kernel-quotient-descent-trichotomy
title: Type II 稳定子包含同余核时的低模数商—递降三分
statement: 令 M=4D_*、M'=4D' 且 D'|D_*，pi:U(M)->pi(U(M')) 为模数降阶映射，K=ker(pi)。对源参数纤维积集 P=产品 B_i，若 K 包含于 T=Stab(P)，则 P=pi^{-1}(pi(P)) 且商集稳定子为 pi(T)，从而 -1∈P 当且仅当 -1∈pi(P)：命中是原模数直接证书，双重缺失时商群阶给出条件性良基递降。若 K 不包含于 T，商群可能出现“只在低模数命中”的伪分支；此时必须检查低模数参数纤维，非空才给出严格降模证书，空则给出 source-fiber 负证书。p=97 的 P={1,11} 模4命中但同余核不包含稳定子，正是该伪分支。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-source-lattice-fibered-kneser-selector
  - type-II-same-modulus-source-switch-crt-criterion
  - type-II-fixed-layer-stabilizer-defect-reduction
  - type-II-stabilizer-kernel-source-box-lattice-criterion
  - type-II-stabilizer-kernel-failure-dual-certificate
topics:
- type-II
- stabilizer
- congruence-kernel
- quotient-descent
- lower-modulus
- target-fiber
- source-switch
- well-founded-potential
- proof-program
sources:
  - claim: type-II-source-lattice-fibered-kneser-selector
    role: source-fiber-product
  - claim: type-II-same-modulus-source-switch-crt-criterion
    role: lower-modulus-parameter-fiber
visibility: public
last_checked: '2026-08-04'
---

# Type II 稳定子包含同余核时的低模数商—递降三分

## 模数商与同余核

令

\[
M=4D_*,\qquad M'=4D',\qquad D'\mid D_*,
\]

并令

\[
G=U(M),\qquad
\pi:G\longrightarrow\bar G=\pi(G)\le U(M')
\]

为模 \(M'\) 的降阶映射，\(K=\ker\pi\)。对一个固定源参数纤维积集（每个块都携带
对应的整数除子来源）

\[
P=B_1\cdots B_r\subseteq G
\]

取最终稳定子 \(T=\operatorname{Stab}_G(P)\)，并假设

\[
K\subseteq T.
\tag{1}
\]

## 稳定子饱和引理

在 (1) 下，

\[
\boxed{
P=\pi^{-1}(\bar P),\qquad \bar P=\pi(P).
}
\tag{2}
\]

### 证明

因为 \(K\subseteq T=\operatorname{Stab}(P)\)，对任意 \(x\in P\) 和 \(k\in K\)，
\(xk\in P\)。若 \(y\in G\) 满足 \(\pi(y)=\pi(x)\)，则 \(y=xk\) 对某个
\(k\in K\) 成立，故 \(y\in P\)。这说明 \(P\) 包含每个 \(\pi\)-纤维，因而
\(P=\pi^{-1}(\pi(P))\)。证毕。

同样有稳定子商恒等式

\[
\boxed{
\operatorname{Stab}_{\bar G}(\bar P)=\pi(T).
}
\tag{3}
\]

包含关系 \(\pi(T)\subseteq\operatorname{Stab}(\bar P)\) 显然。反向地，若
\(\bar g\) 稳定 \(\bar P\)，取 \(g\in G\) 使 \(\pi(g)=\bar g\)。由 (2)，
\(\pi(gP)=\bar g\bar P=\bar P=\pi(P)\) 推出 \(gP=P\)，故 \(g\in T\)。

核包含条件本身可以从源指数盒精确判定，而不应作为抽象假设。令
\(\varphi:\mathbb Z^r\to G\) 是真实源列映射、\(\Lambda=\ker\varphi\)，
\(\mathcal B\) 是 q-height 指数盒。则
\[
K\subseteq T
\iff
K\subseteq\operatorname{im}\varphi
\ \text{且}\
(\mathcal B+\Lambda)/\Lambda+
\varphi^{-1}(K)/\Lambda
=(\mathcal B+\Lambda)/\Lambda.
\]
前一项由 SNF 源列成员检查，后一项由有限商中的生成元平移检查；通过时回执
\(\mathrm{KERNEL\_STABILIZER\_CERT}\)，失败时区分
\(\mathrm{KERNEL\_NOT\_IN\_SOURCE}\) 与 \(\mathrm{KERNEL\_BOX\_MISS}\)。完整判据见
[Type II 稳定子同余核的源指数盒格判据](type-II-stabilizer-kernel-source-box-lattice-criterion.md)。

## 目标—商—递降三分

设目标为 \(-1\in G\)，并令 \(\bar t=\pi(-1)=-1\in\bar G\)。在核包含假设
(1) 下，(2) 立即给出

\[
\boxed{
-1\in P\quad\Longleftrightarrow\quad -1\in\bar P.
}
\tag{4}
\]

所以“原群缺失但商群命中”不可能发生在饱和分支；完整三分必须同时记录
核是否被稳定子吸收。

### A. 原模数直接命中

若 \(-1\in P\)，源因子乘积直接给出 \(M=4D_*\) 上的 Type II 证书。

### B. 饱和商同时缺失

若 \(K\subseteq T\) 且

\[
-1\notin P,\qquad -1\notin\bar P,
\tag{5}
\]

则目标在 \(\bar G\) 中仍缺失。由 (3)，所有 Kneser 稳定子和容量都可在
\(\bar G\) 中重算；若 \(|\bar G|<|G|\)，则

\[
\Psi(G,P)=\bigl(|G|,\ |\!G/T\!|,\ |G|-|P|\bigr)
\]

的词典序第一坐标严格下降到 \(\Psi(\bar G,\bar P)\) 的 \(|\bar G|\)。若标记参数
纤维和 Type II 正规形能沿 \(\pi\) 保持，这就是一条良基商递降；若不能保持，
必须记录 \(LIFT\_OBSTRUCTED\)。

### C. 核不包含时的低模数伪命中

若 \(K\not\subseteq T\)，可能出现

\[
-1\notin P,\qquad -1\in\bar P.
\tag{6}
\]

记录商命中的源因子乘积 \(h\)，并定义低模数参数纤维

\[
\mathcal C_{D'}(h)=
\left\{A':
A'\mid D',\ D'/A'\text{ 平方自由},\
4A'D'<p,\ h\mid p+4A'D'\right\}.
\tag{7}
\]

若 \(\mathcal C_{D'}(h)\ne\varnothing\)，则
\(K'=(h+1)/(4D')\)、\(C'=D'/A'\)、
\(B'=(K'p+A')/h\) 给出低模数 Type II 证书；若 \(D'<D_*\)，
这是严格降模边。若 \(\mathcal C_{D'}(h)=\varnothing\)，则该商命中只是
source-fiber 负证书，不能升级为原问题证书。

核不包含的失败现在也有规范对偶分派：若 \(K\) 不落在真实源子群，有限商
\(G/\operatorname{im}\varphi\) 给出平凡于全部源块而非平凡于某个核元素的
KERNEL_SOURCE_ANNIHILATOR；若 \(K\) 落在源子群但指数盒不饱和，则
\(1_P-1_{Pk}\) 的 Fourier 可逆性给出 KERNEL_BOX_FOURIER。目标商伪命中时优先
使用目标陪集截面的 KERNEL_SPLIT_FOURIER。完整二分见
[Type II 稳定子同余核失败的对偶 Fourier 二分](type-II-stabilizer-kernel-failure-dual-certificate.md)。

## 为什么必须保留核包含条件

在 \(p=97,M=24\) 的单纤维

\[
P=\{1,11\}\subset U(24)
\]

中，投影到 \(U(4)\) 得
\(\pi(P)=\{1,-1\}\)，看起来低模数已经命中；但
\[
\ker\bigl(U(24)\to U(4)\bigr)
\not\subseteq\operatorname{Stab}_{U(24)}(P).
\]

因此 \(P\ne\pi^{-1}(\pi(P))\)，模 \(4\) 命中不能回升到模 \(24\)。
这个边界说明 (1) 不是形式技术条件，而是低模数商递降合法性的核心门槛。

## 研究边界

(1)--(7) 把固定层稳定子约化、低模数 source-switch 和良基商势接成一个严格三分，
但还没有证明任意 Type II 失败积集都包含某个模数降阶同余核，也没有证明
\(\mathcal C_{D'}(h)\) 为空时一定产生其它 Type I/II 证书。下一步需要从 q-height
幂块的稳定子结构证明核包含，或给出核不包含时的 Fourier/二幂严格出口。
