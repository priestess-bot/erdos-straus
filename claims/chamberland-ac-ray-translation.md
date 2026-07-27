---
kind: claim
claim_id: chamberland-ac-ray-translation
title: Chamberland Type II 素数形状与 AC 因子射线的精确翻译
statement: 设 p=qr-4s_1s_2 是 Chamberland 的 Type II 形状，其中 q=3 mod4、s_1,s_2|(q+1)/4。令 A=gcd(s_1,s_2)、C=lcm(s_1,s_2)/A、K=(q+1)/(4lcm(s_1,s_2))、B=Kr-A，则 q=4ACK-1、p=4ACB-r。令 alpha=min(A,B)、beta=max(A,B)，则 h=4alphaCK-1 满足 h|p+4alpha^2C、Kp+alpha=beta*h，并给出缺口 r 的有序 AC Type II 证书；h=q 当且仅当 A<=B。反之，每个成功的 AC 射线因子都给出 Chamberland 形状。故二者在证书存在性层面等价，但以 q 或 (s_1,s_2) 为状态时须记录可能的因子重选；有界 A,C 射线饱和等价于在 Chamberland 形状中选择有界 gcd(s_1,s_2) 与有界 lcm(s_1,s_2)/gcd(s_1,s_2)。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
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
last_checked: '2026-07-28'
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

的生成因子。因为 \(A+B=Kr\)，代入 (4) 还得到

\[
p=4ACB-r. \tag{7}
\]

特别地 \(p>0\) 强制 \(B>0\)。若 \(B\ge A\)，则 \((A,B,C,K)\) 直接是 Type II
的 AC 正规形；其缺口为 \(r=(A+B)/K\)。特别地，充分条件 \(p\ge4A^2C\) 保证这个
序条件。

## 序条件不能省略

上述翻译在因子坐标上总是成立，但任意一张 Chamberland 表示不必直接给出**同一张**
有序 AC Type II 证书。最小的核心素数例子是

\[
73=39\cdot7-4\cdot5\cdot10.
\]

这里 \(L=10\)，从 \((s_1,s_2)=(5,10)\) 得

\[
(A,C,K,B)=(5,2,1,2),\qquad B<A. \tag{8}
\]

尽管 \(39\mid73+4\cdot5^2\cdot2\)，该原始射线的
\(d=A^2C=50\) 大于 \(x=ABC=20\)，故它不是 Type II 除子证书。不过重排为
\(\alpha=2,\beta=5\) 后，得到

\[
73=15\cdot7-4\cdot2\cdot4,
\qquad(\alpha,\beta,C,K)=(2,5,2,1). \tag{9}
\]

一般地，设

\[
\alpha=\min(A,B),\qquad\beta=\max(A,B),\qquad
h=4\alpha CK-1. \tag{10}
\]

由 (7) 以及 \(A+B=Kr\)，分两种排序但同一计算得到

\[
Kp+\alpha=\beta h,\qquad p+4\alpha^2C=rh. \tag{11}
\]

因此 \(h\mid Kp+\alpha\)、\(\alpha\le\beta\)，且

\[
x=\alpha\beta C,\qquad d=\alpha^2C,\qquad
\frac{\alpha+\beta}{K}=r
\]

是一张有序 Type II 除子证书。若 \(A\le B\)，这个 \(h\) 就是原来的 \(q\)；若
\(B<A\)，则必须切换到新的因子 \(h=4BCK-1\)，如上例的 \(39\mapsto15\)。

所以 Chamberland 的**存在性**刻画与“存在某张 AC 证书”完全相容，但在以 \(q,s_1,s_2\)
为状态标签的转移中，不能把任意一个 Chamberland 因子直接当作有序 AC 证书。必须保留
\(B\ge A\) 的序条件，或执行 (10)--(11) 的因子重选。跨移位状态若固定跟踪一个 \(q\)
或一对 \((s_1,s_2)\)，不能由因子翻译本身推出该状态已有 Type II 终端。

## 从成功射线到 Chamberland 形状

反过来，设 AC 射线成功，即

\[
q=4ACK-1,\qquad q\mid p+4A^2C. \tag{12}
\]

写

\[
r=\frac{p+4A^2C}{q},\qquad s_1=A,\qquad s_2=AC. \tag{13}
\]

则 (s_1,s_2mid ACK=(q+1)/4)，且

\[
p=qr-4s_1s_2. \tag{14}
\]

这正是 Chamberland 形状的一个嵌套代表 (s_1\mid s_2)。式 (2) 应用于该代表会
精确恢复原来的 (A,C,K)。因此，成功 AC 射线并非另一种 Type II 机制，而是
Chamberland 定理中一类可由小除子对参数化的表示。

## 有界参数的精确含义

每条半径 \(A,C\le B_0\) 的 AC 射线都由 (13) 给出一对 Chamberland 因子，满足

\[
\gcd(s_1,s_2)\le B_0,\qquad
\frac{\operatorname{lcm}(s_1,s_2)}{\gcd(s_1,s_2)}\le B_0. \tag{15}
\]

而 (K) 和 (q) 不受限制。故“有界 AC 射线饱和”不是固定有限 (q) 模板，而是：
每个核心素数是否都可在 Chamberland 表示中选择一个结构复杂度受控的除子对。反向地，
从任一满足 (15) 的 Chamberland 表示出发，(10) 的规范化有
\(\alpha=\min(A,B)\le A\)，且保持 \(C,K,r\)。所以即使发生因子重选，也仍落在同一
\(B_0\) 射线盒中。换言之，半径 \(A,C\le B_0\) 的 AC 证书存在性精确等价于
Chamberland 表示中

\[
\gcd(s_1,s_2)\le B_0,\qquad
\frac{\operatorname{lcm}(s_1,s_2)}{\gcd(s_1,s_2)}\le B_0
\]

的存在性；不应把这个存在性等价误读为“原始 \(q\) 保持不变”的状态等价。

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

脚本对 (p\le10000) 的全部 143 个核心素数所取半径 14 射线见证逐项完成 (13) 的
往返转换，并以精确分数再次核对 Type II 证书：

```bash
python3 reproductions/chamberland_ac_ray_translation.py
python3 -m unittest tests/test_chamberland_ac_ray_translation.py -q
```

## 范围

Chamberland 的定理本身允许 (s_1,s_2) 和 (15) 中的两个量增长；本卡不把有限
半径 14 的成功外推为有界定理。它的作用是统一两种参数语言，并把下一步明确为
Chamberland 除子对复杂度的选择问题，而非重复搜索另一套 Type II 表示。
