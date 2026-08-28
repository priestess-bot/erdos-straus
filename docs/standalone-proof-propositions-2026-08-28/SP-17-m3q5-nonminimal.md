# SP-17：\(m=3,q=5\) nonminimal 分支

**状态：** OPEN_PROPOSITION
**研究任务：** 闭合 \(m=3,q=5\) 横向域中 5-adic 非最小分支。
**独立性：** 本文件独立定义 q=5 valuation split 和闭合结果，不以其他命题为前提。

## 1. 自包含背景

状态 \(S\) 是带规范编码和 parent 谱系的整数元组
\((p,\varrho,R,K,A,h,D,E,\lambda)\)。定义
\[
p\equiv1\pmod{24},\quad p\text{ 为素数},\quad
\varrho,A,R,K,h,D,E\in\mathbb N_{>0},
\]
\[
g=\frac{p+1}{2},\qquad
T=p^2\varrho-g,\qquad
A=gT,\qquad K=A(p-1),
\]
\[
u=\gcd\left(2\varrho+1,\frac{p^2+p+1}{3}\right),
\qquad h=3u,\qquad 4K=pR+1,\qquad R-h>0,\qquad
DE=R-h,
\]
\[
D^\ast=\frac{D}{\gcd(D,h^2-1)}.
\]

这里 \(D,E\) 不由 \(\gcd(R-h,K)\) 定义。对每个素数 \(\ell\)，令
\(a_\ell=v_\ell(A)\)、\(k_\ell=v_\ell(K)\)、\(\zeta_\ell=v_\ell(R-h)\)，并规定
\[
\bigl(v_\ell(D),v_\ell(E)\bigr)=
\begin{cases}
(\zeta_\ell,0),&\zeta_\ell\le k_\ell,\\
(a_\ell,\zeta_\ell-a_\ell),&\zeta_\ell>k_\ell.
\end{cases}
\]

actual 表示 \(\lambda\) 从根或已验证前驱到达当前编码；terminal-first survivor 表示
一个在证明中明列的有限 terminal schedule 全部未给出 \(4/p\) 的正整数
三分母解。要求 \(p\equiv1\pmod{24}\) 为素数、\(2\le h<p\)、\(m=3\)、
\(5\mid D^\ast\)，并且一个在同一证明中明确构造的 q=5 transcript 已存在。
nonminimal 分支定义为

\[
v_5(T)\ge2.
\]

令 \(\mathscr Q_5\) 表示所有同时满足本节已列出的方程、\(2\le h<p\)、\(m=3\)、
\(5\mid D^\ast\)、actual、terminal-first survivor 和完整 q=5 transcript 条件的状态。
于是 nonminimal domain 是
\[
\mathscr N_5=\{S\in\mathscr Q_5:v_5(T)\ge2\}.
\]
候选 complementary minimal domain 定义为
\[
\mathscr M_5=
\{S\in\mathscr Q_5:
v_5(D^\ast)=v_5(T)=1,\qquad 5\nmid E.
\}.
\]
本命题必须证明 \(\mathscr Q_5=\mathscr N_5\dot\cup\mathscr M_5\)，并进一步证明
\[
v_5(T)\ge2
\Longleftrightarrow
\varrho\equiv\varrho_5(p)\pmod{25},
\qquad
\varrho_5(p)\equiv(p+1)(2p^2)^{-1}\pmod{25}.
\]
这里 \(p\ne5\)，故逆元存在。数值类 \(\varrho_5(p)=11\) 不是普遍事实；它当且仅当
\[
p\equiv11\ \text{或}\ 22\pmod{25}
\]
时成立。任何只讨论 \(\varrho\equiv11\pmod{25}\) 的子命题都必须把这个额外的
\(p\)-同余条件写进自己的量词域。

对任意整数 \(n\)，\(v_5(n)\) 表示 5 在 \(n\) 的素因子分解中的指数。
“primitive p-free child”表示 child 的所有必要分母与 multiplier 都不被 \(p\)
整除，并且其公共最大公因数已归一为 1。

q=5 transcript 是有限整数序列及逐步转换函数；其字母表、顺序、terminal prefixes
和 endpoint 必须在证明中完整给出。设 \(L_\omega\) 是 transcript 末端的 p-free
endpoint multiplier；它必须从 source 规范编码和确定 word 规则重算，不能由目标回推。
所有 candidate 仍须满足同一
\(4/p\) equation interface。

## 2. 待证明命题

对完整 nonminimal domain，证明一个互斥闭合：

\[
\boxed{
\mathscr N_5
=
\mathscr N_5^{+}\ \dot\cup\ \mathscr N_5^{-},
\qquad
\mathscr N_5^{+}=\{S\in\mathscr N_5:5\mid E\},
\qquad
\mathscr N_5^{-}=\{S\in\mathscr N_5:5\nmid E\},
}
\]

并且每一侧都满足：

* 若有 terminal-first hit，返回 TERMINAL；
* 若 \(5\mid E\)，构造 primitive p-free q=5 child，并证明其 E1--E5 和 re-entry；
* 若 \(5\nmid E\)，证明 terminal、FAMILY_EMPTY，或一个 physical final macro；
* 不得把 \(5\nmid E\) 仅记为“没有 q=5 fresh child”。

## 3. 必须从头建立的细节

1. nonminimal/minimal 两类的互斥和穷尽；
2. \(v_5(T)\ge2\) 与 \(\varrho\equiv\varrho_5(p)\pmod{25}\) 的等价关系，以及
   \(\varrho_5(p)=11\) 所需的 \(p\)-同余条件；
3. \(5\mid E\) 和 \(5\nmid E\) 的互补性；
4. primitive child 的整数性、p-free 性和 equation preservation；
5. nonfresh 分支的完整 terminal/empty/alternate partition；
6. target 分类、固定 E3、universal E4、fixed E5 与 re-entry。

## 4. 边界

不能把 minimal-q5 的定理套到 nonminimal branch；也不能把 finite \(5\)-adic
valuation check 当作整个 branch 的 terminal theorem。任何 arithmetic control 必须
标明是否 actual、是否有 predecessor 和 terminal certificate。

## 本文件中的 E-stage 词义

E1 绑定 nonminimal q=5 source；E2 固定两种 valuation 分支的 target；
E3 是证明中固定的 q=5 schema、分类和准入谓词；E4 是全称 equation lift；E5 是固定 \(\mathbb N^7\)
strict ticket；R 是 p-free child 或 final macro 的递归 re-entry。
七个势坐标必须是全部合法状态上的固定总函数，算法和顺序在证明中公布。

## 5. 负控和完成证据

必须包含 \(5\mid E\) 与 \(5\nmid E\) 各一个控制、\(\varrho\) swap、source-path swap、
nonminimal-as-minimal 误标和 p-free child 非 primitive 的拒绝。最终需要一个全 leaf
分割和独立 replay；否则只能登记为 valuation lemma。
