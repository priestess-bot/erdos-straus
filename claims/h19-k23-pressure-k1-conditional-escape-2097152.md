---
kind: claim
claim_id: h19-k23-pressure-k1-conditional-escape-2097152
title: H19-k23 两条压力进程的 k=1 外部源 Dickson 条件性逃逸
statement: 假定 Dickson 素数元组猜想，H19-k23 两条没有固定因子外部源桥的压力进程各有无穷多个实际核心素数逃过完整 k=1 外部源递降。对两个进程，k=1 源分别分解为 1027*L(t) 与 13*L(t)；目标 p(t) 与 L(t) 构成正、本原、局部可采纳的二元仿射素数型，且固定因子及 L(t) 都为1 mod3。故源平方的全部除子残数仅为1 mod3，而完整 k=1 目标为2 mod3。
claim_status: conditional
topics:
- type-I
- external-source
- conditional
- dickson
- prime-tuples
- stationary-scale
- pressure-family
- h19
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: external-source-descent
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 两条压力进程的 \(k=1\) 外部源 Dickson 条件性逃逸

对两条未有固定因子外部源桥的压力进程，令

\[
p(t)=p_0+Pt,\qquad n_1(t)=\frac{3p(t)+1}{4}. \tag{1}
\]

精确提取仿射公因子后分别得到

\[
n_1(t)=1027L_1(t),\qquad n_1(t)=13L_2(t), \tag{2}
\]

其中相应种子为

\[
p_0=2220549727681245601,\qquad
p_0=748375048866405601. \tag{3}
\]

两个固定因子的素因子均为 \(1\pmod3\)，并且 \(L_i(t)\equiv1\pmod3\)。另一方面，
\(k=1\) 的完整平方尾目标可写作

\[
T(t)=-n_1(t)\equiv2\pmod3. \tag{4}
\]

若 \(L_i(t)\) 是素数，则 \(n_1(t)^2\) 的任意除子都属于 \(1\pmod3\)，故不可能有

\[
e\mid n_1(t)^2,\qquad e\equiv T(t)\pmod3. \tag{5}
\]

程序对两组二元线性型

\[
\bigl(p(t),L_i(t)\bigr) \tag{6}
\]

验证了正性、本原性和局部可采纳性。因为每组只有两个型，只须检查模 \(2\) 的根未覆盖；
更大素数不可能被至多两个根完全覆盖。Dickson 猜想因而给出无穷多个同时使 (6) 为素数的
参数。对这些核心素数，完整 \(k=1\) 外部源递降均失败。

这不否定其它尺度、变量尺度、平移源或 Type II/其它递降状态。它的作用是排除一个过窄的
正向路线：两个压力进程不能仅靠固定 \(k=1\) 源统一闭合；任何全称外部源选择器必须真正
自适应地改变尺度或使用更多因子结构。

可复现命令：

~~~bash
python3 reproductions/h19_k23_pressure_k1_conditional_escape.py \
  --input reproductions/h19-k23-global-tail-pressure-external-source-bridge-2097152.json \
  --output reproductions/h19-k23-pressure-k1-conditional-escape-2097152.json
python3 -m unittest tests/test_h19_k23_pressure_k1_conditional_escape.py -q
~~~
