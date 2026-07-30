---
kind: claim
claim_id: type-I-linear-high-carrier-pair-capacity
title: 线性多活跃状态的高度优先配对载体容量
statement: 对线性状态 p=a+s+asR，若一个已选内部证书的活跃方向集合 Q 至少有三个素数，则为每个 q 选择 U=sR+1、V=aR+1 中 q 进高度较大的载体块后，至少有一对方向落在同一块；该对的联合高度至少为各自总指数的一半的向上取整之积。随后可调用同一块的精确除子—剩余容量。该结论是条件性的证书—容量接口，不证明规范 Fourier 证书必有三个活跃方向。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- linear-source
- finite-fourier
- relation-lattice
- multi-active
- carrier-vector
- q-adic
- capacity
- cross-state
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-linear-normal-form-context
visibility: public
last_checked: '2026-07-30'
---

# 线性多活跃状态的高度优先配对载体容量

## 设置

固定线性状态

\[
p=a+s+asR,\qquad s\ {\text{odd}},\qquad R\equiv3\pmod4,
\]

并令

\[
K=\frac{pR+1}{4},\qquad U=sR+1,\qquad V=aR+1,
\qquad UV=4K.
\]

设 \(Q\) 是一个已选的内部 Fourier、关系格或加法组合证书的活跃素数支撑。
外部 G 型分离角色在 \(H=\mathcal H_R(K)\) 上恒等，不属于本引理。

对 \(q\in Q\) 定义高度优先载体标签

\[
t(q)=\operatorname*{argmax}_{t\in\{s,a\}}v_q(tR+1),
\]

平手时固定取 \(s\prec a\)，并记

\[
h_q=v_q(t(q)R+1).
\]

由于 \(UV=4K\)，有

\[
v_q(U)+v_q(V)=
\begin{cases}
v_q(K),&q\ne2,\\
v_2(K)+2,&q=2.
\end{cases}
\]

所以

\[
\boxed{
h_q\ge
\left\lceil\frac{v_q(K)+2\mathbf1_{q=2}}2\right\rceil.
}
\tag{1}
\]

## 高度优先配对

若 \(|Q|\ge3\)，而 \(t(q)\) 只有两个取值，则鸽巢原理给出不同的
\(q_1,q_2\in Q\) 满足

\[
t(q_1)=t(q_2)=t.
\]

令 \(B_t=tR+1\)。则

\[
q_1^{h_{q_1}}q_2^{h_{q_2}}\mid B_t,
\]

且由 (1) 得到严格的联合高度下界

\[
\boxed{
h_{q_1}h_{q_2}
\ge
\left\lceil\frac{v_{q_1}(K)+2\mathbf1_{q_1=2}}2\right\rceil
\left\lceil\frac{v_{q_2}(K)+2\mathbf1_{q_2=2}}2\right\rceil.
}
\tag{2}
\]

这里的配对与任意“先取一个块中出现的两个方向”不同：每个方向先被放到其最高
\(q\)-进载体，再进行鸽巢配对。因此 (2) 不会因选到低高度块而丢失下界。

## 算术容量接口

固定 \(p,t,q_1,q_2\) 和模数窗口 \(I\)。具有该高度优先配对的状态必满足

\[
q_1q_2\mid tR+1\mid p-t.
\]

其状态数由精确除子—剩余集合
\[
\mathcal D_{q_1,q_2}(p,t;I)
\]
控制；联合高度层由
\(\mathcal D_{q_1^k,q_2^\ell}(p,t;I)\) 控制。因此，若一组状态的下界需求超过该窗口
的联合高度容量，则至少有一个状态不能同时保持该证书支撑和线性状态。

该结论与[线性多活跃状态的配对载体与除子型 q 进容量](type-I-linear-multi-active-pair-divisor-capacity.md)
相接；后者给出精确层析和容量计算，本卡只强化每个状态的联合需求下界。

## 证明边界

本卡的逻辑链是

\[
\text{内部证书支撑至少三方向}
\Longrightarrow
\text{高度优先同块配对}
\Longrightarrow
\text{联合载体高度下界}
\Longrightarrow
\text{精确除子—剩余容量}.
\]

它不证明：

1. F 型状态一定存在支撑至少三方向的规范角色；
2. 不同状态会选择同一个 \((q_1,q_2,t)\) 分组；
3. 有限审计中稳定子活跃方向可以直接替代 Fourier/格证书支撑。

因此它是统一选择器的一个严格条件性桥梁；要得到全称选择器，还需证明相位质量
迫使足够多状态进入同一支撑—颜色分组，或者从剩余分支构造可提升算术下降。

## 冻结审计

对四个冻结对抗核心的 45 个有限指数状态，用稳定子活跃方向作诊断输入，逐状态选择
高度优先配对并计算精确窗口容量。复现脚本为

```text
reproductions/type_i_linear_high_carrier_pair_capacity.py
```

该输出只用于检验这条强化接口在真实压力数据上的数量级，不升级为全称证据。
