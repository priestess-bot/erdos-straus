---
kind: claim
claim_id: li-bound-weaker-than-vaughan
title: Li 的任意对数幂界渐近弱于 Vaughan
statement: Li 证明对每个固定 k 有 E(N)=O_k(N/(log N)^k)，但这在渐近量级上弱于 Vaughan 的伸缩指数界。
claim_status: established
topics:
- exceptional-set
- asymptotic-comparison
sources:
- li1981
- vaughan1970
visibility: public
last_checked: '2026-07-23'
---

# Li 的任意对数幂界渐近弱于 Vaughan

## 结论

Li 证明对每个固定 k 有 E(N)=O_k(N/(log N)^k)，但这在渐近量级上弱于 Vaughan 的伸缩指数界。

## 推理与来源

对每个固定 k，exp(c(log N)^(2/3)) 最终增长快于 (log N)^k，因此 Vaughan 的上界更小。

- Li 1981, Journal of Number Theory 13, 485-494, as cited in modern surveys.
- Direct asymptotic comparison of the two displayed functions.

## 边界

“任意 k”中的 k 是先固定再让 N 趋于无穷，不能让 k 随 N 任意增长。
