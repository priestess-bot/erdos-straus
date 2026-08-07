---
kind: claim
claim_id: type-I-g-anchor-c3-adaptive-core19-v5-q19-phase-compatible-candidate-fiber
title: v=5 signed 双叶的 q=19 相位兼容 Type II 候选纤维
statement: 对 v=5 的 signed raw marks mu0=13、mu1=4387621028405，可取同模数 Type II 候选 D=D*=6303、A=573、s=3611619、M*=25212，及两个带来源标签 b0=18909、b1=s。它们在共享 q=19 账本上给出恰为 d19=3 的可回译高度。候选 N=p+4s 含 H0=53*3671 和 H1=19H0，character chi(x)=x^10 (mod 191) 满足 chi(H0)=eta(mu0)、chi(H1)=eta(mu1)、chi(19)=eta(mu1/mu0)。但 H0、H1 都只属于候选 N 而不是两条独立 raw 来源块；该固定纤维也没有 h|N、h=-1 (mod 25212)。故它是严格的 phase-compatible candidate fiber，不是完整 integer adapter、capacity 或 selector edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-c3-adaptive-core19-v5-signed-marked-source-groupoid
  - type-II-source-fiber-shared-q-ledger
  - type-II-filtered-composition-source-slot-terminal
topics:
  - type-I
  - type-II
  - c3
  - core19
  - source-fiber
  - q-adic-height
  - repeated-q
  - signed-mark
  - character
  - candidate-fiber
  - terminal-preempted
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_c3_adaptive_core19_v5_q19_phase_compatible_fiber.py
    role: q=19 ledger, signed-character correspondence, and finite target boundary
visibility: public
last_checked: '2026-08-07'
---

# v=5 signed 双叶的 \(q=19\) 相位兼容 Type II 候选纤维

本卡构造一个同时通过范围、重复 \(q\) 账本和角色相位的有限候选纤维。它特意把
“候选纤维存在”与“raw 到整数 adapter 已完成”分开。

## 1. 输入的 signed 相位

在 v=5 的 core-19 双叶控制中，

\[
\mu_0=13,\qquad
\mu_1=4387621028405\pmod R,
\tag{1}
\]

并且对 \(\zeta=150\in U(191)\)、\(\eta_R(x)=x^{10}\pmod {191}\)，有

\[
\eta_R(\mu_0)=\zeta^{16},\qquad
\eta_R(\mu_1)=\zeta^8,\qquad
\eta_R(\mu_1\mu_0^{-1})=\zeta^{11}.
\tag{2}
\]

这些是带方向的 mark；本卡不把它们降为未标记的 carrier 余数。

## 2. 同模数候选与共享 \(19\) 账本

取

\[
\begin{aligned}
D=D_*&=6303=3\cdot11\cdot191,&
A&=573=3\cdot191,\\
s&=AD_*=3611619,&
M_*&=4D_*=25212.
\end{aligned}
\tag{3}
\]

有 \(A\mid D_*\)、\(D_*/A=11\) 平方自由，且

\[
4s=14446476<p.
\tag{4}
\]

取两个来源参数

\[
a_0=3,\qquad a_1=573,\qquad b_i=Da_i.
\tag{5}
\]

它们也都通过相应的除子、平方自由和范围条件，且

\[
\begin{aligned}
b_0&=18909,&
p+4b_0&=19\cdot45667\cdot1385749,\\
b_1&=s,&
N=p+4s&=17\cdot19^3\cdot53^2\cdot3671.
\end{aligned}
\tag{6}
\]

因此来源高度为 \(e_0=1,e_1=3\)。又

\[
s-b_0=3592710
=2\cdot3^2\cdot5\cdot11\cdot19\cdot191,
\tag{7}
\]

在允许来源 \(q\)-层逐层标记拆分的 shared-ledger 合同下，共同账本精确给

\[
\ell_0=1,\qquad
\ell_1=3,\qquad
L_{19}=4,\qquad
V_{19}=3,\qquad
\boxed{d_{19}=3.}
\tag{8}
\]

这只给出一个候选参数纤维内的可回译幂块

\[
\{1,19,19^2,19^3\}\subset U(25212),
\tag{9}
\]

而不是把两个来源误记成四个可独立收费的 \(19\)-层。该集合中
\(\operatorname{ord}_{25212}(19)=190\)，其集合稳定子为平凡群；这些只是有限群数据，
并不自动给出三条 Q-PREFIX 请求、三个 physical slot 或容量价格。

## 3. 候选余因子与相位对应

令

\[
H_0=53\cdot3671=194563,\qquad H_1=19H_0=3696697.
\tag{10}
\]

两者都整除 \(N\)，并且 \(H_0 19^e\mid N\)（\(0\le e\le3\)）。在
\(U(25212)\) 上定义

\[
\chi(x)=x^{10}\pmod {191}.
\tag{11}
\]

则

\[
\chi(H_0)=121=\zeta^{16},\qquad
\chi(19)=52=\zeta^{11},\qquad
\chi(H_1)=180=\zeta^8.
\tag{12}
\]

和 (2) 相比，得到精确的两点角色对应

\[
\chi(H_0)=\eta_R(\mu_0),\qquad
\chi(H_1)=\eta_R(\mu_1),\qquad
\chi(19)=\eta_R(\mu_1\mu_0^{-1}).
\tag{13}
\]

所以同一个候选纤维已经有一条相位兼容的 \(19\)-高度链：\(H_0\) 与 \(H_1\) 只使用
其中相邻的一层，额外两层仍须由独立 request/slot allocation 说明，不能静默附着到
\(\mu_1\)。

[第三条 C=38 实际 raw 叶](type-I-g-anchor-c3-adaptive-core19-v5-c38-q19-phase-leaf.md)
现已给出与 \(\chi(H_0 19^3)\) 同 character class 的第三个实际 occurrence。它补强的是
raw phase evidence，但不从 raw word 恢复 \(v_{19}(H_0 19^3)=3\)；这些因子仍嵌套在
同一个 candidate record，不能被直接收费为三条 request 或三个 physical slot。

## 4. 这个纤维为什么仍不终止

若这个固定 \((D_*,A)\) 纤维给出 Type II 短证书，则必须有

\[
h\mid N,\qquad h\equiv-1\pmod {25212}.
\tag{14}
\]

目标满足 \(\chi(-1)=1\)。对所有 \(48\) 个因子

\[
h=17^\alpha19^\beta53^\gamma3671^\delta\mid N
\tag{15}
\]

的精确有限枚举中，\(\chi(h)=1\) 的只有

\[
1,\qquad 19\cdot53^2=53371,\qquad
19^2\cdot53\cdot3671=70237243.
\tag{16}
\]

三者均为 \(1\pmod3\)，而 \(-1\equiv2\pmod3\)。所以 (14) 无解。这是此固定
候选纤维的 terminal boundary，不是否定其它 \(D_*,A\) 或其它 Type II 证书。

[D=6303 完整候选纤维边界](type-I-g-anchor-c3-adaptive-core19-v5-d6303-complete-fiber-boundary.md)
进一步穷尽了固定 \(D=6303\) candidate-record 格内的全部八个 \(A\)；其余七行同样不命中
target。因此这里的 target 缺失不是只属于 \(A=573\) 的偶然相位现象。

## 5. 严格边界

\(H_0\) 不整除 \(p+4b_0\)；两条相位匹配余因子都来自候选 \(N=p+4b_1\)，且
\(H_1=19H_0\) 共享 support。因此 (13) 是 character 层的有限对应，不是两条
raw 谱系各自拥有独立 physical source slot 的证明。

仍缺少完整 raw transition/source universe、从每个带方向 raw mark 到
\((a,b,H)\) 的 functor、逐项 \(H\mid p+4b\) 的 provenance、独立 slot、第三条
request 的前缀分配、target-odd carrier、demand-to-slot、E4/E5 和 terminal-first
clearance。特别地，v=5 本身已由既有 \((m,d)=(3,11)\) Type II 证书抢占，不能登记
selector edge。
