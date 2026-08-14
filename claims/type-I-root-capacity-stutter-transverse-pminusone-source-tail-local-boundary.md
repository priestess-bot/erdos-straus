---
kind: claim
claim_id: type-I-root-capacity-stutter-transverse-pminusone-source-tail-local-boundary
title: 横向 p 减一 complete-excess relay 不强制 p 减一 source tail
statement: >-
  p=241 的局部 complete-excess relay 控制和 p=8641 的 proper-root/receipt-q-primary
  定向控制均没有 p-1 source tail。后者已满足 h|p^2+p+1、h<p、root gcd、
  v_q(ph+1)=2b+t、v_q(T)=b+t 以及定向 root-quotient 赋值，而 p-1=8640 的完整
  平移平方因子 source fan 四行全空；这里 t=b=1 且 w+9 恰有 q^(2b) 容量。
  因此 relay、定向 root-quotient 及其精确 w+9 阶梯都不能单独强制 p-1 source
  descent；两个控制均不被冒充为完整 actual stutter receipt，故该边界不否定 actual
  分支或全局出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-transverse-overlap-receipt-relay
  - type-I-root-capacity-stutter-transverse-pminusone-excess-norm-exclusion
  - type-I-root-capacity-stutter-transverse-pminusone-root-quotient-orientation
  - type-I-root-capacity-stutter-transverse-pminusone-w-offset-valuation-staircase
  - p-minus-one-source-descent
topics:
  - type-I
  - root-capacity
  - stutter
  - transverse-residual
  - complete-excess
  - p-minus-one
  - external-source
  - descent
  - counterexample
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-transverse-overlap-receipt-relay
    role: local-q-primary-receipt-and-checkpoint-relay
  - claim: type-I-root-capacity-stutter-transverse-pminusone-excess-norm-exclusion
    role: local-norm-provenance-exclusion
  - claim: type-I-root-capacity-stutter-transverse-pminusone-root-quotient-orientation
    role: proper-root-and-receipt-q-primary-orientation-input
  - claim: type-I-root-capacity-stutter-transverse-pminusone-w-offset-valuation-staircase
    role: exact-w-plus-nine-capacity-boundary-input
  - claim: p-minus-one-source-descent
    role: complete-p-minus-one-source-tail-parameterization
  - reproduction: reproductions/type_i_root_capacity_stutter_transverse_pminusone_source_tail_boundary.py
    role: fixed-local-relay-and-exhaustive-p-minus-one-fan-control
visibility: public
last_checked: '2026-08-14'
---

# 横向 \(p-1\) complete-excess relay 不强制 \(p-1\) source tail

## 1. 要排除的错误推理

在 \(p-1,h+1\) complete-excess overlap 中，receipt/checkpoint relay 给出

\[
q\mid e,\qquad
v_q(e)=v_q(s+1)=v_q(r-1)=v_q(E_1+1)=v_q(p-1).
\tag{1}
\]

这看起来像可进入 \(n=p-1\) 外部源的因子，但完整的 \(p-1\) source fan 还需要
选择

\[
d\mid p-1,\qquad d\equiv1\pmod4,
\tag{2}
\]

并为

\[
s_0=\frac{p-1}{d},\qquad r_0=s_0-1,\qquad
k_0=\frac{p-d}{4},\qquad M_1=k_0s_0
\tag{3}
\]

找到平方尾因子

\[
e_1\mid M_1^2,\qquad e_1\le M_1,\qquad
e_1\equiv-M_1\pmod {r_0}.
\tag{4}
\]

本卡给出一个严格的局部控制，说明 (1) 不能省略 (4)。这里 \(s\) 是
\(E=1+ps\) 的 checkpoint 参数；它不是 (3) 的 \(s_0\)，两者没有由 relay
自动给出的同余桥。

## 2. 核心素数上的局部 relay 控制

取

\[
(p,q,r,E,D)=(241,5,16,3375,25).
\tag{5}
\]

其中 \(p\equiv1\pmod {24}\) 为素数。按 receipt 恒等式定义其余量，得到

\[
\begin{aligned}
T&=929175,& h&=447770264,& m&=1857968,\\
e&=4316505345,& a&=8019928355068696,& s&=14.
\end{aligned}
\tag{6}
\]

令 \(b=v_5(p-1)=1\)、\(t=v_5(D)-b=1\)。直接整数计算给出

\[
\begin{gathered}
v_5(T)=b+t=2,\qquad D_*=5,\qquad
v_5(E)=3>b,\\
5\mid(m+2,p-1,E),\qquad
v_5(e)=v_5(s+1)=v_5(r-1)=v_5(E_1+1)=1,\\
v_5(a)=v_5(B_1)=0.
\end{gathered}
\tag{7}
\]

而 \(v_5(R-h)=5>2b+t=3\)，所以它也满足该支路所需的 q-primary
complete-excess 阈值；同时

\[
a^2-a(e-1)+(e-1)^2\equiv3\pmod5.
\tag{8}
\]

也就是说，(5) 满足当前 relay 和 norm-exclusion 所使用的全部局部 \(q\)-primary
条件。

它不是 actual proper-root receipt：已经有 \(h>p\)，违反 proper-root 域。
因此此处不会把这个控制误报为 actual global-state 反例。

## 3. 完整 p 减一 fan 的精确失败

对 \(p-1=240\)，(2) 的全部可用因子恰为

\[
d\in\{1,5\}.
\tag{9}
\]

将这两行代入 (3)--(4)，得到完整的有限检查表：

| \(d\) | \(s_0\) | \(r_0\) | \(k_0\) | \(M_1\) | \(M_1^2\) 的因子数 | 满足 (4) 的 \(e_1\) |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | 240 | 239 | 60 | 14400 | 325 | 无 |
| 5 | 48 | 47 | 59 | 2832 | 81 | 无 |

完整 \(p-1\) source-tail 参数化因此给出：这个 \(p\) 没有任何该 fan 的
strict source lift，尽管 (7) 的 q-primary relay 全部成立。

## 4. proper-root 与 receipt-q-primary 强化控制

上一个控制故意违反 \(h<p\)。为检验这一缺口是否足以自动恢复 \(p-1\) source fan，
取另一固定控制

\[
(p,h,q,r)=(8641,39,5,266).
\tag{10}
\]

这里 \(p\equiv1\pmod {24}\) 为素数，令

\[
u=13,\qquad
\frac{p^2+p+1}{3}=24891841,\qquad
(2r+1,\,(p^2+p+1)/3)=u.
\tag{11}
\]

所以 \(h=3u\mid p^2+p+1\) 且 \(2\le h<p\)。记 \(b=v_5(p-1)=1\)，直接计算

\[
\begin{gathered}
v_5(h+1)=v_5(r-1)=1,\qquad
v_5(ph+1)=3,\qquad v_5(T)=2,\\
v_5\left(\frac{p^2+p+1}{h}+3\right)=1,\qquad
v_5\left(\frac{2r+1}{u}+9\right)=2.
\end{gathered}
\tag{12}
\]

这正是 root-quotient 定向引理使用的 proper-root 与 receipt-q-primary 输入，
其中 \(t=b=1\)。新的 \(w+9\) 赋值阶梯在这个非共振点给出精确的

\[
v_5(w+9)=2b=2,
\qquad w=\frac{2r+1}{u}=41.
\tag{13}
\]

它仍不构成完整 actual stutter receipt：本控制没有声称存在相应的 canonical
\(D,E\)、最大化 provenance 或状态合同。

但是 \(p-1=8640\) 的完整 \(p-1\) source fan 依旧为空。其全部
\(d\equiv1\pmod4\) 行为：

| \(d\) | \(s_0\) | \(r_0\) | \(k_0\) | \(M_1\) | \(M_1^2\) 的因子数 | 满足 (4) 的 \(e_1\) |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | 8640 | 8639 | 2160 | 18662400 | 1365 | 无 |
| 5 | 1728 | 1727 | 2159 | 3730752 | 819 | 无 |
| 9 | 960 | 959 | 2158 | 2071680 | 1215 | 无 |
| 45 | 192 | 191 | 2149 | 412608 | 351 | 无 |

因此，甚至加入 (12)--(13) 的定向及精确 \(w+9\) 容量，也还不能从当前已知关系构造
\(p-1\) source-tail witness。

## 5. 结论与边界

这两个控制共同严格否定以下仅依赖 relay 或其已知 root/receipt-q-primary 强化的蕴涵：

\[
\text{p-minus-one complete-excess relay}
\Longrightarrow
\text{p-minus-one source-tail witness}.
\tag{14}
\]

所以后续 adapter 必须实质性使用尚未进入 (12)--(13) 的完整 actual receipt 数据，
特别是 canonical \(D,E\) 的逐素数最大化 provenance，或构造一条与 \(p-1\) fan
不同的证书/递降。这不证明 actual proper-root relay 永远不能命中 \(p-1\) fan，
也不排除两个控制素数的其它 Type I/II 证书。

## 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_stutter_transverse_pminusone_source_tail_boundary.py --verify
```

复现器只重算两个固定控制和 \(240,8640\) 的完整有限 fan 行；大载体的平方因子
由分解生成而非逐整数扫描。它不扫描素数，也不运行历史测试。
