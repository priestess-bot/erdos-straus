# SP-12：high stutter \(k=1\) Pell 残差

**状态：** OPEN_PROPOSITION
**研究任务：** 闭合高根 stutter 的 \(k=1\) Pell 型整数曲面。
**独立性：** 本文件重新定义 high stutter 曲面和 Pell 参数；所有量词与对象均在本文给出。

## 1. 独立背景

状态带唯一规范编码和 parent 谱系。actual 表示由根或已验证前驱到达；persistent 表示
通过固定合法性谓词。terminal-first MISS 表示一个明列的有限 terminal schedule
全部未给出 \(4/p\) 的正整数三分母解。

定义 high proper-factor root：

\[
p\equiv1\pmod{24},\quad p\text{ 为素数},\quad r\in\mathbb N_{>0},\quad
C_0=p^2+p+1,\quad M_0=C_0/3,\quad
u=\gcd(2r+1,M_0),\quad h=3u>p,
\]

\[
g=(p+1)/2,\quad T=p^2r-g,\quad A=gT,\quad K=A(p-1),
\quad R=2p^3r-p^2-2pr-p+1,\quad z=R-h=ED.
\]

量词还要求
\[
0<u<M_0,\quad h\mid K,\quad\gcd(h,z)=1,\quad
D\mid K,\quad D\mid ph+1,\quad D,E>0.
\]
“actual maximal”在本文中没有隐藏算法含义。对每个素数 \(\ell\)，令
\(a_\ell=v_\ell(A)\)、\(k_\ell=v_\ell(K)\)、\(\zeta_\ell=v_\ell(z)\)，并按
\[
\bigl(v_\ell(D),v_\ell(E)\bigr)=
\begin{cases}
(\zeta_\ell,0),&\zeta_\ell\le k_\ell,\\
(a_\ell,\zeta_\ell-a_\ell),&\zeta_\ell>k_\ell
\end{cases}
\]
唯一计算 \(D,E\)。这确保 \(z=DE\)、\(D\mid K\)，而且当
\(\zeta_\ell>k_\ell\) 时 \(D\) 不可被替换为 \(\gcd(z,K)\)。

假设 source actual、terminal-first MISS、canonical cofactor
\[
c=\langle D(h-1)^{-1}\rangle_p=p-1.
\]

令
\[
m=\frac{D+h-1}{p},\qquad e=\frac{ph+1}{D},\qquad a=em-h,\qquad b=e-1.
\]

本命题所称的 \(k=1\) 曲面把下列关系作为显式量词条件：

\[
a>e,\qquad
N=a^2-ab+b^2=hk,
\]

且 \(k\) 为奇数。本命题取 \(k=1\)，所以 \(h=N\)。证明者必须从本节已列的
high-root 方程导出这些关系；“stutter”只是此显式曲面的简称，不是可外引的引理。

曲面的因子化参数部分要求存在正整数 \(d,x,y\)，满足：

\[
e=dx^2,\qquad a=dxy-1,\qquad \gcd(x,y)=1,\qquad y>x,
\]

\[
d\equiv2\pmod3,\qquad 3\nmid x,\qquad3\mid y.
\]

还要求存在 \(\gamma\in\mathbb N_{>0}\)，使
\[
y^2+xy-x^2=\gamma(dxy-1),
\qquad \gamma\equiv1\pmod3.
\]

置 \(Q=x^2-xy+y^2\)，则

\[
m=dQ-1,\qquad
h=d^2x^2Q-dx(x+y)+1,
\]

\[
p=
\frac{d^3x^4Q-d^2x^3(x+y)+1}{dxy-1}.
\]

从前述 high-root 条件导出该因子化也是本命题的证明义务。上述方程共同定义完整的
high \(k=1\) Pell 型整数曲面；它们不自动定义
actual root、terminal MISS 或合法递归状态。

## 2. 待证明命题

对所有满足上述曲面方程、核心素数、proper-factor maximality、terminal-first MISS
和 actual persistent source 条件的 tuple，证明：

\[
\boxed{
\text{每个 tuple 是 TERMINAL、FAMILY\_EMPTY，或产生完整 high successor。}
}
\]

更具体地，任何 successor 必须提供：

* 从 actual source 规范编码读取 \((d,x,y)\) 的 E1；
* 无 oracle 的确定 E2；
* high-only 固定 schema、分类和准入 E3；
* 对全部 \(\mathsf{Sol}(T)\) 成立的 E4；
* 固定 N\(^7\) parent-to-final E5；
* 重新进入 high selector 的 R。

若无法构造 successor，则必须证明整个剩余 Pell 曲面在精确 high domain 中为空，
或给出完整 terminal certificate。

## 3. 关键非递归任务

证明者必须在以下路线中至少完成一条：

1. 定义一个由当前 tuple 唯一计算的 canonical-D 子进程，并证明某个完整 valuation
   predicate 在该子进程下 nonrecurrent；
2. 证明所有 surviving tuple 都落入一个已验证 terminal family；
3. 构造一个 high-only source-forward successor，并完成 E1--E5/R。

不能使用 low domain 中 \(a<e\)、\(y<x\) 或 low \(k=1\) Vieta descent；
本命题的基本方向是 \(a>e\)。

## 4. 必须保留的边界控制

例如 \((d,x,y)=(11,101,1020)\) 产生一个整式商为核心素数的 shadow，
但其 shadow divisor 不一定是 actual maximal certificate，且可能被 gap-3 terminal
抢先。该类例子必须作为“曲面点不等于 actual state”的负控。

还要构造一个形式 root-lift subprogression，检验仅凭两个 divisor gates、
canonical D 和只依赖某个明确定义不变量 \(\Theta\) 的有限 terminal menu 不能推出空性。

## 本文件中的 E-stage 词义

E1 是从 actual high source 编码读取 Pell tuple；E2 是无 oracle 的 terminal/successor
projection；E3 是证明中固定的 high-only schema、分类和准入；E4 是全称 lift；E5 是 fixed
\(\mathbb N^7\) parent-to-final descent；R 是 high selector re-entry。
E5 中的七个坐标是全部合法状态上的固定总函数，算法和顺序必须在证明中公布。

## 5. 完成证据

提交 high 曲面上的参数化证明、terminal/empty/successor 三分割、所有 source-path
和 target certificates、固定 E5、re-entry 及独立反控。有限曲面样本或 Pell 参数式本身
不算 closure。
