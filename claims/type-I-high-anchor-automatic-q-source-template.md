---
kind: claim
claim_id: type-I-high-anchor-automatic-q-source-template
title: 高锚 automatic-q 余因子 gate 的来源构造模板
statement: 设 H=(p,R,K;A) 是 canonical 高锚，K=AB，complete-excess bundle 为 Q，令 t=Q/gcd(A,Q)，故 M=lcm(A,Q)=At。若 qA<p，则 rechart cofactor C=qA 当且仅当 4qA^2t=1 (mod p)，也当且仅当 qAt=B (mod p)；若 q>1，则 high-window 强制 q 只能为 2 或 3。此时 gate 自动通过，且若 r=M mod p，cofactor phase 满足 h=(qr-B)/p，0<=h<q，h=-B (mod q)。因此 B=1 (mod q) 当且仅当 h=q-1，并落入 e=c-(h+1)=0 的最小正相位 fixed-n pivot 输入。若 core root 的第一次 complete-excess rechart 已进入高锚，写 R0-1=A beta0，则 beta0 只能为 1 或 2；为使第二锚落入 Q=R-1 子族，beta0=1 被 2-adic 条件排除，beta0=2 仍须独立通过逐素数幂严格 excess 检查。特别地，在额外的互素充分子族 Q=R-1、gcd(A,R-1)=1 中，令 delta=R-p，则 delta=1+(4qA^2)^(-1) (mod p) 是高窗口内唯一候选；加上 0<delta<4A-p、4A divides p(p+delta)+1 和完整 excess 条件，即得到 M=A(R-1)、C=qA 的实际 high-R raw-source/bundle 构造。该模板不强迫 nonterminal、parent provenance、typed fiber、terminal-first priority receipt 或 E1--E5 宏闭包。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-high-anchor-full-excess-gate-design-template
  - type-I-high-anchor-minimal-positive-phase-fixed-n-bridge
  - type-I-high-anchor-cofactor-macro-e1-e4-admission
  - type-I-high-anchor-positive-phase-terminal-boundary
topics:
  - type-I
  - high-anchor
  - full-excess
  - cofactor-gate
  - source-construction
  - congruence
  - root-normal-form
  - valuation
  - positive-phase
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_high_anchor_automatic_q_source_template.py
    role: exact replay of seven named fresh-root controls, two automatic-q controls, a finite terminal prefix, and one q-choice near miss
  - result: reproductions/type-i-high-anchor-automatic-q-source-template-results.json
    role: frozen arithmetic source-template witnesses
  - reproduction: reproductions/type_i_high_r_chart_p3793_audit.py
    role: dedicated fresh-root to q=2 high-anchor control
  - reproduction: reproductions/type_i_high_r_chart_60913_h2_nonreturn.py
    role: dedicated fresh-root to q=3 high-anchor control
visibility: public
last_checked: '2026-08-06'
---

# 高锚 automatic-q 余因子 gate 的来源构造模板

## 1. 把 automatic gate 写成 complete-excess 商条件

固定 canonical 高锚

\[
H=(p,R,K;A),\qquad p<R<4A,\qquad K=AB,\qquad A\mid K.
\]

令 \(Q\) 为 \(R-1\) 相对 \(K\) 的 complete-excess bundle，写

\[
t=\frac{Q}{(A,Q)},\qquad M=\operatorname{lcm}(A,Q)=At.
\tag{1}
\]

若某个 \(q\ge1\) 满足 \(qA<p\)，则 full-excess rechart 的 cofactor 恰为 \(C=qA\)
当且仅当

\[
\boxed{
4qA^2t\equiv1\pmod p
\quad\Longleftrightarrow\quad
qAt\equiv B\pmod p.
}
\tag{2}
\]

第一式只是 canonical rechart 的 \(4MC\equiv1\pmod p\) 代入 (1) 和 \(C=qA\)；
第二式由高锚的 \(4AB\equiv1\pmod p\) 得到。于是 gate 的 reduced divisor 是
\(A/(A,C)=1\)，无需再筛 \(r\)。

若 \(q>1\)，则 \(p<R<4A\) 和 \(qA<p\) 给出

\[
\frac p4<A<\frac pq,
\]

所以仅可能有

\[
\boxed{q\in\{2,3\}.}
\tag{3}
\]

因此寻找 strict automatic support growth 可先把 \(t\) 限为唯一的目标剩余类

\[
t\equiv(4qA^2)^{-1}\pmod p.
\tag{4}
\]

## 2. automatic family 的相位指纹

令 \(r=M\bmod p\)。由 (2)，\(qr\equiv B\pmod p\)，从而

\[
h=\frac{qr-B}{p},\qquad0\le h<q,\qquad h\equiv-B\pmod q.
\tag{5}
\]

这里非负性使用 \(1\le B<p\)，上界使用 \(0<r<p\)。由于
\(p\equiv1\pmod {24}\) 且 (3)，有 \(p\equiv1\pmod q\)，所以

\[
\boxed{B\equiv1\pmod q\quad\Longleftrightarrow\quad h=q-1.}
\tag{6}
\]

automatic family 中 \(g=(A,C)=A\)、\(a=1\)、\(c=q\)。若 (6) 成立，则
\(e=c-(h+1)=0\)，所以 \(q=2\) 给 \(h=1\)，\(q=3\) 给 \(h=2\)。这正是
最小正相位 fixed-\(n\) pivot 的算术输入；仍须另有 typed target、terminal-first 和
完整宏回执才能把 pivot 作为真实后继。

## 3. fresh root 的两种精确形式

令 core root 满足

\[
K_0=\frac{pR_0+1}{4},\qquad R_0<p,
\]

并设 \(R_0-1=A\beta_0\)。第一次 complete-excess rechart 使用 support \(1\)，且
已知其 carrier 为 \(A=Q_0\)、重图表后确实进入 \(p<R<4A\) 的高锚。于是
\(A>p/4\) 和 \(R_0<p\) 给出 \(\beta_0<4\)。complete-excess 的余项
\(\beta_0\) 整除 \(K_0\)，而

\[
4K_0=pR_0+1\equiv p+1\pmod{\beta_0}.
\]

故 \(\beta_0\mid p+1\)。又 \(p\equiv1\pmod3\)，不可能有
\(\beta_0=3\)，因此

\[
\boxed{\beta_0\in\{1,2\}.}
\tag{7}
\]

这里不能把 complete-excess 错写成互素条件。置

\[
s=\frac{p+1}{2},\qquad
\mathcal E_s(D)\ \Longleftrightarrow\
\forall\,\ell^e\parallel D,\quad e>\nu_\ell(s),
\tag{8}
\]

其中 \(D\) 为奇数。保持上述 core-source 前提时，两个 root bundle 的**精确**
条件为

\[
\begin{array}{c|c}
\beta_0 & (Q_0,\beta_0)\\ \hline
1 &
R_0=A+1,\quad A\equiv2\pmod8,\quad \mathcal E_s(A/2)\\[1mm]
2 &
R_0=2A+1,\quad A\equiv3\pmod4,\quad \mathcal E_s(A).
\end{array}
\tag{9}
\]

相应恒等式是

\[
2K_0=p(A/2)+s\quad(\beta_0=1),\qquad
2K_0=pA+s\quad(\beta_0=2).
\tag{10}
\]

所以每个奇素数幂是否完整进入 \(Q_0\) 取决于其幂次是否**严格大于**
\(\nu_\ell(s)\)，而非是否与 \(s\) 互素。比如
\((p,A,R_0)=(409,250,251)\) 的 \(\beta_0=1\) 行和
\((409,175,351)\) 的 \(\beta_0=2\) 行都分别有共同因子 \(5\)，却仍有
\((Q_0,\beta_0)=(250,1)\) 和 \((175,2)\)。式 (9) 本身也不保证 first rechart
是高锚；高窗口必须独立保留。

## 4. 第二锚的 exact full-excess 门与 \(\beta_0=1\) no-go

对第一次 rechart 得到的高锚 \((p,R,K;A)\)，令

\[
D=\frac{R-1}{2}.
\]

由

\[
2K=pD+s
\tag{11}
\]

得到第二 bundle 的精确判据

\[
\boxed{
Q_1=R-1
\quad\Longleftrightarrow\quad
R\equiv3\pmod8\ \text{且}\ \mathcal E_s(D).
}
\tag{12}
\]

第一条件保证 \(K\) 为奇数，从而 \(R-1\) 中唯一的因子 \(2\) 也完整进入
excess；第二条件处理全部奇素数幂。旧的
\((D,s)=1\) 只是 (12) 的方便充分子族，并非必要条件：
\((p,A,R_0)=(1033,351,703)\) 给出
\((R,K)=(1211,312741)\)、\(Q_1=1210=R-1\)，但
\((D,s)=(605,517)=11\)。

当 \(\beta_0=1\) 时，(9) 的 \(A\equiv2\pmod8\) 与 canonical congruence
强制

\[
R\equiv7\pmod8,
\]

故 (12) 不可能成立。于是任何 two-anchor automatic-q 构造若要进入
\(Q_1=R-1\) 子族，必须从 \(\beta_0=2\) root 开始。反向不成立：
\((p,A,R_0)=(97,39,79)\) 已有 \(\beta_0=2\) 和高锚
\((R,K)=(119,2886)\)，但 \((Q_1,\beta_1)=(59,2)\)。因此
\(\beta_0=2\) 只是唯一未被这条 \(2\)-adic 障碍排除的 root type，第二个
strict-valuation 门仍不可省略。

## 5. \(Q=R-1\) 的反向构造子族

再假设

\[
Q=R-1,\qquad(A,R-1)=1.
\tag{13}
\]

令 \(R=p+\delta\)。由 (1) 和 (4)，任何 automatic-q 高锚必须满足

\[
\boxed{
\delta\equiv1+(4qA^2)^{-1}\pmod p.
}
\tag{14}
\]

而 (3) 给 \(4A-p<p\)，所以若

\[
0<\delta<4A-p,
\qquad
4A\mid p(p+\delta)+1,
\tag{15}
\]

则 (14) 在 high window 内至多给一个 \(R\)。若该候选还通过 (13) 的
complete-excess 与互素检查，令

\[
K=\frac{pR+1}{4},
\]

就有 actual high-R raw source、\(M=A(R-1)\) 及 \(C=qA\)。这不是范围搜索：
每一对预先指定的 \((p,A,q)\) 至多需要检查一个候选 \(R\) 的因子分解。

相反，(14)--(15) 不会强迫 \(Q=R-1\) 或 \((A,R-1)=1\)。这两个因子条件是构造
fresh automatic source 的真实筛选门，而不是可由同余单独删除的假设。

## 6. 两个 fixed automatic-q 控制与有限 terminal 前缀

| \(p\) | \(q\) | \(A\) | \(\delta=R-p\) | \(B\) | \(B\bmod q\) | \(h\) |
|---:|---:|---:|---:|---:|---:|---:|
| 3793 | 2 | 1811 | 3218 | 3671 | 1 | 1 |
| 60913 | 3 | 18647 | 11346 | 59011 | 1 | 2 |

两行都从 \(\beta_0=2\) root 出发，满足 (12)--(15)，并由 dedicated fresh-root 到
high-anchor 的 source/path 回放实际生成 \(C=qA\)。它们证明的是 fresh source
可达性、来源构造和 phase 指纹，而不是未解 recursive coverage。

本夹具还记录了一个固定的、但非穷尽的 terminal-first 前缀。令

\[
x=\frac{p+7}{4}.
\]

对 \(p\equiv1\pmod{24}\)，下表中的 \(d\) 总满足
\(d\mid x^2\)、\(d\le x\)、\(x+d\equiv0\pmod7\)，因而给出 gap \(7\) 的
Type II 证书：

| \(p\bmod7\) | \(p\bmod168\) | \(d\) |
|---:|---:|---:|
| 3 | 73 | 1 |
| 5 | 145 | 4 |
| 6 | 97 | 2 |

两条 automatic-q control 都是 \(97\pmod{168}\)，所以夹具以 \(d=2\) 实际重建
Type II terminal。专用 companion replays 也有 Type I terminal；这里选择 Type II
只是为了把这个常数时间的 gap-7 prefix 统一入来源回放。未命中该表只表示没有命中
这个有限 prefix，绝不表示不存在其它 terminal。

在 \(p=60913,A=18647\) 固定时，换取 \(q=2\) 仍有 \(2A<p\)，但实际
\(t\bmod p=11345\)，而 (4) 所要求的是 \(47474\)。所以同一个 high anchor 不会因为
\(qA<p\) 就被错误归入另一 automatic family。

## 7. 边界

本卡的 positive controls 只在本回放器中验证 H1 raw-source/bundle 与 cofactor 算术；
其专用 companion replays 虽已给出 fresh-root parent 链，仍不提供：

- 一个不被 terminal-first 抢占的 high macro；
- H/S/T 的 parent provenance 和 typed F/G/hit reclassification；
- priority-prefix guard、pending dispatch 或全局 E5；
- 任何对所有核心素数的 complete-excess 存在性定理。

因此它是新 fresh source 的有限构造接口，而不是 Erdos--Straus 猜想的递归证明。

## 复现

```bash
python3 reproductions/type_i_high_anchor_automatic_q_source_template.py --verify
```
