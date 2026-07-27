---
kind: claim
claim_id: type-II-h19-mixed-only-prime-factor-boundary
title: H19 半径六失败支路的单、双素因子 mixed 选择器边界
statement: 对十亿 H19 剖面中17个仅靠 mixed-factor 递降闭合的状态，穷尽每个 k|(p-1)/4 后，13个可由某个单素因子 g|kn、g<=n、g=-1 mod(4k-1) 触发严格递降；6868801、107158921、165479161、942584161 四点在所有允许尺度均无这样的单素因子。再穷尽全部 mixed 因子，最少不同素因子数分布为1:13、2:3、3:1；942584161 的任意 mixed 因子至少有三种不同素因子。因此单、双素因子 mixed 选择器均不足以闭合这个固定边界。
claim_status: computationally_reproduced
topics:
- type-I
- descent
- external-source
- factorization
- finite-audit
- h19
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-certificate-context
- paper: ventas2026
  locator: Theorem 2.3
  role: external-source-context
visibility: public
last_checked: '2026-07-27'
---

# H19 半径六失败支路的单、双素因子 mixed 选择器边界

在 [H19 十亿残余的半径六 AC 或 mixed-factor 严格递降闭合](type-II-h19-mixed-short-or-descent.md)
中，17 个状态不具有半径六直接 AC 证书，因而必须由 mixed-factor 分支闭合。对每个状态的
每个允许尺度

\[
k\mid\frac{p-1}{4},\qquad q=4k-1,\qquad n=\frac{qp+1}{q+1},
\]

穷尽 \(kn\) 的全部**素因子** \(\ell\)，检查

\[
\ell\le n,\qquad \ell\equiv-1\pmod q. \tag{1}
\]

若 (1) 成立，取 \(g=\ell\) 即为 mixed-factor 严格递降。17 点中有13点存在这样的
单素因子见证；余下四点在所有允许的 \(k\) 上均失败：

| \(p\) | 存储的 mixed \((k,q,g)\) | \(g\) 的素因子分解 |
| ---: | --- | --- |
| \(6{,}868{,}801\) | \((3,11,3057)\) | \(3\cdot1019\) |
| \(107{,}158{,}921\) | \((2,7,5732)\) | \(2^2\cdot1433\) |
| \(165{,}479{,}161\) | \((14,55,5719)\) | \(7\cdot19\cdot43\) |
| \(942{,}584{,}161\) | \((10,39,123005)\) | \(5\cdot73\cdot337\) |

这些 \(g\) 都满足 mixed 条件，故四点仍有严格递降；结论仅是它们不允许把该递降压缩为
任何尺度上的单素因子 \(g\)。进一步对所有 \(g\mid kn\) 的完整枚举表明，最少不同素因子
支持数的分布是

\[
1:13,\qquad2:3,\qquad3:1.
\]

其中

\[
p=942{,}584{,}161
\]

在任意允许尺度均没有支持数至多2的 mixed 因子；存储的最小支持见证正是
\(g=123005=5\cdot73\cdot337\)。因此未来的强制引理至少必须允许三素因子积，或提供
另一条短证书/递降出口。它不能只追踪“出现一个目标残数素因子”，也不能止于双素因子积。

可复现命令：

~~~bash
python3 reproductions/type_ii_h19_mixed_only_prime_factor_profile.py \
  --input reproductions/type-ii-h19-mixed-short-or-descent-1b-results.json \
  --output reproductions/type-ii-h19-mixed-only-prime-factor-profile-1b-results.json
python3 -m unittest tests/test_type_ii_h19_mixed_only_prime_factor_profile.py -q
~~~
