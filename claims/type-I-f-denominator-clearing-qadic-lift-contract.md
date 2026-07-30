---
kind: claim
claim_id: type-I-f-denominator-clearing-qadic-lift-contract
title: F 状态同分母指数清除的双向 q 进必要合同
statement: 对4K=pR+1的目标纤维见证z，令A/B=prod q_i^z_i为互素分解、m_0=(A+B)/R，并定义N_-=pA+m_0、N_+=pB+m_0。对任一奇素数q，负向或正向缺陷e>0时，相应清分子恰有q进赋值nu=v_q(K)；因此，若一种修复保留原q^(nu+e)局部分母指数并试图以清分子整除它，则相对改变量除以q^nu后必须命中唯一的非零模q^e剩余类。同一全局方向中的多个素数可分别由CRT合并；z与-z是备选方向，只有明确要求同时整数化两向的构造才承担两个带标签条件。裸同余总可通过选择m_0'求解，且不适用于降低分母指数或换支撑的逃逸；本卡只是同需求分子提升分支的必要验证器，不证明合法替代、状态转移或解提升。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-f-overflow-rational-gap-denominator
  - type-I-f-current-block-saturation-and-signed-denominator-defect
topics:
  - type-I
  - F-state
  - relation-lattice
  - signed-denominator-defect
  - q-adic
  - CRT
  - descent
  - proof-program
sources:
  - claim: type-I-f-overflow-rational-gap-denominator
    role: exact-oriented-denominator-valuation
  - claim: type-I-f-current-block-saturation-and-signed-denominator-defect
    role: signed-defect-and-no-current-block-reuse
visibility: public
last_checked: '2026-07-30'
---

# F 状态同分母指数清除的双向 q 进必要合同

## 设定与双向缺陷

设

\[
4K=pR+1,
\qquad
\gcd(K,R)=1,
\qquad
K=\prod_i q_i^{\nu_i},
\]

并令目标纤维见证 \(z=(z_i)\in\mathbb Z^r\) 满足

\[
\prod_iq_i^{z_i}\equiv-1\pmod R.
\]

写成互素正整数之比

\[
A=\prod_iq_i^{(z_i)_+},
\qquad
B=\prod_iq_i^{(-z_i)_+},
\qquad
\gcd(A,B)=1.
\]

因为 \(A+B\equiv0\pmod R\)，整数

\[
m_0=\frac{A+B}{R}
\]

有定义。又因 \(A,B\) 的素因子都来自 \(K\) 且 \(\gcd(K,R)=1\)，有

\[
\gcd(m_0,A)=\gcd(m_0,B)=1.
\tag{0}
\]

两个相反方向的形式缺口分别为

\[
m_-(z)=\frac{4KA/B+1}{R}=\frac{N_-}{B},
\qquad
N_-=pA+m_0,
\tag{1}
\]

以及

\[
m_+(z)=m_-(-z)=\frac{4KB/A+1}{R}=\frac{N_+}{A},
\qquad
N_+=pB+m_0.
\tag{2}
\]

相应形式 Type I 首分母为

\[
x_-(z)=\frac{Km_0}{B},
\qquad
x_+(z)=\frac{Km_0}{A}.
\tag{3}
\]

因此定义带符号的局部分母缺陷

\[
d_q^-(z)=(-z_q-\nu_q)_+,
\qquad
d_q^+(z)=(z_q-\nu_q)_+.
\tag{4}
\]

它们分别是 \(x_-\) 与 \(x_+\) 约分分母的 \(q\)-进指数。以下提升合同只讨论
奇素数 \(q\)。在 \(q=2\) 时，形式缺口 (1)--(2) 的分子还会受到 \(4K\) 中额外
两层二因子的影响，不能把下述清分子赋值公式直接照搬过去。

## 单素数提升定理

固定奇素数 \(q=q_i\)，记 \(\nu=\nu_i=v_q(K)\)。

### 负向通道

若

\[
\beta=v_q(B)=-z_q=\nu+e,
\qquad e=d_q^-(z)>0,
\tag{5}
\]

则

\[
v_q(N_-)=\nu,
\qquad
q\nmid \frac{N_-}{q^\nu},
\qquad
q\nmid m_0pA.
\tag{6}
\]

现设修复保留负向局部分母的 \(q\)-进指数 \(\beta\)，并提议用一对整数
\((A',m_0')\) 的同向清分子

\[
N_-'=pA'+m_0'
\]

以分子整除清除 \(q^\beta=q^{\nu+e}\) 局部分母幂。无论该替代如何构造，它至少必须
满足

\[
pA'+m_0'\equiv0\pmod {q^{\nu+e}}.
\tag{7}
\]

令

\[
\Delta_-=p(A'-A)+(m_0'-m_0)=N_-'-N_-.
\]

则 (7) 等价地强制

\[
\boxed{
\Delta_-\equiv-N_-\pmod {q^{\nu+e}}
}
\tag{8}
\]

并且

\[
v_q(\Delta_-)=\nu.
\tag{9}
\]

特别地，若写 \(u_-=N_-/q^\nu\) 与 \(\delta_-=\Delta_-/q^\nu\)，则

\[
\boxed{
\delta_-\equiv-u_-\pmod {q^e},
\qquad q\nmid u_-\delta_-.
}
\tag{10}
\]

所以缺陷 \(e\) 不只是“还差 \(e\) 层高度”：候选替代必须命中一个由原见证唯一决定的
非零模 \(q^e\) 剩余类。

### 正向通道

若

\[
\alpha=v_q(A)=z_q=\nu+e,
\qquad e=d_q^+(z)>0,
\tag{11}
\]

则对反向见证 \(-z\) 交换 \(A,B\)，得到

\[
v_q(N_+)=\nu,
\qquad
q\nmid \frac{N_+}{q^\nu},
\qquad
q\nmid m_0pB.
\tag{12}
\]

因此，任何保留正向局部分母指数 \(\alpha\) 并以

\[
N_+'=pB'+m_0'
\]

分子整除清除 \(q^\alpha=q^{\nu+e}\) 局部分母幂的候选替代 \((B',m_0')\)，至少必须满足

\[
pB'+m_0'\equiv0\pmod {q^{\nu+e}}.
\tag{13}
\]

令

\[
\Delta_+=p(B'-B)+(m_0'-m_0)=N_+'-N_+.
\]

则

\[
\boxed{
\Delta_+\equiv-N_+\pmod {q^{\nu+e}},
\qquad
v_q(\Delta_+)=\nu.
}
\tag{14}
\]

写 \(u_+=N_+/q^\nu\)、\(\delta_+=\Delta_+/q^\nu\)，还得到

\[
\boxed{
\delta_+\equiv-u_+\pmod {q^e},
\qquad q\nmid u_+\delta_+.
}
\tag{15}
\]

式 (13)--(15) 是 (7)--(10) 在 \(A\leftrightarrow B\) 下的严格对称式，而不是把正向
缺陷含糊地并入负向记号。

## 证明

先证明负向通道。由

\[
RN_-=4KA+B
\]

及 \(\gcd(R,B)=\gcd(A,B)=1\)，有

\[
\gcd(N_-,B)=\gcd(4K,B).
\tag{16}
\]

由于 \(q\) 为奇素数，\(v_q(4K)=v_q(K)=\nu\)。结合
\(v_q(B)=\nu+e>\nu\)，对 (16) 取 \(q\)-进赋值得

\[
\min\{v_q(N_-),\nu+e\}=\nu,
\]

故 \(v_q(N_-)=\nu\)，即 (6)。

这里 (6) 的最后一个单位性断言也可直接看出：\(q\mid B\) 与 \(\gcd(A,B)=1\)
给出 \(q\nmid A\)；由 \(m_0R=A+B\) 及 \(q\nmid R\) 得 \(q\nmid m_0\)；而
\(pR=4K-1\equiv-1\pmod q\) 给出 \(q\nmid p\)。正向通道交换 \(A,B\) 后同理。

若候选替代在保留该局部分母指数时确实以分子整除清除 \(q^{\nu+e}\)，其清分子必须至少被
\(q^{\nu+e}\) 整除，这正是 (7)。减去 \(N_-\) 即得 (8)。再将 (8) 除以
\(q^\nu\)：因为 \(N_-/q^\nu\) 是 \(q\)-进单位且 \(e>0\)，所以

\[
\frac{\Delta_-}{q^\nu}
\equiv-\frac{N_-}{q^\nu}\not\equiv0\pmod q.
\]

这同时证明 \(q^\nu\mid\Delta_-\)、(9) 和 (10)。

对正向通道，把同一个论证应用于反向见证 \(-z\)。此时正分子与负分母互换，
即 \(A\leftrightarrow B\)，而 \(m_0=(A+B)/R\) 不变；于是 (16) 变为

\[
\gcd(N_+,A)=\gcd(4K,A).
\]

由 \(v_q(A)=\nu+e\) 得 (12)，再逐字重复差分论证即得 (13)--(15)。

## 单一全局方向的多素数 CRT 合同

令

\[
J_- =\{q\text{ 为奇素数}:d_q^-(z)>0\},
\qquad
J_+ =\{q\text{ 为奇素数}:d_q^+(z)>0\}.
\]

由于 \(A,B\) 互素，\(J_-\cap J_+=\varnothing\)。对
\(q\in J_-\) 记 \(\beta_q=v_q(B)=\nu_q+d_q^-(z)\)，对
\(q\in J_+\) 记 \(\alpha_q=v_q(A)=\nu_q+d_q^+(z)\)，并定义

\[
Q_- =\prod_{q\in J_-}q^{\beta_q},
\qquad
Q_+ =\prod_{q\in J_+}q^{\alpha_q}.
\tag{17}
\]

空乘积按 \(1\) 处理。这里必须先选定一个全局方向：

- 对见证 \(z\) 的负向表示，只需合并 \(J_-\) 上的条件，即
  \[
  \boxed{pA'+m_0'\equiv0\pmod {Q_-}}; \tag{18-}
  \]
- 对反射见证 \(-z\) 的正向表示，只需合并 \(J_+\) 上的条件，即
  \[
  \boxed{pB'+m_0'\equiv0\pmod {Q_+}}. \tag{18+}
  \]

相对于原见证，这两个备选方向分别等价于

\[
\boxed{
\begin{aligned}
p(A'-A)+(m_0'-m_0)&\equiv-N_-\pmod {Q_-},\\
p(B'-B)+(m_0'-m_0)&\equiv-N_+\pmod {Q_+}.
\end{aligned}
}
\tag{19}
\]

只有当某个构造**明确要求同一候选三元组同时整数化 \(z\) 与 \(-z\)** 时，才同时承担
(18-) 与 (18+)。即使在这种双向构造中，它们也是一个带通道标签的有序对，而不是
同一个清分子被 \(Q_-Q_+\) 整除。多个素数没有消失为一个总层数；每个
\(q^{d_q^\pm}\) 都保留由 (10) 或 (15) 指定的局部单位相位，CRT 只在选定方向内部
把互素模数上的相位打包。

裸合同 (18-) 或 (18+) 本身没有存在性阻力：固定 \(A'\) 或 \(B'\) 后，总能选择正的
\(m_0'\) 命中指定剩余类。真正的算术耦合只有在候选还须满足目标关系

\[
A'+B'=Rm_0'
\tag{20}
\]

时才出现。利用 \(pR=4K-1\)，负向与正向合同分别化为

\[
\boxed{4KA'+B'\equiv0\pmod {Q_-}},
\qquad
\boxed{A'+4KB'\equiv0\pmod {Q_+}}.
\tag{21}
\]

例如，对单个负向缺陷素数 \(q\)，若再要求 \(\gcd(A',B')=1\)，则 (21) 强制

\[
q\nmid A',
\qquad
v_q(B')=\nu.
\tag{22-}
\]

正向则对称地强制 \(q\nmid B'\) 与 \(v_q(A')=\nu\)。因此同需求分子清除并没有凭空
制造额外高度：在互素目标关系内，它会把原先的 \(\nu+e\) 次分母指数降到 \(\nu\)。
如何同时满足支撑、大小、正规形和解提升条件，仍是独立问题。

## 逻辑边界

本卡建立的是**同需求分子提升分支的必要合同**，结论严格止于 (7)、(13)、
(18\(\pm\)) 与加入目标关系后的 (21)：

1. 裸同余总有整数解；即使加入 (20) 也有显式整数族。真正尚未解决的是能否同时满足
   正性、互素性、指定素数支撑、大小界与合法正规形。
2. 即使同余有整数解，也不证明整个形式分母已经清除；其他素数、二进层以及替代后
   分母本身都可能产生额外条件。
3. 它不把候选三元组识别为合法的 F/G 状态、Type I/II 除子证书或同一核心素数的
   合法跨状态转移。
4. 它不提供从替代状态的解回升到原状态的公式，也不证明任何势函数严格下降。
5. 若候选降低原局部分母指数、删除 \(q\) 或换支撑，则不受原来的
   \(q^{\nu+e}\) 整除合同约束；必须按实际新状态重新计算缺陷并验收。
6. \(z\) 与 \(-z\) 是两个备选全局方向。除非构造另有明确理由，不得把两向合同同时
   加在一个候选上，更不得逐坐标拼接两个方向。

因此，(10)、(15) 的作用是把抽象缺陷层数升级为可检验的 \(q\)-进目标剩余类。后续
容量或递降论证若要真正清除一个缺陷，必须构造满足该剩余类的合法算术对象，并另行
证明状态合法性、证书有效性和解提升；仅比较已有块高度与 \(d_q^-+d_q^+\) 不足以
完成这一步。
