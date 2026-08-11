---
kind: claim
claim_id: type-I-gap23-adaptive-divisor-terminal-selector
title: gap 23 的自适应 d=2r Type I 终端选择子
statement: 对核心素数 p=24h+1，置 s=h+1、x=6s。对每个 r|s，令 d=2r，则 d|x 且 d<=x/3；该 gap-23 Type I 模板成立当且仅当 r(s/r)^2=15 (mod 23)。等价地，15 属于上除子盒 U_23(s)={s^2/r (mod 23): r|s}。因此这给出一个由 s 的完整因子分解可判定、可显式恢复的直接 terminal。把它接在 R=11/gap-7/gap-11 三路 dispatch 之后，四路共同残余精确等于原三项残余条件再加 15 不属于 U_23(s)。特别地，p=1201+1656a 的每个素数参数均以 r=17+23a、d=34+46a 直接终止；该 primitive Dirichlet 射线包含 p=1201，并在 p=2857 给出一个不属于已有 gap-23 自动 Type II 九类且不满足固定 d=34 条件的 Type I control。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - short-certificate-equivalence
  - type-I-gap23-d34-terminal-rays
  - type-I-r11-gap7-gap11-terminal-descent-dispatch
topics:
  - type-I
  - terminal-first
  - gap-twenty-three
  - adaptive-divisor
  - short-certificate
  - joint-residual
  - dirichlet-ray
  - proof-boundary
sources:
  - claim: short-certificate-equivalence
    role: Type-I-divisor-reconstruction
  - claim: type-I-gap23-d34-terminal-rays
    role: fixed-r-special-case-and-p1201-control
  - claim: type-I-r11-gap7-gap11-terminal-descent-dispatch
    role: exact-three-route-residual-to-extend
  - claim: type-II-shared-gap-23-automatic-fan
    role: nine-automatic-Type-II-class-boundary
  - reproduction: reproductions/type_i_gap23_adaptive_divisor_terminal_selector.py
    role: symbolic-selector-and-four-route-controls
visibility: public
last_checked: '2026-08-12'
---

# gap (23) 的自适应 (d=2r) Type I 终端选择子

## 1. 精确的上除子盒判据

令

\[
p=24h+1,
\qquad s=h+1,
\qquad m=23,
\qquad x=\frac{p+23}{4}=6s.
\tag{1}
\]

给定任意正因子 (r\mid s)，写 (s=rt)，并取

\[
d=2r.
\tag{2}
\]

**定理。** 对每个核心素数 (p)，(2) 是 gap (23) 的 Type I
除子证书，当且仅当

\[
\boxed{r t^2\equiv15\pmod {23}.}
\tag{3}
\]

在命中时，显式分母为

\[
\boxed{
y=\frac{px+2r}{23},
\qquad
z=\frac{p\left(x+px^2/(2r)\right)}{23},
\qquad
\frac4p=\frac1x+\frac1y+\frac1z.}
\tag{4}
\]

**证明。** 由 (r\mid s)，

\[
d=2r\mid6s=x,
\qquad d\le2s=x/3.
\tag{5}
\]

故特别有 (d\mid x^2)。又 (p=24s-23\equiv s\pmod {23})，所以

\[
23\mid px+d
\Longleftrightarrow
6s^2+2r\equiv0\pmod {23}
\Longleftrightarrow
r\equiv-3s^2\pmod {23}.
\tag{6}
\]

核心素数不可能等于 (23)，故 (23\nmid p)，进而由 (p\equiv s\pmod {23})
有 (23\nmid s) 及 (23\nmid r)。把 (s=rt) 代入 (6) 并除以 (r)，得

\[
1\equiv-3rt^2\pmod {23}
\Longleftrightarrow
rt^2\equiv15\pmod {23},
\tag{7}
\]

其中 (15\equiv-3^{-1}\pmod {23})。这证明了 (3) 与 Type I 除子条件的充要性；
(4) 由标准 Type I 重建式立即得到。证毕。

定义有限的**上除子盒**

\[
\mathcal U_{23}(s)
=\left\{\frac{s^2}{r}\pmod {23}:r\mid s\right\}.
\tag{8}
\]

由于 (s^2/r=rt^2)，上式把定理压缩成精确的因子判据

\[
\boxed{\text{该自适应 Type I terminal 存在}
\Longleftrightarrow15\in\mathcal U_{23}(s).}
\tag{9}
\]

若 (s=\prod \ell_i^{e_i})，盒中元素正是

\[
\prod_i\ell_i^{b_i}\pmod {23},
\qquad e_i\le b_i\le2e_i.
\tag{10}
\]

故 (9) 不是截断搜索：它是 (s) 的完整素因子分解上的有限、精确判定。

## 2. 一条真正自适应的非自动射线

固定余因子 (t=3)，令

\[
r=17+23a,
\qquad
s=3r=51+69a,
\qquad
h=50+69a.
\tag{11}
\]

于是

\[
rt^2=9(17+23a)\equiv15\pmod {23},
\tag{12}
\]

所以每个素数参数

\[
\boxed{p=1201+1656a}
\tag{13}
\]

都有直接 Type I certificate (4)，其中

\[
x=306+414a,
\qquad d=34+46a.
\tag{14}
\]

因为

\[
\gcd(1201,1656)=1,
\tag{15}
\]

Dirichlet 定理保证 (13) 含无穷多个素数。所有这些参数满足

\[
p\equiv5\pmod {23},
\tag{16}
\]

而 (5) 不在 gap-23 自动共享 Type II 九类
\(\{7,10,11,15,17,19,20,21,22\}\) 中。因此此射线不是已有固定共享表的重述。

它在 (a=0) 给出已知控制 (p=1201,r=17,d=34)。但它还包含

\[
p=2857,
\qquad h=119,
\qquad s=120,
\qquad r=40,
\qquad d=80,
\tag{17}
\]

并给出

\[
\boxed{
\frac4{2857}
=\frac1{720}+\frac1{89440}+\frac1{2299770720}.}
\tag{18}
\]

此时 (17\nmid120)，所以旧的固定 (d=34) 条件不成立；同时 (16) 排除了九个
自动 Type II 子扇。这里仅比较已登记的两种 gap-23 模板，不声称 (2857) 没有其它
短证书或递降。

## 3. 对 R=11/gap-7/gap-11 残余的精确增量

把本选择子置于
`type-I-r11-gap7-gap11-terminal-descent-dispatch` 的三项之后。前三项均未命中时，
若 (15\in\mathcal U_{23}(s))，(4) 直接终止；不需要新增递归边或 source receipt。

因此四路均未命中的充要条件是：

\[
\begin{array}{ll}
\text{(i)}&N=22h+1\text{ 属于 R=11 固定尾的 QR11 或 }(2,6,1)\text{ 精确残余类};\\
\text{(ii)}&u=3h+1\text{ 的每个素因子均为模 }7\text{ 二次剩余};\\
\text{(iii)}&-1\notin\mathcal R_{11}(3(2h+1));\\
\text{(iv)}&15\notin\mathcal U_{23}(h+1).
\end{array}
\tag{19}
\]

原三路共同残余控制 (p=1201) 有

\[
s=51=17\cdot3,
\qquad17\cdot3^2\equiv15\pmod {23},
\tag{20}
\]

故第四项精确关闭它。这是对已知 residual 的一条新 terminal 分支；(19) 仍可能非空，
因而不构成全局出口定理或 Erd\H{o}s--Straus 猜想的证明。

复现：

```bash
python3 reproductions/type_i_gap23_adaptive_divisor_terminal_selector.py --verify
```
