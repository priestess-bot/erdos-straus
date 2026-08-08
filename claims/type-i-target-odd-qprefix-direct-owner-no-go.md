---
kind: claim
claim_id: type-i-target-odd-qprefix-direct-owner-no-go
title: target-odd Fourier 的奇 q-prefix 直接 owner 不可对齐引理
statement: 设 q 为奇素数且 q 不整除核心素数 p。若一个 Type-I F 状态的目标 t=-1 q-primary 角色投影来自 t 的无界预像，则其相位 gamma 必为 0 (mod q^e)；而任何真实 q-prefix owner s 必须满足 s=-p*4^{-1} (mod q^e)，这是非零单位类。因此该角色请求不可能通过 identity owner map s=gamma 进入 q-prefix 容量，必须转入非零仿射偏移、其它 source relation、严格障碍或二进/其它图表路线。p=73,R=27 的真实 F 状态在 q=3,e=2 上给出 gamma=0、beta=2 (mod 9) 的明确冲突。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-i-empty-fiber-target-odd-source-demand
  - type-I-f-target-involution-fourier-phase-collapse
  - type-I-qprimary-phase-prefix-intersection-capacity
  - type-I-fg-fourier-phase-owner-capacity-bridge
topics:
  - type-I
  - F-state
  - target-odd
  - q-primary
  - q-prefix
  - owner-map
  - arithmetic-obstruction
  - source-map
  - capacity
  - proof-program
sources:
  - claim: type-i-empty-fiber-target-odd-source-demand
    role: target-odd-q-demand
  - claim: type-I-f-target-involution-fourier-phase-collapse
    role: involution-phase-zero
  - claim: type-I-qprimary-phase-prefix-intersection-capacity
    role: prefix-center-and-conflict
  - reproduction: reproductions/type_i_target_odd_qprefix_direct_owner_no_go.py
    role: p73-q3-conflict
visibility: public
last_checked: '2026-08-09'
---

# target-odd Fourier 的奇 \(q\)-prefix 直接 owner 不可对齐引理

## 输入

设 \(p\equiv1\pmod {24}\) 为核心素数，\(q\) 为奇素数且 \(q\nmid p\)。
固定一个 F 型 Type-I 图表的目标

\[
t=-1
\]

和一个来自 \(t\) 的无界群论预像的 q-primary 角色相位

\[
\gamma\in\mathbb Z/q^e\mathbb Z,\qquad e\ge1.
\]

这里的 \(\gamma\) 是 target-odd 角色的 q-primary 投影在目标预像上的相位：
若原角色阶为 \(q^e d'\)、\((q,d')=1\)，且 \(\chi(t)=-1\)，则
\(\gamma\) 由 \(\chi^{d'}(z_0)\) 定义，其中 \(\phi(z_0)=t\)。

另一方面，奇 q 的真实 q-prefix owner 标签 \(s\) 必须满足

\[
q^e\mid p+4s.
\tag{1}
\]

所谓 identity owner lift，是现有 phase-owner 桥要求的同一标签同余

\[
s\equiv\gamma\pmod {q^e}.
\tag{2}
\]

## 不可对齐定理

### 1. 目标 q-primary 相位必为零

由于 \(t^2=1\)，有

\[
2\gamma\equiv0\pmod {q^e}.
\tag{3}
\]

因 \(q\) 为奇数，2 在 \(\mathbb Z/q^e\mathbb Z\) 中可逆，故

\[
\boxed{\gamma\equiv0\pmod {q^e}.}
\tag{4}
\]

### 2. q-prefix owner 必为非零类

由 \(q\nmid4\)，条件 (1) 等价于

\[
s\equiv\beta_e(p):=-p\,4^{-1}\pmod {q^e}.
\tag{5}
\]

因为 \(q\nmid p\)，\(\beta_e(p)\) 是单位类，特别地

\[
\beta_e(p)\not\equiv0\pmod {q^e}.
\tag{6}
\]

### 3. 直接 owner lift 为空

(2)、(4) 要求 \(s\equiv0\)，而 (1)、(5) 要求
\(s\equiv\beta_e(p)\ne0\)。因此不存在任何整数 \(s\) 同时满足二者：

\[
\boxed{
\{s:q^e\mid p+4s,\ s\equiv\gamma\pmod {q^e}\}
=\varnothing.
}
\tag{7}
\]

这不是区间边界或候选菜单截断，而是模 \(q^e\) 上的结构性冲突。若 source-map
明确声明只允许 identity owner lift，应输出

\[
\mathrm{TARGET\_ODD\_QPREFIX\_DIRECT\_OWNER\_CONFLICT}
\]

或等价的 PHASE_PREFIX_CONFLICT，不得把这个角色请求计入 q-prefix 容量。

## 证明

(3) 是目标对合的 q-primary 相位约束：\(\chi^{d'}(t)=1\) 或其目标预像相位
平方为单位，均给出 \(2\gamma=0\)。奇 q 使 2 可逆，得到 (4)。式 (5) 由 4 在
\(\mathbb Z/q^e\mathbb Z\) 中可逆直接得到；\(q\nmid p\) 给出 (6)。于是两个同余类
不相交，得到 (7)。证毕。

## 正确的后续路由

引理只排除最简单的 identity owner map，不排除所有算术承接。合法后续必须明确属于
下列之一：

1. **非零仿射 source-map：**
   \[
   s\equiv u\gamma+c\pmod {q^e},\qquad c\not\equiv0,
   \]
   并用 gcd—区间或 phase-prefix 交集公式证明标签存在；
2. **其它 source relation：** 目标 q-primary 角色不直接解释为 owner 标签，而是
   通过两块 SNF、CRT、raw lineage 或 Type-II source record 重新定义相位；
3. **严格负证书：** identity owner universe 已声明完备时，(7) 是
   FOURIER_PHASE_NO_LOCAL_LIFT，后续必须转向支撑分离、关系格或良基下降；
4. **二进分支：** \(q=2\) 时 4 不可逆，(5) 不成立；必须使用广义 \(2^j\) 终端、
   dyadic normalization 或独立 2-adic source map，不能把奇 q no-go 外推到 q=2。

因此 target-odd 奇 q 请求不能直接占用已有 \(\beta_e(p)\)-centered owner 槽；任何
容量收费都需要先改变标签语义并通过新的整数合同。

## 真实控制：\(p=73,\ R=27\)

对

\[
K=\frac{73\cdot27+1}{4}=493=17\cdot29
\]

取 \(2\) 为 \(U(27)\) 的生成元。目标 \(-1=2^9\)，而 \(q=3\) 的 q-primary
分量来自阶 \(18=3^2\cdot2\) 的角色 \(\chi(2)=e^{2\pi i/18}\)。其目标相位为

\[
\gamma=2\cdot9\equiv0\pmod9.
\]

另一方面，

\[
\beta_2(73)=-73\cdot4^{-1}
\equiv-1\cdot7
\equiv2\pmod9.
\]

所以 \(q^2\mid73+4s\) 的所有标签均满足 \(s\equiv2\pmod9\)，与 target-odd
直接相位 \(s\equiv0\pmod9\) 完全不交。该冲突发生在真实 F 空纤维的
target-odd q=3 请求上，不是抽象群控制。

同一角色的 q=2 投影不受本引理约束：4 在 2-primary 模数上不可逆，正是应转入
广义 \(2^j\) / dyadic 路线的边界。

## 选择器意义

对空 F 纤维的 target-odd q 请求，当前统一选择器应先运行：

\[
\text{target-odd q request}
\to
\begin{cases}
\text{奇 }q:\ \mathrm{TARGET\_ODD\_QPREFIX\_DIRECT\_OWNER\_CONFLICT},\\
q=2:\ \text{dyadic source/terminal gate},\\
\text{有非零 affine/source relation: phase-prefix/SNF/owner gate}.
\end{cases}
\]

该引理消除了一个看似自然但实际上不可能的容量入口；它没有证明每个核心素数都已有
其它合法出口，也没有把冲突自动升级为严格递降。全称目标的剩余内容是：证明这些奇 q
冲突能够由其它 source relation、F/G 支撑分离、Type-II 直接证书或 E1--E5 严格后继
承接，而不是再次把 \(\gamma=0\) 当作 owner 槽。

## 聚焦复现

~~~bash
python3 reproductions/type_i_target_odd_qprefix_direct_owner_no_go.py --verify
~~~
