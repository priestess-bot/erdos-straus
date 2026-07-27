---
kind: claim
claim_id: type-I-tail-reverse-small-b-source-terminal-500m
title: 五亿低溢出反向二尾源的非核心终止因子
statement: 五亿范围内由m<=127、B<=5的Type I反向二尾剖面选出的1,717条源分母，每一条均含有某个素因子q不congruent to 1 modulo 24。故每条源均可由该非核心素数的经典分解按比例缩放，终止于既知的非核心素数类；所选q最大为3299。
claim_status: computationally_reproduced
topics:
- type-I
- descent
- reverse-lift
- reduction
- finite-audit
sources:
- salez2014
visibility: public
last_checked: '2026-07-27'
---

# 五亿低溢出反向二尾源的非核心终止因子

[低溢出反向二尾剖面](type-I-tail-reverse-small-b-profile-500m.md) 在五亿普通 Type II
尾遗漏上选出 $1{,}717$ 条严格反向边。对每条边的源分母 $n$ 作完整试除分解，取最小素因子

$$
q\mid n,\qquad q\not\equiv1\pmod{24}.
$$

所有 $1{,}717$ 条均有这样的 $q$；没有任何选定源的全部素因子都在核心素数类
$1\pmod{24}$。所选终止素因子的最大值为 $3299$，按模 $24$ 的计数为

| $q\bmod24$ | 2 | 3 | 5 | 7 | 11 | 13 | 17 | 19 | 23 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 条数 | 1437 | 173 | 50 | 20 | 14 | 12 | 3 | 4 | 4 |

这使每条有限反向边都能接到经典终止类：由[困难素数约化](reduction-to-one-mod-24.md)，
$q\not\equiv1\pmod{24}$ 的素数已有经典三分数分解；写 $n=uq$，再由
[素数分母约化](reduction-to-primes.md) 把该分解的三个分母同时乘以 $u$，即得到 $4/n$
的分解。此处的“终止”是指源不再需要作为新的核心素数实例处理。

该结论严格限于已固定的 $p\le5\times10^8,m\le127,B\le5$ 选择剖面。它不证明对任意核心
素数都存在此类低溢出边，也不提供统一的源侧选择规则。

可复现命令：

~~~bash
python3 reproductions/type_i_tail_reverse_small_b_source_terminal_profile.py \
  --profile reproductions/type-i-tail-reverse-small-b5-500m-results.json \
  --output reproductions/type-i-tail-reverse-small-b-source-terminal-500m-results.json
python3 -m unittest tests/test_type_i_tail_reverse_small_b_source_terminal_profile.py -q
~~~
