---
kind: claim
claim_id: type-I-marked-g-universal-anchor-complete-excess-exit
title: 低支撑 marked F/G 的通用锚点 complete-excess 条件性适配器
statement: >-
  设 p=1 (mod 24) 为素数，S=(p,R,K;A,sigma) 是带独立 actual source receipt 的
  persistent TYPEI/CHARGED 状态，满足 4K=pR+1、3<=R<=p-2、A|K、
  W_S=Sol(4,p)，并在已声明 terminal-first 后为 marked F/G。universal p-source
  要么给出 Type I root terminal，要么唯一构造 complete-excess support M 与 canonical
  chart (p,R',K';M,sigma)。该构造给出 E1 的 source algebra、E2、root-wide E4 和
  T5 的严格 LOCAL_DROP；但它本身不为每个 target 构造 E3 normalizer、owner、serializer
  或 recursive re-entry。因此只有在 target 已由独立、版本化 surface 完成 E3/admission 时，
  它才成为 verified successor；本卡不关闭 F1、F2 或 T6。
claim_status: conditional
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-universal-p-source-capacity-anchor-orbit
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
  - type-I-overflow-unbounded-same-chart-promotion-persistence-boundary
  - type-I-t5-full-contract-level-global-well-foundedness
topics:
  - type-I
  - marked-state
  - G-state
  - universal-source
  - complete-excess
  - conditional-adapter
  - local-descent
  - proof-boundary
sources:
  - claim: type-I-universal-p-source-capacity-anchor-orbit
    role: universal-source-anchor-and-complete-excess-receipt
  - claim: type-I-bottom-sink-scc-complete-excess-bundle-selector
    role: full-block-bundle-and-canonical-target
  - claim: type-I-overflow-unbounded-same-chart-promotion-persistence-boundary
    role: low-support-parent-to-target-local-rank-payment
  - concept: t5-global-well-foundedness-contract-v2
    role: fixed-T5-LOCAL-DROP-ticket
  - reproduction: reproductions/type_i_marked_g_universal_anchor_complete_excess_exit.py
    role: p601-marked-G-arithmetic-and-typing-control
visibility: public
last_checked: '2026-08-21'
---

# 低支撑 marked F/G 的通用锚点 complete-excess 条件性适配器

## 1. 范围

固定核心素数

\[
p\equiv1\pmod{24},\qquad B_p=\frac{(p-1)^2}{4}.
\]

设

\[
S=(p,R,K;A,\sigma),\qquad
4K=pR+1,\qquad 3\le R\le p-2,\qquad A\mid K,
\tag{1}
\]

是一个已经由外部 producer receipt 认证为 actual、persistent 的
`TYPEI/CHARGED` 状态，且 \(W_S=\operatorname{Sol}(4,p)\)。本卡只处理该
receipt 已存在、其 declared terminal-first 已 miss 后的 marked F/G 分支；它不从
normal form 或 chart 算术反推出 source owner 或 semantic reachability。

## 2. 通用锚点与唯一目标

规范 source 为

\[
(U,V,m)=\bigl(p,R(p-1)-p,p-1\bigr).
\]

因为 \(p\nmid K\)，唯一的 \(q=p\) raw shift 给出

\[
\bigl(p,R(p-1)-p,p-1\bigr)
\xrightarrow{q=p,t=1}(1,R-1,1).
\tag{2}
\]

若 \(R-1\mid K\)，则 \(1\cdot(R-1)\mid K\)，该 anchor 可直接序列化为
Type I root terminal。若否，唯一写成

\[
R-1=Q\beta,
\qquad
Q=\prod_{v_q(R-1)>v_q(K)}q^{v_q(R-1)}.
\tag{3}
\]

逐素数分解给出

\[
Q>1,\quad \beta\mid K,\quad (Q,\beta)=1,\quad Q\nmid K.
\tag{4}
\]

令

\[
M=\operatorname{lcm}(A,Q).
\tag{5}
\]

某个 \(q\mid Q\) 的指数在 \(Q\) 中严格大于其在 \(K\) 中的指数，故

\[
\frac MA\ge2.
\tag{6}
\]

再取唯一的

\[
1\le R'<4M,\qquad pR'\equiv-1\pmod{4M},\qquad
K'=\frac{pR'+1}{4}.
\tag{7}
\]

这给出确定的算术 target \((p,R',K';M,\sigma)\)，且 \(M\mid K'\)。

## 3. 已支付的合同部分

在 (1) 的 source receipt 前提下，下列部分是全称的。

| 项 | 本卡给出的内容 |
|---|---|
| E1 | (2)--(5) 重放 \(p\)-source、anchor、完整超额 \(Q\)、\(\beta\) 与 support 变更；实际 path/provenance 仍由 source receipt 提供。 |
| E2 | (7) 由 \((p,A,Q)\) 唯一重建，且可直接验证 \(R'\)、\(K'\)、\(M\mid K'\)。 |
| E4 | 若 source 和已认证 target 均以 \(\operatorname{Sol}(4,p)\) 为 marked set，lift 为恒等映射；root terminal 不创建递归边。 |
| E5 | 见下列严格整数不等式，固定为 `LOCAL_DROP`。 |

由 \(R\le p-2\) 得

\[
A\le K=\frac{pR+1}{4}\le\frac{p(p-2)+1}{4}=B_p.
\tag{8}
\]

结合 (6)，

\[
\left\lfloor\frac{B_p}{M}\right\rfloor
\le\left\lfloor\frac{B_p}{2A}\right\rfloor
<\left\lfloor\frac{B_p}{A}\right\rfloor.
\tag{9}
\]

所以无论 target 的次级局部坐标为何，parent-to-target 的第一 T5 local coordinate
已经严格下降。

## 4. 未由本卡给出的 E3

式 (7) 只构造 chart；它不会自动把 chart 变成当前状态合同可递归消费的状态。尤其需要
独立给出：

1. target 的完整 normal form、typed F/G/hit/overflow classification 与内容寻址 state ID；
2. target serializer、scope、owner 和 terminal-first priority；
3. target 在版本化 family surface 中的唯一 T6 owner 与 recursive re-entry；
4. 若 target 引入新的 marked/atomic family，constructor admission firewall 所要求的
   T2/T3、负向测试和 surface 注册。

因此，包内对 \(p=601\) target 的 Jacobi G 重算只是**分类控制**，不构成上述全称 E3
或 owner/re-entry 证明。冻结的 `t6-proof-frontier-v2.json` 也没有登记该 producer。

精确的可用结论是

\[
\begin{aligned}
&\text{source receipt 已存在，且 (7) 的 target 已独立完成 E3/surface admission}\\
&\quad\Longrightarrow
\text{root terminal 或一条具有 E1、E2、E4、E5 的 verified successor}.
\end{aligned}
\tag{10}
\]

式 (10) 是可复用的局部适配器，不是 F1 reachable-state exhaustion 或 post-G Type-I
totality 的证明。

## 5. \(p=601\) 控制

对

\[
(R,K;A)=(599,90000;1),\qquad 598=299\cdot2,
\]

脚本重放 (2)--(7)，得到

\[
Q=299,\qquad M=299,\qquad (R',K';M)=(199,29900;299),
\]

并重算 source 与 target 的 Jacobi G separator 及

\[
(90000,90000)>(301,100).
\]

该例验证算术、局部 typing 和秩支付没有实现错误；\(p=601\) 本身另有 root terminal，
且该控制没有构造 general E3 owner，故不能作为 actual selector edge。

## 6. 状态

```text
F2-M-MARKED-FG-ANCHOR-ADAPTER = CONDITIONAL_ON_E3_AND_SURFACE_ADMISSION
T6-F1-REACHABLE-STATE-EXHAUSTION = OPEN
T6-F2-NONPROPER-DISPATCH-TOTALITY = OPEN
T6_GLOBAL_SELECTOR_TOTALITY = OPEN
```

聚焦整数控制：

```bash
python3 reproductions/type_i_marked_g_universal_anchor_complete_excess_exit.py --verify
```
