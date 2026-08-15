---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-source-residue-finite-bound
title: q=1 高 C=2 19 相位 H4 p-source/p-free 门的有限 p-adic 例外界
statement: >-
  在 q=1 high C=2 19 相位的 H3=>H4 maximal complete-excess 构造中，令 a 是第三
  phase selector，lambda|abs(1536-a)，并令 c4 为 H4 canonical capacity。存在唯一正整数
  t，使 (11943424-2261a)c4+4718592lambda=t p。若 p 大于
  2008653632908535334215，则 R4 不等于 0 或 1 (mod p)。因此在该显式界以上，H4 的
  universal p-source 门和第五 anchor 最大 complete-excess block 的 p-free 门自动通过。
  证明仅对 31 个 phase class 与 213 个 (a,lambda) 因子对作有限常数枚举，不扫描素数；
  它不处理 c5=p-1、H4/H5 typed reclassification、terminal-first 或全局 E5。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
  - type-II-q-one-c-two-19-phase-h4-carry-overlap-boundary
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - fifth-anchor
  - p-adic
  - raw-source
  - complete-excess
  - finite-exception-bound
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
    role: H4-carrier-and-finite-phase-lambda-domain
  - claim: type-II-q-one-c-two-19-phase-h4-carry-overlap-boundary
    role: H4-overlap-and-height-lower-bound
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_source_residue_finite_bound.py
    role: symbolic-coefficients-and-finite-bound-receipt
visibility: public
last_checked: '2026-08-15'
---

# q=1 high \(C=2\) 19-phase 的 H4 p-source/p-free 门有限 p-adic 例外界

## 1. H4 carrier 的前两项

保持 H3 \(\Rightarrow\) H4 的记号。令 \(a=a(p)\) 为第三 anchor 的 selector，且
\(\lambda\mid\lvert1536-a\rvert\) 为 maximal complete-excess receipt 的有限因子。写

\[
D_a=11943424-2261a,
\qquad
N_\lambda=4718592\lambda.
\tag{1}
\]

31 个实际 phase selector 均满足 \(D_a>0\)。把

\[
M_4=M_3\frac{R_3-1}{2\lambda}
\tag{2}
\]

按 \(p\) 展开，直接代入三个已知 p-anchor 的精确式得到

\[
\begin{aligned}
M_4
&=-\frac{D_a}{18874368\lambda}\\
&\quad+
\frac{517D_a-20188240592}{2000388096\lambda}p
+p^2E_{a,\lambda}(p),
\end{aligned}
\tag{3}
\]

其中 \(E_{a,\lambda}\) 是有理系数多项式；在实际 phase 输入上整个 \(M_4\) 是整数。
因为 \(4M_4c_4\equiv1\pmod p\)，(3) 的常数项给出

\[
c_4\equiv-\frac{N_\lambda}{D_a}\pmod p.
\tag{4}
\]

故有唯一正整数

\[
\boxed{t=\frac{D_ac_4+N_\lambda}{p}.}
\tag{5}
\]

H4 的既有 top-capacity 排除给出 \(1\le c_4\le p-2\)。对核心素数 \(p\ge73\)，于是

\[
1\le t\le D_a+\left\lfloor\frac{N_\lambda-1}{73}\right\rfloor.
\tag{6}
\]

这里 \(t\) 是 canonical p-adic lift，不是新选择器参数。

## 2. R4 的两点残数门

由 \(pR_4+1=4M_4c_4\)，将 (3)--(5) 代入并除去首项，得到

\[
R_4\equiv
\frac{F_0(a,\lambda,t)}
{10668736512D_a\lambda}
\pmod p,
\tag{7}
\]

其中

\[
F_e(a,\lambda,t)=2032214838431711232\lambda
-D_a\bigl((52042924032+10668736512e)\lambda+2261t\bigr),
\qquad e\in\{0,1\}.
\tag{8}
\]

具体地，若分母在 \(p\) 下可逆，则

\[
R_4\equiv e\pmod p
\quad\Longrightarrow\quad
p\mid F_e(a,\lambda,t).
\tag{9}
\]

这两个值正是第五锚 parent macro 的 source/p-free 门：\(e=0\) 会使 universal p-source
不 primitive，\(e=1\) 会使 \(p\mid(R_4-1)\)，从而最大 complete-excess block 不再 p-free。

## 3. 有限例外界

式 (6) 的区间、31 个 phase class 与所有 \(\lambda\mid\lvert1536-a\rvert\) 只产生 213 个
\((a,\lambda)\) 对。对每一对，\(F_e\) 是 \(t\) 的一次函数，因此其绝对值最大值只需检查
区间端点；其零点也可直接用整除性排除。精确有限计算给出：

| 量 | 值 |
|---|---:|
| \((a,\lambda)\) 对数 | \(213\) |
| \(\max D_a\) | \(11656277\) |
| \(\max\lambda\) | \(1409\) |
| 式 (6) 的最大上端 | \(102731566\) |
| 区间内 \(F_0,F_1\) 的整数零点 | \(0\) |
| \(\max\lvert F_e\rvert\) | \(2008653632908535334215\) |

记最后一个数为 \(B_4\)。若 \(p>B_4\)，则 \(p\) 大于 (7) 分母的每个素因子来源
\(10668736512,D_a,\lambda\)，故分母可逆。又 (8) 的对应分子非零且绝对值不超过 \(B_4<p\)，
不可能被 \(p\) 整除。由 (9) 得

\[
\boxed{p>B_4\quad\Longrightarrow\quad R_4\not\equiv0,1\pmod p.}
\tag{10}
\]

这把第五锚的前两个算术门从无界条件压缩为 \(p\le B_4\) 的有限残余；没有对该区间的
素数进行扫描。

## 4. 对第五 anchor 的后果

由 \(R_4\not\equiv0\pmod p\)，

\[
(p,R_4(p-1)-p,p-1)
\longrightarrow(1,R_4-1,1)
\tag{11}
\]

是实际 primitive p-source/anchor path。由 \(R_4\not\equiv1\pmod p\)，第五 anchor 的
最大 complete-excess block \(Q_5\mid R_4-1\) 自动 p-free。H4 overlap 界还给出
\((R_4-1,K_4)\le p+1<R_4-1\)，故 \(Q_5>1\)。因此对 \(p>B_4\)，
[第五 anchor parent-macro 准入门](type-II-q-one-c-two-19-phase-fifth-anchor-parent-macro-gate.md)
只剩 \(c_5\le p-2\)、terminal-first 与 typed reclassification 三项未决。

## 5. 范围

本卡不声称有限残余 \(p\le B_4\) 已经枚举或处理，也不证明 \(c_5\ne p-1\)。其中
\(R_4\equiv0\pmod p\) 已可由同锚最小互素素数 source 在 persistent macro 内修复；
\(R_4\equiv1\pmod p\) 则是实际 p-primary bundle 残余，不能静默删除 p-block，见
[H4 p-free 门失败的 p-block 来源障碍](type-II-q-one-c-two-19-phase-h4-p-free-p-block-provenance-obstruction.md)。
它仍只是 p-source/p-free 子门的严格有限化，而不是 G/Type I 全局出口定理。

Focused verification:

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_source_residue_finite_bound.py --verify
```
