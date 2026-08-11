---
kind: claim
claim_id: type-I-g-anchor-r11-fixed-tail-residual-classification
title: R=11 固定尾未命中的精确素因子分类
statement: 设 p=24h+1 为核心素数、N=22h+1、K=3N。固定第三分母 pK 的 R=11 Type I terminal 不存在，当且仅当 N 的素因子满足下列两种互斥情形之一：(i) 每个素因子均为模 11 二次剩余；(ii) N=ell_2 ell_6 A，其中 ell_2=2 (mod 11)、ell_6=6 (mod 11) 为各出现一次的素数，且 A 的每个素因子均为 1 (mod 11)。在其余每一种情形中，都可构造 d|N^2 且 d=7,8,10 (mod 11)，因而给出原始 p 的直接固定尾 Type I 终端。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-r11-adaptive-divisor-terminal
topics:
  - type-I
  - terminal-first
  - R11
  - fixed-tail
  - factorization
  - quadratic-residue
  - residual-classification
  - proof-boundary
sources:
  - claim: type-I-g-anchor-r11-adaptive-divisor-terminal
    role: complete-R11-divisor-box-and-terminal-construction
  - reproduction: reproductions/type_i_g_anchor_r11_adaptive_divisor_terminal.py
    role: finite-residue-classification-controls
visibility: public
last_checked: '2026-08-12'
---

# \(R=11\) 固定尾未命中的精确素因子分类

## 1. 设置

令

\[
p=24h+1,
\qquad
N=22h+1,
\qquad
K=3N.
\tag{1}
\]

于是

\[
N\equiv1\pmod {11},
\qquad (N,11)=1.
\tag{2}
\]

已有的完整 \(R=11\) 固定尾判据说明，第三分母固定为 \(pK\) 的
Type I terminal 存在，当且仅当

\[
\mathcal B(N):=\{d\bmod {11}:d\mid N^2\}
\quad\hbox{与}\quad
T:=\{7,8,10\}
\tag{3}
\]

相交。这里 \(T\) 正是 \(\mathbb F_{11}^{\times}\) 的三个二次非剩余
目标类。

记

\[
Q:=\{1,3,4,5,9\},
\qquad
a=\Omega_2(N),\quad b=\Omega_6(N),
\tag{4}
\]

其中 \(\Omega_r(N)\) 是 \(N\) 的所有素因子（按重数计）中模 \(11\)
同余 \(r\) 的个数。\(2\) 和 \(6\) 是不在 \(T\) 内的两个二次非剩余类。

## 2. 精确分类定理

**定理。** 下列两项等价：

\[
\mathcal B(N)\cap T=\varnothing;
\tag{5}
\]

\[
\boxed{
\begin{array}{ll}
\text{(QR)}&\text{每个素数 }\ell\mid N\text{ 都满足 }\ell\bmod11\in Q;\\[2mm]
\text{(2,6)}&N=\ell_2\ell_6A,\quad
 \ell_2\equiv2,\quad\ell_6\equiv6\pmod {11},\\
&\ell_2,\ell_6\text{ 各以一次幂出现，且每个 }q\mid A\text{ 满足 }q\equiv1\pmod {11}.
\end{array}}
\tag{6}
\]

两种情形互斥。特别地，固定尾残余并不只是“没有一个目标残类因子”：
它要么完全落在二次剩余半群中，要么只能保留那一对严格配对的
\(2\)-和 \(6\)-类因子。

**证明。** 取 \(2\) 为 \(\mathbb F_{11}^{\times}\) 的生成元。各非零类的
离散对数为

\[
\begin{array}{c|cccccccccc}
r&1&2&3&4&5&6&7&8&9&10\\ \hline
\log_2 r&0&1&8&2&4&9&7&3&6&5.
\end{array}
\tag{7}
\]

故 \(Q\) 对应偶指数，\(2\) 与 \(6\) 对应奇指数 \(1,9\)，而
\(T\) 对应奇指数 \(7,3,5\)。

若 \(N\) 有一个素因子落在 \(T\)，它本身就是 (3) 中的所求 \(d\)。所以在
未命中情形可先假设所有素因子都落在 \(Q\cup\{2,6\}\)。由 \(N\equiv1\pmod {11}\)
和 (7) 对 \(2\) 取模，得到

\[
a+b\equiv0\pmod2.
\tag{8}
\]

若 \(a\ge2\)，则从所有 \(2\)-类素因子的 \(N^2\)-指数盒中选出总指数 \(3\)，
得到 \(d\mid N^2\) 且 \(d\equiv2^3=8\pmod {11}\)。同理，若 \(b\ge2\)，
选出总指数 \(3\) 得

\[
d\equiv6^3=7\pmod {11}.
\tag{9}
\]

因此未命中迫使 \(a,b\le1\)。结合 (8)，只有

\[
(a,b)=(0,0)\quad\hbox{或}\quad(1,1).
\tag{10}
\]

第一种正是 (QR)。在第二种中，若另有一个素因子
\(q\equiv3,4,5,9\pmod {11}\)，则分别取

\[
\ell_6q\equiv7,
\qquad
\ell_2q\equiv8,
\qquad
\ell_2q\equiv10,
\qquad
\ell_2q\equiv7
\pmod {11}
\tag{11}
\]

便再次命中 \(T\)。所以所有其余素因子只能为 \(1\pmod {11}\)，这正是
(2,6)。

反过来，(QR) 中每个 \(N^2\) 的因子都是二次剩余，故不在 \(T\)。在 (2,6) 中，
任意因子模 \(11\) 形如 \(2^i6^j\)，其中 \(0\le i,j\le2\)，因而只落在

\[
\{1,2,3,4,6\},
\tag{12}
\]

也不与 \(T\) 相交。证毕。

## 3. 构造性终端后果

定理的反面不仅证明存在性，还给出一个有限的 selector：

\[
\begin{array}{c|c}
\text{检测到的因子模式}&d\mid N^2\text{ 的目标残类}\\ \hline
q\equiv7,8,10&d=q\\
\Omega_2(N)\ge2&d\text{ 为三个 }2\text{-类因子的乘积， }d\equiv8\\
\Omega_6(N)\ge2&d\text{ 为三个 }6\text{-类因子的乘积， }d\equiv7\\
\Omega_2(N)=\Omega_6(N)=1,\ q\equiv3,4,5,9&d\text{ 取 (11) 中相应的二因子积}.
\end{array}
\tag{13}
\]

把该 \(d\) 送入完整 \(R=11\) divisor-box 构造，即恢复原始 \(p\) 的
直接 Type I terminal。故需要继续研究的固定尾残余已从任意因子模式收缩到 (6) 的
两类明确半群。

## 4. 控制与边界

* \(p=73\) 时 \(N=67\equiv1\pmod {11}\)，属于 (QR)，故固定 \(pK\) 尾未命中。
* \(p=241\) 时 \(N=13\cdot17\)，其中 \(13\equiv2\)、\(17\equiv6\pmod {11}\)，
  属于 (2,6)，并恢复既有残类盒 \(\{1,2,3,4,6\}\)。
* 例如抽象因子型 \(3\cdot13\cdot17\cdot37\equiv1\pmod {11}\) 同时含一对
  \(2,6\) 因子及 \(3,4\) 类因子；(11) 取 \(d=17\cdot3\equiv7\)，说明第二类中
  任意非 \(1\) 的二次剩余因子都会立即离开残余。

这是固定第三分母 \(pK\) 的精确分类，不是 Erdős--Straus 反例，也不声称 (QR) 或
(2,6) 的每个核心素数没有其它 Type I/II 终端或严格递降。

复现：

```bash
python3 reproductions/type_i_g_anchor_r11_adaptive_divisor_terminal.py --verify
```
