---
kind: claim
claim_id: type-II-q-one-mask-p-plus-one-upper-bridge-boundary
title: q=1 H3 掩码的 p+1 商上半区桥容量与单项式边界
statement: >-
  令 p=qh-1 是核心素数，其中 q 是整除 p+1 的 1 (mod 4) 素数，且
  h=(p+1)/q。自然的上半区偶源 n=(q-1)h 满足 p/2<n<p。保留一个 n 的标准偶源
  严格提升存在当且仅当某个 e|[np]^2 满足 R|np+e，其中
  R=(3q-4)h+1；等价地，R|(3q-4)^2e+4(q-1)^2。这个等价式是 q=1 H3 掩码的
  精确除子容量映射。不存在令该同余成为 h 的代数恒等式的因子分离单项式
  e=c*h^alpha*p^beta（c|(q-1)^2，0<=alpha,beta<=2）。在实际 H3 硬控制
  p=14449、q=5、h=2890 中，np 的平方的全部 315 个因子均不满足该同余，故
  p+1 商的标准上半区桥不能关闭该掩码分支。这只排除该带标记桥，不否定 p 的
  其它短证书或其它非线性提升。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-fourth-anchor-terminal-gate
  - even-standard-two-tail-descent
  - one-denominator-lift-factor-criterion
topics:
  - type-II
  - type-I
  - q-one
  - p-plus-one
  - upper-half-source
  - strict-descent
  - marked-solution
  - divisor-capacity
  - obstruction
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-fourth-anchor-terminal-gate
    role: H3-bounded-q-one-mask-and-hard-control
  - claim: even-standard-two-tail-descent
    role: complete-even-source-lift-factor-criterion
  - reproduction: reproductions/type_ii_q_one_mask_p_plus_one_upper_bridge_boundary.py
    role: symbolic-capacity-map-and-fixed-control
visibility: public
last_checked: '2026-08-15'
---

# q=1 H3 掩码的 \(p+1\) 商上半区桥容量与单项式边界

## 1. 两个自然的 \(p+1\) 商源

取 H3 掩码中的一个素因子

\[
q\equiv1\pmod4,
\qquad q\mid p+1,
\qquad h=\frac{p+1}{q},
\qquad p=qh-1.
\tag{1}
\]

由于 \(p\equiv1\pmod{24}\)，有 \(h\equiv2\pmod4\)，而 \(q\ge5\)。直接取
\(h\) 作为标准偶源并不能产生有用的保留分母提升：

\[
p-4h=(q-4)h-1>0.
\tag{2}
\]

所以标准源

\[
\frac4h=\frac1{h/2}+\frac1h+\frac1h
\tag{3}
\]

的三个分母都小于 \(p/4\)，但任一 \(4/p\) 的正单位分数分母都严格大于
\(p/4\)。这只排除保留 (3) 中任一分母的直接桥，不排除一般 \(4/h\) 解的非保留
变换。

真正处于已有偶上半区提升定理范围内的自然候选是

\[
n=(q-1)h=p-h+1.
\tag{4}
\]

它是偶数，并且

\[
2n-p=(q-2)h+1>0,
\qquad p-n=h-1>0.
\tag{5}
\]

故 \(p/2<n<p\)，可以从标准标记源

\[
\frac4n=\frac1{n/2}+\frac1n+\frac1n
\tag{6}
\]

尝试保留一个 \(n\)、重组其余两尾。

## 2. 精确的 \(q=1\) 掩码容量式

令

\[
s=3q-4,
\qquad R=4n-p=sh+1,
\qquad S=np=(q-1)h(qh-1).
\tag{7}
\]

由 \(\gcd(R,S)=1\)，偶标准源的完整因子判据给出：严格提升 (6) 存在，当且仅当
存在一个因子 \(e\mid S^2\)（按互补因子交换可取 \(e\le S\)）使

\[
R\mid S+e.
\tag{8}
\]

这里 \(s\) 在模 \(R\) 下可逆，且

\[
sn\equiv-(q-1),
\qquad sp\equiv-4(q-1),
\qquad s^2S\equiv4(q-1)^2\pmod R.
\tag{9}
\]

因此 (8) 恰等价于

\[
\boxed{R\mid s^2e+4(q-1)^2.}
\tag{10}
\]

一旦 (10) 命中，提升是完全显式的：

\[
u=\frac{S+e}{R},
\qquad
v=\frac{S+S^2/e}{R},
\qquad
\frac4p=\frac1n+\frac1u+\frac1v.
\tag{11}
\]

故 (10) 不是启发式筛选，而是这一标记桥的精确容量映射。

## 3. 不存在统一的因子分离单项式选择器

考虑最自然的“只使用已知三块”的因子选择器

\[
e=c h^\alpha p^\beta,
\qquad c\mid(q-1)^2,
\qquad0\le\alpha,\beta\le2.
\tag{12}
\]

它确实总是 \(S^2\) 的因子。下面否定的是更强、也更适合作为全局 selector 的要求：
(10) 要作为 \(h\) 的**代数恒等式**成立，而不是仅在偶发的单个 \(h\) 上成立。

令 \(d=\alpha+\beta\)。把 \(S+e\) 乘以 \(s^{\max(2,d)}\)，再模线性多项式
\(sh+1\) 取余。\(d\) 为偶数时余项是两个正项之和，不可能为零。\(d\) 为奇数时
仅有如下四个零余项候选：

\[
\begin{array}{c|c}
(\alpha,\beta)&\text{零余项所强制的等式}\\ \hline
(1,0)&cs=4(q-1)^2\\
(0,1)&cs=q-1\\
(1,2)&s=4c\\
(2,1)&c=(q-1)s
\end{array}
\tag{13}
\]

但

\[
\gcd(s,q-1)=1,
\qquad s=3q-4>q-1,
\qquad s\equiv3\pmod4.
\tag{14}
\]

第一行会迫使 \(s\mid4\)，第二、四行会迫使 \(s\mid q-1\)，第三行会迫使
\(4\mid s\)。它们全部矛盾。因此：

\[
\boxed{\text{不存在 (12) 形式的统一 }p+1\text{ 商上半区桥。}}
\tag{15}
\]

这不是对 (10) 的逐点否定。它只说明 H3 的有界 \(q\) 不能仅靠从
\(h\)、\(p\)、\(q-1\) 各取固定幂的因子而自动消失；下一步必须选择真正依赖于
\(h\) 的非单项式因子，或者放弃此桥。

## 4. H3 硬控制的完整失败

第四锚门给出的实际 hard branch 控制为

\[
p=14449,
\qquad q=5,
\qquad h=2890,
\qquad n=11560,
\tag{16}
\]

其中 H3 的 \(g=5\)。这里

\[
R=31791=3\cdot10597,
\qquad
S=167030440=2^3\cdot5\cdot17^2\cdot14449.
\tag{17}
\]

于是 \(S^2\) 恰有

\[
(6+1)(2+1)(4+1)(2+1)=315
\tag{18}
\]

个正因子。模 \(10597\) 中，\(5\) 是原根，且

\[
2=5^{2757},\quad17=5^{5547},\quad14449=5^{3688},\quad-S=5^{7160}.
\tag{19}
\]

故 (8) 会强制某个指数盒

\[
0\le i\le6,
\quad0\le j\le2,
\quad0\le k\le4,
\quad0\le\ell\le2
\tag{20}
\]

满足

\[
2757i+j+5547k+3688\ell\equiv7160\pmod{10596}.
\tag{21}
\]

这个 315 点整数盒没有解。因此没有任意 \(e\mid S^2\) 满足 (8)，更不可能得到
(11)。复现器直接枚举同一有限盒并独立检查原整除式。

这是 H3 掩码中一个严格的、有限可证的桥失败控制；它**不是** \(4/14449\) 无解的
断言。它只把后续工作准确收缩为：寻找非标准标记源、非单项式因子选择器，或 H3 图表
之外的状态转移。

Focused verification:

```bash
python3 reproductions/type_ii_q_one_mask_p_plus_one_upper_bridge_boundary.py --verify
```
