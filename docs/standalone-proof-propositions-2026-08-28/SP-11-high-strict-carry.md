# SP-11：high strict-carry 的 source-forward 闭合

**状态：** OPEN_PROPOSITION
**研究任务：** 对所有满足明确高根条件且 canonical cofactor 严格的状态构造终端、空域或完整严格后继。
**独立性：** 本文件完整给出 high root 的数论定义和 E-stage 目标，不使用未重述的主张。

## 1. 独立背景

本文件中的状态是带唯一规范编码和 parent 谱系的整数元组；actual 表示谱系从根或
已验证前驱逐步到达当前编码；persistent 表示状态满足固定合法性谓词并可再次递归。
terminal-first 表示一个在证明中完整列出的有限 terminal predicate 列表全部 MISS；
terminal certificate 是 \(4/p\) 的正整数三分母解。

设 \(p\equiv1\pmod{24}\) 为素数，\(C_0=p^2+p+1\)，
\(M_0=C_0/3\)。取正整数 \(r\)，令

\[
u=\gcd(2r+1,M_0),\qquad h=3u,\qquad v=M_0/u.
\]

只考虑满足

\[
0<u<M_0,\qquad h>p,\qquad 2\le v\le p-1
\]

的 proper-factor high root。用

\[
g=\frac{p+1}{2},\quad T=p^2r-g,\quad A=gT,\quad K=A(p-1),
\]

\[
R=2p^3r-p^2-2pr-p+1
\]

表示根容量图表，并设
\[
z=R-h=ED,\qquad h\mid K,\qquad (h,z)=1,\qquad D\mid K,\qquad D\mid ph+1.
\]

本文中“actual maximal complete-excess normalization”由下列逐素数公式**定义**。对每个
素数 \(\ell\)，令
\[
a_\ell=v_\ell(A),\qquad k_\ell=v_\ell(K),\qquad \zeta_\ell=v_\ell(z),
\]
并规定
\[
\bigl(v_\ell(D),v_\ell(E)\bigr)=
\begin{cases}
(\zeta_\ell,0),&\zeta_\ell\le k_\ell,\\
(a_\ell,\zeta_\ell-a_\ell),&\zeta_\ell>k_\ell.
\end{cases}
\]
这确保 \(z=DE\) 且 \(D\mid K\)；\(D\mid ph+1\) 是本命题 source domain 的额外
算术条件。特别地，当 \(\zeta_\ell>k_\ell\) 时，\(D\) 的指数是 \(a_\ell\)，而不是
\(k_\ell\)，所以不能把此正规化替换为 \(\gcd(z,K)\)。

source 必须满足上述 actual/persistent 定义，并已经通过 terminal-first schedule。
定义 canonical cofactor

\[
c=\left\langle D(h-1)^{-1}\right\rangle_p
\in\{1,\ldots,p-1\}.
\]

本命题的 strict-carry 分支是 \(c\le p-2\)。

## 2. 已知的可独立推导

由 \(h=C_0/v\) 和 \(h>p\) 可得 \(\delta=h-p-1>0\)；
由 \(p\nmid C_0\) 可得 \(2\le v\le p-1\)。在 strict 分支定义

\[
M_{\rm ex}=\operatorname{lcm}(A,Q)=AE,\qquad
K_{\rm ex}=M_{\rm ex}c,\qquad
R_{\rm ex}=\frac{4M_{\rm ex}c-1}{p},
\]

其中 \(Q\) 定义为相对于 \(K\) 的完整超容量块：
\[
Q=\prod_{\nu_\ell(z)>\nu_\ell(K)}\ell^{\nu_\ell(z)},
\qquad z=R-h,
\]
乘积遍历所有素数 \(\ell\)。它必须由 source payload 的完整素因子赋值重放，而不是由目标
反推。根图表的大小不等式给出 \(R_{\rm ex}>p\)，所以目标属于 high
TYPE-I/OVERFLOW，而不是 low chart。

为使分解完全确定，令
\[
g_A=\gcd(A,Q),\qquad E=Q/g_A,\qquad
D=(z/Q)g_A.
\]
于是 \(z=ED\)、\(D\mid K\)，并且 \(M_{\rm ex}=\operatorname{lcm}(A,Q)=AE\)。

两端都代表同一个解集时，候选 E4 是恒等映射；但这只解决算术 lift，不解决
target 分类、固定合法语法、admission、re-entry。

## 3. 待证明命题

对每一个 actual high strict-carry source，证明以下三分割：

\[
\boxed{
\mathscr H_{\rm strict}
=\mathscr T\ \dot\cup\ \mathscr E\ \dot\cup\ \mathscr V,
}
\]

其中 \(\mathscr T\) 是 target 或 source 的直接 terminal，
\(\mathscr E\) 是精确 high domain 上的 family-empty，
\(\mathscr V\) 是满足以下全部条件的 source-forward successor：

1. **E1：** \(D,E,Q\) 和 strict carry 所需的整数均出现在 actual parent payload；
2. **E2：** \(M_{\rm ex},K_{\rm ex},R_{\rm ex}\) 唯一确定；
3. **E3：** target 通过固定 persistent schema、normal form、分类、合法语法和 admission；
4. **E4：** \(\mathsf{Sol}(T)\to\mathsf{Sol}(S)\) 的恒等或明确 lift 对全部解成立；
5. **E5：** 固定 \(\Pi\in\mathbb N^7\) 的 parent-to-final 比较严格下降；
6. **R：** target 重新进入同一个 high/overflow selector domain。

## 4. 证明者必须补出的细节

* 证明 \(Q\) 的定义与选取次序，不得把任意超容量因子当作 Q；
* 证明 \(M_{\rm ex}\) 的所有整除、同余、范围和正性条件；
* 证明 target terminal-first 在 E3 前执行；
* 证明 target 分类不由后继构造自报，而由固定分类函数重算；
* 证明 strict E5 比较最终 target，而非某个中间 carry；
* 证明 high domain 的 source-to-target path 连续。

## 5. 反例和禁用推理

~~~text
只从 c<=p-2 推出“已经是 successor”；
把 identity lift 的名称当成 E4 证明；
把 local charged rank drop 当成 fixed N^7 E5；
把 low-height k 或 D* 定理用于 h>p；
从 arithmetic shadow 反推 actual parent；
忽略 single-side 或 atomic third-step target。
~~~

## 本文件中的 E-stage 词义

E1 绑定 actual maximal \(D,E,Q\)；E2 计算唯一 \(M_{\rm ex},K_{\rm ex},R_{\rm ex}\)；
E3 通过证明中固定的 high-overflow schema、分类函数和准入谓词；E4 是全称 solution lift；
E5 是 fixed \(\mathbb N^7\) 的 parent-to-final strict ticket；R 是 high selector re-entry。
E5 中的七个坐标是全部合法状态上的固定总函数，算法和顺序必须在证明中公布。

## 6. 完成证据

需要一份 high-only 代数证明、source-path certificate、target terminal/分类/E3、
universal E4、fixed E5、re-entry trace 和独立 replay。若只证明 \(R_{\rm ex}>p\)
或算出 \(c\)，命题仍未完成。
