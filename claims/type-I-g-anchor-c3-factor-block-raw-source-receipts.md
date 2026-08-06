---
kind: claim
claim_id: type-I-g-anchor-c3-factor-block-raw-source-receipts
title: c=3 双中间 skeleton 的复合因子块 raw word
statement: 在 c=3 complement target chart 的双中间 skeleton 中，alpha、beta、gamma 不必是素数。对一个 m=1 块 U=eL，只要终点 e 为 L 的每个素因子保留至少 v_q(K) 的 q-进容量，便可按素因子逐个实行实际 raw 边，将 U 剥到 e。应用于 R-1=b alpha、R-b=a beta、R-a=8 gamma 后，得到从 target universal p-source 到 complement seed 的复合因子块 raw word，且原有 endpoint phase 不变。文中给出 c=3 四个允许 h (mod 6) 类上的无穷 Dirichlet ray，并给出 (a,b)=(7,2) 的更精确容量分析。所有结果只建立 target-source raw provenance；词长通常无界，且不构成 short certificate、verified_edge 或 Erdos--Straus 全称证明。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-c3-two-intermediate-target-source-template
  - type-I-g-anchor-marked-raw-peeling-calculus
  - type-I-universal-p-source-capacity-anchor-orbit
  - type-I-g-anchor-even-tail-complement-source-switch
  - denominator-escape-state-contract
topics:
  - type-I
  - G-anchor
  - c3
  - factor-peeling
  - raw-path
  - target-source
  - capacity
  - Dirichlet-ray
  - proof-boundary
sources:
  - claim: type-I-g-anchor-c3-two-intermediate-target-source-template
    role: target-chart-skeleton-and-phase
  - claim: type-I-g-anchor-marked-raw-peeling-calculus
    role: raw-transition-semantics
  - claim: type-I-universal-p-source-capacity-anchor-orbit
    role: declared-target-universal-p-source
  - concept: denominator-escape-state-contract
    role: E1-E5-boundary
visibility: public
last_checked: '2026-08-06'
---

# \(c=3\) 双中间 skeleton 的复合因子块 raw word

## 1. 固定 chart 与 skeleton

令

\[
p=24h+1\ \text{为素数},
\qquad
h\not\equiv2\pmod3,
\qquad
h\not\equiv12\pmod{13},
\tag{1}
\]

并写

\[
R=104h-9,
\qquad
M=26h+1,
\qquad
x=p-3,
\qquad
K=Mx.
\tag{2}
\]

于是

\[
pR+1=4K,
\qquad
R=4M-13,
\qquad
13x=3R+1,
\qquad
v_2(K)=1.
\tag{3}
\]

取正整数 \(a,b\) 满足

\[
(a,b)=1,
\qquad
a\equiv7\pmod8,
\qquad
R-1=b\alpha,
\qquad
R-b=a\beta,
\qquad
R-a=8\gamma.
\tag{4}
\]

在本卡中，\(\alpha,\beta,\gamma\) 只要求为正整数。记
\(\operatorname{Fac}(L)\) 为 \(L\) 的任意素因子序列，按重数计；
\(\operatorname{Fac}(1)\) 是空词。一个以此记号标出的双箭头始终表示一串
单素数 raw 边，不是一条标签为合数的伪边。

## 2. \(m=1\) 因子块去皮引理

**引理（端点保留容量）。** 设

\[
U=eL,
\qquad
(U,R)=1,
\qquad
L=\prod_q q^{\ell_q}.
\tag{5}
\]

从有序 primitive node \((U,R-U,1)\) 出发，按任意顺序逐一选取 \(L\) 的素因子，
可完成全部 \(\operatorname{Fac}(L)\) raw word 并到达 \((e,R-e,1)\)，当且仅当

\[
v_q(e)\ge v_q(K)
\qquad
\text{对每个 }q\mid L.
\tag{6}
\]

每一步都没有 gcd reduction。

**证明。** 设已除掉的因子积为 \(d\mid L\)，当前 node 为

\[
\left(\frac{eL}{d},R-\frac{eL}{d},1\right).
\tag{7}
\]

若接下来选 \(q\mid L/d\)，则 \((eL/d,R)=1\)，故 \(q\nmid R\)，并且
\(q\) 与层数及另一坐标互素。其 shift 为 \(q-1\)，raw 规则恰给出

\[
\left(\frac{eL}{d},R-\frac{eL}{d},1\right)
\xrightarrow{q}
\left(\frac{eL}{dq},R-\frac{eL}{dq},1\right).
\tag{8}
\]

输出两坐标的 gcd 是 \(1\)，因为它等于 \((eL/(dq),R)\)。最后一次剥去给定
\(q\) 前，所选坐标的 \(q\)-进高度为 \(v_q(e)+1\)。严格容量
\(v_q(\text{selected})>v_q(K)\) 因而等价于 (6)。证毕。

特别地，\((L,K)=1\) 是 (6) 的一个干净充分条件，但不是必要条件；端点 \(e\)
可以吸收 \(K\) 中出现的素因子。

## 3. 双中间节点的因子块 word

在 (4) 下，\((b,R)=1\)，且

\[
(a,R)=(a,b)=1.
\tag{9}
\]

因此可把引理分别应用到三个块，其端点为 \(b,a,4\)。精确容量假设是

\[
\begin{aligned}
v_q(b)&\ge v_q(K) &&(q\mid\alpha),\\
v_q(a)&\ge v_q(K) &&(q\mid\beta),\\
v_q(4)&\ge v_q(K) &&(q\mid\gamma).
\end{aligned}
\tag{10}
\]

若 \(\gamma\) 为奇数，最后一行就是 \((\gamma,K)=1\)。在 (1) 的
\(13\)-tail 容量条件和 (10) 下，target universal source 有实际 raw word

\[
\begin{aligned}
\mathsf S_T
&\xrightarrow{p}N_R(1)
\xRightarrow{\operatorname{Fac}(\alpha)}N_R(b)
\xRightarrow{\operatorname{Fac}(\beta)}N_R(a)
\xrightarrow{2}N_R(4\gamma)\\
&\xRightarrow{\operatorname{Fac}(\gamma)}N_R(4)
\xrightarrow{13}N_R(4x)
\xrightarrow{2}N_R(2x)
\xrightarrow{2}N_R(x).
\end{aligned}
\tag{11}
\]

块内的素因子可任意重排；块之间必须保留 (11) 的顺序和被选坐标方向。
原 skeleton 的相位计算只依赖标签积，故不受分解影响：

\[
P=2\alpha\beta\gamma,
\qquad
W=13P,
\qquad
4P\equiv-1,
\qquad
W\equiv-M,
\qquad
4W\equiv-13\pmod R.
\tag{12}
\]

这证明的是一个有声明 universal \(p\)-source 的实际 raw receipt。它不是将
\(\operatorname{Fac}(L)\) 压缩成单条 macro edge 的许可。

## 4. \((a,b)=(7,2)\) 的精确容量 ray

此时基础整除和奇偶条件给出

\[
h=3+14t,
\tag{13}
\]

且

\[
\begin{aligned}
p&=336t+73, & R&=1456t+303,\\
M&=364t+79, & x&=336t+70,\\
\alpha&=728t+151, & \beta&=208t+43, & \gamma&=182t+37.
\end{aligned}
\tag{14}
\]

\(c=3\) 分支排除 \(t\equiv1\pmod3\)。对 \(\alpha\) 块，(10) 恒成立；
\(\beta\) 块失败恰在

\[
t\equiv2\pmod3
\qquad\text{或}\qquad
t\equiv4\pmod5,
\tag{15}
\]

而 \(\gamma\) 块失败恰在

\[
t\equiv4\pmod5
\qquad\text{或}\qquad
t\equiv3\pmod{11}.
\tag{16}
\]

表面上的 \(t\equiv4\pmod7\) 不是障碍：此时 \(7\mid\beta\)、
\(v_7(K)=1\)，但 \(v_7(a)=1\)，所以 \(\beta\) 块最后剥去 \(7\) 前的高度为
\(2>1\)，正好满足 (10)。最后，\(13\)-tail 失败恰在

\[
t\equiv9\pmod{13}.
\tag{17}
\]

因此所有实际 factor-block word 的一个无筛 Dirichlet 子 ray 是

\[
t=2145s,
\qquad
h=3+30030s,
\qquad
p=73+720720s.
\tag{18}
\]

因为 \((73,720720)=1\)，Dirichlet 定理给出无穷多个使 \(p\) 为素数的
\(s\)。每一个这样的 \(p\) 都有 (11) 的实际 raw receipt。该 ray 上的 raw word
长度通常随

\[
\Omega(\alpha)+\Omega(\beta)+\Omega(\gamma)+4
\tag{19}
\]

增长，并不有界。一个非平凡控制是 \(s=13\)：

\[
p=9369433,
\qquad
\beta=7\cdot67\cdot83\cdot149,
\qquad
v_7(K)=1,
\tag{20}
\]

其中恰展示了端点保留容量允许 \(\beta\) 与 \(K\) 共享素因子 \(7\)。

## 5. 四个允许余类上的无穷充分 ray

若采用较强但简洁的充分条件 \((\alpha\beta\gamma,K)=1\)，下表每一行都给出
无穷多个实际 factor-block raw receipt。每行中只要 \(p(t)\) 为素数，(11) 即成立。

\[
\begin{array}{c|c|c|c}
h\bmod6&(a,b)&h(t)&p(t)\\ \hline
3&(7,2)&3+210210t&73+5045040t\\
1&(7,46)&43+5664348690t&1033+135944368560t\\
0&(79,202)&138+222302842640970t&3313+5335268223383280t\\
4&(15,2)&1114+941850t&26737+22604400t
\end{array}
\tag{21}
\]

四个 \(p(t)\) 的初项与步长均互素，故 Dirichlet 定理分别给出无穷多素数值。
各 ray 保持 \(h\not\equiv12\pmod{13}\)，并把每个潜在公共奇素数排除在
\(\alpha\beta\gamma\) 之外。因此它们无条件证明：\(c=3\) 的四个允许
\(h\bmod6\) 类都含无穷多个 target-source raw receipt。

## 6. 合同边界与后续方向

本卡只提供 target chart 内的实际 raw provenance。它没有给出：

1. 一个能把该 receipt 登记为 selector root 的全局 E1--E3 scope 规则；
2. 对 \(\operatorname{Sol}(p)\) 的 E4 lift；
3. 一条已准入 selector edge 的 E5 支付；
4. 有界长度的 Type I/II 证书。

尤其是，任何已命中 direct terminal 的参数都必须在 terminal-first 阶段停止，不能以
factor-block receipt 进入递归分支。因子块引理的可复用研究价值在于：它把后续
adaptive \((a,b)\) 搜索的容量条件缩成端点 reserve (10)，而不是错误地排除所有
\(K\)-共享素因子。
