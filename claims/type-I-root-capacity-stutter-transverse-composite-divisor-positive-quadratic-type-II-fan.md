---
kind: claim
claim_id: type-I-root-capacity-stutter-transverse-composite-divisor-positive-quadratic-type-II-fan
title: 横向 stutter 任意子除子 Q 的正支二次 Type II 终端扇
statement: >-
  对核心素数 p≡1 mod24 的 terminal-first 后 actual proper-root stutter receipt，令
  D*=D/gcd(D,h^2-1)。取 p+3 的奇除数 A0、偶数 K>A0，且 gcd(A0,K)=1。对任意
  正除子 Q|D*（Q 不必为素数），若 Q|Kp+A0 且
  Q≡3K-A0 mod 4A0K，则 s=(Q+A0)/K、C=(p+s)/(4A0Q) 为正整数，
  3≤s≤p-2，且
  4/p=1/(A0QC)+1/(pA0CK)+1/(pQCK)
  是一张 Type II 证书。这个 whole-divisor 菜单包含先前一般二次扇的正支素数情形，
  并允许素数幂或复合 Q；它不证明任何 actual D* 必命中该菜单，也不构造递归边。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-transverse-residual-capacity-map
  - type-I-root-capacity-stutter-transverse-general-quadratic-type-II-fan
  - type-II-raw-ray-certificate
  - short-certificate-equivalence
topics:
  - type-I
  - type-II
  - root-capacity
  - stutter
  - transverse-residual
  - composite-divisor
  - quadratic-shift
  - root-residue
  - bounded-gap
  - two-tail-lift
  - terminal-dispatch
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-transverse-residual-capacity-map
    role: actual-D-star-transverse-divisor-input
  - claim: type-I-root-capacity-stutter-transverse-general-quadratic-type-II-fan
    role: prime-positive-branch-special-case
  - claim: type-II-raw-ray-certificate
    role: Type-II-raw-ray-certificate-reconstruction
  - claim: short-certificate-equivalence
    role: direct-Type-II-certificate-verifier
visibility: public
last_checked: '2026-08-18'
---

# 横向 stutter 任意子除子 $Q$ 的正支二次 Type II 终端扇

## 1. 设置与菜单

固定核心素数

\[
p\equiv1\pmod {24}.
\]

在 terminal-first 后，设仍有一份 actual proper-root stutter receipt。沿用

\[
D=mp+1-h,
\qquad D\mid ph+1,
\qquad
D_*=\frac{D}{(D,h^2-1)}.
\tag{1}
\]

取

\[
A_0\mid p+3,
\qquad A_0\text{ 为奇数},
\qquad K>A_0,
\qquad K\equiv0\pmod2,
\qquad (A_0,K)=1,
\tag{2}
\]

以及一个**任意的**正除子

\[
Q\mid D_*.
\tag{3}
\]

这里不要求 (Q) 为素数或素数幂。假设这个 whole-divisor 同时落在正支和
raw-ray 剩余类：

\[
Q\mid Kp+A_0,
\qquad
Q\equiv3K-A_0\pmod {4A_0K}.
\tag{4}
\]

以下证明这些条件直接给出 Type II terminal。

## 2. 与二次移位的精确接口

因为 (Q\mid D\mid ph+1)，有 ((Q,p)=1)。由 (4) 模 (K) 化简，

\[
Q\equiv-A_0\pmod K,
\]

所以

\[
(Q,K)=1.
\tag{5}
\]

若某个素数同时整除 (Q) 与 (A_0)，则由 (Q\mid Kp+A_0) 和

\((Q,p)=1\)

它也整除 (K)，与 (2) 矛盾。因此

\[
(Q,A_0K)=1.
\tag{6}
\]

特别地，(4) 的右侧为奇数，故 (Q) 为奇数，且 ((Q,4A_0K)=1)。

虽然下面的 terminal 构造只需要 (3)--(4)，它确实仍是一般二次移位的
whole-divisor 正支。由 (Q\mid D) 有

\[
mp^2+p+1\equiv0\pmod Q.
\tag{7}
\]

将 (7) 乘以 (K^2)，并用 (Kp\equiv-A_0\pmod Q)，得到

\[
\boxed{Q\mid mA_0^2+K(K-A_0).}
\tag{8}
\]

同样地，(h\equiv mp+1\pmod Q) 给出

\[
\boxed{A_0h\equiv K\pmod Q.}
\tag{9}
\]

所以 (4) 正是已有一般二次扇中选定正线性因子的 whole-divisor 版本。与素数
情形不同，(3) 在这里必须作为显式前提：对于复合 (Q)，不能由 (9) 反推出每个
素因子都避开 (h^2-1)。

## 3. 缺口与整除性

定义

\[
s=\frac{Q+A_0}{K},
\qquad
C=\frac{p+s}{4A_0Q}.
\tag{10}
\]

式 (4) 先保证 (s\) 是整数，并给出

\[
s\equiv3\pmod {4A_0}.
\tag{11}
\]

因为 (0<3K-A_0<4A_0K)，(4) 的最小正剩余就是 (3K-A_0)。于是

\[
Q\ge3K-A_0>K+A_0,
\qquad s\ge3.
\tag{12}
\]

由 (9) 和 (12) 得 $0<K<Q$。因此正支参数被实际根高度唯一强制为最小正剩余：

\[
\boxed{K=\langle A_0h\rangle_Q.}
\tag{13a}
\]

所以这个 whole-divisor 菜单保留了先前素数 root-residue 构造的根高度 provenance；
它不是任意选择的 raw-ray。

另一方面，

\[
K(p+s)=Kp+Q+A_0\equiv0\pmod Q.
\tag{13}
\]

由 (5)，有 (Q\mid p+s)。又因 (A_0) 为奇数且 (A_0\mid p+3)，

\[
4A_0\mid p+3.
\tag{14}
\]

将 (11) 与 (14) 相加，得 (4A_0\mid p+s)。再用 (6)，即可得

\[
C\in\mathbb Z_{>0}.
\tag{15}
\]

还需证明自然缺口上界。令 (L=Kp+A_0)，它是奇数。若 (Q=L)，把 (4)
模 (K) 化简，得到 (K\mid2A_0)。由 (2) 只能有

\[
(K,A_0)=(2,1).
\]

但这时 (Q=2p+1\equiv3\pmod8)，而 (4) 要求 (Q\equiv5\pmod8)，矛盾。
所以 (Q) 是 (L) 的真因子。由于 (L/Q) 是大于 1 的奇整数，

\[
Q\le\frac{Kp+A_0}{3}.
\tag{16}
\]

故

\[
s\le\frac p3+\frac{4A_0}{3K}
<\frac p3+\frac43
\le p-2.
\tag{17}
\]

最后一步只使用核心素数必有 (p\ge73)。结合 (12)，有

\[
3\le s\le p-2.
\tag{18}
\]

## 4. Type II 证书

令

\[
x=A_0QC,
\qquad d=A_0^2C.
\tag{19}
\]

由 (Q>A_0)，有 (d\le x)，并且

\[
d\mid x^2,
\qquad
x+d=A_0C(Q+A_0)=A_0CKs.
\tag{20}
\]

因此 ((s,d)) 是自然范围的 Type II 除子证书。等价地，它是
`type-II-raw-ray-certificate` 的参数

\[
(A,C,K)=(A_0,C,K),
\qquad
4A_0CK-1=\frac{Kp+A_0}{Q},
\qquad B=Q
\tag{21}
\]

所恢复的证书。显式地，

\[
\boxed{
\frac4p=
\frac1{A_0QC}+
\frac1{pA_0CK}+
\frac1{pQCK}.}
\tag{22}
\]

这是一条 direct terminal；它不需要 E1--E5 或分母递降。

## 5. 低缺口切片的严格两尾提升

再假设

\[
s\in\{3,7,11,23\}.
\tag{LG1}
\]

由于 $s+1\mid24\mid p-1$，整数

\[
n=\frac{p+s}{s+1}
\tag{LG2}
\]

满足 $0<n<p$。由 $Q+A_0=Ks$，

\[
\frac1{A_0QC}+\frac1{A_0CK}+\frac1{QCK}
=\frac{K+Q+A_0}{A_0QCK}
=\frac{s+1}{A_0QC}
=\frac4n.
\tag{LG3}
\]

保留首分母并将后两尾乘以 $p$，恰恢复 (22)。所以 low-gap whole-divisor hit
还给出显式的 singleton two-tail lift

\[
\frac4n\longrightarrow\frac4p,
\qquad n<p.
\tag{LG4}
\]

这是先前 prime root-residue low-gap construction 的 arbitrary-divisor 版本。它只提升
所写出的 $4/n$ 分解，不是全域的
$\operatorname{Sol}(n)\to\operatorname{Sol}(p)$ E4 lift，因此不能单独登记为
T6 recursive edge。

## 6. (A_0=1) 的无选择 whole-divisor 因子门

令

\[
\mathcal Q_s^{\mathrm{whole}}(D_*,h)
=\left\{
Q>1:
Q\mid(D_*,sh-1),
\quad Q\equiv-1\pmod {2s}
\right\},
\qquad s\in\{3,7,11,23\}.
\tag{WG1}
\]

这里的 (Q) 不要求为素数。对任意

\[
Q\in\mathcal Q_s^{\mathrm{whole}}(D_*,h),
\tag{WG2}
\]

令

\[
K=\frac{Q+1}{s}.
\tag{WG3}
\]

由 (Q\equiv-1\pmod {2s})，(K) 是偶整数；又 (s\ge3)，所以

\[
1<K<Q.
\tag{WG4}
\]

此外 ((Q,s)=1)，而 (Q\mid sh-1) 与 (sK=Q+1) 联立给出

\[
K\equiv h\pmod Q.
\tag{WG5}
\]

因为 (Q\mid D_*\mid D\mid ph+1)，有 (Q\mid Kp+1)。最后，

\[
Q=Ks-1\equiv3K-1\pmod {4K},
\tag{WG6}
\]

其中最后一个同余只使用 (s\equiv3\pmod4)。因此 (WG2) 自动满足本定理的

\[
A_0=1,
\qquad K=\langle h\rangle_Q
\tag{WG7}
\]

切片。每个 (Q\in\mathcal Q_s^{\mathrm{whole}}(D_*,h)) 所以给出第 4--5 节的
Type II terminal 与 (n=(p+s)/(s+1)<p) 的 singleton two-tail lift。

当 (Q=q) 为素数时，(WG1) 恰恢复既有 prime root-residue low-gap 因子门；
这里额外允许完整的素数幂或复合 (Q)。剩余类 (Q\equiv-1\pmod {2s}) 不按
素因子继承，因此这一 whole-divisor menu 不能化约为逐个素因子的重复检查。

## 7. 多因子增量与边界

当 (Q=q) 为素数时，已有一般二次扇的 shift gate 加正支正好导出 (3)--(4)，
故它是本菜单的一个特例。这里允许整个 (Q) 同时作为 raw-ray 的 (B)-坐标。
条件

\[
Q\equiv3K-A_0\pmod {4A_0K}
\]

不按素因子继承，因此不能把这个 whole-divisor 菜单缩回为“逐个素数检查”的
重复写法。例如在纯算术层，

\[
(p,A_0,K,Q)=(1297,1,22,65)
\]

满足

\[
65\mid22\cdot1297+1,
\qquad
65\equiv3\cdot22-1\pmod {88},
\]

并给出 (s=3,C=5) 及

\[
\frac4{1297}
=\frac1{325}+\frac1{142670}+\frac1{9273550}.
\tag{23}
\]

但 (65) 的两个素因子 (5,13) 都不满足同一 (K=22,A_0=1) 的剩余类。
这个例子只说明多因子剩余类的真实增量；它**不是** actual stutter receipt，
更不声称 (65\mid D_*)。

本定理没有证明：

* actual (D_*) 必有一个除子 (Q) 满足 (4)；
* 任意未命中本菜单的 actual proper-root state 另有 Type I/II terminal；
* 未命中时存在带 E1--E5 的 strict successor。

因此它只扩张 TR1 的 terminal-first 条件菜单，不能关闭 TR1、QC1、proper-root
totality 或 `T6_GLOBAL_SELECTOR_TOTALITY`。
