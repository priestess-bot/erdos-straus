---
kind: claim
claim_id: type-I-linear-source-shift-transfer-closure-boundary
title: 线性源的变 s 因子转移及双转移闭包边界
statement: 对核心素数 p 的线性源 p=a+s+asR，若 q>1 满足 q|s、q=1 mod a 且 R'=qR+(q-1)/a=3 mod4，则 (a,s/q,R') 是同一 p 的线性源，满足 aR'+1=q(aR+1)、q|K'；该边严格减小 s，故使源分母 p-s 严格增大而非递降。与固定 s 因子转移的前向边合并后，七个完整压力谱共有 719 条边，但仅 39/490 个状态可达目标谱命中，460 个失败状态中仅 9 个可达。因此这两个前向局部因子转移不能构成通用终端选择器。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- linear-source
- shifted-source
- source-state
- factorization
- reselection
- target-square-divisor
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 线性源的变 \(s\) 因子转移及双转移闭包边界

## 变 \(s\) 转移

设

\[
p=a+s+asR,\qquad s\equiv1\pmod2,\qquad R\equiv3\pmod4, \tag{1}
\]

并令

\[
K=\frac{pR+1}{4}. \tag{2}
\]

取 \(q>1\) 满足

\[
q\mid s,\qquad q\equiv1\pmod a. \tag{3}
\]

写

\[
s'=\frac sq,\qquad
t=\frac{q-1}{a},\qquad
R'=qR+t. \tag{4}
\]

则 \(s'\) 仍为奇数。新三元组处于线性源严格参数域，当且仅当

\[
R'\equiv3\pmod4. \tag{5}
\]

这是一个可直接检查的条件；等价地，

\[
\boxed{a\ \text{为奇数}\quad\text{或}\quad4\mid t.} \tag{6}
\]

在 (5) 成立时，\((a,s',R')\) 是同一 \(p\) 的线性源状态，且

\[
aR'+1=q(aR+1),\qquad
p=a+s'+as'R',\qquad
q\mid K'=\frac{pR'+1}{4}. \tag{7}
\]

它严格改变移位坐标：

\[
s'<s,\qquad p-s'>p-s. \tag{8}
\]

故这是一条朝更大源分母的状态边，不能被称为“严格递降”。

## 证明

由 (3)，\(q\) 为奇数。式 (4) 直接给出

\[
aR'+1=a(qR+t)+1=q(aR+1), \tag{9}
\]

因为 \(at=q-1\)。再计算

\[
\begin{aligned}
a+s'+as'R'
&=a+\frac sq+\frac{as}{q}(qR+t)\\
&=a+s+asR=p.
\end{aligned} \tag{10}
\]

因此只须检查 \(R'\) 的模 \(4\)。

若 \(a\equiv1\pmod4\)，则 \(q\equiv1+t\pmod4\)，故

\[
R'\equiv3(1+t)+t\equiv3\pmod4. \tag{11}
\]

若 \(a\equiv3\pmod4\)，则 \(q\equiv1+3t\pmod4\)。又 \(q\) 为奇数，故 \(t\)
为偶数，从而

\[
R'\equiv3(1+3t)+t\equiv3+2t\equiv3\pmod4. \tag{12}
\]

若 \(a\) 为偶数，\(a\equiv0\) 或 \(2\pmod4\)。直接代入
\(q=1+at\) 到 \(R'=3q+t\) 可得两种情形都等价于 \(t\equiv0\pmod4\)。这证明
(5)--(6)。

最后 \(aR'+1=q(aR+1)\)。令 \(E'=s'R'+1\)，有

\[
4K'=E'(aR'+1)=qE'(aR+1).
\]

由于 \(q\) 为奇数，除以 \(4\) 后仍有 \(q\mid K'\)。式 (8) 由 \(q>1\) 立即成立。

## 与固定 \(s\) 边的合并

[固定 \(s\) 因子转移](type-I-linear-source-factor-transfer-rigidity.md)满足

\[
(a,s,R)\longmapsto
\left(\frac aq,s,\ qR+\frac{q-1}{s}\right), \tag{13}
\]

严格减小 \(a\) 而保持 \(s\)。本页的变 \(s\) 边保持 \(a\) 而严格减小 \(s\)。
二者联合后，任何向前路径都使字典序 \((s,a)\) 严格下降，所以状态图无有向环；
但它的终点未必是目标谱命中，更不自动提供单位分数解或严格递降。

## 七个完整谱的闭包边界

对七个完整线性源谱，枚举全部固定 \(s\) 边和满足 (5) 的变 \(s\) 边，再从所有精确
一般 \(B\) 目标命中反向做可达性闭包：

| 指标 | 数量 |
| --- | ---: |
| 有向线性源状态 | 490 |
| 目标谱命中状态 | 30 |
| 固定 \(s\) 转移边 | 463 |
| 原始变 \(s\) 因子候选 | 496 |
| 可行变 \(s\) 转移边 | 256 |
| 两类边合计 | 719 |
| 可达目标命中的状态 | 39 |
| 可达目标命中的失败状态 | 9 |
| 仍不可达的失败状态 | 451 |

变 \(s\) 边确实能穿过固定 \(s\) 的纤维障碍：恰有两个原先 \(s\)-孤立的失败状态经一步
直接到达目标命中，

\[
\begin{array}{c|c|c}
p&(a,s,R)&(a,s',R')\\
\hline
2\,210\,569&(1,276321,7)&(1,92107,23)\\
536\,944\,489&(1,67118061,7)&(1,22372687,23).
\end{array}
\]

但其余五个压力点没有任何失败状态经这两个转移的任意有限组合到达命中。该有限结果
排除“只沿这两个前向局部因子转移即可把任意线性源推进到目标谱”的策略。反向边和
其它因子重分配没有在本剖面中审计；它也不排除直接选择好状态、改变其它参数、或使用
Type II/其它 Type I 机制的证明。

## 可复现性

```bash
python3 reproductions/type_i_linear_source_shift_transfer_closure_profile_600m.py
python3 -m unittest tests/test_type_i_linear_source_shift_transfer_closure_profile_600m.py -q
```
