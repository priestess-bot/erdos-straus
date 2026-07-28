---
kind: claim
claim_id: type-I-source-square-normal-factorization
title: Type I 源平方状态的唯一正规分解与双因子块
statement: 对核心素数 p 的上半区奇移位源 n=p-s，源平方条件可用 lambda=4 或 2 消去 E 与 R，并化为 D|u^2。每个这样的正整数对唯一写成 u=alpha*beta*gamma、D=beta^2*gamma、gcd(alpha,beta)=1；由此 K=(pR+1)/4 自动分解为源块 beta*gamma 与仿射块 L=(alpha*R+beta)/(4/lambda) 的乘积。并且 beta=1 当且仅当 E|n，此时 p=a+s+asR 且 pR+1=(aR+1)(sR+1)。
claim_status: established
proof_provenance: repository_derivation
review_status: independent_review
topics:
- type-I
- source-square
- normal-form
- factorization
- shifted-source
- upper-half-source
- two-adic
- linear-source
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-and-terminal-bridge-context
visibility: public
last_checked: '2026-07-28'
---

# Type I 源平方状态的唯一正规分解与双因子块

## 严格参数域

固定核心素数 \(p\equiv1\pmod {24}\)。取奇数

\[
1\le s\le\frac{p-1}{2},\qquad n=p-s,
\]

并考虑正整数 \(R,E,K\) 满足

\[
R\ge3,\qquad R\equiv3\pmod4,\qquad
E=sR+1,\qquad K=\frac{pR+1}{4}. \tag{1}
\]

源平方条件是

\[
E\mid\frac{n^2}{\gcd(E,4)}. \tag{2}
\]

以下定理只正规化 (1)--(2)。它不包含目标除子选择，也不声称这些源状态对每个核心
素数都能完成一张 Erdős--Straus 证书。

## \(\lambda\) 消元

定义

\[
\lambda=\lambda(s)=
\begin{cases}
4,&s\equiv1\pmod4,\\
2,&s\equiv3\pmod4.
\end{cases} \tag{3}
\]

由 \(p\equiv1\pmod4\) 和 \(R\equiv3\pmod4\)，逐个检查 \(s\) 的两个奇剩余类可得

\[
\lambda=\gcd(n,4)=\gcd(E,4). \tag{4}
\]

令

\[
u=\frac n\lambda=\frac{p-s}{\lambda},\qquad
D=\frac E\lambda. \tag{5}
\]

则 \(u,D\) 是正整数，且

\[
E\mid\frac{n^2}{\gcd(E,4)}
\quad\Longleftrightarrow\quad
\lambda D\mid\lambda u^2
\quad\Longleftrightarrow\quad
D\mid u^2. \tag{6}
\]

同时，\(E=sR+1\) 精确等价于

\[
\lambda D\equiv1\pmod s,\qquad
E=\lambda D,\qquad
R=\frac{\lambda D-1}{s}. \tag{7}
\]

这里反向参数化没有隐藏的符号或模数条件。固定上述 \(p,s\)，若正因子
\(D\mid u^2\) 满足 \(\lambda D\equiv1\pmod s\)，则 (7) 给出正整数 \(R\)。
当 \(s\equiv1\pmod4\) 时，

\[
R\equiv(4D-1)s^{-1}\equiv3\pmod4.
\]

当 \(s\equiv3\pmod4\) 时，\(u=(p-s)/2\) 为奇数；由 \(D\mid u^2\) 知
\(D\) 为奇数，因而

\[
R\equiv(2D-1)s^{-1}\equiv1\cdot3\equiv3\pmod4.
\]

所以自动有 \(R\ge3\)，并且 (5)--(7) 在 (1)--(2) 的源状态与满足所列条件的
\((s,D)\) 之间给出双射。保留的上半区范围还给出

\[
2K-E=\frac{(p-2s)R-1}{2}>0, \tag{8}
\]

即 \(E<2K\)。删去 \(s\le(p-1)/2\) 会丢失这一结论。

## \(D\mid u^2\) 的唯一正规分解

令

\[
g=\gcd(u,D),\qquad
\beta=\frac Dg,\qquad
\gamma=\frac g\beta,\qquad
\alpha=\frac ug. \tag{9}
\]

则 \(\alpha,\beta,\gamma\) 是正整数，并且唯一满足

\[
\boxed{
u=\alpha\beta\gamma,\qquad
D=\beta^2\gamma,\qquad
\gcd(\alpha,\beta)=1.} \tag{10}
\]

证明只需逐素数核对，同时也能补足 (9) 中 \(\gamma\) 的整性。固定素数
\(\ell\)，写

\[
a=v_\ell(u),\qquad d=v_\ell(D),\qquad 0\le d\le2a.
\]

若 \(d\le a\)，则

\[
\bigl(v_\ell(\alpha),v_\ell(\beta),v_\ell(\gamma)\bigr)
=(a-d,0,d). \tag{11}
\]

若 \(a<d\le2a\)，则

\[
\bigl(v_\ell(\alpha),v_\ell(\beta),v_\ell(\gamma)\bigr)
=(0,d-a,2a-d). \tag{12}
\]

特别地，

\[
v_\ell(\beta)=\max(d-a,0)\le\min(a,d)=v_\ell(g),
\]

故 \(\beta\mid g\)，\(\gamma=g/\beta\) 确为整数。式 (11)--(12) 直接验证
(10)。反过来，任一满足 (10) 的三元组在每个素数处都必须落入同样的两种情形，
因此三个赋值均被唯一确定；这也证明了全局唯一性。

## \(K\) 的两个显式因子块

置

\[
\eta=\frac4\lambda\in\{1,2\}. \tag{13}
\]

由 \(4K=pR+1=(p-s)R+(sR+1)=nR+E\)，再代入 (5) 和 (10)，得到

\[
4K
=\lambda\bigl(uR+D\bigr)
=\lambda\beta\gamma(\alpha R+\beta). \tag{14}
\]

定义仿射余因子

\[
L=\frac{\alpha R+\beta}{\eta}. \tag{15}
\]

这里 \(L\) 是正整数。若 \(\lambda=4\)，则 \(\eta=1\)。若
\(\lambda=2\)，则 \(u,D\) 都是奇数，故 \(\alpha,\beta\) 都是奇数；又
\(R\) 为奇数，所以 \(\alpha R+\beta\) 为偶数。于是 (14) 精确化为

\[
\boxed{K=(\beta\gamma)L,\qquad
L=\frac{\alpha R+\beta}{\eta}.} \tag{16}
\]

第一块 \(\beta\gamma\) 完全来自源平方正规分解，第二块 \(L\) 对 \(R\) 是仿射的。
这里没有声称 \(\gcd(\beta\gamma,L)=1\)。作为整性复核，(16) 还给出

\[
\frac{nK}{E}=\alpha\gamma L,\qquad
\frac{4K^2}{E}=\eta\gamma L^2. \tag{17}
\]

## 线性特例 \(\beta=1\)

由 (5) 和 (10)，

\[
E\mid n
\quad\Longleftrightarrow\quad
D\mid u
\quad\Longleftrightarrow\quad
\beta^2\gamma\mid\alpha\beta\gamma
\quad\Longleftrightarrow\quad
\beta\mid\alpha
\quad\Longleftrightarrow\quad
\boxed{\beta=1}, \tag{18}
\]

最后一步使用 \(\gcd(\alpha,\beta)=1\)。在这一情形令

\[
a=\frac nE=\alpha.
\]

由于 \(E=sR+1\) 且 \(p=n+s\)，立即得到两个等价的线性恒等式

\[
\boxed{p=a+s+asR},\qquad
\boxed{pR+1=(aR+1)(sR+1)}. \tag{19}
\]

相应地，

\[
D=\gamma,\qquad
K=\gamma\frac{aR+1}{\eta}
=\frac{E(aR+1)}4. \tag{20}
\]

因此 \(\beta=1\) 精确刻画“线性移位源” \(E\mid n\)，而不是一般源平方状态。
它也不自动等价于完整外源回缩；后者还需满足相应的回缩条件。

可复现检查：

~~~bash
python3 -m unittest tests.test_type_i_source_square_normal_factorization -v
~~~
