---
kind: claim
claim_id: type-i-ii-source-universe-admission-expansion-relay
title: Type I/II source universe 漏项的 admission—容量扩张递降桥
statement: 在 exact source contract、exact source-to-request admission map 和 source-preserving physical projection 已通过的有限状态中，按字典序加入 source universe 的最小未处理记录。若该记录有独立请求且投影到新物理 q 槽，扩张后的 exact flow 缺口不增加，并在容量释放时输出 typed release；若投影到旧槽则输出 owner collision，依赖方向则输出 source-relation circuit；无合法 admission edge 则输出不收费的 SOURCE_RECORD_UNREALIZED。未处理记录势每次严格下降，有限宇宙最终到达 source-map 完备、容量释放、依赖回路或显式障碍；只有 E1--E5 source-switch 通过后，后继才可登记为严格可提升递降。
claim_status: conditional
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-i-ii-fg-universal-finite-source-map-completion
  - type-II-owner-exact-flow-negative-certificate-relay
  - type-II-owner-projection-source-column-expansion-relay
  - type-II-source-column-escape-finite-expansion-relay
  - type-II-owner-joint-circuit-arithmetic-lift-trichotomy
  - type-II-owner-source-preserving-fiber-uniformity-criterion
topics:
  - type-I
  - type-II
  - F-state
  - G-state
  - source-map
  - finite-expansion
  - admission
  - q-capacity
  - owner-collision
  - relation-circuit
  - well-founded-descent
  - proof-program
sources:
  - claim: type-i-ii-fg-universal-finite-source-map-completion
    role: finite-source-universe
  - claim: type-II-owner-exact-flow-negative-certificate-relay
    role: exact-flow-negative-dispatch
  - claim: type-II-owner-projection-source-column-expansion-relay
    role: physical-new-slot-versus-collision
  - claim: type-II-owner-joint-circuit-arithmetic-lift-trichotomy
    role: dependent-source-arithmetic-trichotomy
  - reproduction: reproductions/type_i_ii_source_universe_admission_expansion_relay.py
    role: finite-potential-controls
visibility: public
last_checked: '2026-08-09'
---

# Type I/II source universe 漏项的 admission—容量扩张递降桥

## 1. 三个 exactness 门

固定一个已经由 [Type I/II F-G 源映射的有限整数宇宙完备化](type-I-II-fg-universal-finite-source-map-completion.md)
给出的有限整数宇宙 \(\mathcal U\)，当前已处理菜单为 \(\mathcal M\subseteq\mathcal U\)，
并固定目标请求集合 \(\mathcal R\)。本桥只在下列三个条件都已证明时运行：

1. **source exactness：** \(\mathcal U\) 恰包含当前整数 source contract 的全部记录；
2. **admission exactness：** 对每个 \(r\in\mathcal U\)，有限映射
   \[
   \operatorname{Adm}(r)\subseteq
   \mathcal R\times\mathcal S
   \tag{1}
   \]
   恰包含该 source 对目标请求和物理槽的所有合法边，并保留 source vector、q-height、
   SNF、范围和来源标签；
3. **physical canonicalization：** 同一物理槽的所有合法边共享
   \((q\text{-layer},\text{source record},v_s)\) 签名。

若任一门失败，分别输出
\(\mathrm{SOURCE\_CONTRACT\_EXACTNESS\_UNPROVED}\)、
\(\mathrm{SOURCE\_ADMISSION\_EXACTNESS\_UNPROVED}\) 或
\(\mathrm{OWNER\_TOKEN\_SOURCE\_CANONICALIZATION\_OBSTRUCTED}\)，不能把漏项直接
收费为 q 容量。

## 2. 最小漏项和扩张势

若 \(\mathcal M\ne\mathcal U\)，按固定字典序取
\[
r_*:=\min(\mathcal U\setminus\mathcal M),
\qquad
\Psi(\mathcal M):=|\mathcal U\setminus\mathcal M|.
\tag{2}
\]
只处理 \(r_*\)，然后令 \(\mathcal M^+=\mathcal M\cup\{r_*\}\)。任何继续处理的
分支都有
\[
\boxed{\Psi(\mathcal M^+)=\Psi(\mathcal M)-1.}
\tag{3}
\]
因此 source-universe 补全阶段不会循环，也不会因不同 Fourier 角色重复加入同一
整数记录。

## 3. admission 分类

### A. 无合法请求边

若
\[
\operatorname{Adm}(r_*)=\varnothing,
\tag{4}
\]
输出
\[
\mathrm{SOURCE\_RECORD\_UNREALIZED}(r_*).
\tag{5}
\]
该记录是 exact contract 中的真实 source，但对当前目标请求没有合法同纤维边；它
不产生 q demand，也不能被静默从 source-map 删除。若它分离当前 Rado 角色，保存为
SOURCE_COLUMN_ESCAPE 并执行已有有限扩张；否则只作为不收费的 source provenance。

### B. 新物理槽和独立请求

设 \((r,c)\in\operatorname{Adm}(r_*)\)，且 \(c\) 在当前物理槽集合中不存在，
请求方向 \(d(r)\) 不属于当前独立请求张成空间。把对应 source/token edge 加入
容量展开图。新槽至少提供一个新的容量副本，因此对当前请求集的 Hall 缺口
\(\delta=|U|-|N(U)|\) 有
\[
\delta^+\le\delta.
\tag{6}
\]
重新运行 exact flow：

* 若缺口消失，输出
  \(\mathrm{SOURCE\_UNIVERSE\_EXPANSION\_RELEASE}\)，转入普通 Rado/Hall 或
  F/G source-label 分派；
* 若缺口仍在，保存更新后的最小割和 \(\lambda^+\)，继续处理下一条最小漏项；
* 若 source columns 在满流后线性依赖，输出 source-rank deficit，不把新记录和旧
  记录重复当作独立 q 方向。

式 (6) 是物理槽扩张的容量不增性质；是否最终递降由后续 source-switch/E1--E5
决定，而不是由 (3) 代替。

### C. 旧物理槽

若所有 \(\operatorname{Adm}(r_*)\) 都投影到已有物理槽，则新增整数记录不增加
物理容量，输出
\[
\mathrm{SOURCE\_UNIVERSE\_OWNER\_COLLISION}(r_*,c).
\tag{7}
\]
若其请求方向独立，仍可把它加入 exact flow 的 token 菜单，但必须沿用旧槽预算；若
请求方向依赖当前请求集，取最小依赖系数并输出
\[
\mathrm{SOURCE\_UNIVERSE\_RELATION\_CIRCUIT}(r_*,c,\bar c).
\tag{8}
\]
回路随后进入 SNF/CRT/power-closed 三分；在直接命中或严格 source-switch 之外，
同模数关系 Fourier 只是后继输入，不是新 q 容量。

## 4. 有限 typed 后继

从 \(\mathcal M_0\) 开始反复应用 (2)--(8)。因为 \(\Psi\) 是非负整数，最多
\(|\mathcal U|\) 次加入后终止。终止状态只可能是：

1. \(\mathcal M=\mathcal U\)，随后进入带标记 SNF 和 exact-flow 负证书分派；
2. 新槽使 q flow 释放，进入 Rado/Hall/F/G；
3. 旧槽碰撞或依赖回路，进入 owner circuit 算术三分；
4. 某个合法 source record 没有目标 admission edge，输出 (5) 和完整失败行。

这些状态不互相替代：记录完备不等于容量充足，旧槽碰撞不等于 source-map 缺失，
无 admission edge 也不等于算术 no-lift。

若某个终止状态得到抽象较小商、source-switch 或 primary 下降，只有在来源标签、
SNF/CRT、范围、\(B'>A\) 和 E1--E5 全部通过后，才输出
`STRICT_LIFTABLE_DESCENT`；否则保留对应的 `*_LIFT_OBSTRUCTED` 回执。

## 5. 证明

由 source exactness，若 \(\mathcal M\ne\mathcal U\)，(2) 确实选择一个尚未处理的
合法整数 source；加入它得到 (3)。admission exactness 保证 (4) 穷尽无边、独立边
和依赖边，而 physical canonicalization 保证新槽/旧槽分类不把 token-dependent
source vector 合并成一个伪物理资源。

在 B 中，新槽至少有一个未出现在旧邻域的容量副本，故邻域基数增量至少为一，直接
计算得 (6)；最大流重新计算后若饱和，则是 release，否则保留新的 exact min-cut。
在 C 中，投影槽集合没有变化，所以物理容量不增加；线性依赖的最小系数向量是
真实 source relation circuit。有限宇宙保证扩张势最终归零或在当前状态产生一个
typed 后继。最后，整数提升门是原参数递归的必要条件，不能由有限势下降替代。证毕。

## 6. 研究边界

该桥把 exact source universe 的整数漏项真正接回 q 容量和 source-column 选择器，
并给出一个严格良基的 admission 扩张。它仍不证明所有 F/G 状态都有 exact admission
map；`SOURCE_ADMISSION_EXACTNESS_UNPROVED` 是当前全局覆盖缺口的具体名称。它也不
把 source-universe 补全本身宣称为 Type I/II 证书或整数递降；后者仍须经过 exact flow、
SNF/CRT 和 E1--E5。
