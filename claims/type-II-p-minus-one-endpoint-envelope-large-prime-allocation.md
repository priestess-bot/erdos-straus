---
kind: claim
claim_id: type-II-p-minus-one-endpoint-envelope-large-prime-allocation
title: p-1 因子 Type II 的端点容量包络、大素因子分配与 p=67369 完整分派
statement: >-
  在 p=4qr+1、m=4q-1 的 p-1 因子 Type II 菜单中，令
  k0=ceil((r+2)/4)、a0=4k0-r-1。每张证书都满足闭式端点界
  q<=Q_r=floor(k0(k0+1)/a0)<=(r+2)(r+6)/16，因而
  p-1<=r(r+2)(r+6)/4；这严格加强此前丢弃 a0 后的三次界。若
  U=(p-1)/4=s*ell、(s,ell)=1 且 16ell>(s+2)(s+6)，则任何命中都必须把
  ell 分配给源秩因子 r，故 q|s。对 p=67369，U=42*401 强制 q|42；其中
  q=1,2,3,6,14 由 Jacobi 角色给出 G 空纤维，q=7,21,42 由有界离散对数
  meet-in-the-middle 给出 F 空纤维。因此该素数没有任何 p-1 因子 Type II
  双尾递降，但 gap 31 的显式 Type I 证书直接终止。这是对“自适应 r 必命中”命题的
  全因子严格反例兼 terminal-first 分派，不是有限范围外推。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - short-certificate-equivalence
  - type-II-two-tail-deflation-descent
  - type-II-p-minus-one-fixed-source-rank-finite-menu-cubic-capacity
topics:
  - type-II
  - p-minus-one
  - endpoint-envelope
  - capacity-envelope
  - large-prime-allocation
  - divisor-lattice
  - Fourier-character
  - F-G-state
  - strict-counterexample
  - terminal-dispatch
sources:
  - claim: type-II-p-minus-one-fixed-source-rank-finite-menu-cubic-capacity
    role: linear-square-fixed-rank-menu
  - claim: type-II-two-tail-deflation-descent
    role: exact-two-tail-descent-contract
  - reproduction: reproductions/type_ii_p_minus_one_endpoint_envelope_large_prime_allocation.py
    role: focused-envelope-allocation-and-p67369-certificate-verifier
visibility: public
last_checked: '2026-08-11'
---

# \(p-1\) 因子 Type II 的端点容量包络、大素因子分配与 \(p=67369\) 完整分派

## 1. 端点容量定理

设

\[
p=4qr+1
\tag{1}
\]

为素数，并取

\[
m=4q-1,
\qquad
x=q(r+1).
\tag{2}
\]

这正是 \(m+1=4q\mid p-1\) 的 Type II 双尾递降切片，其源分母为
\(n=r+1\)。令

\[
k_0=k_-(r)=\left\lceil\frac{r+2}{4}\right\rceil,
\qquad
a_0=4k_0-r-1\in\{1,2,3,4\}.
\tag{3}
\]

则每张该切片的 Type II 证书都满足

\[
\boxed{
q\le
Q_r^{\rm end}
:=\left\lfloor\frac{k_0(k_0+1)}{a_0}\right\rfloor.}
\tag{4}
\]

更具体地，若 \(r=4t+j\)，则

\[
\boxed{
Q_r^{\rm end}=
\begin{cases}
\left\lfloor\dfrac{(t+1)(t+2)}3\right\rfloor,&j=0,\\[6pt]
\dfrac{(t+1)(t+2)}2,&j=1,\\[6pt]
(t+1)(t+2),&j=2,\\[6pt]
\left\lfloor\dfrac{(t+2)(t+3)}4\right\rfloor,&j=3.
\end{cases}}
\tag{5}
\]

式 (4) 是保留线性分母 \(4k-r-1\) 后的闭式包络。它严格加强只用
\(4k-r-1\ge1\) 得到的 \(q\le K_r(K_r+1)\)。

## 2. 为什么最大值只在第一个 \(k\)

固定源秩菜单已经给出

\[
k_0\le k\le K_r:=\left\lfloor\frac{2r+1}{3}\right\rfloor,
\qquad
d\mid k^2,
\qquad
q=\frac{d+k}{4k-r-1}.
\tag{6}
\]

所以

\[
q\le F_r(k):=\frac{k(k+1)}{4k-r-1}.
\tag{7}
\]

把 \(k=k_0+h\) 及 \(a_0=4k_0-r-1\) 代入，有精确差式

\[
F_r(k_0)-F_r(k_0+h)
=
\frac{
h\bigl(4k_0(k_0+1)-a_0(2k_0+h+1)\bigr)
}{a_0(a_0+4h)}.
\tag{8}
\]

对 \(k_0\ge3\)，允许窗口给出

\[
0\le h\le K_r-k_0
\le\left\lfloor\frac{5k_0-2a_0-1}{3}\right\rfloor
\le k_0^2-k_0-1.
\tag{9}
\]

又因 \(a_0\le4\)，式 (9) 蕴含

\[
\begin{aligned}
4k_0(k_0+1)-a_0(2k_0+h+1)
&\ge4\bigl(k_0^2-k_0-h-1\bigr)\\
&\ge0.
\end{aligned}
\tag{10}
\]

对 \(k_0=1,2\)，即 \(1\le r\le6\)，对应的
\((r,K_r-k_0,a_0)\) 依次为

\[
(1,0,2),(2,0,1),(3,0,4),(4,1,3),(5,1,2),(6,2,1),
\]

直接代入 (8) 的括号也都非负。故

\[
\boxed{F_r(k)\le F_r(k_0)\quad(k_0\le k\le K_r),}
\tag{11}
\]

从而 (4) 得证。式 (5) 只需把 \(r\) 的四个剩余类代回 (3)。这里没有枚举
\(p\) 或假设最小 \(k\) 本身必命中；(4) 是整个固定秩候选域的上包络。

## 3. 加强后的三次容量界

由 (5) 逐剩余类比较可得统一界

\[
\boxed{
Q_r^{\rm end}
\le\frac{(r+2)(r+6)}{16}.}
\tag{12}
\]

当 \(r\equiv2\pmod4\) 时右端恰为 \((t+1)(t+2)\)，所以这个统一常数不能在
纯端点估计中继续降低。结合 \(p-1=4qr\)，得到

\[
\boxed{
p-1\le\frac{r(r+2)(r+6)}4.}
\tag{13}
\]

若源秩 \(n=r+1\le N\)，则

\[
\boxed{
p>1+\frac{(N-1)(N+1)(N+5)}4
\Longrightarrow
\text{不存在源秩至多 }N\text{ 的这类 Type II 递降}.}
\tag{14}
\]

这把原来约为 \(16r^3/9\) 的统一上界收紧为约 \(r^3/4\)。它仍是必要容量界，
不声称达到该界的候选一定过素数门或除子整除门。

## 4. 单大素因子分配定理

令

\[
U=\frac{p-1}{4}=s\ell,
\qquad
\ell\text{ 为素数},
\qquad
(s,\ell)=1,
\tag{15}
\]

并假设

\[
\boxed{16\ell>(s+2)(s+6).}
\tag{16}
\]

若某个因子分解 \(U=qr\) 命中 \(p-1\) 因子 Type II 菜单，则必有

\[
\boxed{\ell\mid r,\qquad q\mid s.}
\tag{17}
\]

事实上，若 \(\ell\nmid r\)，由 (15) 的平方自由 \(\ell\)-坐标可知
\(r\mid s\) 且 \(\ell\mid q\)，所以 \(q\ge\ell\)。另一方面，(12) 给出

\[
q\le Q_r^{\rm end}
\le\frac{(r+2)(r+6)}{16}
\le\frac{(s+2)(s+6)}{16}
<\ell,
\]

矛盾。这个结论把一个大素数坐标从 \(q\)-侧强制搬到严格源秩 \(r\)-侧，是自适应
因子格上的确定性容量映射。

## 5. \(p=67369\) 的全因子压缩

取核心素数

\[
p=67369,
\qquad
U=\frac{p-1}{4}=16842=42\cdot401.
\tag{18}
\]

这里

\[
\frac{(42+2)(42+6)}{16}=132<401.
\]

所以 (17) 强制任何可能命中都满足

\[
\boxed{q\mid42.}
\tag{19}
\]

原来 \(U\) 的全部因子选择由此压成八个缺口。令 \(x_q=U+q\)、
\(m_q=4q-1\)，其完整分解为

\[
\begin{array}{c|c|c}
q&m_q&x_q\\ \hline
1&3&16843\\
2&7&2^2\cdot4211\\
3&11&3\cdot5\cdot1123\\
6&23&2^4\cdot3^4\cdot13\\
7&27&7\cdot29\cdot83\\
14&55&2^3\cdot7^2\cdot43\\
21&83&3\cdot7\cdot11\cdot73\\
42&167&2^2\cdot3^2\cdot7\cdot67.
\end{array}
\tag{20}
\]

对任意 \(d\mid x_q^2\)，写

\[
z_\lambda=v_\lambda(d)-v_\lambda(x_q),
\qquad
-v_\lambda(x_q)\le z_\lambda\le v_\lambda(x_q).
\tag{21}
\]

Type II 同余 \(d\equiv-x_q\pmod {m_q}\) 等价于有界 signed box 命中

\[
\prod_{\lambda\mid x_q}\lambda^{z_\lambda}\equiv-1\pmod {m_q}.
\tag{22}
\]

下面给出八个盒的完整 G/F 空证书；它们甚至在施加 \(d<x_q\) 之前就排除目标。

## 6. 五张 G 角色证书

对

\[
q\in\{1,2,3,6,14\},
\tag{23}
\]

取模 \(m_q\) 的 Jacobi 角色

\[
\chi_q(a)=\left(\frac{a}{m_q}\right).
\tag{24}
\]

由 (20) 逐项计算，每个 \(x_q\) 的素因子 \(\lambda\) 都满足

\[
\chi_q(\lambda)=1,
\qquad
\chi_q(-1)=-1.
\tag{25}
\]

因此整个 signed box (22) 都落在 \(\ker\chi_q\)，而目标 \(-1\) 位于其外。这五个
纤维是规范 G 态，不需要列举除子。

## 7. 三张 F 有界对数盒证书

余下三个模数的单位群均循环。分别取

\[
(m_q,g_q,N_q)=(27,2,18),(83,2,82),(167,5,166),
\tag{26}
\]

并用 \(\log_{g_q}\) 把 (22) 化为模 \(N_q\) 的有界线性和；目标 \(-1\) 的对数为
\(N_q/2\)。三行生成对数分别含 \(1\)、与 \(82\) 互素的组合、以及
\(165\in U(166)\)，故目标都在生成子群内，所以是 F 而不是 G；但下面的
meet-in-the-middle 集严格分离。

### 7.1 \(q=7\)

对数为

\[
(\log_2 7,\log_2 29,\log_2 83)=(16,1,1)\pmod {18}.
\]

将第一个坐标与后两个坐标分开，得到

\[
L_7=\{0,2,16\},
\qquad
R_7=\{7,8,9,10,11\},
\qquad
L_7\cap R_7=\varnothing.
\tag{27}
\]

这里 \(R_7\) 已包含目标对数 \(9\) 减去右侧所有允许和。

### 7.2 \(q=21\)

对数为

\[
(\log_2 3,\log_2 7;\log_2 11,\log_2 73)
=(72,8;24,69)\pmod {82}.
\]

两侧精确集合为

\[
\begin{aligned}
L_{21}&=\{0,2,8,10,18,64,72,74,80\},\\
R_{21}&=\{4,17,28,30,41,52,54,65,78\},
\end{aligned}
\qquad
L_{21}\cap R_{21}=\varnothing.
\tag{28}
\]

### 7.3 \(q=42\)

对数及指数半径为

\[
(\log_5 2,\log_5 3;\log_5 7,\log_5 67)
=(40,94;118,165)\pmod {166},
\]

其中左侧半径为 \((2,2)\)，右侧半径为 \((1,1)\)。精确集合为

\[
\begin{aligned}
L_{42}={}&\{0,8,14,18,22,32,40,54,58,62,64,72,80,86,94,\\
&102,104,108,112,126,134,144,148,152,158\},\\
R_{42}={}&\{34,35,36,82,83,84,130,131,132\},
\end{aligned}
\tag{29}
\]

且 \(L_{42}\cap R_{42}=\varnothing\)。故三张 F 盒也全部 miss。结合 (19)、
(23) 与 (27)--(29)，得到全因子结论

\[
\boxed{
p=67369\text{ 没有任何 }p-1\text{ 因子 Type II 双尾递降}.}
\tag{30}
\]

## 8. terminal-first 完整分派与边界

式 (30) 不是 Erdős--Straus 反例。原素数有 gap \(31\) 的 Type I 除子

\[
x=16850,
\qquad
d=3370,
\tag{31}
\]

其中 \(x^2/d=84250\)，且 \(31\mid67369x+d\)，所以这确是 Type I 除子而不只是
偶然的单位分数恒等式。它恢复

\[
\boxed{
\frac4{67369}
=
\frac1{16850}
+\frac1{36618420}
+\frac1{12334731684900}.}
\tag{32}
\]

所以这个压力点的 typed 分派是

\[
\boxed{
\texttt{P_MINUS_ONE_TYPE_II_EMPTY}
\longrightarrow
\texttt{TYPE_I_TERMINAL}.}
\tag{33}
\]

本定理完成了三件事：

1. 把固定源秩的粗三次界替换为 residue-sensitive 端点容量；
2. 给出可在 \(U\) 的因子格上强制大素因子归属的全称规则；
3. 对一个真实全因子 miss 给出五张 G 与三张 F 的完整对偶证书，并明确转交终端。

它没有证明每个 \(U\) 都满足单大素因子条件，也没有证明压缩后的 \(q\mid s\) 菜单
必命中或必有 Type I 终端。统一选择器仍需把一般的 F 有界盒空证书映到跨状态容量或
另一条良基下降，而不能把 (33) 的单点终端外推为全称析取。

后续的
[\(p-1\) 因子 Type II 的因子下闭容量域与素数幂分配](type-II-p-minus-one-divisor-downset-prime-power-allocation.md)
证明 \(Q_r^{\rm end}\) 沿 \(r\) 的整除关系单调，把这里的单大素数规则推广为唯一
最小禁止反链，并同时覆盖素数幂层和跨素数联合禁止块。

进一步的
[\(p-1\) 因子 Type II 的 Jacobi 源因子定位与碰撞容量](type-II-p-minus-one-jacobi-source-localization-collision-capacity.md)
证明这里五张 G 的共同原因恰是严格递降源 \(r+1\) 中没有负二次素因子，而三张 F
分别含真实负源集合 \(\{29,83\},\{73\},\{67\}\)。同一负源素数 \(\ell\) 跨
\(q\) 复用时还必须满足 \(q\equiv-U\pmod\ell\)，因而具有显式出现度上界；该上界
不自动升级为源关系格独立性或严格递降边。

聚焦验证：

~~~bash
python3 reproductions/type_ii_p_minus_one_endpoint_envelope_large_prime_allocation.py --verify
~~~

验证器只检查端点差式、四剩余类公式、单大素因子分配、八张 \(p=67369\) G/F
证书与 Type I 终端，不运行历史范围测试。
