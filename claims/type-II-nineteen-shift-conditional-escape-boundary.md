---
kind: claim
claim_id: type-II-nineteen-shift-conditional-escape-boundary
title: 模三剥离后十九条规范 Type II 射线的条件性逃逸
statement: 在前十九条平方自由规范 Type II 射线的一私有素因子模型中，Q_19=77597520 的精确审计得到 90827 个安全核心残数与 265001 个模三剥离后的可采纳分支。因而在 Dickson 素数元组猜想或相应 Schinzel 型线性多项式假设下，存在无穷多个 p=1 mod24 使前十九条规范射线全部失败。这个条件性边界排除固定十九移位扇加有限模三剥离作为全覆盖证明路线，但不构成 Erdős--Straus 猜想的条件性反例。
claim_status: computationally_reproduced
topics:
- type-II
- canonicalization
- multishift
- admissibility
- conditional-boundary
- obstruction
- proof-program
sources:
- paper: chamberland2026
  locator: "Theorem 1"
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-25'
---

# 模三剥离后十九条规范 Type II 射线的条件性逃逸

## 有限分支审计

令 \(s=1,\ldots,19\)，把每个 \(s=a_s^2c_s\) 写成平方自由规范形式，并令

\[
Q_{19}=\operatorname{lcm}\left(24,\{4a_sc_s:1\le s\le19\}\right)
=77{,}597{,}520.
\]

对每个核心残数 \(r\pmod {Q_{19}}\)，写 \(p=Q_{19}n+r\)，并取

\[
D_s=\gcd(Q_{19},r+4s),\qquad
p+4s=D_sL_s(n).
\]

若 \(r\) 在“每个 \(L_s\) 是素数”模型中仍让所有射线避靶，再令
\(n=3m+j\)，剥离每个 \(L_s(3m+j)\) 中对所有 \(m\) 强制的最大三次幂。对每个
余下分支，用有限域根覆盖判据检查下列 20 条线性型是否可采纳：

\[
3Q_{19}m+(Q_{19}j+r),\quad P_{1,j}(m),\ldots,P_{19,j}(m). \tag{1}
\]

完整枚举 \(1{,}658{,}880\) 个核心残数后得到

\[
\#\{\text{一私有因子安全残数}\}=90{,}827,\qquad
\#\{\text{可采纳二层分支}\}=265{,}001. \tag{2}
\]

其中每一个安全残数至少有一个可采纳二层分支。结果摘要在
`reproductions/type-ii-prime-cofactor-ladder-h19-summary.json`；用

```bash
python3 reproductions/type_ii_prime_cofactor_boundary.py --base-shift-bound 19
```

可重建完整检查。

## 条件性推论

假定 Dickson 素数元组猜想，或 Schinzel 型线性多项式素值假设。对任意一个 (1) 的
可采纳分支，存在无穷多个 \(m\) 使所有 20 条线性型同时为素数。对充分大的这些
\(m\)，各强制因子与余下素因子组成的完整除子残数集仍避开每条规范射线的目标
\(-1\)。因此得到无穷多个核心素数 \(p\)，使前十九条规范 Type II 射线全部失败。

这一步和 `type-II-mod-three-recursive-escape-boundary` 的证明形式相同，只是把
固定扇从十四条延至十九条；式 (2) 是新的有限输入。

## 正确的边界

“失败”仅指这十九条规范 Type II 射线不产生证书。这样的 \(p\) 仍可能有：

- 其它规范或非规范 Type II 射线证书；
- 非 \(AC\) 形式的 Type II 证书；
- Type I 证书或其它单位分数分解。

所以本结论既不是原猜想的条件性反例，也不否定允许 \(A,C\) 随 \(p\) 选择的
`type-II-ac-ray-saturation-conjecture`。

它排除的只是一个更窄的主张：不能期望通过固定前十九条规范移位、把每条余因子反复
按有限同余强制素数剥离，来无条件地证明这十九条中必有一条成功。直接证书路线若要
继续，必须使用随目标增长的**新移位**及其平方自由规范射线，或多移位因子分布中并未被
有限模可采纳性保留的信息。同一移位的非规范 \((A,C)\) 表示在序条件自动的范围内会被
规范射线支配，不能提供额外逃逸或覆盖自由度。

实际有限残余也排除了一个更简单的“私有因子数必增长”设想：在一千万范围的 45 个
十九移位共同失败点中，存在 \(p=1127281\) 使
\(p+76=7\cdot11^5\) 完全由 \(Q_{19}\) 的素因子组成，见
`type-II-nineteen-shift-transition-complexity-boundary`。后续结构引理必须使用
残数积集或跨移位加性关系，不能只数模数外素因子。
