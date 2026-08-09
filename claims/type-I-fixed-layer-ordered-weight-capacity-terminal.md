---
kind: claim
claim_id: type-I-fixed-layer-ordered-weight-capacity-terminal
title: 固定层 q-primary 中间区间的有序权重容量与 Davenport 膨胀边界
statement: >-
  设 P=Stab_H(J)、L=K_X/P、Gbar=<pi(q_i)>，并以
  w_y(a)=|Jbar intersect ybar L a^{-1}| 加权残余商像。若任一符号盒大于
  |Gbar|，或过滤计数 C_{y,X} 超过由各符号盒大小和降序权重定义的
  Theta_ord，则存在同符号 P-碰撞，中心化固定层把它提升为完整短核关系偶终端；且
  Theta_ord 不超过 |P|2^r|Gbar intersect L||Jbar intersect ybar Gbar L|，从而不超过
  [K_X:P]T_J。另一方面，C_{y,X}-T_J 达到 D(K_X/P) 只强制一个坐标预算放大至
  D(K_X/P) 倍的非零 P-关系；未重新落回原指数盒时不能称为终端。严格强阈值中的 > 在
  一般 centered 商群模型中不可改为 >=：存在 C_{y,X}=[K_X:P]T_J 而原盒无非零核关系
  的无限抽象族及一个非核心算术实例。但整个一生成元边界模板与 p≡1 (mod 24) 不相容，
  因而不证明核心素数域的阈值最优。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fixed-layer-stabilizer-collision-terminal
topics:
  - type-I
  - fixed-layer
  - stabilizer
  - q-primary
  - representation
  - ordered-weight-capacity
  - Davenport
  - short-relation
  - even-terminal
  - proof-program
sources:
  - claim: type-I-fixed-layer-stabilizer-collision-terminal
    role: P-collision-fixed-layer-absorption
  - reproduction: reproductions/type_i_fixed_layer_ordered_weight_capacity_terminal.py
    role: focused-capacity-and-sharp-boundary-receipts
visibility: public
last_checked: '2026-08-09'
---

# 固定层 q-primary 中间区间的有序权重容量与 Davenport 膨胀边界

## 1. 设置与商权重

沿用固定层稳定子商的记号。设

\[
P=\operatorname{Stab}_H(J),\qquad
\bar H=H/P,\qquad
\bar J=J/P,
\tag{1}
\]

并取非平凡 q-primary 角色子群 \(X\le P^\perp\)。令

\[
K_X=X^\perp,\qquad
L=K_X/P\le\bar H,\qquad
s=|L|=[K_X:P],
\tag{2}
\]

\[
\bar G=\langle\pi(q_1),\ldots,\pi(q_r)\rangle,
\qquad g=|\bar G|.
\tag{3}
\]

对 \(a\in\bar G\) 定义目标权重

\[
\boxed{
w_y(a)=\#\{\bar j\in\bar J:\bar j a\in\bar yL\}
=|\bar J\cap\bar yLa^{-1}|.}
\tag{4}
\]

把每个指数区间按 \([0,\nu_i]\) 与 \([-\nu_i,-1]\) 分开。对符号
\(\sigma\in\{+,-\}^r\)，相应符号盒 \(B_\sigma\) 的大小是

\[
b_\sigma
=\prod_{\sigma_i=+}(\nu_i+1)
 \prod_{\sigma_i=-}\nu_i.
\tag{5}
\]

将 \(\{w_y(a):a\in\bar G\}\) 降序排列为

\[
w_{(1)}\ge\cdots\ge w_{(g)}.
\tag{6}
\]

## 2. 精确重数恒等式

写

\[
a_z=\pi(\Phi(z)),\qquad
m_\sigma(a)=\#\{z\in B_\sigma:a_z=a\},
\tag{7}
\]

并令 \(A_\sigma=\{a:m_\sigma(a)>0\}\)。因为 \(J\) 是 \(P\)-周期集且
\(P\subseteq K_X\)，对固定 \(z\)，满足

\[
j\Phi(z)\in yK_X
\tag{8}
\]

的 \(j\in J\) 恰有 \(|P|w_y(a_z)\) 个。因此

\[
\boxed{
\frac{C_{y,X}}{|P|}
=\sum_\sigma\sum_{a\in\bar G}m_\sigma(a)w_y(a).}
\tag{9}
\]

定义实际商像容量

\[
\Theta_\Phi(y,X)
=|P|\sum_\sigma\sum_{a\in A_\sigma}w_y(a).
\tag{10}
\]

逐项相减得到精确恒等式

\[
\boxed{
C_{y,X}-\Theta_\Phi(y,X)
=|P|\sum_\sigma\sum_{a\in\bar G}
w_y(a)\bigl(m_\sigma(a)-\mathbf1_{m_\sigma(a)>0}\bigr).}
\tag{11}
\]

右边严格为正，当且仅当某个被过滤计数看见的 \(a\) 在同一符号盒内有重数至少
二。权重为零处的碰撞不出现在 (11) 中，但可由 \(a_z\) 的直接去重单独发现；这种碰撞
同样已经是稳定子商碰撞终端。

## 3. 有序权重容量终端

若存在 \(\sigma\) 使 \(b_\sigma>g\)，则鸽巢原理直接给出不同
\(z,w\in B_\sigma\) 满足

\[
a_z=a_w.
\tag{12}
\]

以下设每个 \(b_\sigma\le g\)，并定义先验有序权重容量

\[
\boxed{
\Theta_{\rm ord}(y,X)
=|P|\sum_\sigma\sum_{t=1}^{b_\sigma}w_{(t)}.}
\tag{13}
\]

若不存在同符号 \(P\)-碰撞，则每个映射

\[
B_\sigma\longrightarrow\bar G,\qquad z\longmapsto a_z
\tag{14}
\]

都是单射。由 (9)，每个符号盒的贡献至多是 \(g\) 个权重中最大的
\(b_\sigma\) 个之和，故

\[
C_{y,X}\le\Theta_{\rm ord}(y,X).
\tag{15}
\]

因此得到严格终端门

\[
\boxed{
C_{y,X}>\Theta_{\rm ord}(y,X)
\quad\Longrightarrow\quad
\text{存在同符号 }P\text{-碰撞，进而存在偶终端}.}
\tag{16}
\]

终端是构造性的。取 (12) 的碰撞差 \(\delta=z-w\)，则

\[
|\delta_i|\le\nu_i,\qquad \Phi(\delta)\in P.
\tag{17}
\]

在中心化且固定、残余素支撑分离的 Type I 状态中，取固定层指数向量 \(\alpha\)
满足

\[
\Phi_N(\alpha)=\Phi(\delta)^{-1}.
\tag{18}
\]

拼接得到非零完整指数盒核关系 \(\lambda=(\alpha,\delta)\)。定向使

\[
\rho=\prod_{\ell\mid K}\ell^{\lambda_\ell}<1,
\tag{19}
\]

再令

\[
U=K\rho,\qquad E=4U,\qquad n=\frac{4K-E}{R},
\tag{20}
\]

即得到固定层稳定子碰撞引理的合法偶终端。

## 4. 对原强阈值的收紧

记

\[
d=|\bar G\cap L|,
\qquad
j_y=|\bar J\cap\bar y\bar G L|.
\tag{21}
\]

交换求和次序得

\[
\sum_{a\in\bar G}w_y(a)
=\sum_{\bar j\in\bar J}
|\bar G\cap\bar j^{-1}\bar yL|.
\tag{22}
\]

右侧每个交集为空，或为 \(\bar G\cap L\) 的陪集；它非空当且仅当
\(\bar j\in\bar y\bar G L\)。所以

\[
\boxed{
\sum_{a\in\bar G}w_y(a)=d j_y.}
\tag{23}
\]

由 (13) 和 (23)，

\[
\boxed{
\Theta_{\rm ord}(y,X)
\le |P|2^r d j_y
\le |P|2^r s|\bar J|
=sT_J.}
\tag{24}
\]

因此 (16) 可以严格早于原来的 \(C_{y,X}>sT_J\) 终端门触发。q-primary 假设
赋予该回执规范 primary 标签；(9)--(24) 的计数论证本身只使用
\(P\subseteq K_X\)。

## 5. Davenport 只产生膨胀关系

令 \(D(L)\) 是有限阿贝尔群 \(L=K_X/P\) 的 Davenport 常数。把所有过滤记录按

\[
(j,\operatorname{sgn}z)
\tag{25}
\]

分入至多 \(T_J=|J|2^r\) 个桶。在每个非空桶固定一个基点，其余记录逐一与基点
配对，至少得到

\[
M=C_{y,X}-T_J
\tag{26}
\]

个非零差向量 \(\delta_t\)，满足

\[
|\delta_{t,i}|\le\nu_i,
\qquad
\Phi(\delta_t)\in K_X.
\tag{27}
\]

交换每对端点，使每个 \(\delta_t\) 的首个非零坐标为正。若

\[
M\ge D(L),
\tag{28}
\]

则 Davenport 定义给出非空指标集 \(I\)，其中 \(|I|\le D(L)\)，且

\[
\Phi\!\left(\sum_{t\in I}\delta_t\right)\in P.
\tag{29}
\]

令 \(\lambda=\sum_{t\in I}\delta_t\)。取 \(I\) 中首个非零坐标位置最靠前的
下标 \(i\)。所有首次在 \(i\) 非零的差向量，其第 \(i\) 坐标均为正；其余差向量
在该坐标为零。因此

\[
\lambda_i>0,
\qquad
\lambda\ne0,
\qquad
|\lambda_i|\le D(L)\nu_i\quad(1\le i\le r).
\tag{30}
\]

若另行验证

\[
|\lambda_i|\le\nu_i\quad\text{对所有 }i,
\tag{31}
\]

则 (29) 可按 (17)--(20) 吸收并构造偶终端。若 (31) 失败，唯一合法输出是

```text
certificate_type = q_primary_davenport_dilated_relation
kernel_quotient = K_X/P
davenport_constant = D(K_X/P)
dilation = D(K_X/P)
relation = lambda
original_box_fit = false
recursive_edge_eligible = false
```

不能把 (30) 冒充原 \(K\) 指数盒的短关系。这里 q-primary 的群是
\(H/K_X\) 的对偶，而 Davenport 合成所在的 \(K_X/P\) 一般不是 q-群；所以
q-primary 或 Olson 型零和结论不会自动修复坐标预算。

## 6. 严格阈值的无限抽象边界族与核心排除

先在抽象 centered 商群模型中对任意奇数 \(s\ge3\) 取

\[
H=\langle g\rangle\simeq C_{2s},
\qquad J=P=\{1\}.
\tag{32}
\]

令 \(X\) 为由二次角色 \(\chi(g)=-1\) 生成的二阶角色群。则 \(X\) 是
2-primary，且

\[
K_X=L=\langle g^2\rangle,\qquad |L|=s.
\tag{33}
\]

取一个残余生成元、预算和目标

\[
r=1,\qquad \nu=2s-1,\qquad y=g^s=-1.
\tag{34}
\]

正符号盒 \([0,2s-1]\) 和负符号盒 \([-(2s-1),-1]\) 各含恰好 \(s\) 个
奇指数，故

\[
N_y=2=T_J,
\qquad
C_{y,X}=2s=sT_J.
\tag{35}
\]

两个符号盒上的 \(z\mapsto g^z\) 分别单射。另一方面，

\[
|\lambda|\le2s-1,\qquad g^\lambda=1
\tag{36}
\]

只允许 \(\lambda=0\)。所以 (35) 的强阈值等号处没有非零短核关系，原条件中的
严格不等号不能改为非严格不等号。任意由弱商关系合成的非零核指数，其绝对值至少为
\(2s>\nu\)，这也给出 Davenport 膨胀不能自动终端的严格边界。

因此一般 centered 商群模型确有一个无限边界族。取 \(s=3\) 还可得到一个数值算术嵌入：

\[
R=13,\qquad q=3527,\qquad \nu=5,\qquad
K=q^5=545792166732066407,
\tag{37}
\]

\[
p=\frac{4K-1}{13}=167936051302174279.
\tag{38}
\]

这里 \(p,q\) 都是素数，\(q\bmod13=4\) 的阶为六，且 \(q^3\equiv-1\pmod {13}\)。
过滤指数恰为

\[
\{-5,-3,-1,1,3,5\},
\tag{39}
\]

精确目标指数为 \(\{-3,3\}\)，而 \([-5,5]\) 中核指数只有零。这个嵌入的
\(p\equiv7\pmod {24}\)，所以它只证明一般算术 centered 选择器中严格不等号不可删除。

事实上，整个一生成元模板都不能进入核心素数域。若存在一个算术实现

\[
K=q^{2s-1},\qquad \operatorname{ord}_R(q)=2s,
\qquad q^s\equiv-1\pmod R,
\qquad 4K=pR+1,
\tag{40}
\]

则 \(q^{2s}\equiv1\pmod R\)。把 \(4q^{2s-1}\equiv1\pmod R\) 乘以 \(q\)，得到

\[
q\equiv4\pmod R,
\qquad
4^s\equiv-1\pmod R.
\tag{41}
\]

对每个素数 \(\ell\mid R\)，\(4\bmod\ell\) 的阶是偶数；又因 \(4\) 是平方，该阶
整除 \((\ell-1)/2\)。故 \((\ell-1)/2\) 为偶数、\(\ell\equiv1\pmod4\)，进而

\[
R\equiv1\pmod4.
\tag{42}
\]

但若 \(p\equiv1\pmod {24}\)，由 \(4K=pR+1\) 模四立刻得到
\(R\equiv3\pmod4\)，矛盾。因此 (32)--(39) 的一生成元边界不能证明核心域阈值最优；
核心域下一步必须研究多生成元、非均匀预算或利用 (42) 的改进容量门。

这项后续工作现已完成到等号边界。对每个核心图表取规范 (N=1) 分解，Jacobi
角色与 (4K\equiv1\pmod R) 给出

\[
C_{-1,X}\le
\Theta_{\rm ord}(-1,X)-2^{r-|I|}
\]

的严格余量，覆盖任意多生成元与非均匀预算。因此核心域的
\(C\ge\Theta_{\rm ord}\) 已强制偶终端；规范 \(N=1\) 容量门下的未决区已移到
该严格余量以下。见
[核心 Jacobi 符号盒的严格有序容量余量](type-I-core-jacobi-ordered-capacity-strict-slack-terminal.md)。

## 7. 三个聚焦控制的容量读数

零权重碰撞分支有一个核心算术控制。取

\[
(p,R,K)=(2089,7,3656),
\qquad K=2^3\cdot457.
\tag{43}
\]

此时 \(p\equiv1\pmod {24}\)、\(4K=pR+1\)，并取 \(J=P=K_X=\{1\}\)、
残余生成元 \((2,457)\)、预算 \((3,1)\) 与目标 \(y=2\)。非负符号盒中
\((0,0)\) 与 \((3,0)\) 都映到单位元，而该像的 \(w_y\) 为零；所以它不出现在
(11) 的 weighted surplus 中，却被直接 image-dedup 捕获。关系 \(2^3\equiv1\pmod7\)
给出

\[
E=1828,\qquad n=1828.
\tag{44}
\]

在 \((p,R,K)=(97,67,1625)\) 控制中，\(|\bar G|=22\)，权重谱由十一个
\(2\) 和十一个 \(1\) 组成，两个符号盒大小为 \(4,3\)。因此

\[
\Theta_{\rm ord}=2(4+3)=14,
\qquad
C_{y,X}=10,
\tag{45}
\]

把原强阈值 \(sT_J=198\) 收紧到十四，但该状态仍停留在严格未触发侧。

在 \((p,R,K)=(433,15,1624)\) 控制中，\(|\bar G|=4\)，而最大符号盒大小为
八，故 (12) 已直接触发。显式完整关系

\[
2\cdot7\cdot29^{-1}\equiv1\pmod {15}
\tag{46}
\]

给出

\[
E=3136,\qquad n=224.
\tag{47}
\]

聚焦复现命令为

~~~bash
python3 reproductions/type_i_fixed_layer_ordered_weight_capacity_terminal.py --verify
~~~
