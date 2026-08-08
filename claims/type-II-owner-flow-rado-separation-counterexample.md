---
kind: claim
claim_id: type-II-owner-flow-rado-separation-counterexample
title: Type II owner 流—Rado 分离测试不足的 source-preserving 规范化反例
statement: 存在一个两请求、两物理槽的有限 owner 图，使 q 容量上界、算术候选邻域、物理最大流和联合源列秩都分别通过，但不存在同时满足物理槽注入与源列独立性的匹配。该反例说明 owner 流之后必须先完成 source-preserving canonicalization，或运行精确的联合边—拟阵检查；不能把分离的 flow 与 Rado 必要条件当作充分条件。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-owner-arithmetic-menu-rado-fourier-closure
  - type-II-owner-projection-physical-capacity-flow-gate
  - type-II-rado-linear-rank-hall-capacity-bridge
topics:
  - type-II
  - owner-weight
  - physical-capacity
  - Rado
  - matroid
  - counterexample
  - source-canonicalization
  - proof-program
sources:
  - claim: type-II-owner-arithmetic-menu-rado-fourier-closure
    role: canonical-resource-sufficiency-boundary
  - claim: type-II-owner-projection-physical-capacity-flow-gate
    role: owner-token-flow-input
  - claim: type-II-rado-linear-rank-hall-capacity-bridge
    role: source-rank-necessary-condition
  - reproduction: reproductions/type_ii_owner_flow_rado_separation_counterexample.py
    role: exhaustive-two-request-counterexample
visibility: public
last_checked: '2026-08-09'
---

# Type II owner 流—Rado 分离测试不足的 source-preserving 规范化反例

## 1. 反例图

取两个请求
\[
\mathcal R=\{r_1,r_2\},
\]
两个物理槽 \(c_1,c_2\)，且
\[
b(c_1)=b(c_2)=1.
\]
在 \(\mathbb F_2^2\) 中令
\[
e_1=(1,0),\qquad e_2=(0,1).
\]
四条候选 owner 边的物理投影和源列如下：
\[
\begin{array}{c|cc}
 & c_1 & c_2\\ \hline
r_1 & e_1 & e_2\\
r_2 & e_2 & e_1
\end{array}
\tag{1}
\]
同一物理槽在不同请求上携带不同源列；这正是尚未 source-preserving
canonicalization 的情形。

把每条边看作一个不同 token，则任意非空请求子集的 q 容量上界都可取
\[
\mathsf C_q(U)=2,
\tag{2}
\]
候选 token 邻域大小至少为 \(2\)，物理网络的最大流为
\[
\mathsf F_{\rm phys}(\{r_i\})=1,\qquad
\mathsf F_{\rm phys}(\{r_1,r_2\})=2.
\tag{3}
\]
联合源列集合是 \(\{e_1,e_2\}\)，所以
\[
\rho(\{r_i\})=2,\qquad
\rho(\{r_1,r_2\})=2.
\tag{4}
\]
因此 q、候选邻域、物理 Hall 和“先取并集再算秩”的检查全部通过。

## 2. 严格失败

物理槽容量为一时，完整物理匹配只有两个：

1. \(r_1\to c_1,\ r_2\to c_2\)，所选源列为 \(e_1,e_1\)；
2. \(r_1\to c_2,\ r_2\to c_1\)，所选源列为 \(e_2,e_2\)。

两种选择的源列都线性相关，故不存在满足
\[
\text{不同物理槽}\quad+\quad\text{源列独立}
\tag{5}
\]
的完整匹配。这个结论是穷举两种置换得到的严格反例，而不是数值近似。

因此以下蕴含是错误的：
\[
\left[
\begin{array}{c}
\mathsf C_q(U)\ge |U|,\\
\text{owner 物理最大流}\ge |U|,\\
\operatorname{rank}\bigl(\text{所有候选源列}\bigr)\ge |U|
\end{array}
\right]
\Longrightarrow
\text{独立物理匹配}.
\tag{6}
\]

## 3. 正确的门

要进入 Rado 独立代表定理，必须先满足以下二者之一：

* **source-preserving canonicalization**：每个容量副本 \(d=(c,k)\) 只有一个固定
  源记录和源列，且每个请求的候选边直接是这些副本的子集。此时对任意
  \(U\) 检查
  \[
  \rho(U)=\operatorname{rank}\{v(d):d\in\bigcup_{r\in U}\mathcal D(r)\}
  \ge |U|
  \tag{7}
  \]
  就是单一的 Rado 条件，自动包含副本注入；
* **联合边—拟阵检查**：若源列仍依赖于请求/token，则不能把物理槽先压平。必须
  在带请求、token、物理容量和向量标签的原始边集上直接寻找联合独立匹配；(1)
  的图应输出
  \[
  \mathrm{OWNER\_TOKEN\_SOURCE\_CANONICALIZATION\_OBSTRUCTED}
  \tag{8}
  \]
  或一个更强的联合边证书，而不是 Fourier 容量。

反例中的每个槽都有两个不相容源记录，因此不能构造满足 (7) 前提的规范副本。
它不是算术菜单为空，也不是 q 容量缺口；缺口位于 owner token 到 source-preserving
物理资源的联合提升。

## 4. 对统一选择器的影响

对任意实际 owner 图，分派顺序应增加一个前置门：

\[
\text{E1--E3}
\longrightarrow
\text{source-preserving canonicalization}
\longrightarrow
\text{q / physical flow}
\longrightarrow
\text{Rado}
\longrightarrow
\text{E4 / Fourier}.
\tag{9}
\]

若 canonicalization 失败，必须保存发生冲突的物理槽、请求、token、源列和失败的
来源合同。不能用 owner multiplicity、联合秩或单独的最大流替代该回执。只有
canonicalization 成功后，前一条 owner 算术菜单—Rado—Fourier 闭合定理的
\(\mathcal D(r)\) 才是真实的向量拟阵资源集合。

## 5. 研究边界

该反例没有否定规范资源图上的 Rado 定理；它精确说明了规范化是一个独立数学门，
而不是记账格式。后续全局工作必须为每个核心素数证明：

1. owner token 可以 source-preserving 地规范化到物理容量副本；
2. 若不能规范化，冲突能转为 source-column escape、算术 lift obstruction、
   Type I/II 终端或严格可提升递降；
3. 不能以“候选数、物理流和并集秩均足够”作为联合存在性证明。
