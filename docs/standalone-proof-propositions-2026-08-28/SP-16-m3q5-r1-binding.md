# SP-16：\(m=3,q=5\) source-path binding

**状态：** OPEN_PROPOSITION
**研究任务：** 把一个明确的 \(m=3,q=5\) 整数 transcript 绑定到实际 parent，并形成可递归 target。
**独立性：** 本文件自包含 transcript、source lineage 和 E-stage 定义；所有证据对象均在本文定义。

## 1. 自包含背景

状态 \(S=(p,R,K,A,h,D,E,k,\lambda)\) 是带唯一规范编码和 parent 谱系的整数对象，
其中 \(k\in\mathbb N_{>0}\) 是被编码的 primitive-quotient 整数。actual 表示由根或已验证
前驱到达，persistent 表示满足固定合法性谓词。设 \(p\equiv1\pmod{24}\) 为素数，
且 \(S\) 的根容量数据满足

\[
4K=pR+1,\qquad 2\le h<p,\qquad z=R-h=ED.
\]

还要求
\[
K=A(p-1),\qquad h\mid K,\qquad\gcd(h,z)=1,\qquad
D\mid K,\qquad D\mid ph+1,
\]
且 \(D,E\) 由以下逐素数规则唯一计算：对每个素数 \(\ell\)，令
\(a_\ell=v_\ell(A)\)、\(k_\ell=v_\ell(K)\)、\(\zeta_\ell=v_\ell(z)\)，并规定
\[
\bigl(v_\ell(D),v_\ell(E)\bigr)=
\begin{cases}
(\zeta_\ell,0),&\zeta_\ell\le k_\ell,\\
(a_\ell,\zeta_\ell-a_\ell),&\zeta_\ell>k_\ell.
\end{cases}
\]
该公式不能用 \(\gcd(z,K)\) 替代。

令 \(m=3\)，并令 \(q=5\) 是指定的 transverse factor。定义
\[
D^\ast=\frac{D}{\gcd(D,h^2-1)},\qquad
k_\perp=\frac{k}{\prod_{\ell\mid h}\ell^{v_\ell(k)}},
\]
并要求
\[
5\mid D^\ast,\qquad k_\perp=1.
\]

算术 transcript 是一个有限序列
\[
\mathcal W=(W_0,W_1,\ldots,W_s),
\]
其中 \(W_0\) 是 source 的序列化 payload；每个 \(W_{i+1}\) 由
\(W_i\) 和一个明确整数操作 \(F_i\) 唯一计算；每一步都保留同一个
\(4/p\) equation interface，并给出 p-free/primitive 条件。末端包含
一个 canonical q=5 occurrence、两个 capacity words 以及一个 endpoint payload。
capacity word 在本文中是一个有限整数因子序列及其逐步转换函数；证明者必须给出每个
word 的字母表、顺序、转换公式、终端前缀和最终 endpoint，不允许引用外部策略名称。

本命题把“transcript 的算术公式正确”与“它确实来自 actual persistent parent”
严格区分。actual parent 必须有 root 或已验证 predecessor、terminal-first MISS、
完整规范编码、分类值和合法性证明。terminal-first schedule 是证明中完整列出的有限
有序终端检查，首个 \(4/p\) 三分母 certificate HIT 抢先。

## 2. 待证明命题

对每个满足上述条件的 actual source，证明 transcript 可以变成同一递归系统可消费的
source certificate：

\[
\boxed{
\text{actual parent}
\Longrightarrow
\text{唯一 source-path certificate}
\Longrightarrow
\text{固定 E3 与 target re-entry}.
}
\]

certificate 必须绑定：

1. parent 的完整规范编码和 predecessor lineage；
2. \(m=3,q=5,D^\ast,E\) 的实际 occurrence path/value；
3. 每一个 \(F_i\) 的规范规则编码、输入和输出；
4. terminal-first prefix 的完整结果；
5. transcript 的量词域、prime order 和 endpoint 规范编码；
6. 允许的目标域、唯一映射、独立验证器、固定势函数和 re-entry 分类。

若 transcript 在某个内部 prefix 命中 terminal，唯一结果必须是 terminal，不得继续消费
后续 word。

## 3. E-stage 验收

* E1：路径中的 \(q=5\) 和 transcript 起点来自实际 source 编码；
* E2：每个下一节点由冻结 \(F_i\) 唯一生成；
* E3：最终 target 通过固定 persistent schema、normal form、分类和准入谓词；
* E4：给出全称 solution-set lift；
* E5：比较 parent 与最终 target 的固定 N\(^7\) 势；
* R：target 回到同一状态宇宙，而不是留在 transcript 中间类型。

固定 N\(^7\) 势由七个在全部合法状态上定义的总函数组成；证明必须公布它们的算法、
语义和顺序，不能按 transcript 分支临时改变。

## 4. 禁止的替代证据

~~~text
只提供 q=5 的理想因子；
只提供一个 domain 字符串或对象 ID；
从 p 重建 parent；
把 transcript label 当作 E1；
把中间 capacity word 当作可入队 target；
把某个 control 的 transcript 复制到另一个 source。
~~~

## 5. 完成证据

需有 source-bound transcript 定理、完整 certificate schema、独立重放器、E1/E3/
固定势/re-entry 证据，以及 prefix terminal、parent swap、path swap、domain swap 的负控。
算术 transcript 单独不关闭本命题。
