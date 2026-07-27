---
kind: claim
claim_id: h19-k23-global-full-divisor-conditional-escape-2097152
title: H19-k23 全局尾完整 Type II 除子的 Dickson 条件性逃逸
statement: 假定 Dickson 素数元组猜想，存在无穷多个 H19-k23 实际核心素数，使 72 个规范全局尾中没有任何 Type II 除子证书 d|((p+m)/4)^2、d<=(p+m)/4、d=-(p+m)/4 (mod m)，即使 d 可使用任意多个非基底素因子及任意允许的幂。构造复用一次幂逃逸的 73 个正、本原、局部可采纳仿射素数型；变量余因子在充分大参数处为唯一新素数，大小界迫使其在 d 中的指数至多一，而所有余下有限除子残数均被精确枚举并避开目标。因此固定 72 尾菜单内的任意 Type II 除子选择器不能成为无条件证明路线。
claim_status: conditional
topics:
- type-II
- conditional
- dickson
- prime-tuples
- global-tail-menu
- divisor-enumeration
- factor-support
- high-powers
- cross-tail
- h19
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-criterion
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 全局尾完整 Type II 除子的 Dickson 条件性逃逸

沿
[全局一次幂选择器的条件性逃逸](h19-k23-global-first-power-conditional-escape-2097152.md)
的同一压力进程与同一 73 元素 Dickson 可采纳元组，对每个全局尾 (m=4q-1) 写

\[
x_m=\frac{p+m}{4}=B_mK_mL_m(n). \tag{1}
\]

这里 (B_m) 的全部素因子都在该尾的规范基底中，(K_m) 是冻结的非基底部分，而
(L_m(n)) 是元组中要求为素数的正本原仿射型。加细周期后，(B_m,K_m) 的精确赋值及
(L_m(n)\bmod m) 都不随 (n) 改变。

## 完整除子归约

取足够大的 (n)，使所有 (L_m(n)>B_mK_m)，且它们不同于所有固定素因子。若

\[
d\mid x_m^2,\qquad d\le x_m, \tag{2}
\]

则 (L_m(n)) 在 (d) 中不可能出现二次或更高幂：否则

\[
d\ge L_m(n)^2>B_mK_mL_m(n)=x_m.
\]

故每个可能的 Type II 除子都唯一落入有限表

\[
d=bkL_m(n)^e,\qquad
b\mid B_m^2,quad k\mid K_m^2,quad e\in\{0,1\}, 	ag{3}
\]

其中 (e=1) 时仍逐项检查 (bk\le B_mK_m)。这一步没有预设非基底支撑大小，亦没有
预设 (K_m) 内素因子的幂。

程序对 72 个尾的 (3) 完整枚举后，全部得到

\[
d\not\equiv-x_m\pmod m. \tag{4}
\]

单尾最多检查 8,438 个大小允许的候选，72 尾均为零命中。因为每一项的模 (m) 残数在
整条进程上固定，(4) 是该仿射素数元组的恒定有限核结论，而不只是种子点的试算。

## 条件性结论与范围

该 73 元组正、本原且局部可采纳。Dickson 素数元组猜想因此给出无穷多个同时使 (p) 和
所有 (L_m(n)) 为素数的参数；取其中充分大的参数，(2)--(4) 表明全部 72 个规范全局尾
均无 Type II 除子证书。

这比“一新增素因子一次幂”逃逸更强：在这个固定全球尾菜单中，高幂和任意多个非基底
因子也不能恢复证书。它仍不反驳 Erdős--Straus 猜想，也不排除使用菜单外尾、不同的
递降状态、Type I 证书，或不依赖此 H19-k23 残存进程的论证。事实上，当前这个种子
进程已经由固定尺度 (k=18) 的 Type I 外部源严格递降无条件覆盖，见
[全局尾压力进程的固定因子外部源递降桥](h19-k23-global-tail-pressure-external-source-bridge-2097152.md)。

可复现命令：

~~~bash
python3 reproductions/h19_k23_global_full_divisor_conditional_escape.py \
  --input reproductions/h19-k23-global-base-only-prime-obstruction-2097152.json \
  --output reproductions/h19-k23-global-full-divisor-conditional-escape-2097152.json
python3 -m unittest tests/test_h19_k23_global_full_divisor_conditional_escape.py -q
~~~
