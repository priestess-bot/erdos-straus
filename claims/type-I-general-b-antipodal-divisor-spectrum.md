---
kind: claim
claim_id: type-I-general-b-antipodal-divisor-spectrum
title: 一般 B 中心化谱的反足点除子刻画
statement: 对任意互素于R的K，令A_R(K)={d mod R:d|K}，令C_R(K)为K平方除子的中心化剩余谱，则精确有C_R(K)=A_R(K)A_R(K)^{-1}。所以一般B目标-1属于C_R(K)当且仅当A_R(K)与其负集相交。若-1已在生成子群H_R(K)中而该交集为空，则2|A_R(K)|不超过|H_R(K)|；严格超过半群大小即可强制命中。即使K=gamma L不互素，仍有A_R(K)=A_R(gamma)A_R(L)。七个完整压力谱的278个状态逐项直接复核该等价。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- general-b
- centered-spectrum
- divisor-lattice
- finite-product
- finite-exponent
- target-square-divisor
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 一般 B 中心化谱的反足点除子刻画

## 定理

设 \(\gcd(K,R)=1\)，并定义普通单边除子剩余谱

\[
\mathcal A_R(K)=\{d\bmod R:d\mid K\}. \tag{1}
\]

把一般 \(B\) 的中心化平方除子谱写为

\[
\mathcal C_R(K)=\{dK^{-1}\bmod R:d\mid K^2\}. \tag{2}
\]

则有精确积集恒等式

\[
\boxed{\mathcal C_R(K)=\mathcal A_R(K)\mathcal A_R(K)^{-1}.} \tag{3}
\]

因此

\[
\boxed{
-1\in\mathcal C_R(K)
\Longleftrightarrow
\mathcal A_R(K)\cap\bigl(-\mathcal A_R(K)\bigr)\ne\varnothing.
} \tag{4}
\]

若 \(\mathcal H_R(K)\) 是 \(K\) 的素因子残数生成的子群，且
\(-1\in\mathcal H_R(K)\) 但 (4) 的交集为空，则

\[
\boxed{2|\mathcal A_R(K)|\le|\mathcal H_R(K)|.} \tag{5}
\]

所以严格不等式 \(|\mathcal A_R(K)|>|\mathcal H_R(K)|/2\) 是一般 \(B\) 目标命中的严格充分条件。
临界等号而仍不命中时，\(\mathcal A_R(K)\) 与负集恰好分割 \(\mathcal H_R(K)\)。

此外，若 \(K=\gamma L\)，即使 \(\gcd(\gamma,L)\ne1\)，仍有

\[
\boxed{\mathcal A_R(K)=\mathcal A_R(\gamma)\mathcal A_R(L).} \tag{6}
\]

## 证明

写 \(K=\prod q^{\nu_q}\)。\(\mathcal A_R(K)\) 的指数坐标为
\(0\le e_q\le\nu_q\)，其商集坐标为

\[
e_q-f_q\in[-\nu_q,\nu_q].
\]

这正是 (2) 中 \(dK^{-1}\) 的中心化指数坐标，故得 (3)。式 (4) 是 (3) 的直接改写。
具体地，若 \(u,v\mid K\) 且 \(u\equiv-v\pmod R\)，则

\[
d=\frac{Ku}{v}
\]

是 \(K^2\) 的整数除子，且 \(dK^{-1}\equiv-1\pmod R\)。

在 (4) 的交集为空时，\(\mathcal A_R(K)\) 与 \(-\mathcal A_R(K)\) 是
\(\mathcal H_R(K)\) 的两个不交等势子集，得到 (5)。若等势集合之和已经达到
\(|\mathcal H_R(K)|\)，它们的并只能为整个子群。

最后，对每个素数 \(q\)，区间

\[
[0,\nu_q(\gamma)+\nu_q(L)]
= [0,\nu_q(\gamma)]+[0,\nu_q(L)]
\]

给出 (6)，不需要 \(\gamma,L\) 互素。

## 有限审计与范围

程序在七个完整压力谱的全部 278 个诱导模数上，分别从 \(K^2\) 的全部除子直接构造
\(\mathcal C_R(K)\)，又从 \(K\) 的全部除子构造商集 \(\mathcal A_R(K)\mathcal A_R(K)^{-1}\)，
并逐项验证 (3)、(4)。它恢复既有的 20 个命中模数，未把某个固定状态的反足点恒等式误解为
跨源存在定理。

这把 F 型障碍转化为有限积集增长问题，但不会自动解决它：现有完整谱确有
\(-1\in\mathcal H_R(K)\setminus\mathcal C_R(K)\) 的状态。下一条真正有潜力的命题应比较
同一核心素数不同源状态的 \(\mathcal A_R\) 大小、商群阶与私有指数层，而不是只证明 \(-1\)
进入生成子群。

## 复现

~~~bash
python3 reproductions/type_i_general_b_antipodal_divisor_spectrum.py
python3 -m unittest tests.test_type_i_general_b_antipodal_divisor_spectrum -v
~~~
