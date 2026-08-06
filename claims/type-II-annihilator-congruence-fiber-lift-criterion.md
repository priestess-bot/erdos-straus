---
kind: claim
claim_id: type-II-annihilator-congruence-fiber-lift-criterion
title: Type II annihilator relay 的带来源同余纤维提升判据
statement: 对一个由全源列闭合得到的 annihilator relay 状态 J（J 可为核子群或商群），固定核心素数 p、原始模数 M=4D 和固定来源记录 (a_i,h_i)。定义所有 D'|D、低模数单位群满射到 J、统一合同 AD'=Da_i (mod h_i)、平方自由和范围合同组成的有限提升菜单。该菜单非空当且仅当 relay 状态存在保留这些来源因子的 Type II 整数纤维表示；菜单中若有两两互素子列表乘积 h=-1 (mod 4D')，则正规形公式给出 Type II 短证书；菜单为空时按群映射、CRT/来源合同、范围或 B'>A 分层输出规范 lift-obstructed 负证书。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-annihilator-two-sided-subgroup-quotient-descent
  - type-II-same-modulus-source-switch-crt-criterion
  - type-II-stabilizer-kernel-source-box-lattice-criterion
  - type-II-source-lattice-fibered-kneser-selector
  - type-II-annihilator-unit-group-target-map-snf-criterion
topics:
- type-II
- annihilator
- arithmetic-lift
- congruence-fiber
- source-switch
- CRT
- SNF
- Type-II-certificate
- obstruction
- descent-interface
sources:
  - claim: type-II-annihilator-two-sided-subgroup-quotient-descent
    role: relay-state-and-target
  - claim: type-II-same-modulus-source-switch-crt-criterion
    role: exact-source-CRT-and-normal-form
  - claim: type-II-stabilizer-kernel-source-box-lattice-criterion
    role: finite-kernel-SNF-gate
  - claim: type-II-source-lattice-fibered-kneser-selector
    role: fibered-Kneser-representation
  - claim: type-II-annihilator-unit-group-target-map-snf-criterion
    role: explicit-G1-targeted-surjection
visibility: public
last_checked: '2026-08-05'
---

# Type II annihilator relay 的带来源同余纤维提升判据

## 1. Relay 状态与带来源输入

固定一个核心素数 \(p\)、原始参数 \(D\) 和 \(M=4D\)。设一个全源列闭合的
annihilator relay 已经给出有限阿贝尔状态

\[
J,\qquad t_J\in J\setminus R_J,
\tag{1}
\]

其中 \(J\) 是前一引理中的核子群 \(K\) 或商群 \(H/K\)，
\(R_J\) 是带来源标签的规范源和集。对每个真实源块保存一个标签记录

\[
\sigma_i=(u_i,a_i,h_i),
\tag{2}
\]

其中 \(u_i\in J\) 是其状态像，\(a_i\) 是原参数标签，\(h_i\)
是保留来源索引的实际整数因子，并满足
\(h_i\mid p+4Da_i\) 与 \((h_i,4D)=1\)；重复 q 素因子已经按 shared-q ledger 合并。
这里的“保持来源”是指保留每个来源索引和因子 \(h_i\)，而不是只保留其模
\(4D'\) 的残数。

目标是判断 (1) 是否能在某个严格较小的 \(D'\mid D\) 上回译为同一来源标签的
Type II 状态。这里不把抽象群同构自动当作算术提升，而是显式枚举下列数据：

\[
\mathscr L_J(p,D)=
\left\{
(D',A,\eta):
\begin{array}{l}
D'\mid D,\quad D'<D,\quad A\mid D',\\
D'/A\text{ 平方自由},\quad 4AD'<p,\\
\eta:U(4D')\twoheadrightarrow J,\quad
\eta(-1)=t_J,\\
AD'\equiv Da_i\pmod{h_i}\quad\text{for every }i,\\
h_i\mid p+4AD'\quad\text{for every }i,\\
\eta(h_i\bmod 4D')=u_i\quad\text{for every }i,\\
\text{所有来源索引、互素性、范围和 shared-q 合同通过}
\end{array}
\right\}.
\tag{3}
\]

满射 \(\eta\) 的核是一个候选稳定子商；若 relay 状态本身要求完整单位群，
则额外要求 \(\eta\) 为同构。G1 的目标像、同态约束和满射性由
[单位群—目标带像满射 SNF 判据](type-II-annihilator-unit-group-target-map-snf-criterion.md)
逐个矩阵化；该判据给出 \(\eta\) 的存在性、核和每个 \(u_i\) 的可提升原像。
对固定来源因子还应使用该判据的联合标签菜单
\(\eta(h_i\bmod4D')=u_i\)，不能先独立选 \(\eta\) 再事后补来源像。

并且由 \(h_i\mid p+4Da_i\)、\((h_i,4D)=1\) 以及 \(D'\mid D\)，有精确等价

\[
h_i\mid p+4AD'
\quad\Longleftrightarrow\quad
AD'\equiv Da_i\pmod{h_i}.
\tag{3a}
\]

所以菜单只枚举统一的 \((D',A)\) 和全部原始因子的带来源合同；不允许对不同源块独立更换成不同的低层标签。

### 1a. 统一来源 CRT 预筛

令
\[
r_i\equiv Da_i\pmod{h_i},
\qquad
H_{\mathrm{src}}=\operatorname{lcm}(h_1,\ldots,h_m).
\tag{3b}
\]
所有低层候选都必须满足同一个整数
\[
x=AD',
\qquad
x\equiv r_i\pmod{h_i}\quad(1\le i\le m).
\tag{3c}
\]
广义中国剩余定理给出精确兼容条件
\[
\boxed{
\exists x\text{ 满足 (3c)}
\iff
r_i\equiv r_j\pmod{\gcd(h_i,h_j)}
\quad\text{对所有 }i,j.
}
\tag{3d}
\]
若 (3d) 失败，输出
\(\mathrm{G2\_SOURCE\_CRT\_INCONSISTENT}\)，其最小见证就是一对
\((i,j)\) 及不相容的两个剩余；此时不必枚举 \(D',A\) 或单位群映射。

若 (3d) 通过，所有解构成一个唯一剩余类
\[
x\equiv r_{\mathrm{src}}\pmod{H_{\mathrm{src}}}.
\tag{3e}
\]
而候选条件 \(A\mid D'\mid D\) 给出 \(1\le x=AD'\le D^2\)。因此只需枚举区间
\([1,D^2]\) 中的 \(r_{\mathrm{src}}\) 代表；对每个正整数 \(x\)，分解
\[
x=A^2c,\qquad c\text{ 平方自由},
\tag{3f}
\]
则 \(D'=Ac\) 是唯一可能的参数对。再检查 \(D'\mid D\)、\(D'<D\)、
\(4x<p\)、shared-q 和联合标签 SNF，即得到完整菜单。
特别地，
\[
H_{\mathrm{src}}>D^2
\quad\Longrightarrow\quad
\text{至多一个 }(D',A)\text{ 候选}.
\tag{3g}
\]
这一步把 G2 的来源合同冲突与 G3 的除子/范围空集严格分开，也避免对不同源块
分别重命名低层参数。

## 2. 四个提升门

把 (3) 的条件分为四个可独立回执的门：

\[
\begin{array}{ll}
\mathrm{G1}:&
\text{存在 }D',A,\eta\text{，且 }\eta:U(4D')\twoheadrightarrow J
\text{ 发送 }-1\text{ 到 }t_J;\\
\mathrm{G2}:&
\text{每个 }u_i\text{ 的固定因子 }h_i\text{ 满足统一合同 }
AD'\equiv Da_i\pmod{h_i}\text{，并通过 SNF/CRT；}\\
\mathrm{G3}:&
\text{候选 }A,D'\text{ 通过除子、平方自由、范围、互素和 shared-q 门；}\\
\mathrm{G4}:&
\text{若存在目标子列表 }h\equiv-1\pmod{4D'}\text{，则其正规形自动通过；}\\
&\text{若没有该子列表，保留 relay-only 状态，不记为 G4 失败。}
\end{array}
\tag{4}
\]

当 \(J=C_2\) 且 \(t_J\) 为非平凡元时，G1 可直接取模 \(4\) 符号映射；
此时只需继续检查联合来源标签和算术合同。

若四门同时通过，取该菜单元素的源盒和目标代表，得到

\[
\mathrm{ANNIHILATOR\_FIBER\_REALIZED}
=(D',A,\eta,\boldsymbol\sigma,t_J).
\tag{5}
\]

若某一门失败，保存其最小失败行：

\[
\begin{array}{ll}
\mathrm{G1\_GROUP\_MAP\_OBSTRUCTED}:&
\text{单位群的目标同余、阶结构或满射 SNF 不能实现 }
\eta:U(4D')\twoheadrightarrow J,\ \eta(-1)=t_J;\\
\mathrm{G2\_SOURCE\_CRT\_OBSTRUCTED}:&
\text{某个固定来源对 }(a_i,h_i)\text{ 不满足统一合同或残数映射};\\
\mathrm{G2\_SOURCE\_CRT\_INCONSISTENT}:&
\text{来源剩余 }Da_i\bmod h_i\text{ 不满足广义 CRT 兼容条件};\\
\mathrm{G3\_ADMISSIBLE\_FIBER\_EMPTY}:&
\text{除子、平方自由、范围或共同 q 合同失败};\\
\mathrm{G4\_NORMAL\_FORM\_OBSTRUCTED}:&
\text{在前置合同已声明通过时仍出现整除或 }B'>A\text{ 失败，}\\
&\text{作为前置账本不一致回执，不作为新的数学分支}.
\end{array}
\tag{6}
\]

若所有有限 \(D',A,\eta\) 均失败，按 G1--G4 的优先级输出

\[
\mathrm{ANNIHILATOR\_CONGRUENCE\_FIBER\_EMPTY}
=(J,t_J,\mathscr L_J,\text{failure\ ledger}).
\tag{7}
\]

这只是该 relay 的完整提升负证书，不声称原核心素数没有另一条 Type I/II 路径。

## 3. 提升菜单的充要性

\[
\boxed{
\mathscr L_J(p,D)\ne\varnothing
\iff
\text{annihilator relay }(J,R_J,t_J)
\text{ 存在保持来源标签的低模数 Type II 整数纤维表示}.
}
\tag{8}
\]

### 正向

若菜单元素存在，G1 给出低模数单位群（或稳定子商）到 \(J\) 的状态坐标；
G2 使每个固定源因子 \(h_i\) 落在同一核心合式 \(p+4AD'\) 上；G3 保证它们来自合法
的 Type II 参数纤维，G4 保证正规形的整除、大小和 source-switch 合同。因此
(5) 正是一个保持来源标签的低模数整数状态。

### 反向

若存在这样的低模数 Type II 整数纤维表示，取其模数 \(D'\)、参数 \(A\)、状态
映射 \(\eta\)。由于表示保留每个源索引的固定 \((a_i,h_i)\)，式 (3a) 给出每个带来源合同，再加上其余范围与状态条件就逐项满足 (3)。因此所有
合法表示都出现在 \(\mathscr L_J\) 中，不存在菜单之外的“隐式提升”。

这一步把 G1--G4 从必要检查提升为一个有限充要判据；它与先前的格级等式
\(\varphi^{-1}(K)/\ker\varphi\simeq K\) 相容，后者负责抽象状态，(8) 负责 Type II
整数正规形。

## 4. 从提升状态到短 Type II 证书

设菜单元素中存在两两互素的子列表 \(I\)，令

\[
h=\prod_{i\in I}h_i,\qquad
h\equiv-1\pmod{4D'}.
\tag{9}
\]

由 G2--G3，\(h\mid p+4AD'\)。令

\[
K_h=\frac{h+1}{4D'},\qquad
C'=\frac{D'}A,\qquad
B_h=\frac{K_hp+A}{h}.
\tag{10}
\]

则

\[
h=4AC'K_h-1,\qquad
B_h-A=\frac{K_h(p-4AD')+2A}{h}>0.
\tag{11}
\]

因此

\[
\boxed{
(\,A,C',K_h,h,B_h\,)
}
\tag{12}
\]

是一个合法 Type II 短证书。反向地，任何由该带来源菜单产生的低模数 Type II
短证书都必须满足 (9)--(11)，所以 (9) 不是启发式命中而是精确终端门。

这里的正规形并没有留下一个新的独立 G4 搜索。事实上，设选中的 \(h_i\) 两两
互素，且每个 \(h_i\mid p+4AD'\)、\((h_i,4D')=1\)。则
\[
h=\prod_{i\in I}h_i\mid p+4AD',
\qquad
\gcd(h,4D')=1.
\tag{12a}
\]
由 \(h\equiv-1\pmod{4D'}\) 得 \(K_h\in\mathbb N\)；再由
\[
4D'(K_hp+A)=(h+1)p+4AD'
=h\left(p+\frac{p+4AD'}h\right)
\tag{12b}
\]
和 \(\gcd(h,4D')=1\)，得到 \(h\mid K_hp+A\)，所以 \(B_h\in\mathbb N\)。
最后 (11) 给出 \(B_h>A\)。因此在输入合同、互素和目标剩余均已通过时，
\(\mathrm{G4\_NORMAL\_FORM\_OBSTRUCTED}\) 不会独立发生；若程序报告它，说明
前置的 \(h_i\) 整除、互素或 \(h\equiv-1\) 账本有不一致。

若 (9) 对所有子列表均失败，菜单仍可能给出一个合法的缺失 relay 状态；此时
不得把“没有直接命中”误写成
\(\mathrm{G4\_NORMAL\_FORM\_OBSTRUCTED}\)：这只是
\(\mathrm{ANNIHILATOR\_FIBER\_REALIZED}\) 之后的 relay-only 分支，或需要继续
寻找另一组子列表。

## 5. 有限反例与构造性样例

### \(p=97\) 的 CRT 空菜单

取 \(D=6\)、\(p=97\)，来源块

\[
(a_1,h_1)=(1,11),\qquad
(a_2,h_2)=(3,13).
\]

池化乘积 \(h=143\equiv-1\pmod{24}\)，但带来源合同是

\[
A\equiv1\pmod{11},\qquad A\equiv3\pmod{13},
\]

即 \(A\equiv133\pmod{143}\)。没有 \(A\mid6\) 的 admissible 代表，故
\(\mathrm{G2\_SOURCE\_CRT\_OBSTRUCTED}\) 或
\(\mathrm{G3\_ADMISSIBLE\_FIBER\_EMPTY}\) 输出；\(11\cdot13\equiv-1\pmod{24}\)
仍不是 Type II 证书。
若按统一变量 \(x=AD'\) 记录，则同一来源系统给出
\(x\equiv83\pmod{143}\)；而所有 \(A\mid D'\mid6\) 的候选满足
\(x\le36\)，所以 (3e)--(3g) 直接证明来源纤维为空。

### \(p=5113\) 的真实降模

取 \(D=6\)、\(D'=1\)、\(A=1\)，来源

\[
17\mid5113+24\cdot3,\qquad
7\mid5113+24\cdot6.
\]

原始来源合同在这里具体为
\[
1\equiv6\cdot3\pmod{17},\qquad
1\equiv6\cdot6\pmod7,
\]
所以同一个 \((D',A)=(1,1)\) 同时承载两个源因子。在 \(U(4)\) 中
\(17\equiv1\)、\(7\equiv-1\)，故
\(h=119\equiv-1\pmod4\)。式 (10) 给出

\[
K_h=30,\qquad B_h=1289>1,
\]

从而得到实际 Type II 短证书；这是 (8) 的非空菜单样例。

### 群映射障碍

若 relay 状态 \(J=C_4\)，而候选低模数单位群只有指数为 \(2\) 的
\(U(4)\simeq C_2\)，则不存在 G1 满射 \(C_2\twoheadrightarrow C_4\)；
这是一个纯 invariant-factor 负证书，不能靠增加 q 层弥补。

## 6. 与统一选择器的接线和研究边界

在全源列闭合得到的子群/商 relay 上，先运行提升菜单 (3)：

\[
\text{G1/G2/G3/G4 全通过}
\Longrightarrow
\text{保持标签的低模数 Type II 状态};
\]

\[
\text{某门失败}
\Longrightarrow
\text{精确 lift-obstructed 证书};
\qquad
\text{(9) 命中}
\Longrightarrow
\text{Type II 短证书}.
\tag{13}
\]

因此当前全局剩余不再是含糊的“抽象商能否提升”，而是一个有限菜单覆盖问题：
要么找到某个 \(D',A,\eta\) 和带来源原像，要么得到 G1--G4 的完整障碍。若菜单
为空，下一步必须把障碍接到 Type I/F/G 或另一条严格下降；不能继续把同一 relay
的 Fourier 支撑重复收费。
