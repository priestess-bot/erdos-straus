---
kind: claim
claim_id: type-I-root-capacity-stutter-transverse-overlap-receipt-relay
title: 横向 stutter overlap 的 receipt 商与 checkpoint 赋值 relay
statement: >-
  对核心素数 p≡1 mod24 的 actual proper-root stutter receipt，令
  z=R-h=ED、e=(ph+1)/D、E=1+ps，且在 a=1,d=1 root interface 写
  B0=2pr-1、B1=B0E-s、E1=(p-1)B1-1。若 q|D* 属于 p±1 overlap，
  b=v_q(p±1)、t=v_q(D)-b、tau=v_q(T)，则恒有
  v_q(pE+e)=tau-t。若 q|m、q|p+1 且 q|E，则
  v_q(e)=v_q(a)=0、v_q(ph+1)=b+t。若 q|m+2、q|p-1 且 q|E，则
  v_q(e)=v_q(s+1)=v_q(r-1)=v_q(E1+1)=b，
  v_q(a)=v_q(B1)=0，且 v_q(ph+1)=2b+t。该 relay 是将横向 residual
  接到 actual receipt quotient 与下一 checkpoint 的必要容量映射，不构造
  Type I/II 证书、已注册递降边或全局出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-general-endpoint-divisor-gate
  - type-I-root-capacity-stutter-transverse-overlap-complete-excess-valuation-classification
  - type-I-overflow-full-product-d-one-a-one-single-endpoint-stutter-guarded-relay
topics:
  - type-I
  - root-capacity
  - stutter
  - transverse-residual
  - complete-excess
  - receipt-quotient
  - checkpoint-relay
  - valuations
  - provenance
  - proof-boundary
sources:
  - claim: type-I-root-capacity-general-endpoint-divisor-gate
    role: actual-receipt-identities-and-stutter-multiplier
  - claim: type-I-root-capacity-stutter-transverse-overlap-complete-excess-valuation-classification
    role: p-plus-minus-one-overlap-excess-classification
  - claim: type-I-overflow-full-product-d-one-a-one-single-endpoint-stutter-guarded-relay
    role: canonical-checkpoint-B-one-and-E-one-relay
  - reproduction: reproductions/type_i_root_capacity_stutter_transverse_overlap_receipt_relay.py
    role: fixed-local-receipt-relay-controls
visibility: public
last_checked: '2026-08-14'
---

# 横向 stutter overlap 的 receipt 商与 checkpoint 赋值 relay

## 1. 设置

固定核心素数 \(p\equiv1\pmod {24}\) 的 actual proper-root stutter receipt，写

\[
z=R-h=ED,\qquad
e=\frac{ph+1}{D},\qquad
C=\frac{p^2-1}{2},\qquad K=CT.
\tag{1}
\]

在 nonterminal stutter 中，canonical multiplier 满足 \(E\equiv1\pmod p\)，故可写

\[
E=1+ps,\qquad s\in\mathbb Z_{>0}.
\tag{2}
\]

这里的正性不是额外假设：若 \(E=1\)，则 \(z=D\mid K\)，已经是
terminal-first 分类中的 bottom Type I terminal；因而它不会留在本卡讨论的
nonterminal 分支中。

取一个奇素数 \(q\mid D_*\)，落在此前已经分类的 \(p\pm1\) overlap 中。令

\[
b=v_q(p\pm1),\qquad
t=v_q(D)-b>0,\qquad
\tau=v_q(T),\qquad
\epsilon=v_q(E).
\tag{3}
\]

在当前的 \(a=1,d=1\) root interface，stutter checkpoint 还使用

\[
B_0=2pr-1,\qquad
B_1=B_0E-s,\qquad
E_1=(p-1)B_1-1.
\tag{4}
\]

这里 \(E_1\) 是 relay 的下一 ordinary multiplier。式 (4) 是精确整数 checkpoint
公式；本卡不会把它本身误记为已通过 E1--E5 的递归边。

## 2. receipt 商的基本桥

由 \(4K=pR+1\)、\(z=ED\) 及 \(eD=ph+1\)，有

\[
\begin{aligned}
pED+eD
&=p(R-h)+(ph+1)\\
&=pR+1\\
&=4K.
\end{aligned}
\]

因此

\[
\boxed{
D(pE+e)=4K=2(p^2-1)T.}
\tag{5}
\]

在两种 \(p\pm1\) overlap 中，\(q\) 为奇数且只整除 \(p^2-1\) 的一个线性因子，
所以 \(v_q(p^2-1)=b\)。由 (3)、(5) 得到精确商赋值

\[
\boxed{v_q(pE+e)=\tau-t.}
\tag{6}
\]

特别地，(6) 重新给出 \(\tau\ge t\)，但比单独的 \(q^t\mid T\) 多记录了
actual multiplier \(E\) 与 receipt quotient \(e\) 的抵消方式。

## 3. \(p+1,h-1,m\) 的 excess relay

设 \(q\mid m\)、\(q\mid p+1\)，并再假设 \(q\mid E\)。此前的 actual
complete-excess 分型给出

\[
\tau=t,\qquad \epsilon>0.
\tag{7}
\]

所以 (6) 的左侧是 \(q\)-单位。另一方面 \(q\mid pE\)，故必有

\[
\boxed{v_q(e)=0.}
\tag{8}
\]

再由 \(q\mid m\)、\(h\equiv1\pmod q\) 与 \(a=em-h\)，有

\[
\boxed{a\equiv-1\pmod q,\qquad v_q(a)=0.}
\tag{9}
\]

最后 \(eD=ph+1\) 给出

\[
\boxed{v_q(ph+1)=b+t.}
\tag{10}
\]

因此这个支路中，进入 \(E\) 的 \(q\)-excess 不会同时进入 \(e\)；它保持在
multiplier 一侧，而 \(a\) 仍是 \(q\)-单位。

## 4. \(p-1,h+1,m+2\) 的完整 relay

现在设 \(q\mid m+2\)、\(q\mid p-1\) 且 \(q\mid E\)。此前分型给出

\[
\tau=b+t,\qquad \epsilon>b.
\tag{11}
\]

所以 (6) 给 \(v_q(pE+e)=b\)。而 \(v_q(pE)=\epsilon>b\)，故非阿基米德
比较强制

\[
\boxed{v_q(e)=b.}
\tag{12}
\]

又 \(q\mid e\)、\(m\equiv-2\pmod q\) 与 \(h\equiv-1\pmod q\)，所以

\[
\boxed{a=em-h\equiv1\pmod q,\qquad v_q(a)=0.}
\tag{13}
\]

由 \(eD=ph+1\) 还得到

\[
\boxed{v_q(ph+1)=2b+t.}
\tag{14}
\]

将 (2) 改写为

\[
p(s+1)=E+p-1.
\tag{15}
\]

右端两项的 \(q\)-赋值分别为 \(\epsilon>b\) 与 \(b\)，于是

\[
\boxed{v_q(s+1)=b.}
\tag{16}
\]

此外，(11) 给 \(\tau>b\)。利用

\[
2T=2p^2(r-1)+(p-1)(2p+1)
\tag{17}
\]

及 \(q\ne3\)，两项赋值比较给出

\[
\boxed{v_q(r-1)=b.}
\tag{18}
\]

最后 \(p\equiv r\equiv1\pmod q\) 蕴涵 \(B_0\equiv1\pmod q\)。由
\(q\mid E\) 及 \(s\equiv-1\pmod q\)，(4) 给

\[
B_1=B_0E-s\equiv1\pmod q.
\tag{19}
\]

故 \(v_q(B_1)=0\)，并且

\[
\boxed{
v_q(E_1+1)
=v_q((p-1)B_1)
=b.}
\tag{20}
\]

合并 (12)、(16)、(18)、(20)，得到这条实际 q-primary relay：

\[
\boxed{
q\mid(E,D_*,m+2,p-1)
\Longrightarrow
v_q(e)=v_q(s+1)=v_q(r-1)=v_q(E_1+1)=b,
}
\tag{21}
\]

同时 \(a,B_1\) 都是 \(q\)-单位。换言之，p-minus-one overlap 中超出完整容量门的
raw \(q\)-excess 不是模糊地消失：它在当前 receipt quotient 中留下基准 \(q^b\)，
并在下一 checkpoint 的 \(E_1+1\) 中恰以同一基准重新出现。

## 5. 边界

式 (21) 只是来源与容量的 relay，不是 Type I/II 证书。特别地，
\(q^b\mid E_1+1\) 不自动命中 ordinary multiplier 的 terminal menu，也不能替代
target 的 terminal-first 重分类、persistent lineage、全域 identity lift 或 E5。

它的作用是把 future transverse_residual_provenance_adapter 的输入从“某个
\(q\mid D_*\)”收紧为明确的 receipt/checkpoint 赋值图。任何试图把 p-minus-one
complete-excess overlap 登记为递归 action 的证明，现在必须解释 (21) 在下一图表中
由何种已验证终端、source 或严格势消耗。

## 聚焦复现

~~~bash
python3 reproductions/type_i_root_capacity_stutter_transverse_overlap_receipt_relay.py --verify
~~~

脚本只重放两个固定局部 receipt relay 控制：一个 \(p+1\) excess 和一个
\(p-1\) excess。两者均满足 (1)、(2)、(5) 及相应的 q-primary 赋值，但明确不
冒充 actual root receipt，也不扫描范围。
