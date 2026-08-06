---
kind: claim
claim_id: type-II-source-lattice-fibered-kneser-selector
title: Type II 源块计数格与参数纤维的 Kneser 选择器
statement: 固定原始 D、核心素数 p 与两两互素来源块 h_i|p+4Da_i。对每个候选除子格模数 D_*|D 和 admissible A|D_*，令 I(A)={i:AD_*=Da_i (mod h_i)}，并在 G_*=U(4D_*) 中取 P_A=产品_{i∈I(A)}{1,h_i}。存在该 D_* 上的 source-switch 当且仅当 -1∈并集_A P_A。对 T_A=Stab(P_A) 与 κ_{A,i}=|{1,h_i}T_A/T_A|-1，有 |P_A|≥|T_A|(1+sum_i κ_{A,i})；若 -1 不在 P_A，则 sum_i κ_{A,i}≤|G_*/T_A|-2，若总和至少 |G_*/T_A|-1 则该纤维必命中。p=97 的 pooled hit 被逐纤维排除，p=5113 的 D_*=1 纤维给出真实降模证书。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-same-modulus-source-switch-crt-criterion
  - type-II-multiblock-kneser-active-capacity-dichotomy
topics:
- type-II
- source-lattice
- parameter-fiber
- fibered-kneser
- cross-state-capacity
- source-switch
- constructive-certificate
- pseudo-hit
- proof-program
sources:
  - claim: type-II-same-modulus-source-switch-crt-criterion
    role: source-labelled-CRT-and-divisor-lattice
  - claim: type-II-multiblock-kneser-active-capacity-dichotomy
    role: Kneser-active-capacity-bound
visibility: public
last_checked: '2026-08-04'
---

# Type II 源块计数格与参数纤维的 Kneser 选择器

## 固定候选模数与来源

固定核心素数 \(p\)、原始整数 \(D\)，以及两两互素来源块

\[
h_i\mid p+4Da_i,\qquad (h_i,4D)=1,\qquad 1\le i\le r.
\tag{1}
\]

允许沿 \(D\) 的除子格尝试一个固定候选 \(D_*\mid D\)。其 admissible 参数集合为

\[
\mathcal A_{D_*}(p)=
\left\{A:A\mid D_*,\ D_*/A\text{ 平方自由},\ 4AD_*<p\right\}.
\tag{2}
\]

对 \(A\in\mathcal A_{D_*}(p)\)，源块 \(h_i\) 能用于该参数，当且仅当

\[
h_i\mid p+4AD_*
\iff
AD_*\equiv Da_i\pmod{h_i}.
\tag{3}
\]

定义兼容源集合

\[
I_{D_*}(A)=
\left\{i:AD_*\equiv Da_i\pmod{h_i}\right\}.
\tag{4}
\]

这里使用了 \((h_i,4D)=1\)，所以可以从
\(h_i\mid(p+4Da_i)-(p+4AD_*)\) 消去 \(4D\)。

## 源块载体与精确回译

令

\[
G_*=(\mathbb Z/4D_*\mathbb Z)^\times,\qquad
u_i=h_i\bmod 4D_*,
\]

并定义该参数纤维的乘法积集

\[
P_A=\prod_{i\in I_{D_*}(A)}\{1,u_i\}\subseteq G_*.
\tag{5}
\]

则存在一个 \(D_*\) 上的 source-switch Type II 证书，当且仅当

\[
\boxed{
\exists A\in\mathcal A_{D_*}(p):
-1\in P_A.
}
\tag{6}
\]

### 证明

若 \(-1\in P_A\)，存在子集 \(S\subseteq I_{D_*}(A)\) 使
\(h_S=\prod_{i\in S}h_i\equiv-1\pmod{4D_*}\)。由 (3)，每个
\(h_i\mid p+4AD_*\)，且块两两互素，故
\(h_S\mid p+4AD_*\)。令

\[
K_S=\frac{h_S+1}{4D_*},\qquad
C_*=\frac{D_*}{A},\qquad
B_S=\frac{K_Sp+A}{h_S}.
\]

则 \(K_S,B_S\in\mathbb N\)，并且

\[
h_S=4AC_*K_S-1,\qquad
B_S-A=\frac{K_S(p-4AD_*)+2A}{h_S}>0.
\]

所以 \((A,C_*,K_S)\) 是 Type II 因子生成器。反向地，任何由这些来源块组成的
source-switch 证书，其每个块都必须满足 (3)，且其乘积在 \(G_*\) 中等于 \(-1\)，
因此 \(-1\in P_A\)。
证毕。

式 (6) 是带参数纤维的精确回译条件。把所有 \(u_i\) 直接放入一个无标签积集，
会删除 \(I_{D_*}(A)\) 这一层信息，从而制造伪命中。

## 每个参数纤维的 Kneser 容量二分

对固定 \(A\)，令

\[
T_A=\operatorname{Stab}(P_A),\qquad
\kappa_{A,i}
=\left|\{1,u_i\}T_A/T_A\right|-1
=\min\{1,\operatorname{ord}_{G_*/T_A}(u_iT_A)-1\}.
\tag{7}
\]

迭代 Kneser 不等式给出

\[
|P_A|
\ge |T_A|\left(1+\sum_{i\in I_{D_*}(A)}\kappa_{A,i}\right).
\tag{8}
\]

如果

\[
\sum_{i\in I_{D_*}(A)}\kappa_{A,i}
\ge |G_*/T_A|-1,
\tag{9}
\]

则 (8) 强制 \(|P_A|\ge|G_*|\)，从而 \(P_A=G_*\)，特别有
\(-1\in P_A\)，得到 Type II 短证书。

反之，若 \(-1\notin P_A\)，由于 \(P_A\) 是 \(T_A\)-不变集，整个目标陪集
\(-1T_A\) 都不与 \(P_A\) 相交，故

\[
|P_A|\le |T_A|(|G_*/T_A|-1),
\]

与 (8) 合并得到严格缺口

\[
\boxed{
\sum_{i\in I_{D_*}(A)}\kappa_{A,i}
\le |G_*/T_A|-2.
}
\tag{10}
\]

这是一条逐参数纤维的容量回执；不能把不同 \(A\) 的 \(\kappa_{A,i}\) 相加，因为
\(I_{D_*}(A)\)、\(T_A\) 和目标商群可能不同。

## 两个边界例子

### \(p=97\) 的 pooled pseudo-hit

取原始 \(D=6\)、\(p=97\)、候选 \(D_*=6\)，来源

\[
(a_1,h_1)=(1,11),\qquad (a_2,h_2)=(3,13).
\]

在 \(4AD_*<97\) 下，\(A=1,2,3\)。兼容集合分别为

\[
I_6(1)=\{1\},\qquad I_6(2)=\varnothing,\qquad I_6(3)=\{2\}.
\]

因此

\[
P_1=\{1,11\},\qquad
P_2=\{1\},\qquad
P_3=\{1,13\}\pmod{24},
\]

三个纤维都遗漏 \(-1=23\)。但若删去参数纤维而直接池化，

\[
\{1,11\}\{1,13\}\ni11\cdot13\equiv-1\pmod{24}.
\]

所以 pooled hit 不是 Type II 证书；(6) 精确排除了它。

### \(p=5113\) 的真实降模纤维

取原始 \(D=6\)、\(M=24\)，来源块

\[
17\mid p+4D\cdot3=5185,\qquad
7\mid p+4D\cdot6=5257.
\]

对候选 \(D_*=1,A=1\)，有

\[
1\equiv6\cdot3\pmod{17},\qquad
1\equiv6\cdot6\pmod7,
\]

故 \(I_1(1)=\{1,2\}\)。在 \(G_*=(\mathbb Z/4\mathbb Z)^\times\) 中，

\[
u_1=17\equiv1,\qquad u_2=7\equiv-1,
\]

所以 \(P_1=\{1,-1\}\)。取 \(h_S=17\cdot7=119\) 得

\[
K_S=30,\qquad B_S=1289,\qquad
m=\frac{1+B_S}{K_S}=43,\qquad d=1.
\]

这正是从 \(M=24\) 降到 \(M'=4\) 的 Type II 证书。

## 研究边界

(6)--(10) 完成了“表示—来源—容量”在固定候选模数上的精确接线：表示部分是
\(I_{D_*}(A)\)，对偶/容量部分是 \(T_A,\kappa_{A,i}\)，回译条件是 \(-1\in P_A\)。
它仍未证明对每个核心素数存在某个 \(D_*,A\) 使 (9) 成立，也未证明所有纤维容量
缺口会自动导出标记解提升或严格核心素数递降。下一步必须把 q 进高度或其它跨状态
缺陷证明性地注入同一个 \(I_{D_*}(A)\)，或者把所有纤维的 (10) 缺口送入一个具有
E1--E5 的良基下降构造。
