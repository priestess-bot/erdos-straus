---
kind: claim
claim_id: type-II-same-fiber-factor-box-neutral-role-capacity
title: Type II 同纤维精确因子盒、中性载荷张量与 primary 角色边界
statement: >-
  对 admissible Type II 参数 (D_*,A)，令 M=4D_*、N=p+4AD_*，并写
  N=prod_i q_i^{e_i}。唯一分解把指数盒 prod_i[0,e_i] 双射到 N 的全部正因子；
  因而固定纤维内存在 Type II 证书，当且仅当某个盒记录 h 满足 h=-1 mod M。
  对任意商角色 eta，eta(q_i)=1 的坐标不改变商像，却把每个 labelled fiber 的
  重数精确乘以 e_i+1；其算术深度仍为 e_i，而商像容量为 0。若素数 ell 不整除
  |H|，则 Hom(H,C_ell)=0 且 H/H^ell 平凡，所以 q_i=ell 的算术因子层不能冒充
  ell-primary 角色。对 p=557281、(D_*,A)=(182,1)，完整因子盒恰为
  [0,4]x[0,2]，83 方向给出精确深度 2 和 C3-fiber 重数 3，但 C83 角色秩为 0；
  chi_{-8} 在全部 15 个因子上为 1、在 -1 上为 -1，故这是 exact same-fiber
  Type II target-miss certificate。它不证明这些因子是 F/G physical source records，
  也不提供 owner map。另有双模型严格反例表明 source-contract exactness 本身不蕴含
  divisor-downclosure，membership 也不蕴含 provenance-preserving owner closure。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-source-lattice-fibered-kneser-selector
  - type-II-qadic-height-kneser-block-bridge
  - type-I-II-fg-universal-finite-source-map-completion
  - type-I-raw-certified-q-layer-charge-key-nonreuse
topics:
  - type-II
  - factor-box
  - q-adic-height
  - neutral-cargo
  - Fourier
  - primary-role
  - source-contract
  - divisor-closure
  - capacity-map
  - strict-counterexample
  - proof-program
sources:
  - claim: type-II-source-lattice-fibered-kneser-selector
    role: exact-Type-II-factor-to-certificate-translation
  - claim: type-II-qadic-height-kneser-block-bridge
    role: prime-power-factor-block-and-quotient-capacity
  - claim: type-I-II-fg-universal-finite-source-map-completion
    role: exact-physical-source-contract-boundary
  - claim: type-I-raw-certified-q-layer-charge-key-nonreuse
    role: typed-owner-map-boundary
  - reproduction: reproductions/type_ii_same_fiber_factor_box_neutral_role_capacity.py
    role: focused-p557-factor-box-neutral-fiber-character-role-and-closure-verification
visibility: public
last_checked: '2026-08-10'
---

# Type II 同纤维精确因子盒、中性载荷张量与 primary 角色边界

## 1. 固定纤维的算术因子合同

固定素数 \(p\) 和 admissible Type II 参数

\[
A\mid D_*,\qquad C_*=D_*/A\text{ 平方自由},\qquad 4AD_*<p.
\tag{1}
\]

令

\[
M=4D_*=4AC_*,\qquad N=p+4AD_*=p+AM.
\tag{2}
\]

由 \(M<p\) 及 \(p\) 为素数，

\[
\gcd(N,M)=\gcd(p,M)=1.
\tag{3}
\]

写出唯一素因子分解

\[
N=\prod_{i=1}^r q_i^{e_i},\qquad
E=\prod_{i=1}^r\{0,\ldots,e_i\},
\tag{4}
\]

并定义 labelled factor record

\[
h(a)=\prod_iq_i^{a_i}\qquad(a\in E).
\tag{5}
\]

唯一分解立即给出双射

\[
\boxed{E\overset{h}{\longleftrightarrow}\{d\in\mathbb N:d\mid N\}.}
\tag{6}
\]

由 (3)，每个 \(h(a)\) 都是 \(U(M)\) 中的单位。这里的 (6) 是固定整数 \(N\) 的
**算术因子合同**，所以不同素数块的 product synthesis 由唯一分解自动成立；它没有
声称每个记录都属于某个额外带标签的 F/G physical-source predicate。

## 2. 固定纤维 Type II 目标的充要判据

固定 (1) 后，存在该纤维上的 Type II 因子证书，当且仅当

\[
\boxed{\exists a\in E:\quad h(a)\equiv-1\pmod M.}
\tag{7}
\]

### 证明

若 (7) 成立，令

\[
K=\frac{h(a)+1}{M},\qquad
B=\frac{Kp+A}{h(a)}.
\tag{8}
\]

因为 \(h(a)\mid N=p+AM\) 且 \(h(a)=MK-1\)，有

\[
KN=Kp+KAM=(Kp+A)+Ah(a),
\tag{9}
\]

故 \(B\) 为正整数。又

\[
B-A=\frac{K(p-AM)+2A}{h(a)}>0
\tag{10}
\]

由 \(AM=4AD_*<p\) 得正性。因此 \((A,C_*,K)\) 给出该纤维的 Type II 短证书。
反向地，固定 \((D_*,A)\) 的 Type II 因子生成器具有
\(h=4AC_*K-1=MK-1\)，且 \(h\mid p+4AD_*=N\)，所以由 (6) 对应某个
\(a\in E\)，并满足 (7)。证毕。

因此，完整枚举 (6) 后的 target miss 不是 ambient superset evidence，而是固定
参数纤维的 exact negative factor certificate。它只关闭这一纤维，不关闭换
\((D_*,A)\)、Type I 菜单或其它来源递降。

## 3. 商角色中的中性载荷张量

令

\[
H=\langle q_1,\ldots,q_r\rangle\le U(M),\qquad
\eta:H\to Q
\tag{11}
\]

为任意有限阿贝尔商角色。把坐标分为

\[
Z=\{i:\eta(q_i)=1\},\qquad I=\{1,\ldots,r\}\setminus Z.
\tag{12}
\]

对 \(y\in Q\)，记 labelled factor fiber

\[
F_y=\{a\in E:\eta(h(a))=y\}.
\tag{13}
\]

投影到活跃坐标 \(I\) 后有精确笛卡尔分解

\[
\boxed{
F_y=F_y^{I}\times\prod_{i\in Z}\{0,\ldots,e_i\},
\qquad
|F_y|=|F_y^{I}|\prod_{i\in Z}(e_i+1).
}
\tag{14}
\]

所以 neutral block 不改变 quotient image：

\[
\eta(h(E))=\eta(h(E_I)),
\tag{15}
\]

但它精确增加 labelled fiber multiplicity。若

\[
o_i=\operatorname{ord}_Q(\eta(q_i)),
\tag{16}
\]

则单坐标的 quotient-prefix capacity 为

\[
\boxed{
\kappa_i^\eta
=\bigl|\{1,\eta(q_i),\ldots,\eta(q_i)^{e_i}\}\bigr|-1
=\min(e_i,o_i-1).
}
\tag{17}
\]

对 \(i\in Z\)，(17) 为零，而算术 factor depth 仍是 \(e_i\)。定义 neutral
fiber multiplier

\[
\nu_i^\eta=
\begin{cases}
e_i+1,&i\in Z,\\
1,&i\notin Z.
\end{cases}
\tag{18a}
\]

正确容量卡必须同时保存

\[
\mathcal C_\eta(q_i^{e_i})
=(e_i,\kappa_i^\eta,\nu_i^\eta)
\tag{18b}
\]

这三个不同量：算术深度、商像容量，以及 neutral 时的 labelled multiplicity。
(17) 只是单坐标商像容量；若要加入 Kneser 总价格，仍须使用共同最终稳定子，不能把
各坐标的局部数值无条件相加。

式 (14) 是 labelled-record 等式。若不同 records 在 \(U(M)\) 中碰撞，不能把它直接
改写为 residue-set cardinality 等式；必须另做 fiber/collision 检查。

## 4. Fourier 因子化与 primary 角色秩

令

\[
G=\langle H,-1\rangle\le U(M).
\]

对任意角色 \(\chi:G\to\mathbb C^\times\)，完整 labelled 因子盒的 Fourier 和精确
分解为

\[
\boxed{
\sum_{a\in E}\chi(h(a))
=\prod_{i=1}^r\left(\sum_{j=0}^{e_i}\chi(q_i)^j\right).
}
\tag{19}
\]

特别地，若 \(\chi|_H=1\)，而 \(\chi(-1)\ne1\)，则
\(-1\notin h(E)\bmod M\)。结合 (7)，这给出 exact same-fiber Type II
target-miss character certificate，而不只是某个不完整 source menu 的分离。

另取素数 \(\ell\)。若

\[
\ell\nmid|H|,
\tag{20}
\]

则任意同态 \(H\to C_\ell\) 的像阶同时整除 \(|H|\) 与 \(\ell\)，只能为 1。因此

\[
\boxed{\operatorname{Hom}(H,C_\ell)=0.}
\tag{21}
\]

等价地，幂映射 \(x\mapsto x^\ell\) 是 \(H\) 的自同构，故

\[
\boxed{H/H^\ell=1.}
\tag{22}
\]

所以“\(\ell\) 作为 \(N\) 的素因子出现”与“存在一个 \(\ell\)-primary Fourier
角色”是两回事。前者产生真实算术 factor depth；(20) 成立时，后者的秩严格为零。

## 5. \(p=557281\) 的精确容量卡

取

\[
p=557281,\qquad (D_*,A)=(182,1),\qquad
M=728,
\tag{23}
\]

则

\[
N=p+4AD_*=558009=3^4\cdot83^2.
\tag{24}
\]

由 (6)，

\[
B_3=\{1,3,3^2,3^3,3^4\},\qquad
B_{83}=\{1,83,83^2\}
\tag{25}
\]

的直积恰为全部十五个正因子，不是候选超集。它们模 \(728\) 的像为

\[
\{1,3,9,19,27,57,81,83,121,171,249,283,337,361,363\},
\tag{26}
\]

且十五个像彼此不同。目标 \(727=-1\) 不在 (26)，所以得到

\[
\boxed{\texttt{P557\_SAME\_FIBER\_TYPEII\_FACTOR\_TARGET\_MISS}.}
\tag{27}
\]

这完整关闭了固定 \((182,1)\) 的 Type II 因子搜索。

再取

\[
\eta(u)=(u\bmod13)^4:U(728)\to C_3.
\tag{28}
\]

有

\[
\operatorname{ord}(\eta(3))=3,\qquad \eta(83)=1.
\tag{29}
\]

因此

\[
\mathcal C_\eta(3^4)=(4,2,1),\qquad
\mathcal C_\eta(83^2)=(2,0,3).
\tag{30}
\]

活跃 \(3\)-盒在 \(C_3\) 三个像上的 labelled 重数为 \((2,2,1)\)；乘入
\(83\)-neutral block 后精确变为 \((6,6,3)\)。特别地，kernel records 是

\[
\{(0,0),(0,1),(0,2),(3,0),(3,1),(3,2)\}.
\tag{31}
\]

故 \(83,83^2\) 已经是 exact arithmetic neutral cargo。精确状态应分成

\[
\texttt{TYPEII\_SAME\_FIBER\_H83\_SQUARE\_FACTOR\_RECORD\_EXACT}
\]

与仍未关闭的

\[
\texttt{FG\_H83\_SQUARE\_OWNER\_LAYER\_RECEIPT\_UNPROVED}.
\]

另一方面，

\[
|U(728)|=\varphi(728)=288,\qquad 83\nmid288,
\tag{32}
\]

所以 (21)--(22) 给出

\[
\boxed{\operatorname{Hom}(U(728),C_{83})=0.}
\tag{33}
\]

尽管 \(\operatorname{ord}_{728}(83)=4\)，它也不能产生 \(83\)-primary role；它至多
在其它 primary 商中有非平凡像，而在 (28) 中恰为中性载荷。

最后取 Kronecker 角色

\[
\chi_{-8}(u)=\left(\frac{-2}{u}\right).
\tag{34}
\]

因 \(3\equiv83\equiv3\pmod8\)，有

\[
\chi_{-8}(3)=\chi_{-8}(83)=1,
\qquad \chi_{-8}(-1)=-1.
\tag{35}
\]

式 (19) 在完整 factor box 上给出总和 \(5\cdot3=15\)，从而 (35) 是 (27) 的
exact character certificate。它比“ambient divisor superset 上的 character”更强：
对固定 Type II 因子合同，(6) 已证明这里就是全部候选。但它仍不等于 F/G physical
source-map 的 exactness，也不生成 record-to-state、owner、E4 或 E5。

## 6. exact source contract 不蕴含 divisor/owner closure

算术因子盒在整除偏序下当然下闭；F/G physical source predicate 却可以额外依赖
lineage、label、range、owner 或 phase。仅有“predicate 已 exact”没有任何单调性公理。

在 (24) 的 exponent box 内，取已经可由 typed \(3\)-prefix 相容的记录集

\[
P_0=\{(0,0),(1,0),(2,0)\},
\qquad
P_1=P_0\cup\{(3,2)\}.
\tag{36}
\]

把两个 source schemas 的 exact predicate 分别定义为 membership in \(P_0\) 与
membership in \(P_1\)。两者都有限、都只含 (24) 的实际因子、都包含同一 typed
\(3\)-prefix、都不命中目标。\(P_0\) 是 downset，而 \(P_1\) 不是：

\[
(3,1)\le(3,2),\qquad (3,2)\in P_1,qquad(3,1)\notin P_1.
\tag{37}
\]

所以从 finite exactness、factor admissibility、既有 prefix 和 target miss 不能逻辑
推出

\[
\boxed{\texttt{PROVENANCE\_PRESERVING\_DIVISOR\_CLOSURE}.}
\tag{38}
\]

这是一对满足现有弱公理而 closure 真值不同的严格模型，不是“尚未搜索到证明”。

即使额外假设 set-level downclosure，membership 仍不保证 typed owner admission，
也不决定容量。就在 downclosed 的 \(P_0\) 上，可把 \((2,0)\) 投到 fresh owner，
也可把它投到 \((1,0)\) 的既有 owner。两张图的 membership domain 完全相同，owner
image 的基数分别为 \(3\) 与 \(2\)；后一张图会违反 typed owner-map 单射。这正说明
membership 本身既不能判定 admission，也不能决定物理容量，必须另证 raw/typed
owner map 的单射、charge 与 prefix 条件。

## 7. 统一选择器分派

~~~text
fixed Type II candidate fiber (D_*, A)
  -> factor N = p + 4 A D_*
  -> SAME_FIBER_FACTOR_BOX_EXACT
  -> target -1 mod 4D_* hit?
       yes: construct (A, C_*, K, B) Type II certificate
       no: SAME_FIBER_TYPEII_FACTOR_TARGET_MISS
            -> target-visible character if available
  -> for each quotient eta and prime-power coordinate q^e:
       record arithmetic depth e
       record quotient capacity min(e, ord(eta(q))-1)
       eta(q)=1: record neutral multiplicity e+1, never a new role
       q not dividing |H|: Q_PRIMARY_ROLE_RANK_ZERO
  -> embedding into an F/G successor requested?
       require exact physical-source predicate + record-to-state map
       require typed owner/charge map independently
       do not infer divisor or owner closure from contract exactness
       only then continue to FIBER_REALIZED -> E4 -> E5
~~~

对 (23)，算术 factor-depth 已是 \((4,2)\)，所以 ambient \(83^2\) 方向不存在算术
缺层；真正剩余的是把 neutral factor records 绑定到 F/G 的 physical source、owner 与
state realization。另一方面 (33) 严格终止了“寻找 \(C_{83}\) 角色来支付这两层”的
路线。下一步若仍走该控制，只能构造 typed neutral-cargo owner map，或利用 exact
factor target miss 生成另一个可提升的状态；不能继续把 \(83\)-factor height 当作
\(83\)-primary rank。

## 聚焦验证

~~~bash
python3 reproductions/type_ii_same_fiber_factor_box_neutral_role_capacity.py --verify
~~~

验证器只检查 (23)--(37) 的十五因子盒、残数单射、\(C_3\) fiber 张量、
\(\chi_{-8}\)、\(83\)-primary rank-zero 条件及 closure 双模型；不运行历史范围测试，
也不验证 F/G physical-source predicate、owner map、state realization 或 E4/E5。
