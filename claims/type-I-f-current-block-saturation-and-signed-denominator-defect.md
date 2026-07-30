---
kind: claim
claim_id: type-I-f-current-block-saturation-and-signed-denominator-defect
title: 线性 F 状态的当前块饱和与带符号分母缺陷
statement: 对任意线性状态 p=a+s+asR，令 U=aR+1、V=sR+1、4K=pR+1，则恒有 UV=4K，因而每个素数 q 上的两个块高度之和为 v_q(K)+2*1_{q=2}。对目标纤维见证 z，令 A/B=prod_q q^{z_q} 为互素分解，X_-=B/(B,K)、X_+=A/(A,K)，则两个定向首分母缺陷分别为 d_q^-=(-z_q-v_q(K))_+、d_q^+=(z_q-v_q(K))_+，且无向盒外缺陷恰为 e_q=d_q^-+d_q^+。特别地，奇素数处当前两个块已用尽 K 的全部 q 进高度；再从 e_q 中扣除任一当前块高度，精确等价于把 K 人为扩大相同的 q 进层数，而不是从原状态取得容量。q=2 时 4K 的额外两层只属于形式缺口的定向约分边界，不能混同于 K 的首分母容量。该恒等式不提供跨状态容量注入、合法提升或统一选择器。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-f-overflow-rational-gap-denominator
  - type-I-f-overflow-lower-modulus-omega-carrier-boundary
topics:
  - type-I
  - F-state
  - linear-state
  - target-fiber
  - rational-denominator
  - signed-defect
  - q-adic
  - carrier-saturation
  - capacity-boundary
  - proof-program
sources:
  - claim: type-I-f-overflow-rational-gap-denominator
    role: oriented-first-denominator-and-formal-gap-interface
  - claim: type-I-f-overflow-lower-modulus-omega-carrier-boundary
    role: bidirectional-denominator-defect-interface
visibility: public
last_checked: '2026-07-30'
---

# 线性 F 状态的当前块饱和与带符号分母缺陷

## 定理

设 \(R\) 为奇数，且一个线性状态满足

\[
p=a+s+asR,
\qquad
4K=pR+1.
\tag{1}
\]

定义两个线性块

\[
U=aR+1,
\qquad
V=sR+1.
\tag{2}
\]

对任意素数 \(q\)，记

\[
u_q=v_q(U),
\qquad
v_q^{\mathrm{blk}}=v_q(V),
\qquad
\nu_q=v_q(K).
\tag{3}
\]

则恒有

\[
\boxed{UV=4K}
\tag{4}
\]

以及

\[
\boxed{
u_q+v_q^{\mathrm{blk}}
=\nu_q+2\mathbf 1_{q=2}.
}
\tag{5}
\]

再取一个目标纤维见证 \(z=(z_q)_{q\in\mathcal Q}\)，其中

\[
\prod_{q\in\mathcal Q}q^{z_q}\equiv-1\pmod R,
\qquad
\gcd\!\left(R,\prod_{q\in\mathcal Q}q\right)=1.
\tag{6}
\]

写成互素正整数之比

\[
A=A(z)=\prod_q q^{(z_q)_+},
\qquad
B=B(z)=\prod_q q^{(-z_q)_+},
\qquad
\frac AB=\prod_q q^{z_q}.
\tag{7}
\]

定义两个相反全局方向的形式 Type I 首分母约分缺陷

\[
X_-(z)=\frac{B}{(B,K)},
\qquad
X_+(z)=\frac{A}{(A,K)}=X_-(-z),
\tag{8}
\]

并记

\[
d_q^-(z)=v_q(X_-(z)),
\qquad
d_q^+(z)=v_q(X_+(z)).
\tag{9}
\]

则逐坐标精确地有

\[
\boxed{
d_q^-(z)=(-z_q-\nu_q)_+,
\qquad
d_q^+(z)=(z_q-\nu_q)_+.
}
\tag{10}
\]

因此无向盒外缺陷

\[
e_q(z)=(|z_q|-\nu_q)_+
\tag{11}
\]

满足

\[
\boxed{e_q(z)=d_q^-(z)+d_q^+(z).}
\tag{12}
\]

式 (12) 是两个**相反全局方向**的分母缺陷之和，不是两份可独立分配给当前
\(U,V\) 两块的需求。

## 证明

直接展开 (2)：

\[
UV
=(aR+1)(sR+1)
=asR^2+(a+s)R+1
=(a+s+asR)R+1
=pR+1
=4K,
\]

得到 (4)。对 (4) 取 \(q\)-进赋值，便有

\[
u_q+v_q^{\mathrm{blk}}
=v_q(4K)
=\nu_q+2\mathbf 1_{q=2},
\]

即 (5)。这一步对每个满足 (1) 的线性状态成立，不依赖有限扫描或某个规范源的选择。

由 (7)，

\[
v_q(A)=(z_q)_+,
\qquad
v_q(B)=(-z_q)_+.
\]

所以

\[
v_q\!\left(\frac{B}{(B,K)}\right)
=(-z_q)_+-\min\{(-z_q)_+,\nu_q\}
=(-z_q-\nu_q)_+,
\]

而对 \(A\) 同理得到 \(d_q^+(z)=(z_q-\nu_q)_+\)。若 \(z_q\ge0\)，则
\(d_q^-=0\)，且 \(d_q^+=(|z_q|-\nu_q)_+\)；若 \(z_q\le0\)，两个方向交换。
这证明 (10)--(12)。

## 奇素数处的当前块饱和

对每个奇素数 \(q\)，式 (5) 化为

\[
\boxed{u_q+v_q^{\mathrm{blk}}=\nu_q.}
\tag{13}
\]

因此 \(K\) 在 \(q\) 处能够用于约分的全部 \(\nu_q\) 层，已经精确分布在当前的
\(U,V\) 两块中。式 (10) 所记录的恰是把这 \(\nu_q\) 层全部约掉以后仍留在
\(X_-\) 或 \(X_+\) 中的层数。

更精确地，令有限支撑族 \((h_q)_q\) 满足 \(h_q\in\mathbb Z_{\ge0}\)，其中每个
\(h_q\) 是拟再次抵扣的“当前块高度”；它可以取 \(u_q\)、\(v_q^{\mathrm{blk}}\)，
或由二者构成的其它非负数值。则

\[
\begin{aligned}
(e_q(z)-h_q)_+
&=(|z_q|-\nu_q-h_q)_+,\\
(d_q^-(z)-h_q)_+
&=(-z_q-\nu_q-h_q)_+,\\
(d_q^+(z)-h_q)_+
&=(z_q-\nu_q-h_q)_+.
\end{aligned}
\tag{14}
\]

若形式地置

\[
\widetilde K=K\prod_q q^{h_q},
\tag{15}
\]

那么 (14) 正是把原式中的 \(K\) 换成 \(\widetilde K\) 后得到的分母缺陷。换言之，

\[
\boxed{
\text{从 }e_q\text{ 或 }d_q^\pm\text{ 中再次扣除当前块高度}
\underset{\text{缺陷指数公式}}{\Longleftrightarrow}
\text{把 }K\text{ 人为扩大同样的 }q\text{-进层数}.
}
\tag{16}
\]

但 \(\widetilde K\) 一般不再满足 \(4\widetilde K=pR+1\)，而且 \(h_q\) 本来就来自
\(4K=UV\) 中已经计入 \(\nu_q\) 的因子。因此 (16) 不是原状态中的容量注入，而是对
原指数盒的一次反事实扩张。当前块仍可能通过一个另行证明的跨状态同余、差值整除或
\(q\)-进提升参与后续构造；式 (13)--(16) 只排除“无映射地把同一批层数再扣一次”。

## \(q=2\) 的两层方向边界

在 \(q=2\) 处，(5) 给出

\[
u_2+v_2^{\mathrm{blk}}=\nu_2+2.
\tag{17}
\]

这里多出的两层来自等式 \(UV=4K\) 的系数 \(4\)，而不是来自 \(K\)。这必须与两类
有理式的约分分母分开记录。首分母缺陷 (8) 仍以 \(K\) 为约分因子，故

\[
d_2^-(z)=(-z_2-\nu_2)_+,
\qquad
d_2^+(z)=(z_2-\nu_2)_+.
\tag{18}
\]

另一方面，若只考察形式缺口

\[
\frac{4K(A/B)+1}{R},
\]

则方向 \(z\) 与反方向 \(-z\) 的约分分母分别为

\[
Y_-(z)=\frac{B}{(B,4K)},
\qquad
Y_+(z)=\frac{A}{(A,4K)}=Y_-(-z),
\tag{19}
\]

从而

\[
v_2(Y_-(z))=(-z_2-\nu_2-2)_+,
\qquad
v_2(Y_+(z))=(z_2-\nu_2-2)_+.
\tag{20}
\]

式 (20) 中的两层只说明系数 \(4\) 可以在**所选方向的形式缺口**中参与约分；它们
不会进入式 (18) 的 \(K\)-首分母，也不能同时记成 \(X_-\)、\(X_+\) 或当前两块的
额外可复用容量。若要接入广义 \(2^j\) 终端，必须明确当前处理的是 (18) 还是 (20)，
并证明相应整数化与解提升，不能把阈值 \(\nu_2\) 和 \(\nu_2+2\) 混用。

## 定向单块缺陷必须从 \(z\) 或 \(-z\) 重算

给定目标见证 \(z\)，正向形式首分母的完整缺陷向量是

\[
D^-(z)=(d_q^-(z))_q,
\]

而反向形式首分母的完整缺陷向量是

\[
D^+(z)=(d_q^+(z))_q=D^-(-z).
\]

二者由一次**全局**取反互换。不同坐标不能各自选择 \(z_q\) 或 \(-z_q\) 后再拼成一个
新的定向见证；这种逐坐标换向一般不保持目标纤维同余。类似地，把某个 Fourier 颜色
或线性块指定给一个方向，本身并不证明该块对应 \(D^-\) 还是 \(D^+\)。每次选择方向、
改变见证或迁移状态后，都必须从所得的 \(z\) 或 \(-z\) 重新构造 \(A,B,X_\pm\)，再
计算定向缺陷。无向量 \(e=D^-+D^+\) 只能作为双向总缺陷或选择价格，不能先拆给
\(U,V\) 再按块高度抵扣。

## 逻辑边界

本卡无条件证明的是：

1. 每个线性状态的两个当前块在奇素数处恰好耗尽 \(K\) 的全部赋值预算；
2. \(D^-\)、\(D^+\) 是两个相反方向首分母的精确约分缺陷，且其和等于无向盒外缺陷；
3. “缺陷减当前块高度”在代数上等价于人为扩大 \(K\)，不是原状态内已经存在的支付；
4. \(q=2\) 处必须区分 \(K\)-首分母阈值与 \(4K\)-形式缺口阈值。

它**不能**推出以下任何结论：

- 未支付分母层必然注入某个标签差、模数差、另一状态或某个共同载体；
- \(D^-\) 或 \(D^+\) 自动产生合法 Type I/II 证书；
- 存在保持解可提升的状态迁移或严格下降势函数；
- 每个核心素数已经存在统一的表示—对偶—容量选择器。

要跨过这条边界，仍需给出一个新的算术映射：它必须把某个定向分母缺陷送入**当前
状态之外的新资源或合法新状态**，同时证明资源可比较、解可提升，并在递降分支中证明
一个良基势函数严格下降。仅有式 (4)--(20) 的数值恒等式不足以完成该步骤。
