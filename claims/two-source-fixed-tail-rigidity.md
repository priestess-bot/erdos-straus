---
kind: claim
claim_id: two-source-fixed-tail-rigidity
title: 固定尾分母的双源严格提升刚性障碍
statement: 令 p(t) 是非恒定正仿射进程，k!=l 为两个在该进程上静态整值的正尺度，n_j=((4j-1)p+1)/(4j)。不存在固定正整数 c 使 4/n_k=1/(k n_k)+1/(c n_l)+1/v(t) 对全部 t 具有整数正尾分母 v(t)。等价地，最直接的“以固定倍数的第二来源作尾”不能给出统一双源严格提升。
claim_status: established
topics:
- descent
- external-source
- multisource
- rigidity
- affine-arithmetic
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: external-source-descent-context
visibility: public
last_checked: '2026-07-25'
---

# 固定尾分母的双源严格提升刚性障碍

## 定理

令 \(p(t)\) 为非恒定正仿射整值函数。对两个不同的正尺度 \(k\ne l\)，设

\[
q_k=4k-1,
\qquad
n_j(t)=\frac{(4j-1)p(t)+1}{4j},
\]

并假设两个 \(n_j(t)\) 都在整个进程上取整数。不存在固定的正整数 \(c\)，使得

\[
\frac4{n_k(t)}=\frac1{k n_k(t)}+\frac1{c n_l(t)}+\frac1{v(t)}. \tag{1}
\]

对每个 \(t\ge0\) 都有正整数 \(v(t)\)。因此，固定第二来源倍率的双源尾分母不能
构成一条全参数有效的严格提升。

## 证明

记 \(M(t)=k n_k(t)\)、\(N(t)=n_l(t)\)。由 (1) 必有

\[
v(t)=\frac{cM(t)N(t)}{D(t)},
\qquad
D(t)=c q_kN(t)-M(t). \tag{2}
\]

把 \(M,N\) 视为 \(p\) 的仿射函数，其系数行列式为

\[
\det(M,N)
=\frac{q_k}{4}\frac1{4l}-\frac14\frac{4l-1}{4l}
=\frac{k-l}{4l}\ne0. \tag{3}
\]

故 \(M,N\) 不成比例。又 \(D\) 关于 \(p\) 的一次系数为

\[
\frac{q_k}{4}\left(\frac{c(4l-1)}l-1\right), \tag{4}
\]

它不可能为零，因为正整数 \(c,l\) 不会满足 \(c(4l-1)=l\)。所以 \(D(t)\) 是非恒定
一次多项式。并且

\[
\det(D,M)=c q_k\det(N,M)\ne0,
\qquad
\det(D,N)=-\det(M,N)\ne0. \tag{5}
\]

故 \(D\) 既不与 \(M\) 成比例，也不与 \(N\) 成比例。

若 (2) 对全部参数给出整数 \(v(t)\)，则 \(D(t)\mid cM(t)N(t)\) 对全部 \(t\ge0\)。
在 \(\mathbb Q[t]\) 中作带余除法并清除分母，余数为常数；由于 \(D(t)\) 无界，
该常数只能为零。于是 \(D\mid MN\) 于 \(\mathbb Q[t]\)。但非恒定一次多项式
\(D\) 不可约，故必须与 \(M\) 或 \(N\) 成比例，和 (5) 矛盾。

## 含义与边界

这排除了多源桥接中最自然但过于刚性的模板：从一个来源 \(n_k\) 出发，固定取另一个
来源的 \(c\) 倍作一个尾分母。它没有排除仅在部分参数值成立的恒等式，也没有排除
\(c=c(t)\)、从两个来源共同选择因子、或非线性尾分母。当前 14 条 H19-k23 残存进程的
有限状态因此需要研究真正的标记耦合或参数依赖选择，而不能期待固定双源尾自动闭合。

重建命令为 python3 reproductions/two_source_fixed_tail_rigidity.py 和
python3 -m unittest tests/test_two_source_fixed_tail_rigidity.py -q。代表性 H19-k23 数据含
528 个尺度对和常数倍率的符号行列式检查；证明本身不依赖这些有限检查。
