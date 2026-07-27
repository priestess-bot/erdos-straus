---
kind: claim
claim_id: type-I-h19-uniform-constant-boundary
title: H19-k23 十四条残存进程的统一常数 Type I 边界
statement: H19-k23 当前14条残存进程对所有全参数常数 Type I 除子 d=a（a|E^2，x=E(un+v)）均无自然范围证书。恒等 Type I 同余等价于 m|u 与 a=-4E^2v^2 modm，因此只需枚举 m|S 的有限候选。每条进程恰有564个候选缺口；14条合计19366个最短侧 E^2 除子残数选择均无命中。
claim_status: computationally_reproduced
topics:
- type-I
- constant-divisor
- arithmetic-progression
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

# H19-k23 十四条残存进程的统一常数 Type I 边界

## 常数除子的有限化

令

\[
p=Pn+C,\qquad x=Sn+T=E(un+v),\qquad E=\gcd(S,T).
\]

若常数 \(a>0\) 对全参数满足 \(a\mid x^2\)，则取 \(un+v\) 的值的最大公因子为一，
立即得到

\[
a\mid E^2. \tag{1}
\]

Type I 条件模 \(m\) 化为

\[
4E^2(un+v)^2+a\equiv0pmod m. \tag{2}
\]

原始进程使 \(\gcd(E,m)=1\)，且 \(m\) 为奇数。比较 (2) 的二次、一次与常数系数，
依次得到

\[
m\mid u^2,\qquad m\mid2uv,\qquad a\equiv-4E^2v^2pmod m.
\]

由 \(\gcd(u,v)=1\)，前两式等价于

\[
m\mid u,\qquad a\equiv-4E^2v^2pmod m. \tag{3}
\]

反向代入说明 (3) 也充分。因此 \(m\mid S/E\)，特别 \(m\mid S\)，每个进程只需
审计固定步长 \(S\) 的有限因子和 \(E^2\) 的一个残数类。

## 完整结果

对当前 14 条进程，每条恰有 564 个自然范围 \(m\equiv3\pmod4\) 缺口。脚本逐个计算
\(E,u,v\)，再用 (3) 在 \(E^2\) 的全部因子中选择 \(a\)。结果为：

| 项目 | 数目 |
|---|---:|
| 残存进程 | 14 |
| 每进程候选缺口 | 564 |
| 最短侧除子残数选择 | 19,366 |
| 常数 Type I 命中 | 0 |

## 位置

该结论补齐了统一多项式 Type I 除子的零次部分；此前已处理一次仿射部分和二次
\(d=x^2/h,\ h\le E\) 部分。它不处理随参数变化的非多项式因子、二次 \(h>E\) 尾部，
也不处理多源严格递降。

运行

```bash
python3 reproductions/type_i_h19_uniform_constant_boundary.py
python3 -m unittest tests/test_type_i_h19_uniform_constant_boundary.py -q
```

可重建所有候选和零命中结果。
