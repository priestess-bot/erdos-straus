---
kind: claim
claim_id: type-I-linear-escape-divisor-stratified-recursive-source-closure
title: 线性 escape 的除子分层 D-格递归来源闭包
statement: 固定核心素数 p 与初始 D。标准 Type II 目标格 L_D(p) 精确分解为所有除子层标准来源格的互不相交并 V_D(p)=coprod_{d|D}{d}xA_d(p)。因此，对每个 d|D 分别保留 canonical D-格最大 q-进 route 的分层菜单 E_D^downarrow(p)，就完整覆盖任何仅沿 d'|d 的标准 D-格递归 source-switch 中每一步的新 primitive source；菜单大小至多 sum_{d|D}tau(d)^3 floor(log_2(2p))。严格层变换 d'<d 使 Omega(d) 严格下降，故至多发生 Omega(D) 次。该定理不允许跨层 pool 同一 q，也不把同层步骤、raw、外部 F/G 来源或未验证的 E1--E5 提升算作递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-linear-escape-canonical-d-lattice-source-menu
  - type-II-saturated-source-congruence-stabilizer-trichotomy
  - type-II-arithmetic-lift-raw-factor-fallback
topics:
- type-I
- linear-source
- escape
- Type-II
- divisor-lattice
- source-switch
- source-complete
- recursive-closure
- well-founded-descent
- shared-q
- raw-boundary
- proof-program
sources:
  - claim: type-I-linear-escape-canonical-d-lattice-source-menu
    role: per-layer-canonical-menu-and-source-completeness
  - claim: type-II-saturated-source-congruence-stabilizer-trichotomy
    role: strict-low-modulus-E1-through-E5-gate
  - claim: type-II-arithmetic-lift-raw-factor-fallback
    role: raw-is-an-external-terminal-branch
  - reproduction: reproductions/type_i_linear_escape_divisor_stratified_source_fixture.py
    role: constant-size layer-closure and raw-boundary fixture
visibility: public
last_checked: '2026-08-05'
---

# 线性 escape 的除子分层 D-格递归来源闭包

## 1. 标准层与唯一坐标

固定核心素数 \(p\) 与正整数 \(D\)。对每个 \(d\mid D\)，写

\[
\mathcal A_d(p)=
\{a:a\mid d,\ d/a\text{ 平方自由},\ 4ad<p\}.
\tag{1}
\]

把初始 \(D\) 可见的全部标准层写成

\[
\mathcal V_D(p)=
\{(d,a):d\mid D,\ a\in\mathcal A_d(p)\}.
\tag{2}
\]

另一方面，\(D\) 的一跳 Type II 目标格为

\[
\mathcal L_D(p)=
\left\{
(D',A):D'\mid D,\ A\mid D',\ D'/A\text{ 平方自由},\ 4AD'<p
\right\}.
\tag{3}
\]

于是有精确的、不交并分解

\[
\boxed{
\mathcal L_D(p)
=\mathcal V_D(p)
=\bigsqcup_{d\mid D}\{d\}\times\mathcal A_d(p).
}
\tag{4}
\]

确实，(3) 中取 \(d=D'\)、\(a=A\) 即得到 (1)，反向包含也相同。第一坐标使各层
不交。若只记录共同移位 \(s=ad\)，则

\[
s=a^2(d/a),
\tag{5}
\]

正是 \(s=A^2c\)、\(c\) 平方自由的唯一分解，其中 \(A=a,d=Ac\)。所以 (4) 不是把
不同的 Type II 参数化重复记账。

## 2. 分层 canonical 菜单

令

\[
N_{d,a}=p+4da,
\qquad
N'_{d',A}=p+4Ad'.
\tag{6}
\]

对每个当前层 \(d\mid D\)，其一个 route 的最大 \(q\)-进高度为

\[
e^{(d)}_{a,d',A,q}
=\min\{v_q(N_{d,a}),v_q(N'_{d',A})\}.
\tag{7}
\]

仅保留 \(e^{(d)}_{a,d',A,q}\ge1\)，并定义

\[
\mathcal E_D^{\downarrow}(p)=
\bigsqcup_{d\mid D}
\left\{
(d,a;d',A;q,e^{(d)}_{a,d',A,q}):
\begin{array}{l}
a\in\mathcal A_d(p),\ (d',A)\in\mathcal L_d(p),\\
q\text{ 为素数},\ e^{(d)}_{a,d',A,q}\ge1
\end{array}
\right\}.
\tag{8}
\]

把 (8) 只看作带标签的静态总表。对固定当前层和固定目标纤维

\[
d\mid D,
\qquad
f=(d',A)\in\mathcal L_d(p),
\qquad
\mathcal E_{d,f}(p)=
\{(d,a;d',A;q,e)\in\mathcal E_D^{\downarrow}(p)\},
\tag{8a}
\]

一份有效 profile 必须是 \(P\subseteq\mathcal E_{d,f}(p)\)；一条 route 对每个
\(q\) 只存一个最大高度，并至多选择其一个前缀。重复 \(q\) 的 shared-q ledger、CRT、
单位群和整数回译只在这一对 \((d,f)\) 内运行。特别地，(8) 不是把不同 \(d\) 的同一
\(q\)，或同一 \(d\) 的不同目标纤维，拼成一个更高的整数幂块或群论容量。

每层的 canonical 菜单界给出

\[
\begin{aligned}
|\mathcal E_D^{\downarrow}(p)|
&\le
\left(\sum_{d\mid D}\tau(d)^3\right)
\lfloor\log_2(2p)\rfloor\\
&=
\prod_{r^\alpha\Vert D}
\left(\frac{(\alpha+1)(\alpha+2)}2\right)^2
\lfloor\log_2(2p)\rfloor\\
&\le\tau(D)^4\lfloor\log_2(2p)\rfloor.
\end{aligned}
\tag{9}
\]

这里 \(4ad<p\) 蕴含 \(N_{d,a}<2p\)，故每个来源—目标对至多贡献
\(\lfloor\log_2(2p)\rfloor) 个不同素数；第二行只用了
\(\sum_{j=0}^{\alpha}(j+1)^3=((\alpha+1)(\alpha+2)/2)^2\)。

## 3. 递归来源完备性与层 DAG

考虑声明的标准递归 policy。第 \(r\) 步先固定当前层、目标纤维和候选 profile：

\[
a_r\in\mathcal A_{d_r}(p),
\qquad
f_r=(d_{r+1},A_{r+1})\in\mathcal L_{d_r}(p),
\qquad
P_r\subseteq\mathcal E_{d_r,f_r}(p),
\tag{10}
\]

仅当 \(P_r\) 通过该纤维自己的 shared-q ledger、CRT、范围、来源语义、正规形和标记
提升门，并产出一个实际因子积 \(h_r>1\) 满足既有 source-switch 合同的整数条件

\[
h_r\mid p+4d_ra_r,
\qquad
h_r\mid p+4A_{r+1}d_{r+1},
\qquad
h_r\equiv-1\pmod {4d_{r+1}},
\tag{10a}
\]

时，才接受这条非终端边，并定义 \(a_{r+1}=A_{r+1}\)。因此仅有 (10) 时，\(f_r\)
只是静态候选，而不是已经发生的递归边。由 (4)，

\[
(d_{r+1},A_{r+1})\in\mathcal L_{d_r}(p)
\Longrightarrow
A_{r+1}\in\mathcal A_{d_{r+1}}(p).
\tag{11}
\]

所以每个已接受目标的参数本身就是下一层的标准来源。由 \(d_0=D\)、已接受边的
\(d_{r+1}\mid d_r\) 与 \(a_{r+1}=A_{r+1}\) 归纳得到 \(d_r\mid D\)；再对每一层调用
canonical D-格菜单的 source-completeness，得到

\[
\boxed{
\text{任何已接受非终端路径上的真实 primitive source row 都出现于 }
\mathcal E_D^{\downarrow}(p).
}
\tag{12}
\]

这关闭的是“沿已声明除子 policy 的新来源尚未枚举”缺口，而不是断言静态总表的每一行
都能通过整数门或产生递归边。

对一条已接受且层真正改变的边，

\[
d_{r+1}<d_r
\Longrightarrow
\Omega(d_{r+1})\le\Omega(d_r)-1.
\tag{13}
\]

故严格层变换至多发生 \(\Omega(D)\) 次，任何有向环都必须完全停留在某一固定 \(d\)-层。
同层 Type II 命中仍是直接终端；同层 miss 没有由 (13) 支付的下降。只有已经通过稳定子
吸收、低层参数纤维、标记提升和 E1--E5 门的严格层边，才可以把 (13) 接到已有的
算术良基势中。

## 4. 固定层残余的最低层来源

取

\[
p=57{,}399{,}241,
\qquad D=41,
\qquad R=59.
\tag{14}
\]

根层来源仅为

\[
\mathcal A_{41}(p)=\{1,41\},
\tag{15}
\]

且其已知来源素因子在模 \(59\) 下都位于二次剩余陪集。可是

\[
(1,1)\in\mathcal L_{41}(p)=\mathcal V_{41}(p),
\qquad
p+4=5\cdot11{,}479{,}849,
\qquad
11{,}479{,}849\equiv42\pmod {59},
\tag{16}
\]

其中 \(11{,}479{,}849\) 为素数，且是二次非剩余。它不是根层 \(d=41\) 的来源，却是
最低层 \(1\in\mathcal A_1(p)\) 的标准来源；(8) 因而将该低层来源枚举，而固定层菜单
不会。但是这里尚未构造一条 \(41\to1\) 的实际边：两条根来源与 \(p+4\) 的公因子均为
\(5\equiv1\pmod4\)，不满足 (10a) 的末个门。故它只说明“若已由独立机制到达
\(d=1\)，则有一个新来源”，不消耗已验证的下降步，也不提供相位到整数纤维或 E1--E5
的桥。

## 5. 不能纳入闭包的分支

raw Type II 是独立终端分支，不能伪装为 (10) 的反向层边。已经在

\[
p=73,
\qquad D_0=1,
\qquad a_0=8,
\qquad h=15,
\qquad (A,C,K)=(2,2,1)
\tag{17}
\]

中有来自闭包外代表的 raw 证书：\(15\mid73+4a_0=105\)，其对应
\(B=(Kp+A)/h=5\ge A\)，而 Type II 基础参数为 \(AC=4\not\mid D_0\)。也就是说，
若把该外部 raw 行误作下一层来源，就会从 \(D_0=1\) 人为跳到 \(4\)，破坏 (13)。外部
F/G alternate 以及未通过整数/标记提升门的 Fourier、SNF 回执同样不属于本卡的 finite
closure。

常数规模复现见
[除子分层来源闭包 fixture](../reproductions/type_i_linear_escape_divisor_stratified_source_fixture.py)。
