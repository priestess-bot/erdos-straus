---
kind: claim
claim_id: type-I-r47-cycle-lattice-capacity-three-phase-boundary
title: R=47 五周期的表示格容量三相与无限核心射线
statement: 固定 R=47 的真实五周期 {45,2}->{15,32}->{16,31}->{8,39}->{4,43}->{45,2}，边标号为 3,2,2,2,2。对满足 p=1(mod24) 且周期相关 K=(47p+1)/4 赋值均至多为 1 的核心素数，2、3 在 K 中必恰为一次；令 T=Supp(K) intersect {5,13,31,43}。周期奇表示格与 K 容量盒的状态精确为：T 为空时 MISS_EXTERNAL；31 in T 或 {5,13,43} subset T 时 HIT；其余六个非空掩码为 MISS_CAPACITY。每个掩码都由一条原始 CRT 素数进程无限实现，所以三种状态都在无穷多个真实核心周期上发生。该结论证明周期形状或乘积律本身不能成为全称终端，统一选择器必须读取 K 容量并为两类 miss 提供周期外分支。
claim_status: computationally_reproduced
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-I-formal-cycle-representation-lattice-capacity
  - type-I-formal-target-pair-descent-cycle-boundary
  - type-I-core-universal-cycle-realizability-and-100k-closure
  - type-I-general-b-centered-square-spectrum
topics:
  - type-I
  - formal-target-pair
  - cycle
  - representation-lattice
  - capacity-box
  - external-support
  - support-mask
  - arithmetic-progression
  - selector-boundary
sources:
  - claim: type-I-formal-cycle-representation-lattice-capacity
    role: exact-two-stage-lattice-capacity-criterion
  - claim: type-I-formal-target-pair-descent-cycle-boundary
    role: actual-R47-five-cycle
  - claim: type-I-core-universal-cycle-realizability-and-100k-closure
    role: exact-support-valuation-CRT-method
  - claim: type-I-general-b-centered-square-spectrum
    role: Type-I-certificate-reconstruction
visibility: public
last_checked: '2026-07-31'
---

# \(R=47\) 五周期的表示格容量三相与无限核心射线

## 1. 固定真实周期

固定无序节点周期

\[
\mathcal Z:
\{45,2\}\to\{15,32\}\to\{16,31\}
\to\{8,39\}\to\{4,43\}\to\{45,2\},
\tag{1}
\]

逐边选中坐标和标号为

\[
(45,32,16,8,4),
\qquad
(3,2,2,2,2).
\tag{2}
\]

周期完整坐标支撑是

\[
S_{\mathcal Z}=\{2,3,5,13,31,43\}.
\tag{3}
\]

令 \(p\equiv1\pmod{24}\) 为素数，且

\[
K=\frac{47p+1}{4}.
\tag{4}
\]

由于 \(47\equiv7\pmod8\) 且 \(47\equiv2\pmod3\)，本卡限制到

\[
v_2(K)=v_3(K)=1,
\qquad
v_q(K)\in\{0,1\}\quad(q\in\{5,13,31,43\}).
\tag{5}
\]

式 (2) 的每个标号都是 \(2\) 或 \(3\)，而相应选中坐标至少含其平方。因此 (5) 使 (1) 的每条
边都满足真实严格超高条件；其它四个周期素数只改变表示格可用容量，不改变边的存在性。

## 2. 完整单位盒中的六个周期格表示

按 (1) 的书写方向构造节点指数向量 \(z_i\)，并令

\[
\mathcal T_{\mathcal Z}
=z_0+
\left\langle z_i-z_0\ (1\le i<5),\ 2z_0\right\rangle_{\mathbb Z}
\tag{6}
\]

为周期生成的全部奇表示。对 (3) 的完整单位盒作精确 Smith 格成员枚举后，除互换分子
分母外，交点恰好对应以下六个互素比：

\[
\boxed{
\frac1{93},
\quad\frac5{559},
\quad\frac{13}{645},
\quad\frac{30}{1333},
\quad\frac{62}{1677},
\quad\frac{13}{2666}.}
\tag{7}
\]

它们的分子分母和分别是 \(47\) 的 \(2,12,14,29,37,57\) 倍。式 (7) 的支撑极小元是

\[
\boxed{
\{3,31\},
\qquad
\{5,13,43\},
\qquad
\{2,13,31,43\}.}
\tag{8}
\]

这里“极小”按支撑包含关系理解。其它三个比的支撑都包含 (8) 中至少一个集合。

## 3. 核心支撑掩码的三相分类

记四个可选周期素数在 \(K\) 中的掩码为

\[
T=\operatorname{Supp}(K)\cap\{5,13,31,43\}.
\tag{9}
\]

因为 (5) 已固定 \(\{2,3\}\) 的单位容量，(7)--(8) 立即给出容量盒命中的充要条件

\[
\boxed{
\mathcal T_{\mathcal Z}\cap\mathcal B_K\ne\varnothing
\quad\Longleftrightarrow\quad
31\in T
\quad\text{或}\quad
\{5,13,43\}\subseteq T.}
\tag{10}
\]

外部坐标方程的 Smith 分解还给出

\[
\boxed{
M_Et=-z_{0,E}\text{ 可解}
\quad\Longleftrightarrow\quad T\ne\varnothing.}
\tag{11}
\]

当 \(T=\varnothing\) 时，Smith 对角含一个 \(2\)，而变换后右端对应分量为奇数，产生
`MISS_EXTERNAL`。对四个单元素掩码分别存在整数特解；删除更多外部行只会保留可解性，
所以 (11) 覆盖全部非空掩码。

合并 (10)--(11)，十六个核心掩码精确分为

\[
\boxed{
\begin{array}{c|c|c}
\text{条件}&\text{状态}&\text{掩码数}\\ \hline
T=\varnothing&\texttt{MISS_EXTERNAL}&1\\
31\in T\text{ 或 }\{5,13,43\}\subseteq T&\texttt{HIT}&9\\
\text{其余非空 }T&\texttt{MISS_CAPACITY}&6
\end{array}}
\tag{12}
\]

`MISS_CAPACITY` 的六个掩码正是 \(31\notin T\)，且 \(T\) 是
\(\{5,13,43\}\) 的非空真子集。它们已经可以消去全部外部指数，但内部单位盒仍没有周期
奇表示。

## 4. 每个掩码都有无穷多个核心素数

式 (12) 不是只在三个偶然素数上出现。固定任意

\[
T\subseteq\{5,13,31,43\}.
\tag{13}
\]

先取

\[
p\equiv9\pmod{16},
\qquad
p\equiv1\pmod9.
\tag{14}
\]

它们分别强制 \(v_2(K)=v_3(K)=1\)，并保持 \(p\equiv1\pmod{24}\)。对 \(q\in T\)，
选择一个模 \(q^2\) 提升

\[
p\equiv\alpha_q\pmod{q^2},
\qquad
\alpha_q\equiv-47^{-1}\pmod q,
\qquad
q^2\nmid47\alpha_q+1;
\tag{15}
\]

对 \(q\notin T\) 则取

\[
p\equiv1\pmod q.
\tag{16}
\]

因 \(q\nmid48\)，(16) 保证 \(q\nmid K\)。所有模数经 CRT 合并成一个原始剩余类；
每个局部剩余都不被相应模数的素因子整除。狄利克雷定理因此给出该类中无穷多个素数，
其中充分大的素数还满足 \(p>47\)。每个这样的素数都精确实现 (5)、(9)，并承载同一个
真实周期 (1)。所以 `MISS_EXTERNAL`、`MISS_CAPACITY` 和 `HIT` 三相各自在无穷多个
核心素数上发生。这一步正是
[通用周期核心可实现性定理](type-I-core-universal-cycle-realizability-and-100k-closure.md)
在本周期及十六个精确支撑掩码上的特化。

## 5. 三个最小显式代表

三个状态可由很小的核心素数直接看到：

| \(p\) | \(K=(47p+1)/4\) | \(T\) | 周期格状态 |
|---:|---:|---:|---|
| \(313\) | \(3678=2\cdot3\cdot613\) | \(\varnothing\) | `MISS_EXTERNAL` |
| \(73\) | \(858=2\cdot3\cdot11\cdot13\) | \(\{13\}\) | `MISS_CAPACITY` |
| \(5113\) | \(60078=2\cdot3\cdot17\cdot19\cdot31\) | \(\{31\}\) | `HIT` |

对 \(p=5113\)，式 (7) 的最短见证 \(1/93\) 恢复

\[
(A,B,C,H,h)=(2,1,646,93,55)
\tag{17}
\]

以及单位分数解

\[
(x,y,z)=(1292,120156,307178814).
\tag{18}
\]

这里 \(Bp+A=5115=Hh\)，且 \(4xyz=p(xy+xz+yz)\)。前两个 miss 只否定**这个周期
生成的表示格终端**，不否定相应素数在周期外已有 Type I/II 证书。

## 6. 对统一选择器的含义

同一个节点周期、同一组边标号和同一个乘积律，可以随 \(K\) 的支撑容量落入三种不同
状态。因此以下两种简化都被严格排除：

1. 只按周期形状登记统一终端；
2. 把“外部指数可消去”直接等同于“容量盒命中”。

正确接口必须先输出 (12) 的内禀分类：`HIT` 直接恢复 Type I；`MISS_EXTERNAL` 需要新的
外部支撑或合法 support switch；`MISS_CAPACITY` 则需要周期外的 F/G Fourier、加法组合
或跨状态 \(q\)-进容量。式 (12) 本身不是 Erdős--Straus 猜想的反例，而是统一选择器必须
显式处理的无限三相压力族。

这里的六个 `MISS_CAPACITY` 后来已得到周期外的解析出口，而不是继续扩大周期格盒：
[R=47 非空周期支撑的短 Type I/II 选择器](type-I-r47-cycle-nonempty-support-short-selector.md)
证明，只要 \(T\ne\varnothing\)，就可由 \(31,5,13,43\) 中的首个可用素数触发一张
显式 Type I 或 Type II 证书，并统一满足

\[
m\le\frac{p+32}{15}<p-2.
\]

因此本相图的十五个非空掩码现已全部闭合；真正保留的局部余核只有
\(T=\varnothing\) 的 `MISS_EXTERNAL`。这项后续闭合不改变 (12) 的周期格分类：它给出的
是周期外证书，不能把 `MISS_CAPACITY` 重命名为周期格 `HIT`，也不能把周期格三相混同于
使用 \(K\) 全部素因子的环境 F/G/hit 三分。

空掩码的终端结构也已进一步明确。写 \(K=6Q\) 后，
\(Q\equiv2\pmod {47}\) 强制普通二进对 \((a,b)=(4,Q)\)，从而全族都有
\(E=48,n=p-1\) 的偶终端；但环境 F/G 点没有可承载它的同 \(R=47\) Type I 正规形。
此外，\(A,C\in\{1,2\}\) 的四条小 Type II 射线存在真实空掩码反例。详见
[R=47 空掩码的 p-1 二进终端与外部出口边界](type-I-r47-empty-support-pminusone-dyadic-boundary.md)。
所以这里剩余的对象已不是“找一个终端”，而是选择新的 \(p-1\) 正规形或合法可提升后继。

复现程序与结果为
`reproductions/type_i_cycle_lattice_capacity_certificate.py` 和
`reproductions/type-i-cycle-lattice-capacity-certificate-results.json`。结果保存四个显式实例的
两阶段 Smith 重建与 hit/miss 明细、完整单位盒的六个归一化比及预像，以及十六个掩码各自的
原始 CRT 类；其中 \(p=73\) 的容量 miss 还保存全部可达签名。Smith 坐标只承诺在固定实现下
可重放，不声称跨实现唯一。
