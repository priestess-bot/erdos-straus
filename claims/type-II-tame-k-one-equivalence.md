---
kind: claim
claim_id: type-II-tame-k-one-equivalence
title: Xu 的 tame 解恰为 Type II 的 K=1 切片
statement: 对素数 p=24t+1，令 x=(p+m)/4 为有序解的首分母。Xu 意义下的 tame 解与满足 Type II 互素正规形 x=ABC、d=A^2C、K=(A+B)/m=1 的证书一一对应（交换后两个分母不影响对应）。此时 m=A+B，且 xp/y、xp/z 恰为 B、A。
claim_status: established
topics:
- type-II
- tame-wild
- divisor-parametrization
- certificate
- proof-program
sources:
- paper: xu2026
  locator: "Definition (1.5), Theorem 2.1"
  role: tame-definition-and-divisibility
- paper: bradford2024
  locator: "Propositions 2 and 4"
  role: Type-II-certificate-equivalence
visibility: public
last_checked: '2026-07-23'
---

# Xu 的 tame 解恰为 Type II 的 \(K=1\) 切片

## 定理

令 \(p=24t+1\) 为素数。写有序解的首分母为

\[
x=6t+k=\frac{p+m}{4},\qquad m=4k-1.
\]

在 type-II-coprime-factor-normal-form 的坐标中，Type II 证书写作

\[
x=ABC,\qquad d=A^2C,\qquad \gcd(A,B)=1,\qquad A\le B,
\qquad K=\frac{A+B}{m}.
\]

则 Xu 所定义的 tame 解，恰好是 \(K=1\) 的这些 Type II 证书所恢复的解。
更精确地，\(K=1\) 时

\[
m=A+B,\qquad y=pAC,\qquad z=pBC,
\qquad \frac{xp}{y}=B,\quad \frac{xp}{z}=A. \tag{1}
\]

因此 \(y,z\mid xp\)，而 Xu 的两个 numerator summands 正是 \(B,A\)（可交换）。
反之，每个 tame 解都给出唯一的 \(K=1\) Type II 正规形，直至交换 \(A,B\)
后以 \(A\le B\) 归一化。

## 证明

先从 Type II 正规形出发。Bradford 的恢复公式为

\[
y=\frac{p(x+d)}m,\qquad z=\frac{p(x+x^2/d)}m.
\]

代入 \(x=ABC\)、\(d=A^2C\)、\(A+B=Km\)，得

\[
y=pACK,\qquad z=pBCK. \tag{2}
\]

故若 \(y,z\mid xp=pABC\)，则 \(K\mid B\) 且 \(K\mid A\)。由于
\(\gcd(A,B)=1\)，这强制 \(K=1\)。反过来 \(K=1\) 时，(2) 就是 (1)，故两个
分母都整除 \(xp\)。又 \(A,B\le x<p\)，所以 \(x<y,z\)；它确为 Xu 采用的首分母
顺序。并且 \(m=4x-p=4k-1=A+B\)，所以 (1) 的两个商之和正是 Xu 定义中的
\(4k-1\)。

再从 Xu 的 tame 解出发。按其定义，令

\[
I_y=\frac{xp}{y},\qquad I_z=\frac{xp}{z},
\qquad I_y+I_z=4k-1=m.
\]

Xu 的 Theorem 2.1 断言 \(I_y\mid x\)、\(I_z\mid x\)。因此

\[
\gcd(I_y,I_z)\mid\gcd(x,m)=\gcd(x,p)=1,
\]

其中最后一步用 \(p=4x-m\) 及 \(0<x<p\)。置
\(A=\min(I_y,I_z)\)、\(B=\max(I_y,I_z)\)、\(C=x/(AB)\)，便有

\[
x=ABC,\qquad \gcd(A,B)=1,\qquad m=A+B.
\]

取 \(d=A^2C\)，立刻有 \(d\mid x^2\)、\(d\le x\)，以及

\[
x+d=AC(A+B)=ACm.
\]

所以这正是 Type II 证书，且 \(K=(A+B)/m=1\)。

## \(K\) 是精确的 tame 缺陷

对任意 Type II 正规形，不只 \(K=1\) 情形，\(K\mid A+B\) 与
\(\gcd(A,B)=1\) 蕴含

\[
\gcd(K,A)=\gcd(K,B)=1. \tag{3}
\]

事实上，任何同时整除 \(K,A\) 的数也整除 \(B=(A+B)-A\)，故只能为 1；
对 \(B\) 同理。

由 (2)，对任意正整数 \(\lambda\)，

\[
\frac{\lambda xp}{y}=\frac{\lambda B}{K},\qquad
\frac{\lambda xp}{z}=\frac{\lambda A}{K}. \tag{4}
\]

结合 (3)，这两个量同时为整数当且仅当 \(K\mid\lambda\)。所以 \(K\) 是满足

\[
y,z\mid\lambda xp
\]

的最小正 \(\lambda\)。特别地，Xu tame 正是缺陷为 1 的情形；\(K>1\) 的 Type II
证书仍有同一整除结构，但必须把基数 \(xp\) 精确放大 \(K\) 倍。

## 含义与边界

这给出 tame/wild 语言与短证书坐标的精确翻译：Xu 的 tame 同余类家族只搜索
Type II 空间的 \(K=1\) 薄切片；一个 Xu-wild 素数没有这一切片上的证书，但仍可能有
\(K>1\) 的 Type II 证书或任意 Type I 证书。因此 Xu 所报告的有限 wild 样本既不是
猜想的反例，也不能被解释为没有全部短证书。

这一等价也不产生 \(n<p\) 的实例或从 \(\operatorname{Sol}(n)\) 到
\(\operatorname{Sol}(p)\) 的映射，故它不是“短证书或递降”引理中的递降支；它只是把
现有 tame 研究严格定位到可进一步扩张的 \(K>1\) 残余空间。
