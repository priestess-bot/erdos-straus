---
kind: claim
claim_id: type-II-p-minus-one-jacobi-weighted-minimum-overflow-neutral-carrier-no-go
title: p-1 Type II 奇核空盒的物理权最小溢出与中性载体 no-go
statement: >-
  对空的 Type II 对称指数盒，把任意整数目标表示 z 的物理溢出权定义为
  W(z)=prod_i ell_i^((|z_i|-e_i)_+)。目标为二阶元时 W 在反足对合
  z->-z 下不变，且 W<=B 的目标表示可在逐坐标扩张
  e_i+floor(log_(ell_i)B) 内完整枚举。对 p=67369 的端点允许状态 q=21,42，
  全局最小物理权均精确为 3，最小集各只有一个反足轨道；两者都只在
  Jacobi 中性的 q 侧载体素数 3 上越界，而各自唯一负源 73 与 67 保持在预算内。
  q=21 的最小关系 A+B=664 只给出合法共享缺口 83，q=42 的最小关系
  A+B=1837 只给出 11,167，均无 Type I/II 短证书；按载体删除
  q->q/3 得到的 q=7,14 状态也分别在缺口 27,55 为空。因此最小物理溢出
  不能普遍注入负源槽，也不能仅凭局部共享缺口或删除溢出载体完成转交。
  q=42 的另一个单位计数最小轨道在缺口 59 有 Type I 证书，说明成功分支存在，
  但物理加权会选择另一个无终端轨道；空盒闭合必须增加独立的中性载体适配器。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - short-certificate-equivalence
  - type-II-p-minus-one-divisor-downset-prime-power-allocation
  - type-II-p-minus-one-jacobi-source-localization-collision-capacity
  - type-II-p-minus-one-jacobi-odd-kernel-affine-box-relay
  - type-II-symmetric-divisor-fiber-antipodal-physical-capacity-terminal
topics:
  - type-II
  - p-minus-one
  - Jacobi-character
  - odd-kernel
  - affine-box
  - weighted-overflow
  - physical-capacity
  - neutral-carrier
  - antipodal-orbit
  - constructive-no-go
  - selector
sources:
  - claim: type-II-p-minus-one-jacobi-odd-kernel-affine-box-relay
    role: exact-empty-box-and-full-integer-target-relation
  - claim: type-II-p-minus-one-jacobi-source-localization-collision-capacity
    role: negative-source-and-neutral-q-carrier-separation
  - claim: short-certificate-equivalence
    role: complete-Type-I-Type-II-divisor-test
  - reproduction: reproductions/type_ii_p_minus_one_jacobi_weighted_minimum_overflow_neutral_carrier_no_go.py
    role: exact-weight-minimum-shared-gap-and-carrier-deflation-verifier
visibility: public
last_checked: '2026-08-11'
---

# (p-1) Type II 奇核空盒的物理权最小溢出与中性载体 no-go

## 1. 盒外表示的物理权

设

\[
x=\prod_{i=1}^t\ell_i^{e_i},
\qquad e_i\ge1,
\qquad
\mathcal Z=\prod_i[-e_i,e_i]\cap\mathbb Z^t,
\tag{1}
\]

并设所有 \(\ell_i\) 都是模 \(m\) 的单位。完整整数目标纤维为

\[
\mathcal T^-_{m,x}
=\left\{z\in\mathbb Z^t:
\prod_i\ell_i^{z_i}\equiv-1\pmod m\right\}.
\tag{2}
\]

原 Type II signed box 命中集就是
\(\mathcal T^-_{m,x}\cap\mathcal Z\)。对盒外向量定义逐坐标超额

\[
c_i(z)=(|z_i|-e_i)_+
\tag{3}
\]

和乘法物理权

\[
\boxed{
W(z)=\prod_i\ell_i^{c_i(z)}.}
\tag{4}
\]

当 \(z_i>e_i\) 时，\(c_i(z)\) 是超过 \(x^2\) 中可用
\(\ell_i\)-occurrence 的层数；当 \(z_i<-e_i\) 时，它是清除形式分母所缺的
层数。因此 \(\log W(z)=\sum_i c_i(z)\log\ell_i\) 是自然的素因子加权盒外成本，
而不是把不同素数上的一个单位视为同价。

目标 \(-1\) 是二阶元，所以

\[
z\in\mathcal T^-_{m,x}
\Longrightarrow
-z\in\mathcal T^-_{m,x},
\qquad W(-z)=W(z).
\tag{5}
\]

该对合没有固定点：固定点只能是 \(z=0\)，但其像为 \(1\ne-1\pmod m\)。
所以每个权层都是反足轨道的并。

对任意 \(B\ge1\)，若 \(W(z)\le B\)，则

\[
c_i(z)\le\left\lfloor\log_{\ell_i}B\right\rfloor,
\tag{6}
\]

从而

\[
|z_i|\le e_i+\left\lfloor\log_{\ell_i}B\right\rfloor.
\tag{7}
\]

故每个有界权层都能由 (7) 的有限盒完整枚举。若原 signed box 为空，则
\(W=1\) 层为空；只要 \(-1\) 位于源生成子群，(2) 非空且 \(W\) 的全局最小值
存在。

## 2. (p=67369,q=21)：最小权全部落在中性载体

取

\[
p=67369,\qquad q=21,\qquad m=4q-1=83,
\qquad x=16863=3\cdot7\cdot11\cdot73.
\tag{8}
\]

按 \((3,7,11,73)\) 排列坐标，原预算为

\[
(e_3,e_7,e_{11},e_{73})=(1,1,1,1),
\tag{9}
\]

Jacobi 负源集为

\[
\mathcal N_{21}(67369)=\{73\}.
\tag{10}
\]

原 \(3^4=81\) 个 signed-box 向量全部不命中。盒外最小可能物理权至少为 \(3\)，
因为支撑的最小素数就是 \(3\)。而完整 \(W\le3\) 枚举恰得到

\[
z=(-2,1,0,-1),\qquad -z=(2,-1,0,1).
\tag{11}
\]

两向量都只有 \(3\) 坐标超出一层，故

\[
\boxed{\min_{z\in\mathcal T^-_{83,16863}}W(z)=3.}
\tag{12}
\]

素数 \(3\mid q\) 的 Jacobi 角色为正；负源 \(73\) 的坐标在 (11) 中只达到
边界 \(\pm1\)，没有越界。因此 (12) 的全部最小物理需求都位于
**Jacobi 中性载体**，负源需求数严格为零。

将 (11) 写成互素比值

\[
\prod_i\ell_i^{z_i}=\frac AB=\frac7{3^2\cdot73}=\frac7{657}.
\tag{13}
\]

有

\[
A+B=664=2^3\cdot83.
\tag{14}
\]

由目标同余，\(83\mid A+B\)。在 \(A+B\) 的全部除数中，满足
\(3\le h\le p-2\) 且 \(h\equiv3\pmod4\) 的只有 \(h=83\)；完整
Type I/II 除子判据在该缺口均为空。因此这个唯一最小轨道没有产生新的共享缺口终端。

## 3. (p=67369,q=42)：物理加权选择无终端轨道

再取

\[
q=42,\qquad m=167,\qquad
x=16884=2^2\cdot3^2\cdot7\cdot67.
\tag{15}
\]

按 \((2,3,7,67)\) 排列，预算为 \((2,2,1,1)\)，负源集仍只有

\[
\mathcal N_{42}(67369)=\{67\}.
\tag{16}
\]

原 signed box 为空。\(W=2\) 只能来自 \(2\) 坐标单层越界；完整检查该层仍为空。
\(W\le3\) 的目标集恰为

\[
z=(-2,3,-1,1),\qquad -z=(2,-3,1,-1).
\tag{17}
\]

故

\[
\boxed{\min_{z\in\mathcal T^-_{167,16884}}W(z)=3,}
\tag{18}
\]

且最小集仍只有一个反足轨道。越界坐标是中性载体 \(3\mid q\)，负源 \(67\)
仍只在原预算边界上。规范代表给出

\[
\frac AB=\frac{3^3\cdot67}{2^2\cdot7}
=\frac{1809}{28},
\qquad
A+B=1837=11\cdot167.
\tag{19}
\]

全部合法共享缺口为 \(11,167\)，二者均无 Type I/II 短证书。

若改用未加权成本

\[
\omega_1(z)=\sum_i(|z_i|-e_i)_+,
\tag{20}
\]

则单位层还有另一个反足轨道，代表为

\[
z'=(-2,1,2,1),\qquad W(z')=7.
\tag{21}
\]

它满足

\[
\frac{A'}{B'}=\frac{3\cdot7^2\cdot67}{2^2}
=\frac{9849}{4},
\qquad
A'+B'=9853=59\cdot167.
\tag{22}
\]

缺口 \(59\) 确有 Type I 证书

\[
(x_{59},d,y,z)
=(16857,151713,19250694,144100000454).
\tag{23}
\]

所以单位计数的两个并列轨道中，一个有替代终端，一个没有；自然物理权 (4) 又严格
选择权 \(3\) 的无终端轨道。这同时否定“任选一个最小轨道即可终止”和“物理最小轨道
必终止”两种加强。

## 4. 删除溢出载体也不构成转交

由于两张空盒的最小溢出都位于 \(3\mid q\)，最直接的重图表是

\[
q\longmapsto q/3.
\tag{24}
\]

端点允许域在整除下向下封闭，所以这两条候选分别为

\[
21\longmapsto7,\qquad42\longmapsto14.
\tag{25}
\]

对应 Type II 缺口为

\[
4\cdot7-1=27,\qquad4\cdot14-1=55.
\tag{26}
\]

完整 signed-box 和 Type I/II 除子判据给出：\(q=7\) 与 \(q=14\) 都没有 Type II
命中，缺口 \(27\) 与 \(55\) 也都没有 Type I 证书。故 (24) 虽保持端点合法性，
却不携带终端结论；它更没有自动给出 E4 解提升或 E5 良基势。

作为边界控制，原素数在独立缺口 \(31\) 有 Type I 证书

\[
(x_{31},d,y,z)
=(16850,421250,36631900,98714178844).
\tag{27}
\]

所以这里不是 Erdős--Straus 反例，而是“空盒局部最小溢出转交”机制的严格反例。

## 5. 选择器结论

以上两个状态否定三个全称候选：

1. 最小物理溢出单位必能注入 Jacobi 负源槽；
2. 每个最小溢出反足轨道的 \(A+B\) 都含有 Type I/II 终端缺口；
3. 删除承载最小溢出的 \(q\)-侧素数即可得到终端后继。

因此空盒后的容量域至少必须区分

\[
\boxed{
\text{negative-source overflow}
\quad\text{与}\quad
\text{Jacobi-neutral carrier overflow}.}
\tag{28}
\]

后一通道需要额外的 carrier-to-source/source-switch 适配器：它必须明确构造另一参数
纤维的短证书，或给出满足 E1--E5 的解可提升严格边。仅有溢出位置、最小物理权、
局部共享缺口或因子删除都不足以承担这一步。

聚焦验证：

~~~bash
python3 reproductions/type_ii_p_minus_one_jacobi_weighted_minimum_overflow_neutral_carrier_no_go.py --verify
~~~

验证器只枚举上述两个状态的有界权层、单位层、共享缺口和两条载体删除状态，并逐项
重建短证书；不运行历史范围测试。
