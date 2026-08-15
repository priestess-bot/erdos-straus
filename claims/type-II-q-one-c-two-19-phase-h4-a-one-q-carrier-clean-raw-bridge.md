---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
title: q=1 高 C=2 19 相位 H4 a=1 fresh q-carrier 的清洁 raw bridge 与 pre-root 分派
statement: >-
  在 q=1 high C=2 19 相位的 actual H4 proper-overlap top-capacity a_alt=1 receipt 中，令
  h=gcd(R4-1,K4)<p+1、z=R4-h、w=(p+1)/2、d4=gcd(w,M4)、q=w/d4>1。已有
  H4 handoff 给 q|Q_K4(z)|z 及 p congruent to -1 (mod q)。则 q 与 K4 互素；将 q 的每个素因子
  按其重数从 z 侧剥离，给出一条绑定已有 H4 prefix 的实际 primitive raw word，且其
  端点唯一为 {R4-z/q,z/q}。端点的两个 maximal complete-excess block 给出严格穷尽：
  两块皆空时为 Type I terminal；恰一块非空且 p-free 时满足既有单侧 residual gate；
  两块皆非空且 p-free 时给 path-anchored atomic split 的条件性 E1--E4 payload；含 p
  时精确归为 p-primary residual。对两个 p-free 非终端分支，若其 canonical capacity
  c_q<=p-2，则同一 persistent parent P 的端点秩从 (0,p-1) 严格降到 (0,c_q)；唯一
  留下的容量门是 c_q=p-1，等价于新的 multiplier L_q=-c4 (mod p)。这不把 atomic
  payload 或 raw word 单独登记为 verified edge，也不声称 p-primary/capacity-stutter
  分支为空。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff
  - type-II-q-one-c-two-19-phase-h4-p-primary-small-anchor-renewal
  - type-II-q-one-c-two-19-phase-h4-a-one-fresh-carrier-root-cyclotomic-orthogonality
  - type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
  - type-I-path-anchored-atomic-split-complete-excess-admission
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
  - type-I-formal-full-excess-cycle-or-hit-reduction
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - a-one
  - fresh-carrier
  - raw-path
  - complete-excess-bundle
  - atomic-split
  - source-provenance
  - solution-lift
  - well-founded-rank
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff
    role: actual-H4-q-carrier-and-top-capacity-interface
  - claim: type-II-q-one-c-two-19-phase-h4-p-primary-small-anchor-renewal
    role: actual-small-anchor-raw-prefix-and-proper-overlap-contract
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-fresh-carrier-root-cyclotomic-orthogonality
    role: root-side-no-go-that-forces-pre-root-use-of-q
  - claim: type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
    role: persistent-parent-endpoint-rank
  - claim: type-I-path-anchored-atomic-split-complete-excess-admission
    role: conditional-two-sided-E1-to-E4-and-E5-boundary
  - claim: type-I-bottom-sink-scc-complete-excess-bundle-selector
    role: one-sided-residual-gate
  - claim: type-I-formal-full-excess-cycle-or-hit-reduction
    role: raw-prime-edge-and-terminal-reconstruction
  - concept: denominator-escape-state-contract
    role: typed-guard-solution-lift-and-potential-contract
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_carrier_clean_raw_bridge.py
    role: prime-and-composite-q-focused-raw-bridge-controls
visibility: public
last_checked: '2026-08-16'
---

# H4 \(a=1\) fresh \(q\)-carrier 的清洁 raw bridge

## 1. 入口与目标

保留 actual H4 proper-overlap top-capacity \(a_{\rm alt}=1\) 的全部已有前提。特别地，

\[
K_4=M_4c_4,\qquad pR_4+1=4K_4,\qquad
h=(R_4-1,K_4)<p+1,
\tag{1}
\]

\[
z=R_4-h,\qquad Q=Q_{K_4}(z),\qquad
w=\frac{p+1}{2},\qquad d_4=(w,M_4),\qquad q=\frac w{d_4}>1.
\tag{2}
\]

H4 proper-overlap renewal 与 top-capacity \(a_{\rm alt}=1\) 已给出

\[
q\mid \frac{\operatorname{lcm}(M_4,Q)}{M_4}\mid Q\mid z,
\qquad p\equiv-1\pmod q,
\qquad p\nmid K_4Q.
\tag{3}
\]

此前已证明：把 (3) 只沿 \(a=1\) regeneration 传到 root，不能控制 root capacity。
本卡改在 carrier 仍位于实际 H4 raw node \(\{h,z\}\) 时使用它。结论不是把任意
\(q\mid Q\) 静态重图表为一条边；结论是 \(q\) 本身可被完整地、合法地走成一个
actual raw word。

## 2. fresh carrier 必为 \(K_4\)-clean

### 引理 1（\(q\) 的清洁性）

\[
\boxed{(q,K_4)=1.}
\tag{4}
\]

**证明。** \(w\) 为奇数，故任取 \(\ell\mid q\) 时 \(\ell\ne2\)。由 (3)，
\(\ell\mid z\) 且 \(p\equiv-1\pmod\ell\)。若反设 \(\ell\mid K_4\)，则从
\(pR_4+1=4K_4\) 得

\[
R_4\equiv1\pmod\ell.
\tag{5}
\]

于是 \(\ell\mid(R_4-1,K_4)=h\)。但 \(z=R_4-h\) 随即给

\[
z\equiv1-0\equiv1\pmod\ell,
\tag{6}
\]

矛盾于 \(\ell\mid z\)。逐素数即得 (4)。\(\square\)

这比 \(q\mid Q\) 强：\(Q\) 的其它因子允许已经出现在 \(K_4\) 中、但指数不足；
而 fresh \(q\)-carrier 的每个素因子在 \(K_4\) 中的指数恰为零。

## 3. 完整 \(q\)-word 的实际可达性

写

\[
q=\prod_{\ell}\ell^{a_\ell}.
\tag{7}
\]

从 \(\{h,z\}\) 的 \(z\) 侧按固定的素数递增顺序、每个 \(\ell\) 重复 \(a_\ell\)
次做 raw edge。若已经剥掉 \(d\mid q\)，下一步选 \(\ell\mid q/d\)，则当前 selected
coordinate 是 \(z/d\)。由 (4) 及 \(q\mid z\)，

\[
v_\ell(z/d)\ge1>v_\ell(K_4)=0.
\tag{8}
\]

故这正是 complete-excess raw graph 中允许的素数边。\(m=1\) 的 edge formula 给出

\[
\left\{R_4-\frac zd,\frac zd\right\}
\xrightarrow{\ell}
\left\{R_4-\frac z{d\ell},\frac z{d\ell}\right\}.
\tag{9}
\]

又 \((z,R_4)=(z,h)=1\)，所以每一步的两个坐标仍互素，不发生 gcd reduction。于是
得到一个绑定已有 H4 source/path prefix 的 canonical primitive raw word

\[
\boxed{
\{h,z\}\rightsquigarrow
\{x_q,y_q\}:=
\left\{R_4-\frac zq,\frac zq\right\}.
}
\tag{10}
\]

端点只依赖总乘积 \(q\)，不依赖 (7) 中素因子被执行的顺序；顺序只影响 serializer 的
canonical representation。因而 (10) 不是“存在一个可能的 q-path”，而是已有 H4
receipt 可以实际重放的有限 word。

## 4. 端点的完整分派

在 (10) 处定义唯一 maximal complete-excess 分解

\[
x_q=Q_x\beta_x,\qquad y_q=Q_y\beta_y,
\qquad Q_x=Q_{K_4}(x_q),\quad Q_y=Q_{K_4}(y_q).
\tag{11}
\]

primitive 性给出

\[
(Q_x\beta_x,Q_y\beta_y)=1,\qquad \beta_x\beta_y\mid K_4.
\tag{12}
\]

这给出下表的穷尽分派。这里“payload”只指算术/source gate；是否成为递归输出还要经过
terminal-first、typed reclassification、scope 和 serializer guard。

| 端点条件 | 由 (10)--(12) 得到的对象 | 当前可用结论 |
|---|---|---|
| \(Q_x=Q_y=1\) | \(x_qy_q\mid K_4\) | full-excess sink，交由既有 Type I terminal verifier。 |
| 恰一块非平凡，且 \(p\nmid Q_xQ_y\) | 设非平凡块为 \(Q_x\)。另一侧 \(y_q\mid K_4\)，故 \(y_q\beta_x\mid K_4\) | 既有单侧 complete-excess 的 residual-divisibility gate 通过。 |
| \(Q_x,Q_y>1\)，且 \(p\nmid Q_xQ_y\) | 带颜色的 \((Q_x,Q_y)\) 与同一 raw occurrence | 满足 atomic split schema 的输入；该 schema 只条件性支付 E1--E4。 |
| \(p\mid Q_xQ_y\) | 一般 raw endpoint 的完整 \(p\)-block | 在 abstract taxonomy 中是 p-primary residual；actual H4 域已由后续 endpoint exclusion 排除。 |

第二行的 residual gate 不是额外假设：若 \(Q_y=1\)，则 \(y_q\mid K_4\)；再用
\((y_q,\beta_x)=1\) 与 \(\beta_x\mid K_4\)，便得 \(y_q\beta_x\mid K_4\)。
第三行不能被拆成两个旧单侧 action；它正是既有 atomic split card 所保留的来源边界。

## 5. p-free 分支的 parent-macro 容量门

在表的第二、三行，分别定义

\[
M_q=
\begin{cases}
\operatorname{lcm}(M_4,Q_x),&\text{恰一块非平凡时},\\
\operatorname{lcm}(M_4,Q_x,Q_y),&\text{两块皆非平凡时},
\end{cases}
\tag{13}
\]

\[
L_q=\frac{M_q}{M_4}.
\tag{14}
\]

由于 \(M_4\mid K_4\)，每个完整超额块都使 \(L_q>1\)。该行 p-free 时
\(p\nmid M_q\)，其 canonical capacity 唯一为

\[
c_q=\left\langle c_4L_q^{-1}\right\rangle_p,
\qquad 1\le c_q\le p-1.
\tag{15}
\]

现有 persistent parent 的端点秩是 \(\Lambda_p^\sharp(P)=(0,p-1)\)。故只要 H4
prefix、(10)、表中相应 payload、所有 terminal/typed/serializer guard 及（双侧时）
atomic adapter 都被 verifier 接受，便有

\[
c_q\le p-2
\quad\Longrightarrow\quad
\Lambda_p^\sharp(P)=(0,p-1)>(0,c_q).
\tag{16}
\]

E4 仍为同一 \(4/p\) equation target 上的 identity lift。容量未严格时没有任何
偷换：由 (15)，

\[
\boxed{
c_q=p-1
\quad\Longleftrightarrow\quad
L_q\equiv-c_4\pmod p.
}
\tag{17}
\]

这与把 H4 当作 standalone state 时的 \(c_q<c_4\) 门不同；此处正确比较的是原
persistent parent 与宏的最终端点。双侧分支也不因 (16) 自动成为已登记边：atomic
schema 的 source/target validator、owner 语义和 typed target 仍须逐 receipt 重算。

## 6. 两个固定回执

下表的两行都只是 local H4 arithmetic controls，不声称为 actual H3 \(\Rightarrow\) H4
predecessor；它们逐项核验 (1)--(17)。第二行使 \(q=11^2\)，因此同时核验复合
carrier 的两条连续 raw prime edge。

| \(p\) | \((R_4,K_4,h,q)\) | raw selected sequence | \((Q_x,Q_y)\) | \(L_q\bmod p\) | \(c_q\) |
|---:|---|---|---|---:|---:|
| 73 | \((245719,4484372,2,37)\) | \(245717\to6641\) | \((119539,6641)\) | 70 | 24 |
| 241 | \((7202527,433952252,2,121)\) | \(7202525\to654775\to59525\) | \((3571501,59525)\) | 238 | 80 |

两行都有 \(c_{\rm alt}=p-1,a_{\rm alt}=1\)，端点又都是 p-free 双侧 complete-excess；
因此分别给出条件性 atomic target 的严格 parent-macro capacity。它们验证 bridge 与容量
分派的正控制，不证明 (17) 的 stutter 类为空。

## 7. 范围与新的余项

本卡完成的是一个 pre-root 结构推进：fresh \(q\)-carrier 不能因“可能已经被 \(K_4\)
吸收”而失效，也无需等待它与 root capacity 合流。actual H4 endpoint 的 p-primary 分支
现已由[endpoint p-primary 排除](type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-p-primary-endpoint-exclusion.md)
关闭；尚未关闭的分支精确是：

\[
\boxed{
\text{p-free endpoint with }L_q\equiv-c_4\pmod p
\quad\text{or}\quad
\text{a typed/priority guard intercepts}.
}
\tag{18}
\]

式 (18) 不是 global exit theorem。特别地，本卡没有证明 raw endpoint 一定双侧、
一定 strict，也没有把 local controls 提升为 actual 19-phase predecessor。
它排除的只是此前最基础的障碍：在 actual H4 receipt 中，\(q\) 的完整 raw 使用曾是
未证明的。

## 8. 定向回执

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_carrier_clean_raw_bridge.py --verify
```

回执只重放两个固定整数图表；不扫描素数、分母、历史 selector 或完整 Reach。
