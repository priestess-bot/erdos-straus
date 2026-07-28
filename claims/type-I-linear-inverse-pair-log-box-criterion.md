---
kind: claim
claim_id: type-I-linear-inverse-pair-log-box-criterion
title: 仿射逆元对的循环对数有限盒判据
statement: 若 R 为奇素数、L=q*r 且 r=q^{-1} mod R，且 q 的阶 h>4，则 D_R(L)={q^j:-2<=j<=2}。对任意 t属于<q>，令 k 为 q 的离散对数的最小绝对代表元，则 t进入有限盒当且仅当 |k|<=2；将两个坐标预算从1同时扩大到1+delta时的最小额外预算为 max(0,ceil(|k|/2)-1)。七谱中的两个非空素模数两因子 F 方向分别达到最大溢出77和99。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- linear-source
- finite-exponent
- cyclic-log
- inverse-pair
- subgroup-obstruction
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-29'
---

# 仿射逆元对的循环对数有限盒判据

## 引理

设 `R` 为奇素数，`q,r` 是模 `R` 的单位，满足

`r = q^-1 (mod R)`，且 `h = ord_R(q) > 4`。

令 `L = q*r`，并让两个素因子在中心化差集中各自只有一个指数预算。则

    D_R(L) = {q^zq r^zr : zq,zr in {-1,0,1}}
           = {q^j : -2 <= j <= 2}.

记 `t in <q>`，令 `kappa(t)` 是满足 `t = q^kappa(t)` 的最小绝对代表元，
即 `kappa(t) in [-h/2,h/2]` 且按模 `h` 表示 `t`。则

    t in D_R(L)  <=>  |kappa(t)| <= 2.

若把两个坐标的预算同时扩大为 `1 + delta`，则精确的最小额外预算为

    delta(t) = max(0, ceil(|kappa(t)| / 2) - 1).

## 证明

由 `r = q^-1` 有

    q^zq r^zr = q^(zq-zr).

当 `zq,zr in [-1,1]` 时，指数差恰为 `[-2,2]` 中的整数；因 `h > 4`，这些指数类不会
在模 `h` 下发生跨端点混淆，得到第一式和有限盒判据。

预算扩大为 `1 + delta` 后，指数差区间变为

    [-2(1 + delta), 2(1 + delta)].

最小绝对代表元为 `|kappa(t)|`，所以存在表示当且仅当
`|kappa(t)| <= 2(1 + delta)`。解出最小整数 `delta` 即得所示公式。证毕。

## 七谱中的两个实例

七谱审计中有两个非空的“素数模数 + 两个一次仿射素因子”方向满足逆元关系：

| p | R | q | r | ord_R(q) | 子群可见类数 | 最大最小溢出 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 64,214,329 | 359 | 19 | 135,173 | 358 | 60 | 77 |
| 105,295,129 | 839 | 23 | 73 | 419 | 2 | 99 |

两行的有限盒目标交集均为空。第二行的两个目标类都对应 `|kappa| = 199`，故

    delta = ceil(199 / 2) - 1 = 99.

这些数值不是通过有界试探得到的，而是由离散对数公式直接给出；脚本同时从七谱结果逐项
重建两个方向的目标残类。

## 对递降路线的含义

该引理把某类 F 状态的“指数溢出”精确转成一个循环群中的距离 `|kappa|`。因此，
对这类状态，任何可提升递降命题都必须说明：

1. 如何把 `q^kappa` 的长指数差转化为新的合法源/正规形状态；
2. 或者为什么另一条 `R` 状态会把同一类压回 `[-2,2]`；
3. 或者如何直接产生普通 Type II 证书。

单纯证明 `t in <q>` 不能完成任何一项。该引理是一个可证伪的中间目标，
不是混合终端选择引理本身。

## 复现

~~~bash
python3 reproductions/type_i_linear_inverse_pair_log_box_criterion.py
python3 -m unittest tests.test_type_i_linear_inverse_pair_log_box_criterion -q
~~~

结果文件：
[type-i-linear-inverse-pair-log-box-criterion-results.json](../reproductions/type-i-linear-inverse-pair-log-box-criterion-results.json)
