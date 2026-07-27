---
kind: claim
claim_id: type-II-h19-bounded-r-finite-product-exponent-profile
title: H19 固定 r 有限积集障碍的指数缺口
statement: 在 r<=9999 的15个 H19 残余中，40个有限积集型平方尾失败状态的目标残数全部在某个 M^L 的除子残数集中首次出现，且 L 的分布为3:26、4:2、5:7、6:2、7:1、9:2。因此所有这类状态的纯残数障碍至多需要从平方提升至九次幂；这不是当前递降的证书。
claim_status: computationally_reproduced
topics:
- type-I
- descent
- even-source
- divisor-residues
- exponent
- finite-audit
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-certificate-reconstruction
visibility: public
last_checked: '2026-07-25'
---

# H19 固定 \(r\) 有限积集障碍的指数缺口

对 \(r\le9999\) 的 15 个尾部残余，40 个有限积集型状态的目标已在
\(\langle\operatorname{supp}(M)\rangle\) 中，但尚未由 \(M^2\) 的除子指数盒实现。
对每个状态枚举 \(M^L\) 的全部除子残数，最小进入指数的分布为：

| 首次指数 \(L\) | 状态数 |
|---:|---:|
| 3 | 26 |
| 4 | 2 |
| 5 | 7 |
| 6 | 2 |
| 7 | 1 |
| 9 | 2 |

因此所有 40 个状态在 \(L\le9\) 时已达到目标残数。这个上界应读作明确的研究接口：
若能从另一种可提升源、尾部迭代或因子重数机制中合法地产生这些额外指数，则有限积集型
障碍可被解除。

它**不是** Erdős--Straus 证书，也不意味着把原来的 \(M_1^2\) 条件替换为 \(M_1^L\)
仍能保持整数性、严格递降或三项分解。原偶源定理只允许平方尾；这里的审计仅测量残数
缺口的大小。事实上，沿用原公式 \(u=(M+e)/r,\ v=Mu/e\) 时，\(v\) 的整性当且仅当
\(e\mid M^2\)，故高次候选不能直接补上该缺口，见
[奇距离偶源公式的平方尾刚性](odd-distance-even-source-square-tail-rigidity.md)。

## 重建

~~~bash
python3 reproductions/type_ii_h19_bounded_r_tail_obstruction_profile.py
python3 reproductions/type_ii_h19_bounded_r_finite_product_exponent_profile.py
python3 -m unittest tests/test_type_ii_h19_bounded_r_finite_product_exponent_profile.py -q
~~~
