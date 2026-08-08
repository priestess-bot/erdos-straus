---
kind: claim
claim_id: type-II-owner-source-preserving-fiber-uniformity-criterion
title: Type II owner 物理槽 source-preserving 规范化的纤维一致性判据
statement: 对有限 E1–E3 owner token 图，若同一物理槽的全部可达 token 具有相同 q 层、来源记录和初等源列，并且原始 token 流与请求到物理槽的投影流都通过容量门，则可把每个物理槽拆成固定容量副本，得到可直接应用 Rado 的规范资源图。若纤维源记录不一致而没有显式的 source-class 分槽合同，则只能输出规范化未证实，不得将分离的物理流、并集秩或 owner 质量合并为独立容量。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-owner-arithmetic-menu-rado-fourier-closure
  - type-II-owner-flow-rado-separation-counterexample
  - type-II-owner-projection-physical-capacity-flow-gate
  - type-II-rado-linear-rank-hall-capacity-bridge
topics:
  - type-II
  - owner-weight
  - source-preserving
  - canonicalization
  - physical-capacity
  - Rado
  - Hall
  - constructive-certificate
  - counterexample-boundary
  - proof-program
sources:
  - claim: type-II-owner-arithmetic-menu-rado-fourier-closure
    role: canonical-resource-closure
  - claim: type-II-owner-flow-rado-separation-counterexample
    role: nonuniform-fiber-boundary
  - claim: type-II-owner-projection-physical-capacity-flow-gate
    role: projected-flow-input
  - claim: type-II-rado-linear-rank-hall-capacity-bridge
    role: vector-matroid-matching
  - reproduction: reproductions/type_ii_owner_source_preserving_canonicalization.py
    role: uniform-and-nonuniform-controls
visibility: public
last_checked: '2026-08-09'
---

# Type II owner 物理槽 source-preserving 规范化的纤维一致性判据

## 1. 纤维签名和投影图

固定 E1--E3 过滤后的有限 token 图。每个 token \(\tau\) 有物理投影
\(\pi(\tau)=c\) 和签名
\[
\eta(\tau)=\bigl(j(\tau),\sigma(\tau),v(\tau)\bigr),
\tag{1}
\]
其中 \(j\) 是 q 进层，\(\sigma\) 是带来源标签的算术记录，\(v\) 是当前初等
源商中的源列。对物理槽 \(c\) 的可达 token 纤维记为
\[
\mathcal T_c=\{\tau:\pi(\tau)=c,\ \tau\text{ 可从当前请求族到达}\}.
\]

称槽 \(c\) **source-preserving fiber-uniform**，若
\[
\eta(\tau)=\eta(\tau')
\qquad(\tau,\tau'\in\mathcal T_c).
\tag{2}
\]
空纤维不产生资源。由请求到物理槽的投影邻域 \(\mathcal C(r)\) 构造容量网络，
其中 \(c\to t\) 的容量为 \(b(c)\)；对请求子集 \(U\) 记最大流为
\(\mathsf F_{\rm slot}(U)\)。
同时保留原始请求—token—物理槽网络的流值
\(\mathsf F_{\rm tok}(U)\)，它还检查 token 唯一性。若 source contract 允许同一
token 的显式复用，则其复用预算必须先写入该网络；否则不能用投影流替代
\(\mathsf F_{\rm tok}\)。

## 2. 规范化判据

若所有可达槽满足 (2)，且对每个请求子集
\[
\boxed{\mathsf F_{\rm tok}(U)=\mathsf F_{\rm slot}(U)=|U|,}
\tag{3}
\]
则构造固定资源副本
\[
\mathcal D_c=\{(c,1),\ldots,(c,b(c))\}.
\tag{4}
\]
每个副本 \((c,k)\) 继承槽 \(c\) 的唯一签名 \(\eta_c\)，特别是继承固定源列
\(v_c\)。把请求 \(r\) 的每条投影边 \(r\to c\) 展开到尚未占用的副本
\((c,k)\)，得到 \(\mathcal D(r)\)。

则 \(\mathcal D(r)\) 是一个真正的向量拟阵资源族：物理容量由副本不重复保证，
q 层和来源标签由 \(\eta_c\) 固定，源列由 \(v_c\) 固定。于是对任意请求子集
\[
\rho(U)=\operatorname{rank}\{v_d:d\in\bigcup_{r\in U}\mathcal D(r)\},
\tag{5}
\]
条件
\[
\boxed{\rho(U)\ge |U|\quad\text{对所有 }U}
\tag{6}
\]
由 Rado 独立代表定理等价于存在同时满足物理容量和源列独立的匹配。

判据给出一个可复核的规范化证书：
\[
\mathsf{CANONICAL\_RESOURCE\_CERT}
=(\{\eta_c\},\{\mathcal C(r)\},\{b(c)\},\{\rho(U)\}).
\tag{7}
\]

## 3. 非一致纤维的严格边界

若存在同一槽 \(c\) 及 \(\tau,\tau'\in\mathcal T_c\) 使
\[
\eta(\tau)\ne\eta(\tau'),
\tag{8}
\]
则不能把 \(c\) 的所有 token 任意复制为同一个固定源列副本。此时有两个合法
出口：

1. 给出一个 source-class 分槽合同，把每个副本固定到一个签名类，并逐请求记录
   允许副本集合；然后对该新资源图应用 (6)；
2. 没有分槽合同时输出
   \[
   \mathrm{OWNER\_TOKEN\_SOURCE\_CANONICALIZATION\_OBSTRUCTED},
   \tag{9}
   \]
   附带冲突槽、两条 token、签名和来源失败行。

特别地，不能用 \(\mathsf F_{\rm slot}\) 与所有候选源列的秩分别通过来绕过 (8)；
两者的联合失败由[owner 流—Rado 分离测试不足反例](type-II-owner-flow-rado-separation-counterexample.md)
具体实现。

即使 (2) 成立，只要某个 \(U\) 的
\(\mathsf F_{\rm tok}(U)<|U|\)，也必须输出
\(\mathrm{OWNER\_TOKEN\_ASSIGNMENT\_OBSTRUCTED}\)；投影槽流的通过不能掩盖
token 唯一性缺口。

## 4. 证明

在 (2) 下，\(\eta_c\) 与 \(v_c\) 对槽纤维是良定义的。把每个槽拆成
\(b(c)\) 个副本后，(3) 的两个最大流保证 token 唯一性和请求投影边都可以通过
不重复副本实现；所有
副本的来源和源列仍由同一个 \(\eta_c\) 固定，所以不会产生 token—source
歧义。于是 \(\mathcal D(r)\) 确实是向量拟阵上的请求集合，Rado 定理给出 (6)
与独立代表匹配的等价性。若 (8) 成立，任意固定副本只能选择一个签名，至少有
一个 token 的签名无法被保留；若没有额外分槽合同，规范资源集合没有定义，故
(9) 是必要的保守回执。证毕。

## 5. 构造性控制

### 一致纤维

若 \(c_1,c_2\) 的签名分别固定为
\(\eta_{c_1}=(1,\sigma_1,e_1)\) 和
\(\eta_{c_2}=(1,\sigma_2,e_2)\)，两个请求均可达两个槽，且
\(b(c_1)=b(c_2)=1\)，则投影流为 \(2\)，规范副本为
\((c_1,1),(c_2,1)\)。其源列秩为 \(2\)，(6) 通过并给出独立匹配。

### 不一致纤维

取前述反例的边表
\[
(r_1,c_1)\mapsto e_1,\quad(r_1,c_2)\mapsto e_2,\quad
(r_2,c_1)\mapsto e_2,\quad(r_2,c_2)\mapsto e_1.
\]
物理投影流和并集秩仍为 \(2\)，但 \(c_1,c_2\) 都不是纤维一致；没有 source-class
分槽合同，故输出 (9)，而不输出 Type II 或 Rado 证书。

## 研究边界

纤维一致性是一个易于逐槽计算的充分门，不声称非一致时必无解：非一致图可能
仍存在一个显式的 source-class 分槽合同。它的价值在于把“能否进入规范 Rado
闭合”变成一个可验证的前置对象；对无法通过该门的核心素数，后续必须寻找分槽
合同、source-column escape、算术障碍、Type I/II 终端或严格可提升递降。
