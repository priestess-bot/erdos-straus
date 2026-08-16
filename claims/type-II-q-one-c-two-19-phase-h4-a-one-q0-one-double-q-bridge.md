---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-q0-one-double-q-bridge
title: H4 clean q-bridge 的 q0=1 双 q raw bridge、第二端点 p-primary 排除与 q^2 容量门
statement: >-
  在 actual q=1 high C=2 19-phase H4 proper-overlap top-capacity a_alt=1 的 clean
  q bridge 中，令 M_alt=M4 L0=wT、w=(p+1)/2=qd4、T=(pb-1)/2、
  gamma=gcd(q,b+1)、q0=q/gamma。若 q0=1，则 q^2 divides L0 and q^2 divides Q_K4(z)
  divides z。因而已有 H4 prefix 可从 {h,z} 连续实际重放两条 primitive clean q raw word，
  到达 (x2,y2)=(R4-z/q^2,z/q^2)。该第二端点在全部核心素数域都 p-free：若 p divides x2，
  由 h=2e、e divides d4、p=2qd4-1 可强制唯一非核心解
  (p,q,d4,e)=(5,3,1,1)，故对 p=1 (mod 24) 不可能；p does not divide y2 由 original
  p-free bundle 直接给出。令 Q_x2=Q_K4(x2)、E_x2=Q_x2/gcd(M4,Q_x2)，则
  Q_y2=Q_K4(y2)=Q_K4(z)/q^2，第二 endpoint 的 complete-excess multiplier 为
  L2=(L0/q^2)E_x2，canonical capacity 满足 c2=-q^2 E_x2^{-1} (mod p)。
  所以在 terminal/typed/source/atomic guards 通过时，c2<=p-2 给 persistent parent 的
  identity-lift strict macro；唯一容量 stutter 恰为 E_x2=q^2 (mod p)。该结论不证明
  q0=1 分支全局退出，也不自动支付单侧或 atomic payload 的 E1--E4。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-p-primary-endpoint-exclusion
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-stutter-a-coordinate-transduction
  - type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff
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
  - p-primary
  - complete-excess-bundle
  - capacity-map
  - solution-lift
  - well-founded-rank
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
    role: clean-q-and-first-raw-word
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-p-primary-endpoint-exclusion
    role: actual-proper-overlap-h-shape-and-p-free-bundle
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-stutter-a-coordinate-transduction
    role: full-product-b-coordinate-and-q0-definition
  - claim: type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff
    role: top-capacity-d-one-interface
  - concept: denominator-escape-state-contract
    role: guarded-identity-lift-and-parent-potential
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q0_one_double_q_bridge.py
    role: local-H4-double-q-control
visibility: public
last_checked: '2026-08-16'
---

# H4 \(q_0=1\) 的双 \(q\) clean raw bridge

## 1. 入口与结论

保留 actual H4 proper-overlap top-capacity \(a_{\rm alt}=1\) clean \(q\)-bridge 的全部
前提。写

\[
K_4=M_4c_4,\qquad pR_4+1=4K_4,\qquad h=(R_4-1,K_4),\qquad z=R_4-h,
\tag{1}
\]

\[
w=\frac{p+1}{2}=qd_4,\qquad
L_0=\frac{M_{\rm alt}}{M_4}=\frac{Q}{(M_4,Q)},\qquad
M_{\rm alt}=wT,\qquad T=\frac{pb-1}{2}.
\tag{2}
\]

这里 \(Q=Q_{K_4}(z)\)，并已有

\[
(q,K_4)=1,\qquad q\mid L_0\mid Q\mid z,\qquad p\nmid K_4Q,\qquad p\equiv-1\pmod q.
\tag{3}
\]

actual proper-overlap 的 p-free bundle 还给出 \(z=Q\delta\) 与 \(\delta\mid K_4\)，
所以 \(p\nmid z\)。

令

\[
\gamma=(q,b+1),\qquad q_0=\frac q\gamma.
\tag{4}
\]

本卡只处理此前不属于 \(q_0>1\) re-entry 的 \(q_0=1\) 分支。结论是一个第二 raw
endpoint 的精确容量图，而不是把该分支误称为已经全局闭合。

## 2. \(q_0=1\) 强制第二个 clean carrier

由 \(q_0=1\)，有 \(\gamma=q\)，从而

\[
q\mid b+1.
\tag{5}
\]

又 \(q\mid w\) 给 \(p\equiv-1\pmod q\)。因此

\[
2T=pb-1\equiv(-1)(-1)-1\equiv0\pmod q.
\tag{6}
\]

核心素数使 \(w\)、故 \(q\) 都是奇数，所以 \(q\mid T\)。由 (2) 得

\[
q^2\mid M_{\rm alt}.
\tag{7}
\]

另一方面 \((q,K_4)=1\) 且 \(M_4\mid K_4\)，故 \((q,M_4)=1\)。将 (7) 除以
\(M_4\)，再用 (2)，逐素数幂得到

\[
\boxed{q^2\mid L_0,\qquad q^2\mid Q,\qquad q^2\mid z.}
\tag{8}
\]

这比原来的 \(q\mid Q\) 多出完整的一层 clean carrier；它只使用 \(q_0=1\) 的精确
整除，而不是一个静态 full-product 图表的偶然大公因子。

## 3. 两条实际 primitive raw word

将 \(q\) 的素因子按固定次序逐个剥离。由 (3)、(8)，第一条 word 后每个
\(\ell\mid q\) 仍在 selected coordinate 中保留完整的一层，且

\[
v_\ell(K_4)=0.
\tag{9}
\]

又已有 \((z,R_4)=1\)。所以连续两次都不发生 gcd reduction，给出绑定同一 H4 prefix 的
实际 raw replay

\[
\boxed{
\{h,z\}
\rightsquigarrow
\left\{x_1,y_1\right\}
=\left\{R_4-\frac zq,\frac zq\right\}
\rightsquigarrow
\left\{x_2,y_2\right\}
=\left\{R_4-\frac z{q^2},\frac z{q^2}\right\}.
}
\tag{10}
\]

这不是从第一个 endpoint 反向制造新 source：第二段只是 (8) 所允许的同一 selected
coordinate 的第二个实际 \(q\)-word。其 terminal-first、typed 与 serializer priority
仍须在各个 endpoint 独立重算。

## 4. 第二 endpoint 不会产生 \(p\)-primary residual

由 (3) 立即有 \(p\nmid y_2\)。下面排除 \(p\mid x_2\)。actual proper-overlap 给

\[
h=2e,\qquad h\mid p+1=2qd_4.
\tag{11}
\]

而 \(h\mid K_4\) 与 \((q,K_4)=1\) 给 \((q,h)=1\)，故

\[
e\mid d_4,\qquad (e,q)=1,\qquad p=2qd_4-1.
\tag{12}
\]

反设 \(p\mid x_2\)。由 \(R_4\equiv1\pmod p\) 及 (10)，得到

\[
p\mid q^2+h-1=q^2+2e-1.
\tag{13}
\]

写正整数

\[
k=\frac{q^2+2e-1}{p}.
\tag{14}
\]

先由 \(p\le q^2+2e-1\le q^2+2d_4-1\) 得

\[
d_4\le\frac{q^2}{2(q-1)}<\frac{q+3}{2}.
\tag{15}
\]

由于 \(d_4\) 为整数，(15) 给 \(d_4\le(q+1)/2\)，所以 \(2e-1\le q\)。等号会强制 \(e=d_4=(q+1)/2\)，此时
\(q^2+2e-1=p+1\)，与 (13) 矛盾。因此 \(0<2e-1<q\)。同时

\[
q^2+2e-1<qp
\tag{16}
\]

（用 \(e\le d_4\)、\(q\ge3\) 直接展开即可），故 \(0<k<q\)。将 (13) 模 \(q\)
化简，得

\[
k=q+1-2e.
\tag{17}
\]

将 \(2e-1=q-k\) 代回 (13)--(14)，消去 \(-k\) 后得到

\[
q+1=2d_4k.
\tag{18}
\]

令 \(d_4=ef\)。由 (17)--(18)，

\[
k=2e(fk-1).
\tag{19}
\]

所以 \(k=2ea\) 且

\[
a=2efa-1,\qquad (2ef-1)a=1.
\tag{20}
\]

正整数性强制 \(a=e=f=1\)，进而 \(k=2,q=3,d_4=1,p=5\)。这不是核心素数。
故核心域中 (13) 不可能，得到

\[
\boxed{p\nmid x_2y_2.}
\tag{21}
\]

特别地，(10) 的第二 endpoint 只会进入 Type I terminal、p-free 单侧 payload 或 p-free
atomic split payload；它没有此前 \(q_0>1\) re-entry 所需的额外 \(p\)-primary 分派。

## 5. 第二容量门

设

\[
Q_{x,2}=Q_{K_4}(x_2),\qquad
Q_{y,2}=Q_{K_4}(y_2),\qquad
E_{x,2}=\frac{Q_{x,2}}{(M_4,Q_{x,2})}.
\tag{22}
\]

由 (8)、(10) 及 \((q,M_4)=1\)，最大 complete-excess block 满足

\[
Q_{y,2}=\frac Q{q^2},\qquad
\frac{Q_{y,2}}{(M_4,Q_{y,2})}=\frac{L_0}{q^2}.
\tag{23}
\]

又 \((x_2,y_2)=1\)，故两个 block 的新素因子支撑互素。于是第二 endpoint 的 total
multiplier 精确为

\[
\boxed{
L_2=\frac{\operatorname{lcm}(M_4,Q_{x,2},Q_{y,2})}{M_4}
=\frac{L_0}{q^2}E_{x,2}.
}
\tag{24}
\]

初始 top capacity 是 \(c_4L_0^{-1}\equiv-1\pmod p\)，即 \(c_4\equiv-L_0\pmod p\)。
由 (21) 可对 (24) 取模逆，故

\[
\boxed{
c_2\equiv c_4L_2^{-1}\equiv-q^2E_{x,2}^{-1}\pmod p.
}
\tag{25}
\]

因此

\[
\boxed{
c_2=p-1
\quad\Longleftrightarrow\quad
E_{x,2}\equiv q^2\pmod p.
}
\tag{26}
\]

若 endpoint payload 和所有 E1--E4 guards 已获准，则 \(c_2\le p-2\) 给出

\[
\Lambda_p^\sharp(P)=(0,p-1)>(0,c_2),
\tag{27}
\]

并以同一 \(4/p\) equation target 上的 identity map 支付 E4。故 (26) 是 \(q_0=1\)
分支的第二个精确容量门，而不是未标记的同-support stutter。

## 6. 边界与定向回执

本卡把 \(q_0=1\) 从“没有 nontrivial \(q_0\)-word”推进为：一个第二 p-free actual
endpoint，带唯一的 \(q^2\)-stutter congruence。它仍未证明
\(E_{x,2}\not\equiv q^2\pmod p\)，也不自动把单侧或 atomic payload 登记为 recursive
edge；这些是现在明确、独立的全局出口义务。

这里的结论对一般 \(d_4\) 仍是有效的条件性 bridge。后继的
[\(d_4=1\) original q-bridge source \(D\)-gate](type-II-q-one-c-two-19-phase-h4-a-one-d-one-q-bridge-stutter-source-d-gate-closure.md)
已排除生成本卡 \(q_0=1\) 入口的第一层 capacity stutter；故 actual \(d_4=1\)
子域在到达 (10) 前已经关闭，不能把本卡的 \(d_4=1\) normal form 当作剩余 branch。

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q0_one_double_q_bridge.py --verify
```

回执只重放一个 \(p=73\) 的 local H4 arithmetic control：它具有实际 H4 的
\(pR_4+1=4K_4\)、proper overlap、top capacity、\(q_0=1\) 与 \(q^2\mid Q\) 结构，
但不声称存在 actual H3 predecessor、typed payload 或 persistent macro。
