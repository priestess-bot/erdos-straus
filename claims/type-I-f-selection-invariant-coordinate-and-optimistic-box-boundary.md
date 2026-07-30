---
kind: claim
claim_id: type-I-f-selection-invariant-coordinate-and-optimistic-box-boundary
title: 冻结 F 状态的单坐标零缺陷与反事实重复高度扩盒边界
statement: 对253个冻结平方终端F状态的1181个K支撑坐标，独立使用支撑商群和完整仿射关系格投影计算选择不变单坐标overflow下限，结果全部为0；37个完整源谱私有代理过载坐标也全部为0，故这些代理样本不是固定私有q缺陷。历史计算再把每个坐标的指数界按当前两源块的最大q进高度重复放宽，完整目标纤维精确命中91个反事实矩形盒、遗漏162个；遗漏状态的最小投影阻碍维数均至少为2，且每个状态的最小基数层都只有一个阻碍集。固定(a,s)时整条逐q最大高度向量可由同一对源块同时读出，并不存在“各坐标最大值不能来自同一物理分配”的问题；真正边界是这些高度已计入K，且尚无把overflow注入它们的代数映射。因此nu+H扩盒只是一项重复使用当前高度的应力测试，不是兼容容量上界或overflow-to-carrier证书。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: independent_review
depends_on:
  - type-I-target-fiber-coordinate-quotient-floor
  - type-I-f-square-terminal-relation-certificate
  - type-I-f-overflow-all-assignment-height-upper-bound
  - type-I-private-carrier-proxy-overflow-escape-profile
  - type-I-f-current-block-saturation-and-signed-denominator-defect
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

# 冻结 F 状态的单坐标零缺陷与反事实重复高度扩盒边界

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

历史计算还对当前线性源 \(p=a+s+asR\) 定义

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

并计算相对这个扩展盒的单位距离

\[
\Psi_H(F)=
\min_{z\in F}\sum_i(|z_i|-b_i)_+.
\tag{4}
\]

这里必须修正此前对“乐观”的解释。固定 \((a,s)\) 后，两块

\[
U=aR+1,\qquad V=sR+1
\]

已经同时确定整条向量 \((H_i)_i\)；逐 \(q_i\) 混合读取两块中较大的高度，并不要求
换用另一个物理源对。它未必尊重一个预先指定的 Fourier 颜色，但不存在“不同坐标的
最大值不能同时来自同一合法源对”的障碍。

问题比颜色竞争更基本。在这批平方终端中

\[
UV=4K,
\qquad
\nu_i=v_{q_i}(K)=v_{q_i}(U)+v_{q_i}(V)
\tag{5}
\]

（支撑素数 \(q_i\) 均为奇数）。所以 \(H_i\) 所读取的正是已经包含在原盒半径
\(\nu_i\) 中的当前块高度。把边界从 \(\nu_i\) 改成 \(\nu_i+H_i\)，是在没有
overflow-to-carrier 注入的情况下反事实地再次使用同一份高度。因而 \(B_b\) 只是
重复高度扩盒应力测试，不是真实兼容载体资源空间，\(\Psi_H\) 也不是已证明可清除的
分母残余。

## 全部单坐标下限为零

253 个冻结 F 状态共有 1181 个 \(K\)-支撑坐标。商阶分布为

\[
\begin{array}{c|rrr}
o_i&1&2&3\\ \hline
\#&1165&15&1.
\end{array}
\tag{6}
\]

其中 1173 个坐标在商掉自身后，剩余支撑已经包含目标；另外 8 个坐标虽有非零目标类，
但该类仍落在原指数界内。最终

\[
\boxed{\mu_i=0\quad\text{对全部 }1181\text{ 个坐标成立}.}
\tag{7}
\]

此前筛出的 37 个完整源谱私有代理过载坐标也全部满足商阶 1 和 \(\mu_q=0\)。所以

\[
\boxed{
37_{\text{私有代理过载}}
\quad\longrightarrow\quad
0_{\text{选择不变私有 }q\text{ 缺陷}}.}
\tag{8}
\]

这不影响既有有限选择器 \(37=35+2\) 的计算正确性，但改变了它的证据含义：该分流只
闭合确定性首见证，不能支持“真实固定私有 \(q\) 缺陷”这一前提。37 个状态都另有一个
\(q\)-free Type I 命中；其中 35 个在更小 \(R\)，两个在更大 \(R\)。

## 反事实重复高度扩盒与单位距离

对式 (3) 做精确 meet-in-the-middle 成员检查，得到

\[
\boxed{
91_{\text{hit}}+162_{\text{miss}}=253.}
\tag{9}
\]

旧的 `no_assignment_can_carry_all_excess` 分类有 165 个状态，其确定性首见证均未通过
历史重复高度比较；
其中三个状态却有另一个完整目标表示落入反事实扩展盒：

\[
(p,R)=(79312489,1571),
(214360969,11171),
(549401449,6787).
\tag{10}
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
\tag{11}
\]

最大值 \(15\) 只出现在

\[
(p,R)=(310002289,137595).
\tag{12}
\]

## 最小联合阻碍子集

对坐标集 \(J\subseteq\{1,\ldots,r\}\)，令 \(\pi_J(F)\) 为目标仿射格的坐标投影。
若

\[
\pi_J(F)\cap\prod_{i\in J}[-b_i,b_i]=\varnothing,
\tag{13}
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
\tag{14}
\]

162 个状态在最小基数层都只有一个阻碍集，且没有单坐标阻碍。37 个私有代理状态的
最小基数分布为

\[
2:7,\qquad3:4,\qquad4:13,\qquad5:11,\qquad6:2;
\tag{15}
\]

其唯一的最小基数阻碍集全部包含相应私有 \(q\)。这只说明私有 \(q\) 是反事实
\(\nu+H\) 扩盒中的联合阻碍超边成员；它从来不是独立的强制坐标，也不能据此认定为
真实分母容量的必要载体。

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
\tag{16}
\]

它与 \([-2,2]^2\) 不交，但两个单坐标投影都与 \([-2,2]\) 相交。相对扩展盒的完整
Pareto 溢出前沿为

\[
(0,3),(1,2),(2,1),(3,0).
\tag{17}
\]

因此这个例子同时满足

\[
\forall z\in F\ \exists i:\ |z_i|>b_i,
\qquad
\forall i\ \exists z\in F:\ |z_i|\le b_i,
\tag{18}
\]

却不存在

\[
\exists i\ \forall z\in F:\ |z_i|>b_i.
\]

式 (18) 是不能交换 \(\forall z\exists i\) 与 \(\exists i\forall z\) 的具体算术反例。
这个量词反例和全部有限统计仍然成立，但它们只描述目标仿射格相对反事实扩展盒的
几何：91 个 hit 不等于 91 个合法载体命中，162 个 miss 也不等于 162 个已证明的
容量不足状态。要得到容量结论，仍须构造来自新状态或外部资源的代数注入，并证明其
没有重复使用已经计入 \(K\) 的 \(q\)-进高度。

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
result-generation script sha256:
790467ce101fc6be306574ee6906f72186e34588619001a5cee717f174198157

current assertion-strengthened script sha256:
d1f059d984d077d7757e37f06863621fdcb39ad7c4579a78af85b6b7748e3a51

result sha256:
c3be0594411122823453d76f7065ce70eb83631f996b97d3a696f5119a0d5558

coordinate certificate rows sha256:
4841ddcae6c8ec710355e6214bda3498c20c1da88d9ca194078ce1b0a8095781
~~~

脚本哈希锁定三个既有输入；使用单位群离散对数、支撑商群 HNF 与已有仿射关系格做独立
交叉验证，并冻结全部统计和证书行哈希。它只运行本轮新计算，没有回跑历史素数扫描。

本主张没有证明：

- 式 (2) 的逐坐标最大高度能作为 \(K\) 之外的新增容量；同一源对同时读出只证明
  物理可见性，不证明资源可重复使用；
- 盒外指数必须逐层注入这些块高度；
- 最小阻碍超边能够在跨状态中使用同一资源坐标或共同价格；
- 162 个有限状态覆盖所有核心素数，或已经给出统一 Type I/II 选择器。

因此下一步不应继续寻找固定私有 \(q\) 缺陷，也不能把反事实扩盒中 162 个唯一阻碍集的
统计沿用到原始盒。正确对象是相对原始 \(\nu\) 的全部最小基数投影阻碍与内禀带符号
分母缺陷；原始盒中 249 个状态的最小层唯一，4 个各有两组并列阻碍。随后仍须为新状态
或外部资源构造显式 \(q\)-进注入，继而寻找跨状态共同价格、超图容量矛盾或改变 \(K\)
支撑且可提升的严格下降。
