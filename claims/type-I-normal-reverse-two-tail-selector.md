---
kind: claim
claim_id: type-I-normal-reverse-two-tail-selector
title: Type I 正规形最大尾的反向二尾选择器
statement: 设Type I正规形x=ABC、m|(4B^2C+1)，令R=(4B^2C+1)/m、H=AR-B、K=BCH，则目标三元组为(ABC,ACH,pK)，且4K=pR+1。保持前两项、将最大项pK反向替换为a而得到严格源4/n，当且仅当存在E|4K^2，使R|(4K-E)、n=(4K-E)/R满足2<=n<p且E|nK；此时a=nK/E。它等价于通用反向因子D=p^2E，因而不必分解巨大目标项pK。
claim_status: established
topics:
- type-I
- normal-form
- descent
- reverse-lift
- factorization
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: divisor-certificate-context
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization-context
visibility: public
last_checked: '2026-07-27'
---

# Type I 正规形最大尾的反向二尾选择器

## 定理

令 $p\equiv1\pmod {24}$ 的 Type I 证书具有正规形

$$
x=ABC,\qquad(A,B)=1,\qquad m\mid4B^2C+1.
$$

置

$$
R=\frac{4B^2C+1}{m},\qquad H=AR-B,\qquad K=BCH. \tag{1}
$$

其目标三元组为

$$
\frac4p=\frac1{ABC}+\frac1{ACH}+\frac1{pK},\qquad4K=pR+1. \tag{2}
$$

保持 (2) 的前两项、以 $a$ 替换最大分母 $pK$，存在严格源

$$
\frac4n=\frac1a+\frac1{ABC}+\frac1{ACH},\qquad2\le n<p, \tag{3}
$$

当且仅当存在正因子

$$
E\mid4K^2 \tag{4}
$$

满足

$$
R\mid4K-E,\qquad n=\frac{4K-E}{R}\in[2,p-1],\qquad E\mid nK. \tag{5}
$$

在此情形 $a=nK/E$。这是由正规形因子直接确定的完整有限选择器；它不需要分解最大
目标分母 $pK$。

## 证明

Type I 正规形恢复式给出第二、三分母分别为 $ACH,pK$。并且

$$
\frac1{ABC}+\frac1{ACH}
=\frac{H+B}{ABCH}
=\frac R K. \tag{6}
$$

由 $p=4ABC-m$ 和 $mR=4B^2C+1$ 得 $4K=pR+1$，故 (2) 成立。于是 (3) 等价于

$$
\frac4n=\frac1a+\frac RK.
$$

令 $E=4K-nR$，清分母得到 $aE=nK$。因此 $E\mid nK$，而

$$
nKR=4K^2-EK,
$$

给出 $E\mid4K^2$。这证明必要性。反过来，由 (5) 和 $a=nK/E$ 有

$$
4aK-nRa=aE=nK,
$$

故恢复 (3)。

对通用反向枚举中的最大目标项 $t=pK$，其因子为

$$
D=4pt-n(4t-p)=p^2(4K-nR)=p^2E. \tag{7}
$$

所以 (4)--(5) 与通用 $D$-枚举完全等价，但剔除了目标素数 $p$ 引入的冗余平方因子。

## 作用与限制

该选择器解释了五亿压力集审计中为何每条首边都替换最大项，并将因子搜索从 $pK$ 降至 $K$。
它仍以目标正规形 $(A,B,C,m)$ 为输入；若没有从源侧或递归状态中选择这一正规形的规则，
它本身不能构成全局递降证明。

`boundary_gap_27_reverse_two_tail_bridge.py` 同时实现 (4)--(5) 与通用 $D$-枚举，并在
边界点的三张 gap-27 证书上逐项交叉核验两者完全一致。
