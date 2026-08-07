---
kind: claim
claim_id: type-I-fg-raw-transcript-persistent-ledger-carry-core
title: raw transcript 中持续 E2 账本的 gcd carry core
statement: 对同一核心素数的一个已证明 sound 的 raw-to-overflow 物理行 transcript，若同一个旧 ledger A 必须在所有行保留且在指定行通过 E2，则 A 可行当且仅当 A 整除所有 carrier M_i 与所有 C_i(M_i mod p) 的 gcd。该 gcd 是无需预先选择 A 的最大持续 E2 charge；局部边 core 为 gcd(M_w,M_w',C_w'(M_w' mod p))，等于 1 时没有非平凡旧账本可跨边并在目标 E2 通过。若同一张 sound/complete 物理表还给出持续旧账本、实际相位匹配且碰撞至多为 eta 的 demand_to_slot，则其 q-primary 需求必满足 D_tau <= eta |I| min(e,v_q(CarryCore))；这个必要不等式不构造该映射。标准 c=3 参数的单行局部筛满足 gcd(26h+1,(24h-2)2h)=19 当且仅当 h=8 (mod 19)，否则为 1；在该同余类还存在一个同图表、两条不同 cofactor-overflow determinant 行的 A=19 算术 pair，且其两行 CarryCore 恰为 19。后二者均不构造 raw source、sound/complete transcript、F 层、terminal 或 selector 证书。p=73 给出严格正、负 overflow 控制；p=5281 的 Jacobi-odd raw rows 则在 E2 之前失败，因为 4M-n=R=p-2<p，不能把它们误作为 cofactor-overflow lift。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-cofactor-ledger-e2-gate
  - type-I-overflow-e2-fixed-fiber-constancy
  - type-I-fg-physical-carry-arc-lift-interface
  - type-I-g-anchor-jacobi-odd-p5281-physical-row-ledger
topics:
  - type-I
  - F-state
  - G-state
  - source-map
  - raw-transition
  - overflow
  - E2
  - carry
  - gcd
  - q-primary
  - capacity
  - proof-boundary
sources:
  - claim: type-I-fg-physical-carry-arc-lift-interface
    role: single-row-carry-interface
  - claim: type-I-g-anchor-jacobi-odd-p5281-physical-row-ledger
    role: physical-raw-scope-control
  - reproduction: reproductions/type_i_raw_transcript_persistent_carry_core.py
    role: carry-core-controls
visibility: public
last_checked: '2026-08-07'
---

# raw transcript 中持续 E2 账本的 gcd carry core

## 1. 输入与定义

固定核心素数 \(p\)。设 \(\mathcal T\) 是一个已经由独立算术命题给出
sound raw-to-overflow 意义的有限物理行 transcript。每行 \(i\) 有

\[
pn_i=4M_i d_i+1,
\qquad
C_i=p-d_i,
\qquad
r_i=M_i\bmod p\in\{1,\ldots,p-1\},
\tag{1}
\]

并满足当前 cofactor-overflow 的严格域条件 \(4M_i-n_i>p\)。令
\(I\) 是其中必须检查 E2 的行集合。定义

\[
\boxed{
\operatorname{CarryCore}(\mathcal T,I)
=\gcd\left(\{M_i:i\in\mathcal T\}
\cup\{C_i r_i:i\in I\}\right).
}
\tag{2}
\]

这里的所有 gcd 都是正整数 gcd。它不是从 Fourier 相位推得的有限群量，而是实际
integer carriers 的共同不变量。

## 2. 持续账本充要判据

设一个旧 ledger \(A>0\) 必须在 transcript 的每行保留：

\[
A\mid M_i\qquad(i\in\mathcal T).
\tag{3}
\]

该行的 E2 条件是

\[
\frac{A}{(A,C_i)}\mid r_i.
\tag{4}
\]

于是有精确等价：

\[
\boxed{
A\text{ 满足 (3) 且在所有 }i\in I\text{ 通过 E2}
\quad\Longleftrightarrow\quad
A\mid\operatorname{CarryCore}(\mathcal T,I).
}
\tag{5}
\]

**证明。** 固定一行，写 \(g=(A,C_i)\)、\(A=ga\)、\(C_i=gc\)。则
\((a,c)=1\)，故

\[
\frac{A}{(A,C_i)}\mid r_i
\Longleftrightarrow a\mid r_i
\Longleftrightarrow A\mid C_i r_i.
\tag{6}
\]

与所有 (3) 和所有 E2 行的 (6) 取交，即为 (5)。证毕。

因此 (2) 是最大的、在整除偏序下可从根持续携带的 E2 charge。若 ledger 允许单调增长

\[
A_0\mid A_i\mid M_i,
\tag{7}
\]

且每个 \(i\in I\) 的 \(A_i\) 在该行通过 E2，则 (6) 仍给出
\(A_0\mid\operatorname{CarryCore}(\mathcal T,I)\)；反过来任意整除 (2) 的 \(A\)
取常值 \(A_i=A\) 即可在 \(I\) 的行实现。故允许中间加账本并不能绕过这个 root
charge 上界。

对一条 raw-to-overflow 边 \(w\to w'\)，目标行需 E2 时的局部版本为

\[
\boxed{
\operatorname{CarryCore}(w,w')
=\gcd(M_w,M_{w'},C_{w'}r_{w'}).
}
\tag{8}
\]

若它等于 \(1\)，任何非平凡旧 ledger 都不能跨这条边并在目标行 E2 通过。

## 3. p=73 的物理 overflow 正、负控制

负控制为

\[
(p,A,M,C,d,n)=(73,34,1598,57,16,1401).
\tag{9}
\]

它确为 physical overflow：

\[
73\cdot1401=4\cdot1598\cdot16+1,
\qquad
4\cdot1598-1401=4991>73.
\tag{10}
\]

此时 \(r=65\)，并且

\[
\operatorname{CarryCore}=\gcd(1598,57\cdot65)=1.
\tag{11}
\]

所以 \(A=34\) 严格失败；等价地

\[
\left\lfloor1598/73\right\rfloor=21\not\equiv0\pmod {34}.
\tag{12}
\]

正控制取

\[
(p,A,M,C,d,n)=(73,69,10626,69,4,2329),
\tag{13}
\]

并有

\[
73\cdot2329=4\cdot10626\cdot4+1,
\qquad r=41,
\qquad
\operatorname{CarryCore}=\gcd(10626,69\cdot41)=69.
\tag{14}
\]

由于 \(A/(A,C)=1\)，完整 \(A=69\) 通过 E2。两例共同证明 (2) 不是只会排除候选的
失败筛，而是精确的正、负判据。

## 4. p=5281 的更早 scope 失败

已有 Jacobi-odd physical raw ledger 的每行满足

\[
n_\delta=4M_\delta-R,
\qquad R=5279=p-2.
\tag{15}
\]

故

\[
4M_\delta-n_\delta=R<p.
\tag{16}
\]

它们不是这里假设的 cofactor-overflow 行；不能把 (2) 误称为这些 raw 边上的合法 E2
gate。即使只作不具递归语义的诊断，菜单首边

\[
7\xrightarrow{13}91
\tag{17}
\]

也已有

\[
M_7=278784,\quad M_{91}=6969600,\quad C_{91}=1,
\quad r_{91}=3961,
\tag{18}
\]

从而

\[
\gcd(M_7,M_{91},C_{91}r_{91})=1.
\tag{19}
\]

这只表明：若未来某个合法 raw-to-overflow map 保留这里的 \(M_7,M_{91},C_{91}\)（或
另证其 carry core 不变），并试图从该边持续携带一个非平凡旧 charge，则会遇到 carry
障碍。它不把当前 G/Jacobi rows 伪装成 overflow E2 edge，也不限制可重图表后具有不同
物理 carrier 的未来 map。

## 5. 持久 E2 q-slot 的必要条件

本节只把已经存在的持续旧账本转换成一个**必要的** q-primary 计数上界；它不把
Fourier deficit 自动变成 q-height。令 \(\bar H\) 是一个预先固定的 F 商，\(\tau\) 是其目标对合，
\(\psi:\bar H\to\mu_{q^e}\) 是阶为 \(q^e\) 的角色，其中 \(q\) 为奇素数、\(e\ge1\)，并写

\[
\psi_k=\psi^{q^{e-k}}\qquad(1\le k\le e).
\tag{20}
\]

给定固定表示数 \(c\)，把 anti-target deficit 的每个单位保留为一个不同的需求 occurrence：

\[
\mathscr D_\tau=
\{(x,a):x\in\bar H,\ 1\le a\le[c(x)-c(\tau x)]_+\},
\qquad
|\mathscr D_\tau|=D_\tau.
\tag{21}
\]

为避免把 history clone 或事后相位选择计入容量，以下前提必须全部实际成立：

1. \(\mathcal T\) 是对所声明 transition universe sound **且 complete** 的
   cofactor-overflow 物理行表，每个物理行只按一次 canonical occurrence 计数；\(I\subseteq
   \mathcal T\) 正是需要 E2 的物理行集。
2. 一个旧账本 \(A_0>0\) 持续存在：每行有有效账本 \(A_i\) 满足
   \(A_0\mid A_i\mid M_i\)，且每个 \(i\in I\) 的 \(A_i\) 通过 E2。
3. 每个 \(w\in I\) 已有由独立 source semantics 强制出的 row-to-anchor 标记
   \(\bar j_w\)；每个需求 \(\delta\in\mathscr D_\tau\) 的相位标签
   \(\sigma(\delta)\in\bar H\) 由表示构造预先固定，而不是在查看 slot 后选择。
4. 存在一个实际的、有界碰撞 `demand_to_slot` 映射 \(f\)，其中

\[
h(A_0)=\min\{e,v_q(A_0)\},
\qquad
\operatorname{Slot}_{q,A_0}=I\times\{1,\ldots,h(A_0)\},
\qquad
f:\mathscr D_\tau\longrightarrow\operatorname{Slot}_{q,A_0},
\tag{22}
\]

   并且对某个 \(\eta\ge1\)，每个 slot 至多有 \(\eta\) 个原像，且若
   \(f(\delta)=(w,k)\)，则有实际相位匹配

\[
\psi_k(\sigma(\delta))=\psi_k(\bar j_w).
\tag{23}
\]

这里 (22) 的一个 \((w,k)\) 表示同一个持续旧账本 \(A_0\) 在物理 E2 行 \(w\) 的第
\(k\) 个 q-primary 层；它不是 raw edge 数、tail occurrence 数或单独 Fourier phase
的别名。

**定理（ledger-supported q-slot 必要条件）。** 在上述前提下，令
\(\mathcal C=\operatorname{CarryCore}(\mathcal T,I)\)。则

\[
\boxed{
A_0\mid\mathcal C,
\qquad
D_\tau\le\eta\,|I|\min\{e,v_q(\mathcal C)\}.
}
\tag{24}
\]

**证明。** 前提 2 正是第 2 节的持续账本条件，故由 (5) 有
\(A_0\mid\mathcal C\)。因此

\[
|\operatorname{Slot}_{q,A_0}|
=|I|\min\{e,v_q(A_0)\}
\le |I|\min\{e,v_q(\mathcal C)\}.
\tag{25}
\]

前提 4 的碰撞界给出

\[
D_\tau=|\mathscr D_\tau|
\le\eta|\operatorname{Slot}_{q,A_0}|.
\tag{26}
\]

与 (25) 合并即得 (24)。相位匹配 (23) 不是这一步鸽巢计数所需的额外因子；它是排除
“只按 slot 数任意配对需求与行”的实现前提。证毕。

(24) 的逆命题为假作为构造原则：即使数值不等式成立，也不会产生 \(A_i\)、E2 通过、
\(\bar j_w\)、\(\sigma\) 或映射 \(f\)，更不会证明共同 affine law、E4 解提升或 E5
递降。特别地，\(\operatorname{CarryCore}\) 的 q-adic valuation 只能限制一个已注册的
ledger-supported `demand_to_slot`，不能把任意 Fourier deficit 自动提升为物理容量。

## 6. 标准 \(c=3\) 的单行局部 core 同余筛

以下是一个为后续 receipt 筛选准备的纯算术计算，不是新的 physical transcript。令

\[
p=24h+1,
\qquad M=26h+1,
\qquad C=p-3=24h-2,
\qquad h>0.
\tag{27}
\]

则

\[
M=p+2h,
\qquad 0<2h<p,
\qquad r:=M\bmod p=2h.
\tag{28}
\]

因为 \(M\) 为奇数且 \((M,h)=1\)，有 \((M,2h)=1\)。故这个行的局部
E2 core 筛恰为

\[
\gcd(M,Cr)=\gcd(26h+1,(24h-2)2h)=\gcd(26h+1,24h-2).
\tag{29}
\]

而

\[
13(24h-2)-12(26h+1)=-38.
\tag{30}
\]

所以 (29) 的 gcd 整除 \(38\)，又因 \(M\) 为奇数而只能为 \(1\) 或 \(19\)。最后

\[
\begin{aligned}
19\mid M
&\Longleftrightarrow 7h+1\equiv0\pmod {19}
\Longleftrightarrow h\equiv8\pmod {19},\\
19\mid C
&\Longleftrightarrow 5h-2\equiv0\pmod {19}
\Longleftrightarrow h\equiv8\pmod {19}.
\end{aligned}
\tag{31}
\]

因而得到精确筛：

\[
\boxed{
\gcd(M,C(M\bmod p))=
\begin{cases}
19,&h\equiv8\pmod {19},\\
1,&h\not\equiv8\pmod {19}.
\end{cases}}
\tag{32}
\]

这只是一个**单行**局部计算。它没有断言 \(p\) 是素数，也没有给出 actual raw source、
sound/complete physical transcript、F fixed layer、E2 admission、terminal-first 状态、
q-primary character、`demand_to_slot`、E4 或 E5。即使某个 future c=3 receipt 取
\(h\equiv8\pmod {19}\)，仍须逐项补齐这些独立前提，才可能把 (32) 用作 (24) 的
ledger charge 输入。

有限复现逐一检查模 \(19\) 的 19 个代表元，并保存 \(h=8\) 的纯算术正控制
\((M,C,r,\mathrm{core})=(209,190,16,19)\)，以及实际 p=7129 control 的
\(h=297\)、\((M,C,r,\mathrm{core})=(7723,7126,594,1)\)。这不是 range scan。

## 7. 标准 \(c=3\) 同图表的两行 \(A=19\) 算术 pair

现在固定 \(h\equiv8\pmod {19}\) 且 \(h>0\)，并继续使用 (27) 的
\(p,M_0,C_0\)。写

\[
h=8+19t,
\qquad
\mu=26t+11,
\qquad
\gamma=24t+10.
\tag{33}
\]

因 \(h>0\)，必有 \(t\ge0\)。于是

\[
M_0=19\mu,
\qquad
C_0=19\gamma,
\qquad
p=19\gamma+3,
\qquad
R=104h-9=76\mu-13.
\tag{34}
\]

令 \(K=M_0C_0=19^2\mu\gamma\)。除了原来的 \(c=3\) 行，再取同一个
\((p,R,K)\) 图表的互补因子行：

\[
\begin{array}{c|c|c|c|c}
 i&M_i&C_i&d_i=p-C_i&n_i=4M_i-R\\ \hline
0&19\mu&19\gamma&3&13\\
1&19\mu\gamma&19&p-19&76\mu(\gamma-1)+13.
\end{array}
\tag{35}
\]

**命题（两行 \(A=19\) 算术证书）。** 若参数 \(p=24h+1\) 在所用语义中是核心素数，
则 (35) 是两条不同的 cofactor-overflow determinant 行；候选旧账本 \(A=19\) 在两行都
通过 E2。若声明 \(\mathcal T=I=\{0,1\}\)，则

\[
\boxed{
\gcd\bigl(M_0,M_1,C_0(M_0\bmod p),C_1(M_1\bmod p)\bigr)=19.
}
\tag{36}
\]

**证明。** 由 (33)，直接消元得到

\[
13\gamma-12\mu=-2,
\qquad
19\mu-26h=1.
\tag{37}
\]

特别地 \((\mu,\gamma)=(\mu,h)=1\)，且 \(\mu\) 为奇数。第一行的 determinant
恒等式可写作

\[
p\cdot13=4(19\mu)\cdot3+1,
\tag{38}
\]

它正是 (37) 的第一式乘以 \(19\) 后的重排。又由同一式，

\[
pR=(19\gamma+3)(76\mu-13)=76(19\mu\gamma)-1,
\tag{39}
\]

故第二行满足

\[
p\bigl(4M_1-R\bigr)=4M_1(p-19)+1.
\tag{40}
\]

两行都有 \(4M_i-n_i=R\)，而

\[
R-p=80h-10>0,
\tag{41}
\]

所以均处于 cofactor-overflow 域。它们不同，因为 \(M_1>M_0\) 且 \(C_1<C_0\)
（\(\gamma\ge10\)）。两个 \(M_i\) 都被 \(19\) 整除，且两个 \(C_i\) 也被 \(19\)
整除，因此 \(A/(A,C_i)=1\)，两行的 E2 自动通过。

为计算 (36)，第一行的余数是 \(r_0=2h\)，第二行的余数是
\(r_1=p-3\mu=378t+160\)。由于

\[
\gcd(M_0,M_1,C_0r_0)
=\gcd(19\mu,19\mu\gamma,38\gamma h)=19,
\tag{42}
\]

左侧的四项 gcd 至多为 \(19\)。这里最后一个等式只使用
\((\mu,\gamma)=(\mu,h)=1\) 和 \(\mu\) 为奇数。另一方面每个
\(M_i\) 与每个 \(C_ir_i\) 都被 \(19\) 整除：对 \(i=0\) 由 (34)，对 \(i=1\)
由 \(C_1=19\)。所以整个 gcd 恰为 \(19\)，证毕。

这个命题只消除了“需要两条不同 physical determinant 行且候选 \(19\)-账本能在两行
通过 E2”这一**算术**障碍。它没有产生一个持续旧账本，也没有给出第二行的 raw source
word；第一行与第二行也尚未组成 sound/complete transcript。尤其 \(d_1=p-19\)，不是第二条 \(d=3\) 行。
它同样不声明 F fixed layer、terminal-first 状态、角色、相位/anchor、
`demand_to_slot`、E4、E5、解提升或递降。

在 \(h=8\)、\(p=193\) 的有限正控制中，(35) 具体为

\[
(M_0,C_0,d_0,n_0,r_0)=(209,190,3,13,16),
\]

\[
(M_1,C_1,d_1,n_1,r_1)=(2090,19,174,7537,160),
\tag{45}
\]

并且其两行 CarryCore 为 \(19\)。复现仅检查这些符号恒等式和该正控制。

对 \(h=255\)、\(p=6121\)，这组两行还各自有同一 declared universal source 下的逐步
raw receipt，见 [p=6121 的同源双叶控制](type-I-g-anchor-c3-core19-dual-leaf-raw-tree-p6121.md)。
该点已有 direct Type II terminal，且没有 \(19\)-primary unit-group character；所以它只把
本节的纯算术 pair 升级为一个 raw-provenance 正控制，不把 (24) 的物理表、q-slot 映射或
selector 接口自动补齐。

## 8. 接入边界

`CarryCore` 只有在 raw 行与 transition universe 已独立证明 sound/complete、并且行确属
cofactor-overflow 后才能调用。它不创建 source map，不从 finite Fourier/SNF 相位推出
E2，也不提供 E1、E3、E4、E5、解提升或严格递降。其作用是把“一个旧账本能否跨实际
物理 transcript 持续存活”压缩为一个可重算 gcd gate。

窄复现：

```bash
python3 reproductions/type_i_raw_transcript_persistent_carry_core.py --verify
```
