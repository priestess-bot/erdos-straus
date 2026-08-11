---
kind: claim
claim_id: two-denominator-lift-core-d-only-support-dichotomy-three-target-spectrum
title: 核心 D-only 的支撑二分、非自然完全正规形与三目标谱
statement: 对核心素数 p、2<=n<p 及任意合法 D-only 参数 D，令 a'=p lambda。既约尾比总由 delta=gcd(4lambda-1,p) 决定，且 delta=p 当且仅当 D|n^2；所以 source-supported 分支就是已有中心 Type I 谱。若 D 不整除 n^2，则唯一有 D=pd、mu=4lambda-1、sigma=p lambda，并存在 H=p+(4lambda-1)(p-n) 整除 4lambda^2 的完全正规形；该分支强制 n>sqrt(p) 以及 lambda>max(p-n,sqrt(p)/2)。标记纤维非空当且仅当 lambda^2 的某个规范真因子命中 -p lambda、-lambda、-p^{-1}lambda 三个模 mu 目标之一。所有核心 D-only 状态均有 mu=3 (mod 4)，且报告建议的 mu=1、mu=2、mu|(sigma+1) 三个低复杂度出口全部不可能。
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
  - support-dichotomy
  - divisor-parametrization
  - factor-congruence
  - three-target-spectrum
  - proof-boundary
sources:
  - claim: two-denominator-lift-d-only-marked-normal-form
    role: D-only-coordinate-and-marked-fiber-interface
  - claim: two-denominator-lift-source-supported-tail-ratio-rigidity
    role: source-supported-branch-classification
visibility: public
last_checked: '2026-08-11'
---

# 核心 \(D\)-only 的支撑二分、非自然完全正规形与三目标谱

## 1. 既约尾比的统一消元

固定核心素数

\[
p\equiv1\pmod {24},
\qquad 2\le n<p,
\qquad r=p-n,
\tag{1}
\]

并取

\[
D\in\mathcal D(p,n).
\tag{2}
\]

沿用 [D-only 标记正规形](two-denominator-lift-d-only-marked-normal-form.md)的记号

\[
a=\frac{np-D}{4r},
\qquad
a'=\frac{(np)^2/D-np}{4r}.
\tag{3}
\]

已有 \(p\mid a'\)，故唯一写成

\[
a'=p\lambda,
\qquad \lambda\in\mathbb N.
\tag{4}
\]

源状态与目标状态保留同一双尾，所以它们的既约尾比满足

\[
\frac\mu\sigma
=\frac4n-\frac1a
=\frac4p-\frac1{p\lambda}
=\frac{4\lambda-1}{p\lambda}.
\tag{5}
\]

由于 \((4\lambda-1,\lambda)=1\)，若定义

\[
\delta=(4\lambda-1,p)\in\{1,p\},
\tag{6}
\]

则

\[
\boxed{
\mu=\frac{4\lambda-1}{\delta},
\qquad
\sigma=\frac{p\lambda}{\delta}.}
\tag{7}
\]

## 2. 支撑二分是精确等价

有严格等价

\[
\boxed{
\delta=p
\iff
D\mid n^2.}
\tag{8}
\]

右推左已经包含在 source-supported 尾比刚性定理中。反过来，若
\(4\lambda-1=pk\)，由 \(a'=npa/D=p\lambda\) 得到 \(D\lambda=na\)。于是

\[
4na-D=p(4a-n)=pkD,
\]

即 \(4a-n=kD\)。再代入 \(D=np-4ra\)，得到

\[
D=n^2-rkD,
\qquad
D(1+rk)=n^2,
\tag{9}
\]

所以 \(D\mid n^2\)。

因此两支没有重叠，也没有遗漏：

1. \(D\mid n^2\) 时，
   \(4\lambda=p\mu+1\)、\(\sigma=\lambda\)，标记非空性就是同图表的中心
   Type I 命中；
2. \(D\nmid n^2\) 时，
   \[
   \boxed{\mu=4\lambda-1,\qquad\sigma=p\lambda.}
   \tag{10}
   \]

又因 \(p\equiv1\pmod4\)，两支都满足

\[
\boxed{\mu\equiv3\pmod4,\qquad\mu\ge3.}
\tag{11}
\]

特别地，合法核心 \(D\)-only 状态不可能出现 \(\mu=1\) 或 \(\mu=2\)。

## 3. 非 source-supported 分支的完全正规形

以下固定 \(D\nmid n^2\)。因为

\[
D\mid p^2n^2,
\qquad D<n^2<p^2,
\]

若 \(p\nmid D\) 就会有 \(D\mid n^2\)，矛盾；而 \(p^2\nmid D\)。所以唯一写成

\[
D=pd,
\qquad d\mid n^2.
\tag{12}
\]

由 \(0<D<n^2\) 和 \(d\ge1\) 立即得到

\[
p\le D<n^2,
\qquad
\boxed{n>\sqrt p.}
\tag{12a}
\]

所以任意 \(n\le\sqrt p\) 的合法 D-only 参数都只能落在 source-supported 分支。
若另一路线明确把某个 gap、路径标签或重图表模数选作后继秩 \(n\)，它才受此界约束；
本结论本身不提供这种桥接。

式 (3) 又强制 \(a=pt\)，并给出

\[
d=n-4rt,
\qquad
d\lambda=nt.
\tag{13}
\]

令

\[
H=\frac{n^2}{d}.
\tag{14}
\]

从 (13) 消去 \(d,t\)，得到

\[
\boxed{
H=n+4r\lambda
=p+(4\lambda-1)r.}
\tag{15}
\]

而 \(Ht=n\lambda\)，故

\[
H(\lambda-t)=4r\lambda^2.
\]

由于 \((H,r)=(p,r)=1\)，可定义正整数

\[
s=\frac{4\lambda^2}{H},
\qquad
t=\lambda-rs>0.
\tag{16}
\]

全部坐标随之恢复为

\[
\boxed{
n=p-r,
\quad
D=\frac{pn^2}{H},
\quad
a=pt,
\quad
a'=p\lambda.}
\tag{17}
\]

这也是无冗余的反向参数化。反过来，若给定奇素数 \(p\)、
\(1\le r\le p-2\) 与 \(\lambda\ge1\)，并且

\[
H=p+(4\lambda-1)r\mid4\lambda^2,
\tag{18}
\]

还有两个无条件尺寸约束。由 \(H>p\) 和 \(H\le4\lambda^2\) 得

\[
\lambda>\frac{\sqrt p}{2}.
\]

若 \(\lambda\le r=p-n\)，则

\[
H=n+4r\lambda>4\lambda^2,
\]

与 \(H\mid4\lambda^2\) 矛盾。因此

\[
\boxed{
\lambda>\max\left(p-n,\frac{\sqrt p}{2}\right).
}
\tag{18a}
\]

则置 \(n=p-r\)、\(s=4\lambda^2/H\)、\(t=\lambda-rs\)。因为
\(H=n+4r\lambda>4r\lambda\)，有 \(t>0\)。又由
\(n\equiv-4r\lambda\pmod H\) 可知 \(H\mid n^2\)。按 (17) 定义
\(D,a,a'\) 后，有

\[
D=np-4ra,
\qquad
D(np+4ra')=(np)^2.
\tag{19}
\]

并且 \(H>p>n\)，所以 \(0<D<n^2\) 且 \(D\nmid n^2\)。这恰好恢复唯一的
\(D\in\mathcal D(p,n)\)。

## 4. 三目标平方除子谱

在非 source-supported 分支，(13) 还说明 \(p\nmid\lambda\)：事实上
\(0<n,t,d<p\)，而 \(d\lambda=nt\)。所以每个 \(z\mid(p\lambda)^2\) 唯一写成

\[
z=p^e u,
\qquad
e\in\{0,1,2\},
\qquad
u\mid\lambda^2.
\tag{20}
\]

将 (20) 代入标记非空判据

\[
z\equiv-p\lambda\pmod\mu,
\qquad \mu=4\lambda-1,
\]

得到精确的三目标谱：

\[
\boxed{
\begin{array}{c|c}
e&u\pmod\mu\\ \hline
0&-p\lambda\\
1&-\lambda\\
2&-p^{-1}\lambda
\end{array}}
\tag{21}
\]

因子互补把

\[
(e,u)\longleftrightarrow
\left(2-e,\frac{\lambda^2}{u}\right)
\tag{22}
\]

并保持命中条件。中点 \(u=\lambda\) 在核心分支不可能命中：\(e=1\) 会给出
\(\mu\mid2\)，而 \(e=0,2\) 都会给出 \(\mu\mid p+1\)。对后一种可能，写
\(p+1=k\mu\)、\(\ell=k+r\)，则 \(k\equiv2\pmod4\)、\(\ell\ge3\)，并有

\[
H=\ell\mu-1,
\qquad
(\mu+1)^2=4sH.
\]

模 \(\mu\) 可写 \(4s+1=j\mu\)，其中 \(j\equiv3\pmod4\)、\(j\ge3\)。消元后却要求

\[
(j\ell-1)\mu=j+\ell+2,
\tag{23}
\]

其左端在 \(j,\ell,\mu\ge3\) 下严格大于右端，矛盾。

因此 (22) 总能把命中规范到真因子侧：

\[
\boxed{
W(p,n,D)\ne\varnothing
\iff
\exists e\in\{0,1,2\},\ \exists u\mid\lambda^2,
\quad u<\lambda,
\quad u\text{ 命中 (21) 的第 }e\text{ 个目标}.}
\tag{24}
\]

给定命中 \((e,u)\)，令 \(z=p^eu\)，保留双尾可显式写成

\[
\boxed{
b=\frac{p\lambda+p^eu}{\mu},
\qquad
c=\frac{p\lambda+p^{2-e}\lambda^2/u}{\mu}.}
\tag{25}
\]

于是 \((pt,b,c)\in\operatorname{Sol}(n)\)，且
\((p\lambda,b,c)\in\operatorname{Sol}(p)\)。这时已经得到目标终端，而不只是条件递降边。

## 5. \(z=1\) 低复杂度出口在核心分支也为空

条件 \(\mu\mid\sigma+1\) 恰好表示可以取 \(z=1\)。它在两支都不可能。

若 \(D\mid n^2\)，则 \(\mu=k\)、\(\sigma=\lambda\)、\(4\lambda=p\mu+1\)。
若再有 \(\mu\mid\lambda+1\)，则

\[
\mu\mid4(\lambda+1)=p\mu+5,
\]

所以 \(\mu\mid5\)，这与 \(\mu\equiv3\pmod4\) 矛盾。

若 \(D\nmid n^2\)，则 \(\sigma=p\lambda\)，而

\[
\mu\mid p\lambda+1
\iff
\mu\mid p+4.
\tag{26}
\]

写 \(p+4=k\mu\)、\(\ell=k+r\)。由核心同余得到
\(k\equiv3\pmod4\)、\(\ell\ge4\)，并且

\[
H=\ell\mu-4,
\qquad
(\mu+1)^2=4sH.
\tag{27}
\]

模 \(\mu\) 可写

\[
16s+1=j\mu,
\qquad j\equiv3\pmod4,
\qquad j\ge3.
\tag{28}

将 (28) 代回 (27)，得到

\[
(j\ell-4)\mu=4j+\ell+8.
\tag{29}

在 \(j\ge3,\ell\ge4,\mu\ge3\) 下，左端不小于右端；等号只能发生在
\((j,\ell,\mu)=(3,4,3)\)，但此时 (28) 给出 \(s=1/2\)，并非整数。因此仍然矛盾。

综上，路线报告中建议优先构造的三个充分条件

\[
\boxed{
\mu=1,
\qquad
\mu=2,
\qquad
\mu\mid\sigma+1}
\tag{30}

在合法核心 \(D\)-only 状态上全部为空，不能产生无限递降子族。

## 6. 边界例与新的开放选择器

三目标谱并非形式上的空菜单。任取负 Pell 方程

\[
v^2-2u^2=-1
\tag{31}
\]

的正整数解，令

\[
\begin{aligned}
r&=1,&
\lambda&=u(v+2u),&
p&=4u(u+v)-1,\\
n&=p-1,&
D&=2pv^2,&
z&=u^2.
\end{aligned}
\tag{32}
\]

由 \(v^2=2u^2-1\) 直接得到

\[
H=2(v+2u)^2,
\qquad
\frac{4\lambda^2}{H}=2u^2,
\qquad
t=\lambda-2u^2=uv,
\qquad
\frac Dp=2v^2.
\]

若 \(p\) 为素数，则这是合法的非 source-supported \(D\)-only 状态，并且

\[
4(z+p\lambda)=(p+1)(4\lambda-1).
\tag{33}
\]

所以 \(z\) 命中三目标谱，且显式映射为

\[
\boxed{
\bigl(puv,\ u(u+v),\ p(u+v)(v+2u)\bigr)
\longmapsto
\bigl(pu(v+2u),\ u(u+v),\ p(u+v)(v+2u)\bigr).}
\tag{34}
\]

这里恒有 \(p\equiv7\pmod8\)，所以 Pell 族不会进入核心类，但它证明非自然支撑纤维
并非普遍为空，也说明正确候选是 \(\lambda^2\) 的非平凡平方因子，而不是小 \(\mu\)。
前两组素数例正是 \((u,v,p)=(1,1,7)\) 与 \((5,7,239)\)。

核心非 source-supported 空纤维例

\[
(p,n,D)=(73,65,73)
\]

给出

\[
(\lambda,\mu,\sigma,H,s,t)=(130,519,9490,4225,16,2),
\]

而三个目标都没有 \(u\mid130^2\) 命中。另一方面，核心条件不能从第 5 节删除：

\[
(p,n,D)=(7,6,14)
\]

有 \((\lambda,\mu,\sigma)=(3,11,21)\)，且 \(z=1\) 给出共同尾
\((b,c)=(2,42)\)。更非平凡的非核心命中

\[
(p,n,D)=(239,238,23422)
\]

有 \((\lambda,\mu,\sigma)=(85,339,20315)\)，并由
\((e,u)=(0,25)\) 得到

\[
(8365,60,48756)\longmapsto(20315,60,48756).
\]

本卡原始版本没有证明三个目标之一对每个核心状态必命中，而只把非自然支撑余项压缩为
两个同时可核验的选择条件：

\[
\boxed{
H=p+(4\lambda-1)r\mid4\lambda^2}
\tag{35}
\]

以及 (21) 的三目标真因子命中。

后续结果现已把这两个条件在全域中完全关闭。首先，规范真因子侧的 \(e=1\) 目标由
\(u+\lambda<\mu\) 恒空；由 \(ps\equiv\lambda\pmod\mu\) 与 \(s<\lambda\)，
\(e=2\) 也恒空。若唯一剩余的 \(e=0\) 命中，把

\[
Hs=(2\lambda)^2
\]

写成互素平方载体，再与互补因子相乘消元，会得到一侧分母
\(L=(p-n)+m\) 的 Vieta 方程。极小根下降强制 \(L\le2\)，故所有命中必有
\(p-n=m=1\)，并进一步恰由负 Pell 方程

\[
b^2-2a^2=-1
\]

参数化。特别地，命中总满足 \(p\equiv7\pmod8\)。因此对本卡的核心域，所有
non-source-supported 标记纤维都为空，不再存在需要从 large-slab 或路径字构造的
D-only E4。完整充要分类见
[non-source D-only 的负 Pell 全分类](two-denominator-lift-nonsource-pell-terminal-classification.md)。

先前的
[p 减一秩 no-go](two-denominator-lift-core-rank-one-no-go.md)与
[同 1 mod 4 秩 no-go](two-denominator-lift-same-one-mod-four-no-go.md)
现在都是该全分类在局部同余域上的严格推论；它们保留各自的专用载体和历史证明，但不再
定义开放选择器区域。

聚焦复现入口为

~~~bash
python3 reproductions/two_denominator_lift_core_d_only_three_target_spectrum.py
python3 reproductions/two_denominator_lift_core_d_only_three_target_spectrum.py --verify
~~~

结果文件为

~~~text
reproductions/two-denominator-lift-core-d-only-three-target-spectrum-results.json
~~~
