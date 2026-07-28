---
kind: claim
claim_id: type-I-linear-general-b-obstruction-profile-878089
title: 878089 的线性一般 B 中心化谱障碍剖面
statement: 对p=878089的全部54个线性E整除n源状态所诱导的24个不同R，B=1目标均失败；按一般B中心化平方除子谱分类，R=59命中，21个R为子群/角色障碍，R=279与R=503为有限指数障碍。R=59的最小平方除子为816781，规范恢复已知B=7线性桥。该精确单点剖面说明一般B的成功来自更换目标指数盒，而非线性B=1目标的隐含命中。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- general-b
- linear-source
- shifted-source
- selector-counterexample
- target-square-divisor
- subgroup-character
- finite-exponent
- exhaustive-computation
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# \(p=878089\) 的线性一般 \(B\) 中心化谱障碍剖面

## 结论

[\(p=878089\) 的线性 \(B=1\) 反例](type-I-linear-shifted-source-counterexample-878089.md)
已经完整枚举了 \(E\mid n\) 的线性源。它给出 54 个定向状态和 24 个不同模数 \(R\)，并证明
每个 \(R\) 的 \(B=1\) 除子条件都失败。

把一般 \(B\) 条件改写为

\[
d\mid K^2,\quad d\equiv-K\pmod R,\quad K=\frac{pR+1}{4}, \tag{1}
\]

再使用[中心化平方除子谱障碍二分](type-I-general-b-centered-square-spectrum.md)，24 个模数的完整结果是

\[
24=1_{\mathrm{hit}}+21_{\mathrm{subgroup/character}}
+2_{\mathrm{finite\ exponent}}. \tag{2}
\]

也就是说，全部 24 个状态都没有 \(B=1\) 命中，但一般 \(B\) 有且只有一个目标谱命中：

\[
R=59,\quad K=12951813,\quad d=816781. \tag{3}
\]

这里 \(d<K\)、\(d\mid K^2\)、\(d\equiv-K\pmod {59}\)，并规范恢复

\[
(A,B,C,H,m)=(2,7,16669,111,55375), \tag{4}
\]

即已有的线性一般 \(B\) 证书。

## 完备性与输入冻结

输入为
[`type-I-linear-shifted-source-counterexample-878089.json`](../reproductions/type-I-linear-shifted-source-counterexample-878089.json)，
SHA-256 为
`9e491bf3816f7880aa3468c61dd7dce0385068ab6fd2388cc0da9f15ca65928c`。
它已通过 \(u=\min(a,s)\) 的有限枚举以及独立的全部奇移位扫描，冻结了所有线性状态。

本剖面不复用其中的目标判断。对每个存储的 \(R\)，它重新分解 \(K\)，直接枚举所有
\(d\mid K^2\)，并计算

\[
\mathcal C_R(K)=\{dK^{-1}\pmod R:d\mid K^2\},
\qquad
\mathcal H_R(K)=\langle q\pmod R:q\mid K\rangle. \tag{5}
\]

测试再以独立的奇 \(s\) 扫描重建 54 个状态、直接枚举 \(K^2\) 的所有除子、并独立做有限群闭包。

## 两个有限指数状态

除命中 \(R=59\) 外，只有下列两个状态满足

\[
-1\in\mathcal H_R(K)\setminus\mathcal C_R(K), \tag{6}
\]

即角色不能排除目标，但现有的指数盒仍不够：

| \(R\) | \(K\) | \(K\) 的素因子分解 | 中心化谱大小 | 生成子群阶 |
| ---: | ---: | --- | ---: | ---: |
| 279 | 61,246,708 | \(2^2\cdot73\cdot349\cdot601\) | 53 | 180 |
| 503 | 110,419,692 | \(2^2\cdot3\cdot17\cdot37\cdot14629\) | 205 | 502 |

其余 21 个失败状态都满足 \(-1\notin\mathcal H_R(K)\)，因而有精确的子群/角色障碍。
这显示在同一个核心素数内，两种失败机制确实同时出现；不能用单一的“指数不够”或单一的
“角色排除”叙述整个失败集。

## 含义与边界

该点并没有反驳一般 \(B\) 线性猜想：\(R=59\) 已经闭合。它反而给出下一阶段必须解释的
更精确现象：**源选择需要逃离 21 个子群障碍和 2 个有限指数障碍，才能进入 \(R=59\) 的命中谱。**

这仍是一个单点有限剖面。它不能说明不同素数的障碍角色可比较，也不能推出每个普通 Type II
尾遗漏都存在这样的逃逸模数；这些正是全称选择引理尚缺的内容。

可复现命令：

~~~bash
python3 reproductions/type_i_linear_general_b_obstruction_profile_878089.py
python3 -m unittest tests/test_type_i_linear_general_b_obstruction_profile_878089.py -v
~~~
