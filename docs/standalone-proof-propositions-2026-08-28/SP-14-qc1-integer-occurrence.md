# SP-14：横向素因子 \(q_\perp\) 的整数 occurrence 与 deflation 闭合

**状态：** OPEN_PROPOSITION
**研究任务：** 将横向素因子的 ideal 信息转化为 actual integer occurrence，或闭合其补集。
**独立性：** 本文件自包含 root、ideal、raw occurrence 和 E1--E5 定义，不依赖任何项目术语。

## 1. 独立背景

状态是带规范编码和 parent 谱系的整数元组
\(S=(p,R,K,A,h,D,E,k,\lambda)\)，其中 \(k\in\mathbb N_{>0}\) 是被编码并可重算的
primitive-quotient 整数；actual 表示由根或已验证前驱到达；
terminal-first survivor 表示明列的有限 terminal schedule 全部未给出 \(4/p\)
的正整数三分母解。设 \(p\equiv1\pmod{24}\) 为素数，考虑 low proper-root
状态，其基本数据为

\[
2\le h<p,\qquad z=R-h=ED,\qquad K=A(p-1),
\]

并要求
\[
4K=pR+1,\qquad A\mid K,\qquad h\mid K,\qquad
\gcd(h,z)=1,\qquad D\mid K,\qquad D\mid ph+1.
\]
本文“完整最大化正规化”的精确定义是：对每个素数 \(\ell\)，令
\(a_\ell=v_\ell(A)\)、\(k_\ell=v_\ell(K)\)、\(\zeta_\ell=v_\ell(z)\)，并规定
\[
\bigl(v_\ell(D),v_\ell(E)\bigr)=
\begin{cases}
(\zeta_\ell,0),&\zeta_\ell\le k_\ell,\\
(a_\ell,\zeta_\ell-a_\ell),&\zeta_\ell>k_\ell.
\end{cases}
\]
不允许从同余条件任取 \(D\) 或 \(E\)，也不能把该规则替换为 \(\gcd(z,K)\)。

并设 \(D^\ast>1\) 是从 \(D\) 去除 root-support 因子后得到的 transverse factor。
定义 primitive quotient 的非 h-support 部分为
\[
k_\perp=
\frac{k}{\prod_{\ell\mid h}\ell^{v_\ell(k)}}>1.
\]
一个 oriented ideal certificate 是显式有限数据，能由可靠整数算法选出一个
素数 \(q_\perp\mid D^\ast\) 及其方向；证明者必须给出该算法和唯一性证明。
ideal divisibility 本身不是整数 occurrence。

若使用 Eisenstein 表示，必须在同一证明中定义
\[
\mathbb Z[\omega],\qquad \omega^2+\omega+1=0,
\]
给出所用 norm、共轭、ideal factorization 和“方向”的规范规则。若不使用该环，
则 oriented ideal certificate 必须被替换成一个完全由整数同余定义的等价对象。

本文件中 root-support 固定为 \(H=h^2-1\)，并定义
\[
D^\ast=\frac{D}{\gcd(D,H)}.
\]
又因 \(D\mid ph+1\)，有 \(\gcd(D,h)=1\)，从而 \(D^\ast\) 与 \(h\) 互素；任何 primitive quotient 或 ideal 标记都必须
由 source payload 明确给出，不能由名称推断。

对 \(q=q_\perp\)，令
\[
\delta=v_q(D),\quad a=v_q(A),\quad c=v_q(p-1),\quad \zeta=v_q(z).
\]

定义 endpoint multiplier \(E\) 的 source identity：

\[
z=D(1+p\sigma)=DE.
\]

于是

\[
q\mid E\Longleftrightarrow \zeta>a+c,
\qquad
q\nmid E\Longleftrightarrow \zeta\le a+c.
\]

若 \(q\mid E\)，令 \(\mu=v_q(E)>0\)，候选 endpoint-excess target 的算术形状为

\[
A'=\frac{AE}{q^\mu},\qquad
c'=\left\langle-q^\mu\right\rangle_p.
\]

这不同于 norm-ideal 形状 \(Aq\)、\(\langle-q^{-1}\rangle_p\)。

## 2. 待证明命题

对 \(m=3\) 与 \(m>3\) 两个完整 actual domain，分别证明以下互斥闭合：

\[
\boxed{
\text{terminal hit}
\ \lor\
\text{q-divides-E source-forward successor}
\ \lor\
\text{q-not-divides-E terminal/empty/alternate closure}.
}
\]

其中 q-divides-E successor 必须证明：

1. q 的 exact integer occurrence 在 source 规范编码中有路径和一次性守恒证明；
2. \(A'\)、target \(R'\)、target \(K'\) 由确定映射唯一产生；
3. target 通过自身 terminal schedule 和本文件定义的 E3；
4. \(\mathsf{Sol}(T)\to\mathsf{Sol}(S)\) 对全部解成立；
5. 固定 N\(^7\) 的 parent-to-final E5 严格下降；
6. target 重新属于同一个状态宇宙并可再次使用同一选择规则。

q-not-divides-E 分支不能只返回“没有 fresh factor”。必须进一步证明：

* 一个完整 terminal；
* 或 exact source domain 上的 family-empty；
* 或一个不依赖 ideal label 的 alternate integer occurrence。

## 3. \(m=3\) 与 \(m>3\) 两域

第一域精确定义为 \(m=3\)，第二域精确定义为 \(m>3\)。二者必须分别证明其 terminal
priority 和 target map，不得把一个分支的 occurrence 规则移植给另一个。

应包含一个非实际反控：例如某个 \(q_\perp\mid N\)，但
\(q_\perp\nmid R-h,D,E,K\)。它说明 norm/ideal 数据不能定位 endpoint raw occurrence。

## 4. 禁止的替代论证

~~~text
ideal factor = integer occurrence；
q|N 推出 q|E；
q|E 只算出 A' 就称 successor；
把 norm-ideal target map 和 endpoint-excess target map 混合；
把 atomic rank decrease 当作 E5；
从单个 q 的局部公式推出两个 domain 的 totality。
~~~

## 本文件中的 E-stage 词义

E1 是 path-bound integer \(q_\perp\) occurrence；E2 是区分 norm-ideal 与 endpoint-excess
的确定映射；E3 是两域各自固定的 schema、分类和准入谓词；E4 是全称解 lift；E5 是 fixed
\(\mathbb N^7\) strict ticket；R 是目标回到同一 proper-root selector。
七个势坐标必须是全部合法状态上的固定总函数，算法和顺序在证明中公布。

## 5. 完成证据

需要 \(m=3\)/\(m>3\) source partition、actual occurrence certificate、守恒证明、
两个映射的独立验证、terminal/empty alternate 分支、E1--E5、固定准入、
re-entry 和 ideal-to-raw 负控。没有 raw path 的“存在 q”不算完成。
