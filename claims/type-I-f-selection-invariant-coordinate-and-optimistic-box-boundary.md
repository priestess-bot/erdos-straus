---
kind: claim
claim_id: type-I-f-selection-invariant-coordinate-and-optimistic-box-boundary
title: 冻结 F 状态的单坐标零缺陷与乐观扩展盒联合阻碍边界
statement: 对253个冻结平方终端F状态的1181个K支撑坐标，独立使用支撑商群和完整仿射关系格投影计算选择不变单坐标overflow下限，结果全部为0；37个完整源谱私有代理过载坐标也全部为0，故这些代理样本不是固定私有q缺陷。把每个坐标的指数界按当前两源块的最大q进高度独立放宽后，完整目标纤维精确命中91个乐观矩形盒、遗漏162个；遗漏状态的最小投影阻碍维数均至少为2，且每个状态的最小基数层都只有一个阻碍集。该结果证明冻结的乐观矩形模型中存在联合坐标相关性，而非固定单坐标强制，但矩形放宽仍不是兼容载体流或overflow-to-carrier注入。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: independent_review
depends_on:
  - type-I-target-fiber-coordinate-quotient-floor
  - type-I-f-square-terminal-relation-certificate
  - type-I-f-overflow-all-assignment-height-upper-bound
  - type-I-private-carrier-proxy-overflow-escape-profile
topics:
  - type-I
  - F-state
  - target-fiber
  - relation-lattice
  - quotient-group
  - Pareto
  - private-carrier
  - selection-invariant
  - joint-obstruction
  - finite-certificate
  - proof-program
sources:
  - claim: type-I-target-fiber-coordinate-quotient-floor
    role: exact-coordinate-floor-theorem
  - claim: type-I-f-square-terminal-relation-certificate
    role: complete-affine-target-fiber-input
  - claim: type-I-f-overflow-all-assignment-height-upper-bound
    role: deterministic-proxy-and-block-height-input
  - claim: type-I-private-carrier-proxy-overflow-escape-profile
    role: private-proxy-subfamily-and-finite-escape-profile
visibility: public
last_checked: '2026-07-30'
---

# 冻结 F 状态的单坐标零缺陷与乐观扩展盒联合阻碍边界

## 精确对象

对冻结平方终端 F 状态

\[
K=\prod_{i=1}^r q_i^{\nu_i},
\qquad
F=\left\{z\in\mathbb Z^r:
\prod_iq_i^{z_i}\equiv-1\pmod R\right\},
\]

定义

\[
e_i(z)=(|z_i|-\nu_i)_+,
\qquad
\mu_i=\min_{z\in F}e_i(z).
\tag{1}
\]

按照[单坐标商群公式](type-I-target-fiber-coordinate-quotient-floor.md)，商掉其它支撑素数后，
\(q_i\) 的目标指数类和商阶给出 \(\mu_i\) 的精确值。复现脚本同时从已有完整关系格
\(F=z_0+\Lambda\) 计算第 \(i\) 行 gcd 和仿射陪集距离，逐坐标要求两种计算完全一致。

为研究联合缺陷，再对当前线性源 \(p=a+s+asR\) 定义

\[
H_i=\max\{v_{q_i}(aR+1),v_{q_i}(sR+1)\},
\qquad
b_i=\nu_i+H_i.
\tag{2}
\]

脚本精确判定

\[
F\cap B_b,
\qquad
B_b=\prod_i[-b_i,b_i],
\tag{3}
\]

并计算乐观单位残余

\[
\Psi_H(F)=
\min_{z\in F}\sum_i(|z_i|-b_i)_+.
\tag{4}
\]

这里的“乐观”是实质限定：式 (2) 对每个 \(q_i\) 独立选取两块中的最大高度，不要求
不同坐标的选择来自同一载体分配。因此 \(B_b\) 是逐坐标矩形放宽，不是真实兼容载体
资源空间。

## 全部单坐标下限为零

253 个冻结 F 状态共有 1181 个 \(K\)-支撑坐标。商阶分布为

\[
\begin{array}{c|rrr}
o_i&1&2&3\\ \hline
\#&1165&15&1.
\end{array}
\tag{5}
\]

其中 1173 个坐标在商掉自身后，剩余支撑已经包含目标；另外 8 个坐标虽有非零目标类，
但该类仍落在原指数界内。最终

\[
\boxed{\mu_i=0\quad\text{对全部 }1181\text{ 个坐标成立}.}
\tag{6}
\]

此前筛出的 37 个完整源谱私有代理过载坐标也全部满足商阶 1 和 \(\mu_q=0\)。所以

\[
\boxed{
37_{\text{私有代理过载}}
\quad\longrightarrow\quad
0_{\text{选择不变私有 }q\text{ 缺陷}}.}
\tag{7}
\]

这不影响既有有限选择器 \(37=35+2\) 的计算正确性，但改变了它的证据含义：该分流只
闭合确定性首见证，不能支持“真实固定私有 \(q\) 缺陷”这一前提。37 个状态都另有一个
\(q\)-free Type I 命中；其中 35 个在更小 \(R\)，两个在更大 \(R\)。

## 乐观扩展盒与单位残余

对式 (3) 做精确 meet-in-the-middle 成员检查，得到

\[
\boxed{
91_{\text{hit}}+162_{\text{miss}}=253.}
\tag{8}
\]

旧的 `no_assignment_can_carry_all_excess` 分类有 165 个状态，其确定性首见证均不可承载；
其中三个状态却有另一个完整目标表示落入乐观扩展盒：

\[
(p,R)=(79312489,1571),
(214360969,11171),
(549401449,6787).
\tag{9}
\]

这三个对象直接展示了为什么不能用一个规范首见证替代完整目标纤维。

式 (4) 由扩展盒像到目标 \(-1\) 的有限 Cayley 图多源最短路精确计算。生成边是乘以
\(q_i^{\pm1}\)，每条边费用 1。对任意目标指数向量，把各坐标夹到
\([-b_i,b_i]\) 给出长度为总正部的路径；反过来，从盒内点出发的任一路径给出的指数
向量，其总正部不超过路径长度。因此最短路距离恰等于 \(\Psi_H\)。

162 个正残余的直方图为

\[
\begin{array}{c|rrrrrrrrrrrrrrr}
\Psi_H&1&2&3&4&5&6&7&8&9&10&11&12&13&14&15\\ \hline
\#&46&25&20&10&19&9&6&4&7&5&6&1&1&2&1.
\end{array}
\tag{10}
\]

最大值 \(15\) 只出现在

\[
(p,R)=(310002289,137595).
\tag{11}
\]

## 最小联合阻碍子集

对坐标集 \(J\subseteq\{1,\ldots,r\}\)，令 \(\pi_J(F)\) 为目标仿射格的坐标投影。
若

\[
\pi_J(F)\cap\prod_{i\in J}[-b_i,b_i]=\varnothing,
\tag{12}
\]

则称 \(J\) 为投影阻碍；这允许 \(J\) 外的所有坐标无界，因而精确定位联合合同发生在
哪些坐标。脚本把完整关系格基限制到 \(J\) 的行，计算列 Hermite 正规形，并逐点判定
盒中向量与目标仿射类的格成员关系。按 \(|J|\) 递增枚举，得到 162 个 miss 的最小基数
阻碍维数分布：

\[
\begin{array}{c|rrrrrr}
|J|&2&3&4&5&6&7\\ \hline
\#&27&12&35&53&32&3.
\end{array}
\tag{13}
\]

162 个状态在最小基数层都只有一个阻碍集，且没有单坐标阻碍。37 个私有代理状态的
最小基数分布为

\[
2:7,\qquad3:4,\qquad4:13,\qquad5:11,\qquad6:2;
\tag{14}
\]

其唯一的最小基数阻碍集全部包含相应私有 \(q\)。所以私有 \(q\) 在这组有限数据中是联合
阻碍超边的一员，但从来不是独立的强制坐标。

## 最小显式例与量词反例

最小例为

\[
p=214729,\qquad R=43,\qquad K=151\cdot15287,
\qquad b=(2,2).
\]

因为

\[
151\equiv15287\equiv22\pmod{43},
\quad\operatorname{ord}_{43}(22)=14,
\quad22^7\equiv-1\pmod{43},
\]

完整目标纤维满足

\[
z_1+z_2\equiv7\pmod{14}.
\tag{15}
\]

它与 \([-2,2]^2\) 不交，但两个单坐标投影都与 \([-2,2]\) 相交。相对扩展盒的完整
Pareto 溢出前沿为

\[
(0,3),(1,2),(2,1),(3,0).
\tag{16}
\]

因此这个例子同时满足

\[
\forall z\in F\ \exists i:\ |z_i|>b_i,
\qquad
\forall i\ \exists z\in F:\ |z_i|\le b_i,
\tag{17}
\]

却不存在

\[
\exists i\ \forall z\in F:\ |z_i|>b_i.
\]

式 (17) 是不能交换 \(\forall z\exists i\) 与 \(\exists i\forall z\) 的具体算术反例。

## 复现与边界

复现命令：

~~~bash
python3 reproductions/type_i_private_carrier_selection_invariant_defect.py
~~~

结果文件：

~~~text
reproductions/type-i-private-carrier-selection-invariant-defect-results.json
~~~

~~~text
script sha256:
0c5fb541bf2d078b6400e645ef125ee8fed8febbe925a89adad879f98ad22258

result sha256:
34ae63a1ae092943535287110688bf089bd3377c879870a099def9e55f09e7e1

coordinate certificate rows sha256:
4841ddcae6c8ec710355e6214bda3498c20c1da88d9ca194078ce1b0a8095781
~~~

脚本哈希锁定三个既有输入；使用单位群离散对数、支撑商群 HNF 与已有仿射关系格做独立
交叉验证，并冻结全部统计和证书行哈希。它只运行本轮新计算，没有回跑历史素数扫描。

本主张没有证明：

- 式 (2) 的逐坐标最大高度能够由同一个合法载体分配同时实现；
- 盒外指数必须逐层注入这些块高度；
- 最小阻碍超边能够在跨状态中使用同一资源坐标或共同价格；
- 162 个有限状态覆盖所有核心素数，或已经给出统一 Type I/II 选择器。

因此下一步不应继续寻找固定私有 \(q\) 缺陷，而应把唯一的最小基数阻碍集、完整残余
前沿和真实兼容载体配置映到同一资源空间，再寻找跨状态共同价格、超图容量矛盾或改变
\(K\) 支撑且可提升的严格下降。
