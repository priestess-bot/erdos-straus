---
kind: claim
claim_id: type-II-canonical-fan-composition-deficit
title: Type II 规范扇支撑内失败的过滤合成列容量缺口
statement: 设一条平方自由规范 Type II 射线满足 s=a^2 c、4s<p，M=4ac，N=p+4s。若 -1 属于由 N 的素因子残数生成的群 H，则沿 H 的任意素数阶合成列，每层只要有至少 ell_j-1 个按 N 的真实赋值计数、在该层商中非平凡的物理因子槽，就能构造 h|N、h=-1 mod M，从而给出实际 Type II 短证书。故该射线失败且 -1 属于 H 时，任意这样的合成列必有一层的真实槽容量至多 ell_j-2。该缺口是单纤维、带来源的容量回执，不是抽象商递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-canonical-critical-fan-escape-trichotomy
  - type-II-filtered-composition-source-slot-terminal
topics:
- type-II
- canonical-fan
- composition-series
- capacity-deficit
- source-fiber
- terminal
- proof-program
sources:
  - claim: type-II-filtered-composition-source-slot-terminal
    role: filtered-source-slot-cover
  - claim: type-II-canonical-critical-fan-escape-trichotomy
    role: support-inside-failure-context
visibility: public
last_checked: '2026-08-06'
---

# Type II 规范扇支撑内失败的过滤合成列容量缺口

## 1. 规范射线与物理槽

固定核心素数 \(p\)，取一条满足

\[
s=a^2c,
\qquad c\text{ 平方自由},
\qquad 4s<p
\tag{1}
\]

的规范 Type II 射线。令

\[
D_*=ac,
\qquad M=4D_*=4ac,
\qquad N=p+4s=p+4aD_*=\prod_q q^{e_q}.
\tag{2}
\]

因 \(M<p\)，有 \((N,M)=1\)。令

\[
H=\left\langle q\bmod M:q\mid N\right\rangle\le U(M).
\tag{3}
\]

每个 \(q^{e_q}\parallel N\) 提供 \(e_q\) 个同一参数纤维中的可区分物理槽；这些槽
只能使用一次，故其总数就是整数 \(N\) 的真实赋值账本，而不是跨射线池化的容量。

取任一素数阶合成列

\[
1=H_0<H_1<\cdots<H_L=H,
\qquad H_j/H_{j-1}\simeq C_{\ell_j}.
\tag{4}
\]

定义第 \(j\) 层的可用真实槽数

\[
c_j(s)=
\sum_{\substack{q\mid N\\ q\bmod M\in H_j\setminus H_{j-1}}}e_q.
\tag{5}
\]

残数为单位元的因子不进入任何层；它们不能为一个非平凡合成商提供容量。

## 2. 覆盖—终端定理

若 \(-1\in H\) 且

\[
c_j(s)\ge\ell_j-1
\qquad(1\le j\le L),
\tag{6}
\]

则存在一个实际除子

\[
\boxed{h\mid N,\qquad h\equiv-1\pmod M.}
\tag{7}
\]

因此该规范射线给出 Type II 短证书。

### 证明

从第 \(j\) 层取 \(\ell_j-1\) 个互不复用的物理槽。它们在
\(H_j/H_{j-1}\) 中均为非单位元；过滤合成列覆盖定理表明，所有选中二点块的积集
覆盖 \(H\)。由 \(-1\in H\)，可选择其中一个子集，使其代表元的实际乘积 \(h\)
满足 (7)。物理槽来自 \(N\) 的不重叠赋值层，故 \(h\mid N\)。

令

\[
\kappa=\frac{h+1}{M},
\qquad C=c,
\qquad B=\frac{\kappa p+a}{h}.
\tag{8}
\]

因为 \(h\mid N=p+4aD_*\) 且 \(h=4a c\kappa-1\)，有
\(h\mid\kappa p+a\)，所以 \(B\) 为正整数。进一步，

\[
B-a
=\frac{\kappa(p-4a^2c)+2a}{h}>0.
\tag{9}
\]

于是 \((A,C,K)=(a,c,\kappa)\) 满足 Type II 因子正规形，并给出实际短证书。证毕。

## 3. 失败的规范容量缺口

若该射线没有 (7) 型 Type II 命中而 \(-1\in H\)，则 (6) 不可能对所有层成立。因此

\[
\boxed{
\exists j\in\{1,\ldots,L\},
\qquad c_j(s)\le\ell_j-2.}
\tag{10}
\]

这把 canonical-fan escape 中的支撑内多孔分支细化为带合成列层号和真实整数容量的
`CANONICAL_FAN_COMPOSITION_DEFICIT`。它不允许把不同 \(s\) 的素因子相乘，也不把
缺口本身解释为 lower-modulus relay。

## 4. 精确控制例

取

\[
p=73,
\qquad s=5=1^2\cdot5,
\qquad M=20,
\qquad N=93=3\cdot31.
\]

此时 \(H=U(20)\)。取合成列

\[
1<\langle9\rangle<\langle3\rangle<U(20),
\tag{11}
\]

三个商均为 \(C_2\)。因子 \(3\) 落在第二层，而 \(31\equiv11\pmod{20}\) 落在
第三层，故

\[
(c_1,c_2,c_3)=(0,1,1).
\tag{12}
\]

首层的 \(0=\ell_1-2\) 是严格的容量缺口。相应除子残数积集为

\[
\{1,3\}\{1,11\}=\{1,3,11,13\},
\]

确实不含 \(-1\equiv19\pmod{20}\)。该例同时说明总槽数足够大并不替代逐层条件。

## 5. 研究边界

式 (10) 是 Type II 规范扇中一个新的单纤维 q/因子槽容量映射。它没有证明这个不足层
一定给出 Type I、Type II 的另一条射线或严格可提升递降；尤其不能把抽象低模数商的
伪命中当作证书。下一步必须把具体 deficit 层接到带来源的 source-switch、稳定子核
包含或独立的良基势。
