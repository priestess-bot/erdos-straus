---
kind: claim
claim_id: type-I-root-capacity-stutter-transverse-residual-capacity-map
title: proper-root stutter 约化残余的横向商容量定位
statement: >-
  对核心素数 p≡1 mod24 的 terminal-first 后 actual proper-root stutter receipt，令
  M0=(p^2+p+1)/3、u=gcd(2r+1,M0)、h=3u、H=h^2-1、
  D*=D/gcd(D,H)、m=(D+h-1)/p，及 v=M0/u、w=(2r+1)/u。则 v,w 为互素奇数，
  2T=u(p^2w-3v)，并且
  1<D*|gcd(T/u,m+2r)，gcd(D*,p M0 (2r+1)(m-1))=1。
  因而 D* 的每个素因子都不具备既有根容量 external-source 菜单所需的 q|u 来源；
  这是横向 residual 的精确容量定位，不构造 Type I/II 证书、解提升或全局递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-receipt-factor-split
  - type-I-root-capacity-stutter-finite-curve-constraint
  - type-I-root-capacity-stutter-reduced-divisor-product
  - type-I-root-capacity-stutter-h-overlap-m-bound
  - type-I-root-capacity-prime-external-terminal-coupling
topics:
  - type-I
  - overflow
  - root-capacity
  - stutter
  - divisor-filter
  - transverse-residual
  - provenance
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-receipt-factor-split
    role: actual-cyclotomic-exclusion-and-root-data
  - claim: type-I-root-capacity-stutter-finite-curve-constraint
    role: stutter-parameters-and-equals-identities
  - claim: type-I-root-capacity-stutter-reduced-divisor-product
    role: D-star-divides-T
  - claim: type-I-root-capacity-stutter-h-overlap-m-bound
    role: actual-proper-root-D-star-nontriviality
  - claim: type-I-root-capacity-prime-external-terminal-coupling
    role: q-divides-u-menu-precondition
  - reproduction: reproductions/type_i_root_capacity_stutter_transverse_residual.py
    role: fixed-arithmetic-controls-for-quotient-and-coprimality-map
visibility: public
last_checked: '2026-08-14'
---

# proper-root stutter 约化残余的横向商容量定位

## 1. 设置

固定核心素数

\[
p\equiv1\pmod {24}.
\]

terminal-first 后，设一个 actual proper-root maximal complete-excess receipt
仍在唯一非严格 stutter 门中。沿用

\[
M_0=\frac{p^2+p+1}{3},\qquad
u=(2r+1,M_0),\qquad h=3u,
\tag{1}
\]

\[
T=p^2r-\frac{p+1}{2},\qquad
D=mp+1-h,\qquad eD=ph+1,
\tag{2}
\]

\[
H=h^2-1,\qquad D_*=\frac{D}{(D,H)}.
\tag{3}
\]

此前已严格得到

\[
(D,M_0)=1,\qquad D_*\mid T,\qquad D_*>1.
\tag{4}
\]

这里的最后一个不等式使用 actual proper-root 的 \(H\)-overlap 界；不能把它替换为
任意抽象的 stutter 除子。

定义根容量的两个互素商

\[
v=\frac{M_0}{u},\qquad w=\frac{2r+1}{u}.
\tag{5}
\]

由于 \(M_0\)、\(u\) 与 \(2r+1\) 都是奇数，\(v,w\) 为奇数；由 \(u\) 的最大
公因子定义，

\[
\boxed{(v,w)=1.}
\tag{6}
\]

## 2. 根容量商中的 \(T\) 残余

从 (1) 和 (5) 直接计算：

\[
\begin{aligned}
2T
 &=p^2(2r+1)-(p^2+p+1)\\
 &=u(p^2w-3v).
\end{aligned}
\tag{7}
\]

所以 \(T/u\) 是整数，且

\[
\boxed{\frac Tu=\frac{p^2w-3v}{2}.}
\tag{8}
\]

由 \(D\mid ph+1\) 及 \(h=3u\)，有 \((D,u)=1\)，故也有
\((D_*,u)=1\)。将 (4) 中的 \(D_*\mid T\) 与 \(u\mid T\) 联立，得到

\[
\boxed{D_*\mid\frac Tu.}
\tag{9}
\]

这一步保留了 root capacity 中被 \(u\) 吸收的部分，不能只从 \(D_*\mid T\) 的
形式整除式省略它。

## 3. 到 \(m+2r\) 的精确接口

stutter 参数恒等式给出

\[
\begin{aligned}
(p+e)D
 &=pD+eD\\
 &=mp^2+p+1.
\end{aligned}
\tag{10}
\]

因此有一条不含近似的接口恒等式

\[
\boxed{2T=p^2(m+2r)-(p+e)D.}
\tag{11}
\]

因为 \(D_*\mid T,D\) 且 \((D_*,p)=1\)，(11) 立刻给出

\[
\boxed{D_*\mid m+2r.}
\tag{12}
\]

结合 (4)、(9) 和 (12)，actual proper-root stutter 的非平凡残余已被压到

\[
\boxed{1<D_*\mid\gcd\!\left(\frac Tu,m+2r\right).}
\tag{13}
\]

式 (12) 也可由旧的 \(D_*\mid S=h^2-h-2r\) 与
\(Da=h^2-h+m\) 相减得到；(11) 的作用是把它展示为 \(T\)-余量和 stutter
参数之间的直接精确接口。

## 4. 横向互素性

由 (4) 有 \((D_*,v)=1\)。现证明 \((D_*,w)=1\)。若素数 \(q\) 同时整除
\(D_*\) 与 \(w\)，则 \(q\ne2\)（\(w\) 为奇数），且 \(q\ne3\)（因为
\((D_*,h)=1\)）。由 (8)--(9)，

\[
p^2w-3v\equiv0\pmod q.
\]

再代入 \(q\mid w\)，得到 \(q\mid v\)，与 \((D_*,v)=1\) 矛盾。因此

\[
\boxed{(D_*,u)=(D_*,v)=(D_*,w)=1,}
\tag{14}
\]

特别地

\[
\boxed{(D_*,M_0)=(D_*,2r+1)=1.}
\tag{15}
\]

最后，若某个素数同时整除 \(D_*\) 与 \(m-1\)，则由 (12) 也整除

\[
(m+2r)-(m-1)=2r+1,
\]

与 (15) 矛盾。又 \(p\nmid D\)，故总括为

\[
\boxed{\bigl(D_*,\,pM_0(2r+1)(m-1)\bigr)=1.}
\tag{16}
\]

## 5. 对 external-source 菜单的准确边界

已有根容量 external-source 终端菜单的输入是某个素数 \(q\mid u\)。但 (14) 表明，
每个 \(q\mid D_*\) 都满足 \(q\nmid u\)，并且 (15) 还给出
\(q\nmid2r+1\)。所以这个新的非平凡 residual 不是已有 root-capacity 素因子的
重命名：

\[
q\mid D_*
\quad\Longrightarrow\quad
\text{既有 \(q\mid u\) 菜单的前提不成立。}
\tag{17}
\]

这正是“横向”的含义。它**不**表示一般 external-source 搜索在该 \(q\) 上必为空，
也不表示 \(D_*\) 自动给出 Type I/II 证书；它只排除了把这个 residual 当作原有
root-capacity provenance 直接投递。要得到全局出口，仍须构造一个新的
`transverse_residual_provenance_adapter`，或把 (13)--(16) 转化为独立的短证书或带
identity lift 的严格递降。

## 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_stutter_transverse_residual.py --verify
```

脚本重算四个固定整数控制（包括 core-congruent composite shadow、odd、mixed 与 dyadic
\(D_*\)）。它核对 (7)--(16)，但所有控制都只验证必要算术，绝不冒充核心素数上的
actual proper-root stutter receipt，也不执行范围扫描。
