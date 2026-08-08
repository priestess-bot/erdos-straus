---
kind: claim
claim_id: type-II-owner-projection-source-column-expansion-relay
title: Type II owner 投影源列逃逸的物理槽扩张递降桥
statement: 在 owner-token 流缺口中，若 Rado/线性角色湮灭当前 token 源列而分离一个真实 source column，则任一合法独立外部请求都先按其物理投影分类：投影到新物理槽时，扩张后的物理缺口不增，并在容量释放时停止；投影到旧物理槽时，物理缺口严格增加，输出 OWNER_COLLISION_EXPANSION 而不伪造 Hall 扩张；请求依赖或无合法边分别输出关系或算术障碍。有限请求菜单下，该扩张势严格终止于 source-column 闭合、容量释放、owner collision、依赖关系或边障碍。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-owner-projection-physical-capacity-flow-gate
  - type-II-source-column-escape-finite-expansion-relay
  - type-II-qprefix-owner-escape-capacity-decomposition
  - type-II-owner-weighted-stabilizer-annihilator-well-founded-selector
topics:
  - type-II
  - owner-weight
  - source-column
  - finite-expansion
  - physical-capacity
  - Hall
  - annihilator
  - q-adic
  - well-founded-descent
  - proof-program
sources:
  - claim: type-II-owner-projection-physical-capacity-flow-gate
    role: owner-token-physical-flow-and-linear-trichotomy
  - claim: type-II-source-column-escape-finite-expansion-relay
    role: finite-independent-request-expansion
  - claim: type-II-qprefix-owner-escape-capacity-decomposition
    role: alternate-owner-and-tight-chain-dispatch
  - reproduction: reproductions/type_ii_owner_projection_source_column_expansion.py
    role: new-physical-slot-release-and-collision-controls
visibility: public
last_checked: '2026-08-09'
---

# Type II owner 投影源列逃逸的物理槽扩张递降桥

## 1. 当前缺口与逃逸列

固定一个已经通过 source-SNF、整数回译和 owner token 流建模的有限请求状态。记
\(U\) 为当前独立请求集，\(D(U)\) 为其需求张成空间，\(\widetilde N(U)\) 为
owner token 邻域，\(\mathcal C(U)=\pi(\widetilde N(U))\) 为物理槽邻域，物理容量为

\[
\mathsf P(U)=\sum_{c\in\mathcal C(U)}b(c),
\qquad
\delta_P(U)=|U|-\mathsf P(U).
\tag{1}
\]

假设 \(\delta_P(U)>0\)，并有一个已经通过线性化的角色 \(\lambda\)，满足

\[
\lambda\bigl(\operatorname{span}\{\upsilon(\tau):
\tau\in\widetilde N(U)\}\bigr)=0.
\tag{2}
\]

若某个真实 source column \(g_i\) 满足 \(\lambda(g_i)\ne0\)，称其为当前逃逸列。
任何带有 \(\upsilon(\tau)=g_i\) 的合法 token 都不在
\(\widetilde N(U)\)，因为否则 (2) 会给出 \(\lambda(g_i)=0\)。

## 2. Owner 投影扩张步

取一个逃逸列的合法外部边 \((r,\tau)\)，其中
\(\upsilon(\tau)=g_i\)、\(r\notin U\)。按两个门分类。

### 独立且新物理投影

若

\[
d(r)\notin D(U),
\qquad
\pi(\tau)\notin\mathcal C(U),
\tag{3}
\]

令 \(U'=U\cup\{r\}\)。token 邻域至少增加 \(\tau\)，物理槽邻域至少增加
\(c=\pi(\tau)\)。若新增物理槽集合为
\(\mathcal C_{\rm new}=\mathcal C(U')\setminus\mathcal C(U)\)，则有精确恒等式

\[
\boxed{
\delta_P(U')
=\delta_P(U)+1-\sum_{c\in\mathcal C_{\rm new}}b(c)
\le\delta_P(U).
}
\tag{4}
\]

特别地，若只有一个新槽且 \(b(c)=1\)，物理缺口保持；若
\(b(c)\ge2\) 或一次增加多个槽，则缺口严格释放。每一步都增加一个此前未出现的
独立请求，随后必须重算流、需求空间和角色。

### 独立但旧物理投影

若 \(d(r)\notin D(U)\) 但

\[
\pi(\tau)\in\mathcal C(U),
\tag{5}
\]

则 \(\mathsf P(U')=\mathsf P(U)\)，从而

\[
\boxed{\delta_P(U')=\delta_P(U)+1.}
\tag{6}
\]

这不是普通 Hall 扩张；输出

\[
\mathrm{OWNER\_COLLISION\_EXPANSION}
(i,r,\tau,\pi(\tau),\delta_P(U)).
\tag{7}
\]

该回执要求改找 alternate owner、提高显式复用预算 \(b(c)\)、进入 q-prefix 紧链
或调用广义 \(2^j\) 终端。不能仅因 token 标签新而把 (7) 当作新增物理容量。

### 依赖边与无边

若所有逃逸列外部边都满足

\[
d(r)\in D(U),
\tag{8}
\]

则记录具体坐标关系
\(\mathrm{DEPENDENT\_OWNER\_ESCAPE\_RELATION}\)，不增加独立请求势。
若没有任何 source-SNF、CRT、范围和标签门均通过的 token，输出
\(\mathrm{OWNER\_SOURCE\_COLUMN\_EDGE\_OBSTRUCTED}\)，并保留完整失败行。

## 3. 有限终止和递归接口

只在 (3) 成立且物理投影新时扩张。定义独立扩张势

\[
\Psi_{\rm owner}(U)=|\mathcal R|-|U|,
\tag{9}
\]

其中 \(\mathcal R\) 是完整有限独立请求菜单。每次扩张使
\(\Psi_{\rm owner}\) 严格减一，因此不可能循环。每次扩张后按以下顺序重算：

1. 若 \(\delta_P(U')\le0\)，输出
   \(\mathrm{OWNER\_PROJECTION\_EXPANSION\_RELEASE}\)，停止沿用旧缺口角色，
   转入普通 Hall、q 进容量或 Kneser 分派；
2. 若新角色湮灭全部真实 source columns，输出
   \(\mathrm{OWNER\_SOURCE\_COLUMN\_CLOSED}\)，可调用 annihilator 子群/商二分；
3. 若仍有逃逸列，继续应用本节四种边分类；
4. 若只剩 (7)、依赖关系或边障碍，输出相应 typed 回执，不把它写成递归边。

若外部边的物理投影都落入旧槽，(6) 说明扩张会消耗而不是释放当前物理势；这正是
owner collision 必须优先于 source-column 闭合处理的原因。

## 4. 证明

由 (2)，逃逸列的合法 token 不在当前 token 邻域，所以 (3) 中加入的 \(\tau\)
是新 token。新物理投影条件保证 \(\pi(\tau)\) 不在 \(\mathcal C(U)\)，而其它
新增物理槽也只能增加容量；直接代入 (1) 得到 (4)。若投影旧槽，则物理容量不变，
请求数增加一，得到 (6)，所以不能把它当作 Hall surplus。

独立性条件使 \(U'\) 仍是可用于 Rado 对偶的请求集；依赖条件只能给出关系 Fourier，
无边条件是有限合法菜单上的穷尽。由于 \(|U|\) 每次只在 (3) 分支增加一，(9) 保证
有限终止。终止时容量释放、全源列闭合、collision、依赖和算术障碍覆盖所有
外部边类型，故分派完备。证毕。

## 5. 构造性控制

### 新物理槽：缺口不增

取 \(|U|=2\)、\(\mathsf P(U)=1\)、一个独立外部请求，其 token 投影到容量为
\(b(c)=1\) 的新槽。则

\[
\delta_P(U)=1,\qquad
\delta_P(U')=3-2=1,
\]

正好验证 (4) 的等号情形。若新槽容量改为 \(2\)，则
\(\delta_P(U')=3-3=0\)，触发容量释放。

### 旧物理槽：严格 collision

仍取 \(|U|=2,\mathsf P(U)=1\)，让独立外部 token 投影到已有容量为一的槽。
此时

\[
\delta_P(U')=3-1=2=\delta_P(U)+1,
\]

触发 'OWNER_COLLISION_EXPANSION'，而不是 source-column surplus。

### 真实 owner 控制

在 \(p=57399241,D=41,f=(1,1)\) 中，source rows \(a=1,41\) 对共同因子
\(q=5\) 给出两个 owner token，但都投影到同一个物理 \(q=5\) 槽。若当前
\(b(c_5)=1\)，任意试图把两个 owner 当成两个独立扩张槽的操作都落入 (5)--(7)；
只有显式的跨状态复用合同或 alternate owner 才能改变该结论。

## 研究边界

该引理把 owner 加权流缺口接到有限 source-column expansion，并证明了“新物理槽
扩张不增缺口、旧物理槽扩张反增缺口”的精确势关系。它仍不保证每个逃逸列存在
新物理投影的独立外部边；collision、依赖和算术障碍必须分别接入 alternate-owner、
q-prefix/广义 \(2^j\) 终端或其它 Type I/II 射线。全局选择器的剩余决定性条件现在
是：对 rank-annihilator 分支证明新物理槽边或直接构造上述终端。
