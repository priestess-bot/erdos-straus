---
kind: claim
claim_id: h19-k23-global-tail-finite-menu-obstruction-2097152
title: H19-k23 全局尾的一新增素因子有限模板障碍
statement: 在H19-k23的72尾规范Type II框架中，对任意有限素数集合P，都存在一条原始p≡1 (mod 24)等差进程，Dirichlet定理给出其中无穷多个素数；对每个这样的素数，所有全局尾均无零缺陷基底证书，且不存在非基底支持至多一、其唯一非基底素因子属于P的证书。因此任何固定有限的一新增素因子模板库不能覆盖全部实际核心素数。
claim_status: established
topics:
- type-II
- descent
- p-minus-one
- global-tail-menu
- factor-support
- finite-menu
- crt
- dirichlet
- h19
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-criterion
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 全局尾的一新增素因子有限模板障碍

这里的“有限模板库”指一个固定有限素数集 \(P\)。库中一个模板允许使用规范基底、再乘
\(P\) 中一个素数的任意正幂；也就是非基底支持至多一。结论不处理两个或更多非基底
素因子的模板。

从二百万层压力进程中选取

\[
p_0=2\,729\,866\,198\,796\,697\,601,
\]

它位于残存分支 \(v\equiv16\pmod{29}\)，并满足全部 72 个全局尾的规范基底零缺陷失败。
令 \(M_0\) 为该失败状态的冻结周期。

## 有限局部素数

定义有限集合

\[
R=\{\ell\le73:\ell\text{ prime}\}
\cup\{\ell:\ell\mid AM_0\}. \tag{1}
\]

脚本逐尾穷尽规范基底除子及每个 \(\ell\in R\) 的所有合法幂，发现该种子没有任何
\(\ell\in R\) 的一新增因子证书。再将周期加细为

\[
M=\operatorname{lcm}\left(
M_0,\{\ell^{v_\ell(u_m)+1}:m,\ell\in R\}
\right), \tag{2}
\]

从而冻结每条 \(u_m\) 的这些局部赋值。故 \(R\) 中任意素数在整个进程
\(t=t_0+Mn\) 上仍不能形成一新增因子证书。

## 任意有限菜单的 CRT 避开

对任意有限 \(P\)，集合 \(P\setminus R\) 的每个素数 \(\ell\) 都满足

\[
\ell>73,\qquad \gcd(\ell,AM)=1.
\]

模 \(\ell\) 下，\(\ell\mid p\) 至多给出一个参数根，而 72 个条件
\(\ell\mid u_m\) 各至多给出一个根。因此至多 73 个外层参数余数不能使用。因为
\(\ell>73\)，可选一个同时避开 \(p\) 与所有 \(u_m\) 的余数；中国剩余定理将
所有 \(\ell\in P\setminus R\) 的避免条件合并。

所得进程是原始的 \(1\pmod{24}\) 等差数列。Dirichlet 定理给出无穷多个素数项。对每个
这样的素数：

\[
\begin{array}{c}
\text{全部 72 尾都无规范基底零缺陷证书},\\
\text{不存在唯一非基底素因子属于 }P\text{ 的规范证书}.
\end{array} \tag{3}
\]

所以固定有限的一新增素因子库不能完成全局尾覆盖。默认复现菜单同时包含小素数、分歧
素数和 \(87\,060\,409\,452\,631\) 这个实际的大变量素数，仍得到 (3)。

这严格留下两条未排除的正向路径：根据实际因子化作无界选择，或使用至少两个非基底
素因子/不同的递降状态。它不构成 Erdos-Straus 猜想的反例。

可复现命令：

~~~bash
python3 reproductions/h19_k23_global_tail_finite_menu_obstruction.py \
  --input reproductions/h19-k23-global-base-only-prime-obstruction-2097152.json \
  --output reproductions/h19-k23-global-tail-finite-menu-obstruction-2097152.json
python3 -m unittest tests/test_h19_k23_global_tail_finite_menu_obstruction.py -q
~~~
