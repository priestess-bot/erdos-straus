---
kind: claim
claim_id: type-II-mod-three-recursive-escape-boundary
title: 模三强制因子剥离后出现可采纳的十四移位逃逸分支
statement: 以前十四个规范移位的一私有素因子模型为起点，对每个 616 个安全核心残数 r 和每个 n mod 3 分支，剥离 L_s(3m+j) 中对所有 m 强制的最大三次幂。精确审计得到 1793 个仍使全部射线避靶的分支，且每个安全 r 至少有一个分支；所有这些分支对应的 p 与十四个新线性商构成可采纳的 15 元线性型族。因而在 Dickson/Schinzel 型素数元组猜想下，固定的十四规范移位扇有无穷多个共同失败素数。这个条件性边界排除用单纯递归模三可采纳性推导该固定扇全覆盖的路线。
claim_status: computationally_reproduced
topics:
- type-II
- canonicalization
- multishift
- admissibility
- conditional-boundary
- obstruction
- proof-program
sources:
- paper: chamberland2026
  locator: "Theorem 1"
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-24'
---

# 模三强制因子剥离后出现可采纳的十四移位逃逸分支

## 第二层分支

沿用 `type-II-one-prime-private-cofactor-boundary` 的记号。对安全核心残数
$r\pmod Q$ 和一个分支 $j\in\{0,1,2\}$，令

\[
n=3m+j.
\]

每个第一层商 $L_s(3m+j)$ 是一个仿射线性型。将其系数与常数中共同的最大三次幂
剥离：

\[
L_s(3m+j)=3^{e_{s,j}}P_{s,j}(m), \tag{1}
\]

其中 $P_{s,j}$ 的系数和常数不同时被 3 整除。相应地

\[
p+4s=D_s3^{e_{s,j}}P_{s,j}(m). \tag{2}
\]

对每个分支，直接枚举固定因子 $D_s3^{e_{s,j}}$ 的全部除子残数，并检查在
“每个 $P_{s,j}$ 为素数”时，十四条规范射线是否仍避开目标残数 $-1$。

## 精确结果

在第一层的 616 个安全残数中，得到

\[
\#\{\text{二层安全分支}\}=1793,\qquad
\#\{\text{有二层安全分支的 }r\}=616. \tag{3}
\]

对每个二层安全分支，15 条线性型

\[
3Qm+(Qj+r),\quad P_{1,j}(m),\ldots,P_{14,j}(m) \tag{4}
\]

都是可采纳的：没有任何素数整除 (4) 中至少一条式子对所有 $m$ 的取值。

可采纳性检查是有限的。一个有 15 条线性型的非退化系统若被素数覆盖，该素数至多为
15；脚本逐个检查这些有限域上的根，并处理恒零型。

```bash
python3 reproductions/type_ii_prime_cofactor_boundary.py \
  --base-shift-bound 14 \
  --output reproductions/type-ii-prime-cofactor-boundary-results.json
```

会产生 (3) 的计数及前若干二层安全分支的全部固定因子和线性型。

## 条件性推论

若采用 Dickson 素数元组猜想或相应的 Schinzel 型线性多项式素值假设，则每个
可采纳分支 (4) 有无穷多个 $m$ 使所有 15 条线性型同时为素数。由 (2)，这些
目标素数在固定十四规范移位扇的每一条射线上都失败。因此在这一标准但未证的
素数元组假设下，该固定扇有无穷多个共同失败点。

这不是对 Erdős--Straus 猜想的条件性反例：失败仅指这十四条 Type II 射线不提供
证书，目标素数仍可能由其它 Type I/II 证书或其它方法解决。

## 研究边界

第一层的模三覆盖确实迫使私有商出现额外因子，但第二层已经恢复为可采纳的素数型
系统。因此不能将“剥离一个小强制因子，再以局部同余覆盖递归”当作固定小移位扇的
全覆盖证明策略。

后续若继续 Type II 射线方向，必须引入随目标增长的移位、跨越这个固定扇的其它证书
坐标，或利用比有限模可采纳性更强的因子分布信息。
