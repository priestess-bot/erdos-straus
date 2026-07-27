---
kind: claim
claim_id: type-II-tail-deflation-p-minus-one-pure-new-release
title: 五千万双位移递降残余的纯新单素因子释放
statement: 在 p<=5*10^7 时，双尾抽缩与完整 p-1 严格递降后仍未被规范位移s<=2覆盖的四个素数，均在首次后续位移3,3,4,5由一个不整除p+4或p+8的新素数h=47,3347,31,239单独给出 Type II 证书。故该有限压力集全部是纯新单素因子释放，而非碰撞或旧私有因子复用。
claim_status: computationally_reproduced
topics:
- type-II
- short-certificate
- canonical-ray
- new-factor
- factorization
- transition
- finite-audit
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-certificate-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-25'
---

# 五千万双位移递降残余的纯新单素因子释放

令旧来源为最初两条规范移位数

\[
p+4,\qquad p+8.
\]

在五千万的双尾抽缩、完整 \(p-1\) 严格递降和 \(s\le2\) 短证书共同残余上，逐项比较
首次后续证书因子 \(h\) 与旧来源的全部素因子。四点的结果为：

| \(p\) | 首次释放位移 | \(h\) | \(h\) 是否为旧来源素因子 | 新重数 |
|---:|---:|---:|---|---:|
| 25,073,689 | 3 | 47 | 否 | 1 |
| 33,011,449 | 3 | 3,347 | 否 | 1 |
| 42,622,969 | 4 | 31 | 否 | 1 |
| 48,825,529 | 5 | 239 | 否 | 1 |

每个 \(h\) 都是素数，且不整除 \(p+4\) 或 \(p+8\)。因此四个释放均为纯新单素因子
Type II 证书，没有碰撞或旧私有因子成分。

这为单新因子选择器提供一个与 H19 窗口不同的、由严格递降残余导出的有限样本，但不证明
任意这类状态都会在有界深度释放。

## 重建

~~~bash
python3 reproductions/type_ii_tail_deflation_p_minus_one_pure_new_release.py
python3 -m unittest tests/test_type_ii_tail_deflation_p_minus_one_pure_new_release.py -q
~~~
