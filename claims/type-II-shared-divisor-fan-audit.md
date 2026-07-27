---
kind: claim
claim_id: type-II-shared-divisor-fan-audit
title: 无界首尺度、缺口至多 239 的共享因子 Type II 扇覆盖一千万
statement: 精确审计表明，对全部 82887 个 p<=10^7、p=1 mod24 的核心素数，存在合法 Type II 缺口 m<=239 及 p+m 的因子 D=1 mod m；令 k=(D-1)/m 后，得到一张带共享因子标记的 Type II 证书及其严格源表示。该有限扇在范围内零遗漏。最大最小缺口为 239，保持者 p=7636561；最大首尺度为 664185，保持者 p=9962761，发生在 m=15。有限全覆盖不证明固定缺口扇对所有素数充分，也不构成无标记递归下降。
claim_status: computationally_reproduced
topics:
- type-II
- descent
- factor-selection
- computation
- shared-divisor
- proof-program
sources:
- paper: bradford2024
  locator: Section 2, Type II divisor certificates
  role: certificate-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-24'
---

# 无界首尺度、缺口至多 \(239\) 的共享因子 Type II 扇

## 审计对象

对每个 \(p\equiv1\pmod {24}\)，逐个检查

\[
3\le m\le239,\qquad m\equiv3\pmod4.
\]

对每个 \(m\)，完整分解 \(p+m\)，并检查每个

\[
D\mid p+m,\qquad D\equiv1\pmod m,\qquad D>1.
\]

令 \(k=(D-1)/m\)。若相同 \(m\) 上 Type II 除子条件成立，则
type-II-scaled-first-tail-deflation 给出

\[
(kx,Y,Z)\longmapsto(x,pY,pZ)
\]

及严格较小的带标记源分母。这一程序没有对 \(k\) 施加上界。

## 精确有限结果

    python3 reproductions/type_ii_shared_divisor_full_audit.py \
      --limit 10000000 --gap-cap 239 \
      --output reproductions/type-ii-shared-divisor-10m-gap239-results.json

对全部 \(82{,}887\) 个核心素数，输出为

\[
\#\{\text{命中}\}=82{,}887,\qquad
\#\{\text{遗漏}\}=0.
\]

最小成功缺口的最大值是

\[
p=7{,}636{,}561,\qquad m=239.
\]

首尺度没有类似的小界：范围内的最大值为

\[
p=9{,}962{,}761,\qquad m=15,\qquad k=664{,}185.
\]

后一个例子来自 \(D=p+m\) 的大因子切片；此时 \(m\mid p-1\)，源分母恰为
\(k=1+(p-1)/m\)。它说明缺口小不代表递降尺度小。

## 含义与边界

这把当前最强的有限证据推进到“存在带共享因子条件的 Type II 短证书”。对应的源表示
是带标记提升，见 `type-II-scaled-tail-marked-lift-equivalence`；因此它不能替代
独立的无标记递降。尺度记录者仍证明任何证书选择证明若依赖 \(k\) 的固定常数上界，
必然错过已知有限样本。

结果仍不蕴含全称猜想。固定 \(m\le239\) 是一次有限诊断，不是已证的全体选择器；
后续理论问题仍是：如何对任意核心素数强制某个共享因子
\(D\equiv1\pmod m\) 与同一缺口的 Type II 除子残数同时出现。
