---
kind: claim
claim_id: h19-k23-uniform-tail-base-invariant
title: H19-k23 普通双尾的最大统一基底不变量
statement: 设14条 H19-k23 残存进程为 p=A t+C_i。对每个全局可用的尾缺口 m=4q-1，令 u=(p+m)/(m+1)=a t+b_i，则 g_m=gcd(a,b_1,...,b_14) 是整除所有分支、所有参数 u 的最大整数。故 B_m=rad(qg_m) 是由仿射数据强制的规范支持基底。在m=31,35,39,47,59,71,79,91,95处，(g_m,B_m) 分别为 (133,{2,7,19})、(13,{3,13})、(1,{2,5})、(1,{2,3})、(7,{3,5,7})、(1,{2,3})、(1,{2,5})、(1,{23})、(1,{2,3})；m=63不在全部14条进程上全局可用。
claim_status: established
topics:
- type-II
- descent
- affine-progressions
- factor-support
- h19
sources:
- paper: bradford2024
  locator: Proposition 2
  role: ordinary-Type-II-tail-context
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 普通双尾的最大统一基底不变量

将 14 条 H19-k23 残存进程写为

\[
p=A t+C_i\qquad(1\le i\le14). \tag{1}
\]

考虑一个在每条进程上都可用的普通双尾缺口 \(m=4q-1\)，即

\[
4q\mid A,\qquad 4q\mid C_i-1\quad(1\le i\le14). \tag{2}
\]

于是

\[
u_i(t)=\frac{p+m}{4q}=a t+b_i,
\quad a=\frac A{4q},\quad b_i=\frac{C_i+m}{4q}. \tag{3}
\]

定义

\[
g_m=\gcd(a,b_1,\ldots,b_{14}),\qquad B_m=\operatorname{rad}(qg_m). \tag{4}
\]

## 最大性

显然 \(g_m\mid u_i(t)\) 对所有 \(i,t\) 成立。反过来，若 \(h\) 整除全部
\(u_i(t)\)，取 \(t=0,1\) 可得

\[
h\mid u_i(1)-u_i(0)=a,\qquad h\mid u_i(0)=b_i,
\]

故 \(h\mid g_m\)。因此 (4) 给出的是精确的、最大的一致因子，而不只是某个方便的
固定因子。把 \(q\) 的素因子加入后，\(B_m\) 正好是 \(x=qu\) 的统一素因子支持。

## H19-k23 的结果

| 尾缺口 \(m\) | 全局可用 | \(q\) | \(g_m\) | \(B_m\) |
|---:|:---:|---:|---:|:---|
| 31 | 是 | 8 | 133 | \(\{2,7,19\}\) |
| 35 | 是 | 9 | 13 | \(\{3,13\}\) |
| 39 | 是 | 10 | 1 | \(\{2,5\}\) |
| 47 | 是 | 12 | 1 | \(\{2,3\}\) |
| 59 | 是 | 15 | 7 | \(\{3,5,7\}\) |
| 63 | 否 | 16 | -- | -- |
| 71 | 是 | 18 | 1 | \(\{2,3\}\) |
| 79 | 是 | 20 | 1 | \(\{2,5\}\) |
| 91 | 是 | 23 | 1 | \(\{23\}\) |
| 95 | 是 | 24 | 1 | \(\{2,3\}\) |

这严格解释了支持度二梯中 31、35、39、47、59 和末端 71、79、91、95 的阶段基底。
\(m=63\) 不满足 (2)，所以只能在经过前序筛选的子样本上讨论；不能把它误称为
14 条进程的统一层。

这个引理没有给出 \(\delta_{B_m}\le2\)：它只消除了基底选择的任意性，把真正未解决的
问题收缩为规范基底下跨缺口支持缺陷的下降或逃逸定理。

重建命令：

~~~bash
python3 reproductions/h19_k23_uniform_tail_base_invariants.py
python3 -m unittest tests/test_h19_k23_uniform_tail_base_invariants.py -q
~~~
