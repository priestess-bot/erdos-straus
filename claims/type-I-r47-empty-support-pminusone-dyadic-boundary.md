---
kind: claim
claim_id: type-I-r47-empty-support-pminusone-dyadic-boundary
title: R=47 空掩码的 p-1 二进终端与外部出口边界
statement: 对 R=47 周期相图的空掩码，写 K=(47p+1)/4=6Q；精确赋值 v_2(K)=v_3(K)=1 强制 Q≡2 (mod 47)。取 L=2K、(a,b,j)=(4,Q,1) 统一得到 E=48、n=p-1 的广义二进终端。该终端在同一 R 上的自然标记提升仍等价于中心谱 Type I 命中，且该无限进程同时含真实 F 与 G 状态。A,C∈{1,2} 的四条 raw Type II 菜单也不能由空掩码同余强制：p=193391641 同时遗漏四个移位除子目标。前 100 个规范进程素数均有普通 p-1 Type II 双尾递降只是可复现支持数据，不是全称定理。
claim_status: established
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-I-r47-cycle-lattice-capacity-three-phase-boundary
  - type-I-r47-cycle-nonempty-support-short-selector
  - type-I-general-dyadic-terminal-transfer
  - type-I-general-b-centered-square-spectrum
  - type-I-normal-pminusone-upper-half-bridge
  - type-II-coprime-factor-normal-form
  - type-II-raw-ray-certificate
  - type-II-two-tail-deflation-descent
topics:
  - type-I
  - type-II
  - r47
  - cycle
  - empty-support
  - dyadic-terminal
  - p-minus-one
  - F-state
  - G-state
  - selector-boundary
  - proof-program
sources:
  - claim: type-I-r47-cycle-lattice-capacity-three-phase-boundary
    role: empty-mask-progression-and-exact-valuations
  - claim: type-I-r47-cycle-nonempty-support-short-selector
    role: nonempty-mask-short-certificate-closure
  - claim: type-I-general-dyadic-terminal-transfer
    role: dyadic-terminal-verifier
  - claim: type-I-general-b-centered-square-spectrum
    role: exact-F-G-and-hit-classification
  - claim: type-I-normal-pminusone-upper-half-bridge
    role: same-R-p-minus-one-marked-bridge
  - claim: type-II-raw-ray-certificate
    role: four-small-ray-divisor-equivalence
  - claim: type-II-two-tail-deflation-descent
    role: p-minus-one-marked-lift
visibility: public
last_checked: '2026-07-31'
---

# \(R=47\) 空掩码的 \(p-1\) 二进终端与外部出口边界

## 空掩码统一产生 \(E=48\)

令 \(p\equiv1\pmod {24}\) 为素数，

\[
K=\frac{47p+1}{4},
\tag{1}
\]

并处在 \(R=47\) 五周期相图的空掩码分支：

\[
v_2(K)=v_3(K)=1,
\qquad
5,13,31,43\nmid K.
\tag{2}
\]

写

\[
K=6Q,
\qquad (Q,6)=1.
\tag{3}
\]

由 \(4K\equiv1\pmod {47}\) 得

\[
24Q\equiv1\pmod {47},
\qquad
Q\equiv2\pmod {47}.
\tag{4}
\]

现在取一般二进传输中的

\[
L=2K=12Q,
\qquad a=4,
\qquad b=Q,
\qquad j=1.
\tag{5}
\]

因为 \(Q\) 为奇数，\((a,b)=1\)，且 \(a,b\mid L\)。式 (4) 给出

\[
a\equiv2b\pmod {47}.
\]

若 \(Q=2\)，式 (1)、(3) 会迫使 \(p=1\)；故 \(Q>2\)，从而 \(a<2b\)。
一般二进终端定理于是统一给出

\[
\boxed{
E=L\frac ab=48,
\qquad
n=\frac{4K-48}{47}=p-1.}
\tag{6}
\]

因此，十五个非空掩码已有短 Type I/II 证书之后，唯一的周期格
`MISS_EXTERNAL` 也不再缺少**偶终端**。它缺少的是把 (6) 接回原目标的解提升。

## 同一 \(R\) 的自然提升仍等价于 Type I

把 (6) 输入 Type I 最大尾反向选择器，只能从一个已经存在的 \(R=47\) Type I 正规形
反向得到标记 \(p-1\) 源。中心化平方谱给出精确条件

\[
-1\in\mathcal C_{47}(K).
\tag{7}
\]

这里正反两向都没有遗漏。若 (7) 命中，就先恢复一个同 \(R=47\) Type I 正规形；
再令

\[
r=\frac{R+1}{4}=12,
\qquad u=\frac{p-1}{4}.
\]

核心同余使 \(6\mid u\)，故 \(r\mid u^2\)。\(p-1\) 最大尾桥判据于是把该正规形
严格反向连接到 (6)。反过来，任何这种自然最大尾提升的目标端本来就是同 \(R=47\)
Type I 正规形，必满足 (7)。故 \(E=48\) 不能把 F/G miss 自动升级成解；它只在
(7) 已命中时附着到对应正规形。

规范空掩码进程中两种失败都真实出现。取

\[
p=31\,192\,201,
\qquad
K=366\,508\,362
=2\cdot3\cdot11\cdot5\,553\,157.
\]

其中心谱有 45 个剩余类、不含 \(-1\)，而支撑生成整个 46 阶单位群，所以这是 F 状态。
另取

\[
p=81\,099\,721,
\qquad
K=952\,921\,722
=2\cdot3\cdot158\,820\,287.
\]

其中心谱有 13 个剩余类；支撑子群阶为 23，且不含 \(-1\)，所以这是 G 状态。
两点均满足 (2)，也均有 (6) 的 \(p-1\) 偶终端，但没有同一 \(R=47\) 的自然 Type I
标记提升。

它们仍可被其它状态闭合。例如普通 Type II 双尾分别给出

\[
\begin{array}{c|c|c|c}
p&m&x&d\\ \hline
31\,192\,201&7&7\,798\,052&4\\
81\,099\,721&3&20\,274\,931&17
\end{array}
\tag{8}
\]

其中 \(d\mid x^2\)、\(d\le x\)、\(m\mid x+d\)，且
\(m+1\mid p-1\)。所以 (8) 同时给出目标 Type II 证书和严格较小的标记源。这说明正确的
出口必须允许切换正规形或模数，不能把“同 \(R\) 不可提升”误报成原素数无解。

## 四条小 raw Type II 射线并不受同余强制

固定正整数 \(A,C\)，令

\[
\ell=4AC\kappa-1.
\]

Type II raw 射线条件 \(\ell\mid\kappa p+A\) 等价于

\[
\ell\mid p+4A^2C,
\qquad
\ell\equiv-1\pmod {4AC}.
\tag{9}
\]

反向由 \(\kappa=(\ell+1)/(4AC)\) 及

\[
4AC(\kappa p+A)=\ell p+(p+4A^2C)
\]

恢复整除。由于 \(\ell\equiv-1\pmod {4AC}\)，有
\(\gcd(\ell,4AC)=1\)，所以可以从右式消去 \(4AC\)，得到
\(\ell\mid\kappa p+A\)。当 \(p\ge4A^2C\) 时序条件 \(A\le B\) 自动成立。因此
\(A,C\in\{1,2\}\) 的四项菜单精确化为

\[
\begin{array}{c|c|c}
(A,C)&\text{移位整数}&\text{所需除子类}\\ \hline
(1,1)&p+4&-1\pmod4\\
(1,2)&p+8&-1\pmod8\\
(2,1)&p+16&-1\pmod8\\
(2,2)&p+32&-1\pmod {16}.
\end{array}
\tag{10}
\]

规范空掩码 CRT 进程是

\[
p=6\,238\,441+12\,476\,880t.
\tag{11}
\]

其中第五个素数

\[
p=193\,391\,641
\qquad(t=15)
\tag{12}
\]

已经使四项同时失败。其移位分解和完整除子剩余类为

\[
\begin{array}{c|l|l}
N&\text{素因子分解}&\Pi_N\\ \hline
p+4&5\cdot229\cdot168901&\Pi_N(4)=\{1\}\\
p+8&3^2\cdot11\cdot1953451&\Pi_N(8)=\{1,3\}\\
p+16&5939\cdot32563&\Pi_N(8)=\{1,3\}\\
p+32&3\cdot73\cdot139\cdot6353&\Pi_N(16)=\{1,3,9,11\}.
\end{array}
\tag{13}
\]

目标 \(3,7,7,15\) 均缺失。并且

\[
K=2\,272\,351\,782
=2\cdot3\cdot29\cdot1297\cdot10069,
\]

所以 (12) 确属空掩码。这严格否定了“空掩码同余必强制四射线之一”的候选命题。

该点并不是联合选择器反例：它在缺口 \(m=3\) 处取

\[
x=48\,347\,911,
\qquad d=6761,
\]

便有普通 \(p-1\) Type II 双尾递降。

## 定向有限画像

复现器沿 (11) 按 \(t\) 递增只取前 100 个素数；范围为

\[
2\le t\le479,
\qquad
31\,192\,201\le p\le5\,982\,663\,961.
\]

结果为

\[
\begin{array}{c|r}
\text{分支}&\text{命中数}\\ \hline
A,C\in\{1,2\}\text{ 四射线}&97\\
\text{四射线 miss}&3\\
\text{普通 }p-1\text{ Type II 双尾}&100.
\end{array}
\tag{14}
\]

三个四射线 miss 是

\[
193\,391\,641,
\quad1\,091\,727\,001,
\quad3\,686\,918\,041.
\]

普通双尾的首见缺口只取 \(3,7,11,19,23\)，计数分别为

\[
44,41,7,3,5.
\tag{15}
\]

式 (14)--(15) 是为下一步选择假设服务的有限数据，不是由 (11) 的同余推出的定理。
首见除子读取每个移位整数变化中的因子结构，不能把 100/100 升级成全称量词。

一个更大的 \(p-1\) Type I 射线菜单现已得到角色级解析。对每个参数奇偶恰有 24 个
桥尺度 \(S\mid6\,238\,440\)、\(v_2(S)=3\)；所有固定 \(S\) 支撑都被一个 Jacobi
角色送到 \(+1\)，而目标 \(-1\) 被送到 \(-1\)，所以命中必须读取变量余因子。
其中 \(S=8,24,40\) 的固定中心谱恰等于角色核，目标命中精确等价于变量余因子含负
Jacobi 素因子。见
[R=47 空掩码 p-1 射线的 Jacobi 障碍与三条精确角色选择器](type-I-r47-pminusone-jacobi-ray-selector.md)。
该结果给出三条真正的规范 Fourier/角色选择器，但也证明固定尺度部分本身不可能覆盖空
掩码余核。

## 当前最短缺口

空掩码路线现在可以精确分层：

1. 周期格外部消元失败；
2. 但统一存在 \(E=48,n=p-1\) 的偶终端；
3. 同 \(R=47\) 的 F/G 状态不能借该终端自动提升；
4. 四条小 raw Type II 射线也不受 AP 同余强制；
5. 当前有限样本由变化的普通 \(p-1\) Type II 因子全部闭合。

因此下一步不应继续寻找另一个偶终端，而应研究 \(p-1\) 的有限因子射线之间是否存在
容量互补，或从其失败构造一个具有新 \(R,K\) 且满足完整提升合同的后继状态。

复现：

```text
python3 reproductions/type_i_r47_empty_support_dyadic_boundary.py
```

结果文件：

```text
reproductions/type-i-r47-empty-support-dyadic-boundary-results.json
```

脚本与结果文件的 SHA-256 分别为
`423759d2777aa8b432de0325675bd7beeab540694d1031e74a217cca327f4d45`、
`3bd4eca824df0d123168b7ccc63224620706577e879ffdbac268893139a4ef57`。
