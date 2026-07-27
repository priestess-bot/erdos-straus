---
kind: claim
claim_id: type-I-tail-reverse-even-source-closure-500m
title: 五亿普通尾遗漏的偶源反向二尾闭合
statement: 对p<=500000000的1,717个普通Type II p-1尾遗漏，完整枚举m<=215的Type I正规形和严格最大尾反向边后，每个p均有偶数源n<p。故源解可由n=2的解按比例缩放获得，所有1,717点有直接终止证书。首个偶源边的最大缺口215，且p=493936249在m<=211无偶源边、于m=215首次命中。该结果是有限目标侧闭合，不是全局源侧选择定理。
claim_status: computationally_reproduced
topics:
- type-I
- type-II
- descent
- reverse-lift
- even-source
- terminal-factor
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: certificate-and-lift-context
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization-context
visibility: public
last_checked: '2026-07-27'
---

# 五亿普通尾遗漏的偶源反向二尾闭合

对普通 Type II $p-1$ 尾抽缩留下的全部 $1{,}717$ 个素数，枚举

$$
3\le m\le215,\qquad m\equiv3\pmod4
$$

内的所有 Type I 正规形及其严格最大尾反向边。每个目标均可选到一个偶数源分母

$$
2\le n<p,\qquad 2\mid n. \tag{1}
$$

对 $n=2t$，已知 $4/2=1+1/2+1/2$ 按比例缩放即给出

$$
\frac4n=\frac1t+\frac1{2t}+\frac1{2t}. \tag{2}
$$

因此 (1) 中的每一条严格边都不是仅有“较小实例”的标记递降，而是可直接接到终止基底的
显式证书。审计得到

$$
1{,}717=1{,}717_{\text{偶源反向二尾}},\qquad\text{遗漏}=\varnothing. \tag{3}
$$

首个偶源边的缺口最大为 $215$。最大点为

$$
p=493{,}936{,}249,\qquad m=215,\qquad n=445{,}691{,}332.
$$

因为搜索按 $m$ 递增并对每个 $m$ 穷尽全部正规形和严格边，该点在同一选择器的
$m\le211$ 盒中没有偶源边。另两个较大首缺口是

$$
81{,}209{,}209\ (m=151),\qquad334{,}995{,}049\ (m=135).
$$

这比“低平方剩余量或外源”的有限菜单更统一：它只保留一个 Type I 反向选择器和固定终止类
$2\mathbb Z$。代价是必须允许 $m$ 到 $215$，且 $B$ 不再有小常数上界。更根本地，选择仍然从
目标 $p$ 的因子状态出发，所以不能据此断言对任意核心素数存在可从源侧维护的全称规则。

可复现命令：

~~~bash
python3 reproductions/type_i_tail_reverse_even_source_closure.py
python3 -m unittest tests/test_type_i_tail_reverse_even_source_closure.py -q
~~~
