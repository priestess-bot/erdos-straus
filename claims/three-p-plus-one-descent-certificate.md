---
kind: claim
claim_id: three-p-plus-one-descent-certificate
title: 来自 (3p+1)/4 的完整二分母递降分类与平方根级 Type I 证书
statement: 对核心素数 p=1 mod24，令 n=(3p+1)/4，并令 W_p={(n,b,c) in Sol(n)}。映射 (n,b,c)->(np,b,c) 在全体 W_p 上提升到 Sol(p)，且 W_p 非空当且仅当 n 含有 q=2 mod3 的素因子。更强地，任何从 Sol(n) 到 Sol(p) 的二分母保留提升都必替换坐标 n，故完全落入此 W_p 分支。取最小此类 q，有 q^2<=n；令 r=(n/q+1)/3、m=(4q+1)/3、x=qr、d=qr^2，则 (m,d) 是 p 的 Type I 证书，m<=4sqrt(n)/3+1/3<=(p-2)。
claim_status: established
topics:
- certificate
- type-I
- descent
- factorization
- proof-program
sources:
- paper: bradford2024
  locator: "Proposition 1 and Corollary 1"
  role: Type-I-certificate-reconstruction
visibility: public
last_checked: '2026-07-23'
---

# 来自 \((3p+1)/4\) 的完整二分母递降分类与平方根级 Type I 证书

## 定理

令 \(p\equiv1\pmod{24}\) 为素数，并令

\[
n=\frac{3p+1}{4}.
\]

定义目标依赖的标记解集

\[
W_p=\left\{(n,b,c)\in\operatorname{Sol}(n)\right\}.
\]

则映射

\[
\Phi_p:W_p\longrightarrow\operatorname{Sol}(p),
\qquad (n,b,c)\longmapsto(np,b,c) \tag{1}
\]

在全体 \(W_p\) 上有定义，且

\[
W_p\ne\varnothing
\quad\Longleftrightarrow\quad
\text{\(n\) 有一个素因子 }q\equiv2\pmod3. \tag{2}
\]

若 (2) 的右侧成立，取其中最小的 \(q\)。定义

\[
r=\frac{n/q+1}{3},\qquad
m=\frac{4q+1}{3},\qquad
x=qr,\qquad d=qr^2. \tag{3}
\]

则 \(m,d\) 是 \(p\) 的 Type I 除子证书；特别地

\[
m\le\frac{4\sqrt n+1}{3}
 =\frac{2\sqrt{3p+1}+1}{3}
 \le p-2. \tag{4}
\]

它同时给出一个严格递降：\(n<p\)，且

\[
\frac4n=\frac1n+\frac1{qr}+\frac1{nr}
\quad\Longrightarrow\quad
\frac4p=\frac1{np}+\frac1{qr}+\frac1{nr}. \tag{5}
\]

所以这一显式源解属于 \(W_p\)。它不是偶然的单点恒等式：式 (1) 对 \(W_p\) 的
每一个元素都成立。

更强地，若某个 \((a,b,c)\in\operatorname{Sol}(n)\) 通过只替换 \(a\)、保留
\(b,c\) 提升到 \(\operatorname{Sol}(p)\)，则必有 \(a=n\)。因此所有从这个源分母
出发的二分母保留提升恰为 (1) 所描述的标记分支。

这一分母并非任意选择。设一般地 \(2\le N<p\)，且某个 \((N,b,c)\in
\operatorname{Sol}(N)\) 能通过只替换 \(N\) 保留 \(b,c\) 而提升到
\(\operatorname{Sol}(p)\)。则对核心素数，必有

\[
N=\frac{3p+1}{4},
\]

且替换后的分母是 \(Np\)。换言之，(1) 是“替换源分母自身”这一自然二分母模板的
唯一严格递降候选。

## 证明

先证 (1)。任取 \((n,b,c)\in W_p\)，则

\[
\frac1b+\frac1c=\frac3n.
\]

因 \(4n=3p+1\)，故

\[
\frac1{np}+\frac1b+\frac1c
=\frac1{np}+\frac3n
=\frac{3p+1}{np}=\frac4p.
\]

所以 \(\Phi_p\) 是全域提升，且 \(n<p\)。

## 替换源分母的唯一性

设 \(2\le N<p\)，并有

\[
\frac4N=\frac1N+\frac1b+\frac1c,
\qquad
\frac4p=\frac1{A}+\frac1b+\frac1c.
\]

消去 \(b,c\) 后，令 \(r=4N-3p\)，便有

\[
\frac1A=\frac{r}{Np}.
\]

正性要求 \(r>0\)，而 \(N<p\) 给出 \(r<p\)。积分性要求 \(r\mid Np\)；
又 \(0<r<p\) 和 \(p\) 为素数给出 \(\gcd(r,p)=1\)，所以 \(r\mid N\)。
从 \(r=4N-3p\) 再得 \(r\mid3p\)，故 \(r\mid3\)。于是 \(r=1\) 或 \(r=3\)。
后者会给出 \(N=3(p+1)/4\)，但 \(p\equiv1\pmod4\) 时它不是整数；所以 \(r=1\)，
即 \(N=(3p+1)/4\) 且 \(A=Np\)。

## 二分母保留的完备性

设 \((a,b,c)\in\operatorname{Sol}(n)\)，并设存在正整数 \(a'\) 使

\[
\frac4p=\frac1{a'}+\frac1b+\frac1c.
\]

消去保留的两项后，\(a'\) 被强制为

\[
a'=\frac{npa}{D},
\qquad
D=np-4(p-n)a>0,
\qquad D\mid npa. \tag{6}
\]

由 \(p=(4n-1)/3\)、\(p-n=(n-1)/3\)，正性给出

\[
a<\frac{n(4n-1)}{4(n-1)}
=n+\frac{3n}{4(n-1)}<n+1.
\]

故 \(a\le n\)。若 \(a<n\)，写 \(s=n-a\ge1\)。则

\[
D=n+\frac{4(n-1)s}{3}. \tag{7}
\]

又 \(D\equiv4na\pmod p\)，而 \(a,n<p\)，故 \(p\nmid D\)。由 (6) 可得
\(D\mid na\)。令 \(g=\gcd(D,n)\)。因为 \(n=18t+1\) 为奇数，且

\[
\gcd\left(\frac{4(n-1)}3,n\right)=1,
\]

式 (7) 给出 \(g=\gcd(s,n)\le s\)。但 \(D\mid na\) 意味着 \(D/g\mid a\)，
而

\[
\frac Dg\ge\frac Ds
=\frac ns+\frac{4(n-1)}3
>n-1\ge a,
\]

矛盾。故 \(a=n\)。此时 (6) 中 \(D=n\)、\(a'=np\)，恰恢复 (1)。

## 标记集与证书

现在证 (2)。集合 \(W_p\) 非空当且仅当 \(3/n\) 能写成两个单位分数。对任意正整数
\(b,c\)，这等价于

\[
(3b-n)(3c-n)=n^2. \tag{8}
\]

若 (8) 有解，因 \(n\equiv1\pmod3\)，其左侧的每个因子均为 \(2\pmod3\)。
又 \(1/b<3/n\)，故 \(e=3b-n>0\)。取 \(e\mid n^2\)，则
\(e\equiv2\pmod3\)，所以 \(n\) 必有一个
\(2\pmod3\) 素因子。反过来，若 \(q\mid n\)、\(q\equiv2\pmod3\)，则

\[
b=\frac{n+q}{3},\qquad c=\frac{n+n^2/q}{3}
\]

都是正整数，并满足 (8)，故属于 \(W_p\)。

现在取最小的 \(q\)。因为 \(n\equiv1\pmod3\)，\(n\) 的所有
\(2\pmod3\) 素因子的指数和为偶数；最小的此类素因子 \(q\) 必有另一个（可为同一
素数的第二次出现）不小于它，故 \(q^2\le n\)。又

\[
\frac nq\equiv2\pmod3,
\]

所以 \(r\) 是正整数，并有 \(n+q=3qr\)。于是

\[
\frac1{qr}+\frac1{nr}
=\frac{n+q}{nqr}=\frac3n,
\]

给出 (5) 左式。再利用 \(4n=3p+1\)，得到

\[
\frac1{np}+\frac3n
=\frac{3p+1}{np}=\frac4p,
\]

从而 (5) 的显式提升恒等式成立。

再证证书。由 \(x=qr\)，有 \(d=qr^2=x^2/q\mid x^2\)。并且

\[
p+r=m\frac nq, \tag{9}
\]

因为将两边乘以 \(3q\) 后，(9) 化为

\[
3pq+n+q=(4q+1)n,
\]

这正是 \(q(3p+1)=4qn\)。故以 Type I 正规形

\[
x=r\cdot1\cdot q,\qquad d=r^2q,
\]

其整除条件 \(m\mid p+r\) 由 (9) 成立。直接地也可写成

\[
\frac{px+d}{m}=nr,\qquad
\frac{p(x+px^2/d)}m=np,
\]

正好是 (5) 的两个未改分母和新分母。于是 \((m,d)\) 是 Type I 证书。

最后，直接由 \(n+q=3qr\) 和 \(4n=3p+1\) 计算

\[
3(4x-p)=4(n+q)-3p=4q+1=3m,
\]

故该证书的缺口确为 (3) 中的 \(m\)。\(q^2\le n\) 给出 (4) 的第一个不等式。对
\(p\ge5\)，

\[
2\sqrt{3p+1}\le3p-7
\]

等价于 \(9(p-1)(p-5)\ge0\)，故 (4) 的第二个不等式成立。又
\(m=4x-p\equiv3\pmod4\)，所以它确在自然缺口范围内。

## 边界

该构造失败当且仅当 \((3p+1)/4\) 的所有素因子都为 \(1\pmod3\)。它是一个新的
平方根级直接分支，也是一个带显式源叶子的严格递降分支；但尚未证明这些失败素数为空，
故不能单独完成“短证书或递降”引理。
