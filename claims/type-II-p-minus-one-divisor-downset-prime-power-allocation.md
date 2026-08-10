---
kind: claim
claim_id: type-II-p-minus-one-divisor-downset-prime-power-allocation
title: p-1 因子 Type II 的端点整除单调性、因子下闭容量域与素数幂分配
statement: >-
  对端点包络 Q_r=floor(k0(k0+1)/(4k0-r-1))，若 r|R，则 Q_r<=Q_R。
  因而对 p=4U+1，所有可能命中的 p-1 因子 Type II 余因子 q 必落在
  C_U={q|U:q<=Q_(U/q)}；C_U 是因子格下闭集，其补集由唯一的最小禁止反链
  B_U 生成。若 L|U 且 L>Q_(U/L)，则任何命中都不可能满足 L|q。特别地，
  若 ell^e||U 且 ell^h>Q_(U/ell^h)，则 v_ell(q)<h、v_ell(r)>=e-h+1。
  这同时给出素数幂层分配和跨素数组合禁止块，严格加强单大素因子分配。
  p=601、1321、67369 分别给出禁止 5^2、禁止 5*11 但不禁止单个 5 或 11、
  以及禁止 401 的精确控制。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-p-minus-one-endpoint-envelope-large-prime-allocation
  - type-II-p-minus-one-fixed-source-rank-finite-menu-cubic-capacity
topics:
  - type-II
  - p-minus-one
  - endpoint-envelope
  - divisibility-monotonicity
  - divisor-downset
  - forbidden-antichain
  - prime-power-allocation
  - cross-prime-capacity
  - factor-lattice
  - selector
sources:
  - claim: type-II-p-minus-one-endpoint-envelope-large-prime-allocation
    role: endpoint-envelope-and-single-large-prime-allocation
  - claim: type-II-p-minus-one-fixed-source-rank-finite-menu-cubic-capacity
    role: exact-fixed-rank-Type-II-menu
  - reproduction: reproductions/type_ii_p_minus_one_divisor_downset_prime_power_allocation.py
    role: focused-downset-antichain-and-three-control-verifier
visibility: public
last_checked: '2026-08-11'
---

# \(p-1\) 因子 Type II 的端点整除单调性、因子下闭容量域与素数幂分配

## 1. 端点函数

对 \(r\ge1\)，令

\[
k_0(r)=\left\lceil\frac{r+2}{4}\right\rceil,
\qquad
a_0(r)=4k_0(r)-r-1,
\]

并定义

\[
\boxed{
Q(r)=Q_r^{\rm end}
=\left\lfloor\frac{k_0(r)(k_0(r)+1)}{a_0(r)}\right\rfloor.}
\tag{1}
\]

此前端点定理已经证明：若

\[
p=4qr+1,\qquad U=\frac{p-1}{4}=qr
\tag{2}
\]

的 \(p-1\) 因子 Type II 菜单命中，则

\[
\boxed{q\le Q(r).}
\tag{3}
\]

当 \(r=4t+j\) 时，

\[
Q(r)=
\begin{cases}
\left\lfloor (t+1)(t+2)/3\right\rfloor,&j=0,\\
(t+1)(t+2)/2,&j=1,\\
(t+1)(t+2),&j=2,\\
\left\lfloor (t+2)(t+3)/4\right\rfloor,&j=3.
\end{cases}
\tag{4}
\]

## 2. 新引理：端点包络沿整除关系单调

若 \(r\mid R\)，则

\[
\boxed{Q(r)\le Q(R).}
\tag{5}
\]

注意 \(Q(r)\) 对通常的整数次序并不单调，例如

\[
Q(2)=2>1=Q(3).
\]

式 (5) 只断言因子格上的整除单调性，这正是自适应分解 \(U=qr\) 所需要的
序结构。

### 2.1 倍数 \(2\) 与 \(3\)

写 \(r=4t+j\)。把 \(2r\)、\(3r\) 代入 (4)，分别得到

\[
\begin{array}{c|c|c}
j&Q(2r)&Q(3r)\\ \hline
0&
\left\lfloor(2t+1)(2t+2)/3\right\rfloor&
\left\lfloor(3t+1)(3t+2)/3\right\rfloor\\
1&
(2t+1)(2t+2)&
\left\lfloor(3t+2)(3t+3)/4\right\rfloor\\
2&
\left\lfloor(2t+2)(2t+3)/3\right\rfloor&
(3t+2)(3t+3)\\
3&
(2t+2)(2t+3)&
(3t+3)(3t+4)/2.
\end{array}
\tag{6}
\]

逐行与 (4) 比较即得

\[
Q(2r)\ge Q(r),\qquad Q(3r)\ge Q(r).
\tag{7}
\]

两个需要把有理式与整数目标直接比较的行为

\[
\frac{(2t+2)(2t+3)}3-(t+1)(t+2)
=\frac{t(t+1)}3\ge0,
\qquad
\frac{(3t+2)(3t+3)}4-\frac{(t+1)(t+2)}2
=\frac{7t^2+9t+2}{4}\ge0.
\]

两个右侧比较对象都是整数，所以取整后仍成立。其余各行由因子逐项增大或直接的
非负多项式差得到。

### 2.2 倍数至少 \(4\)

由 \(a_0(r)\le4\) 及
\(k_0(r)\ge(r+2)/4\)，一方面有

\[
Q(r)\ge
\left\lfloor\frac{(r+2)(r+6)}{64}\right\rfloor,
\tag{8}
\]

另一方面已有统一上界

\[
Q(r)\le\frac{(r+2)(r+6)}{16}.
\tag{9}
\]

若 \(c\ge4\) 且 \(r\ge3\)，则

\[
\frac{(4r+2)(4r+6)}{64}
-\frac{(r+2)(r+6)}{16}
=\frac{3r^2-9}{16}>1.
\tag{10}
\]

所以 (8)--(10) 给出

\[
Q(cr)\ge Q(r).
\tag{11}
\]

对 \(r=1\)，式 (4) 给出 \(Q(r)=1\)，而所有端点值至少为 \(1\)；对 \(r=2\)，
\(Q(2)=2\)，且 \(cr\ge8\) 时 (8) 已给出 \(Q(cr)\ge2\)。结合 (7) 与
(11)，任意整数 \(c\ge1\) 都满足 \(Q(cr)\ge Q(r)\)，从而证明 (5)。

## 3. 端点因子下闭容量域

固定核心素数

\[
p=4U+1
\tag{12}
\]

并在 \(U\) 的因子格中定义

\[
\boxed{
\mathcal C_U
=\left\{q\mid U:q\le Q(U/q)\right\}.}
\tag{13}
\]

式 (3) 说明每个 \(p-1\) 因子 Type II 命中的 \(q\) 都属于
\(\mathcal C_U\)。

更强地，\(\mathcal C_U\) 是因子下闭集。若 \(d\mid q\) 且
\(q\in\mathcal C_U\)，则

\[
\frac Uq\mid\frac Ud.
\]

由 (5)，

\[
d\le q\le Q(U/q)\le Q(U/d),
\]

所以 \(d\in\mathcal C_U\)。因此

\[
\boxed{
q\in\mathcal C_U,\ d\mid q
\Longrightarrow d\in\mathcal C_U.}
\tag{14}
\]

把 \(U=\prod_i\ell_i^{e_i}\) 的因子
\(q=\prod_i\ell_i^{\alpha_i}\) 识别为指数向量
\((\alpha_i)\in\prod_i\{0,\ldots,e_i\}\)，则 \(\mathcal C_U\) 是这个积链中的
有限序理想，也就是一个多重复形；仅当 \(U\) 平方自由时，它才是通常的抽象
单纯复形。下文统一使用“因子下闭容量域”以避免混淆。

其补集

\[
\mathcal F_U=\{q\mid U:q>Q(U/q)\}
\tag{15}
\]

相应地是整除上闭集。令

\[
\boxed{
\mathcal B_U
=\left\{
b\in\mathcal F_U:
\text{\(b\) 的每个真因子都属于 }\mathcal C_U
\right\}.}
\tag{16}
\]

则 \(\mathcal B_U\) 是唯一的最小禁止反链，并且

\[
\boxed{
q\in\mathcal C_U
\iff
\text{不存在 }b\in\mathcal B_U\text{ 使 }b\mid q.}
\tag{17}
\]

式 (17) 把原来逐个尝试 \(U=qr\) 的自适应菜单压成一个规范的单调容量对象。
它仍只是端点必要域：\(q\in\mathcal C_U\) 不保证除子门 \(d\mid k^2\) 命中。

## 4. 禁止块与素数幂分配

由 (15)，任取 \(L\mid U\)，若

\[
\boxed{L>Q(U/L),}
\tag{18}
\]

则 \(L\in\mathcal F_U\)。上闭性立即给出

\[
\boxed{
\text{任何 Type II 命中都不可能满足 }L\mid q.}
\tag{19}
\]

利用 (9)，一个无需计算四剩余类的充分条件是

\[
\boxed{
16L>
\left(\frac UL+2\right)
\left(\frac UL+6\right)
\Longrightarrow L\nmid q.}
\tag{20}
\]

现在设

\[
\ell^e\Vert U,\qquad1\le h\le e.
\]

若

\[
\ell^h>Q(U/\ell^h),
\tag{21}
\]

则由 (19)

\[
\ell^h\nmid q.
\]

因为 \(qr=U\)，得到精确赋值分配

\[
\boxed{
v_\ell(q)\le h-1,
\qquad
v_\ell(r)\ge e-h+1.}
\tag{22}
\]

对应的闭式充分条件为

\[
\boxed{
16\ell^h>
\left(\frac U{\ell^h}+2\right)
\left(\frac U{\ell^h}+6\right)
\Longrightarrow
v_\ell(r)\ge e-h+1.}
\tag{23}
\]

当 \(e=h=1\) 时，(23) 正是先前的单大素因子分配。式 (22) 还允许
\(e>1\)，并且 (19) 可取含多个不同素数的 \(L\)；后者表达的是“这些素因子不能
同时留在 \(q\) 侧”，不能由任何单坐标分配替代。

## 5. 三个精确控制

### 5.1 \(p=601\)：真正的素数幂层分配

\[
p=601,\qquad U=150=2\cdot3\cdot5^2.
\]

端点因子下闭容量域及其最小禁止反链为

\[
\mathcal C_{150}=\{1,2,3,5,6\},
\qquad
\mathcal B_{150}=\{10,15,25\}.
\tag{24}
\]

特别地，

\[
25>Q(6)=6,
\]

所以每个命中都满足 \(v_5(q)\le1\)、\(5\mid r\)。这不能由要求
\((s,5)=1\) 的旧单素数表述得到。完整 Type II 菜单实际在
\(q=2,3\) 命中，二者都通过 (24)。

### 5.2 \(p=1321\)：不可拆成单坐标的跨素数禁止块

\[
p=1321,\qquad U=330=2\cdot3\cdot5\cdot11.
\]

这里

\[
\mathcal C_{330}=\{1,2,3,5,6,10,11,15\},
\]

\[
\mathcal B_{330}=\{22,30,33,55\}.
\tag{25}
\]

单个 \(5\) 与 \(11\) 都属于 \(\mathcal C_{330}\)，但

\[
55>Q(6)=6
\]

使 \(5\cdot11\) 成为最小禁止块。因此任何命中都不能同时把 \(5,11\) 留在
\(q\) 侧；这是严格的联合容量约束。实际命中

\[
q\in\{2,6,10,15\}
\]

全部位于 (25) 的下闭容量域中。

### 5.3 \(p=67369\)：旧单大素数结果成为一元反链

\[
p=67369,\qquad U=16842=2\cdot3\cdot7\cdot401.
\]

此时

\[
\mathcal B_{16842}=\{401\},
\qquad
\mathcal C_{16842}=\{q:q\mid42\}.
\tag{26}
\]

所以先前的 \(q\mid42\) 压缩正是容量域只有一个最小禁止块的特例。随后八个
允许纤维仍需各自执行 Type II 除子门；已有五张 G 与三张 F 空证书证明它们全部
miss，并由 gap-\(31\) Type I 终端接管。

## 6. 对统一选择器的含义与边界

本定理新增的不是另一个有限样本结论，而是三个全称接口：

1. 端点函数在自适应源秩因子格上具有整除单调性；
2. 所有端点可行余因子形成规范下闭容量域，可由最小禁止反链无损编码；
3. 禁止块同时给出素数幂层分配和不可拆分的跨素数联合容量。

选择器应先计算 \(\mathcal B_U\)，再只对 \(\mathcal C_U\) 中的 \(q\) 建立
实际 \(d\mid k^2\) 菜单和 F/G 证书。禁止块是完备的端点 no-go，但不是 Type I
终端、Type II 命中或严格递降；\(\mathcal C_U\) 中全部纤维为空时，仍须转交
其它 terminal 或具备 E1--E5 的 verified edge。

聚焦验证：

~~~bash
python3 reproductions/type_ii_p_minus_one_divisor_downset_prime_power_allocation.py --verify
~~~

验证器只重建 (24)--(26)、下闭/反链合同和三个控制点的实际 Type II 命中集合，
不运行历史素数范围测试。
