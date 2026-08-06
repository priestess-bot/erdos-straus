---
kind: claim
claim_id: type-I-linear-escape-primary-factor-donly-no-conductor
title: 可容许 primary 因子商不产生新的 non-source D-only 双尾导体
statement: 设核心素数 p、可容许 Type II 纤维 s=AD' 满足 0<4s<p，并设实际 primary 因子积 h>1 整除 p+4s，n=(p+4s)/h 在 [2,p) 内。该因子商不产生新的 non-source D-only 双尾 E4：若 h=1 (mod 4)，既有同余类 no-go 使所有 non-source 标记纤维为空；若 h=3 (mod 4)，任何 non-source D-only 参数本身均不存在，因为它同时强制 n>4p/5 与 n<2p/3。source-supported 分支只复述既有中心 Type I 命中或空标记集。对于 h=3 (mod 4)，另有完全独立的直接 gap-h Type II 检验和有限 raw-ray 终端菜单；二者都是终端而非 D-only 递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - two-denominator-lift-d-only-marked-normal-form
  - two-denominator-lift-same-one-mod-four-no-go
  - two-denominator-lift-source-supported-tail-ratio-rigidity
  - type-II-raw-ray-certificate
topics:
- type-I
- linear-source
- escape
- primary
- source-switch
- two-tail
- D-only
- marked-lift
- no-go
- Type-II
- raw-fallback
- proof-program
sources:
  - claim: two-denominator-lift-d-only-marked-normal-form
    role: complete-D-only-parameterization
  - claim: two-denominator-lift-same-one-mod-four-no-go
    role: h-one-mod-four-non-source-no-go
  - claim: two-denominator-lift-source-supported-tail-ratio-rigidity
    role: source-supported-central-Type-I-rigidity
  - claim: type-II-raw-ray-certificate
    role: source-free-finite-raw-terminal-menu
  - reproduction: reproductions/type_i_linear_escape_primary_factor_donly_no_conductor_fixture.py
    role: constant-size h-mod-four dispatch fixture
visibility: public
last_checked: '2026-08-05'
---

# 可容许 primary 因子商不产生新的 non-source D-only 双尾导体

## 1. 范围与分派

固定核心素数 \(p\equiv1\pmod {24}\)，并取一个可容许 Type II 纤维

\[
s=AD'>0,
\qquad
D'\mid D_0,
\qquad
A\mid D',
\qquad
D'/A\text{ 平方自由},
\qquad
4s<p.
\tag{1}
\]

设一个已经通过来源账本的实际因子积满足

\[
h>1,
\qquad
h\mid p+4s,
\qquad
n=\frac{p+4s}{h},
\qquad
2\le n<p.
\tag{2}
\]

这里 \(h\) 为奇数，且 \(p+4s\equiv1\pmod4\)，所以

\[
n\equiv h\pmod4.
\tag{3}
\]

本卡只考察把 \(n\) 的两条尾保持到 \(p\) 的 D-only 参数
\(\mathcal D(p,n)\)。它不排除 raw Type II、改变保留尾、改变支撑或其它方程目标的
出口。

## 2. \(h\equiv1\pmod4\)：既有 no-go 已关闭 non-source 分支

若

\[
h\equiv1\pmod4,
\tag{4}
\]

则由 (3) 有 \(n\equiv1\pmod4\)。已有同 \(1\pmod4\) D-only 全域 no-go 给出

\[
D\in\mathcal D(p,n),
\qquad
D\nmid n^2
\Longrightarrow
W(p,n,D)=\varnothing.
\tag{5}
\]

另一支 \(D\mid n^2\) 是 source-supported；其非空性只等价于既有中心 Type I 尾谱的
命中，并不产生新的 D-only E4。因此 (4) 下本分支只输出

\[
\mathrm{PRIMARY\_TAIL\_NO\_CONGRUENCE\_CONDUCTOR}
\bigl(\mathrm{h\_mod\_1\_same\_residue\_donly\_no\_go}\bigr).
\tag{6}
\]

## 3. \(h\equiv3\pmod4\)：non-source 参数本身矛盾

现在设

\[
h\equiv3\pmod4.
\tag{7}
\]

则 \(n\equiv3\pmod4\)。反设存在 non-source D-only 参数

\[
D\in\mathcal D(p,n),
\qquad
D\nmid n^2.
\tag{8}
\]

既有 D-only 正规形强制

\[
D=p\delta,
\qquad
\delta\mid n^2.
\tag{9}
\]

由 \(D<n^2\) 与 \(n<p\) 得

\[
0<\delta<n.
\tag{10}
\]

令 \(r=p-n\)。D-only 的第一个同余为

\[
D\equiv np\pmod {4r}.
\tag{11}
\]

因为 \((p,4r)=1\)，将 (9) 代入并消去 \(p\) 后得到

\[
\delta\equiv n\pmod {4r}.
\tag{12}
\]

式 (10) 使 \(n-\delta\) 成为正的 \(4r\) 倍数，故

\[
n>4r=4(p-n),
\qquad
n>\frac{4p}{5}.
\tag{13}
\]

另一方面，(1)、(2) 与 \(h\ge3\) 给出

\[
n=\frac{p+4s}{h}<\frac{2p}{3},
\tag{14}
\]

这和 (13) 矛盾。因此

\[
\boxed{
h\equiv3\pmod4
\Longrightarrow
\not\exists D\in\mathcal D(p,n)\text{ with }D\nmid n^2.
}
\tag{15}
\]

这直接排除 non-source D-only 参数，而不只是一个数值必要门。\(n(n+1)>p\) 仅使标准
源首项的形式量 \(n(n+1)-p\) 为正；它不能代替 (15) 的同余矛盾。

## 4. 独立的直接 Type II terminal 门

仍在 (7) 的条件下，令

\[
x=\frac{p+h}{4}.
\tag{16}
\]

由 \(n\ge2\)、\(p+4s<2p\) 可知 \(h<p\)，而 \(h\) 为奇数，故

\[
3\le h\le p-2.
\tag{17}
\]

由 (2) 有

\[
x+s=\frac{h(n+1)}4,
\qquad
h\mid x+s,
\qquad
0<s<x.
\tag{18}
\]

若

\[
s\mid x^2,
\tag{19}
\]

则 \((p,s)=1\)。又 \(h\mid p+4s\) 且 \(h<p\)，故 \((h,s)=1\)。由
\(x\equiv-s\pmod h\) 得

\[
\frac{x^2}{s}\equiv s\pmod h,
\qquad
x+\frac{x^2}{s}\equiv0\pmod h.
\tag{20}
\]

所以以下两个后项均为正整数：

\[
\boxed{
\frac4p
=\frac1x
+\frac1{p(x+s)/h}
+\frac1{p(x+x^2/s)/h}.
}
\tag{21}
\]

确实，\(x+x^2/s=x(x+s)/s\)，所以

\[
\frac1{x+s}+\frac1{x+x^2/s}=\frac1x;
\tag{22}
\]

将其代入 (21) 的后两项，和为 \(1/x+h/(px)=4/p\)。这是 gap \(h\)、首分母
\(x\)、除子 \(s\) 的直接 Type II terminal。

同样在 \(h\equiv3\pmod4\) 下，可作不依赖旧来源格的有限 raw-ray 检查：

\[
\mathscr R_{\rm raw}(h;p)=
\left\{(A,C,K)\in\mathbb N^3:
ACK=\frac{h+1}{4},\quad
h\mid Kp+A,\quad
A\le\frac{Kp+A}{h}
\right\}.
\tag{23}
\]

每一行由 Type II 原始射线证书给出一个 terminal。它以 \(h\) 为原始因子，其实际
gap 由 \((A,C,K)\) 决定；不能把它误叫成“gap \(h\) 的穷尽菜单”。

## 5. 正确的 typed 分派

\[
\begin{array}{c|c}
\text{分支}&\text{结论}\\ \hline
D\nmid n^2,\ h\equiv1\pmod4&\text{(6)，non-source marked fiber 空}\\
D\nmid n^2,\ h\equiv3\pmod4&\text{(15)，non-source parameter 空}\\
D\mid n^2&\text{既有中心 Type I 命中或空标记集}\\
h\equiv3\pmod4\text{ 且 (19) 或 (23) 命中}&\text{独立 Type II terminal}
\end{array}
\tag{24}
\]

任何仍未命中的行必须改变双尾保留模式、尾比、支撑或 equation target；不能再将本类
primary 因子商登记为新的 non-source D-only E4。

## 6. 常数夹具

取

\[
p=97,
\qquad
D'=2,
\qquad
A=1,
\qquad
s=2,
\qquad
p+4s=105.
\tag{25}
\]

因子 \(h=3\) 给出 \(n=35\)，满足 (14) 而不可能满足 (13)；
\(s\nmid((p+h)/4)^2=25^2\)，其 raw-ray 菜单也为空。因子 \(h=5\) 给出
\(n=21\equiv1\pmod4\)，进入 (5) 的既有全域 no-go；raw-ray 菜单对该同余类不适用。
两项均只说明 non-source D-only 导体关闭，不否定该素数的其它证书。常数规模复现见
[primary-factor D-only no-conductor fixture](../reproductions/type_i_linear_escape_primary_factor_donly_no_conductor_fixture.py)。
