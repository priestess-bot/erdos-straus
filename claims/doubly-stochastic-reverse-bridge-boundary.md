---
kind: claim
claim_id: doubly-stochastic-reverse-bridge-boundary
title: 首个共同递降逃逸点的低分母双随机三坐标反向桥接边界
statement: 对 p=2451289 的全部 21 张原始 Type II AC<=14 目标解，枚举分母 2<=D<=10 的全部 5082 个约化、可逆、每行每列至少二项非零的 3x3 双随机矩阵 M/D；每个矩阵的精确逆像均不含严格整数源 2<=n<p。由逆矩阵和最小公倍数判据，该结果穷尽此矩阵盒的所有源，而非有界源搜索。
claim_status: computationally_reproduced
topics:
- descent
- weighted-transport
- doubly-stochastic
- type-II
- reverse-lift
- obstruction
- computation
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 2 and 4
  role: Type-II-certificate-reconstruction
visibility: public
last_checked: '2026-07-25'
---

# 首个共同递降逃逸点的低分母双随机三坐标反向桥接边界

## 矩阵传输与完整反演

设 \(M\) 是非负整数 \(3\times3\) 矩阵，其每行、每列之和均为 \(D\)，并写

\[
W=\frac MD,\qquad
t'=\frac n pWt=\frac n{pD}Mt. \tag{1}
\]

列和为 \(D\) 保证倒数和从 \(4/n\) 变为 \(4/p\)；行和相同只是把搜索限制为对三个
坐标对称的双随机模板。若 \(\det M\ne0\)，固定目标 \(t'\) 后，任意逆像必为

\[
t=\frac Hn,\qquad
H=pD\,M^{-1}t'
=\frac{pD}{\det M}\operatorname{adj}(M)t'. \tag{2}
\]

将 \(H_i\) 约为 \(u_i/v_i\)。正整数源存在当且仅当每个 \(H_i>0\)，且

\[
L=\operatorname{lcm}(u_1,u_2,u_3)<p, \tag{3}
\]

其中 \(n=L\)（必要时取 \(2\)）已经给出所有整数源分母 \(n/H_i\)。所以 (3) 对一个
固定矩阵和目标穷尽了全部严格源 \(2\le n<p\)，无须枚举较小分母的所有埃及分数解。

## 明确矩阵盒

为排除坐标置换、保留一个坐标等退化模板，审计只保留：

1. \(2\le D\le10\)；
2. 所有条目非负，且全部条目的最大公因子为 \(1\)；
3. 每行、每列至少有两个正条目；
4. \(\det M\ne0\)。

逐行枚举和为 \(D\) 的三元组，再由列和唯一恢复第三行。得到矩阵数：

| \(D\) | 约化真正混合矩阵数 |
|---:|---:|
| 2 | 6 |
| 3 | 12 |
| 4 | 72 |
| 5 | 180 |
| 6 | 264 |
| 7 | 588 |
| 8 | 834 |
| 9 | 1278 |
| 10 | 1848 |
| 合计 | 5082 |

这个盒包含分母 \(2\) 的循环平均矩阵

\[
\frac12
\begin{pmatrix}1&1&0\\0&1&1\\1&0&1\end{pmatrix},
\]

因此严格包含先前的等权循环候选；但它不包含任意高分母、非双随机、仿射或非线性传输。

## 压力点结果

对首个共同真实递降逃逸点

\[
p=2{,}451{,}289
\]

的全部 \(A,C\le14\) 原始 Type II 射线按目标三元组去重，得到 21 张目标解。对每张解
及上表全部 5,082 个矩阵应用 (2)--(3)，共检查

\[
21\cdot5{,}082=106{,}722
\]

个精确逆像；结果为

\[
\#\{\text{严格反向源}\}=0. \tag{4}
\]

运行：

```bash
python3 reproductions/doubly_stochastic_reverse_bridge.py \
  --prime 2451289 --ac-bound 14 --max-matrix-denominator 10 \
  --output reproductions/doubly-stochastic-reverse-bridge-2451289-ac14-d10-results.json
```

实现用 `fractions.Fraction` 计算伴随矩阵逆像，并将任何非空结果重新代入源方程和
(1)。独立正例为 \(p=31\)：上面的循环矩阵把
\((n;a,b,c)=(15;4,120,120)\) 送到 \((16,248,16)\)，逆程序精确恢复该源。

## 研究边界

该结论把零偏移循环权重的反例范围推广到一类有限但完整的非循环线性传输。它不排除
分母 \(D>10\)、非双随机矩阵、带偏移或非线性映射，或携带额外因子标记的三项互异源。
不过后续递降方案若仍采用线性混合，至少必须解释为何需要越过这个低复杂度矩阵盒，并先
给出独立于目标 Type II 证书的严格势函数。
