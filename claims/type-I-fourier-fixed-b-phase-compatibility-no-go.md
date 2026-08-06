---
kind: claim
claim_id: type-I-fourier-fixed-b-phase-compatibility-no-go
title: Fourier 与固定 B 清分相位的冲突—非互素吸收二分
statement: 设奇素数 q 满足 v_q(B)=v_q(K)+e 且 e>0。若 F 状态的规范 q-primary Fourier 相位为 gamma_F，而固定 B 算术清分相位为 gamma_B=-A R^{-1} (mod q^e)，则同一固定 B 图表的 phase-lift 只有三种结果：gamma_F 不等于 gamma_B 时输出 FOURIER_FIXED_B_PHASE_CONFLICT；两相位相等时所有标签落在唯一模 q^e 剩余类，且每个清分分子候选都满足 q^e | gcd(A+Rs,B)，约分后 q 缺陷严格降为零；若 (A,B,R) 的算术 source map 未封闭，则输出 FOURIER_FIXED_B_SOURCE_UNCLOSED。故同一固定 B 图表不能同时保留 q 缺陷、保持互素性并产生递归 phase-lift 边。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fourier-qprimary-phase-lift-capacity-dichotomy
  - type-I-f-denominator-clearing-qadic-lift-contract
  - type-I-f-qadic-numerator-lift-rigidity-and-gcd-reduction
topics:
  - type-I
  - F-state
  - finite-fourier
  - q-primary
  - fixed-B
  - phase-compatibility
  - numerator-lift
  - gcd-reduction
  - descent
  - proof-program
sources:
  - claim: type-I-fourier-qprimary-phase-lift-capacity-dichotomy
    role: Fourier-q-primary-phase
  - claim: type-I-f-denominator-clearing-qadic-lift-contract
    role: arithmetic-clearing-phase
  - claim: type-I-f-qadic-numerator-lift-rigidity-and-gcd-reduction
    role: fixed-B-gcd-absorption
visibility: public
last_checked: '2026-08-05'
---

# Fourier 与固定 \(B\) 清分相位的冲突—非互素吸收二分

## 1. 两个相位

固定一个 F 型目标表示的有向形式

\[
4K=pR+1,\qquad A+B=Rm_0,\qquad (A,B)=1,
\]

并取奇素数 \(q\) 满足

\[
q^\nu\Vert K,\qquad v_q(B)=\nu+e,\qquad e>0.
\tag{1}
\]

因为 \(q\mid B\) 且 \((A,B)=1\)，有 \(q\nmid A\) 和 \(q\nmid R\)。固定 \(B\) 时保持
目标关系的所有整数标签都写成

\[
A_s=A+Rs,\qquad m_s=m_0+s.
\tag{2}
\]

算术清分要求 \(q^{\nu+e}\mid pA_s+m_s\)。由 q-adic 分子刚性，它等价于

\[
s\equiv\gamma_B:=-AR^{-1}\pmod {q^e}.
\tag{3}
\]

另一方面，规范 Fourier 证书的 q-primary 投影给出目标相位

\[
s\equiv\gamma_F\pmod {q^e}
\tag{4}
\]

作为所选 source map 的 phase-lift 条件。式 (4) 是独立的算术映射假设；Fourier
角色本身只产生 \(\gamma_F\)，不自动推出它等于 (3)。

## 2. 精确三分

### 2.1 相位冲突

若

\[
\gamma_F\not\equiv\gamma_B\pmod {q^e},
\tag{5}
\]

则不存在任何整数 \(s\) 同时满足 (3) 和 (4)。因此同一固定 \(B\) 图表不存在同时
保留 Fourier phase-lift 和算术清分的候选，输出

\[
\boxed{\texttt{FOURIER\_FIXED\_B\_PHASE\_CONFLICT}}.
\]

若令 \(k=v_q(\gamma_F-\gamma_B)<e\)，则 \(k\) 是最大兼容层；它可以进入相位树的
\(D_k\) 分裂，但不能被记成完整的 q-height \(e\)。

### 2.2 相位相等但非互素吸收

若

\[
\gamma_F\equiv\gamma_B\pmod {q^e},
\tag{6}
\]

则所有共同候选正好是

\[
s=s_0+q^e t,\qquad t\in\mathbb Z,
\tag{7}
\]

其中 \(s_0\) 是 (3) 的任一代表。由 (2)--(3)，

\[
q^e\mid A_s.
\tag{8}
\]

而 (1) 给出 \(q^{\nu+e}\mid B\)，故

\[
\boxed{q^e\mid\gcd(A_s,B).}
\tag{9}
\]

令 \(D_s=(A_s,B)\)，约分为

\[
a_s=A_s/D_s,\qquad b_s=B/D_s.
\]

则

\[
v_q(b_s)\le(\nu+e)-e=\nu,
\]

所以约分后的负向分母缺陷

\[
\bigl(v_q(b_s)-v_q(K)\bigr)_+=0.
\tag{10}
\]

这不是增加 q-height 后仍保持原状态的递归边，而是把 q 缺陷吸收到非互素中间坐标
后再消除。若 \(D_s\) 含有更多 q 层，(10) 只会更严格。

### 2.3 source map 未封闭

若没有已证明且完备的 \((A,B,R)\) source map，或者候选 \(B\) 不是固定图表中由
目标表示产生的实际整数块，则不能判定 (3)。此时唯一合法回执是

\[
\boxed{\texttt{FOURIER\_FIXED\_B\_SOURCE\_UNCLOSED}}.
\]

不能把 (5) 当作冲突，也不能把 (9) 当作真实算术容量。

## 3. 证明

式 (3) 是固定 \(B\) 的精确差分合同。由

\[
N_s=pA_s+m_s=N+4Ks,\qquad RN_s=4KA_s+B,
\]

在 \(v_q(B)=\nu+e\)、\(q\nmid R\) 下，
\(q^{\nu+e}\mid N_s\) 当且仅当 \(q^e\mid A_s\)，再由
\(A_s=A+Rs\) 得 (3)。因此 (5) 时两同余类没有交点，(6) 时交集正是 (7)。

由 (3) 直接有 \(A+Rs\equiv0\pmod {q^e}\)，得到 (8)；与
\(q^{\nu+e}\mid B\) 合并即得 (9)，再取 q-进赋值得 (10)。证毕。

### 3.1 一个真实固定图表回执

取

\[
(p,R,K)=(193,7,338)=(193,7,2\cdot13^2),
\qquad A=1,\qquad B=13^3=2197.
\]

则 \(A+B=7\cdot314\)，且 \(A/B\equiv-1\pmod7\)。对 \(q=13\) 有
\(\nu=2,e=1\)，自然固定 \(B\) 相位为

\[
\gamma_B=-7^{-1}\equiv11\pmod {13}.
\]

最小相位匹配标签 \(s=11\) 给出

\[
A_s=1+7\cdot11=78,\qquad
m_s=314+11=325,\qquad
13^3\mid193A_s+m_s.
\]

但

\[
\gcd(A_s,B)=\gcd(78,2197)=13,
\qquad
v_{13}(B/13)=2=\nu.
\]

所以该相位匹配确实只产生一个非互素中间点；约分后的 q 缺陷为零。若 Fourier 相位
改为 \(12\pmod {13}\)，则与 \(11\pmod {13}\) 无公共标签，立即落入
FOURIER_FIXED_B_PHASE_CONFLICT。

## 4. 跨状态容量的正确使用方式

对一族状态 \(i\)，若都已通过独立 source map 证明

\[
\gamma_{F,i}\equiv\gamma_{B,i}\pmod {q^{e_i}},
\]

则其固定 \(B_i\) 标签各自落入唯一模 \(q^{e_i}\) 类，可以使用相位树容量；但该容量
只约束非互素中间标签的数量。约分后每个状态的 q 缺陷已归零，不能把原 \(e_i\) 再次
记作可递归的 q 进载体需求。

反之，若某些状态满足 (5)，它们只能在相容层 \(k<e_i\) 上参与相位胞；完整 q 层
必须转入 alternate \(B\)、换模数、Type II 或其它 source map。这样可以避免把
“相位相容”误读成“同图表递降”。

## 5. 对统一选择器的结论

该二分排除了一个具体的错误桥接：

\[
\text{Fourier phase}
\Longrightarrow
\text{固定 }B\text{ 的互素 q-height recursive edge}
\]

并非自动成立。对同一固定 \(B\)，全称上只有：相位冲突、非互素吸收，或 source map
未封闭。真正仍未解决的是：

1. 证明某个 alternate \(B\)/换图表相位映射在所有 F 状态中完备；
2. 证明相位冲突的剩余层能进入 Type II 短证书；或
3. 在约分后的 \(a_s,b_s\) 上建立满足 E1--E5 的新状态和严格下降。

因此本卡给出的是一个无条件的局部 no-go 与缺口分类，不声称已经完成原猜想的全称
选择器。
