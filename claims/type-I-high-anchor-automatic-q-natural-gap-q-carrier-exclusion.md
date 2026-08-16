---
kind: claim
claim_id: type-I-high-anchor-automatic-q-natural-gap-q-carrier-exclusion
title: automatic-q 高锚自然 gap 的 full-excess Q-carrier 排除
statement: >-
  这是高窗口 R-1 full-excess 载体自然 gap 排除在 strict automatic-q 高锚来源上的
  推论。若第二 complete-excess bundle 为 Q=R-1，令
  delta=R-p、m=delta+1、x=(p+m)/4=(R+1)/4。则 m 是合法 Bradford gap，且
  gcd(x,Q)=1。因此任何同时满足 d|x^2 与 rad(d)|Q 的 Q-supported 除子只能为
  d=1。该 d 不可能给出 Type I；它给出 Type II 当且仅当 m|p+4。故若
  m 不整除 p+4，则这个 natural gap 上的每一张 Type I/II 证书都必须使用一个
  不整除 Q 的新素因子。该结论仅排除由 second full-excess carrier 独自支付的
  natural-gap 证书，不排除其它 gap、non-Q divisor、宏准入或 outer-rank exit。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-high-window-natural-gap-full-excess-carrier-exclusion
  - type-I-high-anchor-automatic-q-source-template
  - gap-residue-reachability
  - short-certificate-equivalence
topics:
  - Erdos-Straus
  - type-I
  - type-II
  - high-anchor
  - automatic-q
  - complete-excess
  - terminal-first
  - carrier-exclusion
  - capacity-map
  - proof-boundary
sources:
  - claim: type-I-high-anchor-automatic-q-source-template
    role: strict-source-range-and-Q-equals-R-minus-one
  - claim: gap-residue-reachability
    role: Bradford-divisor-boundary-conditions
  - reproduction: reproductions/type_i_high_anchor_automatic_q_natural_gap_q_carrier_exclusion.py
    role: two-actual-source-controls-and-sharp-d-one-control
visibility: public
last_checked: '2026-08-17'
---

# automatic-\(q\) 高锚 natural gap 的 full-excess \(Q\)-carrier 排除

## 1. 设定

取一个严格 automatic-\(q\) 高锚来源：

\[
p\equiv1\pmod {24},\qquad
p<R<4A,\qquad qA<p,\qquad q>1,
\tag{1}
\]

并且第二个 complete-excess bundle 满足

\[
Q=R-1.
\tag{2}
\]

在这个严格来源域中，\(q\in\{2,3\}\) 且
\(R\equiv3\pmod8\)。记

\[
\delta=R-p,\qquad
m=\delta+1,\qquad
x=\frac{p+m}{4}=\frac{R+1}{4}.
\tag{3}
\]

这是由 high chart 的增量 \(\delta\) 自然诱导的一个
Bradford gap。本卡只问：第二 full-excess carrier \(Q\) 自身能否
为这个 gap 支付一张证书。

这里的载体排除本身不依赖 automatic cofactor、support 或 phase。严格 source 的
\(R<2p\) 只来自 \(R<4A\) 与 \(qA<p,q>1\)，故本卡的定理现可直接视为
[高窗口 \(R-1\) full-excess 载体的自然 gap 排除](type-I-high-window-natural-gap-full-excess-carrier-exclusion.md)
在 automatic-\(q\) 域的推论；下面保留原来的 source-specific controls 与解释。

## 2. 精确排除定理

**定理。** 在 (1)--(3) 下，\(m\) 是一个合法 gap：

\[
3\le m\le p-2,\qquad m\equiv3\pmod4.
\tag{4}
\]

若正整数 \(d\) 满足

\[
d\mid x^2,\qquad \operatorname{rad}(d)\mid Q,
\tag{5}
\]

则 \(d=1\)。因此，这个 natural gap 上由 \(Q\)-supported 除子给出的
Bradford 证书存在当且仅当

\[
\boxed{m\mid p+4.}
\tag{6}
\]

如果 (6) 成立，证书必为 Type II 的 \(d=1\) 叶节点；Type I
在 (5) 下从不可能。如果 (6) 不成立，则这个 gap 上的每一张
Type I 或 Type II 证书都必须含有一个 \(\ell\nmid Q\) 的素因子。

### 证明

由 \(q\ge2\) 和 \(qA<p\)，有

\[
R<4A<2p.
\tag{7}
\]

所以 \(0<\delta<p\)。又 \(p\equiv1\pmod8\)、\(R\equiv3\pmod8\)，故

\[
\delta\equiv2\pmod8.
\tag{8}
\]

这立即给出 (4)：\(\delta\) 不可等于 \(p-1\)，因而
\(\delta\le p-3\)。并且

\[
x=\frac{R+1}{4}\quad\text{是奇数}.
\tag{9}
\]

若一个素数同时整除 \(x\) 和 \(Q=R-1\)，它也整除
\(R+1\) 与 \(R-1\)，因而整除 \(2\)。但 (9) 排除了 \(2\)，所以

\[
\gcd(x,Q)=1.
\tag{10}
\]

将 (10) 代入 (5) 立即得 \(d=1\)。

对 Type I，\(d=1\) 的整除条件为 \(m\mid px+1\)。乘以 \(4\) 并用
\(4x=p+m\)，它等价于

\[
m\mid p^2+4.
\tag{11}
\]

但 \(m\equiv3\pmod4\) 的某个素因子 \(r\) 满足
\(r\equiv3\pmod4\)；\(r\mid p^2+4\) 会使 \(-1\) 成为模 \(r\)
的平方，矛盾。所以 Type I 不可能。

对 Type II，\(d=1\) 的条件是 \(m\mid x+1\)。同样乘以
\(4\)，它正好等价于 \(m\mid p+4\)。当 (6) 成立时，
\(d=1\mid x^2\) 且 \(1\le x\)，故这是一个 Type II 证书；当 (6)
不成立时，(5) 下的唯一候选 \(d=1\) 也失败。证毕。

## 3. 对 automatic-\(q\) 出口的含义

这个结论不是说 natural gap 上没有证书。它只说，严格
automatic-\(q\) 来源已经由 second full-excess 给出的 \(Q=R-1\)
素因子不能充当这张证书的非平凡除子。因此对于

\[
m\nmid p+4,
\tag{12}
\]

任何尝试用这个 natural gap 来抢占 automatic macro 之前的 terminal
叶节点，都必须引入 \(R-1\) 之外的新素因子。也就是说，不能将
second full-excess 的既有 carrier 误认为一个充足的自动 terminal menu。

这个排除与 current outer-rank exit 互补：它不影响
\(A\mapsto qA\) 的 E5 支付，也不补上 E1--E4、terminal-first
complete menu 或全域 lift 的缺口。

## 4. 聚焦控制

两个实际 strict automatic 来源分别覆盖 \(q=2\) 和 \(q=3\)：

\[
\begin{array}{c|c|c|c|c}
p&q&R&m&x\\
\hline
3793&2&7011&3219&1753\\
60913&3&72259&11347&18065
\end{array}
\tag{13}
\]

两行都满足 \(m\nmid p+4\)，所以 (5) 下的完整
\(Q\)-supported 除子菜单都是空的。这不与它们已被更早的
gap-7 terminal-first 叶节点抢占矛盾；这里只测试一个特定 natural gap。

条件 (6) 是锐的：算术 high-window 控制

\[
p=73,\qquad R=83,\qquad m=11,\qquad x=21
\tag{14}
\]

满足 \(11\mid73+4\)，因而 \(d=1\) 给出

\[
\frac4{73}=\frac1{21}+\frac1{146}+\frac1{3066}.
\tag{15}
\]

此行只证明 (6) 的算术锐性；它不声称是 strict automatic source。

聚焦复现：

~~~bash
PYTHONPATH=reproductions python3 \
  reproductions/type_i_high_anchor_automatic_q_natural_gap_q_carrier_exclusion.py --verify
~~~
