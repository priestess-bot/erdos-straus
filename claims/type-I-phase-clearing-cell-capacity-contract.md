---
kind: claim
claim_id: type-I-phase-clearing-cell-capacity-contract
title: q 进清分相位胞与跨状态容量合同
statement: 设奇素数 q 对每个状态 i 给出盒外高度 e_i>0、固定 B 清分相位 gamma_i=-A_i R_i^{-1} (mod q^e_i)，并选择整数标签 s_i 满足 s_i=gamma_i (mod q^e_i)。若同一相位胞内任意 i,j 满足 gamma_i=gamma_j (mod q^min(e_i,e_j))，则 q^min(e_i,e_j) 整除 s_i-s_j；若标签落在长度 M 的区间、最大重复度不超过 mu，则 sum_i e_i <= mu*(M/(q-1)+H)，H=max e_i。该合同只把 q-adic 清分必要条件转成条件性容量上界，不证明有界标签存在、标记解非空或合法 E1--E5 递归边。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-f-denominator-clearing-qadic-lift-contract
  - type-I-f-qadic-numerator-lift-rigidity-and-gcd-reduction
  - type-I-cross-state-q-adic-capacity-bound
topics:
  - type-I
  - F-state
  - q-adic
  - phase-clearing
  - capacity
  - cross-state
  - signed-carrier
  - proof-boundary
sources:
  - claim: type-I-f-denominator-clearing-qadic-lift-contract
    role: exact-fixed-B-phase
  - claim: type-I-f-qadic-numerator-lift-rigidity-and-gcd-reduction
    role: numerator-lift-rigidity
  - claim: type-I-cross-state-q-adic-capacity-bound
    role: nested-capacity
visibility: public
last_checked: '2026-08-01'
---

# \(q\) 进清分相位胞与跨状态容量合同

## 1. 设定

固定一个奇素数 \(q\)。对每个状态 \(i\)，设其目标见证在固定 \(B_i\) 的负向通道中
有一个正的盒外高度

\[
e_i>0,
\qquad v_q(B_i)=v_q(K_i)+e_i.
\]

令 \(A_i,R_i\) 是相应的固定分子和图表模数，并假设

\[
q\nmid A_iR_i.
\]

固定 \(B_i\) 的所有目标关系保持移位写成

\[
A_i(s)=A_i+R_i s,
\qquad m_i(s)=m_{0,i}+s.
\]

精确清分条件是

\[
q^{e_i}\mid A_i+R_i s_i,
\]

所以定义相位中心

\[
\gamma_i\equiv-A_iR_i^{-1}\pmod{q^{e_i}}.
\tag{1}
\]

任何保留该固定 \(B_i\) 局部结构的清分候选都必须满足

\[
s_i\equiv\gamma_i\pmod{q^{e_i}}.
\tag{2}
\]

式 (1)--(2) 是已有 \(q\) 进 numerator-lift 合同的精确相位形式；它不是把
角色阶或 Fourier 分母当作实际载体高度。

## 2. 相位兼容胞

称一组状态为同一个 \(q\)-进相位胞，如果对任意 \(i,j\) 都有

\[
\gamma_i\equiv\gamma_j
\pmod{q^{\min(e_i,e_j)}}.
\tag{3}
\]

若 \(s_i,s_j\) 分别满足 (2)，则相减得到

\[
s_i-s_j
\equiv
\gamma_i-\gamma_j
\equiv0
\pmod{q^{\min(e_i,e_j)}}.
\tag{4}
\]

因此相位胞恰好提供现有跨状态容量引理所需的嵌套同余链。注意 (3) 是额外的
跨状态假设；单个状态的 q 进刚性不自动产生它。

## 3. 容量结论

设相位胞中的标签 \(s_i\) 两两不同且落在长度为 \(M\) 的整数区间内。令

\[
H=\max_i e_i.
\]

对每个 \(k\le H\)，所有 \(e_i\ge k\) 的标签由 (4) 两两同余于同一个模
\(q^k\) 的剩余类。因此

\[
\#\{i:e_i\ge k\}
\le\left\lfloor\frac M{q^k}\right\rfloor+1.
\]

层析求和给出

\[
\boxed{
\sum_i e_i
\le
\sum_{k=1}^{H}
\left(\left\lfloor\frac M{q^k}\right\rfloor+1\right)
\le\frac M{q-1}+H.
}
\tag{5}
\]

若标签允许重复，令每个整数标签的重复度不超过 \(\mu\)，同样的装箱论证给出

\[
\boxed{
\sum_i e_i
\le
\mu\left(\frac M{q-1}+H\right).
}
\tag{6}
\]

更精确地，可以按标签纤维分别计数；不能在重复标签时直接使用 (5)。

## 4. 选择器接口

该合同为表示—对偶—容量链补上一个严格但条件性的中间接口：

\[
\text{q 进清分相位}
\longrightarrow
\text{相位兼容胞}
\longrightarrow
\text{嵌套标签容量}.
\]

要把它升级为 F/G 状态的跨状态递降，仍必须另行证明：

1. 每个未闭合状态确实产生一个非零 \(e_i\) 和一个可重算的清分相位；
2. 这些状态可以分成有限个相位胞，且每个胞有统一的有界标签区间；
3. 标签对应的候选保持正性、互素性、目标关系和完整标记集；
4. 由容量超载得到的是直接 Type I/II，或一个满足 E1--E5 的可提升后继。

没有第 2 项时，(5)--(6) 不能使用；没有第 3--4 项时，容量超载也不能称为递归证明。
相位胞合同因此保留 `analysis_evidence` / `candidate_transition` 边界，不能单独
设置 `recursive_edge_eligible=true`。

## 5. 聚焦冻结回执

新增验证器
`reproductions/type_i_phase_clearing_cell_capacity.py` 从冻结的有理缺口结果中取三组
小回执：

- \(q=5\) 的两个不同相位标签，\(e=1,2\)，相位在模 \(5\) 上兼容；
- \(q=151\) 的两个相同标签，显式检验重复度因子；
- \(q=5\) 的一个不兼容相位对，明确不套用容量界。

前两组的容量不超载，后一组状态为 `phase_incompatible`。这些只是桥接合同的
算术回放，不声称冻结状态已经产生可提升清分解。

复现：

```bash
python3 reproductions/type_i_phase_clearing_cell_capacity.py --verify
```

聚焦复现的 SHA-256：

```text
c62a706cb343396b0128e4f854f964bfe67d60e0092e843528bcea4d4187c5a6  reproductions/type_i_phase_clearing_cell_capacity.py
f4b204018d38f669ee85603a68fd560ea31e3565ec272755a05d6b51ca0220e2  reproductions/type-i-phase-clearing-cell-capacity-results.json
```
