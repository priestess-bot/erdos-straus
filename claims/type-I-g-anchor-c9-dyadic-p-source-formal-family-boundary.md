---
kind: claim
claim_id: type-I-g-anchor-c9-dyadic-p-source-formal-family-boundary
title: c=9 dyadic 前驱的 p-source formal family 与 provenance 边界
statement: 对每个 c=9 核心素数及其合法 dyadic 前驱 P_gamma=(2 gamma x,2 gamma y-R,2 gamma-1)，通用 p-parent 的 g=B 特例总给出实际两边 formal raw path S_B -> P_gamma -> (x,y,1)。更强地，可用有限 CRT 避让构造无穷多个 gamma，使无约分 p-source S_1 -> P_gamma 也实际存在。该结论说明 c=9 不缺局部 raw source；但 S_1 和 S_B 都由目标节点反向参数化，尚无 target-independent root policy、m>1 E3 mark adapter、E4 lift 或 E5，因此不能登记为 verified_edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-raw-universal-p-parent-root-policy-boundary
  - type-I-g-anchor-c9-dyadic-high-layer-predecessor
  - type-I-g-anchor-marked-raw-peeling-calculus
  - denominator-escape-state-contract
topics:
  - type-I
  - G-anchor
  - c9
  - dyadic
  - p-parent
  - CRT
  - raw-path
  - source-provenance
  - proof-boundary
sources:
  - claim: type-I-raw-universal-p-parent-root-policy-boundary
    role: adjustable-p-parent-theorem
  - claim: type-I-g-anchor-c9-dyadic-high-layer-predecessor
    role: dyadic-predecessor-parameterization
  - concept: denominator-escape-state-contract
    role: E1-E5-admission-boundary
visibility: public
last_checked: '2026-08-06'
---

# \(c=9\) dyadic 前驱的 \(p\)-source formal family

## 1. \(c=9\) 记号与已有 dyadic 前驱

令

\[
p=72k+49,
\qquad
x=72k+40,
\qquad
M=50k+34,
\tag{1}
\]

并写

\[
R=200k+111,
\qquad
y=128k+71,
\qquad
K=Mx,
\qquad
\nu=v_2(M).
\tag{2}
\]

这就是 \(h=3k+2\) 的 \(c=9\) complement chart。对满足

\[
2^\nu\mid\gamma,
\qquad
(\gamma,R)=1,
\qquad
(x,2\gamma-1)=1,
\tag{3}
\]

的正整数 \(\gamma\)，令

\[
A=2\gamma x,
\qquad
B=2\gamma y-R,
\qquad
P_\gamma=(A,B,2\gamma-1).
\tag{4}
\]

已有 dyadic 前驱参数化给出实际 raw 边

\[
P_\gamma
\xrightarrow[q=2,\ \gcd\ \mathrm{reduction}=\gamma]{}
(x,y,1).
\tag{5}
\]

## 2. 总存在的 \(g=B\) 两边 formal path

在核心 \(c=9\) 域中

\[
2p<R<3p,
\tag{6}
\]

所以 \(p\nmid R\)。又 (3) 保证 \(P_\gamma\) primitive，且
\(pA>R\)。可调 \(p\)-parent 定理的 \(g=B\) 特例因此给出

\[
S_{B,\gamma}
=\left(pB^2,\ pAB-R,\ pB(2\gamma-1)-1\right)
\xrightarrow[q=p,\ \gcd\ \mathrm{reduction}=B]{}
(B,A,2\gamma-1).
\tag{7}
\]

这里 \((B,A,2\gamma-1)\) 只是 \(P_\gamma\) 的坐标交换。把它规范化回
\(P_\gamma\) 后，结合 (5)，每一个合法 dyadic 前驱都有一条实际的两边 formal raw path

\[
S_{B,\gamma}\longrightarrow
(B,A,2\gamma-1)\stackrel{\mathrm{can}}{\equiv}P_\gamma
\longrightarrow(x,y,1).
\tag{8}
\]

这是存在性最强的版本，却也最清楚地显示它不能单独成为 root rule：同样的反向构造
对任意 primitive target 都成立。

## 3. 无约分 \(p\)-source 的无限 CRT family

令

\[
N=p(2\gamma-1)-1,
\qquad
D=px-y.
\tag{9}
\]

若再有

\[
(B,N)=1,
\tag{10}
\]

则 \(g=1\) 的版本是 primitive，且

\[
S_{1,\gamma}
=\left(pB,\ 2p\gamma x-R,\ N\right)
\xrightarrow[q=p,\ \mathrm{shift}=1,\ \gcd\ \mathrm{reduction}=1]{}
(B,A,2\gamma-1).
\tag{11}
\]

**定理（每个核心 \(p\) 上无穷多个无约分 source）。** 对每个固定的 \(c=9\)
核心素数，存在无穷多个 \(\gamma\) 同时满足 (3) 和 (10)。

**证明。** 由 \(N=2p\gamma-p-1\)，有 \(2p\gamma\equiv p+1\pmod N\)，故

\[
pB=p(2\gamma y-R)
\equiv(p+1)y-p(x+y)
=-D
\pmod N.
\tag{12}
\]

\(B\) 为奇数而 \(N\) 为偶数，所以 \((B,N)\) 的任一素因子都是奇素数；按 (12)，
它必整除 \(D\)。另一方面，\(p\nmid RxD\)：由 (6) 有 \(p\nmid R\)，
\(0<x<p\)，且 \(p<y<2p\)，故 \(D\equiv-y\not\equiv0\pmod p\)。

对每个奇素数 \(\ell\mid RxD\)，选择 \(\gamma\pmod\ell\) 时分别避开：

\[
\begin{array}{c|c}
\ell\mid R&\gamma\equiv0\pmod\ell\\
\ell\mid x&\gamma\equiv\tfrac12\pmod\ell\\
\ell\mid D&\gamma\equiv\dfrac{p+1}{2p}\pmod\ell.
\end{array}
\tag{13}
\]

第一、二、三行分别保证 \((\gamma,R)=1\)、\((x,2\gamma-1)=1\)、
以及 \(\ell\nmid N\)。若 \(\ell\ge5\)，至多排除三个余类，仍有可选余类。
对 \(\ell=3\)，有

\[
p\equiv x\equiv1,
\qquad
R\equiv2k,
\qquad
D\equiv k-1
\pmod3.
\tag{14}
\]

若 \(k\equiv0\pmod3\)，只需避开 \(\gamma\equiv0\pmod3\)；若
\(k\equiv1\pmod3\)，只需避开 \(\gamma\equiv1\pmod3\)；若
\(k\equiv2\pmod3\)，三条都没有条件。于是 \(\ell=3\) 也总有余类可选。

把这些有限多个奇模条件与

\[
\gamma\equiv0\pmod{2^\nu}
\tag{15}
\]

用 CRT 合并，得到无穷多个正 \(\gamma\)。它们满足 (3) 与 (10)，故 (11) 成立。证毕。

## 4. 两个控制与固定 \(\gamma=2\) 的反例

对 \(p=409\)，有 \(k=5\)、\(\nu=2\)。取 \(\gamma=4\)，则

\[
P_4=(3200,4577,7),
\qquad
N=2862,
\qquad
(4577,2862)=1,
\tag{16}
\]

并且

\[
(1871993,1307689,2862)
\xrightarrow{409}
(4577,3200,7)=\tau(P_4).
\tag{17}

\]

相反，对 \(p=1489\)、\(k=20\)、\(\nu=1\)，\(\gamma=2\) 时

\[
B=6413,
\qquad
N=4466,
\qquad
(B,N)=11,
\tag{18}
\]

故 \(S_{1,2}\) 并不 primitive；但 \(\gamma=4\) 时

\[
B=16937,
\qquad
N=10422,
\qquad
(B,N)=1.
\tag{19}
\]

这严格排除了“固定 \(\gamma=2\) 覆盖全部 \(c=9\) 核心素数”的过强说法。

## 5. provenance 边界

(7) 说明 formal \(p\)-parent 的存在几乎没有筛选力；(11) 的 CRT 版本虽具有
无约分首边，\(\gamma\) 仍是针对已选 target seed 构造的。它们均没有提供：

1. target-independent 的具名 root family 与 `fresh_source_tree_only` scope；
2. 将 \(m>1\) node 接到偶侧 mark 的 E3 normal form；
3. \(\operatorname{Sol}(p)\) 的 E4 lift；
4. 已准入状态边的 E5 支付。

所以 (8) 和 (11) 的正确状态仍是 `analysis_evidence_not_verified_edge`。这不是
\(c=9\) 的 source 缺失，而是 provenance、mark 与递归合同缺失；任何把它们直接
升级为 root 或 RESET 的实现都是不合法的。
