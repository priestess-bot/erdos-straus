---
kind: claim
claim_id: type-i-linear-escape-target-supply-spectrum-strict-adapter
title: 目标纤维 source-supply spectrum 的严格降层 adapter 判据
statement: 给定核心素数 p、当前标准 D 层的声明来源 profile 与严格低层目标 f=(d',A)，令每个奇素数 q 的共同可用高度为 eta_q=max_a min(v_q(p+4Da),v_q(p+4Ad'))，并令 H_f 为这些 q 进高度的全部有限乘积。则存在保留来源标签且命中 f 的算术严格 adapter，当且仅当 H_f 中有 h>1 满足 h=-1 (mod 4d')；见证 h 直接给出 K'=(h+1)/(4d')、B'=(K'p+A)/h 的 Type II 证书。若所有 q 都为 1 (mod 4)，该 spectrum 为空于 -1 残类，恢复模 4 供给障碍；若严格 spectrum 未命中，则对 Hall 因子按 raw 有限集回退，raw 非空给出直接 Type II，raw 也为空才记录 adapter-empty。该判据只对声明的 source profile 有效，不能绕过 E1--E5、标记解提升或全局良基势。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-same-modulus-source-switch-crt-criterion
  - type-II-arithmetic-lift-raw-factor-fallback
  - type-I-linear-escape-strict-layer-mod-four-supply-obstruction
topics:
  - type-I
  - linear-source
  - target-fiber
  - source-spectrum
  - q-adic-height
  - strict-descent
  - Type-II
  - raw-fallback
  - finite-obstruction
  - proof-program
sources:
  - claim: type-II-same-modulus-source-switch-crt-criterion
    role: lower-layer-CRT-and-Type-II-construction
  - claim: type-II-arithmetic-lift-raw-factor-fallback
    role: raw-fallback-dispatch
  - claim: type-I-linear-escape-strict-layer-mod-four-supply-obstruction
    role: mod-four-support-corollary
  - reproduction: reproductions/type_i_linear_escape_target_supply_spectrum_strict_adapter.py
    role: exact-spectrum-controls-at-p5113-p57399241-and-p73
visibility: public
last_checked: '2026-08-09'
---

# 目标纤维 source-supply spectrum 的严格降层 adapter 判据

## 1. 目标纤维与共同高度

固定核心素数 \(p\)、当前 Type II 层 \(D\)，以及一个声明为 source-complete
的来源 profile \(\mathcal S\subseteq\mathcal A_D(p)\)，其中

\[
\mathcal A_D(p)=\{a:\ a\mid D, D/a\text{ 平方自由},\ 4aD<p\}.
\]

这里的 source-complete 是相对于所声明的 profile 而言：若只研究 active source
rows，就必须把它们全部列入 \(\mathcal S\)，不能把未列出的来源当作已排除。

取严格低层目标

\[
f=(d',A),\qquad d'\mid D,\quad d'<D,\quad A\mid d',
\quad d'/A\text{ 平方自由},\quad 4Ad'<p,
\]

并记

\[
N_{D,a}=p+4Da,\qquad N_f=p+4Ad'.
\]

对每个奇素数 \(q\nmid4D\)，定义当前来源对目标纤维可支付的最大共同高度

\[
\eta_q(f;\mathcal S)
=\max_{a\in\mathcal S}
\min\!\left(v_q(N_{D,a}),v_q(N_f)\right).
\tag{1}
\]

只有 \(\eta_q>0\) 的 \(q\) 进入账本。令

\[
E_f=\prod_{\eta_q>0}q^{\eta_q},
\qquad
\mathscr H_f=\{h:h\mid E_f\}.
\tag{2}
\]

这是一个有限集合，且

\[
|\mathscr H_f|=\prod_{\eta_q>0}(\eta_q+1).
\tag{3}
\]

同一 \(q\) 在多个来源行中出现时只保留一个 \(q\)-进高度；达到
\(\eta_q\) 的来源行作为该 \(q\) 的 owner 标签保存。这正是 shared-\(q\)
ledger 的目标纤维版本。

## 2. owner 谱的精确性

对任意 \(h\in\mathscr H_f\)，写

\[
h=\prod_{\eta_q>0}q^{u_q},\qquad0\le u_q\le\eta_q.
\tag{4}
\]

由 (1) 的最大值定义，对每个 \(u_q>0\) 都能选择一个 owner
\(a(q,u_q)\in\mathcal S\)，使

\[
q^{u_q}\mid N_{D,a(q,u_q)},\qquad q^{u_q}\mid N_f.
\tag{5}
\]

不同 \(q\) 的块两两互素，因而 (4)--(5) 给出一个带来源标签的
source-preserving factorization。反过来，任何由来源 prime-power blocks
组成、且同时整除 \(N_f\) 的 \(h\)，其每个 \(q\)-进指数都不超过 (1)，所以
\(h\in\mathscr H_f\)。

因此有精确等价

\[
\boxed{
h\in\mathscr H_f
\iff
\begin{array}{c}
h>0\text{ 的每个素幂块同时整除 }N_f\text{ 与某个 }N_{D,a},\\
\text{且 owner 标签属于 }\mathcal S.
\end{array}}
\tag{6}
\]

这一步把“某个来源因子可能可用”的支撑近似提升成完整的有限 factor
spectrum；它不把不同 \(q\) 的高度重复收费。

## 3. 严格 adapter 的必要且充分判据

定义目标纤维的严格残数谱

\[
\Sigma_{D\to f}
=\{h\bmod 4d':h\in\mathscr H_f,\ h>1\}.
\tag{7}
\]

则在声明的 source profile 内，存在命中 \(f\) 的目标实现型算术 adapter 当且仅当

\[
\boxed{-1\bmod 4d'\in\Sigma_{D\to f}.}
\tag{8}
\]

确实，若 \(h\) 命中 (8)，则 \(h\mid N_f\)，并令

\[
K'=\frac{h+1}{4d'},\qquad
B'=\frac{K'p+A}{h},\qquad c'=\frac{d'}A.
\tag{9}
\]

由 \(h\mid p+4Ad'\) 和 \(4d'K'=h+1\)，有

\[
K'(p+4Ad')=K'p+A(h+1),
\]

故 \(h\mid K'p+A\)。此外

\[
B'-A=\frac{K'(p-4Ad')+2A}{h}>0.
\tag{10}
\]

所以

\[
h=4Ac'K'-1,\qquad h\mid K'p+A
\]

给出 \((A,c',K')\) 的合法 Type II 正规形，且 (6) 保留了来源 owner 标签。

反过来，任意保留这些来源标签且命中 \(f\) 的目标实现型 source-switch 因子 \(h\)
同时整除 \(N_f\)，由 (6) 得 \(h\in\mathscr H_f\)；严格 Type II 条件又要求
\(h\equiv-1\pmod{4d'}\)，故 (8) 必成立。证毕。

注意：由 (9) 构造出来的对象本身已经是 \(4/p\) 的直接 Type II 证书。只有
当研究策略需要把它作为从旧层 \(D\) 出发的递归状态边时，还必须增加旧层合同

\[
h\equiv-1\pmod{4D},
\tag{9a}
\]

并检查标记解的全域提升、E1--E5 和严格下降势。由于 \(d'\mid D\)，(9a)
自动蕴含 (8) 的模 4 条件；但 (8) 本身不蕴含 (9a)。因此 arithmetic adapter
和 verified recursive edge 是两个不同的 typed 状态。

## 4. 模 4 障碍与精确谱缺口

若所有有 \(\eta_q>0\) 的素数满足

\[
q\equiv1\pmod4,
\tag{11}
\]

则每个 \(h\in\mathscr H_f\) 都满足 \(h\equiv1\pmod4\)，从而
\(-1\equiv3\pmod4\) 不可能属于 (7)。这恢复并严格定位了已有的模 4 供给障碍。

比支撑障碍更强的是：即使供给中出现 \(q\equiv3\pmod4\)，也必须实际计算
\(\Sigma_{D\to f}\)。例如某个 \(3\pmod4\) 素数只能以偶数高度出现时，它在
\(\mathscr H_f\) 中的贡献仍可能全部落在 \(1\pmod4\)。因此

\[
-1\notin\Sigma_{D\to f}
\tag{12}
\]

是一个比“所有供给素数为 \(1\pmod4\)”更精确的、有限可复核的严格 adapter
负证书；它要求保留每个 \(q\)-进高度和 owner，而不是只保存素数支撑。

## 5. raw 回退的规范分派

设 \(\mathscr H_{\mathrm{Hall}}\) 是当前来源匹配产生的有限 Hall 因子集合。
对其中满足 \(h\equiv-1\pmod4\) 的每个 \(h\)，调用

\[
\mathscr R_{\mathrm{raw}}(h;p)
=
\left\{(A_0,C_0,K):
\begin{array}{l}
A_0C_0K=(h+1)/4,\\
h\mid Kp+A_0,\quad
A_0\le(Kp+A_0)/h
\end{array}\right\}.
\tag{13}
\]

在 terminal-first 规则下，针对一个目标纤维的算术分派为：

1. (8) 命中：记录 STRICT_ARITHMETIC_ADAPTER；其 (9) 同时是直接 Type II
   证书。只有同时通过 (9a)、E1--E5 和势检查后，才可记录递归边。
2. (8) 未命中但某个 \(h\in\mathscr H_{\mathrm{Hall}}\) 的 (13) 非空：记录
   RAW_TYPE_II_TERMINAL。
3. 两者均未命中且 (11) 成立：记录 STRICT_LAYER_MOD4_OBSTRUCTED。
4. 两者均未命中且 (11) 不成立：记录 STRICT_LAYER_SPECTRUM_EMPTY，
   并保留 (12) 的完整 q-进谱缺口。
5. source profile 或 shared-\(q\) ledger 未闭合：记录 SOURCE_PROFILE_UNCLOSED，
   不能把有限结果解释成全层结论。

raw 分支是独立的有限正规形回退；它不要求 \(A_0,C_0\) 落在旧除子格中。
只有 raw 集也为空时，才允许把算术分支交给 Fourier/SNF 或其它已定义的
对偶容量接口。任何上述负回执都只排除声明的 source universe，不是原猜想反例。

## 6. 三个控制

### \(p=5113\) 的正谱

取 \(D=6\)、目标 \(f=(1,1)\)，并只看两个 active source rows

\[
N_{6,3}=5185=17\cdot305,\qquad
N_{6,6}=5257=7\cdot751.
\]

目标整数为 \(N_f=5117=7\cdot17\cdot43\)，所以

\[
\eta_7=\eta_{17}=1,\qquad E_f=7\cdot17=119,
\]

且

\[
\mathscr H_f=\{1,7,17,119\}.
\]

因为 \(7\equiv-1\pmod4\)，\(h=7\) 已命中 (8)，给出较低目标的直接
Type II 证书

\[
K'=2,\qquad B'=(2\cdot5113+1)/7=1461.
\]

若坚持使用两个 active source blocks，则 \(h=119\) 也命中，并且
\(119\equiv-1\pmod{24}\)，因此它还通过旧层合同 (9a)，得到

\[
K'=30,\qquad B'=1289.
\]

后一个见证正是已有的 \(D=6\to D'=1\) 两来源严格降模控制。

### \(p=57399241\) 的精确模 4 负谱

取 \(D=41\)、\(f=(1,1)\)，标准来源为 \(a=1,41\)。两条来源与目标的共同
因子都只有 \(5\)，故

\[
\eta_5=1,\qquad E_f=5,\qquad\mathscr H_f=\{1,5\}.
\]

这里 \(5\equiv1\pmod4\)，所以 \(-1\) 不在严格谱中；这给出
STRICT_LAYER_MOD4_OBSTRUCTED，并复现已有 \(D=41\) 的 source-map 障碍。

### \(p=73\) 的 raw-only 回退

旧除子格控制取 \(D_0=1,a_0=8,h=15\)。虽然旧参数纤维为空，但

\[
(A_0,C_0,K)=(2,2,1),\qquad
B=(73+2)/15=5
\]

属于 (13)，故分派为 RAW_TYPE_II_TERMINAL。这说明 spectrum 未命中时仍必须
执行 raw 回退，不能把旧除子格空集直接写成无证书。

## 7. 研究边界

该引理完成的是目标纤维内的 exact source-spectrum 与有限残数选择；它不证明
\(\Sigma_{D\to f}\) 对所有核心素数都命中，也不证明未命中时一定存在 F/G 载体、
Fourier 容量超载或严格核心素数下降。source profile 不完整时必须停止在
SOURCE_PROFILE_UNCLOSED，不能用有限谱冒充全称选择器。

窄复现：

~~~bash
python3 reproductions/type_i_linear_escape_target_supply_spectrum_strict_adapter.py --verify
~~~
