---
kind: claim
claim_id: type-I-source-word-bottom-projection-dual-capacity
title: 来源路径的底层投影、双节点相位差与双容量接口
statement: 任意互素形式节点 A+B=Rm 都有唯一无序底层投影 {r,R-r}，且沿正规路径按祖先坐标追踪时，路径字 Theta 给出非负整数商。两个底层节点的两种相对定向分别产生小于 R 的规范相位 +1 差值；它们本身不是目标表示，也不必产生 Type I/II。另一方面，首后继 U+V=Rm_1 与底层终点 X+Y=R 的路径字精确产生两个互素相位 -1 交叉表示；任一交叉乘积整除 K 即给出中心 Type I，整除 x_R=(p+R)/4 即给出 gap R 的 Type II。若两种容量都 miss，则得到规范 q 进缺陷而不是递降。把路径字或底层差值送入非 source-supported D-only 只在额外满足 H|4lambda^2 和三目标因子条件时成立；同模桥还强制 mu>2sqrt(p)-1，故小底层差值不能普遍承担该 E4。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-psi-one-source-word-large-slab-constraint
  - type-I-formal-full-excess-cycle-or-hit-reduction
  - type-I-general-b-centered-square-spectrum
  - type-I-coprime-factor-normal-form
  - type-II-coprime-factor-normal-form
  - two-denominator-lift-core-d-only-support-dichotomy-three-target-spectrum
topics:
  - type-I
  - type-II
  - formal-target-pair
  - path-word
  - bottom-projection
  - q-adic-capacity
  - external-slab
  - marked-descent
  - proof-boundary
sources:
  - claim: type-I-psi-one-source-word-large-slab-constraint
    role: nonnegative-path-word-transport
  - claim: type-I-formal-full-excess-cycle-or-hit-reduction
    role: formal-target-to-direct-type-I
  - claim: type-II-coprime-factor-normal-form
    role: target-product-to-gap-R-type-II
  - claim: two-denominator-lift-core-d-only-support-dichotomy-three-target-spectrum
    role: non-source-supported-D-only-interface
visibility: public
last_checked: '2026-08-01'
---

# 来源路径的底层投影、双节点相位差与双容量接口

## 1. 形式节点的规范底层投影

固定

\[
p\equiv1\pmod {24},
\qquad 4K=pR+1,
\qquad R\ge3.
\tag{1}
\]

任取互素形式节点

\[
A+B=Rm,
\qquad (A,B)=1.
\tag{2}
\]

由 (2) 可知

\[
(A,R)=(B,R)=1.
\tag{3}
\]

令 \(a\in\{1,\ldots,R-1\}\) 是 \(A\bmod R\) 的代表，则唯一存在
\(u_0,v_0\in\mathbb Z_{\ge0}\)，使

\[
A=a+Ru_0,
\qquad
B=R-a+Rv_0,
\qquad
u_0+v_0=m-1.
\tag{4}
\]

置 \(r=\min(a,R-a)\)，得到唯一无序投影

\[
\boxed{
\pi_R(A,B,m)=\{r,R-r\},
\qquad1\le r<R/2.
}
\tag{5}
\]

式 (3) 保证 \((r,R-r)=1\)，所以 (5) 确实是环境形式图中的 \(m=1\) 节点。
但 \(\pi_R\) 只是保留模 \(R\) 剩余类的代数投影；它没有声称存在从原节点到该节点的
formal 路径，更没有给出 E4 或解提升。

## 2. 路径字的非负整数商

设某条正规 formal 路径从

\[
U+V=Rm_0
\tag{6}
\]

到达底层终点 \(X+Y=R\)。每条边的素数标签为 \(q_i\)，正规公因子为 \(g_i\)，令

\[
h_i=q_ig_i,
\qquad
\Theta=\prod_i h_i.
\tag{7}
\]

按 \(U,V\) 的后代关系定向终点后，存在

\[
u,v\in\mathbb Z_{\ge0}
\tag{8}
\]

使

\[
\boxed{
\Theta X=U+Ru,
\qquad
\Theta Y=V+Rv,
\qquad
u+v=\Theta-m_0.
}
\tag{9}
\]

这是[来源路径字约束](type-I-psi-one-source-word-large-slab-constraint.md)中同余式的加强。
单条边在未交换定向下满足

\[
h_iC'=C,
\qquad
h_iD'=D+Rt_i,
\qquad t_i\ge0.
\tag{10}
\]

从终点反向代入 (10)，被选侧的整数商乘以 \(h_i\)，补坐标侧的整数商变成
\(t_i+h_i\) 倍旧商；两者始终非负。归纳得到前两式，求和即得第三式。

## 3. 两个底层节点的两种相位差

取两个规范底层节点

\[
N_r=\{r,\bar r\},
\qquad
N_s=\{s,\bar s\},
\qquad
\bar r=R-r,
\quad
\bar s=R-s,
\tag{11}
\]

其中 \(1\le r,s<R/2\)。平行定向令

\[
g_{\parallel}=\gcd(rs,\bar r\bar s).
\tag{12}
\]

因为 \((g_{\parallel},R)=1\)，且

\[
\bar r\bar s-rs=R(R-r-s),
\]

所以

\[
\boxed{
\delta_{\parallel}=\frac{R-r-s}{g_{\parallel}}\in\mathbb Z,
\qquad
\frac{\bar r\bar s}{g_{\parallel}}
-\frac{rs}{g_{\parallel}}
=R\delta_{\parallel}.
}
\tag{13}
\]

交叉定向令

\[
g_{\times}=\gcd(r\bar s,\bar r s).
\tag{14}
\]

同理，由

\[
\bar r s-r\bar s=R(s-r)
\]

得到

\[
\boxed{
\delta_{\times}=\frac{|s-r|}{g_{\times}}\in\mathbb Z,
\qquad
\left|
\frac{\bar r s}{g_{\times}}
-\frac{r\bar s}{g_{\times}}
\right|
=R\delta_{\times}.
}
\tag{15}
\]

两式中的约分后坐标都互素，且

\[
0\le\delta_{\parallel},\delta_{\times}<R.
\tag{16}
\]

非退化平行差总为正；交叉差在 \(r=s\) 时为零。关键语义是：这些约分对满足
“差被 \(R\) 整除”，即模 \(R\) 的相位为 \(+1\)。形式目标对要求“和被 \(R\)
整除”，相位为 \(-1\)。因此 (13)--(15) 不是新的 formal 节点，也不自动满足任一
Type I/II 平方除子条件。

### 最小核心反例

取最小的核心素数和一个线性图表

\[
p=73,
\qquad R=11,
\qquad K=201,
\qquad p=1+6+6R.
\tag{17}
\]

底层节点 \(\{1,10\}\)、\(\{4,7\}\) 的两种约分对分别为

\[
(1\cdot4,10\cdot7)/2=(2,35),
\qquad
(1\cdot7,10\cdot4)=(7,40),
\]

而且这两个节点不是任意拼接：完整 raw bottom 图中有真实边

\[
\{4,7\}\xrightarrow{7}\{1,10\}.
\]

所以两种 \(\delta\) 都等于 3，甚至来自一条实际路径的首尾。但

\[
x_3=\frac{73+3}{4}=19,
\qquad
\operatorname{Div}(x_3^2)=\{1,19,361\}.
\]

三个平方除子逐一不满足 Type I 同余；满足 \(d\le x_3\) 的 \(1,19\) 也不满足
Type II 同余。因此 gap 3 完整 miss。这个例子不满足更窄的 terminal-first
\(\Psi_0=1\) 前提，但已经否定“任意两个底层节点的差值必终端”这一纯代数命题。

## 4. 单个底层节点的双容量判据

对任一底层节点 \(N_r\)，记

\[
L_r=r(R-r),
\qquad
x_R=\frac{p+R}{4}.
\tag{18}
\]

若 \(R\) 是合法缺口，即 \(3\le R\le p-2\)，则有两个无样本判据：

\[
\boxed{
L_r\mid K
\Longrightarrow
\text{同状态中心 Type I 命中},
}
\tag{19}
\]

\[
\boxed{
L_r\mid x_R
\Longrightarrow
\text{gap }R\text{ 的 Type II 命中}.
}
\tag{20}
\]

第一式取 \(C=K/L_r\)，则 \(K=r(R-r)C\)，而 \(r+(R-r)=R\)；完整形式图的
汇点恢复定理直接给出 Type I。第二式取 \(C=x_R/L_r\)，将

\[
(A,B,C)=(r,R-r,C)
\]

代入 Type II 互素因子正规形即可。

在 (17) 中，两个乘积为 \(10,28\)，均不整除 \(K=201\) 或 \(x_R=21\)。所以
即使同时拥有两个底层节点，也没有纯组合恒等式强制 (19) 或 (20)。

## 5. 来源路径产生的两个交叉目标表示

回到 (6)--(9)。定义

\[
d_U=\gcd(U,\Theta Y),
\qquad
d_V=\gcd(V,\Theta X).
\tag{21}
\]

路径上的全部坐标以及每个 \(h_i\) 都与 \(R\) 互素，所以

\[
(d_U,R)=(d_V,R)=1.
\tag{22}
\]

由 (9) 和 \(U+V=Rm_0\)，有

\[
U+\Theta Y=R(m_0+v),
\qquad
V+\Theta X=R(m_0+u).
\tag{23}
\]

因此约分得到两个新的互素形式目标对

\[
\boxed{
(P_U,Q_U)=\left(\frac U{d_U},\frac{\Theta Y}{d_U}\right),
\qquad
(P_V,Q_V)=\left(\frac V{d_V},\frac{\Theta X}{d_V}\right).
}
\tag{24}
\]

它们的层数分别为 \((m_0+v)/d_U\)、\((m_0+u)/d_V\)。记

\[
L_U=P_UQ_U,
\qquad
L_V=P_VQ_V.
\tag{25}
\]

对 \(i\in\{U,V\}\)，(19)--(20) 的证明不使用层数为 1，故精确有

\[
\boxed{
L_i\mid K
\Longrightarrow
\text{直接 Type I},
\qquad
L_i\mid x_R
\Longrightarrow
\text{gap }R\text{ 的直接 Type II}.
}
\tag{26}
\]

第一支中，若 \(a_i<b_i\) 是 \(P_i,Q_i\) 的定向，取
\(C_i=K/L_i\)，中心除子

\[
D_i=a_i^2C_i
\]

满足 \(D_i\mid K^2\)、\(D_i<K\)、\(D_i\equiv-K\pmod R\)，并由已有中心恢复公式
生成合法 Type I 缺口。第二支直接取
\(C_i=x_R/L_i\) 代入 Type II 正规形。

因此，在中心 Type I miss 且 gap \(R\) Type II miss 的状态中，每个来源路径都输出
四个精确容量 miss：

\[
L_U\nmid K,
\quad L_V\nmid K,
\quad L_U\nmid x_R,
\quad L_V\nmid x_R.
\tag{27}
\]

对任意容量 \(N\in\{K,x_R\}\)，可把失败规范记录为

\[
\eta^{(N)}_{i,q}
=\max\{0,v_q(L_i)-v_q(N)\}.
\tag{28}
\]

式 (27) 等价于每个相应向量至少有一个正坐标。这就是来源表示到双容量缺陷的精确接口；
它没有证明两个容量的正坐标落在同一个素数，也没有给出跨状态超载。

## 6. 映入非自然 D-only 的两个条件桥

### 6.1 同模路径字桥

在 (6)--(9) 中再假设 \(U\mid K\)，令 \(Y\) 是 \(V\) 的后代，并置

\[
C=\frac KU.
\]

取任意

\[
\mu\mid R,
\qquad \mu\equiv3\pmod4,
\qquad \lambda=\frac{\mu+1}{4}.
\tag{29}
\]

由 \(V\equiv-U\pmod R\) 和 (9)，整数

\[
w=C\Theta Y
\tag{30}
\]

满足

\[
w\equiv-K\equiv-\lambda\pmod\mu.
\tag{31}
\]

最后一步使用 \(4K=pR+1\) 以及 \(\mu\mid R\)。所以，若还存在

\[
1\le\rho\le p-2,
\qquad
H=p+\mu\rho\mid4\lambda^2,
\qquad
w\mid\lambda^2,
\tag{32}
\]

则 (31) 正是非 source-supported D-only 三目标谱的 \(e=1\) 命中。令

\[
n=p-\rho,
\qquad
s=\frac{4\lambda^2}{H},
\qquad
t=\lambda-\rho s,
\qquad
D=\frac{pn^2}{H},
\tag{33}
\]

以及

\[
b=\frac{p(\lambda+w)}\mu,
\qquad
c=\frac{p(\lambda+\lambda^2/w)}\mu.
\tag{34}
\]

已有 D-only 正规形逐式给出

\[
(pt,b,c)\in\operatorname{Sol}(n)
\Longleftrightarrow
(p\lambda,b,c)\in\operatorname{Sol}(p).
\tag{35}
\]

由于 (34) 已显式给出非空尾，满足 (29)--(32) 时实际上已经得到直接终端，而不是仍待
递归闭合的条件边。

这个桥有一个严格尺寸障碍。由 \(H>p\) 和 (32)，

\[
p<H\le4\lambda^2=\frac{(\mu+1)^2}{4},
\]

故必有

\[
\boxed{\mu>2\sqrt p-1.}
\tag{36}
\]

特别地，若 \(R\le2\sqrt p-1\)，则所有 \(\mu\mid R\) 的同模路径字桥同时为空。
若 \(\mu\nmid R\)，现有路径字只有模 \(R\) 信息，(31) 不再成立；必须先构造新的跨模数
同态或整数因子恒等式。

### 6.2 保留 single-slab 好尾的差值桥

设底层 single-external slab 满足

\[
Q\alpha+\beta=R,
\qquad
K=\alpha\beta c_0.
\tag{37}
\]

令

\[
U=\alpha c_0,
\qquad
h=4U-p=\frac{\alpha pQ+1}{\beta}>0.
\tag{38}
\]

给定任意正整数 \(\delta\)。若

\[
h\mid U+\delta,
\qquad
\lambda=\frac{U+\delta}{h},
\tag{39}
\]

并且存在 \(\rho,H\) 满足 (32) 中的 D-only 整除条件，且

\[
\delta\mid(p\lambda)^2,
\tag{40}
\]

则对 \(\mu=4\lambda-1\) 有精确恒等式

\[
\boxed{
\mu U-p\lambda
=\lambda(4U-p)-U
=\delta.
}
\tag{41}
\]

所以 \(z=\delta\) 直接命中 D-only 标记因子同余。另一共同尾为

\[
V=\frac{p\lambda+(p\lambda)^2/\delta}{\mu},
\tag{42}
\]

并显式得到

\[
(pt,U,V)\in\operatorname{Sol}(p-\rho)
\Longleftrightarrow
(p\lambda,U,V)\in\operatorname{Sol}(p).
\tag{43}
\]

这同样是条件满足即终端的桥。D-only 条件 \(H>p\)、\(H\mid4\lambda^2\) 还强制

\[
\lambda>\frac{\sqrt p}{2},
\qquad
\boxed{
\delta>\frac{h\sqrt p}{2}-U.
}
\tag{44}
\]

因此把 (13) 或 (15) 的小底层差值直接代入 (39)，一般会遭遇量级障碍；纯同余匹配并不
足够。

## 7. 两条冻结路径的精确边界

第一条路径取

\[
(p,R,K)=(5596369,35,48968229),
\qquad
(U,V,m_0)=(237,8,7),
\]

到达定向终点 \((X,Y)=(32,3)\)，且

\[
\Theta=(2\cdot4)\cdot17\cdot11=1496,
\qquad
(u,v)=(1361,128).
\]

(24) 给出

\[
(P_U,Q_U)=(79,1496),
\qquad
(P_V,Q_V)=(1,5984),
\]

乘积分别为 \(118184,5984\)。两者都不整除 \(K\) 或

\[
x_R=1399101.
\]

同一底层周期中的 \(r=1,s=3\) 给出 \(\delta_{\parallel}=31\)，且 \(d=85\)
同时验证 Type I 和 Type II；但这是一张直接终端证书，不是 formal 边或 D-only E4。
此例的 \(R\) 的候选 \(\mu=7,35\) 均被 (36) 排除。若固定 slab 好尾

\[
U=16322743,
\qquad h=59694603,
\]

则 (44) 的最小整数 \(\lambda=1183\) 已要求

\[
\delta\ge70602392606.
\]

第二条路径取

\[
(p,R,K)=(212973049,215,11447301384),
\qquad
(U,V,m_0)=(1259,1966,15),
\]

经 \(\Theta=983\) 到达 \((X,Y)=(213,2)\)，且 \((u,v)=(968,0)\)。两个交叉目标对为

\[
(1259,1966),
\qquad
(2,213),
\]

乘积 \(2475194,426\) 同样双容量 miss。底层节点 \(r=2,s=3\) 是实际单边
\(\{2,213\}\xrightarrow{71}\{3,212\}\) 的首尾，并给出 gap 35 的
Type I 证书 \(d=66471\)。它不是三步词 \((107,71,53)\) 的首尾差；该三步首尾只给
\((\delta_\parallel,\delta_\times)=(105,3)\)。而同一实际四周期中的 \(r=3,s=1\) 给出
\(\delta_{\parallel}=211\)，完整平方除子空间没有 Type I/II。

聚焦复现入口为

~~~bash
python3 reproductions/type_i_source_word_bottom_projection_dual_capacity.py
python3 reproductions/type_i_source_word_bottom_projection_dual_capacity.py --verify
~~~

结果文件为

~~~text
reproductions/type-i-source-word-bottom-projection-dual-capacity-results.json
~~~

## 8. 证明边界与下一接口

本卡完成了路线报告要求的第一段桥接：来源路径不再只输出一个模 \(R\) 同余，而是输出
两个规范相位 \(-1\) 表示及其 \(K/x_R\) 双容量缺陷；底层双节点组合也被精确分成两种
相位 \(+1\) 差值。它同时排除了两个过强结论：

1. 任意底层双节点差值或其因子必产生终端；
2. 小底层差值可直接成为非自然 D-only 的统一递降参数。

真正剩余的选择器必须完成以下至少一项：

- 证明某个规范交叉乘积命中 \(K\) 或 \(x_R\)；
- 证明两个非零容量缺陷共享一个可重用载体，并在跨状态账本中形成超载；
- 从 \(\Theta,u,v\) 或高层仿射量构造尺寸至少为 \(\sqrt p\) 的 D-only 参数；
- 建立把模 \(R\) 路径字传到 \(\mu=4\lambda-1\) 的新跨模数恒等式；
- 若这些都 miss，则构造改变根尾数据、满足完整 E1--E5 的合法后继。

在完成其中一步以前，(24)、(28)、(31) 都是
`analysis_evidence` 或直接终端接口，不能登记为递降边。
