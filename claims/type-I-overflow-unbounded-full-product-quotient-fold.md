---
kind: claim
claim_id: type-I-overflow-unbounded-full-product-quotient-fold
title: overflow 固定-n 完整乘积商折叠的无界 support 严格递降
statement: >-
  设真实 persistent overflow 满足 pn=4Md+1、M=Ab、1<=d<p、
  1<=A<=B_p=(p-1)^2/4，并且 bd>=2。取完整乘积 L=Md，便有 q=Md/L=1；
  因而固定-n 商折叠的 target 是 (M_T,d_T,n_T;A_T)=(Md,1,n;Md)。该 target
  满足 R_T=(p-1)n-1、K_T=Md(p-1)、A_T|K_T，并且精确秩
  Lambda_p^sharp=(floor(B_p/A),K/A) 的第一坐标严格下降，即使 A_T>B_p。
  对带原样 scope、独立 typed normal-form/F-G-hit 重算和内容寻址的 charged-chart
  adapter，恒等 Sol(4,p) lift 因而给出条件性完整 E1--E5 的 O 边；target hit
  应 terminal-first 退出。故在这一 adapter 准入层，所有低 support 且 Md>A 的
  persistent overflow 均有严格出口，包含 M=A,d>1 的 H-rough 支撑饱和分支。
  该选择器严格失败当且仅当 M=A,d=1；一般 typed adapter 尚未接入统一 selector，
  所以本卡不把旧 analysis evidence 批量升格为 verified_edge。
claim_status: conditional
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-fixed-n-quotient-fold-descent
  - type-I-overflow-total-cofactor-canonical-projection-persistence-rank
  - type-I-overflow-total-cofactor-typed-projection-dispatch
  - denominator-escape-state-contract
topics:
  - type-I
  - overflow
  - fixed-n
  - quotient-fold
  - full-product
  - charged-support
  - unbounded-support
  - well-founded-descent
  - typed-dispatch
  - proof-boundary
sources:
  - claim: type-I-overflow-fixed-n-quotient-fold-descent
    role: quotient-fold-arithmetic-and-identity-lift
  - claim: type-I-overflow-total-cofactor-canonical-projection-persistence-rank
    role: exact-unbounded-charged-capacity-rank
  - claim: type-I-overflow-total-cofactor-typed-projection-dispatch
    role: terminal-first-typed-adapter-admission-boundary
  - reproduction: reproductions/type_i_overflow_unbounded_full_product_quotient_fold.py
    role: focused-algebraic-rank-and-stutter-receipts
visibility: public
last_checked: '2026-08-12'
---

# overflow 固定-\(n\) 完整乘积商折叠的无界 support 严格递降

## 定理与适用域

固定核心素数

\[
p\equiv1\pmod {24},
\qquad
B_p=\frac{(p-1)^2}{4}.
\tag{1}
\]

设

\[
X=(p,R,K;A,\sigma)
\tag{2}
\]

是一个真实入队、内容寻址、带原样 scope \(\sigma\) 的 persistent overflow state。其
绑定的 determinant receipt 重算出

\[
pn=4Md+1,
\qquad
M=Ab,
\qquad
1\le d<p,
\qquad
1\le A\le B_p.
\tag{3}
\]

这里的 source chart 为

\[
R=4M-n>p,
\qquad
K=M(p-d).
\tag{4}
\]

令

\[
S:=Md=Abd=\frac{pn-1}{4}.
\tag{5}
\]

本卡处理的精确条件是

\[
\boxed{S>A\quad\Longleftrightarrow\quad bd\ge2.}
\tag{6}
\]

在此条件下，不寻找小除子，而直接选完整乘积

\[
L=S.
\tag{7}
\]

这是固定-\(n\) 商折叠的一个特殊但全称的选择：其商为

\[
q=\frac{S}{L}=1= p\cdot0+1.
\tag{8}
\]

因此定义 target determinant 数据

\[
\boxed{
(M_T,d_T,n_T;A_T)=(S,1,n;S).
}
\tag{9}
\]

与旧的 bounded-divisor contract 不同，(9) **不要求** \(S\le B_p\)。目标 charged
support 可以越过 \(B_p\)；状态合同要求的是 \(A_T\mid K_T\)，而不是
\(A_T\le B_p\)。

## 算术 target 与合法 charged support

由 (3)、(5)、(9)，

\[
pn_T=pn=4S+1=4M_Td_T+1.
\tag{10}
\]

其 canonical chart 是

\[
\begin{aligned}
R_T&=4S-n=(p-1)n-1,\\
K_T&=S(p-1).
\end{aligned}
\tag{11}
\]

因为 \(p>1\)、\(n>0\)，有 \(0<R_T<4S\)；又 \(n\equiv1\pmod4\)，故
\(R_T\equiv3\pmod4\)。直接计算还给出

\[
pR_T+1
=p(4S-n)+1
=4S(p-1)
=4K_T.
\tag{12}
\]

特别地，

\[
A\mid S=A_T,
\qquad
A_T=S\mid K_T.
\tag{13}
\]

所以该转换既不丢失旧 charged support，也不需要 forgetful reset。它只是把记账载体
从 \(A\) 单调升级到 \(S\)。

## 无界精确秩的严格付款

采用已经建立的全域 charged-capacity 秩

\[
\Lambda_p^\sharp(p,R,K;D)
=\left(
\left\lfloor\frac{B_p}{D}\right\rfloor,
\frac KD
\right).
\tag{14}
\]

写 \(u=S/A=bd\)。由 (6)，\(u\ge2\)。又 \(A\le B_p\)，令

\[
H=\left\lfloor\frac{B_p}{A}\right\rfloor\ge1.
\tag{15}
\]

如果 \(\lfloor B_p/S\rfloor\ge H\)，则

\[
\frac{B_p}{A}\ge uH\ge2H\ge H+1,
\tag{16}
\]

这与 \(B_p/A<H+1\) 矛盾。因此

\[
\boxed{
\left\lfloor\frac{B_p}{S}\right\rfloor
<
\left\lfloor\frac{B_p}{A}\right\rfloor.
}
\tag{17}
\]

源、目标的完整秩分别为

\[
\Lambda_p^\sharp(X)
=\left(
\left\lfloor\frac{B_p}{A}\right\rfloor,
b(p-d)
\right),
\qquad
\Lambda_p^\sharp(T)
=\left(
\left\lfloor\frac{B_p}{S}\right\rfloor,
p-1
\right).
\tag{18}
\]

式 (17) 已经在第一坐标严格支付 E5，故不需要比较第二坐标。后者确实可能上升；例如

\[
(p,A,M,d,n)=(73,97,97,19,101)
\tag{19}
\]

给出

\[
(13,54)\longmapsto(0,72).
\tag{20}
\]

这正是使用字典序 \(\Lambda_p^\sharp\) 而非单独 residual capacity 的必要性，也说明
目标越过 \(B_p\) 并不破坏良基性。

## E1--E5 准入与当前实现边界

在 (2)--(6) 的真实 persistent-source 前提下，这条候选属于 `O` 型 paid
outer-rank 边。完整 adapter 应逐项验证：

| 合同 | 支付内容 |
|---|---|
| E1 | 已入队的 source state ID、绑定的 determinant receipt 与原样 scope \(\sigma\) |
| E2 | (10)--(13)，特别是 \(A_T\mid K_T\) |
| E3 | 对 target 重新计算 canonical chart、完整分解、F/G/hit、normal form 与内容地址 |
| E4 | \(\operatorname{Sol}(4,p)\to\operatorname{Sol}(4,p)\) 的恒等映射 |
| E5 | (17) 的严格第一秩坐标下降 |

target 的 F/G/hit 字段绝不能从 source 继承。若 target 是 `hit`，应直接返回其 Type I
终端；若为 F 或 G，才以 (9) 的 charged state 继续入队。

本仓库已有独立 target typed-dispatch 的完备重算合同，但尚未把一般 charged-chart
normal-form verifier、F/G 角色和 state/receipt hash 序列化为统一 selector adapter。
因此这里的结论是：**一旦该 adapter 逐项通过上表，这是一条完整 E1--E5 边**；当前
不能仅凭 (10)--(18) 将旧的 transient receipt 或 `analysis_evidence` 批量提升为
`verified_edge`。这也是本卡标为 `conditional` 的唯一原因，不是算术或 E5 的缺口。

## 精确残余

完整乘积选择没有严格付款当且仅当 \(S=A\)。由于

\[
\frac SA=bd
\tag{21}
\]

是正整数，故

\[
\boxed{
S=A
\quad\Longleftrightarrow\quad
b=d=1
\quad\Longleftrightarrow\quad
M=A,\ d=1.
}
\tag{22}
\]

因此，原先有界 fixed-\(n\) 菜单的所有支撑饱和 \(M=A,d>1\) 粗糙分支，都已由
(9) 在无界 support 合同下消去；它们不再是这个扩大分支的算术残余。真正未被此
selector 处理的是 \(M=A,d=1\) 的 d=1 G 重图表分支，以及源端已经
\(A>B_p\) 时第一坐标为零的独立高支撑问题。

例如

\[
(p,M,d,n;A)=(73,91,1,5;91)
\tag{23}
\]

满足 \(73\cdot5=4\cdot91+1\)、\(R=359>73\)、\(A\le B_{73}=1296\)，但
\(S=A=91\)。完整乘积目标与 source 完全相同，秩固定为 \((14,72)\)，所以不能被
误登记为严格边。该行只展示本选择器的 sharp 边界；它不声称该状态可达，也不排除
其它 Type I/II 终端或高支撑出口。

## 聚焦复现

```bash
python3 reproductions/type_i_overflow_unbounded_full_product_quotient_fold.py --verify
```

回执核验两条普通支撑升级、两个既有 \(H\)-rough 载体和四条支撑饱和 F/G 算术控制的
(10)--(18)，并以 (23) 核验唯一的完整乘积 stutter。它不做范围扫描，也不替代 E3 的
一般 typed verifier。
