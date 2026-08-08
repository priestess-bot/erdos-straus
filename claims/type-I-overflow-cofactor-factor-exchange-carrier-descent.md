---
kind: claim
claim_id: type-I-overflow-cofactor-factor-exchange-carrier-descent
title: overflow 余因子因子转移与交换的载体秩递降
statement: 设核心素数 p=1 (mod 24) 的 verified overflow 满足 pn=4Md+1、n>1、1<=d<p，并携带 A|M、1<=A<=B_p=(p-1)^2/4。写 b=M/A>1。若存在 g|b 且 1<g、dg<p，则取其中最大的 g，(M,d;A) 重图表为 (M/g,dg;A)，给出完整 E1--E5 且以 (floor(B_p/A),M) 的字典序严格下降。独立地，只要 d<b<p，即可交换为 (Ad,b;A)，同样给出完整 E1--E5 和严格载体秩下降；规范 selector 在因子转移不可用时才选此交换。两条边保持 A 与 Sol(p) 恒等提升；未满足任一条件的余项不由本引理闭合。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-fixed-n-bounded-divisor-saturation
  - type-I-overflow-fixed-s-bounded-divisor-saturation
topics:
  - type-I
  - overflow
  - cofactor
  - denominator-transfer
  - cofactor-exchange
  - carrier-rank
  - well-founded-descent
  - selector
sources:
  - claim: type-I-overflow-fixed-n-bounded-divisor-saturation
    role: outer-rank-edges-for-combined-potential
  - claim: type-I-overflow-fixed-s-bounded-divisor-saturation
    role: dual-outer-rank-edges-for-combined-potential
  - reproduction: reproductions/type_i_overflow_cofactor_factor_exchange_carrier_descent.py
    role: focused-four-route-receipt
visibility: public
last_checked: '2026-08-08'
---

# overflow 余因子因子转移与交换的载体秩递降

## 定理

设 \(p\equiv1\pmod {24}\) 为素数，且一个已有 source/path/node 回执的 overflow
满足

\[
pn=4Md+1,
\qquad n>1,
\qquad 1\le d<p.
\tag{1}
\]

令 \(A\mid M\) 为当前 absorbed support，\(1\le A\le B_p:=(p-1)^2/4\)，并取
图表无关的标记集 \(W=\operatorname{Sol}(p)\)。写

\[
b=\frac MA>1,
\qquad
\Pi_p(A)=\left\lfloor\frac{B_p}{A}\right\rfloor.
\tag{2}
\]

定义可移余因子集合

\[
\mathcal G(M,d;A)=\{g:g\mid b,\ 1<g,\ dg<p\}.
\tag{3}
\]

则有两个规范的严格递降出口：

1. 若 \(\mathcal G\ne\varnothing\)，令 \(g_*=\max\mathcal G\)，并取

   \[
   (M,d;A)\longmapsto
   \left(M_g,d_g;A\right)=\left(\frac Mg,dg;A\right).
   \tag{4}
   \]

2. 若 \(d<b<p\)，可取

   \[
   (M,d;A)=(Ab,d;A)\longmapsto
   \left(M_\times,d_\times;A\right)=(Ad,b;A).
   \tag{5}
   \]

两种情形都给出完整 E1--E5，保持旧 support \(A\)，并且对状态内禀的良基势

\[
\boxed{\ \Lambda_p(M,d;A)=\bigl(\Pi_p(A),M\bigr)\ }
\tag{6}
\]

的字典序严格下降。这里第二坐标是载体本身，不是局部 \(R\) 或一次性相位标志。
为消除同一状态的选择歧义，规范 dispatcher 先取 (4) 的最大 \(g_*\)，只有
\(\mathcal G\) 为空时才取 (5)。

还应注意，(1) 与 \(p\equiv1\pmod4\) 强制 \(n\equiv1\pmod4\)。所以以下每个正
目标 \(R=4M'-n\) 都自动满足 \(R\equiv3\pmod4\)，而 \(n>0\) 自动给出
\(R<4M'\)；这补齐 canonical 代表的同余与区间条件。

## 因子转移

设 \(g=g_*\)。因为 \(g\mid b=M/A\)，有

\[
M_g=\frac Mg=A\frac bg,
\qquad A\mid M_g,
\qquad 1<d_g=dg<p.
\tag{7}
\]

乘积保持不变：

\[
4M_gd_g+1=4Md+1=pn.
\tag{8}
\]

而 \(dg<p\) 和 \(n>1\) 给出

\[
4M_g=\frac{pn-1}{dg}>n,
\tag{9}
\]

因为 \(pn-1-dgn=n(p-dg)-1\ge n-1>0\)。故

\[
R_g=4M_g-n>0,
\qquad
K_g=M_g(p-dg)>0
\tag{10}
\]

形成合法 canonical chart，且

\[
pR_g+1=4K_g,
\qquad A\mid K_g.
\tag{11}
\]

由于 \(g>1\)，

\[
M_g=\frac Mg<M,
\qquad R_M-R_g=4M\left(1-\frac1g\right)>0.
\tag{12}
\]

所以 (4) 保持 \(\Pi_p(A)\) 而严格降低 (6) 的第二坐标。

## 余因子交换

现在设 \(d<b<p\)。由 (5)，

\[
4M_\times d_\times+1=4(Ad)b+1=pn.
\tag{13}
\]

同样，\(b<p\) 和 \(n>1\) 给出

\[
4M_\times=4Ad=\frac{pn-1}{b}>n.
\tag{14}
\]

于是

\[
R_\times=4Ad-n>0,
\qquad K_\times=Ad(p-b)>0,
\qquad pR_\times+1=4K_\times,
\qquad A\mid K_\times.
\tag{15}
\]

交换条件 \(d<b\) 还给出

\[
M_\times=Ad<Ab=M,
\qquad R_M-R_\times=4A(b-d)>0.
\tag{16}
\]

故 (5) 也保持第一坐标并严格降低第二坐标。

## E1--E5 与组合势

两种构造都继承输入的 source/path/node 回执（E1），由 (8)/(13) 及 (10)/(15)
给出整数恒等式和 canonical 条件（E2--E3），并取
\(W_T=W_S=\operatorname{Sol}(p)\) 与恒等映射（E4）。E5 正是 (6) 的严格下降。

该势还与既有 fixed-\(n\)/fixed-\(s\) 有界除子边兼容：那些边把后继 charged
support 设为选中的 \(L\)，并已证明 \(\Pi_p(L)<\Pi_p(A)\)。因此无论其后继载体
如何，第一坐标已经严格下降；本卡的两类转移则只在第一坐标相等时降低 \(M\)。
故它们可置于同一个有向 selector 中，而不需要为每个分母层另设不可逆 phase bit。

规范 selector 在 \(\mathcal G\ne\varnothing\) 时已选择因子转移；在
\(\mathcal G=\varnothing\) 且 \(b\le d\) 或 \(b\ge p\) 时，本引理不提供后继。
这些余项仍须由有界除子、support reset、终端或其它容量机制处理。

## 两个立即推论

- \(d=1\) 且 \(1<b<p\) 时，\(g=b\in\mathcal G\)，所以直接把全部余因子转入
  分母，得到 \((M,d)\mapsto(A,b)\)。
- \(d=2,b=2\) 时，\(g=2\in\mathcal G\)，得到 \((M,2)\mapsto(A,4)\)；
  \(d=2,2<b<p\) 时，若因子转移不可用则自动满足交换条件，得到
  \((M,2)\mapsto(2A,b)\)。

## 聚焦复现

```bash
python3 reproductions/type_i_overflow_cofactor_factor_exchange_carrier_descent.py --verify
```

四条精确回执覆盖 \(d=1\) 的全余因子转移、复合余因子的 proper-factor 转移、
因子转移不可用时的交换，以及 \(d=2,b=2\) 的平方分母转移；不做历史范围扫描。
