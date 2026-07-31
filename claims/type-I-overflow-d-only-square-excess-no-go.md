---
kind: claim
claim_id: type-I-overflow-d-only-square-excess-no-go
title: overflow 补秩的累积支撑互素性与 D-only 平方超额边界
statement: 设核心素数 p 的 absorbed-support overflow 给出 R_M>p、u=4M-R_M 及 pu=4Md+1。若 2<=u<p，则 u=1 (mod 4)、r=p-u 是 4 的正倍数，且每个 D-only 参数 D 都与 M、d、r 互素。source-supported 分支只复述中心 Type I；non-source 分支唯一写成 D=p delta、delta|u^2。若 delta|u，则三个规范平方除子目标全部无解；若 delta 不整除 u，则唯一具有 delta=cw^2、u=acw、lambda=abc、t=bcw、a=w+4rb 的平方载体正规形，其中 w>=3，并满足 delta>=9、u>3sqrt(p)、13u>=12p+9 且 u(u+3)>12p。本卡给出这一必要条件边界；后续同 1 mod 4 秩的全域 no-go 又证明平方超额层同样为空，因而 overflow-to-D-only 已整体关闭。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-marked-support-accumulation-rechart-saturation
  - two-denominator-lift-d-only-marked-normal-form
  - two-denominator-lift-core-d-only-support-dichotomy-three-target-spectrum
  - two-denominator-lift-source-supported-tail-ratio-rigidity
topics:
  - type-I
  - overflow
  - marked-solution
  - two-denominator-lift
  - D-only
  - absorbed-support
  - support-erasure
  - square-excess
  - three-target-spectrum
  - no-go
  - proof-boundary
sources:
  - claim: type-I-marked-support-accumulation-rechart-saturation
    role: overflow-determinant-and-absorbed-support-interface
  - claim: two-denominator-lift-core-d-only-support-dichotomy-three-target-spectrum
    role: non-source-normal-form-and-three-target-interface
  - claim: two-denominator-lift-d-only-marked-normal-form
    role: complete-D-only-parameter-and-size-interface
  - claim: two-denominator-lift-source-supported-tail-ratio-rigidity
    role: source-supported-branch-classification
visibility: public
last_checked: '2026-08-01'
---

# overflow 补秩的累积支撑互素性与 \(D\)-only 平方超额边界

## 1. overflow receipt 与严格补秩

固定核心素数

\[
p\equiv1\pmod {24}.
\tag{1}
\]

设 absorbed-support 重图表已经进入 overflow。沿用
[累积支撑重图表](type-I-marked-support-accumulation-rechart-saturation.md)的记号，存在
正整数 \(M,C,R_M\) 满足

\[
1\le R_M<4M,
\qquad
R_M>p,
\qquad
4MC=pR_M+1.
\tag{2}
\]

定义

\[
u=4M-R_M,
\qquad
d=p-C.
\tag{3}
\]

则 \(u,d>0\)，并有精确 determinant

\[
\boxed{pu=4Md+1.}
\tag{4}
\]

本卡只讨论该 receipt 真正给出较小 equation rank 的情形

\[
2\le u<p.
\tag{5}
\]

若 \(u=1\) 或 \(u\ge p\)，它本身不能作为严格 rank descent；这两支仍须换载体、
直接终端或其它 marked 状态。

由 \(R_M\equiv3\pmod4\) 得

\[
\boxed{u\equiv1\pmod4.}
\tag{6}
\]

令

\[
r=p-u.
\tag{7}
\]

结合 (1)、(5)--(6)，有

\[
\boxed{r\equiv0\pmod4,\qquad r\ge4.}
\tag{8}
\]

所以 overflow 的严格补秩自动避开已经关闭的 \(r=1\) 层；事实上它只进入
\(r\in4\mathbb N\)。

## 2. 累积支撑与自然 determinant 量全部不能进入 \(D\)

式 (4) 立即给出

\[
(M,pu)=1,
\qquad
(d,pu)=1.
\tag{9}
\]

又由 \(0<u<p\) 和 \(p\) 为素数，\((r,p)=(r,u)=1\)，故

\[
(r,pu)=1.
\tag{10}
\]

任意 \(D\in\mathcal D(p,u)\) 都满足

\[
D\mid(pu)^2.
\tag{11}
\]

因此

\[
\boxed{(D,Mdr)=1.}
\tag{12}
\]

这比只排除 \(D=M\) 更强：任何 D-only handoff 都不能在 \(D\) 中保留 absorbed
support \(M\)，也不能直接使用 determinant 的 \(d\) 或 rank gap \(r\) 作为新因子。
若后继需要重置 accumulated support，必须由较小 equation rank \(u<p\) 或更外层的
良基势支付；(12) 本身不是 E4。

还有一个有用的互补恒等式。由 (2)--(4) 得

\[
\boxed{uC-R_Md=1.}
\tag{13}
\]

并且

\[
R_M>p
\iff
C(p+u)>p^2+1.
\tag{14}
\]

因为 \(u<p\)，式 (14) 特别推出

\[
\boxed{C>\frac p2.}
\tag{15}
\]

所以 \(C\) 是大互补量；它若要参与 D-only，只能通过与 \(u^2\) 的共同平方指数进入，
不能作为由 (4) 自动提供的因子。

## 3. \(D\)-only 支撑二分

对任意 \(D\in\mathcal D(p,u)\)，核心 D-only 支撑二分给出且只给出以下两支：

1. \(D\mid u^2\)。这是 source-supported 分支，其标记非空性精确等价于目标
   \(p\) 图表已有中心 Type I 命中；
2. \(D\nmid u^2\)。此时唯一写成
   \[
   \boxed{D=p\delta,\qquad\delta\mid u^2,}
   \tag{16}
   \]
   并存在正整数 \(\lambda\) 使
   \[
   \mu=4\lambda-1,
   \qquad
   H=\frac{u^2}{\delta}=p+\mu r,
   \qquad
   H\mid4\lambda^2.
   \tag{17}
   \]

在 terminal-first 的中心 miss 状态中，第 1 支标记纤维为空。因此新的递归出口只能来自
(16)--(17) 的 non-source-supported 分支，并且还必须证明其三目标标记集非空。

## 4. 原指数预算层的全域空纤维定理

现在假设 (16)--(17) 还满足

\[
\delta\mid u.
\tag{18}
\]

写

\[
H=uh,
\qquad
h=\frac u\delta,
\qquad
h\mid u.
\tag{19}
\]

由 \(H=p+\mu r\)、\(p=u+r\) 和 \(\mu=4\lambda-1\)，得到

\[
u(h-1)=4\lambda r.
\tag{20}
\]

式 (6)、\((u,r)=1\) 给出 \((u,4r)=1\)，所以 \(u\mid\lambda\)。唯一写成

\[
\boxed{
\lambda=\ell u,
\qquad
h=1+4\ell r,
\qquad
\mu=4\ell u-1,}
\tag{21}
\]

其中 \(\ell\ge1\)。又因 \(h\mid u\)，有

\[
u\ge h\ge1+4r,
\qquad
\lambda\ge u.
\tag{22}
\]

标记纤维非空当且仅当存在

\[
v\mid\lambda^2,
\qquad
0<v<\lambda,
\tag{23}
\]

命中以下三个模 \(\mu\) 目标之一：

\[
\begin{array}{c|c}
e&v\pmod\mu\\ \hline
0&-p\lambda\\
1&-\lambda\\
2&-p^{-1}\lambda.
\end{array}
\tag{24}
\]

下面逐一排除。

### 4.1 中间目标 \(e=1\)

若命中，则 \(\mu\mid v+\lambda\)。但

\[
0<v+\lambda<2\lambda<4\lambda-1=\mu,
\tag{25}
\]

矛盾。

### 4.2 目标 \(e=0\)

若命中，则 \(\mu\mid v+p\lambda\)。利用 \(4\lambda\equiv1\pmod\mu\)，得到

\[
\mu\mid4v+p.
\tag{26}
\]

由 (22) 有 \(r\le(u-1)/4\)，所以

\[
p=u+r\le\frac{5u-1}{4}\le\frac{5\lambda-1}{4}.
\tag{27}
\]

结合 \(v\le\lambda-1\)，得到

\[
0<4v+p<2\mu.
\tag{28}
\]

因此 (26) 只能要求 \(4v+p=\mu\)。然而

\[
4v+p\equiv1\pmod4,
\qquad
\mu\equiv3\pmod4,
\tag{29}
\]

仍然矛盾。

### 4.3 目标 \(e=2\)

若命中，则 \(\mu\mid pv+\lambda\)。由 \(H=p+\mu r=uh\) 和 (21)，

\[
p\equiv uh\pmod\mu,
\qquad
(u,\mu)=1,
\]

所以

\[
\mu\mid hv+\ell.
\tag{30}
\]

写

\[
hv+\ell=L\mu,
\qquad L\in\mathbb N.
\tag{31}
\]

由 \(v\le\ell u-1\) 与 \(4\ell<3h\)，有

\[
4(hv+\ell)<h(4\ell u-1)=h\mu,
\]

故

\[
0<L<\frac h4.
\tag{32}
\]

另一方面，\(h\mid u\) 使 \(\mu\equiv-1\pmod h\)。将 (31) 模 \(h\) 化简，得到

\[
h\mid L+\ell.
\tag{33}
\]

但 \(r\ge4\) 与 \(h=1+4\ell r\) 给出 \(\ell<h/16\)。结合 (32)，

\[
0<L+\ell<\frac{5h}{16}<h,
\tag{34}
\]

与 (33) 矛盾。

三个目标全部为空。因此证明了

\[
\boxed{
D=p\delta,\ \delta\mid u
\Longrightarrow
W(p,u,D)=\varnothing.}
\tag{35}
\]

这包含 \(D=p\) 以及所有 \(D=p\delta\)、\(\delta\mid u\) 的自然一层因子候选，
不依赖有限样本上界。

## 5. 唯一幸存区域的平方载体正规形

由第 3--4 节，在中心 miss 后若要得到 genuinely new 且非空的 D-only 后继，必要条件是

\[
\boxed{
D=p\delta,
\qquad
\delta\mid u^2,
\qquad
\delta\nmid u.}
\tag{36}
\]

等价地，存在某个 \(q\mid u\)，使

\[
v_q(u)<v_q(\delta)\le2v_q(u).
\tag{37}
\]

这正是相对于 \(u\) 原指数盒的平方超额。它还有一个无冗余的显式平方载体参数化。
令

\[
g=(u,\delta),
\qquad
u=ga,
\qquad
\delta=gw,
\qquad
(a,w)=1.
\tag{38}
\]

由 \(\delta\mid u^2\) 得 \(w\mid g\)，写 \(g=cw\)。条件
\(\delta\nmid u\) 等价于 \(w>1\)。因为 \(u\) 为奇数，\(w\) 也是奇数，所以

\[
w\ge3.
\tag{39}
\]

non-source 正规形还给出正整数 \(t\) 满足

\[
\delta=u-4rt,
\qquad
\delta\lambda=ut.
\tag{40}
\]

将 (38) 代入，先由 \(w\lambda=at\) 和 \((a,w)=1\) 写
\(\lambda=ab_0,t=wb_0\)。再由第一式和 \((c,4r)=1\) 得 \(c\mid b_0\)。
写 \(b_0=bc\)，便得到

\[
\boxed{
\delta=cw^2,
\qquad
u=acw,
\qquad
\lambda=abc,
\qquad
t=bcw,
\qquad
a=w+4rb,}
\tag{41}
\]

其中 \(a,b,c,w\) 为正整数、\((a,w)=1\)、\(w\ge3\)。反过来，(41) 精确恢复
(38)--(40)，所以平方超额不是只有 valuation 描述；它必须携带显式平方因子 \(w^2\)。

## 6. 大补秩阈值

式 (41) 首先给出

\[
\boxed{\delta=cw^2\ge9.}
\tag{42}
\]

D-only 的严格大小 \(D=p\delta<u^2\) 于是推出

\[
\boxed{u>3\sqrt p.}
\tag{43}
\]

又因 \(t=bcw\ge3\)，式 (40) 给出

\[
u=\delta+4rt\ge9+12r.
\]

代入 \(r=p-u\)，得到更强的线性窗口

\[
\boxed{13u\ge12p+9.}
\tag{44}
\]

所以潜在 square-excess rank 必须非常接近 \(p\)，而不只是大于 \(\sqrt p\)。

此外 \(u\equiv1\pmod4\)，通用 D-only 尺寸界中的 \(\kappa=3\)，故

\[
D\le u(u+3)-3p.
\tag{45}
\]

将 \(D=p\delta\ge9p\) 代入，先得到 \(u(u+3)\ge12p\)。事实上 (44) 还给出
\(12r\le u-9\)，所以

\[
\begin{aligned}
u(u+3)-12p
&=u^2-9u-12r\\
&\ge u^2-10u+9\\
&=(u-1)(u-9)>0.
\end{aligned}
\]

因此可加强为

\[
\boxed{u(u+3)>12p.}
\tag{46}
\]

所以所有不满足 (43)--(46) 的 overflow 补秩都不可能产生新的非空 D-only 后继。
若尝试由互补量 \(C\) 构造 \(\delta\)，唯一尚可能的部分来自

\[
\delta\mid(C,u^2),
\qquad
\delta\nmid u,
\tag{47}
\]

即 \(C\) 必须真的携带 \(u^2\) 的平方超额指数。

## 7. 本卡得到的选择器边界

本卡完成的是 overflow-to-D-only 的必要条件压缩，不是存在性定理：

1. \(u\ge p\) 时没有较小 equation rank；
2. \(2\le u<p\) 时，所有 \(D\) 都擦除 \(M,d,r\) 的因子支撑；
3. source-supported 分支只复述已有中心 Type I；
4. non-source 的原预算层 \(\delta\mid u\) 全空；
5. 仅凭本卡的论证，当时尚未排除满足 (36)、(41)、(43)--(46) 的近 \(p\)
   平方超额候选。

一个同时来自真实 clean slab 的边界为

\[
(p,R,Q,R_M,u)=(1129,1023,1021,2959,1125).
\]

这里 \(1021+2=1023\) 是 clean slab，并且同一个 overflow 补秩有两个合法 non-source
参数：

\[
\delta=5\mid u
\qquad\text{和}\qquad
\delta=405\mid u^2,\quad\delta\nmid u.
\]

前者由 (35) 无样本排除；后者已经进入 square-excess，但其三目标仍全部 miss。
最小的聚焦 square-excess 边界

\[
(p,u,\delta,D)=(193,185,25,4825)
\]

也有空标记纤维。这说明 (36)、(41)、(43)--(46) 只是严格必要条件，不是非空充分条件。

后续的同余类 no-go 已经继续证明 (41) 的三个目标也恒空。因此平方载体现在只保留为
被排除分支的正规形，不再是待搜索的 E4 候选。完整闭合见
[同 1 mod 4 秩的 non-source D-only 标记纤维全域空定理](two-denominator-lift-same-one-mod-four-no-go.md)。

聚焦复现入口为

~~~bash
python3 reproductions/type_i_overflow_d_only_square_excess_no_go.py
python3 reproductions/type_i_overflow_d_only_square_excess_no_go.py --verify
~~~

结果文件为

~~~text
reproductions/type-i-overflow-d-only-square-excess-no-go-results.json
~~~

对应 SHA-256 为

~~~text
52d3e7d97279aa9b40fda7da7dfaafd09965a4d6b14dc2a5f147b417a27c4582  reproductions/type_i_overflow_d_only_square_excess_no_go.py
741aa57d2916a96a5a94100ad4cbb2c9860ff3c993b3bd0b560344eb2f920f1a  reproductions/type-i-overflow-d-only-square-excess-no-go-results.json
~~~

该脚本只核对五个聚焦 overflow receipt、支撑互素性、一个原预算 no-go 参数和两个
square-excess 空纤维参数；它不扫描历史数据，也不承担后续全域 no-go 的证明。
