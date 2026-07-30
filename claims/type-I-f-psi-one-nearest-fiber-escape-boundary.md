---
kind: claim
claim_id: type-I-f-psi-one-nearest-fiber-escape-boundary
title: 内禀缺陷一的最近目标纤维与一层逃逸边界
statement: 若目标纤维到原指数盒的内禀 L1 距离 Psi_0 等于 1，令 D 为全部最短见证可能溢出的坐标集，则 D 必包含于每一组投影盒阻碍 J；反向包含一般不成立。对冻结平方终端链中的 55 个 Psi_0=1 状态，完整一层壳共有 140 条正向最短见证及其 140 条符号反射，D 的大小为 1 至 5；55 个最小投影阻碍都唯一，但只有 11 个满足 D=J。D 与规范双活跃 Fourier 支撑相交 49/55，另 6 个完全不相交，故最近纤维不能普遍压到活跃方向。把最短见证直接剪去一层后，既有广义 2^j 偶终端判据在全部 280 条带符号见证上零命中；从缺陷素数 q=8h-1 提取 Type II K=2 相邻桥候选也在 6 个合法候选上零命中。进一步把每条见证定向为唯一负缺陷并完整参数化固定 B 的精确 gcd 约分端点，在必要大小界内共得 881472 个互素端点，任意 Type II 命中仍为零。这些零命中都只是冻结样本中指定映射的负边界，不排除其它二进终端、Type I/II 证书或支撑逃逸规则。一层见证还具有显式外部分母迁移恒等式，它严格降低形式对的良基势，但 K 不能吸收的剩余因子尚未被实现为合法 F/G 状态、解提升或原猜想的递降。
claim_status: computationally_reproduced
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-I-f-intrinsic-joint-denominator-defect-profile
  - type-I-f-square-terminal-relation-certificate
  - type-I-f-current-block-saturation-and-signed-denominator-defect
  - type-I-f-qadic-numerator-lift-rigidity-and-gcd-reduction
  - type-I-f-bounded-fourier-radius-boundary
  - type-I-f-overflow-square-terminal-lift-boundary
  - type-I-linear-b-gt-one-full-spectrum-profile-600m
  - type-I-general-dyadic-terminal-transfer
  - type-II-k2-adjacent-type-I-cross-chart-bridge
topics:
  - type-I
  - F-state
  - target-fiber
  - nearest-fiber
  - relation-lattice
  - signed-defect
  - joint-obstruction
  - finite-fourier
  - q-adic
  - dyadic
  - support-escape
  - descent
  - proof-program
sources:
  - claim: type-I-f-intrinsic-joint-denominator-defect-profile
    role: intrinsic-distance-and-minimum-obstruction-input
  - claim: type-I-f-square-terminal-relation-certificate
    role: complete-affine-target-fiber-input
  - claim: type-I-f-qadic-numerator-lift-rigidity-and-gcd-reduction
    role: exact-fixed-denominator-gcd-reduction-endpoints
  - claim: type-I-f-bounded-fourier-radius-boundary
    role: canonical-active-Fourier-support-input
  - claim: type-I-f-overflow-square-terminal-lift-boundary
    role: square-terminal-active-block-input
  - claim: type-I-linear-b-gt-one-full-spectrum-profile-600m
    role: complete-same-prime-linear-spectrum-input
  - claim: type-I-general-dyadic-terminal-transfer
    role: exact-dyadic-budget-and-terminal-test
  - claim: type-II-k2-adjacent-type-I-cross-chart-bridge
    role: exact-adjacent-cross-chart-closure-condition
visibility: public
last_checked: '2026-07-30'
---

# 内禀缺陷一的最近目标纤维与一层逃逸边界

## 一般的一层壳结构

设

\[
K=\prod_{i=1}^r q_i^{\nu_i},
\qquad
B_\nu=\prod_{i=1}^r[-\nu_i,\nu_i],
\qquad
F=\left\{z\in\mathbb Z^r:\prod_iq_i^{z_i}\equiv-1\pmod R\right\},
\]

并假设

\[
\Psi_0(F)=\min_{z\in F}\sum_i(|z_i|-\nu_i)_+=1. \tag{1}
\]

每个最短见证恰有一个坐标 \(j\) 满足

\[
z_j=\varepsilon(\nu_j+1),\qquad \varepsilon\in\{-1,1\}, \tag{2}
\]

其余坐标都在原盒内。令 \(D\) 为全部最短见证可能使用的坐标集合。等价地，
\(j\in D\) 当且仅当下面某个有限面非空：

\[
\mathcal W_j^+
=\left\{w\in B_\nu:
w_j=\nu_j,
\ \prod_iq_i^{w_i}\equiv-q_j^{-1}\pmod R
\right\}. \tag{3}
\]

此时 \(w+e_j\in F\) 是正向最短见证。因为 \((-1)^{-1}=-1\)，纤维在
\(z\mapsto-z\) 下不变；所以 \(-w-e_j\) 是对应的负向见证，正负方向严格成对。

## 最短缺陷坐标必在每个投影阻碍中

设 \(J\subseteq\{1,\ldots,r\}\) 满足

\[
\pi_J(F)\cap\prod_{i\in J}[-\nu_i,\nu_i]=\varnothing. \tag{4}
\]

这里 \(J\) 不必是最小阻碍。取任意最短见证 \(z\)，并令 \(j\) 是它在 (2) 中唯一的
盒外坐标。若 \(j\notin J\)，那么 \(z\) 在 \(J\) 上的每个坐标都在原盒内，于是

\[
\pi_J(z)\in
\pi_J(F)\cap\prod_{i\in J}[-\nu_i,\nu_i],
\]

与 (4) 矛盾。因此

\[
\boxed{D\subseteq J\quad\text{对每一组投影盒阻碍 }J\text{ 成立}.} \tag{5}
\]

式 (5) 是全称定理，不依赖冻结样本。反向包含没有同样的逻辑来源：一个坐标可以参与
阻止盒投影命中，却从不承担任何全局最短见证的唯一溢出层。

## 55 个冻结状态的完整最短壳

从 253 个冻结平方终端状态中取 \(\Psi_0=1\) 的 55 个状态。对每个坐标 \(j\)，固定
\(z_j=\pm(\nu_j+1)\)，完整枚举其余原盒坐标并直接重算模 \(R\) 乘积。这穷尽了
(1)--(2) 的全部最短见证，而不只保留 BFS 的规范首见证。

正向壳共有 140 条见证，符号反射再给出 140 条，合计 280 条。每态带符号见证数为

\[
\begin{array}{c|rrrrrrrr}
\#\text{见证}&2&4&6&8&10&12&14&18\\ \hline
\#\text{状态}&18&17&7&5&5&1&1&1.
\end{array} \tag{6}
\]

55 个状态一共产生 120 个不同的“状态--缺陷素数”坐标。按单个正方向面中的见证数，
其分布是

\[
1:103,\qquad2:14,\qquad3:3, \tag{7}

\]

并且 \(|D|\) 的状态分布为

\[
\begin{array}{c|rrrrr}
|D|&1&2&3&4&5\\ \hline
\#\text{状态}&20&17&8&8&2.
\end{array} \tag{8}
\]

这 55 个状态在最小基数层都只有一组投影阻碍 \(J\)，其维数分布为

\[
2:9,\qquad3:4,\qquad4:16,\qquad5:12,\qquad6:12,\qquad7:2. \tag{9}

\]

逐项验证均满足定理 (5)，但只有

\[
11/55\text{ 满足 }D=J,
\qquad44/55\text{ 满足 }D\subsetneq J. \tag{10}
\]

差值 \(|J|-|D|\) 的分布为

\[
0:11,\ 1:9,\ 2:13,\ 3:10,\ 4:7,\ 5:3,\ 6:2. \tag{11}

\]

因此最小投影阻碍给出“缺陷素数必须从哪里选”的安全上界，却通常不是全部最近逃逸
坐标的精确刻画。

## Fourier 活跃方向与物理半块

每个冻结状态带有两个规范活跃素数 \(q_a,q_s\)。令
\(A_{\rm Four}=\{q_a,q_s\}\)。精确交叉统计为

\[
\begin{aligned}
D\cap A_{\rm Four}\ne\varnothing &:49/55,\\
D\cap A_{\rm Four}=\varnothing &:6/55,\\
D\subseteq A_{\rm Four} &:28/55.
\end{aligned} \tag{12}

\]

在 120 个缺陷坐标中，73 个活跃、47 个非活跃。按两个指定活跃方向是否进入 \(D\)，
55 态分为

\[
(q_a,q_s)\text{ 都进入}:24,\qquad
\text{仅 }q_a:16,\qquad
\text{仅 }q_s:9,\qquad
\text{二者都不进入}:6. \tag{13}

\]

最小的不相交反例是

\[
(p,R)=(57399241,155),
\qquad
K=3^2\cdot23\cdot79\cdot136013. \tag{14}

\]

它的唯一缺陷素数是 \(23\)，一条正向最短见证在上述因子次序下为

\[
z=(-2,2,-1,0), \tag{15}

\]

而规范活跃支撑是 \(\{79,136013\}\)。所以“\(\Psi_0=1\) 时从规范 Fourier
活跃方向选缺陷素数”已经被 (14)--(15) 否定。

再写两个奇半块

\[
G=\frac{aR+1}{2},
\qquad
H=\frac{sR+1}{2},
\qquad K=GH. \tag{16}

\]

120 个缺陷坐标中，118 个只出现在 \(G,H\) 的一个块中；两个例外都是 \(q=3\)
在两块中各有一层：

\[
(p,R)=(41708209,371),\qquad(257483209,83). \tag{17}

\]

状态层面，22 个状态的全部 \(D\) 落在同一物理半块，33 个状态的 \(D\) 横跨两块。
因此一层缺陷也不能普遍固定为单一 Fourier 颜色或单一物理块。

## 广义二进终端的直接剪枝边界

当前 55 态的 \(K\) 都是奇数，故在一般二进传输定理中 \(L=2K\) 满足
\(v_2(L)=1\)。对一条正向最短见证 \(z=w+e_j\)，把多出的一层剪掉后写

\[
\frac CD=\prod_iq_i^{w_i},
\qquad (C,D)=1,
\qquad C,D\mid K. \tag{18}

\]

若不引入其它奇支撑，只允许把 \(L\) 的唯一二因子放到 \(C,D\) 的一侧，那么定理的
全部直接嵌入只有：

\[
(a,b)=(C,D),\ j=1;
\qquad
(a,b)=(2C,D),\ j=1,2, \tag{19}

\]

以及由符号反射覆盖的交换方向；把 2 放进分母时没有正的二进预算。这等价于检查剪枝
比值是否落入 \(1,2,2^{-1}\) 的相应定向类，并同时核验严格大小条件
\(a<2^jb\)。

55 态中有 31 个满足某个抽象同余 \(2^j\equiv-1\pmod R\)，24 个不满足。但对
全部 280 条带符号最短见证逐项执行 (18)--(19) 后，合法偶终端数为零。前一个
“\(-1\) 是 2 的幂”统计显然不足以支付 (19) 的实际二进预算。

这里的零命中只排除“剪掉唯一缺陷层并原样代入现有二进传输定理”这一指定映射。它不
排除乘入其它 \(K\) 因子后的重新配对、换模数、广义 \(2^j\) 的其它输入，或完全不同的
偶终端构造。

## 缺陷素数驱动的 Type II \(K=2\) 相邻桥边界

对一个缺陷素数 \(q\equiv23\pmod {32}\)，最直接的外部候选规则是

\[
q=8h-1,
\qquad
h=\frac{q+1}{8}\equiv3\pmod4,
\qquad
L=2h-1=\frac{q-3}{4}. \tag{20}

\]

把它送入 Type II \(K=2\) 相邻桥，还必须满足独立闭合条件

\[
L\mid x,
\qquad x=\frac{p+h}{4}. \tag{21}

\]

120 个缺陷坐标中只有 6 个满足 (20)，结果如下：

| \(p\) | \(R\) | \(q\) | \(h\) | \(L\) | \(x\bmod L\) |
|---:|---:|---:|---:|---:|---:|
| 16002529 | 27 | 599 | 75 | 149 | 1 |
| 25073689 | 91 | 321367 | 40171 | 80341 | 11867 |
| 57399241 | 155 | 23 | 3 | 5 | 1 |
| 192235129 | 563 | 23 | 3 | 5 | 3 |
| 475619929 | 1427 | 251639 | 31455 | 62909 | 14836 |
| 488961169 | 107 | 1399 | 175 | 349 | 294 |

因此这 6 个候选全部在 (21) 失败。式 (20) 是本卡选取的一个自然外部规则，并不是由
一般联合阻碍定理强制输出的 \(h\)；表中零命中既不能否定相邻桥定理，也不能排除同一
状态的其它 \(h\)、Type II 或 Type I 证书。

## 一层外部分母迁移恒等式

一层壳还给出一个不依赖有限样本的外部分母迁移公式。取正向最短见证并写

\[
A=q^{\nu+1}A_0,
\qquad B\mid K,
\qquad \frac Aq\mid K,
\qquad A+B=Rm_0, \tag{22}

\]

其中 \(q\nmid B R m_0\)。令 \(t\) 是唯一满足

\[
1\le t\le q-1,
\qquad t\equiv-m_0\pmod q \tag{23}

\]

的整数，并定义

\[
\widetilde A=\frac Aq,
\qquad
\widetilde B=\frac{B+Rt}{q},
\qquad
\widetilde m=\frac{m_0+t}{q}. \tag{24}

\]

由 \(B+Rt=R(m_0+t)-A\) 可知三者都是正整数，而且

\[
\boxed{\widetilde A+\widetilde B=R\widetilde m.} \tag{25}

\]

若 \(m_0=qk+r\)、\(1\le r<q\)，则 \(t=q-r\)，所以

\[
\widetilde m=k+1=\left\lceil\frac{m_0}{q}\right\rceil. \tag{26}

\]

于是 \((\widetilde m,\widetilde A)\) 按字典序严格小于 \((m_0,A)\)：当 \(m_0>1\)
时第一坐标严格下降；当 \(m_0=1\) 时第一坐标相等而 \(\widetilde A=A/q<A\)。若再以
\(g=(\widetilde A,\widetilde B)\) 约分，因为 \(g\mid\widetilde A\mid K\) 且
\((K,R)=1\)，有 \(g\mid\widetilde m\)，约分后的互素对仍满足目标合同 (25)。

这条恒等式把唯一的 \(q\) 溢出层迁移到 \(\widetilde B\) 中。它不是现有 \(K\) 内的
清分母：令约分对为 \((\widehat A,\widehat B)\)，则

\[
Y=\frac{\widehat B}{(\widehat B,K)} \tag{27}

\]

正是 \(K\) 不能吸收的外部分母因子。一般地，\(Y\) 的素因子可能不在
\(\operatorname{supp}(K)\) 中，也可能仍在原支撑中而只是指数超额，不能一律称为
“新支撑”。这里还能无条件证明 \(Y>1\)：已有 \(\widehat A\mid K\)；若再有
\(\widehat B\mid K\)，则互素性给出 \(\widehat A\widehat B\mid K\)，从而
\(\widehat A/\widehat B\) 是原指数盒中的目标见证，与 \(\Psi_0>0\) 矛盾。

在冻结的 140 条正向见证中，原来的 \(m_0\) 全部大于 1，故 (26) 全部严格下降；
但 \(Y>1\) 也对全部 140 条成立。按 \(Y\) 的不同素因子数 \(\omega(Y)\)，分布为

\[
\omega(Y)=1:69,\qquad2:58,\qquad3:12,\qquad4:1. \tag{28}

\]

55 态中有 37 个至少存在一条 \(\omega(Y)=1\) 的外部分母迁移边，另 18 个的每条边都
含至少两个不同素因子。在 140 条见证中，133 条的 \(Y\) 支撑与
\(\operatorname{supp}(K)\) 不交，7 条同时含原支撑指数超额和支撑外素数；没有一条
只含原支撑指数超额。这个 133/7 是冻结样本统计，不是一般定理。最小的多因子反例正是
(14)：其唯一缺陷 \(q=23\) 给出约分对

\[
(\widehat A,\widehat B,\widehat m)=(23,132,1),
\qquad Y=2^2\cdot11. \tag{29}

\]

最小状态 \((p,R)=(16002529,27)\) 则有两个缺陷素数 \(599,9491\)，两条正向切换
恰好汇合到

\[
(\widehat A,\widehat B,\widehat m)
=(5685109,11,210560),
\qquad5685109=599\cdot9491. \tag{30}

\]

式 (25)--(26) 是目前最有希望纸面化的一层逃逸引理：它给出规范剩余类、显式外部分母
因子和一个严格良基量。但该势函数只定义在形式目标对上，尚不是原目标要求的合法状态
递降；而且它只比较当前选定方向的一条边，不能作为允许换向后的全边势。显式
\(m=1\) 支撑内五周期已经证明，全部未剪枝形式迁移边不存在共同严格下降势；见
[形式目标因子对转移的循环边界](type-I-formal-target-pair-descent-cycle-boundary.md)。

## 固定负缺陷的精确 gcd 约分端点与 Type II 边界

现在把每条最短见证定向为唯一缺陷在负向。于是

\[
v_q(B)=\nu+1,
\qquad
D_-(z)=\frac{B}{(B,K)}=q. \tag{31}
\]

固定这个 \(B\)，应用精确 \(q\)-进约分定理。令 \(s_0\in\{1,\ldots,q-1\}\) 是
唯一满足

\[
A+Rs_0\equiv0\pmod q \tag{32}
\]

的剩余类，并定义

\[
a_0=\frac{A+Rs_0}{q},
\qquad
b=\frac Bq,
\qquad
r_0=\frac{m_0+s_0}{q}. \tag{33}
\]

固定 \(B\) 后全部约去这一层 \(q\) 的候选恰可写为

\[
s=s_0+qt,
\qquad
a=a_0+Rt,
\qquad
r=r_0+t,
\qquad t\in\mathbb Z, \tag{34}
\]

并且

\[
a+b=Rr,
\qquad
\gcd(A+Rs,B)=q
\iff
\gcd(a,b)=1. \tag{35}
\]

所以正的精确 gcd 约分端点就是算术进程 \(a=a_0+Rt\) 中满足 \(a>0\) 与
\((a,b)=1\) 的全部项，没有隐藏的搜索变量。

若这对端点产生 Type II 正规形，则必须存在

\[
h\mid a+b,
\qquad
4ab\mid p+h,
\qquad
3\le h\le p-2,
\qquad h\equiv3\pmod4. \tag{36}
\]

必要大小界为

\[
4ab\le2p-2,
\qquad
1\le a\le\left\lfloor\frac{p-1}{2b}\right\rfloor. \tag{37}
\]

这个有限检查不需要分解 \(a+b\)。因为 \(b=B/q\) 仍含 \(q^\nu\) 且 \(\nu\ge1\)，
故 \(b\ge2\)，
从而对每个 \(a\ge1\)，

\[
M:=4ab>a+b=:S. \tag{38}
\]

任何 \(h\mid S\) 都严格小于 \(M\)，而 (36) 的同余在 \([1,M-1]\) 中只有一个候选

\[
h_0=(-p)\bmod M. \tag{39}
\]

它自动满足 \(h_0\equiv3\pmod4\)。在 (37) 下还有
\(S\le(p+1)/2<p-2\)，所以端点命中 Type II 当且仅当

\[
\boxed{h_0\mid S.} \tag{40}
\]

对 140 条负向最短见证，式 (37) 内共有 1,214,833 个仿射端点；其中 881,472 个满足
\((a,b)=1\)，覆盖 81/140 条见证和 35/55 个状态。其余 20 个状态连必要大小界内的
精确端点都没有。对全部 881,472 个端点执行唯一候选检验 (39)--(40)，结果为

\[
\boxed{0\text{ 个 Type II 命中}.} \tag{41}
\]

最小状态 \((p,R)=(16002529,27)\) 的两个负向见证分别使用 \(q=599,9491\)，但两族
都化为

\[
a=11+27t,
\qquad b=5685109,
\qquad
\left\lfloor\frac{p-1}{2b}\right\rfloor=1, \tag{42}
\]

故先被大小界排除。最小的非空端点反例是
\((p,R)=(41708209,371)\)：9 条负向见证合计产生 9,269 个精确端点，仍然零命中。
例如其中 \(q=3\) 的首个端点为

\[
(a,b,S,M,h_0)=(362,9,371,13032,7223), \tag{43}
\]

已经有 \(h_0>S\)。

式 (41) 完备排除的是：保持原 \(B\)、精确约去唯一负缺陷 \(q\)，再原样使用约分端点
生成 Type II 的分支。它不排除改变 \(B\)、使用非最短目标见证、重新选端点因子、独立
Type II 证书或换 \(R/K\) 的合法状态。

## 跨线性状态的高度提升边界

还有一个与见证无关的精确高度合同。设 \(q^\nu\Vert K_R\)，并令

\[
K_{R'}=\frac{pR'+1}{4}. \tag{44}

\]

则对奇素数 \(q\)，

\[
q^{\nu+1}\mid K_{R'}
\iff
\begin{cases}
q^\nu\mid R'-R,\\
\displaystyle
\frac{R'-R}{q^\nu}
\equiv-\frac{4K_R}{q^\nu}p^{-1}\pmod q.
\end{cases} \tag{45}

\]

这由 \(4(K_{R'}-K_R)=p(R'-R)\) 直接得到；式 (45) 在下一层只留下唯一的非零
模 \(q\) 类。

在相同 55 态所属核心素数的冻结完整线性源谱中，120 个缺陷坐标只有 23 个在另一个
线性模数上出现了 (45) 的新增高度，97 个没有。状态层面，19/55 至少有一个缺陷坐标
获得这种高度，只有 4/55 的全部缺陷坐标都获得；36/55 完全没有。最小的完全失败点
是 (30) 的 \((16002529,27)\)：完整线性谱中没有其它状态使 \(599^2\) 或 \(9491^2\)
整除新 \(K\)。

式 (45) 只认证另一个线性块中存在一层 \(q\)-进高度。它不证明该层命中原见证的
清分子剩余类，不保持目标纤维关系，也不提供解提升；因此 23/120 不能解释为合法容量
命中，97/120 也不能解释为原猜想的失败。

## 尚缺的闭合条件

当前最窄的下一步不是继续扩大 55 态扫描，而是把外部分母迁移 (24) 升级为下列析取引理：

1. 证明新增部分 \(Y\) 被一个明确的 Type II 正规形、换模数 Type I 状态或外部线性块
   吸收，并逐项满足相应整除与自然范围条件；
2. 若使用另一个状态的 \(q\)-进层，除高度 (45) 外，还要命中带符号清分子的指定剩余类，
   并证明资源的有界重复度；
3. 若称为递降，必须把形式对的严格势 (26) 提升成合法状态上的良基势，同时给出从较小
   状态解到原 \(p\) 解的显式提升映射；
4. 处理 \(Y\) 含多个不同素因子的 18 个状态，不能把有限样本中的单因子分支误写成
   全称。

只有完成这些条件之一，\(\Psi_0=1\) 才从“离盒一步”变成统一选择器中的真正出口。

## 冻结输入与量词边界

本卡的一般结论是 (5)、(25)--(26)、(31)--(40) 和 (45)。其余数字来自固定的 55 个
状态及其完整
一层壳。使用的冻结输入为：

```text
type-i-private-carrier-selection-invariant-defect-results.json
type-i-f-bounded-fourier-full-spectrum-results.json
type-i-f-overflow-square-terminal-lift-results.json
type-i-linear-b-gt-one-full-spectrum-profile-600m-results.json
```

统一复现命令与结果文件为：

```bash
python3 reproductions/type_i_f_psi_one_nearest_fiber_escape_boundary.py
```

```text
reproductions/type-i-f-psi-one-nearest-fiber-escape-boundary-results.json

script sha256:
7c24b4f5c65191bfd05c649a705ffba4a9bb6c8db74ddd952515fc5b02fe5eeb

result sha256:
a7babc394423104647090a6bdae4255ff8cc73d2bb06dae6a0e3e1aefce4b2d2
```

脚本锁定并核验四个冻结输入的 SHA-256，在约 1.1 秒内重新生成全部逐状态记录和汇总；
运行时间只打印到标准输出，不写入结果文件，因此结果哈希是确定的。

本卡没有扩大核心素数范围。280 条最短见证、二进零命中、6 个相邻桥失败、881,472 个
约分端点零 Type II 命中和线性谱 23/120 高度命中，都只是这些输入内指定规则的完备
枚举；它们不构成全称密度结论、统一半径界、Type I/II 不存在定理或 Erdős--Straus
猜想的反例。
