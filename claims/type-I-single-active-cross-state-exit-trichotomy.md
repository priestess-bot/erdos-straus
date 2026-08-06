---
kind: claim
claim_id: type-I-single-active-cross-state-exit-trichotomy
title: 单活跃 Fourier—载体容量的跨状态退出三分
statement: 对同一核心素数中满足单活跃循环商假设的 Type I F 状态，若其规范载体都使用同一素数 q，并满足线性块的标签差/模数差 q 进整除链，则载荷总和受标签—模数矩形容量上界控制。若需求超过该上界，则至少一个状态不能继续保持单活跃 F：要么有限指数盒已命中 Type I，要么进入 G 型支撑逃逸，要么退出单活跃循环商而进入多活跃/固定层商分支。该三分不闭合多活跃分支，也不自动产生算术递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
- type-I-linear-single-active-fourier-carrier-bridge
- type-I-linear-hybrid-label-modulus-q-adic-capacity
- type-I-representation-dual-capacity-selector-contract
topics:
- type-I
- F-state
- G-state
- single-active
- cross-state
- q-adic-capacity
- exit-trichotomy
- proof-program
sources:
- claim: type-I-linear-single-active-fourier-carrier-bridge
  role: single-active-carrier-extraction
- claim: type-I-linear-hybrid-label-modulus-q-adic-capacity
  role: label-modulus-capacity
- claim: type-I-f-g-fourier-obstruction-certificate
  role: finite-F-G-branching
visibility: public
last_checked: '2026-08-04'
---

# 单活跃 Fourier—载体容量的跨状态退出三分

## 假设

固定一个核心素数 \(p\)，考虑一组线性 Type I 状态。对状态 \(i\)，记

\[
K_i=\frac{pR_i+1}{4},\qquad R_i\equiv3\pmod8.
\]

假设该状态满足单活跃桥的全部条件：

1. \(Q_i=H_i/T_i\cong C_{2m_i}\)；
2. 同一个奇素数 \(q\) 的像生成 \(Q_i\)，其它 \(K_i\) 素因子在 \(T_i\) 中；
3. 目标像为 \(q^{m_i}T_i\)；
4. 该状态为 F 型，故 \(e_i=v_q(K_i)<m_i\)。

由单活跃 Fourier—载体桥，状态 \(i\) 有一个实际载荷

\[
\rho_i=\rho_i(t_i)>0,\qquad q^{\rho_i}\mid t_iR_i+1,
\]

其中 \(t_i\in\{s_i,a_i\}\) 是规范块标签。对同一组状态，假设块刚性已给出

\[
q^{\min(\rho_i,\rho_j)}
\mid
\begin{cases}
|t_i-t_j|,&t_i\ne t_j,\\
|R_i-R_j|,&t_i=t_j.
\end{cases}
\tag{1}
\]

令标签和模数坐标分别落在宽度 \(M_t,M_R\) 的矩形中，并先对载体块
\((t_i,R_i)\) 去重；令 \(H_q=\max_i\rho_i\)。若最大重复度为 \(\mu\)，下面两个
容量右端都应乘以 \(\mu\)。

## 容量与退出定理

则

\[
\boxed{
\sum_i\rho_i
\le
\frac{M_tM_R}{q^2-1}
+\frac{M_t+M_R}{q-1}
+H_q.}
\tag{2}
\]

特别地，若每个状态都要求 \(\rho_i\ge h_0\)，则

\[
\boxed{
|\mathcal S_q|\,h_0
\le
\frac{M_tM_R}{q^2-1}
+\frac{M_t+M_R}{q-1}
+H_q.}
\tag{3}
\]

因此一旦已证明的载荷需求违反 (2) 或 (3)，至少一个状态不能继续同时满足上述四个
单活跃 F 假设。对该状态，按失效原因得到精确退出三分：

1. **有限盒命中**：仍在同一循环商中但 \(e_i\ge m_i\)，指数 \(z=m_i\) 给出
   \(-1\in\mathcal C_{R_i}(K_i)\)，构成 Type I 短证书；
2. **支撑逃逸**：\(-1\notin H_i\)，转为 G 型分离角色；
3. **结构退出**：目标仍在 \(H_i\)，但唯一活跃素数、循环商或固定层假设失效，
   转入多活跃 Fourier、一般固定层稳定子商或目标纤维分支。

## 证明

单活跃桥给出 \(q^{\rho_i}\mid t_iR_i+1\)，而 (1) 给出任意两个载体块在其较低高度
层上的标签/模数嵌套同余。固定高度层 \(k\) 时，载荷记录至多落在

\[
\left(\left\lfloor\frac{M_t}{q^k}\right\rfloor+1\right)
\left(\left\lfloor\frac{M_R}{q^k}\right\rfloor+1\right)
\]

个矩形残类中；去重假设使每个残类至多对应一条载体记录。对每个 \(k\) 求和并使用

\[
\sum_{k\ge1}q^{-2k}=\frac1{q^2-1},
\qquad
\sum_{k\ge1}q^{-k}=\frac1{q-1},
\]

得到 (2)，从而得到 (3)。若 (2) 被违反，则至少一个状态不满足单活跃桥的输入。
若唯一活跃循环商仍成立，单活跃有限盒等价式给出 \(e_i<m_i\) 与 F 型；其逆否命题
是 \(e_i\ge m_i\) 时的 Type I 命中。否则按 \(-1\notin H_i\) 或结构假设失效分别进入
第 2、3 分支。证毕。

## 选择器意义与边界

该定理封闭了统一选择器中的一个可证明子分支：

\[
\text{单活跃 F}
\longrightarrow
\text{实际 q 进载荷}
\longrightarrow
\text{跨状态容量}
\longrightarrow
\{\text{Type I 命中},\text{G},\text{多活跃/商群}\}.
\]

它不把多活跃/商群退出自动变成合法算术后继，也不允许把不同 \(q\) 分组的容量直接
相加。因而当前全局缺口已进一步收缩为：处理第三分支，或证明第三分支中的目标纤维
缺口必触发 Type II/偶终端严格提升。
