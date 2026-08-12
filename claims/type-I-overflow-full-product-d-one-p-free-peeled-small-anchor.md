---
kind: claim
claim_id: type-I-overflow-full-product-d-one-p-free-peeled-small-anchor
title: 完整乘积 d=1 的 p-free 失败真实剥离与小锚点重生
statement: >-
  在完整乘积 d=1 饱和行的 p-free failure 类中，写
  (p+1)/2=ga、(n+1)/2=gb、(a,b)=1、E=(p-1)b-a=p^e u。
  从 anchor (1,R-1,1) 真实剥离全部 p^e 后得到
  y=2gu、x=1+(p^e-1)y；精确有 gcd(y,K)=2g 以及
  gcd(x,K)=gcd(x,|p^e-p-1|)。继续沿 y 侧做真实容量剥离，必到达小锚
  {2g,z=R-2g}。其下一容量坐标 D=gcd(z,K)=gcd(z,2gp+1)，故
  2g<=p+1、D<=p^2+p+1，而 z>D，故 z 侧必产生新的 clean complete-excess
  bundle Q。该 Q 为 p-free 当且仅当 a>1。a>1 时其 canonical target 容量
  c=< -L^{-1}>_p，其中 L=Q/gcd(A,Q)>1；一个整除反证全称排除
  L=1 (mod p)，故 c<=p-2，严格降低高支撑容量。a=1 时 2g=p+1 且新 bundle
  仍含 p，必须继续真实 Reach。本结论把原无界 competing-excess 余项压到一个
  O(p^2) 小锚容量盒，并完全关闭 a>1 分支；唯一算术边界是 a=1 的重复 p-block。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-full-product-d-one-p-block-peeling-obstruction
  - type-I-overflow-full-product-d-one-complete-excess-capacity-map
  - type-I-universal-p-source-capacity-anchor-orbit
  - type-I-high-support-bundle-carry-capacity-terminal-dispatch
  - denominator-escape-state-contract
topics:
  - type-I
  - overflow
  - full-product
  - d-one
  - p-free-failure
  - p-primary-peeling
  - small-anchor
  - complete-excess-bundle
  - residual-capacity
  - proof-boundary
sources:
  - claim: type-I-overflow-full-product-d-one-p-block-peeling-obstruction
    role: actual-p-block-peeling-and-direct-rechart-no-go
  - claim: type-I-universal-p-source-capacity-anchor-orbit
    role: actual-capacity-peeling-and-anchor-orbit
  - claim: type-I-high-support-bundle-carry-capacity-terminal-dispatch
    role: canonical-target-capacity-gate
  - reproduction: reproductions/type_i_overflow_d_one_p_free_peeled_small_anchor.py
    role: focused-small-anchor-and-boundary-receipts
visibility: public
last_checked: '2026-08-12'
---

# 完整乘积 \(d=1\) 的 \(p\)-free 失败真实剥离与小锚点重生

## 1. 归一化与唯一剩余类

固定核心素数

\[
p\equiv1\pmod {24},
\qquad n>1,
\qquad n\equiv1\pmod4,
\tag{1}
\]

以及完整乘积 \(d=1\) 饱和行

\[
A=\frac{pn-1}{4},
\qquad
R=(p-1)n-1,
\qquad
K=A(p-1).
\tag{2}
\]

令

\[
\alpha=\frac{p+1}{2}=ga,
\qquad
v=\frac{n+1}{2}=gb,
\qquad
(a,b)=1.
\tag{3}
\]

anchor \(\{1,R-1\}\) 的 complete-excess support 倍率为

\[
E=(p-1)b-a.
\tag{4}
\]

本卡只处理倒计时末端唯一尚未消除的算术门失败

\[
p\mid E
\quad\Longleftrightarrow\quad
b\equiv-a\pmod p.
\tag{5}
\]

写

\[
e=\nu_p(E)\ge1,
\qquad
E=p^eu,
\qquad
p\nmid u.
\tag{6}
\]

因为

\[
R-1=(p-1)n-2
=2\bigl((p-1)v-\alpha\bigr)
=2gE,
\tag{7}
\]

式 (6) 的 \(p\)-进深度也正是 anchor 对侧的 \(p\)-进深度。

## 2. 真实 \(p^e\)-剥离及两侧精确容量

从 bottom anchor \(\{1,R-1\}\) 开始，每次选择含 \(p\) 的一侧并使用
\(q=p\) raw 边。第 \(j\) 步前的两坐标为

\[
y_j=\frac{R-1}{p^j},
\qquad
x_j=R-y_j,
\qquad 0\le j<e.
\tag{8}
\]

此时 \(p\mid y_j\)、\(p\nmid K\)，而 \(m=1\) 的唯一 shift 是 \(p-1\)。raw
公式给出

\[
\left(y_j,x_j,1\right)
\longmapsto
\left(\frac{y_j}{p},R-\frac{y_j}{p},1\right).
\tag{9}
\]

又 \((y_j,R)=1\)，故每一步都无额外 gcd reduction。恰做 \(e\) 步后到达

\[
\boxed{
y=\frac{R-1}{p^e}=2gu,
\qquad
x=R-y=1+(p^e-1)y.
}
\tag{10}
\]

### 定理 1（peeled node 的两侧容量）

对 (10) 全称有

\[
\boxed{(y,K)=2g},
\tag{11}
\]

以及

\[
\boxed{
(x,K)=\bigl(x,|p^e-p-1|\bigr).
}
\tag{12}
\]

**证明。** 先注意 \(\alpha\) 为奇数，且

\[
(\alpha,p-1)=1.
\tag{13}
\]

由 \((a,b)=1\) 和 (4) 得

\[
(a,E)=(a,(p-1)b)=1,
\qquad
(a,u)=1.
\tag{14}
\]

在模 \(y\) 下，(10) 给出 \(x\equiv1\)，所以

\[
4K=pR+1=p(x+y)+1\equiv p+1=2ga\pmod y.
\tag{15}
\]

由 \(y=2gu\) 和 (14)，

\[
(y,4K)=(2gu,2ga)=2g.
\tag{16}
\]

这里 \(g,u\) 都是奇数、\(y\) 的 2-adic 估值恰为 1，而 \(K\) 为偶数，故
\((y,K)=(y,4K)\)，得到 (11)。

另一方面 \(x\) 为奇数，于是

\[
(x,K)=(x,4K)=(x,py+1).
\tag{17}
\]

而

\[
(p^e-1)(py+1)-px=p^e-p-1,
\tag{18}
\]

并且由 \(x=1+(p^e-1)y\) 有

\[
(x,p^e-1)=1.
\tag{19}
\]

式 (18)--(19) 双向给出

\[
(x,py+1)=\bigl(x,|p^e-p-1|\bigr),
\tag{20}
\]

即 (12)。证毕。

式 (12) 也校正了一个容易误用的边界：只有 \(e=1\) 时才自动有 \((x,K)=1\)；
当 \(e\ge2\) 时，另一侧可以保留非平凡但被 \(p^e-p-1\) 控制的 competing
capacity。

## 3. 沿真实路径到达 \(O(p^2)\) 小锚

对 (10) 的 \(y\) 侧继续应用容量剥离定理。式 (11) 说明所有超出 \(K\) 容量的素数幂
恰可沿实际 raw 边剥离到

\[
\boxed{
h=2g,
\qquad
z=R-2g.
}
\tag{21}
\]

这不是把 \(y\) 静态替换成 gcd，而是一条从原 anchor 延伸出来、顺序无关的有限 raw
路径。还可直接验证

\[
p\equiv n\equiv-1\pmod {2g},
\qquad
R=(p-1)n-1\equiv1\pmod {2g},
\tag{22}
\]

所以

\[
(2g,z)=1,
\qquad
2g\mid K.
\tag{23}
\]

令下一容量坐标为

\[
D=(z,K).
\tag{24}
\]

由于 \(z\) 为奇数，使用

\[
4K=pR+1=pz+(2gp+1)
\tag{25}
\]

得到精确式

\[
\boxed{
D=(z,2gp+1),
\qquad
D\mid2gp+1.
}
\tag{26}

又 \(g\le(p+1)/2\)，故

\[
\boxed{
2g\le p+1,
\qquad
D\le p^2+p+1.
}
\tag{27}

因此原来随 \(n\) 无界的 peeled competing-excess node，沿一条明确真实路径被压进
只依赖 \(p\) 的小锚容量盒。式 (23) 还给出 \((2g,D)=1\)，所以

\[
2gD\mid K.
\tag{28}

## 4. 小锚上必有新的 clean bundle

式 (5) 等价于 \(n\equiv-2\pmod p\)。写 \(n=kp-2\)，再用
\(n\equiv p\equiv1\pmod4\) 得 \(k\equiv3\pmod4\)，所以

\[
n\ge3p-2.
\tag{29}
\]

因此

\[
z=R-2g
\ge(p-1)(3p-2)-1-(p+1)
=3p^2-6p.
\tag{30}
\]

对核心域 \(p\ge73\)，式 (27)、(30) 给出

\[
z>p^2+p+1\ge D.
\tag{31}
\]

所以 \(z\nmid K\)，小锚在这里不可能直接 terminal。定义该侧新的完整超额块

\[
Q=\prod_{\nu_q(z)>\nu_q(K)}q^{\nu_q(z)},
\qquad
\beta=\frac zQ.
\tag{32}
\]

逐素数立即得到

\[
Q>1,
\qquad
\beta\mid D,
\qquad
(Q,\beta)=1,
\qquad
2g\beta\mid K.
\tag{33}
\]

所以 (21)、(32)--(33) 是新的 clean、path-anchored complete-excess receipt；这正是
直接删除原 bundle 中 \(p^e\) 所缺失的来源条件。

现在判定它何时 \(p\)-free。由 (5)，

\[
z=R-2g
\equiv-2g(b+1)
\equiv2g(a-1)\pmod p.
\tag{34}
\]

因为 \(p\nmid2g\) 且 \(1\le a<p\)，有

\[
\boxed{
p\mid z
\quad\Longleftrightarrow\quad
a=1.
}
\tag{35}

又 \(p\nmid K\)，所以 \(p\mid z\) 当且仅当 \(p\) 的完整幂进入 (32) 的 \(Q\)。
因此

\[
\boxed{
p\nmid Q
\quad\Longleftrightarrow\quad
a>1.
}
\tag{36}

## 5. \(a>1\) 的无条件严格容量出口

设 \(a>1\)，并令

\[
M=\operatorname{lcm}(A,Q)=AL,
\qquad
L=\frac{Q}{(A,Q)}.
\tag{37}
\]

对每个 \(q\mid Q\)，有 \(\nu_q(Q)=\nu_q(z)>\nu_q(K)\ge\nu_q(A)\)，故

\[
L>1.
\tag{38}
\]

若需要从小锚数据直接重算 \(L\)，式 (24)、(32) 还给出

\[
\boxed{
L=\frac zD
\prod_{q\mid Q}q^{\nu_q(p-1)}.
}
\tag{39}
\]

由 (36)，\(p\nmid M\)，所以 canonical target 存在。写其 residual capacity 为

\[
c=\frac{K_M}{M}\in\{1,\ldots,p-1\}.
\tag{40}
\]

由 \(4A\equiv-1\pmod p\) 得

\[
\boxed{
c=\langle-L^{-1}\rangle_p.
}
\tag{41}

于是

\[
\boxed{
c=p-1
\quad\Longleftrightarrow\quad
L\equiv1\pmod p;
}
\tag{42}

下面证明式 (42) 的右侧在 \(a>1\) 时不可能发生。为简化记号，令

\[
H=2g,
\qquad
p+1=aH.
\tag{43}
\]

因 \(a\) 是奇数且 \(a>1\)，实际上 \(a\ge3\)。令

\[
w=\frac zD,
\qquad
J=\prod_{q\mid w}q^{\nu_q(p-1)}.
\tag{44}
\]

为写清逐素数比较，固定素数 \(q\)，记

\[
s=\nu_q(z),
\qquad
u_q=\nu_q(A),
\qquad
r_q=\nu_q(p-1).
\tag{45}
\]

由 \(K=A(p-1)\)，有 \(q\mid w\) 当且仅当 \(s>u_q+r_q\)。在这种情况下

\[
\nu_q(w)=s-u_q-r_q,
\qquad
\nu_q(L)=s-u_q,
\tag{46}
\]

其中第二式来自 \(q\) 的完整 \(z\)-幂进入 \(Q\)。若 \(q\nmid w\)，则
\(s\le u_q+r_q=\nu_q(K)\)，故 \(q\) 不进入 \(Q\)，也不进入 \(L\)。因此 (39)
逐素数精确等价于

\[
L=wJ,
\qquad
J\mid D.
\tag{47}
\]

后一整除关系来自 \(q\mid w\) 时 \(\nu_q(D)=u_q+r_q\ge r_q=\nu_q(J)\)。写
\(d=D/J\)。由 (26)、(44)、(47) 得

\[
\boxed{
z=Ld,
\qquad
d\mid Hp+1,
\qquad
p\nmid d.
}
\tag{48}

反设 \(L\equiv1\pmod p\)。由 (34)、(43)、(48)，

\[
d\equiv z\equiv p+1-H\pmod p.
\tag{49}
\]

且 \(1\le p+1-H<p\)，故存在 \(k\ge0\) 使

\[
d=(k+1)p+1-H.
\tag{50}
\]

令

\[
q_0=\frac{Hp+1}{d},
\qquad
t=q_0(k+1)-H.
\tag{51}
\]

由 \(Hp+1=q_0d\) 与 (50)，

\[
pt=q_0(H-1)+1,
\tag{52}
\]

所以 \(t\ge1\)。再令 \(m=at-q_0\)，代入 \(p=aH-1\) 后，(52) 给出

\[
Hm=t-q_0+1,
\qquad
(H-1)m=1-(a-1)t<0.
\tag{53}
\]

故 \(m=-\ell\)，其中 \(\ell\ge1\)。第一条 (53) 于是给出

\[
q_0=t+1+H\ell\ge t+H+1.
\tag{54}
\]

但 (51) 同时给出

\[
t=q_0(k+1)-H\ge q_0-H\ge t+1,
\tag{55}
\]

矛盾。因此

\[
\boxed{L\not\equiv1\pmod p}.
\tag{56}

结合 (41)--(42)，有 \(1\le c\le p-2\)。又由 (29)，

\[
A=\frac{pn-1}{4}>B_p=\frac{(p-1)^2}{4}.
\tag{57}
\]

故 canonical target 在
\(\Lambda_p^\sharp=(\lfloor B_p/A\rfloor,K/A)\) 的第二坐标上无条件从 \(p-1\)
严格降到 \(c\le p-2\)。也就是说，\(a>1\) 分支已经没有 terminal 或 arithmetic
stutter 余项。

## 6. \(a=1\) 的准确边界

若 \(a=1\)，则

\[
g=\alpha=\frac{p+1}{2},
\qquad
2g=p+1.
\tag{58}

由 (35)--(36)，小锚 \(\{p+1,R-p-1\}\) 的新 complete-excess bundle 仍含
\(p\)，所以它没有 canonical Type I chart。合法后续必须继续该 bundle 的真实
\(p\)-peeling / capacity-anchor Reach。式 (26)--(27) 至少保证下一容量坐标

\[
D=(R-p-1,K)\mid p^2+p+1,
\tag{59}
\]

已落入显式 \(O(p^2)\) 盒；但本卡尚未证明该有限因子状态随后必 terminal、必重新
\(p\)-free，或必有另一个严格势付款。

因此当前精确余项是：

1. \(a=1\) 时从 (59) 开始的继续真实 Reach；
2. 将上述算术路径接入真实 persistent parent、typed target、terminal-first 和全局
   E1--E5 serializer。

这两个余项尚未闭合，故本卡不是 G/Type I global exit 的最终证明。

## 7. 聚焦回执

```bash
python3 reproductions/type_i_overflow_d_one_p_free_peeled_small_anchor.py --verify
```

回执使用四个固定 \(p=73\) 状态和一个固定 \(p=97\) 状态：两个 \(e=1\) 的
\(a>1\) 严格容量出口、一个 \(e=2\) 且 \((x,K)=5\) 的 sharp 控制、一个
\(a=1\) 后新 bundle 仍含 \(p\) 的边界，以及一个 \(J=3>1\) 的 valuation 控制。
它重放精确 raw 坐标、两侧 gcd、小锚、complete-excess 与 canonical capacity；不扫描
素数、分母、历史 selector 或完整 Reach。
