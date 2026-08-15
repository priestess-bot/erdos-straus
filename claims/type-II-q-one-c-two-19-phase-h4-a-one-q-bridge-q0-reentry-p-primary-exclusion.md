---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-p-primary-exclusion
title: H4 clean q-bridge 的 q0 raw re-entry p-primary 排除
statement: >-
  在 actual q=1 high C=2 19-phase H4 proper-overlap top-capacity a_alt=1 clean
  q bridge 中，写 w=(p+1)/2=qd、h=2e、gamma=gcd(q,b+1)、q0=q/gamma，并设唯一
  q-bridge stutter E_x=q+ps 满足 q0|s、q0>1。则 actual raw word
  {x_q,y_q} -> {xi=x_q/q0,zeta=R4-xi} 的两个 endpoint 坐标都 p-free；特别地
  p 不整除 zeta。证明首先由 H4 carry 与 clean-q 强制 e=d。令
  D=gcd(M4,Q_x)*beta_x，其中 x_q=Q_x beta_x 是 maximal complete-excess
  分解；则 D|K4、xi=(gamma+pt)D 且 D|ph-q+1。若反设 p|zeta，则
  gamma D=1+pk。k=0 强制 gamma=D=1、q0=q，并把事件化为固定常数
  p | 1-2d+4d^2(1-2d)；在 d<=1535 的 exact phase-factor screen 中没有任何
  同时满足 p=2dq-1 的记录。k>=1 时，写 k=1+gamma u 与
  ell=(ph-q+1)/D；由 D|K4、clean q、h=2d 可得 1<=u,ell<=2d-1，且
  q0[gamma(2dC+2d-1)-2d ell]=C，其中 C=2d-1-ell u。C=0 违反奇偶性，
  C<0 两边异号，C>0 则令 C=q0 r 并强制 gamma=2d-r、
  ell=(2d-r)(q0 r+1)-1>2d-1-q0 r>=ell，矛盾。该结果关闭 q0>1 re-entry 的
  p-primary 支路；它不自动给出 terminal、strict capacity、atomic admission，亦不处理
  q0=1 的 residual。
claim_status: established
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-carry-overlap-boundary
  - type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff
  - type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-stutter-a-coordinate-transduction
  - type-II-q-one-c-two-19-phase-fourth-anchor-terminal-gate
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
  - q0-reentry
  - p-primary
  - complete-excess-bundle
  - carry-stutter
  - finite-sieve
  - source-provenance
  - well-founded-rank
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-carry-overlap-boundary
    role: H4-carry-identity-and-gcd-w-M3-one
  - claim: type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff
    role: fresh-q-carrier-and-bounded-d-provenance
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
    role: clean-q-and-actual-raw-word
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-stutter-a-coordinate-transduction
    role: q0-reentry-and-E-x-normal-form
  - claim: type-II-q-one-c-two-19-phase-fourth-anchor-terminal-gate
    role: base-19-phase-parameter-domain
  - concept: denominator-escape-state-contract
    role: terminal-typed-lift-and-potential-contract
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_q0_reentry_p_primary.py
    role: exact-k-zero-diagonal-factor-screen
visibility: public
last_checked: '2026-08-16'
---

# H4 clean \(q\)-bridge 的 \(q_0\) raw re-entry p-primary 排除

## 1. 范围

保留 actual q=1 high \(C=2\) 19-phase H4 proper-overlap top-capacity
\(a_{\rm alt}=1\) clean \(q\)-bridge 的记号：

\[
w=\frac{p+1}{2}=qd,
\qquad
h=2e,
\qquad
(q,K_4)=(q,M_4)=1,
\tag{1}
\]

\[
x_q=Q_x\beta_x,
\qquad
E_x=\frac{Q_x}{(M_4,Q_x)}=q+ps,
\tag{2}
\]

其中 \((Q_x,\beta_x)=1\)、\(\beta_x\mid K_4\)，且

\[
\gamma=(q,b+1),
\qquad q_0=\frac q\gamma.
\tag{3}
\]

本卡处理 \(q_0\mid s\) 且 \(q_0>1\) 的 cells；这包括两个正 \(a=1\)
residual 通道，也允许 \(s=0\) 的同一 raw subword。已有 q-bridge 转导给

\[
E_x=q_0(\gamma+pt),
\qquad
q_0\mid Q_x\mid x_q,
\tag{4}
\]

并把 \(q_0\) 的全部素因子实际剥离到 primitive node

\[
\boxed{
\{x_q,y_q\}\rightsquigarrow
\{\xi,\zeta\}:=
\left\{\frac{x_q}{q_0},R_4-\frac{x_q}{q_0}\right\}.
}
\tag{5}
\]

这里要排除的不是原 q-word endpoint 的 \(p\)-block（它已被排除），而是
re-entry 后另一侧 \(\zeta\) 重新出现的 \(p\)-block。结论只关闭这个算术
gate；(5) 的 terminal-first、typed、单侧/atomic payload 和容量仍要独立处理。

## 2. Actual Clean Bridge 强制 \(e=d\)

这个等式此前只以两个相反方向的局部整除出现；在 actual H4 clean bridge 中它们可合并。
H4 carry 记号给

\[
M_4=M_3L,
\qquad (w,M_3)=1,
\qquad
Lc_4=c_3+ps_4.
\tag{6}
\]

因为 \(p\equiv-1\pmod w\)，

\[
Lc_4\equiv c_3-s_4\pmod w.
\tag{7}
\]

由 \(d=(w,M_4)=(w,L)\)，式 (7) 给

\[
d\mid (w,c_3-s_4)=e.
\tag{8}
\]

另一方面 \(e\mid w\) 且 \(2e=h\mid K_4\)。clean-q 给 \((e,q)=1\)，而
\(w=qd\)，所以 \(e\mid d\)。因此

\[
\boxed{e=d.}
\tag{9}
\]

特别地，\(d,e,q,\gamma,q_0\) 都是奇数，且

\[
p=2d\gamma q_0-1,
\qquad h=2d.
\tag{10}
\]

这一步使用 actual H4 carry；脱离该 provenance，只有 \(e\mid d\) 的旧 clean-q
结论，不能替换成 (9)。

## 3. Support-Normalized Small Divisor

令

\[
g=(M_4,Q_x),
\qquad D=g\beta_x.
\tag{11}
\]

因为 \(g\mid M_4\mid K_4\)、\(\beta_x\mid K_4\) 且
\((g,\beta_x)=1\)，有

\[
\boxed{D\mid K_4,\qquad (D,q_0)=1.}
\tag{12}
\]

由 (2)、(4)、(11)，

\[
\boxed{\xi=(\gamma+pt)D.}
\tag{13}
\]

原 q-word 满足 \(qy_q=R_4-h\)，而 \(x_q=q_0\xi\)、
\(x_q+y_q=R_4\)，故

\[
(q-1)R_4=\gamma q_0^2\xi-h.
\tag{14}
\]

再以 \(pR_4+1=4K_4\) 模 \(D\) 约化，得到

\[
\boxed{D\mid ph-q+1.}
\tag{15}
\]

这不是把完整超额块 \(Q_x\) 静态替换为其余块：\(D\) 是由 support overlap 和
\(\beta_x\) 组成、确实整除 \(K_4\) 的归一化小除子。

又 \(p\nmid\xi\)，因为 \(p\nmid\gamma D\)。若反设 \(p\mid\zeta\)，则
\(R_4\equiv1\pmod p\) 和 (13) 给

\[
\boxed{\gamma D\equiv1\pmod p.}
\tag{16}
\]

写

\[
\gamma D=1+pk,
\qquad k\ge0.
\tag{17}
\]

以下逐项排除 (17)。

## 4. \(k=0\)：回到固定 Diagonal Phase Gate

若 \(k=0\)，正性使

\[
\gamma=D=1,
\qquad q_0=q.
\tag{18}
\]

所以 (5) 恰是完整 clean \(q\)-word；(14) 化为

\[
(q-1)R_4=q^2\xi-h.
\tag{19}
\]

由于 \(p\mid\zeta\) 等价于 \(\xi\equiv1\pmod p\)，由
\(R_4\equiv1\pmod p\)、\(h=2d\) 得

\[
p\mid q^2-q+1-2d.
\tag{20}
\]

代入 \(q=(p+1)/(2d)\) 并乘 \(4d^2\)，这是固定常数门

\[
\boxed{
p\mid C_d:=1-2d+4d^2(1-2d).
}
\tag{21}
\]

actual H4 provenance 给 \(d\mid\Delta=|1536-a(p)|\) 与
\(1\le\Delta\le1535\)，所以只需检查 \(1\le d\le1535\)。对这 1,535 个
非零常数作精确因子分解，在 base 19-phase
\(p\equiv769\pmod{912}\) 中只有 16 个 \((p,d)\) factor records；其中没有一个使

\[
q=\frac{p+1}{2d}
\tag{22}
\]

为整数。故 (21) 不可能来自 actual H4 bridge。这个更小的筛不需要重用
\(s=0\) 卡中 \(\xi\mid K_4\) 的额外结论；它只使用当前 full-q re-entry 的
endpoint identity (19)、实际 phase 和 H4 的 \(d\) provenance。

## 5. \(k\ge1\)：无枚举矛盾

现在设 \(k\ge1\)。因为 \(p\equiv-1\pmod\gamma\)，(17) 给

\[
k\equiv1\pmod\gamma,
\qquad k=1+\gamma u.
\tag{23}
\]

由 (10)、(17) 得

\[
D=\frac{p+1}{\gamma}+pu=2dq_0+pu.
\tag{24}
\]

若 \(u=0\)，(24) 使 \(q_0\mid D\mid K_4\)，矛盾于 clean-q；所以 \(u\ge1\)。
令

\[
A=ph-q+1,
\qquad \ell=\frac AD.
\tag{25}
\]

式 (15) 使 \(\ell\) 为正整数；又 \(D>pu\)、\(A<ph=2dp\)，故

\[
1\le u,\ell\le2d-1.
\tag{26}
\]

用 (10)、(24) 展开 \(A=\ell D\)，并定义

\[
C=2d-1-\ell u,
\tag{27}
\]

得到精确恒等式

\[
\boxed{
q_0\bigl[\gamma(2dC+2d-1)-2d\ell\bigr]=C.
}
\tag{28}
\]

若 \(C=0\)，(28) 会给

\[
\gamma(2d-1)=2d\ell,
\tag{29}
\]

左边为奇数、右边为偶数，矛盾。若 \(C<0\)，令 \(c=-C\)。则
\(2dC+2d-1<0\)，而

\[
2d\ell-\frac c{q_0}>0
\tag{30}
\]

（由 \(c=\ell u-(2d-1)<2d\ell\)）使 (28) 除以 \(q_0\) 后两边异号，矛盾。

于是 \(C>0\)。由 (28)，\(q_0\mid C\)；写 \(C=q_0r\)。因为 \(q_0>1\) 为奇数，

\[
C\ge3,
\qquad 0<r<2d.
\tag{31}
\]

将 (28) 除以 \(q_0\) 后，有

\[
\gamma(2dC+2d-1)=2d\ell+r.
\tag{32}
\]

这里 \(2dC+2d-1\ge8d-1\)，而由 (26)、(31)，

\[
0<2d\ell+r\le4d^2-1
<2d(8d-1)\le2d(2dC+2d-1).
\tag{33}
\]

故 \(0<\gamma<2d\)。模 \(2d\) 约化 (32) 给

\[
-\gamma\equiv r\pmod{2d},
\qquad\text{故}\qquad
\gamma=2d-r.
\tag{34}
\]

代回 (32)，得到强制值

\[
\ell=(2d-r)(q_0r+1)-1.
\tag{35}
\]

但 (27) 与 \(u\ge1\) 同时给

\[
\ell\le2d-1-q_0r.
\tag{36}
\]

两式之差为

\[
\ell-(2d-1-q_0r)
=r\bigl[q_0(2d-r+1)-1\bigr]>0,
\tag{37}
\]

与 (35) 矛盾。因此 \(k\ge1\) 不可能。

## 6. 后果与边界

第 4、5 节共同排除了 (16)，故

\[
\boxed{p\nmid\xi\zeta.}
\tag{38}
\]

也就是说，所有 \(q_0>1\) 的 actual re-entry 已经回到 p-free endpoint taxonomy；
它不会在两条正 \(a=1\) residual 通道中再制造新的 \(p\)-primary provenance 问题。

这不是 global exit theorem。仍需从 (5) 的 p-free complete-excess blocks 证明
Type I terminal、strict capacity，或获准的 atomic/typed target；另外 \(q_0=1\)
时没有 nontrivial \(q_0\) word，仍不属于本卡的结论。

## 7. 定向复现

~~~bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_q0_reentry_p_primary.py --verify
~~~

回执只分解 \(k=0\) 的 1,535 个固定 diagonal 常数，并检查正 \(k\) 矛盾的最终整数式；
它不扫描素数区间、分母、历史 Reach 或 H4 predecessor。
