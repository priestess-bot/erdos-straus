---
kind: claim
claim_id: type-I-linear-private-carrier-support-exit-marked-equivalence
title: 线性私有载体的跨状态支撑退出与共享两尾等价
statement: 设核心素数 p 的线性源状态含块 t_0R_0+1 被奇素数 q 整除，且 0<R_0<q。对任意合法模数 r，q|K_r=(pr+1)/4 当且仅当 r=R_0 (mod q)；若该块还满足完整有序源谱私有唯一性，则除原无序源状态外，所有其它线性源的 K 支撑均不含 q。另一方面，对任意线性源 p=a+s+asR，共享两尾的严格偶源标记解与同一 R 上的 Type I 中心化平方除子命中双射。因此较小 R 的 Type I 命中确是 q-free 换支撑终端，但共享两尾 marked lift 不是独立递降分支；原状态为 F-box miss 时该标记解集为空。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-linear-private-carrier-isolation-criterion
  - type-I-linear-cross-modulus-gcd-rigidity
  - type-I-general-b-centered-square-spectrum
  - type-I-normal-source-state-realization
topics:
  - type-I
  - linear-source
  - private-carrier
  - support-exit
  - marked-lift
  - centered-square-spectrum
  - descent
  - proof-program
sources:
  - claim: type-I-linear-private-carrier-isolation-criterion
    role: complete-ordered-source-private-block-uniqueness
  - claim: type-I-linear-cross-modulus-gcd-rigidity
    role: cross-modulus-support-rigidity
  - claim: type-I-general-b-centered-square-spectrum
    role: exact-target-spectrum-coordinate
  - claim: type-I-normal-source-state-realization
    role: exact-source-and-target-normal-form-lift
visibility: public
last_checked: '2026-07-30'
---

# 线性私有载体的跨状态支撑退出与共享两尾等价

## 私有素数所在的模数直线

设

\[
p=t_0+u_0+t_0u_0R_0,
\qquad q\mid t_0R_0+1,
\qquad 0<t_0,R_0<q,
\tag{1}
\]

其中 \(p\equiv1\pmod4\)，\(q\) 为奇素数。由 (1) 有

\[
p\equiv t_0\pmod q,
\qquad t_0R_0\equiv-1\pmod q.
\tag{2}
\]

对任意使

\[
K_r=\frac{pr+1}{4}\in\mathbb Z
\tag{3}
\]

的正整数 \(r\)，由于 \(q\ne2\)，式 (2) 给出精确等价

\[
\boxed{
q\mid K_r
\iff q\mid pr+1
\iff t_0r\equiv-1\pmod q
\iff r\equiv R_0\pmod q.}
\tag{4}
\]

特别地，

\[
0<r<R_0<q
\quad\Longrightarrow\quad
q\nmid K_r.
\tag{5}

所以任何真正向下的合法换模都会自动移除当前 \(q\) 支撑。这一结论只使用块整除与
\(R_0<q\)，尚不需要完整谱私有性。它也可由跨模数公因子刚性

\[
\gcd(K_{R_0},K_r)
=\gcd\left(K_{R_0},\frac{R_0-r}{4}\right)
\]

直接读出。

## 完整私有性给出的全谱支撑退出

进一步假设 (1) 的有序块满足
[完整线性源谱私有唯一性判据](type-I-linear-private-carrier-isolation-criterion.md)。
任取另一线性源

\[
p=a+s+asr,
\qquad
4K_r=(ar+1)(sr+1).
\tag{6}
\]

若 \(q\mid K_r\)，则奇素数 \(q\) 必整除 (6) 的一个块。若它整除 \(ar+1\)，对
有序源 \((a,s,r)\) 调用私有唯一性；若它整除 \(sr+1\)，则对交换后的有序源
\((s,a,r)\) 调用同一定理。两种情形都迫使 (6) 是原来的同一个无序源状态。因此

\[
\boxed{
\text{除原无序源状态外，完整线性谱中所有其它状态都满足 }q\nmid K_r.}
\tag{7}
\]

式 (4) 说明 \(q\) 在全部整数模数上只能位于一条剩余类直线；式 (7) 更强，它说明这条
直线与完整线性源谱的交点只有原状态。这里的“状态”按交换 \(a,s\) 取商；交换坐标不会
制造第二个 \(K_r\) 或第二份支撑。

## 共享两尾标记集的精确等价

现在固定任意线性源

\[
p=a+s+asR,
\qquad s\equiv1\pmod2,
\qquad R\equiv3\pmod4,
\tag{8}
\]

并记

\[
K=\frac{pR+1}{4},
\qquad E=sR+1,
\qquad n=p-s=aE.
\tag{9}
\]

线性分解给出

\[
4K=(aR+1)E.
\tag{10}
\]

于是逐式有

\[
\boxed{
\frac4n-\frac1{aK}
=\frac RK
=\frac4p-\frac1{pK}.}
\tag{11}

定义共享两尾的源、目标标记集

\[
\mathcal W_{a,s,R}
=\left\{(aK,U,V):
\frac4n=\frac1{aK}+\frac1U+\frac1V\right\},
\tag{12}
\]

\[
\mathcal T_{p,R}
=\left\{(pK,U,V):
\frac4p=\frac1{pK}+\frac1U+\frac1V\right\}.
\tag{13}

由 (11)，映射

\[
(aK,U,V)\longmapsto(pK,U,V)
\tag{14}
\]

在 (12) 与 (13) 间是双射。更关键的是，这个源标记集非空不比目标 Type I 命中更弱。

确实，若

\[
\frac RK=\frac1U+\frac1V,
\tag{15}
\]

则 \(RU-K>0\)、\(RV-K>0\)，并且

\[
(RU-K)(RV-K)=K^2.
\tag{16}

令 \(D=RU-K\)。交换 \(U,V\) 后可以取 \(D<K\)；等号 \(D=K\) 会由
\(D\equiv-K\pmod R\)、\((K,R)=1\) 迫使 \(R\mid2\)，不可能。因此 (15) 推出

\[
D\mid K^2,
\qquad 1\le D<K,
\qquad D\equiv-K\pmod R.
\tag{17}

反过来，任取满足 (17) 的 \(D\)，置

\[
U=\frac{K+D}{R},
\qquad
V=\frac{K+K^2/D}{R},
\tag{18}

即可直接恢复 (15)。整数性来自 (17)，正性显然。

把 \(g=(D,K)\) 代入

\[
B=\frac Dg,
\qquad C=\frac{g^2}{D},
\qquad H=\frac Kg,
\qquad A=\frac{B+H}{R},
\tag{19}

便得到

\[
U=ABC,
\qquad V=ACH,
\qquad D=B^2C,
\tag{20}

以及一般 \(B\) 的 Type I 正规形。故

\[
\boxed{
\mathcal W_{a,s,R}\ne\varnothing
\iff
\mathcal T_{p,R}\ne\varnothing
\iff
-1\in\mathcal C_R(K)
\iff
\text{同一 }R\text{ 上有 Type I 目标命中}.}
\tag{21}

因为 \(s,R\) 都是奇数，\(E\) 与 \(n=aE\) 都是偶数；并且 \(2\le n<p\)。所以
(21) 的命中同时给出一张直接 Type I 证书和显式严格偶源终端

\[
\frac4n
=\frac1{aK}+\frac1{ABC}+\frac1{ACH},
\qquad
\frac4p
=\frac1{pK}+\frac1{ABC}+\frac1{ACH}.
\tag{22}

这不是“先假设较小实例有任意解”再提升；源端所需的标记解已由同一个目标平方除子显式
构造。反过来，若该 \((R,K)\) 是有限指数 F-box miss，则 (17) 不存在，故
\(\mathcal W_{a,s,R}\) 严格为空。**因此共享两尾 marked lift 不能作为与同状态 Type I
命中并列的独立第三分支。** 真正独立的递降必须改变标记分母、两条保留尾、\(K\) 支撑
或提升结构，并单独证明新标记状态非空。

## 两个容量余核的实际向下退出

此前两个容量一代理余核都有严格更小的线性模数命中：

| \(p\) | 原 \((R_0,q)\) | 新 \(R\) | 新 \(K\) | \(D\) | \((A,B,C,H;m)\) |
|---:|:---:|---:|---:|---:|:---|
| 99151369 | \((82011,115561)\) | 11 | 272666265 | 261 | \((284918,3,29,3134095;95)\) |
| 487572409 | \((318051,6965317)\) | 23 | 2803541352 | 684 | \((534619,3,76,12296234;119)\) |

第一例可取线性源 \((a,s)=(8262614,1)\)，第二例可取
\((a,s)=(20315517,1)\)。二者都由 (22) 给出源 \(p-1\) 的严格偶终端。又因新
\(R<R_0<q\)，式 (5) 保证新 \(K\) 不含原私有 \(q\)。第一例的新旧 \(K\) 仍共享
素数 \(5\)，所以这里应称为“退出私有 \(q\) 支撑”，不能夸大为整个支撑互素；第二例
的新旧 \(K\) 才互素。

因此这两个有限对象不仅已有候选差生成的 Type II 旁路，也已经真实落入“较小 \(R\)、
不含原私有 \(q\) 的 Type I 偶终端”分支。

## 私有性本身不选择固定 p 减一射线

私有支撑退出是必要的逻辑清理，不是新状态存在定理。单点 \(p=297049\) 给出一个精确
边界。它有两组满足完整唯一性判据的载体：

\[
(t,u,R_0,q,d_0,n_0)=(94,9,351,6599,5,45),
\tag{23}
\]

\[
(19,3,5211,9901,10,30).
\tag{24}

既有完整枚举已经排除该素数的所有 \(p-1\) Type I 最大尾桥和普通 \(p-1\) Type II
双尾。实际 Type I 退出必须移动到

\[
(a,s,R)=(624,25,19),
\quad K=1410983,
\quad D=71,
\quad(A,B,C,H;m)=(1046,1,71,19873;15).
\tag{25}

所以私有性本身不能推出 \(s=1\)、\(a=1\)、固定 \(p-1\) 射线或任何预先冻结的有限旧
菜单。它没有反驳逃逸三分支：式 (25) 正是更小 \(R\) 的严格偶终端，而且该点还有独立
Type II 证书。它也没有验证当前容量模型中的强制过载，不能被误作“私有加过载”的反例。

## 剩余全称缺口

本卡证明了两个接口：一旦找到另一线性命中状态，原私有 \(q\) 不会被循环复用；一旦使用
共享两尾提升，它与新状态 Type I 命中是同一张证书。尚未证明的存在性箭头仍是

\[
\text{选择不变的私有载体缺陷}
\Longrightarrow
\begin{cases}
\text{另一合法状态的 Type I 命中},\\
\text{或独立 Type II 正规形},\\
\text{或不同标记/不同支撑且可递归闭合的严格下降}.
\end{cases}
\tag{26}

其中“选择不变”不能只指一个确定性最短关系向量；还必须覆盖完整目标纤维或明确定义的
Pareto 集。式 (26) 才是私有载体逃逸引理仍未证明的内容。
