---
kind: claim
claim_id: type-I-odd-primary-component-kernel-crt-rechart-descent
title: 奇主阶记录的完整分量核、CRT 重图表递降与全支撑障碍
statement: >-
  设核心 Type I Jacobi F 图表满足 p=1 (mod 24)、4K=pR+1、R=3
  (mod 4)，并有一条 Jacobi-negative 记录 z，记 s=-Phi(z) 属于
  ker(chi_R)。对任一奇素数 ell 整除 ord(s)，令 ell^a||ord(s)、
  k=ord(s)/ell^a，并按 k 的奇偶规范定义
  omega=Phi(delta ell^(a-1) k z)，其中 delta=1 (k 偶) 或 2 (k 奇)。则
  omega 在 U(R) 中精确为 ell 阶，lambda=delta ell^a k z 是非零核关系。
  令 R_0 为 R 的全部素数幂分量中 omega 恰为 1 的乘积，R_1=R/R_0。
  若 R_0>1，则 R_0,R_1 是互素真因子；其中唯一的 3 (mod 4) 因子 R_*<R
  给出 K_*=(pR_*+1)/4、恒等解提升 Sol(4,p)->Sol(4,p)，以及在既有
  CRT_DESCENT 调度下由 (epsilon_CRT,R) 严格降低的完整 E1--E5 重图表边。
  若 R_0=1，则输出 ODD_PRIMARY_FULL_COMPONENT_SUPPORT：该精确障碍只说明
  此奇主阶记录没有非平凡完整 CRT kernel 分量，不能推出不存在别的 source、终端或递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-core-jacobi-punctured-kernel-primary-selector
  - type-I-pure-dyadic-half-power-crt-rechart-descent
  - type-I-canonical-complete-support-rechart-g-obstruction
  - denominator-escape-state-contract
topics:
  - type-I
  - jacobi
  - odd-primary
  - CRT
  - component-kernel
  - rechart
  - well-founded-descent
  - E1-E5
  - proof-program
sources:
  - claim: type-I-core-jacobi-punctured-kernel-primary-selector
    role: Jacobi-negative-record-and-odd-Hall-input
  - claim: type-I-pure-dyadic-half-power-crt-rechart-descent
    role: shared-chart-independent-lift-and-CRT-phase-policy
  - reproduction: reproductions/type_i_odd_primary_component_kernel_crt_rechart_descent.py
    role: focused-primary-extraction-component-split-and-obstruction-controls
visibility: public
last_checked: '2026-08-12'
---

# 奇主阶记录的完整分量核、CRT 重图表递降与全支撑障碍

## 1. 从任意奇主阶记录规范抽出精确 ell 阶元

设

\[
p\equiv1\pmod {24},\qquad R\equiv3\pmod4,\qquad 4K=pR+1,
\tag{1}
\]

且核心 Jacobi F 状态给出一个负记录 \(z\)，写

\[
\Phi(z)=-s,\qquad s\in L=\ker\chi_R.
\tag{2}
\]

取任一奇素数 \(\ell\mid\operatorname{ord}(s)\)，并写

\[
\ell^a\Vert\operatorname{ord}(s),\qquad
k=\frac{\operatorname{ord}(s)}{\ell^a},\qquad
\delta=
\begin{cases}
1,&2\mid k,\\
2,&2\nmid k.
\end{cases}
\tag{3}
\]

令 \(v=s^k\)。那么 \(v\) 的精确阶为 \(\ell^a\)。定义

\[
\boxed{
\omega=\Phi(\delta\ell^{a-1}kz),\qquad
\lambda=\delta\ell^akz.}
\tag{4}
\]

若 \(k\) 为偶数，\(\Phi(kz)=s^k=v\)；若 \(k\) 为奇数，
\(\Phi(kz)=-v\)，而 \(\delta=2\) 消去该负号。因此

\[
\omega=v^{\delta\ell^{a-1}},qquad
\operatorname{ord}_R(\omega)=\ell,qquad
\Phi(\lambda)=1.
\tag{5}
\]

这里 \(z\ne0\)，故 \(\lambda\ne0\)。式 (4) 不要求把放大的 \(\lambda\)
伪装成原指数盒中的短终端；它只是从原始带来源记录提取一个确定性的奇主阶
CRT 数据。若需要一个唯一输出，可先按冻结的记录编码选择 \(z\)，再选
\(\operatorname{ord}(s)\) 的最小奇素因子 \(\ell\)。

## 2. 完整素数幂分量核是精确的分裂条件

对 \(R\) 的每个完整素数幂 \(q^e\Vert R\)，\(\omega\) 在
\(U(q^e)\) 中的阶只能是 \(1\) 或 \(\ell\)。定义它的**完整分量核**

\[
\boxed{
R_0=\prod_{\substack{q^e\Vert R\\\omega\equiv1\ (\bmod q^e)}}q^e,
\qquad R_1=\frac R{R_0}.}
\tag{6}
\]

这个定义刻意按完整素数幂而不是只写 \(\gcd(R,\omega-1)\)：当
\(q=\ell\) 时，\(\omega-1\) 可以只含 \(q\) 的一部分赋值，不能据此把一个
素数幂错误地拆成两个 CRT 因子。由定义

\[
R_0R_1=R,\qquad (R_0,R_1)=1.
\tag{7}
\]

又因 \(\omega\) 精确为 \(\ell\) 阶，\(\omega\not\equiv1\pmod R\)，从而
\(R_1>1\)。所以

\[
\boxed{R_0>1\quad\Longrightarrow\quad R_0,R_1\text{ 均为 }R\text{ 的互素真因子}.}
\tag{8}
\]

这正是奇阶版本中可替代二进 \(\omega\pm1\) 的信息：一个完整 CRT 分量为
kernel，另一个完整 CRT 分量承载非平凡 \(\ell\)-阶相位。反之，\(R_0=1\) 精确地说
该 \(\omega\) 在每个完整素数幂分量上都非平凡；它不是“没有因子”的断言，
更不是全局无解结论。

## 3. 部分支撑时的严格重图表

以下假设 \(R_0>1\)。由于 \(R\equiv3\pmod4\)，互素奇因子 \(R_0,R_1\)
中恰有一个满足 \(3\pmod4\)。记

\[
\boxed{
R_*=\text{\(R_0,R_1\) 中唯一的 }3\pmod4\text{ 因子},
\qquad c=R/R_*.}
\tag{9}
\]

于是

\[
1<R_*<R,\qquad c>1,\qquad c\equiv1\pmod4,
\tag{10}
\]

并可定义合法的新中心图表

\[
K_*=\frac{pR_*+1}{4}.
\tag{11}
\]

与二进半幂分裂完全相同的整数恒等式为

\[
\boxed{
K=cK_*-\frac{c-1}{4},\qquad
\gcd(K,K_*)=\gcd\!\left(K_*,\frac{c-1}{4}\right).}
\tag{12}
\]

它既记录了旧素数支撑可否留在新图表，也防止把该边误写成保持旧 target fiber 的
同图表操作。

终端优先选择器已检查直接 Type I、Type II 以及适用的已验证 marked terminal 后，
将 (2)--(12) 作为具名边

```text
core_odd_primary_component_kernel_crt_rechart_v1
```

的 E1--E5 回执：

| 门 | 证明数据 |
|---|---|
| E1 | 原图表、Jacobi-negative 记录 \(z\)、\(\ell,a,k,\delta\) 与式 (4)--(5) 的精确阶/核关系 |
| E2 | 完整分量核 \(R_0,R_1\)、唯一 \(R_*\) 及 \(K_*\) |
| E3 | 从整数重算相位、完整素数幂分量、式 (7)--(12) 和新图表的 hit/F/G 类型 |
| E4 | \(W_T=W_S=\operatorname{Sol}(4,p)\)，提升 \(w\mapsto w\) 为恒等映射 |
| E5 | 进入既有不可逆 `CRT_DESCENT` 调度，并使用 \(\Pi_{\rm CRT}=(\epsilon_{\rm CRT},R)\) 的字典序势 |

第一次授权 CRT 边把 \(\epsilon_{\rm CRT}\) 从 \(1\) 置为 \(0\)；之后每条授权的
此类边均由 (10) 严格降低 \(R\)。因此该边不能无代价回到增大 \(R\) 的旧图表，且
和纯二进半幂边共享同一个全域良基策略。新图表必须独立重算 target fiber、F/G 类型和
因子支撑，不能继承旧标记。

由此得到精确的二分：

\[
\boxed{
\begin{array}{rcl}
\text{odd-primary Jacobi record}+R_0>1
&\Longrightarrow&\text{terminal 或严格可提升 }R\to R_*\text{ rechart},\\
\text{odd-primary Jacobi record}+R_0=1
&\Longrightarrow&\texttt{ODD\_PRIMARY\_FULL\_COMPONENT\_SUPPORT}.
\end{array}}
\tag{13}
\]

第二行只阻断本卡的 component-kernel CRT 构造；它仍应转交已有的 odd-Hall
Fourier/source 选择器，而不是升级成无解声明。

## 4. 聚焦控制

所有控制均从完整整数与原指数向量重算；它们验证的是本引理的输入和边界，
不声称这些已知素数会绕过 terminal-first 调度。

### 4.1 \(p=73,R=95\)：真实 F 记录给出严格 \(95\to19\)

\[
K=1734=2\cdot3\cdot17^2,qquad z=(0,-1,1),
\qquad\Phi(z)=69,quad s=26,quad\operatorname{ord}(s)=3.
\]

所以 \(\ell=3,a=1,k=1,\delta=2\)，并有

\[
\omega=69^2=11\pmod {95},qquad
R_0=5,\quad R_1=19,quad R_*=19,
\quad K_*=347.
\tag{14}
\]

这里 \(c=5\)，且 \(1734=5\cdot347-1\)、\(\gcd(1734,347)=1\)。
故该实际 F 记录的奇主阶分量核给出严格重图表 \(95\to19\)。

### 4.2 \(p=73,R=63\)：\(\ell\mid R\) 仍须按完整分量判断

\[
K=1150=2\cdot5^2\cdot23,qquad z=(-1,1,1),
\qquad\Phi(z)=26,quad s=37,quad\operatorname{ord}(s)=3.
\]

抽取后 \(\omega=26^2=46\pmod {63}\)。它在 \(9\) 上恰为 \(1\)，
在 \(7\) 上非平凡，故

\[
R_0=9,\qquad R_1=7,\qquad R_*=7,\qquad K_*=128.
\tag{15}
\]

这说明只使用 \(\gcd(R,\omega-1)\) 的部分赋值会丢失关键语义；完整素数幂定义
(6) 正确给出 \(63\to7\)。本素数另有既知 Type II 短证书，所以全局调度会更早终止。

### 4.3 \(p=97,R=67\)：精确的全分量支撑障碍

\[
K=1625=5^3\cdot13,qquad z=(-3,0),
\qquad\Phi(z)=52,quad s=15,quad\operatorname{ord}(s)=11.
\]

此时 \(\omega=52^2=24\pmod {67}\)，而 \(R=67\) 的唯一完整分量上
\(\omega\ne1\)。故

\[
R_0=1.
\tag{16}
\]

输出 `ODD_PRIMARY_FULL_COMPONENT_SUPPORT`。这严格说明本卡不能从该 11 阶记录
制造真 CRT kernel 分量；它不否定该状态的其它 odd-owner/source 路径。

## 聚焦验证

```bash
python3 reproductions/type_i_odd_primary_component_kernel_crt_rechart_descent.py --verify
```

验证器只重算三个控制的 Jacobi-negative 记录、奇主阶提取、完整分量核、
中心恒等式和全支撑障碍；不运行历史扫描。
