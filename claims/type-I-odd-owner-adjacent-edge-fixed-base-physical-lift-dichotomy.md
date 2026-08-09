---
kind: claim
claim_id: type-I-odd-owner-adjacent-edge-fixed-base-physical-lift-dichotomy
title: 奇阶相邻 owner 边的共同固定基塌缩、终端与源秩障碍
statement: >-
  固定奇素数 q、j>=1 和核心素数 p，并设 Q=q^j。任一来源合格的相邻
  Q-owner 边 (s,s+Q) 都满足 gcd(s,s+Q)=1；因此把两个端点同时写成同一
  Type II 固定源基 D_0 的整数行时必有 D_0=1，除子格目标也只剩
  D_*=A=x=1。该目标的 exact-Q source CRT 可解当且仅当 beta_j(p)=1，等价于
  Q|p+4。可解只证明目标处有真实 Q 因子 occurrence；由于 U(4) 的阶为 2，任意
  奇 q 的非零 F_q 源列到该目标单位群的直接同态 lift 必为零，不能据此宣称
  source-class token、物理流或 Rado 已通过。独立于该边的 D=1 raw 单因子菜单恰为
  h|p+4、h=3 (mod 4)，且必须 terminal-first 检查：菜单非空即给出 Type II
  短证书；菜单为空当且仅当 p+4
  的每个素因子均为 1 (mod 4)，此时同时得到该 D=1 单因子菜单为空、无 D-除子
  下降和无直接目标 U(4) q-primary lift 的严格障碍。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-odd-owner-incidence-edge-source-preserving-capacity
  - type-II-source-lattice-fibered-kneser-selector
  - type-II-owner-primary-mask-arithmetic-lift-criterion
  - type-II-raw-ray-certificate
topics:
  - type-I
  - type-II
  - odd-owner
  - adjacent-edge
  - fixed-source-base
  - source-CRT
  - physical-occurrence
  - q-primary
  - normal-form
  - strict-obstruction
  - proof-program
sources:
  - claim: type-I-odd-owner-incidence-edge-source-preserving-capacity
    role: provenance-qualified-edge-and-additive-source-column
  - claim: type-II-source-lattice-fibered-kneser-selector
    role: fixed-base-source-CRT-and-divisor-lattice
  - claim: type-II-owner-primary-mask-arithmetic-lift-criterion
    role: E1-E5-gate-order-and-source-contract-boundary
  - claim: type-II-raw-ray-certificate
    role: D1-Type-II-normal-form
  - reproduction: reproductions/type_i_odd_owner_adjacent_edge_fixed_base_physical_lift_dichotomy.py
    role: p73-terminal-p1033-source-rank-no-go-p241-terminal-priority-and-p97-CRT-controls
visibility: public
last_checked: '2026-08-09'
---

# 奇阶相邻 owner 边的共同固定基塌缩、终端与源秩障碍

## 1. 相邻端点强制共同固定基为 1

固定奇素数 \(q\nmid p\)、\(j\ge1\)，记

\[
Q=q^j,
\qquad
\beta=\beta_j(p)\in\{1,\ldots,Q-1\},
\qquad
p+4\beta\equiv0\pmod Q.
\tag{1}
\]

设标准 owner 窗口中有一条已经通过来源门的相邻边

\[
\Pi=(s_0,s_1;\text{named provenance}),
\qquad
s_1=s_0+Q,
\qquad
s_i\equiv\beta\pmod Q.
\tag{2}
\]

来源门采用
[奇阶 owner 关联边的来源保持规范化与精确一维秩容量](type-I-odd-owner-incidence-edge-source-preserving-capacity.md)
的定义：\(\Pi\) 保存带名记录、整数构造规则和相位标量，并在 additive incidence
商中已有规范源列

\[
u(\Pi)=1\in\mathbb F_q.
\tag{3}
\]

由 \(Q\mid p+4s_0\) 及 \(q\nmid p\)，有 \(q\nmid s_0\)。因此

\[
\boxed{
\gcd(s_0,s_1)=\gcd(s_0,s_1-s_0)
=\gcd(s_0,Q)=1.}
\tag{4}
\]

若要求两个 endpoint occurrence 同时进入一个固定 Type II 源基，写成

\[
s_i=D_0a_i,
\qquad a_i\in\mathbb N,
\qquad i=0,1,
\tag{5}
\]

这里的 \(D_0\) 是 source-lattice 合同中的**共同算术行基**：只要求
\(Q\mid p+4D_0a_i\)，不要求 \(a_i\mid D_0\)，也不把 \((D_0,a_i)\) 称为两个
endpoint 的规范 Type II 状态。若另采用更强的 \(a_i\mid D_0\) 状态语义，则
\(s_1>1\) 时根本没有共同状态，而不是得到下面的唯一 \(D_0=1\) 行基。

在上述广义 source-row 语义下，\(D_0\mid\gcd(s_0,s_1)\)，所以

\[
\boxed{D_0=1,\qquad(a_0,a_1)=(s_0,s_1).}
\tag{6}
\]

Type II source-switch 的除子格候选满足

\[
D_*\mid D_0,
\qquad A\mid D_*,
\qquad x=AD_*.
\tag{7}
\]

故共同固定基菜单只有

\[
\boxed{D_*=A=x=1.}
\tag{8}
\]

式 (4)--(8) 穷尽所有同时满足 (5) 且沿 \(D_*\mid D_0\) 运行的相邻边合同；它们
不是规范分解的偶然选择。

## 2. exact-\(Q\) source CRT 的充要条件

两个 source row 都满足

\[
Q\mid p+4D_0a_i=p+4s_i.
\tag{9}
\]

对唯一目标 (8)，E2 的 source CRT 是

\[
x=AD_*\equiv D_0a_i=s_i\pmod Q
\qquad(i=0,1).
\tag{10}
\]

两个余数同为 \(\beta\)，故

\[
\boxed{
\text{共同固定基 exact-}Q\text{ CRT 可解}
\iff \beta_j(p)=1
\iff Q\mid p+4.}
\tag{11}
\]

若 \(\beta\ne1\)，唯一候选 (8) 的 E2 必要同余行失败，输出

~~~text
ADJACENT_EDGE_FIXED_BASE_QJ_SOURCE_CRT_OBSTRUCTED
  common_source_base = 1
  only_target = (D_*, A, x) = (1, 1, 1)
  required_residue = beta_j(p)
  failed_row = 1 != beta_j(p) (mod q^j)
~~~

这是完整固定基除子菜单上的严格障碍，不是抽样未命中。
它只排除当前 \(Q=q^j\) 层；即使 \(\beta_j(p)\ne1\)，仍可能有
\(q^e\mid p+4\)（\(e<j\)），不能把较低嵌套层一并删除。并且任何独立于 \(\Pi\)
的直接 Type I/II 终端都必须在登记该障碍之前预检。

## 3. CRT 正分支只有物理 occurrence，不自动产生 source token

现在设 \(\beta=1\)。由 (11)，目标处确有真实整数因子

\[
Q=q^j\mid p+4.
\tag{12}
\]

所以可以登记一个深度至少为 \(j\) 的嵌套 occurrence：

~~~text
ADJACENT_EDGE_FIXED_BASE_QJ_PHYSICAL_OCCURRENCE
  target = (D_*, A, x) = (1, 1, 1)
  factor = q^j in p+4
  E2_SOURCE_CRT = pass
  E3_RANGE = pass
~~~

若 \(v_q(p+4)>j\)，这不是 exact-height-\(j\) 的独立槽；不同 \(j\) 的前缀必须由
shared-\(q\) 账本嵌套去重，不能重复收费。

但 (12) 不能把 additive incidence 源列 (3) 直接附着到该因子。目标乘法环境是

\[
U(4D_*)=U(4)\simeq C_2.
\tag{13}
\]

对奇 \(q\)，两个方向的群同态都为零：

\[
\operatorname{Hom}(C_q,U(4))
=\operatorname{Hom}(U(4),C_q)=0.
\tag{14}
\]

这是因为任一像的阶同时整除 \(q\) 和 2。等价地，\(U(4)\) 的
\(q\)-primary source rank 为零。因此

\[
\boxed{
u(\Pi)\ne0
\quad\not\Longrightarrow\quad
\text{a nonzero physical source column at }D_*=1.}
\tag{15}
\]

这给出严格的直接同态障碍

~~~text
DIRECT_TARGET_U4_Q_PRIMARY_LIFT_OBSTRUCTED
  additive_source_rank = 1
  target_unit_group_order = 2
  target_q_primary_rank = 0
~~~

如果要绕过 (14)，必须另行构造一个非同态的整数 factor-toggle/source-class 合同，
逐项证明：选与不选该 factor 都保持同一来源关系，完整边签名确实决定一个物理副本，
并且所有允许的 0/1 组合都可回译。仅把 \(\Pi\) 与 (12) 并列成一个 tuple 不构成
E1，也不能宣称 token flow、slot flow 或 Rado 已通过。

更一般地，经目标单位群或其商保存非零 \(q\)-source rank 的必要条件是

\[
\boxed{q\mid\lvert U(4D_*)\rvert=\varphi(4D_*).}
\tag{16}
\]

相邻共同固定基已由 (8) 强制 \(D_*=1\)，所以永远不满足 (16)。这把下一搜索对象
收紧为：具有非平凡 endpoint gcd 的非相邻边、异质源基/换状态，或带完整整数回译的
非同态 factor-toggle。

## 4. \(D=1\) raw 单因子菜单的完备二分

源秩 lift 失败并不妨碍 terminal-first 直接结束原素数。独立于 \(\Pi\) 及
\(\beta_j\)，定义

\[
\mathcal H_1(p)=
\{h>1:h\mid p+4,\ h\equiv-1\pmod4\}.
\tag{17}
\]

若 \(h\in\mathcal H_1(p)\)，令

\[
K_h=\frac{h+1}{4},
\qquad
B_h=\frac{K_hp+1}{h}.
\tag{18}
\]

因为

\[
4(K_hp+1)=(h+1)p+4\equiv p+4\equiv0\pmod h
\tag{19}
\]

且 \((h,4)=1\)，\(B_h\) 是整数。又

\[
B_h-1=\frac{K_h(p-4)+2}{h}>0.
\tag{20}
\]

所以 \((A,C,K,B)=(1,1,K_h,B_h)\) 是 raw Type II 证书，并给出

\[
\boxed{
\frac4p
=\frac1{B_h}+\frac1{pK_h}+\frac1{pB_hK_h}.}
\tag{21}
\]

反向地，\(D=A=C=1\) 的 raw-ray 单因子有 \(h=4K-1\) 且
\(h\mid Kp+1\)。乘以 4 得 \(h\mid p+4\)，所以它必在 (17) 中。因此 (17)
是该族的完整菜单。

由于 \(p\equiv1\pmod4\)，\(p+4\) 为奇数且是 \(1\pmod4\)，并有

\[
\boxed{
\mathcal H_1(p)=\varnothing
\iff
\text{每个素因子 }r\mid p+4\text{ 都满足 }r\equiv1\pmod4.}
\tag{22}
\]

若有素因子 \(r\equiv3\pmod4\)，\(r\) 本身在菜单中；反之，全部素因子为
\(1\pmod4\) 时每个除数也为 \(1\pmod4\)。特别地，若 (11) 成立且
\(q\equiv3\pmod4\)，可直接取 \(h=q\) 得到 Type II 终端，不论 \(j\) 的奇偶。

若菜单为空，则 \(D_0=1\) 没有真除数供 E5 使用。结合 (12)、(15) 和 (22)，得到

~~~text
D1_QJ_OCCURRENCE_NO_D1_SINGLE_FACTOR_RAW_OR_DIRECT_U4_Q_LIFT
  physical_qj_occurrence = verified
  direct_target_U4_q_primary_rank = 0
  D1_single_factor_raw_menu = empty
  strict_D_divisor_descent = impossible
  external_integer_factor_toggle = unproved
~~~

这是严格障碍回执，不是递归边。式 (17) 必须在 (11) 的负分支之前检查；只有
\(\mathcal H_1(p)=\varnothing\) 时，选择器才继续输出当前边的 CRT 或 q-primary
障碍。

## 5. 四个算术控制

### \(p=73,q=11,j=1\)：terminal-first 预占源秩障碍

这里

\[
\beta_1(73)=1,
\qquad(s_0,s_1)=(1,12),
\qquad73+4=77.
\]

所以 exact-11 CRT 与物理 occurrence 都存在。虽然 \(U(4)\) 仍不能承载非零
\(\mathbb F_{11}\) 源列，但 \(11\equiv3\pmod4\) 使 raw 菜单直接命中。取

\[
h=11,\qquad K=3,\qquad B=20
\]

得到

\[
\frac4{73}=\frac1{20}+\frac1{219}+\frac1{4380}.
\]

因此选择器应先返回 Type II terminal，而不是继续请求 source-rank lift。该控制只
验证条件算术分支；这里没有另行声称 owner-row 编号已经构成外部 F/G provenance。

### \(p=1033,q=17,j=1\)：physical occurrence 不蕴含源容量

有

\[
1033+4=1037=17\cdot61,
\qquad17\equiv61\equiv1\pmod4,
\]

相邻 owner 为 \((1,18)\)，故 exact-17 CRT 和真实 17 occurrence 都存在。但

\[
\operatorname{Hom}(C_{17},U(4))
=\operatorname{Hom}(U(4),C_{17})=0,
\qquad
\mathcal H_1(1033)=\varnothing.
\]

同时 \(D_0=1\) 无真除数。这是对“真实 q 因子 occurrence 自动支付 additive
q-source rank”的严格整数反控制；它不否定 \(p=1033\) 的其它 Type I/II 证书。
例如另一个状态已有 raw 参数
\((A,C,K,h,B)=(1,3,1,11,94)\)，所以这里的空结论严格限于 (17) 的
\(D=A=C=1\) 单因子菜单。

### \(p=241,q=5,j=2\)：终端必须先于高层 CRT 障碍

标准相邻 25-owner 为 \((21,46)\)，且 \(\beta_2(241)=21\ne1\)，所以若只看当前
层会得到 exact-25 E2 障碍。但

\[
241+4=245=5\cdot7^2,
\qquad7\in\mathcal H_1(241),
\]

故选择器必须先取 \(h=7\) 的 \(D=1\) Type II 终端。该例同时说明
\(\beta_2\ne1\) 不排除较低的 \(5\mid p+4\) occurrence。

### \(p=97,q=11,j=1\)：强 provenance 仍在 E2 失败

已有反演记录给出来源合格边 \((6,17)\) 和规范源列 1，但

\[
\beta_1(97)=6,
\qquad97+4=101\not\equiv0\pmod {11}.
\]

共同固定基和目标仍唯一为 \(D_0=D_*=A=x=1\)，而 E2 要求

\[
1\equiv6\pmod {11}.
\]

所以该边在物理 occurrence 之前即得到固定基 source-CRT 障碍。\(p=97\) 已有独立
\(h=7\) Type II 终端，但它不提升当前 11-owner 角色。

## 6. 统一选择器分派与边界

对来源合格的相邻奇阶 owner 边，固定基分派现在是

~~~text
terminal-first precheck
  -> H_1(p) nonempty: D1_TYPE_II_RAW_SHORT_CERTIFICATE
  -> H_1(p) empty:
       adjacent qualified edge
         -> gcd(endpoint labels) = 1
         -> common arithmetic row base D0 = 1
         -> beta_j(p) != 1
              : ADJACENT_EDGE_FIXED_BASE_QJ_SOURCE_CRT_OBSTRUCTED
         -> beta_j(p) = 1
              : QJ_PHYSICAL_OCCURRENCE
                + DIRECT_TARGET_U4_Q_PRIMARY_LIFT_OBSTRUCTED
              : D1_QJ_OCCURRENCE_NO_D1_SINGLE_FACTOR_RAW_OR_DIRECT_U4_Q_LIFT
~~~

该结果没有构造新的 physical source-class token。它关闭的是相邻边的共同固定算术行基
菜单，并证明最自然的 \(D_*=1\) 目标无法承载奇阶源秩；非相邻边可能有非平凡
endpoint gcd，异质源基和换状态也不受负分支排除。两个独立请求仍受既有 transverse
rank-capacity 1 的限制。
