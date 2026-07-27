---
kind: claim
claim_id: type-II-ac-box-depth-four-recursive-escape
title: 原始 AC 半径五盒的四层局部覆盖递归重新出现可采纳逃逸
statement: 在原始 AC 盒 1<=A,C<=5 中，从全部240个一私有余因子安全根状态出发，第一步统一选覆盖素数7，之后每个状态选其最小局部覆盖素数，完整枚举四次参数分支与强制素因子幂剥离。逐层得到720、3420、22276、268250个仍避靶状态；第四层的268250个状态中242390个剩余线性型族可采纳。特别地，初始残数1和分支(7,0),(11,0),(13,0),(17,0)给出 p(t)=245044800t+1 的显式可采纳见证。故在 Dickson/Schinzel 型素数元组假设下，固定半径五 AC 盒存在无穷多个逃过该四层递归模型的核心素数。
claim_status: computationally_reproduced
topics:
- type-II
- ac-rays
- factorization
- admissibility
- conditional-boundary
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

# 原始 AC 半径五盒的四层局部覆盖递归重新出现可采纳逃逸

## 状态转移

从原始盒 \(1\le A,C\le5\) 的一私有余因子状态

\[
p+4A^2C=F_{A,C}L_{A,C}(t)
\]

出发。若目标素数线性式与全部余商线性式被素数 \(q\) 局部覆盖，则枚举
\(t=qu+b\)。目标式恒被 \(q\) 整除的分支不能产生充分大的目标素数，故丢弃；对其余
分支，剥离每个余商中对所有 \(u\) 强制的最大 \(q\)-幂，并重新检查更新后固定因子的
全部除子残数。每一步只保留所有原始 AC 射线仍避开 \(-1\pmod{4AC}\) 的状态。

第一步对全部根状态选共同覆盖素数 \(7\)，此后在每个状态选其最小覆盖素数。选择一个
覆盖素数不会遗漏候选参数，因为该素数已覆盖该状态中参数的每个残数类。

## 四层枚举

240 个根状态按 60 个一组分成四个独立切片，逐层相加得到：

| 转移步数 | 输入状态 | 展开分支 | 目标素数整除分支 | 仍避靶状态 |
|---:|---:|---:|---:|---:|
| 1 | 240 | 1,680 | 240 | 720 |
| 2 | 720 | 6,000 | 480 | 3,420 |
| 3 | 3,420 | 43,020 | 3,420 | 22,276 |
| 4 | 22,276 | 363,572 | 22,276 | 268,250 |

末层 268,250 个仍避靶状态中，有 242,390 个目标式和全部剩余余商式的局部覆盖素数集
为空，因而是可采纳线性型族。故此前的二层闭合不是单调势函数：强制因子状态在更深层
重新打开。

## 显式见证

初始残数为 \(p\equiv1\pmod{14400}\)。连续选择

\[
(q,b)=(7,0),(11,0),(13,0),(17,0)
\]

得到 \(p(t)=245044800t+1\)。对每一个原始 \((A,C)\)，审计给出正整数
\(F_{A,C}\) 与正仿射式 \(P_{A,C}(t)\)，满足

\[
p(t)+4A^2C=F_{A,C}P_{A,C}(t),
\]

并且每条射线的固定因子与余商的全部除子残数均避开 Type II 目标。全部 25 条因子
恒等式、余商线性式和空覆盖检验保存在
reproductions/type-ii-ac-box-recursive-depth4-batch-0-results.json 的
recursive_admissible_witness 字段中。例如

\[
p(t)+4=5(49008960t+1),\qquad p(t)+8=9(27227200t+1).
\]

该见证的目标式和全部剩余余商式构成可采纳族。假定 Dickson 素数元组猜想或相应的
Schinzel 型线性多项式素值假设，存在无穷多个 \(t\) 使这些不同线性式同时为素数。
于是该固定 AC 盒的所有射线都失败。

重建四个切片：

    python3 reproductions/type_ii_prime_cofactor_boundary.py --ac-bound 5 \
      --recursive-covering-prime 7 --recursive-depth 4 \
      --root-start 0 --root-stop 60 \
      --output reproductions/type-ii-ac-box-recursive-depth4-batch-0-results.json

将根切片依次改为 60--120、120--180、180--240，即可重建其余三份结果并逐层相加。

## 含义与边界

这是固定半径五 AC 盒、固定的“局部覆盖后剥离全部强制幂”递归的条件性逃逸边界，
不是 Erdős--Straus 猜想的条件性反例。它只说明这 25 条 Type II 射线与这种有限深度
因子状态不能给出全称覆盖；其它 AC 射线、Type I 证书和可提升递降仍可能解决同一目标。

因此下一条正向路线必须跨越固定盒：要么在递归状态中加入随深度增长的新 \((A,C)\)
射线并证明状态减少，要么把某类状态接到可验证的严格递降，而不能只对已有射线继续做
局部可采纳性剥离。
