---
kind: claim
claim_id: type-II-kneser-saturated-one-coset-hole-certificate
title: Type II Kneser 饱和纤维的一孔陪集与 quotient Fourier 证书
statement: 设有限阿贝尔群 G 中的源积集 P 具有最终稳定子 T，目标 t 不属于 P，且逐块 Kneser 活跃容量满足 sum_i kappa_i<=|G/T|-2。定义 delta=|G/T|-2-sum_i kappa_i，令 c 为 P 在 G/T 中遗漏的陪集数。则 1<=c<=delta+1；特别地 delta=0 时 P 恰为 G 去掉唯一目标陪集 tT。此时所有非平凡 quotient 角色 chi（平凡于 T）都有精确 Fourier 系数 -|T| overline{chi(t)}，给出规范 quotient Fourier 负证书。跨纤维加权时，sum_A w_A(c_A-1)<=sum_A w_A delta_A；零总缺口迫使每个遗漏纤维均为一孔结构。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-cross-state-fiber-capacity-surplus-certificate
  - type-II-source-lattice-fibered-kneser-selector
  - type-II-congruence-kernel-split-fourier-certificate
  - type-II-stabilizer-kernel-quotient-descent-trichotomy
topics:
- type-II
- kneser
- saturated-fiber
- one-coset-hole
- quotient-fourier
- capacity
- cross-state
- constructive-certificate
- proof-program
sources:
  - claim: type-II-cross-state-fiber-capacity-surplus-certificate
    role: cross-fiber-deficit-ledger
  - claim: type-II-source-lattice-fibered-kneser-selector
    role: source-product-and-stabilizer
  - claim: type-II-congruence-kernel-split-fourier-certificate
    role: quotient-kernel-Fourier-interface
  - claim: type-II-stabilizer-kernel-quotient-descent-trichotomy
    role: quotient-descent-routing
visibility: public
last_checked: '2026-08-05'
---

# Type II Kneser 饱和纤维的一孔陪集与 quotient Fourier 证书

## 单纤维缺口与遗漏陪集数

令 \(G\) 为有限阿贝尔群，\(P\subseteq G\) 为源块积集，最终稳定子为

\[
T=\operatorname{Stab}_G(P),\qquad n=|G/T|.
\tag{1}
\]

目标 \(t\notin P\)，且每个源块的 Kneser 活跃容量为 \(\kappa_i\)。定义

\[
\delta=n-2-\sum_i\kappa_i.
\tag{2}
\]

在目标缺失时，逐块 Kneser 不等式给出 \(\delta\ge0\)。由于 \(P\) 是 \(T\)-不变集，
令

\[
c=\frac{|G\setminus P|}{|T|}
=n-\frac{|P|}{|T|}
\tag{3}
\]

为稳定子商中遗漏的陪集数。目标陪集 \(tT\) 缺失，所以 \(c\ge1\)。另一方面，

\[
|P|\ge |T|\left(1+\sum_i\kappa_i\right)
=|T|(n-1-\delta),
\tag{4}
\]

从而

\[
\boxed{1\le c\le\delta+1.}
\tag{5}
\]

这把 Kneser 容量缺口精确转成遗漏陪集预算。

## 饱和一孔定理

当 \(\delta=0\) 时，(4) 与目标缺失给出的上界
\(|P|\le |G|-|T|=|T|(n-1)\) 同时取等号。因此

\[
\boxed{
P=G\setminus tT.
}
\tag{6}
\]

也就是说，纤维不是一个任意的“差一点”积集，而是稳定子商中恰好只缺一个
目标陪集。这是 Kneser_SATURATED_ONE_HOLE 结构回执。

## 一孔的精确 quotient Fourier 频谱

令 \(\chi\in\widehat G\) 为平凡于 \(T\) 的角色，等价于商群
\(\bar\chi\in\widehat{G/T}\) 的提升。采用

\[
\widehat{1_P}(\chi)=\sum_{x\in G}1_P(x)\overline{\chi(x)}
\tag{7}
\]

的约定，由 (6)：

\[
\widehat{1_P}(\chi)=
\begin{cases}
|P|,&\chi=1,\\[2mm]
-|T|\,\overline{\chi(t)},&\chi\ne1,\ \chi|_T=1,\\[2mm]
0,&\chi|_T\ne1.
\end{cases}
\tag{8}
\]

证明是直接的：非平凡角色在 \(G\) 上总和为零；若 \(\chi|_T=1\)，目标陪集
\(tT\) 的 Fourier 和为 \(|T|\overline{\chi(t)}\)；若 \(\chi\) 在 \(T\) 上非平凡，
该陪集和也为零。故 (8) 给出完整频谱。

只要 \(n>1\)，就存在非平凡 quotient 角色；按有限角色的固定排序选择第一个，
即可得到规范的 quotient Fourier 负证书。该角色是实际 \(G\) 的内禀角色，不能被
误标记为外部加法频率的 LIFT_OBSTRUCTED。

## 一孔纤维的新增源块填洞引理

对任意新增二点源块 \(B(u)=\{1,u\}\subseteq G\)，有

\[
P\,B(u)=P\cup Pu
=
\begin{cases}
P,&u\in T,\\
G,&u\notin T.
\end{cases}
\tag{10}
\]

事实上，\(u\in T\) 时 \(Pu=P\)。若 \(u\notin T\)，则 \(P\) 的唯一缺失陪集
\(tT\) 与 \(Pu\) 的唯一缺失陪集 \(tTu^{-1}\) 不同；两个补集不相交，故
\(P\cup Pu=G\)。对幂块

\[
B_d(u)=\{1,u,\ldots,u^d\},\qquad d\ge1,
\tag{11}
\]

同样有：\(u\notin T\) 时 \(PB_d(u)=G\)，\(u\in T\) 时
\(PB_d(u)=P\)。

因此，饱和一孔纤维的新增源块分派是严格二分：

1. 若存在保持同一参数纤维且 \(u\notin T\) 的源块，则立即填满目标陪集，给出
   \(-1\in P B_d(u)\) 的 Type II 短证书；
2. 若所有可用新增源块都满足 \(u\in T\)，它们全部被吸收，不能继续产生容量，
   纤维保留一孔 quotient Fourier 负证书；
3. 若某源块不满足 source-switch 合同，则记为 UNAVAILABLE_SOURCE_BLOCK，不能
   把它当作填洞块，也不能把其跨纤维残数加入当前容量。

## 少孔纤维的平移交与剩余容量

更一般地，令 \(\bar G=G/T\)、\(\bar P=P/T\)，缺口集
\(C=\bar G\setminus\bar P\)，以及一组新增源块的去重积集
\(\bar R\subseteq\bar G\)。则有精确补集恒等式

\[
\boxed{
\bar G\setminus(\bar P\,\bar R)
=\bigcap_{r\in\bar R}Cr.
}
\tag{12}
\]

若右侧非空，任取 \(x\) 属于右侧，则 \(x\bar R^{-1}\subseteq C\)，从而
\[
|\bar R|\le |C|=c.
\tag{13}
\]
因此

\[
\boxed{
|\bar R|>c\Longrightarrow \bar P\,\bar R=\bar G.
}
\tag{14}
\]

若 \(|\bar R|=c\) 且仍有缺口，则对每个 \(x\) 都有
\(x\bar R^{-1}=C\)，即缺口集被新增源积集刚性锁定为一个平移；这给出
HOLE_LOCKED 的有限结构回执。结合 (5)，若当前 Kneser 缺口为 \(\delta\)，则只要
剩余合法源积集满足

\[
|\bar R|\ge\delta+2,
\tag{15}
\]

就必填满目标。对 \(\bar R\) 再应用 Kneser 下界，可用剩余 q-height 的
\(\kappa\) 直接验证 (15)。

更精确地，令剩余源块在 \(\bar G\) 中的 Kneser 活跃容量为
\(\kappa_i^{\mathrm{rem}}\)。即使剩余积集自身有稳定子，Kneser 仍给出

\[
|\bar R|
\ge |\operatorname{Stab}(\bar R)|
\left(1+\sum_i\kappa_i^{\mathrm{rem}}\right)
\ge 1+\sum_i\kappa_i^{\mathrm{rem}}.
\tag{15a}
\]

故有严格的剩余 q-height 填洞门

\[
\boxed{
\sum_i\kappa_i^{\mathrm{rem}}\ge c
\Longrightarrow
\bar P\,\bar R=\bar G.
}
\tag{15b}
\]

只有 \(\sum_i\kappa_i^{\mathrm{rem}}\le c-1\) 时，剩余源块才可能停留在
HOLE_LOCKED 或 UNAVAILABLE_SOURCE_BLOCK 分支。

在最终稳定子商中 \(\operatorname{Stab}_{\bar G}(\bar P)=1\)，且补集 \(C\) 的稳定子
也为平凡群。故 HOLE_LOCKED 等号分支若仍有缺口，必满足

\[
\operatorname{Stab}_{\bar G}(\bar R)
=\operatorname{Stab}_{\bar G}(C)
=1.
\tag{16}
\]

所以该分支不存在可继续吸收的隐藏稳定子；后续只能调用源关系 Fourier、外部
合法非平凡源块或另一条 Type I/II 递降。

## HOLE_LOCKED 的源—对偶 Fourier 传递

在等号分支 \(C=x\bar R^{-1}\) 中，对任意 quotient 角色
\(\bar\chi\in\widehat{\bar G}\) 有

\[
\widehat{1_C}(\bar\chi)
=\overline{\bar\chi(x)}
\sum_{r\in\bar R}\bar\chi(r),
\tag{17}
\]

而对非平凡角色

\[
\boxed{
\widehat{1_{\bar P}}(\bar\chi)
=-\overline{\bar\chi(x)}
\sum_{r\in\bar R}\bar\chi(r).
}
\tag{18}
\]

因此，源积集 \(\bar R\) 的每一个非平凡 Fourier 方向都被精确传递为目标积集
\(\bar P\) 的负相位方向。若 \(1\le|\bar R|<|\bar G|=n\)，Parseval 给出

\[
\sum_{\bar\chi\ne1}
\left|\sum_{r\in\bar R}\bar\chi(r)\right|^2
=|\bar R|(n-|\bar R|),
\tag{19}
\]

从而存在规范选择的非平凡角色满足

\[
\boxed{
\left|\widehat{1_{\bar P}}(\bar\chi)\right|
\ge
\sqrt{\frac{|\bar R|(n-|\bar R|)}{n-1}}.
}
\tag{20}
\]

这些角色是实际商群的内禀角色；只有把 (20) 外部解释成加法参数频率时，才需要
重新经过源关系相容性门。

## Fourier 锚点—关系二分

固定一个非平凡 quotient 角色 \(\bar\chi\)，令

\[
N=|\bar R|,
\qquad
\rho_{\bar\chi}
=\frac{\left|\sum_{r\in\bar R}\bar\chi(r)\right|}{N}.
\tag{21}
\]

则有严格二分：

\[
\boxed{
\rho_{\bar\chi}=1
\iff
\bar\chi\text{ 在 }\bar R\text{ 上恒相位}
\iff
\bar\chi|_{\Delta_R}=1,
}
\tag{22}
\]

其中 \(\Delta_R=\langle rr'^{-1}:r,r'\in\bar R\rangle\) 是源积集差分群。此时
HOLE 角色只检测锚点相位，成对关系需求为零。

若 \(\rho_{\bar\chi}<1\)，则

\[
\boxed{
\sum_{r,r'\in\bar R}
\left|1-\bar\chi(rr'^{-1})\right|^2
=2N^2(1-\rho_{\bar\chi}^2)>0.
}
\tag{23}
\]

因此至少存在一条相位不一致的关系边，\(\Delta_R\ne1\)。取任意素数
\(\ell\mid|\bar\chi(\Delta_R)|\)，则

\[
\dim_{\mathbb F_\ell}(\Delta_R/\ell\Delta_R)\ge1.
\tag{24}
\]

由固定纤维 q-height 到初等商秩的列注入，(24) 强制至少一个保持当前目标纤维的
\(\ell\)-方向源列；若源关系核的初等商秩为零，则得到
SOURCE_RANK_INCONSISTENT，而不能把相位能量误算成容量超载。若该列存在，则
进入 q-height/Kneser 容量账本。

## 跨纤维的近饱和传递

对参数纤维 \(A\) 写 \(c_A,\delta_A\)，并取 \(w_A>0\)。由 (5)：

\[
\boxed{
\sum_Aw_A(c_A-1)
\le
\sum_Aw_A\delta_A
=\mathcal B_w-\mathcal Q_w.
}
\tag{9}
\]

因此：

1. 若 \(\mathcal Q_w>\mathcal B_w\)，前一 surplus 定理已经强制某个纤维命中；
2. 若 \(\mathcal Q_w=\mathcal B_w\)，所有遗漏纤维都满足 \(c_A=1\)，每个都是一孔
   quotient Fourier 分支；
3. 若 \(\mathcal Q_w<\mathcal B_w\)，额外遗漏陪集总数被精确预算
   \(\mathcal B_w-\mathcal Q_w\) 控制，不能把残余笼统称为“容量不足”。

## 例子

在加法循环群 \(C_5\) 中取三个二点块
\[
\{0,1\}+\{0,1\}+\{0,1\}=\{0,1,2,3\}.
\]
稳定子平凡、\(n=5\)、\(\sum\kappa_i=3=n-2\)，所以 \(\delta=0\)，唯一缺口是
\(tT=\{4\}\)。每个非平凡角色的 Fourier 系数都是
\(-\overline{\chi(4)}\)，符合 (8)。

\(p=97\) 的三个源参数纤维均不是一孔饱和：各自的单列被自身稳定子吸收，
\(\delta_A\) 保持正值；跨纤维直接相乘产生的 \(11\cdot13=-1\) 不改变这一结论。

## 研究边界

本引理把非正 surplus 中的饱和和近饱和纤维压缩为明确的遗漏陪集数、quotient
Fourier 证书、“新增非平凡源块填洞”出口、少孔平移交容量判据和源—对偶 Fourier
传递，以及 Fourier 锚点—关系二分。尚未闭合的是：证明每个核心素数的
一孔纤维都存在合法的非平凡新增源块，或证明所有 UNAVAILABLE_SOURCE_BLOCK/
稳定子吸收残余必转入 Type I/F/G 容量或严格良基递降；一孔角色本身仍不是自动命中。
