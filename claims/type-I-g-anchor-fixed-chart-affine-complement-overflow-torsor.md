---
kind: claim
claim_id: type-I-g-anchor-fixed-chart-affine-complement-overflow-torsor
title: G-anchor 固定图表的仿射与补余 overflow torsor
statement: 对 G-anchor 固定图表 R=p-2、K=(p-1)^2/4 的任一 determinant 行 pn=4Md+1，令 C=p-d、K=MC。保持 d 的全部整数行恰为 (M+pz,n+4dz)，其半径为 R+4Cz；z>=1 恰产生真实 overflow。若旧账本 A|M 被保留，则 A|z；在 overflow 子族中 E2 与 cofactor r-chart 完全不变，故平移不能修复 E2。带标记行的旧 raw 因子 delta|Q 若仍要求整除新半尾 Q_z=(R_z-1)/2，则恰有 delta|z；在这个弱标签保持条件下，full-Q 的任一正 overflow 平移越过 B_p 有界区。交换 d 与 C 的补余 torsor 给出另一类完整 determinant 行，并在其 overflow 子族把 E2 精确改写为 A/gcd(A,d)|(p-(M mod p))，仍不随平移参数改变。full-Q 行在 A=1 下给出统一的 E2-positive overflow 算术种子，但这些构造尚无 action-preserving raw adapter、marked lift 或 E5，不能登记为递归边。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-raw-fixed-chart-factor-projection
  - type-I-fixed-chart-determinant-factor-table
  - type-I-overflow-cofactor-ledger-e2-gate
  - type-I-overflow-e2-fixed-fiber-constancy
  - type-I-overflow-same-chart-support-promotion
  - denominator-escape-state-contract
topics:
  - type-I
  - G-anchor
  - fixed-chart
  - determinant
  - affine-torsor
  - complement
  - overflow
  - E2
  - charged-support
  - raw-label
  - proof-boundary
sources:
  - claim: type-I-g-anchor-raw-fixed-chart-factor-projection
    role: marked-low-chart-determinant-rows
  - claim: type-I-overflow-cofactor-ledger-e2-gate
    role: ledger-preserving-E2-criterion
  - claim: type-I-overflow-same-chart-support-promotion
    role: bounded-overflow-promotion-prerequisites
  - concept: denominator-escape-state-contract
    role: E1-E5-edge-requirements
visibility: public
last_checked: '2026-08-06'
---

# G-anchor 固定图表的仿射与补余 overflow torsor

## 1. 输入与固定 \(d\) 的完整仿射族

固定核心素数 \(p\equiv1\pmod {24}\)，并取 G-anchor 图表

\[
R=p-2,
\qquad
K=\frac{(p-1)^2}{4}.
\tag{1}
\]

设 \((M,c,t,\delta)\) 是带标记因子表中的一行。也就是说

\[
c=\frac KM,
\qquad
d=p-c,
\qquad
n=4M-R,
\qquad
pn=4Md+1.
\tag{2}
\]

下述第一个结论其实只使用 (2)，不要求 \(\delta\) 存在。

**定理 1（固定 \(d\) determinant torsor）。** 所有保持 \(p,d\) 不变的整数
determinant 解恰为

\[
M_z=M+pz,
\qquad
n_z=n+4dz,
\qquad z\in\mathbb Z.
\tag{3}
\]

相应图表满足

\[
R_z=4M_z-n_z=R+4cz,
\qquad
K_z=M_zc=K+pcz,
\qquad
pR_z+1=4K_z.
\tag{4}
\]

在 G-anchor 情形，所有 \(z\ge1\) 都给出正的规范 overflow 行，并且

\[
R_z=p-2+4cz>p.
\tag{5}
\]

反之，在这个 torsor 中 \(R_z>p\) 强制 \(z\ge1\)。因此固定 \((R,K)\) 内的任何
因子重选都不能产生 overflow；真正跨越低/高图表的最小算术自由度正是 \(z\)。

**证明。** 两个解相减给出

\[
p(n'-n)=4d(M'-M).
\]

因为 \((p,4d)=1\)，有 \(M'-M=pz\)，并恢复 (3)。代入即可得 (4)。
对 \(z\ge1\)，(2) 给出 \(M_z,n_z>0\)，而 (5) 显然；\(n_z=4M_z-R_z>0\)
同时验证规范范围。反向由 \(R_z=p-2+4cz>p\) 得 \(z>1/(2c)\)，故整数
\(z\ge1\)。证毕。

## 2. 保留账本时 carry 不会改变

设旧 charged support 满足 \(A\mid M\)。由 (2) 有 \(p\nmid M\)，因而
\(p\nmid A\)。所以

\[
\boxed{A\mid M_z\Longleftrightarrow A\mid z.}
\tag{6}
\]

令

\[
a=\frac{A}{(A,c)},
\qquad
r=[M]_p\in\{1,\ldots,p-1\}.
\tag{7}
\]

在 \(z\ge1\) 的 overflow 子族中，若 (6) 成立，则 \(a\mid z\)，且

\[
[M_z]_p=r,
\qquad
\left\lfloor\frac{M_z}{p}\right\rfloor
\equiv
\left\lfloor\frac Mp\right\rfloor\pmod a.
\tag{8}
\]

故带账本 E2 在整个保账本的 overflow 平移族上恒为

\[
\boxed{\mathrm{E2}(M_z)\Longleftrightarrow a\mid r.}
\tag{9}
\]

相同的余因子目标也完全不变：

\[
s=\frac{4rd+1}{p},
\qquad
R_r=4r-s,
\qquad
K_r=rc.
\tag{10}
\]

因此 (3) 是一个真实的 overflow 入口，却不是 E2 修复器，也不能改变既有
cofactor r-chart。这个结论比固定纤维常值性更窄但更具构造性：这里图表已经改变，
但任何**保留同一账本**的固定-\(d\) 平移仍无法改变 E2。

正整数缩放没有额外自由度。若 \(M'=qM\) 仍保持 \(d\)，则

\[
q\equiv1\pmod p,
\qquad q=1+pt,
\qquad M'=M+p(Mt),
\tag{11}
\]

所以它只是 (3) 的 \(z=Mt\) 子族。带标记 G 行满足 \(M>5p/4\)，故任何
非平凡缩放都有 \(M'>B_p=(p-1)^2/4\)，只能落入高载体余项。

## 3. raw 标签的最弱平移保持条件

对带标记行，令 \(Q=(R-1)/2=(p-3)/2\) 且 \(\delta\mid Q\)。新图表的自然半尾为

\[
Q_z=\frac{R_z-1}{2}=Q+2cz.
\tag{12}
\]

因为 \((Q,K)=1\)、\(c\mid K\)、\(\delta\mid Q\) 以及 \(Q\) 为奇数，
\((\delta,2c)=1\)。于是

\[
\boxed{\delta\mid Q_z\Longleftrightarrow\delta\mid z.}
\tag{13}
\]

式 (13) 只是“旧标签仍是新半尾的一个除子”的最弱算术条件；它不声称新的
Jacobi 相位、raw peeling path 或 marked lift 仍然存在。

特别地，canonical full 标签 \(\delta=Q\) 若要在正 overflow 平移中连这一弱条件也
保持，就必须有 \(Q\mid z\)。因此

\[
M_z\ge M+pQ> B_p,
\qquad
pQ-B_p=\frac{p^2-4p-1}{4}>0.
\tag{14}
\]

所以最小的 \(z=1\) overflow 构造必丢失全部 Jacobi-odd raw 标签；而 full-\(Q\)
标签的任何弱保持平移已经离开有界 support-promotion 区域。

## 4. 交换余因子的补余 torsor

固定 (2)，交换 \(d\) 与 \(c=p-d\)。所有这样得到的整数 determinant 行为

\[
M_\ell^\vee=\ell p-M,
\qquad
n_\ell^\vee=4c\ell-R,
\qquad \ell\in\mathbb Z,
\tag{15}
\]

并满足

\[
d^\vee=c,
\qquad
c^\vee=d,
\qquad
R_\ell^\vee=4d\ell-n,
\qquad
K_\ell^\vee=M_\ell^\vee d.
\tag{16}
\]

当且仅当 \(\ell>M/p\) 时，(15) 给出正的规范图表；它成为 overflow 当且仅当

\[
\ell>\frac{p+n}{4d}.
\tag{17}
\]

若 \(A\mid M\)，则

\[
A\mid M_\ell^\vee\Longleftrightarrow A\mid\ell.
\tag{18}
\]

在 \(\ell>(p+n)/(4d)\) 的 overflow 补余子族中，若 (18) 成立，则新残数为
\([M_\ell^\vee]_p=p-r\)，故其 E2 门精确为

\[
\boxed{
\mathrm{E2}(M_\ell^\vee)
\Longleftrightarrow
\frac{A}{(A,d)}\mid p-r.
}
\tag{19}
\]

它同样与 \(\ell\) 无关。补余能够改变 E2 的真值，但在其 overflow 子族中“取更高的
\(\ell\)”永远不能修复该门；是否可保留账本并通过 E2 在起点已经完全决定。

**证明。** 将 (15) 代入
\(4cM_\ell^\vee+1\) 即得 \(pn_\ell^\vee\)，再由 (2) 得 (16)。若
\(\ell>M/p\)，因为 \(4Mc=pR+1\)，有 \(M/p>R/(4c)\)，从而
\(n_\ell^\vee>0\)。写 \(M=kp+r\)、\(1\le r<p\)，则最小可取整数
\(\ell=k+1\) 时

\[
R_\ell^\vee=\frac{4d(p-r)-1}{p}>0,
\]

故图表规范。反向地，\((-M,-R)\) 是交换后方程
\(pn'=4cM'+1\) 的一个整数解；任取另一个解 \((M',n')\)，相减后有

\[
p(n'+R)=4c(M'+M).
\]

由 \((p,4c)=1\)，得到 \(M'+M=p\ell\)、\(n'+R=4c\ell\)，恰恢复 (15)。
其余等价式直接由 (15)--(16) 模 \(A\) 或模 \(p\) 化简。证毕。

## 5. full-\(Q\) 的统一 fresh overflow 种子

写 \(p=24h+1\)。full-\(Q\) 行满足

\[
c=(p-4,K)=
\begin{cases}
3,&h\not\equiv2\pmod3,\\
9,&h\equiv2\pmod3.
\end{cases}
\tag{20}
\]

取 fresh ledger \(A=1\)，E2 自动通过。固定-\(d\) torsor 的 \(z=1\) 给出

\[
(M^+,n^+,R^+,K^+)
=\bigl(M+p,\ n+4(p-c),\ p-2+4c,\ (M+p)c\bigr),
\tag{21}
\]

其中恒有 \(R^+>p\)、\(M^+\le B_p\)。例如

\[
p=73:\quad(M^+,n^+,R^+)=(505,1937,83),
\]
\[
p=193:\quad(M^+,n^+,R^+)=(1217,4641,227).
\tag{22}
\]

确实，\(c=3\) 时 \(M=48h^2\)，而 \(c=9\) 时 \(M=16h^2\)，故

\[
B_p-M^+=
\begin{cases}
96h^2-24h-1,&c=3,\\
128h^2-24h-1,&c=9,
\end{cases}
>0
\tag{23}
\]

（核心域从 \(h=3\) 开始）。

补余 torsor 还给出两类较小 \(d^\vee=c\) 的 seed：

\[
\begin{array}{c|c|c|c|c}
c&M^\vee&d^\vee&n^\vee&R^\vee\\ \hline
3&26h+1&3&13&104h-9\\
9&(50h+2)/3&9&25&(200h-67)/3
\end{array}
\tag{24}
\]

第一行取 \(\ell=2h+1\)，第二行取 \(\ell=(2h+2)/3\)。二者均满足

\[
pn^\vee=4M^\vee d^\vee+1,
\qquad R^\vee>p,
\qquad M^\vee\le B_p.
\tag{25}
\]

最后一个不等式分别由 \(144h^2-26h-1>0\) 与
\(144h^2-(50h+2)/3>0\) 给出。

这些是全 \(p\) 的真实 overflow determinant chart 和 E2-positive arithmetic seed，
而不是已经登记的递归输出。

## 6. 严格边界

本卡没有构造从旧 G raw path 到 (21) 或 (23) 的 action-preserving adapter。
特别地，(13) 已严格表明 \(z=1\) 丢失全部旧 Jacobi-odd 标签；补余更改变了
\((d,c,R,K)\)，现有 \((M,t,\delta)\) 嵌入也没有定义其像。

此外，保持 \(A\) 的重图表不改变既有 charged-support 势
\(\lfloor B_p/A\rfloor\)，因而不能独自支付 E5。\(A=1\)、\(M\le B_p\) 只说明
目标在算术上满足未来 same-chart support-promotion 的部分前提；仍须独立给出 target
source-tree、F/G 重分类、marked solution lift 和全域良基势。一个独立的 universal
\(p\)-source 也不能被冒充为旧 G raw path 的 adapter。
