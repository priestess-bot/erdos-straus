---
kind: claim
claim_id: type-I-t6-f3-m3-q5-source-bound-macro-interface
title: F3 m=3,q=5 的 source-bound raw word、同步 target 与 parent-to-final E5
statement: >-
  对一个已由完整状态合同接纳的 actual persistent Type-I/CHARGED proper-root parent
  S=(p,R,K;A,scope)，若其 m=3、5|D_star 且 terminal-first miss，则从 S 的 canonical
  integers 唯一构造 universal_p_source_v1，经 q=p 到 (1,R-1)，再按非降素数顺序
  剥尽 R-1 与 R-p-1 的超容量层，确定地到达 root endpoint (h,R-h)。每个前缀先运行
  同一 finite terminal scheduler：命中即 terminal，否则全部 miss receipt 连同 S.state_id、
  A 和 scope 构成 source-forward E1 transcript；它不是新 root 或 recursive edge。
  对此后任一由同一 transcript 到达的 primitive p-free endpoint u+v=R，重新计算唯一
  complete-excess blocks Q_u,Q_v，令 M=lcm(A,Q_u,Q_v)、L_omega=M/A、
  c=<C L_omega^{-1}>_p，其中 C=K/A=p-1。terminal-first miss 后若 L_omega!=1 mod p，
  则 M>A>B_p，因而 R_T>p，且以 CHARGED local tuple
  (0,p-1,eta)->(0,c,0) 的 LOCAL_DROP 支付 parent-to-final T5 ticket。全部中间
  raw/atomic/p^2 checkpoints 不入队。
  该定理建立 R1 的数学路径覆盖、R2 的确定 E2、Sol(p) 恒等 E4 与 strict branch E5，
  但活动 common producer、完整 terminal scheduler 与 overflow admission serializer
  仍须 coordinator 接入；L_omega=1 mod p、特别是 p^2 gate，以及 nonminimal q=5 leaf
  均不由本定理关闭。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-strict-carry-universal-raw-word-policy-boundary
  - type-I-universal-p-source-capacity-anchor-orbit
  - type-I-path-anchored-atomic-split-complete-excess-admission
  - type-I-t6-f3-policy-endpoint-p2-divisor-source-normal-form
  - type-I-t5-full-contract-level-global-well-foundedness
  - type-I-overflow-full-product-d-one-a-one-single-endpoint-stutter-guarded-relay
topics:
  - type-I
  - t6
  - f3
  - proper-root
  - m-three
  - q-five
  - source-path
  - serializer
  - complete-excess
  - well-foundedness
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_t6_f3_m3_q5_source_bound_macro.py
    role: focused-path-target-rank-and-boundary-replay
visibility: public
last_checked: '2026-08-24'
---

# F3 (m=3,q=5) 的 source-bound raw word、同步 target 与 parent-to-final E5

## 1. Scope

固定一个完整状态合同已经接纳的 actual persistent source

\[
S=(p,R,K;A,\varsigma),
\qquad
p\equiv1\pmod {24},
\qquad
4K=pR+1,
\qquad
K=A(p-1),
\qquad
A>B_p:=\frac{(p-1)^2}{4}.
\tag{1}
\]

它携带不可伪造的 `state_id`、persistent origin、charged-support provenance、
`source_tree_scope` (arsigma) 和 source-state terminal-first miss。再假设它是 low-height
actual proper-root receipt，且

\[
2\le h<p,
\qquad
m=3,
\qquad
5\mid D_*.
\tag{2}
\]

这里 (1)--(2) 是本定理的 source 输入，不从下游希望得到的 target 反向制造。

## 2. R1 的 canonical raw transcript

标准 root-capacity 坐标中存在唯一参数 (r\ge1)，满足

\[
R=2p^3r-p^2-2pr-p+1,
\qquad
K=\frac{p^2-1}{2}left(p^2r-\frac{p+1}{2}\right).
\tag{3}
\]

定义具名 formal source

\[
(U,V,n)=\bigl(p,R(p-1)-p,p-1\bigr).
\tag{4}
\]

由 (p\nmid K)，唯一 (q=p)、shift (1) 的 raw edge 无约分地给

\[
(U,V,n)\longmapsto(1,R-1,1).
\tag{5}
\]

root-capacity 恒等式又给

\[
(R-1,K)=p+1,
\qquad
(R-p-1,K)=h.
\tag{6}
\]

令

\[
L_0=\frac{R-1}{p+1},
\qquad
L_1=\frac{R-p-1}{h}.
\tag{7}
\]

分别把 (L_0,L_1) 写成含重数的非降素数 word。对一个 (m=1) primitive node
((x,R-x))，若 (q\mid x) 且 (v_q(x)>v_q(K))，则 shift 唯一为 (q-1)，并有

\[
(x,R-x)\longmapsto(x/q,R-x/q).
\tag{8}
\]

无 gcd reduction，因为 (q\nmid R)。逐素数应用 (8) 后，(5)--(7) 唯一给出

\[
(1,R-1)\leadsto(p+1,R-p-1)\leadsto(h,R-h).
\tag{9}
\]

### 定理 1（source-forward R1 coverage）

在 (1)--(2) 下，(4)--(9) 是从 persistent (S) 的 canonical integers 唯一重算的
有限 raw transcript。给每个暴露给 selector 的 prefix 先运行同一个版本化 finite
terminal scheduler：若首个 hit 出现，返回该 terminal；否则所有 miss receipts 与

```text
S.state_id
S.source_tree_scope
S.charged_support = A
ordered labels and oriented nodes
terminal-prefix receipt digests
```

一起形成 `f3_m3_q5_path_bound_source_receipt_v1`。这张 receipt 关闭的是 R1 的
source/path existence，而不是创建一个 successor。

**证明。** (4)--(6) 是整数恒等式；完整 capacity peeling 定理证明每段 (8) 都实际存在、
保持 primitive，且不同素数次序可交换。固定非降次序后 transcript 唯一。由于 (S)
已经独立携带 persistent origin、charged support 与 scope，把 (4)--(9) 绑定到
`S.state_id` 不会生成 fresh root，也不会重置 (A)。每个 terminal predicate 是有限、
确定的，故其首个 hit 或全部 miss 是穷尽二分。\(\square\)

活动 v1 header 目前只保存 opaque source/terminal digests，未公开 raw transcript 与 scope；
所以定理 1 的数学覆盖不能被布尔 `raw_path_bound=true` 代替。coordinator 必须把 receipt
payload 接入 common producer 才能从 registry 中删除 R1。

## 3. Endpoint 的同步 recanonicalization

从定理 1 的 path-bound source 继续重放任一已证明的 first-child/
(omega_{\rm pf}) policy，设 terminal-first 后得到 primitive (p)-free endpoint

\[
u+v=R,
\qquad
(u,v)=1,
\qquad
p\nmid uv.
\tag{10}
\]

相对原 (K) 唯一计算完整超额块

\[
u=Q_u\beta_u,
\qquad
v=Q_v\beta_v.
\tag{11}
\]

若 (Q_u=Q_v=1)，则 (uv\mid K)，直接 Type I terminal。以下假设 miss。令

\[
M=\operatorname{lcm}(A,Q_u,Q_v),
\qquad
L_\omega=M/A>1.
\tag{12}
\]

由 (K/A=p-1)，target cofactor 与 chart 唯一为

\[
c_T=\left\langle-(L_\omega)^{-1}\right\rangle_p,
\qquad
K_T=Mc_T,
\qquad
R_T=\frac{4K_T-1}{p}.
\tag{13}
\]

这一步在 one-sided 与 genuine two-sided occurrence 上完全相同；颜色只属于 E1/E3
edge receipt，不成为 caller-supplied target family。

## 4. Strict endpoint 的 parent-to-final T5 ticket

由 (13)，

\[
c_T=p-1
\Longleftrightarrow
L_\omega\equiv1\pmod p.
\tag{14}
\]

所以 strict branch (L_\omega\not\equiv1\pmod p) 精确满足

\[
1\le c_T\le p-2.
\tag{15}
\]

### 定理 2（second-child parent-to-final E5）

所有 first child、raw suffix、atomic split 与 (p^2) chart 只作 macro internal
checkpoint。由 (12)，非终止 endpoint 有

\[
M=A L_\omega>A>B_p.
\tag{16}
\]

若 (R_T<p)，则 (R_T\le p-2)，而 (M\mid K_T) 给

\[
M\le K_T=\frac{pR_T+1}{4}\le\frac{(p-1)^2}{4}=B_p,
\]

与 (16) 矛盾。因此 target 唯一属于 `TYPEI/CHARGED OVERFLOW`。对 original
persistent parent (1) 与最终 target (13)，两端 local ranks 为

\[
(0,p-1,\eta_S,0)
\quad\text{和}\quad
(0,c_T,0,0).
\tag{17}
\]

strict branch (15) 给 `LOCAL_DROP`。

因此 strict one-sided 与 strict two-sided branches 都有固定 parent-to-final T5 ticket；
不会使用 selected-side formal cofactor，也不会把 checkpoint 的局部升降计入 persistent
graph。

同一证明还覆盖 odd first child 的 strict branch：若 first-child one-sided，cofactor
为 (p-ell<p-1)；若是 atomic，(F_y\not\equiv\ell\pmod p) 等价于 canonical
first-child cofactor 小于 (p-1)。两者都直接使用 original parent 与该 final first-child
target 的 `LOCAL_DROP`，不需要调用 (omega_{\rm pf})。只有 first-child atomic
stutter (F_y\equiv\ell\pmod p) 才进入后续 policy endpoint 与 (L_\omega) 分派。

## 5. E1--E5 与 re-entry 边界

| obligation | 结论 |
|---|---|
| E1 | 定理 1 加 first-child/(omega_{\rm pf}) forward suffix；必须保存完整 payload 与 prefix receipts |
| E2 | (11)--(13) 是 source/path 的确定函数；tie-break 已固定 |
| E3 | occurrence owner 可唯一内容寻址；最终 state 必同步 normalize，并投影到既有 high-support overflow fallback；active producer 仍由 coordinator 注册 |
| E4 | source/target marked sets 同为图表无关 (operatorname{Sol}(p))，lift 为恒等映射 |
| E5 | 定理 2；只比较 original parent 与 final target |
| re-entry | target 的 arithmetic owner 是既有 overflow fallback；只有 common producer rule 接入后才算 actual re-entry |

所以 strict arithmetic leaves 已不再缺数学 E1、E2、E4 或 E5；它们只缺 common E3
integration。相反，

\[
L_\omega\equiv1\pmod p
\tag{18}
\]

没有上述 ticket。特别地 (L_\omega=1+p^2\chi) 的 parent/target CHARGED rank stutter
仍必须继续到最终 strict target 或 terminal。nonminimal (v_5(T)\ge2) leaf 同样只有
root-residue orientation。继续提高同余阶不改变这两个 OPEN 结论。

### 5.1 两个 ordinary (p)-stutter channels 的 guarded closure

在 (18) 的 stutter 行唯一写

\[
L_\omega=1+p\theta,
\qquad
\theta>0.
\tag{19}
\]

由 (a=1,d=1) ordinary relay，target checkpoint 的下一 multiplier 模 (p) 恰为
(	heta)。因此：

1. 若 (	heta\equiv-1\pmod p)，ordinary (p)-source 失败，但规范最小互素素数
   alternate source 的 arithmetic capacity 精确为 (1)。定理 1 的 source-bound path
   与该 alternate suffix 连续拼接；所有 checkpoint 不入队，最终 local cofactor
   (1<p-1)，所以 parent-to-final 是 `LOCAL_DROP`。
2. 若 (	heta\not\equiv-1,0,1\pmod p)，下一 ordinary residual capacity 为

   \[
   c_\theta=\langle-\theta^{-1}\rangle_p\le p-2.
   \]

   同理，forward suffix、恒等 lift和 original-parent-to-final `LOCAL_DROP` 完整。

两支只剩 common producer/normalizer/owner 接入，不再是数学 E1 或 E5 residual。
若 (	heta\equiv1\pmod p)，regeneration valuation 有限下降，但首个 non-regeneration
digit 仍可能落到 (p)-free failure；所以该支保持 OPEN。若 (	heta\equiv0\pmod p)，
正是 (L_\omega\equiv1\pmod {p^2}) 的两类 hard residual。

## 6. Nonminimal (q=5) 的 first-child 收缩

对 nonminimal leaf，若 (5\mid E)，则 complete-excess 定义保证 root endpoint
((z,h)) 的 (z)-side 有 actual (q=5) overcapacity。唯一 shift 为 (4)，给

\[
(z,h,1)\longmapsto(z/5,R-z/5,1).
\tag{20}
\]

它保持 primitive。两侧还必 (p)-free：(p\nmid z/5)；若
(p\mid R-z/5)，则 (z/5\equiv R\equiv1\pmod p)，从
(z=R-h\equiv1-h\pmod p) 得 (h=p-4)。但 q=5 管有

\[
p\equiv11\pmod {25},
\qquad
h\equiv9\pmod {25},
\]

而 (p-4\equiv7\pmod {25})，矛盾。因此 (20) 是确定、source-bound、p-free
first child，并可进入第 3 节的同步 recanonicalizer。

这里不声称 selected-side support 必下降。因为 (5\mid p-1)，一次除以 5 后的指数
可能恰落到 (K) 容量层，canonical support 会吸收 formal drop。真正 E5 仍只由最终
(L_\omega) target 判断。nonminimal 且 (5\nmid E) 时，q=5 在 root endpoint 没有
overcapacity occurrence，仍是该 leaf 最小的 E1/exit residual。

## 7. 未闭合量词

本定理不声称 `R1/R2/F3 CLOSED`。活动闭合仍需：

1. coordinator 接入完整 path/prefix receipt，而不是接受 `raw_path_bound` boolean；
2. common producer、同步 normalizer与 overflow owner re-entry；
3. pure-dyadic companion 的最终 recanonicalization；
4. nonminimal (q=5) 中 (5\nmid E) 子叶的 EMPTY/TERMINAL/PAID theorem，以及
   (5\mid E) child recanonicalization 后的 non-strict channels；
5. full-capacity one-sided 和 genuine two-sided (E_uE_v=1+p^2\chi) 的最终 exit。

这些正是 proof receipt 中保留的最小 gaps。
