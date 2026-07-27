---
kind: claim
claim_id: h19-k23-global-min-nonbase-factor-boundary-2097152
title: H19-k23 全局一次幂递降的最小非基底素因子边界
statement: 在 H19-k23 二百万层全局重写子样本的5,128条最终一次幂 Type II 递降中，逐项枚举有效尾的全部规范基底部分后，3,685条可用 x=(p+m)/4 的最小非基底素因子构成 d=b*ell，另有1,443条不能。因此跨尾一次幂选择器不能简化为“取最小非基底素因子”的确定性规则。
claim_status: computationally_reproduced
topics:
- type-II
- descent
- factor-selection
- least-prime-factor
- global-tail-menu
- one-factor
- computation
- h19
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-criterion
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 全局一次幂递降的最小非基底素因子边界

对 [一次幂后移闭合](h19-k23-global-first-power-tail-reroute-2097152.md) 的每条最终记录，
固定其已验证的全局尾 \(m\)、首分母

\[
x=\frac{p+m}{4},
\]

以及规范基底 \(\mathcal B_m\)。令 \(\ell_{\min}\) 为 \(x\) 的最小非基底素因子。审计不只
比较已选证书的素因子，而是完整枚举所有

\[
b\mid x^2,\qquad
\operatorname{supp}(b)\subseteq\mathcal B_m, \tag{1}
\]

并检查

\[
d=b\ell_{\min}\le x,\qquad d\equiv-x\pmod m. \tag{2}
\]

精确结果是

\[
5\,128=3\,685_{\ell_{\min}\text{ 可用}}+
1\,443_{\ell_{\min}\text{ 不可用}}. \tag{3}
\]

这 1,443 条并非没有一次幂证书：它们已经由同尾或后移尾的某个**非最小**新素因子闭合。
因此失败归因于“最小素因子”这个额外选择规则，而不是 Type II 证书、严格递降或一次幂
跨尾选择器的失败。

结论只作用于这份有限重写子样本和其已选终态尾。它不排除在不同尾上最小素因子可用，
也不证明任意规模的最小素因子失败；但足以排除把当前开放选择器归约为一个纯粹的最小
素因子估计。正向论证必须控制因子**残数角色**或跨尾关系，而不能只控制最小素因子的大小。

可复现命令：

~~~bash
python3 reproductions/h19_k23_global_min_nonbase_factor_boundary.py \
  --profile-input reproductions/h19-k23-global-one-prime-power-descent-profile-2097152.json \
  --reroute-input reproductions/h19-k23-global-first-power-tail-reroute-2097152.json \
  --output reproductions/h19-k23-global-min-nonbase-factor-boundary-2097152.json
python3 -m unittest tests/test_h19_k23_global_min_nonbase_factor_boundary.py -q
~~~
