---
kind: claim
claim_id: audige-divisor-lattice-completion-equivalence
title: LCM 除子格局部完成的非空性就是受限三项分解命题
statement: 令 L_n=lcm(1,...,n)、D_n={d:d|L_n}、T=4L_n/n。Audige 定义中可选择 u_x(n) 当且仅当存在 d,e,f 属于 D_n 使 d+e+f=T；这当且仅当 4/n 存在三个分母均整除 L_n 的单位分数三项分解。因此 T 为整数且 1 属于 D_n 不能证明该定义域非空。
claim_status: established
topics:
- proof-audit
- divisor-lattice
- greedy-algorithm
- certificate
- obstruction
sources:
- paper: audige_divisor_lattice2026
  locator: "Sections 1--2 and Proposition 4"
  role: audited-definition-and-nonemptiness-claim
visibility: public
last_checked: '2026-07-24'
---

# LCM 除子格局部完成的非空性就是受限三项分解命题

## 定理

令

\[
L_n=\operatorname{lcm}(1,\ldots,n),\qquad
D_n=\{d\in\mathbb N:d\mid L_n\},\qquad
T_n=\frac{4L_n}{n}.
\]

定义

\[
G_n=\{d\in D_n:\exists e,f\in D_n,\ d+e+f=T_n\}. \tag{1}
\]

则以下三项等价：

1. \(G_n\ne\varnothing\)；
2. 存在 \(d,e,f\in D_n\)，使 \(d+e+f=T_n\)；
3. 存在正整数 \(x,y,z\)，满足
   \[
   \frac4n=\frac1x+\frac1y+\frac1z,\qquad x\mid L_n,\ y\mid L_n,\ z\mid L_n. \tag{2}
   \]

故 \(G_n\) 的非空性是一个受限的 Erdős--Straus 存在性命题，而不是由
\(T_n\in\mathbb Z\) 与 \(1\in D_n\) 自动推出的结论。

## 证明

第一项与第二项的等价就是集合 (1) 的定义。若第二项成立，令

\[
x=\frac{L_n}{d},\qquad y=\frac{L_n}{e},\qquad z=\frac{L_n}{f};
\]

则

\[
\frac1x+\frac1y+\frac1z
=\frac{d+e+f}{L_n}
=\frac{T_n}{L_n}
=\frac4n,
\]

所以得到第三项。反之，若第三项成立，则

\[
d=\frac{L_n}{x},\qquad e=\frac{L_n}{y},\qquad f=\frac{L_n}{z}
\]

都属于 \(D_n\)，并且把第三项中的单位分数等式乘以 \(L_n\) 即得
\(d+e+f=T_n\)。

## 对 Audige 2026 的审计

论文的集合 \(S_d\) 正是给定 \(d\) 后 (1) 的完成集合；其“最大兼容除子” \(u_x(n)\)
有定义当且仅当 \(G_n\ne\varnothing\)。Lemma 2 所列的两项事实

\[
T_n\in\mathbb Z,\qquad 1\in D_n
\]

不能产生三个和为 \(T_n\) 的除子，因而没有证明该定义域非空。

其后的 Proposition 4 以 \(u_x(n)\) 为已选元素，再要求
\(T_n-u_x(n)\) 是两个除子之和；这正是 \(u_x(n)\) 有定义所需的性质。因此该步骤不能
为 Lemma 2 提供非循环证明。泛化的多项除子分割只控制总和 \(4A_n\)，没有给出包含
和为 \(T_n\) 的三项子分割的论证。

这不否定已有的有限示例。例如 \(n=10\) 时

\[
1008=840+140+28,
\]

确实给出 \((x,y,z)=(3,18,90)\)；但示例不能证明 \(G_n\) 对所有 \(n\) 非空。
