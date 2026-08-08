---
kind: claim
claim_id: type-I-linear-escape-strict-layer-mod-four-supply-obstruction
title: 线性 escape 严格降层的模 4 因子供给障碍
statement: 固定核心素数 p、标准 Type II D-格层 d 及其严格低层目标 f=(d',A), d'<d。令 Q_{d,f} 为所有同时整除某个来源 N_{d,a}=p+4da 与目标 N_f=p+4Ad' 的奇素数。任何保留该来源的标准 D-格 source-switch 因子 h 的素因子都在 Q_{d,f} 中；故若 Q_{d,f} 的所有素数均为 1 (mod 4)，则 h=1 (mod 4)，不可能满足严格 source-switch 所需的 h=-1 (mod 4d')。因此该目标没有严格可提升的 D-格边；若层 d 的全部严格低层目标都满足这一条件，则声明的除子分层 policy 没有严格离开 d 的边。在 p=57399241、R=59、d=41 的 C2 block-escape 控制中，唯一低层 f=(1,1) 的供给集为 {5}，从而没有 41->1 的严格边；固定 d=41 的全部 canonical source 素因子又是模 59 二次剩余，不能支付该 C2 escape。该结论只排除声明的标准 D-格来源 universe，且该素数已有直接 Type I terminal。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-linear-escape-canonical-d-lattice-source-menu
  - type-I-linear-escape-divisor-stratified-recursive-source-closure
  - type-II-same-modulus-source-switch-crt-criterion
topics:
  - type-I
  - linear-source
  - escape
  - Type-II
  - source-switch
  - divisor-lattice
  - strict-descent
  - mod-four
  - arithmetic-obstruction
  - proof-program
sources:
  - reproduction: reproductions/type_i_linear_escape_strict_layer_mod4_supply_obstruction.py
    role: p=57399241, d=41 strict-layer obstruction and C2 escape control
visibility: public
last_checked: '2026-08-08'
---

# 线性 escape 严格降层的模 4 因子供给障碍

## 1. 严格层边的可用因子支撑

固定核心素数 (p)，当前标准 Type II 层 (d)，并令

\[
\mathcal A_d(p)=
\{a:a\mid d,\ d/a\text{ 平方自由},\ 4ad<p\}.
\]

取严格较低的目标纤维

\[
f=(d',A),\qquad d'\mid d,\quad d'<d,\quad
A\mid d',\quad d'/A\text{ 平方自由},\quad4Ad'<p,
\]

并写

\[
N_{d,a}=p+4da,\qquad N_f=p+4Ad'.
\]

定义该层到该纤维的 **模 4 供给集**

\[
\mathscr Q_{d,f}=
\left\{q:\ q\text{ 为奇素数，存在 }a\in\mathcal A_d(p)
\text{ 使 }q\mid\gcd(N_{d,a},N_f)\right\}. \tag{1}
\]

这是 canonical D-格菜单中所有可用于 (f) 的原子来源的素数支撑；它不把不同
来源的同一 (q) 重复计为多个块。若需要高度，可进一步由 shared-(q) ledger 截断，
但下述障碍只需支撑信息。

按标准除子分层 source-switch 合同，一个从 (d) 到 (f) 的已接受严格边必须有
一个因子积 (h>1)，其原子块分别来自某些 (N_{d,a_i})，同时满足

\[
h\mid N_f,
\qquad h\equiv-1\pmod {4d'}, \tag{2}
\]

以及 CRT、标记、范围与 E1--E5 的其余门。这里 (2) 只是严格边的必要条件，已经足够
给出下面的剪枝。

## 2. 模 4 供给障碍

**引理。** 若

\[
\mathscr Q_{d,f}\subseteq\{q:q\equiv1\pmod4\}, \tag{3}
\]

则在声明的标准 D-格 source-switch universe 中，不存在从 (d) 到 (f) 的严格层边。

**证明。** 设 (h) 是任意这样的 source-switch 因子，并取 (q\mid h)。因 (h)
由带来源原子块组成，存在某个 (a\in\mathcal A_d(p)) 使 (q\mid N_{d,a})；又
(h\mid N_f)，故 (q\in\mathscr Q_{d,f})。两个 (N) 都是奇数，所以 (h) 的每个
素因子都是奇素数。由 (3)，每个 (q\mid h) 都为 (1\pmod4)，从而

\[
h\equiv1\pmod4.
\]

但 (2) 蕴含 (h\equiv-1\equiv3\pmod4)，矛盾。canonical D-格菜单对该声明的
一跳 source universe 完备，因此不存在未枚举的标准原子来源能绕开该矛盾。证毕。

**推论。** 若层 (d) 的每个严格低层目标 (f=(d',A)) 都满足 (3)，则该
除子分层 policy 没有 (d' < d) 的已接受边。于是其 (Omega(d)) 层势不能下降；
它只能在同层终端、同层非递归回执，或 universe 外的 raw/F/G/外部来源之间分派。

这个结论不是“所有 Type II 因子都不存在”。它只在已声明、source-complete 的
标准 D-格来源范围内排除严格降层；一个直接 Type II 命中仍应按 terminal-first
规则优先输出。

## 3. (p=57{,}399{,}241) 的 (d=41) C2 控制

取已有线性 block-escape 状态

\[
p=57{,}399{,}241,\qquad R=59,\qquad d=41.
\]

因为 (41) 是素数，唯一的严格低层目标是 (f=(1,1))。当前层的标准来源与低层
目标整数为

\[
\begin{aligned}
N_{41,1}&=57{,}399{,}405=3\cdot5\cdot7\cdot546661,\\
N_{41,41}&=57{,}405{,}965=5\cdot2861\cdot4013,\\
N_f&=p+4=57{,}399{,}245=5\cdot11479849.
\end{aligned} \tag{4}
\]

精确公因子为

\[
\gcd(N_{41,1},N_f)=\gcd(N_{41,41},N_f)=5. \tag{5}
\]

故

\[
\mathscr Q_{41,(1,1)}=\{5\},\qquad5\equiv1\pmod4. \tag{6}
\]

引理排除所有 (41\to1) 的严格标准 D-格 source-switch。由于 (41) 的除子只有
(1,41)，这个 policy 没有任何严格离开 (d=41) 的递归边。特别地，较低层的
非剩余因子 (11479849\equiv42\pmod{59}) 不能被误读为已经可达的下一层 source。

该状态的两块奇部满足

\[
U^\circ=15,\qquad
V^\circ=2693\cdot20959,
\qquad |\langle15\rangle|=29\subset\mathbb F_{59}^{\times}. \tag{7}
\]

其中 (2693\equiv38\pmod{59}) 是二次非剩余，给出相对两块模型的 (C_2) escape。
另一方面，(4) 中固定 (d=41) 的所有素因子

\[
3,5,7,546661,2861,4013
\]

均为模 (59) 二次剩余。因此任意固定层 canonical source 因子积在

\[
\mathbb F_{59}^{\times}/\langle15\rangle\simeq C_2
\]

中的像均为平凡元，不能支付这一个 escaped rank direction。结合 (6)，得到该
声明的递归 D-格 universe 的精确回执

\[
\boxed{\mathrm{D41\_C2\_RECURSIVE\_SOURCE\_OBSTRUCTED}.} \tag{8}
\]

这不是原猜想的反例：该素数已有 direct Type I terminal，譬如

\[
\frac4{57399241}
=\frac1{14349815}
+\frac1{43350973295260}
+\frac1{11446239633292287329236}. \tag{9}
\]

所以 (8) 是 terminal-preempted 的 source-map 负控制。它的作用是阻止把一个
未到达的低层非剩余因子虚报为 C2 demand 的可提升支付来源。

## 4. 边界

该障碍不覆盖 raw 因子、外部 F/G alternate、不同初始 (D)、非标准参数变换，
也不从 C2 商角色本身构造全局 G 证书。若 (3) 失败，结论也不会反向保证存在严格边：
仍需通过完整的 CRT、同纤维、SNF、范围、标记和 E1--E5 检查。

窄复现：

~~~bash
python3 reproductions/type_i_linear_escape_strict_layer_mod4_supply_obstruction.py --verify
~~~
