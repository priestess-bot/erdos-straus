---
kind: claim
claim_id: type-I-b1-square-essential-same-gap-nonoverlap-ray
title: B等于一p减一桥的无界平方缺额同缺口非重叠射线
statement: 对每个a>=1，存在无穷多个核心素数，每个都有B=1的p减一Type I终端桥，令t=(p-1)/4、r=(R+1)/4，则v_2(r)=2a且v_2(t)=a。因此桥条件r|t^2成立但r∤t，同一正规形不能回缩为完整外源；同时同一缺口没有普通Type II双尾证书。故p减一桥的二进平方缺额无绝对上界，即使排除同缺口Type II取代。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- type-II
- b1
- p-minus-one
- square-divisibility
- external-source
- same-gap
- dirichlet
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-and-Type-II-certificate-context
visibility: public
last_checked: '2026-07-28'
---

# \(B=1\) \(p-1\) 桥的无界平方缺额同缺口非重叠射线

这里的平方缺额指对 \(p-1\) 桥的

\[
t=\frac{p-1}{4},\qquad r=\frac{R+1}{4}
\]

而言，桥只要求 \(r\mid t^2\)，而外源回缩要求更强的 \(r\mid t\)。

## 定理

对任意整数 \(a\ge1\)，令

\[
r=2^{2a},\qquad q=5,\qquad m=4q-1=19,\qquad
R=4r-1,\qquad C=mr-q=19r-5.
\tag{1}
\]

取唯一的 \(A_0\pmod M\)，其中

\[
M=15\cdot2^{a+1},
\tag{2}
\]

满足

\[
A_0+1\equiv2^a\pmod {2^{a+1}},\qquad
A_0\equiv1\pmod3,\qquad
A_0\equiv2\pmod5.
\tag{3}
\]

对每个 \(z\ge0\)，置

\[
A=A_0+Mz,\qquad
p=4AC-m=(4CM)z+(4CA_0-m).
\tag{4}
\]

则 (4) 是原始的 \(1\pmod {24}\) 等差进程，故含无穷多个素数。对每个这样的素数：

\[
\begin{aligned}
&(A,1,C)\text{ 是缺口 }m=19\text{ 的 Type I 正规形；}\\
&\text{源 }n=p-1\text{、桥因子 }E=4r\text{ 给出偶终端桥；}\\
&v_2(t)=a<2a=v_2(r),\quad
v_2(E)-v_2(p-1)=a;\\
&r\nmid K,\quad E\nmid p-1,\quad q\nmid Ar.
\end{aligned}
\tag{5}
\]

因此该桥是平方本质的，不能按同一正规形回缩为完整平方因子外源；而同一缺口没有普通
Type II 双尾证书。随着 \(a\) 任意增大，平方缺额也无界。

## 证明

三个模数 \(2^{a+1},3,5\) 两两互素，故 (3) 由 CRT 有唯一模 \(M\) 的解。它使
\(A\) 为奇数且 \(A\equiv1\pmod3\)，所以 \(A\equiv1\pmod6\)。另一方面
\(r=4^a\equiv4\pmod6\)，从而

\[
C=19r-5\equiv5\pmod6,\qquad
p=4AC-19\equiv1\pmod {24}.
\tag{6}
\]

令 \(P=4CM\)、\(p_0=4CA_0-19\)。由 \(p_0\equiv-19\pmod C\) 及
\(C=19r-5\)，可知 \((C,p_0)=1\)。式 (6) 给出 \((6,p_0)=1\)。最后，模 \(5\) 有

\[
p_0\equiv4(4r)A_0-4\equiv2r-4\not\equiv0\pmod5,
\tag{7}
\]

因为 \(r\equiv\pm1\pmod5\)。故 \((P,p_0)=1\)。Dirichlet 定理遂给出 (4) 中无穷多个
素数项。

恒等式 \(mR=4C+1\) 给出 \(B=1\) 正规形。对其 \(p-1\) 桥，使用

\[
t=\frac{p-1}{4}=AC-q=19Ar-5(A+1).
\tag{8}
\]

式 (3) 给出 \(v_2(A+1)=a\)。由于 \(A\) 和 \(19\) 都是奇数，(8) 的第一项具有
二进赋值 \(2a\)，第二项具有二进赋值 \(a\)，所以

\[
v_2(t)=a.
\tag{9}
\]

于是 \(r=2^{2a}\mid t^2\)，却 \(r\nmid t\)。由
[p减一桥判据](type-I-normal-pminusone-upper-half-bridge.md) 获得桥因子 \(E=4r\)；
[外源回缩判据](type-I-b1-external-source-retraction-criterion.md) 把
\(r\nmid t\) 等价为 \(r\nmid K\)，也等价为 \(E\nmid p-1\)。又

\[
v_2(E)-v_2(p-1)=(2a+2)-(a+2)=a.
\tag{10}
\]

最后，\(A\equiv2\pmod5\)，而 \(5\nmid r\)，故 \(q=5\nmid Ar\)。由
[B等于一同缺口二分](type-I-b1-pminusone-same-gap-dichotomy.md)，同缺口普通 Type II
双尾不存在。这证明全部断言。

## 样本

取各 \(a\) 的最小正素数项，可得

\[
\begin{array}{c|c|c}
a & z & p\\ \hline
1&1&27529\\
2&1&223633\\
3&0&33889\\
4&5&53779393\\
5&6&495378049
\end{array}
\]

样本只作回归；无穷性及无界性来自上述参数化证明。

## 范围

本定理不排除这些素数在其他缺口拥有普通 Type II 证书，也不排除另一个 Type I 正规形
可回缩为外源。因此它不是 Erdős--Straus 猜想或原混合选择引理的反例。它排除的是一类
过窄归约：对 \(p-1\) Type I 终端桥施加任何绝对有界的二进平方缺额，并指望由同缺口
普通 Type II 补齐其余情形。
