---
kind: claim
claim_id: type-I-root-capacity-stutter-transverse-pure-t-p-free-root-expulsion
title: 横向 pure-T excess 的 p-free 根锚 q-排出
statement: >-
  对 actual L>1 low-gap negative-root pure-T-side complete-excess，令 q|D*、
  epsilon=v_q(E)>0、delta=v_q(D)，并若 endpoint multiplier 满足
  E=1+p^2 t（等价于 sigma=0 mod p）。p-free return 给出 K_1=EK，及重入根锚
  h_1=p+1 的容量 D_root=gcd(R_1-p-1,K_1)|p^2+p+1。所有四个 low gap
  s∈{3,7,11,23} 都强制 q 不整除 p^2+p+1；故 q 不整除 D_root，且
  q 不整除 R_1-(p+1)。另一方面 v_q(K_1)=delta+epsilon>0，且 q 不整除 p+1。
  因此 pure-T complete-excess 的 q-primary 高度在 p-free 回返后仍在全局状态容量
  K_1 中，却不会作为重入根锚两侧的 root-capacity residual 延续。这是一个精确的
  residual-persistence 排出结论；它不构造 Type I/II 证书、identity lift 或全局势。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-transverse-negative-branch-bezout-reflection-terminal
  - type-I-root-capacity-stutter-transverse-pure-t-complete-excess-relay
  - type-I-overflow-full-product-d-one-a-one-endpoint-s-zero-p-free-return
topics:
  - type-I
  - root-capacity
  - stutter
  - transverse-residual
  - negative-branch
  - pure-T-side
  - complete-excess
  - p-free-return
  - q-adic
  - persistence
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-transverse-negative-branch-bezout-reflection-terminal
    role: low-gap-negative-root-L-and-pure-T-data
  - claim: type-I-root-capacity-stutter-transverse-pure-t-complete-excess-relay
    role: q-excess-capacity-height-in-K
  - claim: type-I-overflow-full-product-d-one-a-one-endpoint-s-zero-p-free-return
    role: p-free-return-and-root-box-divisibility
  - reproduction: reproductions/type_i_root_capacity_stutter_transverse_pure_t_complete_excess_relay.py
    role: finite-low-gap-root-box-and-q-primary-p-free-return-controls
visibility: public
last_checked: '2026-08-14'
---

# 横向 pure-\(T\) excess 的 \(p\)-free 根锚 \(q\)-排出

## 1. 低缺口负根不能落入 Eisenstein 根盒

设 \(q\) 是一个 \(L>1\) low-gap negative-root carrier。沿用

\[
s\in\{3,7,11,23\},
\qquad
q=s(L+1)-1,
\qquad
Lp\equiv1\pmod q.
\tag{1}
\]

记

\[
N=p^2+p+1.
\tag{2}
\]

这里 \(q\nmid L\)，否则 (1) 的最后一个同余不可能成立。若反设 \(q\mid N\)，
以 \(L^2\) 乘 \(p^2+p+1\equiv0\pmod q\)，得到

\[
L^2+L+1\equiv0\pmod q.
\tag{3}
\]

另一方面，由 \(q=s(L+1)-1\) 有 \(sL\equiv1-s\pmod q\)。故 (3) 以 \(s^2\)
相乘后给出

\[
q\mid s^2-s+1.
\tag{4}
\]

但四个允许 gap 的有限核为

| \(s\) | \(s^2-s+1\) | 素因子在模 \(2s\) 下的剩余 | 所需 \(q\equiv-1\pmod {2s}\) |
| ---: | ---: | --- | --- |
| \(3\) | \(7\) | \(7\equiv1\pmod6\) | \(5\pmod6\) |
| \(7\) | \(43\) | \(43\equiv1\pmod{14}\) | \(13\pmod{14}\) |
| \(11\) | \(111=3\cdot37\) | \(3,15\pmod{22}\) | \(21\pmod{22}\) |
| \(23\) | \(507=3\cdot13^2\) | \(3,13\pmod{46}\) | \(45\pmod{46}\) |

没有一行允许这样的奇素数 \(q\)。因此

\[
\boxed{q\nmid p^2+p+1.}
\tag{5}
\]

这条排除只用低缺口负根的精确同余，不把 \(q\) 当作任意根盒因子。pure-T
分派还给出 \(q\nmid p^2-1\)，所以特别有

\[
q\nmid p+1.
\tag{6}
\]

## 2. \(p\)-free 回返时的残余排出

现在附加 actual pure-T complete-excess 条件。记

\[
\delta=v_q(D),
\qquad
\epsilon=v_q(E)>0.
\tag{7}
\]

complete-excess 分型和 pure-T 容量定位给出

\[
v_q(K)=\delta.
\tag{8}
\]

考察唯一的 checkpoint p-free suffix：

\[
E=1+p^2t,
\qquad t>0.
\tag{9}
\]

既有 p-free return 的精确正规形给出

\[
K_1=EK,
\qquad
D_{\mathrm{root}}=(R_1-p-1,K_1)\mid N.
\tag{10}
\]

于是 (5)、(7)--(10) 立即给出

\[
\boxed{
v_q(K_1)=\delta+\epsilon>0,
\qquad
q\nmid D_{\mathrm{root}}.}
\tag{11}
\]

后一个结论可在 root-anchor 的整数层加强。由 \(4K_1=pR_1+1\) 和 \(q\mid K_1\)，
模 \(q\) 有

\[
p\bigl(R_1-(p+1)\bigr)
\equiv-(p^2+p+1)=-N\pmod q.
\tag{12}
\]

结合 (5) 与 \(q\nmid p\)，得到

\[
\boxed{q\nmid R_1-(p+1).}
\tag{13}
\]

由 (6) 还知 \(q\nmid p+1\)。所以在重入的根锚对

\[
\{p+1,\ R_1-(p+1)\},
\tag{14}
\]

中，\(q\) 不在任一节点侧的 root-capacity residual 上；但 (11) 表明它没有从状态的
\(K_1\) 中消失。准确说，这是一次从 root-capacity **位置**的排出，而不是对 \(q\)
因子的删除。

## 3. 对全局路线的含义与边界

该结果为难的 \(E\equiv1\pmod {p^2}\) 类增加了一个严格的不可持久性约束：一个原
pure-T complete-excess carrier \(q\) 不能仅沿 p-free 回返后根锚的对侧容量
继续作为同一 residual。若它以后再次成为 unresolved root residual，必须在后续
actual path 中获得新的节点/receipt provenance；不能把 \(D_{\mathrm{root}}\) 误认成
原 \(q\)-height 的延续。

这仍**不**推出 terminal 或严格下降。\(q\) 仍整除 \(K_1\)，并且现有 p-free return
可以有饱和根盒和长的 raw/capacity 轨道。要把排出升级为 global exit，还必须证明
这种重新播种必触发已有 Type I/II menu、受限的 source-switch，或一个有 identity lift
的良基递降边。

## 4. 聚焦复现

~~~bash
python3 reproductions/type_i_root_capacity_stutter_transverse_pure_t_complete_excess_relay.py --verify
~~~

脚本固定核对四个 \(s^2-s+1\) 的低 gap 有限例外表，并在
\((p,q,r,t)=(313,17,15,9)\) 的 q-primary/p-free 兼容控制上重放
\(K_1=EK\)、\(D_{\mathrm{root}}\mid p^2+p+1\)、\(q\mid K_1\) 以及
\(q\nmid D_{\mathrm{root}}\)。后一个控制不冒充 actual root receipt；它只复现本引理
所需的 p-free return 与 q-primary 整数层。
