---
kind: claim
claim_id: type-II-h19-second-layer-1b-boundary
title: H19 二层严格递降在十亿处的距离尺度边界
statement: 在 p<=10^9 的664个 H19 残余中，完整平方因子外部源严格递降命中660个；旧三点由c=7,3,3的偶源递降闭合，而新点640775689在c<=9999仍未命中、在c=34091首次命中。故十亿范围有纯严格递降闭合664=660+4，但其距离必须状态依赖；该点也有s=45、h=359的纯新单因子 Type II 证书。
claim_status: computationally_reproduced
topics:
- type-II
- type-I
- descent
- even-source
- external-source
- new-factor
- boundary
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: certificate-and-descent-context
visibility: public
last_checked: '2026-07-25'
---

# H19 二层严格递降在十亿处的距离尺度边界

十亿 H19 残余剖面共有 664 点。完整平方因子外部源递降给出 660 条严格递降，遗漏为

\[
35{,}840{,}809,\quad132{,}285{,}169,\quad141{,}326{,}089,\quad640{,}775{,}689. \tag{1}
\]

前三点分别由奇距离偶源 \(c=7,3,3\) 严格提升。第四点在完整奇距离偶源扇
\[
c\in\{1,3,\ldots,9999\}
\]
中仍未命中，却在 \(c=34091\) 首次命中。因此五亿范围的二层纯递降等式能推广为
十亿范围的有限闭合，却不能推广为固定小距离结论。

另一方面，第四点有完全独立的纯新单因子 Type II 证书：

\[
s=45=3^2\cdot5,\qquad h=359=4\cdot3\cdot5\cdot6-1,\qquad
359\mid640{,}775{,}689+4\cdot45. \tag{2}
\]

第四点的偶源首释放给出十亿审计的精确纯递降闭合

\[
664=660+4. \tag{3}
\]

四个偶源距离依次为 \(7,3,3,34091\)。另一方面，短证书分支也给出相同计数的独立混合
闭合。

式 (3) 是有限审计证据，不是全称证明。新点同时表明：将偶源距离截断到 9999 仍不足以
替代状态依赖分支；下一条理论引理必须从共同失败状态导出**状态依赖**的偶源距离，或直接
导出受限的新因子证书。首释放的逐距离复现见
[第四压力点的偶源首释放](type-II-h19-fourth-even-source-release-boundary.md)。
将源端兼容性与平方尾残数拆开后，可见 \(c\le34091\) 中已有 33 条兼容射线，却仅首释放
射线命中平方尾目标；因此当前瓶颈是后者，见
[第四压力点的源射线与平方尾分离](type-II-h19-fourth-even-source-tail-profile.md)。
其余 32 条失败再精确分为 23 条子群--字符型与 9 条有限积集型，故后续必须分别处理
跨模角色兼容性和受限指数覆盖，见
[第四压力点平方尾的子群--积集分流](type-II-h19-fourth-even-source-subgroup-profile.md)。
前一类在当前点全部已有显式二次角色分离，因此可先从 Legendre/Jacobi 条件的兼容性而非
高阶角色入手，见
[第四压力点平方尾障碍的二次角色化](type-II-h19-fourth-even-source-quadratic-character-profile.md)。

重建依赖以下已有审计：

~~~bash
python3 reproductions/type_ii_source_free_transition_profile.py \
  --limit 1000000000 --base-shift-bound 19 --shift-cap 200 \
  --output reproductions/type-ii-source-free-transition-h19-1b-results.json
python3 reproductions/type_ii_h19_targeted_quadratic_descent.py \
  --input reproductions/type-ii-source-free-transition-h19-1b-results.json \
  --output reproductions/type-ii-h19-targeted-quadratic-descent-1b-results.json
python3 reproductions/type_ii_h19_adaptive_even_source_descent.py \
  --input reproductions/type-ii-h19-targeted-quadratic-descent-1b-results.json \
  --distance-cap 99999 \
  --output reproductions/type-ii-h19-adaptive-even-source-descent-1b-c99999-results.json
python3 reproductions/type_ii_h19_fourth_even_source_release_boundary.py
python3 reproductions/type_ii_minimal_collision_support.py \
  --input reproductions/type-ii-source-free-transition-h19-1b-results.json \
  --output reproductions/type-ii-minimal-collision-support-h19-1b-results.json
python3 reproductions/type_ii_h19_hybrid_short_or_descent.py \
  --profile reproductions/type-ii-minimal-collision-support-h19-1b-results.json \
  --descent reproductions/type-ii-h19-targeted-quadratic-descent-1b-results.json \
  --output reproductions/type-ii-h19-hybrid-short-or-descent-1b-results.json
~~~
