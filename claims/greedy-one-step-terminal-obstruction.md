---
kind: claim
claim_id: greedy-one-step-terminal-obstruction
title: Erdős--Straus 的单步贪心终端并不总能二项分裂
statement: 对 p=73，贪心首分母 ceil(p/4)=19 后的余项是 3/1387，不能写成两个正单位分数。因此“首步贪心后总可由二项因子式完成三项分解”的算法断言是错误的，不能构成 Erdős--Straus 猜想的递降或证明。
claim_status: established
topics:
- obstruction
- greedy-algorithm
- two-unit-fractions
- counterexample
- proof-program
sources:
- paper: roy_hgdd2026
  locator: "Section 2.2 and Section 4.3; terminal two-unit solver claim"
  role: contradicted-algorithm-claim
visibility: public
last_checked: '2026-07-24'
---

# Erdős--Straus 的单步贪心终端并不总能二项分裂

## 反例

取核心素数

\[
p=73,\qquad \left\lceil\frac p4\right\rceil=19.
\]

首步贪心后的余项为

\[
\frac4{73}-\frac1{19}
=\frac3{1387},\qquad 1387=19\cdot73. \tag{1}
\]

它不能写为 \(1/u+1/v\)。

## 证明

若

\[
\frac3{1387}=\frac1u+\frac1v,
\]

则标准二项单位分数因子式给出

\[
(3u-1387)(3v-1387)=1387^2. \tag{2}
\]

令 \(D=3u-1387\)。因为 \(u,v>0\)，有 \(D>0\) 且

\[
D\mid1387^2,\qquad D\equiv-1387\equiv2\pmod3. \tag{3}
\]

但 \(19\equiv73\equiv1\pmod3\)，所以 \(1387^2\) 的每个正因子都
\(\equiv1\pmod3\)，与 (3) 矛盾。

## 对 HGDD 的含义

Roy 的 HGDD 预印本在终端阶段使用同一因子式，并声称对任意
\(0<m'<n'\) 总能找到适合的二项因子。例 (1)--(3) 直接否定该断言：这里
\(m'=3,n'=1387\)，所有因子均错过所需残数类。因此贪心分子递减只保证有限项
Egyptian 分数展开的通常终止性，不能保证在 Erdős--Straus 所需的固定三项长度处终止。
