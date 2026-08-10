---
kind: claim
claim_id: type-I-p-minus-one-equal-tail-marker-capacity-terminal-collapse
title: p-1 等尾显式标记的精确容量与单坐标终端坍缩
statement: >-
  设 p≡1 (mod 24) 为素数、B=(p-1)/4。对每个 1<=h<=B，令
  m=4h-1、c=B+h、T=2B(B+h)/h。则 (c,T,T) 是 p-1 的正单位分数解，
  当且仅当 h|2B^2；所以全部等尾显式源标记的精确容量菜单为
  H_eq(p)={h|2B^2:1<=h<=B}。对任一准入 h，保留 c 到 p 的目标解存在，
  当且仅当存在 q|c^2 使 m|4q+1 或 m|c+q；前者、后者分别是原 p 在
  gap m 的完整 Type I、Type II 菜单。因此全部这类显式单标记源在
  terminal-first 之后的新增递归容量严格为零：源不存在、目标直接终端或目标
  纤维为空三者完备分派，没有独立 E4。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - middle-coordinate-lift-certificate-equivalence
  - gap-residue-reachability
  - type-I-first-overflow-factor-pair-tail-gate-joint-obstruction
  - type-I-high-support-c2-rank-one-retention-exhaustion
topics:
  - type-I
  - type-II
  - p-minus-one
  - equal-tail-source
  - marked-solution
  - exact-capacity
  - one-coordinate-retention
  - terminal-collapse
  - strict-no-go
  - selector
sources:
  - claim: middle-coordinate-lift-certificate-equivalence
    role: one-coordinate-retention-terminal-equivalence
  - claim: type-I-first-overflow-factor-pair-tail-gate-joint-obstruction
    role: complete-p-adic-factor-split
  - reproduction: reproductions/type_i_p_minus_one_equal_tail_marker_capacity.py
    role: focused-source-admission-and-terminal-collapse-verifier
visibility: public
last_checked: '2026-08-11'
---

# \(p-1\) 等尾显式标记的精确容量与单坐标终端坍缩

## 1. 全参数设置

固定核心素数

\[
p\equiv1\pmod {24},
\qquad
B=\frac{p-1}{4}.
\tag{1}
\]

每个合法首分母缺口都可唯一写成

\[
m=4h-1,
\qquad
1\le h\le B.
\tag{2}
\]

相应首分母为

\[
c=\frac{p+m}{4}=B+h.
\tag{3}
\]

此前 gap-\(3\) 与 gap-\(7\) 的显式 \(p-1\) 源只是 (2)--(3) 的
\(h=1,2\) 两项。本卡一次性分类所有同形等尾源。

## 2. 等尾源准入的充要条件

要求

\[
\frac4{p-1}=\frac1c+\frac2T.
\tag{4}
\]

由 \(p-1=4B\) 和 \(c=B+h\)，有

\[
\frac4{p-1}-\frac1c
=
\frac1B-\frac1{B+h}
=
\frac{h}{B(B+h)}.
\tag{5}
\]

所以 (4) 唯一强制

\[
\boxed{
T=T_h=\frac{2B(B+h)}h.}
\tag{6}
\]

其整性满足

\[
\begin{aligned}
T_h\in\mathbb N
&\iff h\mid2B(B+h)\\
&\iff h\mid2B^2.
\end{aligned}
\tag{7}
\]

因此全部等尾显式标记源的精确准入菜单为

\[
\boxed{
\mathscr H_p^{\rm eq}
=
\{h\in\mathbb N:h\mid2B^2,\ 1\le h\le B\}.}
\tag{8}
\]

且容量为

\[
\boxed{
|\mathscr H_p^{\rm eq}|
=
\sum_{h\mid2B^2}\mathbf1_{h\le B}.}
\tag{9}
\]

若 \(g=(h,B)\)，写 \(h=ga,B=gb\)、\((a,b)=1\)，则 (7) 还等价于

\[
\boxed{\frac h{(h,B)}\mid2(h,B).}
\tag{10}
\]

逐素数写成

\[
\boxed{
v_\ell(h)
\le
2v_\ell(B)+\mathbf1_{\ell=2}.}
\tag{11}
\]

每个准入项都给出一张不依赖猜想归纳的显式源：

\[
\boxed{
(c,T_h,T_h)\in\operatorname{Sol}(p-1).}
\tag{12}
\]

并且

\[
\frac{T_h}{c}=\frac{2B}{h}\ge2,
\tag{13}
\]

所以 \(c\) 确实是该源解中被区分的最小坐标。

核心域中 \(B=6t\)，故 \(2B^2=72t^2\)。特别地，每个满足
\(h\mid72\)、\(h\le B\) 的固定 \(h\) 都自动进入 (8)；这统一包含
gap \(3,7,11,15,23,31,35,47,71\) 等固定切片。

## 3. 保留单坐标的目标纤维

现在固定任一 \(h\in\mathscr H_p^{\rm eq}\)，询问是否存在正整数 \(u,v\) 使

\[
\frac4p=\frac1c+\frac1u+\frac1v.
\tag{14}
\]

由 \(4c-p=m\)，二单位分数因子化给出

\[
(mu-pc)(mv-pc)=p^2c^2.
\tag{15}
\]

这里

\[
\frac p4<c\le\frac{p-1}{2}<\frac p2,
\qquad
(m,pc)=1.
\tag{16}
\]

后一互素式不需要额外假设：\(m<p\) 给出 \((m,p)=1\)；若素数
\(\ell\mid(m,c)\)，则由 \(4c=p+m\) 得 \(\ell\mid p\)，又与 \(m<p\) 矛盾。

第二个互补因子同余因而由第一个自动推出：若 \(e\equiv-pc\pmod m\)，则
\((e,m)=1\)，故 \((pc)^2/e\equiv-pc\pmod m\)。又因 \(p\nmid c\)，任一
\(e\mid p^2c^2\) 唯一写成

\[
e=p^jd,
\qquad
j\in\{0,1,2\},
\qquad
d\mid c^2.
\tag{17}
\]

使用

\[
p\equiv4c\pmod m,
\tag{18}
\]

得到

\[
pc+p^jd
\equiv
\begin{cases}
d\bigl(4(c^2/d)+1\bigr),&j=0,\\
p(c+d),&j=1,\\
4c^2(1+4d),&j=2
\end{cases}
\pmod m.
\tag{19}
\]

式中约去的因子都与 \(m\) 互素。第一、第三支在互补变换
\(d\leftrightarrow c^2/d\) 下相同；第二支独立。因此

\[
\boxed{
\begin{aligned}
c\in\operatorname{Den}(p)
\iff
\exists q\mid c^2:\quad
&m\mid4q+1\\
&\text{或 }m\mid c+q.
\end{aligned}}
\tag{20}
\]

没有第四个 \(p\)-进分支。

## 4. 两类命中的闭式恢复

若 \(q\mid c^2\) 且

\[
m\mid4q+1,
\tag{21}
\]

令

\[
d_{\rm I}=\frac{c^2}{q}.
\]

则

\[
pc+d_{\rm I}
\equiv
4c^2+\frac{c^2}{q}
=
\frac{c^2}{q}(4q+1)
\equiv0\pmod m.
\]

所以 \(d_{\rm I}\) 是原 \(p\) 的 Type I 除子，并恢复

\[
\boxed{
\left(
c,\frac{pc+d_{\rm I}}m,
\frac{p(c+pq)}m
\right)
\in\operatorname{Sol}(p).}
\tag{22}
\]

若 \(q\mid c^2\) 且

\[
m\mid c+q,
\tag{23}
\]

用互补除子可规范到 \(q<c\)：若 \(q>c\)，令 \(q'=c^2/q<c\)。由
\(q\equiv-c\pmod m\) 及 \((q,m)=(c,m)=1\)，有
\(q'=c^2q^{-1}\equiv-c\pmod m\)。等号 \(q=c\) 会迫使 \(m\mid2c\)，与
\((m,c)=1\)、\(m\ge3\) 矛盾。于是规范后的 \(q\) 是 Type II 除子，并恢复

\[
\boxed{
\left(
c,\frac{p(c+q)}m,
\frac{p(c+c^2/q)}m
\right)
\in\operatorname{Sol}(p).}
\tag{24}
\]

式 (22)、(24) 正是 gap \(m\) 的完整 Type I/II terminal 菜单，而不是新的
跨状态边。

## 5. 三态完备分派

对每个 \(1\le h\le B\)，等尾单标记路线恰落入以下一项：

\[
\boxed{
\begin{array}{c|c}
\text{条件}&\text{typed 结果}\\ \hline
h\nmid2B^2&\text{显式等尾源不存在}\\
h\mid2B^2\text{ 且 (20) 命中}&\text{原 }p\text{ 的直接 Type I/II terminal}\\
h\mid2B^2\text{ 且 (20) miss}&\text{保留 }c\text{ 的完整目标纤维为空}
\end{array}}
\tag{25}
\]

这三项无交且完备。特别地，已知源解 (12) 不能为选择器支付独立 E4：
若目标存在，式 (22) 或 (24) 已直接结束原实例；若目标不存在，则没有提升映射。
因此

\[
\boxed{
\text{全部 }p-1\text{ 等尾显式单标记在 terminal-first 后的新增递归容量为 }0.}
\tag{26}
\]

该结论只关闭显式等尾源和保留 \(c\) 的单坐标语法。它不排除标记随未知 source
解变化、改变被保留坐标、保留两个尾的其它正规形或完全重组三个坐标。

## 6. 聚焦控制

对 \(p=73\)，有 \(B=18\) 及

\[
\mathscr H_{73}^{\rm eq}
=\{1,2,3,4,6,8,9,12,18\}.
\tag{27}
\]

三种分派都有精确控制：

1. \(h=5\)：\(5\nmid648\)，所以 \(T=828/5\)，源不存在；
2. \(h=8\)：\((c,T,T)=(26,117,117)\in\operatorname{Sol}(72)\)，但
   \(26^2\) 的全部除子均避开 (20)，目标纤维为空；
3. \(h=2\)：\((20,360,360)\in\operatorname{Sol}(72)\)，而 (20) 命中并恢复
   \((20,219,4380)\in\operatorname{Sol}(73)\)，这只是 gap-\(7\) 直接终端。

\(p=97,h=1\) 另给出 terminal-first 次序控制：

\[
(25,1200,1200)\in\operatorname{Sol}(96),
\qquad
(25,970,4850)\in\operatorname{Sol}(97).
\tag{28}
\]

它说明 gap-\(3\) 可以先于 gap-\(7\) 命中，但仍服从同一个终端坍缩定理。

聚焦验证：

~~~bash
python3 reproductions/type_i_p_minus_one_equal_tail_marker_capacity.py --verify
~~~

验证器只核对 (6)--(13)、完整 \(p\)-进菜单及上述四个控制，不运行历史范围扫描。
