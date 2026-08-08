---
kind: claim
claim_id: type-I-overflow-high-carrier-height-staircase
title: 高载体 overflow 的分母高度阶梯与首带 d=1 收缩
statement: 设核心素数 p=1 (mod 24) 的 verified overflow 满足 pn=4Md+1、1<=d<p、M>B_p=(p-1)^2/4，并令 A|M、1<=A<=B_p 为当前 absorbed support。对每个 1<=j<=p-2，d>=j 必强制 n>=nu_j(p):=j(p-2)+1+(j mod 4)；特别地 n<2p-1 时必有 d=1。于是整个首高载体带 p<=n<=2p-5 收缩为 r=(p-1)/4、s=1、rd=(p-1)/4 的已知 p-2 G 图表：若 A<(p-1)/4，则 L=(p-1)/4 给出既有 fixed-s 完整 E1--E5 外层秩递降；若 A>=(p-1)/4，则该 fixed-s 除子图谱严格为空。后一个分支仍不是终端或全局递归边。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-high-carrier-p-plus-four-complement
  - type-I-overflow-d-one-p-minus-two-g-rechart
  - type-I-overflow-fixed-s-bounded-divisor-saturation
topics:
  - type-I
  - overflow
  - high-carrier
  - denominator-height
  - d-one
  - G-state
  - fixed-s
  - well-founded-descent
  - proof-boundary
sources:
  - claim: type-I-overflow-high-carrier-p-plus-four-complement
    role: high-carrier-domain-and-n-congruence
  - claim: type-I-overflow-d-one-p-minus-two-g-rechart
    role: d-one-G-normal-form-and-fixed-s-boundary
  - claim: type-I-overflow-fixed-s-bounded-divisor-saturation
    role: complete-E1-E5-fixed-s-contract
  - reproduction: reproductions/type_i_overflow_high_carrier_height_staircase.py
    role: focused-boundary-receipt
visibility: public
last_checked: '2026-08-08'
---

# 高载体 overflow 的分母高度阶梯与首带 \(d=1\) 收缩

## 定理

设 \(p\equiv1\pmod {24}\) 为素数，且一个已验证的 overflow 满足

\[
pn=4Md+1,
\qquad 1\le d<p,
\qquad M>B_p:=\frac{(p-1)^2}{4}.
\tag{1}
\]

令 \([j]_4\in\{0,1,2,3\}\) 表示 \(j\) 模 \(4\) 的最小非负剩余，并对
\(1\le j\le p-2\) 定义

\[
\nu_j(p):=j(p-2)+1+[j]_4.
\tag{2}
\]

则有离散高度阶梯

\[
\boxed{d\ge j\quad\Longrightarrow\quad n\ge\nu_j(p).}
\tag{3}
\]

前四层为

\[
\nu_1=p,
\qquad
\nu_2=2p-1,
\qquad
\nu_3=3p-2,
\qquad
\nu_4=4p-7.
\tag{4}
\]

特别地，若 \(n<2p-1\)，则由 \(n\equiv1\pmod4\) 有

\[
p\le n\le2p-5,
\qquad d=1.
\tag{5}
\]

再令 \(A\mid M\) 是当前 absorbed support，\(1\le A\le B_p\)，并记
\(c=(p-1)/4\)。在 (5) 的首带中：

\[
\boxed{
A<c\Longrightarrow L=c\text{ 给出既有 fixed-s 完整 E1--E5 递降};
\qquad
A\ge c\Longrightarrow\text{fixed-s 有界除子图谱为空}.
}
\tag{6}
\]

第二个分支仅排除这一张 fixed-\(s\) 菜单；它不声称 Type I/II 终端、跨状态容量
证书或完整递归边。

## 证明

由 (1) 和 \(M>B_p\)，若 \(d\ge j\)，则

\[
pn-1=4Md>4jB_p=j(p-1)^2.
\]

所以

\[
n>j(p-2)+\frac{j+1}{p}.
\tag{7}
\]

另一方面，\(p\equiv1\pmod4\) 与 (1) 给出 \(n\equiv1\pmod4\)。当
\(1\le j\le p-2\) 时，\((j+1)/p<1\)，而

\[
j(p-2)\equiv-j\pmod4.
\]

因此严格大于 (7) 的最小 \(1\pmod4\) 整数，正是

\[
j(p-2)+\bigl(1+[j]_4\bigr)=\nu_j(p).
\]

这证明 (3)。取 \(j=1,2,3,4\) 得 (4)。高载体已经强制
\(n\ge p\)，而若 \(n<2p-1\)，允许的最大 \(1\pmod4\) 值是 \(2p-5\)；(3) 在 \(j=2\)
时排除 \(d\ge2\)，所以得到 (5)。

现在在首带写 \(n=4k+1\)。由 \(d=1\) 得

\[
M=pk+c,
\qquad r=M\bmod p=c,
\qquad s=\frac{4r+1}{p}=1,
\qquad rd=c.
\tag{8}
\]

现有的 \(d=1\) 重图表定理将该行送到

\[
(R_r,K_r)=(p-2,B_p),
\tag{9}
\]

这是 G 态，而非自动的 support-preserving 后继。对 fixed-\(s\) 图谱，若 \(A<c\)，
取 \(L=c\)。由 (8)，\(L\mid rd\)、\(4L>s\)，且

\[
\left\lfloor\frac{B_p}{L}\right\rfloor=4c
<\left\lfloor\frac{B_p}{A}\right\rfloor.
\]

故已建立的 fixed-\(s\) 合同给出完整 E1--E5。反之，若 \(A\ge c\)，每个
\(L\mid rd=c\) 都满足 \(L\le c\le A\)，不可能满足该合同所需的 \(A<L\)。这证明
(6)。证毕。

## 对选择器的作用

这个引理不是新的通用终端。它的作用是把高载体的第一个无限高度带从一般
\((d,r,s)\) 搜索压成一个确定的分流：

1. \(A<c\) 时直接进入已有的 fixed-\(s\) 严格外层秩递降；
2. \(A\ge c\) 时不再枚举 fixed-\(s\) 除子，转交 G 态的非支撑 Type I/II、marked
   lift 或跨状态容量接口；
3. \(d\ge2\) 只可能从 \(n\ge2p-1\) 开始，因而不会污染首带的 d=1 专门分析。

这保留了现有逻辑边界：G 图表的支撑内目标纤维为空，且 (6) 的空图谱不能被解释为
Erdos--Straus 猜想的反例。

## 聚焦复现

脚本只复核阶梯的边界行与 (6) 的两种路由，不做历史范围扫描：

```bash
python3 reproductions/type_i_overflow_high_carrier_height_staircase.py --verify
```

其中 \(p=73\) 的 \(d=2,n=145=2p-1\) 和 \(d=3,n=217=3p-2\) 展示前两个
非 \(d=1\) 阈值可以达到；\(d=4\) 例子同时保留分母同余会把实际首项推到通用
模 \(4\) 下界之上的事实。
