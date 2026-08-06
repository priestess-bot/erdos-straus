---
kind: claim
claim_id: type-II-qadic-height-kneser-block-bridge
title: Type II 单状态 q 进高度到 Kneser 幂块的精确桥
statement: 对规范 Type II 状态 s=a^2c、M=4ac、N=p+4s，若 q^e 整除 N 且 q 与 M 互素，把 q 因子块 B_q={1,q,...,q^e} 加入目标积集并取最终稳定子 T，则其活跃容量精确为 kappa_q=min(e,ord_{H/T}(qT)-1)。在最终稳定子语义下，非零价格分支满足 e+1<ord_{H/T}(qT) 且逐层支付；若 e+1>=ord_{H/T}(qT)，最终方向已被 T 吸收。非平凡有限阶折叠只能在插入时稳定子记录并转入稳定子塔。该桥是单状态精确容量映射，不自动提供跨移位注入或核心素数递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-shared-factor-q-adic-difference-bound
  - type-II-multiblock-kneser-active-capacity-dichotomy
  - type-II-private-factor-kneser-growth-stabilizer-bridge
topics:
- type-II
- q-adic
- Kneser
- active-capacity
- finite-order
- stabilizer
- dyadic
- relay
- proof-program
sources:
  - claim: type-II-shared-factor-q-adic-difference-bound
    role: q-adic-height-input
  - claim: type-II-multiblock-kneser-active-capacity-dichotomy
    role: multiblock-Kneser-capacity
visibility: public
last_checked: '2026-08-04'
---

# Type II 单状态 q 进高度到 Kneser 幂块的精确桥

## 状态与幂块

令

\[
s=a^2c,\qquad M=4ac,\qquad N=p+4s=p+aM,
\]

其中 \(p\) 为核心素数，且 \(\gcd(N,M)=1\)。后一个条件在规范扇的
\(4s<p\) 范围内自动成立。取奇素数 \(q\) 和

\[
e=v_q(N)\ge1.
\]

令 \(H\le U(M)\) 为目标积集所使用的有限残数生成群。把 \(N\) 的素因子逐个写成
有界幂块；固定除 \(q\) 以外的所有块，记其乘积集为 \(A_0\)，并令

\[
B_q=\{1,\bar q,\bar q^2,\ldots,\bar q^e\}\subseteq H,
\qquad
P=A_0B_q.
\]

取最终稳定子

\[
T=\operatorname{Stab}_H(P),
\qquad
o_q=\operatorname{ord}_{H/T}(\bar qT).
\]

因为 \(q\nmid M\)，\(\bar q\) 确实是 \(U(M)\) 中的单位，故上述幂块是合法的
目标除子残数块。

## 精确容量等式

定义 q 块的 Kneser 活跃容量

\[
\kappa_q=|B_qT/T|-1.
\]

则有精确公式

\[
\boxed{
\kappa_q
=\min(e+1,o_q)-1
=\min(e,o_q-1).
}
\tag{1}
\]

### 证明

在商群 \(H/T\) 中，\(B_qT/T\) 是循环子群
\(\langle\bar qT\rangle\) 内的连续指数段

\[
\{1,\bar qT,\ldots,(\bar qT)^e\}.
\]

该集合的基数恰为 \(\min(e+1,o_q)\)：若 \(e+1<o_q\)，所有指数不同且尚未绕满；
若 \(e+1\ge o_q\)，它已经绕满该循环子群。减去一即得 (1)；最终稳定子下后一种
情形由折叠塌缩引理进一步迫使 \(o_q=1\)。证毕。

## q 进高度的最终/插入层分派

公式 (1) 给出没有歧义的局部分流。

### 1. 完全支付分支

若

\[
e+1<o_q,
\]

则

\[
\boxed{\kappa_q=e.}
\tag{2}
\]

q 的每一个实际赋值层 \(1,\ldots,e\) 都在 \(H/T\) 中留下一个新的幂块残类；
此时 q 进高度可以逐层注入 Kneser 的活跃容量。

### 2. 有限阶折叠分支

若

\[
e+1\ge o_q,
\]

则 q 幂块在 \(H/T\) 中已经绕满其商循环。由于这里的 \(T\) 是完整积集的
最终稳定子，最终稳定子下的 q 折叠塌缩引理给出

\[
\boxed{o_q=1,\qquad \kappa_q=0.}
\tag{3}
\]

这时 q 方向完全被最终稳定子吸收，不能把 \(e\) 层继续当作最终容量。该塌缩的
独立证明见[Type II 最终稳定子下 q 幂折叠的吸收塌缩](type-II-final-stabilizer-q-fold-collapse.md)。
若需要记录
\(o_q\ge2\) 的非平凡有限阶关系，必须把 \(T\) 改为 q 块插入前的中间稳定子
\(T^{\mathrm{ins}}\)：在
\(e+1\ge\operatorname{ord}_{H/T^{\mathrm{ins}}}(qT^{\mathrm{ins}})\) 时记录
\(\mathrm{Q\_PREFIX\_ORDER\_FOLD}\)，并把新稳定子送入稳定子塔；该中间价格不能再
与最终 \(T\) 下的价格相加。原公式
\(\kappa_q=\min(e,o_q-1)\) 仍成立，但在最终稳定子语义下其非零分支只能是
\(e+1<o_q\)，此时 \(\kappa_q=e\)。

## 与有限移位 q 进容量的组合

对一组规范移位 \(S\)，记

\[
e_s=v_q(p+4s),\qquad
o_s=\operatorname{ord}_{H_s/T_s}(qT_s),\qquad
\kappa_s=\min(e_s,o_s-1).
\]

已有移位差容量不等式给出

\[
\sum_{s\in S}e_s
\le
\sum_{r=1}^{E}C_r(S,q),
\qquad E\ge\max_{s\in S}e_s.
\tag{4}
\]

将每个状态按 \(e_s+1<o_s\) 或 \(e_s+1\ge o_s\) 分组，得到精确账本

\[
\sum_{\{s:e_s+1<o_s\}}\kappa_s
=\sum_{\{s:e_s+1<o_s\}}e_s,
\tag{5}
\]

\[
\sum_{\{s:e_s+1\ge o_s\}}(e_s-\kappa_s)
=\sum_{\{s:e_s+1\ge o_s\}}e_s.
\tag{6}
\]

式 (5) 是可直接送入跨状态容量的“完全支付”部分；式 (6) 则标记已经被最终
稳定子吸收的高度。若某个外部 relay 要求每个 q 进层都保持为独立目标残数，则它只能
使用 (5) 中的状态；一旦出现 (6)，只能保留最终吸收回执，或在插入时稳定子上
携带有限阶/商群标签进入稳定子塔，否则就是重复计费。

## 与多块 Kneser 目标终端的接口

把所有素因子块重新编号为 \(B_1,\ldots,B_r\)，令
\(P=A_0B_1\cdots B_r\) 和最终稳定子 \(T\)。多块 Kneser 给出

\[
|P|\ge |A_0T|+|T|\sum_i\kappa_i.
\]

因此，若目标缺失，完全支付的 q 进部分只能贡献
\(\sum\kappa_i\) 中的精确项 (5)；最终稳定子吸收的部分不能再按原始高度
\(e_s\) 增加容量。若在插入时稳定子上出现二阶或非对合有限阶，则分别进入
二幂/primary 终端或可枚举的稳定子塔关系；不能把该中间关系改写成最终商中的
非平凡有限阶价格。

这给出一个严格的单状态选择器：

\[
\text{q-height }e
\longrightarrow
\begin{cases}
\text{逐层 Kneser 活跃容量},&e+1<o_q,\\
\text{最终稳定子吸收},&e+1\ge o_q,\\
\text{插入层有限阶关系},&e+1\ge o_q^{\mathrm{ins}}.
\end{cases}
\]

## 边界

本卡没有证明：

1. 不同移位的 \(H_s/T_s\) 可以自然识别为同一个商群；
2. 所有 q 进高度都处于最终完全支付分支；
3. 插入层有限阶关系自动给出 Type I/II 证书或可提升递降；
4. 式 (4) 的跨移位容量可以直接与不同状态的 Kneser容量相加。

因此它填补的是“单状态 q 高度到 Kneser 块”的精确算术映射，下一步的决定性任务变为：
对完全支付状态建立共同商群/载体识别；对插入层折叠证明其稳定子塔关系导致严格
商群下降、二幂终端或新的 Type II 证书。
