---
kind: claim
claim_id: type-I-high-anchor-q3-bku-source-parameterization
title: 互素 beta_0=2、q=3 automatic 高锚来源的 b-k-u 因子参数化与相位门
statement: >-
  在 gcd(A,R-1)=1、beta_0=2、Q_1=R-1 的 q=3 automatic 高锚子族中，令
  p=3A+b、R=p+delta，并定义 e=(4b^2(delta-1)-3)/p。则 b=0 mod 4、
  delta=2 mod 8、1<=k<=b/4，且由
  3b(b+delta)+3=(4k-1)(p-b) 定义的 k 满足
  u=16bk-4b-3e 是
  N_b^(3)(k)=12b^3+8b^2+12b+9+16b^2k 的正因子，p=N_b^(3)(k)/u。
  反之，满足明确的素数、窗口、赋值、互素与 canonical 门的 (b,k,u) 因子行
  恢复实际 fresh-root q=3 automatic 高锚来源。其 phase 满足 h=2 当且仅当
  B=(pR+1)/(4A) 在模 3 下为 1，也当且仅当 k=2 mod 3；否则该来源不接入最小正相位
  fixed-n bridge。该结果只构造来源，不保证 terminal-first unresolved、typed macro
  或全局递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-high-anchor-automatic-q-source-template
  - type-I-high-anchor-full-excess-gate-design-template
topics:
  - Erdos-Straus
  - type-I
  - high-anchor
  - automatic-q
  - source-construction
  - complete-excess
  - factor-parameterization
  - phase-gate
  - proof-boundary
sources:
  - claim: type-I-high-anchor-automatic-q-source-template
    role: exact-root-second-excess-and-phase-gates
  - reproduction: reproductions/type_i_high_anchor_q3_bku_parameterization.py
    role: two-h-zero-boundaries-and-one-h-two-control
visibility: public
last_checked: '2026-08-16'
---

# 互素 beta_0=2、q=3 automatic 高锚来源的 b-k-u 因子参数化与相位门

## 1. 受限来源模型

只考虑已有 automatic-q 模板中的以下子族。令 \(p\equiv1\pmod {24}\) 为素数，
first root 为 \(R_0=2A+1\)，第一次 complete-excess 给出

\[
Q_0=A,\qquad \beta_0=2.
\]

它重图表到 canonical 高锚 \(H=(p,R,K;A)\)。再要求

\[
R=p+\delta,\qquad Q_1=R-1,\qquad \beta_1=1,
\qquad (A,R-1)=1,
\]

且第二次 complete-excess rechart 的 cofactor 为 \(C=3A\)。写

\[
p=3A+b,\qquad B=K/A.
\]

这里 \(b>0\)，因为 \(3A<p\)。root parity 给出 \(A\equiv3\pmod4\)，故

\[
b\equiv0\pmod4.
\tag{1}
\]

第二 full-excess 的 \(2\)-adic 条件给出 \(R\equiv3\pmod8\)，所以

\[
\delta\equiv2\pmod8,
\qquad 0<3\delta<p-4b.
\tag{2}
\]

后一个不等式正是 high window \(p<R<4A\) 的改写。与 \(q=2\) 的来源不同，
\(b\) 不固定在一个模 \(8\) 类；它可为 \(0\) 或 \(4\pmod8\)。

定义

\[
e={4b^2(\delta-1)-3\over p}.
\tag{3}
\]

这是正整数：automatic congruence

\[
12A^2(R-1)\equiv1\pmod p
\]

乘以 \(3\)、再代入 \(3A=p-b\)，恰给出 (3) 的整除性。

## 2. 因子参数式

canonical high-anchor 等式 \(4AB=pR+1\) 乘以 \(3\) 后，模 \(p-b\) 化为

\[
p-b\mid 3b(b+\delta)+3.
\]

由 (1)--(2)，左侧除数为 \(1\pmod4\)，而右侧为 \(3\pmod4\)。因此存在正整数
\(k\) 使

\[
3b(b+\delta)+3=(4k-1)(p-b).
\tag{4}
\]

将 (3) 代回 (4)，并清除 \(4b\)，得到

\[
\bigl(16bk-4b-3e\bigr)p
=12b^3+8b^2+12b+9+16b^2k.
\tag{5}
\]

令

\[
N_b^{(3)}(k)=12b^3+8b^2+12b+9+16b^2k,
\qquad u=16bk-4b-3e.
\tag{6}
\]

则

\[
u>0,\qquad u\mid N_b^{(3)}(k),\qquad
p={N_b^{(3)}(k)\over u}.
\tag{7}
\]

这把每条来源行化为有限的 \((b,k,u)\) 因子数据。它不是对全部 \(p,A\) 的范围扫描。

由 (2) 有

\[
3b(b+\delta)+3<b(p-b)+3.
\]

又 \(p-b=3A>3\)，故 (4) 的商严格小于 \(b+1\)。由于 \(b\equiv0\pmod4\) 且
\(4k-1\equiv-1\pmod4\)，这给出精确窗口

\[
1\le k\le {b\over4}.
\tag{8}
\]

## 3. 反向恢复和 phase 门

给定 \(b>0\)、\(b\equiv0\pmod4\)、\(1\le k\le b/4\) 及一个正因子
\(u\mid N_b^{(3)}(k)\)，定义

\[
p={N_b^{(3)}(k)\over u},\qquad
e={16bk-4b-u\over3},
\]

\[
\delta=1+{ep+3\over4b^2},\qquad
A={p-b\over3},\qquad R=p+\delta.
\tag{9}
\]

反向行必须逐项检查：\(p\) 是 core prime；\(e\) 与 \(\delta\) 是正整数；(2) 的
window 和 parity 成立；\(A\equiv3\pmod4\)；\(4A\mid pR+1\) 且
\(p<R<4A\)；\((A,R-1)=1\)；以及相对
\(s=(p+1)/2\) 的两条严格 odd-prime excess 条件

\[
\mathcal E_s(A),\qquad \mathcal E_s((R-1)/2).
\tag{10}
\]

这些门给出 \(Q_0=A,\beta_0=2\) 与 \(Q_1=R-1,\beta_1=1\)。另一方面，(3) 等价于

\[
12A^2(R-1)\equiv1\pmod p,
\]

所以 complete-excess carrier \(M=A(R-1)\) 的 rechart cofactor 确为 \(C=3A\)。
于是 (9)--(10) 是实际 fresh-root automatic 来源的可验证构造接口。

还须把 phase 单独保留。将 (4) 回代入 canonical 等式的展开式，可得

\[
4B=3p+3b+3\delta+4k-1.
\tag{11}
\]

所以 \(B\equiv k-1\pmod3\)。令 \(r=M\bmod p\)，则

\[
h={3r-B\over p},\qquad 0\le h<3,
\qquad h\equiv-B\pmod3.
\tag{12}
\]

因为 \(p\equiv1\pmod3\)，故

\[
\boxed{\ h=2\quad\Longleftrightarrow\quad B\equiv1\pmod3
\quad\Longleftrightarrow\quad k\equiv2\pmod3.\ }
\tag{13}
\]

只有 (13) 成立的行才是最小正相位 \(h=q-1\) 的 fixed-\(n\) bridge 输入。把
automatic \(C=3A\) 误当成自动 \(h=2\) 会错误扩张该桥的定义域。

## 4. 固定控制与相位边界

下表全部由 (9) 恢复，并逐项重放 root、two complete-excess bundles、
\(C=3A\) 和 canonical phase：

| \(p\) | \(b\) | \(k\) | \(u\) | \(A\) | \(R\) | \(B\) | \(h\) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 41617 | 8464 | 2041 | 231066297 | 11051 | 43811 | 41247 | 0 |
| 60913 | 4972 | 1088 | 31281961 | 18647 | 72259 | 59011 | 2 |
| 93481 | 14824 | 2365 | 507142593 | 26219 | 95387 | 85023 | 0 |

两条 \(h=0\) 行仍是实际 fresh-root、two-anchor、互素的 \(q=3\) automatic
来源，但 \(B\equiv0\pmod3\) 且 \(k\equiv1\pmod3\)。它们是 (13) 必要性的控制，
而不是 fixed-\(n\) 的 \(h=2\) 输入。\(p=60913\) 的 \(B\equiv1\pmod3\) 与
\(k\equiv2\pmod3\) 给 \(h=2\)，但已有 terminal-first
叶优先抢占；这张卡不把它登记为非终端宏边。

## 5. 边界

这个参数化将 \(q=3\) 来源发现缩小为 \(N_b^{(3)}(k)\) 的因子选择，再由有限的
source、phase、priority 与 typed-lift 门过滤。它没有证明存在避开完整 terminal-first
菜单的行，也没有给出 parent API、E1--E5 或全局良基递降。它只消除了该严格子族中
对 \((p,A)\) 的盲枚举，并明确排除了 phase gate 被遗漏的误用。

## 聚焦验证

~~~bash
PYTHONPATH=reproductions python3 \
  reproductions/type_i_high_anchor_q3_bku_parameterization.py --verify
~~~
