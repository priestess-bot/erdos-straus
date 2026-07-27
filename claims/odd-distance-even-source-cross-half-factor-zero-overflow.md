---
kind: claim
claim_id: odd-distance-even-source-cross-half-factor-zero-overflow
title: 奇距离偶源零溢出的交叉半因子判据
statement: 设 p-c=d(1+cr) 是兼容奇距离偶源射线，r=7 mod8，A=(cr+1)/2，B=(dr+1)/2，故 M=(rp+1)/4=AB。则该射线存在零溢出平方尾，当且仅当存在 alpha|A、beta|B 使 alpha beta=-1 mod r。该判据把偶源射线的因子对与零溢出尾合并为一次双侧除子残数命中。十亿 H19 剖面的649个首 r 状态逐项复核后，恰有558个命中、91个不命中。
claim_status: established
topics:
- type-I
- even-source
- overflow
- factorization
- divisor-residues
- normal-form
- selector
sources:
- paper: bradford2024
  locator: Proposition 1
  role: even-source-descent
visibility: public
last_checked: '2026-07-26'
---

# 奇距离偶源零溢出的交叉半因子判据

设 \(p\equiv1\pmod {24}\)，并给定兼容的奇距离偶源射线

\[
p-c=d(1+cr),\qquad c\equiv1\pmod2,\qquad d\equiv1\pmod4.
\]

由半因子对等价，\(r\equiv7\pmod8\)，且

\[
A=\frac{cr+1}{2},\qquad B=\frac{dr+1}{2},
\qquad M=AB=\frac{rp+1}{4}. \tag{1}
\]

则以下两项等价：

\[
\begin{aligned}
&\text{存在零溢出偶源平方尾 }e; \\[-2pt]
\Longleftrightarrow\quad
&\exists\alpha\mid A,\ \beta\mid B:\quad
\alpha\beta\equiv-1\pmod r. \tag{2}
\end{aligned}
\]

这里“零溢出”指

\[
e\mid M^2,\qquad e\le M,\qquad e\equiv-M\pmod r,
\qquad e\mid\frac{M+e}{r}. \tag{3}
\]

## 证明

由[普通除子判据](odd-distance-even-source-zero-overflow-divisor-criterion.md)，(3) 等价于

\[
\exists a\mid M:\quad a\equiv-1\pmod r,\qquad e=M/a. \tag{4}
\]

若 \(a\mid AB\)，逐个素数 \(\ell\) 分配 \(v_\ell(a)\) 个指数：先向 \(A\) 分配至多
\(v_\ell(A)\) 个，其余分配给 \(B\)。由于
\(v_\ell(a)\le v_\ell(A)+v_\ell(B)\)，得到

\[
a=\alpha\beta,\qquad\alpha\mid A,\quad\beta\mid B. \tag{5}
\]

于是 (4) 蕴含 (2)。反过来，(2) 的 \(a=\alpha\beta\) 整除 \(AB=M\)，故由 (4) 恢复
零溢出尾。这证明等价。

重要的是，(2) 不要求 \(A,B\) 互素，也不把同一素因子的幂错误地限制在某一侧；上述指数
分配正是处理共享素因子的完整理由。

## 有限剖面与研究意义

对十亿 H19 残余中 649 个有首 \(r\) 命中的状态，逐项按 (1) 构造半因子对并枚举两侧
除子残数：558 个命中 (2)，91 个不命中，和独立的 Type I 溢出剖面完全一致。558 个
命中状态再按单侧是否已命中 \(-1\) 分为：

| 类型 | 状态数 |
| --- | ---: |
| 仅 \(A\) 一侧命中 | 89 |
| 仅 \(B\) 一侧命中 | 279 |
| 两侧各自均命中 | 6 |
| 两侧各自均不命中、但交叉积命中 | 184 |

最后一类是**本质跨侧**状态：不能把判据拆成“\(A\) 或 \(B\) 的单侧因子表应命中”。
四个标准平方因子递降遗漏中，\(p=35\,840\,809\) 正属此类，其见证为
\(\alpha=361\mid A\)、\(\beta=101\mid B\)、\(361\cdot101\equiv-1\pmod {103}\)。

因此，零溢出分支不再需要表述为“给定 \(M\) 后在 \(M^2\) 中找尾”。真正的选择器问题是：
先得到同余半因子对 \(A,B\)，再证明两个**不同来源**的因子残数积集命中 \(-1\)。这与固定
距离扇的条件性逃逸边界相容，并指向跨因子对的残数耦合，而不是单侧继续扩大除子表。

可复现命令：

~~~bash
python3 reproductions/type_ii_h19_zero_overflow_half_factor_pair_profile.py \
  --input reproductions/type-ii-h19-bounded-r-selector-boundary-1b-results.json \
  --overflow reproductions/type-ii-h19-bounded-r-overflow-profile-1b-results.json \
  --output reproductions/type-ii-h19-zero-overflow-half-factor-pair-profile-1b-results.json
python3 -m unittest tests/test_type_ii_h19_zero_overflow_half_factor_pair_profile.py -q
~~~
