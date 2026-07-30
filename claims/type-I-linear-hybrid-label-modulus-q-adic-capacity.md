---
kind: claim
claim_id: type-I-linear-hybrid-label-modulus-q-adic-capacity
title: 线性载体块的标签—模数混合 q 进容量
statement: 对同一核心素数的有限线性坐标块 (t,R)，固定素数 q 并令 h=v_q(tR+1)。若不同标签块的共同 q 进幂整除标签差、同标签块的共同 q 进幂整除模数差，则高度阈值层的状态数至多为 (floor(M_t/q^k)+1)(floor(M_R/q^k)+1)，总高度至多 M_t M_R/(q^2-1)+(M_t+M_R)/(q-1)+H。线性块 gcd 刚性为这些假设提供了算术来源；该容量界仍需与每个 F 状态的对偶证书高度需求结合。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- linear-source
- q-adic
- capacity
- label-collision
- modulus-collision
- cross-state
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-linear-normal-form-context
visibility: public
last_checked: '2026-07-30'
---

# 线性载体块的标签—模数混合 \(q\) 进容量

## 定理

固定一个核心素数 \(p\)，取其有限线性状态产生的不同坐标块
\[
\mathcal X\subseteq
\bigl([A,A+M_t]\cap\mathbb Z\bigr)
\times
\bigl([B,B+M_R]\cap\mathbb Z\bigr).
\]
对 \(x=(t_x,R_x)\in\mathcal X\) 令
\[
B_x=t_xR_x+1,\qquad h_x=v_q(B_x),
\]
其中 \(q\) 为固定素数，\(H=\max_x h_x\)。假设任意不同
\(x,y\in\mathcal X\) 满足
\[
\begin{cases}
q^{\min(h_x,h_y)}\mid(t_x-t_y),&t_x\ne t_y,\\
q^{\min(h_x,h_y)}\mid(R_x-R_y),&t_x=t_y.
\end{cases}
\tag{1}
\]
令
\[
N_k=\#\{x\in\mathcal X:h_x\ge k\}.
\]
则对 \(1\le k\le H\)，有
\[
\boxed{
N_k\le
\left(\left\lfloor\frac{M_t}{q^k}\right\rfloor+1\right)
\left(\left\lfloor\frac{M_R}{q^k}\right\rfloor+1\right).
}
\tag{2}
\]
从而
\[
\boxed{
\sum_{x\in\mathcal X}h_x
\le
\frac{M_tM_R}{q^2-1}
+\frac{M_t+M_R}{q-1}
+H.
}
\tag{3}
\]

## 证明

固定 \(k\)，令 \(\mathcal X_k=\{x:h_x\ge k\}\)。由 (1)，
\(\mathcal X_k\) 中任意两个不同标签 \(t_x,t_y\) 都同余于
\(q^k\)；因此不同标签的个数至多为
\(\lfloor M_t/q^k\rfloor+1\)。在固定标签 \(t\) 的纤维内，
任意两个不同模数 \(R_x,R_y\) 也同余于 \(q^k\)，所以每个标签纤维至多有
\(\lfloor M_R/q^k\rfloor+1\) 个块。相乘得到 (2)。

层析恒等式给出
\[
\sum_xh_x=\sum_{k=1}^{H}N_k.
\]
再用
\[
\left(\left\lfloor\frac{M_t}{q^k}\right\rfloor+1\right)
\left(\left\lfloor\frac{M_R}{q^k}\right\rfloor+1\right)
\le
\frac{M_tM_R}{q^{2k}}
+\frac{M_t+M_R}{q^k}+1
\]
并求和，即得
\[
\sum_{k\ge1}\frac{M_tM_R}{q^{2k}}
=\frac{M_tM_R}{q^2-1},\qquad
\sum_{k\ge1}\frac{M_t+M_R}{q^k}
=\frac{M_t+M_R}{q-1}.
\]
证毕。

## 线性源中的算术接口

在线性源
\[
p=a+s+asR,
\]
每个坐标块 \(B(t,R)=tR+1\) 整除 \(p-t\)。因此已有的带标签块刚性给出：

- 若 \(t_x\ne t_y\)，则 \(\gcd(B_x,B_y)\mid|t_x-t_y|\)；
- 若 \(t_x=t_y\)，则
  \[
  \gcd(B(t,R_x),B(t,R_y))
  =\gcd(tR_x+1,|R_x-R_y|).
  \]

取 \(q\)-进赋值后正好得到 (1)。所以 (3) 是把标签差和模数差两类碰撞预算统一起来的
严格容量界，不需要预先为 \(q\) 指定固定颜色。

## 与 F/G 对偶证书的关系

若一个 F 型状态的规范 Fourier、关系格或临界加法证书能够证明某个载体素数
\(q\) 必须承担至少 \(h_0\) 层的 \(q\)-进高度，则一组线性 F 状态若满足
\[
|\mathcal S_q|h_0>
\frac{M_tM_R}{q^2-1}
+\frac{M_t+M_R}{q-1}
+H
\]
就不可能全部保持该证书类型；至少一个状态必须进入另一种活跃方向、目标命中或终端分支。

对已经选出的活跃素数 \(q\)，线性块分解本身给出高度优先载体
\(\max(v_q(U),v_q(V))\ge\lceil(v_q(K)+2\mathbf1_{q=2})/2\rceil\)；
当前缺口不再是单状态正高度，而是证明规范 Fourier/格证书在跨状态中重复选择同一
方向/颜色，并处理一个状态同时有多个 \(q\) 的联合质量。故本卡完成了线性算术侧的容量桥，
但尚未完成统一 Type I/II 选择器。
