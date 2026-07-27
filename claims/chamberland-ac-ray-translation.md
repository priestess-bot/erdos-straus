---
kind: claim
claim_id: chamberland-ac-ray-translation
title: Chamberland Type II 素数形状与 AC 因子射线的精确翻译
statement: 设 p=qr-4s_1s_2 是 Chamberland 的 Type II 形状，其中 q=3 mod4、s_1,s_2|(q+1)/4。令 A=gcd(s_1,s_2)、C=lcm(s_1,s_2)/A、K=(q+1)/(4lcm(s_1,s_2))，则 q=4ACK-1、p=qr-4A^2C，且 B=Kr-A 满足 qB=Kp+A。反之，每个成功的 AC 射线因子 q=4ACK-1|p+4A^2C 都给出 Chamberland 形状 p=qr-4(A)(AC)，r=(p+4A^2C)/q。故在 B>=A 的自然 AC 证书范围，二者给出同一张 Type II 证书；有界 A,C 射线饱和等价于在 Chamberland 形状中选择有界 gcd(s_1,s_2) 与有界 lcm(s_1,s_2)/gcd(s_1,s_2)。
claim_status: established
topics:
- type-II
- chamberland
- factorization
- ac-rays
- divisor-parametrization
- short-certificate
sources:
- paper: chamberland2026
  locator: Theorem 1 and its proof
  role: Type-II-prime-shape
- paper: bradford2024
  locator: Section 2, Type II divisor certificates
  role: AC-ray-certificate-context
visibility: public
last_checked: '2026-07-25'
---

# Chamberland Type II 素数形状与 AC 因子射线的精确翻译

## 从 Chamberland 形状到射线

Chamberland 的定理采用

\[
p=qr-4s_1s_2,\qquad q\equiv3\pmod4,\qquad
s_1,s_2\mid L:=\frac{q+1}{4}. \tag{1}
\]

令

\[
A=\gcd(s_1,s_2),\qquad
C=\frac{\operatorname{lcm}(s_1,s_2)}A,\qquad
K=\frac{L}{\operatorname{lcm}(s_1,s_2)}. \tag{2}
\]

因为两个 (s_i) 都整除 (L)，所以 (K) 是正整数。又

\[
A^2C=s_1s_2,\qquad AC=\operatorname{lcm}(s_1,s_2), \tag{3}
\]

故

\[
q=4ACK-1,\qquad p=qr-4A^2C. \tag{4}
\]

令 (B=Kr-A)。直接代入 (4) 得

\[
qB=(4ACK-1)(Kr-A)=Kp+A. \tag{5}
\]

所以 Chamberland 的因子 (q) 正是 AC 射线条件

\[
q=4ACK-1,\qquad q\mid Kp+A
\tag{6}
\]

的生成因子。若 (B\ge A)，则 ((A,B,C,K)) 直接是 Type II 的 AC 正规形；其
缺口为 (r=(A+B)/K)。特别地，充分条件 (p\ge4A^2C) 保证这个序条件。

## 从成功射线到 Chamberland 形状

反过来，设 AC 射线成功，即

\[
q=4ACK-1,\qquad q\mid p+4A^2C. \tag{7}
\]

写

\[
r=\frac{p+4A^2C}{q},\qquad s_1=A,\qquad s_2=AC. \tag{8}
\]

则 (s_1,s_2mid ACK=(q+1)/4)，且

\[
p=qr-4s_1s_2. \tag{9}
\]

这正是 Chamberland 形状的一个嵌套代表 (s_1\mid s_2)。式 (2) 应用于该代表会
精确恢复原来的 (A,C,K)。因此，成功 AC 射线并非另一种 Type II 机制，而是
Chamberland 定理中一类可由小除子对参数化的表示。

## 有界参数的精确含义

由 (2)，半径 (A,C\le B_0) 的射线盒对应于 Chamberland 因子对满足

\[
\gcd(s_1,s_2)\le B_0,\qquad
\frac{\operatorname{lcm}(s_1,s_2)}{\gcd(s_1,s_2)}\le B_0. \tag{10}
\]

而 (K) 和 (q) 不受限制。故“有界 AC 射线饱和”不是固定有限 (q) 模板，而是：
每个核心素数是否都可在 Chamberland 表示中选择一个结构复杂度受控的除子对。

例如 Chamberland 给出的

\[
1009=23\cdot47-4\cdot3\cdot6
\]

经 (2) 变为

\[
(A,C,K,B)=(3,2,1,44),
\]

并满足 (23\cdot44=1009+3)。半径 14 审计的记录保持者

\[
(p,A,C,K,q)=(84\,525\,841,1,14,30,1679)
\]

反向给出 (r=50\,343,s_1=1,s_2=14)。

脚本对 (p\le10000) 的全部 143 个核心素数所取半径 14 射线见证逐项完成 (8) 的
往返转换，并以精确分数再次核对 Type II 证书：

```bash
python3 reproductions/chamberland_ac_ray_translation.py
python3 -m unittest tests/test_chamberland_ac_ray_translation.py -q
```

## 范围

Chamberland 的定理本身允许 (s_1,s_2) 和 (10) 中的两个量增长；本卡不把有限
半径 14 的成功外推为有界定理。它的作用是统一两种参数语言，并把下一步明确为
Chamberland 除子对复杂度的选择问题，而非重复搜索另一套 Type II 表示。
