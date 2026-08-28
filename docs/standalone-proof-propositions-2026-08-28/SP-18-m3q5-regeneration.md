# SP-18：\(m=3,q=5\) regeneration 到 p-free failure 的闭合

**状态：** OPEN_PROPOSITION
**研究任务：** 证明 q=5 最小分支中的 regeneration 过程必然终止于直接解、空域或严格后继。
**独立性：** regeneration、终止势和 p-free failure 均在本文件中定义；没有未明示的外部前提。

## 1. 独立背景

状态 \(S\) 是带规范编码和 parent 谱系的整数对象。actual 表示由根或已验证前驱
到达。设
\[
p\equiv1\pmod{24},\quad p\text{ 为素数},\quad
\varrho,R,K,A,h,D,E\in\mathbb N_{>0},\quad
g=(p+1)/2,\quad T=p^2\varrho-g,\quad A=gT,\quad K=A(p-1),\quad4K=pR+1,
\]
\[
D^\ast=D/\gcd(D,h^2-1),\quad
m=3,\quad2\le h<p,\quad R-h=ED>0,
\quad5\mid D^\ast,\quad
v_5(D^\ast)=v_5(T)=1,\quad 5\nmid E.
\]
对每个素数 \(\ell\)，令 \(a_\ell=v_\ell(A)\)、\(k_\ell=v_\ell(K)\)、
\(\zeta_\ell=v_\ell(R-h)\)，并由
\[
\bigl(v_\ell(D),v_\ell(E)\bigr)=
\begin{cases}
(\zeta_\ell,0),&\zeta_\ell\le k_\ell,\\
(a_\ell,\zeta_\ell-a_\ell),&\zeta_\ell>k_\ell
\end{cases}
\]
唯一确定 \(D,E\)。这一定义是 complete-excess normalization；它不是
\(\gcd(R-h,K)\) 的别名。
这些等式定义本文件所谓 minimal-q5 domain。nonterminal 表示明列的 finite
terminal schedule 全部未给出 \(4/p\) 的正整数三分母解。

证明输入还必须构造一个 finite prefix 和一个 p-free word：它们都是有限整数序列，
每一步由公布的确定函数从前一步计算，并在每个内部 prefix 重新执行 terminal schedule。
经过该 word 后得到

\[
L_\omega=1+p\theta_\omega,\qquad
\theta_\omega\equiv1\pmod p.
\]

本文件中 p-free 表示 \(\gcd(p,n)=1\)。endpoint payload 至少包含
\(p,L_\omega,\theta_\omega\)、当前 source 规范编码、已消耗 word、剩余 valuation
和 equation-preserving 分母数据；缺少任一字段的对象不属于本命题量词。

regeneration 是一个必须显式给出公式的确定变换
\[
\mathcal R:\text{endpoint payload}\longrightarrow\text{next endpoint payload}.
\]

它应保持 \(4/p\) equation interface、primitive 条件和 source lineage，并消耗一个
可记录的 valuation/word 位。若最终 payload 不能满足 p-free 条件，称为
p-free failure。

## 2. 待证明命题

对所有 \(\theta_\omega\equiv1\pmod p\) 的 actual endpoint，证明：

\[
\boxed{
\text{有限 regeneration countdown}
\Longrightarrow
\text{TERMINAL}
\ \lor\
\text{FAMILY\_EMPTY}
\ \lor\
\text{one parent-to-final paid macro}.
}
\]

其中“有限”必须由一个明确的自然数势（例如剩余 valuation、word length 或
固定 N\(^7\) 外层坐标）证明，而不能只凭观察。

若 regeneration 产生 successor，必须同时提供：

* E1：每个 regeneration step 都从前一步实际 payload 读取；
* E2：\(\mathcal R\) 和 tie-break 唯一；
* E3：最终 target 的固定 schema、分类和准入谓词；
* E4：对全部目标解的 lift；
* E5：parent-to-final 的固定 N\(^7\) 严格下降；
* R：最终 target re-entry。

## 3. 必须排除的循环

* \(\theta_\omega=1\) 反复再生而不降低任何固定坐标；
* 中间 p-free-looking endpoint 被当作最终 target；
* regeneration 失败只被记录为 pending；
* 从另一个 residue \(\theta=-1\) 的 strict 证明直接推断 \(\theta=1\)；
* 用 local valuation countdown 替代最终 E5。

## 本文件中的 E-stage 词义

E1 绑定每一步 regeneration 的前驱 payload；E2 是确定 regeneration map；
E3 是最终 target 的固定 typing/admission；E4 是全称 lift；E5 是 parent-to-final
\(\mathbb N^7\) 严格下降；R 是最终 target re-entry。
七个势坐标必须是全部合法状态上的固定总函数，算法和顺序在证明中公布。

## 4. 完成证据

需要 regeneration 公式、终止势、p-free failure 的精确定义、terminal/empty/macro
三分割、source-bound continuous certificate、fixed E5、固定 admission、re-entry
以及非终止循环负控。只证明某个有限样本会失败，不构成命题证明。
