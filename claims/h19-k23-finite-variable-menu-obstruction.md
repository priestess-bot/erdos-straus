---
kind: claim
claim_id: h19-k23-finite-variable-menu-obstruction
title: H19-k23 固定尾的有限变量素数模板障碍
statement: 在 H19-k23 的v=0残存进程及全局尾m=31上，参数类t=0 (mod 31) 的Type II目标剩余为11，完整固定基底F=(8*133)^2的所有除子均不命中该剩余。对任意有限个可实际作为u=48522699225t+684088426的非基底因子的素数ell（ell与31、斜率及进程系数互素），可用CRT构造一个原始p等差进程，其中保持该目标且所有ell不整除u；Dirichlet定理给出无穷多个实际核心素数。因此任何有限预选非基底素数模板库不能在素数参数意义下补齐该固定尾失配类。此结论不排除无界自适应因子选择器。
claim_status: established
topics:
- type-II
- affine-progressions
- divisor-selection
- factor-support
- crt
- h19
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-criterion
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 固定尾的有限变量素数模板障碍

在 \(v\equiv0\pmod{29}\) 的 H19-k23 残存进程上，取全局尾 \(m=31\)、\(q=8\)。
其变量因子为

\[
u=48\,522\,699\,225t+684\,088\,426. \tag{1}
\]

共同因子为 \(133\)，所以完整固定平方基底为

\[
F=(8\cdot133)^2=1\,132\,096. \tag{2}
\]

在 \(t\equiv0\pmod{31}\) 上，目标 Type II 剩余固定为

\[
-8u\equiv11\pmod{31}. \tag{3}
\]

而任何 \(d\mid F\) 都不满足 \(d\equiv11\pmod{31}\)。这正是全参数固定基底覆盖
边界中的一个具体失配状态。

## CRT 避开有限菜单

设 \(\mathcal P\) 是任意有限个可作为 (1) 的**非基底变量因子**的素数。非平凡的此类
素数都与 \(31\) 和 (1) 的斜率互素；否则它要么从不整除 \(u\)，要么已经属于统一基底。
于是对每个 \(\ell\in\mathcal P\)，条件 \(\ell\mid u\) 恰是一个根类

\[
t\equiv-684\,088\,426\,(48\,522\,699\,225)^{-1}\pmod\ell. \tag{4}
\]

在模 \(\ell\) 下同时避开 (4) 和使
\(p=1\,552\,726\,375\,200t+21\,890\,829\,601\) 被 \(\ell\) 整除的唯一根类，
并与 \(t\equiv0\pmod{31}\) 联立。有限次中国剩余定理给出一个类

\[
t\equiv t_0\pmod{31\prod_{\ell\in\mathcal P}\ell} \tag{5}
\]

使 (3) 保持，所有 \(\ell\in\mathcal P\) 都不整除 \(u\)，且相应的 \(p\) 不被
\(\mathcal P\) 中的素数整除。又进程系数的任何素因子都不整除常数项，故所得
\(p\) 等差数列是原始的。

例如对

\[
\mathcal P=\{37,41,43,59,73,89,103\},
\]

脚本产生的避开类为

\[
t\equiv0
\pmod{79\,839\,504\,563\,309}. \tag{6}
\]

其对应的核心素数候选为

\[
p=123\,968\,904\,518\,350\,642\,487\,536\,800n
+21\,890\,829\,601, \tag{7}
\]

且系数与常数项互素。由 Dirichlet 关于等差数列中素数的定理，(7) 含无穷多个素数；
它们自动仍满足 \(p\equiv1\pmod{24}\)。所以有限模板障碍确实发生在无穷多个实际核心
素数上，而不只是复合参数。

## 边界含义

这排除的是“固定基底加有限预选非基底素数模板”对素数参数的覆盖。它仍不排除根据
\(u\) 的实际、无界素因子自适应选择的证书。

所以任何无限证明若沿全局尾菜单推进，必须真正利用无界因子分布或多个变量因子的结构；
有限地增加候选素数或有限 CRT 模板即使限制到素数参数也不可能完成闭合。

重建命令：

~~~bash
python3 reproductions/h19_k23_finite_variable_menu_obstruction.py
python3 -m unittest tests/test_h19_k23_finite_variable_menu_obstruction.py -q
~~~
