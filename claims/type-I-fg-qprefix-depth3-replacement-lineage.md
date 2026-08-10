---
kind: claim
claim_id: type-I-fg-qprefix-depth3-replacement-lineage
title: p=557281 的 q=3 depth-3 规范基候选分类与 standalone fresh-ledger realization
statement: >-
  固定 p=557281、actual-F digest EXPLICIT_TARGET_ODD_INDEX_43、target x=182、
  q=3、规范 named factor-2 edge 0->e_(2) 及其无单位重标的 elementary value c=1。
  depth 3 强制 J=1；全部 candidate-binding deep records 恰有十个，全部通过
  canonical-base、source-map 与 elementary-role 算术门的 pairs 恰有五个，其中恰有
  两个还保持 chosen edge 的完整 C9 phase 4。非恒等 pair
  (s0,s1,D0)=(14924,104468,7462) 给出显式最大 depth-3 block {1,3,9,27}。
  对只含该 request 的空 ledger，可显式选择新的 assignment/lineage/charge，建立三层
  单射 owner map、六个 fresh source/target keys 和一个 shallow occurrence，故得到
  standalone fresh-ledger typed lineage。若旧 s0=19838 的 depth-2 assignment 已活跃，
  新旧 target keys 部分重叠而 source keys 不同，既非全 fresh 也非完整 replay；原子
  replacement ledger 仍未证明。因而从头选择新 witness 时 ambient depth 可取
  c_new=(3,0)、delta_new=(0,2)，但不能与旧 receipt 叠加，也不能宣称 in-place
  supersession 或 Kneser price 已登记；83 typed owner、physical-source exactness、
  FIBER_REALIZED、E4 和 E5 均仍未证明。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fg-qprefix-block-bound-first-overflow-terminal
  - type-I-fg-qprefix-request-depth-admission
  - type-I-owner-profile-canonical-base-target-slot-capacity
  - type-I-raw-certified-q-layer-charge-key-nonreuse
  - type-I-fg-qprefix-kernel-depth-neutral-cargo-capacity
topics:
  - type-I
  - F-state
  - q-prefix
  - candidate-fiber
  - canonical-source-base
  - source-switch
  - replacement-lineage
  - q-adic-height
  - capacity-map
  - constructive-certificate
sources:
  - claim: type-I-fg-qprefix-block-bound-first-overflow-terminal
    role: candidate-binding-and-typed-admission-iff
  - claim: type-I-owner-profile-canonical-base-target-slot-capacity
    role: canonical-base-inverse-divisor-slot-dictionary
  - claim: type-I-fg-qprefix-kernel-depth-neutral-cargo-capacity
    role: ambient-kernel-depth-vector-and-fixed-lineage-boundary
  - reproduction: reproductions/type_i_fg_qprefix_depth3_replacement_lineage.py
    role: focused-double-enumeration-and-depth3-witness
visibility: public
last_checked: '2026-08-10'
---

# \(p=557281\) 的 \(q=3\) depth-\(3\) 候选分类与 standalone fresh-ledger realization

## 1. 固定范围与合同

本卡只讨论以下已经固定的 actual F 请求：

\[
p=557281,\qquad R=199,\qquad x=182,\qquad q=3,
\tag{1}
\]

Fourier digest 为 `EXPLICIT_TARGET_ODD_INDEX_43`，named source edge 是

\[
0\longrightarrow e_{(2)}.
\tag{2}
\]

它在仓库 \(C_9\) 坐标中的完整 phase 为 \(4\)，elementary \(C_3\) value 为

\[
c=1.
\tag{3}
\]

不允许在本卡中更换 named edge、反转 (2)、更换 digest，或事后加入一个未记录的
unit normalization。现行 `CANDIDATE_FIBER_QBLOCK_BOUND` 与
`TYPED_QPREFIX_REALIZED` 合同要求：

1. \(J\ge1,d=3\)，且 \(0<4x,4s_0,4s_1<p\)；
2. \(D_*=D(x)\mid D_0=D(s_0)=D(s_1)\)，且 \(3\nmid4D_*\)；
3. target、deep source 和 source switch 满足
   \[
   \min\{v_3(p+4s_0),v_3(x-s_0),v_3(p+4x)\}\ge J+3,
   \tag{4}
   \]
   其中 \(v_3(0)=\infty\)；
4. shallow source 满足
   \[
   v_3(p+4s_1)=J,\qquad
   \frac{s_1-s_0}{3^J}\equiv1\pmod3;
   \tag{5}
   \]
5. named edge 的整数 source map、固定 elementary role、target
   \(\eta\)-map，以及同一 charge 的 fresh 或完整 replay lineage ledger 全部通过。

前四项和第 5 项的算术/角色部分可以先分类；occurrence/owner 必须在具体 ledger 上
另行实例化。本卡分别处理空的单请求 ledger 与“旧 depth-\(2\) assignment 已活跃”
两种状态，不能用前者替后者作 replay。

这里的 source pairs 是同一个 request 的替代 assignments，不是可同时收费的五个请求。

## 2. \(J\) 与全部 candidate-binding deep records 的解析分类

target numerator 为

\[
N_x=p+4x=558009=3^4 83^2,
\qquad v_3(N_x)=4.
\tag{6}
\]

由 (4)，\(J+3\le4\)；结合 \(J\ge1\)，得到

\[
\boxed{J=1.}
\tag{7}
\]

因此固定 target 下任何 q-prefix lineage 都有 \(d\le3\)。现在

\[
B_p=\left\lfloor\frac{p-1}{4}\right\rfloor=139320,
\qquad D_*=D(182)=182=2\cdot7\cdot13.
\tag{8}
\]

因为 \(D_*\) 平方自由，

\[
D_*\mid D(s_0)\iff182\mid s_0.
\tag{9}
\]

另一方面，(4) 的 target--deep 两个同余都精确压成

\[
s_0\equiv x\equiv182\pmod{81}.
\tag{10}
\]

由 \((182,81)=1\)，(9)--(10) 等价于

\[
s_0=182(1+81j).
\tag{11}
\]

严格窗口 \(1\le s_0\le B_p\) 强制 \(0\le j\le9\)。逐项使用

\[
D(s)=\prod_\ell \ell^{\lceil v_\ell(s)/2\rceil}
\tag{12}
\]

得到全部且仅有的十个 candidate-binding deep records：

\[
\begin{array}{c|rrrrrrrrrr}
s_0&182&14924&29666&44408&59150&73892&88634&103376&118118&132860\\
\hline
D(s_0)&182&7462&29666&22204&910&5278&88634&25844&118118&66430.
\end{array}
\tag{13}
\]

所以旧 \(s_0=19838\) 只是一条 depth-\(2\) 正控制；它不属于 depth-\(3\) deep menu。

## 3. 全部 arithmetic typed-admission candidates

每个 deep source 都满足 \(s_0\equiv182\equiv2\pmod9\)，且
\(p\equiv1\pmod9\)。因此 (5) 精确等价于

\[
\boxed{s_1\equiv5\pmod9.}
\tag{14}
\]

确实，(14) 给出 \(s_1-s_0\equiv3\pmod9\)，所以 normalized value 为 \(1\)；同时
\(p+4s_1\equiv3\pmod9\)，故 shallow height 恰为一。

固定规范基 \(D\) 的全部 canonical source labels 恰为

\[
\mathcal S(D)=
\left\{\frac{D^2}{c}:c\mid\operatorname{rad}(D)\right\}.
\tag{15}
\]

把 (15) 与 \(1\le s_1\le B_p\) 及 (14) 相交，十个 deep records 的完整 shallow
菜单为

\[
\begin{array}{c|c|c}
s_0&D_0&\mathcal S(D_0)\cap[1,B_p]\cap(5\bmod9)\\
\hline
182&182&\{1274\}\\
14924&7462&\{104468\}\\
29666&29666&\varnothing\\
44408&22204&\varnothing\\
59150&910&\{4550,12740\}\\
73892&5278&\{137228\}\\
88634&88634&\varnothing\\
103376&25844&\varnothing\\
118118&118118&\varnothing\\
132860&66430&\varnothing.
\end{array}
\tag{16}
\]

规范基逆引理使 (15) 是 iff 字典，因此 (16) 不是抽样搜索。全部通过
canonical-base、shallow-height 和 elementary-role 算术门的 pairs 恰为

\[
\boxed{
\begin{aligned}
&(182,1274,182),\quad(14924,104468,7462),\\
&(59150,4550,910),\quad(59150,12740,910),\\
&(73892,137228,5278),
\end{aligned}}
\tag{17}
\]

其中三元组依次表示 \((s_0,s_1,D_0)\)。

## 4. source-line 与完整 \(C_9\) phase 过滤

在 named rank-one line 上，每个 (17) 的整数 source map 唯一限制为

\[
\boxed{\mathcal L(ne_{(2)})=s_0+n(s_1-s_0)\qquad(n\in\mathbb Z).}
\tag{18}
\]

edge content 为一；(14) 又给出

\[
v_3(s_1-s_0)=1,
\qquad \frac{s_1-s_0}{3}\equiv1\pmod3,
\tag{19}
\]

所以 (18) 精确实现 fixed elementary role。若要把它扩为整个指数格上的一个规范
elementary-role 整数映射，可取

\[
\mathcal L_{\mathbf t}(z)=s_0+(s_1-s_0)z_{(2)}
+9t_5z_{(5)}+9t_{11}z_{(11)}+9t_{2083}z_{(2083)},
\tag{20}
\]

其中 \(t_5,t_{11},t_{2083}\in\mathbb Z\)。式 (20) 只证明整数/SNF role map；它不声称
其它 exponent-box endpoints 也通过 owner range 或共同规范基。

固定 digest 在 chosen edge 上的完整 \(C_9\) phase 是 \(4\)。对 (17) 逐项得到

\[
\begin{array}{c|c|c}
(s_0,s_1)&s_1-s_0&(s_1-s_0)/3\pmod9\\
\hline
(182,1274)&1092&4\\
(14924,104468)&89544&4\\
(59150,4550)&-54600&7\\
(59150,12740)&-46410&1\\
(73892,137228)&63336&7.
\end{array}
\tag{21}
\]

所以完整 phase-compatible 子菜单恰为

\[
\boxed{(182,1274,182),\qquad(14924,104468,7462).}
\tag{22}
\]

(17) 是 elementary arithmetic-admission menu；(22) 是保持既有高阶 digest 的更强
子菜单。只有在 occurrence/owner gate 实例化后，其中的某一条才能成为正式 typed
assignment；也不能反过来把另外三条误删为 elementary arithmetic failures。

## 5. 非恒等 depth-\(3\) 构造

为避免依赖 \(x=s_0\) 时的 occurrence 去重解释，取 (22) 的第二条：

\[
D_0=7462=182\cdot41,\qquad
s_0=14924=7462\cdot2,\qquad
s_1=104468=7462\cdot14.
\tag{23}
\]

两个 source rows 的规范数据为

\[
(D_0,A_0,C_0)=(7462,2,3731),
\qquad
(D_0,A_1,C_1)=(7462,14,533),
\tag{24}
\]

其中 \(3731=7\cdot13\cdot41\)、\(533=13\cdot41\) 均平方自由。target 的规范数据是
\((D_*,A_*,C_*)=(182,1,182)\)，且 \(D_*\mid D_0\)。范围和高度精确为

\[
4s_0=59696<p,\qquad4s_1=417872<p,
\tag{25}
\]

\[
\begin{aligned}
p+4s_0&=616977=3^5\cdot2539,\\
p+4s_1&=975153=3\cdot325051,\\
s_0-x&=14742=3^4\cdot182,\\
s_1-s_0&=89544=3\cdot29848,
\qquad29848\equiv4\pmod9.
\end{aligned}
\tag{26}
\]

因此整数 map

\[
\boxed{\mathcal L(z)=14924+89544z_{(2)}}
\tag{27}
\]

同时通过 candidate binding、canonical-base、named-edge SNF、elementary role 和
chosen-edge \(C_9\) phase。取 \(\beta_1=2\) 并在 tail modulus \(27\) 中定义

\[
\tau(s)=\frac{s-2}{3}\pmod {27},
\tag{28}
\]

则

\[
(\tau(x),\tau(s_0),\tau(s_1))=(6,6,19),
\qquad19-6\equiv4\pmod9.
\tag{29}
\]

最后

\[
B_3=\{1,3,9,27\}\subseteq\operatorname{Div}(N_x),
\tag{30}
\]

且对既有

\[
\eta(u)=(u\bmod13)^4
\tag{31}
\]

有

\[
\eta(B_3)=(1,3,9,1).
\tag{32}
\]

### 5.1 空的单请求 ledger 上的显式 fresh assignment

先固定本卡的 scope：ledger \(\Lambda_0\) 只服务这一个 request，且在选择 witness 前
为空；旧 depth-\(2\) witness 只是另一个可选证明对象，没有先写入 \(\Lambda_0\)。
定义内容寻址标识

\[
\begin{aligned}
\mathsf{assignment}_{\rm new}
  &=(\texttt{EXPLICIT\_TARGET\_ODD\_INDEX\_43},182,14924,104468,7462),\\
\mathsf{lineage}_{\rm new}
  &=(\mathsf{assignment}_{\rm new},q=3,J=1,d=3),\\
\mathsf{direction}_{\rm new}
  &=(\mathsf{candidate\_fiber\_digest}(182,1,182),3\bmod728,
     \mathsf{lineage}_{\rm new}),\\
\mathsf{stabilizer\_snapshot}_{\rm new}
  &=(H=U(728),\operatorname{Stab}_H(B_3)=\{1\}),\\
\mathsf{charge}_{\rm new}
  &=(\mathsf{direction}_{\rm new},\mathsf{stabilizer\_snapshot}_{\rm new}),\\
\mathsf{price\_status}_{\rm new}
  &=\texttt{UNPRICED}.
\end{aligned}
\tag{33}
\]

若 \(tB_3=B_3\)，则 \(t=t\cdot1\in B_3\)；直接检查
\(t=3,9,27\) 均不保持 \(B_3\)，故这里的 stabilizer snapshot 确为 \(\{1\}\)。

令三条 raw/relative atoms 为

\[
\mathcal A_{\rm new}
=\{(\mathsf{assignment}_{\rm new},r):r=1,2,3\},
\tag{34}
\]

并显式定义 owner map

\[
\boxed{
\alpha_{\rm new}(\mathsf{assignment}_{\rm new},r)
=(\mathsf{charge}_{\rm new},r)\qquad(1\le r\le3).}
\tag{35}
\]

它单射且像恰为连续前缀 \(\{1,2,3\}\)。相应 occurrence keys 是

\[
\begin{aligned}
O_S(r)&=(\mathsf S_{\rm new},14924,3,1+r),\\
O_T(r)&=(\mathsf T,182,3,1+r)
\qquad(1\le r\le3),\\
O_{\rm sh}&=(\mathsf S_{\rm new},e_{(2)},104468,7462).
\end{aligned}
\tag{36}
\]

因为 \(14924\ne182\)，六个 q-layer keys 两两不同；\(\Lambda_0=\varnothing\) 使它们
全部 fresh。唯一 shallow edge \(O_{\rm sh}\) 只被这个 request 使用，容量为一。
结合 (23)--(32)，typed gate 的 candidate、source-map、role、owner-prefix、fresh
occurrence 与 shallow-capacity 条件全部闭合，从而得到

\[
\boxed{
\texttt{P557\_ACTUAL\_F\_Q3\_DEPTH3\_STANDALONE\_FRESH\_LEDGER\_LINEAGE}.}
\tag{37}
\]

这里的 \(\mathsf{price\_status}_{\rm new}=\texttt{UNPRICED}\) 独立于 charge key，
不是 stabilizer snapshot，也不是零价格：在
\(\texttt{FIBER\_REALIZED}\) 之前不得登记 Kneser 价格。因为 (6)--(7) 给出普遍上界
\(d\le3\)，(37) 达到固定 target \(x=182\) 的最大 q-prefix 深度。

## 6. 旧 assignment 已活跃时的严格迁移边界

旧 receipt 使用 \((s_0,s_1,D_0)=(19838,138866,19838)\)，其 source height 只有三，
所以“该固定 lineage 不能到 depth 3”仍然正确。令旧、新 target key 集分别为

\[
K_{\rm old}^T=\{(\mathsf T,182,3,2),(\mathsf T,182,3,3)\},
\tag{38}
\]

\[
K_{\rm new}^T=K_{\rm old}^T\cup\{(\mathsf T,182,3,4)\}.
\tag{39}
\]

两者部分重叠，而 source value、canonical base、assignment id 与 lineage id 都改变。
因此在**旧 assignment 已写入的 ledger** 上，新 witness 既非 all-fresh，也非同一
assignment 的 full replay。现有 fresh/replay 二分只能输出

\[
\boxed{\texttt{Q\_PREFIX\_ATOMIC\_REPLACEMENT\_LEDGER\_UNPROVED}.}
\tag{40}
\]

所以 (37) 是从空 ledger 选择新 witness 的存在证书，不是对已活跃旧账本的 in-place
mutation。两种合法分派必须分开写：

~~~text
standalone construction:
  old depth-2 witness: not selected
  new depth-3 witness: active
  request count / elementary role rank / lineage count: 1 / 1 / 1
  capacity price: unregistered; future price may use B3 only

legacy ledger already active:
  old depth-2 assignment: active
  new depth-3 candidate: migration obstructed by partial overlap
  status: Q_PREFIX_ATOMIC_REPLACEMENT_LEDGER_UNPROVED
~~~

绝不能把 \(B_2\) 与 \(B_3\)、两组 source keys、角色秩或未来 Kneser 价格相加。

相对于 \(w=-1\pmod {728}\)，\(B_3\) 的 prefix-local kernel section 为

\[
\boxed{S_w(B_3)=\{701,727\}},
\qquad |S_w|(96-|S_w|)=188.
\tag{41}
\]

在 ambient exponent coordinates \((v_3,v_{83})\) 中，从空 ledger 选择 (37) 时可取

\[
\boxed{c_{\rm fresh}=(3,0),\qquad\delta_{\rm fresh}=(0,2).}
\tag{42}
\]

旧 ledger 未迁移时仍是 \(c_{\rm legacy}=(2,0)\)、\(\delta_{\rm legacy}=(1,2)\)。
两张向量都是完整 ambient-kernel completion 分支的 labelled requirements，不是可
同时收费的状态，也不把 \((0,2)\) 解释为两个独立角色槽。

## 7. 精确边界

本卡证明的是固定 request、digest、named edge、方向和 \(c=1\) 合同下的完整
canonical-base depth-\(3\) arithmetic menu，以及其中一个 standalone fresh-ledger
typed lineage。它不覆盖：

* 其它 named edges、反向 \(c=2\)、alternate digest 或未记录的 unit normalization；
* 五条 pairs 的同时使用，或任何重复 request/rank/capacity 收费；
* 已活跃旧 assignment 到新 assignment 的 atomic replacement transaction；
* \(83\) 与 \(83^2\) 的 F/G neutral owner tokens；
* \(27\cdot83^b\) 的 F/G provenance-preserving product synthesis；
* 任意已登记 Kneser price；
* exact physical-source predicate、完整 `FIBER_REALIZED`、E4 或 E5。

\(p=557281\) 另由首个 overflow gap \(79\) 的 Type II 短证书预先终止；本卡的作用是关闭
actual F calibration 中“从空 ledger 可选择 \(q=3\) 第三层”的构造缺口，并精确暴露
旧 ledger 原地迁移门，而不是提供一个未终止核心素数的新终端。

## 聚焦验证

~~~bash
python3 reproductions/type_i_fg_qprefix_depth3_replacement_lineage.py --verify
~~~

验证器只对本固定 \(p,x,q\) 做解析 deep 分类、direct-label 与 inverse-slot 双枚举、
五条 elementary candidates、两条 \(C_9\) candidates、显式 witness、standalone
owner/occurrence assignment、旧新 key 的 partial-overlap obstruction 和 kernel section
检查；不运行历史测试。
