---
kind: claim
claim_id: type-I-overflow-d-two-capacity-window-complete-reduction
title: 高载体 d=2 容量窗的完整余因子递降
statement: 设核心素数 p=1 (mod 24) 的已有来源回执 overflow 满足 pn=8M+1、M>B_p=(p-1)^2/4、2p-1<=n<=4p-11，并携带 A|M、1<=A<=B_p 及图表无关标记集 Sol(p)。令 c=(p-1)/4、b=M/A。则必有一条严格可提升递降：A<c 时 L=c 给出 fixed-s 边；A>=c、b 合数时 L=M/spf(b) 给出保留 A 的 fixed-n 边；A>=c、b 为奇素数且 b<p 时 (M,d=2;A) 重图表为 (2A,b;A)，而 b=2 时重图表为 (A,4;A)，二者均由不可逆 d=2 预转移位 1->0 严格下降；A>=c、b 为素数且 b>p 时 L=b 给出支付 support reset 的 fixed-n 边。b=p 不可能。故该 d=2 容量窗在既有 source/solution-lift 合同下不留未分流的 overflow。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-high-carrier-height-staircase
  - type-I-overflow-fixed-n-bounded-divisor-saturation
  - type-I-overflow-fixed-s-bounded-divisor-saturation
topics:
  - type-I
  - overflow
  - high-carrier
  - d-two
  - capacity-window
  - cofactor-primality
  - denominator-transfer
  - support-reset
  - well-founded-descent
  - selector
sources:
  - claim: type-I-overflow-high-carrier-height-staircase
    role: d-two-entry-height-and-high-carrier-context
  - claim: type-I-overflow-fixed-n-bounded-divisor-saturation
    role: complete-fixed-n-edge-contract
  - claim: type-I-overflow-fixed-s-bounded-divisor-saturation
    role: complete-fixed-s-edge-contract
  - reproduction: reproductions/type_i_overflow_d_two_capacity_window_complete_reduction.py
    role: focused-five-route-receipt
visibility: public
last_checked: '2026-08-08'
---

# 高载体 \(d=2\) 容量窗的完整余因子递降

## 定理

设 \(p\equiv1\pmod {24}\) 为素数，且一个已有 source/path/node 回执的
overflow 满足

\[
pn=8M+1,
\qquad M>B_p:=\frac{(p-1)^2}{4},
\qquad 2p-1\le n\le4p-11.
\tag{1}
\]

令 \(A\mid M\) 为当前 absorbed support，\(1\le A\le B_p\)，并假设该
overflow 使用图表无关的标记集 \(W=\operatorname{Sol}(p)\)。写

\[
c=\frac{p-1}{4},
\qquad b=\frac MA.
\tag{2}
\]

则此状态必有一条带恒等解提升的严格递降，按下列互斥分流构造：

\[
\begin{array}{c|c|c}
\text{条件}&\text{后继构造}&\text{严格付款}\\ \hline
A<c&L=c\mid rd&\text{既有 fixed-}s\\
A\ge c,\ b\text{ 合数}&L=M/\operatorname{spf}(b)&\text{fixed-}n\text{，保留 }A\\
A\ge c,\ 2<b<p\text{ 为素数}&(M,2)\mapsto(2A,b)&d=2\text{ 预转移位 }1\to0\\
A\ge c,\ b=2&(M,2)\mapsto(A,4)&d=2\text{ 预转移位 }1\to0\\
A\ge c,\ b>p\text{ 为素数}&L=b&\text{fixed-}n\text{，支付 support reset}
\end{array}
\tag{3}
\]

这里第二和第三个素数行共同覆盖 \(1<b<p\)。特别地，该 \(d=2\) 容量窗在既有
source/solution-lift 合同下不再留下需要 alternate 或 capacity 才能处理的 overflow
子族。这不是对猜想的全称证明：\(d=1\) 的更高带、\(d\ge3\) 以及 \(d=2\) 的
\(n\ge4p-3\) 均不在本定理范围内。

## 公共预备结论

因为 \(p\equiv1\pmod8\)，(1) 给出

\[
n\equiv1\pmod8,
\qquad M\equiv h:=\frac{p-1}{8}\pmod p.
\tag{4}
\]

所以 dual 图表满足

\[
r=h,
\qquad s=\frac{4rd+1}{p}=1,
\qquad rd=2h=c.
\tag{5}
\]

此外，(1) 的上界给出

\[
8M=pn-1\le4p^2-11p-1<4(p-1)^2,
\qquad M<2B_p.
\tag{6}
\]

故 \(M>B_p\ge A\) 蕴含 \(b>1\)；而当 \(A\ge c\) 时，

\[
b\le\frac Mc<\frac{2B_p}{c}=2(p-1).
\tag{7}
\]

又 \(p\nmid M\)，否则 (1) 模 \(p\) 给出 \(0\equiv1\pmod p\)。所以当 \(b\)
是素数时，\(b\ne p\)，恰有 \(b<p\) 或 \(b>p\) 两种可能。

## 三类已有边

若 \(A<c\)，取 \(L=c\)。式 (5) 给出 \(L\mid rd\)、\(4L>s\)，且

\[
\left\lfloor\frac{B_p}{L}\right\rfloor=4c
<\left\lfloor\frac{B_p}{A}\right\rfloor.
\]

既有 fixed-\(s\) 合同给出完整 E1--E5。

现在设 \(A\ge c\)。若 \(b\) 合数，令 \(q=\operatorname{spf}(b)\)。由 (7) 和
\(p\ge73\)，

\[
q\le\sqrt b<\sqrt{2(p-1)}<\frac p2.
\tag{8}
\]

于是

\[
L=\frac Mq=A\frac bq,
\qquad A\mid L,
\qquad 2A\le L\le\frac M2<B_p.
\tag{9}
\]

又

\[
4L=\frac{pn-1}{2q}>n,
\]

因为 \(q<p/2\) 且 \(n\ge2p-1>1\)。所以

\[
\left\lfloor\frac{B_p}{L}\right\rfloor
\le\left\lfloor\frac{B_p}{2A}\right\rfloor
<\left\lfloor\frac{B_p}{A}\right\rfloor,
\]

既有 fixed-\(n\) 合同给出保留 \(A\) 的完整 E1--E5。

若 \(b>p\) 为素数，令 \(L=b\)。由 (1) 与 \(b>p\)，

\[
8A=\frac{pn-1}{b}<n,
\qquad A<\frac n8\le\frac{4p-11}{8}<p<b.
\tag{10}
\]

再由 (7) 和 \(p\ge73\)，\(b<2(p-1)<B_p\)，而 \(n<4p<4b\)。于是
\(L=b\mid M\)、\(A<L\le B_p\)、\(4L>n\)，且同一个 floor 势严格下降。
这里 \(A\nmid L\)，所以 fixed-\(n\) 合同明确把它登记为支付 support reset 的完整
E1--E5 边，而不伪称旧支撑被保留。

## 小素余因子的分母转移

剩下 \(b<p\) 的素余因子。先设 \(2<b<p\)。定义确定的后继 determinant 坐标

\[
M_T=2A,
\qquad d_T=b,
\qquad R_T=8A-n,
\qquad K_T=2A(p-b).
\tag{11}
\]

因为

\[
8A=\frac{pn-1}{b}>n
\]

（等价于 \(n(p-b)>1\)），有 \(0<R_T<8A\)，且

\[
pn=4M_Td_T+1,
\qquad pR_T+1=4K_T,
\qquad A\mid K_T,
\qquad 1<d_T<p.
\tag{12}
\]

它严格降低 canonical \(R\)：

\[
(4M-n)-R_T=4A(b-2)>0.
\tag{13}
\]

当 \(b=2\) 时，上式不能产生严格变化，因而必须改取

\[
M_T=A,
\qquad d_T=4,
\qquad R_T=4A-n,
\qquad K_T=A(p-4).
\tag{14}
\]

此时 \(pn=16A+1=4M_Td_T+1\)，且 \(4A>n\) 等价于
\(n(p-4)>1\)。所以 (14) 也是合法 canonical chart，并有

\[
(4M-n)-R_T=4A>0.
\tag{15}
\]

为避免把“较小 \(R\)”单独误当作全局势，定义由状态整数坐标重算的预转移位

\[
\epsilon_2(M,d;A)=
\begin{cases}
1,&d=2,\ M/A\text{ 为素数且 }1<M/A<p,\\
0,&\text{其余情形}.
\end{cases}
\tag{16}
\]

并在本分流与既有 fixed-\(n\)/fixed-\(s\) 外层秩边的并集中使用

\[
\Lambda_p(M,d;A)=
\left(
\left\lfloor\frac{B_p}{A}\right\rfloor,
\epsilon_2(M,d;A)
\right)
\tag{17}
\]

的字典序。普通 fixed-\(n\)/fixed-\(s\) 边已经严格降低第一坐标；(11) 与 (14)
保持 \(A\)，并把 \(\epsilon_2\) 从 \(1\) 变为 \(0\)。反向重写不在这个有向
dispatcher 的规则中，且任何未来把 determinant 坐标改回 \(d=2\) 的提案必须另行
通过 E1--E5。因此两种转移都对预先声明的边集合严格降低良基势。

E1 继承原 overflow 的 source/path/node 回执；E2--E3 是 (11)--(15) 的整数恒等式；
E4 取 \(W_T=W_S=\operatorname{Sol}(p)\) 与恒等映射；E5 是 (17)。故它们分别是
`d_two_odd_prime_cofactor_transfer_v1` 与
`d_two_prime_two_cofactor_transfer_v1` verified edge，而不是只降低局部载体的
RESET 候选。这完成 (3) 的全部分支。

## 聚焦复现

```bash
python3 reproductions/type_i_overflow_d_two_capacity_window_complete_reduction.py --verify
```

五条精确回执分别覆盖 fixed-\(s\)、合数 \(b\)、奇素数 \(b<p\) 的分母转移、
\(b=2\) 的专门转移，以及素数 \(b>p\) 的 support reset；不做历史范围扫描。
