---
kind: claim
claim_id: type-II-h19-pure-new-square-ray-boundary-1b
title: 十亿 H19 新因子状态中刚性平方射线的完整边界
statement: 在十亿范围的541个 H19 新因子状态中，A=r、C=1、h 为 H19 新素数的平方移位 Type II 射线在其全部序条件允许半径内恰捕获530个；其余11个状态均无此类证书。它们仍各有非平方射线的纯新单素因子证书，故这是子族边界而非 Erdős--Straus 反例。
claim_status: established
topics:
- type-II
- square-ray
- pure-new-factor
- H19
- finite-audit
- boundary
- canonicalization
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-certificate-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-27'
---

# 十亿 H19 新因子状态中刚性平方射线的完整边界

## 命题

取 [H19 源自由状态剖面](type-II-source-free-transition-profile.md) 中
\(p\le10^9\) 的全部 541 个“新因子状态”。对每个状态，令

\[
\mathcal O_p=\bigcup_{1\le t\le19}\operatorname{Supp}(p+4t).
\]

只允许刚性平方射线

\[
A=r,\qquad C=1,\qquad h=q,\qquad
q\mid p+4r^2,\qquad q\equiv-1\pmod{4r},\qquad q\notin\mathcal O_p. \tag{1}
\]

完整枚举给出

\[
541=530_{\rm hit}+11_{\rm order\mbox{-}exhausted}. \tag{2}
\]

这里的“完整”不依赖任意半径截断。对该射线，原始 Type II 序条件为

\[
B-A=\frac{K(p-4r^2)+2r}{h}\ge0,\qquad K=\frac{q+1}{4r}. \tag{3}
\]

一旦

\[
4r^2-2r>p, \tag{4}
\]

式 (3) 对每个 \(K\ge1\) 都为负。因此每个 \(p\) 只需检查

\[
r\le R_p:=\max\{r:4r^2-2r\le p\}. \tag{5}
\]

本审计的最大 \(R_p\) 为 \(15{,}750\)，故实际使用 \(r\le16{,}000\) 已穷尽全部
541 个状态的合法平方射线。11 个未命中状态为

\[
\begin{split}
&176089,\ 225289,\ 870241,\ 4722169,\ 20368321,\ 26953921,\\
&70005049,\ 87503329,\ 439768081,\ 629071081,\ 826129441.
\end{split} \tag{6}
\]

## 非平方释放

式 (6) 不构成原猜想的反例。它们在同一份 H19 状态集中均有纯新单素因子 Type II
证书，只是必须离开 \(C=1\) 的平方射线。例如：

| \(p\) | \(s=A^2C\) | \((A,C)\) | \(h\) |
|---:|---:|---:|---:|
| 176089 | 40 | (2, 10) | 79 |
| 225289 | 32 | (4, 2) | 2591 |
| 4722169 | 96 | (4, 6) | 1151 |
| 70005049 | 90 | (3, 10) | 55079 |
| 439768081 | 20 | (2, 5) | 29959 |
| 826129441 | 57 | (1, 57) | 8663 |

其余五点及所有重建参数见
reproductions/type-ii-minimal-collision-support-h19-1b-s1008-results.json；
该审计已证明 541 个状态均可在 \(s\le1008\) 以纯新单素因子闭合。

## 意义

[增长平方移位上的纯新单素因子 Type II 射线具有超对数稀薄尾部](type-II-pure-new-square-ray-superlog-tail.md)
仍给出一个独立的密度一结论。式 (2) 表明不能把它直接加强成点态定理：即使有限压力集，
也有状态在全部合法 \(A=r,C=1\) 射线上失败。

因此点态选择器至少要增加一种自由度，例如允许 \(s=A^2C\) 中的 \(C>1\)，或在平方射线
失败时转入已知的 Type I/外部源严格递降。这个结论排除了一个过窄的证明目标，同时保留了
平方族作为解析筛的低熵骨架。

## 复现

~~~bash
python3 reproductions/type_ii_h19_pure_new_square_ray_profile.py \
  --radius-cap 16000 \
  --output reproductions/type-ii-h19-pure-new-square-ray-1b-results.json
python3 -m unittest tests/test_type_ii_h19_pure_new_square_ray_profile.py -q
~~~
