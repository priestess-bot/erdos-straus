---
kind: claim
claim_id: type-II-raw-e1-anchor-relation-obstruction-bridge
title: Type II raw e=1 空洞的锚点—商递降—源关系—提升障碍四分
statement: 设 raw 参数残数空洞的允许阶投影满足 e=gcd(h,exp(H_raw))=1，并且该状态已嵌入一个有限阿贝尔环境群 Gbar，目标截面写成 S=alpha R、R 包含于 Delta=<R>。若 alpha 不在 Delta，则存在幅度等于 |R| 的锚点分离 Fourier 证书；当 Delta 非平凡时，投影到 Gbar/Delta 给出严格较小的目标缺失，并由来源 CRT、目标映射 SNF、范围和正规形门决定是否是真实整数递降；若 alpha 在 Delta，则 Parseval 能量完全进入源关系角色，按相容角色容量、秩/Hall 缺口或带系数 SNF 障碍分派。因而 e=1 不是无类型终点；唯一剩余的是环境嵌入或不可提升角色是否能产生严格整数下降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-raw-divisor-residue-fourier-certificate
  - type-II-source-fiber-anchor-separating-character-certificate
  - type-II-kernel-fourier-energy-role-capacity-dispatch
  - type-II-anchor-rank-fourier-dispatch
  - type-II-raw-finite-abelian-source-lift-snf
  - type-II-annihilator-congruence-fiber-lift-criterion
  - type-II-stabilizer-kernel-source-box-lattice-criterion
  - type-II-source-label-snf-failure-anchor-relation-dichotomy
topics:
- type-II
- raw-ray
- e1-obstruction
- anchor
- source-relation
- Fourier
- capacity
- SNF
- F/G
- descent-interface
sources:
  - claim: type-II-raw-divisor-residue-fourier-certificate
    role: e1-raw-parameter-obstruction
  - claim: type-II-source-fiber-anchor-separating-character-certificate
    role: anchor-separation
  - claim: type-II-kernel-fourier-energy-role-capacity-dispatch
    role: compatible-role-capacity
  - claim: type-II-raw-finite-abelian-source-lift-snf
    role: source-relation-SNF
visibility: public
last_checked: '2026-08-05'
---

# Type II raw \(e=1\) 空洞的锚点—商递降—源关系—提升障碍四分

## 1. 输入状态

固定一个 raw 参数空洞
\[
t_0\notin\mathcal S\subseteq\mathbb Z/h\mathbb Z,
\qquad
e=\gcd(h,\exp(H_{\mathrm{raw}}))=1.
\tag{1}
\]
这里 \(H_{\mathrm{raw}}\) 是用于解释 raw 参数标签的真实源关系商。由阶筛，
任何非平凡参数频率的阶都必须整除 \(\exp(H_{\mathrm{raw}})\)，而又整除 \(h\)；
因此 \(e=1\) 时所有非平凡 raw 参数频率都不能通过源商提升。

假设同一个状态另有一个有限阿贝尔环境群 \(\overline G\)，其规范化目标截面可写为
\[
S=\alpha R\subseteq\overline G,
\qquad
R\subseteq\Delta:=\langle R\rangle,
\qquad
1_{\overline G}\notin S.
\tag{2}
\]
环境嵌入可以来自原模数单位群、稳定子商或已经通过来源标签的 F/G 状态；(2) 是
把 raw 空洞接回真实目标纤维所必需的显式接口。

## 2. 锚点外置分支

若
\[
\alpha\notin\Delta,
\tag{3}
\]
则 \(\alpha\Delta\) 是 \(\overline G/\Delta\) 中的非单位陪集。有限阿贝尔对偶分离
给出一个角色
\[
\chi\in\widehat{\overline G},
\qquad
\chi|_\Delta=1,
\qquad
\chi(\alpha)\ne1.
\tag{4}
\]
于是
\[
\boxed{
\widehat{1_S}(\chi)
=\overline{\chi(\alpha)}\,|R|,
\qquad
|\widehat{1_S}(\chi)|=|R|.
}
\tag{5}
\]
输出
\[
\mathrm{E1\_ANCHOR\_SEPARATING\_FOURIER}
=(\overline G,\Delta,\alpha,R,\chi,|R|).
\tag{6}
\]
这是一个真实环境 F/G Fourier 负证书，不依赖 \(h\) 上的参数频率，也不把
e=1 的 raw 阶筛失败误写成无结构。

若要把 (5) 降到更小环境商 \(\pi:\overline G\to\overline G'\)，还必须满足
\(\ker\pi\subseteq\ker\chi\)；若要转成 Type I/II 整数证书，还需通过来源关系和
参数正规形门。失败时保留 \(\mathrm{E1\_ANCHOR\_LIFT\_OBSTRUCTED}\)。

### 2a. 锚点外置的严格商 relay

若进一步有

\[
1<|\Delta|<|\overline G|,
\tag{6a}
\]

令

\[
\pi:\overline G\longrightarrow Q:=\overline G/\Delta,
\qquad q_\alpha=\pi(\alpha).
\tag{6b}
\]

由 (3)，\(q_\alpha\ne1_Q\)；又因 \(R\subseteq\Delta\)，有精确的像公式

\[
\pi(S)=\{q_\alpha\},
\qquad
1_Q\notin\pi(S).
\tag{6c}
\]

所以商状态仍然是目标缺失，而且

\[
|Q|=|\overline G|/|\Delta|<|\overline G|.
\tag{6d}
\]

这一步是严格的有限群势下降；它不同于 (5) 的 Fourier 证书，也不要求在 raw
循环 \(\mathbb Z/h\mathbb Z\) 上存在非平凡参数角色。

要把 (6c) 作为原猜想的整数递降，必须通过一个可复核的
\(\mathrm{Q\mbox{-}LIFT}\) 门。令真实环境源列为
\(\varphi:\mathbb Z^r\to\overline G\)，源关系格为
\(\Lambda=\ker\varphi\)，并设 \(\mathcal B\subset\mathbb Z^r\) 是当前有限源盒。定义

\[
\widetilde\Delta=\varphi^{-1}(\Delta),
\qquad
\overline\varphi:\mathbb Z^r/\widetilde\Delta\longrightarrow Q.
\tag{6e}
\]

这里的整数回译还要求环境源盒确实由同一组来源生成：
\(\varphi(\mathcal B)=S\)；若只能得到包含关系或未实现的跨状态映射，则不能登记
商递降，只能保留对应的 UNREALIZED/LIFT_OBSTRUCTED 回执。
另记 \(t_Q\) 为低模数参数态中目标 \(-1\) 的规范化标签；若 source-switch 保持
当前的目标规范化，则 \(t_Q=1_Q\)，否则 \(t_Q\) 必须作为额外标签送入同一 SNF
系统。

一个商递降记录必须同时给出一个严格较小的整数参数态
\((D',A)\) 及其目标映射 \(\eta\)，满足下列有限门：

\[
\begin{array}{ll}
\mathrm{Q1}:&D'\mid D,\ D'<D,\ A\mid D',\ D'/A\text{ 平方自由},\ 4AD'<p;\\
\mathrm{Q2}:&\eta:U(4D')\twoheadrightarrow Q\text{（或实际商像）且 }\eta(-1)=t_Q;\\
\mathrm{Q3}:&\text{每个保留来源记录 }(u_i,a_i,h_i)\text{ 的商像满足}\\
&\quad AD'\equiv Da_i\pmod{h_i},\quad h_i\mid p+4AD',\quad
\eta(h_i\bmod4D')=\pi(u_i);\\
\mathrm{Q4}:&\text{Q2--Q3 的联合标签同余系统通过有限 SNF，且源盒像满足}\\
&\quad\overline\varphi\!\left((\mathcal B+\widetilde\Delta)/\widetilde\Delta\right)
 =\pi\!\left(\varphi(\mathcal B)\right)=\pi(S);\\
&\quad\text{若采用稳定子饱和 relay，还须有商核包含于该盒像的稳定子，}\\
&\quad\text{并通过所有范围、互素和 shared-q 门。}
\end{array}
\tag{6f}
\]

Q2--Q4 不是抽象存在性假设：Q2 使用单位群目标带像满射 SNF，Q3 使用统一来源
CRT 预筛，Q4 使用有限阿贝尔源商的联合标签 SNF，并检查上述源盒像等式；若使用
稳定子饱和 relay，再在有限商中逐生成元检查核平移。它们分别对应
[Type II annihilator relay 的带来源同余纤维提升判据](type-II-annihilator-congruence-fiber-lift-criterion.md)
和
[Type II 稳定子同余核的源指数盒格判据](type-II-stabilizer-kernel-source-box-lattice-criterion.md)。

### 2b. Q1--Q4 的有限压缩

把商回译中保留的来源记录写成
\(\sigma_i=(u_i,a_i,h_i)\)，并令
\[
r_i\equiv Da_i\pmod{h_i},
\qquad
H_{\mathrm{src}}=\operatorname{lcm}_i(h_i).
\tag{6i}
\]
则所有 Q1 候选的唯一整数 \(x=AD'\) 必须满足
\[
x\equiv r_i\pmod{h_i}\quad\text{对所有 }i.
\tag{6j}
\]
广义 CRT 因而给出一个二分：

* 若存在 \(i,j\) 使
  \(r_i\not\equiv r_j\pmod{\gcd(h_i,h_j)}\)，输出
  \(\mathrm{E1\_ANCHOR\_QUOTIENT\_SOURCE\_CRT\_INCONSISTENT}\)；
* 否则所有解构成 \(x\equiv r_{\mathrm{src}}\pmod{H_{\mathrm{src}}}\)。令
  \(x_+\) 是该剩余类的最小正代表，则
  \[
  N_x=
  \max\!\left(0,\left\lfloor\frac{D^2-x_+}{H_{\mathrm{src}}}\right\rfloor+1\right)
  \tag{6k}
  \]
  是满足 \(1\le x\le D^2\) 的候选数。

 对每个候选 \(x\)，平方自由分解
\[
x=A^2c,\qquad c\text{ 平方自由},\qquad D'=Ac
\tag{6l}
\]
是唯一满足 \(A D'=x\)、\(A\mid D'\)、\(D'/A\) 平方自由的参数对。于是还需检查
\(D'\mid D\)、\(D'<D\)、\(4x<p\) 和 shared-q 账本；在输入来源记录本身有效时，
Q3 中的 \(h_i\mid p+4x\) 由 (6j) 自动成立。最后，对每个剩余的 \(D'\) 只需用
目标映射 SNF 枚举 \(\eta\) 并检查联合标签。若 \(N_x=0\)，输出
\(\mathrm{E1\_ANCHOR\_QUOTIENT\_ADMISSIBLE\_FIBER\_EMPTY}\)；若所有候选的目标
映射 SNF 均失败，先调用
[Type II 源标签 SNF 失败的锚点外置—源关系二分](type-II-source-label-snf-failure-anchor-relation-dichotomy.md)：
源标签子系统失败时输出纯源关系障碍，源标签可解而目标在源子群外时输出锚点商
分离，目标在源子群内时输出带目标系数的关系障碍；仍无法承接时再输出
\(\mathrm{E1\_ANCHOR\_QUOTIENT\_TARGET\_MAP\_SNF\_OBSTRUCTED}\)。这给出一个
完全有限、可复核且不依赖搜索上界猜测的 Q1--Q4 负回执。

### 2c. Q 菜单失败的对偶化

Q 菜单为空不应把所有失败合并为同一个标签。若 (6j) 的 CRT 预筛在一对来源
\(i,j\) 上失败，令
\[
g_{ij}=\gcd(h_i,h_j),\qquad
d_{ij}=r_i-r_j\not\equiv0\pmod{g_{ij}},
\qquad
H_{ij}=\operatorname{lcm}(h_i,h_j).
\tag{6m}
\]
在有限参数商 \(\mathbb Z/H_{ij}\mathbb Z\) 上取角色
\[
\psi_{ij}(x)=\exp\!\left(\frac{2\pi i x}{g_{ij}}\right).
\tag{6n}
\]
因为 \(g_{ij}\mid h_i,h_j\)，\(\psi_{ij}\) 在两个同余纤维
\[
C_i=\{x:x\equiv r_i\pmod{h_i}\},\qquad
C_j=\{x:x\equiv r_j\pmod{h_j}\}
\]
上分别为常相位，且两相位不同。对归一化差测度
\[
\mu_{ij}=\frac{1_{C_i}}{|C_i|}
-\frac{1_{C_j}}{|C_j|}
\]
有
\[
\widehat{\mu_{ij}}(\psi_{ij})
=\exp\!\left(-\frac{2\pi i r_i}{g_{ij}}\right)
-\exp\!\left(-\frac{2\pi i r_j}{g_{ij}}\right)\ne0.
\tag{6o}
\]
因此 CRT 不相容同时有一个最小整数见证和一个参数关系 Fourier 见证，输出
\[
\mathrm{E1\_ANCHOR\_QUOTIENT\_SOURCE\_CRT\_INCONSISTENT}
\ /\
\mathrm{SOURCE\_RELATION\_FOURIER}
\]
时不得把 (6o) 计入环境 F/G 或 q-height 容量；它只说明固定来源标签不能落在同一
整数参数纤维。

若 \(N_x=0\)，或所有平方自由分解后的候选都违反 \(D'\mid D\)、\(D'<D\)、
范围或 shared-q 门，则保留最小失败候选的
\(\mathrm{E1\_ANCHOR\_QUOTIENT\_ADMISSIBLE\_FIBER\_EMPTY}\) 及其范围/除子见证；
这是一份算术空集证书，不是 Fourier 容量缺口。若候选存在但 Q2--Q4 的目标映射
联合 SNF 失败，则取 SNF 的第一失败行，按上述源标签二分回译；若该行不能回译为
锚点或源关系出口，才输出
\(\mathrm{E1\_ANCHOR\_QUOTIENT\_TARGET\_MAP\_SNF\_OBSTRUCTED}\) 和对应的
\(\mathrm{SOURCE\_RELATION\_LIFT\_OBSTRUCTED}\)，并保存目标标签与来源关系的明确
整除矛盾。三类失败互斥，避免同一个空菜单被重复收费。

若 (6f) 通过，输出

\[
\mathrm{E1\_ANCHOR\_QUOTIENT\_SOURCE\_SWITCH}
=(D',A,\eta,\pi,\overline\varphi,\mathcal B),
\tag{6g}
\]

并以 \(|Q|<|\overline G|\) 作为第一坐标的严格下降。若所有有限候选均失败，输出

\[
\mathrm{E1\_ANCHOR\_QUOTIENT\_LIFT\_OBSTRUCTED}
\tag{6h}
\]

同时保留 (6) 的锚点 Fourier 证书；(6h) 只说明该商不能按当前来源标签回译，不能
被误写成原素数的 Type I/II 负证书。

当 \(\Delta=1\) 时，商 \(Q=\overline G\) 没有严格变小，故不得登记
\(\mathrm{E1\_ANCHOR\_QUOTIENT\_SOURCE\_SWITCH}\)，只能保留
\(\mathrm{E1\_ANCHOR\_SEPARATING\_FOURIER}\)。

## 3. 锚点在源差分群内

若
\[
\alpha\in\Delta,
\tag{7}
\]
则 \(S\subseteq\Delta\)，且 \(1\notin S\)。令
\[
n=|S|,\qquad 0<n<|\Delta|.
\tag{8}
\]
对 \(\chi\in\widehat\Delta\) 记
\[
F_S(\chi)=\sum_{x\in S}\overline{\chi(x)}.
\tag{9}
\]
Parseval 给出
\[
\sum_{\chi\ne1}|F_S(\chi)|^2=n(|\Delta|-n)>0.
\tag{10}
\]
因此至少有一个非平凡源关系角色。按已有 SNF 相容性集合
\(\mathcal X_{\mathrm{comp}}\subseteq\widehat\Delta\) 分解：
\[
n(|\Delta|-n)
=
\sum_{\substack{\chi\in\mathcal X_{\mathrm{comp}}\\\chi\ne1}}|F_S(\chi)|^2
+
\sum_{\chi\notin\mathcal X_{\mathrm{comp}}}|F_S(\chi)|^2.
\tag{11}
\]

由此得到互斥三分：

1. 不相容能量为正：选最小角色阶、最大幅度的失败角色，输出
   \[
   \mathrm{E1\_SOURCE\_RELATION\_LIFT\_OBSTRUCTED}
   =(\Delta,S,\chi_{\mathrm{obs}},F_S(\chi_{\mathrm{obs}})).
   \tag{12}
   \]
   该能量不得计入 q-height 或 Kneser 容量。
2. 不相容能量为零：相容非平凡角色必存在。按其阶进入
   \(\ell\)-初等 Rado/Hall、较高 \(2^j\) 或 mixed-primary 分支；通过独立源列
   匹配后，若已经三角化为单一 \(C_{\ell^a}\) primary，则调用
   [Type II 源标签 SNF 失败的锚点外置—源关系二分](type-II-source-label-snf-failure-anchor-relation-dichotomy.md)
   的进位层桥，得到 SNF_RELATION_CYCLIC_PRIMARY_HIT 或具体
   SNF_RELATION_CYCLIC_DIGIT_DEFICIT；否则才可形成一般 F/G 容量需求。
3. 相容角色产生源列秩缺口或 Hall 缺口：输出
   \(\mathrm{E1\_SOURCE\_RANK\_OR\_HALL\_DEFICIT}\)，并转入固定层
   annihilator/严格下降闭包。

因此 \(e=1\) 只排除了 raw 参数角色的直接提升，并没有排除真实环境中的源关系
角色；两者必须区分。

## 4. 证明

由 (1)，若 raw 参数频率 \(j\ne0\) 能提升到 \(H_{\mathrm{raw}}\)，则
\(h/\gcd(h,j)\mid\exp(H_{\mathrm{raw}})\)，与 \(\gcd(h,\exp H_{\mathrm{raw}})=1\)
矛盾，所以 raw 参数分支全部是显式阶障碍。

若 (3) 成立，商 \(\overline G/\Delta\) 中的非单位陪集 \(\alpha\Delta\) 可由角色
分离；将商角色复合投影得到 (4)，再由 \(S=\alpha R\) 和
\(\chi|_\Delta=1\) 得 (5)。若 \(\Delta\ne1\)，则 (6c)--(6d) 直接给出商状态的
严格群阶下降。Q1--Q4 恰好是把该群商状态回译到整数参数态所需的四个有限门；
通过时得到 (6g)，并且 (6i)--(6l) 将候选搜索压缩为有限菜单；失败时只能得到
(6h) 或 2b 中的具体 CRT/范围/SNF 回执与原环境的 Fourier 证书，不能越过算术提升
障碍。

若 (7) 成立，则 \(S\) 是有限群 \(\Delta\) 的非空真子集，(10) 是 Parseval。
按 \(\mathcal X_{\mathrm{comp}}\) 与补集拆分得到 (11)。若补集能量为正，(12) 是
明确的 SNF/关系障碍；若补集能量为零，(10) 强制相容角色存在，随后使用已有
角色阶和 Rado/Hall 定理。三分穷尽，证毕。

## 5. \(p=97\) 边界

取
\[
G=U(24),\qquad
P=\{1,11\},\qquad
t=23.
\]
目标陪集截面可规范化为
\[
\Delta=\{1\},\qquad
\alpha=13,\qquad
R=\{1\}.
\]
于是 \(\alpha\notin\Delta\)，角色
\[
\chi(5)=1,\qquad \chi(13)=\chi(17)=-1
\]
给出
\[
|\widehat{1_S}(\chi)|=1.
\]
另一方面，raw 混合因子 \(h=143\) 的参数源商为 \(U(24)\)，指数为 2，
故 \(e=\gcd(143,2)=1\)，所有非平凡 raw 参数频率都
\(\mathrm{LIFT\_OBSTRUCTED}\)。这说明两条回执可以同时成立：
raw 参数角色不可提升，但环境锚点角色给出真实 F/G Fourier 证书。

同一 \(D=6\) 的来源记录
\((a_i,h_i)=(1,11),(3,13)\) 给出
\[
x=AD'\equiv83\pmod{143},\qquad x\le D^2=36,
\]
所以 (6k) 的候选数 \(N_x=0\)，商递降菜单在 CRT/范围层即为空。
相反，\(p=5113\)、\((a_i,h_i)=(3,17),(6,7)\) 给出
\[
x\equiv1\pmod{119},\qquad N_x=1,\qquad (A,D')=(1,1).
\]
这说明 Q1--Q4 的算术部分确实能从“抽象商是否可提升”压缩为有限、可枚举的
单一剩余类；是否通过 Q2 的目标标签和联合 SNF 仍需逐状态检查。

若改取加法记号下
\[
\overline G=C_2\oplus C_2,\qquad
\Delta=\{(0,0),(0,1)\},\qquad
\alpha=(1,0),\qquad R=\Delta,
\]
则 \(S=\alpha+R=\{(1,0),(1,1)\}\)，目标 \((0,0)\) 缺失，而
\(\overline G/\Delta\simeq C_2\) 中源像是非零单陪集；这是一个严格的群商 relay
样例。它只有在 Q1--Q4 通过时才是整数 source-switch；否则仍必须保留商提升障碍。

若改取 \(\Delta=C_2\)、\(R=\{1\}\)、\(\alpha\) 为非平凡元，则锚点在
\(\Delta\) 内，(10) 给出源关系角色；此时应进入源列秩/Hall 分派，而不是继续
寻找 raw 参数频率。

## 研究边界

该桥把 \(e=1\) 从“参数 Fourier 全部失败”的空分支精化为环境锚点、严格商 relay、
真实源关系或显式提升障碍四分。商 relay 的群论下降已由 (6c)--(6d) 完成；它尚未
证明 Q1--Q4 对每个原始状态都有解，也未证明所有
E1_SOURCE_RELATION_LIFT_OBSTRUCTED 都产生原素数的严格下降。后两项仍是统一
选择器的决定性剩余。
