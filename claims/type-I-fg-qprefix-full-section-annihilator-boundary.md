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
  N=3^4*83^2 的完整 ambient divisor
  fiber 截面有 6 点、Fourier 能量 540。二次角色 chi_{-8} 在全部因子像上平凡而在
  -1 上取 -1，给出 target-visible C2 ambient-divisor character certificate；它不
  代替 exact physical-source predicate。保持真实来源
  (a,h)=(1,83) 的所有严格低模数 Type II 候选又在统一 source-CRT 剩余 16 mod 83
  的 G2 门全空。因此该控制产生 ambient 有限群对偶证书和严格整数提升障碍，但不
  自动产生 physical-source relay 或 E4。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fg-qprefix-block-bound-first-overflow-terminal
  - type-I-fg-exterior-grassmann-slice-successor-descent
  - type-I-fg-exact-successor-source-overhead-rank-slack-selector
  - type-II-annihilator-congruence-fiber-lift-criterion
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

## 3. actual-F full-C3 控制的 ambient divisor 截面

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

完整 ambient divisor fiber 是

\[
\mathcal P_N
=\{3^a83^b\bmod728:0\le a\le4,\ 0\le b\le2\}.
\tag{12}
\]

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
\mathcal P_N\cap K
=\{1,27,57,83,337,363\},
\tag{14}
\]

\[
\boxed{
S_w(\mathcal P_N)
=\{365,391,645,671,701,727\}.}
\tag{15}
\]

第一个被前缀遗漏的 kernel divisor 已经是 \(27\)。因此 (3) 在这里严格失败，
(11) 只能登记为 `PREFIX_LOCAL_KERNEL_SECTION`。对 \(K\) 上的指示函数，去掉平凡
角色后的 Parseval 能量为

\[
|S_w(\mathcal P_N)|
\bigl(|K|-|S_w(\mathcal P_N)|\bigr)
=6(96-6)=540,
\tag{16}
\]

而不是 singleton 的 \(1(96-1)=95\)。

## 4. ambient divisor fiber 的显式 target-visible 角色

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

所以它在全部 ambient divisor images 生成的群上平凡，却看见目标。对 ambient 截面，

\[
\boxed{
\sum_{k\in S_w(\mathcal P_N)}
\overline{\chi_{-8}(k)}=-6.}
\tag{20}
\]

于是 prefix-local singleton 被规范升级为
`FULL_AMBIENT_DIVISOR_FIBER_TARGET_VISIBLE_C2_CHARACTER`。这是对完整 divisor
候选超集的 exact finite-group separation。若另证每个 physical source image 都落在
该超集内，该角色也必在真实 source images 上平凡；但这仍不证明 exact physical-source
predicate、record-to-state/owner 映射或 Type I/II 整数后继。

## 5. 保持 \(h=83\) 的严格低模数提升为空

若继续保存真实 source record \((a,h)=(1,83)\)，则任意严格低模数 Type II
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

其中没有一项模 \(83\) 等于 \(16\)。因此该 ambient-divisor \(C_2\) 角色控制下，
全部 provenance-preserving strict low-modulus Type II lifts 已在 G2 source-CRT 门由

\[
\boxed{
\texttt{AMBIENT\_DIVISOR\_CHARACTER\_H83\_G2\_SOURCE\_CRT\_EMPTY}}
\tag{23}
\]

关闭。式 (23) 不排除换来源、换分母或其它直接终端；同一 \(p\) 已有独立的 Type II
终端，所以这里只声明局部整数提升障碍。

## 6. 选择器分派与边界

~~~text
typed q-prefix target miss
  -> compute PREFIX_LOCAL_KERNEL_SECTION
  -> enumerate the complete ambient divisor fiber
  -> compute AMBIENT_DIVISOR_KERNEL_SECTION / target-visible character
  -> exact physical-source predicate + record maps proved?
       yes: restrict to the exact physical source image
            -> KERNEL_SECTION_SOURCE_COMPLETE?
                 yes: exact section equality may enter state realization
                 no: replace prefix statistic by exact physical-source section
       no: retain ambient-divisor evidence only
  -> provenance-preserving integer lift gate
       pass: continue through FIBER_REALIZED + E4 + E5
       fail: typed integer-lift obstruction; no recursive edge
~~~

本定理真正增加的是从 prefix statistic 到任一已声明完整集合截面的充要门，以及同一
actual-F 控制上的完整 ambient-divisor character certificate。它同时证明：singleton
能量再大，也不能在未证明 physical source predicate 和被省略 records 时承担 exact
successor。

## 聚焦验证

~~~bash
python3 reproductions/type_i_fg_qprefix_full_section_annihilator_boundary.py --verify
~~~

验证器只重算 (10)--(23) 的单位群、完整 ambient divisor fiber、截面、角色、
divisor-generated group 和低模数来源候选；不验证 exact physical-source predicate，
也不运行历史测试。
