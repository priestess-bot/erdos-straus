---
kind: claim
claim_id: type-II-kernel-fourier-energy-role-capacity-dispatch
title: Type II 核分裂 Fourier 能量的相容角色—容量分派
statement: 对非空真目标核截面 S_t 子集 K，Parseval 缺陷能量 n(|K|-n) 可按源关系格相容角色与不相容角色精确分解。若不相容能量非零，则最小阶不相容角色给出带系数的 LIFT_OBSTRUCTED，不能计入容量；若不相容能量为零，则至少存在一个相容非平凡角色，按最小角色阶分派为 ell-初等源需求、高阶 ell^a/广义 2^j 角色或混合 primary 角色。对一组相容的 ell-初等角色，其独立限制秩进入 Rado/Hall 容量；秩缺口给出 KERNEL_FOURIER_CAPACITY_DEFICIT，匹配通过后才允许进入 Kneser 或 Type II 目标纤维。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-congruence-kernel-split-fourier-certificate
  - type-II-kernel-fourier-source-relation-compatibility
  - type-II-rado-linear-rank-hall-capacity-bridge
  - type-II-two-power-character-depth-sieve
topics:
- type-II
- kernel-fourier
- parseval
- role-dispatch
- source-relation
- capacity
- Hall
- Rado
- generalized-dyadic
- lift-obstruction
- proof-program
sources:
  - claim: type-II-congruence-kernel-split-fourier-certificate
    role: exact-kernel-section-energy
  - claim: type-II-kernel-fourier-source-relation-compatibility
    role: affine-source-lift-test
  - claim: type-II-rado-linear-rank-hall-capacity-bridge
    role: independent-role-capacity
  - claim: type-II-two-power-character-depth-sieve
    role: higher-order-character-depth
visibility: public
last_checked: '2026-08-05'
---

# Type II 核分裂 Fourier 能量的相容角色—容量分派

## 1. 核截面与精确能量

令 \(K\) 为有限阿贝尔核，\(S_t\subset K\) 为目标伪命中的非空真截面，
\[
n=|S_t|,\qquad 0<n<|K|,
\]
并对 \(\chi\in\widehat K\) 记
\[
F_t(\chi)=\sum_{k\in S_t}\overline{\chi(k)}.
\tag{1}
\]
Parseval 给出非平凡核能量
\[
\boxed{
\mathcal E_t
=\sum_{\chi\ne1}|F_t(\chi)|^2
=n(|K|-n)>0.
}
\tag{2}
\]

令 \(\mathcal X_{\mathrm{comp}}\subseteq\widehat K\) 是通过源关系格仿射相容性
判据的角色集合，包含平凡角色；其余角色记为
\(\mathcal X_{\mathrm{obs}}=\widehat K\setminus\mathcal X_{\mathrm{comp}}\)。定义
\[
\mathcal E_{\mathrm{comp}}
=\sum_{\substack{\chi\in\mathcal X_{\mathrm{comp}}\\\chi\ne1}}
|F_t(\chi)|^2,\qquad
\mathcal E_{\mathrm{obs}}
=\sum_{\chi\in\mathcal X_{\mathrm{obs}}}|F_t(\chi)|^2.
\tag{3}
\]
于是有精确分解
\[
\boxed{\mathcal E_t=\mathcal E_{\mathrm{comp}}+\mathcal E_{\mathrm{obs}}.}
\tag{4}
\]
这里的相容性不是“角色存在”的抽象判断，而是由源关系格、锚点相位和 SNF
恒等式逐条核验。

## 2. 不相容能量回执

若
\[
\mathcal E_{\mathrm{obs}}>0,
\tag{5}
\]
则存在 \(\chi\in\mathcal X_{\mathrm{obs}}\) 使 \(F_t(\chi)\ne0\)。按
\[
\bigl(\operatorname{ord}\chi,\ -|F_t(\chi)|^2,\ \operatorname{SNF\_index}(\chi)\bigr)
\]
的字典序选规范角色 \(\chi_{\mathrm{obs}}\)，输出
\[
\mathrm{KERNEL\_FOURIER\_LIFT\_OBSTRUCTED}
=\bigl(K,S_t,\chi_{\mathrm{obs}},F_t(\chi_{\mathrm{obs}}),
\mathcal E_{\mathrm{obs}}\bigr).
\tag{6}
\]
它是一个带精确非零系数的有限负证书；该角色不能计入 q-height、Kneser 或 Hall
容量。若同时 \(\mathcal E_{\mathrm{comp}}>0\)，只允许把相容部分另行分派，不能
用相容角色掩盖不相容能量。

## 3. 全相容能量与最小阶角色

若
\[
\mathcal E_{\mathrm{obs}}=0,
\tag{7}
\]
则由 (2) 必有 \(\mathcal E_{\mathrm{comp}}>0\)，从而至少存在一个相容非平凡角色
\(\chi_*\) 使 \(F_t(\chi_*)\ne0\)。在所有此类角色中取角色阶最小者，并在并列时
取 Fourier 幅度最大的规范角色。令
\[
d=\operatorname{ord}(\chi_*).
\tag{8}
\]
按 \(d\) 分派：

1. \(d=\ell\) 为素数：\(\chi_*\) 给出一个真实的
   \(\ell\)-初等 SOURCE\_RELATION\_FOURIER 角色，可形成一个独立源需求方向；
2. \(d=\ell^a\)、\(a\ge2\)：给出 HIGHER\_PRIMARY\_FOURIER\_ROLE；当
   \(\ell=2\) 时是规范的广义 \(2^a\) 角色，进入二幂深度或高阶数字终端；
3. \(d\) 含至少两个不同素因子：给出 MIXED\_PRIMARY\_FOURIER\_ROLE，必须先
   经 CRT/primary 分解验证；不能把它拆成多个独立容量单位。

这些回执都保留 \(F_t(\chi_*)\) 的精确系数；角色阶本身不等价于 q-height。

## 4. \(\ell\)-初等角色的 Rado/Hall 容量

取一组已经通过相容性检查的 \(\ell\)-初等角色
\(\chi_1,\ldots,\chi_r\)，并把它们在
\[
\widehat K[\ell]\simeq
\operatorname{Hom}_{\mathbb F_\ell}(K_\ell/\ell K_\ell,\mathbb F_\ell)
\]
中的限制记为需求向量 \(d_1,\ldots,d_r\)。令 \(U\) 为线性独立需求子集，真实
q 槽的源列张成空间为 \(W(U)\)。若
\[
\operatorname{rank}_{\mathbb F_\ell}W(U)<|U|,
\tag{9}
\]
则输出
\[
\mathrm{KERNEL\_FOURIER\_CAPACITY\_DEFICIT}
(\ell,U,\operatorname{rank}W(U),|U|).
\tag{10}
\]
若所有请求子集都通过 Rado 条件，则构造独立源列匹配，再将其送入 Kneser
稳定子容量。式 (10) 是真正的源列秩缺口，不是 Parseval 能量缺口。

对多个截面 \(S_{t_i}\)，先按 \((\ell,\chi|_{K_\ell})\) 去重；相同角色方向只
产生一个请求。不同截面的 Fourier 能量可以分别保留为
\[
\mathcal E_{\mathrm{comp}}^{\mathrm{tot}}
=\sum_i\mathcal E_{\mathrm{comp}}(S_{t_i}),
\]
但只有去重后的独立角色秩才能计入 Hall 容量，不能按能量大小重复收费。

即使相容角色全部通过，非零 Fourier 支撑的数量也只能作为候选角色信息；只有同时
具有互异 q 槽、独立源关系限制和共同实现映射的角色，才可进入容量账本。这一层的
Parseval 支撑下界与 `SIMULTANEOUS_ROLE` 必要门见
[Type II 核 Fourier 支撑不确定性下界与 simultaneous-role 容量门](type-II-kernel-fourier-support-uncertainty-demand.md)。
特别是 (C_4) 两点截面的两个非零非平凡系数不能自动收费为两个 q 需求。

## 5. 证明

(2) 是有限阿贝尔群 Parseval 的非平凡角色部分；(3)--(4) 只是把角色集合按
相容性划分，因此 (5) 立即给出 (6)。若 (7) 成立，(2) 保证相容非平凡角色存在，
有限角色群的阶有最小值，故 (8) 的规范选择存在。角色阶的三种情形由有限阿贝尔
群的 primary 分解直接得到。

对素数阶角色，其限制是一个 \(\mathbb F_\ell\) 线性泛函；一组独立限制可作为
Rado 请求。若 (9) 成立，邻域源列维数严格小于需求数，Rado 对偶给出线性秩缺口；
若所有子集通过，Rado 独立代表定理给出匹配。Parseval 只提供角色能量，不替代
这一步的独立性检查，证毕。

## 6. 边界例子

### 不相容能量

取 \(K=C_4\)、\(S_t=\{1\}\)。所有三个非平凡角色的 Fourier 系数模长均为 \(1\)。
若只有平凡角色和阶 \(2\) 角色通过源关系相容性，则阶 \(4\) 角色贡献
\(\mathcal E_{\mathrm{obs}}=2\)，输出 (6)，不能把总能量 \(3\) 计为容量。

### 高阶二幂角色

取 \(K=C_4\)、\(S_t=\{1,2\}\)。阶 \(2\) 角色的系数为零，而阶 \(4\) 角色系数
\(-1-i\) 非零；若该阶 \(4\) 角色相容，则最小非零角色阶为 \(4\)，输出
HIGHER\_PRIMARY\_FOURIER\_ROLE，而不是虚构一个阶 \(2\) 请求。

### 独立性缺口

两条相容阶 \(\ell\) 角色若限制到同一个源列方向，则能量可能都非零，但
\(\operatorname{rank}W(U)=1<2\)。此时回执是 (10)，不能按两个角色收费。

## 研究边界

该引理把核分裂的 Parseval 能量首次变成“相容角色、不可提升角色、角色阶和源列
秩”的规范分派。支撑下界本身仍不证明相容角色一定造成 q-height 超载；必须先通过
`SIMULTANEOUS_ROLE`，再把 \(\mathcal E_{\mathrm{comp}}\) 选出的独立角色与真实源槽
价格、稳定子容量或保持标签的商递降连接起来。
