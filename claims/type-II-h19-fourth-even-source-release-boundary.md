---
kind: claim
claim_id: type-II-h19-fourth-even-source-release-boundary
title: H19 十亿第四压力点的偶源首释放距离
statement: 对十亿 H19 平方因子递降的第四遗漏 p=640775689，完整奇距离偶源扇在 c<=34089 无严格递降，而 c=34091 首次给出严格递降到 640741598；见证参数为 k=4699、q=18795、因子1761718、Type I 缺口375。因此十亿有限剖面可以纯递降闭合664=660+4，但该闭合需要状态依赖的距离，不能由固定小距离扇解释。
claim_status: computationally_reproduced
topics:
- type-II
- type-I
- descent
- even-source
- boundary
- finite-audit
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: certificate-and-descent-context
visibility: public
last_checked: '2026-07-25'
---

# H19 十亿第四压力点的偶源首释放距离

完整平方因子外部源递降在十亿 H19 剖面仅遗漏四点。其中前三点分别在距离
\(c=7,3,3\) 已有偶源严格递降。第四点为

\[
p=640{,}775{,}689.
\]

逐个穷尽奇数距离

\[
c=1,3,\ldots,34{,}091
\]

的完整偶源扇，并对每个候选进行精确试除分解和源、目标有理恒等式验证，首个命中恰为

\[
c=34{,}091,\qquad n=p-c=640{,}741{,}598. \tag{1}
\]

其见证为

\[
k=4699,\qquad q=4k-1=18{,}795,\qquad e=1{,}761{,}718. \tag{2}
\]

并给出 Type I 缺口 \(375\) 的提升证书。因此所有 \(c\le34{,}089\) 都失败，而 (1)
是该有限扇的首次严格递降。

这将十亿剖面的纯递降闭合精确写为

\[
664=660+4. \tag{3}
\]

其中四个偶源距离为 \(7,3,3,34091\)。式 (3) 是有限审计结论；特别是它不提供统一的
距离上界。第四点反而说明，将“存在某个状态依赖距离”替换为固定小距离界的证明路线不成立。

## 重建

~~~bash
python3 reproductions/type_ii_h19_fourth_even_source_release_boundary.py
python3 -m unittest tests/test_type_ii_h19_fourth_even_source_release_boundary.py -q
~~~
