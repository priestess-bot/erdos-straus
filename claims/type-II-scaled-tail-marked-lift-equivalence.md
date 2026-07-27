---
kind: claim
claim_id: type-II-scaled-tail-marked-lift-equivalence
title: 缩放首分母双尾提升与固定 Type II 证书等价
statement: 固定合法缺口 m、首分母 x=(p+m)/4 与正整数 k，若 n=k(p+m)/(km+1) 为整数，则映射 (kx,Y,Z)->(x,pY,pZ) 在满足 4/n=1/(kx)+1/Y+1/Z 的带标记源解和满足 4/p=1/x+1/(pY)+1/(pZ) 的固定首分母 Type II 目标解之间是双射。因此这类提升本身不能把“n 有任意三项解”的普通归纳假设转化为 p 的解；它是带标记的严格下降和 Type II 证书选择器，而非独立的无标记递归步骤。
claim_status: established
topics:
- type-II
- descent
- lifting
- marked-solution
- logical-boundary
- exact-algebra
sources:
- paper: bradford2024
  locator: Section 2, Type II divisor certificates
  role: certificate-context
visibility: public
last_checked: '2026-07-24'
---

# 缩放首分母双尾提升的带标记等价边界

## 定理

令 \(p\) 为奇素数，取合法缺口

\[
m=4x-p,\qquad 3\le m\le p-2,
\]

并取 \(k\ge1\)，使

\[
n=\frac{k(p+m)}{km+1}
\]

为整数。定义

\[
\Phi(kx,Y,Z)=(x,pY,pZ).
\]

则 \(\Phi\) 在下列两类三元组之间是双射：

\[
\mathcal S=\left\{(kx,Y,Z):
\frac4n=\frac1{kx}+\frac1Y+\frac1Z\right\},
\]

\[
\mathcal T=\left\{(x,pY,pZ):
\frac4p=\frac1x+\frac1{pY}+\frac1{pZ}\right\}.
\]

后者正是首分母固定为 \(x\) 的 Type II 解。

## 证明

由 \(4x=p+m\) 和 \(n=k(p+m)/(km+1)\)，有

\[
\frac4n-\frac1{kx}
=\frac{km+1}{kx}-\frac1{kx}
=\frac mx. \tag{1}
\]

另一方面

\[
p\left(\frac4p-\frac1x\right)
=4-\frac px
=\frac mx. \tag{2}
\]

所以源式成立当且仅当

\[
\frac1Y+\frac1Z=\frac mx,
\]

而这又当且仅当目标式成立。映射及其逆

\[
(x,pY,pZ)\longmapsto(kx,Y,Z)
\]

均由此直接验证。

## 对递降的限制

`type-II-scaled-first-tail-deflation` 所给出的下降是严格的：\(n<p\)。但它是
带标记下降，源端必须有首分母恰为 \(kx\) 的解。普通 Erdős--Straus 归纳假设只给出

\[
\frac4n=\frac1a+\frac1b+\frac1c
\]

的某个解，并不保证 \(a=kx\)。由上面的双射可知，取得该标记源解本身已经等价于
取得目标的固定 Type II 证书。

因此共享因子条件 \(D\mid p+m,\ D\equiv1\pmod m\) 的正确作用是缩小 Type II
短证书选择空间；它不能单独被计为一个把任意较小实例解提升到目标的递归证明。真正的
递降路线还需一个独立的“标记源解存在”定理，或一个对任意源解有效的提升变换。
