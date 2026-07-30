---
kind: claim
claim_id: type-I-f-intrinsic-joint-denominator-defect-profile
title: 冻结 F 状态的内禀联合分母缺陷与最小投影阻碍剖面
statement: 对253个冻结平方终端F状态，以K的原始素因子指数nu为盒界，完整目标纤维到原始盒的L1距离Psi_0全部严格为正，分布于1至19且总和1277；最小投影阻碍维数均为2至7，249个状态在最小基数层唯一、4个状态有两组并列阻碍。每个状态保存一个最短指数见证及其符号反射，给出可复核的(d^-,d^+) Pareto点，其中d_q^-=(-z_q-nu_q)_+、d_q^+=(z_q-nu_q)_+分别是原表示与符号反射的剩余q进分母层。37个私有代理状态中，private q只在35个状态的某组最小阻碍中出现、仅在34个状态的全部最小阻碍中出现，故它不是内禀联合缺陷的普遍必要坐标。历史nu+H扩盒把已包含在K中的当前块高度再次计入，只是反事实重复使用比较，不能作为兼容容量。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-square-terminal-relation-certificate
  - type-I-f-overflow-rational-gap-denominator
  - type-I-f-selection-invariant-coordinate-and-optimistic-box-boundary
  - type-I-f-current-block-saturation-and-signed-denominator-defect
topics:
  - type-I
  - F-state
  - target-fiber
  - relation-lattice
  - denominator-defect
  - q-adic
  - Pareto
  - joint-obstruction
  - private-carrier
  - finite-certificate
  - proof-program
sources:
  - claim: type-I-f-square-terminal-relation-certificate
    role: complete-affine-target-fiber-input
  - claim: type-I-f-overflow-rational-gap-denominator
    role: signed-denominator-interpretation
  - claim: type-I-f-selection-invariant-coordinate-and-optimistic-box-boundary
    role: coordinate-floor-and-counterfactual-reuse-boundary
  - claim: type-I-f-current-block-saturation-and-signed-denominator-defect
    role: intrinsic-signed-defect-and-current-block-saturation
visibility: public
last_checked: '2026-07-30'
---

# 冻结 F 状态的内禀联合分母缺陷与最小投影阻碍剖面

## 内禀对象

对冻结平方终端状态

\[
K=\prod_{i=1}^r q_i^{\nu_i},
\qquad
F=\left\{z\in\mathbb Z^r:
\prod_iq_i^{z_i}\equiv-1\pmod R\right\},
\]

定义原始指数盒与内禀联合缺陷

\[
B_\nu=\prod_i[-\nu_i,\nu_i],
\qquad
\Psi_0(F)=\min_{z\in F}\sum_i(|z_i|-\nu_i)_+.
\tag{1}
\]

再把每个坐标的缺陷分成两个方向：

\[
d_i^-(z)=(-z_i-\nu_i)_+,
\qquad
d_i^+(z)=(z_i-\nu_i)_+.
\tag{2}
\]

于是

\[
\Psi_0(F)=\min_{z\in F}\sum_i\bigl(d_i^-(z)+d_i^+(z)\bigr).
\tag{3}
\]

若

\[
A=\prod_iq_i^{\max(z_i,0)},
\qquad
B=\prod_iq_i^{\max(-z_i,0)},
\]

则既有精确分母公式给出

\[
X_-(z)=\frac{B}{\gcd(B,K)},
\qquad
v_{q_i}(X_-(z))=d_i^-(z).
\tag{4}
\]

对符号反射 \(-z\in F\) 应用同一公式，则

\[
X_+(z)=\frac{A}{\gcd(A,K)},
\qquad
v_{q_i}(X_+(z))=d_i^+(z).
\tag{5}
\]

因此式 (2) 不是载体容量，而是目标表示在两个方向上超过当前 (K) 全部
素因子高度以后仍未清除的精确分母层。

## 精确有限算法

脚本先计算 (B_\nu) 在模 (R) 支撑群中的完整像，再以
(q_i^{\pm1}) 为单位费用生成边，从该像到目标 (-1) 做多源 BFS。任一指数向量
逐坐标夹到原始盒给出长度

\[
\sum_i(|z_i|-\nu_i)_+
\]

的路径；反向地，盒像中的起点和任一路径给出同样费用上界的目标指数向量。因此
BFS 距离与式 (1) 严格相等，而不只是搜索上界。

每个状态保存一条确定性的最短指数向量及其 (z\mapsto-z) 反射。两者的
((d^-,d^+)) 总和都等于全局最小值 \(\Psi_0\)，故均为坐标偏序下的 Pareto
极小点：若某个可实现缺陷向量严格支配其中之一，其坐标和会严格小于
\(\Psi_0\)，矛盾。这里仅认证这两个 Pareto 点，不声称枚举了完整带符号前沿。

对坐标集 (J\subseteq\{1,\ldots,r\})，脚本还判定

\[
\pi_J(F)\cap\prod_{i\in J}[-\nu_i,\nu_i]=\varnothing.
\tag{6}
\]

方法是把完整关系格基投影到 (J)，计算列 Hermite 正规形，并穷举原始投影盒
做精确格成员判定。按 \(|J|\) 递增枚举，输出首个非空维数层的全部阻碍集，
所以并列最小阻碍不会被首见证选择抹去。

## 全体 253 个状态

全部状态都满足

\[
\boxed{\Psi_0(F)>0},
\qquad
253_{\rm miss}+0_{\rm hit}=253.
\tag{7}
\]

完整直方图为

\[
\begin{array}{c|rrrrrrrrrrrrrrrrr}
\Psi_0&1&2&3&4&5&6&7&8&9&10&11&12&13&14&15&18&19\\ \hline
\#&55&29&29&27&28&10&17&15&10&3&5&5&4&7&6&2&1.
\end{array}
\tag{8}
\]

总和、均值和中位数分别为

\[
\sum_F\Psi_0=1277,
\qquad
\frac1{253}\sum_F\Psi_0=\frac{1277}{253}\approx5.0474308300,
\qquad
\operatorname{med}(\Psi_0)=4.
\tag{9}
\]

唯一的最大状态是

\[
(p,R,K)=(310002289,137595,10663691238739),
\qquad \Psi_0=19.
\tag{10}
\]

原始盒最小投影阻碍维数分布为

\[
\begin{array}{c|rrrrrr}
|J|&2&3&4&5&6&7\\ \hline
\#&42&23&65&67&49&7.
\end{array}
\tag{11}
\]

特别地，没有单坐标阻碍；这与 1181 个选择不变单坐标下限全为零一致。
249 个状态在最小基数层只有一组阻碍。其余四个状态各有两组并列最小阻碍：

\[
(p,R)=(50290249,540755),\ (148659289,155),\
(214360969,267),\ (242042089,82411).
\tag{12}
\]

## 37 个私有代理状态的量词边界

私有子集的 \(\Psi_0\) 总和为 336，均值 (336/37\approx9.0810810811)，
中位数为 8，范围为 3 至 15。其直方图为

\[
3:2,\ 4:2,\ 5:3,\ 6:2,\ 7:7,\ 8:4,\ 9:2,\
11:3,\ 12:3,\ 13:2,\ 14:4,\ 15:3.
\tag{13}
\]

最小阻碍维数分布为

\[
2:10,\qquad3:6,\qquad4:12,\qquad5:7,\qquad6:2,
\tag{14}
\]

其中 36 个状态的最小基数层唯一，一个状态有两组并列阻碍。private (q) 的正确
量词统计是

\[
\boxed{
35/37\text{ 在至少一组最小阻碍中出现},\qquad
34/37\text{ 在每一组最小阻碍中出现}.}
\tag{15}
\]

两个完全避开 private (q) 的状态为

\[
\begin{array}{c|c|c|c}
(p,R)&q_{\rm private}&\Psi_0&\text{唯一最小阻碍}\\ \hline
(366108649,33171)&4693697&12&\{5,18481\}\\
(403509649,899)&549739&5&\{3,11\}.
\end{array}
\tag{16}
\]

唯一的可选出现状态是

\[
(p,R,q_{\rm private})=(148659289,155,10608743),
\qquad \Psi_0=8,
\tag{17}
\]

其两组并列最小阻碍为

\[
\{3,181\},\qquad\{3,10608743\}.
\tag{18}
\]

所以 private (q) 可以是联合阻碍中的有用标记，但不是内禀缺陷的普遍必要坐标，
更不能单独承担全称递降的量词。

## 与反事实扩盒的对照

当前线性源的两块

\[
U=aR+1,\qquad V=sR+1
\]

在这批状态中满足 (UV=4K)，且所有 (q_i\mid K) 都是奇素数。因此脚本逐状态
核验

\[
v_{q_i}(U)+v_{q_i}(V)=\nu_i.
\tag{19}
\]

历史边界 (b_i=\nu_i+\max(v_{q_i}(U),v_{q_i}(V))) 把式 (19) 中已经包含在
\(\nu_i\) 的高度再加入一次。相对这个反事实扩盒的最小残余总和为 666，比内禀
总和少 611；其中 91 个状态在反事实盒中命中，但在原始盒中全部仍为 miss。
这 91 个命中不能解释为当前块成功清除了分母，也不能据此构造兼容载体流。

## 最小显式例

对

\[
p=214729,\quad R=43,\quad K=151\cdot15287,\quad\nu=(1,1),
\]

原始目标合同为 (z_1+z_2\equiv7\pmod {14})，故

\[
\Psi_0=5,
\qquad
J_{\min}=\{151,15287\}.
\]

脚本给出的规范最短证书为 (z=(-6,-1))，于是

\[
d^-(z)=(5,0),\quad d^+(z)=(0,0),\quad X_-=151^5.
\]

符号反射 (z=(6,1)) 给出交换后的证书

\[
d^-(z)=(0,0),\quad d^+(z)=(5,0),\quad X_+=151^5.
\]

反事实重复高度扩盒给出的距离是 3；这项差值正好展示了为什么不能继续从当前块
高度中扣减内禀分母缺陷。

## 证明边界与下一接口

本卡证明的是冻结有限样本中的精确表示层边界：原始盒缺陷全正、障碍必为联合对象，
并提供两方向分母的可复核最短证书。它没有证明：

1. 任一 (d_i^\pm) 能被另一个合法 F/G 状态清除；
2. 最小阻碍集能够规范地产生 Type I/II 短证书；
3. 存在保持解可提升的跨状态变换；
4. 某个势函数在该变换下严格下降；
5. 253 个冻结状态以外的全称结论。

下一步的正确容量接口应把非零 (d_i^\pm) 解释为外部状态必须完成的
(q_i)-进提升需求，并同时给出合法新状态、提升映射和良基下降；不能再从生成它的
同一个 (K) 或当前两块中重复扣除高度。

## 复现

唯一运行命令：

```bash
/usr/bin/time -f 'elapsed_seconds=%e max_rss_kb=%M' python reproductions/type_i_private_carrier_selection_invariant_defect.py
```

运行结果：253 个状态、1181 个坐标、253 个内禀 miss，最大
\(\Psi_0=19\)。耗时 126.54 秒，峰值内存 285068 KiB。

- 结果生成版本脚本 SHA-256：`790467ce101fc6be306574ee6906f72186e34588619001a5cee717f174198157`
- 当前脚本 SHA-256：`d1f059d984d077d7757e37f06863621fdcb39ad7c4579a78af85b6b7748e3a51`
- 结果 SHA-256：`c3be0594411122823453d76f7065ce70eb83631f996b97d3a696f5119a0d5558`
- 关系格输入 SHA-256：`53119e9aaeadac7080811782f3a3eb07f3cd6674dfb9a18776a3c5e68d108297`
- 私有状态输入 SHA-256：`7466040e4f693ff39ab5d8f53e2222c18e10f3e48d1316ff8dbf767f458448df`
- 全赋值容量输入 SHA-256：`62fb9fc0f59bb011ad39276c3cd450ee1fe93fbafba7e7fc5f3800517f0bd3c5`

当前脚本只在结果生成版本之后增加了
\((aR+1)(sR+1)=pR+1=4K\) 的显式断言，不改变任何输出字段或算法。为遵守不重复运行
已通过计算的约束，本次没有再执行 126 秒的完整程序；而是直接对冻结结果的 253 条记录
逐条核验该等式，全部通过。
