---
kind: claim
claim_id: type-II-c3-common-carrier-mark-transfer-no-go
title: c=3 中共同 p-carrier 两尾提升的严格 no-go
statement: 在核心 c=3 域 p=24h+1=12q-11、q=2h+1 中，若一个 4/q 解在保留两尾比值的前提下，将两尾共同缩放为 lambda*p 后提升到 4/p，即 4/q=1/a+1/b+1/c 与 4/p=1/x+1/(lambda*p*b)+1/(lambda*p*c)，且目标首分母属于合法 gap 正规形，则必有 lambda=1 且 x=a=3q。因此该自然 transfer 类完全等价于已有 gap-11 Type II 直接证书，不产生新的严格递降边。对 q=3 (mod 4) 的等尾标准源，甚至允许两尾采用不同缩放 lambda*p、mu*p 也不可能产生合法 target gap。允许不同 carrier 时只可能选定单一有序源尾对；一个显式非对称族仍退化为既有 gap-7 direct terminal。结果不排除其它 source-only mark 或非仿射变换。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-factor-pair-carrier-strict-descent
  - type-II-c3-q-complementary-divisor-r7mod11-descent
  - short-certificate-equivalence
  - denominator-escape-state-contract
topics:
  - type-II
  - c3
  - mark-transfer
  - strict-descent
  - no-go
  - common-carrier
  - proof-boundary
sources:
  - claim: type-II-factor-pair-carrier-strict-descent
    role: gap-eleven-marked-two-tail-layer
  - claim: short-certificate-equivalence
    role: legal-gap-normal-form
  - concept: denominator-escape-state-contract
    role: lift-boundary
visibility: public
last_checked: '2026-08-06'
---

# \(c=3\) 中共同 \(p\)-carrier 两尾提升的严格 no-go

## 1. 共同尾缩放只会回到 gap \(11\)

令

\[
p=24h+1=12q-11,\qquad q=2h+1\ge7,\qquad \lambda\ge1.
\tag{1}
\]

假设存在正整数 \(a,b,c,x\)，使

\[
\frac4q=\frac1a+\frac1b+\frac1c,
\tag{2}
\]

\[
\frac4p=\frac1x+\frac1{\lambda pb}+\frac1{\lambda pc}.
\tag{3}
\]

再要求目标首分母 \(x\) 属于合法 gap 正规形：

\[
m=4x-p,\qquad 3\le m\le p-2,\qquad m\equiv3\pmod4.
\tag{4}
\]

**定理（共同 carrier no-go）。** 在 (1)--(4) 下必有

\[
\boxed{\lambda=1,\qquad m=11,\qquad x=a=3q.}
\tag{5}
\]

所以 (3) 只是已有的 marked gap-\(11\) 形式

\[
\frac4q=\frac1{3q}+\frac1b+\frac1c
\Longrightarrow
\frac4p=\frac1{3q}+\frac1{pb}+\frac1{pc}.
\tag{6}
\]

**证明。** 将 (2) 的两尾和代入 (3)，得到

\[
a=\frac{qx}{p-m(\lambda q-1)},
\qquad
p-m(\lambda q-1)>0.
\tag{7}
\]

故

\[
m<\frac p{q-1}<13,
\tag{8}
\]

所以 \(m\in\{3,7,11\}\)。结合 (7) 的正性，\(\lambda\le3\)，且仅有

\[
(\lambda,m)\in
\{(1,3),(1,7),(1,11),(2,3),(3,3)\}.
\tag{9}
\]

相应的 \(a\) 依次为

\[
\frac{q(3q-2)}{9q-8},\qquad
\frac{q(3q-1)}{5q-4},\qquad
3q,\qquad
\frac{q(3q-2)}{6q-8},\qquad
\frac{q(3q-2)}{3q-8}.
\tag{10}
\]

前两项中分母分别与 \(q\) 互素且大于第二因子，故不为整数。第四项分子为奇数、
分母为偶数。最后一项若为整数，则 \(3q-8\mid6\)，但 \(q\ge7\) 时不可能。
仅第三项存活，给出 (5)。证毕。

例如 \(p=73,q=7\) 时，

\[
\frac47=\frac1{21}+\frac12+\frac1{42}
\Longrightarrow
\frac4{73}=\frac1{21}+\frac1{146}+\frac1{3066},
\tag{11}
\]

正是 (6) 的唯一存活型。另一方面 \(p=313,q=27\) 虽有普通源解

\[
\frac4{27}=\frac19+\frac1{54}+\frac1{54},
\tag{12}
\]

但该类若能提升必须把首项改为 \(81\)。此时

\[
(11b-81)(11c-81)=81^2
\tag{13}
\]

要求某个 \(3\) 的幂为 \(7\pmod{11}\)，而
\(\{3^j\pmod{11}\}=\{1,3,4,5,9\}\)，故 marked gap-\(11\) 集为空。

## 2. 等尾标准源的非对称缩放也失败

当 \(q\equiv3\pmod4\) 时，有标准等尾源

\[
\frac4q
=\frac1{(q+1)/4}
+\frac2{q(q+1)/2}.
\tag{14}
\]

即使把两个相等的尾分别缩放为 \(\lambda pB,\mu pB\)，其中

\[
B=\frac{q(q+1)}2,\qquad \lambda,\mu\ge1,
\tag{15}
\]

目标合法 gap 也必须满足

\[
m=\frac{p(\lambda+\mu)}
{4B\lambda\mu-\lambda-\mu}
\le\frac p{q(q+1)-1}<3.
\tag{16}
\]

这与 (4) 矛盾。因此仅靠等尾的非对称共同 \(p\)-carrier 也不能创造新边。

## 3. 非对称 carrier 只能选择一个源尾标记

现在固定一个任意的正整数 source 解

\[
\frac4q=\frac1a+\frac1b+\frac1c,
\qquad
\Delta=4a-q>0,
\qquad
s=qa.
\tag{17}
\]

它的两尾满足

\[
\Delta bc=s(b+c).
\tag{18}
\]

令 \(x=(p+m)/4\)，并尝试不同的正整数 carrier

\[
\frac4p=\frac1x+\frac1{p\lambda b}+\frac1{p\mu c}.
\tag{19}
\]

**定理（非对称 carrier 的单标记刚性）。** (17)--(19) 成立当且仅当

\[
m\lambda\mu bc=x(\lambda b+\mu c).
\tag{20}
\]

若 \(\lambda=\mu\)，则它在整张 source 尾纤维上成立当且仅当

\[
m\lambda s=x\Delta,
\tag{21}
\]

这正是第 1 节的共同 carrier 情形。若 \(\lambda\ne\mu\)，至多有一个有序尾对，
而且它存在当且仅当

\[
b=\frac{xs(\mu-\lambda)}{m\lambda\mu s-x\lambda\Delta},
\qquad
c=\frac{xs(\mu-\lambda)}{\mu(x\Delta-m\lambda s)}
\tag{22}
\]

都是正整数（分母非零）。

**证明。** 从 (19) 减去首项并通分，立即得到 (20)；再与 (18) 消元。
当 \(\lambda=\mu\) 时，消元式与 \(b,c\) 无关，恰为 (21)。当
\(\lambda\ne\mu\) 时，两个线性式的行列式非零，解唯一，给出 (22)。证毕。

固定 \(q,a,m,\lambda,\mu\) 后，令

\[
\mathcal F_{q,a}
=\{(b,c)\in\mathbb N^2:\Delta bc=s(b+c)\}.
\tag{23}
\]

则 \(\lambda\ne\mu\) 时，(22) 精确给出

\[
\left|\left\{(b,c)\in\mathcal F_{q,a}:
\text{(19) 成立}\right\}\right|\le1.
\tag{24}
\]

所以不同 carrier 不能在一个非平凡 source tail fiber 上普遍提升；它至多选定一个
预先定义的 source mark。这个结论不允许 \(m,\lambda,\mu\) 随该 mark 改变。

还有一个更窄的全曲线 affine 边界。暂时把 target 的两尾写成

\[
\frac4p=\frac1x+\frac1{pB}+\frac1{pC},
\tag{25}
\]

并令

\[
u=\Delta b-s,\quad v=\Delta c-s,\quad uv=s^2,
\qquad
U=mB-x,\quad V=mC-x,\quad UV=x^2.
\tag{26}
\]

若一个常系数、线性部可逆的实仿射映射作为整个代数双曲线
\(uv=s^2\to UV=x^2\) 的恒等映射，则比较 \(u,u^{-1}\) 与常数项可知，它只能是

\[
(U,V)=\left(\alpha u,\frac{x^2}{\alpha s^2}v\right)
\tag{27}
\]

或交换两坐标。因此在这个强的全曲线意义下不存在真正的 cross-tail affine mixing。
回到分母变量，(27) 允许的对角 affine shift 是

\[
B=\frac{\alpha\Delta}{m}b+\frac{x-\alpha s}{m},
\qquad
C=\frac{x^2\Delta}{\alpha s^2m}c
+\frac{x-x^2/(\alpha s)}{m}.
\tag{28}
\]

常数项一般不为零，故这**不**排除单尾 affine shift，也不处理有限整数纤维上的任意
reassembly。只有再加上纯 carrier 限制 \(B=\lambda b,C=\mu c\) 时，(28) 的常数项
强制 \(\alpha=x/s\)，并由两条斜率得到 \(\lambda=\mu=x\Delta/(ms)\)；此时才回到
第 1 节的共同 carrier no-go。

非对称空间并非空集，但它也不自动产生新递归。若 \(7\mid q\)，则

\[
\frac4q
=\frac1{2q}+\frac1{3q/7}+\frac1{6q/7},
\tag{29}
\]

取 \(x=3q-1\)、\(m=7\)、\(\lambda=1\)、\(\mu=x/2\) 得

\[
\frac4p
=\frac1x
+\frac1{p(3q/7)}
+\frac1{p(x/2)(6q/7)}.
\tag{30}
\]

在 \(q=7,p=73\) 时，这就是

\[
\frac47=\frac1{14}+\frac13+\frac16,
\qquad
\frac4{73}=\frac1{20}+\frac1{219}+\frac1{4380}.
\tag{31}
\]

但 (26) 恰是已有 gap \(7\) 的 \((A,B,C,K)=(1,3q-1,1,3q/7)\) Type II
direct terminal，并同时重现已有的严格递降
\(p\to(3q-1)/2\)，而不是一条 \(p\to q\) 边。因此它只证明不同 carrier 的剩余空间
存在；terminal-first 必须直接输出已有 terminal，不能把它登记为新的递归边。

## 4. 剩余方向

本卡没有排除：

1. 预先由 source-only 数据定义、并通过 (22) 的其它离散 mark；
2. (28) 中单尾 affine shift 的整性、正性与非平凡性；
3. 非仿射且不保持同一 source slice 的两尾变换；
4. 不以 \(q=(p+11)/12\) 为来源的递降；
5. 其它 gap 或直接 terminal。

这些才是寻找真正新 mark-transfer 时需要证明的剩余空间。
