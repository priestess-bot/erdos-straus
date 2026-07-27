---
kind: claim
claim_id: type-II-tail-shifted-quadratic-square-necessity-200m
title: 两亿平移平方外源压力点的平方尾必要性边界
statement: 在两亿范围的65个零偏移外源遗漏中，按每点最小残差偏移并完整枚举该偏移的所有可行 k 后，40点仍有普通尾因子 f|L，25点没有任何 f|L 的见证而必须使用真平方尾因子 f|L^2、f不整除L。故不能把平移平方外源统一简化为普通因子尾。
claim_status: computationally_reproduced
topics:
- type-I
- descent
- external-source
- factorization
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--3
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 两亿平移平方外源压力点的平方尾必要性边界

平移平方外源的正规形要求 $f\mid L^2$。一个诱人的简化是只允许普通因子
$f\mid L$。为检验该简化是否保持两亿闭合，对 65 个压力点逐一固定其最小可用偏移 $s$，
枚举 $k\mid(p-s)/4$ 的全部兼容 $k$，再枚举每个 $L^2$ 的全部合格尾因子。

结果为

$$
65=40_{\exists f\mid L}+25_{\forall f\not\mid L}. \tag{1}
$$

后 25 点在这个最小偏移上仍有完整平方尾见证，却没有任意普通尾因子见证。它们包括

$$
878{,}089,\qquad171{,}292{,}489,\qquad192{,}235{,}129.
$$

例如 $p=171{,}292{,}489$ 的最小偏移 $s=48{,}265$ 下只有一个兼容 $k$，但有三条完整
平方尾见证，全部满足 $f\nmid L$。因此把 $f\mid L^2$ 缩成 $f\mid L$ 会在该精确射线上
完全失去递降。

结论只针对每点的最小偏移：在更大偏移上可能存在普通尾因子，因而这不是“该素数在所有
射线上都需要平方”的声明。它足以说明后续理论选择器必须控制平方因子指数，不能只研究
线性因子残数。

进一步按最少的“超出 $L$ 的指数总数”分类这 25 点，分布为

$$
1:17,\qquad2:3,\qquad3:4,\qquad5:1. \tag{2}
$$

因此单个指数升级只能处理其中17点；其余8点至少需要两个额外指数，
$p=68{,}822{,}329$ 的最小见证甚至需要五个。这排除了“普通因子乘一个额外素因子”
作为该最小偏移压力集的全覆盖选择器。

按命中因子包含的不同素因子数最小化，25 点的分布又为

$$
2:5,\qquad3:13,\qquad4:7. \tag{3}
$$

因此 7 点不存在一、二或三素因子尾，最小命中已需要四种不同素因子；其中包括
$p=68{,}822{,}329$ 与 $171{,}292{,}489$。这独立排除了有界至三素因子支持的内层选择器。

可复现命令：

~~~bash
python3 reproductions/type_ii_tail_shifted_quadratic_square_necessity.py \
  --input reproductions/type-ii-tail-shifted-quadratic-offset-profile-200m-results.json \
  --output reproductions/type-ii-tail-shifted-quadratic-square-necessity-200m-results.json
python3 -m unittest tests/test_type_ii_tail_shifted_quadratic_square_necessity_200m.py -q
~~~
