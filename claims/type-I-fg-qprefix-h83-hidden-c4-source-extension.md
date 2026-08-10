---
kind: claim
claim_id: type-I-fg-qprefix-h83-hidden-c4-source-extension
title: p=557281 的 83 中性 sheets 之隐藏 C4 商、源指数障碍与分层状态扩充
statement: >-
  设 H 为有限阿贝尔目标群、B<=H、c in H，并令 d_B(c) 为 cB 在
  <B,c>/B 中的阶。任何由有限源群 S 单独提供、保持乘法且实现 cB 的
  B-relative adapter 都迫使 d_B(c)|exp(S)；仅通过一个杀掉 c 的商角色记录状态，
  则不能区分同一 base record 的不同 c-sheets。对 p=557281 的 H=U(728)、
  B=<3>、c=83，有 <3,83>/<3>≅C4。四次角色
  psi_4(u)=(u mod 13)^3 杀掉 3 并把 83 送到阶四元素，因而精确区分三张
  b=0,1,2 sheets；chi_2 在 3 与 83 上都取 -1，不下降到该商，只看见其相对
  C2 影子。actual-F 源群 U(199)≅C198 没有阶四角色，且其唯一 C2 角色不能提升为
  C4，所以当前 factor-2 named edge 连相对 C2 相位也不匹配。关系格精化进一步证明：
  原状态中任何包含 b=1 sheet、并保持所选 records 全部源关系的 finite partial adapter
  也严格不可能；不保持关系的 set map 即使存在也不能把 psi_4 拉回为同态 source
  character 或规范 role column，不能支付 C4 角色容量。
  若要求忠实乘法状态，至少须增加一个四阶
  方向；相对 C4 扩充的最小 index 为 2，而在旧源上平凡的外部 C4 坐标或完整
  C6×C4 满射的最小 index 为 4，U(199)×C4 达到后一界，但不是 physical-source
  receipt。严格因子重图表中
  能承载 C4 的 D'|182 恰为 13,26,91；最小 D'=13 已由 A=1、h=103 给出一张直接
  Type II 终端。该结果把剩余接口整理成四层顺序门：eta-key identity loss、
  原状态 whole/partial relation-preserving transport obstruction、set-theoretic physical
  cargo adapter 未证且不计角色容量，以及后者可选的 full-C4 state completion。后续
  同基三-sheet容量已被严格证明为零；一个保持 active pair 的全盒单射 affine 扩展则
  构造出跨基 2->929->182 的 owner-window 83-height ladder，把剩余缺口精确移到
  cross-base physical cargo contract。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fg-qprefix-h83-typed-owner-no-go
  - type-I-fg-qprefix-depth3-replacement-lineage
  - type-II-same-fiber-factor-box-neutral-role-capacity
  - type-II-dyadic-relation-quotient-unit-group-exponent-gate
  - type-I-II-fg-universal-finite-source-map-completion
  - type-I-fg-partial-prefix-relation-snf-physical-capacity-gate
  - type-I-fg-qprefix-h83-common-base-capacity-cross-base-ladder
topics:
  - type-I
  - F-state
  - q-prefix
  - neutral-cargo
  - quartic-character
  - higher-primary-role
  - source-exponent
  - state-extension
  - strict-obstruction
  - capacity-map
  - type-II-terminal
  - proof-program
sources:
  - claim: type-I-fg-qprefix-h83-typed-owner-no-go
    role: exact-neutral-sheets-and-current-grammar-no-go
  - claim: type-I-fg-qprefix-depth3-replacement-lineage
    role: active-q3-block-and-frozen-factor-2-edge
  - claim: type-II-same-fiber-factor-box-neutral-role-capacity
    role: exact-Type-II-factor-records
  - claim: type-II-dyadic-relation-quotient-unit-group-exponent-gate
    role: C4-unit-group-exponent-source-switch-gate
  - claim: type-I-II-fg-universal-finite-source-map-completion
    role: physical-source-contract-boundary
  - claim: type-I-fg-partial-prefix-relation-snf-physical-capacity-gate
    role: finite-selected-record-relation-no-go-and-raw-prefix-classification
  - claim: type-I-fg-qprefix-h83-common-base-capacity-cross-base-ladder
    role: common-base-capacity-no-go-and-cross-base-owner-window-ladder
  - reproduction: reproductions/type_i_fg_qprefix_h83_hidden_c4_source_extension.py
    role: focused-relative-C4-source-obstruction-state-extension-and-terminal-verification
visibility: public
last_checked: '2026-08-11'
---

# \(p=557281\) 的 \(83\) 中性 sheets 之隐藏 \(C_4\) 商、源指数障碍与分层状态扩充

## 1. 相对 transport 阶的必要条件

令 \(S,H\) 为有限阿贝尔群，\(B\le H\)，\(c\in H\)。定义

\[
Q_B(c)=\langle B,c\rangle/B,
\qquad
d_B(c)=\operatorname{ord}_{Q_B(c)}(cB).
\tag{1}
\]

所谓 **\(B\)-relative source-visible multiplicative adapter**，是一个群同态

\[
\rho:S\longrightarrow Q_B(c)
\tag{2}
\]

且某个源元素被送到 \(cB\)。若 \(\rho(s)=cB\)，则

\[
d_B(c)=\operatorname{ord}(\rho(s))\mid\operatorname{ord}(s)\mid\exp(S).
\tag{3}
\]

所以得到严格必要条件

\[
\boxed{d_B(c)\mid\exp(S).}
\tag{4}
\]

若 (4) 失败，则所有在**整个 \(S\) 的群关系上**下降为 (2) 的 adapter 同时失败；
这不是某个 owner 菜单为空，而是该同态型源状态指数不足。它不排除只定义在有限
exponent-box 或三项前缀上、并用 record provenance 区分 sheets、但不保持
\(c^3,c^4\) 全部乘法关系的 partial adapter。

还有一个独立的 state-exactness 门。设 \(\eta:H\to A\) 满足 \(\eta(c)=1\)，并且
对某个 \(r\in B\)，目标 residues

\[
r,rc,\ldots,rc^{m-1}
\tag{5}
\]

彼此不同。若 key 只保存 base record \(r\) 与 \(\eta(rc^b)\)，却不保存
\(b\) 或其它补充坐标，则 (5) 的所有记录具有同一个 key。因此不能从这个
\(\eta\)-only key 恢复 sheet identity 或目标 residue。这个结论本身既不声称
record-to-state map 必须单射，也不声称 (5) 已是 physical F/G receipts；只有未来
合同要求 key 恢复这些不同 receipts 时，它才成为 physical collision。若补充坐标还
要求保持乘法并忠实记录完整 \(cB\) 方向，它必须含有阶 \(d_B(c)\) 的元素。

## 2. \(83\) 方向是隐藏的 \(C_4\) 商

固定

\[
H=U(728),\qquad B=\langle3\rangle,\qquad c=83.
\tag{6}
\]

直接计算

\[
\operatorname{ord}_{728}(3)=6,\qquad
\operatorname{ord}_{728}(83)=4,
\tag{7}
\]

并且

\[
\langle3\rangle=\{1,3,9,27,81,243\},
\qquad
\langle83\rangle=\{1,83,337,307\}.
\tag{8}
\]

两个循环群的唯一可能非平凡交点只能是二阶元，但

\[
3^3=27\not\equiv337=83^2\pmod{728}.
\tag{9}
\]

故

\[
\boxed{
\langle3,83\rangle
=\langle3\rangle\times\langle83\rangle
\simeq C_6\times C_4,
\qquad
Q_B(83)\simeq C_4.}
\tag{10}
\]

特别地，\(d_B(83)=4\)。ambient exponent defect \((0,2)\) 不是两个独立的
\(C_2\) requests；它来自一个阶四方向的三项前缀 \(1,c,c^2\)。

## 3. 忠实四次角色与 \(\chi_2\) 的精确边界

在 \(U(13)\) 中定义

\[
\psi_4(u)=(u\bmod13)^3
\in\mu_4(13)=\{1,5,8,12\}.
\tag{11}
\]

以下用唯一同构
\[
\iota:\mu_4(13)\longrightarrow\{1,i,-1,-i\},
\qquad \iota(8)=i,
\tag{11a}
\]
把有限域中的四次单位根解释为通常的复角色值；特别地
\(\iota(12)=-1\)。

因为三次幂是群同态，且

\[
\psi_4(3)=3^3=1,\qquad
\psi_4(83)=5^3=8,\qquad
\operatorname{ord}_{13}(8)=4,
\tag{12}
\]

所以 \(\psi_4\) 在 \(B\) 上平凡，并诱导同构

\[
\boxed{Q_B(83)\overset{\sim}{\longrightarrow}\mu_4(13).}
\tag{13}
\]

对十二点积块

\[
P=\{3^a83^b:0\le a\le3,\ 0\le b\le2\}
\tag{14}
\]

有

\[
\psi_4(3^a83^b)=8^b\in\{1,8,12\}.
\tag{15}
\]

因此 (15) 精确区分三张 sheets。另一方面，既有

\[
\eta(u)=(u\bmod13)^4
\tag{16}
\]

满足 \(\eta(83)=1\)，故对每个固定 \(a\)，三条 records 在 \(\eta\)-state 中
完全碰撞；这给出

\[
\boxed{\texttt{P557\_ARITHMETIC\_SHEET\_IDENTITY\_NOT\_RECOVERABLE\_FROM\_ETA\_KEY}.}
\tag{17}
\]

二次角色 \(\chi_2(u)=(2/u)\) 只能作为较弱诊断。事实上

\[
\chi_2(3)=\chi_2(83)=-1,
\tag{18}
\]

所以 \(\chi_2\) 不在 \(B\) 上平凡，不能下降到 (10)。只有固定同一个
\(3^a\) 后的相对比值

\[
\frac{\chi_2(3^a83^b)}{\chi_2(3^a)}=(-1)^b
=\iota\!\left(\psi_4(3^a83^b)\right)^2
\tag{19}
\]

看见 \(C_4\) 的唯一 \(C_2\) 商。它把 \(b=0\) 与 \(b=2\) 折叠，不能替代
\(\psi_4\)。

## 4. actual-F 源群的四阶指数障碍

当前 actual-F 状态的源群为

\[
S=U(199)=\langle3\rangle\simeq C_{198}.
\tag{20}
\]

它的二进 Sylow 群是 \(C_2\)，所以

\[
v_2(\exp S)=1<2=v_2(d_B(83)).
\tag{21}
\]

由 (4)，不存在由当前 \(S\) 单独提供并命中 \(83B\) 的全源关系同态型乘法
adapter。特别地，若
某个同态 \(\Phi:S\to U(728)\) 满足 \(\Phi(s)=83\)，则

\[
1=\Phi(s^{198})=83^{198}=83^2=337\not\equiv1\pmod{728},
\tag{22}
\]

矛盾。因此

\[
\boxed{\texttt{P557\_WHOLE\_SOURCE\_RELATION\_HOMOMORPHIC\_C4\_ADAPTER\_NO\_GO}.}
\tag{23}
\]

角色侧给出同一个障碍的更细版本。以加法坐标写 \(C_4\)，任意
\(C_{198}\to C_4\) 同态把生成元送到满足 \(198y=0\pmod4\) 的元素，所以

\[
\operatorname{Hom}(C_{198},C_4)=\{y=0,2\}\simeq C_2.
\tag{24}
\]

它们的像都没有本原四阶元素。并且沿 \(C_4\to C_2\) 的模二投影，(24) 的两个
元素都送到零，故

\[
\boxed{
\operatorname{Hom}(C_{198},C_4)
\longrightarrow\operatorname{Hom}(C_{198},C_2)
\text{ 是零映射}.}
\tag{25}
\]

所以当前源群唯一的非平凡 \(C_2\) 角色也不能提升为 \(C_4\) 角色。

对冻结的 factor-\(2\) named edge，\(2=3^{106}\pmod{199}\)。源端唯一
\(C_2\) 角色在该 edge 上的增量是 \(106\equiv0\pmod2\)，而目标第一张
\(83\)-sheet 的相对相位由 \(\psi_4^2(83)=-1\) 给出，即非零。故还有更窄的

\[
\boxed{\texttt{P557\_CURRENT\_FACTOR2\_EDGE\_C2\_SHEET\_ADAPTER\_NO\_GO}.}
\tag{26}
\]

改用 factor-\(11\) 或 factor-\(2083\) 会改变 named edge、source line、owner 与
occurrence 合同；而且最多只产生 \(C_2\)，仍不能闭合 (13)。

式 (23) 本身的量词止于整个源群上的同态。若一个仅对有限 physical candidate records
定义的映射
\[
T:\mathcal U_{\rm finite}\times\{0,1,2\}\longrightarrow\mathcal V
\tag{23a}
\]
还要把 \(\psi_4\) 拉回源状态，则它至少必须在所选 records 生成的子群上保持全部
关系。有限关系格判据见
[partial-prefix relation-SNF 与物理容量门](type-I-fg-partial-prefix-relation-snf-physical-capacity-gate.md)。
任取服务 \(b=1\) sheet 的原状态 record \(x\in S=C_{198}\)，都有

\[
198x=0,
\qquad
198\cdot1\equiv2\not\equiv0\pmod4.
\tag{23b}
\]

所以不仅 whole-source homomorphism 不存在，任何原状态 finite selected-record
subgroup 上的 relation-preserving \(C_4\) adapter 也严格失败：

\[
\boxed{
\texttt{P557\_ORIGINAL\_STATE\_RELATION\_PRESERVING\_C4\_ADAPTER\_INCLUDING\_B1\_NO\_GO}.}
\tag{23c}
\]

仍未排除的是不保持 (23b)、只显式保留 \(b\) 或其它 provenance 的 set-theoretic
physical map。当前没有这样的 exact F/G construction，所以必须另记
\[
\boxed{\texttt{P557\_SET\_THEORETIC\_PARTIAL\_PREFIX\_PHYSICAL\_ADAPTER\_UNPROVED}.}
\tag{23d}
\]

下游关系格定理进一步在 actual-F exponent box 中完整分类出 \(51\) 条 labelled
三点 raw \(83\)-chains：三种 step pairs 的数量为 \(27,12,12\)，共同压成 \(27\) 个
image-level triples，并覆盖 \(105\) 条 distinct raw records。每类内部均两两不交；
跨类同起点的 lifts 共享首尾，而 \(27\) 条常步长链给每个 image triple 一个不交代表。
全部可行 lifts 的 factor-\(2\) 坐标均为零，所以现有 active
source line \(\mathcal L(z)=14924+89544z_{(2)}\) 把每条链压成同一个 integer row。
后续
[同基容量零与跨基 ladder](type-I-fg-qprefix-h83-common-base-capacity-cross-base-ladder.md)
构造了保持该 active pair 的 full-box 单射 affine 扩展；它保存全部 raw \(83\)-edges
的完整 \(C_9\) phase，并把一条合法 chain 映到 \(2,929,182\)。所以 raw set skeleton、
integer 分离和 selected-chain 的跨基 owner-window state injection 已实现；但共同
target-compatible base 的三-sheet容量严格为零，(23d) 现在只指 cross-base exact
physical membership、product synthesis、owner/charge 与 E4/E5 的提升。

即使未来构造 (23d)，它也不能在原 \(S\) 上把 \(\psi_4\) 拉回为同态 character、形成
规范 evaluation column 或登记 faithful \(C_4\) price；它只能作为独立
cargo/terminal mechanism 保持
`UNPRICED`。若新增 provenance 本身带四阶群坐标，则 source state 已经扩充，应进入
第 5 节，而不是把新坐标称为原状态 partial adapter。

## 5. 相对与完整联合群的分层代数扩充

相对商 (10) 要求任何忠实乘法 state 至少含一个阶四元素。若要求把当前
\(S=C_{198}\) 嵌入一个扩充群 \(\widetilde S\)，仅实现相对 \(C_4\) 已迫使
\(2\mid[\widetilde S:S]\)。若还要求满射到完整联合群
\(\langle3,83\rangle\)（其二进 Sylow 阶为 \(8\)），则拉格朗日定理给出

\[
24\mid198[\widetilde S:S]
\quad\Longrightarrow\quad
4\mid[\widetilde S:S].
\tag{27}
\]

仅实现相对 \(C_4\) 时，index \(2\) 下界也可达到：取
\[
\widetilde S_{\rm rel}=C_{396}=\langle t\rangle,\qquad
S=\langle t^2\rangle,
\tag{27a}
\]
并把 \(t\) 送到 \(C_4\) 的生成元。其在旧 \(S\) 上只给出 \(C_2\) 影子，而新陪集
给出本原四阶相位。这不是一个在旧源上平凡的独立 cargo coordinate。

若要求新增坐标在旧 \(S\) 上平凡，即
\(\widetilde S/S\twoheadrightarrow C_4\)，则 index 已须被 \(4\) 整除；要求满射完整
联合群时也由 (27) 得到同一下界。这个 index \(4\) 下界可达到。取

\[
\widetilde S=S\times C_4,
\tag{28}
\]

令 \(g=3\bmod199\) 生成 \(S\)，\(e\) 生成外部 \(C_4\)，定义

\[
\widetilde\Phi(g^n,e^b)=3^n83^b\pmod{728}.
\tag{29}
\]

因为 \(6\mid198\)、\(\operatorname{ord}_{728}(83)=4\) 及 (9)，(29) 良定义并满射
到 \(C_6\times C_4\)，核的阶为 \(33\)。其在
\(0\le n\le3,0\le b\le2\) 上给出十二个不同像。因此

\[
\boxed{\texttt{P557\_ABSTRACT\_C4\_LABELLED\_STATE\_EXTENSION\_REALIZED}.}
\tag{30}
\]

式 (30) 只是一张“外部坐标在旧源上平凡且满射完整联合群”意义下 index \(4\)
最小的**代数状态模型**。其中 \(g^n\) 不是既有
q-prefix source rows 或 frozen exponent-box records；(29) 没有给出 exact physical
predicate、integer source line、record-to-state map、owner、occurrence 或 E4/E5。
所以它不能登记为 physical adapter，也不能把当前 `UNPRICED` 状态改为 price \(2\)。

## 6. 四层顺序门与一个 role-guided Type II 正控制

对当前三张 sheets，按顺序记录：

1. **ETA_KEY_IDENTITY_LOSS**：只保留 (16) 时，由 (17) 无法恢复 sheet identity；
2. **ORIGINAL_STATE_RELATION_TRANSPORT_OBSTRUCTED**：whole-source 同态由
   (23)--(25) 失败；即使只选有限 records，只要要拉回忠实 \(C_4\) 角色，(23b)--(23c)
   仍严格失败；
3. **SET_THEORETIC_PARTIAL_PREFIX_PHYSICAL_ADAPTER_UNPROVED**：允许有限 record map
   只显式保留 \(b=0,1,2\) 而不保持原 source relations；\(51\) 条 labelled raw
   chains 已完整分类为 \(27,12,12\) 三类；全盒单射 integer line、full-\(C_9\)
   phase 与跨基 \(83\)-height ladder 已构造，而共同基三-sheet容量严格为零。
   cross-base exact physical predicate、fixed-factor product synthesis、
   owner/occurrence、共同稳定子与 E4/E5 仍未证明；即使构造也不得支付 faithful
   \(C_4\) role capacity；
4. **FULL_C4_STATE_EXTENSION_OPTIONAL**：若要求完整乘法闭合，可选用 (30) 的外部
   \(C_4\) state；它仍只证明代数可行，physical 合同与最终稳定子未证。

前两项是可以同时成立的诊断门；第三项是尚待构造的非角色 physical cargo 路线，
第四项是在要求忠实乘法角色时的显式 state-extension 路线，并非四个互斥分支。
这四层不改变固定
\((D_*,A)=(182,1)\) 的完整十五因子 target miss；即使第三或第四支物理实现，当前纤维仍无
\(h\equiv-1\pmod{728}\)，所以 `FIBER_REALIZED` 仍为假。

四阶角色还能给出一个有限 source-switch 过滤。对严格因子 \(D'\mid182\)，既有
单位群指数门说 \(U(4D')\) 能承载目标 \(C_4\) 的必要且无标签时充分条件是

\[
4\mid\lambda(4D').
\tag{31}
\]

逐因子计算得到

\[
\boxed{D'\in\{13,26,91\}.}
\tag{32}
\]

最小候选 \(D'=13\) 不只通过指数门，而且直接终止。取

\[
A=1,\qquad C=13,\qquad h=103=4ACK-1,\qquad K=2.
\tag{33}
\]

有

\[
p+4A^2C=557333=7\cdot103\cdot773,\qquad
103\equiv-1\pmod{52},
\tag{34}
\]

以及

\[
B=\frac{2p+1}{103}=10821>A.
\tag{35}
\]

故得到新的显式 Type II 证书

\[
\boxed{
\frac4{557281}
=\frac1{140673}
+\frac1{14489306}
+\frac1{156788780226}.}
\tag{36}
\]

这里 \(140673=BD'\)、\(14489306=pD'K\)、
\(156788780226=pBCK\)。式 (36) 是 role-guided strict-divisor menu 的直接终端正控制，
不是从 (30) 推出的 physical successor；同一 \(p\) 先前已有其它终端不影响这张新
证书的有效性。

## 7. 对统一选择器的精确更新

当前 \((0,2)\) defect 不再派往“继续寻找 \(83\)-primary role”，也不能只凭
\(\chi_2(83)=-1\) 派往一个 \(C_2\) owner。正确顺序是：

```text
eta-neutral sheets
  -> compute relative transport group <B,c>/B
  -> C4 quotient and faithful quartic character psi4
  -> eta-only key: sheet identity is not recoverable
  -> whole-source homomorphic C4: exponent / character-lift no-go
  -> try role-compatible strict-divisor source-switch (p557: D'=13 terminal)
  -> otherwise common-base three-sheet capacity: zero
  -> cross-base affine ladder exists, require exact physical cargo contract
  -> optionally embed it in a full external C4 state
  -> only after a physical receipt: reprice, check FIBER_REALIZED, E4 and E5
```

该更新产生了 relative-order capacity map、两个严格 no-go、分层最小代数扩充和一张
Type II 短证书；它仍未证明 partial-prefix physical adapter，也未证明任意核心素数
都存在相同的 \(C_4\) source-switch 或 full-\(C_4\) state。

## 聚焦验证

```bash
python3 reproductions/type_i_fg_qprefix_h83_hidden_c4_source_extension.py --verify
```

验证器只重算 (7)--(15)、\(\chi_2\) 边界、源端 Hom/edge 相位、十二点碰撞、
抽象扩充、(32) 和 (36)；不运行历史扫描或已有测试。
