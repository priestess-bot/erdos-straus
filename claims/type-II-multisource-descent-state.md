---
kind: claim
claim_id: type-II-multisource-descent-state
title: H19 残余的多源平方因子递降状态路径
statement: 对 H19 规范 Type II 扇在 p<=2*10^7 的 65 个共同残余，按所有 k|(p-1)/4 的递增顺序检查完整平方因子外部源条件。每个点最终都有严格递降；首次成功 k 的频数为 1:25,2:25,3:4,4:2,5:3,6:4,12:2。成功前共有 81 个精确失败状态，单点最多有 9 个；p=8328961 逃过 H19 且 k=1,2,3,4,5,6,8,9,10 均失败，首次成功为 k=12。因此 H19 加所有 k<=10 的完整平方因子外部源选择器在该有限范围已失效。每个状态的成功判据精确等价于 -M_k 属于 M_k^2 的除子模 q_k 残数集，其中 n_k=p-(p-1)/(4k), M_k=kn_k, q_k=4k-1。
claim_status: computationally_reproduced
topics:
- type-II
- type-I
- descent
- external-source
- divisor-residues
- computation
- proof-program
sources:
- paper: bradford2024
  locator: "Propositions 1 and 3"
  role: certificate-and-descent-context
visibility: public
last_checked: '2026-07-25'
---

# H19 残余的多源平方因子递降状态路径

## 精确状态

设 \(p\equiv1\pmod {24}\)，且

\[
k\mid B=\frac{p-1}{4}.
\]

令

\[
n_k=p-\frac Bk=\frac{(4k-1)p+1}{4k},\qquad
q_k=4k-1,\qquad M_k=kn_k.
\]

则 \(\gcd(M_k,q_k)=1\)，完整平方因子外部源递降所需的因子条件为

\[
e\mid M_k^2,\qquad e\le M_k,\qquad e\equiv-M_k\pmod {q_k}. \tag{1}
\]

因此，若 \(\mathcal D(M_k^2;q_k)\) 表示 \(M_k^2\) 的全部除子模 \(q_k\) 残数集，
则

\[
\text{(1) 有解}\quad\Longleftrightarrow\quad
-M_k\in\mathcal D(M_k^2;q_k). \tag{2}
\]

右推左只须取目标残数的任一除子 \(e\)。若 \(e>M_k\)，则互补因子
\(M_k^2/e<M_k\) 也同余于 \(-M_k\)，因为

\[
M_k^2e^{-1}\equiv M_k^2(-M_k)^{-1}\equiv-M_k\pmod {q_k}.
\]

故 \(e\le M_k\) 不另增选择困难。命中后已有显式恒等式

\[
\frac4{n_k}=\frac1{M_k}+\frac1u+\frac1v
\Longrightarrow
\frac4p=\frac1{M_kp}+\frac1u+\frac1v,
\]

所以 (2) 给出的确实是严格提升。

## H19 残余路径

以两千万级 H19 共同残余的 65 个素数为输入，逐个按 \(k\) 的递增顺序检查 (2)。

| 首次成功 \(k\) | 1 | 2 | 3 | 4 | 5 | 6 | 12 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 点数 | 25 | 25 | 4 | 2 | 3 | 4 | 2 |

在首次成功前，共有 81 个失败状态；它们按候选 \(k\) 的出现次数为

| \(k\) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 失败状态数 | 40 | 15 | 11 | 5 | 3 | 2 | 1 | 1 | 1 | 2 |

最深的路径来自

\[
p=8\,328\,961.
\]

它已逃过 H19，并依次在

\[
k=1,2,3,4,5,6,8,9,10
\]

失败。到 \(k=12\) 时，\(q=47\)，残数集已等于全部 \(46\) 个单位，首次得到
\(e=5628\) 的严格递降。故“前十九条规范 Type II 射线或 \(k\le10\) 的完整平方因子
外部源递降”不是全称选择器，甚至在此有限样本内已经失败。

## 多源问题

这些源不是独立整数；它们满足

\[
n_k-n_\ell
=B\left(\frac1\ell-\frac1k\right). \tag{3}
\]

这正是下一阶段可以利用的额外结构。若所有早期 \(k\) 的状态均失败，每个
\(\mathcal D(M_k^2;q_k)\) 都避开一个明确目标；要取得逐点定理，须将这些残数集的联合
失败与 (3) 的差值关系、或与新增 Type II 移位的因子关系连接起来。单独对每个 \(k\)
使用筛法只会给密度界，不能替代这种跨源选择。

## 可复现性

```bash
python3 reproductions/type_ii_multisource_descent_state.py
python3 -m unittest tests/test_type_ii_multisource_descent_state.py -q
```

输入为
`reproductions/type-ii-h19-quadratic-descent-closure-20m-results.json`；输出逐点保存于
`reproductions/type-ii-multisource-descent-state-h19-20m-results.json`。

## 范围

这是一份有限的状态路径审计，不证明 H19、\(k\le12\) 或任何固定阈值的全称覆盖。
它的作用是给后续证明提供精确的失败语言与最小保持者，而不是将有限成功次数外推为规律。
