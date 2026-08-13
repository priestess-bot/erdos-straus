---
kind: claim
claim_id: type-I-overflow-full-product-d-one-a-one-root-coprime-capacity-fan-half-descent
title: a=1 根接口的互素容量扇与 h=3 显式半降
statement: >-
  对核心素数 p≡1 mod24 的 a=1,d=1 根接口，令
  M=(p^2+p+1)/3、u=gcd(2r+1,M)。根锚 h0=p+1 的真实对侧容量精确为 3u；若
  9u^2<p，则实际容量路径到达 h=3u，并由小 endpoint 定理给 bottom Type I terminal
  或 p-free strict carry。每个精确 u 层在 r mod M 中有 phi(M/u) 个类。特别地，u=1
  在每个核心素数上给无限算术参数类；其中每个已准入 occurrence 的真实容量路径到达
  h=3。置 Q3=(R-3)/4、
  H=(3p+1)/4、w=gcd(r-3,H)，则 h=3 complete-excess receipt 的规范 multiplier、
  charged residual 与 target cofactor 精确为 E=Q3/w、D=4w、
  c=<-E^{-1}>_p=<2w>_p，且 c<=(p+1)/2<p-1。maximal block Q 一般不等于 Q3，
  但逐素数归一化后上述 E,D 公式全称成立。故 terminal-first 未先命中时，u=1 子域有
  一个只需两个 gcd 的显式约半降切换；登记递归边仍要求输入根已有 persistent lineage、
  typed target、priority 与 E1--E5 回执。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-full-product-d-one-p-free-peeled-small-anchor
  - type-I-overflow-full-product-d-one-a-one-s-zero-endpoint-boundary
  - type-I-overflow-full-product-d-one-complete-excess-capacity-map
  - type-I-universal-p-source-capacity-anchor-orbit
topics:
  - type-I
  - overflow
  - full-product
  - d-one
  - a-one
  - common-root
  - capacity-fan
  - small-endpoint
  - complete-excess-bundle
  - strict-carry
  - half-descent
  - selector-switch
  - proof-boundary
sources:
  - claim: type-I-overflow-full-product-d-one-p-free-peeled-small-anchor
    role: exact-a-one-root-capacity
  - claim: type-I-overflow-full-product-d-one-a-one-s-zero-endpoint-boundary
    role: small-endpoint-terminal-or-strict-theorem
  - claim: type-I-overflow-full-product-d-one-complete-excess-capacity-map
    role: canonical-multiplier-residual-and-target-cofactor
  - reproduction: reproductions/type_i_root_coprime_capacity_fan_half_descent.py
    role: coprime-fan-proper-and-saturated-gcd-controls
visibility: public
last_checked: '2026-08-13'
---

# \(a=1\) 根接口的互素容量扇与 \(h=3\) 显式半降

## 1. 根容量扇的精确分层

固定核心素数

\[
p\equiv1\pmod {24},
\tag{1}
\]

并在一个已经由真实 \(p\)-free return lineage 到达的 \(a=1,d=1\) 根接口中取
\(r\in\mathbb Z_{\ge1}\)，写

\[
G=\frac{p+1}{2},
\qquad T=p^2r-G,
\qquad A=GT,
\tag{2}
\]

\[
K=A(p-1),
\qquad
R=2p^3r-p^2-2pr-p+1.
\tag{3}
\]

令

\[
M=\frac{p^2+p+1}{3},
\qquad
u=(2r+1,M).
\tag{4}
\]

既有根容量公式为

\[
\boxed{(R-(p+1),K)=3u.}
\tag{5}
\]

从根锚 \(p+1\) 的对侧沿完整容量剥离，因而有一条实际 raw path 到达

\[
\boxed{h=3u.}
\tag{6}

### 定理 1（小根容量扇）

若

\[
9u^2<p,
\tag{7}
\]

则 (6) 满足 \(h^2<p\)。因此已有小 endpoint 定理给出严格析取：

\[
\boxed{
R-h\mid K\text{ 的 bottom Type I terminal}
\quad\lor\quad
R-h\text{ 的 p-free complete-excess carry 严格到 }c\le p-2.}
\tag{8}
\]

这里的 path 不是静态 gcd 替换：(5) 先由已绑定根节点读取真实对侧容量，通用 capacity
peeling 再逐个删除超容量素数幂，终点才是 (6)。

每个 \(u\mid M\) 的精确层也可计数。因为 \(M\) 为奇数，映射

\[
r\longmapsto2r+1\pmod M
\tag{9}
\]

是双射，而模 \(M\) 中恰有 \(\varphi(M/u)\) 个剩余类与 \(M\) 的 gcd 等于 \(u\)。
所以

\[
\boxed{
\#\{r\bmod M:(2r+1,M)=u\}=\varphi(M/u).}
\tag{10}
\]

特别地，\(u=1\) 对每个核心素数都给出 \(\varphi(M)\) 个类、相对周期密度
\(\varphi(M)/M\)，并有无穷多个正整数代表。因为 \(p\ge73\)，式 (7) 自动成立，
真实 path 必到达 \(h=3\)。下一节把 (8) 在这个互素层加强为一个显式、统一的约半降
公式。

## 2. \(h=3\) receipt 的两个 gcd 参数

以下固定

\[
(2r+1,M)=1.
\tag{11}
\]

置

\[
Q_3=\frac{R-3}{4},
\qquad
H=\frac{3p+1}{4},
\qquad
w=(r-3,H).
\tag{12}

因 \(p\equiv1\pmod8\)，\(Q_3,H\) 都为奇数；又 \(H\equiv1\pmod3\)，故

\[
(H,6)=1.
\tag{13}
\]

首先有两个固定支撑互素式：

\[
\boxed{(Q_3,p-1)=1,\qquad(Q_3,G)=1.}
\tag{14}
\]

对第一式，\(Q_3\equiv-1\pmod{(p-1)/4}\)，而 \(Q_3\) 为奇数；对第二式，
模 \(G\) 有 \(R\equiv1\)，所以 \(4Q_3=R-3\equiv-2\)，且 2 在奇模 \(G\) 下
可逆。

关键消元恒等式为

\[
\boxed{
4pQ_3-2(p^2-1)T=-(3p+1)=-4H.}
\tag{15}

它说明 \((T,Q_3)\mid H\)。反向地，模 \(H\) 有

\[
9T\equiv r-3,
\qquad
27Q_3\equiv4(r-3).
\tag{16}

结合 (13)，(16) 说明 \((r-3,H)\mid(T,Q_3)\)。所以

\[
\boxed{(T,Q_3)=(A,Q_3)=w.}
\tag{17}

第二个等号使用 (14) 与 \(A=GT\)。同样逐素数读取 \(K=A(p-1)\)，得到

\[
\boxed{(R-3,K)=4w.}
\tag{18}

## 3. Maximal complete-excess 后的精确 \(E,D\)

把 endpoint 对侧按 \(K\) 的真实 maximal capacity 分解为

\[
R-3=Q\beta,
\tag{19}
\]

其中

\[
Q=\prod_{\nu_q(R-3)>\nu_q(K)}q^{\nu_q(R-3)}.
\tag{20}

令

\[
g_A=(A,Q),
\qquad
E=Q/g_A,
\qquad
D=\beta g_A.
\tag{21}

必须注意：一般不能写 \(Q=Q_3\)。例如 \(p=73,r=3\) 时

\[
Q_3=582065=5\cdot11\cdot19\cdot557,
\tag{22}
\]

而 \(K\) 已容纳 5、11 的相应容量，实际

\[
Q=19\cdot557=10583,
\qquad \beta=220.
\tag{23}

正确的不变量是归一化后的 \(E,D\)。对任一奇素数 \(q\mid Q_3\)，写

\[
e_q=\nu_q(Q_3),
\qquad k_q=\nu_q(K).
\tag{24}

由 (14)，\(k_q=\nu_q(A)=\nu_q(T)\)；由 (17)，

\[
\min(e_q,k_q)=\nu_q(w).
\tag{25}

若 \(e_q>k_q\)，maximality 把完整 \(q^{e_q}\) 收入 \(Q\)，随后 \(g_A\) 去掉
\(q^{k_q}\)；若 \(e_q\le k_q\)，该完整块留在 \(\beta\)。两种情形统一给出

\[
\nu_q(E)=e_q-\min(e_q,k_q),
\qquad
\nu_q(D)=\min(e_q,k_q).
\tag{26}

二进部分 \(4\) 全部在 \(K\) 容量内并进入 \(D\)。因此

\[
\boxed{
E=\frac{Q_3}{w},
\qquad
D=4w.}
\tag{27}

这也直接重建 \(ED=R-3\)。又 \(w\mid H\)、\((H,3)=1\)，而 \(w\mid T\)，
所以

\[
3D=12w\mid K.
\tag{28}

故 (19)--(21)、(27)--(28) 是绑定于真实 \(h=3\) path occurrence 的合法单侧
complete-excess arithmetic receipt。

## 4. Canonical target 至少约半降

模 \(p\) 有

\[
Q_3\equiv-\frac12,
\qquad
E\equiv-(2w)^{-1}.
\tag{29}

因此 \(p\nmid E\)，且规范 target cofactor 为

\[
\boxed{
c=\langle-E^{-1}\rangle_p=\langle2w\rangle_p.}
\tag{30}

因为 \(H\) 为奇数，若 \(w<H\)，则 \(w\) 至多为 \(H/3\)，从而

\[
c=2w\le\frac{2H}{3}<\frac{p+1}{2}.
\tag{31}

若 \(w=H\)，则

\[
2H=\frac{3p+1}{2}\equiv\frac{p+1}{2}\pmod p,
\tag{32}

所以

\[
c=\frac{p+1}{2}.
\tag{33}

综合得到全称界

\[
\boxed{
c=\begin{cases}
2w,&w<H,\\[2mm]
(p+1)/2,&w=H,
\end{cases}
\qquad
c\le\frac{p+1}{2}<p-1.}
\tag{34}

parent 的高支撑 residual capacity 为 \(p-1\)，所以 (34) 是一个显式严格下降，而
不仅是“排除 stutter 后落在某个 \(c\le p-2\)”。

该 endpoint 自身不会先成为无出边的 bottom Type I terminal。由 (18)，

\[
(R-3,K)=4w\le4H=3p+1<R-3,
\tag{35}

其中最后一步对 \(p\ge73,r\ge1\) 直接成立。因此 \(R-3\nmid K\)。当然，完整
terminal-first 菜单中的其它 Type I/II 证书仍可更早抢占；(35) 只排除这个 bottom node
自身是 sink。

## 5. 可执行切换规则与合同边界

在一个已经 persistent、typed 且来源合法的根接口上，可采用下列确定规则：

1. 计算 \(u=(2r+1,M)\)；
2. 若 \(9u^2<p\)，沿真实容量路径到 \(h=3u\)，调用小 endpoint
   `terminal-or-strict`；
3. 若 \(u=1\)，再计算 \(w=(r-3,H)\)，直接生成
   \((h,E,D,c)=(3,Q_3/w,4w,\langle2w\rangle_p)\)；
4. 其余参数保留在 hard root box，而不是误报失败或重置来源。

第 3 步只使用两个 gcd 和精确整数除法，不需要分解 \(Q_3\) 才能给出 canonical
target。verifier 若要重查 maximality，仍应从原始 \(R-3,K\) 使用 gcd/模幂公式恢复
真实 \(Q,\beta\)，并核对 (27)，不能把 \(Q_3\) 冒充 \(Q\)。

若 terminal-first 未先命中，这条 path-anchored 单侧 action 的算术 target 与 E5 已由
(27)--(34) 支付；正式登记仍必须重放输入根的 persistent origin、完整 raw path、
maximality、typed target、priority、scope、恒等 \(\operatorname{Sol}(4,p)\) lift 与
内容寻址 E1--E5 receipt。本卡没有为一个静态根图表凭空制造 parent。

## 6. 聚焦回执

```bash
python3 reproductions/type_i_root_coprime_capacity_fan_half_descent.py --verify
```

脚本固定核对 \(p=73\) 的三个互素层控制：\(w=1\)、\(1<w<H\)、\(w=H\)，并以
\(r=3\) 明确验证 \(Q\ne Q_3\) 的 maximal-block 边界；另核对
\(p=457,r=3,u=7\) 的非平凡小容量层。它不扫描素数范围、分母范围、selector history
或历史结果。
