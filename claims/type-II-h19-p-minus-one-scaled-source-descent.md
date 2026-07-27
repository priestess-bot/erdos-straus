---
kind: claim
claim_id: type-II-h19-p-minus-one-scaled-source-descent
title: H19 固定 r 残余的 p-1 非倍数缩放源闭合
statement: 对 r<=9999 留下的15个 H19 残余素数，完整枚举源 n=p-1 的 b=2,4 非倍数缩放候选及其强制平方尾后，每一点均有严格提升和 Type I 证书。该有限闭合包含此前 r 射线缩放分支未命中的 p=99532801。
claim_status: computationally_reproduced
topics:
- type-I
- descent
- scaled-source
- p-minus-one
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

# H19 固定 r 残余的 \(p-1\) 非倍数缩放源闭合

令源分母为 \(n=p-1\)。完整枚举所有满足移位因子约化的首项

\[
\frac{an}{2}\quad\text{或}\quad\frac{an}{4},
\]

以及每个候选的强制倍数平方尾。对每个命中，以精确有理数同时验证
\(4/n\) 和 \(4/p\) 的三单位分数恒等式，并恢复 Type I 除子证书。

在既有 \(r\le9999\) H19 残余的 15 个素数上，共 1,231 个去重候选中有 89 个命中，
该分支全部覆盖。它与旧的
兼容偶源射线不同：后者还要求某个标准形参数 \(d\equiv1\pmod4\)，而缩放首项不保留
该限制。因此这不是旧射线扫描的漏项。

这 89 个有限命中恰好都属于 \(b=4\)，但这不能升级为 \(b=2\) 的一般不可能性。
最小核心反例为 \(p=73,n=72,a=35,b=2,t=3\)：
\[
\frac4{72}=\frac1{1260}+\frac1{20}+\frac1{210}
\Longrightarrow
\frac4{73}=\frac1{30660}+\frac1{20}+\frac1{210},
\]
其 Type I 缺口为 \(7\)。故全称研究必须保留 \(b=2\) 类。

此前唯一未被射线缩放分支覆盖的 \(p=99\,532\,801\) 有

\[
\frac4{99\,532\,800}
=\frac1{2\,475\,727\,135\,027\,200}
+\frac1{24\,883\,310}
+\frac1{5\,641\,703\,296\,384}
\Longrightarrow
\frac4{99\,532\,801}
=\frac1{6\,337\,861\,529\,345\,741\,440}
+\frac1{24\,883\,310}
+\frac1{5\,641\,703\,296\,384}.
\]

此例使用 \(a=99\,493\,921,b=4,\mathrm{shift}=38\,880\)，并在缺口 \(439\)
恢复 Type I 证书。

该结果只说明一个有限输入盒已经被 \(p-1\) 缩放源闭合；没有给出对任意核心素数
存在此类候选的证明。

## 重建

~~~bash
python3 reproductions/type_ii_h19_p_minus_one_scaled_source_descent.py
python3 -m unittest tests/test_type_ii_h19_p_minus_one_scaled_source_descent.py -q
~~~
