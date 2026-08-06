---
kind: claim
claim_id: type-II-gap27-square-carrier-strict-descent
title: gap 27 的平方子群载体、残类扇与严格递降
statement: 对素数 p 的 gap m=27，若 x=(p+27)/4 与 27 互素，且 x 含有一个模 27 的非平方素因子，同时一个因子 F|x 的 signed ratio box 等于 U(27) 的平方子群，则完整 Type II factor-pair 层命中并严格递降到 (p+27)/28。对核心域，严格递降恰要求 7|h；其中 h=7t、91|(6t+1) 时 F=7^2*13 是完整平方载体，而 W=6t+1 的单个素因子落在 20、23、26 (mod 27) 时有三条显式 factor-pair 扇。再加 5|(6t+1) 得到 p=76440u+63673 的无穷 Dirichlet 射线。所有结果都只作用于 gap 27 的指定容量子支，不构成全核心覆盖。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-coprime-factor-normal-form
  - short-certificate-equivalence
  - type-II-factor-pair-carrier-strict-descent
  - denominator-escape-state-contract
topics:
  - type-II
  - gap-twenty-seven
  - strict-descent
  - factor-pair
  - composite-modulus
  - square-subgroup
  - Dirichlet-ray
  - proof-boundary
sources:
  - claim: type-II-coprime-factor-normal-form
    role: factor-pair-Type-II-normal-form
  - claim: type-II-factor-pair-carrier-strict-descent
    role: strict-two-tail-lift-and-prime-modulus-carrier-pattern
  - concept: denominator-escape-state-contract
    role: terminal-first-boundary
visibility: public
last_checked: '2026-08-06'
---

# gap \(27\) 的平方子群载体、残类扇与严格递降

## 1. 模 \(27\) 的平方载体

令 \(p\) 为素数，并令

\[
x=\frac{p+27}{4},\qquad
28\mid p-1,\qquad
n=\frac{p+27}{28}.
\tag{1}
\]

假设 \((x,27)=1\)。记 \(U(27)\) 的平方子群为

\[
\operatorname{QR}_{27}=\{u^2:u\in U(27)\}.
\tag{2}
\]

\(U(27)\) 是阶 \(18\) 的循环群，故 \(\operatorname{QR}_{27}\) 的阶为 \(9\)，且
\(-1\notin\operatorname{QR}_{27}\)。

**引理（复合模数平方载体）。** 若

\[
F\mid x,\qquad
\mathcal R_{27}(F)=\operatorname{QR}_{27},
\tag{3}
\]

则 gap \(27\) 的完整 Type II factor-pair 层命中，当且仅当 \(x\) 含有一个
模 \(27\) 的非平方素因子。

**证明。** 若 \(\ell\mid x\) 是非平方，则 \(-\ell\) 是平方。由 (3) 可取
互素 \(a,b\mid F\) 使

\[
a/b\equiv-\ell\pmod{27}.
\tag{4}
\]

因为 (3) 强制 \(F\) 的每个素因子为平方，\(\ell\nmid F\)；又 \((a,b)=1\) 给出
\(ab\mid F\)。令

\[
(A,B,C)=(a,b\ell,x/(ab\ell)),
\tag{5}
\]

必要时交换 \(A,B\)，便有 \(A+B\equiv0\pmod{27}\)，从而得到 Type II
factor-pair certificate。反向时，若 \(x\) 的所有素因子均为平方，任意 \(A/B\)
都是平方，不能等于 \(-1\)。证毕。

在这个 \(28\mid p-1\) 条件下，任一命中都由 factor-pair two-tail lift 给出

\[
\frac4n=\frac1{ABC}+\frac1{ACK}+\frac1{BCK},
\qquad
\frac4p=\frac1{ABC}+\frac1{pACK}+\frac1{pBCK},
\tag{6}
\]

其中 \(K=(A+B)/27\)，且 \(n<p\)。

## 2. \(h=7t\) 的完整载体分支

现在回到核心域。对任意 \(p=24h+1\)，有

\[
x_{27}=\frac{p+27}{4}=6h+7\equiv1\pmod3,
\tag{7a}
\]

所以 \((x_{27},27)=1\) 自动成立；而严格 two-tail source 的门恰为

\[
28\mid p-1=24h
\Longleftrightarrow
7\mid h.
\tag{8a}
\]

因此 gap \(27\) 只能补充 \(7\mid h\) 的核心子支。写 \(h=7t\)，则

\[
p=168t+1,\qquad
x=7(6t+1),\qquad
n=6t+1.
\tag{9a}
\]

下面的完整平方载体分支再附加容量条件

\[
7\cdot13\mid6t+1.
\tag{10a}
\]

特别地，

\[
(x,27)=1,\qquad
28\mid p-1,\qquad
F=7^2\cdot13=637\mid x.
\tag{11a}
\]

模 \(27\) 有

\[
\operatorname{QR}_{27}=\langle7\rangle,\qquad
\operatorname{ord}_{27}(7)=9,\qquad
13\equiv7^5\pmod{27}.
\tag{10}
\]

因此

\[
\mathcal R_{27}(637)
=\left\{7^{r+5s}:
-2\le r\le2,\ -1\le s\le1\right\}
=\langle7\rangle
=\operatorname{QR}_{27}.
\tag{11}
\]

由第 1 节，在 (10a) 的全部参数上有精确判据：

\[
\boxed{
\text{gap \(27\) Type II terminal 与严格 \(n\)-递降存在}
\Longleftrightarrow
x\ \text{有一个模 \(27\) 的非平方素因子}.
}
\tag{12}
\]

这里只由 \(7\mid h\) 自动得到的因子 \(7\) 还不够：

\[
\mathcal R_{27}(7)=\{4,1,7\}\subsetneq\operatorname{QR}_{27}.
\tag{13}
\]

故 \(13\) 的容量条件是实际需要的，而非表述冗余。另一方面

\[
28\mid p-1=24h\Longleftrightarrow7\mid h,
\tag{14}
\]

说明该严格递降机制不可能在全核心类上无条件使用。

## 3. 固定非平方 \(5\) 的无穷射线

再要求

\[
5\mid6t+1.
\tag{15}
\]

合并 (10a) 与 (15) 得

\[
t=455u+379,\qquad
h=3185u+2653,\qquad
p=76440u+63673.
\tag{16}
\]

令

\[
T=6u+5.
\tag{17}
\]

则

\[
x=3185T=5\cdot7^2\cdot13T,
\qquad
n=455T.
\tag{18}
\]

\(5\) 是模 \(27\) 的非平方，且 \(-5\equiv22\equiv7^2\pmod{27}\)。取

\[
(A,B,C,K)=(5,49,13T,2).
\tag{19}
\]

于是

\[
(A,B)=1,\qquad
A+B=54=27K,\qquad
ABC=x,\qquad
d=A^2C=325T\le x.
\tag{20}
\]

故对每个使 \(p\) 为素数的 \(u\)，有显式恒等式

\[
\boxed{
\frac4{455T}
=\frac1{3185T}+\frac1{130T}+\frac1{1274T},
}
\tag{21}
\]

\[
\boxed{
\frac4p
=\frac1{3185T}+\frac1{130pT}+\frac1{1274pT}.
}
\tag{22}
\]

又

\[
\gcd(76440,63673)=1,
\tag{23}
\]

所以 Dirichlet 定理给出无穷多个该射线上的核心素数。

取 \(u=2\) 时，

\[
(p,h,T,x,n)=(216553,9023,17,54145,7735),
\tag{24}
\]

其中 \(p\) 为素数，且

\[
(A,B,C,K)=(5,49,221,2),\qquad d=5525.
\tag{25}
\]

对应的严格递降和提升分别是

\[
\frac4{7735}=\frac1{54145}+\frac1{2210}+\frac1{21658},
\tag{26}
\]

\[
\frac4{216553}
=\frac1{54145}
+\frac1{216553\cdot2210}
+\frac1{216553\cdot21658}.
\tag{27}
\]

## 4. 不依赖平方载体的单素因子残类扇

仍令 \(h=7t\)、\(W=6t+1\)，于是 \(x=7W\)、\(n=W\)。若 \(W\) 含有素因子
\(r\)，则下表的每一行都是一个直接的 factor-pair certificate：

\[
\begin{array}{c|c|c}
r\pmod {27}&(A,B,C)&K\\ \hline
20&(7,r,W/r)&(r+7)/27\\
23&(1,7r,W/r)&(7r+1)/27\\
26&(1,r,7W/r)&(r+1)/27
\end{array}
\tag{28}
\]

**定理（gap \(27\) 单素因子扇）。** 在表中任一行，\(A,B\) 互素、\(A\le B\)、
\(ABC=x\)、\(A+B=27K\)。因此它给出一个 Type II direct terminal，且严格下降到
\(n=W\)。这三个规则不以 \(91\mid W\) 为前提；它们的控制点覆盖固定平方载体容量子支
之外的点，但两种机制不是包含关系。

取 \(r=101\equiv20\pmod {27}\)。令

\[
t=84+101u,\qquad
W=101(6u+5),\qquad
p=14113+16968u.
\tag{29}
\]

则

\[
(A,B,C,K)=(7,101,6u+5,4)
\tag{30}
\]

对每个素数值 \(p\) 都给出上述严格递降。又

\[
\gcd(14113,16968)=1,
\tag{31}
\]

故 Dirichlet 定理给出无穷多个该射线上的核心素数。

这确实补到了旧的固定小 gap 残余。取 \(u=1\)，有

\[
p=31081,\qquad h=1295,\qquad W=1111,\qquad x=7777=7\cdot11\cdot101.
\tag{32}
\]

这个点的 \(m=3,7,11,23\) 完整 Type II factor-pair 层均未命中；但 (28) 给出

\[
(A,B,C,K)=(7,101,11,4),\qquad d=A^2C=539,
\tag{33}
\]

\[
\frac4{1111}=\frac1{7777}+\frac1{308}+\frac1{4444},
\qquad
\frac4{31081}=\frac1{7777}+\frac1{9572948}+\frac1{138123964}.
\tag{34}
\]

同一 source gate 也有真实边界。对

\[
p=18481,\qquad h=770,\qquad x=4627=7\cdot661,
\tag{35}
\]

有 \(-1\notin\mathcal R_{27}(4627)\)，故 gap \(27\) 仍未命中。

## 5. 边界

本卡只建立 gap \(27\) 的 direct terminal 和严格 two-tail descent，且载体充分覆盖
仅限 \(7\mid h\) 的容量子支；第 2 节的平方载体和第 4 节的残类扇都不是全覆盖。
它不提供其它 \(h\) 类的 gap \(27\) 选择器，不证明不同 gap 的并集覆盖，也不把小实例
的可解性自动转化为其它形状的递降。

复现：

    python3 reproductions/type_ii_gap27_square_carrier_descent.py --verify
