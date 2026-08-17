---
kind: claim
claim_id: type-I-root-capacity-stutter-c-equals-h-odd-distance-fan-no-go
title: proper-root stutter 的 c=h 奇距离偶源扇全称 no-go
statement: >-
  对核心素数 p≡1 mod24 的 terminal-first 后 actual proper-root stutter receipt，
  令 h=3u、2≤h<p，并保留已有 cubic hard-root wall 513h^6>8p^4。
  不存在正整数 delta,r 使 p-h=delta(1+hr) 且 delta*r≡-1 mod4。
  因而以自然距离 c=h 调用 odd-distance-even-source-descent 的现有
  translated-square family 恒为空。该命题只排除这一个具名 even-source family；
  它不排除其它距离、marked even-source lift 或三分母 lift，也不构造 terminal、
  E1--E5 successor 或 T6 totality。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-cubic-hard-root-wall
  - odd-distance-even-source-descent
topics:
  - type-I
  - root-capacity
  - stutter
  - even-source
  - odd-distance
  - no-go
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_root_capacity_stutter_c_equals_h_odd_distance_fan_no_go.py
    role: exact-constant-and-relaxed-boundary-controls
visibility: public
last_checked: '2026-08-17'
---

# proper-root stutter 的 \(c=h\) 奇距离偶源扇全称 no-go

## 1. 设置

固定一个 terminal-first 后的 actual proper-root stutter receipt。沿用

\[
p\equiv1\pmod {24},\qquad 2\le h<p,\qquad
h\mid p^2+p+1,
\tag{1}
\]

以及已建立的 cubic hard-root wall

\[
513h^6>8p^4.
\tag{2}
\]

反设自然距离 \(c=h\) 能进入已有的 odd-distance even-source fan。则存在正整数
\(\delta,r\) 使

\[
p-h=\delta(1+hr),\qquad \delta r\equiv-1\pmod4.
\tag{3}
\]

## 2. Fan 条件给出的上界

奇距离偶源定理从 (3) 推出

\[
r\equiv7\pmod8,
\]

所以 \(r\ge7\)。于是

\[
p-h=\delta(1+hr)\ge1+7h,
\]

从而

\[
h<\frac p8.
\tag{4}
\]

令 \(g=p-h\)。由 (1) 有

\[
h\mid g^2+g+1.
\]

而 (3) 给出 \(g\equiv\delta\pmod h\)，故

\[
h\mid\delta^2+\delta+1
\quad\Longrightarrow\quad
h\le\delta^2+\delta+1.
\tag{5}
\]

另一方面，

\[
\delta=\frac{p-h}{1+hr}<\frac p{7h}.
\tag{6}
\]

把 (6) 代入 (5)，再使用 (4)，得到

\[
\begin{aligned}
h^3
&<\frac{p^2}{49}+\frac{ph}{7}+h^2\\
&<\left(\frac1{49}+\frac1{56}+\frac1{64}\right)p^2
=\frac{169}{3136}p^2
<\frac19p^2.
\end{aligned}
\tag{7}
\]

## 3. Hard-root wall 给出的反向下界

由 (2)，

\[
h^6>\frac8{513}p^4.
\]

又

\[
\frac8{513}>\frac1{81},
\]

两侧均为正数，所以

\[
h^3>\frac19p^2.
\tag{8}
\]

(7) 与 (8) 矛盾，故 (3) 不存在。

## 4. 证明边界

该结论使用了 (3) 的完整 named-family 形状，尤其是
\(p-h=\delta(1+hr)\) 和 odd-distance theorem 强制的 \(r\ge7\)。若 future
selector 改变 source family、距离、保留尾或 lift 形状，本 no-go 不适用。它没有产生
terminal 或 persistent successor，不能作为 proper-root 子域或 T6 的闭合证明。

## 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_stutter_c_equals_h_odd_distance_fan_no_go.py --verify
```
