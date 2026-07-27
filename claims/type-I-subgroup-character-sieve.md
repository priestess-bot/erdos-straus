---
kind: claim
claim_id: type-I-subgroup-character-sieve
title: Type I 子群型失败的半维跨缺口筛界
statement: 对任意有限个互异合法缺口 \(\mathcal M\)，令 \(R_{\mathcal M}^{sub}(X)\) 计数 \(p\le X\)、\(p=1\bmod24\) 的素数，使每个 \(m\in\mathcal M\) 都属于 Type I 子群型失败（即 \(-1/4\) 不在 \(x_m\) 的素因子残数生成子群）。则 \(R_{\mathcal M}^{sub}(X)\ll_{\mathcal M}X/(\log X)^{1+|\mathcal M|/2}\)。更一般地，若第 m 个见证字符像阶至少 \(h_m\)，则该缺口贡献至少 \(1-1/h_m\) 个筛维。
claim_status: established
topics:
- type-I
- characters
- sieve
- residual-set
- moving-window
- proof-program
sources:
- paper: elsholtz_tao2013
  locator: Appendix A, shifted-prime additive functions and sieve estimates
  role: upper-bound-sieve-methodology
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-divisor-criterion
visibility: public
last_checked: '2026-07-25'
---

# Type I 子群型失败的半维跨缺口筛界

## 定理

令 \(\mathcal M\) 是有限个互异合法缺口 \(m\equiv3\pmod4\) 的集合，并写

\[
x_m=\frac{p+m}{4}.
\]

令 \(R_{\mathcal M}^{sub}(X)\) 计数所有 \(p\le X\)、\(p\equiv1\pmod{24}\) 的素数，
满足对每个 \(m\in\mathcal M\)

\[
-\frac14\notin
\left\langle q\bmod m:q\mid x_m\right\rangle. \tag{1}
\]

则

\[
R_{\mathcal M}^{sub}(X)
\ll_{\mathcal M}
\frac{X}{(\log X)^{1+|\mathcal M|/2}}. \tag{2}
\]

更一般地，若在每个位置可选的分离字符像阶至少为 \(h_m\ge2\)，则

\[
R_{\mathcal M}^{sub}(X)
\ll_{\mathcal M}
\frac{X}{(\log X)^{1+\sum_{m\in\mathcal M}(1-1/h_m)}}. \tag{3}
\]

## 证明

由 [Type I 子群--字符分流](type-I-subgroup-character-obstruction.md)，(1) 给出一个
非平凡字符 \(\chi_m\)，使全部 \(q\mid x_m\) 都落在

\[
K_m=\ker\chi_m\subset U(m). \tag{4}
\]

若 \(\chi_m\) 的像阶为 \(h_m\)，则允许的单位残数比例恰为 \(1/h_m\)，至多为 \(1/2\)。
固定有限个字符选择后，\(x_m\) 的每个非固定素因子都被限制在这个固定残数子集。

令 \(p=24t+1\)、\(m=4j-1\)。去掉固定公因子 \(g_m=(6,j)\) 后，相关原始线性式为

\[
L_m(t)=\frac6{g_m}t+\frac j{g_m}. \tag{5}
\]

不同 \(m\) 给出的 \(L_m\) 两两不成比例；任何共同根只来自有限个整除它们行列式的
素数。因此，对固定的角色核选择，Elsholtz--Tao 附录 A 的移位整数 Selberg 上界筛
逐项给出局部禁根贡献 \(1-1/h_m\)。同时要求 \(p=24t+1\) 为素数提供基准筛维 1，
于是得到 (3)。每个 \(m\) 的字符选择有限，对全部选择求和只改变隐含常数，取
\(h_m\ge2\) 即得 (2)。

## 含义与边界

该结论无条件地说明：若不断加入固定缺口，而残余在每个新缺口都保持子群型失败，则
残余可压至任意对数幂稀薄。

它不证明残余为空，原因有二：

- 角色条件可在有限多个模数上通过 CRT 兼容；
- 有限积集型失败不受本筛界控制。

所以这条筛界应与三余类饱和判据配合：字符型部分获得定量稀薄性，积集型部分则需要
碰撞因子指数或私有商阶的结构性闭合。

这种边界并非抽象可能性。在
[Type I 自适应逃逸深度剖面](type-I-adaptive-escape-seed-profile.md) 中，种子
\(p=806521\) 的局部可采纳一私有素因子链可条件性逃过前 23 个缺口
\(3,7,\ldots,91\)，并且 23 个位置全部属于子群型，积集型计数为零；它在下一个
\(m=95\) 才关闭。因此即使纯字符型残余已具有任意对数幂的平均稀薄性，也不能把该
筛界升级为任一固定窗口的逐点覆盖。

这个闭合也说明完整饱和不是唯一出口：在该链的 \(m=95\) 转换中，
\(E=306\)、私有残数 \(r=89\)、目标 \(t=71\)，而

\[
4r\equiv71\pmod{95},\qquad 4\mid E^2. \tag{8}
\]

故尚未满足 \(\Pi_{95}(E^2)=K\) 时，三个平移之一也可直接命中目标。对点态证明，
这意味着除了强制饱和，还应追踪目标在受限三平移积集中的位置。
