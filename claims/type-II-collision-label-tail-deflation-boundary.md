---
kind: claim
claim_id: type-II-collision-label-tail-deflation-boundary
title: H19 碰撞标签证书的固定缺口尾部递降边界
statement: 在 p<=10^9 的11个最小正碰撞重数 H19 单新因子 Type II 证书中，只有 p=345601 和 p=92421169 的固定缺口满足存在 D|p+m、D=1 mod m，从而给出严格缩放首分母尾部递降；其余9个，包括两碰撞点 p=372271201，在该固定证书缺口的全部此类 D 上均失败。因此碰撞标签短证书不能自动转化为该标记递降，后续必须换证书、换源状态或使用不同递降机制。
claim_status: computationally_reproduced
topics:
- type-II
- descent
- collision-factor
- short-certificate
- marked-lift
- finite-audit
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-certificate-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-26'
---

# H19 碰撞标签证书的固定缺口尾部递降边界

令一张选定的 Type II 证书有缺口 \(m\)。缩放首分母的双尾递降在这个固定缺口上
等价于存在

\[
D\mid p+m,\qquad D>1,\qquad D\equiv1\pmod m. \tag{1}
\]

此时 \(k=(D-1)/m\)，源分母为 \(k(p+m)/D<p\)。本审计对十亿 H19 剖面中最小
碰撞重数为正的全部 11 张单新因子证书，精确分解 \(p+m\) 并枚举其全部因子 \(D\)。

只有两张命中：

| \(p\) | 碰撞重数 | \(s\) | \(m\) | \(D\) | \(k\) | 源分母 |
|---:|---:|---:|---:|---:|---:|---:|
| 345,601 | 1 | 26 | 95 | 96 | 1 | 3,601 |
| 92,421,169 | 1 | 41 | 867 | 868 | 1 | 106,477 |

其余九点在各自固定缺口上没有满足 (1) 的因子；其中包括首个两碰撞状态
\(p=372{,}271{,}201\)、\(s=89\)、\(m=16{,}867\)。所以两个已命中点都只是
普通双尾去 \(p\)（\(k=1\)），并没有出现额外的缩放首分母救援。

这是一条**固定证书边界**：它不否定同一 \(p\) 的其他 Type II 证书、Type I 证书或
外部源递降。它准确排除的推理是“只要 CRT 碰撞标签给出单新因子短证书，便可在同一
缺口自动递降”。

## 重建

~~~bash
python3 reproductions/type_ii_collision_label_tail_deflation.py
python3 -m unittest tests/test_type_ii_collision_label_tail_deflation.py -q
~~~
