---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-fresh-carrier-root-cyclotomic-orthogonality
title: q=1 高 C=2 19 相位 H4 a=1 fresh carrier 与 root cyclotomic 容量的互素屏障
statement: >-
  在 q=1 high C=2 19-phase 的 actual H4 proper-overlap top-capacity a_alt=1
  receipt 中，令 w=(p+1)/2、d4=gcd(w,M4)、q=w/d4>1。若其已准入 d=1 suffix
  终止于 p-free root return b_*=2pr-1，令 M=(p^2+p+1)/3、
  u=gcd(2r+1,M)，则 gcd(q,3M)=gcd(q,3u)=1，且 root endpoint 满足
  R-(p+1)=1 (mod q)。因此 q 不可能成为 root capacity 3u 的因子。对每个 canonical
  a=1 regeneration，xi_i=b_i+1 满足 xi_(i+1)=xi_i(1-2xi_i) (mod q)，而末态满足
  2r+1=-b_* (mod q)。反过来，对任意 b-bar (mod q)，CRT 可构造静态 a=1 p-free
  root return，保持 b_*=b-bar (mod q)、eta=0、omega=-1 且 u=M，因而
  9u^2>p。故仅由 q|w、再生与 terminal root 的 root-side 同余传输不能推出
  root small-fan condition 9u^2<p；任何 q-based closure 必须在进入 root 前使用
  q|Q 等额外的 actual H4 provenance 或短证书。该 CRT 控制不声称构造 actual H4
  predecessor。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff
  - type-I-overflow-full-product-d-one-p-adic-regeneration-countdown
  - type-I-overflow-full-product-d-one-a-one-root-coprime-capacity-fan-half-descent
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - a-one
  - fresh-carrier
  - p-adic-regeneration
  - root-capacity-fan
  - cyclotomic-orthogonality
  - crt-boundary
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff
    role: actual-H4-fresh-q-carrier-and-admitted-a-one-suffix
  - claim: type-I-overflow-full-product-d-one-p-adic-regeneration-countdown
    role: exact-a-one-regeneration-recurrence
  - claim: type-I-overflow-full-product-d-one-a-one-root-coprime-capacity-fan-half-descent
    role: root-capacity-and-small-fan-contract
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_fresh_carrier_root_cyclotomic_orthogonality.py
    role: congruence-transport-and-static-CRT-boundary-controls
visibility: public
last_checked: '2026-08-16'
---

# H4 \(a=1\) fresh carrier 与 root cyclotomic 容量的互素屏障

## 1. 设置与问题的准确边界

保留 actual H4 proper-overlap top-capacity \(a_{\rm alt}=1\) receipt 的记号：

\[
w=\frac{p+1}{2},\qquad d_4=(w,M_4),\qquad q=\frac{w}{d_4}>1.
\tag{1}
\]

已有 H4 handoff 给出 \(q\mid Q\mid(R_4-h)\)，并且 \(q\mid w\)，故

\[
p\equiv-1\pmod q.
\tag{2}
\]

本卡只考察该已准入 \(d=1\) suffix 若终止在 \(p\)-free root return 的后果。写

\[
b_\ast=2pr-1,\qquad
M=\frac{p^2+p+1}{3},\qquad
u=(2r+1,M).
\tag{3}
\]

这里 \(q\) 由 H4 renewal 在 root 之前注入，\(u\) 则度量 root endpoint 的容量。问题是：
\(q\) 是否能成为 \(u\) 的因子，或只用它的同余信息强制 \(9u^2<p\)？

## 2. \(p+1\) carrier 与 cyclotomic root 容量互素

因为 \(p\equiv1\pmod{24}\)，\(w\) 为奇数且

\[
w\equiv1\pmod3.
\tag{4}
\]

所以 \(q\mid w\) 蕴含 \((q,3)=1\)。由 (2)，

\[
3M=p^2+p+1\equiv1\pmod q.
\tag{5}
\]

于是

\[
\boxed{(q,3M)=(q,3u)=1.}
\tag{6}
\]

root normal form 的 residual 为

\[
R=2p^3r-p^2-2pr-p+1.
\tag{7}
\]

再次使用 \(p\equiv-1\pmod q\)，得到

\[
R\equiv1\pmod q,
\qquad
\boxed{R-(p+1)\equiv1\pmod q.}
\tag{8}
\]

既有 root formula 给出

\[
(R-(p+1),K)=3u.
\tag{9}
\]

因此 (6)--(9) 说明一个 H4 fresh \(q\)-carrier 在 root endpoint 处绝不成为 charged
capacity factor。它仍可留在支撑 \(K\) 中，但不在该 root capacity 中；不能把
\(q\mid Q\) 误读为 \(q\mid u\)。

## 3. 再生对 \(q\)-残数的精确传输

令 \(b_i\) 是一个 canonical \(a=1\) regeneration chain 的参数，并写

\[
E_i=(p-1)b_i-1=1+ps_i,\qquad
b_{i+1}=b_iE_i-s_i,\qquad
\xi_i=b_i+1.
\tag{10}
\]

模 \(q\) 下，(2) 给出 \(s_i\equiv-(E_i-1)\) 且

\[
E_i\equiv-2b_i-1=1-2\xi_i.
\tag{11}
\]

故有不依赖 \(p\)-进长度的闭式一步递推

\[
\boxed{\xi_{i+1}\equiv\xi_i(1-2\xi_i)\pmod q.}
\tag{12}
\]

在终端 (3) 处，

\[
b_\ast+1=2pr\equiv-2r\pmod q,
\qquad
\boxed{2r+1\equiv-b_\ast\pmod q.}
\tag{13}
\]

式 (12)--(13) 是 q-residue 与 root 参数之间全部直接的、无 provenance 假设的传输。
它没有产生一个 \(q\mid u\) 型关系，且 (6) 排除了这种关系。

## 4. CRT 饱和控制：单靠 q-residue 不能压低 \(u\)

取任意 \(\bar b\in\mathbb Z/q\mathbb Z\)。由 (6)，\(M\) 在模 \(q\) 下可逆；又 \(q\)
为奇数，所以可取正奇整数 \(y\) 使

\[
My\equiv-\bar b\pmod q.
\tag{14}
\]

定义

\[
r=\frac{My-1}{2},\qquad b_\ast=2pr-1,\qquad
n_\ast=(p+1)b_\ast-1.
\tag{15}
\]

则 \(r\ge1\)、\(b_\ast\) 为正奇数、\(n_\ast\equiv1\pmod4\)，且这个 full-product 行满足
\(a=1\)。同时

\[
b_\ast\equiv-My\equiv\bar b\pmod q,
\qquad
(2r+1,M)=(My,M)=M.
\tag{16}
\]

又 \(b_\ast\equiv-1\pmod p\)，所以 \(E_\ast=(p-1)b_\ast-1\equiv0\pmod p\)，并且

\[
\eta=\nu_p(E_\ast-1)=0,\qquad
\omega\equiv E_\ast-1\equiv-1\pmod p.
\tag{17}
\]

这是一条静态的 \(a=1\) \(p\)-free root return，且

\[
u=M,\qquad 9u^2>p.
\tag{18}
\]

因此，即使预先指定任何终端 \(q\)-残数，也能在一般 root arithmetic 中实现 saturated
large-capacity layer。该构造不满足、也不被声称满足 actual H3 \(\Rightarrow\) H4
provenance；它精确排除的只是以下 root-side 错误推理：

\[
q\mid w\text{ 与 (12)--(13) 的同余传输}\quad\Longrightarrow\quad 9u^2<p.
\]

## 5. 对全局出口目标的后果

本卡给出的是一条路线边界，而非 global exit：

1. \(q\) 不能作为 root capacity prime 被 \(h=3u\) fan 直接消费；
2. q-residue 在再生中按 (12) 演化，但它与 \(u\) 的 cyclotomic 因子没有共享支撑；
3. 任何利用 \(q\) 关闭 H4 残余的论证，必须在进入 root 前从 actual
   \(q\mid Q\mid(R_4-h)\)、\(4K_4\equiv1-h\pmod q\) 和 H3 \(\Rightarrow\) H4 receipt
   中取得额外的 E1/provenance 或短证书，而不能只追加一个 root gcd 条件。

这把下一步从“证明 \(q\) 压低 \(u\)”转为“在 q-carrier 尚可收费的 H4 renewal 节点寻找
q-carried terminal、split-carrier 或 strict macro”。

## 6. 定向回执

~~~bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_a_one_fresh_carrier_root_cyclotomic_orthogonality.py --verify
~~~

回执核对：一个局部 H4 \(c_4=1\) q-carrier 正控制、一次 \(a=1\) regeneration
的模 \(q\) 传输，以及 \(p=73,q=37\) 的静态 CRT 饱和 root control。它不扫描素数、分母或
actual predecessor history。
