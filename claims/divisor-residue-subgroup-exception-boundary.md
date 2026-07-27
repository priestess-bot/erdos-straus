---
kind: claim
claim_id: divisor-residue-subgroup-exception-boundary
title: 除子残数避开负一的稳定子群分解及线性异常障碍
statement: 对有限阿贝尔群 G、二阶元 tau 和避开 tau 的子序列积序列 S，令 H 为全部子序列积集合的稳定子群，则 tau 不属于 H，且 S 中至多 [G:H]-2 项落在 H 外；该界在偶阶循环群上取等。更强地，对无穷多个 M=4q，存在真实整数的除子残数序列避开 -1，但相对于任何不含 -1 的子群都至少有 phi(M)/2-2 个异常项。因此“真子群加 o(phi(M)) 个异常项”的普适覆盖为假，无论允许多少结构类。
claim_status: established
topics:
- type-II
- divisor-residues
- additive-combinatorics
- Kneser-theorem
- subgroup-structure
- obstruction
- proof-program
sources:
- paper: grynkiewicz_marchan_ordaz2009
  locator: "Theorem C and Example 2, pp. 566--567"
  role: Kneser-input-and-critical-cyclic-example
- paper: linnik1944
  locator: least-prime theorem in arithmetic progressions
  role: prime-factor-residue-realization
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-application-context
visibility: public
last_checked: '2026-07-24'
---

# 除子残数避开负一的稳定子群分解及线性异常障碍

## 先把命题量化

令 \(G\) 为有限阿贝尔群，单位元记为 \(1\)，并固定二阶元
\(\tau\ne1\)。对有限序列

\[
S=(s_1,\ldots,s_n)
\]

定义全部子序列积集合

\[
\Pi(S)=\prod_{i=1}^n\{1,s_i\}.
\tag{1}
\]

允许空子序列，所以 \(1\in\Pi(S)\)。称 \(S\) **避开 \(\tau\)**，若
\(\tau\notin\Pi(S)\)。当 \(G=(\mathbb Z/M\mathbb Z)^\times\)、
\(\tau=-1\) 时，整数

\[
N=\prod_j\ell_j^{e_j}
\]

对应的序列把 \(\ell_j\bmod M\) 重复 \(e_j\) 次；此时 \(\Pi(S)\) 正是
\(N\) 的全部除子模 \(M\) 的残数集合。

一个对筛法有实际意义的“真子群加短异常序列”类必须取

\[
H<G,\qquad \tau\notin H,
\tag{2}
\]

并要求除至多 \(k\) 项外，所有项都在 \(H\) 中。若允许 \(\tau\in H\)，则
“主体落在 \(H\)”本身完全不能保证避靶，因而不再是所讨论的结构类。

## 正向边界：稳定子群分解

**定理 1。** 若 \(S\) 避开 \(\tau\)，令

\[
H=\operatorname{Stab}(\Pi(S))
 =\{h\in G:h\Pi(S)=\Pi(S)\}.
\tag{3}
\]

则

\[
H<G,\qquad \tau\notin H,
\tag{4}
\]

而且若 \(t\) 是 \(S\) 中不属于 \(H\) 的项数，则

\[
t\le [G:H]-2.
\tag{5}
\]

**证明。** 因 \(1\in\Pi(S)\) 且 \(H\Pi(S)=\Pi(S)\)，有
\(H\subseteq\Pi(S)\)。所以 \(\tau\notin H\)，特别地 \(H\ne G\)。

把 Kneser 定理应用于 \(A_i=\{1,s_i\}\)，并模掉 (3) 中的稳定子群。若
\(s_i\in H\)，则 \(A_iH/H\) 只有一个元素；否则有两个元素。因此

\[
|\Pi(S)/H|
 \ge \sum_{i=1}^n|A_iH/H|-n+1
 =t+1.
\tag{6}
\]

另一方面，\(\Pi(S)\) 是 \(H\)-周期集，而它遗漏 \(\tau\)，故它遗漏整个陪集
\(\tau H\)。于是

\[
|\Pi(S)/H|\le [G:H]-1.
\tag{7}
\]

(6) 与 (7) 合并即得 (5)。证毕。

这个结论还给出精确的商群描述：落在 \(H\) 外的异常项投影到 \(G/H\) 后仍避开
\(\tau H\)，其子序列积集合的稳定子群为平凡群。也就是说，Kneser 分解已经把问题
压到一个非周期的临界核心；不能继续仅靠“再取稳定子群”递归缩短它。

## 抽象 sharpness：异常项可达群阶减二

取偶阶循环群

\[
G=\langle g\rangle\cong C_{2r},\qquad \tau=g^r,
\]

以及序列

\[
S_r=g^{[r-1]}(g^{-1})^{[r-1]},
\tag{8}
\]

其中方括号表示重数。任一子序列积为 \(g^{a-b}\)，其中
\(0\le a,b\le r-1\)。差集

\[
\{a-b\}=[-(r-1),r-1]\pmod {2r}
\]

恰好遗漏指数 \(r\)，所以

\[
\Pi(S_r)=G\setminus\{\tau\}.
\tag{9}
\]

该集合的稳定子群是 \(\{1\}\)，而 (8) 的长度为 \(2r-2=|G|-2\)。因此
(5) 对一般有限阿贝尔群不能改成 \(o([G:H])\)。这正是 Kneser/Kemperman
临界算术级数现象，而不是证明技术造成的松弛。

## 实际单位群中的线性反例

抽象反例还可嵌入 Type II 使用的真实模数。令 \(q\equiv3\pmod4\) 为奇素数，

\[
M=4q,\qquad G_M=(\mathbb Z/M\mathbb Z)^\times,\qquad
r=\frac{q-1}{2}.
\tag{10}
\]

取模 \(q\) 的原根 \(a\)，再由中国剩余定理选择 \(u\) 满足

\[
u\equiv-1\pmod4,\qquad u\equiv a\pmod q.
\tag{11}
\]

因为 \(r\) 为奇数，

\[
\operatorname{ord}_M(u)=q-1=2r,\qquad u^r\equiv-1\pmod M.
\tag{12}
\]

令

\[
T_q=u^{[r-1]}(u^{-1})^{[r-1]}.
\tag{13}
\]

与 (8)--(9) 相同，

\[
\Pi(T_q)=\langle u\rangle\setminus\{-1\},
\tag{14}
\]

故它避开 \(-1\)。若一个子群 \(H\le G_M\) 包含 \(u\) 或 \(u^{-1}\)，则由
(12) 必有 \(-1\in H\)。所以对每个满足 \(-1\notin H\) 的子群，(13) 的每一项
都是异常项。其最小异常数为

\[
|T_q|=q-3=\frac{\varphi(M)}2-2.
\tag{15}
\]

这不是不可实现的形式序列。由算术级数素数定理的存在性部分，可取素数

\[
L_+\equiv u\pmod M,\qquad L_-\equiv u^{-1}\pmod M.
\]

于是

\[
N_q=L_+^{r-1}L_-^{r-1}
\tag{16}
\]

的素因子残数序列就是 (13)，而其真实除子残数集合就是 (14)。

## 对“亚指数结构类覆盖”的否定

把“短”取为筛法所需的次线性尺度

\[
k(M)=o(\varphi(M)),
\tag{17}
\]

并把“亚指数”取为

\[
\exp(o(\varphi(M))).
\tag{18}
\]

则所提覆盖命题为假。事实上，对无穷多个 (10) 中的模数，(15) 表明只要
\(k(M)<\varphi(M)/2-2\)，序列 (13) 就不属于**任何**满足 (2) 的
“子群加至多 \(k(M)\) 个异常项”类。因此即使允许无限多个这样的类也不能覆盖，
当然更不可能由 (18) 个类覆盖。

这里所需的模数确有无穷多个：若 \(q_1,\ldots,q_s\) 是全部
\(3\pmod4\) 素数，则 \(4q_1\cdots q_s-1\equiv3\pmod4\) 必有一个新的
\(3\pmod4\) 素因子，矛盾。

这里“亚指数数量”本来不是主要障碍。阶为 \(n\) 的有限阿贝尔群至多有

\[
n^{\log_2 n}=\exp(O((\log n)^2))
\tag{19}
\]

个子群，因为每个子群可由至多 \(\log_2 n\) 个元素生成。若真有统一的
\(k=o(n)\) 异常界，把异常部分作为无序多重集显式记录，只需至多

\[
n^{\log_2 n}\binom{n+k}{k}=\exp(o(n))
\tag{20}
\]

个 \((H,E)\) 类。反例否定的正是使 (20) 成立的“短异常”前提。

## 对 Type II 路线的含义

这一定理否定的是**所有除子残数序列的普适组合压缩**，并不构造
\(p+4A^2C\) 形式的反例，也不否定有界或缓增 \((A,C)\) 的 Type II 饱和猜想。
移位素数族仍带有跨射线相关性，远比任意整数 (16) 受限。

但下一步结构分类不能只包含“真子群加短异常”。至少必须加入第二种主型：

1. 负一不在其中的子群陷阱；
2. 循环商中的双向临界算术级数，及其 Kemperman 型扰动。

若想把它用于增长参数盒筛法，还需证明实际移位整数不可能在许多射线上同时落入第二型，
或证明第二型本身只有可统一筛除的低熵参数。单条射线上的 Kneser 定理不能完成这一步。
