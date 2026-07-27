---
kind: claim
claim_id: marked-solution-descent-closure
title: 带标记解的严格递降闭包引理
statement: 令每个状态 s 附有分母秩 rho(s)>=2 和指定解集 W_s⊆Sol(rho(s))。若每个状态要么有一个显式元素 w_s∈W_s，要么有一条到更小秩状态 t 的显式全域提升 Phi_{t->s}:W_t->W_s，则所有 W_s 非空。以 W_(p,*)=Sol(p) 为根状态时，这给出“短证书或递降”的严格充分条件；源状态不必包含 Sol(n) 的每一个解。
claim_status: established
topics:
- descent
- induction
- solution-lift
- certificate
- proof-program
sources:
- paper: bradford2024
  locator: "Propositions 1--4"
  role: certificate-context
visibility: public
last_checked: '2026-07-23'
---

# 带标记解的严格递降闭包引理

## 定理

记

\[
\operatorname{Sol}(n)=
\left\{(a,b,c)\in\mathbb N^3:
\frac4n=\frac1a+\frac1b+\frac1c\right\}.
\]

一个**带标记状态** \(s\) 由正整数秩 \(\rho(s)\ge2\) 和指定集合

\[
W_s\subseteq\operatorname{Sol}(\rho(s))
\]

组成；此处并不预先假定 \(W_s\) 非空。设每个状态 \(s\) 都满足下列两项之一：

1. 有可直接核验的 \(w_s\in W_s\)；或
2. 存在另一状态 \(t\) 及可显式核验的全域映射
   \[
   \Phi_{t\to s}:W_t\longrightarrow W_s,
   \qquad \rho(t)<\rho(s).
   \]

则对每个状态 \(s\)，都有 \(W_s\ne\varnothing\)。

## 证明

反设存在 \(W_s=\varnothing\) 的状态，取其中 \(\rho(s)\) 最小者。它不可能属于第一种情形。
故存在第二种情形中的 \(t\)，且 \(\rho(t)<\rho(s)\)。按最小性，
\(W_t\ne\varnothing\)。任取 \(w\in W_t\)，则
\(\Phi_{t\to s}(w)\in W_s\)，矛盾。故所有标记集均非空。

这是以分母为秩的良基归纳；状态标签可以依赖于更大的目标分母，只要每条边的
实际分母严格减小，终止性不受影响。

## 对“短证书或递降”的适用形式

对每个核心素数 \(p\)，设根状态 \(r_p\) 满足

\[
\rho(r_p)=p,\qquad W_{r_p}=\operatorname{Sol}(p).
\]

若根状态的直接证据是一张满足 \(m\le H(p)\) 的 Type I/II 除子证书，则它显式给出
\(W_{r_p}\) 的元素。若没有短证书，只需构造一条到某个带标记状态 \(t\) 的边，
不需要构造更强的全域映射

\[
\operatorname{Sol}(n)\longrightarrow\operatorname{Sol}(p).
\]

后者只是本定理中 \(W_t=\operatorname{Sol}(n)\) 的特殊情形。要闭合证明，真正需要
递归地证明的是边所选择的标记集 \(W_t\) 非空。

因此，一个可用的全称证明对象是一个可递归描述的状态图：每个根 \(r_p\) 有短证书叶子，
或沿着分母严格下降的提升边走到另一个状态；每个叶子都有显式的标记解。图可以有无限多个
标签，但不能有无限下降链。

## 二分母保留提升的精确嵌入

给定 \(2\le n<p\)，以有序第一坐标为待替换项，定义目标依赖的标记集

\[
W_{p,n}^{(1)}=
\left\{(a,b,c)\in\operatorname{Sol}(n):
D=np-4(p-n)a>0,\quad D\mid npa\right\}.
\]

two-denominator-lift-criterion 给出全域映射

\[
\Phi_{p,n}(a,b,c)=\left(\frac{npa}{D},b,c\right):
W_{p,n}^{(1)}\longrightarrow\operatorname{Sol}(p).
\]

所以，只要能在状态图中证得 \(W_{p,n}^{(1)}\ne\varnothing\)，它就是一条合法的
严格递降边，尽管它未定义在 \(\operatorname{Sol}(n)\) 的其余解上。

例如 \(p=73,n=33\) 时，两个规范化源解

\[
(15,20,220),\qquad(15,22,110)
\]

属于 \(W_{73,33}^{(1)}\)，并都提升到 \(4/73\) 的解。反之，对自然缺口
\(m=3\) 的 \(n=(p+3)/4\)，
gap-three-two-denominator-lift-obstruction 说明这种标记集对每个核心素数都为空。

## 尚未闭合的部分

本引理修正了递降所需的逻辑强度，但不是 Erdős--Straus 猜想的证明。现有工作尚未给出：

\[
\text{对每个没有短证书的核心素数 }p,
\text{ 构造一个可闭合的更小标记状态。}
\]

特别地，\(33\to73\) 的边是一个局部存在例；固定缺口 \(m=3\) 的标记集恒空；
两者都不能产生覆盖所有 \(p\equiv1\pmod{24}\) 的状态图。
