---
kind: claim
claim_id: type-i-target-odd-d-lattice-affine-menu-completion
title: target-odd 奇 q 与一跳 D-格非零偏移菜单的 source-complete 等价
statement: 固定核心素数 p、D 和一跳保持来源的 canonical D-格 universe。对奇 q 与高度 e，target-odd 相位 gamma=0 的所有菜单内 affine repair 标签恰为 s=AD'，其中 (a,D',A,q,e) 是 canonical route 且 q^e 同时整除 p+4Da 与 p+4AD'；每个这样的标签自动满足 q^e|p+4s，反之任一该 universe 内保持来源的 q^e source-switch 都出现在该 route 菜单。标签按物理 route 去重后，菜单对该 universe source-complete；空集只输出 D_LATTICE_TARGET_ODD_SOURCE_UNCLOSED（相对于该有限 universe），不能升级为全局 no-local-lift。q=2 不产生任何 route。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-i-target-odd-affine-offset-repair-gate
  - type-I-linear-escape-canonical-d-lattice-source-menu
  - type-I-linear-escape-canonical-d-lattice-owner-closure
  - type-i-target-odd-primary-direct-owner-dyadic-two-gate
topics:
  - type-I
  - target-odd
  - q-primary
  - D-lattice
  - affine-source-map
  - source-complete
  - canonical-menu
  - q-prefix
  - physical-capacity
  - proof-program
sources:
  - claim: type-I-linear-escape-canonical-d-lattice-source-menu
    role: finite-D-route-completeness
  - claim: type-I-linear-escape-canonical-d-lattice-owner-closure
    role: route-to-owner-capacity-dispatch
  - claim: type-i-target-odd-affine-offset-repair-gate
    role: beta-offset-gcd-gate
  - reproduction: reproductions/type_i_target_odd_d_lattice_affine_menu_completion.py
    role: p73-menu-hit-and-p67369-menu-escape
visibility: public
last_checked: '2026-08-09'
---

# target-odd 奇 q 与一跳 D-格非零偏移菜单的 source-complete 等价

## 一跳 D-格菜单

固定核心素数 \(p\equiv1\pmod {24}\) 和正整数 \(D\)。只考虑以下已声明的 source
universe：

\[
\mathcal A_D(p)=
\{a:a\mid D,\ D/a\text{ 平方自由},\ 4aD<p\},
\]

\[
\mathcal L_D(p)=
\{(D',A):D'\mid D,\ A\mid D',\ D'/A\text{ 平方自由},\ 4AD'<p\}.
\]

对 \(a\in\mathcal A_D(p)\)、\((D',A)\in\mathcal L_D(p)\) 和素数 \(q\)，定义

\[
N_a=p+4Da,
\qquad
N'_{D',A}=p+4AD',
\]

\[
e_{a,D',A,q}
=\min\{v_q(N_a),v_q(N'_{D',A})\}.
\tag{1}
\]

当 \(e_{a,D',A,q}\ge1\) 时，canonical menu 保存一条 route

\[
(a,D',A,q,e_{a,D',A,q}).
\tag{2}
\]

同一 \(q\) 在一条 profile 中只可取一个前缀高度；相同标签的不同 route 仍须按物理
route/token 计数，不能把一个 owner 槽复制成多个容量槽。

## target-odd 偏移菜单定理

令 \(q\) 为奇素数，\(q\nmid p\)，并取 \(1\le e\le e_{a,D',A,q}\)。把 target-odd
\(q\)-primary 相位的自然值 \(\gamma=0\pmod {q^e}\) 作为 affine map 的输入，则 route
的 canonical source label

\[
s_{D',A}=AD'
\tag{3}
\]

是一个非零偏移（\(s=0+AD'\)），并满足

\[
q^e\mid p+4s_{D',A}.
\tag{4}
\]

定义去重后的菜单标签集合

\[
\mathcal S^{\rm can}_{D,q,e}(p)
=\{AD':(a,D',A,q,e_{a,D',A,q})\text{ 是 route},
\ e\le e_{a,D',A,q}\}.
\tag{5}
\]

则：

1. \(\mathcal S^{\rm can}_{D,q,e}(p)\) 中每个标签都是 affine repair gate 的合法
   \(h=0\) 槽，且其偏移类正是
   \(\beta_e(p)\equiv-p\,4^{-1}\pmod {q^e}\)；
2. 任一属于该一跳 D-格 universe、保持来源语义并携带 \(q^e\) 前缀的 source-switch，
   其物理 route 必在 (2)，其目标标签必在 (5)；
3. 因而按物理 route 和 shared-\(q\) ledger 计数后，(5) 对该 universe
   source-complete。

若 (5) 为空，唯一合法结论是

\[
\boxed{\texttt{D\_LATTICE\_TARGET\_ODD\_SOURCE\_UNCLOSED}}
\]

其含义是“当前固定 \(D\)、一跳保持来源菜单不能承接该角色”，不是整个 Type I/II
source universe 的全局空集。此时必须转入下一层 \(D'\)、raw/外部 source、SNF/CRT
或 Type II/严格递降；不能把空菜单当作 Fourier 角色不存在。

### \(q=2\)

由于 \(p+4Da\) 与 \(p+4AD'\) 都是奇数，菜单 (2) 不含 \(q=2\)。这个结论与直接
\(q\)-prefix 的奇偶 no-go 一致；二进角色只能走广义 \(2^j\) 或其它独立 source map。

## 证明

由 route 定义，\(q^e\mid N'_{D',A}=p+4AD'\)，所以 (3)--(4) 成立；因 \(q\) 奇且
\(q\nmid p\)，4 可逆且该 residue 是非零单位类，正是 affine offset repair gate
的唯一无步长偏移类。另一方面，任何声明中的保持来源 \(q^e\) source-switch 都要求
\(q^e\mid N_a\) 和 \(q^e\mid N'_{D',A}\)，故其 \(e\) 不超过 (1)，并由 canonical
menu 的 source-completeness 出现在 (2)。将所有 route 的目标标签去重后得到 (5)，
shared-\(q\) ledger 处理同 \(q\) 的重复高度，证明第 3 点。\(q=2\) 时两个 \(N\) 都奇，
故不存在正二进 route。证毕。

## 与 Fourier/容量的接线

target-odd 角色本身提供的是零相位；菜单 route 提供的 \(AD'\) 才是实际的非零
算术偏移。选择器必须按以下顺序处理：

\[
\text{target-odd }\gamma=0
\to
\text{canonical }AD'\text{ menu}
\to
\text{\(q\)-prefix/CRT}
\to
\text{physical owner/token flow}
\to
\text{\(q\)-capacity or Type-II terminal}.
\]

如果一个标签在多个 route 出现，容量账本使用 owner/token/physical-slot 的最小流，
而不是 \(|\mathcal S^{\rm can}|\) 的简单倍增。通过菜单只说明 E1--E3 的整数来源已
闭合；Type II 证书、解提升和 E1--E5 仍须独立验证。

## 聚焦控制

### \(p=73,\ D=1\)：菜单命中

此时 \(\mathcal A_D=\{1\}\)、\(\mathcal L_D=\{(1,1)\}\)，且

\[
p+4=77=7\cdot11.
\]

\(q=7\) 与 \(q=11\) 的 route 都给出同一个物理标签 \(s=1\)。分别有

\[
\beta_1(73)\equiv1\pmod7,
\qquad
\beta_1(73)\equiv1\pmod {11},
\]

所以菜单以一个去重 owner 槽承接两条带不同 \(q\) 的 route；同 \(q\) 仍只按一条
前缀计价。

### \(p=67369,\ D=1\)：固定菜单外逃逸

此时同样只有 \(a=D'=A=1\)，但

\[
p+4=67373=89\cdot757.
\]

对 F 控制中 \(K=7\cdot167\cdot389\) 的 \(q=7\) 目标方向，

\[
\beta_1(67369)\equiv5\pmod7,
\]

而 \(7\nmid67373\)，故 (5) 为空。该结果只输出固定 \(D=1\) 菜单的
`SOURCE_UNCLOSED`；它不排除 \(D=7\)、\(D=167\)、\(D=389\) 的下一层来源，也不排除 raw
Type II 或其它图表证书。

## 边界

本卡把 affine repair 的偏移从抽象 \(c\) 具体化为一跳 D-格的 \(AD'\)，并证明在
声明 universe 内 source-complete。它没有证明所有 F 态都落入某个固定 \(D\) 的一跳菜单，
也没有把菜单 route 自动变成递降边；真正的全称缺口是跨 \(D\)/跨状态的菜单扩张与其
E1--E5/Type-II 回译。

## 聚焦复现

```bash
python3 reproductions/type_i_target_odd_d_lattice_affine_menu_completion.py --verify
```
