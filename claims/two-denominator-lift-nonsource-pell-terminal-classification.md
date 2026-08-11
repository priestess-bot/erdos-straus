---
kind: claim
claim_id: two-denominator-lift-nonsource-pell-terminal-classification
title: non-source D-only 标记纤维的负 Pell 全分类与核心全域 no-go
statement: >-
  设 p 为奇素数、2<=n<p，D 是 non-source-supported D-only 参数。若标记纤维
  W(p,n,D) 非空，则三目标谱中的 e=1、e=2 由大小恒空，唯一 e=0 命中经平方载体
  H=gamma A^2、s=gamma B^2、2lambda=gamma AB 和互补除子消元，强制满足
  2AB=A^2/L+B^2/h+1/gamma。一般 Vieta 极小下降证明此方程必有 L,h<=2；而
  L=(p-n)+m、m>0，故 p-n=m=1。进一步的二进分类给出 h=1、gamma=2，并且全部
  命中与负 Pell 方程 b^2-2a^2=-1 的正解一一对应：
  p=4a(a+b)-1、n=p-1、D=2pb^2，命中除子 z=a^2。反之这些数据在 p 为素数时
  总给出显式 source-to-target 映射。因而每个 non-source 命中都有 p=7 (mod 8)，
  且已经是 gap-1 Type II 终端；对 p=1 (mod 4)，特别是全部核心素数，该分支全空。
  source-supported 分支又只复述中心 Type I，所以核心 D-only 菜单不产生任何新 E4。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - two-denominator-lift-d-only-marked-normal-form
  - two-denominator-lift-source-supported-tail-ratio-rigidity
topics:
  - descent
  - marked-solution
  - two-denominator-lift
  - D-only
  - three-target-spectrum
  - one-target-collapse
  - Vieta-jumping
  - Pell-equation
  - terminal-classification
  - no-go
  - selector
sources:
  - claim: two-denominator-lift-core-d-only-support-dichotomy-three-target-spectrum
    role: non-source-normal-form-three-target-spectrum-and-Pell-sufficient-family
  - claim: two-denominator-lift-source-supported-tail-ratio-rigidity
    role: source-supported-centered-Type-I-equivalence
  - reproduction: reproductions/two_denominator_lift_nonsource_pell_terminal_classification.py
    role: focused-Pell-positive-and-core-empty-control-verifier
visibility: public
last_checked: '2026-08-11'
---

# non-source \(D\)-only 标记纤维的负 Pell 全分类与核心全域 no-go

## 1. 定理范围与结论

设 \(p\) 为奇素数，

\[
2\le n<p,
\qquad r=p-n,
\tag{1}
\]

并取一个 non-source-supported \(D\)-only 参数

\[
D\in\mathcal D(p,n),
\qquad D\nmid n^2.
\tag{2}
\]

下面先在本卡内证明所需正规形对任意奇素数都成立，而不借用旧三目标卡的核心同余域。
由目标坐标的 \(p\)-载体刚性，唯一写成 \(a_D'=p\lambda\)。因为
\(D\nmid n^2\)、\(D\mid p^2n^2\) 且 \(D<n^2<p^2\)，必有

\[
D=pd,
\qquad
d\mid n^2,
\qquad
0<d<p.
\tag{3a}
\]

恒等式 \(Da_D'=npa_D\) 给出 \(pd\lambda=na_D\)。因 \((p,n)=1\)，可写
\(a_D=pt\)，并得到

\[
d=n-4rt,
\qquad
d\lambda=nt,
\qquad
0<t<p.
\tag{3b}
\]

这里最后一个界也不需要额外同余条件：由
\(a_D=(np-D)/(4r)<np/(4r)\)，有
\(t<n/(4r)<p\)。

令 \(H=n^2/d\)。从 (3b) 消去 \(d,t\)，得到

\[
Ht=n\lambda,
\qquad
H=n+4r\lambda=p+(4\lambda-1)r.
\tag{3c}
\]

又有 \(H(\lambda-t)=4r\lambda^2\)，而
\((H,r)=(p,r)=1\)。因此 \(H\mid4\lambda^2\)，存在正整数 \(s\) 使

\[
\mu=4\lambda-1,
\qquad
H=p+\mu r,
\qquad
Hs=4\lambda^2,
\qquad
t=\lambda-rs>0.
\tag{3}
\]

成立。以上只使用 \(p\) 为奇素数和 (1)--(2)。

本卡证明精确分类

\[
\boxed{
W(p,n,D)\ne\varnothing
\iff
\begin{array}{l}
\text{存在正整数 }a,b\text{ 满足 }b^2-2a^2=-1,\\
p=4a(a+b)-1\text{ 为素数},\\
n=p-1,\qquad D=2pb^2.
\end{array}}
\tag{4}
\]

除保留双尾的互换外，命中除子、正规形参数和保尾映射唯一恢复为

\[
\begin{aligned}
z&=a^2,
&\lambda&=a(b+2a),
&s&=2a^2,
&t&=ab,\\
\left(pab,\ a(a+b),\ p(a+b)(b+2a)\right)
&\longmapsto
\left(pa(b+2a),\ a(a+b),\ p(a+b)(b+2a)\right).
\end{aligned}
\tag{5}
\]

负 Pell 方程的正解中 \(a,b\) 都为奇数，所以

\[
\boxed{p\equiv7\pmod8.}
\tag{6}
\]

确实，(40) 模 \(2\) 先给出 \(b\) 为奇数，再模 \(8\) 给出 \(a\) 为奇数；于是
\(8\mid4a(a+b)\)。

因此对 \(p\equiv1\pmod4\)，特别是所有核心素数
\(p\equiv1\pmod {24}\)，每个 non-source-supported 标记纤维都为空。

## 2. 任意奇素数上的三目标与单目标塌缩

由 (3)，

\[
ps=(H-\mu r)s
=4\lambda^2-\mu rs
=\lambda+\mu t.
\tag{7}
\]

所以

\[
ps\equiv\lambda\pmod\mu,
\qquad
(s,\mu)=1,
\qquad
0<s<\lambda.
\tag{8}
\]

还需要核对三目标分解在当前全域中合法。由 (3b)，若 \(p\mid\lambda\)，则
\(p\mid nt\)，与 \(0<n,t<p\) 矛盾。因此 \(p\nmid\lambda\)。另一方面，
若 \(p\mid\mu\)，则 (3c) 给出 \(p\mid H\)；但 \(H\mid n^2\) 且 \(p\nmid n\)，
仍矛盾。所以

\[
(p\lambda,\mu)=1.
\tag{8a}
\]

任一保留尾 \((b,c)\) 满足

\[
\frac{\mu}{p\lambda}=\frac1b+\frac1c,
\]

故

\[
(\mu b-p\lambda)(\mu c-p\lambda)=p^2\lambda^2.
\tag{8b}
\]

每个正因子 \(Z\mid p^2\lambda^2\) 唯一写成

\[
Z=p^e z,
\qquad
e\in\{0,1,2\},
\qquad
z\mid\lambda^2.
\tag{8c}
\]

整性条件 \(Z\equiv-p\lambda\pmod\mu\) 正好给出下面的三个目标。因子互补

\[
(e,z)\longleftrightarrow
\left(2-e,\frac{\lambda^2}{z}\right)
\tag{8d}
\]

保持命中，所以可规范到 \(z\le\lambda\)。中点 \(z=\lambda\) 也不可能：
\(e=1\) 会要求 \(\mu\mid2\lambda\)；\(e=2\) 由
\(p^{-1}\lambda\equiv s\pmod\mu\) 会要求 \(\mu\mid\lambda+s\)，而二者都严格位于
\((0,\mu)\)；\(e=0\) 与 \(e=2\) 在中点由 (8d) 配对。因此规范范围严格为
\(0<z<\lambda\)。

于是标记非空性规范为：存在

\[
z\mid\lambda^2,
\qquad 0<z<\lambda,
\tag{9}
\]

命中以下三者之一：

\[
z\equiv-p\lambda,
\qquad
z\equiv-\lambda,
\qquad
z\equiv-p^{-1}\lambda
\pmod\mu.
\tag{10}
\]

第二个目标不可能，因为

\[
0<z+\lambda<2\lambda<4\lambda-1=\mu.
\tag{11}
\]

由 (8)，第三个目标等价于 \(z\equiv-s\pmod\mu\)，同样有

\[
0<z+s<2\lambda<\mu.
\tag{12}
\]

故对每个 non-source 状态，无需任何同余类假设，都有

\[
\boxed{
W(p,n,D)\ne\varnothing
\iff
\exists z\mid\lambda^2,\quad0<z<\lambda,\quad
z\equiv-p\lambda\pmod\mu.}
\tag{13}
\]

令

\[
v=\frac{\lambda^2}{z}>\lambda.
\tag{14}
\]

因为 \((z,\mu)=1\)，将 (13) 的同余乘以 \(s\)，再用 (7)，可消去 \(z\)，得到

\[
\boxed{v+s=h\mu}
\tag{15}
\]

的唯一正整数 \(h\)。所以 (13) 也等价于一个互补大因子命中。

## 3. 命中自动产生跨平方 Type II 容量

若 (13) 命中，定义

\[
x=\frac{p\lambda+z}{\mu},
\qquad
m=4x-p.
\tag{16}
\]

把第一式乘以 \(4\)，并使用 \(4\lambda=\mu+1\)，得到

\[
\boxed{p+4z=m\mu.}
\tag{17}
\]

所以 \(m\) 是正整数。再将 (15) 乘以 \(p\)，并使用 (7)，得到

\[
\frac{\lambda+pv}{\mu}=ph-t>0.
\tag{18}
\]

于是源与目标尾可写成

\[
\boxed{
(pt,x,p(ph-t))
\longmapsto
(p\lambda,x,p(ph-t)).}
\tag{19}
\]

目标式乘以 \(p\) 后给出

\[
\frac m x=\frac1\lambda+\frac1{ph-t}.
\tag{20}
\]

因此 \(z=m\lambda-x\) 还是这张直接 Type II 图表的平方因子，并满足

\[
z\mid x^2.
\tag{21}
\]

令 \(g=(\lambda,x)\)。由 \(z=x\mu-p\lambda\) 及
\(z\mid\lambda^2,x^2\)，还有严格的跨平方容量约束

\[
\boxed{g\mid z\mid g^2.}
\tag{22}
\]

所以任何潜在 non-source 命中在进入下面的 no-go 前，已经是同一除子同时落入源平方
与 Type II 目标平方的直接终端，不是新的递归类型。

## 4. 统一平方载体

等式 \(Hs=(2\lambda)^2\) 有唯一的互素平方载体分解。令

\[
\gamma=(H,s).
\tag{23}
\]

则存在唯一正整数 \(A,B\)，使

\[
\boxed{
H=\gamma A^2,
\qquad
s=\gamma B^2,
\qquad
2\lambda=\gamma AB,
\qquad
(A,B)=1.}
\tag{24}
\]

确实，\(\gamma\mid2\lambda\)，而两个互素正整数之积为平方时二者各自为平方。

置

\[
w=A-2rB.
\tag{25}
\]

把 (24) 代回 (3)，可得完整恢复式

\[
\boxed{
w>0,
\quad
n=\gamma Aw,
\quad
p=\gamma Aw+r,
\quad
D=p\gamma w^2,
\quad
t=\frac{\gamma Bw}{2}.}
\tag{26}
\]

这套载体不依赖 \(n\) 的模 \(4\) 类，同时覆盖此前分开的偶秩、同
\(1\pmod4\) 秩和 \(p-1\) 秩。

## 5. 命中导出的 Vieta 方程

令

\[
L=r+m.
\tag{27}
\]

把 (17) 与 \(H=p+\mu r=\gamma A^2\) 相加，得到

\[
4z+\gamma A^2=L\mu.
\tag{28}
\]

另一方面，(15) 与 \(s=\gamma B^2\) 给出

\[
v+\gamma B^2=h\mu.
\tag{29}
\]

利用 \(4zv=4\lambda^2=Hs=\gamma^2A^2B^2\)，将 (28)--(29) 相乘并消去
共同常数项，得到

\[
Lh\mu=L\gamma B^2+h\gamma A^2.
\]

再代入 \(\mu=2\gamma AB-1\)，便得到

\[
\boxed{
2AB=\frac{A^2}{L}+\frac{B^2}{h}+\frac1\gamma.}
\tag{30}
\]

## 6. 一侧分母至多二的 Vieta 引理

> **引理。** 若正整数 \(X,Y,L,M,C\) 满足
> \[
> 2XY=\frac{X^2}{L}+\frac{Y^2}{M}+\frac1C,
> \tag{31}
> \]
> 则 \(L\le2\) 且 \(M\le2\)。

只证 \(L\le2\)，另一边由对称性得到。反设固定的 \(L>2,M,C\) 有正整数解，
并在全部正整数解中取 \(X+Y\) 最小者。把 (31) 分别看成关于 \(X,Y\) 的二次方程，
Vieta 伴根为

\[
X^*=2LY-X,
\qquad
Y^*=2MX-Y.
\tag{32}
\]

根积为正，故 \(X^*,Y^*\) 都是正整数解。极小性给出

\[
X\le LY,
\qquad
Y\le MX.
\tag{33}
\]

令

\[
\alpha=LY-X\ge0,
\qquad
\beta=MX-Y\ge0.
\tag{34}
\]

清分母并按 (34) 分组，得到

\[
\boxed{LM=CXM\alpha+CYL\beta.}
\tag{35}
\]

先设 \(Y\ge2\)。若 \(\alpha>0\)，(35) 给出 \(L\ge CX\alpha\)。当
\(0<\alpha<L\) 时，

\[
X=LY-\alpha>L,
\]

与 \(L\ge CX\alpha\ge X\) 矛盾；当 \(\alpha\ge L\) 时，全部不等式只能取等，
迫使 \(\alpha=L,C=X=1\)，但此时 \(1=L(Y-1)\)，仍矛盾。因此
\(\alpha=0\)、\(X=LY\)。代回 (31) 得

\[
CY^2(LM-1)=M,
\]

而 \(L>2,Y\ge2\) 时左端严格大于右端。故只能有 \(Y=1\)。

现在 (35) 中

\[
\alpha=L-X,
\qquad
\beta=MX-1.
\]

若 \(X\ge2\) 且 \(M\ge2\)，第二项已经满足

\[
CL(MX-1)\ge L(2M-1)>LM,
\]

不可能。若 \(M=1\)，同一项至少为 \(L=LM\)；唯一可能的等号情形是
\(C=1,X=2\)，但这还要求第一项为零，从而 \(L=X=2\)，与 \(L>2\) 矛盾。
所以 \(X=1\)。此时 (31) 要求

\[
2=\frac1L+\frac1M+\frac1C.
\]

当 \(L>2\) 时，按 \(M,C\) 中零个、一个或两个等于 \(1\) 分开比较，右端分别
严格小于 \(2\)、严格小于 \(2\) 或严格大于 \(2\)。最终矛盾，故 \(L\le2\)。

## 7. 从 Vieta 界到负 Pell 全分类

将引理用于 (30)，得到

\[
L\le2,
\qquad h\le2.
\tag{36}
\]

由 (17)，\(m\ge1\)，而 \(r\ge1\)。结合 \(L=r+m\)，只能有

\[
\boxed{r=m=1,\qquad n=p-1.}
\tag{37}
\]

式 (17) 于是成为

\[
p+4z=\mu,
\]

故 \(p\equiv3\pmod4\)。又由 (26)，

\[
p-1=\gamma Aw\equiv2\pmod4.
\tag{38}
\]

因为 \(w=A-2B\) 与 \(A\) 同奇偶，(38) 强制 \(A,w\) 为奇数，并且

\[
v_2(\gamma)=1.
\tag{39}
\]

若 \(h=2\)，把 \(L=h=2\) 代入 (30) 并乘以 \(2\)，得到

\[
4AB=A^2+B^2+\frac2\gamma.
\]

所以 \(\gamma\mid2\)，结合 (39) 得 \(\gamma=2\)。模 \(2\) 先迫使 \(B\) 为偶数，
再模 \(4\) 得到右边同余于 \(2\)、左边同余于 \(0\)，矛盾。因此 \(h=1\)。

此时 (30) 给出

\[
4AB=A^2+2B^2+\frac2\gamma.
\]

同理 \(\gamma=2\)。令

\[
a=B,
\qquad b=w=A-2B>0.
\]

上式恰化为

\[
\boxed{b^2-2a^2=-1.}
\tag{40}
\]

式 (24)、(26)、(28) 随即给出

\[
\begin{aligned}
A&=b+2a,
&\lambda&=a(b+2a),
&s&=2a^2,
&t&=ab,\\
p&=2b(b+2a)+1=4a(a+b)-1,
&D&=2pb^2,
&z&=a^2.
\end{aligned}
\tag{41}
\]

这证明了 (4) 的必要方向，也把此前只作为充分正例出现的负 Pell 族升级为全部
non-source 命中的无冗余分类。

反过来，给定 (40) 的正解并假设 (41) 中的 \(p\) 为素数，令

\[
n=p-1,
\qquad
H=2(b+2a)^2,
\qquad
\mu=4a(b+2a)-1.
\]

则 \(H=p+\mu\)、\(Hs=4\lambda^2\)、\(t=\lambda-s=ab>0\)，从而恢复合法的
non-source 参数 \(D=2pb^2\)。这里可以直接核验：置 \(A=b+2a\)，则

\[
n=p-1=2Ab,
\qquad
D=np-4pab,
\qquad
D(np+4p\lambda)=(np)^2.
\]

又因 \(2A^2=H=p+\mu>p\)，有 \(0<D<n^2\)；而 \(p\nmid n\)，故
\(D\nmid n^2\)。这正是 \(D\in\mathcal D(p,n)\) 的两项合同、尺寸条件和
non-source 条件。此外

\[
4(a^2+p\lambda)=(p+1)\mu,
\tag{42}
\]

故 \(z=a^2\) 命中 (13)，并由 (19) 恢复 (5)。充分方向得证。

## 8. 对统一选择器的决定性含义

对核心素数 \(p\equiv1\pmod {24}\)，任意 \(D\in\mathcal D(p,n)\) 只有两种情况：

1. \(D\mid n^2\)：标记非空性精确等价于已有中心 Type I 命中；
2. \(D\nmid n^2\)：由 (4)--(6)，标记纤维恒空。

所以

\[
\boxed{
\text{核心 }D\text{-only 双尾保持菜单只含直接中心 Type I 或空分支，}
\text{不含新的 Type II，也不含任何可递归 E4。}}
\tag{43}
\]

这一次性关闭了此前分别处理的 \(n=p-1\)、\(n\equiv1\pmod4\)、偶前驱以及仍开放的
\(n\equiv3\pmod4\) non-source 区域。广义二进关系点的第二层 \(D\)-only 搜索也不再是
递降方向：核心域内的 source-supported 命中已经是中心 Type I，non-source 候选即使
坐标存在，其指定标记纤维也必为空。

对非核心 \(p\equiv7\pmod8\)，唯一可能的 non-source 命中由 (4) 给出，但 (5) 已是
缺口 \(m=1\)、非 \(p\) 分母 \(x=(p+1)/4\) 的直接 Type II 终端，同样没有新增递归状态。

## 9. 聚焦边界与复现

前两组负 Pell 正例为

\[
\begin{array}{c|c|c|c|c|c}
a&b&p&n&D&z\\ \hline
1&1&7&6&14&1\\
5&7&239&238&23422&25.
\end{array}
\tag{44}
\]

它们分别恢复

\[
(7,2,42)\mapsto(21,2,42),
\qquad
(8365,60,48756)\mapsto(20315,60,48756).
\]

三个核心空纤维控制覆盖先前不同区域：

\[
\begin{array}{c|c|c|c|c|c}
p&n&r&D&\lambda&s\\ \hline
73&70&3&730&35&10\\
457&455&2&79975&91&28\\
1801&1776&25&1037376&37&1.
\end{array}
\tag{45}
\]

第二行 \(n\equiv3\pmod4\) 正是此前两个局部 no-go 都未覆盖的区域。

聚焦验证入口为

~~~bash
python3 reproductions/two_denominator_lift_nonsource_pell_terminal_classification.py --verify
~~~

脚本只重算 (44)--(45) 的正规形、三个目标、Pell 恒等式和显式单位分数映射；全称性来自
第 2--7 节的代数与 Vieta 极小下降，不来自有限枚举。
