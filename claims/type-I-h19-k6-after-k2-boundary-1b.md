---
kind: claim
claim_id: type-I-h19-k6-after-k2-boundary-1b
title: H19 k=2子群边界后的k=6偶源释放
statement: H19十亿p=25 mod48残余中，固定k=2的119个模7子群障碍逐点枚举k=6,q=23的全部混合因子g|6n、g<=n、g=-1 mod23后，48个有偶数源严格Type I证书，71个仍遗漏。故k=2再k=6在该243点同余子类中终止172个，并留下精确的71点双尺度边界。
claim_status: computationally_reproduced
topics:
- type-I
- descent
- even-source
- external-source
- factorization
- finite-audit
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-certificate-context
- paper: ventas2026
  locator: Theorem 2.3
  role: external-source-context
visibility: public
last_checked: '2026-07-27'
---

# H19 k=2子群边界后的k=6偶源释放

[k=2 模七二次剩余因子边界](type-I-k2-mod7-even-source-factor.md)在 H19 十亿
$p\equiv25\pmod{48}$ 子类中留下 $119$ 个固定尺度障碍。对每个点令

$$
n=\frac{23p+1}{24},\qquad k=6,\qquad q=23.
$$

此时 $n$ 仍为偶数。完整枚举

$$
g\mid6n,\qquad g\le n,\qquad g\equiv-1\pmod{23},
$$

并按混合因子外部源定理重建证书，得到

$$
119=48_{k=6\text{ 偶源终止}}+71_{k=6\text{ 遗漏}}.
$$

因此该同余子类的两尺度有限菜单已经终止 $124+48=172$ 个点，剩余 $71$ 个是同时避开
固定 $k=2$ 与 $k=6$ 全部混合因子的明确边界。该结果只排除两个固定尺度，不能推广为对
所有外部尺度或所有核心素数的否定。

可复现命令：

~~~bash
python3 reproductions/type_i_h19_k6_after_k2_boundary.py
python3 -m unittest tests/test_type_i_h19_k6_after_k2_boundary.py -q
~~~
