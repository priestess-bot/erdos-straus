---
kind: claim
claim_id: type-I-linear-source-factor-transfer-rigidity
title: 线性源的固定 s 因子转移、K' 因子实现与完整谱边界
statement: 对核心素数 p 的线性源 p=a+s+asR，任取 q>1 满足 q|a 且 q=1 mod s，则 (a,s,R) 显式转移为 (a/q,s,qR+(q-1)/s)，仍是同一 p 的线性源；它严格减小 a、保持 s，并使 E=sR+1 乘以 q。相应 K'=(pR'+1)/4 被 q 整除。该机制是一个有限且可计算的固定-s 重选图，而非严格源分母递降。七个完整压力谱中，460 个目标失败状态有 406 个所在 s 纤维完全不含目标命中，故仅靠这种保持 s 的转移不能成为从任意线性源状态到目标命中的全称策略。
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

# 线性源的固定 \(s\) 因子转移、\(K'\) 因子实现与完整谱边界

## 定理

设核心素数 \(p\equiv1\pmod {24}\) 有一个线性源状态

\[
p=a+s+asR,\qquad s\equiv1\pmod2,\qquad R\equiv3\pmod4. \tag{1}
\]

记

\[
E=sR+1,\qquad K=\frac{pR+1}{4}. \tag{2}
\]

若正整数 \(q>1\) 满足

\[
q\mid a,\qquad q\equiv1\pmod s, \tag{3}
\]

令

\[
a'=\frac aq,\qquad
R'=qR+\frac{q-1}{s},\qquad
E'=sR'+1,\qquad
K'=\frac{pR'+1}{4}. \tag{4}
\]

则 \((a',s,R')\) 仍是同一 \(p\) 的线性源状态，且

\[
E'=qE,\qquad
p=a'+s+a'sR',\qquad
p-s=a'E'. \tag{5}
\]

此外

\[
R'>R,\qquad a'<a,\qquad q\mid K'. \tag{6}
\]

所以它定义一条在固定 \(s\) 纤维内、按 \(a\) 严格下降的有限重选边；这里的下降
不是 \(p-s\) 的下降，因为该源分母在转移中保持不变。

## 证明

令 \(t=(q-1)/s\)。由 (3)，\(t\) 是正整数。于是

\[
sR'+1=s(qR+t)+1=q(sR+1)=qE, \tag{7}
\]

并且

\[
\begin{aligned}
a'+s+a'sR'
&=\frac aq+s+\frac{as}{q}(qR+t)\\
&=a+s+asR,
\end{aligned} \tag{8}
\]

因为 \(st=q-1\)。这同时给出 (5) 和 \(R'>R\)、\(a'<a\)。

还须检查 \(R'\equiv3\pmod4\)，这不是一个可略去的形式条件。若
\(s\equiv1\pmod4\)，由 \(R\equiv3\pmod4\) 直接有

\[
R'\equiv3q+(q-1)\equiv3\pmod4. \tag{9}
\]

若 \(s\equiv3\pmod4\)，从 (1) 模 \(4\) 得

\[
1\equiv p\equiv a+3+9a\equiv2a+3\pmod4,
\]

所以 \(a\) 为奇数，从而 \(q\) 为奇数。再用 \(q\equiv1\) 或 \(3\pmod4\) 分别
代入 (4)，可得 \(R'\equiv3\pmod4\)。故 (4) 的新状态确实仍在严格参数域。

最后，由 \(p-s=aE=qa'E\) 和 \(t=(q-1)/s\)，

\[
4K'=4qK+t(p-s)=q(4K+t a'E). \tag{11}
\]

括号可被 \(4\) 整除：当 \(s\equiv1\pmod4\) 时 \(4\mid E\)；当
\(s\equiv3\pmod4\) 时 \(q\) 为奇数，故 \(t\) 为偶数且
\(E\equiv2\pmod4\)。所以 \(q\mid K'\)，完成证明。

## 严格范围

这不是递降证明。它只改变同一个源分母

\[
n=p-s=aE=a'E',
\]

而不产生更小的 \(n\)。它的价值在于：可以从一个已知线性源状态显式生成另一模数
\(R'\)，并且新 \(K'\) 被转移因子 \(q\) 整除。该 \(q\) 可能与旧 \(K\) 有公共
素因子，所以不能把这条结论误读为“总能注入一个全新的素因子”。是否因此命中
\(-1\in\mathcal C_{R'}(K')\)，仍是独立的目标谱问题。

反向操作只在已知某个 \(q\) 已经从 \(a\) 移入 \(E\) 的边上成立。任意由这种边组成的
路径都保持 \(s\)，因此不能跨越不同的 \(s\) 纤维。

## 七个完整谱的边界

对
[一般 \(B\) 障碍混合剖面](type-I-linear-general-b-obstruction-mixture-profile-600m.md)
中的七个完整线性源谱，逐一枚举每个状态的全部 \(q\mid a\)、\(q>1\)、
\(q\equiv1\pmod s\)，并重建 (4)--(11)。结果如下：

| 指标 | 数量 |
| --- | ---: |
| 有向线性源状态 | 490 |
| 目标谱命中的状态 | 30 |
| 目标谱失败的状态 | 460 |
| 失败但与某个命中状态同 \(s\) 的状态 | 54 |
| 失败且其整个 \(s\) 纤维没有命中的状态 | 406 |
| 已验证的向前因子转移边 | 463 |

特别是，这七个完整有限谱中的每个压力点都含有至少一个没有目标命中的 \(s\) 纤维。
因此，“从任意一个线性源状态出发，只反复使用固定 \(s\) 因子转移，最终必到达目标
命中”的策略已被该有限剖面否定。

这**不**反驳主选择猜想：选择器本来只需为每个 \(p\) 选到一个好状态，并不要求修复
每个失败状态。它排除的是一条更强的、任意起点的固定 \(s\) 重选路线。要把该转移用于
主问题，还需要一个会改变 \(s\) 的机制，或一个能直接选择进入可命中 \(s\) 纤维的定理。

## 可复现性

```bash
python3 reproductions/type_i_linear_source_factor_transfer_profile_600m.py
python3 -m unittest tests/test_type_i_linear_source_factor_transfer_profile_600m.py -q
```

生成工件固定上游七点完整障碍谱的 SHA-256，并验证每条转移都保留线性源恒等式、
\(R'\equiv3\pmod4\) 与 \(q\mid K'\)。
