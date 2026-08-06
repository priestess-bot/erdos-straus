---
kind: claim
claim_id: type-II-q-prefix-source-label-finite-closure
title: Type II q 前缀来源标签与候选纤维的有限穷尽闭包
statement: 对有限 q 请求族，若每个请求的来源标签集合有限，则联合枚举来源标签选择、按纤维的集合分割和每个分块的 CRT 候选列表是有限且完备的。每个分支按 CRT、source-switch/SNF、前缀 Hall、最终稳定子价格和候选纤维匹配门分派为 Type II 命中、已实现但 surplus 不足或带最小失败见证的算术障碍；不再保留未定义的标签选择失败。若输入标签集合本身不有限，则输出 LABEL_SOURCE_ENUMERATION_UNCLOSED，不得调用该闭包冒充全称结论。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-prefix-source-crt-fiber-concentration
  - type-II-q-layer-prefix-kneser-price-certificate
  - type-II-cross-state-fiber-capacity-surplus-certificate
  - type-II-hall-matching-fiber-realization-gate
topics:
- type-II
- q-adic
- source-label
- finite-closure
- parameter-fiber
- CRT
- prefix-Hall
- Kneser
- capacity
- obstruction
- proof-program
sources:
  - claim: type-II-q-prefix-source-crt-fiber-concentration
    role: label-to-fiber-CRT-candidates
  - claim: type-II-q-layer-prefix-kneser-price-certificate
    role: prefix-price
  - claim: type-II-hall-matching-fiber-realization-gate
    role: fiber-realization-gate
visibility: public
last_checked: '2026-08-05'
---

# Type II q 前缀来源标签与候选纤维的有限穷尽闭包

## 输入

固定 \(p,D\) 和一个有限请求族 \(\mathcal R\)。每个请求 \(r\) 不再只给出一个来源，
而给出一个已经通过局部 q 进、来源整除和角色类型初筛的有限标签集合

\[
\Lambda_r
=\{(b,q,h,\omega)\},
\tag{1}
\]

其中 \(b=Da\) 是来源整数，\(q\) 是奇素数，\(h\ge1\) 是所需前缀高度，\(\omega\)
保存该标签的 SNF、source-switch、范围和 \(B'>A\) 局部见证。若某个请求的标签
集合尚未有限化，先输出
\(\mathrm{LABEL\_SOURCE\_ENUMERATION\_UNCLOSED}\)，不能静默假定存在一个可用标签。

一个**标签—纤维分支**由两部分组成：

1. 一个标签选择
   \[
   \lambda=(\lambda_r)_{r\in\mathcal R}
   \in\prod_{r\in\mathcal R}\Lambda_r;
   \tag{2}
   \]
2. 一个按候选纤维的集合分割
   \[
   \Pi=(\mathcal R_1,\ldots,\mathcal R_t),
   \qquad
   \bigsqcup_{j=1}^{t}\mathcal R_j=\mathcal R.
   \tag{3}
   \]

同一候选纤维上的分块必须先合并；因此在后续候选选择中要求不同分块使用不同
纤维，避免把同一请求复制到两个参数状态。

## 每个分支的有限检查

对分支 \((\lambda,\Pi)\) 和每个非空 \(\mathcal R_j\)，令

\[
Q_j=\operatorname{lcm}_{r\in\mathcal R_j}q_r^{h_r}.
\tag{4}
\]

先调用[Type II q 层请求的来源 CRT 纤维集中与唯一候选](type-II-q-prefix-source-crt-fiber-concentration.md)：

* 同 q 来源不相容时，记录最小二元
  \(\mathrm{Q\_PREFIX\_SOURCE\_CRT\_INCONSISTENT}\)；
* CRT 相容后，候选集 \(\mathscr F_j\) 由来源剩余类、\(D_*\mid D\)、平方自由、
  范围和 \(4AD_*<p\) 有限确定；
* \(Q_j>D^2\) 时，\(\mathscr F_j\) 至多含一个候选；\(Q_j\le D^2\) 时保留完整有限
  候选表，不能选一个代表后删除其它候选。

对候选纤维 \(f_j\in\mathscr F_j\)，继续检查每个 q 子族
\(\mathcal R_{j,q}\) 的排序高度
\[
h_{(1)}\le\cdots\le h_{(n_{j,q})}.
\]
若某个 \(h_{(k)}<k\)，记录
\(\mathrm{Q\_PREFIX\_MATCHING\_DEFICIT}(f_j,q,k)\)；若前缀通过，则调用
[Type II q 层前缀匹配到纤维 Kneser 价格的规范压缩](type-II-q-layer-prefix-kneser-price-certificate.md)，
把该族压成一个真实 q 幂块。所有来源、SNF、范围、shared-q 和
\(B'>A\) 门均通过后，才把该分支标记为 **FIBER\_REALIZED**。

若一个分支的多个分块各自有候选表，还要在这些表之间选择一个不重复的纤维映射
\[
\varphi:\{1,\ldots,t\}\hookrightarrow\bigcup_j\mathscr F_j,
\qquad
\varphi(j)\in\mathscr F_j.
\tag{5}
\]
若 (5) 不存在，取候选纤维二部图的最小 Hall 缺口
\[
U\subseteq\{1,\ldots,t\},
\qquad
|U|>|\bigcup_{j\in U}\mathscr F_j|,
\tag{6}
\]
作为 \(\mathrm{LABEL\_FIBER\_ASSIGNMENT\_DEFICIT}\)。该缺口只说明当前标签选择和
分割不能同时实现，不把同一候选复制收费。

## 穷尽性定理

对所有标签选择 (2)、集合分割 (3)、候选纤维映射 (5) 逐一执行上述检查，则总回执
只有以下四种类型；当所有 \(\Lambda_r\) 都有限且非空时，第四类不会出现：

1. **LABEL\_TYPEII\_HIT**：某个分支通过 FIBER\_REALIZED，并且显式成员检查已经
   给出 \(-1\in P_A\)，或其最终稳定子下的加权价格满足
   \[
   \sum_Aw_A\sum_q\underline\kappa_{A,q}
   >
   \sum_Aw_A(|G_*/T_A|-2).
   \tag{7}
   \]
   由跨纤维 q-height surplus 证书得到显式 Type II；
2. **LABEL\_REALIZED\_SURPLUS\_DEFICIT**：至少一个分支通过全部算术和前缀门，但
   所有已实现分支均满足 (7) 的反向不等式。输出逐纤维价格、缺口
   \(\delta_A\)、最终吸收和稳定子塔/primary/Fourier 后继，不把“标签已找到”误称为
   Type II；
3. **LABEL\_ALL\_BRANCHES\_OBSTRUCTED**：没有分支通过 FIBER\_REALIZED。按固定
   字典序输出每个分支的第一个失败见证，见证类型只能是 CRT 不相容、候选空集、
   (6) 的纤维分派缺口、source-switch/SNF/范围障碍或前缀匹配缺口；
4. **LABEL\_SOURCE\_ENUMERATION\_UNCLOSED**：某个请求的 \(\Lambda_r\) 不是有限且
   完整的标签表。该状态不能被前三项覆盖，必须转回来源标签生成器。

### 证明

标签选择数为
\[
|\Lambda|=\prod_{r\in\mathcal R}|\Lambda_r|<\infty,
\]
集合分割数为有限的 Bell 数 \(B_{|\mathcal R|}\)。固定一个分块后，(4) 的 CRT
候选 \(s=AD_*\) 满足 \(1\le s\le D^2\) 且位于一个模 \(Q_j\) 的剩余类中，因此
\[
|\mathscr F_j|
\le \left\lfloor\frac{D^2}{Q_j}\right\rfloor+1
\]
并且每个 \(s\) 由平方自由分解唯一恢复 \((D_*,A)\)。所以候选纤维映射 (5) 也是
有限枚举；(6) 是其存在性的 Hall 充要条件。

反过来，任何真实的来源标签—纤维实现都会给出唯一的标签选择 \(\lambda\)，按实际
纤维给出一个分割 \(\Pi\)，并满足来源 CRT (4)、前缀匹配、所有整数门和 (5)，故
必在枚举中出现。每个枚举分支要么通过全部门，要么在第一个失败门产生列出的
最小见证；通过的分支再由前缀价格和跨纤维 surplus 定理分到 (7) 或价格缺口。
因此不存在未分类的有限标签分支。证毕。

## 构造性边界

### 大 CRT 模数

若某个分支的 \(Q_j>D^2\)，该分块至多有一个候选纤维。此时标签分支要么给出唯一
FIBER\_REALIZED 候选，要么给出 CRT/范围空集或后续合法性障碍；不能再以“还有其它
纤维”保留模糊状态。

### 小 CRT 模数

若 \(Q_j\le D^2\)，同一个标签分支可能留下多个候选。若两个分块的候选表都只有
\(\{f\}\)，则 (6) 立即失败；若候选表有交叠，则必须由 (5) 选择不重复纤维，或合并
分块重新运行 CRT/前缀门。直接把同一 \(f\) 的两个价格相加是伪容量。

### \(p=97\) 的有限负分支

取 \(D=6\)，固定来源 \(b_1=6,q_1=11\) 和 \(b_2=18,q_2=13\)。标签只有这一个选择，
而 \(Q=143>D^2=36\)，CRT/范围候选为空；该分支输出
\(\mathrm{Q\_PREFIX\_SOURCE\_FIBER\_EMPTY}\)，穷尽闭包因而返回
\(\mathrm{LABEL\_ALL\_BRANCHES\_OBSTRUCTED}\)，但不声称 \(p=97\) 没有其它来源或
其它 Type I/II 射线。

## 对全局选择器的意义

该定理把“来源标签选择”从一个未定义的存在性短语变成一个有限分支族。它不能保证
每个核心素数的原始请求族拥有有限完备标签表，也不能保证至少一个分支满足正 surplus；
但在标签表已经由 H19、局部 q 进或 Fourier 角色生成器有限化后，剩余问题只可能是：
某个分支给出 Type II，所有已实现分支留下明确容量缺口，或所有分支都有可复核的
算术/前缀障碍。下一步应证明请求生成器本身覆盖每个未命中状态，或把
\(\mathrm{LABEL\_ALL\_BRANCHES\_OBSTRUCTED}\) 的最小见证接入 Type I/F/G 与良基递降。
