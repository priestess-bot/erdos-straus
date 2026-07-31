---
kind: claim
claim_id: type-I-core-universal-cycle-realizability-and-100k-closure
title: 通用一层周期的核心可实现性与十万模数闭合
statement: 设 R=7(mod8)，Z 是 U_R 的有向简单周期，S 是其全部坐标的素因子支撑。存在核心素数 p=1(mod24) 使 S 包含于 K=(pR+1)/4 的支撑，当且仅当 3 不在 S 中或 R=2(mod3)；条件成立时可进一步要求每个 q in S 在 K 中的赋值恰为 1，并由一个互素算术级数得到无穷多个这样的 p，于是 Z 的每条 q^2 边都成为真实 K 支撑超高边。结合 R<100000 的完整 U_R 扫描：唯一 direct radical miss 是不满足该兼容条件的 R=30031 五周期，所以这一范围内任意真实核心 K 支撑周期都直接产生同状态 Type I 终端，且没有 p 的大小上界。
claim_status: computationally_reproduced
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-I-core-formal-cycle-radical-cube-boundary
  - type-I-formal-cycle-radical-multiplier-bridge
  - type-I-general-b-centered-square-spectrum
topics:
  - type-I
  - formal-target-pair
  - universal-cycle
  - support-realizability
  - arithmetic-progression
  - radical-cube
  - finite-verification
  - centered-spectrum
sources:
  - paper: linnik1944
    locator: least-prime theorem in arithmetic progressions
    role: prime-existence-in-the-primitive-CRT-class
  - claim: type-I-core-formal-cycle-radical-cube-boundary
    role: universal-cycle-and-radical-terminal
  - claim: type-I-formal-cycle-radical-multiplier-bridge
    role: complete-R-less-than-100000-cycle-scan
  - claim: type-I-general-b-centered-square-spectrum
    role: centered-Type-I-reconstruction
visibility: public
last_checked: '2026-07-31'
---

# 通用一层周期的核心可实现性与十万模数闭合

## 1. 可实现性问题

固定

\[
R\equiv7\pmod8
\tag{1}
\]

以及通用一层图 \(U_R\) 的一个有向简单周期 \(\mathcal Z\)。令

\[
S=S(\mathcal Z)
\tag{2}
\]

为周期全部坐标的不同素因子集合。每个节点是互素对 \(\{x,R-x\}\)，所以

\[
(q,R)=1\quad(q\in S).
\tag{3}
\]

又因 \(R\) 为奇数，每个节点恰有一个偶坐标，故 \(2\in S\)。本卡回答：何时存在核心
素数

\[
p\equiv1\pmod{24},
\qquad p>R,
\qquad K=\frac{pR+1}{4},
\tag{4}
\]

使周期的全部坐标都由 \(K\) 支撑，并使 \(U_R\) 中的 \(q^2\) 边成为真实的
\(K\)-超高边。

## 2. 唯一局部障碍

若 \(3\in S\subseteq\operatorname{Supp}(K)\)，则由核心同余
\(p\equiv1\pmod3\) 得

\[
0\equiv4K=pR+1\equiv R+1\pmod3.
\tag{5}
\]

所以必要条件是 \(R\equiv2\pmod3\)。反之，下面的构造说明没有其它局部障碍：

\[
\boxed{
\exists p\text{ 满足 (4) 且 }S\subseteq\operatorname{Supp}(K)
\quad\Longleftrightarrow\quad
3\notin S\text{ 或 }R\equiv2\pmod3.}
\tag{6}
\]

而且只要右侧成立，便可以加强为

\[
\boxed{v_q(K)=1\qquad(q\in S)}
\tag{7}
\]

并得到无穷多个这样的核心素数 \(p\)。

## 3. CRT 与狄利克雷构造

先处理二进坐标。取

\[
p\equiv7R^{-1}\pmod{16},
\qquad p\equiv1\pmod3.
\tag{8}
\]

由 \(R\equiv7\pmod8\)，(8) 的第一个剩余类总满足 \(p\equiv1\pmod8\)，所以两式
合并后有 \(p\equiv1\pmod{24}\)。同时

\[
pR+1\equiv8\pmod{16},
\qquad
v_2(K)=v_2(pR+1)-2=1.
\tag{9}
\]

若 \(3\in S\)，由 (6) 右侧有 \(R\equiv2\pmod3\)。在三个满足
\(p\equiv1\pmod3\) 的模 9 提升中，恰有一个使 \(9\mid pR+1\)；选择另外任一个便有

\[
v_3(K)=1.
\tag{10}
\]

对每个 \(q\in S\)、\(q\ge5\)，先固定

\[
p\equiv-R^{-1}\pmod q.
\tag{11}
\]

它有 \(q\) 个模 \(q^2\) 提升，恰有一个使 \(q^2\mid pR+1\)。选择其余任一个，便有

\[
v_q(K)=v_q(pR+1)=1.
\tag{12}
\]

式 (8)、(10)--(12) 的模数除已经共享的模 3 条件外两两互素，故 CRT 给出一个剩余类

\[
p\equiv a\pmod M,
\qquad (a,M)=1,
\qquad a\equiv1\pmod{24},
\tag{13}
\]

并且该类中的每个整数都保持 (7)。由狄利克雷算术级数素数定理，(13) 中有无穷多个
素数；取其中任意 \(p>R\) 即完成 (6)--(7) 的充分性证明。

## 4. 通用周期变成真实周期

在 (7) 下，周期每个坐标的素因子都属于 \(K\) 支撑。通用边选择某个
\(q\in S\) 并满足

\[
q^2\mid C.
\tag{14}
\]

因此

\[
v_q(C)\ge2>1=v_q(K),
\tag{15}
\]

正是完整超高图的真实边条件。于是满足 (6) 右侧的每个抽象周期，都能在无穷多个核心
素数上实现为真实 \(K\) 支撑周期。反过来，任何真实核心 \(K\) 支撑周期当然满足
\(S\subseteq\operatorname{Supp}(K)\)，所以也必须通过 (6)。

这说明 (6) 不只是筛除一个偶然反例；它精确刻画了 \(U_R\) 周期何时可能成为核心周期。

## 5. (R<100000) 的核心周期闭合

完整 SCC 扫描已经覆盖

\[
7\le R<100000,
\qquad R\equiv7\pmod8
\tag{16}
\]

的全部 12500 个模数，并枚举所有仍可能 direct miss 的有向简单周期。结果只有一个
direct radical miss：

\[
R=30031,
\qquad
\mathcal Z=(31,6000,1200,240,961),
\tag{17}
\]

其坐标支撑为

\[
S=\{2,3,5,7,11,17,19,31,2621,3433\}.
\tag{18}
\]

但 \(3\in S\) 且 \(30031\equiv1\pmod3\)，所以 (6) 排除它成为任何核心
\(K\) 支撑周期。由于扫描中再无 direct miss，得到更贴近原问题的有限定理：

\[
\boxed{
R<100000\Longrightarrow
\text{每个真实核心 }m=1\text{ 的 }K\text{ 支撑周期都由 radical cube 直接终端。}}
\tag{19}
\]

若一个闭合游走不是简单周期，从中抽取有向简单子周期即可应用 (19)。radical witness
只使用子周期坐标支撑，仍包含于原 \(K\) 支撑，故同样恢复原状态 Type I。

式 (19) 没有 \(p\) 或 \(K\) 的大小上界。它把此前真实核心周期的直接闭合范围从
\(R\le9999\) 推进到 \(R<100000\)，同时保留 (17) 作为通用图命题的真实反例。

## 6. 一个显式核心实现

对 \(R=47\) 的周期

\[
\{2,45\}\to\{15,32\}\to\{16,31\}
\to\{8,39\}\to\{4,43\}\to\{2,45\},
\tag{20}
\]

坐标支撑是

\[
S=\{2,3,5,13,31,43\}.
\tag{21}
\]

上述 CRT 构造的一个剩余类及其中的素数为

\[
p\equiv869233214377\pmod{1081059267600},
\qquad
p=3031351749577.
\tag{22}
\]

此时

\[
K=35618383057530,
\qquad v_q(K)=1\quad(q\in S),
\tag{23}
\]

所以 (20) 的边标号 \((3,2,2,2,2)\) 全部满足真实超高条件。平方自由见证

\[
\frac{93}{1}\equiv-1\pmod{47}
\tag{24}
\]

给出 Type I 正规形

\[
(A,B,C,H,h)
=(2,1,382993366210,93,32595180103).
\tag{25}
\]

相应单位分数解为

\[
(x,y,z)=
(765986732420,
71236766115060,
107971847798547340144164810).
\tag{26}
\]

复现程序逐项检查 (20)--(26)、(17)--(18) 的不兼容性，并读取锁定的完整扫描结果推导
(19)。入口与结果分别是
`reproductions/type_i_core_cycle_realizability.py` 和
`reproductions/type-i-core-cycle-realizability-results.json`。

## 7. 证明边界与新的搜索域

式 (6) 是全称可实现性定理，式 (19) 是依赖完整有限扫描的计算结论。它们都没有证明
任意大 \(R\) 的核心周期必命中。正确的纯组合搜索域现在可以严格缩小为

\[
R\equiv7\pmod8,
\qquad
\mathcal Z\subset U_R\text{ 为有向简单周期},
\qquad
3\notin S(\mathcal Z)\text{ 或 }R\equiv2\pmod3.
\tag{27}
\]

若 (27) 中出现 direct radical 或三目标乘子桥的反例，它不能再仅以“不兼容核心支撑”
排除，因为第 3--4 节会把它实现到无穷多个核心素数上。但它仍不自动成为
Erdős--Straus 反例：对应素数可能在周期外已有 Type I/II 或其它终端。下一步应在 (27)
上研究周期表示格盒交、乘子桥与 terminal-first 外部出口，而不是继续扫描全部不兼容的
通用周期。
