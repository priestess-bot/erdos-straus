---
kind: claim
claim_id: type-I-overflow-cofactor-r-chart-support
title: overflow 的余因子支撑 r-图表候选与同图表正控制
statement: 设一个带完整 source/path 回放的 overflow 满足 pn=4Md+1、M=kp+r、1<=r<p、C=p-d、A|M。令 g=gcd(A,C)、a=A/g、A_C=lcm(A,C)=Ca，且 s=(4rd+1)/p、R_r=4r-s、K_r=rC。若 a|r、p<R_r、canonical_chart(p,A_C)=(R_r,K_r)、A<A_C<=B_p、floor(B_p/A_C)<floor(B_p/A)，并且来源是结构化的 fresh-source 默认入口或有经具名 adapter 重放的 charged-support 父回执，且 source/target F/G 纤维已重新验证，则 (p,R_M,K_M;A) 到 (p,R_r,K_r;A_C) 构成一条以 Sol(p) 恒等提升的 source-local normal-form candidate。其真正后继载体为 M_T=A_C，而非 r；令 C_T=r/a、d_T=p-C_T、n_T=4A_C-R_r，则 p n_T=4M_T d_T+1 且 K_r=M_T C_T。旧 S-to-T receipt 仍不是递归边；但若完整 parent 先到高锚 H、确定性 bundle 从 H 生成 transient S、且 macro E1--E4 与 Lambda_p E5 均重放通过，则正确的持久 H-to-T 宏可另行登记。p=1201 与 p=60913 的宏回放已闭合这种账本，但均被 terminal-first Type I 叶抢占，仍保持 analysis_evidence。
claim_status: computationally_reproduced
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
  - type-I-universal-p-source-capacity-anchor-orbit
  - type-I-overflow-determinant-fixed-n-dual-support-conflict
  - type-I-overflow-same-chart-support-promotion
  - denominator-escape-state-contract
topics:
- type-I
- overflow
- r-chart
- cofactor
- charged-support
- source-provenance
- well-founded-descent
- typed-receipt
- proof-boundary
sources:
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: cofactor r-chart constructor and contract verifier
  - result: reproductions/type-i-representation-dual-capacity-selector-results.json
    role: focused source/path, fibre, defect, and potential receipts
  - reproduction: reproductions/type_i_high_r_chart_two_anchor.py
    role: exact two-anchor high-carrier r-chart construction verifier
  - result: reproductions/type-i-high-r-chart-two-anchor-results.json
    role: p-1201 high-r source, fiber, and normal-form receipt
visibility: public
last_checked: '2026-08-06'
---

# overflow 的余因子支撑 r-图表候选与同图表正控制

## 条件与正规形

设一个 source-local overflow 状态满足

\[
pn=4Md+1,\qquad M=kp+r,\qquad 1\le r<p,\qquad
C=p-d,\qquad A\mid M.
\tag{1}
\]

令

\[
g=(A,C),\qquad a=A/g,\qquad A_C=\operatorname{lcm}(A,C)=Ca,
\]
\[
s=(4rd+1)/p,\qquad R_r=4r-s,\qquad K_r=rC.
\tag{2}
\]

接收门为

\[
a\mid r,\quad p<R_r,\quad
\operatorname{canonical\_chart}(p,A_C)=(R_r,K_r),
\tag{3}
\]
\[
A<A_C\le B_p:=\frac{(p-1)^2}{4},\qquad
\left\lfloor\frac{B_p}{A_C}\right\rfloor
<
\left\lfloor\frac{B_p}{A}\right\rfloor.
\tag{4}
\]

来源必须是经具名 adapter 重放的父 charged-support ledger 的 \(A>1\) 状态，或结构化
`universal_raw_default_entry_v1`：同一回执保存 universal raw source、\(A=1\)
anchor orbit、complete-excess bundle 和 `state_scope=fresh_source_tree_only`。
后者仅创建新鲜 source tree 的根，不能从任意 charged history 调用来删除既有 support；
`source_tree_scope` 必须写入 source/target state 并仅能沿边传播。

## 余因子升级

由 (1) 有 \(s=n-4kd\in\mathbb Z_{>0}\)，并且

\[
pR_r+1
=p(4r-s)+1
=4r(p-d)
=4rC
=4K_r.
\tag{5}
\]

关键等价式为

\[
A_C\mid K_r=rC
\quad\Longleftrightarrow\quad
Ca\mid rC
\quad\Longleftrightarrow\quad
a\mid r.
\tag{6}
\]

因此真正的后继 carrier 不是 \(r\)。令

\[
M_T=A_C,\qquad C_T=r/a,\qquad
d_T=p-C_T,\qquad n_T=4A_C-R_r.
\tag{7}
\]

则

\[
K_r=M_TC_T,\qquad
pn_T=4M_Td_T+1.
\tag{8}
\]

所以 \((p,R_r,K_r;A_C)\) 闭合回既有 \(A\mid M\) overflow 正规形。特别地，
`chart_relation=same_chart`（\(r=M\)）不是拒绝条件；它只表示图表数对不变，
但支撑和后继 determinant 已改变。

## 局部 E1--E5 与全局边界

| 条件 | 回执检查 |
|---|---|
| E1 | 重放 universal \(p\)-source、anchor、complete-excess bundle 及来源 determinant。 |
| E2 | 重算 (5)--(8)、canonical chart 和 \(A_C\mid K_r\)。 |
| E3 | 调用 `verify_overflow_cofactor_r_chart_normal_form`，重算 source、构造、target overflow 正规形、树域和来源 ledger。 |
| E4 | 取 \(W_S=W_T=\operatorname{Sol}(p)\)、\(\Phi=\mathrm{id}\)，并重算 source/target F/G；F/hit 重算同一全局定向的 \(D^-,D^+\)。 |
| E5 | 重算 (4) 的严格**局部** absorbed-support 势下降。 |

当前 v1 的两个完整来源控制满足上述局部检查，但统一状态合同要求 E5 支付全部未来递归
转移；后续 RESET 尚无 non-resetting phase scheduler。因此它们输出
`candidate_transition`、`recursive_edge_eligible=false`，而非
`verified_edge`。G 状态还必须另行提供分离角色型 E4，不能伪造空纤维的提升。

## 回放结果

| 来源 | 支撑更新 | 后继 \((M_T,C_T,d_T,n_T)\) | 纤维、势 | 状态 |
|---|---|---|---|---|
| \(p=73\), fresh \(A=1\) | \(1\to51\) | \((51,34,39,109)\) | F \((-2,3,-1)\), \((D^-,D^+)=(2,9)\), \(1296\to25\) | `candidate_transition` |
| \(p=409\), fresh \(A=1\) | \(1\to209\) | \((209,250,159,325)\) | F \((-1,0,-2,-1)\), \((11,1)\), \(41616\to199\) | `candidate_transition` |
| \(p=409\), declared \(A=5\) | \(5\to1045\) | \((1045,50,359,3669)\) | 同一 F, \(8323\to39\) | `analysis_evidence` |

前两条都是各自 fresh source tree 内的完整局部正规形控制，绝不声称从 \(A=5\) 历史
重置而来。它们均有 `chart_relation=same_chart`，所以还不是 \(k\ge1\) 的
真正 r-chart 正控制。第三条的算术、F 见证和局部势都成立，但父收费回执没有经注册
adapter 重放，所以局部 \(E3=false\)，仅把“若补齐父回执”的算术记录为
`conditional_local_e1_e5`。

三个控制例均有 gap-7 直接 Type II 叶，故 terminal-first 会优先终止；它们验证局部
正规形与来源合同，而不是新增困难核心余项覆盖。它也不同于 ordinary r/reset：
\(p=409\) 的 ordinary 更新是 \(1\to250\) 或 \(5\to250\)，cofactor 更新是
\(1\to209\) 或 \(5\to1045\)，且 \(250\nmid1045\)。

## 真 r-chart 的来源边界与两锚点构造

### 形式平移不是来源

把两个低载体 determinant 作平移

\[
M\mapsto M+p,\qquad n\mapsto n+4d,\qquad
R_M\mapsto R_M+4C,\qquad K_M\mapsto K_M+pC,
\tag{9}
\]

得到下列真 r-chart 候选：

| \((p,A,M,d,n)\) | \(r\)-target | source/target F 见证 | provenance |
|---|---|---|---|
| \((73,1,107,22,129)\) | \(A_C=51,(R_r,K_r)=(95,1734),1296\to25\) | \((-1,1,-4)\to(-2,3,-1)\) | 缺 source/path/anchor/bundle |
| \((409,1,659,200,1289)\) | \(A_C=209,(511,52250),41616\to199\) | \((-5,-2,-2)\to(-1,0,-2,-1)\) | 缺 source/path/anchor/bundle |

二者皆有 \(k=1\)、\(a=1\mid r\)、\(p<R_r\) 和 canonical target，但不能绕过 E1/E3
而成为回执。它们事实上在现有 universal-anchor complete-excess 宏步中不可能出现：
该宏步必有

\[
M=\operatorname{lcm}(A,Q),\qquad Q>1,\qquad Q\mid M,\qquad Q<R<p.
\tag{10}
\]

若 \(M\) 是大于 \(p\) 的素数，则 \(Q\mid M\) 强制 \(Q=M>p\)，与 (10) 矛盾。
这里 \(107>73\) 与 \(659>409\) 都是素数，故表中的两个 \(M\) 不是“尚未找到来源”，而是
不属于当前 complete-excess 发生器的严格 no-go。它们只说明同余正规形允许平移，不能作为
递归路径。

对 \(A>1\)，由 \(A\mid M=kp+r\) 及 \(p\nmid a=A/(A,C)\) 可得有用的预筛

\[
a\mid r\quad\Longleftrightarrow\quad a\mid k.
\tag{11}
\]

现有 \(p=409,A=5\) 的高 anchor 行 \((M,r)=(410,1),(1240,13)\) 正好都因
\(a=5\nmid r\) 被拒绝，且其 charged-support 父回执也未重放。两个纯算术高行同样有
gap-7 Type II 终端，所以它们是来源研究的诊断，不是困难核心覆盖。

### 高 \(R\) raw source 引理

通用 \(p\)-source 的整数恒等式其实不需要 \(R<p\)。设

\[
p\equiv1\pmod {24},\qquad R\ge3,\qquad R\equiv3\pmod4,\qquad p\nmid R,
\qquad K=\frac{pR+1}{4}.
\tag{12}
\]

则

\[
(U,V,m)=\bigl(p,\ R(p-1)-p,\ p-1\bigr)
\tag{13}
\]

满足 \(U+V=Rm\)、\(\gcd(U,V)=1\)、\(p\nmid K\)。因 \(v_p(U)=1>v_p(K)=0\)，raw
\(p\)-edge 的唯一 shift 为 \(t=1\)，并精确到达

\[
(U,V,m)\longmapsto(1,R-1,1).
\tag{14}
\]

证明只需

\[
\gcd(U,V)=\gcd(p,R)=1,\qquad
\frac{V+R}{p}=R-1,\qquad \frac{m+1}{p}=1.
\]

现有 universal_p_source_v1 把 \(R\) 限为核心范围 \(3\le R\le p-2\)，所以
(12)--(14) 是一个新的数学 raw-source 引理。下面的专用 adapter 已将它用于一条
固定的两锚点路径；它尚未接入统一选择器，且不能仅凭来源合同升级为全局递归边。

### 高 \(R\) path-anchored bundle 合同

设 (12) 成立，且 \(A\mid K\)。对 \(R-1\) 的每个素因子取完整超额部分

\[
Q=\prod_{v_q(R-1)>v_q(K)}q^{v_q(R-1)},\qquad
\beta=(R-1)/Q.
\tag{H1}
\]

若 \(Q>1\) 且 \(p\nmid Q\)，则

\[
\beta\mid K,\qquad (Q,\beta)=1,\qquad Q\nmid K,\qquad Q<R.
\tag{H2}
\]

令 \(M=\operatorname{lcm}(A,Q)\)。由 \(A\mid K\) 及 \(Q\nmid K\) 得

\[
A<M,\qquad p\nmid M.
\tag{H3}
\]

因此 canonical_chart(p,M) 合法且图表改变；若 \(R_M<p\)，它给出 marked rechart，
若 \(R_M>p\)，写 \(K_M=MC\)、\(d=p-C\)、\(n=4M-R_M\)，则

\[
d,n>0,\qquad pn=4Md+1.
\tag{H4}
\]

这恰好是 high_R_path_anchored_bundle_v1 重放的 source/path 合同。旧的
\(Q<R<p\) 不是代数必需条件：唯一需要替代 \(Q<p\) 的条件是 \(p\nmid Q\)，而
\(p\nmid R\) 则独立且必要。例如 \(p=73,R=219=3p\) 虽有 \(p\nmid Q\)，但
\(\gcd(p,R)>1\)，raw source 不原始；反之 \(p=73,R=159,K=2902,Q=79>p\) 给出
合法 overflow \((R_M,K_M)=(303,5530)\) 和

\[
73\cdot13=4\cdot79\cdot3+1.
\tag{H5}
\]

这只厘清高载体来源与 bundle 的必要算术条件，不产生全局相位秩。

### \(p=1201\) 的两锚点真 r-chart

取

\[
p=1201,\qquad B_p=360000,\qquad
(R_0,K_0)=(987,296347).
\tag{15}
\]

第一条核心范围 source (13) 到达 \((1,986,1)\)，并有

\[
986=2\cdot17\cdot29,\qquad Q_0=986,\qquad\beta_0=1.
\tag{16}
\]

所以

\[
M_0=986,\qquad
\operatorname{canonical\_chart}(1201,M_0)=(1839,552160).
\tag{17}
\]

这是 overflow，但 \(M_0\le B_p\)，同图表支撑提升在算术上给出 \(A:1\mapsto986\)。
现在 \(R_1=1839>p\) 仍满足 (12)。高 \(R\) raw source 到达 \((1,1838,1)\)，且

\[
1838=2\cdot919,\qquad Q_1=919,\qquad\beta_1=2.
\tag{18}
\]

带旧支撑的第二次 anchor 给出

\[
M=\operatorname{lcm}(986,919)=906134=754p+580,
\tag{19}
\]

\[
(R_M,K_M)=(2873071,862639568)=\bigl(R_M,M\cdot952\bigr),
\]

\[
1201\cdot751465=4\cdot906134\cdot249+1.
\tag{20}
\]

因此 \(k=754,r=580,C=952,d=249,n=751465\)。余因子门的全部数值为

\[
s=481,\qquad (R_r,K_r)=(1839,552160),
\]

\[
g=(986,952)=34,\qquad a=29\mid580,\qquad
A_C=\operatorname{lcm}(986,952)=27608.
\tag{21}
\]

目标重新闭合为

\[
K_r=27608\cdot20,\qquad
1201\cdot108593=4\cdot27608\cdot1181+1,
\tag{22}
\]

并有严格局部势下降

\[
\left\lfloor\frac{360000}{986}\right\rfloor=365
>
13=
\left\lfloor\frac{360000}{27608}\right\rfloor.
\tag{23}
\]

这是一张真正 \(k\ge1\) 且 source/target 图表不同的 \(r\)-chart，不是 (9) 的
平移。完整指数盒重算两端皆为 F：在

\[
K_M=2^4\cdot7\cdot17^2\cdot29\cdot919
\]

上，见证 \((-2,1,19,1,-13)\) 给出 \(-1\bmod2873071\) 而盒内无命中；在

\[
K_r=2^5\cdot5\cdot7\cdot17\cdot29
\]

上，见证 \((0,0,-2,2,-3)\) 给出 \(-1\bmod1839\) 而盒内无命中。

该路径的数学来源、anchor、overflow 正规形和 F 数据均由
type_i_high_r_chart_two_anchor.py 重算。该专用复现器现已重放高 \(R\) adapter 和
同图表 \(1\mapsto986\) charged-parent receipt；其 source-local E1--E5 全为真，
所以这条迁移严格登记为 candidate_transition。若单独把它交给一般递归，输出的全局
E5 仍为 false、recursive_edge_eligible=false：它缺的不是局部势，而是可覆盖后续
所有 RESET/anchor 的 non-resetting phase rank。

### 同 bundle 回返的单次耗尽与 Type I 终端

上述 target 回到固定高锚点 \((1839,552160)\)。重用同一 \(Q_1=919\) 时，新的
carrier 不是一条新的严格增长路线，而是

\[
M_1=\operatorname{lcm}(27608,919)=25371752,
\qquad
\operatorname{canonical\_chart}(1201,M_1)=(2873071,862639568),
\]

\[
862639568=M_1\cdot34.
\tag{H6}
\]

这正是 [固定高锚点回返的 complete-excess 单次耗尽](type-I-fixed-high-anchor-return-one-shot-exhaustion.md)
的通式：第二 carrier 整除第一次 \(K_M\)，故图表不变而新余因子 \(34\) 已整除
当前支撑 \(27608\)。事实上

\[
M_1=21125\cdot1201+627,\qquad
\frac{27608}{(27608,34)}=812\nmid627,\qquad
\operatorname{lcm}(27608,34)=27608.
\tag{H7}
\]

所以第二 cofactor gate 失败；即使忽略 gate，支撑势也不再下降。其形式 r-chart 是

\[
(R_r,K_r)=(71,21318).
\tag{H8}
\]

任何合法 charged target support 都必须整除 \(21318<27608\)，因此这不是不遗忘的
后继。另一方面，这张形式低图表是一个真实的 Type I hit：取

\[
(m,A,B,C,H,K)=(1043,1,33,17,38,21318),
\]

则 \(1201=4ABC-m\)、\(1043\cdot71=4B^2C+1\)，并直接得到

\[
\frac4{1201}
=\frac1{561}+\frac1{646}+\frac1{25602918}.
\tag{H9}
\]

所以 p=1201 的 terminal-first 结果是 terminal_leaf；这里的
candidate_transition 只描述其高 \(R\) 余因子迁移，不能误读为该素数仍未终止。

### 高锚宏形状的后续校正

本卡的 `candidate_transition` 是旧的 transient \(S\to T\) receipt，故不能仅把其
local potential 重命名为全局 E5。正确的 high-\(R\) 组合应从已收费高锚
\(H=(p,R,K;A)\) 开始：

\[
P\longrightarrow H\Longrightarrow S\longrightarrow T.
\]

若 parent 精确结束于 \(H\)、bundle 从 \(H\) 可重放、typed F/G 与
\(\operatorname{Sol}(p)\) 恒等提升均已验证，则
[高锚点 direct cofactor 宏步的 E1--E4 准入合同](type-I-high-anchor-cofactor-macro-e1-e4-admission.md)
给出持久 \(H\to T\) 宏的 E1--E4；其 E5 由
[高锚点 direct cofactor 与外层支撑秩重置的词典序拼接](type-I-high-anchor-cofactor-outer-rank-composition.md)
的 \(\Lambda_p\) 支付。p=1201 与 p=60913 的独立宏回放已重算完整 E1--E5，
但都被 terminal-first 的 Type I leaf 抢占，故仍只作为 `analysis_evidence` 保存。

因此“缺全局 non-resetting phase rank”现在只描述未被该宏合同覆盖的 generic
\(S\to T\) receipt、未回放的 charged-history parent、无偿 RESET/fresh-root、或未冻结的
\(c=1\) capability action；不能再用它否定已经闭合的 \(H\to T\) 宏账本。

## 边界

本卡不证明每个 overflow 存在 (3)--(4) 的选择，也不证明可达 \(A>1\) 的父 ledger
总可回放，也不证明每个 high \(R\) 宏通过 terminal/alternate、gate、有限 c=1 action
菜单和 \(\Lambda_p\) 的全部准入门。两锚点例已闭合 source/path、parent replay、同
bundle 单次耗尽，并在 p=1201 上以 Type I 终端结束；它仍不证明其它高锚点会终端。
该 macro adapter 尚未注册到统一选择器，且 generic G 端点仍须由具名 typed verifier
重算。缺少这些输入的候选不得标为 recursive verified_edge。

复现命令：

~~~bash
python3 reproductions/type_i_high_r_chart_two_anchor.py --verify
~~~
