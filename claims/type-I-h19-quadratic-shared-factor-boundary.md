---
kind: claim
claim_id: type-I-h19-quadratic-shared-factor-boundary
title: H19-k23 十四条残存进程的共享因子二次 Type I 边界
statement: H19-k23 经全部统一仿射叶子削减后的14条进程，对每个 x=EN 的全部二次 Type I 除子 d=x^2/h，其中 h|E，均无自然范围证书。每条进程完整枚举 E|S、h|E 的787320对；由进程原始性和 Type I 同余，该子族等价于 m=-C mod4E 且 m|4h+1，每对至多有两个缺口。14条合计检查63882个可行缺口，命中为零。
claim_status: computationally_reproduced
topics:
- type-I
- quadratic-divisor
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

# H19-k23 十四条残存进程的共享因子二次 Type I 边界

## 二次子族与精确条件

在一个残存进程上，令

\[
p=Pn+C,\qquad x=\frac{p+m}{4}=Sn+T=EN,
\qquad E=\gcd(S,T).
\]

考虑最自然的非仿射平方除子子族

\[
d=\frac{x^2}{h}=\frac{E^2}{h}N^2,\qquad h\mid E. \tag{1}
\]

它始终整除 \(x^2\)，但通常随参数二次变化，因此不属于此前的统一仿射审计。Type I
同余化为

\[
px+d
\equiv
\frac{E^2}{h}(4h+1)N^2\pmod m. \tag{2}
\]

进程原始性给出 \(\gcd(E,m)=1\)，而 \(N\) 的全体值的最大公因子为一；故 (2) 对
全部参数成立，当且仅当

\[
m\mid4h+1. \tag{3}
\]

另一方面 \(E\mid T=(C+m)/4\)，所以

\[
m\equiv-Cpmod {4E}. \tag{4}
\]

由于 \(h\mid E\)，(3) 给出 \(m\le4h+1\le4E+1\)。因此对固定 \((E,h)\)，
(4) 只可能给出 \((-C)\bmod4E\) 或其加 \(4E\) 的两个正代表元；这使整个子族的
枚举完整有限化，不涉及未知参数值的因子分解。

## 完整审计

对当前 14 条 H19-k23 残存进程，共同的 \(S=P/4\) 有 4,608 个因子。枚举所有

\[
E\mid S,\qquad h\mid E
\]

恰给出每条进程 787,320 对。筛过自然缺口、精确 \(\gcd(S,T)=E\) 与 (4) 后，
各进程的可行缺口数为 4,538 至 4,569；总计为 63,882。对所有候选，(3) 都失败：

| 项目 | 数目 |
|---|---:|
| 残存进程 | 14 |
| 每进程 \((E,h)\) 对 | 787,320 |
| 全部 \((E,h)\) 对 | 11,022,480 |
| 可行缺口测试 | 63,882 |
| 二次 Type I 命中 | 0 |

## 边界含义

这不否定全部二次除子，因为一般形式允许 \(h\mid E^2\) 而不必 \(h\mid E\)；也不否定
更高复杂度的参数相关因子或多源提升。不过它排除了一个特别自然的“从 \(x^2\) 中抽取
固定共享因子”的非仿射叶子。结合此前的统一仿射 Type I/II 和混合因子边界，余下桥接
机制必须至少使用 \(h\mid E^2\) 且 \(h\nmid E\) 的真正平方因子、随参数的非固定因子，或多个
来源之间的耦合。

运行

```bash
python3 reproductions/type_i_h19_quadratic_shared_factor_boundary.py
python3 -m unittest tests/test_type_i_h19_quadratic_shared_factor_boundary.py -q
```

可重建全部枚举、零命中与每条进程的缺口计数。
