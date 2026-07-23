---
kind: claim
claim_id: mballa-density-one-explicit
title: Mballa 2026 给出 n=1 mod4 整数中的密度一显式族
statement: 在 n=1 mod4 中，含 3 mod4 素因子的 n 有显式 y=z 解，而其补集自然密度为零。
claim_status: established
topics:
- density-one
- explicit-solutions
- symmetric-solutions
sources:
- mballa2026
visibility: public
last_checked: '2026-07-23'
---

# Mballa 2026 给出 n=1 mod4 整数中的密度一显式族

## 结论

在 n=1 mod4 中，含 3 mod4 素因子的 n 有显式 y=z 解，而其补集自然密度为零。

## 推理与来源

若 b|n 且 b=3 mod4，令 x=(n+b)/4、q=n/b，则 q=3 mod4，t=q(q+1)/2 为整数并产生 y=z=tb。补集只含 1 mod4 素因子，Euler 乘积给出密度零。

- Mballa 2026, Proposition 4 and density section.

## 边界

密度一不等于全部；素数 p=1 mod4 本身不含 3 mod4 素因子，因此该构造不直接解决核心素数。
