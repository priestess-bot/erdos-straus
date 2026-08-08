---
kind: claim
claim_id: type-I-target-fiber-density-neighbor-fourier-trichotomy
title: 目标纤维近邻—盒密度—规范 Fourier 三分
statement: 对有限阿贝尔群中的有界指数盒，目标纤维计数若超过 2^r 必有近邻偶终端；若目标纤维不超过 2^r 但盒平均密度 |B|/|H| 超过 2^r，则存在带显式幅度下界的规范非平凡 Fourier 缺口；否则得到严格的低密度容量不等式 |B|<=2^r|H|。若目标不在生成子群中，则先输出 G 型商分离。该三分只提供有限群证书或容量输入，不自动给出整数 lift。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-target-fiber-neighbor-terminal
  - type-I-target-fiber-fourier-overflow-generating-function
  - type-I-target-fiber-neighbor-dyadic-normalization
  - type-I-fg-role-snf-terminal-dispatch
topics:
  - type-I
  - F-state
  - G-state
  - target-fiber
  - near-pair
  - Fourier
  - density
  - capacity
  - selector
  - proof-program
sources:
  - claim: type-I-target-fiber-neighbor-terminal
    role: near-pair-terminal-threshold
  - claim: type-I-target-fiber-fourier-overflow-generating-function
    role: exact-fiber-Fourier-count
  - claim: type-I-fg-role-snf-terminal-dispatch
    role: finite-character-routing
  - reproduction: reproductions/type_i_target_fiber_density_neighbor_fourier_trichotomy.py
    role: four-branch-exact-receipt
visibility: public
last_checked: '2026-08-09'
---

# 目标纤维近邻—盒密度—规范 Fourier 三分

## 设置

令 \(G\) 为有限阿贝尔群，\(g_1,\ldots,g_r\in G\)，并令

\[
H=\langle g_1,\ldots,g_r\rangle,
\qquad
\mathcal B_\nu=\prod_{i=1}^r[-\nu_i,\nu_i]\cap\mathbb Z^r,
\qquad
V=|\mathcal B_\nu|=\prod_i(2\nu_i+1).
\]

定义

\[
\phi(z)=\prod_i g_i^{z_i},
\qquad
N_y=|\{z\in\mathcal B_\nu:\phi(z)=y\}|,
\qquad
T_r=2^r.
\]

对 \(\chi\in\widehat H\) 使用未归一化的盒 Fourier 和

\[
\widehat{\mathcal B}_\nu(\chi)
=\sum_{z\in\mathcal B_\nu}\chi(\phi(z)).
\tag{1}
\]

若 \(y\in H\)，记盒平均纤维数

\[
\mu=\frac V{|H|}.
\tag{2}
\]

## 三分定理

对每个固定的 \(G,(g_i),(\nu_i),y\)，选择器按下列互斥顺序输出：

1. 若 \(y\notin H\)，输出 G_QUOTIENT_SEPARATION。有限商 \(G/H\) 中存在一个
   在 \(H\) 上平凡而在 \(y\) 上非平凡的角色。
2. 若 \(y\in H\) 且 \(N_y>T_r\)，则目标纤维含有不同的 \(z,w\)，满足
   \(|z_i-w_i|\le\nu_i\) 对所有 \(i\)；于是已有近邻终端引理给出广义 \(2^j\) 偶终端。
3. 若 \(y\in H\)、\(N_y\le T_r\)、\(|H|>1\) 且
   \(V>|H|T_r\)，令 \(\delta=\mu-N_y>0\)。则存在非平凡
   \(\chi_*\in\widehat H\) 使

\[
-\operatorname{Re}\left(\overline{\chi_*(y)}
\widehat{\mathcal B}_\nu(\chi_*)\right)
\ge
\frac{|H|\delta}{|H|-1}
=\frac{V-|H|N_y}{|H|-1}>0.
\tag{3}
\]

   按“最大左端、角色阶最小、群坐标字典序”选择 \(\chi_*\)，即可得到规范的
   FIBER_DENSITY_FOURIER_DEFICIT。其角色阶自动整除 \(\exp(H)\)，可以交给已有
   source-label SNF 或固定层 Fourier 分派，但 (3) 本身不声称整数 lift。
4. 若 \(y\in H\)、\(N_y\le T_r\) 且 \(V\le|H|T_r\)，输出
   FIBER_BOX_DENSITY_CAPACITY，其精确容量回执为

\[
\boxed{V\le 2^r|H|.}
\tag{4}
\]

   这不是失败的空白记录，而是一个可与 q 进层容量比较的状态级上界。

当 \(|H|=1\) 时，第三分支不适用；若 \(N_y\le T_r\)，必有 \(V=N_y\le T_r\)，
所以自动落入第四分支。

## 证明

若 \(y\notin H\)，有限阿贝尔对偶性给出商 \(G/H\) 中分离 \(yH\) 的角色，第一分支
成立。

设 \(y\in H\)。把每个坐标区间分成两个符号盒，并将零坐标固定归入正半盒。若
每个符号盒至多含一个目标指数点，则目标纤维总数至多为 \(2^r\)。因此
\(N_y>2^r\) 时必有一对 \(z,w\) 在同一符号盒中，从而
\(|z_i-w_i|\le\nu_i\)；近邻终端引理给出第二分支。

现在设 \(N_y\le T_r\) 且 \(V>|H|T_r\)。有限群角色正交关系给出

\[
\sum_{\chi\in\widehat H}
\overline{\chi(y)}\widehat{\mathcal B}_\nu(\chi)
=|H|N_y.
\tag{5}
\]

平凡角色项等于 \(V\)，故非平凡角色的实部总和为

\[
\sum_{\chi\ne1}\operatorname{Re}\left(
\overline{\chi(y)}\widehat{\mathcal B}_\nu(\chi)\right)
=|H|N_y-V=-|H|\delta.
\tag{6}
\]

共有 \(|H|-1\) 个非平凡角色，所以其中一个实部不大于平均值
\(-|H|\delta/(|H|-1)\)，即得到 (3)。

最后，如果第三分支的密度条件不成立，正是 \(V\le|H|T_r\)，得到 (4)。四个分支
互斥且穷尽。证毕。

## 与 F/G 和容量接口的关系

该三分把已有的两个局部出口接成一个确定性门：

\[
\text{目标不在 }H
\to G\text{ 商分离};
\qquad
N_y>2^r
\to\text{近邻/广义 }2^j\text{ 终端};
\]

\[
N_y\le2^r,\ V>|H|2^r
\to\text{规范 Fourier 缺口};
\qquad
N_y\le2^r,\ V\le|H|2^r
\to\text{低密度容量上界}.
\]

第三分支的角色不是任意“首个非零 Fourier 系数”：式 (3) 给出目标缺失相对于盒
平均的有符号缺口和显式下界，因此可以按固定规则排序后交给 SNF、q-primary 阶筛或
关系格。第四分支则量化了剩余的表示容量，后续若有多个状态共享同一目标需求，可
直接比较这些 \(V/|H|\) 上界。

需要保留的边界是：非平凡 Fourier 角色仍可能没有带来源标签的整数实现，低密度上界
也不自动产生跨状态超载；二者必须继续通过全域解提升、q 进载体映射或良基势门。

## 精确控制

以下四行分别命中四个分支：

| 控制 | \(G\) 与生成元 | \((\nu_i)\) | \(y\) | 输出 |
|---|---|---:|---:|---|
| G 商分离 | \(C_6, g_1=2\) | \((1)\) | \(1\notin\langle2\rangle\) | G_QUOTIENT_SEPARATION |
| 近邻终端 | \(C_3, (g_1,g_2)=(1,1)\) | \((2,2)\) | \(0\) | \(N_y=9>4\) |
| Fourier 缺口 | \(C_2, g_1=1\) | \((2)\) | \(1\) | \(N_y=2,\ V=5>4\) |
| 低密度容量 | \(C_7, g_1=1\) | \((1)\) | \(1\) | \(V=3\le14\) |

在 Fourier 控制中，唯一非平凡角色取值为 \((-1)^x\)，且

\[
\widehat{\mathcal B}_\nu(\chi_*)=1,
\qquad
-\operatorname{Re}\bigl(\overline{\chi_*(1)}
\widehat{\mathcal B}_\nu(\chi_*)\bigr)=1,
\]

恰好达到 (3) 的下界。

## 研究边界

该引理新增的是“近邻阈值—盒平均—规范 Fourier 缺口”的严格选择桥，而不是新的
Erdős--Straus 全称证明。它把 F/G 路线的下一个决定性缺口具体化为：证明第三分支的
\(\chi_*\) 能进入带来源的 q-primary/格证书，或证明第四分支的低密度容量在跨状态
共享需求下必然超载；若两者均不能推进，则应转向新的整数终端或良基递降。

## 聚焦复现

~~~bash
python3 reproductions/type_i_target_fiber_density_neighbor_fourier_trichotomy.py --verify
~~~

该回执只验证四个分支的精确计数、近邻条件、Fourier 下界和低密度不等式，不做历史范围扫描。
