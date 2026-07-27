---
kind: claim
claim_id: type-II-ac-box-recursive-covering-boundary
title: 原始 AC 半径五盒的覆盖素数一层递归仍闭合
statement: 在原始 AC 盒 1<=A,C<=5 的一私有余因子安全模型中，素数 7 覆盖全部 240 个安全核心残数对应的线性型族。对每个残数及每个 n mod 7 分支，剥离每条余商中对该分支强制的最大 7 次幂，再要求所有剩余商为素数。精确枚举的 1,680 个分支中有 960 个仍使所有射线避靶，但均不构成可采纳线性型族；故这一深度二的强制因子模型没有条件性共同遗漏支。
claim_status: computationally_reproduced
topics:
- type-II
- ac-rays
- factorization
- admissibility
- recursive-obstruction
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

# 原始 AC 半径五盒的覆盖素数一层递归仍闭合

## 递归模型

从 type-II-ac-box-one-prime-local-closure 的原始射线盒

\[
1\le A,C\le5,\qquad p=Qn+r,\qquad Q=14400
\]

出发。素数 \(7\) 覆盖全部 240 个一私有余因子安全核心残数的线性型族

\[
p(n),\quad L_{A,C}(n)=(p+4A^2C)/D_{A,C}.
\]

故对每个 \(n=7m+b\) 分支，至少一个余商被 \(7\) 整除。审计对每条射线剥离余商中
对所有 \(m\) 强制的最大 \(7\) 次幂：

\[
p+4A^2C=D_{A,C}7^{e_{A,C,b}}P_{A,C,b}(m).
\]

然后完整检查新的固定因子全部除子残数，并测试 \(p(7m+b)\) 与全部
\(P_{A,C,b}(m)\) 的有限线性型局部可采纳性。

## 精确结果

| 覆盖素数 | 被覆盖安全残数 | 展开分支 | 仍避靶分支 | 可采纳分支 |
|---:|---:|---:|---:|---:|
| 3 | 80 | 240 | 240 | 0 |
| 7 | 240 | 1,680 | 960 | 0 |
| 11 | 240 | 2,640 | 1,560 | 0 |
| 13 | 240 | 3,120 | 1,968 | 0 |
| 17 | 240 | 4,080 | 3,936 | 0 |

特别地，\(7\) 对全部首层安全残数都有效。因此任意处于这一首层模型的候选点都会落入
表中 \(q=7\) 的 1,680 个分支之一；全部仍避靶分支都不可采纳。

重建：

    python3 reproductions/type_ii_prime_cofactor_boundary.py --ac-bound 5 \
      --recursive-covering-prime 3 --recursive-covering-prime 7 \
      --recursive-covering-prime 11 --recursive-covering-prime 13 \
      --recursive-covering-prime 17 \
      --output reproductions/type-ii-ac-box-recursive-covering-bound5-results.json
    python3 -m unittest tests/test_type_ii_prime_cofactor_ac_box.py -q

## 含义与边界

在 Dickson/Schinzel 型素数元组假设下，这排除半径五原始 AC 盒的深度二模型：首层
余商避靶、剥离覆盖素数 \(7\) 的全部强制幂后，每个剩余余商又都是素数。
它不排除第三层或更深的因子分解，也不构成该 AC 盒的 Type II 覆盖证明。

下一步应把当前覆盖素数、各射线已剥离的素因子幂和除子残数积集作为有限状态，研究
它是否在新增 \((A,C)\) 射线或模数扩张下闭合，或是否产生可提升的严格递降。
