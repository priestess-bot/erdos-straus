---
kind: claim
claim_id: type-I-h19-quadratic-square-only-boundary
title: H19-k23 十四条残存进程的平方专用小 h 二次 Type I 边界
statement: H19-k23 经全部统一仿射叶子削减后的14条进程，对所有 x=EN 的二次 Type I 除子 d=x^2/h，其中 h|E^2 且 h<=E，均无自然范围证书。该族包含 h|E 的共享因子族以及 h|E^2 但 h 不整除 E 的平方专用部分。每条进程完整枚举10619136对 (E,h)，总计148667904对；利用 m=-C mod4E、m|4h+1 和 m<=4E+1 的两候选有限化，9364817个可行缺口均无命中。
claim_status: computationally_reproduced
topics:
- type-I
- quadratic-divisor
- square-divisor
- arithmetic-progression
- nonaffine
- certificate
- conditional-boundary
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-divisor-criterion
visibility: public
last_checked: '2026-07-25'
---

# H19-k23 十四条残存进程的平方专用小 h 二次 Type I 边界

## 完整子族

写残存进程上的首分母为

\[
x=EN,\qquad E=\gcd(S,T).
\]

考虑

\[
d=\frac{x^2}{h},\qquad h\mid E^2,\qquad h\le E. \tag{1}
\]

当 \(h\mid E\) 时，这是此前的共享因子二次族；但 (1) 还允许例如 \(E=12,h=9\)
这样的平方专用因子。因此它是对
[共享因子二次边界](type-I-h19-quadratic-shared-factor-boundary.md) 的严格扩张。

由 \(p=4x-m\)，Type I 条件为

\[
px+d\equiv\frac{E^2}{h}(4h+1)N^2pmod m. \tag{2}
\]

原始进程给出 \(\gcd(E,m)=1\)，而 \(N\) 值的最大公因子为一，故 (2) 对全参数成立
当且仅当

\[
m\mid4h+1. \tag{3}
\]

另一方面 \(E\mid(C+m)/4\)，所以 \(m\equiv-C\pmod {4E}\)。由 \(h\le E\) 和
(3)，有 \(m\le4E+1\)，因而每个 \((E,h)\) 只可能给出模 \(4E\) 的最小正代表元或其
加 \(4E\) 的两个缺口。这个二缺口结论使 (1) 的完整枚举不需要因式分解参数相关的大整数。

## 审计结果

当前 14 条进程共有相同的 \(S=P/4\)。对每一条，完整枚举

\[
E\mid S,\qquad h\mid E^2,\qquad h\le E
\]

得到 10,619,136 对。流式并行审计先使用 (3) 剪枝，再核验自然范围与精确
\(\gcd(S,(C+m)/4)=E\)。结果如下：

| 项目 | 数目 |
|---|---:|
| 残存进程 | 14 |
| 每进程 \((E,h)\) 对 | 10,619,136 |
| 全部 \((E,h)\) 对 | 148,667,904 |
| 可行缺口测试 | 9,364,817 |
| 二次 Type I 命中 | 0 |

所有进程均为空；脚本若遇命中会逐项恢复并核验单位分数恒等式。

## 剩余空间

该边界不覆盖 \(h>E\) 的二次因子；在那里 \(m\le4h+1\) 不再把模 \(4E\) 的候选
压缩为两个，新的因子结构才可能出现。它也不覆盖更一般的参数相关除子或多源严格提升。
不过，任何后续二次 Type I 机制都不能停留在 \(h\le E\) 的全部平方专用范围内。

运行

```bash
python3 reproductions/type_i_h19_quadratic_square_only_boundary.py
python3 -m unittest tests/test_type_i_h19_quadratic_square_only_boundary.py -q
```

可重建完整流式枚举与零命中结果。
