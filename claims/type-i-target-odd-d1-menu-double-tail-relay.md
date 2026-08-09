---
kind: claim
claim_id: type-i-target-odd-d1-menu-double-tail-relay
title: D=1 target-odd 菜单的 Type II 双尾严格 source relay
statement: 在 D=1 共享 q 块终端的条件 h|p+4、h=-1 (mod 4) 外，若 h+1|p-1，则令 x=(p+h)/4、Y=(x+1)/h、Z=x(x+1)/h、n=(p+h)/(h+1)。有 2<=n<p、4/n=1/x+1/Y+1/Z，且把 (x,Y,Z) 映到 (x,pY,pZ) 得到 4/p 的 Type II 证书。以这一个标记源解为 W_T、以提升后的目标解为 W_S 时，E1--E4 由显式整数恒等式通过，势 rho=n 严格下降到 p；p=73、241 的 h=7 给出正控制，而 p=241 的 h=35 虽给出直接 Type II，却因 36 不整除 240 而不能走该双尾 relay。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-i-target-odd-d1-menu-typeii-terminal
  - type-II-two-tail-deflation-descent
  - denominator-escape-state-contract
topics:
  - type-I
  - Type-II
  - target-odd
  - D-lattice
  - double-tail
  - strict-descent
  - marked-solution
  - E1-E5
  - proof-program
sources:
  - claim: type-i-target-odd-d1-menu-typeii-terminal
    role: D1-shared-q-terminal-input
  - claim: type-II-two-tail-deflation-descent
    role: double-tail-arithmetic
  - reproduction: reproductions/type_i_target_odd_d1_menu_double_tail_relay.py
    role: p73-p241-relay-controls
visibility: public
last_checked: '2026-08-09'
---

# D=1 target-odd 菜单的 Type II 双尾严格 source relay

## 输入与构造

设 (p\equiv1\pmod {24}) 为核心素数，(h>1) 满足

\[
h\mid p+4,\qquad h\equiv-1\pmod4,\qquad h+1\mid p-1.
\tag{1}
\]

令

\[
m=h,\qquad x=\frac{p+h}{4},\qquad
Y=\frac{x+1}{h},\qquad Z=\frac{x(x+1)}h,
\tag{2}
\]

以及

\[
n=\frac{p+h}{h+1}.
\tag{3}
\]

前两项条件给出 (h\mid x+1)，所以 (Y,Z\in\mathbb N)。第三项给出 n 为整数，且

\[
2\le n<p.
\tag{4}
\]

## 严格 source relay

由 D=1 Type II 终端有

\[
\frac4p
=\frac1x+\frac1{pY}+\frac1{pZ}.
\tag{5}
\]

另一方面，

\[
\frac1Y+\frac1Z
=\frac{h}{x+1}+\frac{h}{x(x+1)}
=\frac{h}{x},
\]

因此

\[
\frac1x+\frac1Y+\frac1Z
=\frac{h+1}{x}
=\frac4n,
\tag{6}
\]

其中最后一步使用 (4x=p+h) 与 (3)。故 ((x,Y,Z)) 是严格更小源 n 的一个标记
解，且映射

\[
\Phi:(x,Y,Z)\longmapsto(x,pY,pZ)
\tag{7}
\]

把它提升为目标 p 的解。

## E1--E5 回执

对这个 route-specific marked state，取

\[
W_T=\{(x,Y,Z)\},
\qquad
W_S=\{(x,pY,pZ)\},
\qquad
\rho(T)=n,
\quad \rho(S)=p.
\]

则：

* **E1**：(p,h,x,Y,Z,n) 的正性、整除和范围由 (1)--(4) 重算；
* **E2**：后继状态的 equation target 为 (4/n)，字段由 (2)--(3) 确定；
* **E3**：直接验证 (5)--(6) 和 (Phi) 的分母正整数；
* **E4**：(W_T) 是单元素标记集，(7) 对其全部元素定义且恒等式成立；
* **E5**：(n<p)，故 (ho(T)<\rho(S))。

因此这是一个合法的 `verified_edge` 模板，而不仅是“存在一个碰巧可提升的源解”。
若将 (W_T) 扩大到未标记的全部 (operatorname{Sol}(4,n))，必须重新证明全域映射；
本卡有意使用精确的单元素 marked-solution set。

## 证明

由 (4x=p+h) 和 (h\mid p+4)，有 (h\mid4(x+1))；h 奇故 (h\mid x+1)，
得到 (2) 的整性。(h+1\mid p-1) 等价于 (h+1\mid p+h)，给出 (3) 的整性。
因为 (3\le h\le p-2)，(4) 成立。式 (5) 是上一张 D=1 Type II 终端的构造，式
(6) 是直接相加，(7) 只把源后两项乘回 p。E1--E5 按定义逐项通过。证毕。

## 真实控制

### p=73、h=7

\[
x=20,quad Y=3,quad Z=60,quad n=10,quad h+1=8\mid72.
\]

\[
\frac4{10}=\frac1{20}+\frac13+\frac1{60},
\qquad
\frac4{73}=\frac1{20}+\frac1{219}+\frac1{4380}.
\]

### p=241、h=7

\[
x=62,quad Y=9,quad Z=558,quad n=31,quad h+1=8\mid240.
\]

### p=241、h=35 的 relay 失败控制

h=35 仍满足 (h\mid245) 且 (h\equiv3\pmod4)，所以给出直接 Type II 证书；但

\[
h+1=36\nmid240=p-1.
\]

故该条 route 不能使用本双尾 source relay。这个失败是精确的整除门，不是对 p=241
本身的反例，因为 h=7 route 已经通过 relay。

## 边界

本卡只覆盖 D=1、d=1 的带 (h+1\mid p-1) 子族，并且 E4 使用显式单元素标记集；
它不证明所有 D=1 terminal 都能双尾去 p，也不覆盖 D'>1、raw source 或未标记的全体源解。
剩余 direct terminal 仍可作为终端叶，未通过 (1) 的 route 必须转入其它 Type II/Type I
分支或新的严格下降构造。

## 聚焦复现

~~~bash
python3 reproductions/type_i_target_odd_d1_menu_double_tail_relay.py --verify
~~~
