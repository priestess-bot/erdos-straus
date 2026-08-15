---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h5-a-one-full-overlap-finite-sieve
title: q=1 高 C=2 19 相位 H5 的 a=1 顶容量残余：H4 全重叠与有限素因子筛
statement: >-
  在 q=1 high C=2 19 相位的 H3=>H4=>H5 complete-excess receipt 中，设所有既有
  source/path、terminal-first、typed 与 serializer guards 已通过，H5 的 canonical
  capacity c5=p-1，且其 d=1 坐标满足 a5=1。令 w=(p+1)/2，令 sigma=a(p) 为 H3
  phase selector，Delta=abs(1536-sigma)，D=11943424-2261 sigma，N=4718592，
  lambda 为 H3=>H4 最大 complete-excess 参数，且 d=gcd(w,M4)。则 w|K4，
  d|gcd(w,c3)|Delta，且存在唯一整数 j，1<=j<2d，使
  c4=j(p+1)/(2d)，并有 p | (D j+2 d N lambda)。因此该 H5 a5=1 类，尤其其
  omega=-1 的 p-free return 子类，只能落在 31 个相位类的 571777 个显式固定整数的
  素因子菜单中；其中 377516 个不同整数的最大值为 18768297821013。它不再有无界的
  H5 a=1 tail。该结果不分解该有限菜单、不处理有限候选的终端/typed guards，也不单独
  证明 G/Type I 全局出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h5-top-capacity-d-one-handoff
  - type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
  - type-II-q-one-c-two-19-phase-h4-carry-overlap-boundary
  - type-II-q-one-c-two-19-phase-h4-source-residue-finite-bound
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fifth-anchor
  - top-capacity
  - d-one
  - a-one
  - full-overlap
  - complete-excess
  - finite-sieve
  - capacity-map
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h5-top-capacity-d-one-handoff
    role: H5-a5-one-is-exactly-w-divides-M5
  - claim: type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
    role: H3-to-H4-maximal-block-lambda-and-g-divides-Delta
  - claim: type-II-q-one-c-two-19-phase-h4-carry-overlap-boundary
    role: w-coprime-M3-and-H4-carrier-contract
  - claim: type-II-q-one-c-two-19-phase-h4-source-residue-finite-bound
    role: affine-D-c4-plus-N-lambda-equals-tp-identity
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h5_a_one_full_overlap_finite_sieve.py
    role: full-overlap-valuation-controls-and-exact-finite-menu-count
visibility: public
last_checked: '2026-08-15'
---

# H5 \(a_5=1\) 顶容量残余的 H4 全重叠有限筛

## 1. 结论位置

本卡的 \(a_5\) 是 H5 full-product \(d=1\) 坐标中的互素因子，不是 H3 的有限
phase selector。保留 H3--H5 receipt 的记号，并写

\[
w=\frac{p+1}{2},\qquad
K_4=M_4c_4,\qquad
pR_4+1=4K_4.
\tag{1}
\]

令 \(Q_5=Q_{K_4}(R_4-1)\) 为 H4 anchor 的真正 maximal complete-excess block，且

\[
M_5=\operatorname{lcm}(M_4,Q_5).
\tag{2}
\]

已有的 H5 handoff 给出

\[
a_5=1\quad\Longleftrightarrow\quad w\mid M_5.
\tag{3}
\]

我们证明 (3) 强迫一个此前未显式记录的 H4 条件：

\[
\boxed{w\mid K_4,\qquad (R_4-1,K_4)=p+1.}
\tag{4}
\]

第二个等式来自 \(p(R_4-1)=4K_4-(p+1)\)。若 \(w\mid K_4\)，则
\(p+1\mid4K_4\)，从而 \(p+1\mid R_4-1\)。H4 的既有构造还给出 \(K_4\) 为偶数；
而 \(w\) 为奇数，所以 \(p+1=2w\mid K_4\)。最后 H4 overlap 恒等式给出
\((R_4-1,K_4)\mid p+1\)，故得到等号。这里的方向只有 (3) 导出 (4)；反向并不成立。

## 2. 完整超额的全重叠必要条件

先给出不依赖 19-phase 的局部引理。设 \(p\equiv1\pmod8\)，

\[
K=Mc,\qquad pR+1=4K,\qquad V=R-1,
\]

并令 \(Q=Q_K(V)\) 为相对于 \(K\) 的完整素数幂 excess，
\(M^+=\operatorname{lcm}(M,Q)\)。则

\[
\boxed{w\mid M^+\ \Longrightarrow\ w\mid K.}
\tag{5}
\]

**证明。** 固定奇素数幂 \(\ell^r\Vert w\)，并写

\[
\mu=\nu_\ell(M),\qquad k=\nu_\ell(K),\qquad v=\nu_\ell(V).
\]

若 \(\mu\ge r\)，则 \(\ell^r\mid K\)。否则，\(w\mid M^+\) 强迫
\(\ell^r\mid Q\)。完整 excess 的定义因而给出 \(v>k\) 及 \(v\ge r\)。另一方面

\[
pV=4K-(p+1).
\tag{6}
\]

若 \(k<r\)，右侧两项的 \(\ell\)-进赋值分别为 \(k,r\)，所以 \(v=k\)，矛盾。
故 \(k\ge r\)。这对 \(w\) 的每个奇素数幂成立，证明 (5)。\(\square\)

将 \(M=M_4,c=c_4,Q=Q_5\) 代入，(3) 和 (5) 即给出 (4)。这一步没有把
complete-excess 误写成任意 \(R_4-1\) 因子：当一个素数幂在 \(K_4\) 中不弱于
\(R_4-1\) 时，它不会进入 \(Q_5\)。

## 3. H4 旧 carrier 与 \(w\) 的交集仍是有限的

令 \(\sigma=a(p)\) 为 H3 phase selector，且

\[
\Delta=\lvert1536-\sigma\rvert,\qquad
g=(w,c_3),\qquad
d=(w,M_4).
\tag{7}
\]

H3--H4 的最大块构造给出

\[
(w,M_3)=1,\qquad
M_4=\operatorname{lcm}(M_3,Q_4),\qquad
g\mid\Delta,
\tag{8}
\]

其中 \(Q_4=Q_{K_3}(R_3-1)\)。因此

\[
\boxed{d\mid g\mid\Delta.}
\tag{9}
\]

确实，令 \(\ell^r\Vert w\)。因为 \((w,M_3)=1\)，若 \(\ell\mid M_4\)，则
\(\ell\mid Q_4\)。记 \(e=\nu_\ell(c_3)=\nu_\ell(K_3)\)。H3 的方程同样有

\[
p(R_3-1)=4K_3-(p+1).
\tag{10}
\]

若 \(e<r\)，则 \(\nu_\ell(R_3-1)=e\)，不可能满足完整 excess 进入 \(Q_4\) 所需的
\(\nu_\ell(R_3-1)>e\)。所以只要 \(\ell\) 出现在 \(M_4\) 中，就有 \(e\ge r\)，即
\(\ell^r\mid g\)。逐素数幂合并得到 (9)。

因此，H5 的 \(a_5=1\) 不是允许 \(w\) 从任意新大因子自由进入 \(M_5\)：由 (4)、(9)，

\[
w\mid M_4c_4,\qquad (w,M_4)=d\mid\Delta.
\tag{11}
\]

约去完整 gcd 后 \(w/d\mid c_4\)。由于 H4 canonical capacity 满足
\(1\le c_4\le p-2=2w-3\)，存在唯一整数 \(j\) 使

\[
\boxed{
c_4=\frac{jw}{d}=\frac{j(p+1)}{2d},
\qquad 1\le j<2d.
}
\tag{12}
\]

## 4. 固定整数素因子菜单

H4 的既有 affine lift 写为

\[
D_\sigma c_4+N\lambda=tp,\qquad
D_\sigma=11943424-2261\sigma>0,\qquad N=4718592,
\tag{13}
\]

其中 \(t\) 为正整数，且 H3--H4 最大 complete-excess receipt 给出
\(\lambda\mid\Delta\)。将 (12) 代入 (13) 并乘以 \(2d\)，得到

\[
\bigl(2dt-D_\sigma j\bigr)p
=D_\sigma j+2dN\lambda.
\tag{14}
\]

右侧严格为正，故左侧系数也严格为正，特别地

\[
\boxed{
p\mid C(\sigma,\lambda,d,j):=D_\sigma j+2dN\lambda.
}
\tag{15}
\]

这不是渐近界，而是候选素数的固定整数整除式。令 \(\mathcal U_{31}\) 是 H3
terminal-first 后留下的 31 个 phase 类。所有 H5 \(a_5=1\) top-capacity 输入都必须落在

\[
\mathcal C=
\left\{
C\bigl(a(p_u),\lambda,d,j\bigr):
u\in\mathcal U_{31},\quad
\lambda\mid\Delta,\quad d\mid\Delta,\quad 1\le j<2d
\right\}.
\tag{16}
\]

对既有的 31 个 selector 和其固定 \(\Delta\) 因子作精确枚举，得到

\[
\begin{array}{c|r}
\text{parameter rows }(u,\lambda,d,j) & 571\,777\\
\text{distinct integers in }\mathcal C & 377\,516\\
\max\mathcal C & 18\,768\,297\,821\,013.
\end{array}
\tag{17}
\]

最大值在

\[
(u,\sigma,\Delta,\lambda,d,j)
=(27,127,1409,1409,1409,2817).
\tag{18}
\]

因此特别有

\[
\boxed{a_5=1\quad\Longrightarrow\quad p\le18\,768\,297\,821\,013}
\tag{19}
\]

在这个 H5 residual route 内成立。它严格小于 H4 source/p-free 门先前的
\(2\,008\,653\,632\,908\,535\,334\,215\) 例外界：不存在一个同时属于本 H5
\(a_5=1\) 残余且随 \(p\) 无界增长的区间。

## 5. 合同含义与范围

前一卡的真正 p-free return 还要求 terminal digit \(\omega=-1\pmod p\)。它是
\(a_5=1\) 的子类，所以同样受 (15)--(19) 约束。对每个实际候选，仍须重放：

1. H3--H5 的 source/path、maximality、terminal-first 和 typed guards；
2. \(d=(w,M_4)\)、\(j\)、\(t\) 的实际 receipt，而不是任意 (16) 的超集行；
3. 若它未被短证书抢占，剩余 p-free return 的独立 exit 或 \(n<p\) lift。

本卡本身没有把 \(\mathcal C\) 的素因子超集误报为实际 phase prime、已可达状态或全局
G/Type I exit。它只把先前唯一的无界 H5 \(a_5=1\) 算术残余变成有限、可逐因子审理的
候选菜单；后续的[有限筛完成](type-II-q-one-c-two-19-phase-h5-a-one-full-overlap-sieve-completion.md)
才精确分解该菜单并排除其唯一 affine 伪候选。

## 6. 定向回执

~~~bash
python3 reproductions/type_ii_q_one_c2_19_phase_h5_a_one_full_overlap_finite_sieve.py --verify
~~~

回执核对完整-excess 全重叠必要条件及其非逆性、两张实际 H4 receipt 的 \(d\mid g\)
约束，以及 (16)--(18) 的精确有限菜单计数；它不扫描原始分母或重放历史 selector。
