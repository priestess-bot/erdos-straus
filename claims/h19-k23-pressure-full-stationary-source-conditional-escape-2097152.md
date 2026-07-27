---
kind: claim
claim_id: h19-k23-pressure-full-stationary-source-conditional-escape-2097152
title: H19-k23 压力进程全部平稳外部源尺度的 Dickson 条件性逃逸
statement: 假定 Dickson 素数元组猜想，存在无穷多个 H19-k23 实际核心素数位于压力进程 p=748375048866405601+P*t，使其全部72个平稳标准外部源尺度 k|41400 均没有完整平方因子外部源严格递降。对每个尺度，源分母分解为固定因子 F_k 乘唯一仿射余因子 L_k(t)；p 与全部72个 L_k 组成正、本原、局部可采纳的73元线性素数型。若它们同时为素数，则逐尺度完整枚举 (kF_kL_k)^2 的除子残数均避开目标。
claim_status: conditional
topics:
- type-I
- external-source
- conditional
- dickson
- prime-tuples
- stationary-scale
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

# H19-k23 压力进程全部平稳外部源尺度的 Dickson 条件性逃逸

取固定因子桥未命中的压力进程

\[
p(t)=748375048866405601+Pt. \tag{1}
\]

整条进程上可保持平稳的标准外部源尺度恰为

\[
k\mid\gcd\left(\frac{p(0)-1}{4},\frac P4\right)=41400, \tag{2}
\]

共有 72 个。对每个这样的 (k)，令 (q_k=4k-1) 及

\[
n_k(t)=\frac{q_kp(t)+1}{4k}=F_kL_k(t), \tag{3}
\]

其中 (F_k) 是仿射系数与常数项的最大公因子，(L_k) 是正本原仿射型。由于尺度平稳，
(L_k(t)\bmod q_k) 固定。

完整平方因子外部源在尺度 (k) 成立当且仅当

\[
e\mid(kF_kL_k(t))^2,\qquad
e\equiv-kF_kL_k(t)\pmod {q_k}. \tag{4}
\]

若 (L_k(t)) 是足够大的素数，则 (4) 左侧的所有除子残数由固定部分
((kF_k)^2) 与 (L_k) 的指数 (0,1,2) 完全列出。程序对 72 个尺度逐项枚举，均有

\[
-kF_kL_k(t)\notin\mathcal D((kF_kL_k(t))^2;q_k). \tag{5}
\]

将 (p(t)) 和 72 个 (L_k(t)) 合并，得到 73 个正、本原、互异的线性型。其有限域根
检查在所有不超过 73 的素数处均未覆盖全体剩余类；大于 73 的素数至多有 73 个根，亦不可能
覆盖。因此该元组 Dickson 可采纳。

假定 Dickson 猜想，取无穷多个使 73 个型同时为素数的充分大参数，即由 (5) 得到所有

\[
k\mid41400 \tag{6}
\]

的平稳标准外部源都失败。

这是尺度选择的条件性边界，而不是 Erdős--Straus 猜想的反例。它不处理非平稳尺度、带
平移参数的外部源、菜单外 Type II 尾或其它递降状态。特别地，任何试图在这条压力进程上
用固定的平稳尺度集合证明全称递降的方案，必须加入这些未审计的自由度。

可复现命令：

~~~bash
python3 reproductions/h19_k23_pressure_full_stationary_source_conditional_escape.py \
  --input reproductions/h19-k23-global-tail-pressure-external-source-bridge-2097152.json \
  --output reproductions/h19-k23-pressure-full-stationary-source-conditional-escape-2097152.json
python3 -m unittest tests/test_h19_k23_pressure_full_stationary_source_conditional_escape.py -q
~~~
