---
kind: claim
claim_id: type-II-shared-residue-selector-conjecture
title: 共享除子残数 Type II 选择器猜想
statement: 猜想对每个素数 p=1 mod24，存在合法缺口 m=3 mod4、x=(p+m)/4，使 1 是 4x 的某个非平凡除子模 m 的残数，且 -x 是 x^2 的某个除子模 m 的残数。后一条件给出 Type II 证书，前一条件是共享因子标记；因此该猜想蕴含 Erdős--Straus 猜想。它是短证书猜想，而不是无标记递降猜想。
claim_status: open
topics:
- type-II
- conjecture
- divisor-residues
- factor-selection
- short-certificate
- proof-program
sources:
- paper: bradford2024
  locator: Section 2, Type II divisor certificates
  role: certificate-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
- claim: type-II-shared-rank-two-davenport-threshold
  role: rank-at-most-two-local-threshold
visibility: public
last_checked: '2026-08-04'
---

# 共享除子残数 Type II 选择器猜想

## 精确命题

对与 \(m\) 互素的正整数 \(N\)，记

\[
\Pi_m(N)=\{d\bmod m:d\mid N\}.
\]

并记

\[
\Pi_m^{>1}(N)=\{d\bmod m:d\mid N,\ d>1\}.
\]

猜想每个核心素数 \(p\equiv1\pmod {24}\) 都存在

\[
3\le m\le p-2,\qquad m\equiv3\pmod4,\qquad
x=\frac{p+m}{4},
\]

满足

\[
1\in\Pi_m^{>1}(4x),
\qquad
-x\in\Pi_m(x^2). \tag{1}
\]

第一式中的 \(\{1\}\) 指整数除子 \(1\) 的平凡贡献；也就是说，要求存在
\(D>1\) 使

\[
D\mid4x,\qquad D\equiv1\pmod m. \tag{2}
\]

## 为什么它给出短证书

由 `gap-residue-reachability`，(1) 的第二个条件等价于该缺口有一张合法 Type II
证书。这里无需额外要求证书除子不大于 \(x\)：补因子对合保持目标残数 \(-x\)，故
自然范围自动满足。

条件 (2) 令 \(k=(D-1)/m\)，从而

\[
km+1=D\mid p+m,\qquad km+1\mid kp-1.
\]

它提供 `type-II-scaled-first-tail-deflation` 的带标记源表示；但根据
`type-II-scaled-tail-marked-lift-equivalence`，这一表示不能被误作无标记归纳。
即使完全忽略它，第二个条件已经直接给出目标 \(4/p\) 的 Type II 证书。因此本猜想
是一条纯粹的短证书充分路线。

## 当前证据

`type-II-shared-divisor-fan-audit` 的精确审计验证了更强的有限断言：
对全部 \(p\le10^7\) 的 \(82{,}887\) 个核心素数，可取

\[
m\le239
\]

使 (1) 成立。该审计没有对 (2) 所诱导的 \(k\) 加上界；最大记录尺度为
\(664{,}185\)。所以有限数据支持小缺口，但明确反对固定小尺度假设。

小缺口并非完全黑箱：`type-II-small-shared-gap-explicit-fan` 证明在
\(m=3,7,11\) 时共享因子分别可固定为 \(4,8,12\)，并给出一个覆盖
\(83.1313\%\) 的显式 Type II 子扇。其余一般因子选择将前三缺口的有限覆盖提高至
\(96.7124\%\)，但还没有统一的因子分布定理。

`type-II-small-shared-gap-single-prime-fan` 再将 \(m=7,11\) 的一个指定残数
素因子转成显式除子，覆盖提高至 \(92.2000\%\)。这把小缺口的下一层难点精确定位为
目标残数只能由多个素因子共同产生的情形。

`type-II-small-shared-gap-linear-square-profile` 进一步将前三缺口的全部 Type II
命中分成线性除子与平方专用除子：前者在千万范围占 \(95.079\%\)，后者只占
\(1.633\%\)。这给出了优先研究平方专用残余和三缺口未命中残余的精确理由。

自动共享结构还延伸到 \(m=23\)：`type-II-shared-gap-23-automatic-fan` 给出固定
共享因子 \(24\) 与九个常数除子类。将其与前三缺口合并后，千万范围内只留下
\(973\) 个四缺口未命中点。

`type-II-automatic-shared-gap-classification` 证明这四条已经穷尽所有仅由
\(p\equiv1\pmod {24}\) 强制、且共享因子不随 \(p\) 变化的缺口。因而剩余问题不能靠
继续增加常数共享因子解决，必须转向自适应因子选择。

在四自动缺口残余内，`type-II-automatic-residual-k-one-funnel` 又将目标缩到
一千万范围的 84 个非 \(k=1\) 点：其余 889 个仍由 \(D=m+1\) 选择器命中。
这些 84 点已有有限的 \(k>1\) 证书，因而是研究自适应共享因子而非继续扩展常数扇的
最小压力集。

这 84 点也不能被单素因子或单素数幂规则解释。对每个点的全部 \(m\le239\)
Type II 缺口扫描后，9 点有 \(q\mid p+m,\ q\equiv1\pmod m\)；在其余 75 点中，
只有 \(p=454969\) 由 \(5^3=125\) 于 \(m=31\) 救回。最终 74 个点没有任何
同缺口单素数幂共享因子，见 `type-II-shared-prime-power-selection-boundary`。
故这些点的共享因子必用至少两个不同素因子。进一步的最小支撑审计表明，固定至多
两素或至多三素也不足：84 点的最小支撑分布为 \(1:10,2:54,3:18,4:2\)，见
`type-II-shared-bounded-support-selection-boundary`。下一步必须处理一般多因子
除子积集，而不能猜测固定有限个素因子的模板。

存在一个完全无条件但过粗的正向充分条件：若一个已有 Type II 证书的缺口 \(m\) 中，
\(p+m\) 与 \(m\) 互素的素因子按重数至少有 \(\varphi(m)\) 个，前缀积碰撞即构造
\(D\equiv1\pmod m\)。不过这个阈值在上述 84 点、全部 \(m\le239\) 的完整扫描中
命中数为零，见 `type-II-shared-totient-threshold-lemma`。因此需要残数分布或跨缺口
信息，而不只是因子总数。

把阈值收缩到实际因子残数生成的子群阶仍不足：若单位因子重数达到该子群的阶，前缀积
同样强制共享除子；但这一强化条件在同一 84 点审计中仍命中为零，见
`type-II-shared-subgroup-threshold-lemma`。剩余任务因而是短零积的逆结构与跨缺口
共同避靶条件，而非再替换一个群规模阈值。

在 p-primary 生成子群上可以再收紧一次：若
\(H\simeq\bigoplus_i C_{\ell^{a_i}}\)，则精确 Davenport 阈值
\(D(H)=1+\sum_i(\ell^{a_i}-1)\) 已在
type-II-shared-p-group-davenport-threshold 中实现。10M 聚焦回放对 84 个
压力点产生 28 个新构造性命中，但仍留下 56 个未覆盖点；因此这是一条有限群结构
分支，不是共享选择器猜想的全称闭合。

对非 p-primary 但秩至多二的生成子群，循环或
\(H=C_{n_1}\oplus C_{n_2}\)、\(n_1\mid n_2\) 时可用
\(D(H)=n\) 或 \(D(H)=n_1+n_2-1\) 的精确阈值。10M、\(m\le239\) 的秩二 profile
覆盖 29/84 个压力点，其中 28 个是既有 \(C_2\oplus C_4\) 见证，新增
\(p=1497049,m=39,H=C_2\oplus C_{12}\) 的共享除子。仍有 55 个 profile miss，且
秩至少三、阈值以下短零积和 marked 到无标记递降未处理；详见
[共享 Type II 秩至多二 Davenport 阈值](type-II-shared-rank-two-davenport-threshold.md)。

最短零积长度的六因子强化已在更大范围失败：\(p=95741809\) 于 \(m=71\) 的最短
共享因子为 \(7364760=2^3\cdot3\cdot5\cdot13\cdot4721\)，有
\(\Omega(D)=7\)，见 `type-II-shared-six-factor-profile-boundary`。同一 100M
审计还出现 \(p=33011449\) 在 \(m\le239\) 内完全无共享证书；对后者逐项扩展至
\(m\le500000\) 仍为空，见 `type-II-shared-half-million-gap-escape-boundary`。
因此下一步必须允许零积长度和缺口均真正增长，或转回不要求共享标记的直接证书路线。

## 与已有方向的关系

这个猜想不同于 `type-II-ac-ray-saturation-conjecture`：后者固定 \(A,C\) 的盒，
而这里直接控制同一 \(x=(p+m)/4\) 的两个除子残数。它也比原猜想强，因为它要求
Type II 形式和额外共享因子；失败并不推出 Erdős--Straus 猜想失败。

要证明它，核心不是单独让 \(4x\) 有 \(1\) 残数因子，或让 \(x^2\) 达到
\(-x\) 残数，而是控制二者在同一缺口 \(m\) 上的耦合。更不能预先固定一个
\(m\)：`type-II-shared-residue-fixed-gap-boundary` 在真实核心素数 \(p=73\) 的
合法缺口 \(m=47\) 上同时给出两个条件的失败。有限阿贝尔群的除子积集、多移位碰撞
分解和增长扇筛法是目前可利用的三个接口；其中后两者必须承担跨缺口的主动选择。
