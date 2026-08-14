---
kind: claim
claim_id: type-I-root-capacity-composite-divisor-external-terminal
title: 根容量任意子除子 Q 的外部源 Type I 终端菜单
statement: >-
  对核心素数 p≡1 mod24、M=(p^2+p+1)/3、u=gcd(2r+1,M)，任取
  1<Q|u。令 rho 为 p mod Q 的最小正剩余、i=Q-rho、N=(p+i)/Q，
  tau=<−pQ^(-1)>_(4i)。则 2<=i<=Q-2、gcd(Q,4i)=1，且所有固定 source i、
  gap 含 Q 的 external-source Type I 终端恰由
  T_(p,Q)={t|N:t≡tau mod4i} 参数化；每个命中 m=Qt 都自动给出自然范围的
  Type I 证书。Q 为素数时恢复既有 q 菜单。该推广严格增加覆盖：
  p=177433,u=91 的两个素数菜单 Q=7,13 均为空，但 composite Q=91 以 t=5
  给出 gap 455、divisor 756024 的 Type I 终端。菜单仍可全空，故不构成全称出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - external-source-type-I-certificate
  - type-I-root-capacity-prime-external-terminal-coupling
topics:
  - type-I
  - root-capacity
  - external-source
  - composite-divisor
  - finite-divisor-menu
  - terminal-first
  - short-certificate
  - proof-boundary
sources:
  - claim: external-source-type-I-certificate
    role: external-source-to-Type-I-certificate-equivalence
  - claim: type-I-root-capacity-prime-external-terminal-coupling
    role: prime-divisor-special-case
  - reproduction: reproductions/type_i_root_capacity_composite_divisor_external_terminal.py
    role: strict-composite-menu-extension-control
visibility: public
last_checked: '2026-08-14'
---

# 根容量任意子除子 \(Q\) 的外部源 Type I 终端菜单

## 1. 设置

固定核心素数

\[
p\equiv1\pmod {24},
\qquad
M=\frac{p^2+p+1}{3},
\qquad
u=(2r+1,M).
\tag{1}
\]

取任意正除子

\[
1<Q\mid u.
\tag{2}
\]

以下 \(Q\) 是 root-capacity 的 source modulus，不是 complete-excess bundle。
因为 \(M\) 为奇数且 \(M\equiv1\pmod3\)，有 \((Q,6)=1\)。又 \(Q\mid M\) 给出

\[
p^2+p+1\equiv0\pmod Q.
\tag{3}
\]

令 \(\rho\in\{1,\ldots,Q-1\}\) 是 \(p\) 模 \(Q\) 的最小正剩余，并置

\[
i=Q-\rho.
\tag{4}
\]

若 \(i=1\)，则 \(p\equiv-1\pmod Q\)，与 (3) 矛盾；若 \(i=Q-1\)，则
\(p\equiv1\pmod Q\)，迫使 \(Q\mid3\)，也与 \((Q,3)=1\) 矛盾。因此

\[
\boxed{2\le i\le Q-2.}
\tag{5}
\]

此外 \((Q,i)=(Q,p)=1\)，且 \(Q\) 为奇数，所以

\[
\boxed{(Q,4i)=1.}
\tag{6}
\]

## 2. 完整菜单

定义

\[
N=\frac{p+i}{Q},
\qquad
\tau=\left\langle-pQ^{-1}\right\rangle_{4i},
\tag{7}
\]

并令

\[
\boxed{
\mathcal T_{p,Q}
=
\left\{t\mid N:t\equiv\tau\pmod {4i}\right\}.}
\tag{8}
\]

对任意正整数 \(t\)，有

\[
t\in\mathcal T_{p,Q}
\quad\Longleftrightarrow\quad
Qt\mid p+i,\qquad4i\mid p+Qt.
\tag{9}
\]

确实，第一项就是 \(t\mid N\)。第二项中可在模 \(4i\) 下消去 \(Q\)，因为 (6)
保证 \(Q\) 可逆，恰得到 (8) 的剩余条件。

所以固定 source \(i\)、且 gap 含 \(Q\) 的全部 external-source terminal 都被
\(\mathcal T_{p,Q}\) 精确参数化。\(Q=q\) 为素数时，这正是既有的
\(\mathcal T_{p,q}\)。

## 3. 每个命中的 Type I 证书

取 \(t\in\mathcal T_{p,Q}\)，并写

\[
m=Qt,\qquad
x=\frac{p+m}{4},\qquad
d=ix,\qquad
B=\frac{p+i}{m}.
\tag{10}
\]

由 (9)，\(x\) 为整数，且 \(i\mid x\)，所以

\[
d=ix\mid x^2.
\tag{11}
\]

还需验证 \(m\) 落在自然范围。\(Q\) 的每个素因子在 (3) 中都给出 \(p\) 的非平凡
三阶剩余，故其为 \(1\pmod3\) 的奇素数；特别地 \(Q\ge7\)，从而 \(m\ge7\)。

若 \(B=1\)，则 \(m=p+i\)。由 \(4i\mid p+m=2p+i\) 得 \(i\mid2p\)。结合
(5)，只能有

\[
i\in\{2,p,2p\}.
\tag{12}
\]

第一种要求 \(8\mid2(p+1)\)，但 \(p\equiv1\pmod4\) 时右端恰为 \(4\pmod8\)；
后两种分别要求 \(4p\mid3p\) 或 \(8p\mid4p\)。三种均矛盾，故 \(B\ge2\)。于是

\[
p-m=m(B-1)-i\ge Q-i=\rho\ge2.
\tag{13}
\]

由 \(4i\mid p+m\) 又有 \(m\equiv3\pmod4\)。因此

\[
3\le m\le p-2.
\tag{14}
\]

最后，\(m\mid p+i\) 蕴涵

\[
m\mid x(p+i)=px+d.
\tag{15}
\]

所以 \((m,d)\) 是 Type I 除子证书，显式地

\[
\boxed{
\frac4p=
\frac1x+
\frac1{xB}+
\frac1{pxB/i}.}
\tag{16}
\]

## 4. Composite \(Q\) 的严格增量

取

\[
p=177433,\qquad
M=10494215641=7\cdot13\cdot19\cdot6069529,
\tag{17}
\]

并令

\[
u=91=7\cdot13,\qquad r=45.
\tag{18}
\]

于是 \(p\) 是核心素数，\((2r+1,M)=91\)，且 \(h=3u=273<p\)。两个已有
prime-only 菜单为

\[
\begin{array}{c|c|c|c|c}
Q&i&N&\tau\pmod {4i}&\mathcal T_{p,Q}\\ \hline
7&3&25348&5\pmod {12}&\varnothing\\
13&4&13649&3\pmod {16}&\varnothing.
\end{array}
\tag{19}
\]

但对 composite divisor \(Q=91\)，有

\[
\rho=74,\qquad
i=17,\qquad
N=1950,\qquad
\tau=5\pmod {68},
\tag{20}
\]

所以

\[
\mathcal T_{p,91}=\{5\}.
\tag{21}
\]

由 \(t=5\) 恢复

\[
(m,x,d,B)=(455,44472,756024,390).
\tag{22}
\]

这给出直接 Type I terminal

\[
\frac4{177433}
=
\frac1{44472}
+\frac1{17344080}
+\frac1{181024243920}.
\tag{23}
\]

因此 composite \(Q\) 不只是 prime menu 的重复书写：在这个 proper-root 控制中，
它严格增加了 terminal-first 可用的 root-capacity 外部源。

## 5. 边界

\(\mathcal T_{p,Q}\) 仍可能为空，甚至对同一 \(u\) 的所有 \(Q\mid u\) 都可能为空。
本结论只把 root-capacity terminal 的来源从单素因子扩展到任意子除子；它没有证明
任意 actual stutter 必命中该菜单，也没有构造尚未命中的全域解提升或严格递降。

## 聚焦复现

~~~bash
python3 reproductions/type_i_root_capacity_composite_divisor_external_terminal.py --verify
~~~

复现器只核对 (17)--(23) 的固定控制、两个 prime-menu 空集和 composite-menu 命中；
它不扫描素数区间、根层、分母或历史 selector。
