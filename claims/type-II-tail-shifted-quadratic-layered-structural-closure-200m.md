---
kind: claim
claim_id: type-II-tail-shifted-quadratic-layered-structural-closure-200m
title: 两亿平移平方尾压力集的三层结构闭合
statement: 对两亿范围65条零偏移遗漏，57条在最小偏移即由对称盒饱和或逆配对奇偶性充分条件闭合；其余8条中，7条在后续s<=202521偏移上由同两种条件闭合，最后p=26034649由N=uvw与u^2v+4=0 mod t的源因子完成条件闭合。因此这65条全部具有由显式结构判据构造并验证的严格递降证书。
claim_status: computationally_reproduced
topics:
- type-I
- descent
- external-source
- divisor-residues
- factorization
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--3
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 两亿平移平方尾压力集的三层结构闭合

平移平方外源的完整尾等价于普通除子反向对。这里使用三种彼此可验证的充分条件：

1. 对称有符号指数盒填满实际生成子群；
2. 对称盒补集的逆配对奇偶性强制 $-1$ 在盒内；
3. 归一化源的三块分解 $N=uvw$ 满足 $u^2v+4\equiv0\pmod t$。

在两亿范围65条零偏移外源遗漏的最小偏移审计中，前两层已经直接命中57条。余下8条中，
对7条从最小偏移之后精确枚举至 $s\le202{,}521$，仍由前两层在更大偏移上命中：其中6条
为子群饱和，1条为逆配对奇偶性。最后一条为

$$
p=26{,}034{,}649,\qquad s=9,\qquad k=421,\qquad t=187.
$$

其归一化源分解为

$$
N=2{,}891{,}021=7\cdot19\cdot21{,}737,
$$

且

$$
7^2\cdot19+4=935=5\cdot187.
$$

所以源因子完成条件取

$$
u=7,\qquad v=19,\qquad w=21{,}737,
$$

给出反向普通除子对

$$
a=uk=2{,}947,\qquad b=w=21{,}737,\qquad a+b=132\cdot187.
$$

对应的归一化尾因子为 $165{,}011{,}371$，并已独立构造为源距离15,460的严格递降证书。

因此在此有限压力集上可按优先级写成精确的互斥闭合

$$
65=57_{\rm 最小偏移结构}+7_{\rm 后续偏移结构}+1_{\rm 源因子完成}. \tag{1}
$$

这是一项对指定两亿审计盒的结构化解释，不是对所有素数或所有偏移的统一定理。它的意义在于
把先前“枚举到某个尾因子”的65条闭合，替换为三类可证明、可独立检验的选择机制；下一步的
理论问题是将这些机制之一推广为无界偏移或无界因子分解的强制规律。

可复现命令：

~~~bash
python3 reproductions/type_ii_tail_shifted_quadratic_opposite_pair_profile.py
python3 reproductions/type_ii_tail_shifted_quadratic_outer_structural_profile.py
python3 reproductions/type_ii_tail_shifted_quadratic_source_factor_completion.py
python3 -m unittest tests/test_type_ii_tail_shifted_quadratic_layered_structural_closure_200m.py -q
~~~
