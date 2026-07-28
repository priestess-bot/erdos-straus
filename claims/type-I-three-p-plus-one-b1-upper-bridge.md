---
kind: claim
claim_id: type-I-three-p-plus-one-b1-upper-bridge
title: 来自三p加一四分之一的B等于一上半区终端桥
statement: 对核心素数p，令N=(3p+1)/4。若奇素数q=2 mod3整除N，令r=(N/q+1)/3，则(m,A,B,C,R,K,E,n)=((4q+1)/3,r,1,q,3,N,2q,(4N-2q)/3)给出B=1的Type I正规形及严格上半区偶源终端桥。该正规形可回缩为典范外部源N，但N为奇数；E=2q提供了所需的偶源终端化。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- b1
- terminal-bridge
- upper-half-source
- three-p-plus-one
- external-source
- factorization
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-and-terminal-bridge-context
- paper: elsholtz_tao2013
  locator: Section 2
  role: Type-I-parametrization-context
visibility: public
last_checked: '2026-07-28'
---

# 来自 \((3p+1)/4\) 的 \(B=1\) 上半区终端桥

## 定理

令 \(p\equiv1\pmod {24}\) 为素数，并写

\[
N=\frac{3p+1}{4}.
\tag{1}
\]

若某个奇素数满足

\[
q\mid N,\qquad q\equiv2\pmod3,
\tag{2}
\]

令

\[
r=\frac{N/q+1}{3},\qquad
m=\frac{4q+1}{3}.
\tag{3}
\]

则

\[
(A,B,C,R,H,K)=(r,1,q,3,N/q,N)
\tag{4}
\]

是缺口 \(m\) 的 \(B=1\) Type I 正规形。进一步令

\[
E=2q,\qquad
n=\frac{4N-2q}{3}
=2q(2r-1)
=p-\frac{2q-1}{3}.
\tag{5}
\]

则

\[
E\mid4K^2,\quad E\equiv1\pmod R,\quad
2\mid E,\quad E<2K,\quad
\frac{p+1}{2}<n<p.
\tag{6}
\]

因而 (4)--(5) 给出[自适应上半区 \(B=1\) 终端选择猜想](type-I-adaptive-upper-b1-terminal-selector-conjecture.md)
第二分支的一张显式见证。

## 正规形与偶桥

由 \(N\equiv1\pmod3\) 和 \(q\equiv2\pmod3\)，式 (3) 中 \(r\) 为正整数，且

\[
N+q=3qr,\qquad 3r-1=\frac Nq.
\tag{7}
\]

于是

\[
mR=4q+1=4C+1,\quad
K=CH=q\frac Nq=N.
\tag{8}
\]

此外，

\[
3(4AC-m)
=12qr-(4q+1)
=4(N+q)-4q-1
=4N-1
=3p,
\tag{9}
\]

故 (4) 确实恢复 \(p=4AC-m\)。对应的目标恒等式是

\[
\frac4p=\frac1{qr}+\frac1{Nr}+\frac1{pN}.
\tag{10}
\]

现在 \(E=2q\) 是偶数且 \(E\equiv1\pmod3\)。由 \(q\mid N=K\)，有
\(E\mid4N^2=4K^2\)。同时

\[
4K-E=4N-2q=3n,
\tag{11}
\]

所以 (5) 正是这张正规形最大尾反向桥的源。因为 \(q<N\)，

\[
E=2q<2N=2K,
\qquad
n-\frac{p+1}{2}=\frac{2N-2q-1}{3}>0.
\tag{12}
\]

这里 \(q<N\) 来自 \(N/q\equiv2\pmod3\)，因而该商不可能为 \(1\)。
又 \(n<p\) 由 (5) 中正的距离 \((2q-1)/3\) 给出。至此 (6) 的全部桥条件成立。

源的首分母为

\[
\frac{nK}{E}=N(2r-1).
\tag{13}
\]

确实，使用 (7)，有

\[
\begin{aligned}
\frac1{N(2r-1)}+\frac1{qr}+\frac1{Nr}
&=\frac1{N(2r-1)}+\frac3N\\
&=\frac{2(3r-1)}{N(2r-1)}
=\frac2{q(2r-1)}
=\frac4n.
\end{aligned}
\tag{14}
\]

## 与既有奇源递降及外部源的关系

[三p加一四分之一的二分母递降](three-p-plus-one-descent-certificate.md)已从相同的 \((q,r)\)
构造 Type I 证书，并以 \(N\) 作为带标记严格递降的源。该 \(N=18t+1\) 恒为奇数，因而不能
直接作为目标终端桥。本卡不改变目标 Type I 证书，而是将同一最大尾以 \(E=2q\) 反向提升到
(5) 的偶源。

同一正规形的 \(R=3=4\cdot1-1\)，故外部源回缩尺度恒为 \(k=1\)，按
[\(B=1\) 外部源回缩判据](type-I-b1-external-source-retraction-criterion.md)，它确实可回缩到
典范外部源 \(N\)。因此这里的新增内容不是一条非回缩外部源，而是一个精确的**奇典范源到偶终端桥**
转换；这正是原有递降分支缺少、而混合终端选择器要求的奇偶性。

## 范围

[三p加一密度一递降](three-p-plus-one-density-one-descent.md)表明 (2) 覆盖相对密度一的
核心素数。本卡说明这一密度一分支实际落入所研究的 \(B=1\) 偶终端选择器，而不只是另一种
标记递降。其失败集仍可能无限；和 \(p+1\) 分支的联合残余及其筛界见
[两条移位因子分支的 \(B=1\) 筛残余](type-I-b1-two-shift-density-bridge.md)。

可复现检查：

~~~bash
python3 -m unittest tests/test_type_i_three_p_plus_one_b1_upper_bridge.py -q
~~~
