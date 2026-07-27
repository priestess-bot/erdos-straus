---
kind: claim
claim_id: h19-k23-global-base-only-prime-obstruction-2097152
title: H19-k23 全局规范基底证书的无限素数参数障碍
statement: H19-k23 的2,097,152层全局基底压力集中的22个素数种子各自给出一条原始参数等差进程；对该进程的每个参数，72个全局尾均没有相对于规范基底的目标残数除子。因此由Dirichlet定理，每条进程包含无穷多个p≡1 (mod 24)的素数，且这些实际核心素数在完整全局尾菜单中均无规范基底零缺陷Type II证书。
claim_status: established
topics:
- type-II
- descent
- p-minus-one
- global-tail-menu
- canonical-base
- affine-progressions
- crt
- dirichlet
- h19
sources:
- paper: bradford2024
  locator: Proposition 2
  role: ordinary-Type-II-tail-context
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 全局规范基底证书的无限素数参数障碍

记 14 条 H19-k23 残存进程中的一条为

\[
p(t)=At+C,
\]

并固定完整全局尾菜单

\[
\mathcal G=\{m: m+1\mid165600,\quad 4\mid m+1\}.
\]

对 \(m=4q-1\in\mathcal G\)，令

\[
u_m(t)=\frac{p(t)+m}{m+1}=a_m t+b_m.
\]

该尾的规范基底只含有限个素数 \(B_m\)。零缺陷证书存在当且仅当
\((qu_m(t))^2\) 中只由 \(B_m\) 支撑的某个除子命中目标

\[
d\equiv-q u_m(t)\pmod m. \tag{1}
\]

## 周期冻结引理

取一个压力种子 \(t_0\)，它在全部 72 个全局尾上都没有零缺陷证书。对每个
\(m\in\mathcal G\) 和 \(\ell\in B_m\)，记

\[
e_{m,\ell}=v_\ell(u_m(t_0)).
\]

令

\[
M=\operatorname{lcm}\left(
\{m:m\in\mathcal G\}\cup
\{\ell^{e_{m,\ell}+1}:m\in\mathcal G,\ \ell\in B_m\}
\right). \tag{2}
\]

则对任意 \(n\ge0\)，在 \(t=t_0+Mn\) 上：

1. \(M\equiv0\pmod m\)，故 (1) 的目标残数不变；
2. \(a_mMn\) 被 \(\ell^{e_{m,\ell}+1}\) 整除，故每个
   \(v_\ell(u_m(t))=e_{m,\ell}\) 不变；
3. 所有规范基底除子及其模 \(m\) 的残数不变。

脚本对每个种子作了更强的精确检查：在每个 \(m\in\mathcal G\)，即使去掉
\(d\le qu_m(t_0)\) 的大小限制，也没有任何规范基底除子命中 (1)。因此这种失败在
所有 \(t_0+Mn\) 上保持，而不是仅在有限样本或前两个周期中保持。

## 无穷多个实际核心素数

二百万层压力产物中的 22 个种子全部满足上述条件。对每个种子，脚本恢复唯一的残存
分支并验证

\[
\gcd(AM,p(t_0))=1,\qquad
p(t_0)\equiv1\pmod{24},\qquad
AM\equiv0\pmod{24}. \tag{3}
\]

所以

\[
p_n=p(t_0)+AMn \tag{4}
\]

是原始的 \(1\pmod{24}\) 等差数列。由 Dirichlet 关于等差数列中素数的定理，每一条
(4) 含无穷多个素数；对这些素数，72 个全局尾全都不存在规范基底零缺陷 Type II
证书。

这严格提升了“每个尾存在某个未覆盖参数状态”的旧边界：这里同一条原始素数进程同时
避开**全部**全局尾的规范基底证书。

## 含义与边界

结论没有排除使用 \(u_m(t)\) 的非基底素因子的 Type II 证书，也没有给出原猜想的
反例。它排除的是更窄但此前仍可能的路线：用固定的全局尾菜单和规范基底零缺陷证书
覆盖全部实际核心素数。

因此任何沿该菜单继续的正向证明必须至少做到下列之一：

1. 自适应地引入无界非基底因子；
2. 把这种一因子状态变换为可提升的递降状态；
3. 改变尾菜单或被保留的下降状态。

可复现命令：

~~~bash
python3 reproductions/h19_k23_global_base_only_prime_obstruction.py \
  --input reproductions/h19-k23-global-tail-base-only-descent-2097152.json \
  --output reproductions/h19-k23-global-base-only-prime-obstruction-2097152.json
python3 -m unittest tests/test_h19_k23_global_base_only_prime_obstruction.py -q
~~~
