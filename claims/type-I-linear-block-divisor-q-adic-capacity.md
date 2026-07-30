---
kind: claim
claim_id: type-I-linear-block-divisor-q-adic-capacity
title: 线性同标签载体块的除子型 q 进容量
statement: 固定核心素数 p 和线性块标签 t，令 B=tR+1 遍历完整线性源谱中不同模数的载体块。因 B|p-t，固定素数 q 的高度层 N_k 同时满足 N_k<=floor(M_R/q^k)+1 与 N_k<=tau((p-t)/q^k)，其中第二项仅在 q^k|p-t 时非零。因此总 q 进高度受两种容量的逐层最小值控制；该局部除子界严格强化只使用模数区间的混合容量，可用于多活跃载体的同标签分组。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- linear-source
- same-label
- divisor-lattice
- q-adic
- capacity
- carrier-vector
- cross-state
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-linear-normal-form-context
visibility: public
last_checked: '2026-07-30'
---

# 线性同标签载体块的除子型 \(q\) 进容量

## 设置

固定核心素数 \(p\equiv1\pmod {24}\) 和一个线性块标签 \(t\)。令

\[
\mathcal X_{p,t}
\subseteq
\{(t,R):p=a+s+asR\text{ 是完整线性源状态}\}
\]

是去重后的坐标对集合，令
\[
\mathcal R_{p,t}=\{R:(t,R)\in\mathcal X_{p,t}\}
\]
为其模数投影，并写

\[
B_R=tR+1,
\qquad
h_R=v_q(B_R),
\qquad
M_R=\max_{R\in\mathcal R_{p,t}}R-\min_{R\in\mathcal R_{p,t}}R.
\]

记 \(\tau(n)\) 为正除子数。

线性源恒等式给出

\[
B_R\mid p-t.
\tag{1}
\]

令

\[
N_k=\#\{R\in\mathcal R_{p,t}:h_R\ge k\},
\qquad
H=\max_{R\in\mathcal R_{p,t}}h_R.
\]

## 双重高度层容量

对任意 \(1\le k\le H\)，模数差刚性给出

\[
N_k\le\left\lfloor\frac{M_R}{q^k}\right\rfloor+1.
\tag{2}
\]

另一方面，若 \(h_R\ge k\)，则 \(q^k\mid B_R\)，由 (1) 必有
\(q^k\mid p-t\)。当 \(q^k\mid p-t\) 时，映射

\[
B_R\longmapsto \frac{B_R}{q^k}
\]

把满足 \(h_R\ge k\) 的块注入到
\[
\operatorname{Div}\!\left(\frac{p-t}{q^k}\right).
\]

因此

\[
N_k\le
\tau\!\left(\frac{p-t}{q^k}\right)
\qquad(q^k\mid p-t),
\tag{3}
\]

而 \(q^k\nmid p-t\) 时 \(N_k=0\)。合并 (2)--(3)，得到精确的逐层上界

\[
\boxed{
N_k\le
\min\!\left\{
\left\lfloor\frac{M_R}{q^k}\right\rfloor+1,\,
\tau\!\left(\frac{p-t}{q^k}\right)
\right\},
}
\tag{4}
\]

其中第二项在 \(q^k\nmid p-t\) 时按 \(0\) 解释。

由层析恒等式

\[
\sum_{R\in\mathcal R_{p,t}}h_R
=\sum_{k=1}^{H}N_k
\]

得到总高度界

\[
\boxed{
\sum_{R\in\mathcal R_{p,t}}h_R
\le
\sum_{k=1}^{v_q(p-t)}
\min\!\left\{
\left\lfloor\frac{M_R}{q^k}\right\rfloor+1,\,
\tau\!\left(\frac{p-t}{q^k}\right)
\right\}.
}
\tag{5}
\]

特别地，若一组状态都要求 \(h_R\ge h_0\)，则

\[
\boxed{
N_{h_0}\le
\min\!\left\{
\left\lfloor\frac{M_R}{q^{h_0}}\right\rfloor+1,\,
\tau\!\left(\frac{p-t}{q^{h_0}}\right)
\right\}.
}
\tag{6}
\]

## 精确除子—剩余局部容量

设模数投影落在区间
\[
I_R=[R_{\min},R_{\max}]\cap\mathbb Z.
\]
对每个 \(k\ge1\)，定义可行除子集合

\[
\mathcal D_k(p,t,q;I_R)
=
\left\{
d:
d\mid\frac{p-t}{q^k},\
q^kd\equiv1\pmod t,\
\frac{q^kd-1}{t}\in I_R
\right\}.
\tag{7}
\]

当 \(q^k\nmid p-t\) 时约定 \(\mathcal D_k=\varnothing\)。若 \(h_R\ge k\)，取
\(d=B_R/q^k\)，则 \(d\in\mathcal D_k\)，且不同 \(R\) 给出不同 \(d\)。所以有精确的

\[
\boxed{
N_k\le
\min\!\left\{
\left\lfloor\frac{R_{\max}-R_{\min}}{q^k}\right\rfloor+1,\,
|\mathcal D_k(p,t,q;I_R)|
\right\}.
}
\tag{8}
\]

层析后得到

\[
\boxed{
\sum_{R\in\mathcal R_{p,t}}h_R
\le
\sum_{k\ge1}
\min\!\left\{
\left\lfloor\frac{R_{\max}-R_{\min}}{q^k}\right\rfloor+1,\,
|\mathcal D_k(p,t,q;I_R)|
\right\},
}
\tag{9}
\]

其中只有 \(q^k\mid p-t\) 的有限层非空。该式只需要分解 \(p-t\)、枚举其除子并做一次
线性同余/区间检查；它不需要枚举 \(K^2\) 的全部平方除子，也不依赖 Fourier 角色的
选择顺序。

## 与多活跃载体的接口

对[线性多活跃 G/F 角色的载体向量提取](type-I-linear-multi-active-fourier-carrier-vector.md)
中的同标签 \(t\) 载体组，(9) 可替换混合容量界中只依赖 \(M_R\) 的粗项。它特别适合
处理以下情形：

- 多个状态共享同一活跃素数 \(q\) 和同一块标签 \(t\)；
- Fourier/格证书要求该方向达到统一高度 \(h_0\)；
- \(p-t\) 的 \(q\)-进分解和除子数明显小于模数区间宽度。

该引理不解决不同标签之间的容量，也不把 \(\tau((p-t)/q^k)\) 自动变成高度下界。
它只是把同标签载荷的可用容量精确绑定到核心素数的具体因子结构。
