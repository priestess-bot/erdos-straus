---
kind: claim
claim_id: type-II-ac-box-one-prime-local-closure
title: 原始 AC 射线盒的一私有余因子局部覆盖边界
statement: 对原始 AC 射线盒 1<=A,C<=5 与 1<=A,C<=7，分别令 Q=lcm(24,{4AC}) 并写 p=Qn+r。若每条 p+4A^2C 都等于其 Q-强制因子乘一个素数余商，且全部原始射线仍失败，则相应 p 与全部余商线性型族都不可能可采纳。精确枚举中，半径 5 的 240 个安全核心残数与半径 7 的 5040 个安全核心残数均无可采纳分支。故最简单的一私有余因子条件逃逸模型在这两个原始 AC 参数盒中闭合。
claim_status: computationally_reproduced
topics:
- type-II
- ac-rays
- factorization
- prime-tuples
- admissibility
- obstruction
- proof-program
sources:
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
- paper: bradford2024
  locator: Section 2, Type II divisor certificates
  role: ray-certificate-context
visibility: public
last_checked: '2026-07-25'
---

# 原始 AC 射线盒的一私有余因子局部覆盖边界

## 模型

固定原始参数盒

\[
1\le A,C\le B,\qquad s=A^2C,\qquad M_{A,C}=4AC.
\]

必须保留每个原始 \((A,C)\)：即使两个参数对有相同移位 \(s\)，它们的模数
\(M_{A,C}\) 仍可能不同，不能用较强的规范射线替换原始盒。

令

\[
Q_B=\operatorname{lcm}\left(24,\{4AC:1\le A,C\le B\}\right),
\qquad p=Q_Bn+r,
\]

并对每条射线定义同余类强制因子

\[
D_{A,C}=\gcd(Q_B,r+4A^2C),\qquad
p+4A^2C=D_{A,C}L_{A,C}(n). \tag{1}
\]

审计采用极简逃逸模型：每个 \(L_{A,C}(n)\) 是一个充分大的素数，并完整检查
\(D_{A,C}L_{A,C}\) 的所有除子残数仍能避开该射线的 \(-1\pmod{4AC}\) 目标。若
所有射线皆避开，则再检查有限线性型族

\[
p(n),\quad \{L_{A,C}(n):1\le A,C\le B\} \tag{2}
\]

的局部可采纳性。若某个素数在每个参数类上都整除 \((2)\) 中至少一条型，则这些型不可能
同时取充分大的素数。

## 精确结果

| 原始盒半径 \(B\) | 射线数 | \(Q_B\) | 核心残数 | 一私有安全残数 | 可采纳安全残数 |
|---:|---:|---:|---:|---:|---:|
| 5 | 25 | 14,400 | 480 | 240 | 0 |
| 7 | 49 | 705,600 | 20,160 | 5,040 | 0 |

半径 5 中，安全残数的局部覆盖素数统计为

\[
3:80,\quad 7:240,\quad 11:240,\quad13:240,\quad17:240.
\]

半径 7 中为

\[
3:1680,\quad11:5040,\quad13:5040,\quad17:5040,
\quad19:5040,\quad23:5040.
\]

例如第二行的 \(11,13,17,19,23\) 都覆盖每一个安全残数对应的线性型族；因此不存在
一条可采纳分支。每个计数来自对模 \(Q_B\) 的全部核心残数、每条原始射线的完整除子
残数以及所有不超过型数的有限域根覆盖检查，未使用素数分布启发式。

重建：

```bash
python3 reproductions/type_ii_prime_cofactor_boundary.py --ac-bound 7 \
  --output reproductions/type-ii-ac-box-one-prime-bound7-results.json
python3 -m unittest tests/test_type_ii_prime_cofactor_ac_box.py -q
```

## 含义与边界

在 Dickson/Schinzel 型素数元组假设下，这排除了每条原始 AC 射线只剩一个新素因子的
无穷共同失败模型。它并不证明 AC 盒覆盖全部核心素数：真实失败仍可让某个
\(L_{A,C}\) 含两个或更多私有素因子，而现有多移位审计已表明这类复杂度不能预先设为
常数。

因此，这是一项针对有界 AC 短证书路线的正向压缩，而不是对 Type II 射线饱和猜想的
证明。下一步必须递归追踪被局部覆盖强制出现的额外素因子及其残数积集，并在模数扩张时
重新计算旧射线的强制因子。
