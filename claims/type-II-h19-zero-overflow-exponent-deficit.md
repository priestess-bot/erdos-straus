---
kind: claim
claim_id: type-II-h19-zero-overflow-exponent-deficit
title: H19 首个 r 状态到零溢出普通除子目标的指数补偿距离
statement: 对存储的649个 r<=9999 首个偶源尾命中状态，定义指数补偿距离为：在 M1 的每个普通除子之后，使用 M1 既有素因子允许重复相乘以达成 -1 mod r 的最少补因子数。精确分布为缺陷0:558、1:75、2:13、3:2、4:1，最大为4。该量在有限剖面上把所有高溢出状态压缩为至多四次支持素因子重复的指数不足，但不构造新尾或给出一般上界。
claim_status: computationally_reproduced
topics:
- type-I
- even-source
- overflow
- divisor-residues
- finite-product-set
- exponent
- finite-audit
- h19
sources:
- paper: bradford2024
  locator: Proposition 1
  role: even-source-descent
visibility: public
last_checked: '2026-07-26'
---

# H19 首个 \(r\) 状态到零溢出普通除子目标的指数补偿距离

令 \(S(M)\) 是 \(M\) 的不同素因子集合。对 \(h\in\langle S(M)\rangle\subseteq
(\mathbb Z/r\mathbb Z)^\times\)，记 \(\ell_{M,r}(h)\) 为把 \(h\) 写成 \(S(M)\) 中
素因子残数之积所需的最少因子个数，允许重复。定义

\[
\delta(M,r)=\min_{a\mid M}
\ell_{M,r}(-a^{-1}\bmod r). \tag{1}
\]

这表示先选一个现有普通除子 \(a\)，再允许重复使用 \(M\) 的支持素因子，达到零溢出目标
\(-1\) 所需的最少额外因子步数。

显然

\[
\delta(M,r)=0
\quad\Longleftrightarrow\quad
\exists a\mid M: a\equiv-1\pmod r,
\]

即恰为零溢出偶源尾存在的普通除子判据。

对 649 个存储的 \(r\le9999\) 首命中状态，精确 BFS 残数计算得到：

| (delta) | 状态数 |
| ---: | ---: |
| 0 | 558 |
| 1 | 75 |
| 2 | 13 |
| 3 | 2 |
| 4 | 1 |

所以全部 91 个高溢出状态在这个有限剖面中离普通除子目标至多四次支持素因子重复。
这给出可攻击的势量候选：若某个源转换、碰撞吸收或递归步骤能受控地补足这些重复，便会
强制零溢出尾。

但 \(\delta\) 是诊断量，不是证书：把额外素因子乘入一个抽象残数词并不表示它已实际整除
当前 \(M\)，也不自动产生新的源或递降。最大值 4 仅是当前 \(10^9\) H19、\(r\le9999\)
窗口的实验事实，不能外推为全称常数。

可复现命令：

~~~bash
python3 reproductions/type_ii_h19_zero_overflow_exponent_deficit.py \
  --input reproductions/type-ii-h19-bounded-r-overflow-profile-1b-results.json \
  --output reproductions/type-ii-h19-zero-overflow-exponent-deficit-1b-results.json
python3 -m unittest tests/test_type_ii_h19_zero_overflow_exponent_deficit.py -q
~~~
