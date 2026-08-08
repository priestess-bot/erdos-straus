---
kind: claim
claim_id: type-II-owner-primary-mask-arithmetic-lift-criterion
title: Type II owner primary 掩码的带来源同余—正规形提升判据
statement: 对一个已经通过 owner 物理流和 primary 数字终端的选择掩码，若每条被选流边携带真实来源参数 a_i 与两两互素因子 h_i，且 h_i 整除 p+4Da_i，则该掩码可按有限菜单精确分派：统一 AD' 同余与单位群目标映射通过后，若选中因子积 h 满足 h=-1 (mod 4D')，正规形公式给出 Type II 短证书；若存在 D'<D 的保持来源标签候选，则给出严格 source-switch 递降；若菜单为空，则输出带最小失败门的算术提升障碍。owner primary 掩码本身不被当作整数证书，只有这组 E1–E5 门通过后才可升级。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-owner-kernel-primary-digit-certificate
  - type-II-annihilator-congruence-fiber-lift-criterion
  - type-II-same-modulus-source-switch-crt-criterion
  - type-II-source-fiber-qheight-kneser-bridge
  - type-II-owner-saturation-quotient-kernel-dispatch
topics:
  - type-II
  - owner-weight
  - arithmetic-lift
  - source-switch
  - CRT
  - normal-form
  - E1-E5
  - constructive-certificate
  - strict-descent
  - proof-program
sources:
  - claim: type-II-owner-kernel-primary-digit-certificate
    role: primary-mask-and-physical-flow-input
  - claim: type-II-annihilator-congruence-fiber-lift-criterion
    role: finite-labelled-fiber-menu
  - claim: type-II-same-modulus-source-switch-crt-criterion
    role: source-congruence-and-normal-form
  - claim: type-II-source-fiber-qheight-kneser-bridge
    role: q-height-to-integer-factor-map
  - claim: type-II-owner-saturation-quotient-kernel-dispatch
    role: owner-saturation-entry-order
  - reproduction: reproductions/type_ii_owner_primary_mask_arithmetic_lift.py
    role: p5113-real-lift-and-p97-empty-menu-controls
visibility: public
last_checked: '2026-08-09'
---

# Type II owner primary 掩码的带来源同余—正规形提升判据

## 1. 掩码载荷和统一变量

固定核心素数 \(p\)、原始层 \(D\)，以及上一引理返回的 primary 选择掩码。
掩码中每条被选流边 \(i\) 保存一条完整来源记录
\[
\sigma_i=(v_i,a_i,h_i),
\tag{1}
\]
其中 \(v_i\) 是 primary 关系块，\(a_i\) 是来源参数，\(h_i>1\) 是该边实际选择的
整数因子。要求这些记录已通过：

\[
h_i\mid p+4Da_i,\qquad
(h_i,4D)=1,
\tag{2}
\]
并且经过 shared-q 合并后，选中的 \(h_i\) 两两互素。令
\[
I=\{\text{掩码中取值为 1 的流边}\},\qquad
h_I=\prod_{i\in I}h_i.
\tag{3}
\]

\(h_I\) 是掩码对应的整数因子积；它不是仅由残数 \(v_i\) 决定的群元素。若
同一物理槽上有多个 owner 标签，物理流门已经保证它们不会在 \(I\) 中重复出现，
除非 source contract 明确给出额外重复预算。

对候选低模数参数使用统一变量
\[
x=AD',
\tag{4}
\]
其中
\[
D'\mid D,\qquad A\mid D',\qquad D'/A\text{ 平方自由},\qquad
4AD'<p.
\tag{5}
\]
所有被选来源必须满足同一个合同
\[
\boxed{
AD'\equiv Da_i\pmod{h_i}
\quad(i\in I).
}
\tag{6}
\]
因为 (2) 中 \((h_i,4D)=1\)，有精确等价
\[
h_i\mid p+4AD'
\iff
AD'\equiv Da_i\pmod{h_i}.
\tag{7}
\]
所以 (6) 同时是带来源 CRT 合同和目标因子整除条件，不能按每个 owner 独立
选择低层参数。

## 2. 有限提升菜单与门序

定义带来源 owner 掩码菜单
\[
\mathscr M_I(p,D)=
\left\{(D',A,\eta):
\begin{array}{l}
(D',A)\text{ 满足 (5)},\\
\eta:U(4D')\twoheadrightarrow J\text{ 是当前 primary/核状态所需的目标映射},\\
\eta(-1)=t_J,\\
\eta(h_i\bmod4D')=u_i\quad(i\in I),\\
AD'\equiv Da_i\pmod{h_i}\quad(i\in I)
\end{array}
\right\}.
\tag{8}
\]
\(J,t_J,u_i\) 来自相容核角色的 source-SNF 记录；若当前状态直接在完整
\(U(4D')\) 中工作，可把 \(\eta\) 取为恒等映射。映射存在性由单位群目标映射
SNF 判据检查，不能从 primary 群同构自动推断。

对 (8) 固定以下门序：

1. **E1/FIBER_REALIZED**：每条掩码边都有来源记录 (1)，且 primary 关系块的
   source contract 与 \(h_i\) 一致；
2. **E2/SOURCE_CRT**：统一合同 (6) 和目标映射标签全部通过；
3. **E3/RANGE**：\(D',A\) 通过除子、平方自由、范围和 shared-q 条件；
4. **E4/NORMAL_FORM**：若 \(h_I\equiv-1\pmod{4D'}\)，运行正规形；
5. **E5/DESCENT**：只有 \(D'<D\) 且来源标签仍由 \(\eta\) 保持时，才登记严格
   可提升递降；\(D'=D\) 不是递降。

E1 或 E2 失败时，不得继续把掩码计入整数容量；E3 失败时输出有限参数纤维空集；
E4 未命中但 E1–E3 通过时，保留一个带来源 relay 候选，而不是伪造短证书。

## 3. 直接 Type II 证书和严格递降

若某个菜单元素 \((D',A,\eta)\) 满足
\[
h_I\equiv-1\pmod{4D'},
\tag{9}
\]
令
\[
K_I=\frac{h_I+1}{4D'},\qquad
C'=\frac{D'}A,\qquad
B_I=\frac{K_Ip+A}{h_I}.
\tag{10}
\]
由 (6)--(7) 有 \(h_I\mid p+4AD'\)，而 (9) 给出
\[
h_I=4AC'K_I-1.
\tag{11}
\]
又有
\[
B_I-A
=\frac{K_I(p-4AD')+2A}{h_I}>0.
\tag{12}
\]
因此
\[
\boxed{
\mathrm{OWNER\_MASK\_TYPE\_II\_SHORT\_CERTIFICATE}
=(D',A,C',K_I,B_I,h_I,\sigma_I).
}
\tag{13}
\]
这一步把 primary 掩码中的每条流边和其真实因子逐项保留，故不是仅有残数群的
伪命中。

若 (9) 未命中，但菜单中存在 \(D'<D\) 的元素，输出
\[
\boxed{
\mathrm{OWNER\_MASK\_STRICT\_SOURCE\_SWITCH\_RELAY}
=(D',A,\eta,\sigma_I,h_I).
}
\tag{14}
\]
只要 E5 的来源标签势严格下降，(14) 就是统一选择器的严格可提升递降边；
若 \(\eta\) 只实现抽象群而不能保持来源，则降级为
OWNER_MASK_LIFT_OBSTRUCTED，不把有限商冒充整数递归。

若菜单只有 \(D'=D\) 的非命中元素，输出
OWNER_MASK_SAME_MODULUS_RELAY_UNCLOSED；它既不是短证书，也不是严格下降，
必须继续寻找另一掩码或另一条 Type I/F/G 出口。

## 4. 菜单为空时的完备障碍

对有限候选对 \((D',A)\)，先计算来源合同的 CRT 剩余
\[
x\equiv Da_i\pmod{h_i}\qquad(i\in I).
\tag{15}
\]
若这些剩余不相容，给出
\[
\mathrm{OWNER\_MASK\_SOURCE\_CRT\_INCONSISTENT}
\tag{16}
\]
及一对最小不相容来源。若 CRT 相容但其唯一剩余类在
\(1\le x=AD'\le D^2\) 中没有合法平方自由分解，给出
\[
\mathrm{OWNER\_MASK\_ADMISSIBLE\_FIBER\_EMPTY}.
\tag{17}
\]
若参数对存在但没有保持 \(J\) 和标签的 \(\eta\)，给出
\[
\mathrm{OWNER\_MASK\_GROUP\_MAP\_OBSTRUCTED}.
\tag{18}
\]
若 E1–E3 通过、但 (9) 不成立且不存在 \(D'<D\)，给出
\[
\mathrm{OWNER\_MASK\_NO\_SHORT\_OR\_STRICT\_EDGE}.
\tag{19}
\]
(16)--(19) 按顺序构成有限、互斥的 owner 掩码算术负证书。它们只否定该掩码的
整数提升，不否定同一核心素数的其它掩码或 Type I 路径。

## 5. 充要性证明

若 (8) 中存在元素，(6)--(7) 使所有 \(h_i\) 同时整除目标因子
\(p+4AD'\)，而 (5) 保证 \(A,D'\) 是合法参数。若 (9) 成立，(10)--(12) 直接
推出正规形和 \(B_I>A\)，所以 (13) 是 Type II 短证书。若 (9) 不成立且
\(D'<D\)，(14) 的来源标签、目标映射和参数势均由菜单元素显式保存，故它是严格
source-switch 候选。

反过来，任意保持掩码来源标签的低模数 Type II 表示，其参数必满足 (5)，每个
保留因子必满足 (7)，其单位群/核坐标给出 \(\eta\)，因而出现在 (8) 中。若该表示
是直接目标证书，目标因子积必满足 (9)；若是严格降模，则 \(D'<D\)。所以
(13)、(14) 和 (16)--(19) 覆盖了这个固定掩码的全部算术出口。

## 6. 算术控制

### \(p=5113\) 的 owner 掩码短证书

取 \(D=6\)，primary 掩码选中来源 \(a_1=6\) 的因子 \(h_1=7\)。候选
\(D'=1,A=1\) 满足
\[
1\equiv6\cdot6\pmod7,\qquad
7\equiv-1\pmod4.
\]
于是
\[
K_I=2,\qquad C'=1,\qquad B_I=(2\cdot5113+1)/7=1461>1.
\]
该掩码输出 (13)，与直接 Type II 证书一致。

保留两个来源 \(a_1=3,h_1=17\) 与 \(a_2=6,h_2=7\) 时，
\(h_I=119\)、\(D'=1,A=1\) 仍满足
\[
1\equiv6\cdot3\pmod{17},\qquad
1\equiv6\cdot6\pmod7,\qquad
119\equiv-1\pmod4,
\]
并得到
\[
K_I=30,\qquad B_I=(30\cdot5113+1)/119=1289>1.
\]
这是带两个来源标签的 owner 掩码提升控制。

### \(p=97\) 的伪池化空菜单

取 \(D=6\)，来源记录
\[
(a_1,h_1)=(1,11),\qquad(a_2,h_2)=(3,13),
\]
掩码因子积 \(h_I=143\equiv-1\pmod{24}\)。统一变量
\(x=AD'\) 必须满足
\[
x\equiv6\pmod{11},\qquad x\equiv18\pmod{13},
\]
故
\[
x\equiv83\pmod{143}.
\]
但所有 \(A\mid D'\mid6\) 都有 \(1\le x\le36\)，没有合法 \(x\)。因此
输出 OWNER_MASK_ADMISSIBLE_FIBER_EMPTY，而不能把
\(11\cdot13\equiv-1\pmod{24}\) 当作 Type II 证书。

### 单位群映射障碍

若当前 primary relay 要求 \(J=C_4\)，而候选低模数只有
\(U(4)\simeq C_2\)，则 E1–E3 之外的目标映射门失败，输出
OWNER_MASK_GROUP_MAP_OBSTRUCTED；增加 owner 标签或 q 重数不能改变
单位群的 invariant factors。

## 7. 研究边界

本判据把上一引理的 primary 掩码首次连接到真实整数因子和 E1–E5 菜单，完成了
固定掩码层面的“短证书 / 严格 source-switch / 精确提升障碍”三分。它仍不证明
每个核心素数都能产生一个通过 E1–E3 的 owner 掩码；全局剩余问题是证明跨状态
q 进容量必产生这样的掩码，或在掩码菜单为空时触发另一条 Type I/F/G 下降。不能
把 (16)--(19) 的负证书误写成整个猜想的反例。
