---
kind: claim
claim_id: eight-branch-sieve-residual
title: 加入内部 (4,3) 分支后的共同残余有 5 维筛界
statement: 令 R_8(X) 为核心素数中同时未被七条既有因子证书分支和 3p+4 的内部 (A,B)=(4,3) Type I 分支覆盖的数目，则 R_8(X)=O(X/(log X)^5)。这只是在已知分支交集上的稀疏性结果，不产生逐点选择器或递降。
claim_status: established
topics:
- sieve
- density
- certificate
- type-I
- internal-parameter
- residual-set
- proof-program
sources:
- paper: elsholtz_tao2013
  locator: "Appendix A, shifted-prime additive functions and sieve estimates"
  role: methodological-foundation
- paper: bradford2024
  locator: "Proposition 1"
  role: Type-I-certificate-equivalence
visibility: public
last_checked: '2026-07-23'
---

# 加入内部 \((4,3)\) 分支后的共同残余有 \(5\) 维筛界

令 \(R_8(X)\) 是 `seven-branch-sieve-residual` 的共同残余中还没有
`three-p-plus-four-internal-type-I-certificate` 证书的核心素数数目。则

\[
R_8(X)\ll\frac{X}{(\log X)^5}. \tag{1}
\]

## 成对素因子的充分条件

完整的内部 \((4,3)\) 判据允许组合因子。令

\[
t=
\begin{cases}
47,&p\equiv1\pmod{48},\\
23,&p\equiv25\pmod{48}.
\end{cases}
\]

则 \(3p+4\equiv7\) 或 \(31\pmod{48}\)，而内部证书条件正是存在一个因子
\(m\equiv t\pmod{48}\)。又 \(3p+4\) 为奇数且 \(1\pmod3\)，故其全部素因子
都属于模 \(48\) 的 16 个单位类。对任意单位残数 \(r\)，令

\[
r^*=tr^{-1}\pmod{48}. \tag{2}
\]

若 \(3p+4\) 同时有残数为 \(r,r^*\) 的两个素因子，则其乘积是一个
\(t\pmod{48}\) 的因子，因而给出内部 \((4,3)\) 证书。目标 \(t\) 本身作为
素因子时当然也直接给出证书。

两个目标都没有模 \(48\) 的平方根，故 \(r\mapsto r^*\) 将 16 个单位类分成
8 个互不相交的二元组。它们显式为

\[
\begin{array}{c|c}
t&\{r,r^*\}\ \text{的八个二元组}\\
\hline
47&\{1,47\},\{5,19\},\{7,41\},\{11,13\},
\{17,31\},\{23,25\},\{29,43\},\{35,37\}\\
23&\{1,23\},\{5,43\},\{7,17\},\{11,37\},
\{13,35\},\{19,29\},\{25,47\},\{31,41\}.
\end{array} \tag{3}
\]

因此，分支失败时每一对至多出现一个素因子残数，并且 \(t\) 不出现。把实际出现的
残数逐对补齐，可得一个含 8 个单位类的横截面 \(T\)，使 \(3p+4\) 的所有素因子
都落在 \(T\) 中。对第一对必须选择 \(1\) 而不是 \(t\)，所以每个目标至多有
\(2^7\) 个这种横截面。这是**失败的必要条件**；横截面内三个或更多素因子的积仍可能
给出 \(t\)，所以它没有被误写成精确分类。

## 筛法证明

`six-branch-sieve-residual` 的局部禁类数按 \(\ell\pmod{24}\) 为

\[
\begin{array}{c|rrrrrrrr}
\ell\pmod{24}&1&5&7&11&13&17&19&23\\
\hline
\nu_6(\ell)&1&4&5&6&2&3&4&7.
\end{array} \tag{4}
\]

`p-plus-six-external-source-certificate` 的失败分成两个系统。对每个系统，
`seven-branch-sieve-residual` 在 (4) 上额外加入 \(p+6\) 的一个禁类：

\[
\begin{array}{c|c|c}
\text{失败系统}&\text{增加禁类的 }\ell\pmod{24}&
\sum\nu_7(\ell)\\
\hline
H_1&5,11,17,23&36\\
H_2&13,17,19,23&36.
\end{array} \tag{5}
\]

这给出原有的平均维数 \(36/8=9/2\)。固定 \(p\pmod{48}\)、\(H_j\) 和一个
横截面 \(T\)。分支失败还要求 \(3p+4\) 的素因子避开 \(T\) 的补集；该补集在
16 个可逆模 \(48\) 素数类中恰有 8 个。因此把 (4) 提升到模 \(48\) 后，局部
禁类数之和从 \(2\cdot36=72\) 增至 \(80\)，平均维数为

\[
\frac{80}{16}=5. \tag{6}
\]

除有限个素数外，这个新增根与全部既有线性式的根不同：任意两条线性式根重合会使
该素数整除它们的一个固定非零行列式。故它们只改变筛积的常数。由算术级数中的
Mertens 定理，有限个（\(p\pmod{48}\)、\(H_j\) 与横截面 \(T\)）筛系统各有

\[
V(z)\asymp(\log z)^{-5}.
\]

对每个系统应用与 `seven-branch-sieve-residual` 相同的 Selberg 上界筛，再对有限个
系统求和，即得 (1)。

## 边界

这个结果只使用成对素因子，未利用横截面内三个或更多因子的额外覆盖，因而没有宣称
指数 \(5\) 最优。它也不把密度零残余误作空集：\(p=5569\) 仍未被这八条指定
分支覆盖（并且 \(3p+4=16711\) 没有 \(47\pmod{48}\) 因子），但它确有另一张
Type I 证书。故全称的“短证书或递降”引理仍缺少逐点强制机制。
