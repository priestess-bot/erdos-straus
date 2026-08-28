# SP-10：high-support noncanonical incoming grammar

**状态：** OPEN_PROPOSITION
**研究任务：** 穷尽分类所有非规范高支撑 incoming states，并为可规范化部分建立实际 source-bound 后继。
**独立性：** 本文件独立定义 noncanonical grammar 和 determinant image，所有对象都在本文给出。

## 1. 背景与定义

设 \(p\equiv1\pmod{24}\) 为素数，\(B_p=(p-1)^2/4\)。状态是带规范编码和
parent 谱系 \(\phi\) 的整数元组 \((p,R,K,A,C,\phi)\)，满足

\[
4K=pR+1,\qquad R>p,\qquad K=AC,\qquad A>B_p,\qquad C\ge p+1.
\]

actual 表示 \(\phi\) 从根或已验证前驱逐步到达当前编码；terminal-first 表示一个
明确列出的有限 terminal schedule 全部 MISS；persistent 表示状态满足固定合法性谓词
且可再次被同一递归规则消费。协议相位固定为
\[
\mathrm{CHARGED}>\mathrm{PRE}>\mathrm{ABSORB}>\mathrm{RESET},
\]
并作为规范状态字段进入固定势函数。

定义 canonical residue

\[
c=\left\langle(4A)^{-1}\right\rangle_p\in\{1,\ldots,p-1\},
\qquad C=c+pt.
\]

noncanonical 分支是 \(t\ge1\)。形式 rebase 为

\[
(R,K;A)\longmapsto(R-4At,\ Ac;A),
\]

它在算术上把 cofactor 从 \(C\) 变成 \(c<p\)，但只有在 source 有合法
determinant occurrence 时才可能成为 actual transition。

允许的 source-bound determinant witness 定义为：存在
\(1\le d<p\)、\(M=Ab\)，满足

\[
K=M(p-d),\qquad C=b(p-d),
\]

且 \(M\) 是从 source 规范编码的固定路径中实际解析出的整数。

## 2. 待证明命题

对所有 actual noncanonical incoming states，证明一个穷尽 grammar：

\[
\boxed{
\text{每个 incoming state}
\in
\text{bound same-chart image}
\ \dot\cup\
\text{explicitly rejected/nonrecursive}
\ \dot\cup\
\text{另一个已证明闭合的构造域}.
}
\]

在 bound same-chart image 中，必须证明：

1. \(M=Ab\)、\(K=M(p-d)\) 的 witness 来自真实 parent；
2. \(C=b(p-d)\) 且 \(p-d<p\)；
3. target 的规范分类、normal form 和 terminal schedule 可重算；
4. target 通过本文件定义的 E3、fixed E5 和 re-entry。

定义
\[
\mathcal D(C)=\{d_0\in\mathbb N:2\le d_0<p,\ d_0\mid C\}.
\]
在 \(\mathcal D(C)=\varnothing\) 的 p-rough complement 中，必须另证
TERMINAL、FAMILY_EMPTY 或不同后继构造；“没有 determinant image”本身不是
closure。

## 3. 必须区分的三种对象

* **实际 source state：** 有 parent、raw occurrence、terminal certificate 和合法准入；
* **算术 determinant image：** 只满足整除/同余；
* **post-hoc identity：** 例如把 \(M=K,d=p-1\) 事后代入得到的表示。

后二者不能被提升为 E1。特别是 \(c=1\) 的 post-hoc 形式必须作为负控，而不是
后继构造。

## 4. 证明任务

1. 给出所有 incoming 后继构造的 source domain 和动作键；
2. 证明 action grammar 互斥、穷尽，且不允许未列入显式有限 action 集合的 branch
   静默出现；
3. 对小 divisor \(2\le c<p\) 建立 source-bound normalizer；
4. 对 p-rough complement 建立 terminal/empty/alternate partition；
5. 证明目标仍是合法 persistent Type-I/CHARGED state；
6. 证明 fixed N\(^7\) parent-to-final descent，不能只比较 \(C\)；
7. 证明所有 target 重新进入本文件固定的分类函数。

## 5. 必须保留的反例

~~~text
c|C 但没有 raw occurrence；
formal p-rough chart 被误写成 actual source；
M=K,d=p-1 的 post-hoc determinant；
source 分类与 target 分类不同却沿用旧编码；
target 通过 transient 中间对象绕过固定 admission；
同一后继构造的两个 action 给出矛盾 guard 结果。
~~~

## 本文件中的 E-stage 词义

E1 要求 bound determinant 的整数 occurrence 来自 actual parent；E2 是 canonical
normalizer 的唯一投影；E3 是固定 persistent schema、分类规则和准入谓词；E4 是全称解 lift；
E5 是固定 \(\mathbb N^7\) parent-to-final 严格下降；R 是重新进入固定分类函数。
七个势坐标必须是在全部合法状态上定义的固定总函数，并在证明中公布算法和顺序。

## 6. 完成证据

需要一个独立 grammar theorem、source-bound determinant certificate、目标 E1--E5、
非 canonical terminal/empty complement、独立 verifier 和 re-entry trace。
只证明 canonical residue \(c\) 存在或 local charged rank 下降，均不完成本命题。
