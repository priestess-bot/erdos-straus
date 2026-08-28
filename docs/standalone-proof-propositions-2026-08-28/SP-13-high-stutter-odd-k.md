# SP-13：high stutter 奇数 \(k\ge3\) 残差

**状态：** OPEN_PROPOSITION
**研究任务：** 闭合高根 stutter 的全部奇数 \(k\ge3\) 参数域。
**独立性：** 本文件自包含 high-domain 参数、奇数 k 分支和 closure evidence；无隐含外部输入。

## 1. 自包含背景

状态带唯一规范编码和 parent 谱系。actual 表示由根或已验证前驱到达；
terminal-first MISS 表示明列的有限 terminal schedule 全部未给出
\(4/p\) 的正整数三分母解。

设 \(p\equiv1\pmod{24}\) 为素数、\(r\in\mathbb N_{>0}\)，取 high proper-factor
actual root：

\[
C_0=p^2+p+1,\quad M_0=C_0/3,\quad
u=\gcd(2r+1,M_0),\quad h=3u>p,
\]

\[
g=(p+1)/2,\quad T=p^2r-g,\quad A=gT,\quad K=A(p-1),
\quad R=2p^3r-p^2-2pr-p+1,\quad z=R-h=ED.
\]

要求 \(0<u<M_0\)、\(h\mid K\)、\((h,z)=1\)、\(D\mid K\)、\(D\mid ph+1\)，
source 经过 terminal-first MISS，并且
\[
c=\langle D(h-1)^{-1}\rangle_p=p-1.
\]

\(D,E\) 由如下逐素数规则唯一计算：令
\(a_\ell=v_\ell(A)\)、\(k_\ell=v_\ell(K)\)、\(\zeta_\ell=v_\ell(z)\)，并取
\[
\bigl(v_\ell(D),v_\ell(E)\bigr)=
\begin{cases}
(\zeta_\ell,0),&\zeta_\ell\le k_\ell,\\
(a_\ell,\zeta_\ell-a_\ell),&\zeta_\ell>k_\ell.
\end{cases}
\]
不得任取满足同余的 shadow divisor，也不能把这一规则简化成 \(\gcd(z,K)\)。

令 \(e=(ph+1)/D\)、\(a=em-h\)、\(b=e-1\)，其中
\(D=mp+1-h\)。本命题的奇数 \(k\) 曲面将下列关系作为显式量词条件：

\[
N=a^2-ab+b^2=hk,
\qquad k\ \text{为奇数}.
\]

本命题只考虑 \(k\ge3\) 的奇数。还必须保留
\[
m\ge3,\qquad m\mid a+3u,\qquad
u\mid (am)^2+(am)(m-a)+(m-a)^2.
\]

这些是 high-only 参数门，不是 low-height 结论。证明者必须从本节写出的 high-root
条件导出曲面关系和参数门；不能以“高域恒等式”这一名称替代推导。

## 2. 待证明命题

对完整 actual \(k\ge3\) domain，证明：

\[
\boxed{
\mathscr H_{k\ge3}
=\mathscr T\ \dot\cup\ \mathscr E\ \dot\cup\ \mathscr V,
}
\]

其中 \(\mathscr T\) 为 terminal、\(\mathscr E\) 为 exact-domain empty、
\(\mathscr V\) 为 high-only verified successor。

对 \(\mathscr V\)，必须逐项构造：

* actual maximal certificate 和 raw high occurrence（E1）；
* deterministic high target map（E2）；
* 固定 high normal form、分类和 admission（E3）；
* universal lift（E4）；
* 固定 N\(^7\) 严格 parent-to-final ticket（E5）；
* high selector re-entry（R）。

## 3. 必须获得的高域定理

至少需要以下之一：

1. 一个对所有 odd \(k\ge3\) 有效且 nonrecurrent 的 valuation predicate；
2. 一个完整 terminal dichotomy，覆盖所有高域参数；
3. 一个 source-lineage 后继构造，将每个剩余参数确定地送至合法 target。

任何使用 low \(k=1\)、low \(D^\ast\)、Eisenstein quotient 或 low-height inequality
的证明，都必须重新检查其假设；不能仅因符号相似而移植。

## 4. 反例控制

需要保留一个形式的 root-lift 无限子进程，使
divisor gates、canonical D、root-bottom MISS 和 Theta-only menus 都继续成立。
这证明静态 gates 不能单独限制 \(k\)。

还要拒绝：

~~~text
把 odd k>=3 当作“有限剩余”却不给界；
用有限搜索宣称 family empty；
用 low-height successor 代替 high occurrence；
把 canonical D 或 divisor gate 当作 E1；
把中间 high rechart 当作 E5。
~~~

## 本文件中的 E-stage 词义

E1 绑定 actual \(k\ge3\) source occurrence；E2 选择唯一 high target map；
E3 通过证明中固定的 high schema、分类、语法和准入谓词；E4 是全称 equation lift；
E5 是固定 \(\mathbb N^7\) 的最终严格下降；R 是 high-domain re-entry。
七个势坐标必须是全部合法状态上的固定总函数，算法和顺序在证明中公布。

## 5. 完成证据

需要 high-only 全称证明或完整参数化 partition、独立 source/target replay、E1--E5、
固定势和 re-entry。若只能得到“尚未找到反例”，命题仍保持 OPEN。
