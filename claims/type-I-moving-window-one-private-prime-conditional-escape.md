---
kind: claim
claim_id: type-I-moving-window-one-private-prime-conditional-escape
title: Type I 前八个移动缺口的一私有素因子条件逃逸
statement: 在 Dickson 素数元组猜想或相应 Schinzel 假设下，存在无穷多个核心素数 p，使其在全部缺口 \(m=3,7,11,15,19,23,27,31\) 都没有 Type I 证书。精确地，存在9个局部可采纳的仿射素数形式，其中 \(p(k)=4506274080k+1126589689\)，且每个 \(x_j=(p+4j-1)/4\) 是一个固定因子与一个仿射素数形式的乘积；每个位置的完整平方除子残数集都避开 \(-1/4\bmod(4j-1)\)。
claim_status: conditional
topics:
- type-I
- moving-window
- conditional-escape
- Dickson
- divisor-residues
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-divisor-criterion
visibility: public
last_checked: '2026-07-25'
---

# Type I 前八个移动缺口的一私有素因子条件逃逸

## 条件命题

设

\[
Q=\operatorname{lcm}(24,3,7,11,15,19,23,27,31)=1126568520
\]

并取

\[
p(k)=4Qk+Q+21169=4506274080k+1126589689. \tag{1}
\]

对 \(j=1,\ldots,8\)，令

\[
m_j=4j-1,\qquad x_j(k)=\frac{p(k)+m_j}{4}.
\]

程序给出精确分解

\[
x_j(k)=E_jL_j(k), \tag{2}
\]

其中 \(E_j\) 为固定正整数，\(L_j\) 为原始仿射形式。九个形式

\[
p,L_1,\ldots,L_8 \tag{3}
\]

两两不同且局部可采纳。又对每个 \(j\)，在假设 \(L_j(k)\) 为素数的
一私有素因子模型中，完整的平方除子残数集满足

\[
-\frac14\notin\Pi_{m_j}(x_j(k)^2). \tag{4}
\]

因此，若 Dickson 素数元组猜想或这些形式的 Schinzel 假设成立，则存在无穷多个
\(k\) 使 (3) 同时为素数；对充分大的这些 \(k\)，\(p(k)\equiv1\pmod{24}\) 是核心素数，
且在所有八个缺口 \(m_j\) 都没有 Type I 证书。

## 检查

构造从实际共同失败点 \(p=21169\) 的窗口残数出发。局部覆盖素数先后为 2、2；
选择分支残数 1、0 后得到

| 项目 | 数值 |
|---|---:|
| 窗口位置 | 8 |
| 素数形式数 | 9 |
| 分支乘数 | 4 |
| 分支偏移 | 1 |
| 剩余局部覆盖素数 | 0 |

每一位置均枚举固定因子与私有仿射素因子的全部 \(0,1,2\) 次幂组合，因此 (4) 是
该一私有素因子模型的完整 Type I 检查，而非只检查线性除子。

## 边界

这是条件性反例族，不是 Erdős--Straus 猜想的反例：它只保证这八个**预先固定**的
缺口没有 Type I 证书，较大或随 \(p\) 变化的缺口仍可能给出 Type I/II 证书或递降。

它的作用是排除一个不恰当目标。尽管 \(m\le239\) 的 Type I 小缺口扇在 \(10^7\) 内
零遗漏，不能希望仅靠前八个固定缺口及一私有素因子残数模型证明全称覆盖。真正的
跨缺口引理必须允许窗口增长并使用新因子，或证明该模型在某个可控深度无法继续。

这份状态本身恰好展示了后一种机制。把其素数形式再按新缺口 \(m=35\) 的全部
35 个残数类细分时，每一类的新增首分母都有相同固定因子

\[
5301=3^2\cdot19\cdot31,
\]

而其平方除子

\[
2511=3^4\cdot31\equiv26=-\frac14\pmod{35}. \tag{5}
\]

因此所有 35 个分支都在第九位置自动获得 Type I 证书。这是该**特定**一私有素因子
逃逸状态的精确下一步闭合，不是所有 Type I 条件逃逸都在 \(m=35\) 闭合的定理。

## 重建

    python3 reproductions/type_i_moving_window_conditional_escape.py
    python3 -m unittest tests/test_type_i_moving_window_conditional_escape.py -q
