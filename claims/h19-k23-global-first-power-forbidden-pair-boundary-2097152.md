---
kind: claim
claim_id: h19-k23-global-first-power-forbidden-pair-boundary-2097152
title: H19-k23 全局压力尾的一次幂禁止余数对边界
statement: 对二百万层 H19-k23 的22条全局基底压力进程及每一条72个全局尾，共1,584个尾状态中，去除规范基底后的实际非基底总余数均可写成两个均不允许构成一次幂 Type II 证书的单位余数之积。因此逐尾的基底状态和非基底总余数，即使允许一个两因子分解模型，也不能强迫一个可用的一次幂素因子。
claim_status: computationally_reproduced
topics:
- type-II
- factor-support
- residue-classes
- one-factor
- cross-tail
- global-tail-menu
- pressure-set
- computation
- h19
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-criterion
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 全局压力尾的一次幂禁止余数对边界

固定一个压力种子和一个全局尾 \(m=4q-1\)，写

\[
x=qu,\qquad
T=-x\pmod m.
\]

令 \(D_{\mathcal B}\) 是 \(x^2\) 所有规范基底除子的模 \(m\) 残数。一个新素数
\(\ell\) 的一次幂能构成 Type II 证书，当且仅当

\[
\ell\bmod m\in
R:=T D_{\mathcal B}^{-1}. \tag{1}
\]

把单位群中其余的残数记为 \(F=(\mathbb Z/m\mathbb Z)^\times\setminus R\)。从 \(u\)
剥离该尾全部规范基底素数幂后，记剩余非基底部分为 \(N\)。

脚本对 22 条压力进程和完整 72 尾菜单的每个状态，穷尽 \(D_{\mathcal B}\) 与单位群，
并直接查找

\[
r,s\in F,\qquad rs\equiv N\pmod m. \tag{2}
\]

结果是

\[
22\times72=1\,584_{\text{states}}
=1\,584_{\text{forbidden-pair states}}+0_{\text{misses}}. \tag{3}
\]

每个状态至少有一个这样的有序对；最多的状态有 \(135\,390\) 个可选对，其中 22 个状态
恰有一个对。

式 (2) 不断言实际仿射 \(u\) 会分解为两个对应素数，也不同时实现不同尾的因子化。
它严格排除的只是一个局部论证模式：仅从某一尾的规范基底、非基底总余数和“两因子”形式，
不能推出必有一个因子落入允许集 \(R\)。因此
[跨尾一次幂选择器](h19-k23-global-first-power-selector-conjecture.md) 的任何证明必须使用
不同尾之间的仿射关系、真实因子分布，或在联合未命中时给出另一种递降，而不能逐尾独立
地作乘积余数抽屉论证。

可复现命令：

~~~bash
python3 reproductions/h19_k23_global_first_power_forbidden_pair_boundary.py \
  --input reproductions/h19-k23-global-base-only-prime-obstruction-2097152.json \
  --output reproductions/h19-k23-global-first-power-forbidden-pair-boundary-2097152.json
python3 -m unittest tests/test_h19_k23_global_first_power_forbidden_pair_boundary.py -q
~~~
