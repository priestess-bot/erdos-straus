---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-p-primary-endpoint-exclusion
title: q=1 高 C=2 19 相位 H4 a=1 q-bridge 端点的 p-primary 排除
statement: >-
  在 actual q=1 high C=2 19-phase H4 proper-overlap top-capacity a_alt=1
  receipt 的 clean q raw bridge 中，令 h=gcd(R4-1,K4)=2*gcd((p+1)/2,c3-s4)、
  z=R4-h、q=((p+1)/2)/gcd((p+1)/2,M4)>1，及
  (x_q,y_q)=(R4-z/q,z/q)。则 p 不整除 x_q y_q，因而 p 不整除端点的任一 maximal
  complete-excess block。证明为：p 不整除 z/q，而 p|x_q 当且仅当
  h=p+1-q；后者与 h|p+1、q|(p+1)/2、h 为偶数矛盾。故 clean q bridge 的此前
  p-primary endpoint 分支在 actual H4 域为空；端点只余 Type I terminal、p-free
  one-sided payload、或 p-free atomic split payload。该结果不关闭 p-free capacity
  stutter、typed guards 或 atomic adapter 的独立准入。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
  - type-II-q-one-c-two-19-phase-h4-p-primary-small-anchor-renewal
  - type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff
  - type-II-q-one-c-two-19-phase-h4-full-overlap-predecessor-exclusion
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
  - p-primary
  - complete-excess-bundle
  - atomic-split
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
    role: clean-q-raw-word-and-endpoint-taxonomy
  - claim: type-II-q-one-c-two-19-phase-h4-p-primary-small-anchor-renewal
    role: actual-H4-overlap-parity-and-p-free-proper-overlap
  - claim: type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff
    role: q-divides-w-and-q-divides-z-interface
  - claim: type-II-q-one-c-two-19-phase-h4-full-overlap-predecessor-exclusion
    role: actual-proper-overlap-domain
  - claim: type-I-path-anchored-atomic-split-complete-excess-admission
    role: p-free-two-sided-payload-boundary
  - concept: denominator-escape-state-contract
    role: typed-edge-and-terminal-contract
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_carrier_clean_raw_bridge.py
    role: prime-and-composite-q-p-primary-gate-controls
visibility: public
last_checked: '2026-08-16'
---

# H4 \(q\)-bridge 端点的 \(p\)-primary 排除

## 1. 设置

保留 actual H4 proper-overlap top-capacity \(a_{\rm alt}=1\) 的 clean \(q\) raw bridge：

\[
K_4=M_4c_4,\qquad pR_4+1=4K_4,\qquad R_4\equiv1\pmod p,
\tag{1}
\]

\[
h=(R_4-1,K_4)=2\left(\frac{p+1}{2},c_3-s_4\right),
\qquad 2\le h<p+1,\qquad h\mid p+1,
\tag{2}
\]

\[
z=R_4-h=Q\delta,\qquad p\nmid K_4Q,\qquad \delta\mid K_4,
\tag{3}
\]

\[
w=\frac{p+1}{2},\qquad d_4=(w,M_4),\qquad
q=\frac w{d_4}>1,\qquad q\mid Q\mid z.
\tag{4}
\]

其中 (2) 的 strict proper-overlap 来自 actual full-overlap predecessor exclusion，
而 (3) 是 actual p-primary small-anchor renewal 的 p-free bundle。clean bridge 已证明
\((q,K_4)=1\)，并给实际 primitive endpoint

\[
\boxed{
y_q=\frac zq,\qquad x_q=R_4-y_q.
}
\tag{5}
\]

本卡只排除 (5) 产生新的完整 \(p\)-block；不重做 bridge 的 source/path proof。

## 2. \(y_q\) 已经 p-free

由 (3) 有 \(p\nmid z\)，又 \(q\mid w<p\)，所以 \(p\nmid q\)。因此

\[
\boxed{p\nmid y_q.}
\tag{6}
\]

任何 endpoint \(p\)-primary failure 因而只能来自 \(x_q\)。这一步使用的是 H4
proper-overlap 的真实 p-free input；若脱离该 input 任取静态 \(q\mid z\)，则 (6) 不应被
假定。

## 3. 唯一 p-primary 同余门

由 \(R_4\equiv1\pmod p\)、\(z=R_4-h\) 及 \(p\nmid q\)，有

\[
\begin{aligned}
p\mid x_q
&\Longleftrightarrow y_q\equiv1\pmod p\\
&\Longleftrightarrow \frac{1-h}{q}\equiv1\pmod p\\
&\Longleftrightarrow h\equiv1-q\pmod p.
\end{aligned}
\tag{7}
\]

又 \(1<q\le w\)，故

\[
w\le p+1-q\le p-1.
\tag{8}
\]

而 (2) 给 \(2\le h<p+1\)。因此 (7) 在这个整数范围中没有第二个代表，精确等价于

\[
\boxed{p\mid x_q\quad\Longleftrightarrow\quad h=p+1-q=2w-q.}
\tag{9}
\]

## 4. divisor-parity 矛盾

反设 (9) 的右端成立。由 \(h\mid p+1=2w\) 及 \(q=2w-h\)，立刻有

\[
h\mid q.
\tag{10}
\]

另一方面，(8)--(9) 给 \(h\ge w\)，而 \(q\mid w\) 给 \(q\le w\)。正整数整除
\(h\mid q\) 强制

\[
h=q=w.
\tag{11}
\]

但 \(p\equiv1\pmod{24}\) 使 \(w=12k+1\) 为奇数，(2) 则使 \(h\) 为偶数；(11) 矛盾。
故

\[
\boxed{p\nmid x_qy_q.}
\tag{12}
\]

endpoint 的两个 maximal complete-excess blocks 分别整除 \(x_q\)、\(y_q\)，于是

\[
\boxed{p\nmid Q_{K_4}(x_q)Q_{K_4}(y_q).}
\tag{13}
\]

## 5. 对 q-bridge 分派的影响

此前 bridge 的一般端点表有四项。式 (13) 删除其中 p-primary 项；在 actual H4 域内只剩：

| endpoint | 可用对象 | 尚需的独立 guard |
|---|---|---|
| 两个 complete-excess block 均为空 | Type I terminal | terminal verifier。 |
| 恰一块非空 | p-free 单侧 complete-excess payload | typed target 与 parent-macro capacity。 |
| 两块均非空 | p-free atomic split payload | atomic source/target validator、owner 语义、typed target 与 capacity。 |

因此 q-bridge 不会重新制造 H4 已经处理过的 \(p\)-block provenance 问题。它仍不保证
后两行的 canonical capacity \(c_q\le p-2\)：\(L_q\equiv-c_4\pmod p\) 的 p-free
capacity stutter，以及所有 priority/typed guard，仍是实际余项。

## 6. 定向回执

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_carrier_clean_raw_bridge.py --verify
```

回执在 \(p=73,q=37\) 与 \(p=241,q=11^2\) 的两个 local H4 controls 上同时检查：
\(p\nmid y_q\)、(7) 的同余 gate 与 endpoint 的两个 p-free complete-excess block。
它不扫描 prime ranges 或静态 predecessor。
