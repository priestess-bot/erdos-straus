---
kind: claim
claim_id: type-II-shared-selector-finite-collision-state
title: 连续共享 Type II 窗口的联合有限碰撞状态分解
statement: 对核心素数 \(p\) 和有限窗口 \(j=1,\ldots,J\)（\(J\ge3\)），令 \(m_j=4j-1\)、\(x_j=(p+m_j)/4\)，并从 \(x_j\) 剥离所有小于 \(J\) 的素数幂，得 \(x_j=E_jR_j\)。则 \(R_1,\ldots,R_J\) 两两互素；同一缺口的 Type II 目标 \(-x_j\in\Pi_{m_j}(x_j^2)\) 与非平凡共享目标 \(1\in\Pi_{m_j}^{>1}(4x_j)\) 都精确分解为有限碰撞部分 \(E_j\) 和私有部分 \(R_j\) 的乘积残数条件。因而任一有限窗口的联合失败可无损编码为有限碰撞状态及两两互素私有除子残数积集，不能再归因于未知的大跨缺口公因子。
claim_status: established
topics:
- type-II
- shared-divisor
- moving-window
- collision-state
- divisor-residues
- product-sets
- proof-program
sources:
- paper: bradford2024
  locator: Section 2, Type II divisor certificates
  role: Type-II-residue-criterion
- paper: grynkiewicz_marchan_ordaz2009
  locator: subsequence-product framework
  role: product-set-language
visibility: public
last_checked: '2026-07-25'
---

# 连续共享 Type II 窗口的联合有限碰撞状态分解

## 设置

令 \(p\equiv1\pmod{24}\) 为素数，且 \(J\ge3\)。对

\[
m_j=4j-1,\qquad x_j=\frac{p+m_j}{4}\qquad(1\le j\le J),
\]

记

\[
\mathcal C_J=\{q:q\text{ 为某个 }1\le r<J\text{ 的素因子}\}.
\]

从 \(x_j\) 中取出所有属于 \(\mathcal C_J\) 的素数幂，写作

\[
x_j=E_jR_j.
\]

对与 \(m\) 互素的 \(N\)，沿用除子残数集

\[
\Pi_m(N)=\{d\bmod m:d\mid N\},
\]

并以 \(\Pi_m^{>1}(N)\) 表示其中由非平凡整数除子得到的残数。后一记号必须
保留：残数 \(1\) 可能既来自平凡除子，也来自非平凡除子。

## 引理

有

\[
\gcd(R_j,R_k)=1\qquad(j\ne k). \tag{1}
\]

并且每个 \(x_j\) 都与 \(m_j\) 互素，故所有下式中的残数都在
\((\mathbb Z/m_j\mathbb Z)^\times\) 内。Type II 条件精确分解为

\[
-x_j\in
\Pi_{m_j}(E_j^2)\Pi_{m_j}(R_j^2). \tag{2}
\]

共享因子条件精确分解为

\[
1\in\Pi^{>1}_{m_j}(4E_jR_j), \tag{3}
\]

也就是存在

\[
a\in\Pi_{m_j}(4E_j),\quad b\in\Pi_{m_j}(R_j),\quad ab=1\pmod {m_j}, \tag{4}
\]

且 \(a\) 或 \(b\) 至少一个来自相应的非平凡除子集。

因此同一缺口的联合共享 Type II 命中，恰为 (2) 与 (3) 同时成立；其失败状态是
有限碰撞残数诱导出的两个私有目标集同时被 \(\Pi_{m_j}(R_j^2)\) 与
\(\Pi_{m_j}(R_j)\) 避开。

## 证明

由 \(x_j-x_k=j-k\)，任一同时整除 \(x_j,x_k\) 的素数整除某个小于 \(J\) 的
正整数，故属于 \(\mathcal C_J\)。剥离该集合中的全部幂即得 (1)。又若素数同时整除
\(x_j,m_j\)，则它整除 \(4x_j-m_j=p\)；但 \(m_j<p\)，矛盾。

唯一分解给出

\[
\Pi_{m_j}(x_j^2)=
\Pi_{m_j}(E_j^2)\Pi_{m_j}(R_j^2),
\]

从而得到 (2)。因为 \(2\in\mathcal C_J\)，乘入固定因子 \(4\) 只改变碰撞部分，
故

\[
\Pi_{m_j}(4x_j)=
\Pi_{m_j}(4E_j)\Pi_{m_j}(R_j).
\]

对所有实际除子记录“是否非平凡”这一位，恰好排除唯一的平凡乘积
\(1\cdot1\)，遂得 (3)--(4)。

## 压力点审计

对已知共享选择器压力点

\[
p=33\,011\,449
\]

取 \(J=31\)，完整分解全部 \(x_j\)，并枚举每个碰撞/私有因子部分的完整除子残数。
所得碰撞素数为

\[
\{2,3,5,7,11,13,17,19,23,29\}.
\]

31 个私有部分两两互素。更重要的是，两个单条件并不同时失败：

| 条件 | 命中缺口 |
|---|---|
| Type II | \(19,27,71,75,79\) |
| 非平凡共享因子 | \(3,7,11,15,23,35,39,47,51,55,119\) |
| 联合共享 Type II | 无 |

这与该点至 \(m=500000\) 没有联合见证的独立完整审计一致，但本卡只声称窗口
\(m\le123\) 的精确状态分解，不把该有限剖面外推为全称规律。

重建：

```bash
python3 reproductions/type_ii_shared_selector_collision_state.py
python3 -m unittest tests/test_type_ii_shared_selector_collision_state.py -q
```

## 下一条可证伪命题

这个引理并未制造跨模数关系；(1) 反而表明困难全部落在同一 \(p\) 所产生的不同
私有积集如何同时避开其诱导目标。所以下一条正向命题应是一个真正的状态闭包：对增长
窗口，证明连续的联合失败要么在新缺口产生联合命中，要么强制一个可验证减少的残数状态。
它必须允许私有素因子数、零积长度和窗口长度增长；固定其中任意一个量都已另有反例边界。

本引理不证明这种闭包，也不蕴含 Erdős--Straus 猜想。
