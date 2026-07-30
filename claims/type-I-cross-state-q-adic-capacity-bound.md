---
kind: claim
claim_id: type-I-cross-state-q-adic-capacity-bound
title: 跨状态嵌套 q 进证书的容量上界
statement: 设一组不同整数标签落在长度为 M 的区间内，每个标签带非负 q 进高度 h_s。若对每一层 k，所有高度至少 k 的标签都落在同一个模 q^k 的剩余类中，则高层状态数至多 floor(M/q^k)+1，且总高度至多 sum_{k=1}^H(floor(M/q^k)+1)<=M/(q-1)+H。该引理给出跨状态容量矛盾的精确上界，但不提供 F 证书到嵌套同余链的映射。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- cross-state
- q-adic
- capacity
- label-collision
- finite-exponent
- descent
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-label-and-factor-context
visibility: public
last_checked: '2026-07-30'
---

# 跨状态嵌套 q 进证书的容量上界

## 定理

设 \(q\) 为素数，\(I=[A,A+M]\cap\mathbb Z\) 为长度 \(M\) 的整数区间。令 \(\mathcal S\) 为
有限状态集；每个状态 \(s\) 有不同的标签 \(\ell_s\in I\) 和高度
\(h_s\in\mathbb Z_{\ge0}\)。令 \(H_0=\max_s h_s\)。假设对每个
\(1\le k\le H_0\)，存在 \(c_k\pmod{q^k}\)，使得

\[
h_s\ge k\quad\Longrightarrow\quad \ell_s\equiv c_k\pmod{q^k}.
\]

则高层状态数

\[
N_k=\#\{s:h_s\ge k\}
\]

满足

\[
\boxed{N_k\le\left\lfloor\frac{M}{q^k}\right\rfloor+1.}
\]

从而总高度满足

\[
\boxed{
\sum_{s\in\mathcal S}h_s
=\sum_{k=1}^{H_0}N_k
\le\sum_{k=1}^{H_0}\left(\left\lfloor\frac{M}{q^k}\right\rfloor+1\right)
\le\frac{M}{q-1}+H_0.}
\]

## 证明

模 \(q^k\) 的同一剩余类中的两个不同整数相差至少 \(q^k\)。长度为 \(M\) 的区间内，
这样的整数至多有 \(\lfloor M/q^k\rfloor+1\) 个，得到第一式。另一方面，整数恒等式

\[
\sum_s h_s=\sum_{k=1}^{H_0}\#\{s:h_s\ge k\}
\]

给出第二式；再用
\(\sum_{k\ge1}M/q^k=M/(q-1)\) 即得最后的粗界。证毕。

## 对统一选择器的接口

要把这条容量上界用于 F 型跨状态矛盾，至少需要建立以下三项：

1. 每个失败状态有一个唯一或可控重复度的整数标签，例如源标签或模数差标签；
2. 其规范 Fourier、关系格或加法组合证书产生明确的高度 \(h_s>0\)；
3. 同一活跃素数 \(q\) 的高层证书确实共享一条嵌套同余链，而不是各自选择不同的剩余类。

已有的标签差、模数差整除性只能说明“共享幂必须落在某个差值中”；它尚未说明所有
高层证书使用同一条链，也没有给出每个 F 状态的正高度下界。因此本卡是容量桥的
**条件性上界**，不是跨状态选择器定理。

若证书按不同的同余中心分裂，应先按中心分组，再对各组应用本卡；若标签允许重复，
必须把重复度显式乘入容量，不能直接套用不同标签的结论。

## 两两差值形式

上述“同一剩余类”假设可以由更直接的两两条件替代。若标签仍然互异，并且对任意
不同状态 \(s,t\) 有

\[
q^{\min(h_s,h_t)}\mid(\ell_s-\ell_t),
\]

则对每个 \(k\)，所有满足 \(h_s\ge k\) 的标签两两同余于 \(q^k\)，从而自动落入同一个
剩余类；因此同样有

\[
\sum_s h_s\le\frac{M}{q-1}+H_0.
\]

这正是跨状态单活跃素因子兼容性的容量版本：共同活跃素因子的最低指数必须整除标签差，
所以任意高度阈值层都受到区间装箱限制。

在线性源模数上，若所有 \(R_s\equiv3\pmod4\)，可取
\(\ell_s=(R_s-R_{\min})/4\)。于是条件

\[
q^{\min(h_s,h_t)}\mid\frac{R_s-R_t}{4}
\]

给出长度 \(M=(R_{\max}-R_{\min})/4\) 的同一容量上界。若同时有标签差和模数差两种
约束，应取较强的那一项或按两类标签分别计数；不能把两个区间的容量未经证明地相乘。

### 单活跃素因子跨模数推论

固定一个核心素数 \(p\) 和奇素数 \(q\)。设 \(\mathcal S_q\) 是一组模数两两不同的
线性 F 型状态；每个状态的单活跃素因子模型给出高度 \(e_s=v_q(K_s)\)，并且
\[
q^{\min(e_s,e_t)}\mid\frac{R_s-R_t}{4}
\qquad(s\ne t).
\]

令
\[
R_{\min}=\min_{s\in\mathcal S_q}R_s,\qquad
R_{\max}=\max_{s\in\mathcal S_q}R_s,\qquad
H_0=\max_{s\in\mathcal S_q}e_s.
\]

则
\[
\boxed{
\sum_{s\in\mathcal S_q}e_s
\le\frac{R_{\max}-R_{\min}}{4(q-1)}+H_0.}
\]

特别地，若所有这些状态都需要 \(e_s\ge e_0\)，而
\[
|\mathcal S_q|e_0>
\frac{R_{\max}-R_{\min}}{4(q-1)}+H_0,
\]
则这组状态不可能全部保持单活跃 F 型；至少有一个状态必须进入多活跃方向、G 型支撑
分支或目标命中分支。

这是现有“共同活跃幂整除模数差”必要条件的第一个全局容量后果。它仍只处理同一个
活跃 \(q\) 的单方向族，不能覆盖不同 \(q\) 之间的混合 F 障碍。

## 多活跃方向的向量容量

单方向容量可以在同一个标签坐标上同时保留多个不同素数方向。设
\(\mathcal Q\) 是有限的非空素数集；每个状态 \(s\) 有不同标签
\(\ell_s\in[A,A+M]\)，并给出非负高度向量

\[
\mathbf h_s=(h_{s,q})_{q\in\mathcal Q}.
\]

对每个 \(q\in\mathcal Q\)，令
\[
H_q=\max_s h_{s,q},
\]
并假设 \(H_q\ge1\)。若任意不同状态 \(s,t\) 和任意 \(q\in\mathcal Q\) 都满足

\[
q^{\min(h_{s,q},h_{t,q})}\mid(\ell_s-\ell_t),
\]

则对任意阈值向量
\(\mathbf k=(k_q)_{q\in\mathcal Q}\)、
\(1\le k_q\le H_q\)，令

\[
Q(\mathbf k)=\prod_{q\in\mathcal Q}q^{k_q},
\qquad
N(\mathbf k)=
\#\{s:h_{s,q}\ge k_q\ \text{对所有 }q\}.
\]

因为不同素数幂互素，满足所有阈值的任意两个标签之差都被
\(Q(\mathbf k)\) 整除。因此它们落在同一个模 \(Q(\mathbf k)\) 的剩余类中，并有

\[
\boxed{
N(\mathbf k)\le
\left\lfloor\frac{M}{Q(\mathbf k)}\right\rfloor+1.
}
\]

对向量高度的联合质量

\[
\mathfrak M_{\mathcal Q}
=
\sum_s\prod_{q\in\mathcal Q}h_{s,q},
\]

使用层析恒等式

\[
\mathfrak M_{\mathcal Q}
=
\sum_{\substack{1\le k_q\le H_q\\q\in\mathcal Q}}
N(\mathbf k)
\]

得到严格上界

\[
\boxed{
\mathfrak M_{\mathcal Q}
\le
\sum_{\mathbf k}
\left(
\left\lfloor\frac{M}{\prod_q q^{k_q}}\right\rfloor+1
\right)
\le
M\prod_{q\in\mathcal Q}\frac1{q-1}
+
\prod_{q\in\mathcal Q}H_q.
}
\]

这条不等式的含义是：若每个失败状态必须同时承担多个活跃方向的正高度，则其
“联合高度质量”不能任意跨状态重复。它把单方向的 \(M/(q-1)\) 容量替换成多方向
\(M\prod_q(q-1)^{-1}\) 的乘积容量，但只在同一标签差上同时承载这些整除约束时成立。

### 证据接口与限制

该向量容量定理仍不自动适用于当前 F 状态。还必须证明：

1. 每个状态的各 \(h_{s,q}\) 是由规范 Fourier、关系格或临界加法证书唯一确定或
   可控重复的正高度；
2. 不同方向的共享幂确实都整除同一标签差，而不是分别落在标签差和模数差两个
   不同坐标上；
3. 状态标签互异，或已对重复标签建立单独的纤维容量界。

因此，本节是多活跃跨状态容量的严格数学接口，不是对 45 个压力状态的全称应用。
当前四个对抗核心的审计显示，实际至少需要三方向版本；见
[四个真实对抗核心的 F 型活跃方向下界](type-I-linear-adversarial-core-f-active-direction-profile-600m.md)。

## 带颜色的多坐标容量

线性块刚性还会把不同素数方向拉回不同的算术坐标。下面给出一个可直接覆盖
“坐标标签差 / 同标签模数差”分流的版本。

令状态 \(s\) 带有一个不同的整数坐标向量

\[
\boldsymbol\ell_s=(\ell_{s,1},\ldots,\ell_{s,d})
\in\prod_{j=1}^d[A_j,A_j+M_j]\cap\mathbb Z^d,
\]

并把活跃素数集合分成固定颜色
\(\mathcal Q=\mathcal Q_1\sqcup\cdots\sqcup\mathcal Q_d\)。每个状态有高度
\(h_{s,q}\ge0\)。假设任意不同状态 \(s,t\) 和任意
\(q\in\mathcal Q_j\) 都满足

\[
q^{\min(h_{s,q},h_{t,q})}
\mid
(\ell_{s,j}-\ell_{t,j}).
\]

对阈值向量 \(\mathbf k=(k_q)_{q\in\mathcal Q}\) 定义

\[
Q_j(\mathbf k)=\prod_{q\in\mathcal Q_j}q^{k_q},
\qquad
N(\mathbf k)=
\#\{s:h_{s,q}\ge k_q\text{ 对所有 }q\}.
\]

则所有被计入 \(N(\mathbf k)\) 的状态，在第 \(j\) 个坐标上落入同一个
模 \(Q_j(\mathbf k)\) 的剩余类。由于坐标向量互异，

\[
\boxed{
N(\mathbf k)
\le
\prod_{j=1}^d
\left(
\left\lfloor\frac{M_j}{Q_j(\mathbf k)}\right\rfloor+1
\right).
}
\]

对联合高度质量

\[
\mathfrak M_{\mathcal Q}
=\sum_s\prod_{q\in\mathcal Q}h_{s,q},
\]

逐层求和得到

\[
\mathfrak M_{\mathcal Q}
\le
\prod_{j=1}^d
\left[
M_j\prod_{q\in\mathcal Q_j}\frac1{q-1}
+
\prod_{q\in\mathcal Q_j}H_q
\right],
\qquad H_q=\max_s h_{s,q}.
\]

空颜色的约定是两个乘积均为 \(1\)，对应因子 \(M_j+1\)。

这个版本允许把一部分活跃方向放到源标签坐标，另一部分放到模数坐标；但它要求
颜色分区在所有状态之间固定。当前线性碰撞定理只给出“对某一对状态，方向可落在
标签差或模数差”，还没有给出这种全局规范颜色。因此它是下一步证明的精确接口，而
不是已经完成的跨状态选择器。
