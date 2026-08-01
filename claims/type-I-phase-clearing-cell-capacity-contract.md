---
kind: claim
claim_id: type-I-phase-clearing-cell-capacity-contract
title: q 进清分相位胞与跨状态容量合同
statement: 设奇素数 q 对每个状态 i 给出盒外高度 e_i>0、固定 B 清分相位 gamma_i=-A_i R_i^{-1} (mod q^e_i)，并选择整数标签 s_i 满足 s_i=gamma_i (mod q^e_i)。相位兼容关系按 gamma_i=gamma_j (mod q^min(e_i,e_j)) 将状态分成两两兼容的等价胞；同胞内 q^min(e_i,e_j) 整除 s_i-s_j。若每个胞的标签落在长度 M_c 的区间、最大重复度不超过 mu，则逐胞求和给出 sum_i e_i <= mu*sum_c(M_c/(q-1)+H_c)。若另加不同胞的模 q 首层残基互异这一假设，胞数才至多为 q-1，并可在共同长度 M 的区间下进一步压缩为 mu*(M+sum_c H_c)。该合同只把 q-adic 清分必要条件转成条件性容量上界，不证明有界标签存在、标记解非空或合法 E1--E5 递归边。
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

## 2.1 表示坐标的交叉行列式判据

因为 \(q\nmid R_iR_j\)，相位差可以完全改写为整数交叉行列式：

\[
\gamma_i-\gamma_j
\equiv
-\frac{A_iR_j-A_jR_i}{R_iR_j}
\pmod{q^{\min(e_i,e_j)}}.
\tag{3a}
\]

所以令

\[
\Delta_{ij}=A_iR_j-A_jR_i,
\qquad k_{ij}=\min(e_i,e_j),
\]

就有精确等价

\[
\boxed{
\gamma_i\equiv\gamma_j\pmod{q^{k_{ij}}}
\iff
q^{k_{ij}}\mid\Delta_{ij}.
}
\tag{3b}
\]

当 \(\Delta_{ij}\ne0\) 且 \(v_q(\Delta_{ij})<k_{ij}\) 时，

\[
\operatorname{sep}_q(i,j)=v_q(\Delta_{ij})
\]

是一个可重算的相位分离层数；它说明这两个状态不能共用高度超过
\(\operatorname{sep}_q(i,j)\) 的同一清分胞。若 \(\Delta_{ij}=0\)，则两状态的相位
中心在所有共同层完全一致。该判据把关系格/表示坐标直接接到相位胞划分，不需要
用浮点角色值或先枚举逆元代表。

## 2.2 相位胞分区

在所有 \(e_i>0\) 的状态族上，定义

\[
i\sim_q j
\iff
q^{\min(e_i,e_j)}\mid\Delta_{ij}.
\]

这是一个等价关系。传递性只需在三个状态上取
\(k=\min(e_i,e_j,e_l)\)：两条同余链都在模 \(q^k\) 上成立，故第三条也成立。
每个等价类内部的首层相位

\[
\gamma_i\pmod q
\]

都是同一个非零残基，因为 \(q\nmid A_iR_i\)。但不同等价类可能共享同一个首层残基；
因此不能仅由非零性推出胞数至多为 \(q-1\)。令 \(\mathcal C_q\) 为这些等价类的集合。
对每个胞 \(c\in\mathcal C_q\)，若其标签落在长度 \(M_c\) 的区间、重复度不超过 \(\mu\)，
令 \(H_c=\max_{i\in c}e_i\)，则

\[
\boxed{
\sum_i e_i
\le
\mu\sum_{c\in\mathcal C_q}
\left(\frac {M_c}{q-1}+H_c\right).
}
\tag{3c}
\]

若再假设不同胞的首层残基两两不同，则 \(C_q\le q-1\)；在所有胞共享长度 \(M\)
的区间时，(3c) 才可进一步推出
\[
\sum_i e_i
\le
\mu\sum_{c=1}^{C_q}\left(\frac M{q-1}+H_c\right)
\le
\mu\left(M+\sum_{c=1}^{C_q}H_c\right).
\tag{3d}
\]
式 (3c)--(3d) 仍是有界标签的条件性容量上界；它不声称相位胞本身产生标记解或递归边。

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
`reproductions/type_i_phase_clearing_cell_capacity.py` 从冻结的有理缺口结果中取四组
小回执：

- \(q=5\) 的两个不同相位标签，\(e=1,2\)，相位在模 \(5\) 上兼容；
- \(q=151\) 的两个相同标签，显式检验重复度因子；
- \(q=5\) 的一个不同首层残基不兼容相位对；
- \(q=5\) 的一个保持同首层残基、但在更高层分离的不兼容相位对。

兼容胞的容量均不超载；两个不兼容 fixture 只分别展示跨胞不共享容量账本和首层
残基碰撞。这些只是桥接合同的算术回放，不声称冻结状态已经产生可提升清分解。

复现：

```bash
python3 reproductions/type_i_phase_clearing_cell_capacity.py --verify
```

聚焦复现的 SHA-256：

```text
02e8c4d65a3c32a0ed69a9f940c655f08f248d2af231318bcc045d64156dd706  reproductions/type_i_phase_clearing_cell_capacity.py
df96187492abbd06dbc1697d5faeaeff933289af883ae79866f33a9a81edfdfb  reproductions/type-i-phase-clearing-cell-capacity-results.json
```
