---
kind: claim
claim_id: type-II-h19-cross-half-factor-complexity-boundary
title: H19 本质跨侧零溢出见证的乘法复杂度边界
statement: 对十亿 H19 首 r 剖面中184个本质跨侧零溢出状态，定义交叉复杂度为满足 alpha|A、beta|B、alpha beta=-1 mod r 的最小 Omega(alpha)+Omega(beta)。精确分布为2:21、3:93、4:53、5:13、6:2、7:2。故仅21个状态可由两侧各取一个素因子处理，70个至少需要四次素因子重数；双线性单素因子选择器不能覆盖该有限状态集。
claim_status: computationally_reproduced
topics:
- type-I
- even-source
- factorization
- divisor-residues
- product-set
- obstruction
- finite-audit
- h19
sources:
- paper: bradford2024
  locator: Proposition 1
  role: even-source-descent
visibility: public
last_checked: '2026-07-26'
---

# H19 本质跨侧零溢出见证的乘法复杂度边界

在[交叉半因子判据](odd-distance-even-source-cross-half-factor-zero-overflow.md)的记号下，
本质跨侧状态满足

\[
\exists\alpha\mid A,\ \beta\mid B:\quad\alpha\beta\equiv-1\pmod r,
\]

但 \(A\)、\(B\) 各自的除子都不命中 \(-1\pmod r\)。定义其最小交叉复杂度为

\[
\lambda(A,B;r)=
\min_{\substack{\alpha\mid A,\ \beta\mid B\\
\alpha\beta\equiv-1\ (\bmod r)}}
\bigl(\Omega(\alpha)+\Omega(\beta)\bigr), \tag{1}
\]

其中 \(\Omega\) 按重数计素因子数。对本质跨侧状态，\(\alpha,\beta>1\)，所以
\(\lambda\ge2\)。

在十亿 H19 剖面的 184 个本质跨侧状态上，完整两侧除子对枚举给出：

| \(\lambda\) | 状态数 |
| ---: | ---: |
| 2 | 21 |
| 3 | 93 |
| 4 | 53 |
| 5 | 13 |
| 6 | 2 |
| 7 | 2 |

因此只有 21 个状态可被“一侧一个素因子”的双线性模型捕获；70 个状态的任何交叉见证
至少需要四个素因子重数。当前最大值是 7，例如 \(p=870241\) 的最短见证为
\(\alpha=40\)、\(\beta=946\)。

这是一项有限复杂度边界，不证明 \(\lambda\) 在一般情形有界，也不构造统一选择器；其作用是
排除过弱的理论目标。下一步若使用两侧乘法残数，必须允许一般受限积集，或证明共同失败会
强制 \(\lambda\) 下降，而不能预设单素因子配对已经足够。

可复现命令：

~~~bash
python3 reproductions/type_ii_h19_cross_half_factor_complexity.py \
  --input reproductions/type-ii-h19-zero-overflow-half-factor-pair-profile-1b-results.json \
  --output reproductions/type-ii-h19-cross-half-factor-complexity-1b-results.json
python3 -m unittest tests/test_type_ii_h19_cross_half_factor_complexity.py -q
~~~
