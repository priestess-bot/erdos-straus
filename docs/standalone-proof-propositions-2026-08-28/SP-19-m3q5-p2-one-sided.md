# SP-19：\(m=3,q=5\) 的 \(p^2\) one-sided factor-pair leaf

**状态：** OPEN_PROPOSITION
**研究任务：** 闭合 \(m=3,q=5\) 最小分支中 \(L_\omega\equiv1\pmod{p^2}\) 的单侧因子系统。
**独立性：** 本文件完整给出 p2 factor-pair 系统和验收条件，不依赖其他文件。

## 1. 完整背景

状态 \(S\) 是带规范编码和 parent 谱系的整数对象。actual 表示由根或已验证前驱
到达；terminal-first survivor 表示明列的有限 terminal schedule 全部未给出
\(4/p\) 的正整数三分母解。persistent 表示状态满足固定合法性谓词并能被同一
选择规则再次消费。全文固定
\[
p\equiv1\pmod{24},\quad p\text{ 为素数},\quad
\varrho,R,K,A,h,D,E\in\mathbb N_{>0},\quad K=A(p-1),\quad4K=pR+1.
\]
minimal-q5 表示存在整数
\[
T=p^2\varrho-(p+1)/2,\qquad
D^\ast=D/\gcd(D,h^2-1),
\]
满足
\[
m=3,\quad2\le h<p,\quad5\mid D^\ast,\quad
v_5(T)=v_5(D^\ast)=1,\qquad5\nmid E,\qquad R-h=ED>0.
\]

complete-excess normalization 在本文中具有明确的本地定义：对每个素数 \(\ell\)，令
\(a_\ell=v_\ell(A)\)、\(k_\ell=v_\ell(K)\)、\(\zeta_\ell=v_\ell(R-h)\)，并取
\[
\bigl(v_\ell(D),v_\ell(E)\bigr)=
\begin{cases}
(\zeta_\ell,0),&\zeta_\ell\le k_\ell,\\
(a_\ell,\zeta_\ell-a_\ell),&\zeta_\ell>k_\ell.
\end{cases}
\]
特别地，\(D\) 不能被替换为 \(\gcd(R-h,K)\)。

末端有两个互素正整数 \(u,v\)。对
\(i\in\{u,v\}\)，相对于同一个 \(K\) 定义 maximal excess block
\[
Q_i=\prod_{\nu_\ell(i)>\nu_\ell(K)}\ell^{\nu_\ell(i)},\quad
\beta_i=i/Q_i,\quad g_i=\gcd(A,Q_i),
\]
\[
E_i=Q_i/g_i,\qquad D_i=\beta_i g_i.
\]
逐定义有
\[
u=E_uD_u,\qquad v=E_vD_v.
\]
定义
\[
M_\omega=\operatorname{lcm}(A,Q_u,Q_v)=AE_uE_v,\qquad
L_\omega=E_uE_v.
\]
本命题量词要求

\[
L_\omega=1+p^2\chi,\qquad \chi\ge1.
\]

endpoint 还必须满足
\[
R=u+v,\qquad 4K=p(u+v)+1.
\]

maximal factor-pair witness 必须满足

\[
E_uE_v=1+p^2\chi,
\]

\[
D_u,D_v\mid K,\qquad \gcd(D_u,D_v)=1,
\]

\[
D_u\mid pE_vD_v+1,\qquad
D_v\mid pE_uD_u+1.
\]

这里 p-free 表示每个相关整数与 \(p\) 互素；由
\(E_uE_v=1+p^2\chi\) 可知若因子为正且整除该乘积，则 p-divisibility 必须
在证明中显式排除或记录。one-sided leaf 定义为恰有一个 \(E_u,E_v\) 等于 1。
所有这些变量必须由上述 maximal 定义从 actual
endpoint 规范编码重算；单纯存在另一组因子分解不等于
occurrence。

## 2. 待证明命题

对 one-sided domain，证明：

\[
\boxed{
\text{terminal hit}
\ \lor\
\text{algebraic contradiction/FAMILY\_EMPTY}
\ \lor\
\text{final strict source-forward macro}.
}
\]

macro 在本文件中是一个有限、确定的 source-to-final-target 映射序列；只有首尾对象
可以持久化，中间对象不能独立递归。若使用 macro，必须构造一个新的、非中间对象的
target，并满足：

1. E2：由 \((E_u,E_v,D_u,D_v)\) 和冻结 tie-break 唯一确定；
2. E3：target 通过固定 persistent schema、分类和准入谓词；
3. E4：给出全称 equation lift；
4. E5：固定 N\(^7\) parent-to-final 严格下降；
5. R：target 重新属于同一状态宇宙并由同一规则消费。

本命题把 E1 作为显式假设：上述 maximal factor-pair 必须绑定 actual parent/path；
这个假设不蕴含 E2/E3/E5。

## 3. 必须处理的边界

* \(E_u=1\) 与 \(E_v=1\) 必须由对称规范唯一化；
* \(D_u,D_v\) 的互素性、正性和整除范围必须逐项证明；
* terminal-first 必须先于 p2 macro；
* \(L_\omega\) 的 \(p^2\) 表示不能被误读为 ordinary p-free endpoint；
* one-sided 不得偷换成 genuine two-sided。

## 4. 禁止的推理

~~~text
E_u E_v=1+p^2 chi 就自动给出 successor；
单边因子分解就是 E1；
把 canonical p2 rechart 当作 strict E5；
从有限 p 样本推出所有 one-sided leaf empty；
把中间对象的局部下降当作可入队 ticket。
~~~

这里 canonical p2 rechart 若被讨论，必须明确指
\[
\varrho'=\varrho+\chi T,\qquad
T'=L_\omega T,\qquad A'=AL_\omega,\qquad K'=KL_\omega.
\]
该 map 令 \(\varrho'>\varrho\) 且 \(K'/A'=p-1\)，所以不能仅凭其规范性
宣称 fixed E5。

## 本文件中的 E-stage 词义

E1 绑定 one-sided factor-pair 的 actual parent/path；E2 是唯一 final macro projection；
E3 是固定 p2 target schema、分类和准入；E4 是全称 lift；E5 是 fixed
\(\mathbb N^7\) strict parent-to-final ticket；R 是同一状态宇宙的 re-entry。
七个势坐标必须是全部合法状态上的固定总函数，算法和顺序在证明中公布。

## 5. 完成证据

需要 one-sided 全域分类、terminal/contradiction/macro 证明、完整 E2/E3/E4/E5、
固定 admission、re-entry、独立 replay，以及左右交换、source swap、p2-to-p
误标和 upward-rank 负控。
