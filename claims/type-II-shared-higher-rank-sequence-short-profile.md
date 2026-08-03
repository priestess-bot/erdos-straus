---
kind: claim
claim_id: type-II-shared-higher-rank-sequence-short-profile
title: 共享 Type II 秩至少三子群的序列级短零积 profile
statement: 在 p<=10^7、m<=239 的 84 个四自动缺口非 k=1 压力点中，完整 Type II 缺口扫描只出现 19 个秩至少三的单位残数生成子群；对按 p+m 素因子顺序给出的有限序列做精确 0/1 动态零积搜索时，4 个压力点产生可提升的共享除子，80 个未产生。该结论是有限序列计算 profile，不是一般秩至少三 Davenport 定理。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-II-shared-residue-selector-conjecture
  - type-II-shared-rank-two-davenport-threshold
  - type-II-two-tail-deflation-descent
topics:
- type-II
- shared-divisor
- finite-abelian-groups
- rank-three
- zero-sum-theory
- short-certificate
- marked-lift
- proof-boundary
sources:
  - reproduction: reproductions/type_ii_automatic_residual_k1_funnel.py
    role: exact-invariant-factor-and-short-zero-product-profile
  - result: reproductions/type-ii-automatic-residual-higher-rank-short-profile-10m-results.json
    role: focused-10m-higher-rank-sequence-profile
  - claim: type-II-shared-rank-two-davenport-threshold
    role: lower-rank-threshold-context
visibility: public
last_checked: '2026-08-04'
---

# 共享 Type II 秩至少三子群的序列级短零积 profile

## 定义与有限命题

在四条自动共享缺口之后，取一千万范围内的 84 个非 k=1 压力点。对每个合法缺口
m = 3 mod 4、m <= 239 且已有 Type II 证书，令 q_1,...,q_t 为 p+m 中与 m 互素的
素因子，按重数列出，并令 H 为这些残数 q_i mod m 生成的单位子群。

脚本先由各 primary 扭元子群的精确基数恢复 H 的不变因子。若 rank(H) >= 3，再对
给定素因子序列运行 0/1 动态程序：每个因子最多使用一次，状态是当前乘积残数，并在
每个残数保留最短长度及其实际整数乘积。若找到非空子序列 I，则得到

    D_I > 1, D_I | p+m, D_I = 1 mod m.

随后逐项重放已有 Type II 证书的 scaled-first marked lift。故本卡的“命中”是同一
缺口上的共享除子和可提升 marked witness，而非无标记递降。

## 10M、m<=239 回执

完整扫描结果为：

- 秩至少三的 Type II 缺口：19 个，全部为秩三；
- 不变因子结构：C2 + C2 + C30 共 17 个，C2 + C4 + C12 共 2 个；
- 序列级最短非空零积命中 4/84 个压力点，未命中 80/84；
- 4 个见证及其最短子积长度为：p=2669209（m=231, D_I=667360, length=8）；
  p=2852809（m=195, D_I=18526, length=3）；p=6254329（m=231, D_I=2080, length=7）；
  p=7504249（m=231, D_I=16864, length=7）。

其中 p=2852809 与既有秩二 profile 的见证重合；其余三个素数是对秩二回放的新增
压力点。因而这一步不是覆盖率闭合，而是把剩余搜索具体化为秩三有限群中的低于未知
Davenport 阈值的短零积与序列排序问题。

## 边界

本卡不使用、也不声称一般秩至少三有限阿贝尔群的 Davenport 常数公式。动态程序
只看脚本提供的素因子多重序列；“未命中”不排除另一个因子顺序、同一压力点的其它
合法缺口、不依赖该序列的群论零和证书、跨缺口联合选择或直接 Type II 终端。

同样，命中只给出 marked Type II 表示；从 marked 状态到无标记递降仍需独立的
全域提升与良基势证明。因此它不能单独闭合共享 Type II 选择器猜想或 Erdős--Straus
猜想。

## 复现

    python3 reproductions/type_ii_automatic_residual_k1_funnel.py --limit 10000000 --gap-cap 239 --higher-rank-short-profile --output reproductions/type-ii-automatic-residual-higher-rank-short-profile-10m-results.json
