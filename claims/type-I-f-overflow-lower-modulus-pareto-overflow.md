---
kind: claim
claim_id: type-I-f-overflow-lower-modulus-pareto-overflow
title: 低模数 F-box miss 的选择不变 Pareto 溢出前沿
statement: 对冻结的 42 个低模数 F-box miss，完整判定单位总成本不超过 9 的每个溢出向量是否命中目标纤维，得到 415 个全局 Pareto 极小点；其中单坐标 69 个，多坐标 346 个。成本 10 壳层的上闭包覆盖进一步证明 8 个状态的整个 Pareto 集已经闭合；其余 28 个有命中状态只得到精确截断前沿，另 6 个状态在本截断内只能推出单位价格至少为 10，后续算法虽已求出其精确单位价格，但完整 Pareto 前沿仍未知。该有限前沿对任意正权生成一个选择不变的 Omega_w 接口，但未证明 q 进容量收费或递降。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: independent_review
depends_on:
  - type-I-f-overflow-lower-modulus-weighted-cost-interface
  - type-I-f-overflow-lower-modulus-weighted-cost-profile
  - type-I-f-overflow-lower-modulus-relation-lattice
  - type-I-f-overflow-repair-transition-potential-boundary
topics:
- type-I
- F-state
- finite-box
- overflow
- Pareto-frontier
- weighted-capacity
- relation-lattice
- finite-audit
sources:
- claim: type-I-f-overflow-lower-modulus-weighted-cost-interface
  role: invariant-definition
- claim: type-I-f-overflow-lower-modulus-weighted-cost-profile
  role: independent-unit-weight-check
- claim: type-I-f-overflow-lower-modulus-relation-lattice
  role: frozen-42-state-input
- claim: type-I-f-overflow-repair-transition-potential-boundary
  role: exact-unit-cost-completion-beyond-cap-nine
visibility: public
last_checked: '2026-07-30'
---

# 低模数 F-box miss 的选择不变 Pareto 溢出前沿

## 对象与截断定理

对每个冻结状态 \(s\)，沿用低模数目标纤维

\[
F_s=\left\{z\in\mathbb Z^r:
\prod_{i=1}^r q_i^{z_i}\equiv-1\pmod t\right\}
\]

及逐坐标溢出

\[
e(z)_i=(|z_i|-\nu_i)_+.
\]

令

\[
\mathcal O_s=\{e(z):z\in F_s\},\qquad
E_s=\min_{\preceq}\mathcal O_s,
\]

其中 \(\preceq\) 是逐坐标偏序。脚本对每个
\(e\in\mathbb Z_{\ge0}^r\)、\(|e|_1\le9\) 完整枚举对应的指数选择：当
\(e_i=0\) 时取 \(-\nu_i\le z_i\le\nu_i\)，当 \(e_i>0\) 时取
\(z_i=\pm(\nu_i+e_i)\)。因此它精确判定该溢出向量是否属于
\(\mathcal O_s\)。

由此得到的截断前沿不是“截断盒里的局部极小”，而恰为

\[
E_s^{\le9}=E_s\cap\{e:|e|_1\le9\}.
\tag{1}
\]

事实上，若 \(|e|_1\le9\) 且存在严格支配它的可实现向量 \(e'\preceq e\)，则
\(|e'|_1\le|e|_1\le9\)，所以 \(e'\) 也在同一次完整枚举中。故脚本保留的
每一个点都是全局 Pareto 极小点；截断性只表示成本 9 之外可能还有与它们不可比的
新极小点。

## 下一壳层的全局闭合证书

对已发现集合 \(P=E_s^{\le9}\)，脚本再检查成本 10 壳层。若

\[
\forall a\in\mathbb Z_{\ge0}^r,\quad |a|_1=10
\Longrightarrow \exists e\in P:\ e\preceq a,
\tag{2}
\]

则 \(E_s=P\)。因为任意 \(|x|_1>10\) 都含有某个
\(a\preceq x\)、\(|a|_1=10\)，再由 (2) 得 \(e\preceq a\preceq x\)。所以成本
10 以上不可能产生新的极小点。

(2) 在下列 8 个状态成立，故这些状态的整个 Pareto 集已被有限证明闭合：

| \(p\) | \(t\) | 方向 | \(|E_s|\) |
|---:|---:|---|---:|
| 106050289 | 97 | forward | 5 |
| 155533849 | 89 | forward | 3 |
| 306963409 | 125 | forward | 5 |
| 408626089 | 177 | forward | 4 |
| 463627609 | 193 | forward | 7 |
| 509434249 | 41 | reverse | 4 |
| 534844249 | 121 | forward | 5 |
| 556685089 | 49 | reverse | 4 |

另外 28 个状态在成本 9 内已有 Pareto 点，但成本 10 壳层未被其上闭包完全覆盖；
对它们只能声明 (1)。剩余 6 个状态在成本 9 内没有目标命中：

~~~text
(p, t, orientation)
(62704849, 649, forward)
(75056809, 21113, reverse)
(310002289, 107977, reverse)
(312918169, 16649, forward)
(366108649, 11057, forward)
(373561609, 208577, forward)
~~~

原 F 见证仍保证这些目标纤维非空；本次截断只能推出
\(\Omega_1\ge10\)，不能推出 \(E_s=\varnothing\)。后续 Cayley 图算法已把六个
单位权最小值精确补齐为 \(12,11,18,10,12,15\)，但标量最小值不提供这些状态的
完整 Pareto 前沿。

## 前沿结构

完整运行覆盖 74316 个非负溢出向量、对应 8038188 个有限指数选择，发现 3611 个
可实现的溢出向量；去除逐坐标受支配点后留下 415 个 Pareto 点。其支撑大小分布为：

~~~text
support size 1: 69
support size 2: 142
support size 3: 136
support size 4: 54
support size 5: 14
~~~

因此单坐标点仅占 69/415；346/415 个点需要至少两个溢出坐标。36 个在截断内有
命中的状态中，23 个至少有一个单坐标点，但只有 6 个状态的已发现前沿全部由单坐标
点组成；30 个状态具有多坐标点。因此当前有限样本的完整 Pareto 需求不能统一压缩为
单坐标列表。

坐标复用同样明显。全部状态共有 158 个被 Pareto 支撑使用的“状态—坐标”对，其中
119 个出现在至少两个 Pareto 点中；36 个非空截断前沿中有 29 个发生这种复用。
415 个点只有 283 种支撑集合，19 个状态在同一支撑上出现多个不可比溢出分配，合计
多出 132 个 Pareto 点。因此容量接口不能只记“活跃坐标集合”，还必须保留同一支撑
内部的层数分配。

## 任意正权的有限生成接口

对正权 \(w_i>0\)，令

\[
\widehat\Omega_{w,9}(s)
=\min_{e\in E_s^{\le9}}\sum_iw_i e_i.
\tag{3}
\]

这使每个已发现前沿成为有限个线性费用的生成器，完全不依赖 Smith 原像或 BFS
代表元：

- 对上述 8 个闭合状态，
  \(\Omega_w(s)=\widehat\Omega_{w,9}(s)\) 对所有正权都精确成立。
- 对 28 个非空但未闭合的状态，(3) 一般只是
  \(\Omega_w(s)\) 的上界。任何未发现点都满足 \(|e|_1\ge10\)，故其费用至少为
  \(10\min_iw_i\)。因此只要
  \[
  \widehat\Omega_{w,9}(s)\le10\min_iw_i,
  \tag{4}
  \]
  (3) 就已经是精确的 \(\Omega_w(s)\)；否则仍可能有成本大于 9、但因权重偏斜而
  更便宜的新 Pareto 点。
- 对 6 个空截断状态，本结果只有
  \(\Omega_w(s)\ge10\min_iw_i\)，没有来自成本 9 前沿的有限上界生成器。后续得到的
  精确 \(\Omega_1\) 只补齐单位权特化，不补齐一般正权生成器。

单位权 \(w_i=1\) 下，36 个非空状态自动满足 (4)，其最小值分布独立复核为

~~~text
1:12, 2:8, 3:2, 4:4, 5:2, 6:2, 7:2, 8:3, 9:1.
~~~

## 冻结输入与复现

独立脚本：

~~~text
reproductions/type_i_f_overflow_lower_modulus_pareto_overflow.py
~~~

结果文件：

~~~text
reproductions/type-i-f-overflow-lower-modulus-pareto-overflow-results.json
~~~

输入及 SHA-256：

~~~text
type-i-f-overflow-r-modulus-repair-results.json
c656c91ebb02a33e8d1f5c78db70ce14ac5fbc2decc0db99e05bcbcc1fbee22f

type-i-f-overflow-support-boundary-results.json
93c571a0fdfe12d18028c21d10c1f8445b1e34ae979489c852478d0bce8ad9b1
~~~

结果 SHA-256：

~~~text
8fd82842893674641cf15928cf436d872e450b5fd175d47f8a825fad5603c6fe
~~~

复现命令：

~~~bash
python3 reproductions/type_i_f_overflow_lower_modulus_pareto_overflow.py
~~~

## 解释边界

本卡把任意表示向量替换为选择不变的目标纤维 Pareto 对象，并给出正权价格的有限
生成接口；它没有把坐标溢出证明为实际的 \(q\)-进载体高度，也没有证明跨状态容量
超载、Type I/II 证书或严格可提升递降。特别是 28 个截断非空状态仍可能在成本 9
之外产生新的多坐标分配；6 个空截断状态的真正前沿尚未触及。
