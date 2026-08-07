---
kind: claim
claim_id: type-I-g-anchor-c3-adaptive-core19-ambient19-terminal-screen
title: c=3 adaptive core-19 ambient-19 substrate 的固定 Type II 筛
statement: 在已证明的 adaptive c=3 factor-block raw family 中取 t=3231+3629v，可得 h=7572510960+8505305445v、p=181740263041+204127330680v。每个素数参数点都有 actual raw receipt，且 h=8 mod19、p=1 mod7、191|R=104h-9；因此 U(R) 有 ambient 19 阶角色。对该整条 affine ray，完整枚举固定 Type II 模板的必要充分有限筛：1536 个 step 因子中有192个 m=3 mod4 候选，合计976个 d|E_m^2 候选，固定 (m,d) 命中为零。该结果只排除整条 ray 的固定 Type II terminal；它不证明单点 terminal-free、F 商中的19角色存活、mixed-side 双叶来源或 selector edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-c3-adaptive-divisor-factor-block-normal-form
  - type-I-g-anchor-c3-factor-block-terminal-preemption
  - type-I-fg-raw-transcript-persistent-ledger-carry-core
  - type-II-small-shared-gap-explicit-fan
topics:
  - type-I
  - c3
  - raw-source
  - adaptive-divisor
  - q-primary
  - ambient-character
  - terminal-first
  - Type-II
  - affine-ray
  - proof-boundary
sources:
  - claim: type-I-g-anchor-c3-adaptive-divisor-factor-block-normal-form
    role: actual-raw-receipt-family
  - claim: type-I-g-anchor-c3-factor-block-terminal-preemption
    role: fixed-pair-affine-screen-interface
  - reproduction: reproductions/type_i_c3_adaptive_core19_ambient19_terminal_screen.py
    role: exact-CRT-and-fixed-pair-screen
visibility: public
last_checked: '2026-08-07'
---

# \(c=3\) adaptive core-19 ambient-19 substrate

## 1. 与 actual raw family 的 CRT 交集

已有 adaptive factor-block raw family 写作

\[
u=3+66963t,
\qquad h=35u,
\qquad p=840u+1.
\tag{1}
\]

其 raw receipt 条件为

\[
u\not\equiv1\pmod3,
\qquad
u\not\equiv10pmod {13},
\qquad
u\not\equiv10pmod {17},
\qquad
u\not\equiv100pmod {101}.
\tag{2}
\]

现在取

\[
t=3231+3629v,
\qquad 3629=19\cdot191,
\qquad v\ge0.
\tag{3}
\]

于是

\[
\begin{aligned}
u&=216357456+243008727v,\\
h&=7572510960+8505305445v,\\
p&=181740263041+204127330680v,\\
R&=787541139831+884551766280v.
\end{aligned}
\tag{4}
\]

这里

\[
\gcd(181740263041,204127330680)=1.
\tag{5}
\]

故 Dirichlet 定理保证 (4) 的 \(p\) 有无穷多个素数值。对每一个这样的素数参数点，
(2) 沿整条 ray 保持为

\[
u\equiv0\pmod3,
\qquad
u\equiv3pmod {13},
\qquad
u\equiv3pmod {17},
\qquad
u\equiv3pmod {101},
\tag{6}
\]

所以既有 theorem 给出 actual factor-block raw receipt。这里的“actual”只指该指定
factor-block normal form 的逐素数 raw word，尚不是 root 或 selector edge。

## 2. core-19、gap-7 residual 与 ambient 角色

由 (4) 直接有

\[
h\equiv8\pmod {19},
\qquad
p\equiv1\pmod7,
\qquad
191\mid R.
\tag{7}
\]

第一式使标准 \(c=3\) 单行的局部 E2 core 为 \(19\)。第二式避开 gap \(7\) 中
\(p\equiv3,5,6\pmod7\) 的三个固定小除子叶；它不排除 gap \(7\) 的其它因子证书。

又 \(191\) 是素数且

\[
191-1=190=2\cdot5\cdot19.
\tag{8}
\]

因此 \(U(191)\) 有一个精确 \(19\) 阶角色。由 \(U(R)\twoheadrightarrow U(191)\)
的约化映射复合，\(U(R)\) 至少有一个 ambient \(19\)-primary 角色。这只说明环境中
有角色；若未来固定层的稳定子把它杀掉，F 商仍可能没有 \(19\)-方向。

## 3. 整条 ray 的固定 \((m,d)\) Type II 筛

对一般 affine ray \(p(v)=P+Dv\)，其中 \(D\equiv0\pmod4\)，固定
\(m\equiv3\pmod4\) 与正整数 \(d\)。令

\[
X_m(v)=\frac{p(v)+m}{4},
\qquad
E_m=\gcd\left(\frac{P+m}{4},\frac D4\right).
\tag{9}
\]

则对每个 \(v\ge0\) 同时有

\[
d\mid X_m(v)^2,
\qquad m\mid X_m(v)+d
\tag{10}
\]

当且仅当

\[
m\mid D,
\qquad d\mid E_m^2,
\qquad m\mid P+4d.
\tag{11}
\]

加上 \(d\le X_m(0)\) 后，(11) 是“一个固定 \((m,d)\) 对整个 ray 都给出 Type II
certificate”的精确有限筛。证明见前一卡的同一 gcd 论证：\(E_m\) 是
\(X_m(v)\) 的所有值的 gcd，而同余条件分别比较 slope 与常数项。

对 (4) 的

\[
D=204127330680
=2^3\cdot3^2\cdot5\cdot7\cdot13\cdot17\cdot19\cdot101\cdot191,
\tag{12}
\]

完整地枚举 (11) 给出：

\[
\begin{array}{c|c}
\text{finite object}&\text{count}\\ \hline
d\mid D&1536\\
m\mid D,\ m\equiv3\pmod4&192\\
\text{all }d\mid E_m^2\text{ across those }m&976\\
\text{passes of (11) plus }d\le X_m(0)&0.
\end{array}
\tag{13}
\]

这里甚至没有额外施加自然范围 \(mle P-2\)，所以零命中确实排除了每个整条 ray 的
固定 \((m,d)\) 模板。它**不**排除依赖 \(v\) 的因子、只在部分 prime parameter 上
成立的模板，或其它 Type I/II terminal。

## 4. 当前地位与下一条证明义务

该 substrate 比 \(p=6121\) 控制多了一个必要资源：ambient \(19\)-character；又比
已截断的 factor-block rays 多了一个已核验的固定-pair terminal residual。它仍不是一个
已选中的核心素数控制点：事实上 (4) 的基点

\[
181740263041=23\cdot149\cdot53031883
\tag{14}
\]

不是素数，而 (5) 只保证无穷多个后续 prime parameter。

下一步的顺序必须是：

1. 在该 ray 的 prime parameter 上构造同一 declared source 的 mixed-side 双叶 raw tree
   \(C_0=p-3\) 与 \(C_1=19\)；
2. 为 \(C_1\) 给出 odd/mixed-side entry，而不是错误复用硬编码 even-tail 的 entry；
3. 证明某个 F fixed layer 的稳定子商仍保留这个 \(19\)-character；
4. 建立两叶相位、完整 physical transcript、持续 ledger 与 terminal-first guard；
5. 最后才讨论 `demand_to_slot`、E4 和 E5。

本卡没有完成上述任何 selector 接口，也没有证明 Erd\H{o}s--Straus 猜想或其任何
全称子情形。

复现：

```bash
python3 reproductions/type_i_c3_adaptive_core19_ambient19_terminal_screen.py --verify
```
