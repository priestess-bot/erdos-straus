---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-stutter-a-coordinate-transduction
title: H4 q-bridge stutter 的 a 坐标转导、两类正残余、raw-p-source 修复与 q0 raw re-entry
statement: >-
  在 actual H4 proper-overlap top-capacity a_alt=1 的 clean q bridge 中，设 q-word endpoint
  的唯一 arithmetic stutter 满足 E_x=q (mod p)，写 E_x=q+ps。令原 d=1
  top-capacity 行为 M_alt=(pn-1)/4，且 n=(p+1)b-1；再令 gamma=gcd(q,b+1) 与
  q0=q/gamma。则 q bridge 的 canonical target 是同一类 d=1 top-capacity 行，参数
  n_q=n+4(M_alt/q)s，且其精确 a 坐标为
  a_q=q0/gcd(q0,s)。故 s>0 且 q0 不整除 s 时，target 进入已有 a>1 strict handoff。
  若 s=q0 t>0，则 target 仍为 a=1，b_q=b+((pb-1)/gamma)t。t=gamma b (mod p) 的
  raw-p-source 由最小互素素数 source 严格修复到 cofactor 1；其它一般 t 也立即给出
  严格 canonical capacity。只剩 t=gamma(b+1) (mod p) 的 p-free failure，或
  t=gamma(b+2) (mod p) 的 regeneration 且其首个非零 p-adic digit 为 -1，这两类正
  residual 通道。此 a=1 分支还强制 q0|E_x|Q_x|x_q；当 q0>1 时，q0 的每个素因子可从
  x_q 侧实际重放为一条 primitive raw word。该结果保留 s=0 的同 support stutter、两类
  正 residual 与所有 typed/atomic adapter guards，未声称 global exit。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-complete-excess-stutter-reduction
  - type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-p-primary-endpoint-exclusion
  - type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff
  - type-I-overflow-full-product-d-one-p-adic-regeneration-countdown
  - type-I-overflow-full-product-d-one-a-one-regeneration-return-digit-normal-form
  - type-I-overflow-full-product-d-one-p-free-peeled-small-anchor
  - type-I-chart-least-coprime-prime-anchor-source
  - type-I-path-anchored-atomic-split-complete-excess-admission
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
  - carry-stutter
  - p-adic-regeneration
  - capacity-transduction
  - source-provenance
  - well-founded-rank
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-complete-excess-stutter-reduction
    role: exact-stutter-gate-and-q-bridge-target-multiplier
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
    role: actual-clean-q-word-and-primitive-endpoint
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-p-primary-endpoint-exclusion
    role: endpoint-p-free-domain-for-d-one-reclassification
  - claim: type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff
    role: original-d-one-a-one-top-capacity-normal-form-and-a-greater-than-one-handoff
  - claim: type-I-overflow-full-product-d-one-p-adic-regeneration-countdown
    role: ordinary-d-one-residue-dispatch
  - claim: type-I-overflow-full-product-d-one-a-one-regeneration-return-digit-normal-form
    role: terminal-digit-classification-of-the-regeneration-cell
  - claim: type-I-overflow-full-product-d-one-p-free-peeled-small-anchor
    role: a-greater-than-one-strict-suffix
  - claim: type-I-chart-least-coprime-prime-anchor-source
    role: raw-p-source-strict-repair
  - claim: type-I-path-anchored-atomic-split-complete-excess-admission
    role: conditional-target-admission-and-guard-boundary
  - concept: denominator-escape-state-contract
    role: terminal-typed-lift-and-potential-contract
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_stutter_a_coordinate.py
    role: static-d-one-transduction-controls
visibility: public
last_checked: '2026-08-16'
---

# H4 \(q\)-bridge stutter 的 \(a\) 坐标转导

## 1. 设置与范围

保留 actual H4 proper-overlap top-capacity \(a_{\rm alt}=1\) clean \(q\)
bridge 的全部前提。此前已经证明，\(q\)-word 的 endpoint

\[
(x_q,y_q)=\left(R_4-\frac zq,\frac zq\right)
\tag{1}
\]

是绑定 H4 prefix 的 primitive raw endpoint，且所有非 terminal 的 arithmetic
capacity stutter 恰为

\[
Q_x>1,
\qquad
E_x:=\frac{Q_x}{(M_4,Q_x)}\equiv q\pmod p.
\tag{2}
\]

这里 \(q\mid(p+1)/2<p\)，而原 renewal 的 top-capacity d=1 行可唯一写为

\[
M_{\rm alt}=\frac{pn-1}{4},
\qquad
n=(p+1)b-1,
\qquad b\equiv1\pmod2.
\tag{3}
\]

令

\[
\gamma=(q,b+1),
\qquad q_0=\frac q\gamma,
\qquad m=\frac{M_{\rm alt}}q.
\tag{4}
\]

式 (4) 有意义：此前的 fresh-carrier handoff 给 \(q\mid
M_{\rm alt}/M_4\)，故 \(q\mid M_{\rm alt}\)。为避免符号混淆，\(\gamma\)
不是原 raw bundle 中的 \(\delta\)。

本卡只分析 (2) 的**算术**后果。无论 endpoint 是单侧 payload 还是双色 atomic
payload，它要成为 persistent macro 仍须通过完整的 terminal-first、typed、source/path、
serializer 以及（双色时）atomic adapter guards。以下的整数结论不替代这些 guards。

## 2. Stutter target 再次成为 full-product \(d=1\) 行

因为 \(1<q<p\)，(2) 中的正整数 \(E_x\) 唯一写为

\[
\boxed{E_x=q+ps,\qquad s\ge0.}
\tag{5}
\]

完整超额 stutter reduction 的 exact multiplier formula 给

\[
M_q=M_4\frac{L_0}{q}E_x
=\frac{M_{\rm alt}}qE_x
=m(q+ps).
\tag{6}
\]

因此

\[
4M_q+1
=4M_{\rm alt}+4mps+1
=p\bigl(n+4ms\bigr).
\tag{7}
\]

定义

\[
\boxed{n_q=n+4ms.}
\tag{8}
\]

则 \(n_q>1\)、\(n_q\equiv1\pmod4\)，并且

\[
\boxed{M_q=\frac{pn_q-1}{4},\qquad c_q=p-1.}
\tag{9}
\]

故 stutter target 并非无结构的同容量 chart；它精确落回 full-product \(d=1\)
normal form。这个结论只使用 (2) 的 arithmetic stutter，不把该 target 自动登记为
已入队状态。

## 3. 精确 \(a\) 坐标

令 \(w=(p+1)/2\)。由 (3)，

\[
M_{\rm alt}=wT,
\qquad
T=\frac{pb-1}{2},
\qquad
w=qd_4
\tag{10}
\]

其中最后一式只是 \(q\mid w\) 的记号。由 (8)--(10)，

\[
\begin{aligned}
a_q
&=\frac{w}{\left(w,(n_q+1)/2\right)}\\
&=\frac{qd_4}{\left(qd_4,d_4\bigl(qb+2Ts\bigr)\right)}\\
&=\frac q{\left(q,2Ts\right)}
=\frac q{\left(q,(b+1)s\right)}.
\end{aligned}
\tag{11}
\]

最后一步使用 \(2T=pb-1\equiv-(b+1)\pmod q\)。将 \(q\) 与 \(b+1\)
的共同素数幂先约掉，得到更适合分派的形式：

\[
\boxed{
a_q=\frac{q_0}{(q_0,s)}.
}
\tag{12}
\]

这里不需要 \(q\) 是素数。逐素数验证 (12)：若 \(v_\ell(q)=e\)、
\(v_\ell(b+1)=f\)，则 \(q_0\) 的 \(\ell\)-指数为 \((e-f)_+\)，而 (11)
的分母恰删去 \(\min(e,f+v_\ell(s))\) 层。

这给出三个互斥的 target 分派：

| 条件 | target 的确定结论 | 可复合的已有路由 |
|---|---|---|
| \(s=0\) | \(M_q=M_{\rm alt}\)、\(n_q=n\)、\(a_q=1\) | q-bridge 本身只回到同一 charged support/capacity；不视为 strict edge。 |
| \(s>0,\ q_0\nmid s\) | \(a_q>1\) | target 通过重分类后可接入既有 \(a>1\) d=1 strict handoff。 |
| \(s=q_0t>0\) | \(a_q=1\) | 进入第 4 节的正残余分派。 |

第二行的“可接入”有明确边界：只有 q-bridge payload 已获 E1--E4、target 的 typed
reclassification 完成、而后续 d=1 suffix 的 guards 都通过时，既有 \(a>1\) handoff
才给 \((0,p-1)>(0,c_T)\) 的 strict macro。式 (12) 本身没有越过这些语义门。

## 4. \(a_q=1\) 时的两类正残余接口

现在设 \(s=q_0t\)。因为 \(\gamma\mid b+1\) 且
\(\gamma\mid q\mid(p+1)/2\)，有

\[
\gamma\mid pb-1=p(b+1)-(p+1).
\tag{13}
\]

所以可定义整数

\[
B=\frac{pb-1}{\gamma}.
\tag{14}
\]

将 (8) 除以 \(p+1\)，并使用 (3)、(4)，得到 target 的 \(a=1\) 坐标

\[
\boxed{
b_q=\frac{n_q+1}{p+1}=b+Bt.
}
\tag{15}
\]

特别地，\(\gamma<p\)，故它在模 \(p\) 下可逆；由 \(\gamma B=pb-1\) 有

\[
\boxed{b_q\equiv b-\gamma^{-1}t\pmod p.}
\tag{16}
\]

这个 target 的 ordinary d=1 complete-excess multiplier 是

\[
F_q=(p-1)b_q-1.
\tag{17}
\]

按已建立的 d=1 residue dispatch，\(b_q\equiv0,-1,-2\pmod p\) 分别是
raw \(p\)-source failure、p-free failure、canonical regeneration；其它 residue
同时通过两条 \(p\) 门，且 \(F_q\not\equiv1\pmod p\)，所以 canonical capacity

\[
c_{\rm ord}=\left\langle-F_q^{-1}\right\rangle_p
\tag{18}
\]

严格满足 \(c_{\rm ord}\le p-2\)。由 (16)，三个接口恰为：

| \(t\pmod p\) | \(b_q\pmod p\) | target 的 ordinary d=1 分派 |
|---:|---:|---|
| \(\gamma b\) | \(0\) | 最小互素素数 source repair；\(a_q=1\) 时容量严格为 \(1\) |
| \(\gamma(b+1)\) | \(-1\) | p-free failure interface |
| \(\gamma(b+2)\) | \(-2\) | canonical regeneration；见下方 terminal-digit 分派 |
| 其它 | 其它 | 两条 \(p\) 门通过，且 (18) 严格 |

第一行不是算术余项。最小互素素数 source 可从同一 accepted d=1 target 到达 canonical
anchor；其严格容量为 \(\langle2g\rangle_p=1\)，因为此处 \(a_q=1\) 给
\(g=(p+1)/2\)。该 repair 仍须继承 target 的 persistent scope 并通过 terminal/typed
guards，但不留下新的数论 gate。

对第三行，令

\[
\eta_q=\nu_p(F_q-1),
\qquad
\omega_q\equiv\frac{F_q-1}{p^{\eta_q}}\pmod p.
\tag{19}
\]

此时 \(\eta_q\ge1\)。既有 regeneration countdown 保持 \(\omega_q\)，并在有限步后
给出：\(\omega_q=-2\) 时再次进入上面的 raw-source repair，\(\omega_q\ne-1,-2\)
时严格降容量，只有

\[
\boxed{\omega_q\equiv-1\pmod p}
\tag{20}
\]

回到 p-free failure/root interface。故除去 \(s=0\) 的同-support checkpoint，
q-bridge arithmetic stutter 的正 \(a=1\) 余项已从三个显式 \(t\bmod p\) cells 收紧为
两条通道：p-free failure，及 (20) 的 regeneration terminal cell。它们仍须沿已有
p-free small-anchor/root route 继续处理，且所有具体 strict macro 仍须重放相应 guards。

## 5. \(q_0\) 在另一侧的实际 raw re-entry

第 4 节还有一个与 static target chart 无关的 actual endpoint 后果。若
\(s=q_0t\)（包括 \(s=0\)），则 (5) 给

\[
\boxed{E_x=q_0(\gamma+pt).}
\tag{21}
\]

clean-q bridge 已给 \((q,M_4)=1\)，故 \((q_0,M_4)=1\)。从
\(E_x=Q_x/(M_4,Q_x)\) 与 (21) 得

\[
q_0\mid Q_x\mid x_q.
\tag{22}
\]

另一方面 \((x_q,y_q)=1\)，而 \(q_0\mid q\mid z=R_4-h\)，结合
\(q_0\mid x_q\)，给

\[
\qquad
\boxed{y_q\equiv h\pmod{q_0}.}
\tag{23}
\]

若 \(q_0>1\)，其每个素因子及重数都在 \(x_q\) 中超过 \(K_4\) 的容量：它们根本
不整除 \(K_4\)。又 \((x_q,R_4)=(x_q,y_q)=1\)，所以依次除去这些素因子不会发生
gcd reduction。于是已有 H4 prefix 可实际重放一个新的 primitive raw word

\[
\boxed{
\{x_q,y_q\}
\rightsquigarrow
\left\{\frac{x_q}{q_0},R_4-\frac{x_q}{q_0}\right\}.
}
\tag{24}
\]

式 (24) 是一个 source-anchored re-entry，不是新的 strict target：其终点的 complete-
excess blocks、terminal priority 和 typed dispatch 必须从头计算。它的价值是把正
\(a=1\) residual 中原本只以同余出现的 \(q_0\)，变成 H4 raw graph 中另一侧可重放的
clean carrier。

## 6. 精确的新余项

纯就本卡的算术分派而言，若 (12)、第 4 节的 ordinary d=1 dispatch 与既有
\(a>1\) handoff 都没有给出 strict-capacity candidate，则必要条件已缩为

\[
\boxed{
s=0
\quad\text{or}\quad
s=q_0t>0,
\quad
\left[
  t\equiv\gamma(b+1)\pmod p
  \ \text{or}\
  \bigl(t\equiv\gamma(b+2)\pmod p\ \text{and}\ \omega_q\equiv-1\pmod p\bigr)
\right].
}
\tag{25}
\]

第一项只是 q-bridge 的 charged-support checkpoint；第二项只含两条具名接口，并且都带
\(q_0\) raw re-entry (24)。这比原来的
\(Q_x>1,\ E_x\equiv q\pmod p\) 更窄，但不是 global exit theorem：每条 strict
candidate 仍须通过 atomic source admission、terminal-first/typed intercept 与 suffix
guards；\(s=0\) 的全局势和 (25) 两条通道的统一 closure 也仍然开放。

后继的[首层容量 stutter 全域 source \(D\)-gate 关闭](type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-universal-stutter-source-d-gate-closure.md)
表明：作为本卡入口的 (2) 在整个 actual 19-phase H4 scope 中根本不发生，而不只是
\(d_4=1\) 子域。因此本卡的 \(q_0=1\) 和 \(q_0>1\) stutter maps 当前都仅保留为
条件性整数正规形；它们可用于核对局部蕴含，但不再是 actual \(d_4>1\) residual。

## 7. 定向静态控制

下表只验证本卡的 full-product 整数恒等式；它们**不**构造 actual 19-phase H4
predecessor 或 actual q-bridge stutter endpoint。

| \(p\) | \(q\) | \(b\) | \(s\) | \(a_q\) | target 类别 |
|---:|---:|---:|---:|---:|---|
| 73 | 37 | 1 | 0 | 1 | 同 support checkpoint |
| 73 | 37 | 1 | 1 | 37 | \(a>1\) handoff cell |
| 73 | 37 | 1 | 37, 74, 111 | 1 | \(t=1\) 由 raw-source repair 严格离开；\(t=2\) 是 p-free cell；\(t=3\) 的 \(\omega_q=-5\)，故再生后严格离开 |
| 73 | 37 | 1 | 10915 | 1 | \(t=295\)；regeneration 的 \(\omega_q=-1\) p-free return control |
| 73 | 37 | 1 | 148 | 1 | \(t=4\)；ordinary capacity \(36<72\) |
| 241 | 121 | 1 | 484 | 1 | 复合 \(q_0=121\) 的 \(t=4\)；ordinary capacity \(120<240\) |

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_stutter_a_coordinate.py --verify
```

回执不扫描 prime ranges、分母、历史 Reach 或 H4 predecessor；它只防止这里的整数
normal form、residue/repair map 和 capacity representatives 被后续编辑破坏。
