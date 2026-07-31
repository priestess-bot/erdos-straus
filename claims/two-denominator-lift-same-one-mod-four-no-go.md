---
kind: claim
claim_id: two-denominator-lift-same-one-mod-four-no-go
title: 同 1 mod 4 秩的 non-source D-only 标记纤维全域空定理
statement: 设 p 是满足 p=1 (mod 4) 的奇素数，2<=n<p 且 n=1 (mod 4)。对任意合法 D-only 参数 D，若 D 不整除 n^2，则 W(p,n,D) 为空。更精确地，non-source 正规形唯一写成 H=a^2 c、lambda=abc、n=acw、delta=cw^2、a=w+4rb；规范 e=1、e=2 目标由大小直接排除，e=0 命中会导出 2XY=X^2/L+Y^2/m+1/c，其中 X 为奇数、Y 为偶数且 L>1，而奇偶保持的 Vieta 极小下降证明该方程无正整数解。因此 source-supported 分支只复述中心 Type I，non-source 分支全空；特别地，overflow 的严格补秩不能通过 D-only 构造新的 E4。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - two-denominator-lift-d-only-marked-normal-form
  - two-denominator-lift-core-d-only-support-dichotomy-three-target-spectrum
  - two-denominator-lift-source-supported-tail-ratio-rigidity
topics:
  - descent
  - marked-solution
  - two-denominator-lift
  - D-only
  - same-residue-class
  - three-target-spectrum
  - Vieta-jumping
  - no-go
  - overflow
  - proof-boundary
sources:
  - claim: two-denominator-lift-core-d-only-support-dichotomy-three-target-spectrum
    role: non-source-normal-form-and-three-target-interface
  - claim: two-denominator-lift-d-only-marked-normal-form
    role: complete-D-only-parameter-and-lift-interface
  - claim: two-denominator-lift-source-supported-tail-ratio-rigidity
    role: source-supported-equivalence
visibility: public
last_checked: '2026-08-01'
---

# 同 \(1\pmod4\) 秩的 non-source \(D\)-only 标记纤维全域空定理

## 1. 定理范围

设 \(p\) 为奇素数，且

\[
p\equiv1\pmod4.
\tag{1}
\]

取

\[
2\le n<p,
\qquad
n\equiv1\pmod4,
\qquad
r=p-n.
\tag{2}
\]

于是

\[
r\in4\mathbb N,
\qquad
r\ge4.
\tag{3}
\]

对任意合法 \(D\)-only 参数

\[
D\in\mathcal D(p,n),
\tag{4}
\]

已有支撑二分：

1. \(D\mid n^2\) 是 source-supported 分支，其标记非空性精确等价于相应中心
   Type I 尾谱已经命中；
2. \(D\nmid n^2\) 是 non-source-supported 分支，并唯一写成
   \[
   D=p\delta,
   \qquad
   \delta\mid n^2.
   \tag{5}
   \]

本卡证明第二支恒空：

\[
\boxed{
D\nmid n^2
\Longrightarrow
W(p,n,D)=\varnothing.}
\tag{6}
\]

因此在中心 Type I miss 状态中，(4) 的每个标记纤维都为空。数值上的
\(n<p\) 不能挽救空 marked state，故这类 \(D\)-only 数据不能充当新的 E4。

该结论只要求 (1)--(3)，范围比核心条件 \(p\equiv1\pmod {24}\) 更广。

## 2. non-source 参数的统一平方载体正规形

固定 (5)。已有完全正规形给出正整数 \(\lambda,t\)，使

\[
\mu=4\lambda-1,
\qquad
H=\frac{n^2}{\delta}=p+\mu r,
\qquad
H\mid4\lambda^2,
\tag{7}
\]

以及

\[
s=\frac{4\lambda^2}{H},
\qquad
t=\lambda-rs>0.
\tag{8}
\]

由 (1)、(3) 和 \(\mu\) 为奇数，\(H\) 为奇数。因此 (7) 实际给出

\[
H\mid\lambda^2.
\tag{9}
\]

令 \(g=(H,\lambda)\)。式 (9) 说明 \(H/g\mid g\)。置

\[
a=\frac Hg,
\qquad
c=\frac ga,
\qquad
b=\frac\lambda g.
\tag{10}
\]

则唯一得到

\[
\boxed{
H=a^2c,
\qquad
\lambda=abc,
\qquad
(a,b)=1.}
\tag{11}
\]

由 (8)、(11)，

\[
s=4b^2c,
\qquad
t=bc(a-4rb).
\tag{12}
\]

定义

\[
w=a-4rb.
\tag{13}
\]

正性 \(t>0\) 给出 \(w>0\)。又由

\[
H=n+4r\lambda
\tag{14}
\]

和 (5)、(11)--(13)，得到完整统一正规形

\[
\boxed{
n=acw,
\qquad
\delta=cw^2,
\qquad
t=bcw,
\qquad
a=w+4rb.}
\tag{15}
\]

这里 \(a,c,w\) 都为奇数。结合 (3)，还有

\[
\boxed{a>16b.}
\tag{16}
\]

此外

\[
(H,r)=(p,r)=1,
\]

所以 \((a,r)=1\)。结合 \((a,b)=1\)、\(a,w\) 为奇数和 \(w=a-4rb\)，得到

\[
(a,w)=1.
\]

式 (15) 同时包含先前分开的两层：

\[
\delta\mid n\iff w=1,
\qquad
\delta\nmid n\iff w\ge3.
\tag{17}
\]

所以所谓 square-excess 只是 \(w\ge3\) 的子区域，不需要再单独假设。

## 3. 三目标中的两个大小障碍

标记纤维非空当且仅当存在

\[
v\mid\lambda^2,
\qquad
0<v<\lambda,
\tag{18}
\]

命中模 \(\mu\) 的三个目标之一：

\[
\begin{array}{c|c}
e&v\pmod\mu\\ \hline
0&-p\lambda\\
1&-\lambda\\
2&-p^{-1}\lambda.
\end{array}
\tag{19}
\]

### 3.1 中间目标 \(e=1\)

若命中，则 \(\mu\mid v+\lambda\)。但

\[
0<v+\lambda<2\lambda<4\lambda-1=\mu,
\tag{20}
\]

矛盾。这个排除对每个规范 non-source \(D\)-only 状态都成立，并不需要
同余类假设。

### 3.2 逆目标 \(e=2\)

由 (7)、(11)，

\[
p\equiv a^2c\pmod\mu.
\tag{21}
\]

又因 \(4abc=\mu+1\)，

\[
a^{-1}\equiv4bc\pmod\mu.
\tag{22}
\]

注意 \((p\lambda,\mu)=1\)：\((\lambda,\mu)=1\)，而
\((p,\mu)=(H,\mu)=1\) 由 \(H\mid4\lambda^2\) 得到。因此 (21)--(22) 给出

\[
p^{-1}\lambda
\equiv4b^2c
\pmod\mu.
\tag{23}
\]

若 \(e=2\) 命中，则

\[
\mu\mid v+4b^2c.
\tag{24}
\]

但 (16) 给出

\[
4b^2c<\frac\lambda4,
\tag{25}
\]

所以

\[
0<v+4b^2c<\frac54\lambda<\mu.
\tag{26}
\]

再次矛盾。这里甚至没有使用 \(v\mid\lambda^2\)。

## 4. 奇偶 Vieta 空解引理

处理 \(e=0\) 前先证明一个独立的整数引理。

> **引理。** 设 \(L,m,c\) 为正整数且 \(L>1\)。不存在正整数 \(X,Y\)，使
> \(X\) 为奇数、\(Y\) 为偶数并满足
> \[
> 2XY=\frac{X^2}{L}+\frac{Y^2}{m}+\frac1c.
> \tag{27}
> \]

反设这样的解存在。固定 \(L,m,c\)，在所有所需奇偶型的正整数解中取
\(X+Y\) 最小者。把 (27) 分别视为关于 \(X\)、\(Y\) 的二次方程，Vieta 伴根为

\[
X^*=2LY-X,
\qquad
Y^*=2mX-Y.
\tag{28}
\]

对应根积分别为

\[
XX^*=L\left(\frac{Y^2}{m}+\frac1c\right)>0,
\qquad
YY^*=m\left(\frac{X^2}{L}+\frac1c\right)>0.
\tag{29}
\]

因此 \(X^*,Y^*\) 都是正整数；(28) 还保持 \(X\) 奇、\(Y\) 偶。极小性于是强制

\[
X\le LY,
\qquad
Y\le mX.
\tag{30}
\]

令

\[
A=LY-X,
\qquad
B=mX-Y.
\tag{31}
\]

由于 \(LY\) 为偶数而 \(X\) 为奇数，\(A\) 是正奇数；并且 \(B\ge0\)。将
(27) 清分母并用 (31) 分组，得到

\[
\boxed{Lm=cXmA+cYLB.}
\tag{32}
\]

故

\[
L\ge cXA.
\tag{33}
\]

若 \(A<L\)，则 \(Y\ge2\) 给出

\[
X=LY-A>L,
\]

与 \(L\ge cXA\ge X\) 矛盾。若 \(A\ge L\)，(33) 强制

\[
A=L,
\qquad
c=X=1.
\]

再代回 \(A=LY-X\)，得到

\[
(Y-1)L=1,
\]

这与 \(L>1\) 矛盾。引理得证。

条件 \(L>1\) 不能删除：\((X,Y,L,m,c)=(1,2,1,2,1)\) 正好满足 (27)。

## 5. 正目标 \(e=0\) 导出的不可能 Vieta 方程

反设存在 (18) 命中 \(e=0\)。由 \(4\lambda\equiv1\pmod\mu\)，存在正整数
\(j\) 满足

\[
4v+p=j\mu.
\tag{34}
\]

令

\[
L=r+j.
\tag{35}
\]

结合 (3)、(7)、(11)、(34)，

\[
\boxed{4v+a^2c=L\mu,}
\qquad
L\ge r+1\ge5.
\tag{36}
\]

置互补因子

\[
Y_1=\frac{\lambda^2}{v}.
\tag{37}
\]

因 (34) 使 \(v\) 在模 \(\mu\) 下可逆，(19) 的因子互补把 \(Y_1\) 送到
\(e=2\) 目标。由 (23)，存在正整数 \(m\) 使

\[
\boxed{Y_1+4b^2c=m\mu.}
\tag{38}
\]

现在利用

\[
(4v)Y_1=4\lambda^2=(a^2c)(4b^2c).
\tag{39}
\]

将 (36)、(38) 代入 (39) 并展开，消去非零的 \(\mu\)，得到

\[
Lm\mu=a^2cm+4b^2cL.
\tag{40}
\]

再用 \(\mu=4abc-1\) 化简为

\[
\boxed{
4ab=\frac{a^2}{L}+\frac{4b^2}{m}+\frac1c.}
\tag{41}
\]

取

\[
X=a,
\qquad
Y=2b.
\tag{42}
\]

则 \(X\) 为奇数、\(Y\) 为偶数，而 (41) 正是

\[
2XY=\frac{X^2}{L}+\frac{Y^2}{m}+\frac1c.
\]

这与第 4 节在 \(L\ge5>1\) 下的引理矛盾。因此 \(e=0\) 也恒空。结合
第 3 节，三个目标全部无解，证明 (6)。

## 6. 对 overflow 和选择器合同的含义

absorbed-support overflow 的严格补秩满足

\[
u=4M-R_M,
\qquad
2\le u<p,
\qquad
u\equiv1\pmod4.
\tag{43}
\]

所以本定理可以直接代入 \(n=u\)。在 terminal-first 的中心 miss 状态中：

1. source-supported \(D\mid u^2\) 只复述中心 Type I，因而为空；
2. non-source-supported \(D\nmid u^2\) 由 (6) 全部为空；
3. 原先的 \(\delta\mid u\) 与 square-excess \(\delta\nmid u\) 两层都已经被统一删除。

因此 overflow-to-D-only 应由 verifier 记录为 `rejected_branch`，不能创建后继状态：

- E1 可以验证 receipt 和候选参数；
- E2 不应输出 D-only 后继；
- E3 应引用本 no-go 与 source-supported 等价；
- E4 不存在，空映射不是 solution lift；
- E5 中的 \(u<p\) 不能替代 E4。

这不证明 overflow 已闭合。剩余合法出口必须改变双尾保留模式、尾比或实际支撑，例如：

- 从 source/path/node 锚定的另一载体得到直接 Type I/II；
- 找到 clean alternate slab 且新规范代表小于 \(p\)，使用已有 MARKED_ABSORB 边；
- 把实际底层节点送入 competing-excess，并证明其 SCC 最终产生 clean slab 或直接终端。

单独的平方因子 \(w\)、Fourier miss 或容量超额都不能代替上述跨状态算术桥。

## 7. 聚焦边界与复现

三个精确代表说明本定理同时覆盖自然层和平方超额层：

\[
\begin{array}{c|c|c|c|c|c}
p&n&r&(a,b,c,w)&\delta&\lambda\\ \hline
73&65&8&(65,2,1,1)&1&130\\
193&185&8&(37,1,1,5)&25&37\\
673&657&16&(73,1,1,9)&81&73.
\end{array}
\tag{44}
\]

第三行的 \(e=0\) 最小正目标为 \(50<73\)，但 \(50\nmid73^2\)；所以全域证明
不能只依赖目标落在规范区间之外。

真实 clean overflow

\[
(p,u,M,R_M)=(1129,1125,1021,2959)
\]

中的 \(\delta=5\) 与 \(405\) 分别对应 \(w=1\) 与 \(w=9\)，现在由同一定理关闭。

聚焦复现入口为

~~~bash
python3 reproductions/two_denominator_lift_same_one_mod_four_no_go.py
python3 reproductions/two_denominator_lift_same_one_mod_four_no_go.py --verify
~~~

结果文件为

~~~text
reproductions/two-denominator-lift-same-one-mod-four-no-go-results.json
~~~

对应 SHA-256 为

~~~text
070a3a987500dc485c87e6c1caf4b19c9ffd239c40e3bc9ad375789bfafcc57d  reproductions/two_denominator_lift_same_one_mod_four_no_go.py
40816983ef4c497ac67781100e317c06d21110edda7c9e84acc63972ca27362a  reproductions/two-denominator-lift-same-one-mod-four-no-go-results.json
~~~

该复现只核对五个参数、完整 \(D\)-only 条件、统一正规形和三个目标 miss；它不是
历史扫描，也不是全称证明的替代品。全称性来自第 2--5 节的代数与 Vieta 引理。
