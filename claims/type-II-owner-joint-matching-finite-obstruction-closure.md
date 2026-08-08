---
kind: claim
claim_id: type-II-owner-joint-matching-finite-obstruction-closure
title: Type II owner 物理槽—source 联合匹配的有限穷尽闭合
statement: 对任意固定有限 owner 边图，先按 q 上界和物理流检查请求数；若存在物理满匹配，则逐一检查其源列独立性。若某个匹配独立，得到联合 source-preserving 资源证书并可进入 E4/Fourier；若所有物理满匹配均含源列依赖，则由每个匹配的规范最小依赖回路组成精确的 JOINT_SOURCE_SLOT_OBSTRUCTION。该闭合不把非一致 owner 纤维的联合障碍伪装成普通 Rado 秩缺口或容量。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-owner-source-preserving-fiber-uniformity-criterion
  - type-II-owner-flow-rado-separation-counterexample
  - type-II-owner-arithmetic-menu-rado-fourier-closure
  - type-II-owner-projection-physical-capacity-flow-gate
topics:
  - type-II
  - owner-weight
  - joint-matching
  - physical-capacity
  - source-rank
  - finite-obstruction
  - constructive-certificate
  - proof-program
sources:
  - claim: type-II-owner-source-preserving-fiber-uniformity-criterion
    role: Rado-shortcut-when-canonical
  - claim: type-II-owner-flow-rado-separation-counterexample
    role: joint-obstruction-boundary
  - claim: type-II-owner-arithmetic-menu-rado-fourier-closure
    role: post-matching-Fourier-dispatch
  - claim: type-II-owner-projection-physical-capacity-flow-gate
    role: physical-flow-gate
  - reproduction: reproductions/type_ii_owner_joint_matching_finite_obstruction.py
    role: exhaustive-joint-matching-controls
visibility: public
last_checked: '2026-08-09'
---

# Type II owner 物理槽—source 联合匹配的有限穷尽闭合

## 1. 固定边图

固定请求集 \(\mathcal R=\{r_1,\ldots,r_m\}\) 和有限 owner 边集 \(E\)。每条边
\[
e=(r(e),\tau(e),c(e),j(e),\sigma(e),v(e))
\tag{1}
\]
同时记录请求、token、物理槽、q 层、来源签名和初等源列。物理槽 \(c\) 有容量
\(b(c)\)。不假定同一槽的不同 token 具有相同源列；这正是 source-preserving
规范化尚未通过的残余情形。

称 \(M\subseteq E\) 为物理可行匹配，若
\[
\{r(e):e\in M\}=\mathcal R,\qquad
\tau(e)\text{ 两两不同},\qquad
\#\{e\in M:c(e)=c\}\le b(c).
\tag{2}
\]
其源列独立若
\[
\operatorname{rank}\{v(e):e\in M\}=m.
\tag{3}
\]
令 \(\mathfrak M_{\rm phys}\) 为所有物理可行匹配，令
\(\mathfrak M_{\rm ind}\subseteq\mathfrak M_{\rm phys}\) 为独立者。两者都是有限集；
按边内容寻址排序后可以选择规范最小元素。

## 2. 穷尽分派

先对请求子集 \(U\) 应用已有 q 上界。若
\[
\mathsf C_q(U)<|U|,
\tag{4}
\]
输出
\(\mathrm{OWNER\_JOINT\_Q\_ADIC\_DEFICIT}\)，不需要枚举匹配。

若所有 q 上界通过，但物理网络最大流小于 \(m\)，则
\[
\mathfrak M_{\rm phys}=\varnothing
\tag{5}
\]
并输出带最小割的
\(\mathrm{OWNER\_JOINT\_PHYSICAL\_HALL\_DEFICIT}\)。

若 \(\mathfrak M_{\rm ind}\ne\varnothing\)，取规范最小
\(M_*\in\mathfrak M_{\rm ind}\)，输出
\[
\mathrm{OWNER\_JOINT\_SOURCE\_MATCH}
=(M_*,\{j(e),\sigma(e),v(e)\}_{e\in M_*}).
\tag{6}
\]
只有该回执才允许把选中的物理资源送入 E4 直接命中或前一条
算术菜单—Rado—Fourier 闭合的匹配后分支。

最后，若
\[
\mathfrak M_{\rm phys}\ne\varnothing,\qquad
\mathfrak M_{\rm ind}=\varnothing,
\tag{7}
\]
则对每个 \(M\in\mathfrak M_{\rm phys}\) 取按边序字典最小的线性依赖回路
\[
C_M\subseteq M,\qquad
\sum_{e\in C_M}a_{M,e}v(e)=0,\quad
a_{M,e}\ne0,
\tag{8}
\]
并输出
\[
\mathrm{OWNER\_JOINT\_SOURCE\_SLOT\_OBSTRUCTION}
=\bigl(\mathfrak M_{\rm phys},\{(M,C_M)\}_M\bigr).
\tag{9}
\]
(9) 是一个精确的有限联合障碍：它证明所有物理满匹配都失去至少一个独立
source 方向，但不声称已产生 Fourier 容量或严格下降。后继必须寻找
source-class 分槽合同、source-column escape、算术障碍、Type I/II 终端或
可提升递降。

## 3. 证明

\(\mathfrak M_{\rm phys}\) 有限，故最大流不足时 (5) 与物理 Hall 缺口等价。
若 \(\mathfrak M_{\rm ind}\) 非空，定义 (6) 即给出联合物理—source 证书。若其为空，
每个有限集合 \(M\) 的向量族都线性相关；从其非空依赖子集取极小者得到 (8)。
因对全部 \(M\in\mathfrak M_{\rm phys}\) 都有一个 \(C_M\)，(9) 等价于不存在
独立物理匹配，且回执可由有限枚举复核。三种出口互斥且覆盖固定边图；证毕。

## 4. 与规范 Rado 门的关系

若 source-preserving fiber-uniformity 判据通过，物理副本上的向量不再依赖请求，
则 Rado 独立代表定理可在不枚举 \(\mathfrak M_{\rm phys}\) 的情况下判定
\(\mathfrak M_{\rm ind}\) 是否非空。故 (9) 是只在非一致纤维或联合边未能压平时
需要的后备闭合，而不是对规范资源图的替代定义。

反例
\[
(r_1,c_1)\mapsto e_1,\quad(r_1,c_2)\mapsto e_2,\quad
(r_2,c_1)\mapsto e_2,\quad(r_2,c_2)\mapsto e_1
\]
有两个物理满匹配，分别产生回路 \(\{e_1,e_1\}\) 和 \(\{e_2,e_2\}\)，因此
准确输出 (9)。

## 5. 研究边界

该闭合把“流通过但 Rado 不适用”的残余变成可复核的联合边证书，消除了把
并集源秩误当成联合存在性的逻辑跳步。它仍未证明
\(\mathrm{OWNER\_JOINT\_SOURCE\_SLOT\_OBSTRUCTION}\) 必然连接到每个核心素数的
Type I/II 短证书或严格递降；这正是下一步需要研究的算术后继问题。
