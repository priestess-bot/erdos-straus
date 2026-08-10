---
kind: claim
claim_id: type-II-linear-square-gcd-allocation-core-gap-cutoff
title: Type II 的线性平方因子分配、最小余量构造与核心缺口 p/3 隔离线
statement: >-
  设 p 为 1 mod 4 素数、3<=m=4y-p<=p-2 为合法自然缺口。令
  y/m<L<=2y/m、d_L=Lm-y，
  g_L=gcd(d_L,L)。则 gap m 的 Type II 证书与满足 d_L|L^2 的整数 L 一一对应，
  且 d_L|L^2 当且仅当 d_L/g_L|g_L；命中时可显式恢复互素正规形
  A=d_L/g_L、B=y/g_L、C=g_L^2/d_L、K=L/g_L。最小 L_0=floor(y/m)+1 的
  余量 r=L_0m-y 命中，当且仅当 r 的平方根核 rho(r) 整除 L_0。若 m>p/3，
  L 区间只有 L=1，Type II 存在当且仅当 p=3m-4；因此每个核心素数
  p=1 mod 24 的任何 Type II 缺口都严格满足 m<p/3。first-overflow 另有
  gcd(M,y)=1，所以所有 Type II 因子 d 都与 q-prefix 模数 M 互素；q-primary
  prefix 本身不能直接充当 Bradford 因子。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - short-certificate-equivalence
  - type-II-coprime-factor-normal-form
  - type-II-raw-normal-form-sqrt-cutoff
  - type-I-fg-qprefix-block-bound-first-overflow-terminal
topics:
  - type-II
  - divisor-parametrization
  - linear-square
  - gcd-allocation
  - short-certificate
  - gap-bound
  - first-overflow
  - q-prefix
  - proof-program
sources:
  - claim: short-certificate-equivalence
    role: complete-natural-gap-Type-II-menu
  - claim: type-II-coprime-factor-normal-form
    role: ABC-K-normal-form
  - claim: type-II-raw-normal-form-sqrt-cutoff
    role: previous-p-over-3-plus-sqrt-p-boundary
  - reproduction: reproductions/type_ii_linear_square_gcd_allocation_core_gap_cutoff.py
    role: focused-bijection-minimal-residual-and-two-overflow-controls
visibility: public
last_checked: '2026-08-10'
---

# Type II 的线性平方因子分配、最小余量构造与核心缺口 \(p/3\) 隔离线

## 1. Type II 证书的线性平方参数化

令 \(p\equiv1\pmod4\) 为素数，并令

\[
m=4y-p,
\qquad
3\le m\le p-2.
\tag{1}
\]

于是 \(p/4<y<p/2<p\)，并且

\[
\gcd(m,y)=\gcd(p,y)=1.
\tag{2}
\]

定义有限整数区间

\[
\mathcal L(m,y)
=\left\{L\in\mathbb Z:
\frac ym<L\le\frac{2y}{m}\right\},
\tag{3}
\]

并对 \(L\in\mathcal L(m,y)\) 置

\[
d_L=Lm-y,
\qquad
g_L=\gcd(d_L,L).
\tag{4}
\]

由 (3)，恰有 \(0<d_L\le y\)。Type II 证书

\[
d\mid y^2,\qquad d\le y,\qquad m\mid y+d
\tag{5}
\]

与满足

\[
\boxed{L\in\mathcal L(m,y),\qquad d_L\mid L^2}
\tag{6}
\]

的整数 \(L\) 一一对应；双向变换为

\[
L=\frac{y+d}{m},
\qquad
d=d_L=Lm-y.
\tag{7}
\]

证明只需观察

\[
\gcd(d_L,m)=\gcd(y,m)=1,
\qquad
y\equiv Lm\pmod{d_L}.
\]

因此

\[
d_L\mid y^2
\quad\Longleftrightarrow\quad
d_L\mid L^2m^2
\quad\Longleftrightarrow\quad
d_L\mid L^2.
\tag{8}
\]

这把“枚举 \(y^2\) 的全部除子”改写成长度约为 \(y/m\) 的线性 \(L\)-窗口。

## 2. gcd 因子分配与互素正规形

由 \(d_L=Lm-y\)，还有

\[
g_L
=\gcd(d_L,L)
=\gcd(y,L)
=\gcd(d_L,y).
\tag{9}
\]

写 \(d_L=g_La,L=g_Lb\)，其中 \((a,b)=1\)。则

\[
d_L\mid L^2
\quad\Longleftrightarrow\quad
g_La\mid g_L^2b^2
\quad\Longleftrightarrow\quad
a\mid g_L.
\]

所以 (6) 还有不需要平方大整数的精确判据

\[
\boxed{
d_L\mid L^2
\quad\Longleftrightarrow\quad
\frac{d_L}{g_L}\mid g_L.}
\tag{10}
\]

命中时定义

\[
A=\frac{d_L}{g_L},
\qquad
B=\frac y{g_L},
\qquad
C=\frac{g_L^2}{d_L},
\qquad
K=\frac L{g_L}.
\tag{11}
\]

式 (10) 保证 \(C\in\mathbb N\)。由 (9) 与 \(d_L\le y\)，逐项得到

\[
\boxed{
y=ABC,
\quad d_L=A^2C,
\quad (A,B)=1,
\quad A\le B,
\quad A+B=Km.}
\tag{12}
\]

所以 (11) 不是另一套候选坐标，而是每张 Type II 证书的规范 gcd 因子分配；反向
代入 (12) 唯一恢复 (7)。

## 3. 最小线性余量的平方根核门

取窗口中的最小整数

\[
L_0=\left\lfloor\frac ym\right\rfloor+1,
\qquad
r=L_0m-y.
\tag{13}
\]

因 \(m<p\)，有 \(m<2y=(p+m)/2\)。若 \(y<m\)，则 \(L_0=1<2y/m\)；
若 \(y\ge m\)，则 \(L_0\le y/m+1\le2y/m\)。所以
\(L_0\in\mathcal L(m,y)\) 且 \(1\le r\le y\)。又由
\(\gcd(m,y)=1\) 与 \(m\ge3\)，有 \(r<m\)。对正整数
\(r=\prod_\ell\ell^{e_\ell}\)，定义平方根核

\[
\rho(r)=\prod_\ell\ell^{\lceil e_\ell/2\rceil}.
\tag{14}
\]

逐素数比较指数立即给出

\[
\boxed{
d=r\text{ 是 Type II 证书}
\quad\Longleftrightarrow\quad
r\mid L_0^2
\quad\Longleftrightarrow\quad
\rho(r)\mid L_0.}
\tag{15}
\]

这是一个构造性充分必要门：只需分解小余量 \(r<m\)，而不必分解 \(y^2\)。若 (15)
失败，仍可能有更大的 \(L\in\mathcal L(m,y)\) 命中；它不是全 Type II 菜单的 no-go。

## 4. 核心素数的精确 \(p/3\) 隔离线

若

\[
m>\frac p3,
\tag{16}
\]

则由 \(y=(p+m)/4\) 得

\[
\frac m2<y<m.
\tag{17}
\]

所以 (3) 中唯一的整数是 \(L=1\)。相应

\[
d_1=m-y.
\]

又由 (2)，\(\gcd(d_1,y)=1\)。因此 \(d_1\mid y^2\) 当且仅当 \(d_1=1\)，即

\[
\boxed{
m>p/3\text{ 时 Type II 存在}
\quad\Longleftrightarrow\quad
m-y=1
\quad\Longleftrightarrow\quad
p=3m-4.}
\tag{18}
\]

若 \(p\equiv1\pmod3\)，等式 \(p=3m-4\) 不可能，因为右侧模 \(3\) 等于 \(2\)。
每个核心素数 \(p\equiv1\pmod{24}\) 都满足这一条件，故

\[
\boxed{
p\equiv1\pmod{24}
\quad\Longrightarrow\quad
\text{每张 Type II 证书的缺口 }m<\frac p3.}
\tag{19}
\]

式 (19) 把既有 \(p/3+O(\sqrt p)\) 上界加强为严格的精确隔离线。它只约束 Type II；
Type I 仍可能出现在 \(m\ge p/3\) 的区域。

## 5. first-overflow 与 q-prefix 的正交性

first-overflow CRT map 还给出

\[
\gcd(M,y)=1.
\tag{20}
\]

任意 Type II 因子 \(d\mid y^2\) 因而满足

\[
\boxed{\gcd(d,M)=1.}
\tag{21}
\]

特别地，若 \(M=q^a\)，则 \(d\) 必为 \(q\)-free。q-prefix 的非平凡 \(q\)-幂不能
直接重复收费为 Bradford divisor；真正的终端门是某个 \(L\) 满足 (10)，或最小余量
满足 (15)。同一个 \(M\) 可以同时出现命中与空菜单，因此 q-primary prefix 本身不
强制 Type II。

## 6. 两个 \(M=27\) 控制

### 菜单空控制

对

\[
(p,M,m,y)=(73,27,43,29),
\]

有 \(m>p/3\) 且 \(p\equiv1\pmod3\)，所以 (18) 已整体排除 Type II。Type I 只需
检查 \(d\mid29^2\)，三个候选 \(d=1,29,841\) 给出

\[
73\cdot29+d\equiv11,39,34\pmod{43},
\]

全部非零，故完整 Bradford 菜单为空。

### 最小余量命中控制

对

\[
(p,M,m,y)=(557281,27,79,139340),
\]

式 (13)--(15) 给出

\[
L_0=1764,
\qquad r=16,
\qquad \rho(r)=4\mid1764.
\tag{22}
\]

因此 \(d=16\) 是 Type II 证书。这里 \(g=\gcd(16,1764)=4\)，而 (11) 精确恢复

\[
(A,B,C,K)=(4,34835,1,441).
\tag{23}
\]

这再次给出既有分解

\[
\frac4{557281}
=\frac1{139340}
 +\frac1{983043684}
 +\frac1{8561081683035}.
\tag{24}
\]

两个控制使用相同 \(M=27\)：前者由 (18) 结构性排除 Type II，后者由 (15) 的最小
余量直接构造 Type II。这精确定位了下一全称命题所需的额外信息：证明某个 \(L\) 的
gcd allocation 命中，或转入 Type I/common-denominator E4，而不是继续扩大 q-prefix
自身的容量解释。

## 聚焦验证

~~~bash
python3 reproductions/type_ii_linear_square_gcd_allocation_core_gap_cutoff.py --verify
~~~

验证器只在 \(p=17\) 边界和两个 \(M=27\) 聚焦控制上核对 (6)--(15) 的双向变换；
全称结论由正文代数证明，不由有限测试代替。验证器不运行历史扫描。
