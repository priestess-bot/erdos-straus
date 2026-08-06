---
kind: claim
claim_id: type-I-high-anchor-e2-residue-arc-criterion
title: high-anchor complete-excess bundle 的 E2 残数短弧判据
statement: 设 high-anchor complete-excess bundle 取 M=lcm(A,Q)，并给出 overflow K_M=MC、1<=C<p、4MC=pR_M+1。令 a=A/gcd(A,C)，u 为 M/a 的最小正模 p 剩余。则带账本 cofactor E2 门 a|(M mod p) 当且仅当 a*u<p，当且仅当 u<=floor((p-1)/a)。故该门是由 (p,A,Q) 决定的精确短弧/无进位条件；它不由 Fourier 相位自动保证。特别地，M<p 时门自动通过，而 a>1 且 p<=M<a*p 时门必失败。在 n=p G-anchor 的 M=A(p-3)/2 子族中，若 g=gcd(A,p-d) 属于 {1,2,3,4,6}，则该门严格失败；其中 a=1 的自动通过层恰由 Pell 方程 (2x+1)^2-12z^2=1 参数化，并精确回返原 G-anchor 的 (p,p-2,B_p;A) 算术检查点，故不提供严格递降。此结论只给 E2 预筛，不单独构成递归边或终端。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-cofactor-ledger-e2-gate
  - type-I-overflow-cofactor-r-chart-support
  - type-I-high-anchor-cofactor-macro-e1-e4-admission
  - type-I-overflow-high-carrier-n-prime-g-anchor-phase
topics:
  - type-I
  - high-carrier
  - high-anchor
  - complete-excess-bundle
  - overflow
  - cofactor
  - E2
  - no-carry
  - residue-arc
  - G-anchor
  - Pell-equation
  - self-return
  - proof-boundary
sources:
  - claim: type-I-overflow-cofactor-ledger-e2-gate
    role: ledger-persistence-equivalence
  - claim: type-I-overflow-cofactor-r-chart-support
    role: complete-excess-cofactor-normal-form
  - claim: type-I-high-anchor-cofactor-macro-e1-e4-admission
    role: high-anchor-bundle-interface
  - claim: type-I-overflow-high-carrier-n-prime-g-anchor-phase
    role: n-equals-p-G-anchor-subfamily
visibility: public
last_checked: '2026-08-06'
---

# high-anchor complete-excess bundle 的 E2 残数短弧判据

## 1. bundle 数据中的唯一整数门

设一个 high-anchor complete-excess bundle 已经给出

\[
M=\operatorname{lcm}(A,Q),
\qquad
K_M=MC,
\qquad
1\le C<p,
\qquad
4MC=pR_M+1.
\tag{1}
\]

这里 \(A\mid M\) 是旧 charged ledger，\(Q\) 是该 bundle 的完整超额块。由 (1)
模 \(p\)，\(C\) 不是额外自由变量，而是

\[
C=[(4M)^{-1}]_p,
\tag{2}
\]

其中 \([\cdot]_p\) 表示 \(1,\ldots,p-1\) 中的标准剩余。令

\[
g=(A,C),
\qquad
a=\frac Ag,
\qquad
u=\left[\frac Ma\right]_p\in\{1,\ldots,p-1\}.
\tag{3}
\]

因为 overflow 行列式蕴含 \(p\nmid M\)，也有 \(p\nmid a\)。因此 (1)--(3) 的
数据完全由 \((p,A,Q)\) 的 bundle 输出确定。

## 2. E2 的精确短弧形式

**定理。** 令 \(r=M\bmod p\) 取 \(1,\ldots,p-1\) 中的代表。则下列条件等价：

\[
\boxed{
a\mid r
\quad\Longleftrightarrow\quad
au<p
\quad\Longleftrightarrow\quad
u\le\left\lfloor\frac{p-1}{a}\right\rfloor.
}
\tag{4}

因而 (4) 恰是带账本 cofactor E2 门，而不是一个仅由角色阶或群像决定的条件。

**证明。** 写

\[
\frac Ma=pq+u,
\qquad
au=pw+r,
\tag{5}
\]

其中 \(q\ge0\)、\(0\le w<a\)、\(1\le r<p\)。后一个范围来自 \(0<u<p\) 与
\(p\nmid au\)。由 (5)，

\[
M=p(aq+w)+r,
\tag{6}
\]

所以 \(\lfloor M/p\rfloor=aq+w\)。又

\[
a\mid r
\quad\Longleftrightarrow\quad
a\mid pw
\quad\Longleftrightarrow\quad
a\mid w
\quad\Longleftrightarrow\quad
w=0,
\tag{7}
\]

其中使用 \((a,p)=1\) 和 \(0\le w<a\)。最后 \(w=0\) 正是 \(au<p\)，而因为
\(u\) 为整数，它又等价于右端的不等式。由带账本 E2 引理，\(a\mid r\) 等价于
存在保留旧 \(A\) 的 cofactor target ledger。证毕。

也可将 (4) 写成完全显式的同余门：

\[
M\equiv r\pmod {ap}.
\tag{8}
\]

它等价于 \(a\mid\lfloor M/p\rfloor\)，故称为 quotient/no-carry 条件。

## 3. 两个立即的预筛

由 (4) 可得无需重建完整 \(r\)-chart 的两个精确结论：

\[
\boxed{M<p\ \Longrightarrow\ \text{E2 通过};}
\tag{9}
\]

事实上此时 \(u=M/a\)，故 \(au=M<p\)。另一方面，若 \(a>1\)，则

\[
\boxed{p\le M<ap\ \Longrightarrow\ \text{E2 失败}.}
\tag{10}
\]

此时仍有 \(u=M/a\)，但 \(au=M\ge p\)。式 (9)--(10) 是 bundle 的算术预筛；
它们不检验 canonical target、来源回放、typed F/G 纤维、terminal-first 或 E5。

## 4. 同一 high bundle 的一次通过与一次耗尽

现有 \(p=1201\) high-anchor bundle 提供一个完全定点的对照。第一次取

\[
A=986,
\qquad Q=919,
\qquad M=906134,
\qquad C=952.
\tag{11}
\]

于是 \(g=34\)、\(a=29\)，并且

\[
\frac Ma=31246\equiv20\pmod{1201},
\qquad
29\cdot20=580<1201.
\tag{12}
\]

故 E2 通过，实际有 \((\lfloor M/p\rfloor,r)=(754,580)\)，两者均被 \(29\) 整除。
同一 \(Q\) 在首次 target support \(A'=27608\) 上重用时，

\[
M'=25371752,
\qquad C'=34,
\qquad g'=34,
\qquad a'=812,
\tag{13}
\]

而 \(M'/a'=31246\equiv20\pmod{1201}\) 未变，却有

\[
812\cdot20>1201,
\qquad
(\lfloor M'/p\rfloor,r')=(21125,627).
\tag{14}
\]

所以 E2 严格失败。这精确解释 complete-excess one-shot exhaustion 的第二 gate fail；
它不需要、也不能由新势函数修复。

## 5. 一个自然 \(n=p\) G-anchor 子族的严格障碍

令

\[
B_p=\frac{(p-1)^2}{4},
\qquad
Q=\frac{p-3}{2},
\qquad
A=\frac{B_p}{c_0},
\qquad
M=AQ,
\tag{15}
\]

其中 \(c_0\mid B_p\)、\(2\le c_0<Q\)。这是 \(n=p\) G-anchor 的完整超额
bundle 在支持 \(A\) 上的自然子族。事实上 \((Q,B_p)=1\)，所以 \((Q,A)=1\)，
式 (15) 的 \(M=AQ\) 正是 \(\operatorname{lcm}(A,Q)\)。令
\(\kappa\in\{0,1,2\}\) 满足
\(\kappa\equiv c_0\pmod3\)，并取

\[
d=\frac{2c_0+\kappa p}{3},
\qquad
C=p-d,
\qquad
g=(A,C),
\qquad
a=A/g.
\tag{16}
\]

相应行列式满足 \(pn=4Md+1\)。令 \(k=\lfloor M/p\rfloor\)。对全部核心素数
\(p\ge73\)，有

\[
\frac A3<k<\frac A2.
\tag{17}
\]

上界由 \(Q<p/2\) 立即得到。下界来自

\[
k>\frac{AQ}{p}-1=\frac{A(p-3)}{2p}-1>\frac A3;
\tag{18}
\]

最后一个严格不等式由 \(A>B_p/Q\) 和
\((p-1)^2(p-9)>12p(p-3)\)（\(p\ge73\)）给出。

因为 \(a\mid M\) 且 \((a,p)=1\)，E2 等价于 \(a\mid k\)。若它通过，写

\[
k=m\frac Ag,
\tag{19}
\]

则 (17) 强制

\[
\frac g3<m<\frac g2.
\tag{20}
\]

所以得到严格 no-go：

\[
\boxed{g=(A,p-d)\in\{1,2,3,4,6\}
\quad\Longrightarrow\quad\text{E2 失败}.}
\tag{21}

特别地 \((A,p-d)\le4\) 时必失败。作为非空对照，取

\[
(p,c_0,A,M,d,C)=(241,8,1800,214200,166,75).
\tag{22}
\]

这里 \(g=75\)、\(a=24\)，且

\[
(k,r)=(888,192),
\qquad 24\mid888,
\qquad24\mid192.
\tag{23}

故 E2 确实通过；其 cofactor 图表为 \((R_r,K_r)=(239,14400)\)。该例只说明
整数 gate 可发生，且目标低于 \(p\)，不登记新的 overflow 递归边。

## 6. 自动通过的 \(a=1\) 层恰为 Pell 自回返

式 (21) 留下的自动通过情形可以完全分类。仍在 (15)--(16) 的域内，特别是
\(c_0\mid B_p\)、\(2\le c_0<Q\) 及 \(p\equiv1\pmod {24}\)。

**定理。** \(a=1\) 当且仅当存在正整数 \(x,z\)，使

\[
\boxed{
c_0=3x,
\qquad
x(x+1)=3z^2,
\qquad
p=6x+1+6z,
}
\tag{24}
\]

并且 \(p\) 为素数、\(x+z\equiv0\pmod4\)。此时

\[
A=C=4x+1+6z,
\qquad
d=2x,
\qquad
Q=3x+3z-1.
\tag{25}
\]

等价地，前一式中的整数点落在 Pell 曲线

\[
(2x+1)^2-12z^2=1.
\tag{26}
\]

**证明。** \(c_0<Q\) 给出

\[
A=\frac{B_p}{c_0}>\frac{B_p}{Q}
=\frac{p+1}{2}+\frac2{p-3}>\frac p2.
\tag{27}
\]

而 \(0<C<p\)，故

\[
a=1
\quad\Longleftrightarrow\quad A\mid C
\quad\Longleftrightarrow\quad C=A.
\tag{28}
\]

把 \(C=A\) 代入 (16)。若 \(\kappa=1\)，相应二次式的判别式为
\(32c_0(3-c_0)\)；但 \(c_0\equiv1\pmod3\) 且 \(c_0\ge2\) 蕴含 \(c_0\ge4\)，
故无实根。若 \(\kappa=2\)，判别式为 \(16c_0(3-5c_0)<0\)。所以只能有
\(\kappa=0\)、\(c_0=3x\)，并且

\[
(p-6x-1)^2=12x(x+1).
\tag{29}
\]

由于 \(p\equiv1\pmod {24}\)，左端的平方根可写为 \(6z\)，于是得到 (24) 的
正根或负根。负根使 \(Q=3x-3z-1<c_0\)，违反输入域；正根给出 (24)--(26)。
反向代入可得 \(B_p=3xA\) 与 \(c_0<Q\)，所以它确实恢复该子族的一行。最后
\(p=6(x+z)+1\) 表明核心同余恰等价于 \(x+z\equiv0\pmod4\)。证毕。

这不是新的递降层。由 (24)--(25)，有精确整数式

\[
M=AQ=p(2x+3z-1)+3x,
\qquad
r=M\bmod p=3x=c_0.
\tag{30}
\]

所以 cofactor target 满足

\[
K_r=rC=B_p,
\qquad
R_r=p-2,
\qquad
[A,C]=A.
\tag{31}
\]

它在 \((p,R,K;A)\) 与账本层精确回返原 G-anchor。若写

\[
h=\frac{K_r-B_p}{pA},
\qquad
c_{\rm mac}=\frac{C}{(A,C)},
\tag{32}
\]

则 \(h=0\)、\(c_{\rm mac}=1\)。因此本层只能在另有 frozen action/capability/source
digest 一致性合同的情况下标成 `STUTTER`；它本身既不给严格势下降，也不宣称完整
selector state 相同。

例如 \((x,z)=(48,28)\) 给出核心素数 \(p=457\)，并有

\[
(B_p,Q,c_0,A,C,d)=(51984,227,144,361,361,96),
\tag{33}
\]

\[
M=81947=457\cdot179+144,
\qquad
n=68857,
\qquad
(K_M,R_M)=(29582867,258931),
\tag{34}
\]

而 \((K_r,R_r)=(51984,455)=(B_{457},457-2)\)，正是 (31) 所述回返。

## 7. 边界

本卡把 high bundle 的 E2 从“寻找一个可能的 target”化为可计算的短弧条件，并给出
一个自然子族的精确拒绝器。它不证明每一个 bundle 的 \(u\) 落在该短弧，也不把
E2 通过升级为来源完整、F/G 相位提升、Type I/II 终端或完整 E1--E5 递降。
