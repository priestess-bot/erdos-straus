---
kind: claim
claim_id: type-I-ii-fg-universal-finite-source-map-completion
title: Type I/II F-G 源映射的有限整数宇宙完备化
statement: 对固定的 Type II 整数参数纤维，或固定的 Type I 广义二进图表，若 source contract 明确规定合法记录恰由有限除子、整除、同余、范围和二进预算条件生成，则可以枚举一个有限且完备的整数 source universe。任意候选 source menu 若未覆盖该宇宙，最小漏项给出 SOURCE_UNIVERSE_MENU_ESCAPE；覆盖后再用带标记 SNF 区分群方向逃逸与 source-label 相位关系障碍。记录投影到同一物理 q 槽时只能合并，不增加 q 容量。未证明 source contract 的 exactness 时，唯一回执是 SOURCE_CONTRACT_EXACTNESS_UNPROVED，而不是把角色阶当作 q-height。
claim_status: conditional
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fg-marked-source-menu-saturation
  - type-I-fg-role-snf-terminal-dispatch
  - type-II-q-prefix-source-label-finite-closure
  - type-II-owner-circuit-qcapacity-flow-bridge
  - type-II-owner-exact-flow-negative-certificate-relay
  - type-I-general-dyadic-terminal-transfer
  - type-I-generalized-dyadic-j-one-terminal-normalization
topics:
  - type-I
  - type-II
  - F-state
  - G-state
  - source-map
  - source-completeness
  - finite-enumeration
  - divisor-lattice
  - dyadic
  - q-capacity
  - SNF
  - constructive-certificate
  - proof-program
sources:
  - claim: type-I-fg-marked-source-menu-saturation
    role: marked-group-completeness-test
  - claim: type-I-fg-role-snf-terminal-dispatch
    role: source-label-four-way-dispatch
  - claim: type-II-q-prefix-source-label-finite-closure
    role: finite-q-label-fiber-closure
  - claim: type-I-general-dyadic-terminal-transfer
    role: Type-I-integer-universe
  - claim: type-II-owner-exact-flow-negative-certificate-relay
    role: physical-capacity-after-enumeration
  - reproduction: reproductions/type_i_ii_fg_universal_finite_source_map_completion.py
    role: finite-universe-and-dedup-controls
visibility: public
last_checked: '2026-08-10'
---

# Type I/II F-G 源映射的有限整数宇宙完备化

## 1. 精确 source contract

“source-map 已闭合”不能只表示当前菜单中暂时没有发现新行。先声明一个整数
source contract \(\mathsf C\)，包含：

1. 一个有限参数盒 \(\mathcal B\)；
2. 一组整除、同余、互素、平方自由、范围和二进预算谓词；
3. 一个把合法整数记录送到 \(H\oplus E\) 的群像—标记映射；
4. 一个把记录送到物理 owner/q 槽的投影映射。

要求 \(\mathsf C\) 的 **exactness** 是一个独立算术命题：整数记录属于 contract
当且仅当它是当前 F/G 或 Type I/II 状态允许的真实 source。若 exactness 尚未证明，
回执只能是
\[
\mathrm{SOURCE\_CONTRACT\_EXACTNESS\_UNPROVED};
\tag{1}
\]
下面的有限枚举不会把一个过宽的候选集合误称为实际 source-map。

## 2. Type II 的有限整数宇宙

固定核心素数 \(p\) 和原始除子 \(D\)。把 admissible 参数纤维写成
\[
\mathcal F^{\mathrm{II}}_{p,D}
=\left\{(D_*,A):
\begin{array}{l}
D_*\mid D,\quad A\mid D_*,\quad D_*/A\text{ square-free},\\
4AD_*<p
\end{array}\right\}.
\tag{2}
\]
对 \(f=(D_*,A)\) 令 \(s_f=AD_*\)，并定义整数 source record 宇宙
\[
\mathcal U^{\mathrm{II}}_{p,D}
=\{(f,h):f\in\mathcal F^{\mathrm{II}}_{p,D},\ h\mid p+4s_f,\ h\ge1,
\ \mathsf C_{\mathrm{II}}(f,h)\text{ 通过}\}.
\tag{3}
\]
其中 \(\mathsf C_{\mathrm{II}}\) 可以要求 \((h,4D_*)=1\)、q-primary 形状、来源
索引、shared-q 和其它已声明的 Type II 合同。把所有正因子都先放入候选宇宙，
再由 exact contract 过滤，比只枚举当前 Fourier 角色看到的几个 q 更安全。

该宇宙是有限的：\(D\) 的除子数有限，且每个 \(p+4s_f\) 的正除子数有限。
若需要 q-height 记录，则把
\[
v_q(h)=j\quad(1\le j\le v_q(p+4s_f))
\tag{4}
\]
的每一个 q-primary 前缀作为同一整数 record 的带来源展开；展开不会产生新的
物理槽，物理投影仍按 \(h\) 或 shared-q ledger 去重。

## 3. Type I 广义二进的有限整数宇宙

固定 \(p,R,K\) 满足
\[
4K=pR+1,\qquad L=2K,\qquad (L,R)=1.
\tag{5}
\]
定义
\[
\mathcal U^{\mathrm I}_{p,R,K}
=\left\{(a,b,j):
\begin{array}{l}
a,b\mid L,\ (a,b)=1,\ j\ge1,\\
j\le v_2(L)+v_2(a)-v_2(b),\\
a\equiv2^jb\pmod R,\quad a<2^jb
\end{array}\right\}.
\tag{6}
\]
因为 \(a,b\) 来自有限除子集，且
\[
1\le j\le v_2(L)+v_2(a)-v_2(b)\le v_2(L)+v_2(L),
\tag{7}
\]
式 (6) 是有限集合。每条记录附带
\[
E_j=2^{1-j}L\frac ab,\qquad n_j=\frac{2L-E_j}{R},
\tag{8}
\]
并保存 \((a,b,j)\) provenance。若 source contract 不需要保留二进标签，使用既约
\(j=1\) 归一形作为记录键；原始记录仍保留，不能让同一 \((E_j,n_j)\) 重复收费。

## 4. 完备性和最小漏项证书

令 \(\mathcal M\) 是当前由 Fourier、q-prefix 或局部生成器产生的 source menu，并
令 \(\mathcal U\) 是与该状态相匹配的 (3) 或 (6) 的 contract 宇宙。若 exactness
通过，则
\[
\boxed{
\mathcal M=\mathcal U
\quad\Longleftrightarrow\quad
\text{当前 source-map 已在整数记录层完备}.
}
\tag{9}
\]
若 \(\mathcal M\ne\mathcal U\)，按固定字典序取
\[
r_* =\min(\mathcal U\setminus\mathcal M)
\tag{10}
\]
并输出
\[
\mathrm{SOURCE\_UNIVERSE\_MENU\_ESCAPE}(r_*).
\tag{11}
\]
这不是 arithmetic no-lift：它表示当前生成器漏掉了一个仍在 exact contract 中的
整数 source。只有把 \(r_*\) 加入菜单、或证明它被一个已有记录的带标记群关系蕴含，
才能继续运行带标记 SNF。

若菜单覆盖整数宇宙，把记录映射为
\[
\iota(r)=(u(r),\lambda(r))\in H\oplus E.
\tag{12}
\]
此时先按记录来源保留 provenance，再运行带标记子群饱和：

* 群像未被当前菜单生成：输出 `MARKED_SOURCE_MENU_GROUP_ESCAPE`，并保存一个实际
  整数记录而不是抽象角色阶；
* 群像已生成但标记关系不一致：输出
  `MARKED_SOURCE_MENU_LABEL_RELATION_OBSTRUCTED`；
* 带标记子群相等且目标联合子群没有纯标记元：才允许进入 F/G source-label SNF
  四分和 q-primary exact-order 门。

因此 `F_SOURCE_MAP_UNCLOSED` 只在 (1) 未闭合时使用；对已证明 exactness 的 Type I/II
整数合同，它被 (11) 的具体漏项取代。

若 exact-order 门随后构造了实际 \(q\)-primary roles，则 (12) 同时封闭了所有
eligible edge 的 ambient 群坐标。令
\(S=\langle u(r):r\in\mathcal U\rangle\)，把 role 标签模 \(q\) 后在

\[
V_q=(S+qH)/qH
\]

上取限制，即规范得到 role space、右根基商和每条 record 的 evaluation column。
因此“有限 universe 完备 + fixed-order SNF”足以产出
`SNF_CANONICAL_ROLE_EVALUATION_CERT`；不再需要另猜角色到 source columns 的同构。

## 5. 物理 q 容量不因完备枚举增加

设 \(\pi_{\mathrm{phys}}:\mathcal U\to\mathcal S\) 把整数 source record 投影到
物理 q 槽或 owner 资源。对任一菜单子集 \(X\)，真实容量是
\[
\operatorname{cap}(X)
=\sum_{s\in\pi_{\mathrm{phys}}(X)}b(s),
\tag{13}
\]
而不是 \(|X|\)。同一 q 的不同来源标签、同一 Type-I 终端的不同 \(j\) provenance
或同一 source record 的不同群表示，只能在 exact-flow 网络中共用对应的物理槽容量。
若 \(\pi_{\mathrm{phys}}\) 非均匀地依赖请求，则 source-preserving canonicalization
失败，必须转入联合匹配 obstruction；不能先用 (9) 的完备性给它们分配不同 q 槽。

这一步把两个逻辑问题分开：
\[
\text{source-map completeness}
\quad\ne\quad
\text{physical capacity completeness}.
\tag{14}
\]
前者由有限整数宇宙和 SNF 处理，后者由 exact token—slot flow 与 Rado 处理。

## 6. 证明

式 (2) 的参数对来自有限除子偏序，且范围条件只删去候选；固定 \(f\) 后，
\(h\mid p+4s_f\) 的正因子集合有限，所以 (3) 有限。任何满足 Type II contract
的真实 source 都有某个合法 \(f\)，并且其来源因子整除同一个 \(p+4s_f\)，故属于
(3)；反过来，\(\mathsf C_{\mathrm{II}}\) 的 exactness 保证宇宙中保留的每条记录
都是合法 source。于是 (9) 和 (10)--(11) 成立。

式 (6) 的除子对有限，(7) 给出有限的 \(j\) 窗口；一般二进传输定理说明每条真实
广义二进 source 必满足 (6)，而式 (8) 是其实际终端数据。因此 Type I contract
同样满足 (9)。

带标记映射只是有限记录到有限阿贝尔群的函数；记录层完备后，带标记子群的相等性
和纯标记关系由已有 SNF 判据逐行决定。最后，物理投影的容量定义 (13) 对投影纤维
按集合计数；最大流网络恰好实现该容量，故枚举记录的多重性不会改变 q 流或 Rado
秩。证毕。

## 7. 构造性回执和边界

* `SOURCE_UNIVERSE_MENU_ESCAPE`：有最小漏项，但它仍在 exact integer contract 内；
  优先补菜单或把漏项送入 source-column expansion。
* `MARKED_SOURCE_MENU_GROUP_ESCAPE`：整数宇宙已覆盖，但群像存在未生成方向；
  运行 F/G source-label SNF。
* `MARKED_SOURCE_MENU_LABEL_RELATION_OBSTRUCTED`：群像相同而标签关系矛盾；进入
  source-relation Fourier 或 Type-I/F/G 障碍，不收费 q-height。
* `SOURCE_CONTRACT_EXACTNESS_UNPROVED`：整数宇宙的候选规则尚不能证明恰好等于
  真实 source；这是全局选择器仍需补的外部算术命题。

## 研究边界

该引理把固定 Type I/II 整数合同下的 `source-map unclosed` 改写为有限、可定位的
漏项或带标记 SNF 回执，并证明完整枚举不会制造额外 q 容量。对仍未处理的漏项，
应继续使用 [Type I/II source universe 漏项的 admission—容量扩张递降桥](type-I-ii-source-universe-admission-expansion-relay.md)
将其接回 exact flow，而不是停在菜单审计。它没有证明所有 F/G
状态都属于 (2) 或 (6) 的 exact contract，也没有证明 exactness 未知时的
`SOURCE_CONTRACT_EXACTNESS_UNPROVED` 必然能递降；因此全局剩余问题被精确收缩为
证明 F/G 状态的整数合同覆盖，及其漏项/合同障碍到 Type I/F/G 或 E1--E5 递降的承接。
已闭合分支的规范求值构造见
[F/G source-SNF 的规范初等角色求值商](type-I-fg-snf-canonical-role-evaluation-quotient.md)。
