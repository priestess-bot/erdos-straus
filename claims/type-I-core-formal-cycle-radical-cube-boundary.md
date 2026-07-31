---
kind: claim
claim_id: type-I-core-formal-cycle-radical-cube-boundary
title: 核心一层形式周期的奇偶约化、有限 radical 命中与反例边界
statement: 对核心素数 p≡1(mod24) 和 4K=pR+1，必有 R≡3(mod4)。若 R≡3(mod8)，则 K 为奇数，任何 A+B=R 的互素 K 支撑形式对都因一侧为偶数而不存在；所以核心的一层 K 支撑周期只可能位于 R≡7(mod8)。任一实际周期嵌入通用图 U_R：节点为 {x,R-x}，q^2 整除所选坐标时允许把它除以 q。对 7≤R≤9999 的全部 1250 个 R≡7(mod8) 模数，U_R 的 435 个有向简单周期的坐标素因子 radical cube 全部包含 -1，因而产生同状态 Type I 命中。这个完整有限结论不能推广为所有 R：R=30031 已给出 direct radical miss 五周期；该周期由更弱的 multiplier bridge 闭合且不兼容核心 K 支撑。
claim_status: computationally_reproduced
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-I-formal-target-pair-descent-cycle-boundary
  - type-I-general-b-centered-square-spectrum
  - type-I-coprime-factor-normal-form
topics:
  - type-I
  - formal-target-pair
  - support-preserving-cycle
  - radical-cube
  - centered-spectrum
  - terminal-first
  - parity-reduction
  - finite-verification
  - counterexample-boundary
sources:
  - claim: type-I-formal-target-pair-descent-cycle-boundary
    role: formal-cycle-interface
  - claim: type-I-general-b-centered-square-spectrum
    role: centered-box-terminal
visibility: public
last_checked: '2026-07-31'
---

# 核心一层形式周期的奇偶约化与 radical cube 命中边界

## 1. 核心周期只需考虑 \(R\equiv7\pmod8\)

设

\[
p\equiv1\pmod{24},
\qquad
4K=pR+1.
\tag{1}
\]

由 \(p\equiv1\pmod4\) 和 (1) 得 \(R\equiv3\pmod4\)，故只需区分
\(R\equiv3,7\pmod8\)。若 \(R\equiv3\pmod8\)，则

\[
pR+1\equiv4\pmod8,
\qquad K\equiv1\pmod2.
\tag{2}
\]

一层形式对 \(A+B=R\) 的两坐标一奇一偶。若它是 \(K\) 支撑对，则两坐标的全部
素因子都必须整除奇数 \(K\)，与偶坐标矛盾。因此：

\[
\boxed{
R\equiv3\pmod8\Longrightarrow
\text{核心 }m=1\text{ 的 }K\text{ 支撑形式图为空}.}
\tag{3}

所以核心周期问题精确约化到 \(R\equiv7\pmod8\)。这是一般定理，不依赖有限扫描。

## 2. 不依赖 \(K\) 大小的通用周期图

固定奇数 \(R\)，定义通用图 \(U_R\)。节点是

\[
\{x,R-x\},
\qquad
1\le x<R/2,
\qquad
(x,R)=1.
\tag{4}

若某一坐标 \(C\in\{x,R-x\}\) 和素数 \(q\) 满足 \(q^2\mid C\)，加入边

\[
\{C,R-C\}\longrightarrow
\{C/q,R-C/q\}.
\tag{5}

对任一实际 \(K\) 支撑边，\(q\mid K\) 且
\(v_q(C)>v_q(K)\ge1\)，所以 \(q^2\mid C\)；实际边的形式又正是 (5)。因此任意
大小 \(K\) 的实际一层形式图都是 \(U_R\) 的子图，任一实际周期都嵌入 \(U_R\)。

这个放大图消除了 \(p\) 和 \(K\) 的搜索上界：有限验证只按 \(R\) 截断。

## 3. 周期支撑的平方自由带符号立方

对 \(U_R\) 的一个有向简单周期 \(\mathcal Z\)，令 \(S(\mathcal Z)\) 为周期全部
坐标的不同素因子集合，并定义

\[
\mathcal C_S=
\left\{
\prod_{q\in S}q^{\varepsilon_q}\pmod R:
\varepsilon_q\in\{-1,0,1\}
\right\}.
\tag{6}

若 \(-1\in\mathcal C_S\)，把正、负指数分别相乘为 \(a,b\)，则

\[
(a,b)=1,
\qquad
ab\mid\operatorname{rad}\!\left(\prod_{q\in S}q\right),
\qquad
a+b\equiv0\pmod R.
\tag{7}

对任何包含该实际周期的 \(K\)，都有 \(S\subseteq\operatorname{Supp}(K)\)，故

\[
ab\mid\operatorname{rad}(K)\mid K.
\tag{8}

于是 \((a,b)\) 已落入原始 \(K\) 指数盒并命中目标 \(-1\)。按中心谱与 Type I
正规形，这给出同一 \((p,R,K)\) 的直接 Type I 终端。终端优先选择器会在进入周期前
删除所有这类边。

## 4. \(R\le9999\) 的完整核心兼容扫描

复现程序对

\[
7\le R\le9999,
\qquad
R\equiv7\pmod8
\tag{9}

的全部 1250 个模数构造 \(U_R\)，枚举每一个有向简单周期，并对每个周期完整生成
(6)。精确结果为：

\[
\begin{array}{c|r}
\text{含周期的模数}&99\\
\text{有向简单周期}&435\\
-1\in\mathcal C_S&435\\
-1\notin\mathcal C_S&0.
\end{array}
\tag{10}

支撑大小介于 5 与 22；程序为 435 个周期各自保存一组平方自由互素 \((a,b)\)，并
直接核对 \(R\mid a+b\)。由于扫描对象是通用图，这个结论对范围内任意大小的 \(K\)
成立，而不是按 \(p\) 或 \(K\) 取样。

复现入口为 `reproductions/type_i_core_formal_cycle_radical_hit.py`，结果文件为
`reproductions/type-i-core-formal-cycle-radical-hit-results.json`。

## 5. 非核心边界

不能删去核心同余条件。取

\[
R=7219,
\qquad
K=12{,}298{,}570{,}220{,}629{,}770,
\qquad
p=6{,}814{,}556{,}154{,}941.
\tag{11}

这里 \(p\) 是素数但

\[
p\equiv5\pmod{24}.
\tag{12}

存在实际 \(K\) 支撑周期

\[
\{19,7200\}\to
\{3600,3619\}\to
\{1800,5419\}\to
\{360,6859\}\to
\{361,6858\}\to
\{19,7200\},
\tag{13}

所用素数依次为 \(2,2,5,19,19\)。周期坐标支撑的 (6) 不含 \(-1\)，加入 \(K\)
的全部素因子后完整中心盒仍不含 \(-1\)。所以“任意奇 \(R\) 的周期都强制中心命中”
是假的；(3) 的核心约化是实质条件。

## 6. 原全称命题已被否定

有限结果 (10) 曾指向一个不再含 \(p\)、\(K\) 或解提升的纯组合命题：

\[
\boxed{
R\equiv7\pmod8\text{ 时，}U_R\text{ 的每个有向简单周期 }\mathcal Z
\text{ 都满足 }-1\in\mathcal C_{S(\mathcal Z)}.}
\tag{14}

这个命题现在已知为假。第一个按 \(R\) 递增找到的反例位于

\[
R=30031,
\qquad
\mathcal Z=(31,6000,1200,240,961).
\tag{15}
\]

它的周期坐标支撑为

\[
S=\{2,3,5,7,11,17,19,31,2621,3433\},
\tag{16}
\]

完整 signed cube 有 25357 个不同残数，但不含 \(-1\)。因此 435/435 只能保留为
\(R\le9999\) 的完整有限定理，不能再作为 (14) 的无反例证据外推。

不过 (15) 没有否定“实际核心 \(K\) 支撑周期必终端”。一方面，它的支撑含 3，而
\(R\equiv1\pmod3\)、核心 \(p\equiv1\pmod3\) 强制 \(K\equiv2\pmod3\)，所以它不可能
嵌入真实核心 \(K\) 支撑图。另一方面，同一 support cube 命中
\(-4\operatorname{rad}(S)\) 及其对应的逆目标，并由三目标乘子桥恢复完整 \(K\) 中心盒
命中。精确反例、桥定理和见证见
[周期平方自由支撑的三目标乘子桥与首个直接反例](type-I-formal-cycle-radical-multiplier-bridge.md)。

所以新的开放对象不再是 (14)，而是以下更弱且更贴近原状态的析取：实际核心支撑周期
是否总由三目标乘子桥命中，或由
[周期表示格与容量盒判据](type-I-formal-cycle-representation-lattice-capacity.md)
产生交点。两者都仍不处理含外部支撑的合法 support switch 或 \(m>1\) 状态。
