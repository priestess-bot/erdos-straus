---
kind: claim
claim_id: type-II-shared-small-a-boundary
title: 共享 Type II 选择器不存在全局小 A 界
statement: 核心素数 p=878089 的全部合法缺口穷举中，恰有两张同时满足共享因子 D|p+m、D=1 modm 和 Type II 条件的正规形证书：(m,D,d,A,B,C,K)=(51,460,34445,83,529,5,12) 与 (143,12728,204723,69,74,43,1)。故该素数没有 A<=68 的共享 Type II 证书，特别否定共享选择器可取 A<=3 或任一不超过 68 的固定界的强化。
claim_status: computationally_reproduced
topics:
- type-II
- shared-divisor
- normal-form
- parameter-bound
- obstruction
- computation
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-criterion
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-25'
---

# 共享 Type II 选择器不存在全局小 \(A\) 界

## 穷举对象

对核心素数

\[
p=878{,}089,
\]

穷举全部合法缺口

\[
3\le m\le p-2,\qquad m\equiv3\pmod4,
\]

所有共享因子

\[
D>1,\qquad D\mid p+m,\qquad D\equiv1\pmod m,
\]

以及所有 Type II 目标除子

\[
d\mid x^2,\qquad d\le x,\qquad d\equiv-x\pmod m,\qquad
x=\frac{p+m}{4}.
\]

将每张证书归一化为 `type-II-coprime-factor-normal-form` 的

\[
x=ABC,\qquad d=A^2C,\qquad K=\frac{A+B}{m}. \tag{1}
\]

## 精确结果

全范围穷举只得到两张不同的共享正规形：

\[
\begin{array}{c|c|c|c|c|c|c}
m&D&d&A&B&C&K\\
\hline
51&460&34{,}445&83&529&5&12\\
143&12{,}728&204{,}723&69&74&43&1
\end{array} \tag{2}
\]

因此

\[
\min A=69. \tag{3}
\]

复现：

```bash
python3 reproductions/type_ii_shared_small_a_boundary.py
python3 -m unittest tests/test_type_ii_shared_small_a_boundary.py -v
```

## 含义与边界

这严格否定了下列共享选择器强化：

\[
\text{“对每个核心素数存在共享 Type II 证书，且 }A\le68\text{。”} \tag{4}
\]

特别地，84 点中大多数当前见证具有 \(A\le3\) 的有限现象不能被外推为全称
小 \(A\) 定理。

## 与直接 Type II 的分离

同一个素数并不难于直接 Type II 意义下的证书。事实上

\[
p+4=878{,}093=131\cdot6{,}703,\qquad
131=4\cdot33-1. \tag{5}
\]

取

\[
(A,C,K)=(1,1,33),\qquad B=221{,}198,
\]

便有

\[
131\mid33p+1,\qquad
m=\frac{A+B}{K}=6{,}703,\qquad d=1. \tag{6}
\]

所以 \(p=878{,}089\) 有一张 \(A=C=1\) 的直接 Type II 证书；但该缺口并没有
共享因子证书，所有共享证书仍是 (2) 中 \(A\ge69\) 的两张。

(5)--(6) 说明共享选择器的参数障碍不能被误读为直接 Type II \(AC\) 射线的障碍。
前者是更强的短证书猜想；后者仍可利用移位 \(p+4A^2C\) 的因子结构独立推进。

(4) 因而并不否定一般的 Type II \(AC\) 射线饱和猜想：这里额外要求同一缺口存在
共享因子 \(D\equiv1\pmod m\)。它也不否定 Erdős--Straus 猜想，因为该素数确有
两张共享 Type II 证书。它排除的只是把自适应共享因子选择简化为固定小 \(A\) 参数盒的
证明路线。
