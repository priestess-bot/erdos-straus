---
kind: claim
claim_id: reduction-to-one-mod-24
title: 困难素数约化为 p=1 mod 24
statement: 结合三个经典恒等式和素数约化，只需处理素数 p congruent to 1 modulo 24。
claim_status: established
topics:
- reduction
- congruences
- core-case
sources:
- salez2014
visibility: public
last_checked: '2026-07-23'
---

# 困难素数约化为 p=1 mod 24

## 结论

结合三个经典恒等式和素数约化，只需处理素数 p congruent to 1 modulo 24。

## 推理与来源

恒等式分别处理 n=-1 mod3、n=-1 mod4、n=-3 mod8。对大于 3 的素数取这些条件的补集并用 CRT，剩余为 1 mod24。

- Salez 2014, Section 1.1, displayed identities and concluding paragraph.

## 边界

对一般整数说“只剩 1 mod24”不够精确；这个简洁约化依赖先转到素数。
