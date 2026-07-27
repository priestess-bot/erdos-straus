---
kind: claim
claim_id: adaptive-external-source-escape-audit
title: 自适应外部源递降逃逸型的有限分类审计
statement: 在 p<=3*10^6 的核心素数中，去掉 m=3、(p+1)/2、p+4、4p+1 四条直接分支后剩余 1213 个；998 个有 adaptive-external-source-descent 的严格递降，215 个没有。完整平方因子外部源递降命中其中 199 个，奇距离至多 99 的偶源递降扇命中 134 个，允许全部 k<(p/4) 的非零平移平方因子外部源递降再命中 7 个，完整偶数标准大尾递降命中 3 个，四类补充分支并集命中 214 个；按这些真正递降机制表首个未命中点为 p=2451289。该点仍有 source=2 的直接外部源证书和 (A,C,K)=(1,2,13) 的 Type II 射线证书。后续的 type-II-two-tail-deflation-descent 可为旧表全部 215 个点提供带标记 Type II 证书表示，但由 type-II-scaled-tail-marked-lift-equivalence 它不消除真实递降逃逸；原结果仍是对所列机制的精确边界。
claim_status: computationally_reproduced
topics:
- descent
- external-source
- type-I
- type-II
- computation
- finite-audit
- proof-program
sources:
- paper: bradford2024
  locator: "Propositions 1--4"
  role: certificate-reconstruction
- paper: ventas2026
  locator: "Theorem 2.3"
  role: external-source-context
visibility: public
last_checked: '2026-07-24'
---

# 自适应外部源递降逃逸型的有限分类审计

## 分类对象

对每个核心素数 \(p\)，先排除四条直接因子分支

\[
m=3,\qquad (p+1)/2,\qquad p+4,\qquad4p+1.
\]

在余集上，测试 `adaptive-external-source-descent` 的所有允许参数

\[
k\mid\frac{p-1}{4},\qquad q=4k-1,\qquad
n_k=\frac{qp+1}{q+1},
\]

是否有一个因子 \(f\equiv-1\pmod q\)。未命中时，审计不把它称作无解或无证书；
而是另外记录：

1. 所有 \(k\) 的 \(n_k\) 素因子分解及模 \(q\) 残数；
2. 有限 source 窗口中最小的普通外部源见证，并正规化为 \(rp+1=4qt\)；
3. `quadratic-factor-external-source-descent` 的完整平方因子外部源递降；
4. 奇距离至多 99 的完整偶源递降扇；
5. 对余下实例穷举全部 \(k<(p/4)\) 的非零平移平方因子外部源递降；
6. 对仍余实例穷尽偶数标准大尾递降；
7. 有界 \(A,C\)、不限制 \(K\) 的 Type II AC 射线见证。

这把“递降选择器失败”与“直接证书失败”严格分开。

## \(3\cdot10^6\) 内结果

运行

```bash
python3 reproductions/adaptive_external_escape.py \
  --limit 3000000 --source-limit 128 --ac-bound 14 \
  --output reproductions/adaptive-external-escape-3m-results.json
```

得到

\[
\begin{array}{c|r}
\text{量} & \text{数目}\\
\hline
\text{四条直接分支后的残余} & 1213\\
\text{自适应严格递降命中} & 998\\
\text{自适应递降逃逸} & 215\\
\text{逃逸中完整平方因子外部源严格递降} & 199\\
\text{逃逸中距离至多 99 的偶源严格递降} & 134\\
\text{余下非零平移平方因子外部源严格递降} & 7\\
\text{最后偶数标准大尾严格递降} & 3\\
\text{最后三倍数标准大尾严格递降} & 0\\
\text{上述五类补充分支并集} & 214\\
\text{仍未命中任一记录递降} & 1\\
\text{逃逸中 source}\le128\text{ 的普通外部源证书} & 95\\
\text{逃逸中 }A,C\le14\text{ 的 Type II 证书} & 95
\end{array}
\]

在先前 \(10^6\) 审计中，逃逸样本的所选原始 Type II 射线最小半径为

\[
\begin{array}{c|rrrr}
\max(A,C)&2&3&4&5\\
\hline
\text{数目}&69&20&3&3.
\end{array}
\]

例如第一个逃逸 \(p=2521\) 的所有允许 \(k\) 都未触发该递降；但普通外部源给出
\((i,m,q,r,t)=(2,87,29,15,326)\)，而原始 Type II 射线给出
\((A,C,K,h,m,d)=(2,2,7,111,23,8)\)。

## 对研究路线的约束

这 95 个实例证明当前自适应外部源条件本身不是四条基础分支余集上的全覆盖选择器。
在 \(10^6\) 子范围中，完整平方因子外部源递降、距离至多 99 的偶源扇和其完整非零平移扩张合计接回
93 个真正的严格递降；剩余的两个实例
\[
253369,\qquad310489.
\]
对它们，全部奇距离 \(0<c<p\) 的偶源扇仍无严格提升，非零平移平方因子外部源也已在
全部 \(1\le k<(p/4)\) 上穷尽；但完整偶数标准大尾递降分别在源
\(127444\) 和 \(166532\) 命中。因此全部 95 个都有至少一条记录的严格递降，
并且仍各有两类直接证书。

在 \(3\cdot10^6\) 时，首个共同逃逸为

\[
p=2{,}451{,}289.
\]

它的普通外部源正规形是

\[
(i,m,q,r,t)=(2,79,31029,15515,306421),
\]

而 Type II 原始射线可取

\[
(A,C,K,h,m,d)=(1,2,13,103,23799,2).
\]

故它明确有两张直接证书。另一方面，审计已穷尽它的自适应外部源、完整平方因子
外部源、所有 \(1\le k<(p/4)\) 的允许平移平方因子外部源、全部奇距离偶源扇，
以及完整偶数和三倍数标准大尾扇，均未得到严格递降。这是当前最小的、可复核的
递降结构反例，不应被误述为 Erdős--Straus 猜想的反例。

这只是一个有限范围内、分支和参数上逐项穷举的审计结果；它不提供对更大素数的统一
参数界，也不蕴含原猜想。

特别要区分原始 AC 射线的 \(K\) 与互素正规形中的 tame 缺陷：
审计选择的原始见证中 91 个有 \(K>1\)，但原始参数可能含冗余，不能直接推出
Xu 意义的 non-tame。任何试图从这些 Type II 见证反向提炼递降的方案，必须先做
互素正规化，再证明所需映射确实以较小标记状态为源。

这些结果最适合作为第二选择器的反例库：候选递降若不能处理这份显式因子残数数据，
就不能被视为对当前边界的推进。它们不证明 source 128 或半径 14 为统一界，也不蕴含
原猜想。
