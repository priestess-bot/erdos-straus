---
kind: claim
claim_id: column-stochastic-reverse-bridge-boundary
title: 首个共同递降逃逸点的低分母列随机三坐标反向桥接边界
statement: 对 p=2451289 的全部 21 张原始 Type II AC<=14 目标解，完整枚举分母 2<=D<=6 的全部 13026 个约化、可逆、非负、每行每列至少二项非零的 3x3 列随机矩阵 M/D；每个矩阵的精确逆像均不含严格整数源 2<=n<p。该族严格包含同分母范围内的双随机线性传输，且反矩阵和最小公倍数判据穷尽了每个固定目标与矩阵的所有严格源。
claim_status: computationally_reproduced
topics:
- descent
- linear-transport
- column-stochastic
- reverse-lift
- obstruction
- computation
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 2 and 4
  role: Type-II-target-certificate-reconstruction
visibility: public
last_checked: '2026-07-25'
---

# 首个共同递降逃逸点的低分母列随机三坐标反向桥接边界

## 列随机传输与精确反演

令 (M) 为非负整数 (3\times3) 矩阵，每列之和为 (D)，并写

\[
W=\frac MD,\qquad t'=\frac n pWt. \tag{1}
\]

这里 (t=(1/a,1/b,1/c)^T) 是源解的倒数向量。列和条件给出

\[
\mathbf 1^Tt'=\frac np\mathbf1^TWt
=\frac np\mathbf1^Tt=\frac4p,
\]

所以 (1) 在实数层面把 (4/n) 的解送到 (4/p) 的解。它只要求列随机；此前的
双随机盒额外要求每行之和也为 (D)。

若 (det M\ne0)，固定目标倒数向量 (t') 后，所有逆像都必为

\[
t=\frac Hn,\qquad
H=pD M^{-1}t'
=\frac{pD}{\det M}\operatorname{adj}(M)t'. \tag{2}
\]

把 (H_i) 约为 (u_i/v_i)。正整数源存在当且仅当三项均正且

\[
n_0=\operatorname{lcm}(u_1,u_2,u_3)<p. \tag{3}
\]

此时 (n=n_0) 已给出所有坐标为整数的最小严格源；任何其它整源分母是 (n_0) 的
倍数。因此 (3) 对一个固定目标和矩阵穷尽了全部 (2\le n<p) 的源，不需要枚举源
埃及分数分解。

## 完整矩阵盒

审计取

1. (2\le D\le6)；
2. 每列和为 (D)，所有条目非负，且全部条目的最大公因子为 (1)；
3. 每行、每列至少有两个正条目；
4. (det M\ne0)。

第 3 条只排除坐标置换、单坐标复制等非混合模板；它不强加行和条件。按三列分别枚举
所有和为 (D) 的有序三元组，得到：

| (D) | 列随机真正混合矩阵数 |
|---:|---:|
| 2 | 6 |
| 3 | 102 |
| 4 | 720 |
| 5 | 3,006 |
| 6 | 9,192 |
| 合计 | 13,026 |

这个盒严格包含同一分母范围内的双随机矩阵。例如

\[
\frac12
\begin{pmatrix}1&1&0\\0&1&1\\1&0&1\end{pmatrix}
\]

仍在其中，并在 (p=31) 上反向恢复严格源
((n;a,b,c)=(15;4,120,120))。因此空结果并非实现遗漏了先前的循环正例。

## 压力点结果

对首个共同真实递降逃逸点

\[
p=2\,451\,289
\]

的全部 (A,C\le14) 原始 Type II 射线目标去重后有 21 张目标解。将每张解与上述
13,026 个矩阵逐一代入 (2)--(3)，共精确检查

\[
21\cdot13\,026=273\,546
\]

个完整反向逆像，得到

\[
\#\{\text{严格列随机线性源}\}=0. \tag{4}
\]

重建：

```bash
python3 reproductions/column_stochastic_reverse_bridge.py
python3 -m unittest tests/test_column_stochastic_reverse_bridge.py -q
```

## 正确边界

结果只排除所列有限分母盒内、源解无关的可逆零偏移线性传输；它不排除分母
(D>6)、奇异矩阵、带偏移的仿射映射、依赖源因子标记的映射或非线性耦合。特别地，
它不构成 Erdős--Straus 猜想的反例。

不过它将现有的双随机空盒扩展到严格更大的列随机族。因此后续“严格递降”工作不应只
扩大这种低复杂度矩阵搜索，而应给出能使某个带标记源集递归非空的独立机制。
