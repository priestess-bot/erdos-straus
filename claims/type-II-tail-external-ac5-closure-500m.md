---
kind: claim
claim_id: type-II-tail-external-ac5-closure-500m
title: 五亿核心素数的双尾、平方因子外源递降或半径五 AC 闭合
statement: 对所有 p<=500000000、p=1 mod24 的3292848个核心素数，3291131个有普通 Type II 双尾严格递降；其1717个遗漏中1593个有完整平方因子外源严格递降；余下124个全有 max(A,C)<=5 的直接 AC Type II 证书，最小半径分布为1:52、2:60、3:8、4:3、5:1。半径4唯一遗漏为p=373949689，故半径5在这个固定压力集内必要。因此该范围有3292848=3291131+1593+124的严格递降或半径五短证书闭合。
claim_status: computationally_reproduced
topics:
- type-II
- type-I
- descent
- ac-rays
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

# 五亿核心素数的双尾、平方因子外源递降或半径五 AC 闭合

对全部

\[
p\le5\cdot10^8,\qquad p\equiv1\pmod{24}
\]

的核心素数，按以下顺序做精确分流：

1. 普通 Type II 双尾严格递降；
2. 对双尾遗漏枚举完整平方因子外源严格递降；
3. 对三层外源共同遗漏枚举 \(\max(A,C)\le5\)、\(K\) 不设界的直接 Type II
   \(AC\) 射线。

前两层的输入结果给出 \(1{,}717\) 个双尾遗漏，其中 \(1{,}593\) 个有平方因子
外源严格递降，剩余 \(124\) 个由第三层逐项因子分解

\[
p+4A^2C
\]

并恢复证书。得到不交分流

\[
3{,}292{,}848
=3{,}291{,}131_{\text{双尾严格递降}}
+1{,}593_{\text{平方因子外源严格递降}}
+124_{\mathrm{AC}_5}. \tag{1}
\]

直接 \(AC\) 补点的最小半径分布为

| 最小 \(\max(A,C)\) | 点数 |
| ---: | ---: |
| 1 | 52 |
| 2 | 60 |
| 3 | 8 |
| 4 | 3 |
| 5 | 1 |

半径 \(4\) 的完整扫描只留下

\[
p=373{,}949{,}689.
\]

它在半径 \(5\) 的首次见证为

\[
(A,C,K,h,m,d)=(4,5,1955,156399,2391,80), \tag{2}
\]

并且

\[
p+4A^2C=373{,}950{,}009=156399\cdot2391.
\]

所以半径 \(5\) 是该固定的 124 点压力集上使第三分支全覆盖的最小整数界。

这不是全称递降证明：第三层只是直接 Type II 证书，且整个分流仍依赖有限范围内对目标
因子结构的枚举。它的作用是把“平方因子外源共同失败”与“真实短证书压力”区分开：在
五亿范围内，前者全部仍有极小的直接 \(AC\) 证书。

可复现命令：

~~~bash
python3 reproductions/type_ii_tail_external_ac2_closure.py \
  --input reproductions/type-ii-tail-deflation-external-boundary-500m-results.json \
  --ac-bound 5 \
  --output reproductions/type-ii-tail-external-ac5-closure-500m-results.json
python3 -m unittest tests/test_type_ii_tail_external_ac5_closure_500m.py -q
~~~
