---
kind: claim
claim_id: type-I-g-anchor-r11-adaptive-divisor-terminal
title: R=11 固定尾的自适应 8 mod 11 因子 Type I 终端
statement: 设 p=24h+1 为核心素数。若 r divides 22h+1 且 r=8 (mod 11)，写 s=(22h+1)/r、K=3rs=(11p+1)/4。则 u=r(3s+1)/11、v=3rs(3s+1)/11 为正整数，且 u<v<pK，并给出直接 Type I 短证书 4/p=1/u+1/v+1/(pK)。对每个奇数 r=8 (mod 11)，令 h0=-22^(-1) (mod r)，则 gcd(24h0+1,24r)=1；Dirichlet 定理给出无穷多个素数 p=24(h0+rt)+1，且每个都由该构造终止。该结果是 terminal-first 的自适应除子扇，不依赖 c=3/c=9 complement seed 的 source receipt，也不覆盖没有这种因子的核心素数。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-complement-seed-n-minus-two-terminal-sieves
  - short-certificate-equivalence
topics:
  - type-I
  - terminal-first
  - R11
  - adaptive-divisor
  - Dirichlet-ray
  - G-anchor
  - short-certificate
  - proof-boundary
sources:
  - claim: type-I-g-anchor-complement-seed-n-minus-two-terminal-sieves
    role: R11-fixed-tail-factorization
  - reproduction: reproductions/type_i_g_anchor_r11_adaptive_divisor_terminal.py
    role: symbolic-terminal-and-Dirichlet-ray-controls
visibility: public
last_checked: '2026-08-12'
---

# \(R=11\) 的自适应 \(8\pmod {11}\) 因子终端

## 1. 定理

令

\[
p=24h+1
\]

为核心素数，并假设存在正因子

\[
r\mid22h+1,
\qquad r\equiv8\pmod {11}.
\tag{1}
\]

写

\[
s=\frac{22h+1}{r},
\qquad
K=3(22h+1)=3rs=\frac{11p+1}{4}.
\tag{2}
\]

则

\[
\boxed{
u=\frac{r(3s+1)}{11},
\qquad
v=\frac{3rs(3s+1)}{11}
}
\tag{3}
\]

是正整数，并且

\[
\boxed{
\frac4p
=\frac1u
+\frac1v
+\frac1{pK}.}
\tag{4}
\]

所以 (1) 是一个直接、可验证的 Type I terminal 条件。它在任何 raw root、
source-switch 或 \(R=11\) RESET 前执行。

## 2. 证明

由 \(22h+1\equiv1\pmod {11}\) 和 (1)，

\[
rs\equiv1\pmod {11}.
\tag{5}
\]

而 \(8^{-1}\equiv7\pmod {11}\)，故

\[
s\equiv7\pmod {11},
\qquad
3s+1\equiv0\pmod {11}.
\tag{6}
\]

这证明 (3) 的整性。又 \(s\ge7\)，从而 \(u,v>0\) 且

\[
v=3su>u.
\tag{7}
\]

由 (3) 直接计算

\[
\frac1u+\frac1v
=\frac{11}{r(3s+1)}+\frac{11}{3rs(3s+1)}
=\frac{11}{3rs}
=\frac{11}{K}.
\tag{8}
\]

另一方面，\(11p+1=4K\) 给出

\[
\frac4p=\frac{11}{K}+\frac1{pK}.
\tag{9}
\]

合并 (8)--(9) 即得 (4)。此外，\(s\le22h+1\) 蕴含

\[
3s+1\le66h+4<11(24h+1)=11p,
\tag{10}
\]

故 \(v<pK\)。三个分母因而严格递增。

这正是现有 \(R=11\) 固定第三分母判据中的 divisor

\[
e=r\mid K\mid K^2,
\qquad
e\equiv r\equiv-K\pmod {11},
\tag{11}
\]

但 (1)--(4) 把它从固定 \(e=19\) 射线推广为按 \(22h+1\) 的实际因子选择的
终端扇。

## 3. 无穷 Dirichlet 射线

反过来，固定任意奇数

\[
r\equiv8\pmod {11}.
\tag{12}
\]

它自动与 \(22\) 互素。取唯一的

\[
0<h_0<r,
\qquad
22h_0+1\equiv0\pmod r.
\tag{13}
\]

对所有 \(t\ge0\)，令

\[
h=h_0+rt,
\qquad
p=24h+1=(24h_0+1)+24rt.
\tag{14}
\]

显然 \(r\mid22h+1\)。而若某奇素数同时整除 \(r\) 和 \(24h_0+1\)，它也整除

\[
24(22h_0+1)-22(24h_0+1)=2,
\tag{15}
\]

矛盾。因此

\[
\gcd(24h_0+1,24r)=1.
\tag{16}
\]

Dirichlet 定理于是保证 (14) 含无穷多个素数；每个这样的素数都满足 (1)，故有
(4) 的直接终端。这里并未声称任一给定核心素数必含这类因子。

## 4. 控制

* \(p=313\)、\(h=13\)：\(22h+1=41\cdot7\)。取 \(r=41\)，得到
  \((u,v,pK)=(82,1722,269493)\)。
* \(p=601\)、\(h=25\)：\(22h+1=19\cdot29\)。取 \(r=19\)，得到
  \((u,v,pK)=(152,13224,993453)\)，恢复原 \(e=19\) 控制。
* \(p=1993\)、\(h=83\)：\(22h+1=63\cdot29\)。复合因子 \(r=63\) 同样给出
  \((u,v,pK)=(504,43848,10923633)\)。

## 5. 与 G-anchor 原始自环族的交集

此前的原始 physical-row 自环障碍覆盖

\[
p\equiv601\pmod {936}.
\tag{17}
\]

它并不自动表示原始 \(p\) 没有 terminal。事实上，取其中的子射线

\[
p=601+17784t,
\qquad
h=25+741t.
\tag{18}
\]

则

\[
22h+1=551+16302t=19(29+858t),
\tag{19}
\]

所以 (1) 对 \(r=19\) 恒成立。又

\[
\gcd(601,17784)=1,
\tag{20}
\]

Dirichlet 定理给出无穷多个素数参数点；每一个同时属于 (17) 且由 (4) 直接终止。
因此未标记 physical-row 自环确实阻止把 raw action 当作严格势，却不能被当作该
无穷子族的 terminal-free 证据。

## 6. 边界

这是一张原始 \(p\) 的 terminal leaf：它不需要也不生成递归状态、全域 E4 lift 或
G-anchor raw source。它不会覆盖 \(22h+1\) 的所有因子均不落在 \(8\pmod {11}\)
的核心素数，因而不是 G/Type I 全局出口定理。

复现：

```bash
python3 reproductions/type_i_g_anchor_r11_adaptive_divisor_terminal.py --verify
```
