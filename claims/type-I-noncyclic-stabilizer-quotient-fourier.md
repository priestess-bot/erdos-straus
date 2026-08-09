---
kind: claim
claim_id: type-I-noncyclic-stabilizer-quotient-fourier
title: 非循环固定层稳定子商的规范 Fourier 证书
statement: 对任意有限阿贝尔稳定子商 Q=直和 Z/n_iZ，固定层与残余块产生的整数表示函数 c 都有精确的群环自相关和 Parseval 能量；若目标 t 的表示数 c(t)=0 且总表示数 T>0，则非平凡角色中存在负相关至少为 T/(|Q|-1) 的角色。按负相关、角色阶和不变因子坐标字典序可规范选择该角色；该证书不要求 Q 循环，但仍只是状态内对偶证书，不能自动转成 q 进容量或递降边。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fixed-layer-stabilizer-defect-reduction
  - type-I-fixed-layer-cyclic-fourier-profile
  - type-I-fixed-layer-fourier-q-primary-projection
topics:
  - type-I
  - F-state
  - G-state
  - fixed-layer
  - stabilizer
  - noncyclic-quotient
  - finite-fourier
  - group-ring
  - parseval
  - dual-certificate
  - proof-program
sources:
  - claim: type-I-fixed-layer-stabilizer-defect-reduction
    role: exact-stabilizer-quotient-and-target-count
  - claim: type-I-fixed-layer-cyclic-fourier-profile
    role: cyclic-special-case-and-energy-ledger
  - reproduction: reproductions/noncyclic_quotient_fourier.py
    role: C2xC4-exact-control
visibility: public
last_checked: '2026-08-09'
---

# 非循环固定层稳定子商的规范 Fourier 证书

## 1. 商表示函数

固定层稳定子约化后，令

\[
Q=\bigoplus_{i=1}^{r}\mathbb Z/n_i\mathbb Z,
\; |Q|=\prod_i n_i,
\]

其中不变因子坐标已经固定。这里不要求 \(Q\) 循环。设
\(\bar J\subseteq Q\) 是无周期固定层，\(\bar S_i\subseteq Q\) 是残余块，定义

\[
c(x)=\#\{(j,s_1,\ldots,s_k):j\in\bar J,
s_i\in\bar S_i,\ j+s_1+\cdots+s_k=x\}.
\tag{1}
\]

乘法单位群经过坐标化后写成加法，不改变表示数。记

\[
T=\sum_{x\in Q}c(x),
\;
N_t=c(t).
\tag{2}
\]

若目标不在最初的生成群，应先输出 G 型商分离；以下只讨论目标已经位于当前商群
而 \(N_t=0\) 的 F 型缺失。

## 2. 非循环角色与群环自相关

对每个坐标索引
\(k=(k_1,\ldots,k_r)\in Q\)，取角色

\[
\chi_k(x)=
\exp\left(2\pi i\sum_{i=1}^{r}\frac{k_i x_i}{n_i}\right),
\;
\widehat c(k)=\sum_{x\in Q}c(x)\chi_k(x).
\tag{3}
\]

对 \(d\in Q\) 定义整数群环自相关

\[
C(d)=\sum_{x\in Q}c(x)c(x-d).
\tag{4}
\]

则对每一个角色都有精确恒等式

\[
\boxed{
|\widehat c(k)|^2=\sum_{d\in Q}C(d)\chi_k(d).}
\tag{5}
\]

所以非循环商的 Fourier 能量不需要选择一个循环生成元，也不需要把代数幅度存成
浮点数；整数向量 \(C\) 和字符索引 \(k\) 已经是可重放的群环证书。

进一步，Parseval 恒等式为

\[
\sum_{k\in Q}|\widehat c(k)|^2
 =|Q|\sum_{x\in Q}c(x)^2,
\tag{6}
\]

从而非平凡能量精确等于

\[
\boxed{
\sum_{k\ne0}|\widehat c(k)|^2
 =|Q|\sum_xc(x)^2-T^2.}
\tag{7}
\]

## 3. 目标缺失的规范负相关

有限群反演给出

\[
\sum_{k\in Q}\overline{\chi_k(t)}\widehat c(k)=|Q|c(t).
\tag{8}
\]

平凡角色项为 \(T\)。因此在 \(c(t)=0\) 时，非平凡角色满足精确的实部账本

\[
\sum_{k\ne0}
\operatorname{Re}\left(\overline{\chi_k(t)}\widehat c(k)\right)=-T.
\tag{9}
\]

若 \(T>0\)，则 \(|Q|>1\)，并存在 \(k\ne0\) 使

\[
\boxed{
-\operatorname{Re}\left(\overline{\chi_k(t)}\widehat c(k)\right)
\ge\frac{T}{|Q|-1}.}
\tag{10}
\]

令

\[
D(k)=-\operatorname{Re}\left(\overline{\chi_k(t)}\widehat c(k)\right).
\tag{11}
\]

规范字符取为先最大化 \(D(k)\)，再最小化
\(\operatorname{ord}(\chi_k)\)，最后按不变因子坐标 \(k\) 字典序取最小者。其最小
证书载荷为

```text
quotient_invariant_factors = (n_1,...,n_r)
target_coordinate = t
representation_vector = (c(x))_{x in Q}
autocorrelation_vector = (C(d))_{d in Q}
character_index = k
character_order = ord(chi_k)
twisted_real_part = -D(k)
deficit = D(k)
threshold = (T, |Q|-1)
certificate_type = noncyclic_quotient_fourier_deficit
recursive_edge_eligible = false
```

式 (10) 的分母是完整稳定子商的阶，而不是原群阶；这是固定层周期已经被约化后
才获得的精确门。

## 4. 证明

由 (3)，

\[
|\widehat c(k)|^2
=\sum_{x,y}c(x)c(y)\chi_k(x-y).
\]

令 \(d=x-y\)，内层和正是 (4)，得到 (5)。角色正交关系给出 (6)，去掉平凡字符
得到 (7)。同样的正交关系应用于目标 \(t\) 给出 (8)；若 \(c(t)=0\)，减去平凡
项 \(T\) 得 (9)。非平凡字符共有 \(|Q|-1\) 个，若所有 \(D(k)\) 都小于
\(T/(|Q|-1)\)，则 (9) 不可能成立，故 (10) 成立。有限集合上的三层排序定义了
唯一规范字符。证毕。

## 5. 与固定层和 q-primary 接口

此前的稳定子约化给出固定目标表示数的精确恒等式
\(N_J(t)=\bar N(\pi(t))\)。因此 (1)--(10) 可以直接作用于任意
\(H/P\)，不再要求商群为循环群；循环商 profile 是本卡在
\(Q=\mathbb Z/m\mathbb Z\) 时的特例。

若规范角色的阶为 \(d\)，只有 \(q\mid d\) 的 q-primary 分量才可由已有角色阶投影
提取。即便该分量存在，还必须通过整数相位、source-label SNF 和 owner 对齐门；
式 (10) 本身不产生 q-height，也不允许把角色幅度直接记为跨状态容量。

因此非循环商的合法分派是：

1. 目标命中时输出状态内 Type I/II 表示；
2. 目标缺失时输出本卡的规范 Fourier 对偶；
3. 角色通过额外整数拉回后，才交给已有 q-primary、格或 source-switch 分支；
4. 拉回失败时保留 `SOURCE_RELATION_LIFT_OBSTRUCTED` 或 `FOURIER_PHASE_OWNER_NONIDENTIFIED`，不升级为容量矛盾。

## 6. \(C_2\times C_4\) 精确控制

取

\[
Q=\mathbb Z/2\mathbb Z\times\mathbb Z/4\mathbb Z,
\;
\bar J=\{(0,0)\},
\]

以及两个残余块

\[
\bar S_1=\{(0,0),(1,0)\},
\;
\bar S_2=\{(0,0),(0,1),(0,3)\}.
\tag{12}
\]

它们的表示向量在六个点上各为 \(1\)，唯一未命中的点可取
\(t=(1,2)\)。于是

\[
T=6,
\;
\sum_xc(x)^2=6,
\;
|Q|\sum_xc(x)^2-T^2=12.
\tag{13}
\]

角色 \(k=(0,2)\) 的值为 \(\chi_k(a,b)=(-1)^b\)。它在六个表示点上的 Fourier
系数为 \(-2\)，而 \(\chi_k(1,2)=1\)，所以

\[
D(0,2)=2>\frac67.
\tag{14}
\]

复现脚本

```bash
python3 reproductions/noncyclic_quotient_fourier.py --verify
```

以高斯整数重算角色值、群环能量、非平凡 Parseval 能量、目标负相关和规范角色
排序；没有使用浮点阈值。

## 研究边界

本卡封闭的是“稳定子商不是循环群时仍能构造规范 Fourier 证书”的表示—对偶缺口。
它没有证明非平凡角色有整数 owner、q 进载体或可提升递降；跨状态容量和 E1--E5
仍是后续独立门。若商群为非循环且角色拉回失败，该失败现在至少有完整的群环和
SNF 输入，不再因为缺少循环坐标而留下未分类状态。
