---
kind: claim
claim_id: type-II-arithmetic-lift-raw-factor-fallback
title: Type II 算术提升空集后的 raw 因子回退判据
statement: 给定带来源混合因子 h、当前 D_0 与 CRT 参数 a_0，原除子格提升候选为空并不等于没有 Type II 证书。令 L=(h+1)/4，枚举所有 A C K=L 且 h|Kp+A、A<=B=(Kp+A)/h 的 raw 三元组；该有限集合非空时直接给出 Type II 证书。原除子格候选自然嵌入该 raw 集合，因此 raw 集为空才是更强的有限算术负证书。该回退不提供统一的有界 A,C 上界。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-same-modulus-source-switch-crt-criterion
  - type-II-raw-ray-certificate
topics:
  - type-II
  - source-switch
  - arithmetic-lift
  - raw-ray
  - finite-obstruction
  - short-certificate
  - proof-boundary
sources:
  - claim: type-II-same-modulus-source-switch-crt-criterion
    role: source-labelled-crt-and-divisor-lattice
  - claim: type-II-raw-ray-certificate
    role: raw-type-ii-normal-form
visibility: public
last_checked: '2026-08-05'
---

# Type II 算术提升空集后的 raw 因子回退判据

## 1. 设置与有限回退集

设当前来源混合因子满足

\[
h>1,\qquad h\equiv-1\pmod {4D_0},\qquad
h\mid p+4D_0a_0.
\tag{1}
\]

令

\[
K_0=\frac{h+1}{4D_0},\qquad
L=\frac{h+1}{4}=D_0K_0.
\tag{2}
\]

定义有限 raw 回退集

\[
\mathscr R_{\rm raw}(h;p)=
\left\{(A,C,K):
\begin{array}{l}
A,C,K\in\mathbb N,\quad ACK=L,\\
h\mid Kp+A,\quad
A\le (Kp+A)/h
\end{array}
\right\}.
\tag{3}
\]

因为 \(ACK=L\)，枚举只需遍历 \(L\) 的有限因子三元组。由 (1) 还有精确的同余
筛选式

\[
p\equiv-4D_0a_0\pmod h,
\qquad
h\mid Kp+A
\iff
A\equiv4D_0Ka_0\pmod h.
\tag{4}
\]

所以 (3) 是一个带来源的有限算术判据，不需要重新分解 \(p+4D_0a_0\) 之外的
整数。

## 2. raw 回退给出直接 Type II

若 \((A,C,K)\in\mathscr R_{\rm raw}(h;p)\)，令

\[
B=\frac{Kp+A}{h}.
\tag{5}
\]

则

\[
h=4ACK-1,\qquad h\mid Kp+A,\qquad A\le B.
\]

由 raw Type II 正规形引理，\((A,C,K,h,B)\) 直接给出一个合法 Type II 除子证书；
必要时再对 \(A,B\) 做互素正规化。因此

\[
\boxed{
\mathscr R_{\rm raw}(h;p)\ne\varnothing
\Longrightarrow
\text{Type II 短证书}.
}
\tag{6}
\]

注意这里的 \(A,C\) 不要求 \(A\mid D_0\) 或 \(C=D'/A\)。它是对原除子格
source-switch 的严格扩展，而不是把不合法的参数纤维误当作旧模数状态。

## 3. 原除子格候选嵌入 raw 集

若 \((D',A)\) 属于已有的带来源除子格候选集，则令

\[
C=\frac{D'}A,\qquad
K=\frac{h+1}{4D'}.
\tag{7}
\]

于是 \(ACK=L\)，并且旧提升门保证 \(h\mid Kp+A\)；旧正规形还给出
\(A\le B\)。故

\[
\boxed{
\mathscr L_{D_0}(h,a_0;p)\ne\varnothing
\Longrightarrow
\mathscr R_{\rm raw}(h;p)\ne\varnothing.
}
\tag{8}
\]

因此原先的 ARITHMETIC_LIFT_EMPTY 只能说明旧 \(D_0\) 除子格没有候选，不能直接
说明没有 Type II 证书。正确的分派顺序是：

1. 先枚举旧除子格候选；
2. 若为空，再枚举 \(\mathscr R_{\rm raw}(h;p)\)；
3. raw 集非空时升级为直接 Type II；
4. raw 集也为空时，才记录更强的 RAW_LIFT_EMPTY，并转交 Fourier、另一条射线
   或递降构造。

若只允许 \(A,C\le B_{\rm short}\)，还可把 (3) 限制到该有界盒；盒内为空只能记为
RAW_SHORT_BOUND_EMPTY，不能误写成无界 raw 集为空。

## 4. 边界例子

### 原除子格为空但 raw 回退命中

取

\[
p=73,\qquad D_0=1,\qquad a_0=8,\qquad h=15.
\]

有 \(15\equiv-1\pmod4\) 且 \(15\mid73+4\cdot1\cdot8=105\)。旧除子格只有
\((D',A)=(1,1)\)，但 \(1\not\equiv8\pmod{15}\)，所以旧集合为空。另一方面

\[
L=(15+1)/4=4,\qquad
(A,C,K)=(2,2,1),\qquad
B=(73+2)/15=5
\]

属于 \(\mathscr R_{\rm raw}\)，并给出
\(h=4\cdot2\cdot2\cdot1-1\) 的直接 Type II 证书。

### raw 回退仍为空

在

\[
p=97,\qquad D_0=6,\qquad a_0=133,\qquad h=143
\]

中，\(L=36\)。完整遍历 \(ACK=36\) 的三元组后 raw 集为空；所以这个例子在
该混合因子下确实保留 RAW_LIFT_EMPTY，不能把“扩展 raw 参数”当作自动出口。

### 旧除子格候选是 raw 的特例

对 \(p=5113,D_0=6,a_0=20,h=119\)，
\((D',A)=(1,1)\) 产生
\((A,C,K)=(1,1,30)\)、\(B=1289\)，正好同时出现在两种候选集中。

## 5. 研究边界

raw 回退把一部分算术提升空集严格转成直接 Type II，但不证明 \(A,C\) 有统一小
上界，也不保证所有核心素数都能找到非空 raw 集。若 raw 集为空，仍需证明另一条
Type I/II 射线、Fourier 对偶容量或带标记的良基递降；RAW_LIFT_EMPTY 本身不是
递降回执。
