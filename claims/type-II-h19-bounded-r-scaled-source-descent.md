---
kind: claim
claim_id: type-II-h19-bounded-r-scaled-source-descent
title: H19 固定 r 残余的非倍数缩放源严格递降
statement: 在 r<=9999 未命中的15个 H19 残余的1025个去重非倍数缩放源候选中，82个候选给出经精确有理数与 Type I 证书复核的严格递降，覆盖14个残余素数；唯一未覆盖的是 99532801。因此改变首项为 an/2 或 an/4 是实际有效的新递降机制，不只是参数重写。
claim_status: computationally_reproduced
topics:
- type-I
- descent
- scaled-source
- even-source
- certificate
- finite-audit
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-certificate-reconstruction
visibility: public
last_checked: '2026-07-25'
---

# H19 固定 \(r\) 残余的非倍数缩放源严格递降

在固定 \(r\le9999\) 的 15 个平方尾残余上，先以移位因子约化生成 1,025 个不同的
非倍数缩放首项候选

\[
\frac{an}{2}\quad\text{或}\quad\frac{an}{4}.
\]

再对每个候选完整枚举强制满足 \(b\,\mathrm{shift}\mid e\) 的平方尾因子，并以精确
有理数验证源、目标三项分解以及恢复的 Type I 除子证书。结果为：

| 项目 | 数量 |
|---|---:|
| 去重缩放候选 | 1,025 |
| 给出严格递降的候选 | 82 |
| 被覆盖的残余素数 | 14 / 15 |
| 未覆盖素数 | 99,532,801 |

例如 \(p=3361\) 可取 \(n=3354,a=237,b=2,\mathrm{shift}=43\)，得到

\[
\frac4{3354}
=\frac1{397449}+\frac1{936}+\frac1{8216}
\Longrightarrow
\frac4{3361}
=\frac1{31065723}+\frac1{936}+\frac1{8216},
\]

并在缺口 \(383\) 恢复 Type I 证书。

这说明非倍数缩放源是与原偶源平方尾不同的有效递降分支。它仍是有限输入盒上的结果；
不能由此推断对所有核心素数或所有 \(r\) 残余必有该候选。

## 重建

~~~bash
python3 reproductions/type_ii_h19_bounded_r_scaled_source_descent.py
python3 -m unittest tests/test_type_ii_h19_bounded_r_scaled_source_descent.py -q
~~~
