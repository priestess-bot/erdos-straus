---
kind: claim
claim_id: type-I-p25-fixed-even-scale-boundary
title: p等于25模48类的固定偶源外部尺度边界
statement: 对全体p≡25 mod48，若固定正整数k总满足k|(p-1)/4，则k|6；在k=1,3时源n=((4k-1)p+1)/(4k)恒为奇数，在k=2,6时恒为偶数。故k=2与k=6穷尽该同余类中可统一使用的固定偶源混合因子尺度。
claim_status: established
topics:
- type-I
- descent
- even-source
- external-source
- congruence
- selector-boundary
sources:
- paper: bradford2024
  locator: Proposition 1
  role: external-source-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# p等于25模48类的固定偶源外部尺度边界

写 $p=25+48t$，则

$$
\frac{p-1}{4}=6+12t.
$$

特别地 $73,409\equiv25\pmod{48}$ 都是素数，且相应值为 $18,102$。因此一个对该同余类
所有素数都可用的固定尺度 $k$ 必须整除

$$
\gcd(6,12)=6.
$$

故仅需考察 $k=1,2,3,6$。其外部源为

$$
n_k=\frac{(4k-1)p+1}{4k}.
$$

直接代入 $p=25+48t$ 可得 $n_1,n_3$ 恒为奇数，而 $n_2,n_6$ 恒为偶数。
所以任何适用于全体 $p\equiv25\pmod{48}$ 的固定偶源混合因子菜单，至多包含

$$
k=2,\qquad k=6.
$$

这解释了双尺度审计后余下的71点为何不能由“再加一个统一固定尺度”解决：后续必须选择依赖
于 $p$ 的尺度、切换外源族，或回到内部 Type I 偶桥积集。
