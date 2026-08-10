---
kind: claim
claim_id: type-I-high-support-c2-rank-one-retention-exhaustion
title: 最小 C=2 偶前驱的跨图表重索引、双尾保持穷尽与 gap-7 单标记边界
statement: >-
  设 p=1 (mod 24) 为素数、n=p-1。最小高支撑 C=2 图表给出的短关系偶前驱
  正是 n。该前驱到 p 的全部 D-only 双尾保持候选可被精确穷尽：source-supported
  候选与 E 满足 4|E、E|(p-1)^2/4 的有限图表
  (R_E,K_E)=(E-1,(p(E-1)+1)/4) 自然标记一一对应；其标记纤维非空当且仅当
  该图表已有 centered Type I 命中，并可闭式恢复 Type I 短证书。所有
  non-source-supported 候选的标记纤维恒空。因此相对原 C=2 图表看似非自然的
  双尾标记，要么只是另一张 p-1 图表的自然标记并直接终端，要么严格为空，
  不产生新的递归状态。若 p-1=2^e u、u 为奇数，则图表容量精确为
  (2e-3)tau(u^2)。另外 c_7=(p+7)/4 总属于一个显式 p-1 源解；保留 c_7
  提升到 p 非空当且仅当原 p 的完整 gap-7 Type I/II 菜单命中，故也只是
  terminal-first 边界，不是独立 E4。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-high-support-c2-boundary-carry-dyadic-capacity-transduction
  - type-I-high-support-c2-centered-vieta-antipodal-no-go
  - two-denominator-lift-d-only-marked-normal-form
  - two-denominator-lift-source-supported-tail-ratio-rigidity
  - two-denominator-lift-core-rank-one-no-go
  - type-I-first-overflow-common-denominator-marked-lift
  - gap-three-criterion
  - short-certificate-equivalence
topics:
  - type-I
  - type-II
  - high-support
  - c2-boundary
  - even-predecessor
  - marked-solution
  - two-denominator-lift
  - common-denominator
  - cross-chart
  - exact-capacity
  - terminal-collapse
  - strict-no-go
sources:
  - reproduction: reproductions/type_i_high_support_c2_rank_one_retention_exhaustion.py
    role: focused-menu-bijection-empty-fiber-and-terminal-reconstruction-verifier
  - claim: gap-three-criterion
    role: prior-terminal-first-single-marker-boundary
visibility: public
last_checked: '2026-08-11'
---

# 最小 \(C=2\) 偶前驱的跨图表重索引、双尾保持穷尽与 gap-\(7\) 单标记边界

## 1. 问题与结论

固定核心素数

\[
p\equiv1\pmod {24},
\qquad n=p-1.
\tag{1}
\]

最小高支撑 \(C=2\) 图表中的内部关系

\[
\frac2{2p-1}\equiv1\pmod {2p-3}
\tag{2}
\]

已经给出算术偶前驱 \(n=p-1\)。自然标记等于

\[
A_2=\frac{(p-1)(2p-1)}8,
\tag{3}
\]

由反足 Vieta no-go，它对每个核心素数都严格为空。剩下的第一个问题是：能否在
同一个较小秩 \(n\) 上换一个标记，再通过保留两个分母的 \(D\)-only 规则提升到
\(p\)？

本卡证明答案已可完全分类。令

\[
\mathscr E_p=
\left\{
E\in\mathbb N:
4\mid E,\quad E\mid\frac{n^2}{4}
\right\}.
\tag{4}
\]

对 \(E\in\mathscr E_p\)，定义

\[
R_E=E-1,
\qquad
K_E=\frac{pR_E+1}{4}
=\frac{pE-n}{4},
\tag{5}
\]

\[
D_E=\frac{n^2}{E},
\qquad
\alpha_E=\frac{nK_E}{E}.
\tag{6}
\]

则全部可能非空的双尾保持候选恰由 (4)--(6) 给出；而且每个非空候选已经是
原 \(p\) 的直接 Type I 终端，不是新递归类型。

## 2. \(n=p-1\) 的完整 \(D\)-only 候选分拆

沿用双尾保持正规形。这里

\[
r=p-n=1,\qquad N=np,\qquad C=4,
\tag{7}
\]

所以候选集合为

\[
\mathfrak D_p=
\left\{
D:
\begin{array}{l}
D\mid p^2n^2,\quad0<D<n^2,\\
4\mid D,\quad4\mid p^2n^2/D
\end{array}
\right\}.
\tag{8}
\]

式 (8) 已经是原来两条模 \(4\) 同余的完整化简，因为 \(4\mid np\)。
又因 \((p,n)=1\)，任一 \(D\in\mathfrak D_p\) 若不含 \(p\)，便整除 \(n^2\)；
若含 \(p^2\)，则 \(4\mid D\) 会给出

\[
D\ge4p^2>(p-1)^2=n^2,
\]

与 (8) 矛盾。因此存在无交并

\[
\boxed{
\mathfrak D_p=
\mathfrak D_p^{\rm src}
\mathbin{\dot\cup}
\mathfrak D_p^{\rm ns},}
\tag{9}
\]

其中

\[
\mathfrak D_p^{\rm src}
=
\{D\mid n^2:4\mid D,\ 4\mid n^2/D\},
\tag{10}
\]

\[
\mathfrak D_p^{\rm ns}
=
\{pd:d\mid n^2,\ 4\mid d,\ 4\mid n^2/d,\ pd<n^2\}.
\tag{11}
\]

第一支就是 source-supported，第二支就是 non-source-supported；没有第三种
\(p\)-进情形。

## 3. source-supported 支精确重索引为 \(p-1\) 图表

映射

\[
\boxed{
D\longmapsto E=\frac{n^2}{D}}
\tag{12}
\]

给出自然双射

\[
\boxed{
\mathfrak D_p^{\rm src}\longleftrightarrow\mathscr E_p.}
\tag{13}
\]

事实上，(10) 的两个四整除条件正好变成

\[
4\mid E,\qquad E\mid n^2/4.
\]

反向就是 \(D=D_E=n^2/E\)。

对 \(D_E\) 应用 \(D\)-only 坐标公式，得到

\[
a_{D_E}
=\frac{np-D_E}{4}
=\frac{np}{4}-\frac{n^2}{4E}
=\frac{nK_E}{E}
=\alpha_E,
\tag{14}
\]

\[
a'_{D_E}
=\frac{p^2n^2/D_E-pn}{4}
=\frac{p^2E-pn}{4}
=pK_E.
\tag{15}
\]

同时

\[
4K_E=pR_E+1
\tag{16}
\]

且

\[
\frac{4K_E-E}{R_E}
=\frac{p(E-1)+1-E}{E-1}
=p-1=n.
\tag{17}
\]

所以 (12) 不只是除子换名。它把相对原 \(C=2\) 图表的第二层 source-supported
候选，精确改写成另一张 \((R_E,K_E)\) 图表的第一层自然 \(p-1\) 标记：

\[
\boxed{
\frac4n-\frac1{\alpha_E}
=\frac{R_E}{K_E}
=\frac4p-\frac1{pK_E}.}
\tag{18}
\]

因此相应标记纤维为

\[
W_E=
\left\{
(\alpha_E,b,c)\in\operatorname{Sol}(n):
\frac1b+\frac1c=\frac{R_E}{K_E}
\right\}.
\tag{19}
\]

原 \(C=2\) 自然标记恰是 (4) 中的一项。取

\[
E_2=2n,
\tag{20}
\]

则 \(E_2\in\mathscr E_p\)，并有

\[
R_{E_2}=2p-3=R_2,\qquad
K_{E_2}=K_2,\qquad
D_{E_2}=\frac n2,\qquad
\alpha_{E_2}=A_2.
\tag{21}
\]

反足 Vieta no-go 进一步给出：这一特定 \(E_2\) 项对每个核心素数都 miss，
不需要先假设 \(H_2(p)\) 已被分类为 F 或 G。

所以其它 \(E\ne E_2\) 的标记虽然相对 \(H_2(p)\) 是“非自然”的，却是
\(H_E(p)\) 的自然标记。它们不能作为新的、独立收费的容量单位。

## 4. 每个非空重索引都闭式坍缩为 Type I

标准二尾因子化给出

\[
\boxed{
W_E\ne\varnothing
\iff
\exists z:
z\mid K_E^2,\quad0<z<K_E,\quad
z\equiv-K_E\pmod {R_E}.}
\tag{22}
\]

若最初命中的除子大于 \(K_E\)，取互补因子 \(K_E^2/z\) 即得到 (22) 的规范
小除子。等号 \(z=K_E\) 不可能，因为 \((R_E,K_E)=1\) 且 \(R_E\ge3\)。

给定 (22)，定义

\[
x=\frac{K_E+z}{R_E},
\qquad
y=\frac{K_E+K_E^2/z}{R_E},
\qquad
m=\frac{4z+1}{R_E},
\qquad
d=\frac{x^2}{z}.
\tag{23}
\]

这些量全部为正整数。对 \(d\)，由

\[
R_Ex\equiv K_E\pmod z,\qquad z\mid K_E^2,\qquad(R_E,z)=1
\]

得到 \(z\mid x^2\)；这里 \((R_E,z)=1\) 直接来自
\((R_E,K_E)=1\) 与 \(z\mid K_E^2\)。又有

\[
mK_E-pz
=\frac{(4z+1)K_E-pzR_E}{R_E}
=\frac{K_E+z}{R_E}
=x.
\tag{24}
\]

而 \(y=K_Ex/z\)，所以

\[
my-px=\frac{x(mK_E-pz)}z=\frac{x^2}{z}=d.
\tag{25}
\]

于是

\[
d\mid x^2,\qquad m\mid px+d,
\tag{26}
\]

并且

\[
\boxed{
\frac4p=\frac1x+\frac1y+\frac1{pK_E}.}
\tag{27}
\]

最后，

\[
\frac p4<x<\frac p2+\frac1{2R_E},
\]

故整数 \(x\le(p-1)/2\)，从而

\[
3\le m=4x-p\le p-2,\qquad m\equiv3\pmod4.
\tag{28}
\]

所以 \((m,x,d)\) 是一张合法 Type I 短证书。反方向由任意
\((\alpha_E,b,c)\in W_E\) 的二尾因子化恢复 (22)。因此

\[
\boxed{
W_E\ne\varnothing
\iff
(R_E,K_E)\text{ centered Type I 命中}
\iff
\text{式 (23)--(28) 给出直接 Type I 终端}.}
\tag{29}
\]

## 5. non-source-supported 支全空

对 \(D\in\mathfrak D_p^{\rm ns}\)，rank-one no-go 已给出无条件结论

\[
\boxed{W(p,p-1,D)=\varnothing.}
\tag{30}
\]

其证明不是有限测试。该支唯一可正规化为

\[
\mu=4\lambda-1,\qquad
H=p+\mu\mid4\lambda^2,\qquad
0<s=\frac{4\lambda^2}{H}<\lambda.
\tag{31}
\]

写

\[
s=a^2c,\qquad\lambda=abc,\qquad(a,b)=1,\quad a<b,
\tag{32}
\]

两个规范平方除子目标由大小排除；剩余目标若命中，会导出正整数方程

\[
4ah=\frac{a^2}{u}+\frac{h^2}{v}+\frac1c.
\tag{33}
\]

对 \(a+h\) 极小的正解作 Vieta 跳跃会产生更小正解，矛盾。故 (30) 对每个
\(p\equiv1\pmod4\) 都成立，尤其覆盖当前核心域。

结合 (13)、(29)、(30)，得到本卡的主穷尽式：

\[
\boxed{
\begin{array}{c}
\text{全部 }(p-1)\to p\text{ 双尾保持 }D\text{-only 候选}\\[2mm]
=
\text{有限跨图表 centered Type I 终端菜单}
\ \dot\cup\
\text{严格空 non-source 菜单}.
\end{array}}
\tag{34}
\]

这里没有 candidate transition 或新的 marked 递归状态。

## 6. 精确容量

写

\[
n=2^e u,\qquad u\text{ 为奇数},\qquad e\ge3.
\tag{35}
\]

在 (4) 中，\(E\) 的二进指数可以且只能取

\[
2,3,\ldots,2e-2,
\]

共 \(2e-3\) 个值；奇部可取 \(u^2\) 的任意除子。因此

\[
\boxed{
|\mathscr E_p|=(2e-3)\tau(u^2).}
\tag{36}
\]

这是 \(C=2\) 偶前驱上全部 source-supported 双尾保持容量的精确计数。它计算的是
候选图表数，不是命中数；(22) 仍可能对全部图表同时 miss。

## 7. 保留一个分母的 gap-\(7\) 边界

双尾保持已由 (34) 穷尽。单分母保留必须继续服从全局 terminal-first 次序；尤其

\[
c_3=\frac{p+3}{4},
\qquad
T_3=\frac{(p-1)(p+3)}8,
\qquad
\frac4{p-1}=\frac1{c_3}+\frac1{T_3}+\frac1{T_3}
\]

给出比 gap-\(7\) 更小的普适源切片，而且可能直接提升：例如
\((25,1200,1200)\in\operatorname{Sol}(96)\)，而
\((25,970,4850)\in\operatorname{Sol}(97)\)。因此下面不声称 gap-\(7\) 最小，
只分析另一个方便且在当前控制中命中的固定切片：

\[
c_7=\frac{p+7}{4},
\qquad
T_7=\frac{(p-1)(p+7)}{16}.
\tag{37}
\]

核心同余保证二者为正整数，且

\[
\boxed{
\frac4{p-1}=\frac1{c_7}+\frac1{T_7}+\frac1{T_7}.}
\tag{38}
\]

于是源标记切片总非空。但是，把同一个 \(c_7\) 保留到目标 \(p\) 的条件正好是

\[
c_7\in\operatorname{Den}(p).
\tag{39}
\]

因为 \(4c_7-p=7\)，式 (39) 等价于原 \(p\) 的完整 gap-\(7\) Type I/II
因子菜单命中。这里 \(p\nmid c_7\)，且 \(7\nmid c_7\)：否则
\(p=4c_7-7\) 会迫使核心素数 \(p\) 被 \(7\) 整除。目标双因子门的因子与互补因子
对称，所以可把 \(p\)-进指数规范为 \(0\) 或 \(1\)，写成 \(q\) 或 \(pq\)，其中
\(q\mid c_7^2\)。在第一种情形把 \(q\) 换成其互补因子 \(c_7^2/q\)，并使用
\(p\equiv4c_7\pmod7\)；两种同余便分别化成下面两项：

\[
\boxed{
c_7\in\operatorname{Den}(p)
\iff
\exists q\mid c_7^2:
7\mid4q+1\ \text{或}\ 7\mid c_7+q.}
\tag{40}
\]

命中 (40) 已经直接恢复目标的两条尾分母。因此 (37)--(40) 是一张有用的
terminal-first adapter，却不是独立于 gap-\(7\) 终端的 E4。

这不排除保留其它、随 source 解变化的一个分母，也不排除完全重组三个坐标的
映射；它只证明最自然的固定 gap-\(7\) 单标记没有绕过原终端问题。

## 8. 两个完整控制

对 \(p=73\)，有 \(n=72=2^3\cdot3^2\)，所以

\[
|\mathscr E_{73}|=3\cdot5=15.
\]

完整 centered 菜单只有 \(E=4,24\) 命中，共给出四张规范证书：

\[
\begin{array}{c|c|c|c|c}
E&z&m&x&d\\ \hline
4&5&7&20&80\\
4&11&15&22&44\\
24&40&7&20&10\\
24&63&11&21&7
\end{array}
\tag{41}
\]

原 \(C=2\) 项 \(E_2=144\) miss。完整 \(D\)-only 集有 22 项，其中 15 项
source-supported、7 项 non-source-supported；后 7 项的标记纤维全部为空。
单标记控制为

\[
(20,360,360)\in\operatorname{Sol}(72)
\longmapsto
(20,219,4380)\in\operatorname{Sol}(73).
\tag{42}
\]

对 \(p=193\)，有 \(n=192=2^6\cdot3\)，所以

\[
|\mathscr E_{193}|=9\cdot3=27.
\]

完整 centered 菜单只有 \(E=4,8,144\) 命中，共有四张规范证书：

\[
\begin{array}{c|c|c|c|c}
E&z&m&x&d\\ \hline
4&5&7&50&500\\
4&29&39&58&116\\
8&26&15&52&104\\
144&250&7&50&10
\end{array}
\tag{43}
\]

原 \(C=2\) 项 \(E_2=384\) miss。完整 \(D\)-only 集有 40 项，其中 27 项
source-supported、13 项 non-source-supported；后 13 项的标记纤维全部为空。
单标记控制为

\[
(50,2400,2400)\in\operatorname{Sol}(192)
\longmapsto
(50,1380,1331700)\in\operatorname{Sol}(193).
\tag{44}
\]

这些控制同时展示三种不同状态：原 \(C=2\) chart miss、另一个
\(p-1\) chart Type I 命中、以及独立 gap-\(7\) terminal-first 命中。

## 9. 对统一选择器的推进

最小 \(C=2\) 边界的分派现在应更新为：

1. 进入该边界前先运行标准短证书菜单，特别包括 gap-\(3\)；命中即 terminal-first
   终止；
2. 未被抢占的 **CARRY_NO_GO** 状态登记短关系偶前驱 \(n=p-1\)，但不再创建未分类的
   \(D\)-only 递归分支；
3. 枚举 (4) 的有限重索引菜单，命中 (22) 时立即输出 (23)--(28) 的 Type I
   证书；
4. 菜单 miss 时，(30) 已同时删除全部真正 non-source 双尾候选；
5. gap-\(7\) 单标记只按 terminal-first 运行；其 source 非空不支付新的 E4；
6. 此后仍未决的出口必须改变保留尾、使用随 source 变化的单坐标映射、完全重组
   三个坐标，或在进入边界前由 alternate/dual/total-cofactor/paid reset 抢占。

因此，上一张 C=2 主张中“构造 \(p-1\) 的非自然标记”现在必须加上严格限定：
任何仍有新数学内容的标记都不能属于双尾保持 \(D\)-only 语法。式 (34) 是一条
真正的适配器 no-go，同时 (13) 和 (36) 给出没有重复计容的跨图表容量映射。

聚焦验证：

~~~bash
python3 reproductions/type_i_high_support_c2_rank_one_retention_exhaustion.py --verify
~~~

验证器只重算 \(p=73,193\) 的完整小型 \(D\)-only/图表菜单、non-source 空纤维、
Type I 恢复式和 gap-\(7\) 两个控制，不运行历史范围扫描。
