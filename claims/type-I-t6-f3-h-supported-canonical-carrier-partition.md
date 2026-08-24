---
kind: claim
claim_id: type-I-t6-f3-h-supported-canonical-carrier-partition
title: T6-F3 R4/R6 的规范 h-menu 资格与 D-star 算术余项分派
statement: >-
  对一份 actual persistent、terminal-first 后仍非终止的 low proper-height
  stutter receipt，设 2<=h=3u<p、k>1、D*=D/gcd(D,h^2-1)>1，且
  k_perp=1，即 k 的每个素因子都整除 h。若 m=3 且 5 不整除 D*，则
  k=3kappa、kappa=7 mod24、kappa>=31，故 kappa 有规范最小的
  7 mod12 素因子 q_h；它必整除 u，因而落在 actual root receipt 所确定的
  root-capacity source-menu 输入域，绝非 quotient-only，但这只是菜单资格而非
  raw occurrence/E1。若 m>3，则 m=0 或 1 mod3；在
  m=1 mod3 时 3 不整除 k，最小素因子 q_h 整除 u；在 m=0 mod3 时
  v_3(k)=1，故 k>3 时 k/3 的最小素因子 q_h 整除 u，而 k=3 是唯一没有
  非 3 h-carrier 的子叶。另一方面，D*>1 且 gcd(D*,h)=1，故 D* 的规范
  最小素因子（或 whole D*）是由 actual maximal receipt 的 D 确定的
  source-bound arithmetic factor，并严格属于 transverse arithmetic provenance；
  它仍不是可消费的 raw occurrence/E1。于是 R4/R6 被全称分为 terminal、规范
  root-supported menu、规范 D*-terminal menu、k=3 transverse 子叶及一个
  最小 unphysicalized TR1 residual。该结果证明 menu/factor existence 与算术来源分类，
  但不证明 root menu 必命中，也不从 D* 构造 target、全域 lift 或 T5 ticket；
  因而 OPEN_TR1_PHYSICAL_SERIALIZER、F3 与 T6 仍开放。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-t6-f3-proper-root-routing-with-explicit-residuals
  - type-I-root-capacity-stutter-eisenstein-support
  - type-I-root-capacity-stutter-provenance-dispatch
  - type-I-root-capacity-stutter-common-divisor-alignment
  - type-I-root-capacity-stutter-primitive-quotient-normalization
  - type-I-root-capacity-stutter-m-three-biquadratic-norm-reduction
  - type-I-root-capacity-stutter-transverse-residual-capacity-map
  - type-I-root-capacity-composite-divisor-external-terminal
topics:
  - type-I
  - t6
  - proper-root
  - h-supported
  - transverse-residual
  - carrier-provenance
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_t6_f3_h_supported_carrier_partition.py
    role: focused-partition-and-reason-code-controls
visibility: public
last_checked: '2026-08-24'
---
# T6-F3 R4/R6 的规范 h-menu 资格与 (D_*) 算术余项分派

## 1. 量词域

固定一个已经通过活动 persistent admission 的 proper-root source (S)。其 actual
maximal receipt 和 terminal-first digest 重算出

\[
p\equiv1\pmod {24},\qquad 2\le h=3u<p,\qquad k>1,
\tag{1}
\]

\[
D=mp+1-h,\qquad eD=ph+1,\qquad
D_*={D\over(D,h^2-1)}>1.
\tag{2}
\]

本卡只处理

\[
k_\perp=1,
\tag{3}
\]

即 (k) 的每个素因子都整除 (h)。owned routes 为：

\[
\begin{array}{ll}
R4:&m=3,\quad 5\nmid D_*;\\
R6:&m>3.
\end{array}
\tag{4}
\]

`m=3, 5|D_star`、quotient-only、high endpoint 与 (k=1) 均不在量词内。
条件 (3) 从不允许把任何因子标为 quotient-only。

## 2. R4 必有规范的非 3 根支撑载体

已有 (m=3) primitive theorem 给出

\[
k=3\kappa,
\qquad \kappa\equiv7\pmod {24},
\qquad k\ge93.
\tag{5}
\]

所以 (kappa\ge31)。Eisenstein 支撑定理说明 (kappa) 的每个素因子都为
(1\pmod6)，即模 12 只能为 1 或 7。又 (kappa\equiv3\pmod4)，故其素因子
分解中至少一个 (7\pmod {12}) 的素因子出现奇数次。定义

\[
q_h(S)=\min\{q:q\mid\kappa,\ q\equiv7\pmod {12}\}.
\tag{6}
\]

这是不依赖人工选择的确定因子。由 (3)，(q_h\mid h=3u)；而
(q_h\ne3)，所以

\[
\boxed{q_h\mid u.}
\tag{7}
\]

式 (7) 说明 (q_h) 的 **menu eligibility** 可从 actual root-height receipt
(u=(2r+1,(p^2+p+1)/3)) 重算。因此它属于既有 root-capacity
external-source menu 的输入类型，不是 quotient-only chart。这里没有构造 raw path
occurrence，也没有授权把 (q_h) 收费进新的 Type-I support；menu eligibility 不等于 E1。

这仍不证明该有限菜单命中。对 (q\mid u) 的菜单可以为空；已有
((p,q)=(457,7)) 是严格负控制。因此 R4 的非 3 menu-factor existence 不能误写成
terminal totality。

## 3. R6 的规范载体与唯一 (k=3) 例外

actual 三进分派给出

\[
m\not\equiv2\pmod3,
\qquad
3\mid k\Longleftrightarrow m\equiv0\pmod3.
\tag{8}
\]

### 3.1 (m\equiv1\pmod3)

此时 (3\nmid k)。令 (q_h) 为 (k) 的最小素因子。由 (3)，
(q_h\mid h)，且 (q_h\ne3)，故同样有 (q_h\mid u)。

### 3.2 (m\equiv0\pmod3)

由实际模 3 分流，(3\mid a,b=e-1)。写

\[
a=3A,\quad b=3B,\quad m=3M,\quad h=3u.
\tag{9}
\]

公共因子正规化给出

\[
k=3\kappa,
\qquad
A^2-AB+B^2=u\kappa.
\tag{10}
\]

并且 (e=3B+1)、(pA+B=eu)。由于 core root 的每个 (u)-素因子均为
(1\pmod3)，有 (u\equiv1\pmod3)；再将后一等式模 3 化简，得到

\[
A+B\equiv1\pmod3.
\tag{11}
\]

而

\[
A^2-AB+B^2\equiv(A+B)^2\equiv1\pmod3.
\tag{12}
\]

所以

\[
\boxed{\kappa\equiv1\pmod3,\qquad v_3(k)=1.}
\tag{13}
\]

若 (k>3)，则 (kappa>1)。定义 (q_h) 为 (kappa) 的最小素因子；它不等于
3，并由 (3) 再次满足 (q_h\mid u)。若 (k=3)，则 (kappa=1)，这是 R6
中唯一没有非 3 h-supported carrier 的子叶；不得把素数 3 伪装成
(q\mid u) source，因为 (3\nmid u)。

## 4. Source-bound transverse arithmetic factor 对每个输入都存在

已有 (h^2-1) overlap theorem 对整个 low proper-height actual domain 给出

\[
D_*>1.
\tag{14}
\]

又由 (D\mid ph+1) 与 (h\mid p^2+p+1) 有 ((D,h)=1)，所以

\[
\boxed{(D_*,h)=1.}
\tag{15}
\]

令

\[
q_T(S)=\min\{q:q\text{ prime},\ q\mid D_*\}.
\tag{16}
\]

式 (14) 保证它存在。`D_star_factorization_receipt` 必须重放 (D_*\mid D)，而
(D) 来自 actual maximal decomposition (R-h=ED)。这使 (16) 成为
source-bound arithmetic factor，而不是任意外部输入；但它仍未证明某条 raw path 上有可消费
的 complete-excess block，也不支付 E1。式 (15) 只表明该 factor 与 h-supported
root menu 的算术支撑严格不同。若 (q_T=2)，则它进入 dyadic transverse 子叶；不得调用只对
奇素数成立的 low-gap/negative-root menus。

这只证明“没有 (D_*>1) arithmetic factor”的 family 为空。它没有证明
`TR1PhysicalTransitionV1` 存在：integer raw occurrence/E1、确定 target、E3 owner、全域
E4 与 parent-to-final E5 均仍缺失。

## 5. 完整有序分派

对每个 (1)--(4) 的输入依次执行：

1. 重放活动 terminal-first；命中即 direct terminal。
2. 若存在第 2--3 节的 (q_h)，按所有 (1<Q\mid u) 的递增顺序运行完整
   root-capacity composite external menu；首个命中是 direct Type I terminal。
3. 重放当前声明的 whole-(D_*)、native raw、quadratic positive、local overlap 与
   reflected negative terminal menus；首个命中是 direct terminal。
4. 若仍 miss，记录 (16) 的 source-bound arithmetic factor；只有另一个定理把它绑定成
   可消费 integer raw occurrence 后，才允许送入 proposed `TR1PhysicalTransitionV1`。
5. 若该 envelope 尚未建立，唯一输出为下面的显式最小 residual，而不是
   `verified_edge`。

前缀顺序使各叶互斥。第 2 步有限，因为 (u) 与每个 source quotient 的除子集有限；
第 3 步的每张 menu 也由实际 receipt 的有限因子集合决定。有限性不是非空性证明。

## 6. 最小 residual

现有定理留下两个同一物理缺口的 payload 变体：

```text
R4_H_MENU_AND_DSTAR_TERMINALS_MISS_NO_TR1_TARGET
R6_H_MENU_AND_DSTAR_TERMINALS_MISS_NO_TR1_TARGET
```

R6 的 `k=3` 只把第一段 h-menu 置为空；它仍有 (14)--(16) 的 source-bound transverse
factor candidate。一个最小失败 receipt 必须保存：

```text
actual parent/admission/source path
terminal-first complete miss digest
m, k, k_perp, D_star and their verified factorizations
q_h/root-menu miss digest when q_h exists
D_star terminal-menu miss digest
q_T arithmetic-factor id inside actual D
integer raw occurrence status = UNBOUND
absence of any accepted TR1 target/ticket
```

缺失的是 arithmetic factor 到 integer occurrence/E1 再到 successor 的数学桥。准确状态为：

```text
H_SUPPORTED_MENU_FACTOR_PARTITION = ESTABLISHED
NO_DSTAR_ARITHMETIC_FACTOR = EMPTY
TR1_INTEGER_RAW_OCCURRENCE = OPEN
TR1_PHYSICAL_TRANSITION_V1 = OPEN
R4 = OPEN_MINIMAL_RESIDUAL
R6 = OPEN_MINIMAL_RESIDUAL
F3 = OPEN
T6 = OPEN
```

还有两个不能从相邻 (m=3,q=5) 轨借用的边界。其一，policy endpoint 的
(L_\omega=E_uE_v) 是一般 primitive p-free endpoint 的代数恒等式，但产生该 endpoint
的确定 `omega_pf`、单侧 factor-pair 与 source-bound priority proof 只在该专门 lineage
建立；R4/R6 必须重新证明自己的 actual path。其二，target support (M\le B_p)
本身**不**推出 ABSORB。必须先由 target 的 (R_T<p) marked-absorb 语义、完整
ABSORB protocol fields 与对应 local rank 证明一次不可逆 `CHARGED -> ABSORB`
commit；若 (R_T>p)，target 仍是 overflow，只有真实 parent-to-final CHARGED rank
严降时才可留在 CHARGED。两者都不能从 support 大小或局部 checkpoint 数值下降推断。

## 7. 聚焦重放

```bash
python3 reproductions/type_i_t6_f3_h_supported_carrier_partition.py --verify
python3 -m unittest tests.test_type_i_t6_f3_h_supported_carrier_partition -v
```

复现器核对 R4、R6 的 carrier tie-break、(k=3) 特例、`k_perp=1` 防误投、
(D_*>1) arithmetic-factor candidate 与稳定 residual codes。fixture 只是 typed partition control，
不冒充 actual persistent receipt；全称结论由第 2--5 节的符号证明承担。
