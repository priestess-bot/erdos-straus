---
kind: claim
claim_id: type-II-affine-uniform-divisor-rigidity
title: 统一仿射 Type II 除子的平方因子刚性正规形
statement: 令 x(n)=Sn+T，E=gcd(S,T)，并令 d(n)=An+B 是正的非恒定整数仿射函数。若对全部 n>=0 有 d(n)|x(n)^2，且 d(n)<=x(n) 对充分大 n 成立，则存在唯一 a 使 d(n)=a x(n)/E、1<=a<=E 且 a|E^2。若固定缺口 m 对全部 n 都满足 m|x(n)+d(n)，则 m|E+a。因而统一仿射 Type II 除子包含 d|x 的 a|E 子族，但还允许 a|E^2 且 a 不整除 E 的平方专用子族。
claim_status: established
topics:
- type-II
- arithmetic-progression
- affine-rigidity
- divisor-parametrization
- square-divisor
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-criterion
visibility: public
last_checked: '2026-07-25'
---

# 统一仿射 Type II 除子的平方因子刚性正规形

## 定理

令

\[
x(n)=Sn+T,\qquad S,T>0,\qquad E=\gcd(S,T),
\]

并设

\[
d(n)=An+B,\qquad A,B>0
\]

是非恒定整数仿射函数。假设对每个 \(n\ge0\)，

\[
d(n)\mid x(n)^2,
\]

并且 \(d(n)\le x(n)\) 对充分大的 \(n\) 成立。则存在唯一整数 \(a\) 使

\[
d(n)=aN(n),\qquad
x(n)=EN(n),\qquad
1\le a\le E,\qquad
a\mid E^2.
\]

若固定缺口 \(m\) 对所有 \(n\) 还满足 Type II 同余

\[
m\mid x(n)+d(n),
\]

则

\[
m\mid E+a.
\]

## 证明

令

\[
\Delta=AT-SB.
\]

有恒等式

\[
A\,x(n)=S\,d(n)+\Delta.
\]

模 \(d(n)\) 平方后得到

\[
A^2x(n)^2\equiv\Delta^2\pmod {d(n)}.
\]

由假设 \(d(n)\mid x(n)^2\)，可得 \(d(n)\mid\Delta^2\)。若
\(\Delta\ne0\)，正线性函数 \(d(n)\) 无界，却始终整除固定非零整数
\(\Delta^2\)，矛盾。故 \(\Delta=0\)，即 \(d/x=A/S\) 为常数。

写

\[
N(n)=\frac{x(n)}E
=\frac SE n+\frac TE.
\]

因为 \(\gcd(S/E,T/E)=1\)，由 \(d/x=A/S\) 的整数性可唯一写成 \(d=aN\)。
不等式给出 \(a\le E\)。又

\[
aN(n)\mid E^2N(n)^2
\]

对全部 \(n\) 成立。\(N(n)\) 的所有值的最大公因子为 1，故 \(a\mid E^2\)。

最后 \(x+d=(E+a)N\)。再次利用 \(N(n)\) 的值的最大公因子为 1，得到固定同余
当且仅当 \(m\mid E+a\)。

## 平方专用部分

通常的固定因子陷阱只使用 \(a\mid E\)，因而 \(d\mid x\)。但这里允许

\[
a\mid E^2,\qquad a\nmid E,
\]

所以 \(d\mid x^2\) 而 \(d\nmid x\)。例如

\[
x(n)=12(n+1),\qquad d(n)=9(n+1),\qquad m=7.
\]

此时 \(E=12\)、\(a=9\)，而 \(9\mid12^2\)、\(9\nmid12\) 且
\(7\mid E+a=21\)。脚本逐项恢复 \(p=4x-7\) 的 Type II 单位分数恒等式。

## 对当前边界的含义

[H19-k23 固定因子陷阱边界](type-II-h19-external-scale-fixed-trap-boundary.md)
只穷尽了较窄的 \(a\mid E\) 子族。要在残存仿射进程上寻找全部统一非恒定仿射
Type II 除子，正确的因子参数是

\[
E\mid S,\qquad a\mid E^2,\qquad a\le E,\qquad m\mid E+a.
\]

这个更宽枚举尚未完成，不能由旧的空结果推出空结论。

运行

```bash
python3 reproductions/type_ii_affine_uniform_divisor_rigidity.py
python3 -m unittest tests/test_type_ii_affine_uniform_divisor_rigidity.py -q
```

可重建平方专用例子及整数、分数恒等式核对。
