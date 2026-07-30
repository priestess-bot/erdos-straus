---
kind: claim
claim_id: type-I-f-qadic-numerator-lift-rigidity-and-gcd-reduction
title: F 状态 q 进清分子的参数刚性与公因子约分
statement: 设 4K=pR+1，A+B=Rm_0，且 A/B 是 K 支撑上的互素目标表示。对奇素数 q|K，若 v_q(B)=nu+e>nu=v_q(K)，则满足 A'+B'=Rm_0' 与 q^(nu+e)|(pA'+m_0') 的全部整数三元组可显式参数化；其中任一满足 gcd(A',B')=1 的三元组必有 q 不整除 A'、v_q(B')=nu，并满足唯一的单位相位。若固定 B，则全部候选恰为 A'=A+Rs、m_0'=m_0+s，清除条件等价于 s=-A/R mod q^e；它必先制造 q^e 公因子再约分，且 A'=A+q^nu t 不可能清除一层。更一般地可用 CRT 同时约去 D=B/(B,K)，得到互素 a+b=Rr、b=(B,K)|K；该约分总能清除负向首分母，但在 F-box miss 中不可能回落为同一 (p,R,K) 的 Type I 盒内命中。以 a,b 生成 Type II 还必须独立满足某个合法 h|a+b 及 4ab|p+h。上述结论只实现整数 numerator lift，不构造换 K/R/支撑的合法递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-f-denominator-clearing-qadic-lift-contract
  - type-I-f-overflow-rational-gap-denominator
  - type-I-target-divisor-overflow
  - type-II-coprime-factor-normal-form
topics:
  - type-I
  - type-II
  - F-state
  - target-fiber
  - signed-denominator-defect
  - q-adic
  - gcd-reduction
  - support-switch
  - descent
  - proof-program
sources:
  - claim: type-I-f-denominator-clearing-qadic-lift-contract
    role: necessary-q-adic-numerator-phase
  - claim: type-I-f-overflow-rational-gap-denominator
    role: exact-rational-gap-and-first-denominator
  - claim: type-I-target-divisor-overflow
    role: type-I-target-divisor-normal-form
  - claim: type-II-coprime-factor-normal-form
    role: exact-type-II-endpoint-test
visibility: public
last_checked: '2026-07-30'
---

# F 状态 q 进清分子的参数刚性与公因子约分

## 1. 设定

设 \(p\equiv1\pmod {24}\) 为素数，\(R\) 为正整数，并且

\[
4K=pR+1,
\qquad
\gcd(K,R)=1,
\tag{1}
\]

式 (1) 模 \(4\) 自动给出 \(R\equiv3\pmod4\)，所以后文使用这一模类不需要额外
假设。

且一个正有理目标纤维表示写成

\[
A+B=Rm_0,
\qquad
\gcd(A,B)=1,
\tag{2}
\]

其中 \(A,B\in\mathbb N\) 的全部素因子都来自 \(K\)。于是

\[
\frac AB\equiv-1\pmod R,
\qquad
N=pA+m_0,
\qquad
RN=4KA+B.
\tag{3}
\]

固定一个奇素数 \(q\mid K\)，记

\[
\nu=v_q(K),
\qquad
v_q(B)=\nu+e,
\qquad
e>0.
\tag{4}
\]

由精确有理缺口分母定理，\(v_q(N)=\nu\)。所谓负向清分子的 \(e\) 层提升条件是

\[
A'+B'=Rm_0',
\qquad
q^{\nu+e}\mid pA'+m_0'.
\tag{5}
\]

本卡只研究 (5) 的整数实现。它不预设 \((A',B')\) 仍在原 \(K\) 指数盒内，也不把
一个整数实现称为合法状态边。

## 2. 保持目标关系的全部整数通解

令 \(L=\nu+e\)。满足 (5) 的全部整数三元组恰由两个整数 \(a,t\) 参数化为

\[
\boxed{
\begin{aligned}
A'&=a,\\
m_0'&=q^L t-pa,\\
B'&=Rq^L t-4Ka.
\end{aligned}
}
\tag{6}
\]

事实上，若 (5) 成立，写

\[
pA'+m_0'=q^Lt.
\]

取 \(a=A'\)，便有 \(m_0'=q^Lt-pa\)，再由 \(B'=Rm_0'-A'\) 与
\(pR+1=4K\) 得到 (6)。反向代入立即重建 (5)。

式 (6) 特别说明：纯整数正解从来不是瓶颈。取 \(a=1\)，再令 \(t\) 足够大，就有

\[
A'>0,
\qquad B'>0,
\qquad m_0'>0,
\qquad \gcd(A',B')=1.
\]

这样的正互素解有无穷多个，但 \(B'\) 和 \(m_0'\) 可以任意大，且 \(B'\) 一般带有
原 \(K\) 以外的素因子；因此这不是容量、短证书或递降定理。

### 互素通解的局部刚性

若 (5) 还满足 \(\gcd(A',B')=1\)，则必有

\[
\boxed{
q\nmid A',
\qquad
v_q(B')=\nu.
}
\tag{7}
\]

写

\[
c=\frac{4K}{q^\nu},
\qquad
b'=\frac{B'}{q^\nu},
\]

则 \(c,b'\) 都是 \(q\)-进单位，并且

\[
\boxed{
b'\equiv-cA'\pmod {q^e}.
}
\tag{8}
\]

证明很直接。由 (5) 乘以 \(R\)，得到

\[
4KA'+B'\equiv0\pmod {q^{\nu+e}}.
\tag{9}
\]

因为 \(\nu\ge1\)，式 (9) 先给出 \(q\mid B'\)。互素性遂强制 \(q\nmid A'\)，所以
\(v_q(4KA')=\nu\)。若 \(v_q(B')\ne\nu\)，两个加数的较小赋值不能抵消到
\(\nu+e\) 层，故必须有 \(v_q(B')=\nu\)。将 (9) 除以 \(q^\nu\) 即得 (8)。

因此不存在同时满足下列三项的候选：

\[
\gcd(A',B')=1,
\qquad
v_q(B')=\nu+e,
\qquad
q^{\nu+e}\mid pA'+m_0'.
\tag{10}
\]

互素实现必须已经把候选分母的 \(q\)-指数降到基线 \(\nu\)；若坚持保留原来的
\(B\)，则只能先进入非互素坐标，再通过最大公因子约分。

## 3. 固定 \(B\) 时的唯一提升类

现要求 \(B'=B\)。由 (2) 与 \(A'+B=Rm_0'\)，全部保持目标关系的候选必且只必写成

\[
\boxed{
A_s=A+Rs,
\qquad
B_s=B,
\qquad
m_s=m_0+s
}
\tag{11}
\]

其中 \(s\in\mathbb Z\)。其清分子满足精确差分式

\[
\boxed{
N_s=pA_s+m_s=N+4Ks.
}
\tag{12}
\]

因为 \(v_q(B)=\nu+e\)、\(v_q(4K)=\nu\) 且 \(q\nmid R\)，由

\[
RN_s=4KA_s+B
\]

得到下列完全等价的条件：

\[
\boxed{
q^{\nu+e}\mid N_s
\iff
q^e\mid A_s
\iff
s\equiv-AR^{-1}\pmod {q^e}.
}
\tag{13}
\]

再令

\[
u=\frac N{q^\nu},
\qquad
c=\frac{4K}{q^\nu}.
\]

由 \(RN=4KA+B\) 除以 \(q^\nu\)，并利用
\(q^{\nu+e}\mid B\)，还可把 (13) 写成原必要合同的相位形式

\[
\boxed{
s\equiv-u c^{-1}\pmod {q^e}.
}
\tag{14}
\]

这里的 \(s\) 必为 \(q\)-进单位。因此 (12) 中的清分子改变量满足

\[
v_q(N_s-N)=v_q(4Ks)=\nu,
\tag{15}
\]

正好命中必要合同要求的非零单位相位。

令 \(s_{q,e}\in\{1,\ldots,q^e-1\}\) 为 (13) 的最小正代表，则

\[
A_{s_{q,e}}-A=Rs_{q,e}
\]

是所有正向固定 \(B\) 提升中的最小正改变量。若还要求
\(v_q(A_s)=e\)，则在

\[
s=s_{q,e}+q^e k
\]

中只需避开唯一一个 \(k\pmod q\)；其余 \(q-1\) 个模 \(q^{e+1}\) 的提升类都只制造
恰好 \(e\) 层公因子。

### \(A'=A+q^\nu T\) 方案不可能

若取

\[
A'=A+q^\nu T,
\qquad
B'=B
\tag{16}
\]

并要求目标关系仍成立，则由 \(R\mid A'-A\) 及 \(\gcd(R,q)=1\) 得 \(R\mid T\)。写
\(T=Rk\)，式 (11) 中对应的参数为 \(s=q^\nu k\)，故 \(q\mid s\)。这与 (13) 中
\(s\equiv-AR^{-1}\not\equiv0\pmod q\) 矛盾。因此

\[
\boxed{
A'=A+q^\nu T,\ B'=B
\text{ 不可能在保持 }A'+B'=Rm_0'\text{ 时清除哪怕一层缺陷。}
}
\tag{17}
\]

这也解释了“最小改变量”的方向：需要具有 \(q\)-进单位的 \(A\) 坐标改动，而不是给
\(A\) 加一个被 \(q^\nu\) 整除的量；真正具有赋值 \(\nu\) 的对象是清分子差
\(N_s-N=4Ks\)。

## 4. 一次约去全部负向分母缺陷

定义完整负向 Type I 首分母缺陷

\[
D=\frac{B}{(B,K)}
=\prod_{\ell\mid B}\ell^{e_\ell},
\qquad
e_\ell=\bigl(v_\ell(B)-v_\ell(K)\bigr)_+.
\tag{18}
\]

这里的代数约分对所有素数成立；当 \(\ell\) 为奇素数且 \(e_\ell>0\) 时，它同时实现
前节的 \(\ell\)-进清分子合同。对每个 \(\ell\mid B\)，可以选取 \(s\) 的局部剩余类使

\[
\begin{cases}
v_\ell(A+Rs)=e_\ell,&e_\ell>0,\\
v_\ell(A+Rs)=0,&e_\ell=0.
\end{cases}
\tag{19}
\]

确实，若 \(e_\ell>0\)，先取

\[
s\equiv-AR^{-1}\pmod {\ell^{e_\ell}},
\]

再避开模 \(\ell^{e_\ell+1}\) 的唯一更深提升类；若 \(e_\ell=0\)，只需避开模
\(\ell\) 的唯一根。不同素数的模数互素，所以 CRT 可以同时完成全部选择。最后给 \(s\)
加上共同模数的充分大正倍数，可同时保证

\[
A+Rs>0,
\qquad
m_0+s>0.
\]

这个选择精确给出

\[
\boxed{
\gcd(A+Rs,B)=D.
}
\tag{20}
\]

于是定义约分后的整数

\[
a=\frac{A+Rs}{D},
\qquad
b=\frac B D=(B,K),
\qquad
r=\frac{m_0+s}{D}.
\tag{21}
\]

因为 \(D\mid A+Rs\)、\(D\mid B\)、\(\gcd(D,R)=1\)，关系
\(R(m_0+s)=A+Rs+B\) 说明 \(D\mid m_0+s\)，故 (21) 确为整数。由 (20) 还有

\[
\boxed{
a+b=Rr,
\qquad
\gcd(a,b)=1,
\qquad
b\mid K.
}
\tag{22}
\]

并且 \(\gcd(a,r)=\gcd(b,r)=1\)。例如若某素数同时整除 \(a,r\)，它也整除
\(Rr-a=b\)，与 \(\gcd(a,b)=1\) 矛盾。

式 (21)--(22) 给出一个无条件的**整数约分实现**：固定原 \(B\)，先令新分子与
\(B\) 共有恰好 \(D\)，再把这份公因子从 \(A+Rs,B,m_0+s\) 中同时约去。约分后的
负向形式首分母

\[
x=\frac{Kr}{b}
\tag{23}
\]

必为整数。它没有创造新的 \(q\)-进容量；它只是把原分母超额搬入新分子 \(a\) 的
因子结构。

## 5. 回落到同一 \(R\) 的 Type I 的精确条件

令

\[
H=\frac Kb.
\]

由 \(a+b=Rr\)、\(4K\equiv1\pmod R\) 和 \(\gcd(b,R)=1\)，整数

\[
h_I=\frac{4Ha+1}{R}
\tag{24}
\]

有定义，并满足

\[
x=\frac{p+h_I}{4}=Hr,
\qquad
E=Ha,
\qquad
4E+1=Rh_I.
\tag{25}
\]

因此 \(E\) 是这对约分端点给出的规范 Type I 目标除子候选。由于
\(\gcd(a,r)=1\)，其平方整除条件精确化为

\[
\boxed{
E\mid x^2
\iff
Ha\mid H^2r^2
\iff
a\mid H=K/b.
}
\tag{26}
\]

在给定方向上，自然范围 \(E<K\) 等价于 \(a<b\)。由第 1 节已经得到
\(R\equiv3\pmod4\)，所以一旦 \(a<b\) 且 (26) 成立，就有
\(h_I\equiv3\pmod4\)。又

\[
p-h_I=\frac{4H(b-a)-2}{R}>0,
\qquad
p-h_I\equiv2\pmod4,
\]

故 \(3\le h_I\le p-2\)，确实得到同一 \((p,R,K)\) 的 Type I 证书。

由于 \(a,b\) 互素且 \(b\mid K\)，将目标关系按较小端点定向后，式 (26) 可对称地写成

\[
\boxed{
\text{约分端点在同一 }(p,R,K)\text{ 中给出 Type I 盒内命中}
\iff ab\mid K.
}
\tag{27}
\]

这里若 \(a<b\)，(27) 就是 (26) 与 \(a\mid K/b\)；若 \(b<a\)，交换端点并使用反射
方向，同一论证把条件写成 \(b\mid K/a\)。两种情形都恰好等价于 \(ab\mid K\)。

若原状态是 F-box miss，则目标纤维与 \(K\) 的指数盒不相交，故 (27) 不可能发生。
于是 (21) 的无条件约分并没有解决 F 状态：它只能使 \(a\) 在某个 \(K\) 坐标上产生
正向超额，或使 \(a\) 含有 \(K\) 支撑之外的素因子。换言之，负向缺陷被清除后，联合
障碍必在另一方向或外部支撑中重新出现。

## 6. 以约分端点生成 Type II 的精确附加条件

把 \(a,b\) 按大小重排。Type II 互素因子正规形表明：恰以这两个数作为前两项的
Type II 证书存在，当且仅当存在整数 \(h\) 满足

\[
\boxed{
\begin{aligned}
&h\equiv3\pmod4,
\qquad 3\le h\le p-2,\\
&h\mid a+b=Rr,\\
&ab\mid\frac{p+h}{4},
\quad\text{等价地}\quad
4ab\mid p+h.
\end{aligned}
}
\tag{28}
\]

若 (28) 成立，取

\[
C=\frac{p+h}{4ab}
\]

便得到 \(x_h=abC\) 的 Type II 正规形。反之，任何使用这对端点的 Type II 正规形都
必须满足 (28)。特别地，

\[
ab\le\frac{p-1}{2}
\tag{29}
\]

是必要的大小条件。

提升关系只给出 \(a+b=Rr\)，所以它只产生 (28) 中的候选缺口因子；它完全不强制
\(4ab\mid p+h\)。因此 Type II 是一个独立的终端碰撞条件，不能由 q 进清分子同余
自动推出。

## 7. 状态与递降边界

上述结论必须分成三层理解：

1. **same-state numerator lift。** 式 (6) 或固定 \(B\) 的式 (11)--(15) 只在同一
   \(p,R,K\) 下解目标关系和清分子同余。它们有无穷多个整数解，因而“同余可解”本身
   没有容量内容。
2. **同一支撑内的目标改写。** 若约分后的 \(a,b\) 仍为 \(K\)-smooth，但
   \(ab\nmid K\)，它只是同一目标纤维中的另一个盒外表示；F-box miss 下至少一个正向
   指数仍然超界。它既不是新状态，也不是严格下降。
3. **支撑逃逸。** 若 \(a\) 含有 \(K\) 以外的素因子，这给出一个规范的
   support-escape 标签，但不是合法 support switch。固定 \(p,R\) 时
   \(K=(pR+1)/4\) 唯一，不能把新素因子任意加入 \(K\)。若要改变 \(K\) 或 \(R\)，还须
   显式构造新状态、验证正规形、给出全域解提升，并证明预先定义的良基势函数严格下降。

因此本卡推进的是“必要 q 进合同能否在整数层实现”的问题：答案是能，而且实现具有
精确的参数刚性和公因子约分结构。它同时证明这一步远未构成统一选择器；真正剩余的
算术任务是迫使 (27) 或 (28) 命中，或者把支撑逃逸升级成换 \(K/R\)、解可提升且严格
下降的合法状态边。
