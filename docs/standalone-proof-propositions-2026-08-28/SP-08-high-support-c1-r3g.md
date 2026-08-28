# SP-08：high-support \(C=1\) 的 \(R=3\)-G 分支

**状态：** OPEN_PROPOSITION
**研究任务：** 对高支撑 \(C=1\) hard-core 参数域证明终端、空域或非上升严格后继的全称三分割。
**独立性：** 所有变量、hard-core 条件和闭合目标均在本文件中给出，没有隐含外部前提。

## 1. 自包含背景

设 \(p\equiv1\pmod{24}\) 为素数，令
\(B_p=(p-1)^2/4\)。Type-I high-support state 是带规范编码和 parent 谱系的
\((p,R,K,A,C,\phi)\)，满足

\[
4K=pR+1,\qquad R>p,\qquad K=AC,\qquad A>B_p,\qquad C=1.
\]

协议相位集合固定为
\[
\{\mathrm{CHARGED},\mathrm{PRE},\mathrm{ABSORB},\mathrm{RESET}\},
\]
并固定顺序
\[
\mathrm{CHARGED}>\mathrm{PRE}>\mathrm{ABSORB}>\mathrm{RESET}.
\]
从 ABSORB 回到 CHARGED 只有在更高优先级的自然数势坐标严格下降时才允许。
actual 表示 \(\phi\) 是从根或已验证前驱到当前编码的逐步谱系；terminal-first 表示
明列的有限终端谓词全部 MISS。

本文件中的 direct terminal 统一按下式验证。对
\(m\equiv3\pmod4\)、\(3\le m\le p-2\)，令 \(x=(p+m)/4\)。Type-I
证书是 \(d\mid x^2\)、\(m\mid px+d\)；Type-II 证书还要求
\(d\le x\)、\(m\mid x+d\)。命中时分别用
\[
\left(x,\frac{px+d}{m},\frac{p(x+px^2/d)}m\right)
\quad\text{或}\quad
\left(x,\frac{p(x+d)}m,\frac{p(x+x^2/d)}m\right)
\]
直接验证 \(4/p\) 的三分母恒等式。

定义

\[
P=p+4,\qquad N=\frac{3p+1}{4},\qquad D=2p-3.
\]

hard-core 子域由以下可检查条件定义：

* \(P\) 的所有素因子都为 \(1\pmod4\)；
* \(N\) 的所有素因子都为 \(1\pmod3\)；
* source 已通过上述 terminal-first schedule；
* source 的 parent 谱系和规范合法性可验证。

本文把 \(N=(3p+1)/4\) 的每个素因子均为 \(1\pmod3\) 的条件简称为
\(R=3\)-G；字母 G 不包含任何额外的实现或图论含义。

无条件可从头证明的恒等式包括

\[
3P-4N=11,\qquad \gcd(P,N)\mid11.
\]

只有在本节的 \(P\)-hard-core 条件下，才有 \(\gcd(P,N)=1\)：若 \(11\mid P\)，
则 \(11\) 是 \(P\) 的一个 \(3\pmod4\) 素因子，矛盾。等价地，不施加该条件时
\(\gcd(P,N)=11\) 恰在 \(p\equiv7\pmod{11}\) 发生。

以及 Jacobi 符号关系
\[
\left(\frac{33}{N}\right)=\left(\frac{P}{11}\right).
\]

令 \(\operatorname{spf}(P)\) 表示 \(P>1\) 的最小素因子。若 \(P\) 有素因子
\(h=\operatorname{spf}(P)\)，可考察 gap \(m=3h\) 的混合终端；
若 \(P\) 为素数，则进入 \(D=2p-3\) contact 系统。

在 \(D\)-contact 系统中，一个候选 witness 由正整数
\((A,C,K,m,h,B,g,s,r,t,\ell)\) 组成，定义
\[
x=ABC,\quad d=A^2C,\quad B=Km-A,\quad h=4ACK-1,
\]
\[
D=2p-3,\quad g=\gcd(h,D),\quad
h=gs,\quad D=gr,
\]
\[
T=8A^2C+3=gt,\qquad L=3K+2A=g\ell.
\]
在 mixed-contact 子域 \(1<g<h\) 中，完整 quotient 条件是
\[
r+t=2sm,\qquad t=4AC\ell-3s,\qquad
2sB=Kr+\ell.
\]
因此候选是否是真正 Type-II witness，必须逐项检查
\[
B\ge A,\quad \gcd(A,B)=1,\quad m\equiv3\pmod4,\quad3\le m\le p-2,
\]
以及上式的整除和正性；partial congruence 不能替代这些条件。

## 2. 待证明命题

对上述整个 actual hard-core source domain，证明一个互斥穷尽的闭合：

\[
\boxed{
\mathscr H_{C=1}
=\mathscr T\ \dot\cup\ \mathscr E\ \dot\cup\ \mathscr V,
}
\]

其中：

* \(\mathscr T\)：完整 terminal certificate 可验证；
* \(\mathscr E\)：在精确 actual domain 上证明 family empty；
* \(\mathscr V\)：有 source-bound E1、确定 E2、固定 E3、universal E4、
  fixed E5 和 re-entry 的 successor。

定义 canonical \(R=3\) anchor 为
\[
R_0=3,\qquad K_0=A_0=\frac{3p+1}{4},
\]
它满足 \(4K_0=pR_0+1\)。特别要求排除仅靠该 anchor 的假出口：若这个 map
从 ABSORB 回到 CHARGED，使固定 N\(^7\) 势上升，则它不得被隐藏进 finite macro，
也不能作为 E5。

## 3. D-contact 分支必须完整处理

定义 mixed-D normal form 的整数变量 \(A,C,h\)，并在文件内明确：

* quotient/cofactor/order/gcd 条件；
* \(D\) 的整除关系；
* Type-II terminal 的恢复公式；
* \(4A^2C\le p-5\) 的边界（若采用该引理，须独立证明）。

对于每个固定 \(p\)，有限 divisor table 可以证明某些 row 为
FAMILY_EMPTY，某些 \(1<\gcd(h,D)<h\) row 为 TERMINAL。
但必须说明：逐素数有限表不等于对所有 p 的 selector totality；若要闭合全域，需给参数化证明。

## 4. 必须处理的剩余出口

1. \(P\) composite 的 \(m=3h\) mixed-residue terminal screen；
2. \(P\) prime 且 \(D=2p-3\) composite 的 quotient contact；
3. \(D\) prime 时的 family-empty 证明；
4. \(R=3\)-G source 的 parent 谱系和 domain-preserving routing；
5. ABSORB 的 E3 分类、non-upward admission 和 re-entry。

## 5. 禁止的捷径

~~~text
把 p+4 hard-core 与 N hard-core 当作整个数论分支 closure；
把有限 divisor table 当作所有 p 的 terminal theorem；
把 canonical ABSORB cursor 当作 strict successor；
把 p=2521 的 hard control 外推为 universal non-anchor edge；
把 mixed-D parameterization 当作 actual E1；
把局部 rank drop 当作 parent-to-final E5。
~~~

## 本文件中的 E-stage 词义

E1 是 actual high-support C=1 source 与 D-contact occurrence；E2 是确定的 contact/
terminal projector；E3 是固定相位分类、schema、合法语法与准入谓词；E4 是全称解提升；
E5 是固定 \(\mathbb N^7\) 的最终严格票；R 是不向上回到非法 ABSORB 的递归 re-entry。
七个势坐标必须是在全部合法状态上定义的固定总函数，并在证明中公布算法和顺序。

## 6. 完成证据

需要一个参数化证明或明确的全域 partition theorem、每个 leaf 的 terminal/empty/
successor 结果、实际 source certificate、E2--E5、固定 admission 和 re-entry。
若只关闭固定 p 的 table，命题状态仍为 OPEN，只能登记为 per-prime arithmetic lemma。
