---
kind: claim
claim_id: type-I-h19-linear-e-tail-deflation-hybrid-1b
title: H19 全盒线性反向二尾或 Type II 双尾的严格递降闭合
statement: 对存储的664个十亿H19源自由残余，固定m<=127的全Type I正规形盒中有622点存在E|4K的严格最大尾反向边；其余42点全部有经精确重建的Type II p-1双尾严格递降，最大缺口119。因此该固定剖面有664=622+42的纯严格递降闭合，无未闭合点。
claim_status: computationally_reproduced
topics:
- type-I
- type-II
- descent
- reverse-lift
- tail-deflation
- h19
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: certificate-and-descent-context
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization-context
visibility: public
last_checked: '2026-07-27'
---

# H19 全盒线性反向二尾或 Type II 双尾的严格递降闭合

[无B上界的线性尾边界](type-I-h19-reverse-two-tail-linear-e-full-b-boundary-1b.md) 把 H19
残余精确分为 $622$ 个全盒线性反向二尾状态和 $42$ 个必须使用平方尾的状态。后者并不需要
作为新的递归难点：逐一重建普通 Type II 的 $p-1$ 双尾抽缩，42点全部存在严格源。

两条分支逐点不交，给出

$$
664=622_{\text{Type I }E\mid4K\text{ reverse descent}}
+42_{\text{Type II tail deflation}}.
$$

第二分支的最大最小缺口为 $119$；每条源、目标的三项单位分数恒等式均以精确有理数重新
验证。因此这不是“直接证书备用”，而是整个固定 H19 剖面的严格递降闭合。

该结论不能升级为全称递降定理：它没有证明任意核心素数落在两条分支之一，也没有控制
缺口或源侧状态随 $p$ 的增长。它的研究价值在于：当前多素因子平方尾状态可被另一条
独立的 Type II 递降机制完全接住，故下一条统一引理应研究两分支的强制析取，而不是仅
试图线性化每一张 Type I 证书。

可复现命令：

~~~bash
python3 reproductions/type_i_h19_linear_e_tail_deflation_hybrid_closure.py \
  --linear reproductions/type-i-h19-reverse-two-tail-linear-e-full-b-boundary-1b-results.json \
  --tail reproductions/type-ii-h19-tail-deflation-short-closure-1b-results.json \
  --output reproductions/type-i-h19-linear-e-tail-deflation-hybrid-1b-results.json
python3 -m unittest tests/test_type_i_h19_linear_e_tail_deflation_hybrid_closure.py -q
~~~
