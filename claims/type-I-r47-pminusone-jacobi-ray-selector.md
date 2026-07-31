---
kind: claim
claim_id: type-I-r47-pminusone-jacobi-ray-selector
title: R=47 空掩码 p-1 射线的 Jacobi 障碍与三条精确角色选择器
statement: 在 R=47 空掩码规范进程 p=1+6238440(2t+1) 上，取 S|6238440、v_2(S)=3 且 H=(p-1)/S≡1 (mod 4)，并令 R_S=S-1、A_S=(R_SH+1)/4、K_S=(R_Sp+1)/4=SA_S。每个 t 奇偶恰有 24 个合法 S。Jacobi 角色 chi_S=(·/R_S) 在所有 q|S 上取 +1、在 -1 上取 -1，故只用固定 S^2 的除子永不命中；若 A_S 的全部素因子也为正角色，则该状态严格为 G。对 S=8,24,40，固定中心谱恰等于 ker chi_S，因此目标命中当且仅当 A_S 含负 Jacobi 素因子；其中 S=8,40 只适用于偶 t，S=24 只适用于奇 t。命中可规范为 d<K_S，并附着到 n=p-1 的合法 Type I 桥。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-r47-empty-support-pminusone-dyadic-boundary
  - type-I-general-b-centered-square-spectrum
  - type-I-normal-pminusone-upper-half-bridge
  - type-I-f-g-fourier-obstruction-certificate
topics:
  - type-I
  - r47
  - empty-support
  - p-minus-one
  - Jacobi-symbol
  - quadratic-character
  - G-state
  - centered-spectrum
  - canonical-selector
  - proof-program
sources:
  - claim: type-I-r47-empty-support-pminusone-dyadic-boundary
    role: canonical-empty-mask-progression
  - claim: type-I-general-b-centered-square-spectrum
    role: centered-target-and-F-G-classification
  - claim: type-I-normal-pminusone-upper-half-bridge
    role: exact-p-minus-one-source-bridge
visibility: public
last_checked: '2026-07-31'
---

# \(R=47\) 空掩码 \(p-1\) 射线的 Jacobi 障碍与三条精确角色选择器

## 规范进程与 24 个合法桥尺度

写

\[
N=6\,238\,440
=2^3\cdot3^2\cdot5\cdot13\cdot31\cdot43
=8M,
\qquad
M=779\,805.
\tag{1}
\]

\(R=47\) 空掩码的规范进程可写为

\[
p=p(t)=1+N(2t+1),
\qquad t\ge0.
\tag{2}
\]

本卡只把其中为素数的 \(p(t)\) 解释为 Erdős--Straus 核心输入；下面的 Jacobi 代数对
所有 \(t\) 都成立。

取

\[
S\mid N,
\qquad
v_2(S)=3,
\qquad
H=\frac{p-1}{S}\equiv1\pmod4.
\tag{3}
\]

令

\[
R_S=S-1,
\qquad
A_S=\frac{R_SH+1}{4},
\qquad
K_S=\frac{R_Sp+1}{4}.
\tag{4}
\]

由于 \(p=1+SH\)，直接展开得到

\[
R_Sp+1
=(S-1)(1+SH)+1
=S\bigl(1+R_SH\bigr),
\]

故

\[
\boxed{K_S=SA_S.}
\tag{5}
\]

这里 \(R_S\equiv7\pmod8\)。若写 \(R_S=4r-1\)，则 \(r=S/4\)，且

\[
\frac{p-1}{4}=\frac{SH}{4}=rH.
\]

所以 \(r\mid((p-1)/4)^2\)，由 \(p-1\) 桥判据，任何 \((R_S,K_S)\) 的中心谱
Type I 命中都附着到唯一桥因子

\[
E=R_S+1=S,
\qquad n=p-1.
\tag{6}
\]

式 (3) 的尺度数也精确固定。写 \(S=8d\)、\(d\mid M\)，并令 \(c=M/d\)，则

\[
H=c(2t+1).
\]

\(M\) 有 48 个除子；切换因子 31 的指数把 \(c\equiv1\pmod4\) 与
\(c\equiv3\pmod4\) 配对。因此每个固定 \(t\) 恰有 24 个尺度满足 (3)。当 \(t\)
奇偶切换时，\(2t+1\) 在模 4 下由 1 切换为 3，所以两组 24 个尺度互补并分割全部
48 个 \(v_2(S)=3\) 的尺度。

## 全部尺度共有的 Jacobi 角色障碍

在单位群上定义 Jacobi 角色

\[
\chi_S:(\mathbb Z/R_S\mathbb Z)^\times\longrightarrow\{\pm1\},
\qquad
\chi_S(a)=\left(\frac{a}{R_S}\right).
\tag{7}
\]

因 \(R_S\equiv7\pmod8\)，有

\[
\chi_S(2)=+1,
\qquad
\chi_S(-1)=-1.
\tag{8}
\]

再取任意奇素数 \(q\mid S\)。此时 \((q,R_S)=1\)、\(R_S\equiv-1\pmod q\)，且
\(R_S\equiv3\pmod4\)。Jacobi 二次互反律给出

\[
\begin{aligned}
\left(\frac q{R_S}\right)
&=(-1)^{(q-1)/2}\left(\frac{R_S}{q}\right)\\
&=(-1)^{(q-1)/2}\left(\frac{-1}{q}\right)
=+1.
\end{aligned}
\tag{9}
\]

结合 (8)，得到

\[
\boxed{\chi_S(q)=+1\quad(q\mid S),
\qquad \chi_S(-1)=-1.}
\tag{10}
\]

另一方面，\(4A_S\equiv1\pmod {R_S}\)，故 \((A_S,R_S)=1\) 且

\[
\chi_S(A_S)=\chi_S(4^{-1})=+1.
\tag{11}
\]

任意 \(d\mid S^2\) 都有 \(\chi_S(d)=+1\)，而

\[
\chi_S(-K_S)
=\chi_S(-1)\chi_S(S)\chi_S(A_S)
=-1.
\]

因此

\[
\boxed{
d\mid S^2
\Longrightarrow
d\not\equiv-K_S\pmod {R_S}.}
\tag{12}
\]

这证明固定尺度支撑本身永远不能完成目标；任何命中都必须读取变量余因子 \(A_S\)。
更强地，若 \(A_S\) 的每个素因子 \(\ell\) 都满足 \(\chi_S(\ell)=+1\)，则
\(K_S\) 的整个素因子生成子群都包含在 \(\ker\chi_S\) 中，而 \(-1\) 不在其中。
所以该状态严格属于 G 分支，而不只是有限指数盒 F miss。

这里不假设 \((S,A_S)=1\)。同一素数可以同时出现在两者中；中心指数区间按

\[
[-v_q(SA_S),v_q(SA_S)]
=[-v_q(S),v_q(S)]+[-v_q(A_S),v_q(A_S)]
\tag{13}
\]

相加，角色论证仍然成立。

## 三条精确角色选择器

记固定尺度的中心谱为

\[
\mathcal C_{R_S}(S)
=\left\{\prod_{q\mid S}q^{z_q}\pmod {R_S}:
-v_q(S)\le z_q\le v_q(S)\right\}.
\tag{14}
\]

对三个最小合法尺度，直接群论计算给出

\[
\begin{aligned}
\mathcal C_7(8)
&=\{1,2,4\}=\ker\chi_8,\\
\mathcal C_{23}(24)
&=\{1,2,3,4,6,8,9,12,13,16,18\}=\ker\chi_{24},\\
\mathcal C_{39}(40)
&=\{1,2,4,5,8,10,11,16,20,22,25,32\}=\ker\chi_{40}.
\end{aligned}
\tag{15}
\]

于是对 \(S\in\{8,24,40\}\)，有精确选择条件

\[
\boxed{
-1\in\mathcal C_{R_S}(K_S)
\Longleftrightarrow
\exists\,\ell\mid A_S:\ \chi_S(\ell)=-1.}
\tag{16}
\]

必要性（命中推出存在负角色素因子）已由上一节的 G 角色障碍的逆否命题给出。
充分性证明如下：若
\(\ell\mid A_S\) 且 \(\chi_S(\ell)=-1\)，则

\[
\chi_S(-\ell^{-1})=+1.
\]

由 (15)，存在 \(c\in\mathcal C_{R_S}(S)\) 满足
\(c\equiv-\ell^{-1}\pmod {R_S}\)。再从 \(A_S\) 的中心指数区间取 \(\ell^1\)，便有

\[
c\ell\equiv-1\pmod {R_S}.
\]

即使 \(\ell\mid S\)，式 (13) 也保证两个指数贡献可以相加到
\(\mathcal C_{R_S}(K_S)\) 中。这证明 (16)。

三个尺度不能对同一 \(t\) 无条件同时调用。由 (3) 精确得到

\[
\begin{array}{c|c|c}
S&R_S&\text{适用参数}\\ \hline
8&7&t\equiv0\pmod2,\\
24&23&t\equiv1\pmod2,\\
40&39&t\equiv0\pmod2.
\end{array}
\tag{17}
\]

所以偶 \(t\) 有 \(S=8,40\) 两条精确角色选择器，奇 \(t\) 只有 \(S=24\) 这一条。

## 从中心角色命中到严格除子证书

由中心谱恒等式，式 (16) 命中当且仅当存在

\[
d\mid K_S^2,
\qquad
d\equiv-K_S\pmod {R_S}.
\tag{18}
\]

若某个命中除子 \(d>K_S\)，则互补因子 \(K_S^2/d\) 的中心比值仍为 \(-1\)。而
\(d=K_S\) 会迫使 \(R_S\mid2\)，与 \(R_S\ge7\) 矛盾。因此可规范选择

\[
\boxed{d<K_S.}
\tag{19}
\]

式 (18)--(19) 恢复同一素数 \(p\) 的一般 \(B\) Type I 正规形；式 (6) 又把它连接到
严格较小的偶源 \(n=p-1\)。所以三条角色条件一旦命中，输出的是可独立验真的 Type I
证书和合法 \(p-1\) 标记桥，而不是抽象 Fourier 相关性。

## 复现与边界

复现器
`reproductions/type_i_r47_pminusone_jacobi_ray_selector.py` 精确枚举两种参数奇偶的
24 个尺度，逐尺度核对 (8)--(12)，并验证 (15) 的三个谱等式。它只保存六个定向样例
来回归 (16)，不从样例外推全称量词。冻结结果为
`reproductions/type-i-r47-pminusone-jacobi-ray-selector-results.json`。

本卡没有证明三个精确尺度之一对每个进程素数都命中。若 \(A_S\) 的素因子全部落在
正角色核内，式 (16) 精确给出 G miss；对其余 21 条尺度，固定谱一般只是
\(\ker\chi_S\) 的真子集，出现负角色素因子也只消除 G 障碍，仍可能留下 F 容量障碍。
因此下一步应研究变量 \(A_S\) 的角色因子析取，或把 24 条角色/Fourier 失败接到普通
\(p-1\) Type II 双尾与合法换状态，而不能把“每个奇偶有 24 个候选”本身当作覆盖证明。
