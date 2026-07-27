---
kind: claim
claim_id: h19-k23-global-tail-large-prime-menu-obstruction-2097152
title: H19-k23 全局尾的大素数有限模板障碍
statement: 固定二百万层压力集导出的一条全局规范基底失败进程。对任意有限个两两不同的素数ell>73，若每个ell与该进程的系数及基底周期互素，则可用CRT构造一条原始p≡1 (mod 24)进程，使每个ell都不整除p或72个全局尾的任何变量因子u_m。Dirichlet定理给出无穷多个实际核心素数；它们同时避开该有限大素数菜单，且仍无任何全局规范基底零缺陷证书。
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

# H19-k23 全局尾的大素数有限模板障碍

从 [全局规范基底证书的无限素数参数障碍](h19-k23-global-base-only-prime-obstruction-2097152.md)
取一条压力进程

\[
p(t_0+Mn)=p_0+AMn,
\]

其中对每个 \(n\)，完整 72 尾菜单仍无规范基底零缺陷证书。

对一个全局尾 \(m\)，变量因子为

\[
u_m(n)=\frac{p(t_0+Mn)+m}{m+1}.
\]

令 \(\ell>73\) 是与 \(AM\) 互素的素数。模 \(\ell\) 下：

1. \(\ell\mid p(t_0+Mn)\) 至多给出一个 \(n\) 根；
2. 对每个 72 个全局尾，\(\ell\mid u_m(n)\) 至多给出一个 \(n\) 根。

所以至多有

\[
1+72=73
\]

个禁止余数类。因为 \(\ell>73\)，存在一个余数类同时满足

\[
\ell\nmid p(t_0+Mn),
\qquad
\ell\nmid u_m(n)\quad\text{for every global }m. \tag{1}
\]

对任意有限个两两不同且同样未分歧的大素数，把这些局部避免类用中国剩余定理合并。
所得进程仍保持 \(t\equiv t_0\pmod M\)，故保留全局基底失败；同时不含菜单中任何素数
作为任何尾的变量因子。进程系数与常数项互素，且恒为 \(1\pmod{24}\)，所以 Dirichlet
定理给出无穷多个实际核心素数。

默认例子使用

\[
\{97,101,103,107,113,127,131\},
\]

并逐项检验所有 72 个变量因子均避开该菜单。

这把 [固定尾的有限变量素数模板障碍](h19-k23-finite-variable-menu-obstruction.md) 从一个
\(m=31\) 尾提升到完整全局尾菜单，但有明确边界：这里仅处理大于 73 且不整除 \(AM\)
的菜单素数。有限小素数或分歧素数的全局同时避免尚未由此结论覆盖；更不排除根据实际
因子化无界选择的因子。

可复现命令：

~~~bash
python3 reproductions/h19_k23_global_tail_large_prime_menu_obstruction.py \
  --input reproductions/h19-k23-global-base-only-prime-obstruction-2097152.json \
  --output reproductions/h19-k23-global-tail-large-prime-menu-obstruction-2097152.json
python3 -m unittest tests/test_h19_k23_global_tail_large_prime_menu_obstruction.py -q
~~~
