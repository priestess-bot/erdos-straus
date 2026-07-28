---
kind: claim
claim_id: type-I-linear-shifted-source-counterexample-878089
title: 878089 的全局线性移位源 B 等于一反例
statement: 在仓库当前普通 Type II p减一双尾遗漏序列中，p=878089 是“每个遗漏都有成功的 E整除n 线性移位源 B=1 桥”的首个反例。由 p=a+s+asR 和 min(a,s)不超过sqrt((p-2)/3) 完备枚举得到42个无序参数对、54个定向源状态及24个不同R；逐个完整分解K=(pR+1)/4并穷尽1655个除子后，目标剩余类命中为零。该点仍有一张beta=9的非线性上半区B=1桥，所以这不反驳自适应B=1或原混合终端猜想。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: independent_review
topics:
- type-I
- type-II
- shifted-source
- b1
- terminal-bridge
- selector-counterexample
- exhaustive-computation
- source-square
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-and-Type-II-certificate-context
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization-context
visibility: public
last_checked: '2026-07-28'
---

# \(p=878089\) 的全局线性移位源 \(B=1\) 反例

## 精确结论

令 \(p=878089\)。逐项成立：

1. \(p\) 没有普通 Type II \(p-1\) 双尾终端见证；
2. 对任意线性移位源状态 \(E\mid n\)，都不存在 \(B=1\) 的 Type I 正规形最大尾实现；
3. \(p\) 仍有一张成功的上半区 \(B=1\) Type I 桥，但其源平方正规分解满足
   \(\beta=9>1\)。

因此，下列加强命题为假：

\[
\text{普通 Type II 双尾失败}
\Longrightarrow
\text{存在成功的线性移位源 }E\mid n\text{ 的 }B=1\text{ 桥}.
\]

这里的“全局”不限制 Type I 缺口 \(m\)，但只讨论
[移位源 \(B=1\) 除子选择器](type-I-shifted-source-b1-divisor-residue-selector.md)定义的
正规形最大尾桥。

## 为什么线性源可以有限完备枚举

写

\[
n=p-s,\qquad E=sR+1,\qquad E\mid n,
\]

并令 \(a=n/E\)。则

\[
p=a+s+asR. \tag{1}
\]

反过来，任意满足 (1)、\(s\) 为奇数且 \(R\equiv3\pmod4\)、\(R\ge3\) 的
\((a,s,R)\) 都给出 \(E=sR+1\mid p-s\)。而且

\[
\min(a,s)^2\le as=\frac{p-a-s}{R}\le\frac{p-2}{3}. \tag{2}
\]

对本点，因而只需枚举

\[
1\le u=\min(a,s)\le
\left\lfloor\sqrt{\frac{p-2}{3}}\right\rfloor=541.
\]

令 \(v=\max(a,s)\)。由 (1)，

\[
p-u=v(1+uR). \tag{3}
\]

所以对每个 \(u\le541\)，完整分解 \(p-u\)，枚举每个除子
\(d=1+uR\mid p-u\)，再置 \(v=(p-u)/d\)，便不会漏掉任何线性源。
对 \(\{u,v\}\) 的每个奇数坐标作 \(s\) 定向，即得到全部定向状态。

## 全局排除结果

平方根枚举的精确计数为：

| 对象 | 数量 |
| --- | ---: |
| 无序 \((u,v,R)\) 参数对 | 42 |
| 定向 \((a,s,R,E,n)\) 线性源状态 | 54 |
| 不同模数 \(R\) | 24 |
| 全部 \(K=(pR+1)/4\) 的除数总数 | 1,655 |
| 去重后的可达除数剩余类数之和 | 1,244 |
| \(B=1\) 目标命中 | 0 |

24 个模数是

\[
\begin{aligned}
&3,7,11,23,31,59,71,87,111,159,199,279,287,375,503,871,\\
&1991,2439,3851,24391,146347,292695,439043,878087.
\end{aligned}
\]

对每个 \(R\)，计算

\[
K=\frac{pR+1}{4}.
\]

由 [\(B=1\) 单除子剩余判据](type-I-normal-source-state-b1-realization.md)，成功实现
当且仅当存在 \(C\mid K\) 满足

\[
4C\equiv-1\pmod R, \tag{4}
\]

等价地存在 \(H=K/C\equiv-1\pmod R\)。计算产物保存了每个 \(K\) 的完整素因数分解、
全部可达除数剩余类以及 (4) 的缺失；24 个 \(R\) 上的 \(C/H\) 命中数都为零。

独立测试没有复用 (2)--(3) 的平方根枚举，而是直接扫描全部 219,522 个奇数

\[
1\le s\le\frac{p-1}{2},
\]

并对每个 \(s\) 穷尽 \(E\mid p-s\)。它独立恢复同一组 54 个定向状态。

## 普通尾失败与“首个”的边界

\(p-1=2^3\cdot3\cdot36587\)。普通 Type II \(p-1\) 双尾的八个候选缺口为

\[
3,7,11,23,146347,292695,439043,878087,
\]

完整重算的见证数为零。

在权威五亿普通尾遗漏产物中，\(p\le878089\) 的遗漏共有 14 个。对前 13 个点逐点运行
同一全局线性源枚举均找到 \(B=1\) 见证，\(878089\) 首次失败。因此“首个”严格限定为
该已存普通尾遗漏序列中的首个，不声称脱离该输入产物独立证明一个新的素数前缀定理。

## 成功的非线性正对照

仓库权威 \(B=1\) 证书为

\[
\begin{gathered}
s=2065,\quad n=876024,\quad R=83,\quad E=171396,\quad K=18220347,\\
(m,A,B,C)=(143,74,1,2967),\quad H=6141.
\end{gathered}
\]

它是严格上半区偶源桥，并满足归一化源平方条件，但

\[
n\equiv19044\pmod E,
\]

所以 \(E\nmid n\)。取

\[
\lambda=4,\qquad u=\frac n\lambda=219006,
\qquad D=\frac E\lambda=42849,
\]

其唯一平方正规分解为

\[
u=46\cdot9\cdot529,
\qquad
D=9^2\cdot529.
\]

故 \((\alpha,\beta,\gamma)=(46,9,529)\)，明确有 \(\beta>1\)。精确回放为

\[
\frac4{878089}
=\frac1{219558}+\frac1{1348305678}+\frac1{15999086276883},
\]

以及

\[
\frac4{876024}
=\frac1{93126218}+\frac1{219558}+\frac1{1348305678}.
\]

因此该点不是自适应 \(B=1\) 选择器的反例；它严格说明在 \(B=1\) 目标限制内，
平方中超过 \(n\) 本身的额外指数在全局重选后仍可能是必需的。该点另有一般 \(B\)
的线性实现，所以不能把本结论升级为原一般-\(B\) 混合架构中的平方本质障碍。

## 一般 \(B\) 的线性正对照

同一素数在 \(B=1\) 限制之外确有线性桥：

\[
(a,s,R,E,K)=(4,3705,59,218596,12951813),
\]

\[
(m,A,B,C,H)=(55375,2,7,16669,111).
\]

这里 \(n=p-s=874384=4E\)，故 \(\beta=1\)；同时
\(B^2C=816781\mid K^2\)、\(4B^2C\equiv-1\pmod R\)，并且自然缺口及源、目标
两侧单位分数恒等式都由脚本和测试精确回放。这直接证明本卡的反例性来自 \(B=1\)
目标限制，而不是线性源在一般-\(B\) Type I 架构中完全失效。

## 证据与范围

- 实现：
  [type_i_linear_shifted_source_counterexample_878089.py](../reproductions/type_i_linear_shifted_source_counterexample_878089.py)
- 完整 54 状态及 24 个目标谱：
  [type-I-linear-shifted-source-counterexample-878089.json](../reproductions/type-I-linear-shifted-source-counterexample-878089.json)
- 独立直接 \(s\) 扫描：
  [test_type_i_linear_shifted_source_counterexample_878089.py](../tests/test_type_i_linear_shifted_source_counterexample_878089.py)

本卡只否定“普通尾失败必有线性 \(E\mid n\) 的 \(B=1\) 分支”。它不否定允许
\(\beta>1\) 的 [自适应上半区 \(B=1\) 猜想](type-I-adaptive-upper-b1-terminal-selector-conjecture.md)，
更不否定一般 \(B\) 的混合终端选择器或 Erdős--Straus 猜想。

~~~bash
python3 reproductions/type_i_linear_shifted_source_counterexample_878089.py
python3 -m unittest tests.test_type_i_linear_shifted_source_counterexample_878089 -v
~~~
