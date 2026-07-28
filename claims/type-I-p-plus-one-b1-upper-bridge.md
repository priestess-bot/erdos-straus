---
kind: claim
claim_id: type-I-p-plus-one-b1-upper-bridge
title: 来自p加一三模四因子的B等于一上半区终端桥
statement: 对核心素数p，若奇素数q=3 mod4整除(p+1)/2，令h=(p+1)/q，则(m,A,B,C,R,K,E,n)=(q,1,1,(p+q)/4,h+1,Ch,h^2,(q-1)h)给出B=1的Type I正规形及严格上半区偶源终端桥。因而该B=1分支覆盖相对密度一的核心素数；同一正规形回缩为完整平方因子外部源当且仅当(h+2)/4整除(q+1)/2。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- b1
- terminal-bridge
- upper-half-source
- p-plus-one
- density
- external-source
- factorization
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-and-terminal-bridge-context
- paper: elsholtz_tao2013
  locator: Appendix A
  role: upper-bound-sieve-context-for-density-corollary
visibility: public
last_checked: '2026-07-28'
---

# 来自 \(p+1\) 三模四因子的 \(B=1\) 上半区终端桥

## 定理

令 \(p\equiv1\pmod {24}\) 为素数。若某个奇素数

\[
q\equiv3\pmod4,
\qquad q\mid\frac{p+1}{2},
\tag{1}
\]

令

\[
h=\frac{p+1}{q},\qquad
C=\frac{p+q}{4},\qquad
R=h+1,\qquad K=Ch.
\tag{2}
\]

则 \(h\equiv2\pmod4\)，且

\[
(m,A,B,C)=(q,1,1,C)
\tag{3}
\]

是一张 Type I 正规形。更强地，令

\[
E=h^2,\quad n=(q-1)h=p-(h-1).
\tag{4}
\]

则

\[
E\mid4K^2,\quad E\equiv1\pmod R,\quad
2\mid E,\quad E<2K,\quad
\frac{p+1}{2}<n<p.
\tag{5}
\]

因此 (3)--(4) 是[自适应上半区 \(B=1\) 终端选择猜想](type-I-adaptive-upper-b1-terminal-selector-conjecture.md)
第二分支的一张显式见证。其源恒等式为

\[
\frac4n
=\frac1{(q-1)C}+\frac1C+\frac1{Ch},
\tag{6}
\]

把最大尾从 \(pK=pCh\) 反向替换为 \((q-1)C=nK/E\)，便恢复 \(4/p\) 的
Type I 解。

## 证明

由 \(p\equiv1\pmod4\) 与 \(q\equiv3\pmod4\)，(1) 给出

\[
h\equiv2\pmod4.
\tag{7}
\]

所以 (2) 中 \(C\) 为正整数，\(R\equiv3\pmod4\)。又 \(p=qh-1\)，因此

\[
qR=q(h+1)=4C+1,\quad
4K=4Ch=h(4C)=pR+1.
\tag{8}
\]

这正是 (3) 的 \(B=1\) 正规形恒等式：其 \(H=AR-B=h\)，并恢复目标三项

\[
\frac4p=\frac1C+\frac1{Ch}+\frac1{pCh}.
\tag{9}
\]

由 \(h\equiv-1\pmod R\)，有 \(E=h^2\equiv1\pmod R\)，且 \(E\mid4C^2h^2=4K^2\)。
而 (8) 给出

\[
\begin{aligned}
4K-E
 &=4Ch-h^2\\
 &=h\bigl(q(h+1)-1-h\bigr)\\
 &=(q-1)h(h+1)=nR.
\end{aligned}
\tag{10}
\]

故 (4) 正是最大尾反向桥的源。由 (7)，\(E\) 与 \(n\) 都是偶数。并且

\[
2h<qh+q-1=4C,
\tag{11}
\]

所以 \(E=h^2<2Ch=2K\)。再由 \(q\ge3\)，

\[
n=(q-1)h>\frac{qh}{2}=\frac{p+1}{2},
\tag{12}
\]

并且 \(n<p\)，因为 \(p-n=h-1>0\)。最后，(6) 的左侧通分为

\[
\frac1C\left(\frac1{q-1}+1+\frac1h\right)
=\frac{qh+q-1}{C(q-1)h}
=\frac4{(q-1)h},
\tag{13}
\]

其中最后一步使用 \(4C=qh+q-1\)。这也逐项验证了 \(nK/E=(q-1)C\)。

## 与 \(p+1\) 证书及外部源的关系

这不是另一张不相关的 Type I 解。`p-plus-one-sqrt-certificate` 的首分母正是
\(x=C\)，其余分母为 \(Ch,pCh\)，所以 (9) 与已有 \(p+1\) 证书完全相同；这里新得到的
是它的显式 \(B=1\) 上半区偶源终端桥。

写

\[
k=\frac{R+1}{4}=\frac{h+2}{4},\quad q=4b-1.
\tag{14}
\]

由 \(h=4k-2\) 和 (2)，

\[
C=qk-b,\quad K=Ch\equiv2b=\frac{q+1}{2}\pmod k.
\tag{15}
\]

因此[\(B=1\) 外部源回缩判据](type-I-b1-external-source-retraction-criterion.md)精确给出

\[
\text{同一 }(R,K,C)\text{ 可回缩为完整平方因子外部源}
\quad\Longleftrightarrow\quad
\frac{h+2}{4}\mid\frac{q+1}{2}.
\tag{16}
\]

故本分支不能被笼统地归类为外部源：例如 \(p=433\)、\(q=7\)、\(h=62\) 时，
\(k=16\nmid4\)，但 (4) 仍给出有效上半区桥。

## 密度推论与范围

`p-plus-one-density-one-certificate` 已证明：没有满足 (1) 的 \(p\le X\) 数目为

\[
O\!\left(\frac{X}{(\log X)^{3/2}}\right).
\tag{17}
\]

本定理将其逐点构造直接运输到 \(B=1\) 上半区终端桥。因此 \(B=1\) 的第二分支本身已覆盖
相对密度一的核心素数，而不必依赖普通 Type II \(p-1\) 双尾。

这仍不推出全称选择器：由 (17) 留下的集合可以无限，且 (16) 表明即使本分支命中，也可能
落在非回缩状态。最终缺口仍是对每个残余核心素数主动选择 \((q,h)\) 的替代桥，或选择其他
\((s,R,E,C)\) 数据。

可复现检查：

~~~bash
python3 -m unittest tests/test_type_i_p_plus_one_b1_upper_bridge.py -q
~~~
