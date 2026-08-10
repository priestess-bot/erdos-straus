---
kind: claim
claim_id: type-I-first-overflow-factor-pair-tail-gate-joint-obstruction
title: first-overflow 商倍数的因子配对、规范尾精确门与四菜单联合障碍
statement: >-
  对合法 first-overflow 数据 2p=Mn-m、n<p，令 Delta=p^2+4n。每个
  quotient-multiple 候选 r_k=4kn-p 命中当且仅当 r_k|Delta；命中与
  Delta 中所有不超过 p 且等于 -p mod 4n 的因子一一对应，并产生两个同余因子的
  规范配对。特别地，n 为平方时整个 quotient-multiple 菜单严格为空，并存在无穷多
  合法核心素数控制。另一方面，若 p 不整除 c 且 4c>p，则共同分母目标门 E_p(c)
  非空当且仅当某个 d|c^2 满足 4c-p|4d+1 或 4c-p|c+d；这给出两条规范 source tail 的完整而非
  仅充分判据。合法控制 (p,M,y,m,n)=(193,27,53,19,15) 的自然 Bradford 菜单、
  quotient-multiple 菜单和两条规范尾完整目标门同时为空，严格否定这四个局部菜单的
  全称覆盖。p=193 另有 (m,d)=(7,20) 的直接 Type II 终端，因此该控制是
  terminal-preempted 的局部反例，不是猜想或 terminal-first 全局选择器的反例。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-first-overflow-common-denominator-marked-lift
  - type-I-fg-qprefix-block-bound-first-overflow-terminal
  - short-certificate-equivalence
  - marked-solution-descent-closure
topics:
  - type-I
  - first-overflow
  - quotient-multiple
  - factor-pair
  - common-denominator
  - canonical-tail
  - strict-obstruction
  - exact-gate
  - candidate-transition
sources:
  - claim: type-I-first-overflow-common-denominator-marked-lift
    role: original-quotient-menu-and-common-denominator-target-gate
  - claim: short-certificate-equivalence
    role: Bradford-Type-I-II-reconstruction
  - reproduction: reproductions/type_i_first_overflow_factor_pair_tail_joint_obstruction.py
    role: focused-factor-pair-square-no-go-tail-gate-and-p193-joint-obstruction-verification
visibility: public
last_checked: '2026-08-10'
---

# first-overflow 商倍数的因子配对、规范尾精确门与四菜单联合障碍

## 1. 范围与记号

保留合法 first-overflow 数据

\[
m=4y-p,\qquad nM=p+4y=2p+m,\qquad 2p=Mn-m,
\tag{1}
\]

其中 \(p\equiv1\pmod4\) 为素数，\(M\ge3\) 为奇数，\((M,p)=1\)，且
\(0<m<p\)、\(n<p\)。定义

\[
\mathcal K(p,n)=\{k\in\mathbb N:p<4kn\le2p\},
\qquad r_k=4kn-p,
\tag{2}
\]

以及

\[
\Delta=\Delta(p,n):=p^2+4n
=\frac{(Mn-m)^2+16n}{4}.
\tag{3}
\]

本卡只压缩 (2) 的 quotient-multiple Type I 菜单和两条既有规范 source tail。
它不声称这些局部菜单已经覆盖 terminal-first 之后的全部状态。

## 2. quotient-multiple 因子定理

对每个 \(k\in\mathcal K(p,n)\)，有精确等价

\[
\boxed{
r_k\mid kp+1
\quad\Longleftrightarrow\quad
r_k\mid4k^2n+1
\quad\Longleftrightarrow\quad
r_k\mid\Delta.}
\tag{4}
\]

事实上 \(p\equiv4kn\pmod {r_k}\)，给出第一个等价。又

\[
\Delta\equiv(4kn)^2+4n
=4n(4k^2n+1)\pmod {r_k}.
\tag{5}
\]

由 \((p,n)=1\) 得 \((r_k,4n)=1\)，故可约去 (5) 中的 \(4n\)。结合既有
quotient-multiple 恢复式，(4) 命中时 \((r_k,d=n)\) 是 Type I 短证书。

在 \((M,m,n)\) 坐标中，

\[
2r_k=m+(8k-M)n.
\tag{6}
\]

因此定义

\[
\mathcal D(M,m,n)=
\left\{d\in\mathbb N:
\begin{array}{l}
d\mid\Delta,\\
2d\le Mn-m,\\
2d+Mn-m\equiv0\pmod {8n}
\end{array}
\right\}.
\tag{7}
\]

则映射

\[
\boxed{k\longmapsto r_k}
\tag{8}
\]

把 quotient-multiple 命中双射到 \(\mathcal D(M,m,n)\)，逆映射为

\[
\boxed{
k_d=\frac{2d+Mn-m}{8n}=\frac{d+p}{4n}.}
\tag{9}
\]

等价地，命中恰由以下有界因子刻画：

\[
\boxed{
d\mid p^2+4n,\qquad 1\le d\le p,
\qquad d\equiv-p\pmod {4n}.}
\tag{10}
\]

式 (10) 的逆向确实落在 (2)：\(4nk=d+p>p\)，且 \(d\le p\) 给出
\(4nk\le2p\)。此外 \(p\nmid\Delta\)，所以边界 \(d=p\) 实际不会发生。

## 3. 同余因子配对与局部降次

若 \(d=r_k\) 是 (10) 的命中因子，令 \(d^\vee=\Delta/d\)。因为
\((d,4n)=1\)，由

\[
dd^\vee\equiv p^2\pmod {4n},
\qquad d\equiv-p\pmod {4n}
\]

得到

\[
d^\vee\equiv-p\pmod {4n}.
\tag{11}
\]

故

\[
\ell=\frac{d^\vee+p}{4n}\in\mathbb N,
\qquad \ell>k,
\]

并有规范因子配对

\[
\boxed{
p^2+4n=(4kn-p)(4n\ell-p),
\qquad kp+1=\ell(4kn-p).}
\tag{12}
\]

反之，每个满足 (12) 的同余因子对唯一恢复一个命中。因此

\[
\#\{\text{quotient-multiple hits}\}
=\#\{d\mid\Delta:d\le p,\ d\equiv-p\pmod {4n}\}.
\tag{13}
\]

还可在不分解 \(\Delta\) 时作一次局部降次。置 \(t_k=M-8k\)。由
\(t_kn\equiv m\pmod {r_k}\) 有

\[
t_k(4k^2n+1)\equiv4k^2m+t_k\pmod {r_k},
\qquad
(t_k,r_k)=(t_k,m).
\tag{14}
\]

所以当 \((M-8k,m)=1\) 时，

\[
\boxed{
r_k\mid kp+1
\quad\Longleftrightarrow\quad
r_k\mid4k^2m+M-8k.}
\tag{15}
\]

## 4. 平方商菜单空性定理

若

\[
n=s^2,
\tag{16}
\]

则整个 quotient-multiple 菜单为空。此时

\[
\Delta=p^2+(2s)^2
\tag{17}
\]

是本原平方和，因为 \(n<p\) 蕴含 \((p,2s)=1\)。若素数
\(q\equiv3\pmod4\) 整除 (17)，平方和定理强制 \(q\mid p\) 且 \(q\mid2s\)，矛盾。
而 \(\Delta\) 为奇数，所以它的每个素因子、进而每个正因子都等于 \(1\pmod4\)。
另一方面每个候选 \(r_k\equiv-p\equiv3\pmod4\)，故 (4) 不可能命中。

这不是孤立数值现象。固定 \(s\ge5\)、\((s,6)=1\)，由 CRT 取唯一剩余类

\[
a_s\equiv1\pmod {24},
\qquad 2a_s+3\equiv0\pmod {s^2}.
\tag{18}
\]

该类与 \(24s^2\) 互素，故 Dirichlet 算术级数素数定理给出无穷多个
\(p\equiv a_s\pmod {24s^2}\) 的素数。对充分大的这些 \(p\)，令

\[
m=3,\qquad n=s^2,\qquad M=\frac{2p+3}{s^2},
\tag{19}
\]

并取

\[
y=\frac{p+3}{4}.
\]

则 \(M\) 为奇数。若 \(p\mid M\)，由 \(Mn=2p+3\) 会有 \(p\mid3\)，与
\(p>3\) 矛盾，故 \((M,p)=1\)。又 \(p\equiv1\pmod3\)、\(s^2\equiv1\pmod3\)，
所以 \(M\equiv2\pmod3\)。任一 \(M,y\) 的公因子同时整除
\(4y=p+3\) 与 \(Mn=2p+3\)，因而整除 \(3\)；结合 \(3\nmid M\) 得
\((M,y)=1\)。

对充分大的 \(p\)，\(M\ge3\)、\(n=s^2<p\)，且

\[
y-M=\frac{p(s^2-8)+3s^2-12}{4s^2}>0,
\]

并有

\[
4(y-M)=p+3-4M<p<4y=p+3.
\]

所以 \(y-M\) 是前一个严格 owner-window 标签，\(y\) 是首个 overflow 标签，
(1) 的全部算术合法性条件成立。当 \(p>4s^2\) 充分大时，(2) 的区间长度
\(p/(4s^2)>1\)，故 \(\mathcal K(p,n)\ne\varnothing\)，而其全部候选仍由
(16)--(17) 排除。

一个小控制是

\[
(p,M,y,m,n)=(2161,173,541,3,25),
\]

其中 \(p\) 为素数，

\[
\Delta=4670021=193\cdot24197,
\]

两个素因子均为 \(1\pmod4\)，且 \(\mathcal K(2161,25)=\{22,\ldots,43\}\)
完整为空。另一个菜单串联控制为

\[
(p,M,y,m,n)=(73,21,29,43,9).
\tag{20}
\]

这里 gap-\(43\) 自然 Bradford 菜单与 \(M=27\) 控制相同而为空，随后
\(\mathcal K(73,9)=\{3,4\}\) 给出 \(r_k=35,71\)，也因平方商定理全部失败。
相反，既有正控制 \((p,M,m,n)=(73,27,43,7)\) 满足

\[
\Delta=5357=11\cdot487,
\]

两个因子都等于 \(-73\pmod {28}\)；\(d=11\) 在 (9) 中给出
\((k,\ell)=(3,20)\)。

## 5. 共同分母目标门的精确 \(p\)-free 约化

沿用既有定义 \(\mathcal E_p(c)\)。设 \(p\nmid c\)，且

\[
R=4c-p>0.
\tag{21}
\]

则有新的精确约化

\[
\boxed{
\mathcal E_p(c)\ne\varnothing
\quad\Longleftrightarrow\quad
\exists d\mid c^2:\quad
R\mid4d+1\ \text{或}\ R\mid c+d.}
\tag{22}
\]

证明如下。由 \((R,pc)=1\)，\(\mathcal E_p(c)\) 的第二个互补因子同余由第一个自动
推出。每个 \(e\mid p^2c^2\) 唯一写成 \(e=p^jd\)，其中
\(j\in\{0,1,2\}\)、\(d\mid c^2\)。又 \(p\equiv4c\pmod R\)，所以

\[
pc+p^jd\equiv
\begin{cases}
4c^2+d=d\bigl(4(c^2/d)+1\bigr),&j=0,\\
p(c+d),&j=1,\\
4c^2(1+4d),&j=2
\end{cases}
\pmod R.
\tag{23}
\]

式中被约去的因子都与 \(R\) 互素；\(j=0,2\) 在 \(d\leftrightarrow c^2/d\)
下给出同一个 \(R\mid4d+1\) 族，\(j=1\) 给出 \(R\mid c+d\) 族，证毕。

记

\[
\mathscr H(c)=
\bigcup_{d\mid c^2}
\left(\operatorname{Div}(4d+1)\cup\operatorname{Div}(c+d)\right).
\tag{24}
\]

对 first-overflow 中任意 \(c=nB\)，

\[
R=\frac{n(8B-M)+m}{2},
\qquad 2R\equiv m\pmod n,
\qquad R\equiv3\pmod4.
\tag{25}
\]

若 \(p\nmid nB\)，则

\[
\boxed{
\mathcal E_p(nB)\ne\varnothing
\quad\Longleftrightarrow\quad
R>0\ \text{且}\ R\in\mathscr H(nB).}
\tag{26}
\]

等价地，固定 \(n,m,B\) 后的所有命中载体满足

\[
M=8B+\frac{m-2R}{n},
\quad R\in\mathscr H(nB),
\quad2R\equiv m\pmod n,
\quad R\equiv3\pmod4,
\tag{27}
\]

并另行保留 (1) 的合法性条件。

## 6. 两条规范 source tail 的完整门

若 \(n\equiv7\pmod8\)，置

\[
a=\frac{3(n+1)}8,\qquad c_1=na,
\qquad
R_1=\frac{n(3(n+1)-M)+m}{2}.
\tag{28}
\]

此时 \(a<p\) 且 \(p\nmid n\)，所以 \(p\nmid c_1\)。当 \(R_1>0\) 时，(22)
给出 \(c_1\) 的完整目标门。旧充分见证 \(e=n\) 则进一步精确等价于

\[
\boxed{R_1\mid K_1:=4na^2+1.}
\tag{29}
\]

因为 \(4c_1^2+n=nK_1\)，且 \((R_1,n)=1\)。若写 \(q=K_1/R_1\)，则

\[
mq\equiv2\pmod n,
\qquad
M=3(n+1)+\frac{m-2K_1/q}{n}.
\tag{30}
\]

在核心域中 \(R_1\equiv q\equiv3\pmod4\)。注意 (29) 只分类固定的 \(e=n\)
子族；完整门仍是 (22) 的两个除子族。

若 \(n\equiv3\pmod4\)，置

\[
u=\frac{n+1}{4},\qquad T=nu,\qquad
B=u(nu+1),\qquad c_2=nB=T(T+1),
\tag{31}
\]

则

\[
R_2=\frac{n(8B-M)+m}{2}.
\tag{32}
\]

若 \(p\nmid c_2\) 且 \(R_2>0\)，旧式 (33) 的全部 \(p\)-free 见证恰为

\[
\exists d\mid c_2^2:\quad R_2\mid4d+1,
\tag{33}
\]

而完整目标门还且只增加

\[
\exists d\mid c_2^2:\quad R_2\mid c_2+d.
\tag{34}
\]

## 7. \(p=193,M=27\) 的四菜单联合障碍

取

\[
(p,M,y,m,n)=(193,27,53,19,15).
\tag{35}
\]

这里 \(193\equiv1\pmod {24}\)，\(b=y-M=26\) 满足 \(4b<193<4y\)，且

\[
15\cdot27=2\cdot193+19,
\qquad (M,y)=1.
\]

因此这是合法 first-overflow 控制。

自然 Bradford 菜单为空。\(y^2\) 的全部除子为 \(1,53,2809\)，Type I 残数

\[
(py+d)\bmod19=8,3,4,
\]

而满足 \(d\le y\) 的 Type II 候选 \(d=1,53\) 给出

\[
(y+d)\bmod19=16,11.
\tag{36}
\]

quotient-multiple 菜单也为空：

\[
\mathcal K(193,15)=\{4,5,6\},
\qquad (r_4,r_5,r_6)=(47,107,167),
\]

且相应的 \((kp+1)\bmod r_k\) 为

\[
21,3,157.
\tag{37}
\]

等价地，\(\Delta=37309\) 为素数，没有 (10) 所需的有界同余因子。

因 \(15\equiv7\pmod8\)，两条规范尾同时存在。第一条有

\[
c_1=90,\qquad R_1=167,\qquad c_1^2=8100,
\]

而每个 \(d\mid c_1^2\) 唯一写成

\[
d=5^jA,\qquad 0\le j\le2,\quad A\mid324.
\]

式 (22) 要求 \(d\equiv125\) 或 \(77\pmod {167}\)。在每个 \(j\) 下，区间
\(1\le A\le324\) 中仅有以下可能：

| \(j\) | 来自 \(d\equiv125\) 的 \(A\) | 来自 \(d\equiv77\) 的 \(A\) |
|---:|---|---|
| 0 | \(125,292\) | \(77,244\) |
| 1 | \(25,192\) | \(149,316\) |
| 2 | \(5,172\) | \(130,297\) |

没有一项整除 \(324\)，故

\[
\mathcal E_{193}(90)=\varnothing.
\tag{38}
\]

第二条有

\[
c_2=3660,\qquad R_2=14447,\qquad c_2^2=13395600,
\]

而每个 \(d\mid c_2^2\) 唯一写成

\[
d=61^jA,\qquad0\le j\le2,\quad A\mid3600.
\]

式 (22) 的两个必要剩余类为

\[
d\equiv10835\quad\text{或}\quad10787\pmod {14447}.
\tag{39}
\]

当 \(j=0\) 时 \(d=A\le3600\)，小于两个正代表。若 \(j=1\)，写
\(d=t+kR_2\)，则 \(0\le k\le14\)，而 \(61\mid d\) 分别强制

\[
k\equiv16\quad\text{或}\quad60\pmod {61},
\]

不可能。若 \(j=2\)，同理 \(0\le k\le926\)，而 \(61^2\mid d\) 分别强制

\[
k\equiv3005\quad\text{或}\quad3354\pmod {3721},
\]

仍不可能。因此

\[
\mathcal E_{193}(3660)=\varnothing.
\tag{40}
\]

综合 (36)--(40)，命题

\[
\text{自然菜单命中}\ \lor\
\text{quotient-multiple 命中}\ \lor\
\mathcal E_p(c_1)\ne\varnothing\ \lor\
\mathcal E_p(c_2)\ne\varnothing
\tag{41}
\]

即使限制在 \(n\equiv7\pmod8\)、两条尾均定义的合法 first-overflow 数据域，
(41) 也不恒成立。

这个结论的作用域必须保持精确。\(p=193\) 另有 gap \(7\)、\(x=50\)、\(d=20\)
的直接 Type II 终端：

\[
\frac4{193}=\frac1{50}+\frac1{1930}+\frac1{4825}.
\tag{42}
\]

所以 (35) 在 terminal-first 选择器中会被预占。(41) 严格否定的是四个指定局部
菜单的无条件全称覆盖，而不是 Erdős--Straus 猜想、其它终端、其它 source coordinate、
扩展 tail 或 exact physical-source/kernel successor。

## 8. 对统一选择器的约束

原先的三项希望

~~~text
natural Bradford menu
  -> quotient-multiple menu
  -> two canonical source tails
~~~

现在必须改成带显式失败出口的局部分派：

~~~text
FOUR_LOCAL_MENUS_EMPTY
  -> exact physical-source/kernel successor
  -> another exact source-coordinate or tail class
  -> independently verified terminal or well-founded descent
~~~

平方商定理还说明 quotient-multiple 不能承担统一后继的普适正容量：它在无穷多合法
核心 first-overflow 控制上结构性为零。后续正向定理必须使用 \(\Delta\) 的同余因子
结构、(22) 的完整两族，或引入独立的物理来源/容量信息；重复扩大同一个
quotient-multiple 扫描范围不会改变这一障碍。

## 聚焦验证

~~~bash
python3 reproductions/type_i_first_overflow_factor_pair_tail_joint_obstruction.py --verify
~~~

验证器只核对 (4)--(42) 的四个定向控制、精确门等价、有限残数表和直接终端；
不运行历史扫描，也不以有限计算替代 (4)、(16) 或 (22) 的全称证明。
