---
kind: claim
claim_id: type-II-q-one-full-carrier-second-anchor-fixed-n-macro
title: q=1 full-carrier 第二 anchor overflow 的固定-n 严格宏出口
statement: >-
  对每个 ordinary q=1 G full-carrier root，在首个 Type I child 的第二 anchor
  complete-excess rechart 被迫进入 high overflow 后，都存在一个不依赖搜索的
  fixed-n quotient-fold macro。奇数 t 时取 L=2(10t+1)，它以已支付的 support reset
  严格降低 Pi_p=floor(B_p/A)；偶数 t=2s 时取 q 为 complete-excess 中任一满足
  q|6s-1 的素数并令 L=9sq，它保留旧 support 并严格降低同一势。两种情形均有
  L|Md、A<L<=B_p，并把 transient determinant pn=4Md+1 归一到 canonical target
  (M_T,d_T,n_T;A_T)=(L,delta,n-4Lh;L)，其中 Md/L=ph+delta、1<=delta<p。
  从低 child 到该 target 的组合宏有实际 universal-p anchor provenance、Sol(p)
  恒等 lift 和严格 E5；target 是 marked absorb 或新的 overflow。两支的 delta 都
  不等于 1；每个仍为 overflow 的 macro target 都有 M_T=A_T=L、d_T=delta>=2，故
  L'=L delta 给出第二条完整乘积 strict edge。n_T<p 时它正是有界 fixed-n 饱和边；
  n_T>=p 时同一构造以无界 support 继续。若 macro target 已低于 p，则它是 marked
  absorb 并离开 high-overflow interface。该结论关闭该 q=1 子族的第二-anchor
  high-overflow 接口，但不证明后续 Type I selector 全称、terminal membership 或最终
  n<p exit。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-full-carrier-phase-root-entry
  - type-II-q-one-full-carrier-second-anchor-overflow
  - type-I-universal-p-source-capacity-anchor-orbit
  - type-I-overflow-fixed-n-quotient-fold-descent
  - type-I-overflow-fixed-n-bounded-divisor-saturation
  - type-I-overflow-unbounded-full-product-quotient-fold
  - denominator-escape-state-contract
topics:
  - type-II
  - q-one
  - full-carrier
  - type-I
  - complete-excess
  - overflow
  - fixed-n
  - quotient-fold
  - macro-edge
  - support-reset
  - well-founded-descent
  - proof-boundary
sources:
  - claim: type-II-q-one-full-carrier-second-anchor-overflow
    role: exact high-overflow input and forced even-branch excess prime
  - claim: type-I-overflow-fixed-n-quotient-fold-descent
    role: determinant quotient-fold arithmetic and outer-rank contract
  - reproduction: reproductions/type_ii_q_one_full_carrier_second_anchor_fixed_n_macro.py
    role: parity formulas, macro receipts, and focused controls
visibility: public
last_checked: '2026-08-15'
---

# q=1 full-carrier 第二 anchor overflow 的固定-n 严格宏出口

## 1. 输入与宏的形状

令

\[
p=24t+1
\]

是 ordinary \(q=1\) G endpoint 的核心素数，并从预声明 full-carrier root
执行已知的首个 Type I dispatch。记所得低 child 为

\[
H=(p,R_H,K_H;A),
\qquad 3\le R_H\le p-2,
\qquad A\mid K_H.
\tag{1}
\]

其 universal \(p\)-source 一步到达实际 anchor \((1,R_H-1,1)\)。在该 anchor
取完整超容量块

\[
Q=\prod_{v_q(R_H-1)>v_q(K_H)}q^{v_q(R_H-1)},
\qquad
M=\operatorname{lcm}(A,Q).
\tag{2}
\]

前一张卡已证明这一族恒有

\[
R_M>p,
\qquad
pR_M+1=4K_M,
\qquad
K_M=MC,
\tag{3}
\]

其中令

\[
n=4M-R_M,
\qquad d=p-C,
\]

便得到 transient overflow determinant

\[
pn=4Md+1,
\qquad 1\le d<p.
\tag{4}
\]

这里的 \(M\) 是 bundle carrier，transient overflow 保留 parent \(H\) 的 charged
support \(A\)；它不被单独入队。我们直接构造宏

\[
H\Longrightarrow T.
\tag{5}
\]

给定下文指定的 \(L\mid Md\)，写

\[
\frac{Md}{L}=ph+\delta,
\qquad h\ge0,
\qquad 1\le\delta<p,
\tag{6}
\]

并定义

\[
M_T=L,
\qquad d_T=\delta,
\qquad n_T=n-4Lh,
\qquad
R_T=4L-n_T,
\qquad K_T=L(p-\delta).
\tag{7}
\]

因为 \(p\nmid Md\)，式 (6) 的 \(\delta\) 非零。固定-\(n\) 商模 \(p\) 折叠恒等式
给出

\[
pn_T=4L\delta+1,
\qquad 0<n_T<4L,
\qquad pR_T+1=4K_T,
\qquad L\mid K_T.
\tag{8}
\]

故 \(T=(p,R_T,K_T;L)\) 是 canonical chart；\(R_T<p\) 时它是 marked absorb，
\(R_T>p\) 时它是新的 overflow。下面只需在两个 parity branch 中给出满足既有
quotient-fold 合同的显式 \(L\)。

## 2. 奇数 \(t\)：固定 paid-reset carrier

设 \(t\) 为奇数。首 child 与第二 anchor 的精确公式为

\[
A=2(8t+1),
\qquad
Q=10t+1,
\qquad
M=2(8t+1)(10t+1)=AQ.
\tag{9}
\]

这里 \((8t+1,10t+1)=1\)，且 \(Q\) 为奇数。取不依赖 \(d\) 的载体

\[
\boxed{L_o=2Q=2(10t+1).}
\tag{10}
\]

它满足

\[
L_o-A=4t>0,
\qquad
L_o\mid M\mid Md,
\qquad
A\nmid L_o.
\tag{11}
\]

最后一项不是缺陷：它正是既有 quotient-fold 合同允许的 paid support reset。
令 \(B_p=(p-1)^2/4=144t^2\)。对 \(t\ge3\)，有

\[
L_o=20t+2\le144t^2=B_p.
\tag{12}
\]

而且

\[
\frac{B_p}{A}-\frac{B_p}{L_o}
=\frac{144t^3}{(8t+1)(10t+1)}>1.
\tag{13}
\]

因此

\[
\boxed{
\left\lfloor\frac{B_p}{L_o}\right\rfloor
<
\left\lfloor\frac{B_p}{A}\right\rfloor.}
\tag{14}
\]

式 (10)--(14) 恰是 (6)--(8) 所需的全部有界除子和严格外层势条件。于是
\(H\Longrightarrow T\) 使用 \(L_o\) 是一条 paid-reset strict macro；不需要
对 \(10t+1\) 或 \(d\) 的因式分解作任何假设。

这个最后的量词点很重要。例如 \(t=25,p=601\) 时 \(Q=251\) 为素数；闭式规则
仍直接给出 \(L_o=502\)，并将 macro 送到低 target \(R_T=431<p\)。该构造不需要
预先分解 \(Q\) 或 \(d\)，更不依赖有限 carrier 搜索。

## 3. 偶数 \(t\)：forced excess prime 给出保支撑 carrier

设 \(t=2s\)。此时 \(s\ge2\)，且首 child 为

\[
A=9s,
\qquad
R_H=12s-1,
\qquad
K_H=9s(16s-1).
\tag{15}
\]

第二 anchor 是 \(2(6s-1)\)。已有第二-anchor no-go 的证明同时给出非空集合

\[
\mathcal Q_s=
\{q:\ q\text{ is prime},\ q\mid Q,\ q\mid6s-1\}.
\tag{16}
\]

取其中最小素数 \(q_*\)。由

\[
(6s-1,9s)=1
\tag{17}
\]

有 \(q_*\nmid A\)，而 \(q_*\mid Q\mid M\)，故

\[
\boxed{L_e=Aq_*=9s q_*\mid M\mid Md.}
\tag{18}
\]

它保持旧 charged support，且

\[
A<L_e,
\qquad
q_*\le6s-1<64s=\frac{B_p}{A},
\tag{19}
\]

因为

\[
B_p=\frac{(p-1)^2}{4}=576s^2.
\]

从而 \(L_e\le B_p\)，并有严格势支付

\[
\boxed{
\left\lfloor\frac{B_p}{L_e}\right\rfloor
=
\left\lfloor\frac{64s}{q_*}\right\rfloor
<64s
=
\left\lfloor\frac{B_p}{A}\right\rfloor.}
\tag{20}
\]

所以把 \(L=L_e\) 代入 (6)--(8)，得到一条 support-preserving strict macro。
与奇数支不同，这里不需要 reset；强制存在的 \(q_*\) 本身已经把 fixed-\(n\)
载体送入有界势窗口。

## 4. E1--E5 与良基支付

将 (5) 明确登记为

```text
q_one_full_carrier_second_anchor_fixed_n_escape_v1
```

它只在当前 fresh full-carrier Type I tree 内调用，并遵守 terminal-first：若 parent
已有直接 Type I/II 终端，终端优先；否则此宏的回执由以下各项组成。

| 合同 | 宏回执 |
|---|---|
| E1 | parent 的 universal \(p\)-source、唯一 \(p\)-edge 到 \((1,R_H-1,1)\)、完整 excess (2)、以及 (3)--(6) 的连续整数构造。transient overflow 不作为伪入队 source。 |
| E2 | (7)--(8) 重算 \(T\) 的 determinant、正性、canonical chart 与 \(L\mid K_T\)。 |
| E3 | parent/target 的 equation target、fresh scope、absorbed support、state class、`overflow_fixed_n_quotient_fold_outer_rank_v1` 宏正规形和内容摘要均由当前 \(p\) 与回执重算。两端采用图表无关的 full-solution marking，不继承 transient chart 的局部 F/G/hit 标签；若后继进入 chart-local Type I handler，再由该 handler 独立重算这些标签。 |
| E4 | 两端都标记 \(\operatorname{Sol}(p)\)，提升为恒等映射。 |
| E5 | (14) 或 (20) 给出 \(\Pi_p(T)<\Pi_p(H)\)。奇数支显式记录 `support_reset_paid=true`；偶数支记录 \(A\mid L_e\)。 |

故这是从真实低 child 到 \(T\) 的 strict macro，而不是用 transient
\(R_M>p\) receipt 的内部容量下降付款。特别地，宏势可取

\[
\left(1,\left\lfloor\frac{B_p}{A}\right\rfloor,\frac{K_H}{A}\right)
>
\left(1,\left\lfloor\frac{B_p}{L}\right\rfloor,\frac{K_T}{L}\right),
\tag{21}
\]

其第一局部坐标已经严格下降。

## 5. unit-defect 排除与第二条强制边

对 (6) 的任意 quotient-fold carrier，有一个直接的 unit-defect 判据。由 (4) 和
\(Md=L(ph+\delta)\)，

\[
4L\delta\equiv-1\pmod p.
\]

故

\[
\boxed{
\delta=1
\quad\Longleftrightarrow\quad
p\mid4L+1.}
\tag{22}
\]

这个判据在两个闭式 carrier 上都排除 unit defect。奇数支中

\[
4L_o+1=80t+9=3p+(8t+6),
\qquad 0<8t+6<p,
\tag{23}
\]

所以 \(p\nmid4L_o+1\)。偶数支中，\(q_*\mid6s-1\) 蕴含 \(q_*\) 为奇素数且
\(3\le q_*\le6s-1\)，并有

\[
4(4L_e+1)-3q_*p=4-3q_*.
\tag{24}
\]

右侧非零且

\[
0<3q_*-4\le18s-7<48s+1=p,
\tag{25}
\]

故也不可能被 \(p\) 整除。由 (22)，两支统一得到

\[
\boxed{d_T=\delta\ge2.}
\tag{26}
\]

macro target 的 determinant 正规形已经有

\[
M_T=A_T=L,
\qquad d_T=\delta.
\tag{27}
\]

若 \(R_T<p\)，它按定义已是 marked absorb，因而 high-overflow interface 到此结束。
以下只考虑 \(R_T>p\) 的 persistent overflow target。令

\[
S_T=L\delta=\frac{pn_T-1}{4}.
\tag{28}
\]

由 (26) 有 \(S_T>L\)。因此完整乘积 quotient-fold 可取 \(L'=S_T\)，其商为一，
并给出第二个 target

\[
\boxed{
M_U=A_U=S_T,
\qquad d_U=1,
\qquad n_U=n_T,
\qquad
R_U=(p-1)n_T-1,
\qquad K_U=S_T(p-1).}
\tag{29}
\]

直接有

\[
pR_U+1=4K_U,
\qquad S_T\mid K_U,
\qquad
\left\lfloor\frac{B_p}{S_T}\right\rfloor
<
\left\lfloor\frac{B_p}{L}\right\rfloor,
\tag{30}
\]

其中最后的不等式只用 \(S_T/L=\delta\ge2\) 与 \(L\le B_p\)。所以 (29) 是从
已持久 macro target 出发的第二条 strict full-product edge；它原样继承 scope 与
\(\operatorname{Sol}(p)\) 恒等 lift。其 E1 是本卡第一宏的完整 receipt 加 target
determinant，E2--E3 是 (29)--(30) 的 canonical charged state 重算，E4 是恒等 lift，
E5 由 (30) 支付。这里没有用 transient receipt 的内部数值作为势源。

\(n_T<p\) 只是 (29) 的一个有界特例。因为 \(n_T\equiv p\equiv1\pmod4\)，此时
\(n_T\le p-4\)，而 macro target 本身必为 high chart：奇数支

\[
4L_o-p=56t+7>p,
\tag{31}
\]

偶数支则由 \(q_*\ge3\) 得

\[
4L_e-p=36sq_*-48s-1\ge60s-1>p.
\tag{32}
\]

所以 \(R_T=4L-n_T>p\)，且 \(S_T\le B_p\)。这时 (29) 正是已有 bounded fixed-\(n\)
饱和边；\(n_T=1\) 时 \(U\) 是 marked absorb，\(n_T\ge5\) 时 \(U\) 仍是 overflow。
若 \(n_T\ge p\)，\(S_T\) 可以越过 \(B_p\)，但 (29) 仍由无界 complete-product
contract 保持严格。故本卡的第二条边不留下一个 \(n_T\ge p\) 的 high-overflow
算术残余。对立即的 \(U\) receiver，后续的
[p-free 门全称排除与严格 complete-excess 继电](type-II-q-one-full-carrier-d-one-p-free-gate-exclusion-relay.md)
进一步关闭了 p-free bundle failure，并给出一条严格 relay；其仍待处理的边界是
relay 后的非 q=1 \(d=1\) regeneration target，以及一般 Type I selector。

## 6. 范围与后果

这个结果消除了一个具体的未闭合接口：第二 anchor 被迫形成的 high overflow 不再需要
另行猜测一个因子或使用有限扫描；两支都有闭式 quotient-fold carrier。它没有给出
\(T\) 的最终 Egyptian-fraction certificate，也没有证明每个后继 Type I overflow
仍有同类 carrier。因此尚未证明全局 G/Type I exit 或 Erdős--Straus 猜想。

聚焦重放：

```bash
python3 reproductions/type_ii_q_one_full_carrier_second_anchor_fixed_n_macro.py --verify
```
