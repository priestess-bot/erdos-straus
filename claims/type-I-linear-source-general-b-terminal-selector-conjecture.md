---
kind: claim
claim_id: type-I-linear-source-general-b-terminal-selector-conjecture
title: 线性上半区一般 B 混合终端选择猜想
statement: 对每个核心素数 p，要么存在普通 Type II p-1 双尾证书，要么存在正整数 a、奇数 s 和 R=3 mod4，使 p=a+s+asR；令 K=(pR+1)/4，则 K^2 有正因子 d<=K 满足 d=-K modR。后一条件规范恢复一般 B 的自然 Type I 正规形，而 E=sR+1 整除偶源 n=p-s，因此给出严格上半区线性终端桥。该猜想强于原混合终端选择引理，但弱于已经被 p=878089 反驳的 B=1 线性版本。
claim_status: open
proof_provenance: repository_derivation
review_status: independent_review
topics:
- type-I
- type-II
- linear-source
- shifted-source
- general-b
- upper-half-source
- terminal-bridge
- target-square-divisor
- mixed-selector
- proof-program
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

# 线性上半区一般 \(B\) 混合终端选择猜想

## 全称主张

对每个核心素数 \(p\equiv1\pmod {24}\)，猜想至少一个分支成立：

1. \(p\) 有普通 Type II \(p-1\) 双尾证书；
2. 存在正整数 \(a,s,R,d\) 满足

   \[
   s\equiv1\pmod2,\qquad R\ge3,\qquad R\equiv3\pmod4,
   \qquad p=a+s+asR, \tag{1}
   \]

   并且，令

   \[
   K=\frac{pR+1}{4}, \tag{2}
   \]

   有

   \[
   d\mid K^2,\qquad 1\le d\le K,
   \qquad d\equiv-K\pmod R. \tag{3}
   \]

式 (1) 是线性移位源条件，式 (3) 是允许一般 \(B\) 的目标平方除数条件。真正的
开放内容是：普通双尾失败时，能否同时选择这两层参数。

## 线性源为何自动给出严格偶终端

由 (1) 定义

\[
E=sR+1,\qquad n=p-s=aE. \tag{4}
\]

因为 \(s,R\) 都是奇数，\(E\) 和 \(n\) 都是偶数。又有

\[
pR+1=(aR+1)(sR+1),
\qquad 4K=(aR+1)E. \tag{5}
\]

因此

\[
E\mid n,\qquad E\mid4K,\qquad E\equiv1\pmod R,
\qquad n=\frac{4K-E}{R}. \tag{6}
\]

并且

\[
p=a+s+asR\ge1+4s,\qquad
s\le\frac{p-1}{4},\qquad
n=p-s\ge\frac{3p+1}{4}. \tag{7}
\]

线性源实际落在最上四分之一区间，而不只是上半区。又由
\(aR+1\ge4\) 和 (5) 得 \(E\le K\)。特别地，\(2\le n<p\)，且

\[
E=4K-nR\le4K-2R. \tag{8}
\]

故 \(E\) 已经满足原混合终端引理要求的偶因子、同余和大小条件；其源项为

\[
\frac{nK}{E}=aK. \tag{9}
\]

在[源平方正规分解](type-I-source-square-normal-factorization.md)的记号中，这一分支
精确对应 \(\beta=1\)。

## 固定 \(p\) 的完备有限枚举

置

\[
u=\min(a,s),\qquad v=\max(a,s).
\]

由 (1) 及 \(v\ge u\)，

\[
p=u+v+uvR\ge2u+3u^2,
\qquad
u\le
\left\lfloor\frac{\sqrt{1+3p}-1}{3}\right\rfloor. \tag{10}
\]

同时

\[
p-u=v(1+uR). \tag{11}
\]

所以只需对上述范围内的每个 \(u\) 分解 \(p-u\)，枚举
\(1+uR\mid p-u\)，再令 \(v=(p-u)/(1+uR)\)，就能恢复全部无序
\((u,v,R)\)。随后把每个奇坐标分别定向为 \(s\)，便得到全部线性源状态。
这给出一个严格有限的反证算法，但不把有限搜索本身升级成全称证明。

## 一般 \(B\) 目标平方除数的规范恢复

由 \(4K\equiv1\pmod R\)，式 (3) 的目标同余等价于

\[
4d\equiv-1\pmod R. \tag{12}
\]

令

\[
g=(d,K),\qquad B=\frac d g,\qquad
C=\frac{g^2}{d},\qquad H=\frac K g. \tag{13}
\]

逐素指数可得

\[
B,C,H\in\mathbb Z_{>0},\qquad BCH=K,\qquad
B^2C=d,\qquad (B,H)=1. \tag{14}
\]

式 (12) 与 \(4K\equiv1\pmod R\) 进一步给出

\[
H\equiv-B\pmod R. \tag{15}
\]

因此

\[
A=\frac{B+H}{R},\qquad
m=\frac{4B^2C+1}{R} \tag{16}
\]

是正整数。式 (12) 还给出 \((B,R)=1\)，故

\[
\gcd(A,B)=\gcd(AR,B)=\gcd(B+H,B)=1.
\]

另外 \(m\equiv3\pmod4\)，并且

\[
\frac dK=\frac BH. \tag{17}
\]

式 (3) 的 \(d\le K\) 因而给出 \(B\le H\)。相等情形结合 \((B,H)=1\) 会迫使
\(B=H=1\)，再由 (12) 和 \(4K\equiv1\pmod R\) 得到 \(R\mid2\)，与
\(R\ge3\) 矛盾。所以 \(H>B\)，并且

\[
R(p-m)=4BC(H-B)-2>0. \tag{18}
\]

于是 \(3\le m\le p-2\)，且

\[
p=4ABC-m. \tag{19}
\]

这规范恢复一张自然 Type I 正规形，并给出

\[
\frac4p
=\frac1{ABC}+\frac1{ACH}+\frac1{pK}, \tag{20}
\]

以及由 (9) 得到的线性偶源桥

\[
\frac4n
=\frac1{aK}+\frac1{ABC}+\frac1{ACH}. \tag{21}
\]

反过来，任意满足 \(E\mid n\) 的一般 \(B\) 线性源正规形令 \(d=B^2C\)，再在
必要时交换 \(B,H\)，都会落回 (1)--(3)。因此第二分支不是松散的充分条件，而是该
证书子类的精确坐标。

## \(d\le K\) 不损失一般性

若先找到任意正因子 \(d\mid K^2\) 满足 \(d\equiv-K\pmod R\)，则互补因子

\[
d'=\frac{K^2}{d} \tag{22}
\]

也满足 \(d'\equiv-K\pmod R\)：因为 \(K,d\) 模 \(R\) 均可逆，

\[
d'=K^2d^{-1}\equiv K^2(-K)^{-1}\equiv-K\pmod R.
\]

两者至少有一个不超过 \(K\)，而 \(d=K\) 会像上面
一样迫使 \(R\mid2\)，故实际可取严格的 \(d<K\)。在正规形坐标中，\(d\leftrightarrow
d'\) 正是交换 \(B,H\)，目标分解的前两个分母随之互换。

## 与现有两条路线的关系

本猜想一旦成立，就直接推出
[一般混合终端选择引理](type-I-target-divisor-even-terminal-selector.md)。具体地，令

\[
x=ABC=\frac{p+m}{4},\qquad e=B^2C.
\]

则 \(e\mid x^2\)、\(mR=4e+1\)，并且

\[
K=BCH=xR-e.
\]

再结合 (6)--(9)，正好得到该选择器的目标除子和偶终端因子。因此不再需要
额外的猜想性递降桥。它对 Type I 分支增加了 \(E\mid n\) 的线性限制，所以仍是原目标的
加强版。

它与[自适应上半区 \(B=1\) 猜想](type-I-adaptive-upper-b1-terminal-selector-conjecture.md)
把平方自由度放在相反两侧：

- 本猜想固定源侧 \(\beta=1\)，允许目标侧 \(B\ge1\)；
- 自适应 \(B=1\) 猜想固定目标侧 \(B=1\)，允许源侧 \(\beta\ge1\)。

两类证书在参数层面互不包含。它们的交集是“\(B=1\) 且 \(E\mid n\)”的线性版本，
该版本已经被
[\(p=878089\) 的全局反例](type-I-linear-shifted-source-counterexample-878089.md)否定；同一点
却有 \(B=7\) 的线性桥，说明允许一般 \(B\) 是实质放宽，而不是记号变化。

## 有限证据与证明边界

冻结的五亿普通双尾遗漏及独立的五亿到六亿区间共给出 1,964 个压力点。对应的
[一般 \(B\) 线性源闭合剖面](type-I-linear-source-general-b-completion-profile-600m.md)
在该有限集合上命中 1,964 点、遗漏为零。

这仍不是全称证明。下一阶段不应只继续扩大顺序上界，而应研究固定线性状态的目标谱

\[
\mathcal D_R^{(2)}(K)=\{d\bmod R:d\mid K^2\} \tag{23}
\]

为何必须在某个源可达 \(R\) 上包含 \(-K\)。经过
[中心化平方除子谱障碍二分](type-I-general-b-centered-square-spectrum.md)，这已成为固定状态上的
精确定理：将平方除子谱乘以 \(K^{-1}\) 后，目标变为 \(-1\)，失败有且只有：

1. \(-1\) 不在 \(K\) 的素因子残数生成子群中的子群/角色障碍；
2. \(-1\) 在该子群中，但不在有限指数盒
   \(-v_q(K)\le z_q\le v_q(K)\) 内的有限指数障碍。

所以全称证明不再需要重新分类单一源状态；它必须解释这些已精确定义的障碍为何不能对同一个
核心素数的全部线性源状态同时持续存在。单点 \(p=878089\) 已经同时出现两类失败并有一个
一般 \(B\) 逃逸命中，见[其完整中心化谱剖面](type-I-linear-general-b-obstruction-profile-878089.md)。
