---
kind: claim
claim_id: type-I-g-anchor-jacobi-odd-complete-excess-source-menu
title: G-anchor 的 Jacobi-odd 完整超额块与有限 raw 路径菜单
statement: 对每个核心素数 p=1 (mod 24)，令 R=p-2、K=(p-1)^2/4、Q=(p-3)/2，并令 chi_R(u)=(u/R)。则 chi_R 是 U(R) 上非平凡二次角色，所有 q|K 都满足 chi_R(q)=1，而 chi_R(Q)=-1。通用 p 源经实际 raw 边到达 (1,2Q,1)，其中 Q 是唯一的完整超额 bundle，且 (Q,K)=1、2|K。因而 D_p^-={d|Q:chi_R(d)=-1} 是非空有限的 path-anchored raw 路径菜单；每个 d 给出终点 {2Q/d,R-2Q/d} 的实际相位分离。该结论提供真实 G-anchor source/provenance，不推出 Type I/II、CRT 整数纤维、E4 或 E5。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-universal-p-source-capacity-anchor-orbit
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
  - type-I-overflow-d-one-p-minus-two-g-rechart
topics:
- type-I
- G-state
- G-anchor
- Jacobi-symbol
- complete-excess-bundle
- universal-source
- raw-path
- phase-source
- finite-menu
- proof-boundary
sources:
  - claim: type-I-universal-p-source-capacity-anchor-orbit
    role: actual-universal-source-and-anchor-path
  - claim: type-I-bottom-sink-scc-complete-excess-bundle-selector
    role: complete-excess-bundle-definition
  - claim: type-I-overflow-d-one-p-minus-two-g-rechart
    role: G-chart-Jacobi-separation
visibility: public
last_checked: '2026-08-05'
---

# G-anchor 的 Jacobi-odd 完整超额块与有限 raw 路径菜单

## 1. 规范 G-anchor

固定核心素数

\[
p\equiv1\pmod {24},
\qquad
R=p-2,
\qquad
K=\frac{(p-1)^2}{4},
\qquad
Q=\frac{p-3}{2}.
\tag{1}
\]

写 \(p=24h+1\)。则

\[
R=24h-1\equiv7\pmod8,
\qquad
Q=12h-1,
\qquad
K=144h^2,
\qquad
R-1=2Q.
\tag{2}
\]

这正是高载体 \(n=p\) 分支的规范 \(G\)-图表；但下文的实际来源不依赖某条
overflow 边是否已经可提升。

令

\[
\chi_R:U(R)\longrightarrow\{\pm1\},
\qquad
\chi_R(u)=\left(\frac{u}{R}\right)
\tag{3}
\]

为 Jacobi 角色。\(R\) 可以合数；Jacobi 符号仍给出 \(U(R)\) 上的乘法二次角色。
由于 \(\chi_R(-1)=-1\)，该角色必非平凡。

## 2. K 支撑与 Q 的精确相位

先有

\[
\chi_R(2)=1,
\qquad
\chi_R(-1)=-1,
\tag{4}
\]

因为 \(R\equiv7\pmod8\)。若 \(q\) 是 \(K\) 的奇素因子，则 \(q\mid p-1\)，所以
\(R=p-2\equiv-1\pmod q\)。二次互反律给出

\[
\left(\frac qR\right)
=(-1)^{(q-1)/2}\left(\frac Rq\right)
=(-1)^{(q-1)/2}\left(\frac{-1}q\right)=1.
\tag{5}
\]

式 (4) 和 (5) 合起来给出

\[
\boxed{\chi_R(q)=1\quad\text{对每个素数 }q\mid K.}
\tag{6}
\]

另一方面 \(2Q=R-1\equiv-1\pmod R\)，故

\[
\boxed{
\chi_R(Q)
=\chi_R(2)^{-1}\chi_R(-1)
=-1.
}
\tag{7}
\]

因此 \(Q\) 是一个真实的、与全部 \(K\) 支撑相反的 Jacobi 相位载体，而不只是
Fourier 角色中的抽象方向。

## 3. Q 是完整超额 bundle

通用 \(p\) 源

\[
\bigl(p,\ R(p-1)-p,\ p-1\bigr)
\tag{8}
\]

沿唯一的 \(q=p,t=1\) raw 边实际到达锚点

\[
(1,R-1,1)=(1,2Q,1).
\tag{9}
\]

在该锚点，\(2\mid K\) 且 \(v_2(2Q)=1<v_2(K)\)。对每个奇素数
\(q\mid Q\)，由

\[
\gcd(Q,K)=\gcd(12h-1,144h^2)=1
\tag{10}
\]

有 \(v_q(2Q)>v_q(K)=0\)。按完整超额 bundle 的定义，必须保留每个 offending
素数的完整幂块，故唯一的完整超额 bundle 是

\[
\boxed{Q_{\mathrm{exc}}=Q,}
\tag{11}
\]

而不是 \(Q\) 的任意真因子。其余因子为 \(\beta=2\)，并且

\[
1\cdot\beta=2\mid K,
\qquad
(Q,\beta)=1,
\qquad
Q\nmid K.
\tag{12}
\]

所以 (8)--(12) 构成一个可回放的 path-anchored complete-excess receipt。

## 4. 有限 Jacobi-odd 路径菜单

定义

\[
\mathcal D_p^-=
\{d:d\mid Q,\ \chi_R(d)=-1\}.
\tag{13}
\]

它非空，因为 \(Q\in\mathcal D_p^-\)。实际上

\[
|\mathcal D_p^-|=\frac{\tau(Q)}2.
\tag{14}
\]

为证明 (14)，对所有 \(d\mid Q\) 求角色和。存在某个 \(q^e\Vert Q\) 满足
\(\chi_R(q)=-1\) 且 \(e\) 为奇数，否则 (7) 不可能成立；于是

\[
\sum_{d\mid Q}\chi_R(d)
=\prod_{q^e\Vert Q}\bigl(1+\chi_R(q)+\cdots+\chi_R(q)^e\bigr)=0.
\tag{15}
\]

正、负两个符号的除子数遂相等。

对任意 \(d\in\mathcal D_p^-\)，按 \(d\) 的素因子逐层 raw peeling，可从 (9) 到达

\[
\left\{\frac{2Q}{d},\ R-\frac{2Q}{d}\right\}.
\tag{16}
\]

每一步使用的素数都在当前坐标中超出 \(K\) 的指数，且 \(\gcd(q,R)=1\)，因此是实际
raw 边而非形式除法。终点满足

\[
\chi_R\left(\frac{2Q}{d}\right)
=\chi_R(2)\chi_R(Q)\chi_R(d)^{-1}=1,
\]
\[
\chi_R\left(R-\frac{2Q}{d}\right)
=\chi_R(-1)\chi_R\left(\frac{2Q}{d}\right)=-1.
\tag{17}
\]

若只需要一个确定性的小菜单，可取

\[
\mathcal P_p^-=
\left\{
q^{v_q(Q)}:
q\mid Q,\ \chi_R(q)=-1,\ v_q(Q)\text{ 为奇数}
\right\};
\tag{18}
\]

它也必非空，按数值最小元即可规范选择。

## 5. 不能越过的边界

\(\chi_R(d)=-1\) 只说明 \(d\) 位于 Jacobi 负陪集；它不推出
\(d\equiv-1\pmod R\)、Type I/II 整除式、共同 CRT 纤维或范围条件。特别地，真因子
\(d<Q\) 不能替代 (11) 成为原锚点的 complete-excess bundle：剩余
\(2Q/d\) 仍含 \(K\) 外因子，通常不再满足 \(x\beta\mid K\)。

本卡给出的是已验证的实际 source/path provenance，可作为 G-anchor 的相位来源输入，
不是 Type II 终端，也不是 E1--E5 递归边。将它与高载体重图表、source-switch 或
marked-absorb 递降连接起来，仍须分别给出整数纤维、全域解提升和严格势下降。
