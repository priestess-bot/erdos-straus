---
kind: claim
claim_id: type-I-overflow-full-product-d-one-a-one-split-carrier-stutter-relay
title: 完整乘积 d=1 的 a=1 双侧载荷正规形、stutter 继电与无限族严格旁路
statement: >-
  在完整乘积 d=1 的 a=1 图表中，primitive peeled node x+y=R 的两侧若都有完整超额块
  x=Q_x beta_x、y=Q_y beta_y，则存在精确的带颜色来源恒等式
  4c_0 beta_x beta_y=pQ_x beta_x+pQ_y beta_y+1，其中
  c_0=K/(beta_x beta_y)；联合 support 的唯一 multiplier 为
  L=(Q_x/gcd(A,Q_x))(Q_y/gcd(A,Q_y))。这给出确定的 split-carrier
  算术正规形与 identity-lift candidate；现有单侧 E1/E3 不蕴含“双侧块可原子联合收费”，
  后续独立的 atomic split primitive 已给出这一新接口的条件准入 schema，但不改写旧单侧 action，
  两条逐侧 raw 分支也不能在两个顺序中都保留原始完整块而形成交换菱形，因此本卡不把它
  登记为 verified edge。在固定 receipt
  cell 中，L=1 (mod p) 是一个至多二次的剩余条件；根锚 p+1 的最小 cell
  (beta_x,beta_y)=(2,3) 具有判别式 -23。若条件性 split target stutter，写
  L=1+ps，则目标仍是 a=1、d=1，且下一完整超额倍率 E' 满足 E'=s (mod p)：除
  s=0 外，现有严格 carry、p 进倒计时或最小互素素数源接管。最后，对
  p=73、r_k=50+k*2464177192963200 的每个 k>=0，真实节点上的联合 canonical 算术都
  stutter；但同一路径的
  容量锚 h=3 总产生合法单侧完整超额 receipt，并严格降到 canonical capacity 2。因此对任一
  已 persistent 入队且完成 typed-target 重分类的该族实例，现有单侧宏给出严格候选出口；全局
  剩余已收缩为关闭 s=0 与其它 endpoint-terminal 未命中状态。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-full-product-d-one-a-one-two-sided-capacity-tree-no-go
  - type-I-universal-p-source-capacity-anchor-orbit
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
  - type-I-overflow-full-product-d-one-p-adic-regeneration-countdown
  - type-I-chart-least-coprime-prime-anchor-source
  - type-I-f-qadic-numerator-lift-rigidity-and-gcd-reduction
  - short-certificate-equivalence
  - denominator-escape-state-contract
topics:
  - type-I
  - overflow
  - full-product
  - d-one
  - a-one
  - split-carrier
  - complete-excess-bundle
  - source-provenance
  - carry-stutter
  - p-adic-countdown
  - infinite-family
  - terminal-first
  - proof-boundary
sources:
  - claim: type-I-overflow-full-product-d-one-a-one-two-sided-capacity-tree-no-go
    role: double-excess-source-boundary-and-fixed-stutter
  - claim: type-I-universal-p-source-capacity-anchor-orbit
    role: actual-capacity-peeling-to-endpoint-semantics
  - claim: type-I-bottom-sink-scc-complete-excess-bundle-selector
    role: existing-single-side-path-anchored-receipt-contract
  - claim: type-I-overflow-full-product-d-one-p-adic-regeneration-countdown
    role: d-one-residue-dispatch-and-regeneration-rank
  - claim: type-I-chart-least-coprime-prime-anchor-source
    role: raw-p-failure-alternate-source
  - claim: type-I-f-qadic-numerator-lift-rigidity-and-gcd-reduction
    role: native-pair-Type-II-terminal-criterion
  - claim: short-certificate-equivalence
    role: complete-direct-Type-I-II-boundary
  - concept: denominator-escape-state-contract
    role: e1-e5-persistent-edge-contract
  - reproduction: reproductions/type_i_overflow_d_one_a_one_split_carrier_stutter_relay.py
    role: focused-colored-source-stutter-relay-and-infinite-family-receipts
visibility: public
last_checked: '2026-08-13'
---

# 完整乘积 \(d=1\) 的 \(a=1\) 双侧载荷正规形、stutter 继电与无限族严格旁路

## 1. 证据分层

本卡接续双侧容量树 no-go，只研究 peeled node 的两侧都超过 \(K\) 容量时还能做什么。
为避免把换图表的算术恒等式误写成证明边，先固定三层结论：

1. 第 2--4 节是无条件整数恒等式与来源 no-go；
2. 第 5 节是“若新的 split 来源合同获准”之后的条件性 target 继电；
3. 第 6 节的 \(h=3\) 单侧 receipt 使用现有 path-anchored 合同，不依赖 split 合同。

因此，本卡建立了 split-carrier 的**唯一候选正规形**，但没有宣称
`atomic_two_sided_disjoint_complete_excess_charge` 已经由现有 E1/E3 推出。后续
[双侧完整超额原子来源的条件准入 schema](type-I-path-anchored-atomic-split-complete-excess-admission.md)
把它定义为新的不可拆分 primitive，并证明完整 verifier receipt 条件性满足 E1--E4；
该结果不是 registry 已实现的声明，也不是对旧单侧合同的反向改写。

## 2. 带颜色的双侧来源恒等式

固定核心素数 \(p\equiv1\pmod {24}\) 及图表

\[
4K=pR+1,
\qquad
A\mid K.
\tag{1}
\]

设同一条已重放 raw path 到达 primitive node

\[
x+y=R,
\qquad
(x,y)=1.
\tag{2}
\]

分别按 \(K\) 容量抽取两侧全部完整超额素数幂块：

\[
x=Q_x\beta_x,
\qquad
y=Q_y\beta_y.
\tag{3}
\]

即 \(Q_x\) 包含全部满足 \(v_q(x)>v_q(K)\) 的完整 \(q^{v_q(x)}\) 块，\(Q_y\)
同理。若 \(Q_x,Q_y>1\)，则

\[
(Q_x,\beta_x)=(Q_y,\beta_y)=1,
\qquad
(Q_x\beta_x,Q_y\beta_y)=1,
\tag{4}
\]

而且

\[
\beta_x\beta_y\mid K.
\tag{5}
\]

令

\[
c_0=\frac{K}{\beta_x\beta_y}.
\tag{6}
\]

把 (2)--(3) 代入 (1)，得到精确的双色来源恒等式

\[
\boxed{
4c_0\beta_x\beta_y
=pQ_x\beta_x+pQ_y\beta_y+1.}
\tag{7}
\]

式 (7) 保留了每个超额块来自哪一侧；若只保存无色乘积 \(Q_xQ_y\)，这项 provenance
会丢失。带符号指数向量

\[
z_q=v_q(x)-v_q(y)
\tag{8}
\]

又唯一恢复两种颜色，所以候选 receipt 不允许任选子块：它必须由 (8) 的正、负完整
超额支撑确定。

令

\[
g_x=(A,Q_x),
\qquad
g_y=(A,Q_y),
\tag{9}
\]

并假设 \(p\nmid Q_xQ_y\)。由于 \((Q_x,Q_y)=1\)，规范联合 support 与倍率唯一为

\[
M=\operatorname{lcm}(A,Q_x,Q_y),
\tag{10}
\]

\[
\boxed{
L=\frac MA
=\frac{Q_x}{g_x}\frac{Q_y}{g_y}.}
\tag{11}
\]

每个 \(q\mid Q_xQ_y\) 的完整块指数都严格大于 \(v_q(K)\ge v_q(A)\)，所以

\[
M>A,
\qquad
M\nmid K,
\qquad
p\nmid M.
\tag{12}
\]

因此 (10) 有唯一 canonical target

\[
c_M=\langle(4M)^{-1}\rangle_p,
\quad
K_M=Mc_M,
\quad
R_M=\frac{4K_M-1}{p}.
\tag{13}
\]

式 (2)--(13)、原 raw path、双色完整块 maximality 及 target 哈希，足以定义一个确定的
`path_anchored_split_complete_excess_bundle_v1` **候选回执**；在解集语义上，它的
E4 只能是 \(\operatorname{Sol}(p)\) 的恒等映射，不读取也不制造一个解。

但是，现有单侧 E1/E3 的来源语法是

\[
u+Q\beta=R,
\qquad
u\beta\mid K.
\tag{14}
\]

当 \(Q_x,Q_y>1\) 时，两种定向都由 residual gate 排除。式 (7) 是一个新的、严格得多
的来源 normal form，却不等于“现有单侧合同已经蕴含双侧原子收费”。在这个新原子规则
被独立证明兼容状态语义和全局 selector 之前，(10)--(13) 仍是
`candidate_transition`，不是 `verified_edge`。

## 3. 两条逐侧分支不能代替原子合同

设先把 \(x\) 侧全部真实超额层剥到

\[
g_x^{\rm cap}=(x,K),
\qquad
E_x=\frac{x}{g_x^{\rm cap}}.
\tag{15}
\]

另一侧随之变为

\[
R-g_x^{\rm cap}
=y+g_x^{\rm cap}(E_x-1).
\tag{16}
\]

因为 \(Q_y\mid y\) 且 \((Q_y,g_x^{\rm cap})=1\)，原来的 \(Q_y\) 在新另一侧完整保留
当且仅当

\[
Q_y\mid E_x-1.
\tag{17}
\]

又 \(E_x\le Q_x\)，所以 (17) 强制

\[
Q_y\le E_x-1<Q_x.
\tag{18}
\]

反向先剥 \(y\) 则同理要求 \(Q_x<Q_y\)。两种“保留另一侧原始完整块”的条件不可能
同时成立。因此逐侧 raw branch 不能靠两个顺序都保留 \((Q_x,Q_y)\) 来形成交换菱形，
也就不能把这种旧 action 复合冒充为 (7) 的对称联合来源。该论证不排除中途重新计算
完整块后出现其它动态路径；那类路径必须用新的实际 receipt 独立验证。

固定 \(p=73,r=1\) 的 peeled node 给出

\[
(Q_x,\beta_x)=(761905,1),
\qquad
(Q_y,\beta_y)=(143,74).
\tag{19}
\]

先剥 \(x\) 确实满足 \(143\mid761905-1\)，而反向有
\(761905\nmid143-1\)。这个例子说明单一顺序偶尔可保留另一块，但不存在全称的双向
composition 证明。

## 4. 固定 receipt cell 中的 stutter 二次式

回到完整乘积 \(d=1\) 的 \(a=1\) 图表：

\[
g=\frac{p+1}{2},
\qquad
b=2pr-1,
\qquad
n=(p+1)b-1,
\tag{20}
\]

\[
A=\frac{pn-1}{4},
\qquad
R=(p-1)n-1,
\qquad
K=A(p-1).
\tag{21}
\]

这里 \(R\equiv1\pmod p\)。在任一双 \(p\)-free peeled node 中，令

\[
B=\beta_x\beta_y g_xg_y\pmod p.
\tag{22}
\]

由 (3)、(11) 及 \(x+y\equiv1\pmod p\)，有

\[
\boxed{
L\equiv\frac{xy}{B}
\equiv\frac{y(1-y)}B\pmod p.}
\tag{23}
\]

所以在固定 \((\beta_x,\beta_y,g_x,g_y)\) receipt cell 内，联合 carry stutter 精确为

\[
\boxed{L\equiv1\pmod p
\Longleftrightarrow
y(1-y)\equiv B\pmod p.}
\tag{24}
\]

它是判别式 \(1-4B\) 的二次条件，每个固定 cell 至多占两个 \(y\pmod p\) 类，而不是
一个无结构余项。

特别地，从根锚 \(u=p+1\) 做一次真实 \(p\)-peel 时

\[
x\equiv2r+3,
\qquad
y\equiv-2(r+1)\pmod p.
\tag{25}
\]

在最小 cell

\[
(\beta_x,\beta_y,g_x,g_y)=(2,3,1,1)
\tag{26}
\]

中，(24) 等价于

\[
\boxed{2r^2+5r+6\equiv0\pmod p,}
\tag{27}
\]

其判别式为 \(-23\)。对核心素数 \(p\)，二次互反给出

\[
\left(\frac{-23}{p}\right)=\left(\frac p{23}\right).
\tag{28}
\]

因此这张 cell 有根当且仅当 \(p\bmod23\) 是非零平方类；有根时恰有两个类

\[
r\equiv\frac{-5\pm\sqrt{-23}}4\pmod p.
\tag{29}
\]

这只分类了固定 receipt cell；\(\beta_i,g_i\) 随状态改变时，不能把 (27) 当作全部
split stutter 的统一分类。

## 5. 条件性 split stutter 的 \(d=1\) 继电

本节额外假设 (7) 已通过后续原子 split schema 要求的完整 E1--E4 verifier。若 (11) 满足

\[
L\equiv1\pmod p,
\qquad
s=\frac{L-1}{p},
\tag{30}
\]

则 (13) 的 target cofactor 仍为 \(p-1\)。定义

\[
n'=Ln-s.
\tag{31}
\]

与已有 canonical 再生恒等式相同，直接得到

\[
M=AL=\frac{pn'-1}{4},
\quad
R_M=(p-1)n'-1,
\quad
K_M=M(p-1).
\tag{32}
\]

更强的是，target 仍在 \(a=1\) 正规形。令

\[
b'=bL-s.
\tag{33}
\]

由 \(L=1+ps\) 有

\[
n'=(p+1)b'-1,
\qquad
b'\equiv-1-s\pmod p.
\tag{34}
\]

target 的普通 complete-excess 倍率为

\[
E'=(p-1)b'-1,
\tag{35}
\]

从而

\[
\boxed{E'\equiv s\pmod p.}
\tag{36}
\]

这给出 split stutter 后的完整算术分派：

\[
\begin{array}{c|c}
s\pmod p & \text{下一动作} \\ \hline
0 & E'\equiv0:\ p\text{-free 门失败，返回 }a=1\text{ hard branch}\\
1 & E'\equiv1:\ \text{进入已有 }p\text{ 进再生倒计时}\\
-1 & b'\equiv0:\ \text{raw }p\text{-source 失败，由最小互素素数源给 }c=1\\
\text{其它} & c'=\langle-s^{-1}\rangle_p\le p-2\text{，严格 carry}.
\end{array}
\tag{37}
\]

所以一个获准的 split stutter 不会产生新的无分类状态；真正重复原 hard branch 的唯一
剩余类是

\[
\boxed{s\equiv0\pmod p.}
\tag{38}
\]

式 (37) 仍须逐项通过 persistent parent、typed target、terminal-first 和 E5；它是
精确的 adapter dispatch，不是脱离状态合同的全局证明。

## 6. 一个无限真实 stutter 族及统一 \(h=3\) 严格旁路

取

\[
p=73,
\qquad
W=p(p^2-1)(p^2+p+1)(p^2+1)(3p+1)
=2464177192963200,
\tag{39}
\]

\[
r_k=50+kW,
\qquad
k\ge0.
\tag{40}
\]

令

\[
T=p^2r-g,
\qquad
A=gT,
\qquad
K=\frac{p^2-1}{2}T.
\tag{41}
\]

根锚 \(u=p+1=74\) 始终整除 \(K\)，且

\[
p\parallel R-u
\tag{42}
\]

因为 \(R-u\equiv-2p(r+1)\pmod {p^2}\) 且 \(r_k\equiv50\not\equiv-1\pmod p\)。
做这一个真实 \(p\)-edge 后定向为

\[
y=\frac{R-u}{p}
=2p^2r-p-2r-2,
\tag{43}
\]

\[
x=R-y
=2p^3r-2p^2r-p^2-2pr+2r+3.
\tag{44}
\]

再令 \(z=R-3\)。以下三个消元恒等式控制全部 gcd：

\[
p^2x-2(p-1)(p^2-1)T=p^2+1,
\tag{45}
\]

\[
p^2y-2(p^2-1)T=-(p^2+p+1),
\tag{46}
\]

\[
p^2z-2p(p^2-1)T=-p(3p+1).
\tag{47}
\]

步长 (39) 同时被 \(p\)、\(p^2-1\)、\(p^2+p+1\)、\(p^2+1\) 与 \(3p+1\)
整除，所以 (45)--(47) 中的相关剩余和模 \(p^2-1\) 的容量剩余都冻结在 \(k=0\)。
基点直接给出

\[
(x,T)=(y,T)=(z,T)=1,
\tag{48}
\]

\[
(x,p^2-1)=2,
\qquad
(y,p^2-1)=3,
\qquad
(z,p^2-1)=4.
\tag{49}
\]

因此对每个 \(k\ge0\)，

\[
\boxed{(x,K)=2,
\qquad
(y,K)=3,
\qquad
(R-3,K)=4.}
\tag{50}
\]

相应完整块为

\[
Q_x=\frac x2,
\qquad
Q_y=\frac y3,
\qquad
Q_3=\frac{R-3}{4}.
\tag{51}
\]

式 (45)--(49) 还给出

\[
(Q_x,A)=(Q_y,A)=(Q_3,A)=1,
\qquad
p\nmid Q_xQ_yQ_3.
\tag{52}
\]

具体地，步长也冻结模 \(p+1=74\) 的商剩余，而基点满足

\[
(Q_x,Q_y,Q_3)\equiv(1,49,55)\pmod {74}.
\]

它们都与 \(g=37\) 互素；结合 (48) 即得 (52)。

而 \(r_k\equiv50\pmod {73}\) 使

\[
Q_x\equiv15,
\qquad
Q_y\equiv39,
\qquad
Q_xQ_y\equiv1\pmod {73}.
\tag{53}
\]

所以每个 \(k\) 都在真实双侧完整超额节点上产生 split canonical arithmetic
stutter；这句话不把条件性 split candidate 登记为 edge。基点的联合倍率为

\[
L=3405557677775,
\qquad
\frac{L-1}{73}\equiv65\pmod {73},
\tag{54}
\]

故若强行采用条件性 split edge，(37) 的下一普通 carry 已严格给
\(c'=-65^{-1}\equiv64\pmod {73}\)。

但这条族有更早、且不依赖新 split 合同的严格候选出口。由 (50)，从 peeled node 的 \(y\) 侧做
真实容量剥离会到达锚 \(h=3\)。在节点 \(\{3,R-3\}\) 上，(50)--(51) 给出

\[
3+4Q_3=R,
\qquad
3\cdot4=12\mid K,
\qquad
(Q_3,12)=1.
\tag{55}
\]

这正是现有单侧 path-anchored complete-excess receipt；把它登记为全局 edge 时，仍沿用
既有 selector 的 persistent-parent 与 typed-target gates。又

\[
Q_3\equiv-\frac12\equiv36\pmod {73},
\tag{56}
\]

故 support \(M_3=AQ_3\) 的 canonical cofactor 为

\[
\boxed{c_3=-Q_3^{-1}\equiv2<72.}
\tag{57}
\]

于是 (39)--(40) 是“真实节点上的 split canonical 算术可无限 stutter”的严格反例族。
同时，对任一已 persistent 入队且通过 typed-target/terminal-first gates 的该族实例，
endpoint-first 单侧动作都给出严格候选出口；两句话缺一不可。这里不把尚未序列化的 target
直接称为全局闭合。

## 7. terminal-first 的精确边界

formal raw path 固定同一个 chart data \((p,R,K,A)\)。所以：

1. 只依赖 \(p\) 的完整直接 Type I/II 谓词沿路径不变；
2. 只依赖固定 chart data 的 centered、neighbor、dyadic 或 Fourier 状态谓词也沿路径不变；
3. 读取当前坐标真因子的 candidate generator 可以变化，但每个命中必须另跑完整 verifier。

前一张卡的 \(P/M\) 容量宏内部也不会自己产生 bottom Type I。严格中间坐标仍有超过
\(K\) 容量的素数幂，故不整除 \(K\)；到达树内容量端点 \(v\mid K\) 时，
\(v\equiv R\equiv1\pmod p\)，所以另一侧满足 \(p\mid R-v\)，而 \(p\nmid K\)，
仍不整除 \(K\)。因此这些宏全程都没有两坐标乘积整除 \(K\)。这句话不推广到任意
不满足 \(v\equiv1\pmod p\) 的容量 endpoint；例如第 6 节的 \(h=3\) 必须独立核验。

若直接把某个 primitive pair \(a+b=R\) 当作 Type II 的两因子，已有 numerator
正规形给出的必要充分条件是存在合法 \(h\) 满足

\[
h\mid R,
\qquad
4ab\mid p+h.
\tag{58}
\]

特别地 \(ab\le(p-1)/2\)。在 (39)--(40) 这类巨大 peeled coordinates 上，整对坐标
不可能满足该大小门；可能的新 terminal 只能来自坐标真因子、外部 gap、换图表或独立
全局扫描。

不能用选择 \(r\) 的 CRT 去避开一个固定 \(p\) 的**完整**直接 Type I/II 菜单：该菜单
只依赖 \(p\)。若证明某个 \(p\) 的完整两类证书都不存在，按短证书等价定理就已经得到
Erdos--Straus 反例。因此这里的 no-go 只约束固定深度、固定 gap 或固定模板 selector，
不约束未知的完整 terminal-first。

## 8. 新的最小研究余项

采用后续原子条件准入 schema 后，selector 的正确顺序应调整为：

1. 双侧超额出现后，先计算两侧真实容量 endpoint，并尝试现有单侧 receipt；
2. endpoint-first 全部失败后，才生成 (7)--(13) 的双色 atomic split candidate；
3. 通过新 primitive 的 E1--E4 后，按 \(L\not\equiv1\) 与 \(L\equiv1\) 分流；前者
   还须通过精确 E5，后者只能作为 guarded checkpoint 再用 (37)；
4. 真正新的算术硬核只保留 (38) 及所有 endpoint/terminal 菜单均失败的状态。

这比“继续加深双侧容量树”更窄，也比“直接宣布双侧块可联合收费”更安全。后续工作已经
给出合同 schema：maximal colored receipt、canonical occurrence、唯一 lcm charge 与
独立通过通用 validator 的 typed target 足以条件性支付 E1--E4；其 E5 门也已精确化。
真正未解的是
\(s\equiv0\pmod p\)，即 \(L\equiv1\pmod {p^2}\) 的大 endpoint/\(p\)-block 树。
[s=0 二阶回返与固定深度 no-go](type-I-overflow-full-product-d-one-a-one-s-zero-endpoint-boundary.md)
进一步证明所有小 endpoint 严格退出，但任何只观察统一固定深度 \(P/M\) endpoint
projection 的策略仍不足。

## 9. 聚焦回执

```bash
python3 reproductions/type_i_overflow_d_one_a_one_split_carrier_stutter_relay.py --verify
```

脚本只核对：一个 \(p=73,r=1\) 的非交换双色来源、固定 receipt cell 在 \(p=73\) 的
二次控制、\(p=73,r=50\) 即 \(s\equiv65\) 的普通严格继电，以及 (39)--(57) 的三个
周期点。一般素数上的二次互反、\(s\equiv0,1,-1\) 三类分派和无限性分别由 (28)、
(34)--(38)、(45)--(49) 的文本证明承担。脚本不扫描素数、分母、历史 selector、一般
图表或完整 Type I/II 菜单，也不核验全局 persistent/typed-state 字段。
