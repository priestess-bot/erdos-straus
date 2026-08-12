---
kind: claim
claim_id: type-I-24c-minus-one-adaptive-divisor-terminal-family
title: 24c-1 缺口族的自适应 d=2r Type I 终端
statement: 对核心素数 p=24h+1 和任意 1<=c<=h，置 m=24c-1、s=h+c、x=6s。对每个 r|s，令 d=2r，则 d|x 且 d<=x/3；该 gap-m Type I 模板成立当且仅当 r(s/r)^2=-72^(-1) (mod m)，等价于目标 -72^(-1) 属于 U_m(s)={s^2/r (mod m):r|s}。m=23 给出已有目标 15 的选择子；m=47 也有目标 15，并把该选择子接在 R=11/gap-7/gap-11/gap-23 四路之后，得到精确的第五条 direct terminal 分支。特别地，p=313+1128a 的每个素数参数均以 m=47、r=s=15+47a 直接终止；p=3697 是此前四路共同残余而由此分支关闭的控制点。另一方面，所有对角 r=s 命中恰等价于 m|(3p+1)/4，故完全位于 R=3 非 G 因子分支，不能承担 R=3 G 核心的全称出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - short-certificate-equivalence
  - type-I-gap23-adaptive-divisor-terminal-selector
topics:
  - type-I
  - terminal-first
  - adaptive-divisor
  - gap-family
  - gap-forty-seven
  - joint-residual
  - dirichlet-ray
  - proof-boundary
sources:
  - claim: short-certificate-equivalence
    role: Type-I-divisor-reconstruction
  - claim: type-I-gap23-adaptive-divisor-terminal-selector
    role: c-equals-one-instance-and-four-route-input
  - reproduction: reproductions/type_i_24c_minus_one_adaptive_divisor_terminal_family.py
    role: generic-selector-and-five-route-controls
visibility: public
last_checked: '2026-08-12'
---

# \(24c-1\) 缺口族的自适应 \(d=2r\) Type I 终端

## 1. 统一选择定理

设 \(p=24h+1\) 是核心素数，并取整数

\[
1\le c\le h,
\qquad
m=24c-1,
\qquad
s=h+c,
\qquad
x=\frac{p+m}{4}=6s.
\tag{1}
\]

于是 \(m\equiv3\pmod4\) 且 \(3\le m\le p-2\)，所以这是合法缺口。对任意
正因子 \(r\mid s\)，写 \(s=rt\)，并令

\[
d=2r.
\tag{2}
\]

**定理。** 上述 \(d\) 是 gap \(m\) 的 Type I 除子证书，当且仅当

\[
\boxed{rt^2\equiv\tau_m\pmod m,
\qquad
\tau_m=-72^{-1}\pmod m.}
\tag{3}
\]

命中时，精确分母为

\[
\boxed{
y=\frac{px+2r}{m},
\qquad
z=\frac{p\left(x+px^2/(2r)\right)}{m},
\qquad
\frac4p=\frac1x+\frac1y+\frac1z.}
\tag{4}
\]

**证明。** 因为 \(r\mid s\)，有

\[
d=2r\mid6s=x,
\qquad d\le2s=x/3,
\tag{5}
\]

故 \(d\mid x^2\)。由 \(p=24s-m\)，模 \(m\) 有 \(p\equiv24s\)，从而

\[
m\mid px+d
\Longleftrightarrow
144s^2+2r\equiv0\pmod m
\Longleftrightarrow
r\equiv-72s^2\pmod m.
\tag{6}
\]

又 \(m<p\) 且 \(p\) 为素数，故 \((p,m)=1\)。由于 \(p\equiv24s\pmod m\) 且
\((24,m)=1\)，得到 \((s,m)=1\)，于是也有 \((r,m)=1\)。代入 \(s=rt\) 并除以
\(r\)，式 (6) 等价于

\[
1\equiv-72rt^2\pmod m,
\tag{7}
\]

即 (3)。注意 \(m\equiv-1\pmod{24}\)，所以 \(72\) 在模 \(m\) 下可逆。标准 Type I
重建式给出 (4)。证毕。

定义完整的上除子盒

\[
\mathcal U_m(s)
=\left\{\frac{s^2}{r}\pmod m:r\mid s\right\}.
\tag{8}
\]

由于 \(s^2/r=rt^2\)，定理也可精确写成

\[
\boxed{\text{gap }m\text{ 的该自适应 terminal 存在}
\Longleftrightarrow \tau_m\in\mathcal U_m(s).}
\tag{9}
\]

对 \(c=1\) 有 \(m=23\)、\(\tau_{23}=15\)，这正是既有 gap-23 选择子；对
\(c=2\) 有

\[
m=47,
\qquad
\tau_{47}=-72^{-1}\equiv15\pmod {47}.
\tag{10}
\]

## 2. 对角线与 \(R=3\) G 边界

令

\[
N_3=\frac{3p+1}{4}=18h+1.
\tag{11}
\]

在定理中取对角因子 \(r=s\)，所以 \(d=2s=x/3\)。此时有更强的精确等价：

\[
\boxed{
\text{对角 gap }m\text{ terminal 存在}
\Longleftrightarrow m\mid N_3.}
\tag{12}
\]

事实上

\[
px+2s
=6ps+2s
=2s(3p+1)
=8sN_3.
\tag{13}
\]

由第 1 节中的 \((s,m)=1\) 以及 \((8,m)=1\)，Type I 整除条件
\(m\mid px+2s\) 当且仅当 \(m\mid N_3\)。这也与 (3) 一致：

\[
72s+1=3m+4N_3.
\tag{14}
\]

因此，对角子选择器可以完全由 \(N_3\) 的因子分解实施：每个满足

\[
m\mid N_3,
\qquad m\equiv23\pmod {24}
\tag{15}
\]

的因子直接给出 (4)。因为 \(N_3<p\)，此 \(m\) 自动是合法缺口。

这也是一条重要的边界。若 \(R=3\) 中心图表为 G，则 \(N_3\) 的所有素因子都为
\(1\pmod3\)。其每个因子也为 \(1\pmod3\)，而 (15) 要求
\(m\equiv23\equiv2\pmod3\)，矛盾。故

\[
\boxed{R=3\text{ G}\Longrightarrow
\text{不存在本族的对角 }r=s\text{ terminal}.}
\tag{16}
\]

所以本节对角射线虽然提供真实 direct terminal，却不能被误作 \(R=3\) G 的新出口。
要推进该 G 核心，必须使用 \(t=s/r>1\) 的非对角选择，或构造独立的严格递降。

## 3. gap 47 的新 terminal 射线

在 \(c=2\) 时固定 \(t=1\)，取

\[
r=s=15+47a,
\qquad
h=13+47a.
\tag{17}
\]

由 (10)，\(rt^2=s\equiv15\pmod {47}\)，故每个素数参数

\[
\boxed{p=313+1128a}
\tag{18}
\]

都有 \(m=47\) 的直接 Type I terminal，且

\[
x=90+282a,
\qquad d=30+94a.
\tag{19}
\]

因为

\[
\gcd(313,1128)=1,
\tag{20}
\]

Dirichlet 定理保证该进程含无穷多个素数参数。

当 \(a=3\) 时，

\[
p=3697,
\qquad h=154,
\qquad s=r=156,
\qquad x=936,
\qquad d=312,
\tag{21}
\]

并恢复为

\[
\boxed{
\frac4{3697}
=\frac1{936}+\frac1{73632}+\frac1{816652512}.}
\tag{22}
\]

这个 \(p=3697\) 在 R=11 固定尾、gap 7、gap 11 和自适应 gap 23 四路均未命中；
因此 (22) 是对此前四路共同残余的实际新增 terminal，而不只是一个独立射线。

## 4. 精确的五路残余

把 \(c=2\) 的选择子作为 gap-23 之后的第五路。令

\[
\mathcal U_{47}(h+2)
=\left\{\frac{(h+2)^2}{r}\pmod {47}:r\mid h+2\right\}.
\tag{23}
\]

五路均未命中的充要条件是：

\[
\begin{array}{ll}
\text{(i)}&N_{11}=22h+1\text{ 属于 R=11 固定尾的 QR11 或 }(2,6,1)\text{ 残余类};\\
\text{(ii)}&u=3h+1\text{ 的每个素因子均为模 }7\text{ 二次剩余};\\
\text{(iii)}&-1\notin\mathcal R_{11}(3(2h+1));\\
\text{(iv)}&15\notin\mathcal U_{23}(h+1);\\
\text{(v)}&15\notin\mathcal U_{47}(h+2).
\end{array}
\tag{24}
\]

这是五条既定有限因子判据的精确合取。它没有证明 (24) 为空，也没有构造递归边；
其作用是把新的 \(m=47\) 直接 terminal 以无歧义方式并入全局出口程序。

复现命令：`python3 reproductions/type_i_24c_minus_one_adaptive_divisor_terminal_family.py --verify`
