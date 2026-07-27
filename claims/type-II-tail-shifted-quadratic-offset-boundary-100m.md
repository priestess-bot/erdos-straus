---
kind: claim
claim_id: type-II-tail-shifted-quadratic-offset-boundary-100m
title: 亿级平移平方外源的残差偏移选择器边界
statement: 在 p<=10^8 的500个普通双尾遗漏中，459个有零偏移完整平方因子外源递降；其余41个中39个在残差偏移 s<=241 的完整固定偏移族中有严格递降，p=878089 的最小可用偏移为3705，p=5478169 的最小可用偏移为7161。因此 s<=7161 在此有限压力集上闭合全部41点。
claim_status: computationally_reproduced
topics:
- type-I
- type-II
- descent
- external-source
- tail-deflation
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--3
  role: certificate-and-lift-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-prime-shape-context
visibility: public
last_checked: '2026-07-27'
---

# 亿级平移平方外源的残差偏移选择器边界

令 $s$ 是平移平方外源中的残差偏移。对固定 $s$，兼容参数不应以任意的 $k$ 截断：

\[
p=4kd+s,\qquad s\mid(4k-1),\qquad
k\mid\frac{p-s}{4}. \tag{1}
\]

所以固定 $s$ 时，枚举 $((p-s)/4)$ 的全部因子 $k$，再枚举完整平方尾因子，就是该
偏移射线的完整有限审计。等价的固定源距离因子坐标及其双射证明见
[平移平方外源射线的源距离因子参数化](shifted-quadratic-source-distance-parametrization.md)。

在一亿范围的 500 个普通双尾遗漏中，459 个已由 $s=1$ 的完整平方因子外源递降处理。
对余下 41 点，按正偏移 $s\equiv1\pmod4$ 递增执行式 (1) 的完整枚举，得到

\[
41=39_{s\le241}+1_{s=3705}+1_{s=7161}. \tag{2}
\]

两个后续边界是精确的：在整个较小偏移范围内没有兼容平方尾见证，而首次命中分别为

\[
\begin{array}{c|c|c|c}
p&s&k&\text{源分母}\\ \hline
878{,}089&3{,}705&54{,}649&878{,}085\\
5{,}478{,}169&7{,}161&341{,}938&5{,}478{,}165
\end{array}
\]

这比仅报告 $k\le340{,}574$ 的命中盒更有信息：绝大多数压力点由极小残差偏移释放，
但两个点严格否定了“$s\le241$ 已足够”的候选选择器。它没有证明 $s\le7161$ 对所有
核心素数都成立；下一步的理论问题是解释共同尾失败为何应强制某个小偏移射线出现所需的
平方尾除子。

可复现命令：

~~~bash
python3 reproductions/type_ii_tail_shifted_quadratic_offset_profile.py \
  --input reproductions/type-ii-tail-deflation-external-boundary-100m-results.json \
  --offset-bound 7161 \
  --output reproductions/type-ii-tail-shifted-quadratic-offset-profile-100m-results.json
python3 -m unittest tests/test_type_ii_tail_shifted_quadratic_offset_profile_100m.py -q
~~~
