---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-q0-one-second-stutter-unitary-transduction
title: H4 q0=1 双 q bridge 第二 stutter 的 unitary carrier 转导
statement: >-
  在 actual q=1 high C=2 19-phase H4 proper-overlap top-capacity a_alt=1 clean
  q bridge 的 q0=1 双 q endpoint 中，设 second endpoint 的 nonterminal canonical
  multiplier 为 L2=(L0/q^2)E_x2，且它处于唯一 top-capacity stutter
  E_x2=q^2+p*s（s 为带符号整数）。写 T=(pb-1)/2=qU、rho=gcd(q,2U)、
  qhat=q/rho，则新 full-product target 的精确 a-coordinate 为
  a2=qhat/gcd(qhat,s)。若 a2=1，则 rho 是 q 的 unitary divisor：rho divides y2，
  qhat divides x2；因此 rho 与 qhat 不互素会直接排除该 stutter。若 qhat>1，
  qhat 在 x2 侧给出一条绑定原 H4 prefix 的 primitive raw re-entry；若 qhat=1，
  则 q^3 divides Q_K4(z) divides z，原 selected coordinate 有第三条 actual q raw
  word。a2=1 时，若 s=qhat*t，则 b2=b+(2U/rho)t，且
  b2=b-(q*rho)^(-1)t (mod p)，从而 ordinary d=1 residue dispatch 只留下显式的
  three terminal/residual classes。该结论不排除 unitary re-entry 的 p-primary 或
  typed/payload guards，也不证明全局出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-a-one-q0-one-double-q-bridge
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-stutter-a-coordinate-transduction
  - type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
  - type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - a-one
  - q0-one
  - double-q-carrier
  - raw-path
  - complete-excess-bundle
  - capacity-transduction
  - unitary-divisor
  - q-lock
  - solution-lift
  - well-founded-rank
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q0-one-double-q-bridge
    role: actual-second-endpoint-p-free-and-q-squared-capacity-gate
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-stutter-a-coordinate-transduction
    role: full-product-coordinate-and-ordinary-d-one-residue-dispatch
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
    role: clean-q-raw-word-convention
  - claim: type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff
    role: original-top-capacity-full-product-normal-form
  - concept: denominator-escape-state-contract
    role: guarded-strict-handoff-contract
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q0_one_second_stutter_unitary_transduction.py
    role: focused-signed-second-stutter-controls
visibility: public
last_checked: '2026-08-16'
---

# H4 \(q_0=1\) 第二 stutter 的 unitary carrier 转导

## 1. 入口和记号

保留已经建立的 actual H4 proper-overlap top-capacity \(a_{\rm alt}=1\)
\(q_0=1\) 双 \(q\) bridge。特别地，令

\[
w=\frac{p+1}{2}=qd_4,
\qquad
M_{\rm alt}=wT,
\qquad
T=\frac{pb-1}{2},
\qquad
q\mid T,
\tag{1}
\]

其中 \((q,M_4)=(q,K_4)=1\)，并且

\[
q^2\mid L_0\mid Q:=Q_{K_4}(z)\mid z,
\qquad
(x_2,y_2)=\left(R_4-\frac z{q^2},\frac z{q^2}\right),
\qquad
p\nmid x_2y_2.
\tag{2}
\]

第二 endpoint 的 nonterminal support multiplier 是

\[
L_2=\frac{L_0}{q^2}E,
\qquad
E:=E_{x,2}=\frac{Q_{K_4}(x_2)}{(M_4,Q_{K_4}(x_2))}.
\tag{3}
\]

这里只讨论它唯一尚不严格的算术容量情形

\[
E\equiv q^2\pmod p.
\tag{4}
\]

与第一条 \(q\)-bridge 不同，\(q^2\) 不必小于 \(p\)，所以必须保留带符号参数

\[
\boxed{E=q^2+ps,\qquad s\in\mathbb Z.}
\tag{5}
\]

这不是正性假设；canonical support 的正性由实际 endpoint 给出。

由 (1) 写

\[
T=qU,
\qquad
\rho=(q,2U)=(q,U),
\qquad
\widehat q=\frac q\rho.
\tag{6}
\]

最后一个 \((q,2U)=(q,U)\) 使用 \(q\mid w\) 且核心域使 \(q\) 为奇数。

## 2. 第二顶容量 target 的精确坐标

由 (1)、(6)，

\[
M_{\rm alt}=q^2d_4U,
\qquad
m_2:=\frac{M_{\rm alt}}{q^2}=d_4U.
\tag{7}
\]

将 (3)、(5) 代入，得到

\[
M_2:=M_4L_2=m_2E=M_{\rm alt}+pm_2s.
\tag{8}
\]

因此它仍是 full-product \(d=1\) 行：

\[
4M_2+1=p n_2,
\qquad
\boxed{n_2=n+4m_2s.}
\tag{9}
\]

这里 \(M_2>0\) 保证 \(n_2>0\)，而 \(p\equiv1\pmod4\) 给
\(n_2\equiv1\pmod4\)。令该行的通常坐标为

\[
a_2=\frac{w}{\left(w,(n_2+1)/2\right)}.
\tag{10}
\]

由 \((n+1)/2=wb\)、(6)--(9)，

\[
\begin{aligned}
\frac{n_2+1}{2}
 &=wb+2d_4Us
 =d_4(qb+2Us),\\
a_2
 &=\frac q{(q,2Us)}
 =\boxed{\frac{\widehat q}{(\widehat q,s)}}.
\end{aligned}
\tag{11}
\]

所以所有第二 stutter 有一个精确的首层分派：

\[
\widehat q\nmid s
\Longrightarrow a_2>1.
\tag{12}
\]

在 target 的 terminal-first、typed、source/path、serializer 与 persistent guards
通过时，(12) 可接入已有 \(a>1\) \(d=1\) strict handoff；本卡不把这条条件性接入
自动登记为 global edge。

## 3. \(a_2=1\) 强制 unitary carrier 分派

现在设 \(a_2=1\)，等价于 \(\widehat q\mid s\)。由 (5) 和
\((p,\widehat q)=1\)，

\[
\widehat q\mid E.
\tag{13}
\]

又 \((\widehat q,M_4)=1\)，所以 (3) 的 maximal complete-excess 定义给

\[
\boxed{\widehat q\mid Q_{K_4}(x_2)\mid x_2.}
\tag{14}
\]

另一方面 \(\rho\mid U\)。由 (7) 及 \((q,M_4)=1\)，有

\[
q^2\rho\mid M_{\rm alt}
\Longrightarrow
q^2\rho\mid L_0
\Longrightarrow
q^2\rho\mid Q\mid z.
\tag{15}
\]

将 (15) 除以 (2) 中的 \(q^2\)，得到

\[
\boxed{\rho\mid y_2.}
\tag{16}
\]

双 \(q\) bridge 的 primitive 性给 \((x_2,y_2)=1\)。由 (14)、(16)，

\[
\boxed{(\rho,\widehat q)=1.}
\tag{17}
\]

也就是说，记 \(\rho\parallel q\) 表示 \(\rho\mid q\) 且
\((\rho,q/\rho)=1\)，则

\[
\boxed{a_2=1\Longrightarrow\rho\parallel q.}
\tag{18}
\]

这是一个真实的排除门：若由原 \(T\) 给出的 \(\rho\) 不是 \(q\) 的 unitary divisor，
则 (18) 与 \(a_2=1\) 矛盾，故全部 second stutter 自动落入 (12) 的 \(a_2>1\)
分派。它不是把 composite \(q\) 的不同素因子错误地视为同一个二选一标签。

## 4. 两个实际 raw 后继

式 (18) 留下两种、且只有两种 carrier 几何。

### 4.1 \(\widehat q>1\)：x-side re-entry

由 (14)，\(\widehat q\) 的每个素因子及完整重数都属于 \(x_2\) 的 complete-excess
block；它们又不整除 \(K_4\)。同时 \((x_2,R_4)=1\)。因此可逐素数实际重放 primitive
raw word

\[
\boxed{
\{x_2,y_2\}
\rightsquigarrow
\left\{\frac{x_2}{\widehat q},R_4-\frac{x_2}{\widehat q}\right\}.
}
\tag{19}
\]

它绑定原 H4 prefix，不依赖把 (8) 的 abstract target 先注册为已接受状态。\(\rho\)
同时仍位于 \(y_2\) 一侧，且 (17) 保证两侧 carrier 支撑不重叠。新 endpoint 的
\(p\)-primary、terminal-first、typed 与 payload guards 必须独立重算。

### 4.2 \(\widehat q=1\)：第三条 y-side \(q\)-word

此时 \(\rho=q\)，所以 \(q\mid U\)。式 (7)、(15) 加强为

\[
q^3\mid L_0,
\qquad q^3\mid Q\mid z.
\tag{20}
\]

所以原 selected coordinate 不是停在双 bridge，而是有第三条实际 primitive \(q\)-word：

\[
\boxed{
\{h,z\}
\rightsquigarrow
\{x_1,y_1\}
\rightsquigarrow
\{x_2,y_2\}
\rightsquigarrow
\left\{R_4-\frac z{q^3},\frac z{q^3}\right\}.
}
\tag{21}
\]

本卡只证明它存在；第三 endpoint 的 \(p\)-primary 排除不是 (21) 的自动后果。

## 5. \(a_2=1\) target 的显式 \(b\)-residue 图

设 \(a_2=1\)，并写

\[
s=\widehat q t,
\qquad
B_2=\frac{2U}{\rho}.
\tag{22}
\]

由 (11) 可知 \(w\mid(n_2+1)/2\)，所以 \(b_2=(n_2+1)/(p+1)\) 是正奇整数。
直接代入 (9) 得

\[
\boxed{b_2=b+B_2t.}
\tag{23}
\]

而

\[
q\rho B_2=2qU=2T=pb-1,
\tag{24}
\]

故 \(q\rho\) 在模 \(p\) 下可逆，并且

\[
\boxed{b_2\equiv b-(q\rho)^{-1}t\pmod p.}
\tag{25}
\]

这把所有仍在 \(a=1\) 的 second stutter 变成 existing ordinary \(d=1\) dispatch
的三条具名接口：

| \(t\pmod p\) | \(b_2\pmod p\) | ordinary \(d=1\) 处理 |
|---:|---:|---|
| \(q\rho b\) | \(0\) | raw \(p\)-source repair |
| \(q\rho(b+1)\) | \(-1\) | p-free failure/root interface |
| \(q\rho(b+2)\) | \(-2\) | canonical regeneration |
| 其它 | 其它 | canonical capacity 严格 |

表中的路由仍受各自既有 guards 约束。其价值是：第二 \(q^2\)-stutter 不再是一个无结构的
同容量回路，而是先经 (12)、(18)--(21) 的 actual carrier 门，再经 (25) 的有限 residue
接口。

## 6. 边界和定向回执

本卡没有证明 (19) 的 re-entry endpoint p-free，也没有证明 (21) 的第三 endpoint
p-free；更没有自动支付 single-side/atomic payload 的 E1--E4。它给出的新全称进展是
second stutter 的单位因子容量图，以及 non-unitary \(\rho\) 时 \(a=1\) stutter 的
直接不可能性。

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q0_one_second_stutter_unitary_transduction.py --verify
```

回执使用已有 \(p=73\) local H4 arithmetic skeleton 验证带符号 (5)、(9)、(11)、(23)--(25)，
并以小整数控制检查 proper-unitary、non-unitary contradiction 和 third-carrier 分支；它不
构造 actual stutter endpoint、不扫描素数范围，也不检查历史 Reach。
