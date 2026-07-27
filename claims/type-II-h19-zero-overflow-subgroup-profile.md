---
kind: claim
claim_id: type-II-h19-zero-overflow-subgroup-profile
title: H19 首个 r 状态零溢出失败的子群-指数分流
statement: 在存储的649个 r<=9999 首个偶源尾命中状态中，558个的普通除子集已命中 -1 mod r；余下91个虽无零溢出尾，但 -1 仍属于 M1 的素因子残数生成子群。故该有限剖面没有“目标在子群外”的零溢出障碍，所有91个失败均为有限指数积集不足，而非角色/子群障碍。
claim_status: computationally_reproduced
topics:
- type-I
- even-source
- overflow
- divisor-residues
- subgroup
- finite-product-set
- finite-audit
- h19
sources:
- paper: bradford2024
  locator: Proposition 1
  role: even-source-descent
visibility: public
last_checked: '2026-07-26'
---

# H19 首个 \(r\) 状态零溢出失败的子群-指数分流

零溢出偶源尾等价于 \(M_1\) 的普通除子集在模 \(r\) 命中 \(-1\)。令

\[
H(M_1,r)=\langle q\bmod r:q\mid M_1\rangle\subseteq(\mathbb Z/r\mathbb Z)^\times.
\]

若 \(-1\notin H(M_1,r)\)，即使允许每个素因子任意高幂，普通除子残数也不可能命中目标；
这是子群/角色障碍。反之，若 \(-1\in H\) 而实际 \(\operatorname{Div}(M_1)\) 尚未命中，
障碍只能来自每个素因子可用指数有限。

对存储的 \(r\le9999\) 首个命中剖面，得到：

| 分类 | 状态数 |
| --- | ---: |
| 普通除子已命中 \(-1\)（零溢出） | 558 |
| \(-1\in H\)，但指数不足 | 91 |
| \(-1\notin H\) | 0 |

因此此前 91 个高溢出状态并非角色条件阻止零溢出；它们已在无限指数的生成子群中可达，
却尚未由当前 \(M_1\) 的有限指数盒实现。这比单纯记录最小 \(B>1\) 更有方向性：要证明
混合选择器，优先应研究指数饱和、重复素因子或替代源如何补足有限指数，而不是研究新的
二次角色障碍。

这仍是 \(10^9\) H19 有限剖面，不能推出一般的无子群障碍定理。尤其生成子群中的可达性
不提供可用的指数上界，故本身不构造零溢出尾或严格递降。

可复现命令：

~~~bash
python3 reproductions/type_ii_h19_zero_overflow_subgroup_profile.py \
  --input reproductions/type-ii-h19-bounded-r-overflow-profile-1b-results.json \
  --output reproductions/type-ii-h19-zero-overflow-subgroup-profile-1b-results.json
python3 -m unittest tests/test_type_ii_h19_zero_overflow_subgroup_profile.py -q
~~~
