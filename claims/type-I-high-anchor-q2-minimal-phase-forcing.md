---
kind: claim
claim_id: type-I-high-anchor-q2-minimal-phase-forcing
title: beta_0=2 两锚 automatic q=2 来源的最小相位强制
statement: >-
  在 canonical high-anchor 的严格 two-anchor automatic C=2A 来源中，若 first root
  满足 Q_0=A, beta_0=2 且 second bundle 满足 Q_1=R-1，那么 A=3 mod 4、R=3 mod 8。
  因 p=1 mod 8，K=(pR+1)/4 为奇数；又 K=AB，所以 B 为奇数。automatic phase
  h=(2r-B)/p 落在 {0,1} 且为奇数，故必有 h=1。相应 b-k-u 坐标必有 k 为偶数。
  因而 q=2,k 为奇数、h=0 只是形式相位同余类，不能由该严格来源域中的实际行实现；
  所有实际 q=2 行都处于 e=2-h-1=0 的 fixed-n 算术域。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-high-anchor-automatic-q-source-template
  - type-I-high-anchor-q2-bku-source-parameterization
  - type-I-high-anchor-positive-phase-terminal-boundary
topics:
  - Erdos-Straus
  - type-I
  - high-anchor
  - automatic-q
  - q2
  - phase
  - parity
  - fixed-n
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_high_anchor_automatic_q_phase_descent_trichotomy.py
    role: residue-parity-and-fresh-source-control
visibility: public
last_checked: '2026-08-16'
---

# beta_0=2 两锚 automatic q=2 来源的最小相位强制

## 范围

固定一个来自 strict two-anchor source 的 canonical high anchor：

\[
p\equiv1\pmod {24},\qquad p<R<4A,\qquad K=AB,
\]

其中 first root 的 complete-excess 数据与第二 bundle 分别为

\[
Q_0=A,\quad \beta_0=2,
\qquad
Q_1=R-1.
\tag{1}
\]

再假设 automatic cofactor 为 \(C=2A<p\)。令 \(M\) 为第二 complete-excess
carrier，\(r=M\bmod p\)，则 automatic phase 是

\[
h=\frac{2r-B}{p},\qquad 0\le h<2.
\tag{2}
\]

本卡只处理这个严格来源域。它不涉及 terminal-first priority、parent provenance、
全域解提升或 E1--E5 宏闭合。

## 最小相位强制定理

在 (1)--(2) 的每一个实际来源行上，

\[
\boxed{B\equiv1\pmod2,\qquad h=1.}
\tag{3}
\]

若该行以既有 \(b\)-\(k\)-\(u\) 坐标记录，则进一步有

\[
\boxed{k\equiv0\pmod2.}
\tag{4}
\]

因此 direct automatic target 的余量参数

\[
e=2-h-1
\]

恒为零，并且既有 residual identity 给出 \(n_T=n\)。

### 证明

two-anchor source 模板的 root parity 给出

\[
\beta_0=2\quad\Longrightarrow\quad A\equiv3\pmod4.
\tag{5}
\]

第二 complete-excess 条件 \(Q_1=R-1\) 给出

\[
R\equiv3\pmod8.
\tag{6}
\]

又 \(p\equiv1\pmod8\)，故

\[
pR+1\equiv4\pmod8,
\qquad
K=\frac{pR+1}{4}\equiv1\pmod2.
\tag{7}
\]

由 (5) 知 \(A\) 是奇数，而 \(K=AB\) 与 (7) 遂强制 \(B\) 也是奇数。
对 (2) 模 \(2\) 化简，利用 \(p\) 是奇数，得到

\[
h\equiv2r-B\equiv1\pmod2.
\tag{8}
\]

因 \(0\le h<2\)，只能有 \(h=1\)，这证明 (3)。

最后，q=2 的 canonical \(b\)-\(k\)-\(u\) 恒等式给出

\[
B\equiv k+1\pmod2.
\tag{9}
\]

结合 \(B\) 奇即得 (4)。代入 \(e=2-h-1\) 得 \(e=0\)；已建立的
\(n_T=n+4Ae\) 随即给出 \(n_T=n\)。证毕。

## 对原相位表的修正

恒等式 \(h\equiv k+1\pmod2\) 本身仍保留形式行

\[
k\equiv1\pmod2\ \Longrightarrow\ h=0.
\]

但该行与 (5)--(7) 所强制的 \(B\) 奇性矛盾，因而不能被本卡范围内的 actual
fresh-root source 实现。它只能作为放宽 root/bundle 输入后的形式相位计算，不能再列作
strict \(\beta_0=2,Q_1=R-1\) automatic-q 分支的 nonminimal descent case。

这收缩了此前 direct \(q=2\) 来源的研究成本：其每一条实际行都已经进入最小正相位的
fixed-\(n\) 算术域。仍缺少的不是相位，而是 terminal-first dispatch、charged parent、
typed lift 和严格良基势。

## 聚焦复现

~~~bash
PYTHONPATH=reproductions python3 \
  reproductions/type_i_high_anchor_automatic_q_phase_descent_trichotomy.py --verify
~~~

复现器穷尽 \(p\bmod16\in\{1,9\}\)、\(R\bmod16\in\{3,11\}\) 的全部相关
二进残类，并重放实际 \(p=3793\) 来源；它不做历史范围扫描。
