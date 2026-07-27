---
kind: claim
claim_id: type-I-mixed-terminal-sparse-tail-600m
title: 六亿稀疏尾遗漏族的混合终端闭合
statement: 对q在[20833334,24999999]且q与p=24q+1均为素数的32,394个点，完整枚举p-1的普通Type II双尾条件后有32,320个直接命中；其余74个全部存在m<=215、B=1的Type I正规形，并有偶桥E|4K^2给出严格偶源。最大首选缺口为71。因此该明确的五亿至六亿稀疏族在有界Type I分支中完全闭合。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- type-II
- descent
- even-source
- normal-form
- mixed-selector
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I/II divisor certificate context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II factorization context
visibility: public
last_checked: '2026-07-27'
---

# 六亿稀疏尾遗漏族的混合终端闭合

令

$$
p=24q+1,\quad\quad
20{,}833{,}334\le q\le24{,}999{,}999,\quad\quad p,q\text{ 均为素数}.
$$

这是严格落在五亿与六亿之间的一个稀疏核心素数族。因为

$$
p-1=2^3\cdot3\cdot q,
$$

普通 Type II 双尾分支只须完整检查八个候选

$$
d\in\{4,8,12,24,4q,8q,12q,24q\},\quad\quad m=d-1.
$$

对每个候选，脚本穷尽

$$
e\mid\left(\frac{p+d-1}{4}\right)^2,\quad\quad
e\le\frac{p+d-1}{4},\quad\quad
e\equiv-\frac{p+d-1}{4}\pmod {d-1},
$$

并重建 Type II 目标与双尾去 $p$ 后的严格源。对全部普通尾遗漏，按 $m$ 递增搜索

$$
3\le m\le215,\quad\quad m\equiv3\pmod4,\quad\quad B=1
$$

下每个到达缺口的全部 Type I 正规形及最大尾的所有 $E\mid4K^2$ 桥，并在首个偶源后停止。

## 结果

| 项目 | 数值 |
|---|---:|
| 族内核心素数 | 32,394 |
| 普通 Type II 双尾命中 | 32,320 |
| 普通尾遗漏 | 74 |
| Type I $B=1$ 偶源命中 | 74 |
| Type I 偶源遗漏 | 0 |
| 最大首选 Type I 缺口 | 71 |

达到最大缺口的两点为

$$
500{,}019{,}529,\quad\quad584{,}044{,}729.
$$

前者的首个终端见证为

$$
m=71,\quad\quad(A,B,C)=(30489,1,4100),\quad\quad n=27{,}744{,}864.
$$

因此在这个明确定义的族中有精确分流

$$
32{,}394=32{,}320_{\text{ordinary Type II tail}}
+74_{\text{Type I }B=1\text{ even source}}. \tag{1}
$$

## 边界

式 (1) 是一个有限、目标侧的闭合，不是混合终端选择引理的证明。它只覆盖
$p=24q+1$ 且 $q$ 为素数的给定区间；第二分支还明确限制了 $B=1$ 与 $m\le215$。它的
作用是把反例搜索推进到已有五亿全体审计之外，并在一类低复杂度 $p-1$ 因子格中检验完整
平方桥，而不是从高覆盖率推出全称规律。

可复现命令：

~~~bash
python3 reproductions/type_i_mixed_terminal_sparse_tail_600m.py
python3 -m unittest tests/test_type_i_mixed_terminal_sparse_tail_600m.py -q
~~~
