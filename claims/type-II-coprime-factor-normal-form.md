---
kind: claim
claim_id: type-II-coprime-factor-normal-form
title: Type II 除子证书的互素因子正规形
statement: 固定 p=1 mod 4 与合法缺口 m，令 x=(p+m)/4。Type II 证书除子 d 与满足 x=ABC、d=A^2C、gcd(A,B)=1、A<=B、m|(A+B) 的三元组 (A,B,C) 一一对应。若 K=(A+B)/m，则 (4ACK-1)(4B-1)=4Kp+1-4A(CK-1)；C=K=1 正好给出 4p+1 的因子分支。
claim_status: established
topics:
- certificate
- type-II
- divisor-parametrization
- factorization
- proof-program
sources:
- paper: bradford2024
  locator: "Propositions 2 and 4 (statements; the paper leaves their proofs to the reader)"
  role: Type-II-certificate-statement-context
- paper: chamberland2026
  locator: "Theorem 1"
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-24'
---

# Type II 除子证书的互素因子正规形

## 定理

令 \(p\equiv1\pmod4\) 是素数，\(m\equiv3\pmod4\)、
\(3\le m\le p-2\)，并令 \(x=(p+m)/4\)。Type II 证书除子 \(d\) 与三元组
\((A,B,C)\in\mathbb N^3\) 一一对应，条件为

\[
x=ABC,\qquad d=A^2C,\qquad \gcd(A,B)=1,
\qquad A\le B,\qquad m\mid A+B.
\]

令

\[
K=\frac{A+B}{m}.
\]

则 \(p=4ABC-m\) 还给出精确的因子恒等式

\[
(4ACK-1)(4B-1)=4Kp+1-4A(CK-1). \tag{1}
\]

特别地，\(C=K=1\) 时

\[
4p+1=(4A-1)(4B-1),
\]

这正是 `four-p-plus-one-type-ii-certificate` 所利用的因子扇区。

若同时要求 Bradford 恢复的两个非首分母都整除 \(px\)，则必且只须 \(K=1\)：
恢复式为 \(y=pACK\)、\(z=pBCK\)，故这两个整除性分别给出 \(K\mid B\)、
\(K\mid A\)，再由 \(\gcd(A,B)=1\) 得结论。对 \(p\equiv1\pmod{24}\)，这正是
Xu 所称 tame 的切片，见 `type-II-tame-k-one-equivalence`。

## 等价的因子生成器

上述坐标还给出一个无需先枚举 \(m\) 或 \(d\) 的等价构造。对正整数
\(A,C,K\)，令

\[
q=4ACK-1.
\]

则 \(p\) 有一个对应的 Type II 证书，当且仅当

\[
q\mid Kp+A,\qquad B=\frac{Kp+A}{q},\qquad
\gcd(A,B)=1,\quad A\le B. \tag{2}
\]

在此情形下

\[
m=\frac{A+B}{K},\qquad x=ABC,\qquad d=A^2C
\]

自动是自然范围 \(3\le m\le p-2\) 内的 Type II 证书。因而全部 Type II
证书可精确地搜索为某个形如 \(4ACK-1\) 的因子整除仿射数 \(Kp+A\)。

这里的互素性使 \((A,B,C)\) 成为唯一坐标，而非直接证书构造所必需。若从因子式得到
\(A\le B\) 但 \(\gcd(A,B)>1\)，仍可直接取 \(x=ABC,d=A^2C\) 获得 Type II
证书；它随后归一化为不同的互素三元组。精确的冗余消除见
`type-II-raw-ray-certificate`。

这个因子也满足

\[
q\mid p+4A^2C. \tag{3}
\]

两个边界切片分别复现已知分支：\(A=C=1\) 时，(2) 蕴含
\(4K-1\mid p+4\)，对应 \(d=1\) 的 \(p+4\) 分支；\(C=K=1\) 时，(2)
蕴含 \(4A-1\mid4p+1\)，对应 `four-p-plus-one-type-ii-certificate`。

## 证明

先给定 Type II 证书 \(d\mid x^2\)、\(d\le x\)、\(m\mid x+d\)。令

\[
g=\gcd(d,x),\qquad A=\frac dg,\qquad B=\frac xg.
\]

则 \(\gcd(A,B)=1\)。由 \(d\mid x^2\) 得 \(Ag\mid B^2g^2\)，故
\(A\mid B^2g\)；互素性推出 \(A\mid g\)。写 \(C=g/A\)，便有

\[
x=ABC,\qquad d=A^2C.
\]

不等式 \(d\le x\) 等价于 \(A\le B\)。又 \(\gcd(x,m)=1\)，所以
\(\gcd(AC,m)=1\)。从

\[
x+d=AC(A+B)
\]

可消去 \(AC\)，得到 \(m\mid A+B\)。这给出正向映射。

反向地，设三元组满足所列条件。则 \(d=A^2C\mid x^2\)，而 \(A\le B\) 给出
\(d\le x\)，且

\[
x+d=AC(A+B)
\]

被 \(m\) 整除，故确为 Type II 证书。由 \(g=AC\) 可反向恢复
\(A=d/g\)、\(B=x/g\)、\(C=g/A\)，因而映射唯一。

最后，\(Km=A+B\) 以及 \(p=4ABC-m\) 给出

\[
\begin{aligned}
4Kp+1-4A(CK-1)
 &=16KABC-4(A+B)+1-4ACK+4A\\
 &=16ACKB-4ACK-4B+1\\
 &=(4ACK-1)(4B-1),
\end{aligned}
\]

即 (1)。取 \(C=K=1\) 立即得到最后的分解式。

对因子生成器，正向由 \(Km=A+B\) 和 \(p=4ABC-m\) 直接计算：

\[
Kp+A=4KABC-(A+B)+A=B(4ACK-1)=qB.
\]

反向地，假设 (2)。因为 \(q\equiv-1\pmod K\)，等式 \(qB=Kp+A\)
模 \(K\) 化简为 \(A+B\equiv0\pmod K\)，故 \(m=(A+B)/K\) 是整数。再有

\[
Kp=qB-A=4ACKB-(A+B)=K(4ABC-m),
\]

所以 \(p=4ABC-m\)。由 \(A\le B\) 得

\[
m\le A+B\le2B\le2ABC.
\]

等号会迫使 \(K=A=B=C=1\)，从而 \(p=2\)，与 \(p\equiv1\pmod4\)
矛盾。因此 \(m<2ABC\)，于是 \(0<m<p\)。又
\(m=4ABC-p\equiv3\pmod4\)，故实际上 \(3\le m\le p-2\)。前一节的
反向构造遂给出 Type II 证书。最后，将
\(p=qm-4A^2C\) 模 \(q\) 化简即得 (3)。

## 对短证书或递降计划的含义

这个正规形没有证明每个 \(p\) 都有 Type II 证书，但它将整个 Type II 搜索压缩为
互素因子对 \((A,B)\) 和一个整除条件。特别地，`4p+1` 分支仅是
\(C=K=1\) 的边界；未被该分支覆盖时，仍存在 \(C>1\) 或 \(K>1\) 的内部
Type II 证书空间可供研究。因子生成器也把潜在短证书目标转为对小
\((A,C,K)\) 的整除覆盖问题。它不是从较小实例的解构造 \(p\) 的解，故不构成递降。
