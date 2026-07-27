---
kind: claim
claim_id: h19-k23-global-tail-finite-support-menu-obstruction-2097152
title: H19-k23 全局尾的有限非基底素数支持障碍
statement: 在 H19-k23 的 72 尾规范 Type II 框架中，对任意固定有限素数集合 P，存在一条原始 p≡1 (mod 24) 等差进程，Dirichlet 定理给出其中无穷多个素数；对每个这样的素数及每个全局尾，x^2 的所有目标余数除子中均不存在一个其非基底素因子支持包含于 P 的除子，甚至在略去 d≤x 的证书大小条件后也是如此。因此固定有限素数支持的任何多因子模板库不能覆盖全部实际核心素数。
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

# H19-k23 全局尾的有限非基底素数支持障碍

这里固定一个有限素数集 \(P\)，但不再限制使用其中几个素数。对每个尾，允许的
Type II 除子可含任意多个 \(P\) 中素数、各自任意不超过在 \(x^2\) 中可用的幂；
唯一限制是除去该尾的规范基底后，所有剩余素因子都属于 \(P\)。

## 选择无原始余数除子的压力种子

二百万层压力记录中有

\[
p_0=955\,643\,834\,512\,728\,001,
\]

位于 \(v\equiv24\pmod{29}\) 分支。设 \(M_0\) 是它的全局基底失败周期，\(A\) 是
该分支的 \(p=At+C\) 系数。取有限局部集合

\[
R=
\{\ell:\ell\mid AM_0\}
\cup\{\ell\le73:\ell\text{ prime}\}
\bigcup_m\{\ell:\ell\mid (m+1)/4\}. \tag{1}
\]

最后一项保证所有固定的 \(q_m=(m+1)/4\) 因子都已列入；在此 72 尾菜单中它实际上
只增加 \(2,3,5,23\)。逐尾枚举所有支撑于
\(\mathcal B_m\cup R\) 的 \(x_m^2\) 除子，得到

\[
\{d:d\mid x_m^2,\ \operatorname{supp}(d)\subseteq\mathcal B_m\cup R,\
d\equiv-x_m\pmod m\}=\varnothing \qquad(72\text{ 个 }m). \tag{2}
\]

这里**没有**施加 \(d\le x_m\)。因此 (2) 不是某个余数除子暂时过大造成的有限范围
假象，后续进程变大也不会恢复它。

将周期加细为

\[
M=\operatorname{lcm}\left(M_0,
\{\ell^{v_\ell(u_m)+1}:m,\ell\in R\}\right),
\qquad u_m=\frac{p+m}{m+1}. \tag{3}
\]

这冻结所有尾的目标余数以及每个 \(R\) 素数在 \(u_m\) 中的精确赋值，故 (2) 在
\(t=t_0+Mn\) 的每一项上保持。

## 任意固定有限支持集

对任意有限 \(P\)，每个 \(\ell\in P\setminus R\) 满足

\[
\ell>73,\qquad \gcd(\ell,AM)=1.
\]

模 \(\ell\) 下，条件 \(\ell\mid p\) 至多排除一个外层参数余数，72 个条件
\(\ell\mid u_m\) 也各至多排除一个。因此至多有 73 个禁止余数；因
\(\ell>73\)，可选一个余数使 \(\ell\) 不整除 \(p\) 及所有 \(u_m\)。中国剩余定理
同时处理有限个 \(\ell\in P\setminus R\)。

在得到的原始 \(1\pmod{24}\) 等差进程上，\(P\setminus R\) 中任何素数都不可能出现于
任意 \(x_m=q_mu_m\)，而 \(P\cap R\) 已由 (2) 排除。因此对每个尾均有

\[
\nexists d\mid x_m^2:\quad
d\equiv-x_m\pmod m,\qquad
\operatorname{supp}(d)\setminus\mathcal B_m\subseteq P. \tag{4}
\]

式 (4) 仍略去了 \(d\le x_m\)，故特别排除合法的 Type II 证书。进程原始，Dirichlet
定理给出无穷多个实际素数项。

这排除了固定有限支持集上的零、一或任意多个非基底因子的模板库。它**不**排除根据每个
实际 \(u_m\) 的新素因子作无界自适应选择，也不排除改变全局尾菜单或递降状态；更不构成
Erdős--Straus 猜想的反例。

默认复现菜单同时含小素数、分歧素数和实际大变量素数
\(87\,060\,409\,452\,631\)：

~~~bash
python3 reproductions/h19_k23_global_tail_finite_support_menu_obstruction.py \
  --input reproductions/h19-k23-global-base-only-prime-obstruction-2097152.json \
  --output reproductions/h19-k23-global-tail-finite-support-menu-obstruction-2097152.json
python3 -m unittest tests/test_h19_k23_global_tail_finite_support_menu_obstruction.py -q
~~~
