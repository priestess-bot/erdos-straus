---
kind: claim
claim_id: type-I-overflow-smooth23-high-k-dual-carrier-no-go
title: 2,3-光滑 overflow 高 k 双载体 joined-support RESET 无 go
statement: '在 P=2^a*3^b、p=4P+1 为素数、r=2、d=P/2、M=kp+2、A=M 且 q=spf(d) 的族中，若 qM>B_p=(p-1)^2/4，则固定-s 候选没有支撑增长，d 对偶和 r 对偶都没有有界 joined-support RESET；余项必须转交 Type II、alternate carrier、第二秩或 q-进容量。'
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-smooth23-high-k-potential-boundary
  - type-I-overflow-support-preserving-dual-criterion
  - type-I-overflow-determinant-fixed-n-dual-support-conflict
sources:
  - claim: type-I-overflow-smooth23-high-k-potential-boundary
    role: qM>B_p high-k boundary and outer-potential context
  - claim: type-I-overflow-support-preserving-dual-criterion
    role: joined-support dual reset criterion
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: exact seed thresholds and channel receipts
topics:
  - type-I
  - overflow
  - smooth-support
  - dual-carrier
  - joined-support
  - high-k
  - no-go
  - proof-boundary
visibility: public
last_checked: '2026-08-04'
---

# 2,3-光滑 overflow 高 \(k\) 双载体 joined-support RESET 无 go

## 1. 范围

考虑参数族

\[
P=2^a3^b,\qquad p=4P+1\text{ 为素数},\qquad r=2,\qquad d=P/2,
\]

以及 verified overflow 图表

\[
M=kp+2,\qquad A=M,\qquad pn=4Md+1,
\]

其中

\[
B_p=\frac{(p-1)^2}{4},\qquad q=\operatorname{spf}(d).
\]

本卡只讨论高-\(k\) 尾部

\[
qM>B_p.
\]

它是一个算术菜单边界：不声称这些参数一定从根状态可达，也不声称它们构成
Erdős--Straus 反例。

## 2. 固定-\(s\) 通道没有支撑增长

因为 \(rd=P\)，固定-\(s\) 的所有候选满足

\[
L\mid rd=P.
\]

而 \(P<M=A\)，所以每个固定-\(s\) 候选都满足 \(L<A\)，不能产生当前选择器所需的
支撑增长或 support reset。这个结论不依赖有限扫描。

## 3. \(d\) 对偶通道

将旧支撑与 \(d\) 载体合并，joined support 为

\[
A_d=\operatorname{lcm}(M,d)
    =M\frac{d}{\gcd(M,d)}.
\]

若该通道有支撑增长，则 \(d/\gcd(M,d)>1\)。由于 \(q\) 是 \(d\) 的最小素因子，

\[
\frac{d}{\gcd(M,d)}\ge q,
\qquad A_d\ge qM>B_p.
\]

因此 \(d\) 通道的任何 joined-support RESET 都越出当前有界容量盒，不能成为
有界 E5 外层势递降边。若没有支撑增长，则它不支付旧支撑，因而也不满足当前
对偶 RESET 合同。

## 4. \(r=2\) 对偶通道

该通道的规范图表为

\[
R_r=4r-1=7,\qquad K_r=r(p-d)=2(p-d).
\]

若 \(M\) 为偶数，则

\[
\operatorname{lcm}(M,2)=M,
\]

没有支撑增长。若 \(M\) 为奇数，joined support 只能增为 \(2M\)。要使旧支撑在
该通道中被支付，需要

\[
2M\mid 2(p-d),
\qquad\text{即}\qquad M\mid p-d.
\]

但 \(d=P/2<p<M\)，所以

\[
0<p-d<M,
\]

不可能有 \(M\mid p-d\)。因此 \(r\) 对偶也不存在有界 joined-support RESET。

## 5. 选择器边界

在 \(qM>B_p\) 尾部，当前三条载体菜单均不能提供递归边：

\[
\boxed{
\text{fixed-}s\text{ 无支撑增长}
\quad\land\quad
d\text{ 对偶越出 }B_p
\quad\land\quad
r\text{ 对偶整除矛盾}.
}
\]

故该边界的状态类型固定为 `analysis_evidence`，不能标记为
`recursive_edge_eligible`。剩余路线是：

1. 直接 Type II 短证书；
2. 不同于 \(d,r\) 的 alternate carrier；
3. 第二秩（例如 Fourier/格或 \(q\)-进容量）支付；
4. 跨状态相位或载体容量证明。

对 \(q=2\)，该尾部同时落入 \(M>B_p/2\) 的 \(\Phi(M)=1\) 硬边界；对 \(q=3\)，
还可能有 \(B_p/3<M\le B_p/2\) 的 \(\Phi(M)=2\) 中间带。因此本卡不把
\(q=3\) 中间带误写成所有 fixed-\(n\) 除子都不存在，只关闭固定-\(s\) 及两个原始
对偶载体的有界 RESET。

统一选择器在五个种子

\[
(p,P)\in\{(73,18),(97,24),(193,48),(433,108),(1297,324)\}
\]

上重算高-\(k\) 起点、\(d\) 通道的最小增益 \(q\) 和 \(r\) 通道的整除矛盾；这些
回执只验证上述算术 no-go，不把有限种子外推成猜想的全称证明。

重放命令：

    python3 reproductions/type_i_representation_dual_capacity_selector.py --verify
