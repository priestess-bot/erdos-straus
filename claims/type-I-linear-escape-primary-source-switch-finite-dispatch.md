---
kind: claim
claim_id: type-I-linear-escape-primary-source-switch-finite-dispatch
title: 线性 escaped primary source-switch 的有限条件分派
statement: 固定核心素数 p、原始 D 与有限带标签 escaped source 菜单。对每个候选纤维 s=AD'，重复 q 的可用高度必须重新计算为 d_q(s)=min(v_q(p+4s),sum_i min(e_i,v_q(s-Da_i)))；只可用一个 q 幂块 q^{J_q}，其中 J_q<=d_q(s)。算术 CRT 只要求 q 为奇数，单位群/SNF relay 另要求 q 不整除 4D'。由有效块组成的 h 可有限地检查除子格直接正规形、同纤维容量、raw Type II 回退及有限群映射；E1--E5 必须作为额外的状态见证，而不能从 CRT/SNF 自动推出。因此该表对已声明的 source universe 给出有限、可回放的条件分派；它不单独证明全局 source-complete，也不把有限表为空升级为全局算术障碍。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-source-fiber-shared-q-ledger
  - type-II-q-layer-prefix-kneser-price-certificate
  - type-II-q-prefix-source-crt-fiber-concentration
  - type-II-hall-fiber-arithmetic-closure-trichotomy
  - type-II-arithmetic-lift-raw-factor-fallback
  - type-II-annihilator-congruence-fiber-lift-criterion
  - type-I-linear-escape-primary-hole-capacity
  - type-I-linear-escape-primary-digit-capacity-terminal
topics:
- type-I
- linear-source
- escape
- source-switch
- finite-dispatch
- primary
- q-prefix
- CRT
- SNF
- E1-E5
- Type-II
- strict-relay
- raw-fallback
- source-unclosed
- proof-program
sources:
  - claim: type-II-source-fiber-shared-q-ledger
    role: candidate-specific-shared-q-height
  - claim: type-II-hall-fiber-arithmetic-closure-trichotomy
    role: same-lower-raw-arithmetic-closure
  - claim: type-II-annihilator-congruence-fiber-lift-criterion
    role: finite-target-map-and-lift-gates
  - reproduction: reproductions/type_i_linear_escape_primary_source_switch_fixture.py
    role: constant-size shared-q and raw-fallback regression fixture
visibility: public
last_checked: '2026-08-05'
---

# 线性 escaped primary source-switch 的有限条件分派

## 1. 有限来源菜单与候选高度

固定核心素数 \(p\)、原始参数 \(D\)，以及一个有限的带标签来源菜单

\[
\mathcal E=\{\sigma_i=(a_i,q_i,e_i,\lambda_i)\}_{i\in I_0},
\qquad
q_i^{e_i}\mid p+4Da_i,
\qquad
q_i\text{ 为奇素数}.
\tag{1}
\]

令 \(b_i=Da_i\)。菜单本身只声明它覆盖某个明确的 source universe
\(\mathfrak U\)；除非另有覆盖定理，\(\mathfrak U\) 不能被静默扩充为所有
alternate、raw 或下一递归层来源。

一个前缀 profile 选择有限子集 \(I\subseteq I_0\)，并为每个参与行保存来源层数
\(m_i\in\{1,\ldots,e_i\}\) 和标签分配 \(\Lambda\in\mathscr L_I\)，其中
\(\mathscr L_I\) 是由该固定菜单的有限标签词表预先声明的有限分配集。对每个出现的
素数 \(q\) 写

\[
I_q=\{i\in I:q_i=q\},
\qquad
J_q=\sum_{i\in I_q}m_i,
\qquad
h_{\mathfrak J}=\prod_{q}q^{J_q}.
\tag{2}
\]

这里的 \(J_q\) 只是请求的合并高度，**不是**把 \(q\) 的来源行数自动相加后已经
可用的候选高度。

现在固定一个 admissible 参数纤维

\[
f=(D',A),\qquad
D'\mid D,\quad A\mid D',\quad D'/A\text{ 平方自由},\quad
4AD'<p,
\qquad s_f=AD'.
\tag{3}
\]

对该候选纤维，重复 \(q\) 的真实来源账本为

\[
\text{约定 }v_q(0)=+\infty,
\]
\[
\ell_i(f)=\min\{e_i,v_q(s_f-b_i)\}\quad(i\in I_q),
\]
\[
d_f(q)=
\min\left\{
v_q(p+4s_f),\
\sum_{i\in I_q}\ell_i(f)
\right\}.
\tag{4}
\]

profile 在 \(f\) 上可实现，当且仅当可以保留其标签分配且

\[
m_i\le \ell_i(f)\quad(i\in I),
\qquad
J_q\le v_q(p+4s_f)\quad(q\in q(I)).
\tag{5}
\]

逐标签门 \(m_i\le\ell_i(f)\) 与总高度门必须同时保存。前者已经给出
\(J_q=\sum_{i\in I_q}m_i\le\sum_{i\in I_q}\ell_i(f)\)，所以在逐标签门通过后，
\[
J_q\le v_q(p+4s_f)
\quad\Longleftrightarrow\quad
J_q\le d_f(q).
\]
二者通过时，合并后的连续 q 前缀有效。因此

\[
q^{J_q}\mid p+4s_f
\quad\text{且}\quad
h_{\mathfrak J}\mid p+4s_f.
\tag{6}
\]

这正是重复 q 共同账本的候选特化。每个 \(q\) 只对应一个整数幂块

\[
B_{f,q}=\{1,q,\ldots,q^{J_q}\};
\tag{7}
\]

不得把同一 \(q\) 的多条来源行当成多个独立 Kneser 块。

## 2. 算术 CRT 门与单位群门必须分开

对任一奇素数 \(q\)，由

\[
(p+4s_f)-(p+4b_i)=4(s_f-b_i)
\]

得到精确等价

\[
q^{m_i}\mid p+4s_f
\quad\Longleftrightarrow\quad
s_f\equiv b_i\pmod {q^{m_i}}.
\tag{8}
\]

这里仅使用 \(q\nmid4\)，并不要求 \(q\nmid D\) 或 \(q\nmid D'\)。同一 \(q\)
的多条条件按广义 CRT 检查；不相容时记录

\[
\mathrm{SOURCE\_CRT\_INCONSISTENT}
=(i,i',q,m_i,m_{i'},b_i,b_{i'}).
\tag{9}
\]

另一方面，只有

\[
q\nmid4D'
\tag{10}
\]

时，\(q\bmod4D'\) 才能进入 \(U(4D')\)、Kneser 商或 SNF/annihilator relay。
若 (8) 通过但 (10) 失败，这一行仍是有效的算术整除行；它只能标记
\(\mathrm{SOURCE\_UNIT\_GROUP\_NONUNIT}\)，不能错误地当作 CRT 消元失败。

## 3. 有限候选表

对有限 profile、有限 \((D',A)\) 和 (5) 的每个有效元组，依次执行下列门。

### 3.1 直接 Type II 正规形

若

\[
h_{\mathfrak J}>1,
\qquad
h_{\mathfrak J}\equiv-1\pmod {4D'},
\tag{11}
\]

令

\[
K'=\frac{h_{\mathfrak J}+1}{4D'},
\qquad
B'=\frac{K'p+A}{h_{\mathfrak J}}.
\tag{12}
\]

由 (6) 有

\[
K'(p+4AD')=(K'p+A)+Ah_{\mathfrak J},
\tag{13}
\]

所以 \(B'\in\mathbb N\)。又 \(4AD'<p\) 给出 \(B'>A\)。因此 (11) 直接输出
\(\mathrm{PRIMARY\_BLOCK\_DIRECT\_TYPE\_II}\)。

若还要将该行登记为“保持原 \(D\) 来源”的 source-switch/relay，必须另外有

\[
h_{\mathfrak J}\equiv-1\pmod {4D}.
\tag{14}
\]

(11) 足以证明新的 Type II 证书；(14) 才把它接回旧模数的带来源合同。

### 3.2 raw Type II 回退

不能因为所有 admissible \((D',A)\) 候选为空就宣布算术失败。对菜单生成的每个

\[
h_{\mathfrak J}>1,\qquad h_{\mathfrak J}\equiv-1\pmod4,
\tag{15}
\]

还要枚举有限集

\[
\mathscr R_{\rm raw}(h_{\mathfrak J};p)=
\left\{(A_0,C_0,K_0):
\begin{array}{l}
A_0,C_0,K_0\in\mathbb N,\\
A_0C_0K_0=(h_{\mathfrak J}+1)/4,\\
h_{\mathfrak J}\mid K_0p+A_0,\\
A_0\le(K_0p+A_0)/h_{\mathfrak J}
\end{array}
\right\}.
\tag{16}
\]

其任何元素直接给出 Type II 证书。该终端不要求保留原来源标签，因而是
source-preserving 除子格分派的严格扩展。

### 3.3 同纤维 primary 容量

只有所有参与 \(q\) 满足 (10) 时，才可把 (7) 送入同一 \(U(4D')\) 纤维的
Kneser/primary 容量账本。相同 \(q\) 只以一个 \(B_{f,q}\) 计价；若多个请求需要
同一方向，还要提供 q-prefix Hall 见证。

在 \(\ell\)-初等独立商中，调用 primary 幂块—目标缺口容量门；在同一循环
\(\ell^a\) 因子中，调用加权 digit 容量门。命中只在整数回译、目标状态和所需
E1--E5 均已给出时升级为 Type II；否则分别保留

\[
\mathrm{PRIMARY\_BLOCK\_CAPACITY\_DEFICIT},
\quad
\mathrm{HOLE\_LOCKED},
\quad\text{或}\quad
\mathrm{FIBER\_TARGET\_FILLED\_BUT\_LIFT\_OBSTRUCTED}.
\tag{17}
\]

### 3.4 有限群 relay 与 E1--E5

若该行需要 annihilator/商 relay，有限群部分的数据必须明确包含

\[
\eta:U(4D')\twoheadrightarrow J,\qquad
\eta(-1)=t_J,\qquad
\eta(q^{J_q}\bmod4D')=\mu_q
\quad(q\in q(I)),
\tag{18}
\]

其中 \(\mu_q\) 是与 \(\Lambda\) 绑定的合并来源标签像。满射、核、目标像和联合标签
由有限阿贝尔群 SNF 检查。

但是 \((D',A,\eta)\) 不包含后继状态、全域解提升或严格势下降。因此只有在另外给出
目标状态和 E1--E5 见证后，才输出
\(\mathrm{PRIMARY\_BLOCK\_STRICT\_RELAY}\)。有限群/算术实现但缺少这些见证时，只能
记录 \(\mathrm{RELAY\_ONLY}\) 或 \(\mathrm{LIFT\_OBSTRUCTED}\)。

## 4. 有限性与正确的闭合量词

对固定的有限 \(\mathcal E\) 及其预先声明的有限标签分配集 \(\mathscr L_I\)，profile、
\(\Lambda\)、\((D',A)\)、每个有限单位群满射及每个 raw 因子三元组均有限。因此本卡
给出一个有限、可回放的候选表。

若 \(\mathcal E\) 已被证明覆盖声明的 universe \(\mathfrak U\)，则任一
\(\mathfrak U\)-保持的 source-switch 至少落入该表中的一个 profile；不声称唯一，
因为同一高度可能有不同的标签层分配。表为空时可输出
\(\mathrm{D\_LATTICE\_RAW\_MENU\_EMPTY}\) 或相应的 CRT、unit-group、range、
SNF、容量和 raw 空集账本。它只排除 \(\mathfrak U\) 中已经列明的有限分派，
绝不等价于“核心素数没有其它证书”。

若没有 source-completeness 定理，则保留
\(\mathrm{PRIMARY\_BLOCK\_SOURCE\_UNCLOSED}\)；它优先于任何全局化的算术障碍，
但不否定表中已经直接验证的 Type II 证书。

## 5. 两个边界样例

### 重复 q 高度不能相加

取

\[
p=215617,\quad D=1247=29\cdot43,\quad D'=43,\quad A=1,\quad q=7.
\]

三条来源行 \((a,q,e)=(1,7,1),(29,7,1),(43,7,1)\) 都满足各自的一层来源同余，
但

\[
v_7(p+4AD')=v_7(215789)=1.
\]

故 (4) 给出 \(d_f(7)=1\)，拒绝 \(J_7=3\)。若错误取
\(h=7^3=343\)，虽有 \(h\equiv-1\pmod{172}\)，却有

\[
\frac{((h+1)/(4D'))p+A}{h}\notin\mathbb N.
\]

这说明逐行 CRT 不能代替候选的实际 shared-q 高度门。

### 除子格为空仍可 raw 命中

对

\[
p=73,\qquad D_0=1,\qquad a_0=8,\qquad h=15,
\]

原除子格没有候选，但

\[
(A_0,C_0,K_0)=(2,2,1),
\qquad
B=(73+2)/15=5
\]

属于 (16)。所以正确输出是直接 Type II，而不是除子格算术障碍。

上述两个边界例由常数规模夹具逐项复现，见
[primary source-switch fixture](../reproductions/type_i_linear_escape_primary_source_switch_fixture.py)。

## 6. 研究边界

本卡关闭了三个此前混淆的接口：重复 q 的候选高度、算术 CRT 与单位群的差别，以及
raw 终端的必经回退。它仍没有证明所有 escaped source 都属于一个有限菜单，也没有
从 primary 容量或低模数商自动产生 E4/E5。下一步需要分别证明特定 source universe
的菜单完备性，并为可能的 relay 构造带全域提升的严格势下降。
