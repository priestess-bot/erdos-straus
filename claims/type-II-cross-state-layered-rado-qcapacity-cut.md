---
kind: claim
claim_id: type-II-cross-state-layered-rado-qcapacity-cut
title: Type II 跨状态分层 Rado—q 进容量切割
statement: 固定一个奇素数 q、有限移位集 S 和一组已通过来源标签、SNF、source-switch 与范围门的独立 ell-primary 角色请求。把每个状态 s 的可用 q 层展开为槽 (s,j)，并给每个槽记录真实源列向量。对任意请求子集 U，先检查逐层 q 进槽上界 sum_{j<=E_U} C_j(S_U,q)：若它小于 |U|，输出严格的 Q_ADIC_LAYER_CAPACITY_DEFICIT；若该上界通过而邻域源列秩不足，则输出 LINEAR_RANK_DEFICIT；两项必要上界均通过后才允许进入普通 Hall/Rado 匹配和 Kneser 容量。该优先切割把“移位 q 进层不足”与“源列线性不足”分开，并且 q 进上界在 p=433、S={16,100}、q=7 上达到等号。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-cross-state-source-relation-role-capacity-dispatch
  - type-II-rado-linear-rank-hall-capacity-bridge
  - type-II-shared-factor-q-adic-difference-bound
  - type-II-source-fiber-shared-q-ledger
  - type-II-cross-state-source-demand-hall-capacity-bridge
topics:
- type-II
- cross-state
- q-adic
- layered-capacity
- Rado
- Hall
- linear-rank
- source-switch
- proof-program
sources:
  - claim: type-II-cross-state-source-relation-role-capacity-dispatch
    role: independent-role-requests
  - claim: type-II-rado-linear-rank-hall-capacity-bridge
    role: source-column-rank-cut
  - claim: type-II-shared-factor-q-adic-difference-bound
    role: finite-shift-layer-capacity
  - claim: type-II-source-fiber-shared-q-ledger
    role: repeated-q-deduplication
  - claim: type-II-cross-state-source-demand-hall-capacity-bridge
    role: legal-slot-compatibility
visibility: public
last_checked: '2026-08-05'
---

# Type II 跨状态分层 Rado—q 进容量切割

## 1. 分层请求图

固定核心素数 \(p\)、奇素数 \(q\) 和有限移位集 \(S\)。对每个
\(s\in S\) 记
\[
e_s=v_q(p+4s),\qquad 0\le f_s\le e_s,
\tag{1}
\]
其中 \(f_s\) 是经过 shared-\(q\) ledger、来源标签和候选参数门后真正可使用的
高度。把可用层展开成槽
\[
\mathcal C_q(S)=\{(s,j):s\in S,\ 1\le j\le f_s\}.
\tag{2}
\]
一个槽只有在真实整数整除、source-switch/CRT、SNF、标签合同和 \(B'>A\) 门都
通过时，才能加入某个请求的允许集合 \(\mathcal C(r)\)；稳定子吸收层和重复 q
来源先删除或合并。

固定一个 primary \(\ell\)，设 \(\mathcal R_\ell\) 是已经由相容 Fourier 角色产生
且线性独立的请求集。每个槽 \(c\in\mathcal C_q(S)\) 带有真实源列
\[
v_c\in V_\ell,
\]
其中 \(V_\ell\) 是当前参数纤维的 \(\ell\)-初等源商。对请求子集
\(U\subseteq\mathcal R_\ell\)，定义
\[
\mathcal C_q(U)=\bigcup_{r\in U}\mathcal C(r),\qquad
\nu_q(U)=|\mathcal C_q(U)|,
\]
\[
\rho_\ell(U)=
\operatorname{rank}_{V_\ell}\{v_c:c\in\mathcal C_q(U)\},
\qquad
S_U=\{s:(s,j)\in\mathcal C_q(U)\}.
\tag{3}
\]
令 \(E_U=\max_{s\in S_U}f_s\)，并定义移位集的逐层最大占用
\[
C_j(S_U,q)=
\max_{a\bmod q^j}
\#\{s\in S_U:s\equiv a\pmod {q^j}\}.
\tag{4}
\]
若 \(S_U=\varnothing\)，约定 \(E_U=0\) 且所有容量为零。

## 2. 统一容量上界

任何合法槽邻域都满足
\[
\nu_q(U)
\le\sum_{s\in S_U}f_s
\le\sum_{s\in S_U}\min(v_q(p+4s),E_U).
\tag{5}
\]
对固定层 \(j\)，因 \(q^j\mid p+4s\) 等价于一个唯一的移位残类
\(s\equiv-p\,4^{-1}\pmod {q^j}\)，有
\[
\#\{s\in S_U:q^j\mid p+4s\}
\le C_j(S_U,q).
\tag{6}
\]
逐层求和得到
\[
\boxed{
\nu_q(U)\le
\sum_{j=1}^{E_U}C_j(S_U,q)
}=:\mathsf C_q(U).
\tag{7}
\]
这是一个只依赖移位集和 \(q\) 的可计算上界；它不把不同 q 或不同参数纤维的槽
直接合并。

若一个 q 层请求需要同一来源的连续深度标签，则 (7) 仍是上界，因为每个高度
\(f_s\) 至多贡献 \(f_s\) 个展开槽；shared-\(q\) ledger 只会减少实际槽数。

## 3. 分层 Rado—Hall 切割

任何线性 rank-realizing matching 都必须满足
\[
|U|\le \rho_\ell(U)\le \nu_q(U)\le\mathsf C_q(U)
\qquad\text{对所有 }U\subseteq\mathcal R_\ell.
\tag{8}
\]
因此对每个请求子集按以下规范顺序分派（这是优先级，而非声称各必要条件互斥）：

1. 若 \(\mathsf C_q(U)<|U|\)，输出
   \[
\mathrm{Q\_ADIC\_LAYER\_CAPACITY\_DEFICIT}
(q,U,\mathsf C_q(U),|U|).
\tag{9}
\]
   由 (7) 可知任何合法邻域都少于 \(|U|\)；此时源列秩也可能同时不足，但
   q 进切割给出更具体的移位容量原因。
2. 若 \(\mathsf C_q(U)\ge|U|\) 但 \(\rho_\ell(U)<|U|\)，输出
   \[
\mathrm{LINEAR\_RANK\_DEFICIT}
(\ell,U,\rho_\ell(U),|U|).
\tag{10}
\]
   这是 Rado 对偶的源列秩缺口；普通槽数量不能掩盖它。
3. 若前两项均未触发但实际 \(\nu_q(U)<|U|\)，输出普通
   \(\mathrm{HALL\_DEFICIT}\)；缺口来自 source-switch/SNF/范围兼容边的局部稀疏。
4. 只有所有请求子集都通过 (8) 的三个必要层次时，才可调用 Rado 独立代表定理
   构造独立源列匹配，再把匹配后的真实 q-height 送入 Kneser 稳定子容量。

若某边在 SNF、CRT 或 \(B'>A\) 门失败，应先记 EDGE_OBSTRUCTED，不将该边计入
\(\mathcal C_q(U)\)；这与 (9)--(10) 的真实容量缺口不同。

## 4. 证明

式 (5) 由槽定义和 \(f_s\le v_q(p+4s)\) 直接得到。式 (6) 使用 \(q\nmid4\)：
所有满足 \(q^j\mid p+4s\) 的移位落在同一个模 \(q^j\) 残类中，所以数量不超过
该层的最大占用 \(C_j(S_U,q)\)。对 \(j=1,\ldots,E_U\) 求和即得 (7)。

线性独立匹配要求所选源列独立，故 \(|U|\le\rho_\ell(U)\)；不同请求必须使用
不同槽，故 \(\rho_\ell(U)\le\nu_q(U)\)。与 (7) 合并得到 (8)。若 q 上界失败，
先得到 (9)；否则若源列秩失败得到 (10)；两项均通过后，普通 Hall 给出实际边集
的匹配/缺口二分，故优先分派穷尽。证毕。

## 5. 构造性边界

### \(p=433\)、\(q=7\) 的紧 q 进链

取
\[
S=\{16,100\},\qquad
v_7(433+4\cdot16)=1,\qquad
v_7(433+4\cdot100)=2.
\]
则
\[
C_1(S,7)=2,\qquad C_2(S,7)=1,\qquad
\mathsf C_7(S)=3.
\]
实际层槽数也是 \(1+2=3\)，所以 (7) 达到等号。若一个跨状态角色族要求
两条来源都支付 \(7^2\)，其展开请求数为 \(4\)，而 \(\mathsf C_7(S)=3\)，
立即得到
\[
\mathrm{Q\_ADIC\_LAYER\_CAPACITY\_DEFICIT}
=(4-3).
\]
这严格排除了把同一 q 的第二层复制给两个状态。

### 线性秩先于槽数量

若 \(V_\ell=\mathbb F_2^2\)，两个请求都允许两个槽，但
\[
v_{c_1}=v_{c_2}=(1,0),
\]
则 \(\nu_q(U)=2\) 可能通过普通 Hall，而
\(\rho_2(U)=1<2\)，必须输出
\(\mathrm{LINEAR\_RANK\_DEFICIT}\)，不能输出 q 进容量充足。

## 6. 与统一选择器的接口

对跨状态 SOURCE_RANK_DEMAND，先用 (9) 检查移位 q 进层的全局上界；若通过，再用
(10) 检查真实源列独立性。通过这两个切割后，才允许调用
type-II-cross-state-source-demand-hall-capacity-bridge 和单纤维
Kneser 稳定子增长—吸收证书。若 (10) 发生，当前请求族必须转另一 q/另一条
Type I/II 射线、已证明的 LOWER_RELAY 或新的严格下降；该回执本身不是猜想反例。

对于多个 q-primary 方向，可对每个 q 分别形成 (7)，再用 Rado/Hall 的带标签并集
检查兼容性；不能把不同 q 的最大占用简单相加而忽略请求的跨 q 复用约束。

## 研究边界

该切割完成了一个新的可计算容量映射：对任意请求子集同时给出源列秩上界、实际
合法槽上界和只由移位集决定的 q 进上界，并区分三种不同缺口。它仍不证明
Q_ADIC_LAYER_CAPACITY_DEFICIT 必然已经有 LOWER_RELAY，也不识别不同 q 的共同稳定子
商；全局闭合仍需把这些严格缺口接到保持标签的良基下降或 Type I/F/G 终端。
