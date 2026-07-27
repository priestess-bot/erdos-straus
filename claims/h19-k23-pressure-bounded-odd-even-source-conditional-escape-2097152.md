---
kind: claim
claim_id: h19-k23-pressure-bounded-odd-even-source-conditional-escape-2097152
title: H19-k23 压力进程全部奇距离 c<=99 标准偶源扇的联合 Dickson 条件性逃逸
statement: 假定 Dickson 素数元组猜想，存在无穷多个同一 H19-k23 压力进程核心素数同时逃过全部奇距离 c<=99 的标准偶源扇。对每个 c 写 p-c=B_c*ell_c，并令所有 ell_c 及尾部剩余本原因子同时为充分大素数；50 个距离的完整兼容扇共含36条射线、168463个平方尾模式，所需113个一次因子出现压缩为66个正、本原、局部可采纳型。常数尾模数逐点失败，线性尾模数只留下有限异常参数，故整个有界距离盒逃逸。
claim_status: conditional
topics:
- type-I
- even-source
- conditional
- dickson
- prime-tuples
- factorization
- strict-descent
- pressure-family
- h19
sources:
- paper: bradford2024
  locator: Proposition 1
  role: even-source-descent
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 压力进程全部奇距离 \(c\le99\) 标准偶源扇的联合 Dickson 条件性逃逸

固定同一压力进程 \(p(t)=p_0+Pt\)。对每个奇数 \(1\le c\le99\)，写

\[
p(t)-c=B_c\ell_c(t),
\qquad
B_c=\gcd(p_0-c,P).
\]

\(\ell_c\) 是正、本原一次型。若 \(\ell_c(t)\) 为充分大的素数，则 \(p-c\) 的每个
除子均为 \(a\) 或 \(a\ell_c\)，其中 \(a\mid B_c\)。脚本逐一检查标准偶源所需的

\[
4ck=p-d,
\qquad
cdr=p-d-c,
\]

从而列出每个距离的**全部**兼容移位，并核验严格提升乘积恒等式。

50 个奇距离中，只有

\[
c=1,3,5,9,15,23,25,37,41,45,47,61,69,75
\]

有非空兼容扇；它们共给出 36 条射线。每条射线均穷尽 \(e_1\mid M_1^2\)、
\(e_1\le M_1\) 的最终因子模式，合计 168,463 个。所有常数 \(r\) 射线逐参数避靶；
每个线性 \(r\) 射线的余式非零，故至多在有限参数上命中。

为使上述“\(\ell_c\) 为素数”条件和所有尾部余因子条件在同一参数成立，脚本合并 113 个
一次因子出现位置，得到 66 个不同的正、本原一次型。有限域根覆盖检查表明该 66 元组局部
可采纳。假定 Dickson 猜想，这些型同时取充分大素数无穷次发生；于是每个 \(c\le99\) 的
实际因子都已由枚举覆盖，而所有 33 条兼容射线均失败。

因此，在 Dickson 条件下，无穷多个压力进程核心素数同时逃过**全部奇距离 \(c\le99\) 的
标准偶源扇**。这不反驳 Erdős--Straus 猜想，也不排除距离无界的偶源、非标准源、Type II
或其它递降状态。它把当前正向研究要求具体化：任何偶源递降定理必须强制距离或因子复杂度
随状态增长，不能仅依赖预先固定的奇距离上界。

可复现命令：

~~~bash
python3 reproductions/h19_k23_pressure_bounded_odd_even_source_conditional_escape.py \
  --input reproductions/h19-k23-global-tail-pressure-external-source-bridge-2097152.json \
  --output reproductions/h19-k23-pressure-bounded-odd-even-source-conditional-escape-2097152.json
python3 -m unittest tests/test_h19_k23_pressure_bounded_odd_even_source_conditional_escape.py -q
~~~
