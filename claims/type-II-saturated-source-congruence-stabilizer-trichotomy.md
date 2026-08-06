---
kind: claim
claim_id: type-II-saturated-source-congruence-stabilizer-trichotomy
title: Type II 饱和源积集的同余稳定子—核 Fourier—算术三分
statement: 固定 G=U(4D_*) 中的来源积集 P、目标 -1 notin P 和稳定子 T=Stab(P)。对每个 D'|D_* 令 C_{D'} 为降模核。若 C_{D'} subset T，则 P 对该核饱和，目标缺失精确传递到 U(4D')；若同时保留来源标签的参数纤维门非空、投影字段精确回译且 D'<D_*，得到完整 E1--E5 降模边。若某个源子列表已满足 h_S=-1 (mod 4D')，则先输出直接 Type II 终端，不登记为递降。若 C_{D'} not subset T，则存在 c in C_{D'} 和角色 chi 使 chi(c) !=1 且 1_P 的 Fourier 系数非零；若低模数目标像命中，则进一步得到非空真核截面及 Parseval 能量。若稳定子包含通过但参数纤维门为空，则输出有限 ARITHMETIC_LIFT_OBSTRUCTED。三类对每个候选 D' 穷尽，且不把抽象低模数命中误记为递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-weighted-source-saturated-quotient-kernel-dispatch
  - type-II-stabilizer-kernel-quotient-descent-trichotomy
  - type-II-stabilizer-kernel-failure-dual-certificate
  - type-II-same-modulus-source-switch-crt-criterion
topics:
- type-II
- stabilizer
- congruence-kernel
- quotient-descent
- kernel-fourier
- source-switch
- E1-E5
- arithmetic-obstruction
- proof-program
sources:
  - claim: type-II-weighted-source-saturated-quotient-kernel-dispatch
    role: saturated-source-quotient-input
  - claim: type-II-stabilizer-kernel-quotient-descent-trichotomy
    role: lower-modulus-stabilizer-saturation
  - claim: type-II-stabilizer-kernel-failure-dual-certificate
    role: nonstable-kernel-fourier
  - claim: type-II-same-modulus-source-switch-crt-criterion
    role: source-normal-form-gate
visibility: public
last_checked: '2026-08-05'
---

# Type II 饱和源积集的同余稳定子—核 Fourier—算术三分

## 1. 固定纤维和候选降模核

令

\[
G_*=U(4D_*),\qquad
P\subseteq G_*,\qquad
t=-1\notin P,
\tag{1}
\]

其中 \(P\) 是同一来源参数纤维中的无重数源积集。令

\[
T=\operatorname{Stab}_{G_*}(P)
\tag{2}
\]

为最终稳定子。对每个真除子 \(D'\mid D_*\)，令

\[
\rho_{D'}:G_*\longrightarrow \rho_{D'}(G_*)\le U(4D'),
\qquad
C_{D'}=\ker\rho_{D'}.
\tag{3}
\]

候选低模数的来源参数纤维由有限集合

\[
\mathscr S_{D'}(p;\mathbf h)=
\left\{A:
\begin{array}{l}
A\mid D',\quad D'/A\text{ 平方自由},\quad 4AD'<p,\\
h_i\mid p+4AD'\quad(1\le i\le r)
\end{array}
\right\}
\tag{4}
\]

给出，其中 \(\mathbf h=(h_1,\ldots,h_r)\) 是保留来源标签的两两互素因子列表。
若来源状态原本由 \(h_i\mid p+4Da_i\) 产生，则每个条件等价于
\(AD'\equiv Da_i\pmod{h_i}\)。若
\(\mathscr S_{D'}(p;\mathbf h)\ne\varnothing\)，任取 \(A\) 得到投影源参数纤维
\(P'_{D',A}\)；其每个源块都合法地整除 \(p+4AD'\)。

式 (4) 是有限 source-switch/Type II 参数纤维门，不是抽象商的自动解释。若
某个子列表的乘积 \(h_S\equiv-1\pmod{4D'}\)，则该子列表直接给出 Type II 终端
\[
K_S=(h_S+1)/(4D'),\qquad B_S=(K_Sp+A)/h_S,
\tag{5}
\]
不应再被登记为“目标仍缺失的递降后继”。

## 2. 三分定理

对每个候选 \(D'<D_*\)，恰有以下三类之一。

### A. 稳定子包含：可提升降模边

若

\[
\boxed{C_{D'}\subseteq T,}
\tag{6}
\]

则 \(P\) 对 \(C_{D'}\) 饱和：

\[
\boxed{
P=\rho_{D'}^{-1}\bigl(\rho_{D'}(P)\bigr).
}
\tag{7}
\]

因此

\[
\boxed{
t\notin P
\Longrightarrow
\rho_{D'}(t)\notin\rho_{D'}(P).
}
\tag{8}
\]

若同时 \(\mathscr S_{D'}(p;\mathbf h)\ne\varnothing\)，且
\(P'_{D',A}=\rho_{D'}(P)\) 的来源标签和目标字段均已通过回译，则得到一个较小模数
Type II 参数纤维状态；若其中某个源子列表命中 \(-1\)，先输出直接 Type II 终端。
否则目标仍缺失，E1--E3 由投影源参数和正规形重算；取
\(W=\operatorname{Sol}(p)\) 的图表无关标记集，E4 是恒等映射。固定降模势

\[
\Phi_{\mathrm{II}}(D',A)
=\bigl(D',A,|\rho_{D'}(G_*)/
\operatorname{Stab}(\rho_{D'}(P))|\bigr)
\tag{9}
\]

按字典序比较时，\(D'<D_*\) 使第一坐标严格下降，故得到

\[
\mathrm{STABILIZER\_CONGRUENCE\_LOWER\_EDGE}.
\tag{10}
\]

### B. 稳定子不包含：核 Fourier 证书

若

\[
\boxed{C_{D'}\not\subseteq T,}
\tag{11}
\]

则存在 \(c\in C_{D'}\) 使 \(Pc\ne P\)。定义

\[
f_c=1_P-1_{Pc}.
\tag{12}
\]

因为 \(f_c\ne0\)，有限阿贝尔群 Fourier 变换的可逆性给出某个角色
\(\chi\in\widehat{G_*}\) 使 \(\widehat f_c(\chi)\ne0\)。而

\[
\widehat f_c(\chi)
=(1-\overline{\chi(c)})\,\widehat{1_P}(\chi),
\tag{13}
\]

所以同时有

\[
\boxed{
\chi(c)\ne1,\qquad
\widehat{1_P}(\chi)\ne0.
}
\tag{14}
\]

输出

\[
\mathrm{CONGRUENCE\_KERNEL\_FOURIER}
=(D',c,\chi,\widehat{1_P}(\chi)).
\tag{15}
\]

这条角色不应被解释为低模数递降；它是“该候选降模核没有被当前源积集稳定子吸收”
的构造性对偶证书。

若同时出现低模数伪命中

\[
\rho_{D'}(t)\in\rho_{D'}(P),
\tag{16}
\]

则目标截面

\[
S_t^{(D')}=
\{k\in C_{D'}:tk\in P\}
\tag{17}
\]

非空；因为 \(t\notin P\)，它是 \(C_{D'}\) 的真子集。于是

\[
\boxed{
\sum_{\substack{\psi\in\widehat{C_{D'}}\\\psi\ne1}}
\left|\sum_{k\in S_t^{(D')}}\overline{\psi(k)}\right|^2
=|S_t^{(D')}|\bigl(|C_{D'}|-|S_t^{(D')}|\bigr)>0.
}
\tag{18}
\]

式 (18) 是 LOWER_PSEUDOHIT_KERNEL_SPLIT；它必须继续通过源关系格和算术
source-switch，而不能直接算作 Type II。

### C. 稳定子门通过但算术回译为空

若 (6) 成立但

\[
\mathscr S_{D'}(p;\mathbf h)=\varnothing,
\tag{19}
\]

则抽象商缺失确实存在，但没有由当前保留来源 \(\mathbf h\) 生成合法 Type II
参数纤维。
输出

\[
\mathrm{ARITHMETIC\_LIFT\_OBSTRUCTED}
=(D',\mathbf h,\mathscr S_{D'}(p;\mathbf h)=\varnothing).
\tag{20}
\]

这是有限 source-switch 负证书，不是原猜想反例。

## 3. 穷尽性和证明

对固定 \(D'\)，有限群子群包含关系必满足 (6) 或 (11)，不存在第三类。若 (6) 成立，
对任意 \(x\in P\)、\(c\in C_{D'}\) 有 \(xc\in P\)，所以 \(P\) 是每个
\(\rho_{D'}\)-纤维的并，得到 (7)；(8) 随即成立。若来源参数纤维门 (4) 非空，
先检查 \(P'_{D',A}=\rho_{D'}(P)\) 的来源标签是否精确回译；若某个子列表命中
\(-1\)，得到直接 Type II 终端，否则得到 A 中目标仍缺失的参数纤维和 E1--E5 候选。

若 (11) 成立，取 \(c\) 使 \(Pc\ne P\)，(12)--(14) 是 Fourier 可逆性和
平移公式的直接推论，得到 B。若 (6) 成立而来源参数纤维门为空，则正是
(19)--(20)，得到 C。
因此三分是有限且互斥的。

## 4. 边界实例

在 \(p=97\)、\(G_*=U(24)\)、\(P=\{1,11\}\) 中，

\[
T=\{1,11\}.
\]

对 \(D'=1\)，

\[
C_1=\ker(U(24)\to U(4))
=\{1,5,13,17\}\not\subseteq T.
\tag{21}
\]

取 \(c=5\)，有

\[
Pc=\{5,7\}\ne P,
\]

所以 B 分支成立。另一方面
\(\rho_1(-1)=-1\in\rho_1(P)\)，目标核截面为
\(S_t^{(1)}=\{13\}\)，式 (18) 的能量为
\(1\cdot(4-1)=3\)。这同时展示了低模数伪命中、稳定子失败和核 Fourier
三者的精确关系。

若某个实例满足 (6) 且来源参数纤维门非空，则按直接命中/目标缺失转入 A；若仅有
(6) 而来源参数纤维门为空，则转入 C，
不允许把商缺失当作递归边。

## 5. 研究边界

该三分把每一个候选降模 \(D'\) 的状态级出口完整化为：

\[
\boxed{
\text{稳定子包含且算术可回译}
\;\lor\;
\text{核 Fourier/伪命中截面}
\;\lor\;
\text{算术提升空障碍}.
}
\tag{22}
\]

它仍未证明对每个核心素数至少有一个 \(D'\) 落入 A，也未证明 B/C 必然转入另一条
Type I/II 短证书或已闭合的良基递降；这些仍是全局选择器的最后存在性缺口。
