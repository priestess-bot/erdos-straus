---
kind: claim
claim_id: type-I-f-overflow-lower-modulus-single-support-defect
title: 单坐标溢出的 q 幂缺口与 Type II 充分条件
statement: 设 t=R/m、t≡1 (mod 4)、4K=pR+1，且 z 是低模数目标纤维中只有 q 坐标越界 δ 层的表示。则存在 d_0|K^2，使正溢出满足 t|(4q^δd_0+1)，负溢出满足 t|(4d_0+q^δ)。若相应两项端点商 M=(A+B)/t 满足合法缺口、大小和 AB|(p+M)/4 条件，则得到 Type II 证书；这些附加条件并非由单坐标溢出本身推出。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-f-overflow-lower-modulus-weighted-cost-interface
  - type-I-f-overflow-lower-modulus-pareto-overflow
  - type-II-coprime-factor-normal-form
topics:
- type-I
- F-state
- relation-lattice
- overflow
- q-power
- type-II
- dyadic
- descent
- proof-program
sources:
- claim: type-I-f-overflow-lower-modulus-weighted-cost-interface
  role: target-fiber-overflow-definition
- claim: type-II-coprime-factor-normal-form
  role: Type-II-sufficient-condition
visibility: public
last_checked: '2026-07-30'
---

# 单坐标溢出的 \(q\) 幂缺口与 Type II 充分条件

## 设置

设

\[
R=mt,
\qquad t>1,
\qquad t\equiv1\pmod4,
\qquad 4K=pR+1,
\qquad K=\prod_iq_i^{\nu_i},
\]

并假设 \(\gcd(K,R)=1\)。令 \(z=(z_i)\) 是低模数目标纤维中的一个表示：

\[
\prod_iq_i^{z_i}\equiv-1\pmod t.
\tag{1}
\]

假设恰有一个坐标 \(q=q_j\) 越出指数盒，写

\[
|z_j|=\nu_j+\delta,\qquad \delta\ge1,
\qquad |z_i|\le\nu_i\ (i\ne j).
\tag{2}
\]

以下只在 \(K\) 为奇数时讨论模 4 的结论；这是当前 42 个低模数 F-box miss
输入的实际情形。

## q 幂缺口恒等式

定义有理数

\[
d=K\prod_iq_i^{z_i}.
\tag{3}
\]

由 \(4K\equiv1\pmod t\) 和 (1)，有 \(4d\equiv-1\pmod t\)，其中有理分母均为
\(t\) 上的单位。分两种符号定义整数 \(d_0\mid K^2\)：

\[
\begin{array}{c|c|c}
\text{符号}&d_0&\text{所得整除关系}\\ \hline
z_j=\nu_j+\delta
  &d/q^\delta
  &t\mid4q^\delta d_0+1\\[2mm]
z_j=-\nu_j-\delta
  &q^\delta d
  &t\mid4d_0+q^\delta.
\end{array}
\tag{4}
\]

确实，正号时 \(d=q^\delta d_0\)，且 \(q\) 坐标在 \(d_0\) 中的指数为
\(2\nu_j\)；负号时 \(d=d_0/q^\delta\)，且 \(q\) 坐标在 \(d_0\) 中的指数为零，
其余坐标指数均位于 \([0,2\nu_i]\)。因此两种情形都给出 \(d_0\mid K^2\)。

## Type II 的充分条件

由 (4) 定义端点和商：

\[
\begin{array}{c|c|c|c}
\text{符号}&A&B&M\\ \hline
z_j=\nu_j+\delta
  &1&4q^\delta d_0&(4q^\delta d_0+1)/t\\[2mm]
z_j=-\nu_j-\delta
  &q^\delta&4d_0&(q^\delta+4d_0)/t.
\end{array}
\tag{5}
\]

只要相应的 \(M\) 满足

\[
M\equiv3\pmod4,\qquad 3\le M\le p-2,
\qquad A\le B,\qquad (A,B)=1,
\qquad AB\mid x_M:=\frac{p+M}{4},
\tag{6}
\]

便有 \(A+B=tM\)，所以 \(M\mid A+B\)。令 \(C=x_M/(AB)\)，则

\[
x_M=ABC,\qquad A^2C\mid x_M^2,\qquad A^2C\le x_M,
\]

而 \(M\mid A+B\)。由 Type II 互素因子正规形，\((A,B,C,M)\) 给出 Type II
证书。若负号且 \(q=2\)，应把 \((A,B)=1\) 作为额外假设；当前冻结输入中没有
这样的坐标。

条件 (6) 是充分条件，不是单坐标溢出的自动后果。特别地，(4) 只保证 \(t\) 整除
端点和，不保证 \(M\) 是合法缺口或 \(AB\mid x_M\)。

## 模 (4) 边界与二进终端

在当前 \(K\) 奇数输入中，\(d_0,q\) 均为奇数。于是正号的 \(M\) 必满足

\[
M\equiv1\pmod4,
\]

所以正号的规范端点构造不可能直接产生 Type II 合法缺口。负号则有

\[
M\equiv q^\delta\pmod4;
\]

只有 \(q\equiv3\pmod4\) 且 \(\delta\) 为奇数时，模 4 才允许 \(M\equiv3\pmod4\)。
这仍需满足 (6)。

单坐标溢出也不等于广义二进终端。要从 (1) 得到 \(2^j\equiv-1\pmod t\)，还必须
有 \(q=2\) 且其余盒内坐标的乘积在模 \(t\) 下恰为 1（或已被明确吸收到二进指数中）。
当前 42 个状态的 \(K\) 全部为奇数，故单坐标溢出坐标均为奇素数；记录中的
\(2^j\equiv-1\pmod t\) 不能由这些单坐标溢出自动解释，且二进预算仍为
\(v_2(2K)=1\)。

## 42 状态的有限核对（探索性）

以下数字只用于检验上述分流，不是全称结论。Pareto 前沿脚本完整检查单位溢出成本
\(\ell_1\le9\)，结果文件为

~~~text
reproductions/type-i-f-overflow-lower-modulus-pareto-overflow-results.json
~~~

结果哈希为

~~~text
8fd82842893674641cf15928cf436d872e450b5fd175d47f8a825fad5603c6fe
~~~

42 个状态中，截断前沿有 415 个点，其中 69 个为单坐标点、346 个为多坐标点；
23 个状态至少有一个单坐标 Pareto 点，只有 6 个状态的已发现前沿全部由单坐标点组成。
另有 6 个状态在成本 9 内没有命中；就本 Pareto 截断而言只能得到
\(\Omega_1\ge10\)，后续 Cayley 标量诊断已补齐这六个状态的具体 \(\Omega_1\) 值，
但其完整 Pareto 前沿仍未补齐。因此不能把“单坐标溢出”当作低模数 miss 的普遍终端结构。

独立的最短关系诊断（不是 Pareto 全前沿）对 42 个状态的规范 BFS 代表检查了端点
Type II：33 个因端点积大于 \(p/2\) 被大小界排除，剩余 9 个逐一检查端点和的合法
因子，命中为 0。其输入文件
reproductions/type-i-f-overflow-r-modulus-repair-results.json 的 SHA-256 为

~~~text
c656c91ebb02a33e8d1f5c78db70ce14ac5fbc2decc0db99e05bcbcc1fbee22f
~~~

结果文件为
reproductions/type-i-f-overflow-lower-modulus-shortest-relation-results.json，其 SHA-256 为

~~~text
077f565596f9f06e30aca5c7c6c6de487b455581f9e28801b84950531032ad42
~~~

这个诊断不能排除非最短关系、因子重分配或其它 Type II 形状；它只说明 \((5)\)--\((6)\)
这条规范端点出口在冻结样本中没有自动闭合。

上面的 33/9 分流针对的是“规范 BFS 最短关系”端点；另一份“固定平衡端点对”审计
针对不同的端点对象，结果为 41/42 个状态由大小界排除、1 个小乘积状态，且同样没有
Type II 命中（结果文件为
`reproductions/type-i-f-overflow-balanced-endpoint-type-ii-results.json`）。两组数字
不矛盾，不能互换为统一的 42 状态总体统计。

一个最小的单支撑示例是

\[
p=106050289,\quad R=291,\quad m=3,\quad t=97,
\quad K=5^2\cdot19\cdot23\cdot706193.
\]

向量 \(z=(-3,-1,0,-1)\) 只有 \(q=5\) 越界一层，且

\[
d_0=23,\qquad M=(4\cdot23+5)/97=1.
\]

故规范端点商不是合法缺口；同一修复候选的直接平方命中字段为假。这个例子只反驳
“单坐标溢出必然给出 \((5)\)--\((6)\) 型 Type II”的强断言，不反驳其它 Type II 或更大
关系的可能性。

## 结论边界

单支撑假设目前能严格给出的只有 (4) 及其条件性端点构造。要得到旗舰选择器所需的
Type I/II 或可提升递降，还需额外证明以下至少一项：

1. \(m\mid4q^\delta d_0+1\)（正号）或 \(m\mid4d_0+q^\delta\)（负号），并满足
   对应平方除子条件；
2. 负号端点商 \(M\) 满足 (6)；
3. 溢出层能映入共同 \(q\)-进载体价格，或端点缺口 \(M\) 产生严格可提升的新状态。

因此，这张卡是单坐标溢出的严格算术接口与反例边界，不是 Type I/II 终端定理。
