---
kind: claim
claim_id: type-I-f-overflow-lower-modulus-high-cost-minimum-face
title: 六个高成本低模数状态的完整单位最小面与共享缺口边界
statement: 对此前仅知 Omega_1 不小于 10 的六个低模数 F-box miss，以已验证目标关系给出成本上界，并用保留每个半边剩余类全部最低成本指数向量的精确 meet-in-the-middle 闭合完整单位最小指数面。六状态共有 36 个最小向量，组成 18 个反演对和 18 个溢出模式；没有单支撑向量，支撑大小 2、3、4 各 12 个。完整共享缺口 Type II 审计命中 3 个状态、遗漏 3 个。与原 36 状态合并后，42 个状态的单位最小面全部闭合，其中 21 个状态有旁路证书、21 个在整个最小面无命中。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-overflow-lower-modulus-min-overflow-shared-gap
  - type-I-f-overflow-lower-modulus-pareto-capacity-flow-boundary
  - type-I-f-overflow-lower-modulus-shortest-relation-profile
topics:
- type-I
- type-II
- F-state
- lower-modulus
- minimum-face
- meet-in-the-middle
- overflow
- shared-gap
- finite-audit
sources:
- claim: type-I-f-overflow-lower-modulus-min-overflow-shared-gap
  role: resolved-36-state-baseline
- claim: type-I-f-overflow-lower-modulus-pareto-capacity-flow-boundary
  role: exact-omega-and-overflow-pattern-crosscheck
- claim: type-I-f-overflow-lower-modulus-shortest-relation-profile
  role: finite-valid-upper-bounds
visibility: public
last_checked: '2026-07-30'
---

# 六个高成本低模数状态的完整单位最小面与共享缺口边界

## 完整单位最小面

对低模数目标纤维 \(F_s\)，记

\[
e_s(z)_i=(|z_i|-\nu_i)_+,
\qquad
\Omega_1(s)=\min_{z\in F_s}|e_s(z)|_1,
\]

并定义单位最小指数面

\[
\mathcal M_s
=
\left\{
z\in F_s:\ |e_s(z)|_1=\Omega_1(s)
\right\}.
\tag{1}
\]

本卡闭合的是全部指数向量组成的 \(\mathcal M_s\)，不是只保留一个代表元，也不是
完整 Pareto 前沿。

对每个此前未解析状态，已有最短关系给出一个有限有效上界 \(U\)。把指数坐标分成
左右两半；对每个半边剩余类 \(r\)，脚本完整枚举成本 \(0,\ldots,U\)，保留该剩余类
的最低成本以及该成本下的**全部**半边指数向量。若全局最优向量的某个半边不是其
剩余类的最低成本表示，以更低成本的同剩余类表示替换后仍命中 \(-1\pmod t\)，却会
严格降低总成本，矛盾。因此匹配

\[
r_Lr_R\equiv-1\pmod t
\]

的全部最低半边向量，恰好恢复完整的 \(\mathcal M_s\)。

每个半边的成本层计数还独立由截断生成函数

\[
\prod_{i\in S}
\left((2\nu_i+1)+\frac{2x}{1-x}\right)
\tag{2}
\]

逐系数复核：常数项对应盒内指数，正成本 \(k\) 的两个选择对应
\(\pm(\nu_i+k)\)。因此搜索边界由已验证上界封闭，不是无界扩张。

## 六状态结果

六个最小面的完整统计为：

| \(p\) | \(t\) | \(U\) | \(\Omega_1\) | \(|\mathcal M_s|\) | 溢出模式数 | 支撑大小分布 | Type II 命中缺口 |
|---:|---:|---:|---:|---:|---:|---|---|
| 62704849 | 649 | 12 | 12 | 6 | 3 | \(2:6\) | 无 |
| 75056809 | 21113 | 13 | 11 | 8 | 4 | \(3:4,4:4\) | \(27,59,107,215,311,1247\) |
| 310002289 | 107977 | 19 | 18 | 8 | 4 | \(2:2,3:2,4:4\) | \(19,171\) |
| 312918169 | 16649 | 10 | 10 | 6 | 3 | \(2:2,3:2,4:2\) | \(31,47\) |
| 366108649 | 11057 | 13 | 12 | 6 | 3 | \(3:4,4:2\) | 无 |
| 373561609 | 208577 | 15 | 15 | 2 | 1 | \(2:2\) | 无 |

总计 36 个指数向量，恰好组成 18 个反演对。每个反演对
\(\{z,-z\}\) 具有同一个 overflow 模式以及同一个有理关系和

\[
\prod q_i^{z_i}=\frac ab,
\qquad
a+b\equiv0\pmod t.
\]

18 个模式和 18 个和式一一对应。完整面中没有单支撑向量；双支撑、三支撑、四支撑
向量各 12 个。因此此前六个高成本状态的障碍不是“尚未把单坐标射线搜得足够远”，
而是其单位最优需求本身全部是多坐标的。

## 全部并列最小向量上的 Type II 检查

对每个反演不变的 \(a+b\)，脚本给出完备素因子分解，枚举所有满足

\[
h\mid a+b,\qquad h\equiv3\pmod4,\qquad 3\le h\le p-2
\]

的缺口，并独立完整检查 \(x_h=(p+h)/4\) 的 Type II 规范形除数。大素因子的
素性使用递归 Lucas \(n-1\) 证书，故合法缺口枚举不依赖概率素性判断。

结果为：

- \(p=75056809\) 和 \(p=310002289\) 的每一个最小向量都至少命中一个共享缺口；
- \(p=312918169\) 有 4/6 个最小向量命中；
- 其余三个状态的完整最小面无命中。

所以六状态中 3 个状态获得旁路、3 个状态在完整单位最小面上严格遗漏；共有 20/36
个最小向量命中。三个命中状态的字典序规范向量也都命中，因此没有新增
“仅非规范并列向量命中”的状态。10 个“状态—缺口”命中共给出 33 张不同 Type II
证书；按状态内不同 \(a+b\) 分层后共有 13 个“状态—和—缺口”命中，产生 60 个按
\(a+b\) 分层的证书发生。

命中向量的支撑大小分布为 \(2:2,3:8,4:10\)，遗漏向量则为
\(2:10,3:4,4:2\)。因此双支撑并不自动产生 shared-gap 旁路：六状态的 12 个
双支撑最小向量中只有 2 个命中。

## 对原 36 状态主张的更新

与[低模数最小溢出层的共享缺口 Type II 覆盖边界](type-I-f-overflow-lower-modulus-min-overflow-shared-gap.md)
合并后，原先的六个“最小面未解析”可以全部移除。这里的“审计完成”只指单位最小面
已被完整枚举和判定，不表示 42 个状态都已获得猜想的分解。更新统计为：

~~~text
minimum-face audit complete states: 42
minimum-face audit incomplete states: 0
minimum exponent vectors: 240
inverse pairs: 120
per-state unique sums: 120
globally unique sums: 119

canonical-vector hit states: 17
all-minimum-face hit states: 21
tied-minimum-only hit states: 4
complete-minimum-face miss states: 21

state candidate gaps: 960
minimum-vector/gap incidences: 2214
distinct (p,h) checks: 914
state-gap hits: 35
distinct (p,h) hits: 34
state-scoped Type II certificates: 90
distinct Type II certificates: 89
~~~

全部 240 个最小向量的支撑大小分布为

~~~text
support size 1: 100
support size 2: 64
support size 3: 52
support size 4: 24
~~~

42 个状态中有 22 个状态的最小面含单支撑向量，19 个含双支撑向量；两类状态可以
重叠。按 Type II 结果再分层，命中向量为
\(1:30,2:14,3:14,4:14\)，遗漏向量为
\(1:70,2:50,3:38,4:10\)。精确 \(\Omega_1\) 分布更新为

~~~text
1:12, 2:8, 3:2, 4:4, 5:2, 6:2, 7:2, 8:3, 9:1,
10:1, 11:1, 12:2, 15:1, 18:1.
~~~

因此 cap-9 时代关于 36 个已解析状态的“整个最小面”结论现在可以无条件扩展到冻结
的全部 42 个状态。shared-gap Type II 覆盖率恰为 21/42，另 21 个只是单位最小面上
未命中，并非已证明不可解；这不同于只对较低成本子样本计算的 18/36。

## 冻结输入与复现

脚本：

~~~text
reproductions/type_i_f_overflow_lower_modulus_high_cost_minimum_face.py
~~~

结果：

~~~text
reproductions/type-i-f-overflow-lower-modulus-high-cost-minimum-face-results.json
~~~

关键冻结输入 SHA-256：

~~~text
type-i-f-overflow-lower-modulus-pareto-overflow-results.json
8fd82842893674641cf15928cf436d872e450b5fd175d47f8a825fad5603c6fe

type-i-f-overflow-lower-modulus-shortest-relation-results.json
077f565596f9f06e30aca5c7c6c6de487b455581f9e28801b84950531032ad42

type-i-f-overflow-lower-modulus-pareto-capacity-flow-results.json
993b3280dd8551e7c26bfbf9164f68172c87ac1412b6827c3bda8b44647b6cb4

type_i_f_overflow_lower_modulus_min_overflow_shared_gap_results.json
085a65615fcd2cc1e30330e4039483f36491871c41cad11d54123514a3f2852f
~~~

结果 SHA-256：

~~~text
4bd400d1406bd1395352f052eaad7d9418977375b67bccb1ac95a771dd4493f8
~~~

复现命令：

~~~bash
python3 reproductions/type_i_f_overflow_lower_modulus_high_cost_minimum_face.py
~~~

## 证明边界

本卡只闭合单位权最小指数面 \(\mathcal M_s\)。21 个遗漏状态的结论是：这一精确
最小面没有共享缺口 Type II 旁路；它不排除更高单位成本关系、其它正权
\(\Omega_w\)、完整 Pareto 前沿、因子重分配、非共享缺口 Type II 或其它可提升递降。
反过来，21 个命中也只是冻结状态上的显式短证书旁路，尚未构成对任意核心素数的
统一选择定理。
