---
kind: claim
claim_id: type-I-t6-f3-high-endpoint-normal-form-v1
title: F3 high endpoint 的高域正规形、strict overflow 分流与 stutter 残差
statement: >-
  对 ACTUAL_PERSISTENT、PROPER_FACTOR_ROOT、h>p、terminal_first_miss
  的真实根容量端点，令 C=p^2+p+1、M=C/3、u=gcd(2r+1,M)、h=3u、v=M/u。
  则 2<=v<=p-1、h=C/v、h-p-1>0。actual maximal receipt z=R-h=ED
  满足 D|K、D|ph+1，且 canonical cofactor c=<D(h-1)^(-1)>_p 给出互斥
  strict/stutter 二分。strict 分支的 canonical support M_ex=lcm(A,Q)=AE、
  target cofactor c、R_ex=(4M_ex c-1)/p 满足 R_ex>p，因而 target 的正确
  候选类型是 ordinary TYPEI/OVERFLOW；其 Sol(4,p) lift 与 high-support
  Lambda-sharp 下降只在 common E3/admission 前提下构成 conditional edge。
  stutter 分支在高域内可重新证明 D=(m-1)p-(h-p-1)、m>=3、a=em-h>e、
  h|N=a^2-a(e-1)+(e-1)^2、m|(a+3u) 及
  u|(L^2+Ls+s^2), L=am,s=m-a；不使用 low-height 的 a<e、
  m<1+sqrt(h)、k=1 空域或 D_star 结论。该正规形不关闭
  HIGH_ENDPOINT_RESIDUAL，F3 与 T6 仍 OPEN。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-general-endpoint-divisor-gate
  - type-I-root-capacity-strict-carry-support-rebase
  - type-I-root-capacity-stutter-receipt-factor-split
  - type-I-root-capacity-stutter-pair-root-divisor-gate
  - t6-f3-proper-root-domain-v1
topics:
  - type-I
  - root-capacity
  - f3
  - high-endpoint
  - strict-carry
  - stutter
  - normal-form
  - overflow
  - proof-boundary
sources:
  - claim: type-I-root-capacity-general-endpoint-divisor-gate
    role: actual endpoint receipt and canonical cofactor
  - claim: type-I-root-capacity-strict-carry-support-rebase
    role: strict support target and Lambda-sharp descent
  - claim: type-I-root-capacity-stutter-receipt-factor-split
    role: actual D divisor and cyclotomic capacity split
  - claim: type-I-root-capacity-stutter-pair-root-divisor-gate
    role: high-domain parameter identities rederived below
  - reproduction: reproductions/type_i_t6_f3_high_endpoint_normal_form.py
    role: symbolic identities, strict actual control, and non-core stutter shadow
visibility: public
last_checked: '2026-08-24'
---

# F3 high endpoint 的高域正规形

## 1. 量词与 root quotient

只考虑已有活动 source/admission envelope、且 ordered terminal-first 返回 miss 的真实
root-capacity endpoint：

\[
\mathrm{ACTUAL\_PERSISTENT}\land\mathrm{PROPER\_FACTOR\_ROOT}
\land(h>p)\land\mathrm{terminal\_first\_miss}.
\]

令

\[
C=p^2+p+1,\quad M=C/3,\quad u=(2r+1,M),\quad h=3u,
\quad v=M/u.
\]

由于 \(0<u<M\)，有 \(v>1\)。又 \(h=C/v>p\) 给出 \(v<p+1\)，而
\(p\nmid C\) 排除 \(v=p\)，因此

\[
\boxed{2\le v\le p-1,\qquad h=C/v,\qquad
\delta:=h-p-1>0.}
\tag{1}
\]

这里 \(\delta\) 为奇数，因为 \(p,h\) 都是奇数。没有使用 \(h<p\) 或任何
Eisenstein quotient 的 low-height 假设。

## 2. Actual receipt 与 canonical cofactor

沿用实际 root chart

\[
g=(p+1)/2,\quad T=p^2r-g,\quad A=gT,\quad K=A(p-1),
\quad R=2p^3r-p^2-2pr-p+1,
\]

并令 \(z=R-h=ED\) 为相对 \(K\) 的 maximal complete-excess receipt。actual endpoint
定理给出

\[
h\mid K,\quad (h,z)=1,\quad D\mid K,\quad D\mid ph+1.
\tag{2}
\]

proper-factor 条件 \(u<M\) 还给出 \(p\nmid E\)，并且

\[
c=\left\langle D(h-1)^{-1}\right\rangle_p
 =\left\langle-E^{-1}\right\rangle_p.
\tag{3}
\]

terminal-first miss 意味着 \(Q>1\)，其中 \(Q\) 是 \(z\) 的超容量完整幂块；因此下面的
canonical support rebase 不是 bottom terminal 的重命名。

## 3. Strict 分支的正确 target 类型

若 \(c\le p-2\)，令

\[
M_{\mathrm{ex}}=\operatorname{lcm}(A,Q)=AE,\quad
K_{\mathrm{ex}}=M_{\mathrm{ex}}c,\quad
R_{\mathrm{ex}}=(4M_{\mathrm{ex}}c-1)/p.
\tag{4}
\]

根 chart 的 \(r\ge1\) 给出

\[
4A\ge2p^3+p^2-2p-1,
\]

所以 \(4A-1>p^2\)。由 \(M_{\mathrm{ex}}\ge A\)、\(c\ge1\)，得到

\[
\boxed{R_{\mathrm{ex}}>p.}
\tag{5}
\]

因此 strict high endpoint 的 canonical target 必须按 TYPEI/OVERFLOW 重新分类。它
不能同时被写成 \(R_T<p\) 且 \(M>B_p\)：若 \(R_T<p\)，则
\(K_T=(pR_T+1)/4\le B_p\)，而 \(M\mid K_T\) 强制 \(M\le B_p\)。

在 source 已是 persistent、target 通过 common E3/admission 的条件下，

\[
\Lambda_p^\sharp(S)=(0,p-1),\qquad
\Lambda_p^\sharp(T)=(0,c),
\]

故 \(c\le p-2\) 支付严格 E5；两端都取 \(\operatorname{Sol}(4,p)\) 时 E4 是恒等
lift。尚未支付的是 target normal form、owner、serializer、re-entry 和 admission，
因此该结论是 conditional physicalization，不是已登记 edge。

## 4. Stutter 分支的高域重建

若 \(c=p-1\)，则由 (3)

\[
D\equiv1-h\equiv-\delta\pmod p.
\]

因此唯一正整数 \(m\) 满足

\[
D=(m-1)p-\delta=mp+1-h.
\tag{6}
\]

置 \(e=(ph+1)/D\)、\(a=em-h\)。由 \(eD=ph+1\) 和 (6) 直接消去 \(D\)，得

\[
pa=e(h-1)+1,\qquad Da=m+h(h-1).
\tag{7}
\]

于是 \(a>0\)。进一步

\[
p(a-e)=e(h-p-1)+1=e\delta+1>0,
\]

所以

\[
\boxed{a>e.}
\tag{8}
\]

这是 high 与 low 的关键方向相反；不能套用 low proof 中的 \(a<e\)。

### 4.1 重新证明 \(m\ge3\) 与奇偶模三约束

\(D>0\)、\(h>p\) 与 \(D=mp+1-h\) 先给出 \(m\ge2\)。另一方面
\(D\equiv m+1\pmod3\)，而 \(D\mid ph+1\equiv1\pmod3\)，故
\(m\not\equiv2\pmod3\)。因此

\[
\boxed{m\ge3.}
\tag{9}
\]

由于 \(u\) 奇，\(m\mid a+3u\) 与 (7) 分别给出 \(a\) 为奇数；并且

\[
m\equiv0\pmod3\Rightarrow a\equiv0\pmod3,\qquad
m\equiv1\pmod3\Rightarrow a\equiv2\pmod3.
\tag{10}
\]

## 5. 高域 Eisenstein 整除式

令 \(b=e-1\)。由 \(h\mid C\) 和 \(pa\equiv1-e=-b\pmod h\)，有

\[
a^2C\equiv (pa)^2+(pa)a+a^2
\equiv b^2-ab+a^2\pmod h.
\]

因此在 high stutter 分支中可重新证明

\[
\boxed{N:=a^2-ab+b^2=hk,\qquad k\in\mathbb N.}
\tag{11}
\]

这里 \(N>0\) 来自 \(a>b\ge0\)。式 (11) 仅是本节从 high 假设推出的结果，不是把
low-height \(k\) 定理移植过来；后续 low 的 \(k=1\) 无限下降仍不可调用。

再令

\[
L=am,\qquad s=m-a.
\]

由 (7) 消去 \(D\) 得

\[
Lp=9u^2+3(a-1)u+s,\qquad m\mid a+3u.
\tag{12}
\]

模 \(u\) 使用 \(u\mid M\) 和 \(Lp\equiv s\pmod u\)，得到

\[
\boxed{u\mid L^2+Ls+s^2.}
\tag{13}
\]

式 (12)--(13) 是 high stutter 的有效有限参数门；它们不提供全局界、terminal 或
physical successor。尤其 \(s\) 在 high 域可以为负，不能使用只对 \(s\ge0\) 成立的
low-height 大小估计。

## 6. 精确边界

因此 high endpoint 当前被严格收缩为：

1. HIGH_STRICT_CARRY：确定 support-rebase overflow candidate，算术 E2/E4/E5
   已知，但 E3/admission/re-entry 仍开放；
2. HIGH_STUTTER_GATE：满足 (1)、(6)--(13) 的高域整数曲线，尚未证明
   FAMILY_EMPTY、terminal 或 physical E1--E5 successor。

非核心的高 stutter shadow \(p=67,h=93,D=779,m=13,e=8\) 只能验证正规形，
不能冒充 ACTUAL_PERSISTENT 核心 receipt。类似地，\(p=313,r=271\) 只验证一个
actual maximal arithmetic receipt；它没有活动 admission envelope，不能单独证明
本卡量词域非空。当前唯一安全状态仍是

HIGH_ENDPOINT_TOTAL_EXIT = OPEN；
T6_F3_PROPER_ROOT_PHYSICALIZATION = OPEN；
T6_GLOBAL_SELECTOR_TOTALITY = OPEN。
