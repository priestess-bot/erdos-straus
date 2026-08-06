---
kind: claim
claim_id: type-II-same-modulus-source-switch-crt-criterion
title: Type II 同模数与除子格 source-switch 的带来源 CRT 判据
statement: 固定 M=4D 与核心素数 p，令 admissible 参数 a 满足 a|D、D/a 平方自由且 aM<p，并记 N_a=p+aM。取两两互素因子块 h_i|N_{a_i}，令 h=乘积 h_i。则 h|N_a 当且仅当 a 同时满足 a=a_i (mod h_i)；若再有 h=-1 (mod M)，则 K=(h+1)/M、c=D/a、B=(Kp+a)/h 给出一个合法 Type II 因子生成器，且 B>a。对任意 D'|D、A|D'，较小模数 M'=4D' 的 source-switch 恰等价于 AD'=Da_0 (mod h)，并可由有限除子格候选集判定；h>D^2 时至多有一个候选。反之，任何同一 M 或除子格的合法 source-switch 必须满足这些带来源合同。p=97、M=24 的伪池化见证 h_1=11、h_2=13 给出 CRT 类 a=133 (mod143)，但没有 admissible a|6，也没有除子格候选，因此不能回译为该混合因子的 Type II 状态。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-cross-state-same-modulus-pooling-counterexample
  - type-II-coprime-factor-normal-form
topics:
- type-II
- source-switch
- same-modulus
- CRT
- factor-relay
- constructive-certificate
- descent-interface
- residue-separation
- additive-fourier
- multiplicative-lift-obstruction
- proof-program
sources:
  - claim: type-II-cross-state-same-modulus-pooling-counterexample
    role: pooling-negative-boundary
  - claim: type-II-coprime-factor-normal-form
    role: raw-Type-II-factor-generator
visibility: public
last_checked: '2026-08-04'
---

# Type II 同模数与除子格 source-switch 的带来源 CRT 判据

## 同模数参数化

固定

\[
M=4D,\qquad p\ \text{为核心素数}.
\]

对满足

\[
a\mid D,\qquad c_a=\frac Da\ \text{平方自由},\qquad aM<p
\tag{1}
\]

的参数 \(a\)，令

\[
s_a=a^2c_a=aD,\qquad
N_a=p+4s_a=p+aM.
\tag{2}
\]

这些参数正好是模数 \(M=4a c_a\) 的规范 Type II 射线。

## 带来源的混合因子

取有限个来源参数 \(a_1,\ldots,a_r\)，并取两两互素正整数块

\[
h_i\mid N_{a_i},\qquad (h_i,M)=1,
\qquad
h=\prod_{i=1}^r h_i.
\tag{3}
\]

则对任意正整数 \(a\)，有精确等价

\[
\boxed{
h\mid N_a
\quad\Longleftrightarrow\quad
a\equiv a_i\pmod{h_i}\quad(1\le i\le r).
}
\tag{4}
\]

### 证明

由 \(h_i\mid N_{a_i}=p+a_iM\) 以及 \((h_i,M)=1\)，

\[
h_i\mid N_a
\iff
h_i\mid (a-a_i)M
\iff
a\equiv a_i\pmod{h_i}.
\]

因 \(h_i\) 两两互素，所有逐块整除条件等价于 \(h\mid N_a\)，得到 (4)。
证毕。

如果 \(h_i\) 不两两互素，则 (4) 需替换为标准 CRT 相容条件
\(a_i\equiv a_j\pmod{(h_i,h_j)}\)，并且产品中的重复素因子必须按总指数重新计数；
不能把重叠因子无条件相乘。

## 从 CRT 到 Type II 证书

假设存在满足 (1) 的 admissible \(a\)，且 CRT 条件 (4) 成立；再假设

\[
h\equiv-1\pmod M.
\tag{5}
\]

令

\[
K=\frac{h+1}{M},\qquad c=\frac Da,\qquad
B=\frac{Kp+a}{h}.
\tag{6}
\]

则 \(K\) 和 \(B\) 为正整数，且

\[
h=4acK-1.
\]

由 \(h\mid N_a\) 有

\[
K N_a=Kp+KaM
=Kp+a(h+1),
\]

故 \(h\mid Kp+a\)，即 \(B\in\mathbb N\)。此外

\[
B-a
=\frac{Kp+a-ah}{h}
=\frac{K(p-aM)+2a}{h}>0.
\tag{7}
\]

所以 \(B>a\)。Type II 因子生成器的原始正规形

\[
(A,C,K)=(a,c,K),\qquad h=4ACK-1,\qquad
h\mid Kp+A
\]

遂给出一张合法 Type II 证书；若 \((a,B)>1\)，再按互素因子正规形约分即可。

因此得到构造性 source-switch：

\[
\boxed{
\text{带来源 CRT}
\;+\;
h\equiv-1\pmod M
\;+\;
\text{admissible }a
\Longrightarrow
\text{Type II 短证书}.
}
\tag{8}
\]

反向地，任何保持同一 \(M\) 的合法 source-switch，其证书因子 \(h\) 必须同时整除
各来源块的乘积并满足 (4)，所以 CRT 是必要条件而不是任意的充分筛。

## 对同模数伪池化反例的解释

在 \(p=97,M=24\) 的反例中，\(D=6\)，两个来源为

\[
(a_1,h_1)=(1,11),\qquad
(a_2,h_2)=(3,13).
\]

混合因子 \(h=143\) 满足

\[
143\equiv-1\pmod{24}.
\]

来源 CRT 为

\[
a\equiv1\pmod{11},\qquad
a\equiv3\pmod{13},
\]

其解为

\[
a\equiv133\pmod{143}.
\]

但 admissible 参数必须满足 \(a\mid D=6\)，而 \(133\) 的整个 CRT 类中没有这样的
参数。因此 \(11\cdot13\) 是群论上的混合命中，却不能回译为同一模数的 Type II
证书；失败的正是 source-switch 的整数参数条件，而不是残数群容量。

## 递降接口与边界

若 CRT 给出的最小 admissible 解 \(a\) 具有严格较小的外层秩（例如相对于来源参数
的 \(aD\)、因子支撑或标记状态势严格下降），则 (8) 可以升级为带 E1--E5 的
source-switch/递降边。当前引理只证明算术构造和必要合同，不证明 admissible 解
一定存在，也不证明 CRT 解会降低核心素数 \(p\)。

所以真正的跨状态容量路线必须先通过 (4) 筛选来源混合，再在 admissible 参数和
标记解提升成立时调用 Kneser；直接池化积集而跳过 CRT 会重复制造伪证书。

## 较小模数的除子格 source-switch

同一计算还给出一个严格较小模数的候选接口。设 \(a_0\) 是混合来源 CRT 得到的
任意正整数，且

\[
h\mid p+4Da_0,\qquad h\equiv-1\pmod{4D}.
\tag{9}
\]

取 \(D'\mid D\)，再取 \(A\mid D'\) 使
\(c'=D'/A\) 平方自由，并假设 \(4AD'<p\)。由于
\((h,4D)=1\)，有精确等价

\[
\boxed{
h\mid p+4AD'
\quad\Longleftrightarrow\quad
AD'\equiv Da_0\pmod h.
}
\tag{10}
\]

若 (10) 成立，令

\[
M'=4D',\qquad
K'=\frac{h+1}{M'},\qquad
B'=\frac{K'p+A}{h}.
\tag{11}
\]

因 \(D'\mid D\)，式 (9) 保证 \(K'\in\mathbb N\)；同前面的恒等式，
\(h\mid K'p+A\)，且

\[
B'-A=\frac{K'(p-4AD')+2A}{h}>0.
\]

所以 \((A,c',K')\) 给出新的 Type II 因子生成器。若 \(D'<D\)，新模数
\(M'=4D'\) 严格小于原模数 \(M=4D\)，这是一条可检验的较小模数候选边。

该除子格条件比同模数 CRT 更宽：它允许原混合因子在原 \(D\) 上没有 admissible
参数时，转而命中 \(D\) 的真除子。它仍不是自动递归边；必须额外证明新状态的
标记解提升和全局势下降。

## 除子格候选集与有限障碍证书

把所有可能的较小模数坐标收集为

\[
\mathscr L_D(p)=\left\{(D',A):
  D'\mid D,\ A\mid D',\ D'/A\text{ 平方自由},\ 4AD'<p\right\}.
\]

对满足 (9) 的混合因子，定义带来源的候选集

\[
\mathscr C_D(h,a_0;p)=\left\{(D',A)\in\mathscr L_D(p):
  AD'\equiv Da_0\pmod h\right\}.
\tag{12}
\]

则有精确的有限判据：

\[
\boxed{
\mathscr C_D(h,a_0;p)\ne\varnothing
\iff
\text{该 }h\text{ 在除子格上存在一个 Type II source-switch 候选}.
}
\tag{13}
\]

这里的“候选”指由 (11) 产生的整数 \(K',B'\) 以及正规形
\((A,D'/A,K')\)。正向蕴含就是 (10)--(11)；反向蕴含则由
\(h\mid p+4AD'\) 与 \(h\mid p+4Da_0\) 相减得到 (10)，所以 (12) 不是
启发式筛，而是该分支的完整算术判定。因而

\[
\mathscr C_D(h,a_0;p)=\varnothing
\tag{14}
\]

本身就是一个有限的“该混合因子不能沿除子格 source-switch”的负证书；它不声称
原问题没有其它 Type I/II 证书。

还有一个有用的单候选简化。记 \(x=AD'\)。由 \(A\le D'\le D\) 有

\[
1\le x\le D^2.
\]

若 \(h>D^2\)，两个不同候选的 \(x\) 不可能同余模 \(h\)。同时每个正整数 \(x\)
都有唯一分解

\[
x=A^2c,\qquad c\text{ 平方自由},
\]

故 \(D'=Ac\) 也唯一。令 \(r\in\{0,1,\ldots,h-1\}\) 为 \(Da_0\) 模 \(h\)
的最小剩余，则

\[
\mathscr C_D(h,a_0;p)\ne\varnothing
\iff
\begin{cases}
1\le r\le D^2,\\
r=A^2c\text{ 且 }c\text{ 平方自由},\\
Ac\mid D,\quad 4r<p.
\end{cases}
\tag{15}
\]

若要严格降低模数，还需 \(Ac<D\)。所以在 \(h>D^2\) 的区域，除子格分支不再是
一个开放式搜索：一次平方自由分解即可给出唯一候选或严格排除。

## 空候选的有限 Fourier 对偶

令

\[
\mathcal X_D(h;p)=
\{AD'\bmod h:(D',A)\in\mathscr L_D(p)\}
\subset\mathbb Z/h\mathbb Z,
\qquad r=Da_0\bmod h.
\]

当 \(\mathscr C_D(h,a_0;p)=\varnothing\) 时，\(r\notin\mathcal X_D(h;p)\)。对
加法群 \(G_h=\mathbb Z/h\mathbb Z\) 定义

\[
f(x)=\mathbf 1_{\mathcal X_D(h;p)}(x),\qquad
g(x)=f(x)-\mathbf 1_{\{r\}}(x),
\]

以及未归一化 Fourier 系数

\[
\widehat g(t)=
\sum_{x\in\mathcal X_D(h;p)}e^{2\pi i tx/h}
-e^{2\pi i tr/h},
\qquad 0\le t<h.
\tag{16}
\]

因为 \(r\notin\mathcal X_D(h;p)\)，Parseval 恒等式给出

\[
\sum_{t=0}^{h-1}|\widehat g(t)|^2
=h\bigl(|\mathcal X_D(h;p)|+1\bigr).
\tag{17}
\]

因此存在一个可规范选择的频率 \(t_\ast\)（例如取达到最大值的最小 \(t\)）满足

\[
\left|
\sum_{x\in\mathcal X_D(h;p)}e^{2\pi i t_\ast x/h}
-e^{2\pi i t_\ast r/h}
\right|
\ge\sqrt{|\mathcal X_D(h;p)|+1}.
\tag{18}
\]

(18) 是空 source-switch 分支的有限根单位字符证书：它只使用 \(D,p,h,a_0\)，
不依赖搜索顺序，也不把不同 Type II 状态的乘法残数直接池化。对 \(h>D^2\) 的
单候选区域，\(\mathcal X_D\) 是一个有限整数集合，(18) 可由精确的圆分域或
整数多项式运算复核。

若只要求严格降模，则在 \(\mathcal X_D\) 中删去 \(D'=D\) 的元素，并把相应的
候选集记为 \(\mathcal X_D^{<}\)；同一 Fourier 构造逐字适用。

必须保留一个边界：\(\mathbb Z/h\mathbb Z\) 的加法字符尚未自动成为
\((\mathbb Z/M'\mathbb Z)^\times\) 的乘法角色。只有在后续构造出保持来源标签的同态
或标记提升时，(18) 才能注入 Kneser/Fourier 容量；否则它只是严格的 source-switch
负证书，不能单独推出 Erdős--Straus 证书或全局递降。

## 加法 Fourier 到乘法目标群的必要阶障碍

设 \(G_{M'}=(\mathbb Z/M'\mathbb Z)^\times\)，记其群指数为
\(\lambda(M')\)。若存在群同态

\[
\Phi:\mathbb Z/h\mathbb Z\longrightarrow G_{M'}
\]

以及乘法角色 \(\chi:G_{M'}\to\mathbb C^\times\)，使得某个加法频率
\[
x\longmapsto e^{2\pi i tx/h}
\]
在候选集和目标上都等于 \(\chi(\Phi(x))\)，则该频率的阶

\[
o_t=\frac{h}{\gcd(h,t)}
\]
必须满足

\[
\boxed{o_t\mid\lambda(M').}
\tag{19}
\]

事实上 \(\Phi(1)^h=1\)，而 \(G_{M'}\) 的每个元素的阶都整除
\(\lambda(M')\)；故 \(\chi(\Phi(1))\) 的阶同时整除 \(h\) 和
\(\lambda(M')\)，这正是 (19) 的必要条件。特别地，
\(\gcd(h,\lambda(M'))=1\) 时所有此类提升都只能产生平凡频率。

在 \(p=97,D=6,M=24,h=143\) 的除子格负例中，
\(\lambda(24)=2\)、\(\gcd(143,2)=1\)。因此空候选的加法 Fourier 证书不能通过
任何群同态直接转成 \(U(24)\) 的非平凡乘法角色。这一算术边界解释了为什么
“同一模数/同一商群”不足以建立跨状态容量：必须先分解出与
\(\lambda(M')\) 有共同阶的因子商，或改用保留来源标签的非群同态/严格递降。
(19) 只是必要条件，不声称存在提升；目标群的实际子群结构还会给出更强的
不可提升证书。若不预先指定来源标签，只要求某个同态和某个角色实现给定阶的
单个频率，则 \(o_t\mid\lambda(M')\) 对有限阿贝尔群实际上也是充分的：取
\(G_{M'}\) 中阶为 \(o_t\) 的元素，再用角色分离该循环子群即可。真正的
source-labelled 问题还要满足下面的关系格条件。

### 标记关系格的精确提升判据

给定标签 \(x_1,\ldots,x_r\in\mathbb Z/h\mathbb Z\) 和目标单位
\(u_1,\ldots,u_r\in G_{M'}\)，定义

\[
\mathcal R_x=\left\{n\in\mathbb Z^r:
\sum_i n_i x_i\equiv0\pmod h\right\},
\qquad
\mathcal R_u=\left\{n\in\mathbb Z^r:
\prod_i u_i^{n_i}=1\right\}.
\]

固定频率 \(t\)。存在带标签的同态 \(\Phi\) 和角色 \(\chi\) 满足

\[
\Phi(x_i)=u_i,\qquad
\chi(u_i)=e^{2\pi i t x_i/h}\quad(1\le i\le r)
\tag{20}
\]

当且仅当两个关系条件同时成立：

\[
\prod_i u_i^{n_i}=1\quad(n\in\mathcal R_x),
\qquad
\sum_i n_i t x_i\equiv0\pmod h\quad(n\in\mathcal R_u).
\tag{21}
\]

第一条件保证 \(\sum n_i x_i\mapsto\prod u_i^{n_i}\) 在标签生成的加法子群上
良定义；第二条件保证 \(u_i\mapsto e^{2\pi i t x_i/h}\) 在目标生成的乘法子群
上良定义。有限阿贝尔群子群上的复角色可延拓到整个 \(G_{M'}\)，故 (21) 也
是充分条件。两组整数关系都可由 Smith 正规形有限地计算。

因此，(19) 是无标签的阶过滤，(21) 才是把空候选 Fourier 证书真正注入
Type II 乘法容量的 E1/E2 级门槛；任一关系条件失败都给出严格的
LIFT_OBSTRUCTED 回执，而不应继续累加跨状态容量。

当来源只给出局部标签 \(x_i\bmod h_i\) 而 \(h=\prod_i h_i\) 时，式 (20)--(21)
必须先经 CRT 幂等元合并；不能把局部代表直接当作共同 \(\mathbb Z/h\mathbb Z\)
元素。两个以上互素块中这种直接代入的代表无关频率只有零频率，规范局部相位和
\(p=97,h=143\) 的 \(1,3\mapsto133\) 合并见
[Type II CRT 局部标签到全局 Fourier 的幂等元桥](type-II-crt-local-label-idempotent-phase-bridge.md)。

## 奇阶参数群与正确的源块载体

还有一个比 (19) 更强的普遍边界。若

\[
h\equiv-1\pmod{4D'},
\]

则 \(h\) 为奇数。于是任意同态

\[
\Phi:\mathbb Z/h\mathbb Z\longrightarrow
(\mathbb Z/4D'\mathbb Z)^\times
\]

的像是奇阶群，不可能包含二阶元 \(-1\)。因此，任何试图把
\(\mathbb Z/h\mathbb Z\) 上的加法 Fourier 证书直接变成“目标为
\(-1\pmod{4D'}\)”的乘法角色证书的路线都必然失败；这不是
\(\lambda(4D')\) 的偶因子偶然缺失，而是源群奇阶与目标二阶目标的结构冲突。

正确的容量载体必须保留源块计数。对两两互素来源块
\(h_1,\ldots,h_r\)，定义

\[
\rho:\mathbb Z^r\longrightarrow
(\mathbb Z/4D'\mathbb Z)^\times,\qquad
\rho(e_i)=h_i\bmod 4D',
\]

以及除子格参数纤维

\[
\mathcal F(\mathbf n)=
\left\{(D'',A):
(D'',A)\in\mathscr L_D(p),\
A D''\equiv Da_0\pmod{h_i}\ \text{whenever }n_i=1
\right\}.
\tag{22}
\]

若 \(\mathbf1=(1,\ldots,1)\)，则 \(\rho(\mathbf1)=\prod_i h_i\bmod4D'\)；
只有在同时满足

\[
\rho(\mathbf1)=-1,\qquad
\mathcal F(\mathbf1)\ne\varnothing
\tag{23}
\]

时，源块乘积才是可回译的 Type II source-switch。第一项是乘法载体的目标命中，
第二项是整数参数和标记纤维的提升；删去第二项就会把 Kneser 命中误报成证书。
对一般 \(\mathbf n\)，(22) 给出一个源块计数格到 admissible 参数的拉回，而不是
\(\mathbb Z/h\mathbb Z\) 与单位群的同态。

在 \(p=97,M=24\) 的严格反例中，\(h_1=11,h_2=13\) 满足
\(\rho(1,1)=11\cdot13=-1\pmod{24}\)，但
\(\mathcal F(1,1)=\varnothing\)；故 \(\rho\) 的乘法目标命中是伪命中。
这给出一个可计算的源载体门：先在 \(\rho(\{0,1\}^r)\) 上做 Kneser/Fourier，
再逐个检查 (22) 的参数纤维，不能反过来只由乘法积集推断证书。

## 两个算术边界

### 一个真实来源的严格降模例子

取

\[
p=5113,\quad D=6,\quad M=24.
\]

参数 \(a_1=3,a_2=6\) 的来源数为

\[
N_3=5185=17\cdot305,\qquad
N_6=5257=7\cdot751.
\]

取 \(h_1=17,h_2=7\)，则 \(h=119\equiv-1\pmod{24}\)，而带来源 CRT 给出

\[
a_0\equiv3\pmod{17},\quad a_0\equiv6\pmod7,
\qquad a_0\equiv20\pmod{119}.
\]

确有 \(h\mid p+24a_0=5593=119\cdot47\)。选择真除子
\(D'=1,A=1\) 时，

\[
AD'=1\equiv6\cdot20\pmod{119},
\quad M'=4,\quad K'=30,\quad B'=1289.
\]

于是

\[
119=4\cdot1\cdot1\cdot30-1,
\qquad 119\mid30p+1,
\]

并得到 \(m=(1+B')/K'=43\)、\(d=1\) 的 Type II 证书。这里 \(M'=4<24\)，
所以该例确实把混合来源因子降到了严格更小的模数。

### 一个除子格完全排除的边界

在 \(p=97,D=6,M=24\) 的伪池化中，\(h=11\cdot13=143\)，来源 CRT 类可取
\(a_0=133\)。此时

\[
r=Da_0\bmod h=6\cdot133\bmod143=83,
\qquad h=143>D^2=36.
\]

由 (15) 立即得到 \(\mathscr C_D(h,a_0;p)=\varnothing\)：唯一可能的剩余代表
已经大于 \(D^2\)。因此这个混合因子既不能回译为同模数 admissible 参数，也不能
沿 \(D\) 的真除子格降模；这正是一个有限、可复核的 source-switch 负证书，而不是
对整个 Erdős--Straus 猜想的反例。

## 研究边界

(12)--(15) 把“是否存在可下降 source-switch”从模糊的跨状态容量假设变成了有限
算术分支。它仍没有证明每个核心素数都能找到非空候选，也没有证明空候选时一定
存在另一种 Type I/II 证书或更小核心素数。因此后续容量证明必须把 (14) 的空分支
作为显式负证书输入，再证明它迫使 Fourier/商群容量溢出或另一个带 E1--E5 的下降
边；不能把候选集非空当成自动事实。
