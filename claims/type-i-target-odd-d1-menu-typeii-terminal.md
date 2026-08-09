---
kind: claim
claim_id: type-i-target-odd-d1-menu-typeii-terminal
title: target-odd D=1 菜单的共享 q 块到 Type II 直接终端
statement: 设核心素数 p=1 (mod 24)，且一跳 D=1、D'=A=1 的 canonical source menu 选出的奇素数幂块合成为 h>1，满足 h|p+4、h=-1 (mod 4)。则令 x=(p+h)/4、d=1，必有 d|x^2、d<=x、h|x+d，因而得到显式 Type II 证书 4/p=1/x+1/(p(x+1)/h)+1/(p x(x+1)/h)。这条 source-menu 分支是直接终端，不是递降边；p=73、241 由 h=7 命中，p=193 的 p+4 为素数则该 D=1 fan 空缺。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-i-target-odd-d-lattice-affine-menu-completion
  - short-certificate-equivalence
  - type-I-linear-escape-primary-source-switch-finite-dispatch
topics:
  - type-I
  - Type-II
  - target-odd
  - D-lattice
  - shared-q
  - direct-terminal
  - short-certificate
  - proof-program
sources:
  - claim: type-i-target-odd-d-lattice-affine-menu-completion
    role: D1-menu-source-and-prefix-block
  - claim: short-certificate-equivalence
    role: Type-II-reconstruction
  - reproduction: reproductions/type_i_target_odd_d1_menu_typeii_terminal.py
    role: p73-p241-positive-and-p193-negative-controls
visibility: public
last_checked: '2026-08-09'
---

# target-odd D=1 菜单的共享 q 块到 Type II 直接终端

## 输入

固定核心素数 (p\equiv1\pmod {24})，并取一跳 D-格的最小目标纤维

\[
D=1,\qquad D'=1,\qquad A=1.
\]

此时每个 canonical source route 的真实前缀都来自 (p+4)，目标标签为
(s=AD'=1)。把同一 profile 中选出的奇素数幂块按 shared-q ledger 合成为一个
整数 (h)。假设

\[
h>1,\qquad h\mid p+4,\qquad h\equiv-1\pmod4.
\tag{1}
\]

## 直接 Type II 终端定理

定义

\[
m=h,\qquad x=\frac{p+h}{4},\qquad d=1.
\tag{2}
\]

则 (x\in\mathbb N)，且 (3\le h\le p-2)。另外

\[
d=1\mid x^2,\qquad d\le x.
\tag{3}
\]

由 (h\mid p+4) 和 (4x=p+h)，有

\[
4(x+1)=p+h+4\equiv0\pmod h.
\]

由于 (h) 为奇数，4 可逆，故

\[
h\mid x+1=x+d.
\tag{4}
\]

于是 Type II 判据成立，得到显式分母

\[
y=\frac{p(x+1)}h,
\qquad
z=\frac{p x(x+1)}h,
\tag{5}
\]

并有

\[
\boxed{\frac4p=\frac1x+\frac1y+\frac1z.}
\tag{6}
\]

这是 `direct_type_ii` terminal：它直接证明原素数 (p) 的表示，不需要构造较小状态或
解提升边。D=1 canonical menu 只提供 E1--E3 的 source provenance；(2)--(6) 是终端
的独立 Type II verifier。

### 缺口范围

因为 (h\mid p+4) 且 (h\equiv3\pmod4)，(h\ne p+4)，后者为 (1\pmod4)。
所以 (h) 是 (p+4) 的真因子。作为奇数真因子，

\[
h\le\frac{p+4}{3}<p-2
\]

对所有核心素数成立；(h>1) 且 (h\equiv3\pmod4) 又给出 (h\ge3)。

## 与 target-odd affine menu 的接线

target-odd Fourier 相位是 (gamma=0)，而 D=1 route 的标签 (s=1) 是非零 affine
offset。对每个选中的奇 q，route 条件正是 (q^e\mid p+4s)，shared-q ledger
把这些块合并为 (h\mid p+4)。当 (1) 还满足 h 的三模四方向时，整个请求从

\[
\text{target-odd }\gamma=0
\to\text{ nonzero menu label }1
\to\text{ shared q block }h
\to\text{ Type II terminal}
\]

闭合。这里不能把不同 q 的块误当作重复同一 q；h 是一次共同混合因子，物理槽仍按
source/token 流计数。

## 证明

(p+h\equiv1+3\equiv0\pmod4) 给出 (x\in\mathbb N)。核心素数 (p\ge73)，所以
(x\ge19)，(3) 成立。由 (1) 和 (4x=p+h)，有 (h\mid4(x+1))；h 奇则得到
(4)。代入 Type II 正规形并取 (d=1)，即得 (5)--(6)。缺口范围由 h 为 p+4 的真
因子和 h 的模 4 类得到。证毕。

## 真实控制

### p=73

\[
p+4=77=7\cdot11,\qquad h=7,\qquad x=20.
\]

证书为

\[
\frac4{73}=\frac1{20}+\frac1{219}+\frac1{4380}.
\]

### p=241

\[
p+4=245=5\cdot7^2,\qquad h=7,\qquad x=62,
\]

证书为

\[
\frac4{241}=\frac1{62}+\frac1{2169}+\frac1{134478}.
\]

### p=193 的菜单外控制

\[
p+4=197
\]

是素数，没有 (h>1)、(h\equiv3\pmod4) 的 D=1 块；该最小 fan 只能输出
`D1_TYPE_II_FAN_EMPTY`，不代表 p=193 无其它 Type I/II 证书。

## 边界

本卡只闭合 (D=1)、(d=1) 的一个直接终端子族。它不覆盖 (h\equiv1\pmod4)、
D'>1 或 (A>1) 的 source menu，也不证明所有核心素数的 p+4 都含有 3 mod4 真因子。
剩余菜单必须继续接到 general Type II/raw fallback、跨 D source-switch 或严格递降。

## 聚焦复现

~~~bash
python3 reproductions/type_i_target_odd_d1_menu_typeii_terminal.py --verify
~~~
