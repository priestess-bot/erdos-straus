---
kind: claim
claim_id: h19-k23-one-factor-aggregate-residue-boundary-2097152
title: H19-k23 一因子选择器的单尾聚合残数边界
statement: 对H19-k23二百万层的22条全局基底压力记录，在其当前尾上，即使给定非基底部分的总模残数和精确素因子重数Omega，也不能仅由这些聚合数据强迫一个可用的一新增素因子：每条记录都存在同一长度、完全由禁止残数构成且乘积总残数相同的残数模型。
claim_status: computationally_reproduced
topics:
- type-II
- factor-support
- residue-classes
- one-factor
- global-tail-menu
- pressure-set
- h19
- computation
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-criterion
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 一因子选择器的单尾聚合残数边界

在一个压力状态的当前尾 \(m=4q-1\) 上，设 \(D_B\) 是 \((qu)^2\) 的所有规范
基底除子残数，目标为

\[
T=-qu\pmod m.
\]

若一个非基底素因子 \(\ell\) 的一次幂可与某个基底除子组成一因子证书，则必须有

\[
\ell\bmod m\in R:=T D_B^{-1}. \tag{1}
\]

把单位剩余类中不属于 \(R\) 的部分记作 \(F\)。一个看似可行的证明思路是：仅由非基底
部分 \(N\) 的总残数 \(N\bmod m\)，或再加上精确素因子重数 \(\Omega(N)\)，推出至少一个
素因子必须落在 \(R\)。

对二百万层的 22 条全局基底压力记录，脚本逐条计算 \(R\)、\(F\)、\(N\bmod m\) 和
\(\Omega(N)\)。对每一条都构造出一个长度恰为 \(\Omega(N)\) 的残数列

\[
(f_1,\ldots,f_{\Omega(N)}),\qquad f_i\in F,
\]

满足

\[
f_1\cdots f_{\Omega(N)}\equiv N\pmod m. \tag{2}
\]

因此精确结果为

\[
22_{\text{pressure states}}=0_{\text{aggregate-residue forced}}. \tag{3}
\]

(2) 是一个有限单位群上的动态规划构造，不依赖概率假设。它说明在这些状态中，单尾的
“总乘积余数加因子个数”并没有足够信息推出一个可用素因子。

这不是实际反例构造：脚本没有声称存在一个真实仿射 \(u\) 恰好具有 (2) 的禁止素因子
分解，而实际压力记录本身确有可用因子。它排除的只是一个证明方法，即从单尾聚合模数据
直接强迫一因子。后续正向论证必须利用更强的信息，例如跨尾 \(u_d\) 的仿射关联，或素因子
大小、分布与参数进程之间的关系。

可复现命令：

~~~bash
python3 reproductions/h19_k23_one_factor_aggregate_residue_boundary.py \
  --input reproductions/h19-k23-global-tail-base-only-descent-2097152.json \
  --output reproductions/h19-k23-one-factor-aggregate-residue-boundary-2097152.json
python3 -m unittest tests/test_h19_k23_one_factor_aggregate_residue_boundary.py -q
~~~
