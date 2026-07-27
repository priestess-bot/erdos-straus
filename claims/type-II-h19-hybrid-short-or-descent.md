---
kind: claim
claim_id: type-II-h19-hybrid-short-or-descent
title: H19 残余的十亿短证书或严格递降混合闭合
statement: 在存储的 p<=10^9 H19 残余剖面中，664个状态里660个有完整平方因子外部源严格递降；其余35840809、132285169、141326089、640775689 均有 max(A,C)<=5 的直接 AC Type II 证书（也分别有移位45、27、63、45的纯新因子证书）。因此该有限剖面全部具有半径六短证书或显式严格递降出口。
claim_status: computationally_reproduced
topics:
- type-II
- type-I
- descent
- external-source
- hybrid
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: certificate-and-descent-context
visibility: public
last_checked: '2026-07-25'
---

# H19 残余的十亿短证书或严格递降混合闭合

## 联合命题

以 H19 后的 664 个残余为输入，先尝试完整平方因子外部源严格递降。若它失败，则要求一个
不含旧私有因子、也不含碰撞因子的单新因子规范 Type II 证书。两个出口都逐项验证：

* 递降出口检查源分母严格小于 \(p\)，并以精确有理数验证 \(4/n\) 与 \(4/p\) 的两组解；
* 短证书出口检查 \(h=4ack-1\) 且 \(h\mid p+4a^2c\)。

## 十亿结果

\[
664=660+4. \tag{1}
\]

660 个状态由严格递降闭合。余下四点及其纯新 Type II 备用证书为：

| \(p\) | \(s=a^2c\) | \(h\) |
|---:|---:|---:|
| \(35{,}840{,}809\) | 45 | 31,139 |
| \(132{,}285{,}169\) | 27 | 107 |
| \(141{,}326{,}089\) | 63 | 83 |
| \(640{,}775{,}689\) | 45 | 359 |

这四个递降遗漏也都不必推到后续移位才获得直接证书：

| \(p\) | 直接 AC \((A,C,K,h)\) | 半径 |
|---:|---|---:|
| \(35{,}840{,}809\) | \((4,3,944,45311)\) | 4 |
| \(132{,}285{,}169\) | \((3,3,3,107)\) | 3 |
| \(141{,}326{,}089\) | \((4,3,41469,1990511)\) | 4 |
| \(640{,}775{,}689\) | \((3,5,6,359)\) | 5 |

因而该十亿剖面还有更紧的闭合：

\[
\text{半径六直接 AC 证书}\quad\text{或}\quad
\text{完整平方因子外部源严格递降}. \tag{2}
\]

前一支命中647个、后一支命中660个、共同命中643个；只由递降支承担的17个状态与只由
短证书支承担的上述4个状态恰好互补。

这不是新证明：H19 本身、平方因子递降和证书半径都仍是有限审计参数。但它是当前
“短证书或递降”方案的精确十亿基准，并显示二者不是冗余机制。

## 重建

    python3 reproductions/type_ii_h19_hybrid_short_or_descent.py
    python3 reproductions/type_ii_h19_residual_ac_profile.py --ac-bound 9
    python3 -m unittest tests/test_type_ii_h19_hybrid_short_or_descent.py -q
