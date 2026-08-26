---
kind: claim
claim_id: t6-q-one-phase-root-independent-math-replay-v1
title: q=1 G 到 full-carrier phase-root 的独立非授权数学重放
statement: >-
  对任意通过严格输入检查的 source/candidate/projection 三元组，独立重放器仅从其中的原始整数
  与 X 的完整素因子分解重新证明：p 是 1 mod 24 的素数；source 是 ordinary q=1 G；
  X=(p+3)/4、t=(p-1)/24、R_X=16t+3、K_X=X(16t+1)；(R_X,K_X)
  是低区间内唯一满足 X|K 的合法 Type-I chart；显式 fresh source 经唯一写定的 p-edge
  到达 (1,R_X-1,1)；source 与 canonical Type-I projection 同为 Sol(p) mark，故有恒等
  lift；规范 T5 七元向量由 TYPEII_G_HANDOFF 的 phase 3 严降到 TYPEI 的 phase 2。
  输出严格标为 EVIDENCE_ONLY_MATH_REPLAY，terminal_authority 与 role_authority 均为
  BLOCKED，issuance_allowed=false。本结果不证明 actual occurrence、complete terminal、
  角色分离、Gate 2、后续 Type-I totality、T6 或 Erdos--Straus 猜想。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
  - T6
  - q-one
  - G-state
  - type-I
  - full-carrier
  - independent-replay
  - identity-lift
  - well-founded-potential
  - proof-boundary
sources:
  - reproduction: scripts/t6_q_one_phase_root_independent_math_replay_v1.py
    role: independent exact-integer replay with no runtime or historical reproduction imports
  - reproduction: tests/test_t6_q_one_phase_root_independent_math_replay_v1.py
    role: hard-coded positive controls and p/G/root/chart/source/mark/potential negative swaps
  - claim: type-II-q-one-full-carrier-phase-root-entry
    role: comparison target only, not imported or used as a replay premise
visibility: public
last_checked: '2026-08-26'
---

# q=1 G 到 full-carrier phase-root 的独立非授权数学重放

## 1. 输入与独立性

重放器只接受三个 exact-field JSON object：

1. `source`：方程整数、q=1 gap-3 数据、X 的完整有序素因子分解、ordinary mark 和分支内类型标签；
2. `candidate`：t、X、候选 chart、support 及 fresh raw source/p-edge 的全部整数；
3. `projection`：目标方程、mark、Type-I typed 字段、分支内类型标签与 source/target T5 七元向量。

所有标量都必须是 plain integer；布尔值不能冒充整数，浮点数、重复 JSON key、未知字段和
输入侧 authority 字段均 fail closed。模块不导入或调用 q=1 runtime slice、其中的
producer/projector/validator/scheduler，也不导入历史 reproduction。旧 phase-root claim 只用于比较
结论边界，不是本重放的证明前提。

## 2. ordinary q=1 G 的重算

重放器先用精确试除确认

\[
p\text{ 为素数},\quad p\equiv1\pmod {24},\quad
t=\frac{p-1}{24},\quad U=\frac{p-1}{4},\quad X=\frac{p+3}{4}=6t+1.
\]

输入因子必须是严格递增素数及正指数，乘积必须恰为 X。仅当每个素因子都满足
\(\ell\equiv1\pmod3\)，且 q、gap、endpoint、phase、provenance 分别精确为
\(1,3,G,\texttt{TYPEII_G_HANDOFF},\texttt{ORDINARY_ENDPOINT}\) 时，source 才被识别为
ordinary q=1 G。因而单独写一个 G 标签不能通过：例如 \(p=97\) 时
\(X=25=5^2\)，因 \(5\equiv2\pmod3\) 必须拒绝。

## 3. full-carrier root 与低 chart 唯一性

由 p 独立重算

\[
R_X=16t+3,\quad K_X=X(16t+1).
\]

直接恒等式给出

\[
4K_X=pR_X+1,\quad X\mid K_X,\quad
3\le R_X\le p-2,\quad 3R_X-1=8X.
\]

反过来，任一合法 Type-I chart \(4K=pR+1\) 都满足 \(R\equiv3\pmod4\)。若再有
\(X\mid K\)，则由 \(p=4X-3\) 得 \(3R\equiv1\pmod X\)。因为 X 为奇数且
\(X\equiv1\pmod3\)，这两个同余由 CRT 唯一确定 R 模 \(4X\)。候选 \(R_X\) 满足它们，
而

\[
R_X-4X<3,\quad R_X+4X>p-2.
\]

所以低区间 \(3\le R\le p-2\) 中只有 \((R_X,K_X)\) 一张 full-carrier chart。该证明
不枚举 chart，也不调用 carrier-rail reproduction。

## 4. fresh source、canonical projection 与恒等 lift

重放器逐项核对

\[
(U_X,V_X,m_X)=\bigl(p,R_X(p-1)-p,p-1\bigr),
\]

\[
U_X+V_X=R_Xm_X,\quad \gcd(U_X,V_X)=1,\quad p\nmid K_X,
\]

以及 shift 1、gcd reduction 1 的 raw p-edge

\[
\left(\frac{U_X}{p},\frac{V_X+R_X}{p},\frac{m_X+1}{p}\right)
=(1,R_X-1,1).
\]

目标 projection 只能是同一 equation rank p、chart \((R_X,K_X)\)、support 1、
`TYPEI/CHARGED/FULL_CARRIER_POST_G/fresh_source_tree_only`。在这一精确 typed shape 下，
本分支预期的 source type label 为 `type_ii_relation_g_endpoint`，target type label 为
`type_i_full_carrier_post_g`；输入声明必须与这两个 branch-local 标签一致。这不是对完整 common
classifier facts 和全局 family precedence 的重放，因而不声称得到 exclusive E3 owner、owner
digest 或 queue owner authority。

source 与 target 都被逐字段确认是同一 \(4/p\) 方程上的 `ROOT_SOL(p)` mark。因此

\[
\operatorname{id}:\operatorname{Sol}(p)\longrightarrow\operatorname{Sol}(p)
\]

是全域恒等 lift。这里没有假设 \(\operatorname{Sol}(p)\) 非空，也没有证明任何 terminal
membership。

## 5. T5 phase drop 与权限边界

输入必须携带并被精确重算为

\[
\Pi(S)=(p,3,0,0,0,0,0),
\]

\[
\Pi(T)=\left(p,2,4,\frac{(p-1)^2}{4},K_X,0,0\right).
\]

字典序的首个严格坐标是 major phase，故 \(\Pi(T)<\Pi(S)\)。这只证明
`PHASE_DROP` 的数学判据；输出中的 `admission_ticket_issued=false`，不能被当作已经签发的 T5
ticket。

最终 receipt 的固定状态为：

```text
status                 = EVIDENCE_ONLY_MATH_REPLAY
terminal_authority     = BLOCKED
role_authority         = BLOCKED
issuance_allowed       = false
admission_ticket_issued = false
```

模块没有 role grant、branch binding、COMPLETE schedule、producer registry、transition issuer、
admission 或 queue API。因此它不闭合 complete-terminal obligation、Gate 2、post-root Type-I
selector、T6 或 Erdos--Straus 猜想。

`receipt_to_mapping_v1` 是经过 typed invariant replay 的序列化边界：在信任 content seal 前，
它重新验证每个 nested exact dataclass、全部 root/source/projection/mark/potential 恒等式以及固定
非授权字段。即使用 `object.__new__` / `object.__setattr__` 绕过 frozen dataclass 并重算 digest，
任何 authority flip、ticket-issued flip 或数学字段 flip 仍被拒绝。三个 input digest 只是通过
原始 replay 时得到的内容绑定；脱离原输入后，它们不是 Git provenance 或角色授权。

## 6. 聚焦验证

硬编码正控制覆盖 \(p=73\) 与多素因子
\(p=76129, X=19033=7\cdot2719\)。负控制分别交换 p、G factorization、root 参数、合法但非
full-carrier 的低 chart、fresh source、mark、T5 potentials、source/target branch type label 与 typed
projection，并单独拒绝伪 G 标签、布尔/浮点冒充、重复 key 和 authority 注入。

```bash
python3 -m unittest tests.test_t6_q_one_phase_root_independent_math_replay_v1 -v
ruff check scripts/t6_q_one_phase_root_independent_math_replay_v1.py \
  tests/test_t6_q_one_phase_root_independent_math_replay_v1.py
python3 -m py_compile scripts/t6_q_one_phase_root_independent_math_replay_v1.py \
  tests/test_t6_q_one_phase_root_independent_math_replay_v1.py
```
