---
kind: claim
claim_id: type-I-g-anchor-r11-adaptive-divisor-terminal
title: R=11 固定尾的完整三残类因子盒与自适应 Type I 终端
statement: 设 p=24h+1 为核心素数、N=22h+1、K=3N=(11p+1)/4。固定第三分母 pK 的全部 Type I terminal 恰等价于存在 d divides N^2，且 d lies in {7,8,10} modulo 11：若 d is congruent to 8,10,7，分别取 e=d,3d,9d，再取 u=(K+e)/11、v=(K+K^2/e)/11。每个这样的终端同时给出严格 marked one-tail descent 4/N=1/u+1/v+1/K 到 N<p，并将完整标记切片 (a,b,K) 双射提升为 (a,b,pK)。特别地，若 r divides N 且 r=8 (mod 11)，写 s=N/r，则 u=r(3s+1)/11、v=3rs(3s+1)/11 为正整数，且 u<v<pK，并给出直接 Type I 短证书。对每个奇数 r=8 (mod 11)，令 h0=-22^(-1) (mod r)，则 gcd(24h0+1,24r)=1；Dirichlet 定理给出无穷多个素数 p=24(h0+rt)+1，且每个都由该构造终止。该结果是 terminal-first 的自适应除子扇，不依赖 c=3/c=9 complement seed 的 source receipt，也不覆盖三残类因子盒未命中的核心素数。
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

# \(R=11\) 的完整三残类因子盒与自适应终端

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

## 4. 完整标记单尾递降

对任意正整数 \(N,K,p\) 满足

\[
K=3N,
\qquad
4K=11p+1,
\tag{D1}
\]

定义两个带固定第三分母的有序标记解集

\[
\begin{aligned}
\mathcal W_N(K)
 &=\left\{(a,b,K)\in\mathbb N^3:
 \frac4N=\frac1a+\frac1b+\frac1K\right\},\\
\mathcal W_p(pK)
 &=\left\{(a,b,pK)\in\mathbb N^3:
 \frac4p=\frac1a+\frac1b+\frac1{pK}\right\}.
\end{aligned}
\tag{D2}
\]

**引理（\(R=11\) 的单尾 marked lift）。** 映射

\[
\boxed{
\mathcal L_{N\to p}:(a,b,K)\longmapsto(a,b,pK)}
\tag{D3}
\]

是 \(\mathcal W_N(K)\) 到 \(\mathcal W_p(pK)\) 的双射，逆映射只把第三分母
\(pK\) 还原为 \(K\)。并且对核心素数 \(p=24h+1\)，有

\[
N=\frac{11p+1}{12}=22h+1<p.
\tag{D4}
\]

**证明。** 对 \((a,b,K)\in\mathcal W_N(K)\)，由 \(N=K/3\) 得

\[
\frac1a+\frac1b=\frac4N-\frac1K=\frac{11}{K}.
\tag{D5}
\]

再用 \(11p+1=4K\)，便有

\[
\frac1a+\frac1b+\frac1{pK}
=\frac{11}{K}+\frac1{pK}
=\frac4p.
\tag{D6}
\]

所以 (D3) 有定义。反向从 \(\mathcal W_p(pK)\) 的定义同样得到 (D5)，故逆映射
有定义且两者互逆。最后 (D4) 由 \(h>0\) 立即成立。证毕。

因此，任意 (2) 的 box hit 不仅给出 (4) 的 terminal，也以 (3) 给出
\(\mathcal W_N(K)\ne\varnothing\)，并提供：

* 显式、全域于标记解集的 solution lift (D3)；
* 严格分母秩 \(N<p\)；
* 不依赖 raw source、F/G 标签或 fresh-root scope 的递降证书。

它不把 (D3) 外推为从全部 \(\operatorname{Sol}(4,N)\) 到全部
\(\operatorname{Sol}(4,p)\) 的映射；固定第三分母是这个 marked state 的必要字段。

## 5. 无穷 Dirichlet 射线

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

Dirichlet 定理于是保证 (21) 含无穷多个素数；每个这样的素数都满足 (10)，故有
(4) 的直接终端。这里并未声称任一给定核心素数必含这类因子。

## 6. 控制

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

## 7. 与 G-anchor 原始自环族的交集

此前的原始 physical-row 自环障碍覆盖

\[
p\equiv601\pmod {936}.
\tag{24}
\]

它并不自动表示原始 \(p\) 没有 terminal。事实上，取其中的子射线

\[
p=601+17784t,
\qquad
h=25+741t.
\tag{25}
\]

则

\[
22h+1=551+16302t=19(29+858t),
\tag{26}
\]

所以 (10) 对 \(r=19\) 恒成立。又

\[
\gcd(601,17784)=1,
\tag{27}
\]

Dirichlet 定理给出无穷多个素数参数点；每一个同时属于 (24) 且由 (4) 直接终止。
因此未标记 physical-row 自环确实阻止把 raw action 当作严格势，却不能被当作该
无穷子族的 terminal-free 证据。

## 8. 两个非剩余因子仍可完整未命中

不能把“\(N\) 含一个模 \(11\) 二次非剩余因子”当作 (2) 的充分条件。更精确地，
设 \(\ell,m\) 是满足

\[
\ell\equiv2\pmod {11},
\qquad
m\equiv6\pmod {11}
\tag{28}
\]

的不同素数，并令 \(N=\ell m\)。则 \(N\equiv1\pmod {11}\)，且

\[
\{d\bmod {11}:d\mid N^2\}
=\{2^a6^b\bmod {11}:0\le a,b\le2\}
=\{1,2,3,4,6\}.
\tag{29}
\]

其中 \(2\) 与 \(6\) 都是模 \(11\) 的二次非剩余，但 (29) 与
\(\{7,8,10\}\) 不相交。因此完整 \(R=11\) 固定尾 box 未命中。

若进一步

\[
p=\frac{12\ell m-1}{11}
\tag{30}
\]

为素数，则 \(\ell m\equiv1\pmod {22}\) 给出

\[
h=\frac{\ell m-1}{22},
\qquad
p=24h+1,
\tag{31}
\]

所以这是核心素数中的真实固定尾残余族，而不是仅在有限群内的形式反例。

最小控制是

\[
(\ell,m,N,h,p)=(13,17,221,10,241).
\tag{32}
\]

该 \(p\) 有其它直接 Type II terminal，故这不是 Erdős--Straus 反例；它严格排除的
只是“任意非剩余因子足以关闭 \(R=11\) 固定尾”的错误规则。

## 9. 边界

这是一张原始 \(p\) 的 terminal leaf：它不需要也不生成递归状态、全域 E4 lift 或
G-anchor raw source。它不会覆盖完整三残类因子盒 (9) 未命中的核心素数，因而不是
G/Type I 全局出口定理。

复现：

```bash
python3 reproductions/type_i_g_anchor_r11_adaptive_divisor_terminal.py --verify
```
