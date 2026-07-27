---
kind: claim
claim_id: type-II-canonical-shift-tail-sieve
title: 规范首次移位的固定阈值尾部可达任意对数幂
statement: 令 sigma(p) 是平方自由规范 Type II 射线的首次成功移位。对每个固定 H>=1，满足 p<=X、p=1 mod24 且 sigma(p)>H 的素数数目为 O_H(X/(log X)^(1+H/2))；相对于核心素数总数，其比例为 O_H((log X)^(-H/2))。因而任一固定 H 都在相对密度一意义下捕获核心素数，且通过固定 H 可使尾部达到任意预定对数幂；该结论不允许 H 随 X 增长。
claim_status: established
topics:
- type-II
- canonicalization
- minimal-shift
- sieve
- density
- proof-program
sources:
- paper: elsholtz_tao2013
  locator: Appendix A, shifted-prime sieve methodology
  role: density-methodology
- paper: chamberland2026
  locator: "Theorem 1"
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-24'
---

# 规范首次移位的固定阈值尾部可达任意对数幂

## 定理

令 $\sigma(p)$ 如 `type-II-minimal-canonical-shift-spectrum` 所定义；若前面的
规范射线均失败，则置 $\sigma(p)=\infty$。对每个固定整数 $H\ge1$，令

\[
T_H(X)=\#\{p\le X:p\equiv1\pmod {24},\ \sigma(p)>H\}. \tag{1}
\]

则

\[
T_H(X)\ll_H\frac{X}{(\log X)^{1+H/2}}. \tag{2}
\]

又由算术级数中的素数定理，核心素数总数为 $\asymp X/\log X$，所以

\[
\frac{T_H(X)}
{\#\{p\le X:p\equiv1\pmod {24}\}}
\ll_H(\log X)^{-H/2}. \tag{3}
\]

特别地，任意固定 $H$ 的规范移位扇都覆盖相对密度一的核心素数；给定任意固定
对数幂 $B$，取 $H\ge2B$ 即将尾部压至 $O_B(X/(\log X)^B)$。

## 证明

对每个 $1\le s\le H$，写 $s=a_s^2c_s$ 且 $c_s$ 平方自由。对应的 Type II
因子射线使用参数对 $(a_s,c_s)$，其移位数是

\[
p+4a_s^2c_s=p+4s. \tag{4}
\]

不同 $s$ 给出不同的 $a_s^2c_s$。将这 $H$ 个参数对代入
`type-II-ac-rays-superlog-residual`，其式 (3) 立即给出 (2)。当 $p\ge4H$ 时，
每个命中因子自动满足 Type II 的序条件；较小 $p$ 只造成有限项，已被渐近界吸收。
最后以核心素数的渐近式除以 (2)，得到 (3)。

## 与有限谱的关系

在 $p\le10^7$ 的精确谱中，阈值尾计数为：

| $H$ | $\#\{\sigma(p)>H\}$ |
|---:|---:|
| 1 | 38696 |
| 2 | 14015 |
| 4 | 3945 |
| 8 | 643 |
| 14 | 128 |
| 20 | 37 |
| 30 | 9 |
| 50 | 0 |

这些数只核验实现并展示有限尺度；它们不是 (2) 的证明，也不能决定任何固定 $H$
是否覆盖全体素数。

## 真正缺口

(2) 中的隐含常数依赖于固定 $H$。因此不能令 $H=H(X)$ 直接得到
$\sigma(p)$ 的增长界。`type-II-canonical-fan-uniform-sieve-interface` 给出规范扇
在模数和横截面熵上的显式 $H$ 依赖；下一步必须把该依赖带入上界筛，才可能得到
缓慢增长阈值的定量密度结果。即使完成这一步，仍与对每个单独 $p$ 的选择器存在本质
差距。
