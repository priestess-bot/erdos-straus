---
kind: claim
claim_id: odd-distance-even-source-overflow-support-criterion
title: 奇距离偶源尾的饱和溢出支持判据
statement: 设 (M,r)=1，B 为正整数，并令 S_M(B)=积_{q|B}q^{v_q(M)}。存在正规形溢出恰为 B 的偶源平方尾，当且仅当 B|S_M(B) 且存在 a|M/S_M(B)，满足 B<=a 与 a=-B mod r；此时 g=M/a、e=Bg。十亿 H19 首 r 剖面的31个纯复合溢出状态按最少不同溢出素因子数分布为1:16、2:13、3:2。
claim_status: established
topics:
- type-I
- even-source
- overflow
- normal-form
- divisor-residues
- factorization
- product-set
- h19
sources:
- paper: bradford2024
  locator: Proposition 1
  role: even-source-tail-context
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization
visibility: public
last_checked: '2026-07-26'
---

# 奇距离偶源尾的饱和溢出支持判据

设 \((M,r)=1\)，给定正整数 \(B\)。定义 \(B\) 在 \(M\) 中的**饱和支持部分**

\[
S_M(B)=\prod_{q\mid B}q^{v_q(M)}. \tag{1}
\]

则存在一个偶源平方尾，其正规形溢出恰为 \(B\)，当且仅当

\[
B\mid S_M(B),\qquad
\exists a\mid\frac{M}{S_M(B)}:\quad B\le a,\qquad a\equiv-B\pmod r. \tag{2}
\]

一旦 (2) 成立，取

\[
g=\frac Ma,\qquad e=Bg, \tag{3}
\]

便有 \(e\mid M^2\)、\(e\le M\)、\(e\equiv-M\pmod r\)，且

\[
\frac{e}{\gcd\left(e,(M+e)/r\right)}=B. \tag{4}
\]

## 证明

若尾的正规形为

\[
M=ag,\quad e=Bg,\quad (a,B)=1,\quad B\mid g,\quad B\le a,\quad a+B\equiv0\pmod r,
\]

则 \((a,B)=1\) 迫使 \(M\) 中每个属于 \(B\) 支撑的完整素数幂都落入 \(g\)。故
\(a\mid M/S_M(B)\)，且 \(B\mid S_M(B)\)。余下条件就是 (2)。

反之，(2) 给出 \((a,B)=1\)、\(B\mid g=M/a\)，再由 \(B\le a\) 与
\(a+B\equiv0\pmod r\) 恢复正规形。式 (4) 是该正规形的最大公因子恒等式。

该判据的关键是：固定溢出 \(B\) 后，参与 \(a\) 的因子必须完全避开 \(B\) 的素因子支持。
因而问题不只是 \(B\mid M\)，而是“从补支持因子表中命中 \(-B\)”的受限除子积集问题。
素数溢出判据正是 \(B=q\) 的特例。

## H19 纯复合边界

将该判据独立地与全部 \(M^2\) 尾因子枚举逐项核对。91 个高溢出首状态中，去除有素数
溢出尾的 60 个后，31 个纯复合状态按一个尾所需的最少不同溢出素因子数分为：

| 最少不同素因子数 \(\omega(B)\) | 状态数 |
| ---: | ---: |
| 1（素数幂） | 16 |
| 2 | 13 |
| 3 | 2 |

最后两条三支持状态为

\[
(p,r,B)=(26{,}410{,}609,2351,735),\qquad
(540{,}645{,}121,759,70).
\]

因此，在当前有限剖面中，真正需要同时处理三种以上溢出素因子的边界只剩两点。但这不是
一般有界支持定理；对全称证明而言，仍须控制 \(S_M(B)\) 补支持中的受限积集，或在其失败
时构造可提升外部源递降。

可复现命令：

~~~bash
python3 reproductions/type_ii_h19_composite_overflow_support_profile.py \
  --input reproductions/type-ii-h19-bounded-r-overflow-profile-1b-results.json \
  --output reproductions/type-ii-h19-composite-overflow-support-profile-1b-results.json
python3 -m unittest tests/test_type_ii_h19_composite_overflow_support_profile.py -q
~~~
