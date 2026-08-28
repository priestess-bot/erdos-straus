# SP-15：\(D^\ast\) fresh occurrence 与最小因子选择

**状态：** OPEN_PROPOSITION
**研究任务：** 在 low proper-root 横向域中完成先行终端菜单，并选择最小实际 fresh factor。
**独立性：** 本文件完整定义两个 m-domain、freshness、capacity 和选择规则，不依赖任何外部实现。

## 1. 完整背景

状态 \(S\) 是带规范编码和 parent 谱系的整数元组，至少包含
\((p,R,K,A,h,m,r,T,D,E,k)\)。actual 表示谱系从根或已验证前驱到达当前编码；
terminal-first survivor 表示一个在证明中完整列出的有限 terminal schedule 全部
未给出 \(4/p\) 的正整数三分母解。

设 \(p\equiv1\pmod{24}\) 为素数，且 \(S\) 满足：

\[
2\le h=3u<p,\qquad z=R-h=ED,\qquad D^\ast>1,\qquad k_\perp=1.
\]

还要求
\[
4K=pR+1,\quad K=A(p-1),\quad h\mid K,\quad
\gcd(h,z)=1,\quad D\mid K,\quad D\mid ph+1.
\]
在本文中“完整最大化正规化”精确定义为
\[
\bigl(v_\ell(D),v_\ell(E)\bigr)=
\begin{cases}
(\zeta_\ell,0),&\zeta_\ell\le k_\ell,\\
(a_\ell,\zeta_\ell-a_\ell),&\zeta_\ell>k_\ell,
\end{cases}
\quad
a_\ell=v_\ell(A),\quad k_\ell=v_\ell(K),\quad \zeta_\ell=v_\ell(z),
\]
对每个素数 \(\ell\) 成立。这确保 \(z=DE\)、\(D\mid K\)，但在
\(\zeta_\ell>k_\ell\) 时 \(D\) 的指数是 \(a_\ell\)，不是 \(k_\ell\)。
这不是一个来自外部过程的未定义操作。

固定
\[
D^\ast=\frac{D}{\gcd(D,h^2-1)},
\]
并令 \(D^\ast\) 的素因子按升序排列。定义
\[
k_\perp=\frac{k}{\prod_{\ell\mid h}\ell^{v_\ell(k)}}.
\]
条件 \(k_\perp=1\) 表示 \(k\) 的每个素因子都落在 h-support，而不是标签事实。

把定义域分成两个互斥部分：

\[
\mathscr D_4:m=3,\ 5\nmid D^\ast;
\qquad
\mathscr D_6:m>3.
\]

对每个 \(q\mid D^\ast\)，定义
\[
\delta=v_q(D),\quad \tau=v_q(K),\quad \zeta=v_q(z).
\]

完整 max-normalization 给出互补二分：

\[
\text{fresh}\Longleftrightarrow \zeta>\tau
\Longleftrightarrow q\mid E,
\]

\[
\text{saturated}\Longleftrightarrow \zeta\le\tau
\Longleftrightarrow q\nmid E.
\]

source-readable identity 可写为
\[
E=1+p\sigma,\qquad
\sigma D=2T-(m+2r).
\]

在选择 fresh factor 之前，必须优先执行所有 \(1<Q\mid u\) 的 terminal menus。
每个 menu 必须由证明者给出明确的 divisor/certificate 公式，并以固定升序执行；
仅写“检查 \(Q\)”不算定义。
至少，任何 Bradford 型 menu 都必须按下式明确：对
\(m_0\equiv3\pmod4\) 令 \(x=(p+m_0)/4\)，枚举全部 \(d\mid x^2\)，检查
\(m_0\mid px+d\) 的 Type-I 条件，或
\(d\le x,\ m_0\mid x+d\) 的 Type-II 条件，并直接重建三分母解。
至少要处理两个直接终端过滤器：

\[
q\mid(D^\ast,m),\ q\equiv3\pmod4
\Longrightarrow\text{Type-I terminal},
\]

\[
q\mid(D^\ast,m+2,2p+1),\ q\equiv5\pmod8
\Longrightarrow\text{Type-II terminal}.
\]

## 2. 待证明命题

对所有 actual \(S\in\mathscr D_4\cup\mathscr D_6\)，证明：

\[
\boxed{
\text{先行 terminal}
\ \lor\
\text{FAMILY\_EMPTY}
\ \lor\
\text{选择最小 fresh factor 的 VERIFIED\_SUCCESSOR}.
}
\]

选择规则必须是：固定 prime order，重放每个内部 terminal prefix，拒绝 saturated
factor，取最小具有独立 raw integer occurrence 的 fresh \(q\)。

一个 successor 必须包含：

1. **E1：** \(q\) 和其 consumed endpoint 在 actual source path 中出现；
2. **E2：** freshness、目标容量和 canonical endpoint 由确定规则计算；
3. **E3：** target 重新通过固定 schema、分类规则、合法语法和准入谓词；
4. **E4：** 全称 solution lift；
5. **E5：** fixed N\(^7\) 的最终严格比较；
6. **R：** target 回到同一状态宇宙并由同一选择规则再次消费。

## 3. \(W_y\) 宏的独立要求

若使用一个 prime word \(W_y\)，必须在本文中定义：

* prime 顺序；
* 每个内部 prefix 的 source payload；
* prefix terminal-first 调度；
* p-free 条件；
* fresh/saturated 的重新计算；
* atomic 与 single-side 的分支。

一个初始 MISS 不能证明所有后续 prefix 都 MISS。若内部 prefix 命中 terminal，
宏必须立即停止并返回 terminal。

## 4. 必须闭合的剩余

* \(\mathscr D_4\) 中 \(D,D^\ast\) 奇数导致的 dyadic-fresh 空子域；
* \(\mathscr D_6\) 的 \(q=3\) 与 \(q\mid m+2,2p+1\) 终端子域；
* fresh \(D^\ast\) factor 的真实 raw occurrence；
* saturated complement 的 empty/terminal/alternate 证明；
* dyadic full-capacity child 的 canonical lcm/rank 和 E5。

## 本文件中的 E-stage 词义

E1 绑定最小 fresh \(D^\ast\) factor 的实际 raw path；E2 固定 freshness/word target map；
E3 是两域各自固定的 target schema、分类和准入；E4 是全称 lift；E5 是
parent-to-final fixed \(\mathbb N^7\) 下降；R 是 target re-entry。
七个势坐标必须是全部合法状态上的固定总函数，算法和顺序在证明中公布。

## 5. 反例控制与完成证据

必须展示 fresh 与 saturated 各一个算术控制，并明确它们是否 actual。
需要完整 menu replay、least-factor uniqueness、source certificate、target E1--E5、
固定准入、re-entry 和独立 verifier。只证明
\(q\mid E\Longleftrightarrow\zeta>\tau\) 是 arithmetic partition，不是本命题闭合。
