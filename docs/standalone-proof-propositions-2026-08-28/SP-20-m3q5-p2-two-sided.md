# SP-20：\(m=3,q=5\) 的 genuine two-sided \(p^2\) leaf

**状态：** OPEN_PROPOSITION
**研究任务：** 闭合 \(m=3,q=5\) 最小分支中 \(L_\omega\equiv1\pmod{p^2}\) 的 genuine two-sided 因子系统。
**独立性：** 本文件独立定义 genuine two-sided p2 曲面、canonical rechart 和闭合目标。

## 1. 自包含背景

状态 \(S\) 是带规范编码和 parent 谱系的整数对象。actual 表示由根或已验证前驱
到达；terminal-first survivor 表示明列的有限 terminal schedule 全部未给出
\(4/p\) 的正整数三分母解。minimal-q5 表示存在
\[
p\equiv1\pmod{24},\quad p\text{ 为素数},\quad
\varrho,R,K,A,h,D,E\in\mathbb N_{>0},\quad K=A(p-1),\quad4K=pR+1,
\]
以及
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

末端有互素正整数 \(u,v\)。相对于同一个
\(K\)，对 \(i\in\{u,v\}\) 定义
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
于是
\[
M_\omega=\operatorname{lcm}(A,Q_u,Q_v)=AE_uE_v,\qquad
L_\omega=E_uE_v.
\]
本命题要求

\[
L_\omega=1+p^2\chi,\qquad \chi\ge1.
\]

\[
R=u+v,\qquad 4K=p(u+v)+1,
\]

\[
D_u,D_v\mid K,\quad\gcd(D_u,D_v)=1,
\]

\[
D_u\mid pE_vD_v+1,\qquad
D_v\mid pE_uD_u+1.
\]

所有这些变量必须由上述 maximal 定义从 actual endpoint 规范编码重算。
这里所有 \(E_u,E_v,D_u,D_v\) 都是正整数；p-free 表示与 \(p\) 互素，
primitive 表示相应两端的公共 gcd 已被除去。genuine two-sided leaf 要求

\[
E_u>1,\qquad E_v>1,\qquad
E_uE_v=1+p^2\chi.
\]

在原始 K 归一化下，定义 direct canonical p2 rechart：
\[
\varrho'=\varrho+\chi T,\quad
T'=L_\omega T,\quad A'=AL_\omega,\quad K'=KL_\omega.
\]
它保留 cofactor \(K'/A'=p-1\)，且 \(\varrho'>\varrho\)，所以不能自动提供
fixed N\(^7\) 严格票，也不能直接作为后继。

## 2. 待证明命题

对整个 genuine two-sided domain，证明：

\[
\boxed{
\text{terminal}
\ \lor\
\text{FAMILY\_EMPTY}
\ \lor\
\text{新的 source-preserving final atomic macro with strict E5}.
}
\]

macro 在本文件中是一个有限确定映射序列，只有 source 和 final target 可持久化。
新的 macro 必须不是上述 increasing canonical rechart 的重命名；必须明确：

1. E1：\(E_u,E_v,D_u,D_v\) 和 parent path 的实际来源；
2. E2：最终 atomic target 的唯一投影和 tie-break；
3. E3：固定 schema、分类、normal form、合法语法和准入谓词；
4. E4：对全部目标解的 universal lift；
5. E5：parent-to-final fixed N\(^7\) 严格下降；
6. R：target 重新进入同一个状态宇宙并由相同规则再次消费。

## 3. 必须先完成的分类

1. terminal-first 命中必须在 p2 endpoint 暴露前终止；
2. one-sided 与 two-sided 必须由 \(E_u,E_v\) 的 exact inequalities 互斥分开；
3. p-free、primitive、正性和互素条件必须完整；
4. strict final overflow 与 increasing canonical rechart 必须分开；
5. malformed/nonactual controls 必须被拒绝，而不是进入数学量词。

## 4. 关键负控

~~~text
把 increasing c=p-1 rechart 当作 E5；
把 two-sided factor pair 当作 actual source；
把任一中间 multiplier checkpoint 写入持久队列；
把 one-sided proof 复制到 two-sided；
把 finite p2 search 的无命中写成 FAMILY_EMPTY。
~~~

## 本文件中的 E-stage 词义

E1 绑定 genuine two-sided factor pair 与 actual parent；E2 是新的 source-preserving
atomic target map；E3 是固定 schema、分类、语法和准入谓词；E4 是全称解提升；
E5 是固定 \(\mathbb N^7\) parent-to-final 严格下降；R 是目标重新进入同一状态宇宙。
七个势坐标必须是全部合法状态上的固定总函数，算法和顺序在证明中公布。

## 5. 完成证据

需要 two-sided 参数曲面的完整 terminal/empty/new-macro 分割、source-bound certificate、
独立 target map、E2/E3/E4/E5、固定 admission、re-entry 和对 canonical
increasing map 的严格反证。完成前该 leaf 必须保持 OPEN。
