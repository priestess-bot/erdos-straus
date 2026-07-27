---
kind: claim
claim_id: type-II-tail-shifted-quadratic-four-layer-structural-closure-300m
title: 三亿平移平方尾压力集的四层结构闭合
statement: 对三亿范围89条零偏移遗漏，79条在最小偏移由对称盒饱和或逆配对奇偶性命中；剩余10条中8条在后续s<=202521偏移由同两层命中；余下26034649与212973049均由双侧有界接口完成条件闭合。因此89条均有不依赖自由尾因子枚举的显式结构递降证书。
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

# 三亿平移平方尾压力集的四层结构闭合

在[三层结构边界](type-II-tail-shifted-quadratic-layered-structural-boundary-300m.md)中，
仅 $p=212{,}973{,}049$ 未被前三层选择器强制。加入受限双侧接口完成条件后，89条压力射线
按优先级获得精确闭合：

$$
89=79_{\rm 最小偏移饱和/奇偶性}
+8_{\rm 后续\,s\le202{,}521\,结构}
+2_{\rm 双侧接口完成}. \tag{1}
$$

最后两条为

$$
26{,}034{,}649,\qquad212{,}973{,}049.
$$

后者的最小偏移状态有

$$
k=103{,}788=18\cdot186\cdot31,
$$

$$
N=2{,}917{,}432=59\cdot56\cdot883,
$$

并取

$$
\alpha=18,\quad r=186,\quad\beta=31,
\qquad
\gamma=59,\quad z=56,\quad\delta=883.
$$

于是接口 $b=\beta\delta=27{,}373$ 仅含两个跨侧素数，且

$$
4\cdot186\cdot56\cdot27{,}373^2+1
=5{,}489{,}370{,}311\cdot5{,}687. \tag{2}
$$

故

$$
a=\alpha\gamma=1{,}062,\qquad b=27{,}373,\qquad a+b=5\cdot5{,}687.
$$

这重构了已验证的归一化尾因子 $11{,}747{,}623{,}104$ 和严格递降缺口
$8{,}262{,}791$。

对10条最小偏移的前三层遗漏，限定 $\beta,\delta$ 各为 $1$ 或一个素数幂的完整枚举命中9条；
其中与后续偏移层互补、实际用于 (1) 的正是上述两条。另一个没有命中的
$6{,}294{,}649$ 已在后续偏移层闭合。

这仍是 $p\le300{,}000{,}000$ 的有限结构闭合，不是固定接口数或固定偏移上界的全称定理。
它把下一步研究目标收紧为：证明这种至多双素数幂接口完成、或其有限可控扩展，能由外层偏移
系统地强制出现。

可复现命令：

~~~bash
python3 reproductions/type_ii_tail_shifted_quadratic_two_sided_completion.py
python3 -m unittest tests/test_type_ii_tail_shifted_quadratic_four_layer_structural_closure_300m.py -q
~~~
