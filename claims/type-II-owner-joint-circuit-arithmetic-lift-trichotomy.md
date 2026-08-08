---
kind: claim
claim_id: type-II-owner-joint-circuit-arithmetic-lift-trichotomy
title: Type II owner 联合依赖回路到 SNF—算术提升的三分
statement: 对物理满匹配中的一个最小 source-column 依赖回路，先用保持参数纤维的 source-relation lattice/SNF 检查其有限域系数是否有整数提升。若提升及其 power-closed 来源合同存在，且带来源因子积在某个合法 D' 上命中 -1，则得到 Type II 短证书；若未命中但存在保持来源标签且 D'<D 的已验证 source-switch，则得到严格递降；若只有同模数相容候选，则得到可继续筛选的 SOURCE_RELATION_FOURIER；若 SNF、CRT、power-closure 或范围门失败，则给出精确 CIRCUIT_SOURCE_RELATION_LIFT_OBSTRUCTED。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-owner-joint-matching-finite-obstruction-closure
  - type-II-owner-primary-mask-arithmetic-lift-criterion
  - type-II-kernel-fourier-source-relation-compatibility
  - type-II-source-label-snf-failure-anchor-relation-dichotomy
topics:
  - type-II
  - owner-weight
  - joint-matching
  - source-circuit
  - SNF
  - arithmetic-lift
  - Fourier
  - constructive-certificate
  - strict-descent-interface
  - proof-program
sources:
  - claim: type-II-owner-joint-matching-finite-obstruction-closure
    role: finite-dependent-matching-input
  - claim: type-II-owner-primary-mask-arithmetic-lift-criterion
    role: labelled-factor-normal-form
  - claim: type-II-kernel-fourier-source-relation-compatibility
    role: relation-lattice-lift-gate
  - claim: type-II-source-label-snf-failure-anchor-relation-dichotomy
    role: SNF-obstruction-trichotomy
  - reproduction: reproductions/type_ii_owner_joint_circuit_arithmetic_lift.py
    role: direct-fourier-obstruction-controls
visibility: public
last_checked: '2026-08-09'
---

# Type II owner 联合依赖回路到 SNF—算术提升的三分

## 1. 回路输入

取一个有限 owner 物理满匹配 \(M\)，以及其规范最小 source-column
依赖回路
\[
C=\{e_1,\ldots,e_k\}\subseteq M.
\]
在当前 \(\ell\)-初等商中记录非零系数
\[
\bar c=(\bar c_1,\ldots,\bar c_k)\in\mathbb F_\ell^k,
\qquad
\sum_{i=1}^k\bar c_i\,v(e_i)=0.
\tag{1}
\]
每条边还携带来源参数和因子
\[
\sigma_i=(a_i,h_i),\qquad h_i\mid p+4Da_i,
\tag{2}
\]
并已通过 shared-q 合并；需要时要求选中的 \(h_i\) 两两互素。

令 \(L_{\rm fib}\subseteq\mathbb Z^k\) 是当前 source-SNF/CRT 计算出的保持参数
纤维关系格。一个整数向量 \(c\in\mathbb Z^k\) 称为该回路的合法提升，若
\[
c_i\bmod\ell=\bar c_i,\qquad c\in L_{\rm fib},
\tag{3}
\]
并且它通过来源标签、范围和 \(B'>A\) 门。系数规范化为
\(0\le c_i<\ell\) 后按字典序选第一个合法提升；若需要更大指数，必须明确记录
其增加的 source block 和 q-height，不能静默改变回路。

## 2. 算术菜单三分

对每个合法提升 \(c\)，以及有限候选
\[
D'\mid D,\qquad A\mid D',\qquad D'/A\text{ 平方自由},\qquad 4AD'<p,
\tag{4}
\]
检查统一且 power-closed 的来源合同
\[
AD'\equiv Da_i\pmod{h_i^{c_i}}
\qquad(c_i>0),
\tag{5}
\]
令
\[
h(c)=\prod_{i=1}^k h_i^{c_i}.
\tag{6}
\]

若某个候选同时满足 (5) 和
\[
\boxed{h(c)\equiv-1\pmod{4D'},}
\tag{7}
\]
则由
\[
K'=\frac{h(c)+1}{4D'},\qquad
C'=\frac{D'}A,\qquad
B'=\frac{K'p+A}{h(c)}
\tag{8}
\]
得到
\[
\mathrm{CIRCUIT\_TYPE\_II\_SHORT\_CERTIFICATE}
=(C,D',A,K',B',h(c),\sigma_C).
\tag{9}
\]
(5) 保证 \(h(c)\mid p+4AD'\)，而 (7) 给出
\(h(c)=4AC'K'-1\)；若 \(4AD'<p\)，则
\[
B'-A=\frac{K'(p-4AD')+2A}{h(c)}>0.
\tag{10}
\]

若至少一个合法提升通过 (3)、(5) 和范围门，所有候选都未满足 (7)，但存在一个
保持来源标签且 \(D'<D\) 的 E5 source-switch 映射，则输出
\[
\mathrm{CIRCUIT\_STRICT\_SOURCE\_SWITCH\_RELAY}
=(C,c,D',A,\eta,\{h_i\}).
\tag{11a}
\]
以 \((D',\operatorname{rk}_{\rm SNF},|C|)\) 为词典序势时，第一坐标严格下降；
该回执才是可提升递降。若没有这样的严格候选、但至少一个合法提升通过 (3)、(5)
和范围门，则输出
\[
\mathrm{CIRCUIT\_SOURCE\_RELATION\_FOURIER}
=(C,c,D',A,\{h_i\},\text{failed target rows}).
\tag{11}
\]
该回执是相容的 source-relation Fourier 输入；它可以继续交给
owner primary 算术菜单、F/G 相位或 q-height/Kneser 分派，但本身不是 Type II
或递降。

若不存在任何通过 (3) 的 SNF 提升，或统一合同、范围、目标映射均为空，则输出
\[
\mathrm{CIRCUIT\_SOURCE\_RELATION\_LIFT\_OBSTRUCTED}
=(C,\text{first failed SNF/CRT/range row}).
\tag{12}
\]
不能将 (12) 收费为容量，也不能把它改写为联合物理 Hall 缺口。

## 3. 穷尽性和与联合障碍的接口

对固定回路 \(C\)，有限候选 \(D',A\) 和有限来源菜单使上述检查终止。若 (3)
失败，SNF 第一失败行是整数关系格的反证；若 (3) 通过，有限候选按 (5)、(7)
分为命中或非命中。非命中仍保留 (11)，因为关系角色已经有真实来源和纤维载荷；
若没有合法候选，则 (12) 给出算术障碍。

对联合 source-slot 障碍的回执，按每个物理满匹配 \(M\) 的规范回路 \(C_M\)
逐一执行本三分：

* 任一回路进入 (9)，整个状态立即得到 Type II 短证书；
* 任一回路进入 (11a)，得到保持来源标签的严格递降；
* 所有剩余回路都进入 (11)，得到一个有限的相容关系 Fourier 回路族，随后必须
  检查其 F/G 或 q 进后继；
* 某个回路进入 (12)，保存其具体失败行；它只否定该回路的整数提升，不否定
  其它匹配、其它回路或 Type I 路径。

这把“联合匹配不存在”细化为直接终端、严格递降、相容对偶或算术障碍，而不使用
\(\operatorname{rank}\) 并集作为伪充分条件。

## 4. 证明

若 (3) 成立，\(\bar c\) 在源关系格中的整数提升保持当前参数纤维和来源合同；
由 (5) 每个被选来源因子的所需幂都整除 \(p+4AD'\)，两两互素时 (6) 也整除该
目标因子。
(7) 与正规形公式给出 (8)--(10)，故 (9) 是有效 Type II 证书。

若所有合法提升均不命中 (7)，但 E5 给出 \(D'<D\) 的保持标签映射，则
(11a) 的势严格下降。若没有严格候选但至少一个通过 SNF/CRT/范围，则它定义了一个
带来源的非命中关系 Fourier 载荷，得到 (11)。若没有通过者，有限 SNF/CRT
菜单的第一失败行给出 (12)。这些条件按优先级互斥且覆盖固定回路。对有限个
物理满匹配逐回路应用即可，证毕。

## 5. 构造性控制

### \(p=5113\) 的直接回路终端

取 \(D=6\)、回路系数 \(\bar c=(1,1)\)、来源因子
\[
(h_1,h_2)=(17,7),
\]
以及 \(D'=A=1\)。有
\[
h(c)=17\cdot7=119\equiv-1\pmod4,
\]
并且
\[
K'=30,\qquad B'=1289,\qquad C'=1,
\]
故输出 (9)。

### 相容但非命中

取 \(\ell=3\)、\(\bar c=(1,2)\)、合法提升 \(c=(1,2)\)，令
\(h_1=5,h_2=7\)，且来源关系格包含 \(c\)。在 \(D'=A=1\) 时
\(h(c)=5\cdot7^2=245\equiv1\pmod4\)，所以不命中 (7)，但输出 (11)。
若同一来源合同从原始 \(D=6\) 映射到 \(D'=1\)，且 E5 标签映射已验证，则同一
控制输出 (11a)，其第一势坐标从 \(6\) 降到 \(1\)。

### SNF 不相容

取 \(\ell=2\)、\(\bar c=(1,1)\)，而 \(L_{\rm fib}\) 由
\((2,0),(0,2)\) 生成；没有模 2 系数为 \((1,1)\) 的整数向量属于该格，故第一
SNF 门失败，输出 (12)。

## 研究边界

该三分完成了从联合依赖回路到带来源整数菜单的第一条算术桥：直接命中已经成为
Type II 证书，相容非命中成为可筛选 Fourier 载荷，不能提升的回路留下精确障碍。
仍未证明所有 (11) 都有 q 进超载或良基后继；下一步的全局缺口收缩为相容回路族的
F/G 相位—容量或严格递降映射。
