---
kind: claim
claim_id: type-I-high-window-natural-gap-full-excess-carrier-exclusion
title: 高窗口 R 减一 full-excess 载体的自然 gap 排除
statement: >-
  对核心素数 p=1 (mod 24)，若 p<R<2p、R=3 (mod 8)，并有 actual full-excess
  carrier Q=R-1，令 m=R-p+1、x=(R+1)/4。则 m 是合法 Bradford gap，且所有满足
  d|x^2、rad(d)|Q 的除子只能为 d=1。该除子从不构成 Type I；它构成 Type II
  当且仅当 m|p+4。因此若 m 不整除 p+4，natural gap 的任何 Type I/II 证书都必须
  使用 Q 外的素因子。该定理不需要 automatic-q gate、support A 或 phase；严格
  automatic-q Q=R-1 来源只是其推论。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - gap-residue-reachability
  - short-certificate-equivalence
topics:
  - Erdos-Straus
  - type-I
  - type-II
  - high-anchor
  - high-window
  - complete-excess
  - terminal-first
  - carrier-exclusion
  - capacity-map
  - proof-boundary
sources:
  - claim: gap-residue-reachability
    role: Bradford Type-I/II divisor conditions at a fixed gap
  - reproduction: reproductions/type_i_high_window_natural_gap_carrier_exclusion.py
    role: non-automatic full-excess control, automatic-q corollaries, and sharp Type-II control
visibility: public
last_checked: '2026-08-17'
---

# 高窗口 \(R-1\) full-excess 载体的自然 gap 排除

## 1. 比 automatic-q 更宽的设定

固定核心素数

\[
p\equiv1\pmod {24}.
\]

这里只取一个 high-window chart side \(R\)，并假设

\[
p<R<2p,\qquad R\equiv3\pmod8,\qquad Q=R-1.
\tag{1}
\]

当某个 actual complete-excess receipt 的 carrier 恰为 \(Q\) 时，(1) 就是它的
\(R-1\) full-excess carrier。定义自然 gap 和相应首分母

\[
m=R-p+1,\qquad
x=\frac{p+m}{4}=\frac{R+1}{4}.
\tag{2}
\]

本卡只问 carrier \(Q\) 本身能否为 gap \(m\) 支付 Bradford 除子证书。它不假定
automatic cofactor \(C=qA\)，也不假定任何 parent、phase 或递归宏。

## 2. 全称载体排除

**定理。** 在 (1)--(2) 下，

\[
3\le m\le p-2,\qquad
m\equiv3\pmod4.
\tag{3}
\]

若正整数 \(d\) 满足

\[
d\mid x^2,\qquad
\operatorname{rad}(d)\mid Q,
\tag{4}
\]

则 \(d=1\)。这个唯一候选永远不是 Type I 证书；它是 Type II 证书当且仅当

\[
\boxed{m\mid p+4.}
\tag{5}
\]

因而当 (5) 失败时，gap \(m\) 的任意 Type I 或 Type II 证书都含有某个
\(\ell\nmid Q\) 的素因子。

### 证明

令 \(\delta=R-p\)。由 (1) 得 \(0<\delta<p\)，而

\[
\delta\equiv R-p\equiv2\pmod8.
\tag{6}
\]

因为 \(p-1\equiv0\pmod8\)，\(\delta\) 不可能等于 \(p-1\)。于是
\(\delta\le p-3\)，这给出 (3)。同时 \(x=(R+1)/4\) 是奇数。

若某个素数同时整除 \(x\) 与 \(Q\)，它整除 \(R+1\) 与 \(R-1\)，故整除 \(2\)；
但 \(x\) 为奇数。因此

\[
(x,Q)=1.
\tag{7}
\]

式 (4) 立即给 \(d=1\)。对 Type I，剩余整除条件为

\[
m\mid px+1
\quad\Longleftrightarrow\quad
m\mid p^2+4,
\tag{8}
\]

其中等价性来自 \(4x=p+m\)。任意 \(3\pmod4\) 的奇数 \(m\) 都含有一个
\(3\pmod4\) 素因子 \(r\)。若 \(r\mid p^2+4\)，则
\((p/2)^2\equiv-1\pmod r\)，与 \(r\equiv3\pmod4\) 矛盾。故 Type I 不可能。

对 Type II，\(d=1\) 的条件为

\[
m\mid x+1
\quad\Longleftrightarrow\quad
m\mid p+4,
\tag{9}
\]

再次只须乘以 \(4\)。这证明 (5) 及结论。证毕。

## 3. 与 automatic-q 的关系

严格 automatic-q high source 满足 \(p<R<4A\) 和 \(qA<p\)、\(q>1\)，所以

\[
R<4A<2p.
\tag{10}
\]

其 two-anchor \(Q=R-1\) 子族还已有 \(R\equiv3\pmod8\)。因此
[automatic-q 高锚自然 gap 的 full-excess Q-carrier 排除](type-I-high-anchor-automatic-q-natural-gap-q-carrier-exclusion.md)
只是本定理在该来源域中的推论。

新增范围并非形式上的：

\[
(p,A,R)=(1033,351,1211)
\tag{11}
\]

是一个 actual high-R full-excess control，第二 bundle 为

\[
Q=1210=R-1,\qquad\beta=1,
\tag{12}
\]

但其 rechart cofactor 为 \(C=968\)，不是 \(A=351\) 的整数倍，因而不属于
automatic \(C=qA\) 子族。这里

\[
m=179,\qquad x=303,\qquad179\nmid1037,
\tag{13}
\]

故它的完整 \(Q\)-supported natural-gap 菜单为空。

## 4. 锐性与边界

条件 (5) 是锐的。high-window 算术控制

\[
(p,R,m,x)=(73,83,11,21)
\tag{14}
\]

满足 \(11\mid73+4\)，所以 \(d=1\) 给出 Type II 叶：

\[
\frac4{73}=\frac1{21}+\frac1{146}+\frac1{3066}.
\tag{15}
\]

本定理不排除 natural gap 中使用 \(Q\) 外素因子的证书，不排除其它 gap，也不提供
parent provenance、terminal-first complete menu、全域解提升或严格递降。它的作用是把
\(R-1\) full-excess carrier 单独可支付的自然 terminal 精确压缩为 (5)。

聚焦复现：

~~~bash
PYTHONPATH=reproductions python3 \
  reproductions/type_i_high_window_natural_gap_carrier_exclusion.py --verify
~~~
