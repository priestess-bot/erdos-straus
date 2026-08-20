---
kind: claim
claim_id: type-I-marked-g-universal-anchor-complete-excess-exit
title: 低支撑 marked F/G 的通用锚点 complete-excess 全称出口
statement: >-
  设 p=1 (mod 24) 为素数，S=(p,R,K;A,sigma) 是由独立 producer receipt
  给出的 actual persistent TYPEI/CHARGED 状态，满足 4K=pR+1、
  3<=R<=p-2、A|K、W_S=Sol(4,p)，并在 terminal-first 后仍为 marked F/G。
  则 universal p-source 唯一到达 (1,R-1,1)：若 R-1|K，直接得到 Type I
  root terminal；否则 R-1 的完整超容量块 Q 与 M=lcm(A,Q) 确定一个 canonical
  target。该 target 在 terminal-first 命中时终止，否则经独立 F/G/overflow
  重分类得到完整 E1--E5 verified successor。由于 marked parent 自动有 A<=B_p
  且 M/A>=2，T5 的 floor(B_p/A) 坐标严格下降。特别地，这关闭了独立产生的
  terminal-free marked G 出口量词；它不证明 F1 reachable-state exhaustion，
  也未在冻结的 15-edge v2 surface 上静默注册新 producer。
claim_status: established
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
  - selector-totality
  - verified-edge
  - well-founded-descent
  - proof-boundary
sources:
  - claim: type-I-universal-p-source-capacity-anchor-orbit
    role: universal-source-anchor-and-complete-excess-receipt
  - claim: type-I-bottom-sink-scc-complete-excess-bundle-selector
    role: full-block-bundle-and-canonical-target
  - claim: type-I-overflow-unbounded-same-chart-promotion-persistence-boundary
    role: low-support-parent-to-target-E1-E5-and-rank
  - concept: t5-global-well-foundedness-contract-v2
    role: fixed-T5-LOCAL-DROP-ticket
  - reproduction: reproductions/type_i_marked_g_universal_anchor_complete_excess_exit.py
    role: p601-marked-G-and-target-reclassification-control
visibility: public
last_checked: '2026-08-20'
---

# 低支撑 marked F/G 的通用锚点 complete-excess 全称出口

## 1. 精确量词

固定核心素数

\[
p\equiv1\pmod {24},
\qquad
B_p=\frac{(p-1)^2}{4}.
\tag{1}
\]

设

\[
S=(p,R,K;A,\sigma)
\tag{2}
\]

是由独立 constructor/producer receipt 产生的 actual、persistent、内容寻址的
`TYPEI/CHARGED` 状态，并满足

\[
4K=pR+1,
\qquad
3\le R\le p-2,
\qquad
A\mid K,
\qquad
W_S=\operatorname{Sol}(4,p).
\tag{3}
\]

在 source 上先执行已登记的 terminal-first。以下定理覆盖其 miss 后的 marked F/G
分类；source owner 必须由 producer 独立给出，不能把“normalizer 已成功”写进
legal-state 定义后再循环使用。

## 2. 通用实际 source 与 anchor 三分

定义规范形式 source

\[
(U,V,m)=\bigl(p,R(p-1)-p,p-1\bigr).
\tag{4}
\]

由 $p\nmid K$，唯一 $q=p$ raw edge 的 shift 是 $t=1$，且没有 gcd 约分：

\[
\bigl(p,R(p-1)-p,p-1\bigr)
\xrightarrow{q=p,t=1}
(1,R-1,1).
\tag{5}
\]

若

\[
R-1\mid K,
\tag{6}
\]

则 $1\cdot(R-1)\mid K$，anchor 直接序列化一张 Type I root terminal。对 G
状态，(6) 还会使 $-1\equiv R-1\pmod R$ 落在 $K$-support 生成子群内，故与 G
分离角色矛盾；因此 G 分支必进入下述 bundle。

若 (6) 失败，唯一写成

\[
R-1=Q\beta,
\qquad
Q=\prod_{v_q(R-1)>v_q(K)}q^{v_q(R-1)}.
\tag{7}
\]

逐素数得到

\[
Q>1,
\quad
\beta\mid K,
\quad
(Q,\beta)=1,
\quad
Q\nmid K,
\quad
Q<R<p.
\tag{8}
\]

对当前 charged support 取

\[
M=\operatorname{lcm}(A,Q).
\tag{9}
\]

某个 $q\mid Q$ 满足 $v_q(Q)>v_q(K)\ge v_q(A)$，所以

\[
\boxed{M/A\ge2.}
\tag{10}
\]

## 3. 唯一 canonical target

取唯一整数

\[
1\le R'<4M,
\qquad
pR'\equiv-1\pmod {4M},
\tag{11}
\]

并置

\[
K'=\frac{pR'+1}{4},
\qquad
T=(p,R',K';M,\sigma).
\tag{12}
\]

于是 $R'\equiv3\pmod4$、$R'\ne p$、$M\mid K'$。在 enqueue 前重新运行
terminal-first 与完整 target typing：

1. 若 target 给出 direct root certificate，输出 terminal leaf；
2. 若 $R'<p$，独立重算为 marked F 或 G；
3. 若 $R'>p$，独立重算为 low-support 或 high-support overflow owner。

任何 target 都不得继承 source 的 G 标签、state ID 或 owner digest。

## 4. E1--E5

| 合同 | 支付内容 |
|---|---|
| E1 | actual persistent source receipt；绑定 (4)--(5)、anchor、完整超额 $Q$、scope $\sigma$ 与 terminal-priority digest |
| E2 | 从 $(p,A,Q)$ 唯一重算 $(M,R',K')$，核验正性、canonical range 与 $M\mid K'$ |
| E3 | source/target normal form、state ID、F/G/hit/overflow 与 owner 在 enqueue 前独立重算 |
| E4 | 非终端两端都取 $\operatorname{Sol}(4,p)$，lift 是恒等映射；root terminal 不创建边 |
| E5 | 固定 T5 `TYPEI/CHARGED` 的第一 local coordinate 严格下降 |

E5 是全称整数不等式。由 (3)，

\[
A\le K=\frac{pR+1}{4}
\le\frac{p(p-2)+1}{4}=B_p.
\tag{13}
\]

结合 (10)，

\[
\left\lfloor\frac{B_p}{M}\right\rfloor
\le
\left\lfloor\frac{B_p}{2A}\right\rfloor
<
\left\lfloor\frac{B_p}{A}\right\rfloor.
\tag{14}
\]

所以完整 T5 势

\[
\Pi_{T5}(S)=
(\rho,\mathrm{TYPEI},\mathrm{CHARGED},
\lfloor B_p/A\rfloor,K/A,\eta,0)
\tag{15}
\]

取得 `LOCAL_DROP`，无需对 target 的第二坐标另加假设。这证明了

\[
\boxed{
\text{actual marked F/G terminal-first miss}
\Longrightarrow
\text{root terminal 或 verified successor}.}
\tag{16}
\]

## 5. $p=601$ 的 marked-G 重入控制

取

\[
(R,K;A)=(599,90000;1),
\qquad
K=2^4 3^2 5^4.
\tag{17}
\]

模 $599$ 的 Jacobi 角色在 $2,3,5$ 上均为 $+1$，在 $-1$ 上为 $-1$，故
source 是 G。规范路径与 bundle 为

\[
(601,358799,600)\longrightarrow(1,598,1),
\tag{18}
\]

\[
598=299\cdot2,
\qquad
Q=299,
\quad
\beta=2,
\quad
M=299.
\tag{19}
\]

canonical target 是

\[
(R',K';M)=(199,29900;299),
\tag{20}
\]

且 source/target 分别有 local rank

\[
(90000,90000)>(301,100).
\tag{21}
\]

目标经独立 Jacobi 重算仍为 G；这说明 marked-G re-entry 不是空形式。另一方面
$p=601$ 本身已有直接根证书，所以 (17) 只是图表、typing 与 E1--E5 控制，不是
真正 ESC 反例。

## 6. 接入边界

本定理可把局部原子记为

```text
F2-M-MARKED-G-EXIT = CLOSED_BY_UNIVERSAL_VERIFIED_SUCCESSOR
```

但当前 `data/t6-proof-frontier-v2.json` 冻结的是 15-edge surface，而当前 F1 复核又明确
保持 semantic reachable-state exhaustion 为 OPEN。因此本卡不静默修改 v2 inventory，
也不推出 `GAP-O1-POST-G-TYPE-I` 全局关闭。若把该宏加入实际 selector，必须发布新的
versioned edge surface，并重新核对 producer exhaustion、source owner 与所有 target 的
re-entry。

聚焦验证：

```bash
python reproductions/type_i_marked_g_universal_anchor_complete_excess_exit.py --verify
```
