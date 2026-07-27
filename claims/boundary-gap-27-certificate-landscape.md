---
kind: claim
claim_id: boundary-gap-27-certificate-landscape
title: 五亿边界点最短 gap-27 证书层的完整图
statement: 对p=477015289和全部允许缺口3<=m<=27，逐项分解x=(p+m)/4并完整枚举d|x^2。m=3,7,11,15,19,23均无Type I或Type II证书；m=27恰有三张Type I证书，正规形为(29,433,9497)、(29,1,4112201)、(12557,1,9497)，没有Type II证书。三张证书均不满足规范p尾去缩放的严格递降条件。
claim_status: computationally_reproduced
topics:
- type-I
- type-II
- descent
- finite-audit
- boundary-case
sources:
- paper: bradford2024
  locator: Propositions 1--3
  role: Type-I-and-Type-II-certificate-context
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-27'
---

# 五亿边界点最短 gap-27 证书层的完整图

令

$$
p=477{,}015{,}289,\qquad x_m=\frac{p+m}{4}.
$$

对每个允许缺口 $m\equiv3\pmod4$、$3\le m\le27$，本记录完整分解 $x_m$，枚举每个
$d\mid x_m^2$，并分别检查

$$
m\mid px_m+d \quad\text{(Type I)},\qquad
d\le x_m,\quad m\mid x_m+d \quad\text{(Type II)}. \tag{1}
$$

因此结果是这些缺口上的完整有限结论，不是固定搜索窗口或随机因子搜索。

| $m$ | $\#\{d:d\mid x_m^2\}$ | Type I 数 | Type II 数 |
|---:|---:|---:|---:|
| 3 | 45 | 0 | 0 |
| 7 | 117 | 0 | 0 |
| 11 | 75 | 0 | 0 |
| 15 | 27 | 0 | 0 |
| 19 | 405 | 0 | 0 |
| 23 | 135 | 0 | 0 |
| 27 | 27 | 3 | 0 |

所以 $m=27$ 确为该点最短的 Type I/II 缺口；这个结论在该点并非仅来自“最短搜索先停在
27”，而是对之前六个缺口全部除子状态的穷尽。

## gap-27 的全部 Type I 状态

此时

$$
x_{27}=119{,}253{,}829=29\cdot433\cdot9497.
$$

把每张证书写成 Type I 正规形 $x=ABC$、$d=A^2C$，完整表如下：

| $d$ | $(A,B,C)$ | $R=(4B^2C+1)/27$ | $4BC(A+B)\bmod(R+1)$ |
|---:|---:|---:|---:|
| 7,986,977 | $(29,433,9497)$ | 263,790,079 | 213,225,208 |
| 3,458,361,041 | $(29,1,4,112,201)$ | 609,215 | 608,376 |
| 1,497,470,330,753 | $(12,557,1,9497)$ | 1,407 | 376 |

最后一列正是 [Type I 正规尾部递降选择器](type-I-normal-tail-deflation-selector.md) 的整除条件
$R+1\mid4BC(A+B)$ 的余数。三行均非零，因此没有一张可通过“保持前两项、把 $p$-倍尾
去缩放”的方式给出严格源。这包含此前已知的最短证书第一行，以及 gap-27 的两个外源
直接证书第二、三行。

这个结果仍不排除更大缺口、其它 Type I/II 证书、改变保留项的提升，或完全不同的递降族。
它做的是把当前边界点的**最短证书层**完整封口，从而将下一步明确推进到跨缺口或非规范尾部
的提升。

可复现命令：

~~~bash
python3 reproductions/boundary_gap_certificate_landscape.py \
  --prime 477015289 --gap-cap 27 \
  --output reproductions/type-i-boundary-gap-27-landscape-477015289-results.json
python3 -m unittest tests/test_boundary_gap_certificate_landscape.py -q
~~~
