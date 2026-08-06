---
kind: claim
claim_id: type-II-low-modulus-pseudo-hit-complete-dispatch
title: Type II 低模数伪命中的核—算术—Fourier 完整分派
statement: 设 P 是模数 M_*=4D_* 的带来源源指数盒，K=ker(U(M_*)->U(M'))、M'=4D' 且 D'|D_*。若目标 -1 不在 P 但在商积集 pi(P) 中，则核稳定子饱和不可能成立；源盒核判据必给出 KERNEL_SOURCE_ANNIHILATOR 或 KERNEL_BOX_FOURIER。若商命中的带来源因子束 h 通过单纤维算术门，则同模数/严格降模/raw 三分给出 Type II 或严格较小模数 Type II；三类全空时 raw Fourier 桥给出 SOURCE_RELATION_FOURIER 或 ARITHMETIC_FOURIER_LIFT_OBSTRUCTED。故低模数伪命中没有未分类的“商命中”出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-stabilizer-kernel-quotient-descent-trichotomy
  - type-II-stabilizer-kernel-source-box-lattice-criterion
  - type-II-stabilizer-kernel-failure-dual-certificate
  - type-II-hall-fiber-arithmetic-closure-trichotomy
  - type-II-arithmetic-empty-raw-fourier-bridge
  - type-II-hall-matching-fiber-realization-gate
topics:
  - type-II
  - pseudo-hit
  - lower-modulus
  - stabilizer
  - Fourier
  - arithmetic-lift
  - source-switch
  - descent
sources:
  - claim: type-II-stabilizer-kernel-quotient-descent-trichotomy
    role: quotient-pseudo-hit-setting
  - claim: type-II-stabilizer-kernel-source-box-lattice-criterion
    role: kernel-saturation-test
  - claim: type-II-stabilizer-kernel-failure-dual-certificate
    role: kernel-failure-Fourier-output
  - claim: type-II-hall-fiber-arithmetic-closure-trichotomy
    role: labelled-arithmetic-trichotomy
  - claim: type-II-arithmetic-empty-raw-fourier-bridge
    role: raw-empty-Fourier-refinement
visibility: public
last_checked: '2026-08-05'
---

# Type II 低模数伪命中的核—算术—Fourier 完整分派

## 1. 伪命中输入

令
\[
M_*=4D_*,\qquad M'=4D',\qquad D'\mid D_*,
\]
并令
\[
\pi:U(M_*)\longrightarrow \pi(U(M')),\qquad
K=\ker\pi.
\]
设 \(P\subseteq U(M_*)\) 是同一参数纤维中由带来源 q-height 指数盒得到的积集，
目标为 \(t=-1\)，并满足
\[
t\notin P,\qquad \pi(t)\in\pi(P).
\tag{1}
\]
这正是“低模数看似命中、原模数未命中”的伪命中状态。

若商命中由两两互素、带来源标签的因子块实现，记其乘积为 \(h\)，则
\[
h\equiv-1\pmod {M'},\qquad
h_i\mid p+4D'a_i
\]
或相应的严格 source-switch 后继合同。后续算术门只对已经通过该来源门的 \(h\) 运行。

## 2. 核饱和不可能

若 \(K\subseteq\operatorname{Stab}(P)\)，稳定子饱和引理给出
\[
P=\pi^{-1}(\pi(P)).
\]
由 \(\pi(t)\in\pi(P)\) 得 \(t\in P\)，与 (1) 矛盾。因此
\[
K\not\subseteq\operatorname{Stab}(P).
\tag{2}
\]

源指数盒格判据把 (2) 精化为互斥二分：

- \(K\not\subseteq\operatorname{im}\varphi\)：输出
  KERNEL_SOURCE_ANNIHILATOR；
- \(K\subseteq\operatorname{im}\varphi\) 但盒像不被 \(K\) 平移保持：输出
  KERNEL_BOX_FOURIER；
- 目标商伪命中若有非空目标陪集截面，优先用其更强的
  KERNEL_SPLIT_FOURIER。

这些角色均是有限群上的真实对偶对象；它们尚未自动成为整数 Type II，但已经消除
了“只在低模数命中”的无类型状态。

## 3. 商命中因子束的算术三分

对带来源 \(h\) 按当前商参数和严格降模候选运行
\[
\mathscr C_{\mathrm{same}}(h),\qquad
\mathscr C_{\mathrm{lower}}(h),\qquad
\mathscr R_{\mathrm{raw}}(h;p).
\]
则有以下互斥输出：

1. \(\mathscr C_{\mathrm{same}}(h)\ne\varnothing\)：得到同一商模数纤维的合法
   Type II；若其模数小于 \(M_*\)，这是严格降模后继；
2. 同模数为空而 \(\mathscr C_{\mathrm{lower}}(h)\ne\varnothing\)：得到更小参数
   模数的带来源 Type II source-switch；
3. 前两者为空而 raw 集非空：得到 raw Type II 短证书；
4. 三者全空：先由 raw Fourier 桥构造
   RAW_DIVISOR_FOURIER，再按源群指数阶和 SNF 分成
   SOURCE_RELATION_FOURIER 或 ARITHMETIC_FOURIER_LIFT_OBSTRUCTED。

若 \(h\) 没有单纤维实现映射，则不能执行上述 Kneser 算术门，只能输出
UNREALIZED_CROSS_STATE_MATCH，并保留核 Fourier 证书和来源标签。

## 4. 完整性证明

由 (1) 和稳定子饱和引理，(2) 必成立；源盒格判据和核失败对偶二分保证第二节
的两个 Fourier 分支穷尽核失败情况。若存在带来源 \(h\)，算术闭合三分穷尽同模数、
严格降模和 raw 正规形；前三项分别直接给出 Type II 或严格较小模数后继。第四项
包含 raw 集为空，raw Fourier Parseval 恒等式给出严格正的非平凡频率，再由指数和
SNF 完成角色/障碍分派。因此所有伪命中都落入上述有限回执之一。证毕。

## 5. \(p=97\) 的边界实例

取
\[
p=97,\qquad M_*=24,\qquad M'=4,\qquad
P=\{1,11\},\qquad t=23.
\]
有
\[
\pi(P)=\{1,3\},\qquad \pi(t)=3,
\]
但 \(23\notin P\)。核
\[
K=\{1,5,13,17\}
\]
不落在源子群 \(\langle11\rangle=\{1,11\}\)，于是立即得到
KERNEL_SOURCE_ANNIHILATOR；目标陪集截面 \(S_t=\{13\}\) 还给出更强的
KERNEL_SPLIT_FOURIER。若将另一状态的 \(13\) 错误池化为 \(11\cdot13\equiv-1\),
带来源算术门在 \(h=143\) 上三类全空，继而输出 raw Fourier/提升障碍，而不是
Type II 证书。

## 研究边界

该定理闭合了低模数伪命中的状态级分派：商命中、核失败、算术提升和 Fourier
障碍均有明确出口。它仍不证明每个 Fourier 角色都承接到 F/G 容量，也不证明
ARITHMETIC_FOURIER_LIFT_OBSTRUCTED 自动产生严格核心素数下降；全局目标还需要
补上这两个提升箭头。
