---
kind: claim
claim_id: type-I-fourier-qprimary-phase-lift-capacity-dichotomy
title: Fourier q-primary 相位到算术载体的有限提升—容量二分
statement: 对每个固定层约化后的 F 型状态，若目标 tau=pi(-1) 属于残余指数映射的像，则规范角色的任意 q-primary 分量都给出一个良定义的无界目标预像相位 gamma_i (mod q^{e_i})。若外部算术选择器提供满足该相位同余的有界整数载体标签，则所有状态的 q-height 需求满足相位树容量上界；若有限候选标签表没有这样的局部或联合提升，则输出可验证的 FOURIER_PHASE_NO_LOCAL_LIFT 或 FOURIER_PHASE_ASSIGNMENT_DEFICIT。Fourier 分母本身不等于 q 进高度，因而本二分不声称全称载体存在或递降闭合。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-f-g-fourier-obstruction-certificate
  - type-I-fixed-layer-stabilizer-defect-reduction
  - type-I-f-target-involution-fourier-phase-collapse
  - type-I-phase-clearing-cell-capacity-contract
  - type-I-linear-hybrid-label-modulus-q-adic-capacity
topics:
  - type-I
  - F-state
  - fixed-layer
  - finite-fourier
  - q-primary
  - phase-lift
  - carrier
  - capacity
  - Hall
  - proof-program
sources:
  - claim: type-I-f-g-fourier-obstruction-certificate
    role: canonical-Fourier-character
  - claim: type-I-fixed-layer-stabilizer-defect-reduction
    role: quotient-character
  - claim: type-I-phase-clearing-cell-capacity-contract
    role: q-adic-capacity-template
visibility: public
last_checked: '2026-08-07'
---

# Fourier q-primary 相位到算术载体的有限提升—容量二分

## 1. 输入与 q-primary 投影

考虑一个已经完成固定层稳定子约化的 F 型状态 \(i\)。记商群为

\[
\bar H_i=H_i/P_i,
\qquad
\bar\phi_i:\mathbb Z^{r_i}\longrightarrow \bar H_i,
\qquad
\Lambda_i=\ker\bar\phi_i,
\]

并在 \(\pi_i(-1)\in\operatorname{im}\bar\phi_i\) 时取满足
\(\bar\phi_i(z_i^0)=\pi_i(-1)\) 的一个**无界群论预像** \(z_i^0\)。F 型的有界目标
纤维是空的，故这里不能把 \(z_i^0\) 称为盒内目标表示。规范 Fourier 证书给出一个非平凡角色

\[
\bar\chi_i(\bar\phi_i(z))
 =\exp\!\left(2\pi\mathrm i\,\langle a_i,z\rangle/d_i\right),
\qquad d_i=\operatorname{ord}(\bar\chi_i).
\tag{1}
\]

固定一个素数 \(q\mid d_i\)，写

\[
d_i=q^{e_i}d_i',
\qquad (q,d_i')=1,
\qquad e_i=v_q(d_i)>0.
\tag{2}
\]

角色的 q-primary 分量是 \(\bar\chi_i^{\,d_i'}\)。取

\[
b_i\equiv a_i\pmod {q^{e_i}},
\qquad
\gamma_i\equiv\langle b_i,z_i^0\rangle\pmod {q^{e_i}}.
\tag{3}
\]

这里的 \(b_i\) 对应于
\[
\bar\chi_i^{\,d_i'}(\bar\phi_i(z))
=\exp(2\pi\mathrm i\langle b_i,z\rangle/q^{e_i});
\]
若要选取 CRT 意义下的另一标准 q-primary 因子，只会把 \(b_i\) 乘以一个模
\(q^{e_i}\) 的单位，不改变下面的相位树论证。

因为 \(\bar\chi_i\) 在商群上良定义，所以对关系基矩阵 \(L_i\) 有

\[
L_i a_i\equiv0\pmod {d_i}
\quad\Longrightarrow\quad
L_i b_i\equiv0\pmod {q^{e_i}}.
\tag{4}
\]

因此

\[
\Gamma_i(z):=\langle b_i,z\rangle\pmod {q^{e_i}}
\tag{5}
\]

是 \(\mathbb Z^{r_i}/\Lambda_i\) 上的良定义 q-primary 相位，且任意
目标纤维代表 \(z_i^0+\lambda\) 都给出同一个 \(\gamma_i\)。由于
\(\bar\chi_i^{d_i'}\) 的阶正好为 \(q^{e_i}\)，向量 \(b_i\) 不会全部被 \(q\) 整除；这
避免把一个实际较低阶的相位错误记录成高度 \(e_i\)。

这一步是 Fourier 到算术侧唯一不需要额外假设的部分：它只使用角色的有限阶和关系格。

## 2. 什么叫 phase lift

算术源选择器为状态 \(i\) 指定一个候选标签集

\[
\mathcal S_i(q)\subset\mathbb Z.
\tag{6}
\]

标签可以是线性源中的 \(s\) 或 \(a\)，也可以是固定 \(B\) 清分后的整数标签；关键是
标签定义必须在选择器中先行固定，不能为了满足 (3) 临时改写。称
\(s_i\in\mathcal S_i(q)\) 是一个 q-primary **phase lift**，若

\[
s_i\equiv\gamma_i\pmod {q^{e_i}}.
\tag{7}
\]

若标签还需落在共同区间 \(I=[L,L+M]\cap\mathbb Z\)，则把 (7) 与
\(s_i\in I\) 一并作为局部提升条件。多个状态允许共享同一标签时，记录最大重复度
\(\mu\)；\(\mu=1\) 是通常的标签唯一情形。

注意 (7) 是新的算术输入，不是 (1) 的推论。它必须由线性块整除、固定-B 清分恒等式
或其它已证明的 source map 独立验证。

## 3. 相位树容量定理

设有限状态族 \(\mathcal I\) 已给出 q-primary 数据
\((e_i,\gamma_i)\)，并且每个状态都有一个 phase lift \(s_i\in I\)。令

\[
 D_k=\#\{\gamma_i\bmod q^k: i\in\mathcal I,\ e_i\ge k\},
 \qquad
 H=\max_i e_i.
\tag{8}
\]

则对每个 \(k\ge1\)，相同标签的状态只能占用一个模 \(q^k\) 的相位残类，而长度
为 \(M\) 的区间中每个残类至多有
\(\lfloor M/q^k\rfloor+1\) 个整数。因此

\[
 N_k:=\#\{i:e_i\ge k\}
 \le
 \mu D_k\left(\left\lfloor\frac{M}{q^k}\right\rfloor+1\right).
\tag{9}
\]

用层析恒等式 \(\sum_i e_i=\sum_{k=1}^{H}N_k\)，得到精确的相位树容量上界

\[
\boxed{
\sum_{i\in\mathcal I}e_i
\le
\mu\sum_{k=1}^{H}D_k
\left(\left\lfloor\frac{M}{q^k}\right\rfloor+1\right).
}
\tag{10}
\]

若只保留 \(D_k\le D\)，则有较粗但便于账本比较的形式

\[
\sum_i e_i
\le
\mu D\left(\frac{M}{q-1}+H\right).
\tag{11}
\]

证明只用 (7) 的同余和区间装箱，不把 Fourier 相位幅度当作高度。若状态按
\(\gamma_i\equiv\gamma_j\pmod {q^{\min(e_i,e_j)}}\) 分成相容胞，则在每个胞内把
\(D_k=1\) 代入 (10)，正好恢复固定-B 清分相位合同的逐胞版本。

## 4. 有限候选标签的穷尽二分

在实际选择器中，\(\mathcal S_i(q)\) 通常先被限制为有限表（例如两个线性颜色、有限
的固定-B 标签或一个已经截断的 source 菜单）。对每个状态定义局部可行集

\[
\mathcal C_i(q)=
\{s\in\mathcal S_i(q)\cap I:
 s\equiv\gamma_i\pmod {q^{e_i}}\}.
\tag{12}
\]

于是有以下有限、互斥的回执二分：

1. **FOURIER_PHASE_NO_LOCAL_LIFT**：某个 \(i\) 的 \(\mathcal C_i(q)=\varnothing\)。
   回执保存 \((q,e_i,b_i,\gamma_i,\mathcal S_i,I)\)，它证明当前 source map 无法
   承担该 Fourier q-primary 相位，但不证明原状态可递降。
2. **FOURIER_PHASE_ASSIGNMENT_DEFICIT**：所有 \(\mathcal C_i(q)\) 非空，但在
   标签重复度、颜色或同一模数窗口等联合约束下不存在选择
   \(s_i\in\mathcal C_i(q)\)。若已把标签槽、颜色和模数窗口约束编码为一个带容量的
   二部图匹配，最小 Hall 集 \(U\subseteq\mathcal I\) 满足
   \(|U|> |N(U)|\) 即为有限阻碍证书。
3. **FOURIER_PHASE_LIFTED**：存在完整标签选择。此时用 (8)--(10) 计算
   \(D_k,N_k\) 和总 q-height；若与线性块的标签—模数混合容量或固定-B 容量合并后
     超过需求预算，则得到容量 surplus，否则保留为状态内 Fourier 证书加一个已实现的
     `phase_lift` 字段。

若候选标签表本身不是有限且完备的，唯一合法回执是
**FOURIER_PHASE_SOURCE_UNCLOSED**；不能把未枚举的标签当作不存在。

这给出一个可执行的桥接门：只有第三分支才允许继续检查 E1--E5 的合法提升或严格势
下降；前两分支是 source-map 缺口，不得自动升级为递归边。

## 5. Fourier 数据不能单独决定载体：独立性反例

取 \(H=C_3=\langle g\rangle\)，\(\bar\phi(1)=g\)，指数盒为 \(\{0\}\)，目标
\(g\) 未命中，取目标代表 \(z^0=1\)，并令
\(\chi(g)=e^{2\pi\mathrm i/3}\)。此时 Fourier 数据固定为

\[
q=3,
\quad e=1,
\quad b=1,
\quad \gamma=1\pmod3.
\tag{13}
\]

若算术 source map 给出 \(\mathcal S^{(A)}=\{1\}\)，则存在 phase lift；若给出
\(\mathcal S^{(B)}=\{0\}\)，则不存在 phase lift。两种情形的
\(H,\bar\phi,\chi,z^0\)
完全相同，差别只在 source map。因此不存在仅由角色阶、相位分子或 Fourier 幅度
推出实际 q 进高度的逻辑规则。

这不是 Erdős--Straus 的反例，而是对“角色阶债务自动等于载体高度”这一桥接假设的
精确否定。它说明下一步必须证明一个具体的 source map 完备性，或在
`FOURIER_PHASE_NO_LOCAL_LIFT` / `FOURIER_PHASE_ASSIGNMENT_DEFICIT` 后构造合法的
Type I/II 终端或严格下降。

## 6. 选择器接入与剩余全称缺口

对一个真实 F 状态，建议按以下顺序写入回执：

1. 先在稳定子商群中规范选择 \(\bar\chi\)，记录 \(d_i,a_i\) 和相位预算；
2. 对每个候选素数 \(q\mid d_i\) 做 (2)--(5) 的 q-primary 投影；
3. 由独立算术 source map 生成 \(\mathcal S_i(q)\)，执行 (12) 的有限匹配；
4. 只有 `FOURIER_PHASE_LIFTED` 才调用 (10) 与现有线性载体容量；
5. 将 no-lift、Hall deficit 和 source-unclosed 分别送入可提升、主因子/加法组合或
   新的 source-completeness 证明。

因此本卡完成了“规范 Fourier \(\to\) q-primary 相位 \(\to\) 条件性算术容量”的
精确中间定理，并给出了三个互斥的失败/成功类型；它仍未证明对每个核心素数都存在
phase lift，也未证明容量 surplus 必然满足 E1--E5 或产生良基下降。这两个问题是
下一阶段真正需要解决的全称命题。

对固定 \(B\) 的同图表清分，新增的相位兼容—非互素吸收二分进一步表明：即使
phase lift 存在，也只会得到唯一的 \(q^e\) 标签类，并在约分时消除原 q 缺陷；
相位不一致则给出精确冲突回执。详见
[Fourier 与固定 B 清分相位的冲突—非互素吸收二分](type-I-fourier-fixed-b-phase-compatibility-no-go.md)。

若此处的相位恰是直接目标 \(\pi(-1)\) 的预像相位，则它还有更强的二阶约束：奇
\(q\) 必为零相位，二进至多两胞。这个特化不提供 source map，但排除了把奇 q 的直接
目标相位误当作 fixed-\(B\) 清分相位的桥，详见
[F 型目标对合的 target-odd Fourier 能量与 q-primary 相位塌缩](type-I-f-target-involution-fourier-phase-collapse.md)。
