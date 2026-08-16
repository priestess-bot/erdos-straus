---
kind: claim
claim_id: type-I-g-anchor-strict-q-carried-quadratic-external-source-classification
title: G-anchor 严格 Q-carried 平方因子 external-source 的完整分类
statement: >-
  对核心素数 p=1 (mod 24)，令 Q=(p-3)/2。对每个正整数 k|(p-1)/4，令
  q=4k-1、n=(qp+1)/(q+1)、M=kn。平方因子 external-source 中额外满足
  e|Q 的 witness 完全分类如下：当 k>=2 时不存在；当 k=1 时存在当且仅当
  p=73 (mod 120)，且唯一为 e=5。正例给出 n<p 的显式 marked lift 和
  (m,D)=(7,u^2/5) 的 Type I 证书。证明使用精确恒等式
  gcd(Q,M^2)=gcd(Q,(3q+1)^2) 及互补因子界。结论只覆盖严格 e|Q；
  e 不整除 Q 但满足 e|M^2 的一般平方因子机制仍可能成功。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-jacobi-odd-complete-excess-source-menu
  - type-I-g-anchor-q-carried-external-source-witness-classification
  - quadratic-factor-external-source-descent
topics:
  - type-I
  - G-state
  - G-anchor
  - complete-excess-bundle
  - external-source
  - quadratic-factor
  - marked-descent
  - q-3
  - gcd-intersection
  - capacity-map
  - proof-boundary
sources:
  - claim: type-I-g-anchor-jacobi-odd-complete-excess-source-menu
    role: actual-Q-carrier
  - claim: type-I-g-anchor-q-carried-external-source-witness-classification
    role: linear-Q-carried-gcd-identity-and-q-three-exception
  - claim: quadratic-factor-external-source-descent
    role: complete-square-factor-lift-and-Type-I-certificate-contract
  - reproduction: reproductions/type_i_g_anchor_strict_q_carried_quadratic_external_source_classification.py
    role: strict-Q-square-factor-controls-and-non-strict-boundary
visibility: public
last_checked: '2026-08-16'
---

# G-anchor 严格 \(Q\)-carried 平方因子 external-source 的完整分类

## 1. 严格 \(Q\)-carried 的范围

固定核心素数

\[
p\equiv1\pmod{24},\qquad Q=\frac{p-3}{2}.
\tag{1}
\]

对任意正整数

\[
k\mid\frac{p-1}{4},\qquad q=4k-1,\qquad
n=\frac{qp+1}{q+1},\qquad M=kn,
\tag{2}
\]

平方因子 external-source 的完整条件是

\[
e\mid M^2,\qquad e\le M,\qquad e\equiv-M\pmod q.
\tag{3}
\]

本卡中的“严格 \(Q\)-carried”只指

\[
e\mid Q.
\tag{4}
\]

这比“\(e\) 的某个素因子也整除 \(Q\)”更窄，故结论不会误排除一般平方因子机制。
在 (3)--(4) 内有完整分类：

\[
\boxed{
\begin{array}{c|c}
k&\text{严格 \(Q\)-carried 平方因子 witness}\\
\hline
1&\text{当且仅当 }p\equiv73\pmod{120}\text{，唯一为 }e=5\\
k\ge2&\text{不存在}
\end{array}}
\tag{5}
\]

## 2. 平方公共载体的精确公式

由已知的线性恒等式

\[
(Q,M)=(Q,3q+1)
\tag{6}
\]

得到

\[
\begin{aligned}
(Q,M^2)
&=(Q,(Q,M)^2)\\
&=(Q,(Q,3q+1)^2)\\
&=\boxed{(Q,(3q+1)^2)}.
\end{aligned}
\tag{7}
\]

第一行只须逐素数比较赋值：对任意素数 \(\ell\)，
\(\min(v_\ell(Q),2v_\ell(M))\) 只依赖
\(\min(v_\ell(Q),v_\ell(M))\)。此外，令

\[
H=\frac{p-1}{4}.
\tag{8}
\]

有 \(n=p-H/k\ge p-H=(3p+1)/4>Q\)，故 \(M\ge n>Q\)。
因此在严格 \(e\mid Q\) 的范围中，(3) 的尺度条件 \(e\le M\) 自动成立；候选集合
恰为

\[
\left\{
e:e\mid(Q,(3q+1)^2),\quad q\mid4e+1
\right\}.
\tag{9}
\]

这里最后一个整除条件来自 \(4M=qp+1\)，所以
\(4M\equiv1\pmod q\)。

## 3. \(k\ge2\) 的严格平方因子 no-go

设 \(k\ge2\)。则 \(q\equiv3\pmod4\)、\(q\ge7\)。反设存在 (3)--(4) 的
\(e\)。因为 \(Q\) 为奇数，\(e\) 为奇数。写

\[
s=\frac{3q+1}{2}=6k-1.
\tag{10}
\]

由 (7)，\(e\mid s^2\)。又 (3) 与 \(4M\equiv1\pmod q\) 给出

\[
4e\equiv-1\pmod q.
\tag{11}
\]

令

\[
t=\frac{4e+1}{q}.
\tag{12}
\]

因 \(q\equiv3\pmod4\) 而 \(4e+1\equiv1\pmod4\)，有
\(t\equiv3\pmod4\)，特别地 \(t\ge3\) 及

\[
e\ge\frac{3q-1}{4}.
\tag{13}
\]

令 \(L=s^2/e\)。由

\[
4eL=(3q+1)^2
\tag{14}
\]

模 \(q\) 化简并使用 (11)，得到

\[
L\equiv-1\pmod q.
\tag{15}
\]

另一方面，(13) 给出

\[
0<L\le\frac{(3q+1)^2}{3q-1}<3q+4.
\tag{16}
\]

故 \(L\in\{q-1,2q-1,3q-1\}\)。但 \(s,e\) 都是奇数，故 \(L\) 也是奇数；
这只留下

\[
L=2q-1.
\tag{17}
\]

又 \(L\mid s^2\)，且 \(2(3q+1)=6q+2\equiv5\pmod L\)，所以

\[
2q-1=L\mid25.
\tag{18}
\]

当 \(q\ge7\) 时，唯一可能的正因子会迫使 \(2q-1=25\)，即 \(q=13\)，
但 \(13\not\equiv3\pmod4\)。矛盾。这证明 \(k\ge2\) 时 (3)--(4) 的候选为空。

## 4. 唯一的 \(q=3\) 例外与显式证书

若 \(k=1\)，则 \(q=3\)、\(M=n\)。式 (7) 给出

\[
(Q,n^2)=(Q,100).
\tag{19}
\]

\(Q\) 是奇数，故 \(e\) 只能是 \(1,5,25\) 的因子；而
\(3\mid4e+1\) 只允许 \(e=5\)。于是

\[
e=5
\quad\Longleftrightarrow\quad
5\mid Q
\quad\Longleftrightarrow\quad
p\equiv73\pmod{120}.
\tag{20}
\]

写 \(p=120t+73\)。则

\[
n=90t+55,\qquad
u=\frac{n+5}{3}=30t+20,\qquad
v=\frac{nu}{5}.
\tag{21}
\]

所以 \(e=5\) 给出

\[
\frac4n=\frac1n+\frac1u+\frac1v
\quad\Longrightarrow\quad
\frac4p=\frac1{np}+\frac1u+\frac1v,
\tag{22}
\]

以及显式 Type I 证书

\[
(m,D)=\left(7,\frac{u^2}{5}\right).
\tag{23}
\]

## 5. 必须保留的非严格边界

结论不允许替换为“所有平方因子都不能来自 \(Q\)”。例如

\[
p=409,\qquad k=6,\qquad q=23,\qquad
n=392,\qquad M=2352,\qquad e=63
\tag{24}
\]

满足 (3)，并给出真实平方因子 external-source lift；但

\[
Q=203,\qquad 63\nmid203.
\tag{25}
\]

它含有与 \(Q\) 共同的素因子 \(7\)，却不是严格 \(Q\)-carried 因子。因而后续若要
研究全局剩余，只能说 (5) 已清空 \(e\mid Q\) 的接口，不能把 (5) 外推到
non-strict support 或非 \(Q\)-carried \(e\)。更强地，
[\(Q\)-supported 幂借用射线](type-I-g-anchor-q-supported-power-external-source-ray.md)
给出无穷多个 \(\operatorname{rad}(e)\mid Q\) 但 \(e\nmid Q\) 的有效 witness；因此
这里的“严格”必须保留为整除关系，不能替换成素因子支撑关系。

## 6. 定向回执

~~~bash
python3 reproductions/type_i_g_anchor_strict_q_carried_quadratic_external_source_classification.py --verify
~~~

回执检查 \(p=73,k=1,e=5\) 的正例、三个严格 \(Q\)-内空控制，以及
\(p=409,k=6,e=63\) 的非严格平方因子边界。它不扫描素数范围、分母或 Reach history。
