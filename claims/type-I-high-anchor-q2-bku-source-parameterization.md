---
kind: claim
claim_id: type-I-high-anchor-q2-bku-source-parameterization
title: 互素 beta_0=2、q=2 最小正相位 automatic 高锚来源的 b-k-u 因子参数化
statement: >-
  在 gcd(A,R-1)=1、h=1 的 beta_0=2、q=2 automatic 高锚子族中，令
  b=p-2A、delta=R-p，并定义
  e=(2b^2(delta-1)-1)/p、k=(b(b+delta)+1)/(2(p-b))。则
  1<=k<=(b-1)/2，且 u=4bk-e 是 N_b(k)=2b(b^2+b+1)+1+4b^2k 的正因子，
  p=N_b(k)/u。反之，满足明确的素数、窗口、赋值、互素与相位门的 (b,k,u) 因子行
  恢复一个实际 fresh-root automatic C=2A 高锚来源。该参数化把候选生成降为
  N_b(k) 的因子选择；它不保证 terminal-first unresolved、typed macro 或全局递降。
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
  - proof-boundary
sources:
  - claim: type-I-high-anchor-automatic-q-source-template
    role: exact-root-and-second-excess-gates
  - reproduction: reproductions/type_i_high_anchor_q2_bku_parameterization.py
    role: four-positive-controls-and-parity-boundary
visibility: public
last_checked: '2026-08-16'
---

# 互素 beta_0=2、q=2 automatic 高锚来源的 b-k-u 因子参数化

## 1. 受限来源模型

只考虑下列已知可构造的子族。令 p 是 p=1 mod 24 的素数，first root 为
R_0=2A+1，第一次 complete-excess 给出 Q_0=A、beta_0=2，并进入高锚
H=(p,R,K;A)。再要求第二 complete-excess 满足 Q_1=R-1、beta_1=1，
gcd(A,R-1)=1，second rechart 的 cofactor 是 C=2A，且 B=K/A 为奇数，
所以 automatic phase 为 h=1。

写

$$
p=2A+b, \qquad R=p+delta.
$$

高窗口与 root parity 给出 b=3 mod 8、delta=2 mod 8，且
0<delta<p-2b。令

$$
e={2b^2(delta-1)-1 \over p},
\qquad
k={b(b+delta)+1 \over 2(p-b)}.
$$

在本子族中这两个数是正整数。

## 2. 因子参数式

定义

$$
N_b(k)=2b(b^2+b+1)+1+4b^2k.
$$

由 canonical 高锚条件和 automatic 条件分别得到

$$
b(b+delta)+1=2k(p-b),
$$

$$
2b^2(delta-1)-1=ep.
$$

消去 delta 后有

$$
(4bk-e)p=N_b(k).
$$

所以令 u=4bk-e，便有

$$
u>0, \qquad u \mid N_b(k), \qquad p={N_b(k) \over u}.
$$

又因为 delta<p-2b，

$$
1 \le k \le {b-1 \over 2}.
$$

这不是经验筛选：每个满足模型条件的来源行都给出一组有限的因子数据 (b,k,u)。

相位门也可完全降到因子参数。将第一条等式代回
\(2(p-b)B=p(p+\delta)+1\)，得到

\[
2B=p+b+\delta+2k.
\]

由于 \(p\equiv1\pmod4\)、\(b\equiv3\pmod8\)、\(\delta\equiv2\pmod8\)，有

\[
B\equiv k+1\pmod2.
\]

所以本卡的最小正相位条件等价于

\[
\boxed{\ h=1\quad\Longleftrightarrow\quad B\ {\rm odd}
\quad\Longleftrightarrow\quad k\equiv0\pmod2.\ }
\]

这使 \(q=2\) 的 phase 过滤可在分解 \(N_b(k)\) 前执行。

## 3. 反向恢复

给定 b=3 mod 8、1<=k<=(b-1)/2 和一个正因子 u of N_b(k)，定义

$$
p=N_b(k)/u, \qquad e=4bk-u,
$$

$$
delta=1+{ep+1 \over 2b^2},
\qquad A={p-b \over 2},
\qquad R=p+delta.
$$

反向行必须明确检查：p 是 core prime；e>0；delta 是整数且落在上述窗口；
gcd(A,R-1)=1；A 与 (R-1)/2 分别相对 (p+1)/2 满足 strict odd-prime excess；
并且 B=(pR+1)/(4A) 是奇数。所有这些门都通过时：

1. delta 偶和第一条等式给出 4A divides pR+1，因此 H 是 canonical 高锚；
2. 两个 strict-excess 门分别给出 Q_0=A,beta_0=2 和 Q_1=R-1,beta_1=1；
3. gcd(A,R-1)=1 给 M=A(R-1)，而第二条等式模 p 化为
   8A^2(R-1)=1 mod p；故 canonical second rechart 的 C=2A；
4. \(B\) 为奇数、等价地 \(k\) 为偶数时，automatic phase
   \(h=(2(M\bmod p)-B)/p\) 恰为 \(1\)。

所以这是一个可验证的 fresh-root source-construction interface。它不跳过 terminal-first
priority，也不把 source construction 本身升级为 verified macro edge。

## 4. 固定控制和必要的 parity 门

下表四行由同一公式恢复，且每一行都逐项重放了 root、two complete-excess bundles、
C=2A、cofactor gate 和 h=1：

| p | b | k | u | A | R |
|---:|---:|---:|---:|---:|---:|
| 3793 | 171 | 80 | 5119 | 1811 | 7011 |
| 34897 | 7627 | 1756 | 37139375 | 13635 | 39827 |
| 67801 | 14819 | 4364 | 152540695 | 26491 | 84187 |
| 68713 | 6427 | 2104 | 12787511 | 31143 | 103067 |

四条正控制的 \(k\) 都为偶数，正是上述 phase prefilter。条件 b=3 mod 8 不能删除。形式行

$$
(p,A,R;b,k,u)=(673,317,699;39,2,199)
$$

也满足 N_b(k)=up，且 formal chart(A) 给 R=699；但 b=7 mod 8、A=1 mod 4，
实际 root 的 complete-excess 是 Q_0=2A,beta_0=1，first rechart 使用 M=2A 而不是
A。它严格排除把只满足方程的 formal chart 误报为 beta_0=2 source。

## 5. 边界

该参数化缩小了下一轮来源研究的搜索空间：先选 b 与偶数 k，再分解 N_b(k) 并逐行检查
source、priority、typed lift 和势。它没有证明存在一个避开全部 terminal-first 菜单的行；
p=34897 与 p=68713 已由 gap-3/gap-7 priority boundary 正确截断。全局问题仍是证明
每个 terminal-first unresolved 状态有此类或另一类真实出口。

## 聚焦验证

```bash
PYTHONPATH=reproductions python3 \
  reproductions/type_i_high_anchor_q2_bku_parameterization.py --verify
```
