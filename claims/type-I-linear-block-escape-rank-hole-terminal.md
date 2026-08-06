---
kind: claim
claim_id: type-I-linear-block-escape-rank-hole-terminal
title: 线性 block escape 独立秩的 \(2^r\) 目标填洞终端
statement: 设当前 Type II 源积集 P 的最终稳定子为 T，商群 Gbar=G/T 的缺口陪集数为 c。若线性 block escape 的 r 个 alternate source 已通过 source-switch/SNF/CRT，且它们在某个 ell-初等商中的像线性独立，则相应二点块乘积 R={prod u_i^{epsilon_i}:epsilon_i in {0,1}} 至少有 2^r 个不同商元素。若 c<2^r，则 P R=G，直接得到目标 Type II 命中；若 c=1，任意一个非平凡 escaped source 即闭合该纤维。若 c>=2^r，或某个方向被稳定子吸收，则不能宣称命中，必须转入 HOLE_LOCKED、Kneser 容量、annihilator 或新的 alternate。该结果把 escaped rank demand 与目标纤维缺口建立了精确 \(2^r\) 填洞映射。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-linear-block-escape-hall-annihilator-closure
  - type-I-linear-block-escape-quotient-rank
  - type-II-kneser-saturated-one-coset-hole-certificate
  - type-II-multiblock-kneser-active-capacity-dichotomy
  - type-II-cross-state-fiber-capacity-surplus-certificate
topics:
- type-I
- linear-source
- block-escape
- q-rank
- target-fiber
- Kneser
- hole-filling
- Type-II
- capacity
- source-switch
- E1-E5
- proof-program
sources:
  - claim: type-I-linear-block-escape-quotient-rank
    role: escaped-rank-demand
  - claim: type-I-linear-block-escape-hall-annihilator-closure
    role: alternate-source-matching
  - claim: type-II-kneser-saturated-one-coset-hole-certificate
    role: complement-hole-identity
  - claim: type-II-multiblock-kneser-active-capacity-dichotomy
    role: stabilizer-capacity
visibility: public
last_checked: '2026-08-05'
---

# 线性 block escape 独立秩的 \(2^r\) 目标填洞终端

## 1. 稳定子商与缺口

令 \(G\) 是当前 Type II 有限目标群，\(P\subseteq G\) 是已经加入已有源块的积集，
\(T=\operatorname{Stab}_G(P)\)，并写

\[
\bar G=G/T,\qquad
\bar P=PT/T,\qquad
C=\bar G\setminus\bar P,\qquad
c=|C|.
\tag{1}
\]

目标陪集 \(\bar t=tT\) 在 \(C\) 中。对一个已经通过整数 source-switch、参数纤维、
SNF、CRT 和范围门的 escaped source \(u\)，令 \(\bar u=uT\)。选定一个
\(\ell\)-初等商

\[
\rho:\bar G\longrightarrow V_\ell,
\qquad V_\ell\ \text{为 }\mathbb F_\ell\text{-向量空间}.
\tag{2}
\]

设 \(u_1,\ldots,u_r\) 是 Hall/Rado 匹配出的 \(r\) 个 alternate source，并满足

\[
\rho(\bar u_1),\ldots,\rho(\bar u_r)
\quad\text{线性独立}.
\tag{3}
\]

条件 (3) 正是 escaped rank demand 的独立匹配回执；若某个 \(\bar u_i=1\)，则该
方向被 \(T\) 吸收，不得计入 \(r\)。

## 2. 二点块乘积的独立性

定义二点源块

\[
B_i=\{1,\bar u_i\},\qquad
\bar R=B_1\cdots B_r
=\left\{\prod_{i=1}^{r}\bar u_i^{\varepsilon_i}:
\varepsilon_i\in\{0,1\}\right\}.
\tag{4}
\]

若两组比特向量 \(\varepsilon,\varepsilon'\) 给出相同商元素，则

\[
\prod_i\bar u_i^{\varepsilon_i-\varepsilon_i'}=1.
\]

对 \(\rho\) 取像得到

\[
\sum_i(\varepsilon_i-\varepsilon_i')\rho(\bar u_i)=0
\quad\text{in }V_\ell.
\]

因系数 \(\varepsilon_i-\varepsilon_i'\in\{-1,0,1\}\subset\mathbb F_\ell\)，在
\(\ell=2\) 时仍是 \(\{0,1\}\) 的独立组合，在 \(\ell>2\) 时同样只能全部为零。故

\[
\boxed{|\bar R|=2^r.}
\tag{5}
\]

这一步只使用初等商独立性，不把不同 escaped source 的整数高度相乘；每个方向只
贡献一个二点槽。

## 3. 缺口小于 \(2^r\) 时的 Type II 终端

补集恒等式为

\[
\bar G\setminus(\bar P\,\bar R)
=\bigcap_{\bar v\in\bar R}C\bar v.
\tag{6}
\]

若右端非空，取 \(\bar x\) 属于右端，则
\(\bar x\bar R^{-1}\subseteq C\)，从而

\[
|\bar R|\le|C|=c.
\tag{7}
\]

结合 (5)，得到精确填洞门

\[
\boxed{
c<2^r\quad\Longrightarrow\quad
\bar P\,\bar R=\bar G.
}
\tag{8}
\]

特别地：

* \(c=1\) 且 \(r\ge1\) 时，任意一个非平凡 escaped source 都填满唯一目标缺口；
* \(c=2^r-1\) 时仍必命中；
* \(c\ge2^r\) 时本引理不保证命中，必须继续使用稳定子增长、HOLE_LOCKED 或
  annihilator 分支。

若所有 \(u_i\) 的 source-switch 和整数重建均满足 E1--E5，则 (8) 在原参数状态中
给出一个显式 Type II 短证书；若只有有限群条件通过而某个 E 门未通过，回执只能是
FIBER_TARGET_FILLED_BUT_LIFT_OBSTRUCTED，不能升级为原猜想的证书。

## 4. 与 escaped rank demand 的接口

设上一层逃逸商证书给出

\[
r_\ell^{\rm esc}
=\dim_{\mathbb F_\ell}
(\overline{\Delta}_{\rm esc}/\ell\overline{\Delta}_{\rm esc}).
\tag{9}
\]

若 alternate-source Hall/Rado 分支为 \(r=r_\ell^{\rm esc}\) 提供了满足 (3) 的独立槽，
则

\[
\boxed{
c<2^{r_\ell^{\rm esc}}
\Longrightarrow
\text{当前稳定子商目标被 Type II 填满}.
}
\tag{10}
\]

若匹配出的独立方向只有 \(r'<r_\ell^{\rm esc}\)，则输出
\[
\mathrm{ESCAPE\_RANK\_MATCHING\_DEFICIT},
\tag{11}
\]
并把剩余 rank 送回 Hall/Rado 对偶；不能用已匹配的 \(r'\) 个方向冒充完整需求。

若某些方向在最终稳定子中被吸收，实际 \(\rho(\bar u_i)=0\)，则它们的
\(\kappa_i=0\)，从 (8) 的 \(2^r\) 计数中删除；吸收方向只能进入更小的稳定子商或
quotient Fourier。

## 5. 证明

式 (5) 由 (3) 的线性独立性和二点指数的差分 \(\{-1,0,1\}\) 直接得到。若
\(\bar P\bar R\) 仍缺少一个商元素，则 (6) 给出 \(2^r=|\bar R|\le c\)，与
\(c<2^r\) 矛盾，故得到 (8)。E1--E5 通过时，商群中的目标命中由同一组真实源块
回译为原参数的 Type II 证书；任一门失败都只能保留 lift obstruction。若独立匹配
不足，剩余需求维数没有被支付，得到 (11)；稳定子吸收时二点像退化为单位元，
不应计入乘积大小。证毕。

## 6. 边界例子

### 一孔终端

若 \(c=1\)、\(r=1\)，且 \(\rho(\bar u_1)\ne0\)，则
\(\bar R=\{1,\bar u_1\}\) 有两个元素，\(2>1\)，式 (8) 立即填满目标。

### 两方向填三孔

若 \(c=3\)、\(r=2\)，两个 escaped source 在 \(V_\ell\) 中独立，则
\(|\bar R|=4>3\)，直接命中；不需要把两个高度相乘。

### 等号不闭合

若 \(c=4\)、\(r=2\)，则 \(|\bar R|=4=c\)。补集恒等式只给出可能的
HOLE_LOCKED 平移，不能推出命中；此时必须检查稳定子、Fourier 或第三个合法源方向。

## 7. 研究边界

本卡完成了“独立 escaped rank \(\to\) 目标缺口填洞”的精确 \(2^r\) 容量映射，并
闭合了一孔以及 \(c<2^r\) 的 Type II 子族。它仍未证明一般状态的逃逸 rank 可以
匹配出独立整数 source，亦未处理 \(c\ge2^r\) 的 HOLE_LOCKED/多 primary 分支。
后续应优先证明 alternate 菜单完备性，或把等号缺口转成新的 independent rank/严格
商 relay。
