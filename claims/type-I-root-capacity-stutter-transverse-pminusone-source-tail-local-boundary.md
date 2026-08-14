---
kind: claim
claim_id: type-I-root-capacity-stutter-transverse-pminusone-source-tail-local-boundary
title: 横向 p 减一 complete-excess relay 不强制 p 减一 source tail
statement: >-
  p=241、q=5、r=16、E=3375、D=25 给出一个核心素数上的局部 p-1,h+1
  complete-excess relay 控制：q-primary receipt、D*、canonical complete-excess、
  receipt quotient、checkpoint 和 Eisenstein norm exclusion 条件全部成立。但 p-1=240
  的完整平移平方因子 source fan 仅有 d=1,5 两行，二者均不存在满足
  e1|M1^2、e1<=M1、e1=-M1 mod (s-1) 的 e1。因此仅靠该局部 relay 条件不能
  强制 p-1 source descent。该控制 h>p，故不是 actual proper-root receipt；它严格
  划定的是 relay-to-source-tail 推理的缺失 actual-root 输入，不是否定 actual 分支
  或全局出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-transverse-overlap-receipt-relay
  - type-I-root-capacity-stutter-transverse-pminusone-excess-norm-exclusion
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

## 4. 结论与边界

该控制严格否定以下仅依赖局部 relay 的蕴涵：

\[
\text{p-minus-one complete-excess relay}
\Longrightarrow
\text{p-minus-one source-tail witness}.
\tag{10}
\]

所以后续 adapter 必须实质性使用 actual proper-root 的额外约束，例如
\(h\mid p^2+p+1\)、\(h<p\)、完整最大化 provenance，或构造一条与
\(p-1\) fan 不同的证书/递降。这不证明 actual proper-root relay 永远不能命中
\(p-1\) fan，也不排除 \(p=241\) 的其它 Type I/II 证书。

## 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_stutter_transverse_pminusone_source_tail_boundary.py --verify
```

复现器只重算 (5)--(9)：一个固定局部 relay 和对 \(240\) 的两个完整 fan 行的
有限因子检查；它不扫描素数，也不运行历史测试。
