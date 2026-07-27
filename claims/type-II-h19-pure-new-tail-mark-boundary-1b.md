---
kind: claim
claim_id: type-II-h19-pure-new-tail-mark-boundary-1b
title: 纯新规范证书与同证书双尾递降在十亿 H19 状态中不重合
statement: 对十亿范围541个 H19 新因子状态，完整枚举20<=s<=1008的纯新单素因子规范 Type II 证书后，仅282个证书窗口内存在其自身缺口 m 满足 m+1|p-1，因而同一证书可双尾严格递降；余259个均无此类同证书桥。这是固定窗口的机制边界，而非对独立递降或原猜想的反例。
claim_status: computationally_reproduced
topics:
- type-II
- pure-new-factor
- strict-descent
- tail-deflation
- H19
- finite-audit
- boundary
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--3
  role: Type-II-certificate-and-lift-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-27'
---

# 纯新规范证书与同证书双尾递降在十亿 H19 状态中不重合

## 命题

取 [H19 源自由状态剖面](type-II-source-free-transition-profile.md) 中
\(p\le10^9\) 的 541 个新因子状态。对每个 \(20\le s\le1008\)，写

\[
s=a^2c,\qquad c\text{ 平方自由},\qquad M=4ac,
\]

并只允许 H19 新素数 \(q\) 满足

\[
q\mid p+4s,\qquad q\equiv-1\pmod M. \tag{1}
\]

令 \(m=(p+4s)/q\)。由 (1) 重建的正是缺口为 \(m\) 的 Type II 证书。它能以
**同一张证书**双尾去 \(p\) 严格递降，当且仅当

\[
m+1\mid p-1. \tag{2}
\]

完整精确审计给出

\[
541=282_{\rm pure\ new+same\ tail}+259_{\rm no\ same\ bridge}. \tag{3}
\]

换言之，259 个状态在整个 \(20\le s\le1008\) 窗口内都没有一张同时满足 (1)--(2)
的纯新单素因子规范证书。

## 验证的提升

对任一命中，令

\[
n=\frac{p+m}{m+1}.
\]

审计逐项验证 \(2\le n<p\)，并对 Type II 证书
\((x,y,z)\) 精确检验

\[
\frac4n=\frac1x+\frac1{y/p}+\frac1{z/p},
\qquad
\frac4p=\frac1x+\frac1y+\frac1z. \tag{4}
\]

例如

\[
p=345601,\quad s=315=3^2\cdot35,\quad q=5879,\quad m=59,\quad n=5761.
\]

这里 \(60\mid345600\)，所以这张纯新证书自身就是严格递降边。

## 意义

[增长规范移位扇上的纯新单素因子证书具有超对数稀薄尾部](type-II-pure-new-canonical-fan-superlog-tail.md)
说明纯新规范扇在解析上覆盖相对密度一；但式 (3) 表明，不能在当前窗口中要求这张
**同一**纯新证书自动兼任双尾递降。

这不与 [H19 十亿残余的全严格递降闭合](type-II-h19-all-strict-descent-closure.md)
矛盾：后者允许另一张 Type II 证书或外部源承担递降。因而下一条可能成立的状态转移
不能写成“纯新证书 \(\Rightarrow\) 同证书递降”，而应允许：

\[
\text{纯新扇失败或无标记纯新证书}
\quad\Longrightarrow\quad
\text{另一来源的可验证严格递降}. \tag{5}
\]

如何由来源标签、缺口因子或支持度缺陷强制右端，仍是当前全称缺口。

## 边界

式 (3) 只排除 \(s\le1008\) 的同证书版本；它不排除更大移位、其它 Type I/II
证书、完整平方因子外源或偶源严格递降。259 个遗漏都不是原猜想反例，也不否定
“短证书或递降”的析取策略。

## 复现

~~~bash
python3 reproductions/type_ii_h19_pure_new_tail_mark_profile.py \
  --shift-cap 1008 \
  --output reproductions/type-ii-h19-pure-new-tail-mark-1b-s1008-results.json
python3 -m unittest tests/test_type_ii_h19_pure_new_tail_mark_profile.py -q
~~~
