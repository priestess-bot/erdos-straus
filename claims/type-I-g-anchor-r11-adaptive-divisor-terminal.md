---
kind: claim
claim_id: type-I-g-anchor-r11-adaptive-divisor-terminal
title: R=11 固定尾的自适应 8 mod 11 因子 Type I 终端
statement: 设 p=24h+1 为核心素数、N=22h+1、K=3N=(11p+1)/4。固定第三分母 pK 的全部 Type I terminal 恰等价于存在 d divides N^2，且 d lies in {7,8,10} modulo 11：若 d is congruent to 8,10,7，分别取 e=d,3d,9d，再取 u=(K+e)/11、v=(K+K^2/e)/11。特别地，若 r divides N 且 r=8 (mod 11)，写 s=N/r，则 u=r(3s+1)/11、v=3rs(3s+1)/11 为正整数，且 u<v<pK，并给出直接 Type I 短证书。对每个奇数 r=8 (mod 11)，令 h0=-22^(-1) (mod r)，则 gcd(24h0+1,24r)=1；Dirichlet 定理给出无穷多个素数 p=24(h0+rt)+1，且每个都由该构造终止。该结果是 terminal-first 的自适应除子扇，不依赖 c=3/c=9 complement seed 的 source receipt，也不覆盖三残类因子盒未命中的核心素数。
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

## 1. 完整三残类因子盒

令

\[
p=24h+1,
\qquad
N=22h+1,
\qquad
K=3N=\frac{11p+1}{4}.
\tag{1}
\]

**定理（\(R=11\) 固定尾的完整 \(N\)-box）。** 固定第三分母为 \(pK\) 的
Type I terminal 存在，当且仅当

\[
\boxed{
\exists d\mid N^2,
\qquad
d\pmod {11}\in\{7,8,10\}.}
\tag{2}
\]

更精确地，对一个满足 (2) 的 \(d\)，令

\[
e=
\begin{cases}
d,&d\equiv8\pmod {11},\\
3d,&d\equiv10\pmod {11},\\
9d,&d\equiv7\pmod {11},
\end{cases}
\qquad
u=\frac{K+e}{11},
\qquad
v=\frac{K+K^2/e}{11}.
\tag{3}
\]

则 \(u,v\) 为正整数，并有

\[
\frac4p=\frac1u+\frac1v+\frac1{pK}.
\tag{4}
\]

**证明。** 既有 \(R=11\) 固定尾判据是

\[
\exists e\mid K^2,
\qquad
e\equiv-K\equiv8\pmod {11}.
\tag{5}
\]

因为 \(K^2=9N^2\)，每个 \(e\mid K^2\) 都可写成

\[
e=3^j d,
\qquad
0\le j\le2,
\qquad d\mid N^2.
\tag{6}
\]

这里即使 \(3\mid N\)，也可把最多两个 \(3\) 留给 \(3^j\)，其余的 \(3\)-幂仍在
\(N^2\) 内。反过来，(6) 的每一个数都整除 \(K^2\)。

由 \(3^{-1}\equiv4\)、\(3^{-2}\equiv5\pmod {11}\)，(5) 等价于

\[
d\equiv8\cdot3^{-j}
\equiv
\begin{cases}
8,&j=0,\\
10,&j=1,\\
7,&j=2
\end{cases}
\pmod {11}.
\tag{7}
\]

这恰为 (2)--(3)。标准因式分解

\[
(11u-K)(11v-K)=K^2
\tag{8}
\]

给出 (4)。证毕。

因此三残类盒未命中

\[
\{d\bmod {11}:d\mid N^2\}\cap\{7,8,10\}=\varnothing
\tag{9}
\]

是这个固定尾路线上严格、有限且可复核的剩余条件；它不是 Erdős--Straus 反例。

## 2. \(8\pmod {11}\) 因子子扇

继续假设存在正因子

\[
r\mid N,
\qquad r\equiv8\pmod {11}.
\tag{10}
\]

写

\[
s=\frac{N}{r},
\qquad
K=3N=3rs.
\tag{11}
\]

则 (3) 在 \(d=e=r\) 时成为

\[
\boxed{
u=\frac{r(3s+1)}{11},
\qquad
v=\frac{3rs(3s+1)}{11}.}
\tag{12}
\]

这是一个特别易于按实际因子触发的 terminal 子扇。

## 3. 子扇的直接证明

由 \(N\equiv1\pmod {11}\) 和 (10)，

\[
rs\equiv1\pmod {11}.
\tag{13}
\]

而 \(8^{-1}\equiv7\pmod {11}\)，故

\[
s\equiv7\pmod {11},
\qquad
3s+1\equiv0\pmod {11}.
\tag{14}
\]

这证明 (12) 的整性。又 \(s\ge7\)，从而 \(u,v>0\) 且

\[
v=3su>u.
\tag{15}
\]

由 (12) 直接计算

\[
\frac1u+\frac1v
=\frac{11}{r(3s+1)}+\frac{11}{3rs(3s+1)}
=\frac{11}{3rs}
=\frac{11}{K}.
\tag{16}
\]

另一方面，\(11p+1=4K\) 给出

\[
\frac4p=\frac{11}{K}+\frac1{pK}.
\tag{17}
\]

合并 (16)--(17) 即得 (4)。此外，\(s\le N\) 蕴含

\[
3s+1\le66h+4<11(24h+1)=11p,
\tag{18}
\]

故 \(v<pK\)。三个分母因而严格递增。

## 4. 无穷 Dirichlet 射线
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
\tag{19}
\]

它自动与 \(22\) 互素。取唯一的

\[
0<h_0<r,
\qquad
22h_0+1\equiv0\pmod r.
\tag{20}
\]

对所有 \(t\ge0\)，令

\[
h=h_0+rt,
\qquad
p=24h+1=(24h_0+1)+24rt.
\tag{21}
\]

显然 \(r\mid22h+1\)。而若某奇素数同时整除 \(r\) 和 \(24h_0+1\)，它也整除

\[
24(22h_0+1)-22(24h_0+1)=2,
\tag{22}
\]

矛盾。因此

\[
\gcd(24h_0+1,24r)=1.
\tag{23}
\]

Dirichlet 定理于是保证 (14) 含无穷多个素数；每个这样的素数都满足 (1)，故有
(4) 的直接终端。这里并未声称任一给定核心素数必含这类因子。

## 5. 控制

* \(p=313\)、\(h=13\)：\(N=41\cdot7\)。完整 box 可取 \(d=7\)（对应
  \(e=63\)）或 \(d=41\)（对应 \(e=41\)）；后者即 \(r=41\) 子扇，给出
  \((u,v,pK)=(82,1722,269493)\)。
* \(p=601\)、\(h=25\)：\(22h+1=19\cdot29\)。取 \(r=19\)，得到
  \((u,v,pK)=(152,13224,993453)\)，恢复原 \(e=19\) 控制。
* \(p=1993\)、\(h=83\)：\(22h+1=63\cdot29\)。复合因子 \(r=63\) 同样给出
  \((u,v,pK)=(504,43848,10923633)\)。
* \(p=2017\)、\(h=84\)：\(N=43^2\)。取 \(d=43\equiv10\pmod {11}\)、
  \(e=3d=129\)，得到 \((u,v,pK)=(516,22188,11188299)\)，展示完整 box 的
  第二个残类并非 \(r\equiv8\) 子扇。

## 6. 与 G-anchor 原始自环族的交集

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

## 7. 边界

这是一张原始 \(p\) 的 terminal leaf：它不需要也不生成递归状态、全域 E4 lift 或
G-anchor raw source。它不会覆盖 \(22h+1\) 的所有因子均不落在 \(8\pmod {11}\)
的核心素数，因而不是 G/Type I 全局出口定理。

复现：

```bash
python3 reproductions/type_i_g_anchor_r11_adaptive_divisor_terminal.py --verify
```
