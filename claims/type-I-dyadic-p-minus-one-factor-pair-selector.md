---
kind: claim
claim_id: type-I-dyadic-p-minus-one-factor-pair-selector
title: Type I二幂桥p减一源的因子对判据
statement: 设p=1 mod4，t≥2，E=2^t、R=E-1、K=(pR+1)/4，并假设E|(p-1)^2/4。存在桥因子E、源n=p-1的Type I正规形最大尾反向边，当且仅当存在BC|K，令H=K/(BC)，满足R|(4B^2C+1)及gcd((H+B)/R,B)=1；此时A=(H+B)/R、m=(4B^2C+1)/R恢复正规形。对p=21169可取t=5、(B,C)=(5,1262)，给出m=4071的最小B=5偶源边。
claim_status: established
topics:
- type-I
- normal-form
- descent
- even-source
- source-state
- factorization
- dyadic
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# Type I 二幂桥 p 减一源的因子对判据

设 \(p\equiv1\pmod4\)、\(t\ge2\)，并记

\[
E=2^t,\qquad R=E-1,\qquad K=\frac{pR+1}{4}. \tag{1}
\]

假设

\[
E\mid\frac{(p-1)^2}{4}. \tag{2}
\]

则存在桥因子为 \(E\)、源为 \(n=p-1\) 的 Type I 正规形最大尾反向边，当且仅当存在

\[
BC\mid K,\qquad H=\frac K{BC},\qquad
R\mid4B^2C+1,\qquad
\gcd\left(\frac{H+B}{R},B\right)=1. \tag{3}
\]

成立。恢复公式为

\[
A=\frac{H+B}{R},\qquad m=\frac{4B^2C+1}{R}. \tag{4}
\]

## 证明

取 \(n=p-1\)，于是源距离 \(s=p-n=1\)。在偶源桥的记号中

\[
4K=pR+1,\qquad E=4K-nR=R+1=2^t. \tag{5}
\]

由归一化源平方等价，桥条件正是

\[
E\mid\frac{n^2}{\gcd(E,4)}=\frac{(p-1)^2}{4},
\]

即 (2)。此时将一般源状态实现判据应用于 \((n,E)\)，恰得到 (3)--(4)。反向构造的
源首项为

\[
\frac{(p-1)K}{2^t},
\]

且由 (2) 与一般桥等价保证为整数；两边的三项恒等式随之成立。

## 21169 的异常解释

对 \(p=21169\)，取

\[
t=5,\quad E=32,\quad R=31,\quad K=164060=2^2\cdot5\cdot13\cdot631.
\]

因子对

\[
B=5,\qquad C=1262,\qquad H=26
\]

满足 (3)，故

\[
(A,B,C,m)=(1,5,1262,4071)
\]

给出源 \(21168=p-1\) 的严格偶源边。这说明该点的 \(B=5\) 不是黑箱枚举产物，而是
\(R=31\) 二幂桥上的显式因子对命中。

该判据仍要求在 \(K\) 的真实因子结构中选择 \(B,C\)，所以没有推出一个统一二幂指数或全局
低 \(B\) 界；它把下一步精确定位为模 \(2^t-1\) 的因子对选择问题。

可复现命令：

~~~bash
python3 reproductions/type_i_mersenne_bridge_selector.py
python3 -m unittest tests/test_type_i_mersenne_bridge_selector.py -q
~~~
