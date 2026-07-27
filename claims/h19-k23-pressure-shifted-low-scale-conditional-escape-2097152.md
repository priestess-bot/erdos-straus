---
kind: claim
claim_id: h19-k23-pressure-shifted-low-scale-conditional-escape-2097152
title: H19-k23 压力进程平稳源与低尺度平移因子状态的联合 Dickson 逃逸
statement: 假定 Dickson 素数元组猜想，H19-k23 压力进程 p=748375048866405601+P*t 的一个周期细化子进程上，全部72个平稳标准外部源和所有满足已建立平移因子递降前提、且k<=1000的4个非平稳平移状态同时失败。细化周期为475540065；p及相应仿射余因子化简后仅有73个不同的正、本原、局部可采纳线性素数型。对标准源完整枚举平方除子残数；对平移状态完整枚举 n=F*L 中满足 d|k*f 的 f=f0 或 f0*L 两种最终素数余因子情形，均无 n/f=-1 mod(4k-1)。
claim_status: conditional
topics:
- type-I
- external-source
- shifted-external-source
- conditional
- dickson
- prime-tuples
- multi-scale
- pressure-family
- h19
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: external-source-descent
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 压力进程平稳源与低尺度平移因子状态的联合 Dickson 逃逸

从
[全部平稳标准外部源尺度的条件性逃逸](h19-k23-pressure-full-stationary-source-conditional-escape-2097152.md)
的压力进程出发，考察带平移参数的外部源因子形式

\[
q=4k-1,\qquad n=\frac{qp+d}{4k},\qquad p\equiv d\pmod{4k},\qquad d\mid kq. \tag{1}
\]

只保留 (k\le1000)、整条仿射进程上 (d\mid kn) 的非平稳状态。它们恰为

\[
(k,d)=(13,17),(121,69),(124,33),(790,81). \tag{2}
\]

取参数细化

\[
t=475540065u. \tag{3}
\]

这个数是 (2) 中 (q) 的最小公倍数，故每个余因子的模 (q) 残数固定。对每个状态写

\[
n(u)=F L(u), \tag{4}
\]

其中 (L(u)) 是足够大时要求为素数的本原仿射型。平移因子递降需要一个

\[
f\mid n,\qquad \frac nf\equiv-1\pmod q,\qquad d\mid kf. \tag{5}
\]

当 (L(u)) 是充分大的素数时，(5) 中最后一个整除条件迫使 (f) 的非 (L) 部分已
由固定因子承载。因此只须穷尽

\[
f=f_0\quad\hbox{或}\quad f=f_0L(u),\qquad f_0\mid F,quad d\mid kf_0. \tag{6}
\]

程序对 (2) 的所有 (f_0) 精确枚举；两种情形均不满足 (5)。与此同时，72 个平稳标准
源仍可用其完整平方除子残数表逐项排除。

将目标 (p(u))、72 个标准源余因子和 (2) 的平移余因子合并后，平移型中有重复，最终仅有
73 个不同线性型。它们全部正、本原且局部可采纳。Dickson 猜想因此给出无穷多个同时为素数的
参数；对充分大的这些参数，72 个平稳标准源和 (2) 的四个平移因子状态全都失败。

范围必须严格限定：这排除的是已建立的平移**因子形式**在 (k\le1000) 的所有进程可用状态，
不是对所有可能的平移 Type I 证书的分类，也不涉及更大或随参数增长的尺度、Type II 尾或其它
递降状态。

可复现命令：

~~~bash
python3 reproductions/h19_k23_pressure_shifted_low_scale_conditional_escape.py \
  --input reproductions/h19-k23-global-tail-pressure-external-source-bridge-2097152.json \
  --output reproductions/h19-k23-pressure-shifted-low-scale-conditional-escape-2097152.json
python3 -m unittest tests/test_h19_k23_pressure_shifted_low_scale_conditional_escape.py -q
~~~
