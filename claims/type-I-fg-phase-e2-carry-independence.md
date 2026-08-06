---
kind: claim
claim_id: type-I-fg-phase-e2-carry-independence
title: F/G 有限相位实现与 overflow E2 carry 门的独立性
statement: 有限带标记 source 菜单的饱和、复角色相位实现，乃至一个指定 q-primary 角色的存在，都不能推出 overflow cofactor 的带账本 E2 条件 A/gcd(A,p-d)|(M mod p)。严格反模型可取 p=73、d=A=18、M=1242=17p+1：它有一个饱和且相位可实现的单行 H=U(5), E=C2 带标记模型，但 a=18 不整除 M mod p=1。要把有限相位数据接到 E2，必须额外携带整数 carry 坐标 kappa=floor(M/p) mod a；kappa=0 与 E2 恰等价。这一结论只否定“纯有限相位数据自动给 E2”的推断，不否定加入实际整数 source map 后的 lift。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fg-marked-source-menu-saturation
  - type-I-overflow-cofactor-ledger-e2-gate
topics:
  - type-I
  - F-state
  - G-state
  - source-map
  - Fourier
  - marked-menu
  - SNF
  - overflow
  - cofactor
  - E2
  - carry
  - no-carry
  - counterexample
  - proof-boundary
sources:
  - claim: type-I-fg-marked-source-menu-saturation
    role: finite-marked-phase-interface
  - claim: type-I-overflow-cofactor-ledger-e2-gate
    role: ledger-persistence-interface
visibility: public
last_checked: '2026-08-06'
---

# F/G 有限相位实现与 overflow E2 carry 门的独立性

## 1. 两类数据的逻辑差别

有限带标记菜单只记录一组有限阿贝尔群元素与角色标签：它可以严格检验菜单饱和、
source--target 相位关系和固定阶角色门。overflow cofactor 的 E2 则还要求一个实际整数
carrier \(M\) 满足

\[
a\mid r,
\qquad
a=\frac{A}{(A,p-d)},
\qquad
r=M\bmod p\in\{1,\ldots,p-1\}.
\tag{1}
\]

下面的反模型说明，前一类有限数据不能推出后一类整数条件。

## 2. 严格反模型

取真实 overflow 行列式的整数数据

\[
p=73,
\qquad d=A=18,
\qquad M=1242=17p+1,
\qquad n=1225.
\tag{2}
\]

确有

\[
73\cdot1225=4\cdot1242\cdot18+1.
\tag{3}
\]

因此 \(r=1\)、\(C=p-d=55\)，以及

\[
a=\frac{18}{(18,55)}=18,
\qquad
a\nmid r.
\tag{4}
\]

现在只考虑有限相位层。令 \(H=U(5)=\langle2\rangle\simeq C_4\)、
\(E=C_2\)，并定义一个单行完整 table、菜单和目标 table：

\[
\mathcal A=\mathcal M=\mathcal T=\{(2,1)\}\subset H\oplus E.
\tag{5}
\]

这里的群坐标是物理整数 \(M\bmod5=2\)，但 (5) 是一个有限相位模型，
不声称它是某个额外 Type II divisor lattice 的完整来源宇宙。其带标记子群为

\[
\Gamma(\mathcal A)=\langle(2,1)\rangle
=\{(1,0),(2,1),(4,0),(3,1)\}.
\tag{6}
\]

它没有非平凡纯标记元，故 \(V(\Gamma(\mathcal A))=0\)，且

\[
\Gamma(\mathcal M)=\Gamma(\mathcal A),
\qquad
V\bigl(\Gamma(\mathcal M)+\Gamma(\mathcal T)\bigr)=0.
\tag{7}
\]

因此菜单完全饱和并实现目标相位。更具体地，模 \(5\) 二次角色满足

\[
\chi_5(2)=-1=\zeta_2^1,
\tag{8}
\]

所以这里甚至存在一个阶恰为 \(2\) 的指定 primary 角色。式 (4) 仍表明 E2 失败。
这严格反驳了“有限 marked/Fourier/SNF 相位数据自动给 E2”的逻辑推断。

## 3. 必需新增的 carry 坐标

对每个实际物理 carrier \(M\)，定义

\[
\kappa_{p,A,d}(M)=\left\lfloor\frac Mp\right\rfloor\bmod a,
\qquad
a=\frac{A}{(A,p-d)}.
\tag{9}
\]

由于 \(a\mid M\) 且 \((a,p)=1\)，有精确等价式

\[
\boxed{
\kappa_{p,A,d}(M)=0
\ \Longleftrightarrow\
M\equiv r\pmod {ap}
\ \Longleftrightarrow\
a\mid r
\ \Longleftrightarrow\
\text{E2 通过}.
}
\tag{10}
\]

若 \(t=[M/a]_p\)，(10) 也等价于 \(at<p\)。对 (2)，

\[
\kappa_{73,18,18}(1242)=17\ne0,
\qquad
t=69,
\qquad18\cdot69>73.
\tag{11}
\]

因此 future source-map 的最小充分接口不能只有有限群像、标签和 SNF；它必须携带
\(\kappa\)（或等价的 \(M\bmod ap\)）并把 \(\kappa=0\) 作为整数 lift 的独立门。

## 4. 边界

本卡不说任何一个真实 F/G source menu 都会像 (5) 一样失败，也不排除某个带实际
integer source map 的菜单同时证明相位与 carry。它只证明：若丢失 (9) 的加法商坐标，
则有限角色/SNF 相位信息本身不足以推出 E2；因而不能把 Fourier 相位、角色阶或
source-menu 饱和直接收费为带账本 cofactor 递降。
