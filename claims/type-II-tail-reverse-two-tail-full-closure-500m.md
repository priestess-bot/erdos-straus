---
kind: claim
claim_id: type-II-tail-reverse-two-tail-full-closure-500m
title: 五亿核心素数的普通尾与反向二尾全严格递降闭合
statement: 对p<=500000000的3,292,848个核心素数，3,291,131个有普通Type II尾抽缩严格递降；其全部1,717个遗漏与短反向二尾审计的1,717条记录逐点相同，故无遗漏。于是3,292,848=3,291,131+1,717给出该范围的全严格递降闭合；反向分支最大缺口127。该结论是目标侧有限选择器的计算闭合，不是全局归纳证明。
claim_status: computationally_reproduced
topics:
- type-I
- type-II
- descent
- reverse-lift
- finite-audit
- closure
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: divisor-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 五亿核心素数的普通尾与反向二尾全严格递降闭合

将 [五亿普通 Type II 尾遗漏的反向二尾全闭合](type-II-tail-reverse-two-tail-closure-500m.md)
与完整普通尾审计逐点拼接。两个机器可读结果满足：

$$
\{p:\text{普通 Type II 尾抽缩未命中}\}
=\{p:\text{存储的反向二尾边命中}\}. \tag{1}
$$

集合两侧均有 $1{,}717$ 个元素；它们不是仅比较计数，而是逐个素数的集合相等。于是

$$
3{,}292{,}848
=3{,}291{,}131_{\text{普通 Type II 尾严格递降}}
+1{,}717_{\text{反向二尾严格递降}}. \tag{2}
$$

故对所有

$$
p\le500{,}000{,}000,\qquad p\equiv1\pmod{24},
$$

都已有一条显式且严格小于 $p$ 的源边。反向分支的最大选中缺口为 $127$。

这比早先依赖平移平方外源的五亿分层闭合更紧凑：普通尾遗漏无需再分为外源可解与外源
压力两类。

## 限制

普通尾分支具有已参数化的递降构造。反向二尾分支则先读取目标 $p$ 的 Type I 正规形，再
从其因子状态构造源边。因此 (2) 是强的有限计算闭合，却不是对任意核心素数可递归执行的
统一引理；证明猜想仍需将该目标侧选择转化为源侧可维护的规则。

可复现命令：

~~~bash
python3 reproductions/type_ii_tail_reverse_two_tail_full_closure.py \
  --tail reproductions/type-ii-tail-deflation-500m-full-results.json \
  --reverse reproductions/type-ii-tail-reverse-two-tail-500m-all-misses-results.json \
  --output reproductions/type-ii-tail-reverse-two-tail-full-closure-500m-results.json
python3 -m unittest tests/test_type_ii_tail_reverse_two_tail_full_closure.py -q
~~~
