---
kind: claim
claim_id: type-I-fixed-fiber-affine-qprimary-phase-collapse
title: overflow 固定纤维的全账本仿射 q 进相位碰撞
statement: 固定 overflow 参数 (p,A,d)，令 C=p-d。所有实际 carrier M 满足 M=0 (mod A)、4dM=-1 (mod p)，因而在模 Ap 下属于同一剩余类。于是任意固定整数仿射标签 lambda(M)=alpha M+beta，在 q^k|Ap 的每一层都对整条纤维取同一个 q^k 相位；相位树的 D_k=1，直到 k=v_q(Ap)。若一个有限 source-map 在同一固定纤维声称需要两个不同的该类相位标签，则得到精确的 FIXED_FIBER_PHASE_COLLISION，而不是 q 进容量超载或递降。只有跨 A/d/bundle、使用 q^k 不整除 Ap 的标签，或引入非载体坐标，才能避开该碰撞。本结论不把任意 Fourier 标签自动归入载体仿射标签。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-e2-fixed-fiber-constancy
  - type-I-fg-physical-carry-arc-lift-interface
topics:
  - type-I
  - overflow
  - fixed-fiber
  - q-adic
  - phase-collapse
  - source-map
  - Hall
  - capacity
  - proof-boundary
sources:
  - claim: type-I-overflow-e2-fixed-fiber-constancy
    role: fixed-fiber-crt
  - claim: type-I-fg-physical-carry-arc-lift-interface
    role: physical-carry-label-interface
visibility: public
last_checked: '2026-08-09'
---

# overflow 固定纤维的全账本仿射 (q) 进相位碰撞

## 1. 固定纤维的更强 CRT

固定素数 (p)、(0<d<p) 和正整数 (A)。设 (M) 是一个实际 overflow carrier：

\[
A\mid M,
\qquad
pn=4dM+1
\tag{1}
\]

对某个正整数 (n) 成立。由 (1) 模 (p) 得

\[
4dM\equiv-1\pmod p.
\tag{2}
\]

因为 (p\nmid M)，所以 (p\nmid A)，且 (4d) 在模 (p) 下可逆。令

\[
r_d=[-(4d)^{-1}]_p\in\{1,\ldots,p-1\}.
\]

任意同一固定纤维中的两个 carrier (M,M') 都满足

\[
M\equiv M'\equiv0\pmod A,
\qquad
M\equiv M'\equiv r_d\pmod p.
\]

中国剩余定理给出

\[
\boxed{M\equiv M'\pmod{Ap}.}
\tag{3}
\]

这比只记录 E2 所需的 (ap)（其中 (a=A/(A,p-d))）更强：固定纤维的完整物理
carrier residue 在 (Ap) 上已经坍缩。

## 2. 仿射相位坍缩引理

固定整数 \(\alpha,\beta\)，并由物理 carrier 定义整数标签

\[
s(M)=\alpha M+\beta.
\tag{4}
\]

取任意素数 (q) 和 (k\ge1)，满足

\[
q^k\mid Ap.
\tag{5}
\]

由 (3)--(4)，对同一固定纤维中的所有 (M) 有

\[
\boxed{s(M)\equiv s(M')\pmod{q^k}.}
\tag{6}
\]

因此，若 \(W\) 是该纤维中任意有限物理行集，令

\[
\mathcal R_j(W)=\{s(M)\bmod q^j:M\in W\},
\qquad
D_j(W)=|\mathcal R_j(W)|,
\]

则

\[
\boxed{D_j(W)=1\qquad(1\le j\le v_q(Ap)).}
\tag{7}
\]

这是一条真实的相位树结论，而不是把 Fourier 角色阶当作载体高度。它只适用于
明确由同一整数载体通过固定仿射规则产生的标签。

### 证明

由 (3)，(M-M'=Ap\,t)；代入 (4) 得

\[
s(M)-s(M')=\alpha Ap\,t.
\]

条件 (5) 使右侧被 (q^k) 整除，故 (6) 成立。对 (j\le v_q(Ap)) 应用 (6)，
所有行的相位残基相同，得到 (7)。证毕。

## 3. 对 source-map 与 Hall 账本的精确回执

若一个固定纤维的有限 source table 对同一个标签规则 (4) 给出两个要求

\[
\lambda_1\not\equiv\lambda_2pmod{q^j},
\qquad
j\le v_q(Ap),
\tag{8}
\]

则 (7) 说明没有任何实际 carrier 能同时实现这张表。规范回执为

\[
\boxed{\mathrm{FIXED\_FIBER\_PHASE\_COLLISION}}
\tag{9}
\]

并保存 ((p,A,d,q,j,\alpha,\beta,\lambda_1,\lambda_2))。这不是
`DUAL_PHASE_TREE_CAPACITY_DEFICIT`：后者假设相位标签已经存在，再比较盒容量；
(9) 是 source-map 在固定纤维内部的局部不可实现。

若 Hall 图把相位残基本身作为槽 ID，并在同一残基上合并重复来源，则在
\(j\le v_q(Ap)\) 的层面只有一个相位槽。增加同纤维的物理行数不会增加不同槽数；
若账本给该残基的最大重复容量为 \(\mu\)，其可支付单位至多是该槽的 \(\mu\)，
而不是行数乘以 \(\mu\)。因此请求集合若需要两个互异的该层相位，先触发 (9)，
不能把同一个固定纤维的重复行计作两个 q 进颜色。

## 4. 必须跨越的边界

式 (7) 只封闭 (q^j\mid Ap) 的层。若 (j>v_q(Ap))，(3) 不再强制相位相同，
不能从本引理推出碰撞；这正是更高层 alternate/source-switch 可能开始提供新坐标的
边界。另一方面，任意抽象 Fourier 标签并不必是 (4) 的仿射物理标签；若没有独立的
integer source map，不能套用 (7)。

所以固定纤维内的选择器必须按以下顺序处理：

1. 先在 (Ap) 上合并载体相位并检查 (9)；
2. 再决定是否有高于 (v_q(Ap)) 的真实 q 进标签；
3. 若没有，则跨 (A/d/bundle) 或换用非载体坐标，并重新通过 source-switch、SNF、
   范围和 E1--E5 提升门。

这把“同纤维多行能否提供多个 q 进槽”的问题从容量猜测降为一个精确的 CRT 检查，
但不自动给出 Type I/II 短证书或整数递降。

## 5. 算术控制

取

\[
(p,d,A)=(73,1,27),
\qquad
r_d=18,
\qquad
Ap=1971.
\]

三个实际 carriers 为

\[
M\in\{675,2646,10530\},
\]

对应 (n\in\{37,145,577\})，均满足 (1) 和 overflow 范围。它们都满足

\[
M\equiv0\pmod{27},
\qquad
M\equiv18\pmod{73},
\qquad
M\equiv675\pmod{1971}.
\]

取 (s(M)=M+1)，则 (q=3) 的前三层相位全部分别为 (1\pmod3)、(1\pmod9)、
(1\pmod{27})，因为 (v_3(Ap)=3)。因此要求同一固定纤维产生

\[
0\pmod3\quad\text{和}\quad1\pmod3
\]

的两行 source table 必然触发 `FIXED_FIBER_PHASE_COLLISION`。在第四层则不再有
该结论：三个 carriers 的 (M\bmod81) 分别为 (27,54,0)，说明本引理的层边界是
实际的，不能无限上推。

该算术控制只说明固定纤维 phase slot 的合并规则；它不是 Erdős--Straus 猜想的
反例，也不排除同一例的其它固定-(n)、固定-(s)、Type I/II 或重图表出口。

