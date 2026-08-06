---
kind: claim
claim_id: type-I-high-anchor-full-excess-gate-design-template
title: 高锚 full-excess 余因子 gate 的商窗口与构造模板
statement: 设 p 为核心素数，H=(p,R,K;A) 是 canonical 高锚，A|K；其 deterministic high-R complete-excess bundle 给出 M=lcm(A,Q)=kp+r、0<r<p 与 K_M=MC，且令 g=gcd(A,C)、a=A/g。则余因子 gate a|r 等价于 a|k，也等价于令 t 为 M/a 模 p 的最小非负剩余时 at<p。特别地，对任意整数 q，若 1<=qA<p，则 C=qA 当且仅当 4qAM=1 (mod p)；此时 a=1，gate 自动通过，target support 为 qA。若 gate target 精确回到原图表，记 K=AB，则唯一诱导 A=ga、C=gc、1<=gc<p、r=au、B=uc、(a,c)=1、M=au (mod p) 且 0<au<p；反之这些分解、范围、余数条件及 C=gc 的 canonical congruence 给出同图表 return 的精确算术模板。p=3793 与 p=60913 分别落在 q=2,3 的自动子族，p=1201 落在 (g,a,u,c)=(34,29,20,28) 的 return 子族。该主张只刻画固定锚点的算术 gate，不构造普遍的 full-excess bundle，也不提供 parent provenance、F/G 纤维、terminal-first 或 E1--E5 全局递归闭包。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-cofactor-r-chart-support
  - type-I-high-anchor-cofactor-macro-e1-e4-admission
topics:
  - type-I
  - high-anchor
  - full-excess
  - cofactor-gate
  - congruence
  - divisor-template
  - return
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_high_anchor_full_excess_gate_template.py
    role: targeted exact replay of p=1201, p=3793, and p=60913
  - result: reproductions/type-i-high-anchor-full-excess-gate-template-results.json
    role: frozen arithmetic template witnesses
visibility: public
last_checked: '2026-08-06'
---

# 高锚 full-excess 余因子 gate 的商窗口与构造模板

## 1. 固定高锚的精确 gate

固定一个 canonical 高锚

\[
H=(p,R,K;A),\qquad p<R<4A,\qquad A\mid K,
\]

并令它的 deterministic complete-excess bundle 为

\[
M=\operatorname{lcm}(A,Q)=kp+r,\quad 0<r<p,
\qquad K_M=MC.
\tag{1}
\]

这里 \(p\nmid A\)，且 \(A\mid M\)。写

\[
g=(A,C),\qquad a=A/g.
\tag{2}
\]

标准 cofactor r-chart 的精确 gate 是 \(a\mid r\)。由 \(M=kp+r\) 和
\(a\mid M\)，再用 \((a,p)=1\)，立即得到

\[
\boxed{\quad a\mid r\quad\Longleftrightarrow\quad a\mid k.\quad}
\tag{3}
\]

这将原本看似取决于大余数的条件变成 carrier 商的整除条件。

再令 \(t\in\{0,\ldots,p-1\}\) 是 \(M/a\) 模 \(p\) 的最小非负剩余。则

\[
\boxed{\quad a\mid r\quad\Longleftrightarrow\quad at<p.\quad}
\tag{4}
\]

事实上，若 \(a\mid r\)，写 \(r=at\)，则
\(M/a=p(k/a)+t\)，而 \(at=r<p\)。反向时，
\(M/a=p\ell+t\) 给出 \(M=pa\ell+at\)，其除以 \(p\) 的余数就是 \(at\)。
所以 (4) 是一个宽度 \(p/a\) 的短剩余窗口，不是经验性筛选。

## 2. 自动通过的 \(C=qA\) 子族

令 \(q\ge1\) 且 \(qA<p\)。那么

\[
\boxed{\quad C=qA
\quad\Longleftrightarrow\quad
4qAM\equiv1\pmod p.\quad}
\tag{5}
\]

正向由 \(pR_M+1=4MC\) 直接得出。反向时

\[
R_*=\frac{4qAM-1}{p}
\]

是介于 \(1\) 与 \(4M-1\) 的 canonical residue，故其对应 cofactor 恰为 \(qA\)。
于是 \(g=A\)、\(a=1\)，gate 自动成立，且

\[
A_T=\operatorname{lcm}(A,C)=qA.
\tag{6}
\]

若 \(q>1\)，这是严格的 support 增长；是否可被外层秩支付仍是另一件事。

这给出一个可反向尝试的有限代数目标：先选择或认证 high anchor 与它的 full-excess
\(M\)，再寻找小 \(q\) 使 (5) 成立，而不是直接盲查 \(r\) 的整除性。

## 3. 同图表 return 的除子模板

再写 \(K=AB\)。若通过 gate 的 target 精确回到原 \((R,K)\)，令

\[
u=r/a,\qquad c=C/g.
\]

由于 \(K=rC\)，必且仅必有

\[
\boxed{
A=ga,\qquad C=gc,\qquad r=au,\qquad B=uc.
}
\tag{7}
\]

其中 \((a,c)=1\)、\(1\le gc<p\)、\(M\equiv au\pmod p\) 且 \(0<au<p\)。最后两条确保
\(r\) 确实是这个 carrier 的标准余数，而不是一个仅在形式上分解 \(K\) 的数。

同时 \(C=gc\) 的 canonical 条件是

\[
4gcM\equiv1\pmod p.
\tag{8}
\]

因此 return 并不是模糊的“可能回环”：给定 \((g,a,u,c)\) 后，(7)--(8) 连同
\(1\le gc<p\) 与 \(M\equiv au\pmod p\) 是精确的除子/同余规范。它仍需要
full-excess 定义实际产生给定的 \(M\)，不能倒置为任意
\((g,a,u,c)\) 的存在定理。

## 4. 三个固定控制例

| \(p\) | \(A\) | \(M\) | \(C\) | 机制 |
|---:|---:|---:|---:|---|
| 1201 | 986 | 906134 | 952 | return: \((g,a,u,c)=(34,29,20,28)\) |
| 3793 | 1811 | 12695110 | 3622 | automatic: \(C=2A\) |
| 60913 | 18647 | 1347394926 | 55941 | automatic: \(C=3A\) |

对 \(p=1201\)，\(k=754=29\cdot26\)，而

\[
\frac{M}{a}\bmod p=20,\qquad r=580=29\cdot20,
\]

正好实现 (3)--(4)。又 \(K/A=560=20\cdot28\)，从而给出 (7) 的完整 return
分解。另两例的 \(a=1\)，分别由 (5) 的 \(q=2\) 与 \(q=3\) 自动过 gate。

## 5. 证明边界与下一步

本卡没有把“gate 通过”升级为 selector 边。特别缺少或需单独检查的仍是：

- full-excess \(Q\) 是否从允许的 raw/source normal form 实际得到；
- parent 到高锚 \(H\) 的 charged-history receipt；
- H、transient overflow 与 target 的 typed F/G/hit 纤维和 \(\operatorname{Sol}(p)\) 恒等提升；
- terminal/alternate menu 的先行耗尽；
- 宏 \(H\Rightarrow T\) 的 E1--E5 及跨状态秩支付。

因此 (5) 提供的是最小的可构造 arithmetic gate 接口，而不是 Erdos--Straus 猜想的覆盖。

## 复现

```bash
python3 reproductions/type_i_high_anchor_full_excess_gate_template.py --verify
```
