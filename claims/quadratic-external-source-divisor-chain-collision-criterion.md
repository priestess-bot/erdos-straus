---
kind: claim
claim_id: quadratic-external-source-divisor-chain-collision-criterion
title: 平方因子外部源分母链的精确见证碰撞判据
statement: >-
  对核心素数 p，令 H=(p-1)/4，且 k|l|H、l=ks、s>1。令
  n_j=p-H/j，M_j=jn_j，q_j=4j-1，及
  E_j={e:e|M_j^2,e<=M_j,q_j|4e+1}。再令
  g=gcd(n_k,s-1) 与 L=lcm(q_k,q_l)。则
  E_k∩E_l={e:e|(kg)^2,e<=M_k,L|4e+1}。特别地，若
  4(kg)^2+1<L，则 E_k∩E_l 为空。该式精确描述完整零平移平方因子
  外部源在可比尺度间何时能够复用同一个因子见证；它不声称所有可比菜单都不相交。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - quadratic-factor-external-source-descent
  - adaptive-external-source-divisor-chain-witness-independence
topics:
  - type-I
  - external-source
  - descent
  - divisor-chain
  - gcd
  - collision
  - capacity-map
  - proof-program
sources:
  - claim: quadratic-factor-external-source-descent
    role: complete-fixed-scale-square-factor-menu
  - claim: adaptive-external-source-divisor-chain-witness-independence
    role: source-denominator-chain-gcd-template
  - reproduction: reproductions/quadratic_external_source_divisor_chain_collision_criterion.py
    role: exact-menu-intersection-controls
visibility: public
last_checked: '2026-08-12'
---

# 平方因子外部源分母链的精确见证碰撞判据

## 1. 完整菜单

固定核心素数 \(p\equiv1\pmod {24}\)，记

\[
H=\frac{p-1}{4}.
\]

对 \(j\mid H\)，令

\[
q_j=4j-1,\qquad n_j=p-\frac Hj,\qquad M_j=jn_j. \tag{1}
\]

固定尺度的完整零平移平方因子外部源菜单可写成

\[
\mathcal E_j
 =
\{e>0:e\mid M_j^2,\ e\le M_j,\ e\equiv-M_j\pmod {q_j}\}. \tag{2}
\]

因为

\[
4j\,n_j=q_jp+1,\qquad 4j\equiv1\pmod {q_j},
\]

有 \(n_j\equiv1\pmod {q_j}\)，从而 \(M_j\equiv j\pmod {q_j}\)。故

\[
e\equiv-M_j\pmod {q_j}
\quad\Longleftrightarrow\quad
\boxed{q_j\mid4e+1}. \tag{3}
\]

这把菜单的标记条件从随源变化的余类压缩成单个线性整除式。

## 2. 可比尺度的公共因子

设 \(k\mid l\mid H\)，写 \(l=ks\)，其中 \(s>1\)，并令

\[
g=\gcd(n_k,s-1),\qquad L=\operatorname{lcm}(q_k,q_l). \tag{4}
\]

先有精确公式

\[
\boxed{\gcd(M_k,M_l)=kg}. \tag{5}
\]

事实上，写 \(H=kt\)，再写 \(t=sa\)。则

\[
n_k=(4k-1)t+1,\qquad
n_l=(4ks-1)a+1,
\]

以及

\[
n_l-n_k=a(s-1). \tag{6}
\]

因 \(n_k\equiv1\pmod {sa}\)，故 \(\gcd(n_k,as)=1\)，于是

\[
\gcd(n_k,n_l)=\gcd(n_k,s-1)=g. \tag{7}
\]

又 \(\gcd(n_k,s)=1\)，所以

\[
\gcd(M_k,M_l)
=\gcd(kn_k,ksn_l)
=k\gcd(n_k,sn_l)
=kg.
\]

## 3. 精确碰撞公式

由 (3)、(5) 得

\[
\boxed{
\mathcal E_k\cap\mathcal E_l
=
\left\{
e>0:
\ e\mid(kg)^2,\quad
e\le M_k,\quad
L\mid4e+1
\right\}.}
\tag{8}
\]

左推右：公共 \(e\) 同时整除 \(M_k^2,M_l^2\)，故整除
\(\gcd(M_k,M_l)^2=(kg)^2\)；又分别由 (3) 被 \(q_k,q_l\) 整除
\(4e+1\)，故被 \(L\) 整除。

右推左：由 \(e\mid(kg)^2=\gcd(M_k,M_l)^2\)，\(e\) 同时整除两平方。
条件 \(L\mid4e+1\) 和 (3) 给出两个菜单的余类条件。最后

\[
M_l-M_k=(l-k)p>0, \tag{9}
\]

所以 \(e\le M_k\) 自动也给出 \(e\le M_l\)。这证明 (8)。

因此，完整平方因子机制的“同一 \(e\) 是否可在两尺度复用”不是模糊的相关性，
而是一个有限、精确的除子问题；候选数至多为
\(\tau((kg)^2)\)。

## 4. 一个无条件去重门

若

\[
4(kg)^2+1<L, \tag{10}
\]

则 (8) 右侧为空：其中的正 \(e\) 会满足

\[
0<4e+1\le4(kg)^2+1<L,
\]

不可能被正整数 \(L\) 整除。故

\[
\boxed{
4(kg)^2+1<
\operatorname{lcm}(4k-1,4ks-1)
\quad\Longrightarrow\quad
\mathcal E_k\cap\mathcal E_{ks}=\varnothing.}
\tag{11}
\]

这是真正可放入 source-witness ledger 的充分去重条件。它比只对
\(n_k\) 的线性见证去重更宽，因为 (8) 包含 \(e\mid M_k^2\) 的全部平方因子菜单。

## 5. 必要的边界

以

\[
p=97,\quad H=24,\quad k=2,\quad l=12,\quad s=6
\]

为例，

\[
n_2=85,\qquad g=\gcd(85,5)=5,\qquad
L=\operatorname{lcm}(7,47)=329,
\]

而

\[
4(kg)^2+1=401>329. \tag{12}
\]

故简单范围门在这里不能证明不交。精确式 (8) 仍只需检查
\(e\mid100\) 且 \(329\mid4e+1\)，其候选集合为空，因而菜单确实不交。

这说明不能把范围门失败误报为实际碰撞，也不能把若干有限样本的无碰撞外推成
\(\mathcal E_k\cap\mathcal E_l=\varnothing\) 的全称断言。

## 6. 对全局出口的作用与限度

每个 \(\mathcal E_j\) 中的元素已由完整平方因子外部源定理给出严格递降和显式
Type I 证书。(8) 现在精确指出：沿可比尺度链，唯一可能被重复计数的完全因子
见证落在一个由 \(kg\) 与 \(L\) 控制的短候选菜单；满足 (11) 的边直接无重。

它尚未说明某个菜单必非空，也没有把“全部菜单为空”推出 Type II terminal。
因此它是 global exit 的容量接口，而不是该出口定理本身。

## 聚焦验证

~~~bash
PYTHONPATH=reproductions python3 \
  reproductions/quadratic_external_source_divisor_chain_collision_criterion.py \
  --verify
~~~
