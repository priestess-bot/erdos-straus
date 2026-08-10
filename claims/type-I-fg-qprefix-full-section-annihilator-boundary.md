---
kind: claim
claim_id: type-I-fg-qprefix-full-section-annihilator-boundary
title: F/G q-prefix 的 ambient divisor-kernel 截面、physical-source 完备门与角色边界
statement: >-
  设 eta:H->Q、K=ker eta，w 属于 K 且 w^2=1。任意源集 X 的目标核截面
  S_w(X)={k in K:wk in X} 精确等于 w(X intersect K)。因此前缀 B 的局部截面
  等于完整源集 P 的截面，当且仅当 (P minus B) intersect K 为空；prefix singleton
  本身不能确定 ambient kernel slice、exact physical-source realization 或 E4。对
  p=557281 的 typed full-C3 控制，B={1,3,9} 的局部截面确为 {727}，但
  N=3^4*83^2 的完整同纤维算术因子盒截面有 6 点、Fourier 能量 540。唯一分解和
  Type II 因子回译使该十五点盒成为固定 (D_*,A)=(182,1) 的 exact factor contract；
  二次角色 chi_{-8} 在全部因子像上平凡而在 -1 上取 -1，因而给出 exact same-fiber
  Type II target-miss character certificate。它仍不代替 F/G exact physical-source
  predicate。若把算术因子块 (a,h)=(1,83) 作为 retained source 输入，所有严格低模数
  Type II 候选又在统一 source-CRT 剩余 16 mod 83 的 G2 门全空。因此该控制产生固定
  Type II 因子合同的精确对偶 no-hit 与条件性 provenance-preserving 提升障碍，但不
  自动产生 F/G physical-source relay 或 E4。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fg-qprefix-block-bound-first-overflow-terminal
  - type-I-fg-exterior-grassmann-slice-successor-descent
  - type-I-fg-exact-successor-source-overhead-rank-slack-selector
  - type-II-annihilator-congruence-fiber-lift-criterion
  - type-II-same-fiber-factor-box-neutral-role-capacity
topics:
  - type-I
  - type-II
  - F-state
  - q-prefix
  - kernel-section
  - source-completeness
  - annihilator
  - Fourier
  - exact-successor
  - strict-obstruction
  - proof-program
sources:
  - claim: type-I-fg-qprefix-block-bound-first-overflow-terminal
    role: actual-F-full-C3-prefix-control
  - claim: type-I-fg-exterior-grassmann-slice-successor-descent
    role: exact-kernel-successor-contract
  - claim: type-II-annihilator-congruence-fiber-lift-criterion
    role: provenance-preserving-low-modulus-lift-gate
  - claim: type-II-same-fiber-factor-box-neutral-role-capacity
    role: exact-same-fiber-factor-contract-and-neutral-role-boundary
  - reproduction: reproductions/type_i_fg_qprefix_full_section_annihilator_boundary.py
    role: focused-prefix-ambient-divisor-section-character-and-source-crt-verification
visibility: public
last_checked: '2026-08-10'
---

# F/G q-prefix 的 ambient divisor-kernel 截面、physical-source 完备门与角色边界

## 1. 前缀截面的完备性充要门

令 \(H\) 为有限阿贝尔群，

\[
\eta:H\longrightarrow Q,
\qquad K=\ker\eta,
\]

并固定 \(w\in K\)、\(w^2=1\)。对任意 \(X\subseteq H\)，定义目标核截面

\[
S_w(X)=\{k\in K:wk\in X\}.
\tag{1}
\]

则有精确恒等式

\[
\boxed{S_w(X)=w(X\cap K).}
\tag{2}
\]

事实上，乘以 \(w\) 是 \(K\) 上的对合；又因 \(w\in K\)，对 \(k\in K\) 有
\(wk\in K\)。所以 \(wk\in X\) 当且仅当 \(wk\in X\cap K\)，再乘一次 \(w\)
即得 (2)。

特别地，若前缀 \(B\subseteq\mathcal P\subseteq H\)，则

\[
\boxed{
S_w(B)=S_w(\mathcal P)
\quad\Longleftrightarrow\quad
(\mathcal P\setminus B)\cap K=\varnothing.}
\tag{3}
\]

若再有 \(1\in B,w\notin B\)，则

\[
S_w(B)=\{w\}
\quad\Longleftrightarrow\quad
B\cap K=\{1\}.
\tag{4}
\]

式 (3) 是对**已经声明的完整集合** \(\mathcal P\) 的精确充要门。只有另行证明
\(\mathcal P\) 恰为 physical source image，它才可登记为
`KERNEL_SECTION_SOURCE_COMPLETE`；只枚举一个 ambient divisor superset 还不能通过
该门。通过后，prefix-local section 才能替代完整 source section。若另有真实
kernel-filtered records 满足

\[
1\in\Gamma(\mathcal U_K)
\subseteq\Gamma(\mathcal U)\cap K
\tag{5}
\]

且完整截面确为 singleton，则 (5) 自动升级为

\[
\Gamma(\mathcal U_K)=\Gamma(\mathcal U)\cap K=\{1\}.
\tag{6}
\]

这只补足 exact-kernel 合同中的 source-set 等式。允许状态族中的 realization、记录
provenance、branch/certificate lift、marked E4 与不可重置 E5 仍须独立证明。

## 2. 仅凭 prefix singleton 的 ambient-completion no-go

把可观察的前缀数据记为

\[
\mathfrak d=(H,\eta,B,w,S_w(B)).
\tag{7}
\]

一个 ambient completion 是任意满足 \(B\subseteq\mathcal P\subseteq H\) 的集合。
不存在只读取 \(\mathfrak d\) 而对所有 ambient completions 都正确推出

\[
\mathcal P\cap K=\{1\}
\tag{8}
\]

的规则。只需固定同一个 \(\mathfrak d\)，并取

\[
\mathcal P_0=B,
\qquad
\mathcal P_1=B\cup\{v\},
\qquad v\in K\setminus B.
\tag{9}
\]

两者的 prefix datum 完全相同，但第二个 completion 的 ambient kernel slice 还含
\(v\)。所以 prefix singleton 不能单独确定 \(\Gamma(\mathcal U)\cap K\)。而
\(\Gamma(\mathcal U_K)=\Gamma(\mathcal U)\cap K\) 本来就是另一条必须独立证明的
filtered-record 等式；因此 prefix 数据更不能单独输出
`SELECTED_SOURCE_STATE_REALIZATION` 或以它为前提的 E4。

还有一个独立的商 no-go。若同态 \(f:K\to J\) 试图用 \(f(w)=1\) 杀掉 singleton，
则 \(f(w)=f(1)\) 已落入过滤后 source image；目标缺失立即消失。因此“把 singleton
归一到单位元”不是 target-miss successor。正向方向只能保留 \(w\) 的非平凡像，或
限制到包含 \(w\) 的子群，再另做整数 realization。

## 3. actual-F full-\(C_3\) 控制的同纤维因子截面

沿用 actual-F 控制

\[
p=557281,\qquad D_*=182,\qquad 4D_*=728,
\]

\[
N_x=p+4D_*=558009=3^4\cdot83^2,
\qquad
\eta(u)=(u\bmod13)^4:U(728)\to C_3,
\]

并取 \(w=-1=727\)。有

\[
|U(728)|=288,\qquad |K|=96.
\tag{10}
\]

前缀 \(B=\{1,3,9\}\) 满足

\[
B\cap K=\{1\},
\qquad
S_w(B)=\{727\}.
\tag{11}
\]

固定 Type II 参数 \((D_*,A)=(182,1)\) 的完整算术因子盒是

\[
\mathcal D_N
=\{3^a83^b\bmod728:0\le a\le4,\ 0\le b\le2\}.
\tag{12}
\]

唯一分解把这十五条 labelled records 双射到 \(N_x\) 的全部正因子；固定纤维 Type II
判据又证明，目标命中当且仅当其中一个因子等于 \(-1\bmod728\)。所以
\(\mathcal D_N\) 对固定 Type II factor search 是 exact contract。只有当它被拿来
近似 F/G physical source image 时，才应称为 ambient divisor superset。

因为 \(3\) 的 \(\eta\)-像阶为 \(3\)，而 \(83\equiv5\pmod{13}\) 且
\(5^4\equiv1\pmod{13}\)，所以

\[
3^a83^b\in K
\quad\Longleftrightarrow\quad
3\mid a.
\tag{13}
\]

从而

\[
\mathcal D_N\cap K
=\{1,27,57,83,337,363\},
\tag{14}
\]

\[
\boxed{
S_w(\mathcal D_N)
=\{365,391,645,671,701,727\}.}
\tag{15}
\]

第一个被前缀遗漏的 kernel divisor 已经是 \(27\)。因此 (3) 在这里严格失败，
(11) 只能登记为 `PREFIX_LOCAL_KERNEL_SECTION`。对 \(K\) 上的指示函数，去掉平凡
角色后的 Parseval 能量为

\[
|S_w(\mathcal D_N)|
\bigl(|K|-|S_w(\mathcal D_N)|\bigr)
=6(96-6)=540,
\tag{16}
\]

而不是 singleton 的 \(1(96-1)=95\)。

## 4. exact factor box 的 target-visible 角色及 F/G 边界

ambient kernel divisors 生成

\[
R_K=\langle27,83\rangle
=\{1,27,57,83,281,307,337,363\}
\simeq C_2\times C_4,
\tag{17}
\]

且 \(727\notin R_K\)。更直接地，在奇单位上取 Kronecker 角色

\[
\chi_{-8}(u)=\left(\frac{-2}{u}\right).
\tag{18}
\]

它在模 \(8\) 的 \(1,3\) 类取 \(1\)，在 \(5,7\) 类取 \(-1\)。由于
\(3\equiv83\equiv3\pmod8\)，

\[
\chi_{-8}(3)=\chi_{-8}(83)=1,
\qquad
\chi_{-8}(-1)=-1.
\tag{19}
\]

所以它在全部 factor images 生成的群上平凡，却看见目标。对完整因子截面，

\[
\boxed{
\sum_{k\in S_w(\mathcal D_N)}
\overline{\chi_{-8}(k)}=-6.}
\tag{20}
\]

于是 prefix-local singleton 被规范升级为
`EXACT_SAME_FIBER_TYPEII_FACTOR_TARGET_VISIBLE_C2_CHARACTER`。结合固定纤维 Type II
因子判据，这是对全部十五个算术因子的 exact target-miss certificate，不再只是候选
超集上的证据。若把同一集合用作 F/G source image 的上界，它仍只是一张 ambient
divisor box；角色分离不证明 exact physical-source predicate、record-to-state/owner
映射或 F/G 整数后继。

## 5. 保持 \(h=83\) 的严格低模数提升为空

若把 exact arithmetic factor block \((a,h)=(1,83)\) 作为 retained source 输入，
则任意严格低模数 Type II
候选 \(D'\mid182,D'<182,A\mid D'\) 必须满足统一来源合同

\[
x=AD'\equiv D_*a=182\equiv16\pmod{83}.
\tag{21}
\]

在平方自由与 \(A\mid D'\mid182\) 约束下，全部可能的 \(x=AD'\) 恰为

\[
\begin{aligned}
\{&1,2,4,7,13,14,26,28,49,52,91,98,169,196,338,\\
   &637,676,1183,8281\}.
\end{aligned}
\tag{22}
\]

其中没有一项模 \(83\) 等于 \(16\)。因此该 exact factor-box \(C_2\) 角色控制下，
全部 provenance-preserving strict low-modulus Type II lifts 已在 G2 source-CRT 门由

\[
\boxed{
\texttt{SAME\_FIBER\_FACTOR\_CHARACTER\_H83\_G2\_SOURCE\_CRT\_EMPTY}}
\tag{23}
\]

关闭。式 (23) 不排除换来源、换分母或其它直接终端；同一 \(p\) 已有独立的 Type II
终端，所以这里只声明局部整数提升障碍。

## 6. 选择器分派与边界

~~~text
typed q-prefix target miss
  -> compute PREFIX_LOCAL_KERNEL_SECTION
  -> enumerate the exact same-fiber Type II factor box
  -> target hit: Type II certificate
     target miss: SAME_FIBER_TYPEII_FACTOR_TARGET_MISS / character
  -> using the factor box as an F/G physical-source image?
  -> exact physical-source predicate + record maps proved?
       yes: restrict to the exact physical source image
            -> KERNEL_SECTION_SOURCE_COMPLETE?
                 yes: exact section equality may enter state realization
                 no: replace prefix statistic by exact physical-source section
       no: retain exact Type II factor result, but only ambient F/G source evidence
  -> provenance-preserving integer lift gate
       pass: continue through FIBER_REALIZED + E4 + E5
       fail: typed integer-lift obstruction; no recursive edge
~~~

本定理真正增加的是从 prefix statistic 到任一已声明完整集合截面的充要门，以及同一
actual-F 控制上的完整 same-fiber factor character certificate。它精确关闭固定 Type II
factor search，同时证明：singleton 能量再大，也不能在未证明 F/G physical source
predicate 和被省略 records 时承担 exact successor。

labelled exponent box 层面的最小补全已由后续
[kernel-depth 与 neutral-cargo 容量定理](type-I-fg-qprefix-kernel-depth-neutral-cargo-capacity.md)
精确计算为 \(\kappa=(3,2)\)。后续
[depth-\(3\) replacement lineage](type-I-fg-qprefix-depth3-replacement-lineage.md)
已在空的单请求 ledger 上构造 standalone fresh typed depth \(3\)，故从头选择该
witness 时可用 \(c_{\rm fresh}=(3,0)\)、\(\delta_{\rm fresh}=(0,2)\)。后续
[残余容量原子替换定理](type-I-fg-qprefix-atomic-replacement-capacity-normalization.md)
又证明精确孤立单请求快照可从 depth \(2\) 原子正规化到 depth \(3\)：旧 receipt
只保留 tombstone，active labelled prefix-depth 与 conditional ambient-kernel defect
分别取 \((3,0)\)、\((0,2)\)，两张账本仍不可叠加。
[同纤维因子盒与 neutral-role 容量定理](type-II-same-fiber-factor-box-neutral-role-capacity.md)
又证明算术 factor-depth 本来就是 \((4,2)\)，并且 \(83^2\) 是 exact neutral factor
cargo。进一步的
[\(q=83\) typed-owner no-go](type-I-fg-qprefix-h83-typed-owner-no-go.md)
严格排除现行 q-prefix grammar 下的 \(83\)-primary request；若保持当前 \(\eta:C_3\)、
既有 q=3 charge 与同一 state/grammar，则剩余两层的下一接口是附着于该 charge 的
neutral-product cargo。exact physical-source predicate 证明真实来源
也必须覆盖这些 records 之前，它们不是物理来源的无条件必要容量；
provenance-preserving divisor closure、owner maps 与 state realization 仍是显式未证门。

## 聚焦验证

~~~bash
python3 reproductions/type_i_fg_qprefix_full_section_annihilator_boundary.py --verify
~~~

验证器只重算 (10)--(23) 的单位群、完整 same-fiber factor box、截面、角色、
divisor-generated group 和低模数来源候选；不验证 exact physical-source predicate，
也不运行历史测试。
