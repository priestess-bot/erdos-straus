---
kind: claim
claim_id: type-I-marked-support-accumulation-rechart-saturation
title: 外部支撑累积重图表的良基下降与 overflow 饱和边界
statement: 设核心图表 4K=pR+1 携带 absorbed support A|K，且完整 clean external slab 给出 X=Q alpha、Y=beta、Q=q^e、q不整除K。令 M=AQ，并取唯一规范图表 pR_M=-1 (mod 4M)、1<=R_M<4M。若 R_M<p，则 (p,R_M,K_M;M) 是 equation target 仍为 4/p、标记集仍为 Sol(p)、恒等解提升且势 floor((p-1)^2/(4A)) 严格下降的 E1--E5 support switch；它允许 R_M>R。若 R_M>p，则 M>p/4，并有 K_M=MC、n=4M-R_M、d=p-C 及 pn=4Md+1、gcd(M,pn)=1。初始 A=1 且 alpha=2,3 时 h=4Q-p 是合法 gap，但其完整 p^i q^j 三目标谱并不自动命中；所以 clean large-slab 已被压成累积支撑下降或显式 overflow receipt，而饱和支仍需换载体、直接终端或新的可提升状态。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-formal-external-slab-collision-absorption-rechart
  - type-I-general-b-centered-square-spectrum
  - type-I-f-g-fourier-obstruction-certificate
  - type-I-overflow-a-one-dual-outer-rank-reset
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - external-slab
  - large-slab
  - support-switch
  - absorbed-support
  - rechart
  - well-founded-potential
  - overflow
  - determinant
  - proof-boundary
sources:
  - claim: type-I-formal-external-slab-collision-absorption-rechart
    role: canonical-rechart-and-clean-slab-interface
  - claim: denominator-escape-state-contract
    role: marked-state-and-E1-E5-contract
  - claim: type-I-general-b-centered-square-spectrum
    role: direct-one-denominator-factor-spectrum
  - claim: type-I-f-g-fourier-obstruction-certificate
    role: canonical-f-g-state-certificate
visibility: public
last_checked: '2026-08-03'
---

# 外部支撑累积重图表的良基下降与 overflow 饱和边界

## 1. 增广图表状态

固定核心素数

\[
p\equiv1\pmod {24}.
\tag{1}
\]

本卡使用的增广状态为

\[
\mathsf S=(p,R,K;A),
\qquad
4K=pR+1,
\qquad
3\le R\le p-2,
\qquad
A\mid K.
\tag{2}
\]

字段 \(A\) 称为 absorbed_support。它记录此前已经承诺保留在后继 \(K\) 中的外部
支撑乘积，而不是当前 \(K\) 的完整因子。该状态的

\[
\texttt{equation\_target}=4/p,
\qquad
W_{\mathsf S}=\operatorname{Sol}(p)
\tag{3}
\]

与图表无关，其中

\[
\operatorname{Sol}(p)=
\left\{(x,y,z)\in\mathbb N^3:
\frac4p=\frac1x+\frac1y+\frac1z\right\}.
\]

为避免把“重算”留成未定义动作，linear_absorbed_support_v1 状态采用以下规范字段：

| 字段 | 规范值 |
|---|---|
| state_id | 对除 state_id 自身外的全部规范字段及版本号取规范 JSON SHA-256；载荷由 \((p,R,A)\) 唯一重算 |
| equation_target | \((4,p)\) |
| marked_solution_set | \(\operatorname{Sol}(p)\) |
| induction_rank | \(p\)；本边不靠该分量下降 |
| modulus_context | \(R\equiv3\pmod4,\ 3\le R\le p-2,\ 4K=pR+1\) |
| K_context | \(K\) 的完整排序素因子分解及 \(A\mid K\) |
| target_fiber | hit 取盒内最短见证；F 取生成子群中的最短仿射格见证及 Fourier 角色；G 记 empty 并取分离角色 |
| signed_defect | 从上述唯一见证和完整 \(K\) 指数盒重算；G 态记 not_applicable |
| certificate_context | hit/F/G、规范见证或规范分离角色及其精确整数编码 |
| normal_form | linear_chart_with_absorbed_support_v1 |
| potential_record | \(B_p=(p-1)^2/4\)、\(A\) 及 \(\lfloor B_p/A\rfloor\) |

具名状态 verifier verify_linear_absorbed_support_state_v1 按以下确定顺序重建这些
字段：

1. 分解 \(K\)，按递增素数顺序建立
   \(\phi:\mathbb Z^{\omega(K)}\to(\mathbb Z/R\mathbb Z)^\times\)，再由 CRT 循环
   分量和 Smith 正规形重建关系格 \(\Lambda=\ker\phi\)；
2. 在完整指数盒 \(-v_q(K)\le z_q\le v_q(K)\) 中按
   \((\lVert z\rVert_1,z)\) 排序枚举目标 \(-1\)。盒内命中记 hit；目标只在生成子群中
   命中时记 F，并在仿射格中按同一顺序取最短全局定向见证；
3. G 态按角色阶、相位分子向量的字典序，取第一个在全部 \(q\mid K\) 上平凡而在
   \(-1\) 上非平凡的精确有理相位角色；F 态按规范有限 Fourier 障碍卡的
   \((m,-|A(\chi)|,a_1,\ldots,a_r)\) 顺序取证书；
4. 对 hit/F 见证按完整指数预算重算 \(D^-,D^+\)；G 态写
   signed_defect.status=not_applicable；
5. 将除 state_id 自身外的上述规范 JSON 与版本号哈希为 state_id，并复核它等于由
   \((p,R,A)\) 重建的内容标识。

所以因子分解、关系格、目标纤维、F/G/hit、规范 Fourier 角色和缺陷都由当前
\((R,K)\) 重算，不随 \(A\) 机械继承。有限阿贝尔群对偶性保证第 3 步的 G 分离角色
存在；F 角色的精确编码与完备性由依赖卡给出。

定义全局界和势

\[
B_p=\frac{(p-1)^2}{4},
\qquad
\Phi(\mathsf S)=\left\lfloor\frac{B_p}{A}\right\rfloor.
\tag{4}
\]

由 \(R\le p-2\) 有

\[
K=\frac{pR+1}{4}\le B_p,
\qquad
A\le K\le B_p.
\tag{5}
\]

## 2. 累积支撑重图表定理

设当前完整 formal Reach 或其它已验真的来源给出一个完整 clean external slab

\[
X=Q\alpha,
\qquad
Y=\beta,
\qquad
X+Y=R,
\qquad
(X,Y)=1,
\qquad
\alpha\beta\mid K,
\tag{6}
\]

其中

\[
Q=q^e>1,
\qquad
q\nmid K.
\tag{7}
\]

式 (6) 与 \(R<p\) 给出 \(Q<R<p\)，所以

\[
q\ne p.
\tag{8}
\]

又因 \(A\mid K\)，有 \((A,Q)=1\)。令

\[
M=AQ.
\tag{9}
\]

由 \(p\nmid K\) 和 (8)，\((p,4M)=1\)。定义唯一规范代表

\[
1\le R_M<4M,
\qquad
pR_M\equiv-1\pmod {4M},
\qquad
K_M=\frac{pR_M+1}{4}.
\tag{10}
\]

模 \(4\) 与模 \(M\) 分别给出

\[
R_M\equiv3\pmod4,
\qquad
M\mid K_M.
\tag{11}
\]

而且

\[
\boxed{R_M\ne R.}
\tag{12}
\]

否则 (10) 与 \(4K=pR+1\) 会给出 \(M\mid K\)，继而 \(q\mid K\)，与 (7) 矛盾。

现在假设

\[
R_M<p.
\tag{13}
\]

由模 \(4\) 类，式 (13) 自动加强为 \(3\le R_M\le p-2\)。因此可以定义合法后继

\[
\boxed{
\mathsf T=(p,R_M,K_M;M).}
\tag{14}
\]

具名边 verifier verify_marked_external_accumulation_edge_v1 执行：

1. 从整数输入重算并验证 (1)--(11) 和完整 clean receipt (6)--(8)；
2. 分别调用 verify_linear_absorbed_support_state_v1 重建 \(\mathsf S,\mathsf T\)
   的全部规范字段；
3. 检查后继 absorbed_support 恰为 \(M=AQ\)，而不是任意新因子；
4. 检查两端标记集均为 \(\operatorname{Sol}(p)\)，提升为恒等映射；
5. 重算 (4) 并验证严格不等式 (15)。

所以五项合同为：

| 合同项 | 核验 |
|---|---|
| E1 | (1)--(13) 给出正性、互素、模类、clean 来源和完整支撑数据 |
| E2 | (10)、(14) 确定全部后继字段；新因子分解、F/G/hit 与缺陷按规范构造重算 |
| E3 | 上述具名 verifier 验证源、目标状态和边正规形 |
| E4 | \(W_{\mathsf T}=W_{\mathsf S}=\operatorname{Sol}(p)\)，提升映射是恒等映射 |
| E5 | absorbed_support 从 \(A\) 变为 \(AQ\)，式 (4) 的势严格下降 |

最后一项由纯大小完成。式 (11)、(13) 给出

\[
M\le K_M\le B_p.
\]

而 \(M=AQ\ge2A\)，故 \(B_p/A\ge2\)，并且

\[
\boxed{
\left\lfloor\frac{B_p}{M}\right\rfloor
\le
\left\lfloor\frac{B_p}{2A}\right\rfloor
<
\left\lfloor\frac{B_p}{A}\right\rfloor.}
\tag{15}
\]

所以该边允许 \(R_M>R\)，仍不可能形成环。每走一步 \(A\) 至少翻倍，且已经吸收的
素数以后始终整除 \(A\mid K\)，不能再次以 \(q\nmid K\) 的外部素数身份收费。从
\(A_0\) 出发，连续使用本边的次数至多为

\[
\left\lfloor\log_2\frac{B_p}{A_0}\right\rfloor.
\tag{16}
\]

这一结论只适用于不丢弃 \(A\) 的 marked_external_accumulation 子程序；其它类型的边
若要重置该字段，必须在更外层另给严格下降的秩。

## 3. overflow 的精确行列式边界

若 (13) 失败，则 \(R_M=p\) 因模 \(4\) 类不同而不可能，所以唯一剩下

\[
R_M>p.
\tag{17}
\]

由 \(R_M<4M\) 立即得到

\[
\boxed{M>\frac p4.}
\tag{18}
\]

又由 \(M\mid K_M\)，唯一写成 \(K_M=MC\)。式 (10)、\(R_M<4M\) 给出
\(C\le p\)；若 \(C=p\)，则 \(p(4M-R_M)=1\)，不可能。因此

\[
1\le C\le p-1.
\tag{19}
\]

定义

\[
n=4M-R_M>0,
\qquad
d=p-C>0.
\tag{20}
\]

从 \(4MC-pR_M=1\) 得到规范互补式

\[
\boxed{pn=4Md+1.}
\tag{21}
\]

特别地，

\[
\boxed{(M,pn)=1.}
\tag{22}
\]

所以最自然的 \(D\)-only 尝试 \(D=M\) 不可能满足 \(D\mid(pn)^2\)。此外 (20) 并不
保证 \(n<p\)；即使偶然 \(n<p\)，(22) 仍只排除 \(D=M\)，不会自动排除其它
\(D\)-only 参数。式 (17)--(22) 是 marked_support_overflow receipt，不是后继状态。

后续细化已经把最后一句完全关闭。若 \(2\le n<p\)，则每个 D-only 参数不仅与
\(M\) 互素，还与 \(d\) 和 \(p-n\) 互素；又因
\(p\equiv n\equiv1\pmod4\)，所有 non-source 标记纤维都由奇偶 Vieta 下降证明为空，
包括过去留下的 \(\delta\mid n^2,\delta\nmid n\) 平方超额层。source-supported 分支
仍只复述中心 Type I，所以 overflow-to-D-only 应整体拒绝。见
[同 1 mod 4 秩的 non-source D-only 全域 no-go](two-denominator-lift-same-one-mod-four-no-go.md)。

## 4. 初始 large-slab 的直接 gap 谱

现在取初始 \(A=1\)，并把完整 clean receipt 写成

\[
R=\alpha Q+\beta,
\qquad
\alpha\in\{1,2,3\},
\qquad
\beta>0,
\qquad
\alpha\beta\mid K.
\tag{23}
\]

若进入 overflow，则 \(Q>p/4\)。当 \(\alpha=2\) 或 \(3\) 时，由
\(\alpha Q<R\le p-2\) 还有 \(Q<p/\alpha\le p/2\)。因此

\[
h=4Q-p
\tag{24}
\]

满足 \(h\equiv3\pmod4\) 和

\[
3\le h\le p-2,
\qquad
x_h=\frac{p+h}{4}=Q.
\tag{25}
\]

这是一个合法直接 gap。因为 \(Q=q^e\) 且 \(q\ne p\)，包含首分母 \(Q\) 的完整
一分母因子谱只需检查

\[
z=p^iq^j,
\qquad
i\in\{0,1,2\},
\qquad
0\le j\le2e.
\tag{26}
\]

条件 \(z\equiv-pQ\pmod h\) 使用 \(p\equiv4q^e\pmod h\) 后，精确化为

\[
\boxed{
\begin{array}{c|c}
i&\text{目标同余}\\ \hline
0&q^{j-2e}\equiv-4\pmod h\\
1&q^{j-e}\equiv-1\pmod h\\
2&4q^j\equiv-1\pmod h
\end{array}}
\tag{27}
\]

任一命中都由

\[
(hy-pQ)(hz'-pQ)=(pQ)^2
\]

恢复原素数的直接 Type I/II 证书；全部 miss 则只是一个有限三目标分离证书。

该谱不自动命中。三个精确边界是：

| \((p,R,Q,\alpha,\beta)\) | \(R_Q\) | \(h\) | 完整谱 |
|---|---:|---:|---|
| \((73,63,31,2,1)\) | \(107\) | \(51\) | \(9/9\) miss |
| \((241,215,71,3,2)\) | \(251\) | \(43\) | \(9/9\) miss |
| \((13177,12299,4096,3,11)\) | \(14647\) | \(3207\) | \(75/75\) miss |

第三例中 \(-1\notin\langle2\rangle\pmod {3207}\)，所以 (27) 的三个目标统一失败。
这同时排除了“overflow 后 generalized \(2^j\) 必自动终端”的过强命题。三例都不是
Erdos--Straus 反例；它们只隔离同一个 overflow 菜单。

## 5. 一个自对偶 overflow 参数族

设 \(Q\equiv13\pmod {24}\) 为素数，并且

\[
p=2Q-1
\tag{28}
\]

也是素数。取

\[
R=Q+2,
\qquad
K=\frac{2Q^2+3Q-1}{4},
\qquad
(\alpha,\beta)=(1,2).
\tag{29}
\]

因为 \(Q\equiv5\pmod8\)，有 \(2\mid K\)；又有 \(Q\nmid K\)。所以 (29) 是一条
clean large-slab。直接计算得到

\[
\boxed{
R_Q=p+2=2Q+1,
\qquad
K_Q=Q^2.}
\tag{30}
\]

于是 overflow 数据为

\[
C=Q,
\qquad
n=4Q-R_Q=p.
\tag{31}
\]

同一 \(Q\) 的互补量没有严格下降。对 \(h=2Q+1\)，利用

\[
p\equiv-2,
\qquad
2Q\equiv-1,
\qquad
4Q^2\equiv1\pmod h
\]

可逐项排除 (27) 的全部九个候选。最小实例是

\[
(Q,p,R,K)=(37,73,39,712).
\]

该实例另有 \(Q'=19,\alpha'=2,\beta'=1\) 的 clean slab，且
\(R_{19}=51<p\)，所以它反驳的是“固定同一 \(Q\) 继续递降”，不是换载体后的全局
失败。式 (28) 是否给出无穷多个双素数参数并未使用，也未在这里声称。

## 6. 对旧 large-slab 边界的修正

旧的 absorption 合同只允许 \(R_Q<R\)。累积字段 \(A\) 给出更强且仍良基的判据

\[
\boxed{R_{AQ}<p.}
\tag{32}
\]

特别在初始 \(A=1\) 时，过去列作 local strong miss 的下列上升图表现在都是 verified
support switch：

| \((p,R,Q,\alpha,\beta)\) | \(R_Q\) | 新分类 |
|---|---:|---|
| \((241,7,5,1,2)\) | \(19\) | marked descent |
| \((193,15,7,2,1)\) | \(19\) | marked descent |
| \((337,23,7,3,2)\) | \(27\) | marked descent |
| \((107722177,207,103,2,1)\) | \(375\) | marked descent |
| \((214729,391,193,2,5)\) | \(731\) | marked descent |
| \((21169,23,7,3,2)\) | \(27\) | marked descent |

这里“descent”指 (15) 的 absorbed-support 势下降，不声称 \(R\) 下降，也不声称新图表
立即命中。真正剩余的 clean slab 分支已经收紧为：

\[
\boxed{
R_{AQ}<p\text{ 的累积支撑边}
\quad\lor\quad
R_{AQ}>p\text{ 的 overflow receipt}.}
\tag{33}
\]

本卡的 v1 定理严格针对 \(Q=q^e,\ q\nmid K\)，所以 \(M=AQ\) 仍是正确写法。若完整
节点不是 clean slab，局部上仍会出现 competing-excess raw 分支；但下游的
[完整超额 bundle 选择器](type-I-bottom-sink-scc-complete-excess-bundle-selector.md)
已经证明：在完整 sink-SCC 的最小节点，把所有超额完整块组成复合 \(Q_{\rm bun}\) 后，
规范容量并应取

\[
\boxed{M_{\rm bun}=\operatorname{lcm}(A,Q_{\rm bun}),}
\]

并严格分流到 \(R_{M_{\rm bun}}<p\) 的同类 marked edge 或
\(R_{M_{\rm bun}}>p\) 的 bundle overflow。于是 competing-excess 不再是独立的
sink-SCC 余项；本卡仍未证明的是 prime-power 或 bundle overflow 必有另一载体、直接
证书或可提升后继。

下游的
[overflow 固定 \(n\) 对偶图谱](type-I-overflow-determinant-fixed-n-dual-support-conflict.md)
及其 [\(A=1\) 对偶 RESET 引理](type-I-overflow-a-one-dual-outer-rank-reset.md)
又加强了最后一句：若当前 \(A=1\)，每个 overflow 都有规范 determinant-charged
identity edge；若 \(A>1\)，固定 \(n\) 因子窗口非空时也有同类边。真正未闭合的只剩
累积支撑窗口为空且所有小对偶载体都不能保留旧 \(A\) 的分支。该下游边使用
`overflow_determinant` provenance，不能倒写成本卡的 clean \(Q\)-slab receipt。

## 7. 聚焦复现

~~~bash
python3 reproductions/type_i_marked_support_accumulation_rechart_saturation.py
python3 reproductions/type_i_marked_support_accumulation_rechart_saturation.py --verify
~~~

结果文件为

~~~text
reproductions/type-i-marked-support-accumulation-rechart-saturation-results.json
~~~

对应 SHA-256 为

~~~text
b782bd0af52ba41a6ee56fdaee09a67b3b8d612266c44e8c3a19a81e992fbb97  reproductions/type_i_marked_support_accumulation_rechart_saturation.py
e9461aad992ed715a338cbbd965c4344b267adebb1df964843839a9fe57b1d06  reproductions/type-i-marked-support-accumulation-rechart-saturation-results.json
~~~

该脚本只复核本卡新增的整数边核、聚焦状态分类、累积链和 overflow 因子谱；完整
SNF/HNF Fourier 证书生成规则由第 1 节的状态 verifier 定义，并复用依赖卡的精确
有限群算法。脚本输出不得替代那部分状态合同。
