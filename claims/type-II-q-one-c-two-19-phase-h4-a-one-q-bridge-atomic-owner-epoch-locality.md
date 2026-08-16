---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-atomic-owner-epoch-locality
title: H4 atomic q-bridge 的局部 owner 唯一性与无重收费
statement: >-
  固定一个已经通过 terminal-first prefix 的 actual high C=2 19-phase H4 persistent
  source state S。canonical clean q-word、其定向 endpoint 及两侧 maximal complete-excess
  blocks Q_x,Q_y 都是 S 的确定函数；single-side exclusion 又给 Q_x,Q_y>1。因此
  owner_tuple=(adapter version, source_state_id, canonical physical-path digest) 在此 H4
  branch 中唯一，selector 至多有一个 atomic candidate。若它构造 target support
  M=lcm(A_S,Q_x,Q_y) 与 K_T=M c_T，则每个 ell|Q_xQ_y 均有
  v_ell(K_T)>=v_ell(Q_xQ_y) 在其所属颜色上的指数；同一 colored complete-excess
  block 不可能在同一无 reset epoch 再次被 verifier 认作 fresh。任何后来可收费的 ell
  block 必有更高指数，故 lcm support 严格增长。由于此局部 selector 不聚合多个 outgoing
  action 的容量，良基归纳只使用一个已选 edge；跨 action global one-use ledger 不是该
  H4 atomic edge 的 E1--E5 前提。该结论仅关闭 ownership/ledger 子义务；source/target
  typed validation、terminal priority、serializer 和全局 potential 仍未建立。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
  - type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-single-side-exclusion
  - type-I-path-anchored-atomic-split-complete-excess-admission
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - q-bridge
  - atomic-split
  - source-provenance
  - owner
  - charged-support
  - well-founded-rank
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
    role: persistent-parent-and-unchanged-scope
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
    role: canonical-clean-q-word-and-oriented-endpoint
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-single-side-exclusion
    role: actual-H4-endpoint-is-always-two-sided
  - claim: type-I-path-anchored-atomic-split-complete-excess-admission
    role: atomic-owner-tuple-lcm-charge-and-conditional-contract
  - concept: denominator-escape-state-contract
    role: charged-support-monotonicity-and-edge-local-induction-contract
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_atomic_owner_epoch_locality.py
    role: focused-canonical-owner-and-absorbed-block-controls
visibility: public
last_checked: '2026-08-17'
---

# H4 atomic \(q\)-bridge 的局部 owner 唯一性与无重收费

## 1. 要排除的并不是新的算术分支

actual high H4 endpoint 已经满足

\[
Q_x,Q_y>1,
\qquad p\nmid Q_xQ_y,
\qquad c_q\le p-2.
\tag{1}
\]

因此每个 live nonterminal endpoint 都必须使用 atomic split。已有通用 atomic schema
正确地区分了两件事：同一 action 内不能把双色 payload 拆成两个旧 token；而“跨 action
global one-use”只有在证明把多个 action 的容量**聚合**为一个流或匹配问题时才是额外公理。

本卡证明：H4 clean \(q\)-bridge 的实际 branch 属于后一种情形的反面。它是一个固定 source
上的单候选 action，良基归纳不会同时消费两个 outgoing action，故不需要 global one-use
ledger 来证明该 action 的 ownership 子合同。

## 2. canonical occurrence 是 source 的函数

令 \(S\) 是已经通过 versioned terminal-first prefix 的 legal persistent H4 source，带
内容地址 \(\operatorname{id}(S)\)、charged support \(A\mid K_4\) 和 scope \(\sigma\)。
H4 actual receipt 确定

\[
h=(R_4-1,K_4),
\qquad z=R_4-h,
\qquad q=\frac{(p+1)/2}{((p+1)/2,M_4)}>1.
\tag{2}
\]

clean-q bridge 按素数递增顺序剥离 \(q\) 的完整素因子 word，定向地给

\[
(x_q,y_q)=\left(R_4-\frac zq,\frac zq\right).
\tag{3}
\]

这不是候选菜单：\(q\)、每一个 prefix、被选侧和 (3) 都由原始 source 字段重算。两侧
complete-excess blocks 也唯一：

\[
Q_x=Q_{K_4}(x_q),
\qquad Q_y=Q_{K_4}(y_q).
\tag{4}
\]

于是可取不含 target state id 的 canonical owner tuple

\[
\boxed{
\mathcal O_{H4}=
(\texttt{h4\_atomic\_q\_bridge\_v1},
  \operatorname{id}(S),
  \operatorname{digest}(h,z,q,\text{ordered q-word},x_q,y_q)).
}
\tag{5}
\]

交换 raw pair 的显示方向或重新排列 \(q\) 的素因子都先按 (2)--(3) 归一，因此不能产生
第二个 \(\mathcal O_{H4}\)。single-side exclusion 使 (4) 总是两色非平凡，所以在 H4
branch 内不存在“同一 source 先输出单侧、再输出 atomic”的竞争 owner。

## 3. target support 自动禁止同幂重收费

令 atomic target 的 support 和 carrier 为

\[
M=\operatorname{lcm}(A,Q_x,Q_y),
\qquad K_T=Mc_T.
\tag{6}
\]

这里 \(c_T\) 是 canonical capacity；本节不需要它的具体值。对每个素数 \(\ell\)，若
\(\ell\) 属于 \(Q_x\) 或 \(Q_y\) 的有色 block，则

\[
\nu_\ell(K_T)
\ge\nu_\ell(M)
\ge
\begin{cases}
\nu_\ell(Q_x),&\ell\mid Q_x,\\
\nu_\ell(Q_y),&\ell\mid Q_y.
\end{cases}
\tag{7}
\]

因此相同颜色、相同完整幂的 block 在 target 相对于 \(K_T\) 的 maximal complete-excess
重算中不可能仍是 fresh：它的指数没有超过当前容量。

反过来，若未来无 reset epoch 中某个 \(\ell\)-block \(Q'\) 能通过完整超额门，则

\[
\nu_\ell(Q')>\nu_\ell(K_T)\ge\nu_\ell(M),
\tag{8}
\]

从而

\[
\nu_\ell(\operatorname{lcm}(M,Q'))>\nu_\ell(M).
\tag{9}
\]

它是更高指数的新收费，而不是 (5) 的 owner 重用。任何允许丢弃 \(M\) 的 paid reset
必须由外层势单独验证；它形成新 epoch，不能倒过来使本 edge 需要 global ledger。

## 4. 单 successor 归纳不消费跨边资源

在此 branch 中定义局部 dispatch：先运行既定 terminal/alternate prefix；若它不返回
terminal，则唯一候选就是 (2)--(6) 的 atomic receipt。于是每个 \(S\) 至多有一个
H4-atomic successor \(T\)。

设该 receipt 的其余 E1--E5 guard 已通过。强归纳使用的唯一逻辑步骤是

\[
\operatorname{Sol}(p)\ni u_T
\longmapsto u_S,
\tag{10}
\]

其中 lift 为已定义的恒等映射，并且 \(\Pi(T)<\Pi(S)\)。它不会把另一个 source state 的
payload、也不会把一个未选择的 outgoing candidate 加入同一容量账本。若两个独立 source
state 恰好有数值相同的 raw pair，它们仍由不同的 \(\operatorname{id}(S)\) 和 path digest
给出不同 occurrence；各自的归纳子命题也独立成立。

所以 (5) 的 immutable edge receipt 加上 (7)--(9) 已足以支付 **H4 branch 的 owner
sub-obligation**。声明一个跨 action `owner_fresh` 全局 ledger 既不是 E4 lift 的前提，也
不是这条单 successor 严格边的势比较前提。只有未来的 Fourier/Hall/flow 论证若把多个
source 的物理 carrier 聚合，才必须另行引入那种 ledger。

## 5. 对 T1/T2 的精确影响

这条结果不把 atomic receipt 直接升级为 `verified_edge`。仍需逐 source 完成：

1. persistent H4 source 与完整 raw prefix 的 typed/source validator；
2. target 的 F/G/hit 重分类、scope 连续性和 serializer；
3. terminal/alternate priority 的全部先行检查；
4. 全局 selector 和涵盖 reset 的良基势。

但它删除了一个独立分支：对于 deterministic H4 atomic dispatch，不必再等待
“跨 action one-use registry”才能验证 owner。T2 对任意 raw path 的一般版本仍是开放问题；
这里只证明 actual H4 q-bridge 所需的受限实例。

## 6. 聚焦复现

```bash
PYTHONPATH=reproductions python3 \
  reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_atomic_owner_epoch_locality.py --verify
```

脚本重放 \(q=37\) 与 \(q=11^2\) 两个 H4 atomic fixture 的 canonical q-word、唯一双侧
blocks 和 target lcm support；它验证同一 block 已被 target carrier 吸收，并构造严格更高的
\(\ell\)-adic block 以核对 (9)。它不扫描 state graph、terminal 菜单或历史范围。
