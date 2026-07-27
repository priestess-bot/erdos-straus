---
kind: claim
claim_id: type-I-tail-reverse-simple-external-terminal-closure-500m
title: 五亿普通尾遗漏的低复杂度终止闭合
statement: 对p<=500000000的1,717个普通Type II尾遗漏，存在逐点不交的终止分区：1,683个由m<=127的线性或单素幂反向剩余量严格边闭合，26个由零偏移完整平方外源闭合，8个由偏移s=9或25的平方外源闭合。反向边在所有候选中最小化其非1 mod24终止素因子后，1,670条取q=2，余13条取q<=1453；外源边同样终止。故1717=1683+26+8且无未闭合点。这是有限目标侧选择器闭合，不是全局递降证明。
claim_status: computationally_reproduced
topics:
- type-I
- type-II
- descent
- reverse-lift
- external-source
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

# 五亿普通尾遗漏的低复杂度终止闭合

对五亿普通 Type II $p-1$ 尾抽缩的 $1{,}717$ 个遗漏，先尝试 Type I 最大尾反向边的

$$
S=\frac{E}{\gcd(E,4K)}=1\quad\text{或}\quad q^a,
$$

其中 $m\le127$。这给出 $1{,}683$ 条严格边。对余下 $34$ 点，独立平方外源分支给出

$$
1{,}717
=1{,}683_{\text{线性或单素幂反向}}
+26_{\text{零偏移平方外源}}
+8_{\text{平移平方外源}}. \tag{1}
$$

最后八条所需偏移仅为

$$
s\in\{9,25\},
$$

各有四条。因此，若以短反向边为优先分支，原先五亿平方外源审计中达到 $202{,}521$ 的偏移
记录不再出现在该混合闭合中。

对 (1) 中每条选中严格边的源分母完全分解，均可选到

$$
q\mid n,\qquad q\not\equiv1\pmod{24}.
$$

故每条源解都可按比例缩放接到既知终止素数类；没有仅由核心素因子组成的未终止源。为避免
“首个见证”夸大终止复杂度，反向分支穷尽同一有限盒中所有 $S=1$ 或 $q^a$ 的边，并按最小
终止素因子选择：$1{,}670$ 条取 $q=2$，仅 $13$ 条取奇素数，最大的最优终止素因子为

$$
q=1{,}453.
$$

这 $13$ 条不能选到偶终止因子的反向分支目标为

$$
6{,}294{,}649,\ 31{,}253{,}161,\ 36{,}873{,}769,\ 141{,}064{,}009,
179{,}700{,}889,\ 217{,}380{,}409,\ 259{,}005{,}289,\ 304{,}182{,}169,
316{,}324{,}969,\ 334{,}995{,}049,\ 403{,}925{,}449,\ 405{,}583{,}369,
493{,}936{,}249.
$$

它们是“低平方剩余量且可终止”选择器的下一批精确例外，不应被误读为猜想的反例。

这是一项强的有限闭合：它同时限制反向剩余量的素因子支撑和外源偏移，却仍依赖目标 $p$ 的
分解以选择分支。因此不能将 (1) 误写成对任意核心素数都可从源侧执行的递降定理。

可复现命令：

~~~bash
python3 reproductions/type_i_tail_reverse_single_surplus_profile.py
python3 reproductions/type_i_tail_reverse_single_surplus_terminal_minimization.py
python3 reproductions/type_i_tail_reverse_surplus_external_hybrid.py
python3 reproductions/type_i_tail_reverse_simple_external_terminal_closure.py
python3 -m unittest tests/test_type_i_tail_reverse_simple_external_terminal_closure.py -q
~~~
