---
kind: claim
claim_id: type-I-fg-fourier-phase-owner-capacity-bridge
title: F/G Fourier q-primary 相位到 owner 紧链—容量松弛的类型安全桥
statement: 对固定层稳定子商后的 F/G 状态，q-primary Fourier 角色相位 gamma_i、需求高度 h_i 只有在 gamma_i 与算术目标残类 beta_h=-p*4^{-1} (mod q^h) 对齐，且有限 source map 给出唯一 owner s_i 满足 s_i=gamma_i (mod q^h) 时，才能进入 q-prefix owner 容量。G 态源差分上恒等的角色只给支撑分离，不产生 q 需求；F 态相位不对齐给 FOURIER_PHASE_OWNER_NONIDENTIFIED，候选表为空给 FOURIER_PHASE_NO_LOCAL_LIFT。对齐且 source-complete 时，owner 供给高度 e_i=v_q(p+4s_i) 继承紧链边界 v_q(s_i-s_a)=e_i 及缺口恒等式 (R_j-mu C_j)_+=((R_j-mu|O_j|)_+-mu(C_j-|O_j|))_+，从而把 F/G 对偶证书精确分派为紧 owner 逃逸、需 source-switch 的容量松弛或严格 q 进超载。该桥仍不声称相位 lift 或 E1--E5 递降对所有状态存在。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fg-fourier-to-type-II-role-demand-bridge
  - type-I-fourier-qprimary-phase-lift-capacity-dichotomy
  - type-II-qprefix-owner-escape-capacity-decomposition
  - type-II-qprefix-owner-height-source-closure
topics:
  - type-I
  - F-state
  - G-state
  - Fourier
  - q-primary
  - phase-lift
  - owner-map
  - q-prefix
  - capacity
  - source-switch
  - proof-program
sources:
  - claim: type-I-fg-fourier-to-type-II-role-demand-bridge
    role: F-G-role-to-q-demand
  - claim: type-I-fourier-qprimary-phase-lift-capacity-dichotomy
    role: Fourier-phase-and-local-lift
  - claim: type-II-qprefix-owner-escape-capacity-decomposition
    role: owner-boundary-and-capacity-split
  - claim: type-II-qprefix-owner-height-source-closure
    role: owner-source-completeness
  - reproduction: reproductions/type_i_fg_fourier_phase_owner_capacity_bridge.py
    role: aligned-tight-nonidentified-and-G-controls
visibility: public
last_checked: '2026-08-09'
---

# F/G Fourier q-primary 相位到 owner 紧链—容量松弛的类型安全桥

## 1. 输入角色与算术残类

固定一个已经完成稳定子约化的 F/G 状态。设 \(q\) 为奇素数，F 型规范角色的
q-primary 分量有高度 \(h_i\ge1\)，并在其关系格坐标中给出相位中心

\[
  \gamma_i\in\mathbb Z/q^{h_i}\mathbb Z.
\]

同一核心素数 \(p\) 的 q-prefix 算术残类是

\[
  \beta_h(p)\equiv-p4^{-1}\pmod {q^h}.
\tag{1}
\]

称一个状态拥有**对齐 owner lift**，如果存在有限 source-map 中唯一的 owner 移位
\(s_i\)，满足

\[
  s_i\equiv\gamma_i\pmod {q^{h_i}},
  \qquad
  \gamma_i\equiv\beta_{h_i}(p)\pmod {q^{h_i}}.
\tag{2}
\]

第二个同余不可省略。由 (2)，才有

\[
  q^{h_i}\mid p+4s_i.
\tag{3}
\]

仅有 Fourier 角色阶、相位分子或商群同构，不会推出第二个同余；相位能提升到某个
整数标签，也不等于该标签是 \(p+4s\) 的 q-prefix owner。

若 \(\gamma_i\equiv\beta_{h_i}(p)\) 但有限 owner 标签表中没有满足
\(s_i\equiv\gamma_i\pmod{q^{h_i}}\) 的 \(s_i\)，输出
'FOURIER_PHASE_NO_LOCAL_LIFT'。若标签能满足第一个同余却不满足第二个同余，输出
'FOURIER_PHASE_OWNER_NONIDENTIFIED'；这两种回执都不得进入 q 进容量账本。

## 2. F/G 类型分派

令 \(\Delta_Q\) 为目标指数纤维源支撑的差分群。

### G 型

若角色在 \(\Delta_Q\) 上恒等、但在目标支撑陪集上非恒等，则它是
'G_SUPPORT_SEPARATION'。此时源关系 q 需求定义为零；即使角色阶含有奇素数或
二幂，也不能把它收费为 Type II q 层。

### F 型未对齐

若角色在 \(\Delta_Q\) 上非恒等，它至少产生已有角色—源秩桥所需的
'SOURCE_RANK_DEMAND(q)'。但在进入 q-prefix owner 之前必须检查 (2)：

* 相位中心不等于 \(\beta_{h_i}(p)\)：'FOURIER_PHASE_OWNER_NONIDENTIFIED'；
* 对齐但有限标签表没有 owner：'FOURIER_PHASE_NO_LOCAL_LIFT'；
* 标签表未被证明有限完备：'FOURIER_PHASE_SOURCE_UNCLOSED'。

这些都是对偶到算术的接口障碍，而不是 q 容量超载，也不是递降边。

### F 型对齐且 source-complete

若所有参与请求都有 (2)，owner 标签两两可区分，每个真实源列恰有一个 owner，且
所有 source-switch、SNF、CRT、范围和整数门均已通过，则形成 source-complete owner
map。令

\[
  e_i=v_q(p+4s_i),
  \qquad O_j=\{i:e_i\ge j\},
  \qquad
  C_j=\max_{a\bmod q^j}\#\{s_i:s_i\equiv a\pmod {q^j}\}.
\tag{4}
\]

需求 \(R_j\) 由独立 F 型 q-primary 角色方向在第 \(j\) 层的请求数给出；每个槽
允许重复度为 \(\mu\)。此时可直接调用 q-prefix owner 逃逸分解：

\[
  \Delta_j=C_j-|O_j|\ge0,
\tag{5}
\]

\[
  (R_j-\mu C_j)_+
  =\bigl((R_j-\mu|O_j|)_+-\mu\Delta_j\bigr)_+.
\tag{6}
\]

若 \(i\notin O_j\)、\(e_i=k<j\)，且 \(O_j\ne\varnothing\)，则任取 \(a\in O_j\) 有

\[
  \boxed{v_q(s_i-s_a)=k.}
\tag{7}
\]

所以 Fourier 角色进入 owner map 后，不再只有一个抽象“相位未匹配”标签，而有
一个可复核的 q-adic 边界和三类容量回执：

1. \(\Delta_j=0\)：'FOURIER_OWNER_TIGHT_ESCAPE'，没有容量松弛；若
   \(R_j>\mu|O_j|\)，同时是严格 'Q_ADIC_LAYER_CAPACITY_DEFICIT'；
2. \(\Delta_j>0\)：'FOURIER_OWNER_SLACK_SOURCE_SWITCH'，最多
   \(\mu\Delta_j\) 个 owner 缺口可尝试由非 owner 标签补足，每条边必须重新通过
   source-switch/SNF/整数提升；
3. \(R_j>\mu C_j\)：无论 source-switch 如何重排，该层均有严格 q 进超载，输出
   'Q_ADIC_LAYER_CAPACITY_DEFICIT'。

式 (6) 不把容量松弛误写成已经存在的 alternate edge；它只给出最多可尝试的数量。

## 3. 证明

由 \(q\nmid4\)，算术 q-prefix 条件等价于唯一残类
\(s\equiv-p4^{-1}\pmod {q^j}\)，所以 (2) 推出 (3)，并且

\[
  O_j=\{i:s_i\equiv\beta_j(p)\pmod {q^j}\}.
\]

这正是 owner 高度闭合引理的输入。若 \(i\notin O_j\)、\(e_i=k<j\) 而 \(a\in O_j\)，
写 \(p+4s_i=q^ku_i\)、\(p+4s_a=q^{e_a}u_a\)，其中 \(q\nmid u_iu_a\)；相减后

\[
  4(s_i-s_a)=q^k(q^{e_a-k}u_a-u_i),
\]

括号模 \(q\) 为单位，故得 (7)。容量恒等式 (6) 是
\(C_j=|O_j|+\Delta_j\) 代入正部后的三段恒等式。G 型和 F 型未对齐分派则分别由
角色在源差分群上的恒等/非恒等定义以及对齐条件 (2) 直接得到。证毕。

## 4. 聚焦控制

取 \(p=433,q=7\)。算术目标残类满足

\[
  \beta_1=2\pmod7,
  \qquad \beta_2=2\pmod{49}.
\]

两个对齐 owner 为

\[
  s_{16}=16,\quad e_{16}=1,
  \qquad
  s_{100}=100,\quad e_{100}=2.
\]

它们的 Fourier 相位中心可取
\(\gamma_{16}=2\pmod7\)、\(\gamma_{100}=2\pmod{49}\)，均通过 (2)。第 2 层
只有 100，\(C_2=|O_2|=1\)；若两个独立 Fourier 方向都要求第 2 层，则

\[
  R_2=2,\quad \mu=1,
  \quad (R_2-\mu|O_2|,\mu\Delta_2,(R_2-\mu C_2)_+)=(1,0,1).
\]

16 相对 100 的边界是

\[
  v_7(100-16)=1.
\]

这是一条对齐 Fourier owner 的紧链逃逸，而不是把角色阶直接当成高度。

对照取 \(q=3,h=1,\gamma=1\) 而 \(p=433\) 时
\(\beta_1(433)=2\pmod3\)，相位与算术残类不对齐；即使标签表含有 \(s=1\)，也只能
输出 'FOURIER_PHASE_OWNER_NONIDENTIFIED'，不能收费 q=3 容量。若角色在源差分群上
恒等且目标陪集相位非恒，则输出 G 型支撑分离，q 需求仍为零。

## 5. 统一选择器中的位置

这条桥把三条已有对象接成一个严格的 typed pipeline：

\[
  \text{F/G Fourier role}
  \to
  \text{q-primary phase}
  \to
  \text{arithmetic alignment (2)}
  \to
  \text{owner tight/slack}
  \to
  \text{q-capacity / source-switch / Fourier relay}.
\]

其中任何一步失败都保留较窄的回执，不可用后一步的容量或角色幅度补齐前一步的
算术缺口。对齐且紧链的边界可继续进入广义 \(2^j\)、有限 Fourier 或稳定子 relay；
松弛分支必须先补足实际 alternate-owner 边；G 型直接留在支撑对偶分支。

## 研究边界

本桥证明了 F/G q-primary 相位与 Type II owner 容量之间的必要对齐门和精确缺口
分解，但没有证明每个 F 型角色都有对齐 owner lift，也没有证明松弛分支存在合法
source-switch，更没有把紧链 Fourier 逃逸自动升级为 E1--E5 递降。全称闭合仍要求
一个 source-complete 的有限 owner/source map，或把上述 no-lift、非对齐和紧链回执
分别接入已有 Type I 终端、Type II 商 relay 与广义 \(2^j\) 终端。

## 聚焦复现

~~~bash
python3 reproductions/type_i_fg_fourier_phase_owner_capacity_bridge.py --verify
~~~
