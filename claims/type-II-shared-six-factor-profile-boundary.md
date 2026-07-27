---
kind: claim
claim_id: type-II-shared-six-factor-profile-boundary
title: 共享 Type II 选择器的最短零积长度谱及六因子反例
statement: 对四自动缺口后且无 k=1 选择器的核心素数，枚举 m<=239 的全部 Type II 缺口和 p+m 的共享除子，令 L(p) 为共享除子的最小素因子重数。p<=2*10^7 时最大 L 为 6，但 p=95741809 有 L=7，最短见证在 m=71 为 D=7364760=2^3*3*5*13*4721。因此固定至多六个素因子的共享选择规则在当前小缺口框架已失败。
claim_status: computationally_reproduced
topics:
- type-II
- shared-divisor
- factorization
- zero-sum-theory
- divisor-residues
- short-certificate
- computation
- proof-program
sources:
- paper: bradford2024
  locator: "Proposition 2"
  role: Type-II-divisor-criterion
- paper: grynkiewicz_marchan_ordaz2009
  locator: "subsequence-product framework"
  role: product-length-context
visibility: public
last_checked: '2026-07-25'
---

# 共享 Type II 选择器的最短零积长度谱及六因子反例

## 定义

对每个四自动缺口后且无 \(k=1\) 选择器的核心素数 \(p\)，在所有

\[
3\le m\le239,\qquad m\equiv3\pmod4
\]

且具有 Type II 证书的缺口中，考察全部

\[
D>1,\qquad D\mid p+m,\qquad D\equiv1\pmod m.
\]

记

\[
L(p)=\min\{\Omega(D):D\text{ 满足上述条件}\}, \tag{1}
\]

其中 \(\Omega(D)\) 按重数计素因子数。这正是共享除子残数序列达到单位元所需的
最短零积长度；它不同于不同素因子支撑数 \(\omega(D)\)。

## 精确长度谱

| 范围 | 压力点数 | \(L=1\) | \(L=2\) | \(L=3\) | \(L=4\) | \(L=5\) | \(L=6\) | \(L=7\) | 未命中 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(p\le10^6\) | 15 | 0 | 3 | 7 | 2 | 2 | 1 | 0 | 0 |
| \(p\le10^7\) | 84 | 9 | 32 | 28 | 7 | 5 | 3 | 0 | 0 |
| \(p\le2\cdot10^7\) | 146 | 16 | 58 | 51 | 12 | 6 | 3 | 0 | 0 |
| \(p\le10^8\) | 500 | 60 | 236 | 148 | 41 | 9 | 4 | 1 | 1 |

前三个范围中最大最短长度均为 6；它们只能支持一个有限候选，不能支持全称结论。

长度 6 的最短见证在 \(p\le2\cdot10^7\) 中已有三条：

| \(p\) | \(m\) | \(D\) |
|---:|---:|---:|
| 967129 | 47 | \(16968=2^3\cdot3\cdot7\cdot101\) |
| 5596369 | 71 | \(37560=2^3\cdot3\cdot5\cdot313\) |
| 6569161 | 55 | \(410576=2^4\cdot67\cdot383\) |

每行均有 \(L(p)=6\)。但 100M 审计给出更强的反例：

\[
p=95741809,\qquad m=71,\qquad
D=7364760=2^3\cdot3\cdot5\cdot13\cdot4721,\qquad L(p)=7. \tag{2}
\]

因此上界 6 已失败；上界 5 当然也失败。这个点的见证仍使用可变缺口，而非一个
固定模数模板。

运行：

    python3 reproductions/type_ii_automatic_residual_k1_funnel.py \
      --limit 100000000 --gap-cap 239 --factor-length-profile \
      --output reproductions/type-ii-automatic-residual-minimum-factor-length-profile-100m-results.json

会重建第四行、(2) 与唯一的小缺口未命中点。

## 正确边界

下列有界长度强化已经被 (2) 否定：

\[
\begin{aligned}
\text{对每个 }p\equiv1\pmod {24}\text{，总存在合法 }m\text{ 与 }D
\text{ 使}\\
-x\in\Pi_m(x^2),\quad D\mid p+m,\quad D\equiv1\pmod m,\quad
\Omega(D)\le6,\qquad x=(p+m)/4. \tag{3}
\end{aligned}
\]

(3) 是 `type-II-shared-residue-selector-conjecture` 的有界长度强化；(2) 给出其在
\(m\le239\) 小缺口框架内的明确反例。这里并未证明 \(p=95741809\) 在更大缺口没有
长度至多 6 的证书，因此不把这项审计误写为对 (3) 的全称反例。

研究任务必须允许零积长度随 \(p\) 增长，或改用跨缺口结构，而不能再追求一个固定的
六因子界。
