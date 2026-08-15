---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff
title: q=1 高 C=2 19 相位 H4 proper-overlap 顶容量的 d=1 handoff 与 a=1 root-fan 残余
statement: >-
  在 q=1 high C=2 19-phase 的 actual persistent H4 receipt 中，设 R4=1 (mod p)，
  真实 p-primary peeling 与容量剥离到达 proper-overlap h<p+1，并以 p-free clean
  bundle Q 产生 M_alt=lcm(M4,Q) 和 c_alt=p-1。则 M_alt=(p n_alt-1)/4、
  R_alt=(p-1)n_alt-1，其中 n_alt>1、n_alt=1 (mod 4)，故是合法 full-product d=1
  state。写 (p+1)/2=g a_alt、(n_alt+1)/2=g b_alt、(a_alt,b_alt)=1。若 a_alt>1，
  则 d=1 regeneration countdown、raw-source repair 与 p-free small-anchor handoff
  在有限步后产生 residual capacity <=p-2；在所有 checkpoint 的 terminal-first、typed、
  source/path 与 serializer guards 通过时，它与现有 P=>H4 prefix 合成为从
  Lambda(P)=(0,p-1) 到 (0,c_T) 的 strict guarded macro，并以 Sol(p) identity lift
  提升全域解。对 a_alt=1，令 E0=(p-1)b_alt-1、eta=nu_p(E0-1)、并取 E0-1 的
  首个非零 p-adic digit omega；恰作 eta 次 d=1 regeneration 后，omega=-2 由
  least-coprime source repair 严格离开，omega 不等于 -1,-2 时直接严格离开；只有
  omega=-1 到达 p-free root return b_*=2pr-1。令
  u=gcd(2r+1,(p^2+p+1)/3)，则 9u^2<p 时已有真实 root-fan path 给 terminal
  certificate 或 p-free strict carry。因此，在已准入 suffix 中尚未由这些规则强制
  关闭的必要算术条件缩为 omega=-1 与 9u^2>=p。独立地，令
  d4=gcd((p+1)/2,M4) 与 q=(p+1)/(2d4)，则 a_alt=1 强迫 q>1、
  q|M_alt/M4、q|Q 与 q|(R4-h)，并有 4K4≡1-h (mod q)；q 是 H4 small-anchor
  renewal 新注入的 w-carrier，而非旧 H4 support。该卡不声称这个残余必为空、必无
  terminal，或已经给出全局出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-p-primary-small-anchor-renewal
  - type-II-q-one-c-two-19-phase-h4-full-overlap-predecessor-exclusion
  - type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
  - type-I-overflow-full-product-d-one-p-adic-regeneration-countdown
  - type-I-overflow-full-product-d-one-p-free-peeled-small-anchor
  - type-I-overflow-full-product-d-one-a-one-regeneration-return-digit-normal-form
  - type-I-overflow-full-product-d-one-a-one-root-coprime-capacity-fan-half-descent
  - type-I-chart-least-coprime-prime-anchor-source
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - proper-overlap
  - top-capacity
  - full-product
  - d-one
  - p-adic-regeneration
  - terminal-digit
  - root-capacity-fan
  - root-residual
  - small-anchor
  - fresh-carrier
  - guarded-macro
  - solution-lift
  - well-founded-descent
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-p-primary-small-anchor-renewal
    role: actual-proper-overlap-renewal-and-top-normal-form
  - claim: type-II-q-one-c-two-19-phase-h4-full-overlap-predecessor-exclusion
    role: actual-phase-p-free-proper-overlap-domain
  - claim: type-I-overflow-full-product-d-one-p-adic-regeneration-countdown
    role: full-product-d-one-countdown-and-strict-rank
  - claim: type-I-overflow-full-product-d-one-p-free-peeled-small-anchor
    role: a-greater-than-one-terminal-p-free-exit
  - claim: type-I-overflow-full-product-d-one-a-one-regeneration-return-digit-normal-form
    role: a-one-terminal-digit-classification
  - claim: type-I-overflow-full-product-d-one-a-one-root-coprime-capacity-fan-half-descent
    role: admitted-p-free-root-return-small-fan-exit
  - claim: type-I-chart-least-coprime-prime-anchor-source
    role: raw-source-failure-repair
  - concept: denominator-escape-state-contract
    role: guarded-E1-to-E5-composition
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_proper_overlap_top_capacity_handoff.py
    role: d-one-normal-form-and-a-split-controls
visibility: public
last_checked: '2026-08-16'
---

# H4 proper-overlap 顶容量的 d=1 handoff

## 1. actual p-free renewal 的顶端是已有正规形

设 actual H4 p-primary receipt 已满足 \(R_4\equiv1\pmod p\)。经过真实 \(p\)-block
peeling 和同侧容量剥离，它到达 proper overlap

\[
h=(R_4-1,K_4)<p+1,
\qquad z=R_4-h,
\tag{1}
\]

并产生 path-anchored p-free complete-excess bundle \(Q\)。H4 full-overlap 实际前驱排除
保证 (1) 在本 19-phase receipt 域中总成立。写

\[
M_{\rm alt}=\operatorname{lcm}(M_4,Q),
\qquad
c_{\rm alt}\equiv c_4(M_{\rm alt}/M_4)^{-1}\pmod p.
\tag{2}
\]

现在只讨论顶容量分支 \(c_{\rm alt}=p-1\)。因为 \(M_{\rm alt}>M_4>B_p\) 且
\(4M_{\rm alt}\equiv-1\pmod p\)，定义

\[
n_{\rm alt}=\frac{4M_{\rm alt}+1}{p}.
\tag{3}
\]

则

\[
\boxed{
n_{\rm alt}>1,\qquad n_{\rm alt}\equiv1\pmod4,
\qquad M_{\rm alt}=\frac{pn_{\rm alt}-1}{4},
\qquad R_{\rm alt}=(p-1)n_{\rm alt}-1.
}
\tag{4}
\]

故它不是新的 H4 特有图表，而是完整乘积 \(d=1\) 饱和行。proper-overlap 的 p-free
性质还给出 \(p\nmid M_{\rm alt}\)，所以 (4) 可进入既有的 d=1 state contract。

## 2. 顶容量按 a-coordinate 精确分派

写

\[
\alpha=\frac{p+1}{2}=g a_{\rm alt},
\qquad
v=\frac{n_{\rm alt}+1}{2}=g b_{\rm alt},
\qquad
(a_{\rm alt},b_{\rm alt})=1.
\tag{5}
\]

完整乘积正规形给出

\[
a_{\rm alt}=1
\quad\Longleftrightarrow\quad
\frac{p+1}{2}\mid M_{\rm alt}.
\tag{6}
\]

若 \(a_{\rm alt}>1\)，既有 d=1 handoff 的两个全称算术结论可逐项适用：

1. 若 canonical multiplier 不是 regeneration residue，目标容量立即为 \(\le p-2\)；
2. 若它是 regeneration residue，\(\eta=\nu_p(E-1)\) 每步恰减一，故有限步后离开
   regeneration；
3. 终行的 raw-source failure 由最小互素素数 source 同锚修复；终行的 p-free failure
   由真实 p-primary peeling--small-anchor route 产生 p-free bundle，且 \(a_{\rm alt}>1\)
   全称排除新的 top-capacity stutter。

于是存在一个有限 suffix 的终点 \(T\)，满足

\[
\boxed{c_T\le p-2.}
\tag{7}
\]

这一步不是把 generic theorem 静态贴到 H4 图表：其起点 (4) 已由 (1)--(3) 给出实际
path-anchored receipt，且每个 d=1 checkpoint 必须重新运行 terminal-first、typed
reclassification、source/path 与 serializer guards。

## 3. \(a_{\rm alt}>1\) 与 persistent parent 的严格宏复合

令 \(P\) 是已有 q=1 high \(C=2\) persistent parent。其端点势为

\[
\Lambda_p^\sharp(P)=(0,p-1).
\tag{8}
\]

在 H4 renewal、(4) 以及通向 \(T\) 的每个 d=1 suffix checkpoint 都通过 guards 时，
宏的合同为：

| 合同 | 回执 |
|---|---|
| E1 | 既有 \(P\Rightarrow H4\) prefix；H4 p-peeling/capacity raw word；以及 d=1 suffix 的实际 source/path。 |
| E2 | (2)--(5) 的 lcm、canonical capacity 和 full-product normal form；每步 regeneration 或 small-anchor target 的重算。 |
| E3 | 每个 checkpoint 的 terminal-first、typed reclassification、state id、scope 和 serializer payload。 |
| E4 | 所有状态都是同一 \(4/p\) equation target，故 \(\operatorname{Sol}(p)\) 的 identity map 给出全域解提升。 |
| E5 | 由 (7)--(8)，\((0,p-1)>(0,c_T)\)。 |

所以 \(a_{\rm alt}>1\) 是一个真正的 strict guarded macro，而非单独顶容量 state 的
rank stutter。

## 4. \(a_{\rm alt}=1\) 的有限终类与 root-fan 出口

现在设 \(a_{\rm alt}=1\)。令

\[
E_0=(p-1)b_{\rm alt}-1,
\qquad
\eta=\nu_p(E_0-1),
\qquad
\omega\equiv\frac{E_0-1}{p^\eta}\pmod p.
\tag{9}
\]

把 \(b_\ast\) 记为恰作 \(\eta\) 次 canonical \(d=1\) regeneration 后的参数；
\(\eta=0\) 时这是空操作。每一步都保留 \(a=1\)，并使 \(\nu_p(E-1)\) 恰减一，故末态

\[
E_\ast=(p-1)b_\ast-1\equiv1+\omega\pmod p.
\tag{10}
\]

这里 \(\omega\ne0\) 是 \(\eta\) 的极大性直接给出的。因此，在每个再生 checkpoint 的
terminal-first、typed、source/path 与 serializer guards 都通过的前提下，末态只有三类：

| \(\omega\pmod p\) | 末态 | 已有出口 |
|---|---|---|
| \(-2\) | \(E_\ast\equiv-1,\ b_\ast\equiv0\) | 最小互素素数 source repair 给 strict carry |
| \(-1\) | \(E_\ast\equiv0,\ b_\ast\equiv-1\) | 进入真实 \(p\)-free root return |
| 其它 | \(E_\ast\not\equiv0,-1,1\) | canonical capacity \(c\le p-2\) |

第一、三行不留下顶容量。第二行中，\(n_\ast=(p+1)b_\ast-1\equiv1\pmod4\)，而
\(p+1\equiv2\pmod4\)，所以 \(b_\ast\) 为奇数。又 \(b_\ast\equiv-1\pmod p\)，唯一地写为

\[
b_\ast=2pr-1,\qquad r\ge1.
\tag{11}
\]

此时 full-product 行正是既有 \(a=1\) root interface。令

\[
M_{\rm root}=\frac{p^2+p+1}{3},
\qquad
u=(2r+1,M_{\rm root}).
\tag{12}
\]

其真实根容量为 \(3u\)。若

\[
9u^2<p,
\tag{13}
\]

则已有 actual capacity path 到 \(h=3u\)，小 endpoint dispatch 给出 bottom Type I
terminal certificate 或 p-free strict carry \(c\le p-2\)。特别地，\(u=1\) 时该条件对
所有核心素数自动成立；写

\[
H=\frac{3p+1}{4},\qquad w_3=(r-3,H),
\tag{14}
\]

便有显式 receipt

\[
(h,E,D,c)=\left(3,\frac{(R-3)/4}{w_3},4w_3,\langle2w_3\rangle_p\right),
\qquad c\le\frac{p+1}{2}<p-1.
\tag{15}
\]

因此，(9)--(15) 并没有把所有 \(a_{\rm alt}=1\) 静态图表宣称为已关闭；它给出的精确
结论是：在已准入 H4 suffix 中，若当前这些路由均未产生 terminal 或 strict macro，则必有

\[
\boxed{\omega\equiv-1\pmod p,\qquad 9u^2\ge p.}
\tag{16}
\]

这只是现有路由的必要残余条件，不断言满足 (16) 的 state 真正可达或没有别的短证书。

## 5. \(a_{\rm alt}=1\) 的 fresh \(w\)-carrier 映射

若 \(a_{\rm alt}=1\)，则由 (6) \(w=(p+1)/2\mid M_{\rm alt}\)。这不蕴含
\(w\mid K_4\)：一般 H4 local chart 已有 proper-overlap、\(c_{\rm alt}=p-1\)、
\(a_{\rm alt}=1\) 的正控制。因此不能把刚排除的原 H4 full-overlap 偷换为此处的
full-product return。

令

\[
d_4=(w,M_4),\qquad q=\frac w{d_4},
\qquad L=\frac{M_{\rm alt}}{M_4}=\frac{Q}{(M_4,Q)}.
\tag{17}
\]

因为 \((M_4/d_4,w/d_4)=1\)，由 \(w\mid M_4L\) 得

\[
\boxed{q\mid L\mid Q\mid z=R_4-h.}
\tag{18}
\]

H4 full-overlap 实际前驱排除给出 \(w\nmid K_4\)，从而 \(w\nmid M_4\)、\(q>1\)。
又 \(q\mid w\) 使 \(p\equiv-1\pmod q\)。结合 (18) 和
\(pR_4+1=4K_4\)，得到精确同余

\[
\boxed{4K_4\equiv1-h\pmod q.}
\tag{19}
\]

在实际 H3 \(\Rightarrow\) H4 provenance 中已有
\(d_4\mid\Delta=\lvert1536-a(p)\rvert\)。同一 31-selector fixed-menu receipt 已显式核验
\(\Delta>0\)，故这个新的 carrier 至少有尺度

\[
q=\frac w{d_4}\ge\frac{p+1}{2\Delta}.
\tag{20}
\]

式 (18)--(20) 是 \(a_{\rm alt}=1\) 对原 H4 receipt 的完整可见部分：缺失的
\(w\)-carrier 不是通过原 \(K_4\) full-overlap 出现，而是作为 \(z\) 侧 complete-excess 的
新高度进入 \(Q\)。它解释了为何 H5 的 \(w\mid K_4\) 有限筛不能直接重用，也给后续
寻找 q-carried short certificate 或合法 split-carrier exit 一个明确的、实际路径锚定的
输入。

必须区分两件事：(18)--(20) 是 actual H4 renewal 入点的全称约束；(12)--(16) 是它经过
\(d=1\) suffix 后的终端 root 条件。当前没有证明 \(q\) 在 regeneration 中保留到 \(u\)，
所以不把两者误写成同一个 carrier theorem。

## 6. 当前保留的精确接口

在 actual H3 \(\Rightarrow\) H4 provenance、proper-overlap renewal 与所有已声明 guards
都通过的域内，当前路由未强制给 strict macro 的唯一候选已缩为

\[
\boxed{
c_{\rm alt}=p-1,\qquad a_{\rm alt}=1,\qquad
\omega\equiv-1\pmod p,\qquad 9u^2\ge p.
}
\tag{21}
\]

式 (21) 仍须逐 state 执行 terminal-first；它也不说明该集合非空。它的价值是把下一步的
研究对象从整个 \(a_{\rm alt}=1\) return 精确缩为 large root-capacity layer，并保留 (18)--(20)
所给的 independent fresh-carrier receipt。

## 7. 定向回执

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_proper_overlap_top_capacity_handoff.py --verify
```

回执核对一个 \(a>1\) 的直接严格 d=1 行、一个 \(a>1\) 的 p-free small-anchor
handoff、一个 \(c_4=1\) 局部 H4 图表中的 \(q\)-carrier 特化，以及一个经一次 \(a=1\)
regeneration 后进入 \(u=1\) root-fan 严格出口的通用 d=1 控制。后两个控制不是 actual
19-phase H3 predecessors，也不扫描素数或分母。
