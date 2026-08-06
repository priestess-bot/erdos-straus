---
kind: claim
claim_id: type-II-hall-fiber-arithmetic-closure-trichotomy
title: Type II Hall 混合因子的同模数—降模—raw 算术闭合三分
statement: 对由 Hall 匹配得到的两两互素带来源因子块，若其乘积 h 满足 h=-1 (mod 4D) 且每个块来自某个 p+4Da_i，则同模数 CRT 候选、严格除子格候选和有限 raw 因子候选按顺序给出 Type II 短证书；三类候选全为空时，枚举结果构成该混合因子的完整算术提升负证书。该三分只闭合当前混合因子分支，不声称原素数没有其它证书。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-hall-matching-fiber-realization-gate
  - type-II-same-modulus-source-switch-crt-criterion
  - type-II-arithmetic-lift-raw-factor-fallback
  - type-II-cross-state-source-demand-hall-capacity-bridge
topics:
  - type-II
  - Hall
  - arithmetic-lift
  - CRT
  - source-switch
  - raw-factor
  - finite-obstruction
  - constructive-certificate
sources:
  - claim: type-II-hall-matching-fiber-realization-gate
    role: matched-factor-provenance
  - claim: type-II-same-modulus-source-switch-crt-criterion
    role: same-and-lower-modulus-candidates
  - claim: type-II-arithmetic-lift-raw-factor-fallback
    role: raw-fallback-candidates
  - claim: type-II-cross-state-source-demand-hall-capacity-bridge
    role: Hall-request-bundle
visibility: public
last_checked: '2026-08-05'
---

# Type II Hall 混合因子的同模数—降模—raw 算术闭合三分

## 1. 输入和三个有限候选集

固定核心素数 \(p\)、原始参数 \(D\) 和 \(M=4D\)。设 Hall 匹配选出的来源块为
\[
(a_i,h_i),\qquad h_i\mid p+4Da_i,\qquad (h_i,M)=1,
\]
其中 \(h_i\) 两两互素；共同 q 的重复层必须先按 shared-q ledger 合并。令
\[
h=\prod_i h_i,\qquad h\equiv-1\pmod M.
\]
由 CRT 取 \(a_0\pmod h\) 满足
\[
a_0\equiv a_i\pmod{h_i}.
\]
于是 \(h\mid p+4Da_0\)。

定义同模数候选
\[
\mathscr C_{\mathrm{same}}(h)=
\left\{a:
\begin{array}{l}
a\mid D,\ D/a\text{ 平方自由},\ 4aD<p,\\
a\equiv a_0\pmod h
\end{array}\right\}.
\tag{1}
\]

定义严格除子格候选
\[
\mathscr C_{\mathrm{lower}}(h)=
\left\{(D',A):
\begin{array}{l}
D'\mid D,\ D'<D,\ A\mid D',\\
D'/A\text{ 平方自由},\ 4AD'<p,\\
AD'\equiv Da_0\pmod h
\end{array}\right\}.
\tag{2}
\]

最后定义 raw 候选
\[
\mathscr R_{\mathrm{raw}}(h;p)=
\left\{(A,C,K):
\begin{array}{l}
A,C,K\in\mathbb N,\ ACK=(h+1)/4,\\
h\mid Kp+A,\ A\le(Kp+A)/h
\end{array}\right\}.
\tag{3}
\]

三者都是有限集合；(3) 只需枚举 \((h+1)/4\) 的因子三元组。

## 2. 算术闭合三分

对上述来源混合因子，按如下顺序输出：

1. 若 \(\mathscr C_{\mathrm{same}}(h)\ne\varnothing\)，任取 \(a\) 并令
   \[
   K=(h+1)/(4D),\quad c=D/a,\quad B=(Kp+a)/h.
   \]
   则 \(B>a\)，同一参数纤维给出 Type II 短证书；
2. 若同模数候选为空而 \(\mathscr C_{\mathrm{lower}}(h)\ne\varnothing\)，任取
   \((D',A)\)，令
   \[
   K'=(h+1)/(4D'),\quad C'=D'/A,\quad B'=(K'p+A)/h.
   \]
   则 \(B'>A\)，得到严格较小模数的合法 Type II source-switch；
3. 若前两类为空而 \(\mathscr R_{\mathrm{raw}}(h;p)\ne\varnothing\)，任取
   \((A,C,K)\)，并令 \(B=(Kp+A)/h\)，得到 raw Type II 短证书；
4. 若三类全为空，输出
   \[
   \mathrm{ALL\_ARITHMETIC\_LIFT\_EMPTY}
   =\bigl(h,a_0,\mathscr C_{\mathrm{same}},
     \mathscr C_{\mathrm{lower}},\mathscr R_{\mathrm{raw}}\bigr).
   \tag{4}
   \]

第四项只排除该 \(h\) 的三种提升族，不能宣称 \(p\) 没有其它 Type I/II 证书。

## 3. 证明

由 \(h_i\mid p+4Da_i\) 和 \((h_i,M)=1\)，有
\[
h_i\mid p+4Da
\iff
a\equiv a_i\pmod{h_i}.
\]
两两互素时合并即得
\[
h\mid p+4Da
\iff
a\equiv a_0\pmod h.
\]
因此 (1) 恰是同模数 FIBER_REALIZED 候选的完整判定；带来源 CRT 正规形给出
\(B>a\) 和 Type II 证书。

同理，若 \(D'\mid D\)，则
\[
h\mid p+4AD'
\iff
AD'\equiv Da_0\pmod h.
\]
所以 (2) 恰是严格较小除子格的完整判定；同一正规形恒等式给出 \(B'>A\)。

若 (1)、(2) 均为空，(3) 的每个元素直接满足 raw Type II 正规形的整除和大小条件，
故第三项给出证书；若 (3) 也为空，则三种有限候选逐项均不存在，得到 (4)。证毕。

## 4. 唯一候选和容量接口

对任意除子格候选令 \(x=AD'\)。由 \(A\le D'\le D\) 有
\[
1\le x\le D^2.
\]
若 \(h>D^2\)，同余 \(x\equiv Da_0\pmod h\) 至多有一个正代表。因此同模数和
严格降模候选的来源门可在 \(h>D^2\) 时化为一次平方自由分解、整除和大小检查；
不需要搜索多个参数纤维。

在 Hall 闭包中，这个三分给出精确的 typed 回执：

* 第 1 项是 HC3-FIBER；
* 第 2 项是保持来源标签的较小模数后继；
* 第 3 项是 raw Type II 终端；
* 第 4 项是 HC2 型的有限算术负证书，不能作为容量单位重复收费。

若 \(h_i\) 有共同素因子，必须先以总指数重建 \(h\)；否则三分不适用，且重复 q
来源会造成虚假的候选。

## 5. 边界样例

### \(p=97,D=6,h=143\)：三类全空

来源块 \(11\mid97+24\)、\(13\mid97+72\) 给出
\(a_0\equiv133\pmod{143}\)。没有 \(a\mid6\) 落在该 CRT 类中，所有
\(D'<6\) 的除子格同余也为空；完整枚举 \(ACK=36\) 的 raw 三元组同样为空。
因此该混合因子输出
\(\mathrm{ALL\_ARITHMETIC\_LIFT\_EMPTY}\)，而
\(11\cdot13\equiv-1\pmod{24}\) 仍只是伪池化。

### \(p=73,D=1,h=15\)：raw 回退

取 CRT/旧除子格候选为空的来源代表 \(a_0=8\)。但
\[
(A,C,K)=(2,2,1),\qquad B=(73+2)/15=5
\]
属于 (3)，故第三项直接给出 \(h=4\cdot2\cdot2\cdot1-1\) 的 Type II 证书。

## 研究边界

该三分把 Hall 匹配产生的一个混合因子束完整接到有限算术输出：同模数、严格降模、
raw 终端或精确空集证书。它仍不保证某个 Hall 匹配一定产生 \(h\equiv-1\pmod{4D}\)
的混合因子，也不把 ALL_ARITHMETIC_LIFT_EMPTY 自动转成核心素数下降；后者仍需
Type I/F/G 出口或新的良基势。
