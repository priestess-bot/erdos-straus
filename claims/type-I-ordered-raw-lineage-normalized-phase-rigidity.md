---
kind: claim
claim_id: type-I-ordered-raw-lineage-normalized-phase-rigidity
title: 有序 raw 谱系的归一化相位刚性、gcd 富集标签与 F 奇主层门
statement: 对任一从单位坐标开始的有序 raw 谱系，若第 i 步的实际 gcd reduction 为 g_i、raw 标签为 q_i，则其坐标满足 q_i g_i z_i=z_{i-1} (mod R)。因此 E_i=product_{j<=i}q_jg_j 满足 E_i z_i=z_0，而唯一把该坐标归一到 -1 的相位为 Phi_i=-z_i^(-1)=E_i Phi_0。若该坐标以已声明方向读作物理尾 epsilon C t，且 pR+1=4MC、n=4M-R，则 Phi_i=-epsilon n t^(-1) (mod R)。漏掉 gcd 标签只在角色 psi(product g_i)=1 时保留终点角色相位；它不能替代逐边的 factor-local 条件。更精确地，在 q-primary 角色层，Phi 的边增量是 log psi(q_i g_i)；它仅当同一 raw 因子 q 的所有边具有相同 psi(g_i) 时才能下降为只依赖 q 的 action，若要使用原始 log psi(q) 则每条都须 psi(g_i)=1。若一个 F 奇 q 直接目标相位要由 source 相位给出，仍须另行声明并验证 source-to-F 同态；在此前，psi_F(Lambda(Phi_i))=1 只是必要 compatibility gate。p=1009 给出 g_i=1 的正向 raw 谱系与 c=3 物理尾回执；p=193 给出 g=25 的 F/q=3 定向控制，漏 g 会把实际失败的自然 quotient gate 错判为通过。该结论不建立 source-to-F map、root、E4/E5 或 selector edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-marked-raw-peeling-calculus
  - type-I-g-anchor-c3-p1009-universal-source-bypass-raw-receipt
  - type-I-raw-universal-p-parent-root-policy-boundary
  - type-I-f-target-involution-fourier-phase-collapse
  - type-I-raw-factor-action-affine-preflight
topics:
  - type-I
  - raw-transition
  - ordered-lineage
  - normalized-phase
  - gcd-reduction
  - enriched-label
  - factor-action
  - F-state
  - q-primary
  - source-map
  - proof-boundary
sources:
  - claim: type-I-g-anchor-c3-p1009-universal-source-bypass-raw-receipt
    role: ordered-universal-source-raw-control
  - claim: type-I-raw-universal-p-parent-root-policy-boundary
    role: formal-gcd-reduction-control
  - claim: type-I-f-target-involution-fourier-phase-collapse
    role: F-direct-odd-primary-zero-phase
  - claim: type-I-raw-factor-action-affine-preflight
    role: raw-factor-integrability-interface
  - reproduction: reproductions/type_i_ordered_raw_lineage_normalized_phase_rigidity.py
    role: exact-p1009-and-p193-controls
visibility: public
last_checked: '2026-08-07'
---

# 有序 raw 谱系的归一化相位刚性、gcd 富集标签与 F 奇主层门

这张卡只处理已声明 raw word 中一个**有序坐标后代**的相位输运。它把
`gcd_reduction` 从可丢弃的实现细节提升为相位动作的必要输入；但它不把 raw word
自动解释为 source map、root 或递归边。

## 1. 单步坐标输运

固定奇模数 \(R\)。考虑一条实际 ordered raw step。其输入为 primitive formal node

\[
(a,b,m),\qquad a+b=Rm,
\]

选择坐标 \(s\in\{a,b\}\)，另一个坐标记为 \(o\)，并使用 raw 素数标签 \(q\)。设

\[
\ell\equiv-m\pmod q,\qquad 1\le\ell<q,
\]

且在除法前、gcd 约分前的三元组为

\[
\widetilde s=\frac{s}{q},\qquad
\widetilde o=\frac{o+R\ell}{q},\qquad
\widetilde m=\frac{m+\ell}{q}.
\tag{1}
\]

令

\[
g=(\widetilde s,\widetilde o),
\qquad
(a',b',m')=(\widetilde s/g,\widetilde o/g,\widetilde m/g),
\tag{2}
\]

其中 destination 按“被选坐标在前”的约定有序。raw unit condition 给出

\[
q\in U(R).
\tag{3}
\]

令 \(z\) 是输入的某一个指定坐标，并令 \(z'\) 是它在 (2) 中的指定后代。
若 \(z=s\)，则由 (1)--(2) 有精确整数等式

\[
qgz'=z.
\tag{4a}
\]

若 \(z=o\)，则有

\[
qgz'=z+R\ell.
\tag{4b}
\]

所以无论该有序谱系在这一步是否被选择，均有

\[
\boxed{qgz'\equiv z\pmod R.}
\tag{5}
\]

这里“有序”不可删去：若每一步只存 unordered destination，便不能知道 \(z'\) 是
\(\widetilde s/g\) 还是 \(\widetilde o/g\)，也就没有 (4) 的谱系语义。

## 2. 归一化相位刚性

设 \(z_0,z_1,\ldots,z_r\) 是连续的有序 raw 谱系，且

\[
z_0\in U(R).
\tag{6}
\]

第 \(i\) 步的标签和实际 gcd reduction 分别为 \(q_i,g_i\)。由 (5) 归纳地，

\[
q_i g_i z_i\equiv z_{i-1}\pmod R.
\tag{7}
\]

右端是单位，而 \(q_i\) 已由 (3) 是单位。在交换环 \(\mathbb Z/R\mathbb Z\) 中，
一个乘积为单位蕴含每个因子为单位，故每个 \(g_i,z_i\) 也属于 \(U(R)\)。令

\[
E_0=1,\qquad E_i=\prod_{j=1}^i q_jg_j\pmod R.
\tag{8}
\]

则

\[
\boxed{E_i z_i\equiv z_0\pmod R.}
\tag{9}
\]

定义由 source 坐标归一化的相位

\[
\Phi_i:=-z_i^{-1}\pmod R,
\qquad
\Phi_0=-z_0^{-1}.
\tag{10}
\]

由 (9) 得

\[
\boxed{\Phi_i=E_i\Phi_0,\qquad
\Phi_i\Phi_{i-1}^{-1}=q_i g_i\pmod R.}
\tag{11}
\]

并且 \(\Phi_i\) 是唯一满足

\[
\Phi_i z_i\equiv-1\pmod R
\tag{12}
\]

的相位。因此它不是从 endpoint 倒推后任意选择的 multiplier；一旦 ordered source
coordinate、每条 raw step 及其实际 \(g_i\) 固定，(10) 已强制固定。

**证明。** (7) 的逐步相乘给出 (9)。将 (9) 乘以
\(-z_0^{-1}z_i^{-1}\) 得 (11)。由于 \(z_i\) 为单位，(12) 的解唯一。证毕。

## 3. 物理尾律

现在额外假设给定一行 physical determinant 数据

\[
pR+1=4K=4MC,
\qquad n_{\rm row}=4M-R>0.
\tag{13}
\]

它自动满足

\[
p n_{\rm row}=4M(p-C)+1.
\tag{14}
\]

若谱系的当前坐标已被**带方向地**读为 physical tail

\[
z_i\equiv\varepsilon Ct\pmod R,
\qquad \varepsilon\in\{+1,-1\},\quad t\in U(R),
\tag{15}
\]

则 (13) 给出

\[
C^{-1}\equiv4M\equiv n_{\rm row}\pmod R.
\tag{16}
\]

于是 (10) 精确专门化为

\[
\boxed{
\Phi_i=-\varepsilon\,n_{\rm row}t^{-1}\pmod R.
}
\tag{17}
\]

式 (17) 需要 (15) 的 orientation；将 (Ct) 与 (R-Ct) 混同会使右端符号错误。
它也不说每个 raw 坐标天然就是某一 physical tail，只有已验证的 marked row 才可
调用本式。

## 4. 漏掉 gcd 标签的精确判据

把 (8) 分解为

\[
Q_i=\prod_{j\le i}q_j,
\qquad G_i=\prod_{j\le i}g_j
\pmod R.
\tag{18}
\]

若错误地只按 raw 因子传播相位，则得到

\[
\widehat\Phi_i:=Q_i\Phi_0=G_i^{-1}\Phi_i.
\tag{19}
\]

因此对任意有限值角色 \(\psi:U(R)\to\mathbb C^\times\)，有严格等价

\[
\boxed{
\psi(\widehat\Phi_i)=\psi(\Phi_i)
\Longleftrightarrow
\psi(G_i)=1.
}
\tag{20}
\]

这就是 gcd omission character criterion。它是一个**终点、一个 word、一个角色**的
判据；它不能代替逐边相容性。

为精确说明这一点，令 \(\psi\) 为阶整除 \(q^e\) 的 q-primary 角色，并取

\[
\psi(u)=\zeta_{q^e}^{\lambda_\psi(u)},
\qquad
\lambda_\psi:U(R)\longrightarrow\mathbb Z/q^e\mathbb Z.
\tag{21}
\]

以下讨论多个边时，假设它们的 \(\Phi_v\) 都由同一个已声明的 source normalization
得到，因而确实组成顶点 potential。沿一个 raw 边 \(e:v\to w\)，(11) 的实际
lineage potential 有增量

\[
\lambda_\psi(\Phi_w)-\lambda_\psi(\Phi_v)
=\lambda_\psi\bigl(q(e)g(e)\bigr).
\tag{22}
\]

所以它以 `enriched label` \((q(e),g(e))\)，或其乘积 \(q(e)g(e)\)，而不是自动以
单独 raw factor \(q(e)\) 为边标签。对一个已经带有这个 potential 的 raw 图：

\[
\begin{array}{rcl}
\text{(22) 仅依赖 raw factor }q(e)
&\Longleftrightarrow&
\psi(g(e))\text{ 在所有同一 }q(e)\text{ 的边上相同};\\[2mm]
\text{(22) 恰等于 }\lambda_\psi(q(e))
&\Longleftrightarrow&
\psi(g(e))=1\text{ 在每一条边上}.
\end{array}
\tag{23}
\]

第一行的证明只是在 (22) 中固定 \(q(e)\) 并相消 \(\psi(q(e))\)。第二行是其
特别情形。相比之下，单条路径的 \(\psi(G_i)=1\) 只使 (20) 在该 endpoint 成立；
例如两个边的 gcd 角色值可以是 \(u,u^{-1}\)，使终点乘积消失而每条边仍非 factor-local。

若希望把 gcd 角色值吸收到一个 vertex rephasing，必须另有 \(\theta:V\to\mu_{q^e}\)
满足

\[
\theta(w)\theta(v)^{-1}=\psi(g(e)).
\tag{24}
\]

它在每个弱连通分支上存在当且仅当其**保留平行边的底层无向多重图**的每个闭合游走
都有平凡 holonomy：
沿游走方向穿过原向边 \(e\) 时取 \(\psi(g(e))\)，逆向穿过该边时取
\(\psi(g(e))^{-1}\)，这些值的乘积必须为 \(1\)。这是 gcd enrichment 的路径独立性门；
缺少它时，不可把存有 \(g(e)\) 的 raw transcript 压缩成无标记的 factor-only source
map。只检查有向闭路不够：有向无环菱形也可能有两条相同端点的路径给出不同的
gcd 相位积。

若 state identity 保留完整 ancestry digest，使每条新 raw history 都留在一棵谱系树中，
该底层多重图的每个闭合游走都可由相邻反向边消去，(24) 自动成立。只有把不同
history 合并为同一 physical vertex 或同一 anchor state 时，才必须先通过上述 holonomy
门；不能把 tree 中的自动性误外推到 history-merged 图。

这与 [raw 因子作用到共同仿射相位图的可积性门](type-I-raw-factor-action-affine-preflight.md)
并不冲突。后者处理任意事先给定的 factor action 与其 cycle lattice；本卡只指出，若该
action 声称由 (10) 的 source-lineage phase 导出，那么候选边增量首先必须是 (22)。
它不排除一个完全独立、并不以 \(\Phi\) 为来源的 factor-local affine map。

## 5. F 型奇主层的条件 compatibility gate

设一个 F state 已给出有限商 \(\bar H_F\)、目标对合 \(\tau\)，且
\(\tau\) 属于其指数映射的像。对奇素数 \(q\)，已有 direct-target 结论给出某个
q-primary character \(\psi_F\) 的直接目标相位

\[
\lambda_{\psi_F}(\tau)=0\pmod{q^e}.
\tag{25}
\]

现在再**额外**给定一个已声明并单独验证的 source-to-F homomorphism

\[
\Lambda:U_{\rm src}\longrightarrow\bar H_F,
\tag{26}
\]

并且它的语义确实是把本卡的 normalized source phase 无偏移地识别为该 direct F
target phase。只有在这两个额外条件下，才有必要门

\[
\boxed{
\lambda_{\psi_F}\bigl(\Lambda(\Phi_i)\bigr)=0
\quad\Longleftrightarrow\quad
\psi_F\bigl(\Lambda(\Phi_i)\bigr)=1.
}
\tag{27}
\]

这称为 F-odd-\(q\) direct-target compatibility gate。它不构造 (26)：F 的 Fourier
certificate 和 (25) 本身都不产生 source map。若随后采用的是 affine 或 anchored
phase 而非 direct zero-offset identification，右端必须由其已声明的 offset 改写，不能
套用 (27)。因此 (27) 不是 terminal certificate、解提升或 selector edge。

## 6. \(p=1009\) 的无约分正控制

已有 c=3 universal-source bypass 中

\[
(p,R,K,M,C,n_{\rm row})=(1009,4359,1099558,1093,1006,13).
\tag{28}
\]

从 ordered source 的第一坐标 \(z_0=1009\) 出发，六条实际 raw 边的
\((q_i,g_i,z_i,E_i,\Phi_i)\) 为

\[
\begin{array}{c|r|r|r|r|r}
i&q_i&g_i&z_i&E_i&\Phi_i\\ \hline
0&-&-&1009&1&2942\\
1&349&1&490&349&2393\\
2&41&1&4052&1232&2215\\
3&1013&1&4&1342&3269\\
4&13&1&4024=4C&10&3266\\
5&2&1&2012=2C&20&2173\\
6&2&1&1006=C&40&4346
\end{array}
\pmod {4359}.
\tag{29}
\]

每行均满足 (7)、(9) 和 (11)。最后三行的 orientation 都是正的，故 (17) 给出

\[
3266=-1093=-13\cdot4^{-1},\qquad
2173=-2\cdot1093=-13\cdot2^{-1},\qquad
4346=-13.
\tag{30}
\]

此 transcript 中所有 \(g_i=1\)，所以 factor-only 与 enriched phase 恰好一致。
这只说明该**一条** word 可安全省略 gcd 字段；它不推出其它 raw word 也可省略。

## 7. \(p=193\) 的 F/奇主层定向反控制

考虑 F control

\[
(p,R,K)=(193,63,3040),\qquad K=2^5\cdot5\cdot19.
\tag{31}
\]

其 fixed-layer quotient 可明确写为

\[
P=\langle2\rangle\subset U(63),\qquad U(63)/P\simeq C_6=\langle5P\rangle,
\tag{32}
\]

目标为 \(\tau=(-1)P=(5P)^3\)。fixed layer 的商坐标为 \(\{0,1,5\}\)，再乘
\(5^{-1},1,5\) 的表示数为

\[
(3,2,1,0,1,2),
\tag{33}
\]

故目标坐标 (3) 缺失。取 q-primary character

\[
\psi_3((5P)^a)=\zeta_3^a.
\tag{34}
\]

则 \(\psi_3(\tau)=1\)，正是 (25) 的 \(q=3\) direct phase zero。

现在只为检验 gcd transport，采用由一般 p-parent 公式反向生成的 formal node

\[
(24125,279787,4824)
\xrightarrow[\ell=1,\ g=25]{q=193}
(5,58,1).
\tag{35}
\]

在除法后、约分前的三元组是 \((125,1450,25)\)。选择第一坐标的谱系满足精确等式

\[
193\cdot25\cdot5=24125.
\tag{36}
\]

模 (63) 下

\[
E_1=193\cdot25=37,
\qquad
\Phi_0=-24125^{-1}=16,
\qquad
\Phi_1=-5^{-1}=25.
\tag{37}
\]

另一方面，physical row 是

\[
(C,M,t,n_{\rm row})=(5,608,1,2369),
\tag{38}
\]

且 \(5=+Ct\)，故 \(\Phi_1=-2369=25\pmod {63}\)，与 (17) 一致。

若错误删除 \(g=25\)，则

\[
\widehat\Phi_1=193\Phi_0=1\pmod {63}.
\tag{39}
\]

在 (34) 下，

\[
\psi_3(g)=\zeta_3^2,
\qquad
\psi_3(\Phi_1)=\zeta_3^2\ne1,
\qquad
\psi_3(\widehat\Phi_1)=1.
\tag{40}
\]

所以若把自然群商 \(\Lambda_{\rm nat}:U(63)\to U(63)/P\) **提议**为 (26) 的
direct zero-offset identification，则实际 enriched phase 在 (27) 处失败，而漏掉 gcd
的版本会错误地通过。该例严格说明 (20)--(23) 的必要性。

不过 (35) 是从 endpoint 反向生成的 formal p-parent，故它不是 root provenance；
\(\Lambda_{\rm nat}\) 也只是同一 chart 上可测试的群商候选，并没有被证明为所需的
source-to-F semantic map。该反控制既不排除其它 \(\Lambda\)、其它 offset 或其它
lineage，也不构造 F terminal。并且 \(R=63<p\)，所以 (38) 只是 determinant/tail
控制，不是 cofactor-overflow transcript；它不提供 carry、E2 或 persistent-ledger 结论。

## 8. 范围

本卡已建立的是：实际 ordered raw transcript 的精确相位输运、物理尾的正确读法、
gcd omission 的角色判据，以及把它们接入 F direct-target 数据前所需的条件门。它没有
建立下列任一项：

1. 一个全域或 target-independent 的 source-to-F homomorphism；
2. root policy、E1--E5、解纤维 lift 或严格下降；
3. F/G 的全称分类、短证书有界性或 Erd\H{o}s--Straus 猜想的证明。

窄复现：

~~~bash
python3 reproductions/type_i_ordered_raw_lineage_normalized_phase_rigidity.py --verify
~~~
