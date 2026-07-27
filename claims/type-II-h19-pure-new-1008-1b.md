---
kind: claim
claim_id: type-II-h19-pure-new-1008-1b
title: H19 十亿新因子状态在移位一千零八内纯新闭合
statement: 对p<=10^9的541个H19新因子状态，从各自首次无旧私有因子移位起完整枚举至s<=1008的规范 Type II 单新因子证书，541个全部有碰撞重数0的纯新证书。最大首次纯新移位为1008，唯一保持者p=178400041的见证为s=1008、h=9743、s=12^2*7。因此这个有限状态集满足纯新因子选择器的s<=1008版本；它不证明任何统一移位界或全称选择器。
claim_status: computationally_reproduced
topics:
- type-II
- multishift
- factorization
- new-factor
- collision-factor
- release-depth
- finite-audit
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-certificate-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-27'
---

# H19 十亿新因子状态在移位一千零八内纯新闭合

沿用 `type-II-h19-zero-one-collision-500-1b` 的 H19 状态定义。对全部

\[
541
\]

个存储的 \(p\le10^9\) 新因子状态，从该点首次无旧私有因子的移位起完整枚举所有
规范 Type II 单新因子因子，直到

\[
s\le1008. \tag{1}
\]

这次只接受不含任何 H19 碰撞因子的见证，即

\[
h=q,\qquad q\notin\mathcal O_p,\qquad
q\mid p+4a^2c,\qquad q\equiv-1\pmod{4ac},\qquad s=a^2c. \tag{2}
\]

每个 \(q\) 由完整因子分解选出后，都重新恢复并核验 Type II 证书。

## 结果

所有 \(541\) 个状态均在 (1) 内命中，最小碰撞重数分布为

\[
0:541. \tag{3}
\]

最大首次纯新移位唯一出现在

\[
p=178{,}400{,}041,\qquad s=1008=12^2\cdot7,\qquad h=q=9743. \tag{4}
\]

对应的完整因子对为

\[
p+4s=178{,}404{,}073=9743\cdot18311,
\]

且 \(9743=4\cdot12\cdot7\cdot29-1\)，故 \(K=29\)，恢复的 Type II 证书有
缺口 \(18311\) 和除子 \(1008\)。

此前在 \(s\le500\) 尚需一次碰撞的另一个点

\[
p=751{,}064{,}161
\]

已在 \(s=529=23^2\) 纯新释放，取 \(h=539947\)、\(K=5869\)。而较浅窗口中唯一的
两碰撞点 \(372{,}271{,}201\) 已在 \(s=484\) 纯新释放。故这三条延迟释放共同给出
从 \(s\le200\) 的正碰撞边界到 (3) 的完整有限过渡。

## 边界

这不是“纯新因子总在 \(1008\) 内出现”的猜想或定理。固定有限移位扇仍有条件性逃逸，
并且本结论只针对已有的 H19 状态、十亿范围和按来源定义的“新”。它的价值在于删除了
该有限样本中的碰撞积困难：若要解释这一族的有限数据，下一步可先研究纯新因子释放深度，
而不必把碰撞积视为永久必需。

可复现命令：

~~~bash
python3 reproductions/type_ii_minimal_collision_support.py \
  --input reproductions/type-ii-source-free-transition-h19-1b-results.json \
  --shift-cap 1008 \
  --output reproductions/type-ii-minimal-collision-support-h19-1b-s1008-results.json
python3 -m unittest tests/test_type_ii_minimal_collision_support.py -q
~~~
