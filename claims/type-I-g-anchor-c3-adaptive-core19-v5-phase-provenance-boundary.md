---
kind: claim
claim_id: type-I-g-anchor-c3-adaptive-core19-v5-phase-provenance-boundary
title: v=5 q=19 相位关系的 provenance 边界与条件重建
statement: 在 v=5、D=6303 的完整带标签候选格中，eta(mu)=chi(H) 只给出 raw mark 与 candidate cofactor 的多值关系，不能推出 H 的 19-adic 高度、N_A 的 19-adic 预算或 A 标签。特别地，C38 的 phase zeta^11 有 8 个带标签 candidate cofactors，其 v19(H) 取遍 0,1,2,3；即使固定 A=573，仍有四个同 phase cofactor 分别具有 0,1,2,3 的高度。另一方面，若 future adapter 独立证明 A=573 与共同 q-free base U=53*3671，并使 H_i=U*19^j (0<=j<=3)，则三条 raw phase zeta^16,zeta^8,zeta^11 唯一强制 j=(0,1,3)。此外，对任何 191|D 的 target-odd h=-1 (mod 4D)，chi(h)=1；因此三条当前非平凡 raw phase 均不能经 eta-preserving 的直接 identification 变成 target 因子。更强地，若试图以 cH=-1 (mod 25212) 作乘法 phase correction，则 c=-H^(-1) 唯一依赖 H (mod 25212)；同一 (A,phase)=(573,11) 的四个 H 已要求四个不同 c，故 phase 或 (A,phase) 单独不足以调谐 target residue。结论要求 raw-to-fiber functor 明确保留 factor provenance、candidate label、cofactor residue、shared-q ledger 与 slot injection；它不构成 adapter、capacity 或 selector edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-c3-adaptive-core19-v5-c38-q19-phase-leaf
  - type-I-g-anchor-c3-adaptive-core19-v5-d6303-complete-fiber-boundary
  - type-I-g-anchor-c3-adaptive-core19-v5-q19-phase-compatible-candidate-fiber
  - type-I-g-anchor-c3-adaptive-core19-v5-signed-marked-source-groupoid
topics:
  - type-I
  - Type-II
  - c3
  - core19
  - signed-mark
  - raw-source
  - candidate-fiber
  - q-primary
  - q-adic-height
  - provenance
  - target-odd
  - no-go
  - conditional-reconstruction
  - phase-correction
  - target-residue
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_c3_adaptive_core19_v5_phase_provenance_boundary.py
    role: tagged phase fibers, q-height disguise, conditional reconstruction, and target-phase barrier
visibility: public
last_checked: '2026-08-07'
---

# v=5 相位关系的 provenance 边界

这张卡把“有相同 character”与“有同一 cofactor、高度、candidate record 或 slot”严格
分开，并给出未来 adapter 若补齐 q-free provenance 后可使用的条件重建准则。

## 1. 相位只给出多值关系

固定

\[
D=6303,\qquad
\chi(h)=h^{10}\pmod {191},\qquad
\zeta=150.
\tag{1}
\]

对带标签候选格

\[
\mathscr C=\{(A,H):A\mid D,\ H\mid N_A=p+4DA\},
\tag{2}
\]

记 \(\nu_H=v_{19}(H)\)、\(\nu_N=v_{19}(N_A)\)。三条实际 raw leaf 的 phase 是

\[
\eta(\mu_{C_0},\mu_{C_1},\mu_{C_{38}})
=\left(\zeta^{16},\zeta^8,\zeta^{11}\right).
\tag{3}
\]

第三个 phase 的完整 tagged cofactor fiber 为

\[
\begin{array}{c|c|c|c}
A&H&\nu_H&\nu_N-\nu_H\\ \hline
3&19&1&0\\
11&70715591&0&0\\
11&495009137&0&0\\
11&3465063959&0&0\\
573&19&1&2\\
573&1014049&2&1\\
573&3307571&0&3\\
573&1334507617&3&0.
\end{array}
\tag{4}
\]

表中每一行都满足 \(\chi(H)=\zeta^{11}\)。故仅由

\[
\eta(\mu)=\chi(H)
\tag{5}
\]

不能推出任何在 (4) 上不恒定的性质，例如 \(\nu_H\)、\(\nu_N\)、\(A\)、\(b=DA\)
或 slot。固定查表可以任选 \(H\)，但那是额外选择，不是 (5) 导出的 raw functor。

对三个实际 phase，完整枚举摘要为

\[
\begin{array}{c|c|c|c}
\text{leaf}&\text{candidate 个数}&\nu_H\text{ 可取值}&\nu_N\text{ 可取值}\\ \hline
C_0&3&\{0\}&\{0,3\}\\
C_1&3&\{0,1\}&\{0,3\}\\
C_{38}&8&\{0,1,2,3\}&\{0,1,3\}.
\end{array}
\tag{6}
\]

所以 \(C_0\) 的 phase 虽强制 cofactor \(19\)-free，仍不能认证 candidate record；
\(C_1\) 不能由 phase 判定高度 \(0\) 或 \(1\)；\(C_{38}\) 连正 \(19\)-高度都不能
由 phase 判定。

## 2. 同一 record 内的四高度伪装

即使未来已知 \(A=573\)，phase 仍不能恢复 \(H\) 的高度。定义

\[
\begin{aligned}
H^{(0)}&=3307571,\\
H^{(1)}&=19,\\
H^{(2)}&=1014049=19^2\cdot2809,\\
H^{(3)}&=1334507617=19^3\cdot194563.
\end{aligned}
\tag{7}
\]

它们全部整除 \(N_{573}\)，并且

\[
\chi(H^{(j)})=\zeta^{11},
\qquad
v_{19}(H^{(j)})=j
\quad(0\le j\le3).
\tag{8}
\]

另 \(H=19\) 同时出现在 \(A=3\) 和 \(A=573\)，而记录高度分别为 \(1,3\)；所以即便
保存 \(H\) 本身，也不能省略 \(A/b/N_A\) 标签来认证 shared-q 总预算。

## 3. 条件性的正向重建

令

\[
U=53\cdot3671=194563,\qquad
H_j=U19^j\quad(0\le j\le3).
\tag{9}
\]

则

\[
\left(\chi(H_0),\chi(H_1),\chi(H_2),\chi(H_3)\right)
=\left(\zeta^{16},\zeta^8,1,\zeta^{11}\right).
\tag{10}
\]

若 future adapter 独立证明共同的 q-free factor provenance \(U\)，并证明三条
occurrence 都在 \(A=573\) 的同一 record 内满足 \(H_i=U19^{j_i}\)，则
\(\operatorname{ord}(\chi(19))=19>3\) 使 (10) 在 \(0\le j_i\le3\) 上单射，故

\[
\boxed{(j_{C_0},j_{C_1},j_{C_{38}})=(0,1,3).}
\tag{11}
\]

这只是条件性 cofactor reconstruction。三个 \(H_i\) 仍嵌套在同一个 \(N_{573}\)，没有
因此产生三条 request、三份 capacity 或三条 physical slot。

## 4. Conductor-191 target phase barrier

若 \(191\mid D\)、\(M=4D\)，且 target-odd 因子满足 \(h\equiv-1\pmod M\)，则
\(h\equiv-1\pmod {191}\)，所以

\[
\boxed{\chi(h)=h^{10}\equiv1\pmod {191}.}
\tag{12}
\]

(3) 的三个 phase 都非平凡，故 eta-preserving 的直接 raw-mark 到 target-factor
identification 在现有三条 leaf 上全部失败。这不是 target-factor 的一般 no-go：
adapter 仍可引入 phase correction、非恒等 mark map，或不使用 \(\chi\) 的整数映射。

已有链 \(U19^j\) 的唯一中性项是

\[
U19^2=70237243\equiv49\pmod {191},\qquad
\frac{70237243+1}{4}=7\cdot11\cdot457\cdot499.
\tag{13}
\]

因 \(191\nmid(70237243+1)\)，它也不可能是任何保留 \(191\) conductor 的 target
factor。故不能把 phase 中性误读为 target-odd。

## 5. Target correction 的残数刚性

上一节只排除了保持相位的直接 identification。也可以试图把一个 candidate cofactor
\(H\in U(M)\) 乘以校正因子 \(c\in U(M)\)，使

\[
cH\equiv-1\pmod M,
\qquad M=25212.
\tag{14}
\]

这里没有 phase 的自由选择：因为 \(H\) 是单位，(14) 当且仅当

\[
\boxed{c\equiv-H^{-1}\pmod M.}
\tag{15}
\]

又 \(191\mid M\)、\(\chi(-1)=1\)，故 (15) 自动给

\[
\chi(c)=\chi(H)^{-1}.
\tag{16}
\]

也就是说，相位校正只是 target 同余的必要投影；它不能替代完整的 \(M\)-残数。
事实上 \(|U(M)|=7600\)，而 \(\chi\) 满射到 19 阶群，所以给定一个 inverse phase
仍有 \(400\) 个单位校正候选。

这个差距在同一 label 内已经不可消除。对 \(C_{38}\) 的 phase \(\zeta^{11}\)，固定
\(A=573\) 后的四个允许 cofactor 是

\[
(H_1,H_2,H_3,H_4)
=(19,1014049,3307571,1334507617),
\tag{17}
\]

其 \(M\)-残数和由 (15) 唯一确定的 target corrections 分别为

\[
\begin{array}{c|cccc}
H\bmod M&19&5569&4799&11245\\ \hline
-H^{-1}\bmod M&23885&22799&21193&24647.
\end{array}
\tag{18}
\]

四个 \(c\) 都有相同 character \(\zeta^8\)，却彼此不同。因此不存在一个单值
\(c=\kappa(A,\operatorname{phase})\)，使 (14) 对 (17) 中每一个当前允许的 \(H\)
同时成立；在未提供区分这四个 \(H\) 的 raw-to-\(H\) provenance 时，对固定 raw mark
\(\mu_{C_{38}}\) 的单值 \(\kappa(\mu_{C_{38}},573)\) 也不能作这种一致认证。

这个结论不排除保存 \(H\bmod M\) 的 correction，也不排除非乘法 map。它说明任何后续
整数 lift 至少要携带 cofactor residue，并给出 \(cH\mid N_A\) 或其它 target factor
的真正整除回执；单独把 \(\chi(c)=\chi(H)^{-1}\) 写进 adapter 并没有 terminal 内容。

## 6. Adapter 的必要信息

任何能升级为 capacity 或 selector 的 raw-to-fiber functor，至少须保留与下列数据等价
的信息：

1. raw occurrence、entry digest、signed tail 与逐边 receipt；
2. candidate fiber 标签 \((D_*,A,b,N_A)\)；
3. \(H\mid N_A\) 的因子回执，以及 \(H\bmod4D_*\)，或等价的 q-free base、指数与残数；
4. shared-q 的来源标签、逐层 ledger 与剩余预算；
5. demand-to-slot 单射及 nonreuse/subset-divisibility 回执。

第 3 项认证 \(\nu_H\)，第 2 项认证 \(\nu_N\)，第 4--5 项才可能把高度转化为 slot。
当前控制没有这些数据，故不构成 adapter、capacity 注入或 selector edge。

窄复现：

    python3 reproductions/type_i_c3_adaptive_core19_v5_phase_provenance_boundary.py --verify
