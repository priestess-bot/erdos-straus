---
kind: claim
claim_id: mixed-factor-h19-scale-15-transition-witness
title: H19-k23 残存素数的混合因子尺度十五转移见证
statement: H19-k23 的 v=17 残存进程在参数44处给出素数 p=69252070248001。其 B=(p-1)/4 的全部允许尺度 k<15 为 {1,2,3,4,5,6,8,9,10,12}；这些尺度的全部混合因子 g|k n_k、g<=n_k、g=-1 mod(4k-1) 均为空。下一允许尺度 k=15 有 n_15=68097869077201 和 g=353，产生从 n_15 到 p 的严格混合因子外部源提升。因此小尺度混合因子空结果不对更大自适应尺度单调传播。
claim_status: computationally_reproduced
topics:
- descent
- external-source
- mixed-factor
- adaptive-family
- state-transition
- conditional-boundary
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-certificate-and-lift-context
visibility: public
last_checked: '2026-07-25'
---

# H19-k23 残存素数的混合因子尺度十五转移见证

## 对抗点

取 H19-k23 状态树中 \(v\equiv17\pmod {29}\) 的残存进程，并令其参数为 44：

\[
p=69\,252\,070\,248\,001,
\qquad
B=\frac{p-1}{4}=17\,313\,017\,562\,000.
\]

脚本用确定性 Miller--Rabin 检查 \(p\) 及随后完整因子分解中的全部素因子。小于 15 的
\(B\) 的全部正因子恰为

\[
1,2,3,4,5,6,8,9,10,12. \tag{1}
\]

对每个 \(k\) 令

\[
q_k=4k-1,\qquad n_k=\frac{q_kp+1}{4k}.
\]

脚本保存并核验每个 \(k n_k\) 的完整素因子分解，枚举其全部正因子。对 (1) 中每一个
尺度都没有因子 \(g\) 满足

\[
g\mid k n_k,\qquad gle n_k,\qquad g\equiv-1pmod {q_k}. \tag{2}
\]

所以该点完整逃过所有允许的小尺度混合因子提升，而不是只逃过某几个预选射线。

## 第一个成功尺度

下一个允许尺度是 \(k=15\)，此时

\[
q=59,\qquad n_{15}=68\,097\,869\,077\,201,\qquad g=353.
\]

直接有 \(353\mid15n_{15}\)、\(353\le n_{15}\)，且

\[
353\equiv-1pmod {59}.
\]

混合因子构造给出

\[
\frac4{n_{15}}
=\frac1{15n_{15}}
+\frac1{17\,313\,017\,562\,090}
+\frac1{3\,339\,885\,561\,684\,097\,606\,291\,530},
\]

把首项替换为 \(1/(15n_{15}p)\) 后，等式成为 \(4/p\) 的表示，故这是严格从
\(n_{15}<p\) 出发的提升。

## 研究含义

该点同时有两层作用：它是当前 14 条进程中的一个真实素数样本，也给出对任何固定小尺度
闭合论证的反例。前十个允许尺度均失败，却在第 11 个允许尺度成功。因而可行的状态必须
记录尺度可扩张性、因子来源或一个不会在扩张时重置的势能；不能把
\(k\le12\) 的零结果外推为后续尺度也为空。

这只是一个精确的有限转移见证，不是“每个残存素数最终在某个尺度混合因子成功”的证明。

运行

```bash
python3 reproductions/mixed_factor_h19_scale_transition_witness.py
python3 -m unittest tests/test_mixed_factor_h19_scale_transition_witness.py -q
```

可重建小尺度的所有因子检查与尺度 15 的严格提升。
