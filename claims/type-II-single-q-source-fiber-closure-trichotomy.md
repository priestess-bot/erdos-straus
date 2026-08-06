---
kind: claim
claim_id: type-II-single-q-source-fiber-closure-trichotomy
title: Type II 单 q 来源纤维的 CRT—前缀—稳定子闭包三分
statement: 对一个固定核心素数、原始参数和已经选定来源标签的同一 q 请求族，先按来源同余枚举 admissible 参数纤维，再在每个纤维内按前缀 Hall 条件压缩为一个真实 q 幂块。若请求同余不相容或候选纤维为空，得到精确的来源/范围负证书；若目标命中，得到 Type II 短证书；若目标缺失且同余核被稳定子吸收，则商目标仍缺失并在 source-switch 门通过时给出严格较小模数递降；若核未被吸收，则有限阿贝尔合成列给出较小商缺失、顶层 Fourier 或广义 \(2^j\)/primary 数字缺口。不同候选纤维只逐一处理，不能池化。该闭包定理不声称所有核心素数的请求族都已存在或通过整数提升。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-prefix-source-crt-fiber-concentration
  - type-II-q-layer-prefix-kneser-price-certificate
  - type-II-stabilizer-kernel-quotient-descent-trichotomy
  - type-II-source-fiber-finite-abelian-composition-relay
  - type-II-source-fiber-highest-deficit-tail-compression
  - type-II-source-fiber-multiprimary-digit-terminal
topics:
- type-II
- single-q
- source-fiber
- CRT
- prefix-matching
- Kneser
- stabilizer
- quotient-descent
- Fourier
- generalized-dyadic
- selector
- proof-program
sources:
  - claim: type-II-q-prefix-source-crt-fiber-concentration
    role: source-fiber-candidate-concentration
  - claim: type-II-q-layer-prefix-kneser-price-certificate
    role: same-q-prefix-compression
  - claim: type-II-stabilizer-kernel-quotient-descent-trichotomy
    role: saturated-kernel-lower-modulus-branch
  - claim: type-II-source-fiber-finite-abelian-composition-relay
    role: finite-abelian-missing-target-closure
visibility: public
last_checked: '2026-08-05'
---

# Type II 单 q 来源纤维的 CRT—前缀—稳定子闭包三分

## 1. 输入状态

固定核心素数 \(p\)、原始参数 \(D\) 和一个奇素数 \(q\)。设已经选定一组带来源标签的
q 请求

\[
\mathcal R=\{r_1,\ldots,r_m\},\qquad
b_i=Da_i,\qquad h_i\ge1,
\tag{1}
\]

满足真实来源整除

\[
q^{h_i}\mid p+4b_i.
\tag{2}
\]

一个 admissible 参数纤维写成

\[
f=(D_*,A),\qquad s_f=AD_* ,\qquad
D_*\mid D,\quad A\mid D_*,\quad D_*/A\text{ 平方自由},\quad 4s_f<p.
\tag{3}
\]

如果请求 \(r_i\) 在该纤维上有合法 q-prefix 边，则必须有

\[
s_f\equiv b_i\pmod {q^{h_i}}.
\tag{4}
\]

令 \(H=\max_i h_i\)，并以广义 CRT 检查 (4) 的相容性。候选纤维集合记为

\[
\mathscr F_{\mathcal R}
=\{f\text{ 满足 (3)、(4) 以及 source-switch/SNF/range 门}\}.
\tag{5}
\]

这里的 \(\mathscr F_{\mathcal R}\) 是一个有限集合；当 \(q^H>D^2\) 时至多有一个候选，
因为 \(1\le s_f\le D^2\)。若不同候选的同余、标签或整数提升条件不同，必须保留
逐候选记录，不能先合并目标群。

## 2. 闭包定理

对每个 \(f\in\mathscr F_{\mathcal R}\)，令 \(d_f(q)\) 是该纤维通过共同 q 账本后
可用的连续深度，并把请求限制为 \(h_i\le d_f(q)\)。将 \(h_i\) 升序排列为

\[
h_{(1)}\le\cdots\le h_{(m)}.
\tag{6}
\]

选择器按下面的优先顺序输出：

### A. 来源/纤维层

1. 若某一对来源标签不满足同 q 的必要同余，输出
   'Q_PREFIX_SOURCE_CRT_INCONSISTENT'；
2. 若 \(\mathscr F_{\mathcal R}=\varnothing\)，输出
   'Q_PREFIX_SOURCE_FIBER_EMPTY'；
3. 若 \(|\mathscr F_{\mathcal R}|>1\)，禁止池化，分别运行 B—D。只要一个候选产生
   Type II 或合法递降即可返回；若所有候选只产生负证书或未闭合回执，则输出带
   候选索引的 'Q_PREFIX_PRICE_FRAGMENTED'。

### B. 前缀层

对单个候选 \(f\)，若

\[
\exists k\le m:\quad h_{(k)}<k,
\tag{7}
\]

则输出规范的 'Q_PREFIX_MATCHING_DEFICIT'，并保存最小失败层 \(k\)。若 (7) 不发生，
前缀 Hall 等价式给出一个高度 \(m\) 的真实 q 幂块

\[
B_{f,q}(m)=\{1,\bar q,\ldots,\bar q^m\}\subseteq H_f.
\tag{8}
\]

这一步把同一 q 的 \(m\) 个请求压成一个来源合法的块；不产生 \(m\) 个可重复价格。

### C. 目标/Kneser 层

把 (8) 与该纤维中其它已经通过回译的源块相乘，得到 \(P_f\)，目标记为 \(t_f\)，
最终稳定子为 \(T_f=\operatorname{Stab}(P_f)\)。若

\[
t_f\in P_f,
\tag{9}
\]

则返回 Type II 短证书。若目标缺失，价格只能按

\[
\kappa_{f,q}=\min\bigl(m,\operatorname{ord}_{H_f/T_f}(\bar qT_f)-1\bigr)
\tag{10}
\]

计入；最终稳定子吸收的 q 层不得继续收费。

### D. 缺失目标层

若 \(t_f\notin P_f\)，固定一个模数降阶映射

\[
\pi_f:H_f\longrightarrow\overline H_f,\qquad K_f=\ker\pi_f.
\tag{11}
\]

按如下互斥分派：

1. **饱和核分支。** 若 \(K_f\subseteq T_f\)，则
   \[
   P_f=\pi_f^{-1}(\pi_f(P_f)),
   \tag{12}
   \]
   所以 \(t_f\notin P_f\) 蕴含 \(\pi_f(t_f)\notin\pi_f(P_f)\)。若
   \(|\overline H_f|<|H_f|\)，且商源参数纤维、标签回译和 E1--E5 通过，输出
   'LOWER_MODULUS_RELAY'；若抽象商缺失但任一提升门失败，输出具体的
   'KERNEL_SOURCE_LIFT_OBSTRUCTED'，不能把抽象商直接当作原猜想递降。
2. **未饱和核分支。** 若 \(K_f\not\subseteq T_f\)，沿有限阿贝尔合成列逐层投影。
   第一个商缺失给出严格较小的 'COMPOSITION_QUOTIENT_DEFICIT'；若缺失只在顶层
   素数核中，则得到非空真截面和规范 'TOP_PRIMARY_FOURIER' 角色。
3. **循环数字分支。** 若顶层或剩余差分群是 \(C_{\ell^a}\)，且实际关系块按精确
   \(\ell\)-进层分组，则每层至少 \(\ell-1\) 块会命中；目标仍缺失时必有某层至多
   \(\ell-2\) 块，输出 'GENERALIZED_2J_DIGIT_DEFICIT'。取最高不足层后，高层
   饱和尾压缩到严格较小商；若不足层在顶层，则输出顶层 primary 终端，不把它
   重复计入低层容量。

这三项互斥的顺序是：先检查饱和核；未饱和时再检查合成列的第一个缺失层；若该层
具有循环 primary 的真实独立块，优先输出数字缺口或命中，最后才保留顶层 Fourier。

## 3. 闭包证明

来源层：由 (2) 和共同纤维中的 q-prefix 整除，相减得到 (4)。广义 CRT 给出来源
相容性；由 \(s_f\le D^2\)，当 \(q^H>D^2\) 时候选至多一个。不同候选的源参数、
目标群和标签合同不相同，不能在此之前合并。

前缀层：对前缀邻域，Hall 条件等价于 (6) 中的 \(h_{(k)}\ge k\)。条件通过时，按
排序顺序把第 \(k\) 个请求分配到第 \(k\) 层，得到 (8)，且 (2)--(4) 保证每个
指数都有真实整数回译。

目标层：最终稳定子下的 q 幂块容量是 (10)；若 (9) 成立，幂块和其它源块的
整数来源直接给出 Type II。若 (9) 失败，目标陪集与 \(P_f\) 分离，Kneser 缺口
不能把已吸收的层再次计费。

缺失层：若 \(K_f\subseteq T_f\)，稳定子饱和恒等式给出 (12)，因而商命中不可能
伪装成原层缺失；商若同时缺失，群阶严格下降。若 \(K_f\not\subseteq T_f\)，有限
阿贝尔合成列的第一个未命中层要么是严格较小商，要么顶层核截面是非空真子集，
其 Parseval 能量严格为正，产生非平凡 Fourier 角色。循环 primary 的进位覆盖定理
则给出第三项：全层饱和必命中，缺失必暴露一个精确层缺口；最高不足层尾压缩又给出
严格较小商或顶层数字终端。所有分支都保存 source-switch、范围和标签失败行，
所以没有把抽象群命中误升为整数证书。证毕。

## 4. 选择器势和严格边

在已经通过整数回译的状态上使用

\[
\Phi_f=\bigl(|H_f|,\ |H_f/T_f|,\ H_{\mathrm{remain}},\ k_{\mathrm{fail}}\bigr)
\tag{13}
\]

的字典序势。饱和核的合法商 relay 严格降低第一坐标；合成列商缺失和最高不足层
尾压缩严格降低目标群或 primary 指数；前缀匹配缺口、CRT 空集和 Fourier 角色是
终端/负证书，不计作未证明递归边。若 source-switch 或标签提升失败，保留具体
障碍并禁止重置势而重新收费同一 q 请求。

因此，在单 q 请求族已选定来源标签并且所有合法整数门已闭合的范围内，选择器不再
有“跨纤维池化—重复 q 价格—低模数伪命中—循环层孔”四种未分类状态；它们分别
落入 A、B、D 的 typed 分支。

## 5. 构造性边界

### 5.1 来源候选为空

取 \(p=97,D=6,q=7,h=2,b=37\)。有

\[
7^2\mid p+4b=245,\qquad s_f\equiv37\pmod{49},\qquad 1\le s_f\le D^2=36.
\]

所以没有 admissible \(s_f\)，输出 'Q_PREFIX_SOURCE_FIBER_EMPTY'；不能把该 q 层
直接送入任意 Type II 纤维。

### 5.2 唯一纤维和 Type II 命中

取 \(p=5113,D=6,q=7,h=1,b=36\)。共同候选满足
\(s_f\equiv1\pmod7\)，其中 \(s_f=1\) 给出 \(A=D_*=1\)。在 \(U(4)\) 中
\(7\equiv-1\)，故 \(B_{f,q}(1)=\{1,-1\}\)，直接命中目标。

### 5.3 稳定子饱和而目标仍缺失

在 \(G=U(12)\) 中取 \(P=\{1,5\}\)、目标 \(t=11\)，并用投影
\(U(12)\to U(4)\)。核 \(K=\{1,5\}=T(P)\)，而商中
\(\pi(P)=\{1\}\) 仍不含 \(\pi(t)=3\)。所以这是合法的低模数缺失 relay 候选，
不是“商已命中”的伪递降。

### 5.4 循环顶层缺口

在 \(C_4\) 中只有一个精确层 \(0\) 的二点块而没有精确层 \(1\) 的块，目标相对指数
仍缺失时，输出 'GENERALIZED_2J_DIGIT_DEFICIT'；不能把模 2 的投影命中误写成
整个 \(C_4\) 命中。

## 6. 逻辑边界

本定理闭合的是“已选定同 q 来源请求族”的有限选择器，而不是所有核心素数的全称
选择器。仍需证明至少一项：

1. 每个未命中核心状态都能选出一个非空的同 q 请求族及其来源标签；
2. 所有候选纤维的 source-switch、SNF、范围和 \(B'>A\) 门通过，或失败能转成
   Type I/F/G/严格下降；
3. 顶层 Fourier/数字缺口具有外部参数解释，或其提升失败能支付一个全局良基秩。

所以本卡提供的是一个 single_q_fiber_closed 接口：一旦这些前置条件由 F/G 证书
或跨状态容量提供，剩余分支必落入短证书、严格商递降或显式障碍三者之一。
