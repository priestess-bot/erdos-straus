# T6 F2/F3 第三轮证明复核与下一步接口

> 日期：2026-08-25
>
> 结论：没有闭合 F1、F2、F3、T6 或 Erdős--Straus 猜想。此轮的价值是消除四条看似
> 可行但实际不能过 E1/E3/E5 的路线，并把 proper-root 的下一张可证明接口收缩为一份
> 可验证 receipt 规格。

## 当前状态

| 层 | 状态 | 本轮变化 |
|---|---|---|
| F1 | `OPEN_MINIMAL_GAPS` | 发现 shared receipt 不携带 source scope、raw transcript 或逐前缀 terminal 结果；不能把 digest 字符串当 E1。 |
| F2 | `OPEN` | 排除了 hard-core universal R=3 非锚首边的全称策略，且排除了 C>1 当前 external rechart 作为 phase/E5 出口。 |
| F3 | `OPEN_MINIMAL_GAPS` | proper-root chart 已与 \(p,r\) 绑定；QC1/TR1 有更精确的条件 raw suffix，但均尚未进入 shared producer。 |
| T6 | `OPEN` | 没有新增 registered producer，也没有 active verified successor。 |

机器可读总前沿见
[`data/t6-wave1/t6-f2-f3-residual-frontier-v1.json`](../data/t6-wave1/t6-f2-f3-residual-frontier-v1.json)。

## 1. 先修复合同语义，而不是伪造 C8/proper-root source

原 v1 header 将 `provenance_kind=OVERFLOW` 错当成 \(R>p\) 的唯一表示。真实 C8
parent 和 proper-root chart 都可以是 `TYPEI/CHARGED` overflow；例如 C8 control
\(p=157393\) 有 \(R=68123821967>p\)，而 proper-root control
\((p,r)=(313,90)\) 有

\[
A=1384277321,\qquad K=431894524152,\qquad R=5519418839.
\]

本轮已作如下窄修复：

\[
\texttt{is\_overflow}\Longleftrightarrow R>p
\qquad(\texttt{TYPEI/CHARGED}),
\tag{1}
\]

并对 `PROPER_ROOT` 重算

\[
g=\frac{p+1}{2},\quad A=g(p^2r-g),\quad K=A(p-1),\quad
R=2p^3r-p^2-2pr-p+1.
\tag{2}
\]

`C8_PARENT` 与三个 proper-root owner 现在可以和明确列出的 overflow refinement
合法重叠，固定 precedence 仍选择谱系 owner。该变更只让 type space 忠实表示已知图表；
它没有提供 C8 relay、fresh scope、E1、producer、E3 或 re-entry。

## 2. F2 的两条负向收缩

### 2.1 R=3 hard core 不保证 non-anchor raw 首边

令 \(P=p+4\)、\(N=(3p+1)/4\)、\(D=2p-3\)。hard core 中

\[
8N-3D=11,\qquad (D,N)=1.
\tag{3}
\]

从 universal source \((p,D,p-1)\) 出发，所有非 \(p\) 首 label 正好是 \(D\) 的
素因子 \(q\)，并给出

\[
(p,D,p-1)\longmapsto
\left(\frac Dq,\frac{D/q+3}{2},\frac{D/q+1}{2}\right).
\tag{4}
\]

它 non-anchor 当且仅当 \(D\) 合成。控制
\(p=2521\) 满足 hard core，但 \(D=5039\) 是素数，故唯一首边正是 anchor。
这排除了“hard core 自动给出 non-anchor source”这条全称策略，不排除另一 source、
Type-II terminal 或新 intermediate projection。完整命题见
[`type-I-f2-high-support-r-three-raw-menu-and-external-rechart-boundary`](../claims/type-I-f2-high-support-r-three-raw-menu-and-external-rechart-boundary.md)。

### 2.2 C>1 的现有 full-excess rechart 不能偷渡为 ABSORB 或 E5

若 \(A>B_p\)、\(M=\operatorname{lcm}(A,Q)>A\)，则 canonical target 若有
\(R_M<p\) 会推出 \(K_M\le B_p<M\le K_M\)，矛盾。因此它必为 overflow。空改善叶还有
\(c_M\ge C\)，故在固定 \(\eta_p\) 下无法支付 `LOCAL_DROP`。这只排除当前 external
full-excess rechart；新的 terminal、non-bundle raw carrier 或独立 E5 producer 仍可能存在。

## 3. F3 的三个精确边界

### 3.1 High default tree 的第三 full-product fold 不存在

q=1 fresh default tree 的已命名两步 menu 有 \(M_2<4p^2\)。canonical high root 的任何
exact full-product inverse predecessor 则有

\[
M_d=\frac{A_\star}{d}\ge\frac{A_\star}{p-1}>4p^2.
\tag{5}
\]

所以第三步不能是这类 fold。fixed-\(n\)、r-chart 和 RESET 也都太小。仍开放的是
single-side / atomic complete-excess 路线，它必须带真实 maximal occurrence、terminal
prefix、fresh scope 和 E3 validator。详见
[`type-II-q-one-default-tree-third-full-product-high-root-obstruction`](../claims/type-II-q-one-default-tree-third-full-product-high-root-obstruction.md)。

### 3.2 QC1 的 rank-stutter 不是 raw dead end

已有 \(q_\perp\mid E\) 首次 deflation 在 first atomic multiplier
\(F_y\equiv q^\mu\pmod p\) 时会 rank-stutter。此时取

\[
s=\min\{\ell:\ell\mid F_y,\ \ell\not\equiv1\pmod p\}
\tag{6}
\]

便有第二个 deterministic raw deflation，且其 selected-side cofactor 小于 \(p-1\)。
它仍缺 path receipt、second-child terminal priority、E3/E4/re-entry；故仅是条件
arithmetic continuation，而不是 selector edge。更新后的命题见
[`type-I-t6-f3-qc1-endpoint-excess-deflation`](../claims/type-I-t6-f3-qc1-endpoint-excess-deflation.md)。

### 3.3 TR1 现在有 fresh/saturated 精确分流

对 \(q\mid D_*\)，canonical maximality 精确给出：

\[
q\mid E\Longleftrightarrow v_q(z)>v_q(K).
\tag{7}
\]

所以 \((D_*,E)>1\) 时，最小 fresh prime 有一个 source-bound primitive raw suffix；
\((D_*,E)=1\) 时每个 \(D_*\) 因子都 capacity-saturated，不能作为当前 complete-excess
resource。\(2\mid(D_*,E)\) 还使该 raw child 自动 p-free。此结果不证明前者必发生，也
不完成 child target。详见
[`type-I-t6-f3-tr1-fresh-dstar-endpoint-split`](../claims/type-I-t6-f3-tr1-fresh-dstar-endpoint-split.md)。

## 4. 下一张必须完成的证明接口

当前共同瓶颈不是再添加一个同余条件，而是把实际 root source 正向绑定到 endpoint。新的
[`f3-proper-root-endpoint-path-receipt-v1.json`](../data/interface-requests/f3-proper-root-endpoint-path-receipt-v1.json)
规定最小 payload：

1. admitted parent、scope、origin 与 root-entry identity；
2. \((p,r,A,K,R,h,z)\) root-chart 等式；
3. ordered \(L_0/L_1\) raw words、所有 node、shift/gcd replay；
4. parent、每个 prefix、endpoint 和 child 的 terminal-first receipts；
5. \(Q,\beta,E,D,D_*\) canonical maximality与 branch-specific valuation；
6. final target owner、E1--E5 receipt 与 shared re-entry。

在这个 receipt 被一个真实 producer 使用前，`source_path_digest` 只是一串引用，不能承担
E1。最优先的数学任务是选择一个可控子域（建议 TR1 dyadic-fresh 或 QC1 \(q_\perp\mid E\)），
证明 source-bound endpoint transcript 的存在并完成 first child 的 terminal-or-target dichotomy；
此后才有资格讨论 E3 admission。
