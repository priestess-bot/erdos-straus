---
kind: claim
claim_id: type-I-root-capacity-stutter-transverse-negative-branch-fixed-gap-same-carrier-barrier
title: 横向 stutter 负根对有限固定缺口同载体菜单的边界
statement: >-
  固定 s∈{3,7,11,23} 和任意有限正整数集合 R。存在无穷多个 q-local transverse
  negative-root 数据 (p,q,K,h,m)：p 为核心素数，q 是 D*=D/gcd(D,h^2-1) 的奇素因子，
  K=(q+1)/s 为偶数，q 整除 ((K-1)p-1) 而不整除 Kp+1，且 q 对每个 r∈R 都不整除
  p+r。故只读取这条负支及同一 q、并要求某个固定 r 的 q|p+r 才能进入的任意有限
  fixed-gap adapter，不能全称关闭负支。构造仅满足 q-local stutter 同余，不断言
  D|ph+1 或 actual proper-root receipt；它不排除可变 gap、不同 carrier、其它 Type I/II
  证书或由完整 actual provenance 得到的递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-transverse-residual-capacity-map
  - type-I-root-capacity-stutter-transverse-quadratic-shift-type-II-fan
  - type-I-root-capacity-stutter-transverse-low-gap-m-polynomial-root-split
topics:
  - type-I
  - type-II
  - root-capacity
  - stutter
  - transverse-residual
  - negative-branch
  - bounded-gap
  - fixed-gap
  - same-carrier
  - Dirichlet-theorem
  - counterexample
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-transverse-low-gap-m-polynomial-root-split
    role: negative-root-and-negative-linear-branch-interface
  - claim: type-I-root-capacity-stutter-transverse-root-residue-low-gap-descent
    role: positive-root-same-carrier-low-gap-terminal-interface
  - claim: type-II-finite-template-obstruction
    role: finite-menu-rigidity-context
  - reproduction: reproductions/type_i_root_capacity_stutter_transverse_negative_branch_fixed_gap_barrier.py
    role: fixed-q-local-negative-root-and-residue-equation-controls
visibility: public
last_checked: '2026-08-14'
---

# 横向 stutter 负根对有限固定缺口同载体菜单的边界

## 1. 要排除的精确收口方式

固定一个自动低缺口

\[
s\in\mathcal G=\{3,7,11,23\}.
\tag{1}
\]

前一张卡已经把 \(m\)-side 碰撞的负根精确定位为

\[
q\mid((K-1)p-1),
\qquad
q\nmid Kp+1,
\qquad
K=\frac{q+1}{s}\equiv0\pmod2.
\tag{2}
\]

正根的 \(A=1\) low-gap terminal 还会要求同一载体满足

\[
q\mid p+s.
\tag{3}
\]

因此，一个自然的补法是：保留负支的同一个 \(q\)，但把 (3) 扩展为有限个预先固定的
缺口。为避免把这个狭窄想法误写成一般 Type II 定理，给定任意有限集合

\[
\mathcal R\subset\mathbb Z_{>0},
\tag{4}
\]

本卡只研究以下明确的同载体门：

\[
\exists r\in\mathcal R:\ q\mid p+r.
\tag{SC}_{\mathcal R}
\]

结论是 \(\mathrm{SC}_{\mathcal R}\) 不能仅由负根的局部同余强制。这不等于说这些
数据没有其它证书，也不等于说 actual stutter receipt 可实现该局部数据。

## 2. 负支把同载体门化成有限个 \(L\) 值

令

\[
L=K-1,
\qquad
q=sK-1=sL+s-1.
\tag{5}
\]

在 (2) 的负支上有

\[
Lp\equiv1\pmod q.
\tag{6}
\]

因为 \(0<L<q\)，对任何固定 \(r>0\)，(6) 给出严格等价

\[
q\mid p+r
\Longleftrightarrow
q\mid Lr+1.
\tag{7}
\]

若 (7) 成立，写

\[
Lr+1=tq=t(sL+s-1),
\qquad t\in\mathbb Z_{>0}.
\tag{8}
\]

由于 \(q>sL\)，有

\[
1\le t<\frac{r+1}{s}.
\tag{9}
\]

将 (8) 展开，得到

\[
\boxed{
L(r-ts)=t(s-1)-1.}
\tag{10}
\]

若 \(r-ts=0\)，右端至少为 \(s-2>0\)，矛盾。故每个可能的 \(t\) 至多确定一个
整数 \(L\)。按 (9)，对固定 \(r\) 只有有限个 \(t\)，从而

\[
\mathcal E_{s,\mathcal R}
=\{L>1:\ \exists r\in\mathcal R,\ q=sL+s-1\mid Lr+1\}
\tag{11}
\]

是有限集。注意此处甚至没有要求 \(q\) 为素数；因此对真正的 prime carrier 也同样成立。

## 3. 无穷 q-local 负根族

由 Dirichlet 的算术级数素数定理，进程

\[
q\equiv-1\pmod {2s}
\tag{12}
\]

包含无穷多个奇素数。对充分大的此类 \(q\)，令

\[
K=\frac{q+1}{s},
\qquad L=K-1,
\tag{13}
\]

则 \(K\) 为偶数、\(L>1\)，且可避开有限集 (11)。固定这样的 \((q,L)\)。

这里 \(q\ne2,3\)，且 \(L^{-1}\not\equiv0\pmod q\)，故 CRT 给出的下面剩余类确实与
\(24q\) 互素。再由 CRT 与 Dirichlet 定理，原始剩余类

\[
p\equiv1\pmod {24},
\qquad
p\equiv L^{-1}\pmod q
\tag{14}
\]

含无穷多个素数；取其中充分大的一个。选取唯一的正整数 \(h<3q\)，使

\[
h\equiv-L\pmod q,
\qquad h\equiv0\pmod3,
\tag{15}
\]

并令 \(m\) 是下列非零模 \(q\) 剩余的最小正代表：

\[
m\equiv-L(L+1)\pmod q.
\tag{16}
\]

非零性来自 \(0<L<L+1<q\)。令 \(D=mp+1-h\)。由 (14)--(16) 直接有

\[
ph+1\equiv0,
\qquad
D\equiv0,
\qquad
m+h(h-1)\equiv0
\pmod q.
\tag{17}
\]

又 \(L>1\) 且 \(L+1<q\)，故 \(h\equiv-L\not\equiv\pm1\pmod q\)。所以

\[
q\mid D_*=\frac{D}{(D,h^2-1)}.
\tag{18}
\]

记

\[
\Delta_s=ms^2-s+1,
\qquad
F_s^+=sh-1,
\qquad
F_s^-=s(h-1)+1.
\tag{19}
\]

此时

\[
F_s^-\equiv-s(L+1)+1=-q\equiv0\pmod q,
\qquad
F_s^+\equiv s-2\not\equiv0\pmod q.
\tag{20}
\]

结合 (17) 与恒等的代数二根式
\(\Delta_s+F_s^+F_s^-=s^2(m+h(h-1))\)，有 \(q\mid\Delta_s\)。这正是负根，
而不是正根。并且

\[
(K-1)p-1=Lp-1\equiv0\pmod q.
\tag{21}
\]

若 \(q\mid Kp+1\)，将此式乘以 \(L\)，再使用 \(Lp\equiv1\pmod q\)，会给出
\(q\mid K+L=2L+1\)；但

\[
0<2L+1<q=sL+s-1
\tag{22}
\]

（因 \(s\ge3,L>1\)），矛盾。因此确有 \(q\nmid Kp+1\)。最后，由避开 (11) 和
(7)，对每个 \(r\in\mathcal R\) 均有

\[
q\nmid p+r.
\tag{23}
\]

这完成无穷 q-local family 的构造。

关键量词边界是：式 (17) 只保证 \(q\mid D\) 与 \(q\mid ph+1\)，没有保证完整的

\[
D\mid ph+1.
\tag{24}
\]

所以该族严格排除的是任何**只**使用这些 q-local 关系来强迫

\((\mathrm{SC}_{\mathcal R})\) 的证明；完整 actual receipt 的额外整除、maximality 或
source/path provenance 仍可能创造新的出口。

## 4. 两个固定控制

第一组控制为

\[
(p,q,h,m,s,K,L)=(313,17,12,4,3,6,5).
\tag{25}
\]

它给出

\[
D=1241=17\cdot73,
\qquad ph+1=3757=17\cdot221,
\qquad D_*=1241,
\tag{26}
\]

以及

\[
\Delta_3=34,
\qquad F_3^+=35,
\qquad F_3^-=34.
\tag{27}
\]

故 \(17\) 精确落在负根；同时

\[
17\mid5\cdot313-1,
\qquad17\nmid6\cdot313+1,
\tag{28}
\]

并且 \(17\) 不整除 \(313+r\) 的任一

\[
r\in\{3,7,11,23\}.
\tag{29}
\]

第二组控制

\[
(p,q,h,m,s,K,L)=(3313,41,36,11,7,6,5)
\tag{30}
\]

在不同的自动低缺口 \(s=7\) 上重放同一负支，并同样避开 (29) 的四个 \(r\)。两组都只
检查 q-local 代数；例如 (25) 中 \(1241\nmid3757\)，故绝不被记作 actual stutter
receipt。

复现命令：

```bash
python3 reproductions/type_i_root_capacity_stutter_transverse_negative_branch_fixed_gap_barrier.py --verify
```

脚本只重算这两组局部控制、(7) 的精确同余等价和 (10) 的一个命中例；它不扫描素数、根层、
分母或历史 selector，也不以有限计算替代上面的 Dirichlet--CRT 证明。

## 5. 对下一条 adapter 的限制

本卡不是 Erdős--Straus 猜想的反例，也不否定存在一个新的 negative-branch terminal 或
strict lift。它只消除了一个具体而诱人的收口策略：不断往同一个负支 \(q\) 上添加有限个
预设 \(p+r\) 缺口。下一条有希望的桥必须至少读取下列之一：

* 随 \((p,q,h,m)\) 自适应变化的 gap；
* 与 \(q\) 不同的因子或一个多因子 Type I/II 结构；
* actual receipt 的整除、maximality 或 source/path 数据，以排除上述 q-local 族或构造
  可验证的 lift。

因此 (23) 是一个路线边界，而不是全局无证书结论。
