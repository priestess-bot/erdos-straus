---
kind: claim
claim_id: type-I-root-capacity-strict-carry-support-rebase
title: 根容量严格 carry 的 complete-excess 支撑重基与旧投影阻断
statement: >-
  对核心素数 p≡1 (mod 24) 的 proper-root actual endpoint，令
  R-h=ED 是 maximal complete-excess receipt，且原图表满足
  K=A(p-1)、4K=pR+1。定义 M_ex=lcm(A,Q)=AE。则旧支撑的 canonical
  total cofactor 恒为 C_A=p-1，且其 canonical chart 正是原 (R,K)；root
  cofactor 则精确为 C_M_ex=<-E^(-1)>_p。若 terminal-first 后该 carry 严格
  (C_M_ex<=p-2)，则 M_ex>A、M_ex 不整除旧 K，canonical target 必为 overflow，
  并使精确高支撑秩 Lambda_p^sharp 从 (0,p-1) 严格降到 (0,C_M_ex)。反之，
  把原 root chart 送入 support-preserving total-cofactor dispatch 时，其
  determinant 参数为 (M,d,n)=(A,1,(4A+1)/p)，且 t=0，故该 dispatch 必须
  抑制为 stutter。因而严格 root carry 不能由旧 total-cofactor 投影或同图表 support
  promotion 登记；它必须经过现有单侧 complete-excess 语义的一个保留 actual root path
  的 support-rebase serializer。strict receipt 已自动满足 Q>1、p 不整除 Q、
  (Q,beta)=1 和 h beta|K 等单侧算术准入门。该结论支付 E2、图表无关 Sol(4,p)
  语义下的 E4、以及条件性的 E5；它不凭空支付 persistent provenance、typed normal
  form 或 terminal-first priority 的 E1/E3。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-general-endpoint-divisor-gate
  - type-I-overflow-total-cofactor-typed-projection-dispatch
  - type-I-overflow-unbounded-same-chart-promotion-persistence-boundary
  - type-I-overflow-full-product-d-one-a-one-single-endpoint-stutter-guarded-relay
  - denominator-escape-state-contract
topics:
  - type-I
  - overflow
  - root-capacity
  - complete-excess
  - support-rebase
  - canonical-projection
  - strict-carry
  - persistence-gate
  - well-founded-descent
  - proof-boundary
sources:
  - claim: type-I-root-capacity-general-endpoint-divisor-gate
    role: actual-proper-root-receipt-and-canonical-cofactor
  - claim: type-I-overflow-total-cofactor-typed-projection-dispatch
    role: support-preserving-total-cofactor-stutter-rule
  - claim: type-I-overflow-unbounded-same-chart-promotion-persistence-boundary
    role: exact-high-support-rank-and-same-chart-admission-condition
  - claim: type-I-overflow-full-product-d-one-a-one-single-endpoint-stutter-guarded-relay
    role: single-side-path-receipt-and-conditional-macro-contract
  - reproduction: reproductions/type_i_root_capacity_strict_carry_support_rebase.py
    role: fixed-actual-receipt-and-support-rebase-controls
visibility: public
last_checked: '2026-08-14'
---

# 根容量严格 carry 的 complete-excess 支撑重基与旧投影阻断

## 1. 设置

固定核心素数

\[
p\equiv1\pmod {24}.
\]

在一个 actual proper-root endpoint 中，沿用根容量记号

\[
g=\frac{p+1}{2},\qquad
T=p^2r-g,\qquad
A=gT,
\]

\[
K=A(p-1),\qquad
4K=pR+1,
\tag{1}
\]

\[
u=\left(2r+1,\frac{p^2+p+1}{3}\right),\qquad
h=3u,
\qquad z=R-h.
\tag{2}
\]

取相对 (K) 的 actual maximal complete-excess receipt

\[
Q=\prod_{v_q(z)>v_q(K)}q^{v_q(z)},\qquad
\beta=\frac zQ,
\]

\[
g_A=(A,Q),\qquad E=\frac Q{g_A},\qquad D=\beta g_A.
\tag{3}
\]

于是 (ED=z)、(D\mid K)。proper-root 条件给出 (p\nmid E)，并且 root
endpoint 的 canonical cofactor 是

\[
c=\langle-E^{-1}\rangle_p
=\left\langle D(h-1)^{-1}\right\rangle_p.
\tag{4}
\]

以下只讨论 terminal-first 没有已经终止、且 (4) 严格满足

\[
1\le c\le p-2.
\tag{5}
\]

这不是一个任意除子 (D) 的构造；(3) 的 maximality 是结论的必要输入。

## 2. 两个 canonical cofactor 分属不同支撑

### 单侧 receipt 的自动算术门

strict 性先给出 \(E\ne1\)，所以 \(Q>1\)。由下文 (7) 的
\(4A\equiv-1\pmod p\) 可知 \(p\nmid A\)，故 \(p\nmid g_A\)。proper-root 的
\(p\nmid E\) 因而加强为

\[
p\nmid Q.
\tag{5a}
\]

按 maximal definition，\(\beta\mid K\)、\((Q,\beta)=1\)，且 \(Q>1\) 时
\(Q\nmid K\)。根 endpoint primitive 性还给出 \(h\mid K\)、\((h,z)=1\)；因
\(\beta\mid z\)，有 \((h,\beta)=1\)，从而

\[
\boxed{h\beta\mid K.}
\tag{5b}
\]

因此每个 strict proper-root receipt 已满足单侧 path-anchored complete-excess 的全部
**算术** payload 条件。尚未包含在 (5a)--(5b) 中的是该 raw path 是否来自已入队 source，
以及它的 priority、scope、hash 和 typed state 记录。

定义 root receipt 真正携带的新支撑

\[
\boxed{
M_{\rm ex}:=\operatorname{lcm}(A,Q)=\frac{AQ}{(A,Q)}=AE.}
\tag{6}
\]

原 root chart 自身已经是旧支撑 (A) 的 canonical chart。事实上，由 (1)

\[
4A(p-1)\equiv1\pmod p,
\qquad
4A\equiv-1\pmod p.
\tag{7}
\]

所以它的 total cofactor 为

\[
\boxed{C_A:=\langle(4A)^{-1}\rangle_p=p-1,}
\tag{8}
\]

且

\[
A C_A=K,
\qquad
\frac{4AC_A-1}{p}=R.
\tag{9}
\]

另一方面，由 (6)--(7)

\[
4M_{\rm ex}=4AE\equiv-E\pmod p.
\]

因此

\[
\boxed{
C_{M_{\rm ex}}
=\left\langle(4M_{\rm ex})^{-1}\right\rangle_p
=\langle-E^{-1}\rangle_p
=c.}
\tag{10}
\]

这给出严格区分：root cofactor (c) 不是旧 (A) 的 total cofactor，而是
complete-excess 支撑 (M_{\rm ex}) 的 total cofactor。

严格性 (5) 还强制 (E\ne1)，故 (M_{\rm ex}>A)。更强地，取任一

\[
q\mid E.
\]

由 (3)，(q) 在 (Q) 中的指数严格超过 (v_q(K))，而

\[
v_q(M_{\rm ex})=v_q(Q)>v_q(K).
\]

所以

\[
\boxed{M_{\rm ex}\nmid K.}
\tag{11}
\]

式 (11) 排除了把这个动作误登记为旧 chart 的同图表 support promotion。

## 3. 严格重基 target 与精确势下降

以 (10) 的 canonical cofactor 定义

\[
K_{\rm ex}=M_{\rm ex}c,
\qquad
R_{\rm ex}=\frac{4M_{\rm ex}c-1}{p},
\tag{12}
\]

并写

\[
d_{\rm ex}=p-c,
\qquad
n_{\rm ex}=4M_{\rm ex}-R_{\rm ex}.
\tag{13}
\]

由 canonical congruence 直接得到

\[
pR_{\rm ex}+1=4K_{\rm ex},
\qquad
p n_{\rm ex}=4M_{\rm ex}d_{\rm ex}+1,
\tag{14}
\]

且 strict carry 下

\[
2\le d_{\rm ex}\le p-1.
\tag{15}
\]

这个 target 必为 overflow。因为 (r\ge1)，有

\[
4A\ge 2p^3+p^2-2p-1,
\]

从而 (4A-1>p^2)。又 (M_{\rm ex}\ge A)、(c\ge1)，故

\[
pR_{\rm ex}=4M_{\rm ex}c-1\ge4A-1>p^2,
\qquad
\boxed{R_{\rm ex}>p.}
\tag{16}
\]

令

\[
B_p=\frac{(p-1)^2}{4},
\qquad
\Lambda_p^\sharp(S)=
\left(\left\lfloor\frac{B_p}{A_S}\right\rfloor,\frac{K_S}{A_S}\right).
\tag{17}
\]

同一个下界给出 (4A>(p-1)^2)，所以 (A>B_p)，并且

\[
\Lambda_p^\sharp(A;K)=(0,p-1),
\qquad
\Lambda_p^\sharp(M_{\rm ex};K_{\rm ex})=(0,c).
\tag{18}
\]

由 (5)，于是

\[
\boxed{
\Lambda_p^\sharp(M_{\rm ex};K_{\rm ex})
<_\mathrm{lex}
\Lambda_p^\sharp(A;K).}
\tag{19}
\]

因此，一旦 source 本身已是 persistent typed state，strict root carry 的 E5 不再是
算术缺口。

## 4. 两个既有 adapter 为什么都不能替代它

先把原 root chart 改写成 total-cofactor dispatch 使用的 determinant 形式。令

\[
n_0=4A-R=\frac{4A+1}{p}.
\tag{20}
\]

则

\[
pn_0=4A\cdot1+1,
\qquad
R=4A-n_0,
\qquad
K=A(p-1).
\tag{21}
\]

所以它在该 dispatch 中的输入正是

\[
(M,d,n)=(A,1,n_0).
\tag{22}
\]

该 dispatch 的 residual 写作

\[
\frac KA=C_A+pt.
\]

由 (8)，这里恒有

\[
\boxed{t=0.}
\tag{23}
\]

它因此正确地把旧支撑投影抑制为 stutter。把 root 的严格 (c) 偷换进这个
support-preserving adapter，会跳过 (6) 的 actual (Q) receipt，既不满足其 target
定义，也会错误地把 (23) 当成严格下降。

同图表 support-promotion adapter 也不适用，因为它要求新 support 整除不变的
(K)，而 (11) 给出严格相反的结论。因此唯一正确的方向是现有单侧
complete-excess receipt 的 root-specialized serializer，可命名为
`root_capacity_complete_excess_support_rebase`：其 witness 必须携带原始 root raw path、
(3) 的 maximal receipt、(6) 的 lcm charge 与 (12) 的 canonical target。这里不需要
再发明一个新的算术 action；(5a)--(5b) 已将它对齐到既有单侧接口。

在这个 adapter 中，合同项的当前状态精确如下：

| 合同 | 已支付内容 | 仍需具名 adapter 提供的内容 |
|---|---|---|
| E1 | (5a)--(5b) 的 complete-excess payload | 将 root endpoint 的 raw path 绑定到真实 queued source、保留 scope，并先执行所有 terminal-first priority。 |
| E2 | (6)、(10)、(12)--(16) | 将这些字段序列化为完整 target state。 |
| E3 | 无 | 独立重算 source/target F/G/hit、normal form、receipt 与 state hash。 |
| E4 | 两端使用图表无关 \(\operatorname{Sol}(4,p)\) 时，恒等映射 | target schema 必须确实采用该标记集。 |
| E5 | strict carry 的 (19) | source 必须是 E1 所说的 persistent state，不能把 transient root receipt 当作端点。 |

### 条件性直达准入推论

若原 \(a=1,d=1\) root chart 已是 persistent typed source，且其实际 raw path、
terminal-first prefix 与 source scope 已经被具名回执绑定，那么 (5a)--(5b) 使 strict
proper-root carry 直接进入单侧 complete-excess 宏的输入域。以 (6)、(12) 生成 target，
并独立完成 typed reclassification、normal-form 和 content-addressed replay 后，E1--E5
的支付分别为：输入 persistent path、(10)--(16)、两端 verifier、
\(\operatorname{Sol}(4,p)\) 恒等 lift 与 (19)。因此 strict root 不需要 stutter relay
checkpoint；它的唯一未实现部分是这些已有字段的 serializer/registry 接入。

这个推论不是说每个 root chart 已经有 persistent parent，也不把缺失的 E1/E3 provenance
伪装成已注册的递归边。

## 5. 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_strict_carry_support_rebase.py --verify
```

该脚本仅重放 (p=73,r=3) 与 (p=313,r=271) 两个 actual proper-root strict
receipt，重算旧支撑 stutter、complete-excess support rebase、canonical overflow target、
不变图表 promotion 的整除失败及 (19)。它不搜索素数、参数、selector history 或历史
测试。
