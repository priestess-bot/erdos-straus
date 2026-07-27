---
kind: claim
claim_id: type-II-moving-window-one-private-prime-conditional-escape
title: 直接 Type II 前 37 窗口的一私有素因子条件逃逸
statement: 令 Q=lcm(24,{4j-1:1<=j<=37})，r=153633769。存在 38 条原始且可采纳的线性式 p(k)=16Qk+r、L_1(k),...,L_37(k)，使对充分大的 k，若它们同时为素数，则每个 x_j=(p(k)+4j-1)/4 都等于固定因子 E_j 乘 L_j(k)，且 x_j^2 的全部除子模 4j-1 都避开 Type II 目标 -x_j。因此在 Dickson 素数元组猜想或相应 Schinzel 假设下，存在无穷多个核心素数逃过直接 Type II 的 j<=37 窗口。
claim_status: computationally_reproduced
topics:
- type-II
- moving-window
- conditional-boundary
- prime-tuples
- divisor-residues
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-criterion
- paper: grynkiewicz_marchan_ordaz2009
  locator: subsequence-product framework
  role: divisor-product-set-language
visibility: public
last_checked: '2026-07-25'
---

# 直接 Type II 前 37 窗口的一私有素因子条件逃逸

## 条件性命题

令

\[
Q=\operatorname{lcm}\left(24,\{4j-1:1\le j\le37\}\right)
=36{,}338{,}666{,}624{,}327{,}928{,}020{,}023{,}600{,}057{,}737{,}227{,}611{,}800
\]

并取

\[
r=153{,}633{,}769,\qquad p(k)=16Qk+r. \tag{1}
\]

对 \(1\le j\le37\)，写 \(m_j=4j-1\)，并令

\[
x_j(k)=\frac{p(k)+m_j}{4}
=4Qk+\frac{r+m_j}{4}. \tag{2}
\]

定义

\[
E_j=\gcd\left(4Q,\frac{r+m_j}{4}\right),\qquad
L_j(k)=\frac{4Q}{E_j}k+\frac{r+m_j}{4E_j}. \tag{3}
\]

则 \(x_j(k)=E_jL_j(k)\)。脚本对所有 \(j\le37\) 精确枚举
\(E_j^2L_j(k)^e\;(e=0,1,2)\) 的模 \(m_j\) 残数，验证

\[
-x_j(k)\notin\Pi_{m_j}(E_j^2L_j(k)^2). \tag{4}
\]

这里 \(L_j(k)\bmod m_j\) 与 \(k\) 无关，因为 \(m_j\mid4Q/E_j\)；
所以 (4) 是整个参数族的有限同余断言，而不是对一个数值样本的观察。

此外，\(p,L_1,\ldots,L_{37}\) 都是原始、两两不同的正线性式。局部可采纳性由
完整根覆盖检验给出：对每个素数 \(\ell\le38\)，这些线性式的根并不覆盖
\(\mathbb F_\ell\)；对 \(\ell>38\)，38 个线性式至多给出 38 个根，不可能覆盖
\(\mathbb F_\ell\)。在初始参数 \(p=Qn+r\) 中，唯一出现的覆盖素数是 \(2\)；
连续取四次 \(n\equiv0\pmod2\)，即 \(n=16k\)，便得到上述可采纳族。

故在 Dickson 素数元组猜想，或这 38 条线性式的 Schinzel 假设 H 成立时，有无穷多
\(k\) 使 \(p(k),L_1(k),\ldots,L_{37}(k)\) 同时为素数。充分大时
\(L_j(k)\) 大于 \(E_j\) 的全部素因子，故 (3) 是完整分解；由 (4)，这些核心素数在
每个 \(j\le37\) 位置均没有直接 Type II 证书。

## 精确复现

运行

    python3 reproductions/type_ii_moving_window_conditional_escape.py \
      --seed-prime 153633769 --window 37 --max-depth 8 \
      --output reproductions/type-ii-moving-window-conditional-escape-p153633769-j37-results.json

会输出 38 条线性式、全部 37 个固定因子与除子残数核查。所得分支为

\[
n=16k,\qquad
(2,0),(2,0),(2,0),(2,0), \tag{5}
\]

其中每对表示一次覆盖素数 \(2\) 的分支选择；最终没有局部覆盖素数。

## 对研究路线的含义

这个结论是**条件性边界**，不是 Erdős--Straus 猜想的条件性反例。它构造的只是
“前 37 个指定首分母缺口均不产生直接 Type II 证书”的素数族；这些素数仍可能有：

- 更大的移动窗口位置的 Type II 证书；
- 非此窗口的 Type I/II 证书；
- 任何其它单位分数分解。

但它已经排除一个具体的证明期待：在 Dickson/Schinzel 的通常预测成立时，不存在
一个以 \(j\le37\) 为全称覆盖窗口的直接 Type II 定理。因此 500M 中
\(J=32\) 的全覆盖不能被外推为固定窗口规律。

正向工作应改为：让窗口或 \(AC\) 射线随 \(p\) 自适应增长，或证明这类共同失败模式
可产生一个与目标证书逻辑独立的、可闭合的严格递降状态。仅数私有素因子、只保留总积
字符，或固定有限个窗口位置，都不会跨过这一边界。
