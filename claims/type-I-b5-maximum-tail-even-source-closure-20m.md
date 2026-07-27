---
kind: claim
claim_id: type-I-b5-maximum-tail-even-source-closure-20m
title: 两千万核心素数的B不大于5最大尾偶源闭合
statement: 对所有p≤20000017的158595个核心素数，完整枚举自然Type I缺口、B≤4正规形和最大尾严格偶源反向边；158594个直接命中，唯一遗漏仍为21169。该点的完整正规形审计证明其最小偶源参数为B=5。因此在此范围每个核心素数均有B≤5的最大尾保留两项严格偶源Type I反向边，且B≤4仅在21169失败。
claim_status: computationally_reproduced
topics:
- type-I
- normal-form
- descent
- even-source
- overflow
- finite-audit
- closure
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 两千万核心素数的 B 不大于 5 最大尾偶源闭合

对每个

\[
p\le20{,}000{,}017,\qquad p\equiv1\pmod{24},
\]

穷尽每个自然 Type I 缺口、所有 \(B\le4\) 正规形以及 \(pK\) 最大尾的严格偶源反向桥。结果为

\[
158595=158594_{B\le4}+1_{p=21169}. \tag{1}
\]

该一千万之外新增的 75,708 个核心素数没有产生新的 \(B\le4\) 遗漏；唯一遗漏仍为 \(21169\)。
它的[完整正规形偶源边界](type-I-full-normal-even-source-boundary-21169.md)已证明最小可行参数恰为
\(B=5\)，故得到

\[
\boxed{\text{该两千万前缀的每个核心素数均有 }B\le5\text{ 的最大尾严格偶源 Type I 反向边。}} \tag{2}
\]

这是目前比“存在 Type I 短证书”更强的有限信息：每个命中都同时给出了严格更小的偶源和可复核
的三项分解。它仍不能替代全局证明，因为没有控制更大范围的最小 \(B\)，也没有解释为何唯一异常由
\(B=5\) 释放。

可复现命令：

~~~bash
python3 reproductions/type_i_b4_prefix_profile_10m.py \
  --limit 20000017 \
  --output reproductions/type-i-b4-prefix-profile-20m-results.json
python3 -m unittest tests/test_type_i_b4_prefix_profile_20m.py -q
~~~
