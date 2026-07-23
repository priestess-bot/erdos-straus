---
kind: claim
claim_id: reduction-to-primes
title: 只需证明素数分母
statement: 若猜想对每个素数 p 成立，则对每个 n>=2 成立；最小反例若存在必为素数。
claim_status: established
topics:
- reduction
- primes
sources:
- salez2014
- elsholtz_tao2013
visibility: public
last_checked: '2026-07-23'
---

# 只需证明素数分母

## 结论

若猜想对每个素数 p 成立，则对每个 n>=2 成立；最小反例若存在必为素数。

## 推理与来源

若 p|n 且 4/p=1/x+1/y+1/z，令 n=mp，则 4/n=1/(mx)+1/(my)+1/(mz)。

- Salez 2014, Section 1.1.
- Elsholtz-Tao 2013, Introduction.

## 边界

从一个素因子的分解可以缩放到其倍数；反向一般不成立。
