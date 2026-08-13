---
kind: claim
claim_id: type-I-root-capacity-general-endpoint-divisor-gate
title: 一般根容量端点的精确 complete-excess 除数门
statement: >-
  对核心素数 p≡1 mod24 的 a=1,d=1 根接口，令 M=(p^2+p+1)/3、
  u=gcd(2r+1,M)、h=3u。真实容量端点 h 满足 h|K、gcd(h,R-h)=1。把 R-h
  作 maximal complete-excess 分解并规范化为 R-h=ED、D|K，则 D|ph+1。
  其 multiplier E 为 p-free 当且仅当 u<M；在这个 proper-root 域，规范目标
  cofactor 精确为 c=<D(h-1)^(-1)>_p。先分流 R-h|K 的 bottom Type I terminal；
  在剩余非终端 carry 中，唯一非严格同余门是
  D|ph+1 且 D≡1-h modp。p=313,r=271 给出 h=543 的真实 hard-root 严格正例；
  u=M 是必须继续 p-peel 的唯一非 p-free 根层。尚未证明核心素数上的非严格门恒空。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-full-product-d-one-a-one-root-coprime-capacity-fan-half-descent
  - type-I-overflow-full-product-d-one-complete-excess-capacity-map
  - type-I-overflow-full-product-d-one-a-one-single-endpoint-stutter-guarded-relay
topics:
  - type-I
  - overflow
  - common-root
  - capacity-endpoint
  - complete-excess-bundle
  - divisor-gate
  - hard-root
  - strict-carry
  - p-free-failure
  - proof-boundary
sources:
  - claim: type-I-overflow-full-product-d-one-a-one-root-coprime-capacity-fan-half-descent
    role: root-capacity-layer-h-equals-3u
  - claim: type-I-overflow-full-product-d-one-complete-excess-capacity-map
    role: canonical-complete-excess-target-cofactor
  - reproduction: reproductions/type_i_root_capacity_general_endpoint_divisor_gate.py
    role: hard-root-strict-saturated-and-relaxed-gate-controls
visibility: public
last_checked: '2026-08-13'
---

# 一般根容量端点的精确 complete-excess 除数门

## 1. 一般 \(h=3u\) 端点

固定核心素数 \(p\equiv1\pmod {24}\)，写

\[
g=\frac{p+1}{2},
\qquad
M=\frac{p^2+p+1}{3},
\qquad
T=p^2r-g,
\tag{1}
\]

\[
A=gT,
\qquad
K=A(p-1),
\qquad
R=2p^3r-p^2-2pr-p+1.
\tag{2}

于是 \(4K=pR+1\)。令

\[
u=(2r+1,M),
\qquad
h=3u,
\qquad
z=R-h.
\tag{3}

已有根容量公式说明，从 \(h_0=p+1\) 的真实容量路径可到达端点 \(h=3u\)。
以下不再假设 \(h^2<p\)。

### 引理 1（端点 primitive 性）

对 (1)--(3)，

\[
\boxed{h\mid K,\qquad(h,z)=1.}
\tag{4}

**证明。** 因 \((M,6)=1\)，\(u\) 为奇数且与 3 互素。模 \(u\) 使用
\(2r\equiv-1\) 得

\[
2T=2p^2r-(p+1)
\equiv-(p^2+p+1)\equiv0\pmod u.
\tag{5}

所以 \(u\mid T\)。同时 \(3\mid(p^2-1)/2\)，故 \(3u\mid K\)。

若素数 \(q\mid u\)，则 \(p^3\equiv1\pmod q\)，并且

\[
R\equiv1-p^2-p^3\equiv-p^2\not\equiv0\pmod q.
\tag{6}

而模 3 有 \(R\equiv-1\)。所以 \((h,R)=1\)，等价于 (4) 的第二式。证毕。

## 2. Maximal receipt 的精确除数门

把 \(z\) 相对于 \(K\) 的真实 maximal complete-excess 块写成

\[
Q=\prod_{\nu_q(z)>\nu_q(K)}q^{\nu_q(z)},
\qquad
\beta=\frac zQ,
\tag{7}

并作 canonical 归一化

\[
g_A=(A,Q),
\qquad
E=\frac Q{g_A},
\qquad
D=\beta g_A.
\tag{8}

由逐素数定义，\(ED=z\)、\(D\mid K\)。又由 (4) 有 \((h,D)=1\)，所以

\[
\boxed{hD\mid K.}
\tag{9}

更关键地，由

\[
pz=p(R-h)=4K-(ph+1)
\tag{10}

及 \(D\mid z,K\)，立刻得到

\[
\boxed{D\mid ph+1.}
\tag{11}

这把一般 hard endpoint 的完整逐素数 receipt 压缩成 \(ph+1\) 的一个实际除数。

### 引理 2（唯一非 \(p\)-free 根层）

\[
\boxed{p\nmid E\quad\Longleftrightarrow\quad u<M.}
\tag{12}

**证明。** 因 \(p\nmid K\)，(7)--(8) 给出 \(p\mid E\) 当且仅当 \(p\mid z\)。
而

\[
z\equiv1-h\pmod p.
\tag{13}

若 \(u=M\)，则 \(h=3M=p^2+p+1\equiv1\pmod p\)。反之，若
\(u<M\) 且 \(h\equiv1\pmod p\)，令

\[
v=\frac{p^2+p+1}{h}=\frac Mu>1.
\tag{14}

则 \(v\equiv1\pmod p\)。由于 \(h>1\)，这迫使 \(h,v\ge p+1\)，从而
\(hv\ge(p+1)^2>p^2+p+1\)，矛盾。证毕。

## 3. Proper-root 域的规范 cofactor

以下假设 \(u<M\)。此时 \(h-1,E,D\) 均模 \(p\) 可逆。canonical
complete-excess capacity map 的目标 cofactor 为

\[
c=\langle-E^{-1}\rangle_p,
\tag{15}

其中 \(\langle\cdot\rangle_p\in\{1,\ldots,p-1\}\)。由
\(ED=z\equiv1-h\pmod p\) 得

\[
\boxed{
c=\left\langle D(h-1)^{-1}\right\rangle_p.}
\tag{16}

再令

\[
e=\frac{ph+1}{D},
\tag{17}

则 \(De\equiv1\pmod p\)，所以还有等价形式

\[
\boxed{
c=\left\langle((h-1)e)^{-1}\right\rangle_p.}
\tag{18}

这里必须先执行 terminal-first：若 \(z=R-h\mid K\)，则 \(Q=E=1\)，该 endpoint
已经是 bottom Type I terminal，不应把形式值 \(c=p-1\) 登记成 stutter。以下只讨论
\(z\nmid K\)、等价地 \(Q>1\) 的非终端 carry。

在这个分支中，算术 carry 严格降到 \(c\le p-2\) 当且仅当

\[
\boxed{D\not\equiv1-h\pmod p.}
\tag{19}

唯一剩余的 stutter 同余门精确为

\[
\boxed{D\mid ph+1,\qquad D\equiv1-h\pmod p.}
\tag{20}

若写 \(D=mp+1-h\)，则 (17) 等价改写为

\[
\boxed{p(em-h)=e(h-1)+1.}
\tag{21}

式 (20) 比旧条件 \(h^2<p\) 更精确：后者足以排除 stutter，而 (20) 对所有
proper-root hard endpoint 的非终端 carry 都是必要且充分的单一同余门。“单一”指
只剩这一项同余条件，不表示满足它的除数 \(D\) 唯一。这里的 \(D\) 仍必须来自
真实 maximal receipt；任意抽象的 \(ph+1\) 除数不能自动替代它。

## 4. 一个真实 hard-root 严格正例

取

\[
p=313,
\qquad r=271,
\qquad M=32761,
\qquad u=181,
\qquad h=543.
\tag{22}

此时 \(9u^2>p\)，所以不在既有 small-endpoint 条件内。直接计算

\[
T=26549442,
\quad A=4168262394,
\quad K=1300497866928,
\tag{23}

\[
R=16619781047,
\qquad
z=R-h=8\cdot2077472563.
\tag{24}

真实 maximal receipt 为

\[
Q=2077472563,
\quad\beta=8,
\quad g_A=1,
\quad E=2077472563,
\quad D=8.
\tag{25}

确有

\[
D\mid ph+1=169960,
\qquad
c=\langle D(h-1)^{-1}\rangle_{313}=298<312.
\tag{26}

所以这是原 hard box 中的一条真实严格算术 carry；要登记为全局递归边，仍需既有
persistent lineage、typed target、terminal-first、identity lift 与 E1--E5 回执。

## 5. 饱和层与假设边界

取 \(p=73,r=900\)。此时

\[
M=u=1801,
\qquad h=p^2+p+1=5403,
\tag{27}

且 \(z=700088396\) 含因子 73。它正是 (12) 的唯一非 \(p\)-free 根层，必须先做
真实 \(p\)-peeling，不能套用 (15)--(20)。

最后，不能仅凭初等大小关系证明抽象门 (20) 在更宽域恒空。两个边界控制为

\[
p=361,\quad h=1029,\quad D_0=55,
\tag{28}

其中 \(p\equiv1\pmod {24}\) 但不是素数；以及

\[
p=67,\quad h=93,\quad D_0=779,
\tag{29}

其中 \(p\) 为素数但不是核心类。两例均满足

\[
h\mid p^2+p+1,
\qquad
D_0\mid ph+1,
\qquad
D_0\equiv1-h\pmod p.
\tag{30}

这里 \(D_0\) 只是抽象除数门解，并非对应参数的 actual maximal-receipt \(D\)。
它们说明未来排除 (20) 的证明必须实质使用核心素数条件和 receipt 来源，不能把
宽域中的抽象除数断言误当成已证。

## 6. 当前缺口

本卡没有证明 (20) 对核心素数的实际非终端 receipt 恒不发生。当前决定性的全称子问题
已经缩成：先分流 bottom Type I terminal；对每个剩余 proper-root hard 层，证明实际
\(D\) 不满足 (20)；或者在满足时从
(21) 构造直接 Type I/II 终端或一个可提升的更小实例。这比继续加深固定容量树更接近
原目标，因为它只剩一个明确的一维除数障碍。

## 7. 聚焦回执

```bash
python3 reproductions/type_i_root_capacity_general_endpoint_divisor_gate.py --verify
```

脚本只重算 (22)--(30) 的固定 hard-root、饱和层与放宽假设控制；全称结论由正文证明。
它不运行历史测试，不扫描素数、分母、selector history 或一般参数范围。
