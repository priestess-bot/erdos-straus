---
kind: claim
claim_id: type-II-canonical-small-shift-joint-profile
title: 小规范移位共同失败以支撑外二次深度零为主
statement: 在 p<=10^6 的 9732 个核心素数中，规范移位 s=1,...,14 捕获 9708 个，余下 24 个。对这 24 个 p 的 14 条失败射线逐一作完整除子残数分析，336 个失败中有 297 个是 -1 不属于素因子残数生成支撑且二幂深度为零的支撑外失败；其余 39 个是支撑内缺陷，24 个目标素数出现 22 种不同的十四维失败签名。故此有限共同残余不存在可由单一小缺陷型解释的主机制；下一步须处理随射线和素数变化的支撑外分离字符或直接使用实际因子分布。
claim_status: computationally_reproduced
topics:
- type-II
- canonicalization
- divisor-residues
- failure-profile
- computation
- proof-program
sources:
- paper: grynkiewicz_marchan_ordaz2009
  locator: "subsequence-product framework; Theorem C"
  role: residue-product-set-context
- paper: chamberland2026
  locator: "Theorem 1"
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-24'
---

# 小规范移位共同失败以支撑外二次深度零为主

## 审计对象

取 `type-II-canonical-squarefree-ray-dominance` 的前十四条规范移位

\[
s=1,2,\ldots,14,
\]

并将每个 $s$ 唯一写成 $s=a_0^2c_0$（$c_0$ 平方自由）。对每个
$p\equiv1\pmod{24}$，相应射线检查

\[
h\mid p+4s,\qquad h\equiv-1\pmod {4a_0c_0}. \tag{1}
\]

在 $p\le10^6$ 时，共有 $9732$ 个核心素数；其中 $9708$ 个被至少一条 (1)
捕获，留下 24 个共同失败点。

对每个失败射线，令 $K$ 为 $p+4s$ 的全体素因子残数所生成的单位群子群。记录：

1. 若 $-1\notin K$，则记录其最小二幂分离深度；
2. 若 $-1\in K$ 但未由任一除子取得，则记录支撑内缺失集大小。

这里“支撑外深度零”表示 $-1\notin K U(M)^2$，其中
$M=4a_0c_0$。它允许一个核心活跃的二次分离字符，但字符并不预先固定。

## 结果

24 个共同失败点给出 $24\times14=336$ 条失败射线，其中

\[
297\quad\text{条为支撑外深度零},\qquad
39\quad\text{条为支撑内缺陷}. \tag{2}

此外，24 个目标点产生 22 个不同的十四维类型签名。也就是说，即使只观察这很小的
有限共同残余，也没有一个单一的“缺失集大小”或固定字符类型统一解释它们。

运行

```bash
python3 reproductions/type_ii_canonical_ray.py --limit 1000000 --ac-bound 14 \
  --base-shift-bound 14 \
  --output reproductions/type-ii-canonical-rays-1m-results.json
```

会保存每一个 $p+4s$ 的完全素因子分解、支撑内外分类、深度或缺陷大小，以及
确定性贪心补充射线；这使 (2) 可逐项复核。

## 对下一步的限制

这不是全称频率定理，也不能从 24 个点推断渐近比例。它的价值是排除一项不值得继续的
局部假设：不能期待只靠“一孔或小孔支撑缺陷”闭合小移位共同残余。

由于多数失败已在素因子生成支撑层面排除 $-1$，后续引理必须解决支撑外情况。现有
`type-II-fixed-quadratic-character-boundary` 已说明对单条模数也不能固定一个字符；而
`type-II-character-product-congruence-compatibility-boundary` 又排除只保留总积字符值的
多射线反证。可行的新输入必须利用不同移位数的实际逐素因子分布，或构造新的直接证书/
递降边，而不能只加一层有限同余条件。
