---
kind: claim
claim_id: type-II-h19-zero-overflow-r-release-profile
title: H19 高溢出首个 r 状态的后续零溢出释放边界
statement: 对存储的91个 p<=10^9、r<=9999 首次偶源尾命中却最小溢出 B>1 的 H19 残余，用普通除子 a|(rp+1)/4、a=-1 mod r 判定零溢出，39个状态在 r<=9999 的后续 r 首次释放，52个未释放；再完整扫描 10007<=r<=99999 的连续兼容区间没有任何新增释放。因此增加 r 是真实但不充分的状态转移，不能单独构成一般零溢出选择器。
claim_status: computationally_reproduced
topics:
- type-I
- even-source
- overflow
- divisor-residues
- selector
- finite-audit
- h19
sources:
- paper: bradford2024
  locator: Proposition 1
  role: even-source-descent
visibility: public
last_checked: '2026-07-26'
---

# H19 高溢出首个 \(r\) 状态的后续零溢出释放边界

对每个已存的高溢出首命中状态，保留其素数 \(p\) 和首个命中参数 \(r_0\)。对每个

\[
r>r_0,\qquad r\equiv r_0\pmod 8,\qquad r\le9999
\]

先检查该 \(r\) 是否仍给出相容的偶源射线；若相容，令

\[
M=\frac{rp+1}{4}.
\]

由[奇距离偶源零溢出尾的普通除子判据](odd-distance-even-source-zero-overflow-divisor-criterion.md)，
零溢出当且仅当存在 \(a\mid M\) 使

\[
a\equiv-1\pmod r. \tag{1}
\]

这不是新增近似条件，而是原尾条件的精确等价改写。

在 \(p\le10^9\) 的 91 个 \(B>1\) 首命中状态上，得到：

| 后续 \(r\) 审计范围 | 状态数 |
| --- | ---: |
| 首个后续兼容 \(r\) 即满足 (1) 或随后首次满足 (1) | 39 |
| 至 \(r=9999\) 仍不满足 (1) | 52 |
| 合计 | 91 |

例如 \(p=13\,659\,409\) 从 \(r_0=71\) 在 \(r=143\) 释放，
\(p=78\,097\,321\) 从 \(r_0=23\) 在 \(r=39\) 释放；另一方面
\(p=605\,553\,001\) 的首命中 \(r_0=311\) 至该界仍未释放。

所以改变 \(r\) 的确能把一部分指数不足状态转成普通除子命中，因而应作为候选源转换的一部分。
但 52 个未释放状态排除了“只要继续增大 \(r\)，必然很快获得零溢出尾”的有限窗口版本。
任何一般定理仍须额外控制 \(M\) 的因子指数，或提供二次外部源、碰撞吸收等另一出口。

这个边界并非只停在 \(9999\)：把 \(r\equiv7\pmod8\) 的后续区间完整分为

\[
[10007,19999],\ [20007,29999],\ \ldots,\ [90007,99999],
\]

并对每个区间重新执行兼容因子对和普通除子测试，九段均为零新增释放。因此至
\(r=99999\) 的累计数仍为 39 个释放、52 个未释放。这不是“永不释放”的证明，但把
仅靠扩大 \(r\) 的空窗推高了一个数量级。

释放也通常不把问题简化成单侧因子命中。对 39 个释放状态，在其释放 \(r\) 逐项枚举所有
兼容半因子对并按[交叉半因子判据](odd-distance-even-source-cross-half-factor-zero-overflow.md)分类，
得到 67 条兼容射线：57 条本质跨侧、6 条仅左侧命中、4 条仅右侧命中。更强地，39 个状态中
33 个的全部兼容射线都本质跨侧；只有 2 个状态仅有左侧命中，4 个状态同时有左、右单侧选择。
因此变量 \(r\) 是实际释放机制，但不能被理解为把复杂双侧积集稳定降阶为单侧除子问题。

该计算一共扫描 61,920 个候选 \(r\)，其中 641 个通过射线相容性预筛；当前精确实现的
整次离线审计约需 17 秒。故当前范围内 Python/SymPy 并非研究瓶颈；扩展范围时，主要成本会是
这 641 个候选的整数分解，而非普通循环。

可复现命令：

~~~bash
python3 reproductions/type_ii_h19_zero_overflow_r_release_profile.py \
  --input reproductions/type-ii-h19-bounded-r-overflow-profile-1b-results.json \
  --r-cap 9999 \
  --output reproductions/type-ii-h19-zero-overflow-r-release-profile-1b-results.json
python3 -m unittest tests/test_type_ii_h19_zero_overflow_r_release_profile.py -q
python3 reproductions/type_ii_h19_zero_overflow_r_release_cross_profile.py \
  --input reproductions/type-ii-h19-zero-overflow-r-release-profile-1b-results.json \
  --output reproductions/type-ii-h19-zero-overflow-r-release-cross-profile-1b-results.json
python3 -m unittest tests/test_type_ii_h19_zero_overflow_r_release_cross_profile.py -q
for start in $(seq 10007 10000 90007); do
  end=$((start + 9992))
  python3 reproductions/type_ii_h19_zero_overflow_r_release_profile.py \
    --r-start "$start" --r-cap "$end" \
    --output "reproductions/type-ii-h19-zero-overflow-r-release-profile-1b-r${start}-${end}-results.json"
done
python3 reproductions/type_ii_h19_zero_overflow_high_r_gap_profile.py
python3 -m unittest tests/test_type_ii_h19_zero_overflow_high_r_gap_profile.py -q
~~~
