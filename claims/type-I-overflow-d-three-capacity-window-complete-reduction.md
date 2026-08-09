---
kind: claim
claim_id: type-I-overflow-d-three-capacity-window-complete-reduction
title: 高载体 d=3 容量窗的完整余因子递降分流
statement: >-
  设 p≡1 (mod 24) 的 verified overflow 满足 pn=12M+1、d=3、M>B_p=(p−1)^2/4、3p−2≤n≤4p−11，并携带 A|M、1≤A≤B_p 及图表无关的 Sol(p) 标记集。令 c=(p−1)/4、b=M/A。则 A<c 时 L=c 给出 fixed-s 严格边；A≥c 且 b 合数时以 q=spf(b) 重图表为 (M/q,3q)，并且 3q<p；b=2 或 3 时以 (A,3b) 因子转移；3<b<p 为素数时以 (3A,b) 余因子交换；b>p 为素数时 L=b 给出支付 support reset 的 fixed-n 严格边。b=p 不可能。五类互斥且穷尽，统一势 Λ=(floor(B_p/A),M) 严格下降，并在既有 source/path、恒等解提升和 E1--E5 合同下不留下该 d=3 首容量窗的 overflow 余项。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-high-carrier-height-staircase
  - type-I-overflow-fixed-n-bounded-divisor-saturation
  - type-I-overflow-fixed-s-bounded-divisor-saturation
  - type-I-overflow-cofactor-factor-exchange-carrier-descent
topics:
  - type-I
  - overflow
  - high-carrier
  - d-three
  - capacity-window
  - cofactor-primality
  - denominator-transfer
  - support-reset
  - well-founded-descent
  - selector
  - proof-program
sources:
  - claim: type-I-overflow-high-carrier-height-staircase
    role: d-three-height-window
  - claim: type-I-overflow-fixed-n-bounded-divisor-saturation
    role: fixed-n-support-reset-contract
  - claim: type-I-overflow-fixed-s-bounded-divisor-saturation
    role: fixed-s-contract
  - claim: type-I-overflow-cofactor-factor-exchange-carrier-descent
    role: factor-transfer-and-cofactor-exchange
  - reproduction: reproductions/type_i_overflow_d_three_capacity_window_complete_reduction.py
    role: six-route-d-three-controls
visibility: public
last_checked: '2026-08-09'
---

# 高载体 \(d=3\) 容量窗的完整余因子递降分流

## 1. 状态与结论

令 \(p\equiv1\pmod {24}\) 为核心素数，且已有 source/path/node 回执的 overflow
满足
\[
pn=12M+1,\qquad d=3,\qquad
M>B_p:=\frac{(p-1)^2}{4},
\tag{1}
\]
以及
\[
3p-2\le n\le4p-11.
\tag{2}
\]
令 \(A\mid M\) 是 absorbed support，\(1\le A\le B_p\)，并假设使用图表无关的
\(W=\operatorname{Sol}(p)\)，使既有 fixed-\(n\)、fixed-\(s\) 和因子交换合同能
提供恒等解提升。写
\[
c=\frac{p-1}{4},\qquad b=\frac MA.
\tag{3}
\]

则五个互斥分支如下：
\[
\begin{array}{c|c|c}
\text{条件}&\text{后继}&\text{严格付款}\\ \hline
A<c&\text{fixed-}s\text{，取 }L=c&
\lfloor B_p/c\rfloor<\lfloor B_p/A\rfloor\\
A\ge c,\ b\text{ 合数}&(M,3)\mapsto(M/q,3q),\ q=\operatorname{spf}(b)&M/q<M\\
A\ge c,\ b\in\{2,3\}&(M,3)\mapsto(A,3b)&A<M\\
A\ge c,\ 3<b<p\text{ 为素数}&(M,3)\mapsto(3A,b)&3A<M\\
A\ge c,\ b>p\text{ 为素数}&\text{fixed-}n\text{，取 }L=b&
\lfloor B_p/b\rfloor<\lfloor B_p/A\rfloor
\end{array}
\tag{4}
\]
所有后继都满足 \(pR'+1=4K'\)、\(R'\equiv3\pmod4\)、\(K'>0\)，因而是合法
canonical chart；\(R'<p\) 时是 marked absorb，\(R'>p\) 时仍是新的 overflow。
使用
\[
\boxed{\Lambda_p(M,d;A)=
\left(\left\lfloor\frac{B_p}{A}\right\rfloor,M\right)}
\tag{5}
\]
的字典序势，A、E 两个 fixed-s/fixed-n 边严格降低第一坐标，B、C、D 三个
代数后继保持 \(A\) 并严格降低第二坐标。因此该 \(d=3\) 容量窗在既有 E1--E5
合同下没有未分流余项。

## 2. 固定余数与容量界

由 \(p\equiv1\pmod {12}\) 和 (1)，有
\[
n\equiv1\pmod {12},\qquad n\equiv1\pmod4.
\tag{6}
\]
又由 (2) 的上界，
\[
12M\le4p^2-11p-1<4(p-1)^2,
\]
所以
\[
\boxed{M<\frac{(p-1)^2}{3}=\frac43B_p.}
\tag{7}
\]
模 \(p\) 约化 (1) 得
\[
12M\equiv-1\pmod p.
\]
由于 \(r=(p-1)/12\) 满足 \(12r+1=p\)，规范余数为
\[
r=M\bmod p=\frac{p-1}{12}.
\tag{8}
\]
于是
\[
4rd+1=12r+1=p,\qquad rd=c.
\tag{9}
\]
这解释了 \(d=3\) 窗的 fixed-s 入口：所有 \(A<c\) 的状态共享同一个
\(rd=c\) 载体，而 \(A\ge c\) 时该入口的有界除子菜单自动为空。
此外，若 \(A\ge c\)，(7) 给出
\[
\boxed{1<b<\frac{4(p-1)}3.}
\tag{10}
\]
若 \(b\) 合数、\(q=\operatorname{spf}(b)\)，则 \(q^2\le b\)，而对
\(p\ge73\)
\[
\frac{4(p-1)}3<\frac{p^2}{9},
\qquad
\boxed{3q<p.}
\tag{11}
\]

## 3. 五类后继的证明

### A. \(A<c\)：fixed-s

取 \(L=c\)。由 (9)，\(L\mid rd\)，且 \(4L>1\)，所以既有 fixed-s 合同的整除
和正性门通过。又
\[
\frac{B_p}{A}-\frac{B_p}{c}
\ge\frac{B_p}{c(c-1)}
=\frac{4(p-1)}{p-5}>1,
\tag{12}
\]
故
\[
\left\lfloor\frac{B_p}{c}\right\rfloor
<
\left\lfloor\frac{B_p}{A}\right\rfloor.
\]
这给出第一坐标严格下降的完整 E1--E5 fixed-s 边。

### B. \(A\ge c\)：合数余因子

令 \(q=\operatorname{spf}(b)\)。由 (11)，\(d'=3q<p\)。取
\[
M'=\frac Mq,\qquad d'=3q.
\tag{13}
\]
因为 \(q\mid b=M/A\)，有 \(A\mid M'\)，且
\[
4M'd'+1=4(M/q)(3q)+1=12M+1=pn.
\tag{14}
\]
由 \(d'<p\) 和 \(n>1\)，
\[
4M'-n=\frac{pn-1}{3q}-n
=\frac{n(p-3q)-1}{3q}>0.
\tag{15}
\]
于是 \(K'=M'(p-d')>0\)，(14)--(15) 给出合法 canonical chart。因 \(q>1\)，
\(M'<M\)，第一坐标不变而第二坐标严格下降；这正是既有 factor-transfer E1--E5 边。

### C. \(b=2\) 或 \(b=3\)

对 \(b\in\{2,3\}\) 取
\[
M'=A,\qquad d'=3b.
\tag{16}
\]
这里 \(d'\in\{6,9\}<p\)，且
\[
4M'd'+1=12Ab+1=12M+1=pn.
\tag{17}
\]
因 \(M'=A<M=Ab\)，且 \(A\mid M'\)，正性和 canonical 同余由 \(d'<p\) 同前得到。
这个分支是因子转移 \(g=b\) 的两个小素数边界，不能并入 \(3<b\) 的交换式。

### D. \(3<b<p\) 为素数：余因子交换

取
\[
M'=3A,\qquad d'=b.
\tag{18}
\]
由 \(M=Ab\) 得
\[
4M'd'+1=12Ab+1=pn.
\tag{19}
\]
因为 \(b<p\)，
\[
4M'-n=\frac{pn-1}{b}-n
=\frac{n(p-b)-1}{b}>0,
\tag{20}
\]
所以 \(K'=M'(p-b)>0\)。又 \(b>3\) 给出
\[
M'=3A<Ab=M,
\tag{21}
\]
而 \(A\mid M'\)。这正是既有 cofactor-exchange E1--E5 边，第二坐标严格下降。

### E. \(b>p\) 为素数：fixed-n support reset

先由 (1) 写出
\[
12Ab=pn-1.
\tag{22}
\]
因 \(b>p\)，有
\[
A<\frac n{12}<\frac p3<b,
\tag{23}
\]
其中最后一个不等式用 \(n\le4p-11\)。取 \(L=b\)。它整除
\(S=Md=3M\)，且
\[
4L>4p>n,\qquad L=b<\frac{4(p-1)}3<B_p.
\tag{24}
\]
再由 \(A<p/3\) 和 \(b>p\)，
\[
\frac{B_p}{A}-\frac{B_p}{b}
>
\frac{3B_p}{p}-\frac{B_p}{p}
=\frac{2B_p}{p}>1.
\tag{25}
\]
因此 fixed-n 的有界除子门
\[
A<L\le B_p,\qquad 4L>n,\qquad
\left\lfloor B_p/L\right\rfloor<
\left\lfloor B_p/A\right\rfloor
\]
全部通过。令
\[
R_L=4L-n,\qquad K_L=L\left(p-\frac{S}{L}\right)
=b(p-3A)>0.
\tag{26}
\]
式 (26) 给出合法 fixed-n chart；由于 \(A\nmid L\) 一般不成立，这条边明确由
(5) 支付 support reset，而不是声称保留旧支撑。

## 4. 穷尽性与严格下降

由 \(M>B_p\ge A\)，必有 \(b>1\)。若 \(A<c\)，进入 A；否则 \(A\ge c\)，
此时 \(b\) 要么合数，要么素数。合数进入 B；素数不可能等于 \(p\)，因为
\(p\nmid M\)（否则 (1) 模 \(p\) 给出 \(0\equiv1\)），故只能是 \(b<p\) 或
\(b>p\)。前者按 \(b=2,3\) 或 \(3<b\) 分别进入 C、D，后者进入 E。
五类互斥且穷尽。

A 和 E 由 fixed-s/fixed-n 有界除子合同直接支付第一坐标；B、C、D 保持
\(A\)，并由 (13)、(16)、(18) 严格减小 \(M\)。E1 继承输入的 source/path/node
回执；E2--E3 是上述整数恒等式、范围和正性；E4 取图表无关的
\(W=\operatorname{Sol}(p)\) 恒等提升；E5 是 (5) 的严格下降。若后继的
\(R'\) 小于 \(p\)，记录 marked absorb；否则保留为新的 overflow 并继续使用同一
\(\Lambda_p\) 选择器。证毕。

## 5. 控制实例

取 \(p=193\)，则 \(c=48\)、\(B_p=9216\)。以下六个控制均满足 (1)--(2)：
\[
\begin{array}{c|r|r|r|r|l}
n&M&A&b&\text{分支}&\text{回执}\\ \hline
577&9280&1&9280&A<c&\mathrm{D3\_FIXED\_S}\\
577&9280&58&160&\text{合数}&\mathrm{D3\_COFACTOR\_FACTOR\_TRANSFER}\\
577&9280&4640&2&b=2&\mathrm{D3\_SMALL\_PRIME\_FACTOR\_TRANSFER}\\
601&9666&3222&3&b=3&\mathrm{D3\_SMALL\_PRIME\_FACTOR\_TRANSFER}\\
577&9280&320&29&3<b<p&\mathrm{D3\_PRIME\_COFACTOR\_EXCHANGE}\\
721&11596&52&223&b>p&\mathrm{D3\_FIXED\_N\_SUPPORT\_RESET}
\end{array}
\]
例如 \(b=2\) 的后继为 \((M',d')=(4640,6)\)，\(b=3\) 的后继为
\((3222,9)\)，而 \(b=29\) 的后继为 \((960,29)\)。每个后继均由脚本重新检查
\(pn=4M'd'+1\)、\(R'>0\)、\(K'>0\) 和严格势条件。

聚焦复现命令：

    python3 reproductions/type_i_overflow_d_three_capacity_window_complete_reduction.py --verify

## 6. 研究边界

本定理把已有 d=1、d=2 结果之后的第一个 \(d=3\) 高载体容量窗完全分流，但仍有
明确范围：\(d\ge4\)、\(d=3\) 且 \(n\ge4p-7\)，以及 source/path/node 和
\(\operatorname{Sol}(p)\) 输入回执本身的全称存在性不在本卡内。它证明的是：
一旦状态进入该窗口并满足既有整数来源合同，就不需要再寻找新的 alternate 或
抽象 Fourier 解释，五类算术后继中必有一条严格可提升边。
