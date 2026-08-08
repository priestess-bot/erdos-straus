---
kind: claim
claim_id: type-II-target-fiber-owner-weighted-fourier-capacity-bridge
title: 目标纤维 owner 加权谱到稳定子 Fourier—q 容量的桥
statement: 固定核心素数 p、当前 D 层的声明 source profile 与严格目标纤维 f=(d',A)。对每个共同 q 高度 j 记录可支付的 owner 数 omega_q(j)，并在 G_f=<q mod 4d'> 中构造 owner 加权群代数谱 W_f。若 t=-1 不在 G_f，得到 G 型支撑分离；若 W_f(t)>0，任一正系数指数向量给出带 owner 标签的目标 Type II 证书；若 W_f(t)=0，则加权稳定子商 G_f/P_f 上存在规范非平凡 Fourier 角色，其相关实部至少为 V_f/(|G_f/P_f|-1)。只有该角色通过源关系 SNF、算术相位和 owner 对齐门后，才可产生 q-prefix 请求；每层请求数受目标 owner 槽数和重复度的严格上界约束。该桥保留 owner multiplicity，强于去重乘积集 Fourier，但不把不可提升角色自动升级为容量超载或递归边。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-i-linear-escape-target-supply-spectrum-strict-adapter
  - type-I-fixed-layer-stabilizer-defect-reduction
  - type-I-fg-fourier-phase-owner-capacity-bridge
  - type-II-hall-bundle-target-residue-fourier-gate
  - type-II-source-fiber-shared-q-ledger
topics:
  - type-II
  - target-fiber
  - owner-weight
  - Fourier
  - stabilizer
  - q-adic-capacity
  - F-state
  - G-state
  - source-switch
  - proof-program
sources:
  - claim: type-i-linear-escape-target-supply-spectrum-strict-adapter
    role: target-specific-common-q-height
  - claim: type-I-fixed-layer-stabilizer-defect-reduction
    role: stable-quotient-Fourier-interface
  - claim: type-I-fg-fourier-phase-owner-capacity-bridge
    role: phase-and-owner-capacity-gate
  - claim: type-II-hall-bundle-target-residue-fourier-gate
    role: unweighted-residue-Fourier-contrast
  - claim: type-II-source-fiber-shared-q-ledger
    role: repeated-q-height-accounting
  - reproduction: reproductions/type_ii_target_fiber_owner_weighted_fourier_capacity_bridge.py
    role: p409-F-gap-p57399241-G-separation-p5113-hit-controls
visibility: public
last_checked: '2026-08-09'
---

# 目标纤维 owner 加权谱到稳定子 Fourier—q 容量的桥

## 1. 目标纤维与 owner 权重

固定核心素数 \(p\)、当前层 \(D\)，以及一个已声明 source-complete 的来源 profile
\(\mathcal S\subseteq\mathcal A_D(p)\)。取严格目标

\[
f=(d',A),\qquad d'\mid D,\quad d'<D,\quad A\mid d',
\quad d'/A\text{ 平方自由},\quad4Ad'<p,
\]

并写

\[
s_a=Da,\qquad s_f=Ad',\qquad
N_a=p+4s_a,\qquad N_f=p+4s_f.
\]

对每个 \(q\nmid4d'\) 定义共同高度

\[
\eta_q=\max_{a\in\mathcal S}\min\{v_q(N_a),v_q(N_f)\}.
\tag{1}
\]

若 \(\eta_q>0\)，对 \(1\le j\le\eta_q\) 定义可支付的 owner 数

\[
\omega_q(j)=
\#\{a\in\mathcal S:
v_q(N_a)\ge j,\ v_q(N_f)\ge j\}.
\tag{2}
\]

这里允许同一 source row 为不同 q 复用 owner；若具体 source contract 禁止这种
复用，应将下面的积权重替换为显式兼容 owner assignment 数，Fourier 恒等式仍然
逐项成立。令

\[
\mathcal U_f=\prod_{\eta_q>0}\{0,1,\ldots,\eta_q\},
\qquad
\omega_f(\mathbf u)=
\prod_{q:u_q>0}\omega_q(u_q),
\tag{3}
\]

空指数的权重约定为 \(\omega_f(\mathbf0)=1\)。定义

\[
G_f=\left\langle q\bmod4d':\eta_q>0\right\rangle
\le U(4d'),
\qquad t=-1\bmod4d',
\tag{4}
\]

以及 owner 加权谱

\[
W_f(g)=
\sum_{\substack{\mathbf u\in\mathcal U_f\\
\prod_q q^{u_q}=g}}
\omega_f(\mathbf u),
\qquad
V_f=\sum_{g\in G_f}W_f(g)
=\prod_{\eta_q>0}
\left(1+\sum_{j=1}^{\eta_q}\omega_q(j)\right).
\tag{5}
\]

去掉 \(\omega_f\) 而只记录支撑，正好退化为已有的无权乘积集门；(5) 额外保留
了每个 q 层由多少 owner 支付的信息。

## 2. 加权稳定子与商

定义加权稳定子

\[
P_f=\{x\in G_f:W_f(xg)=W_f(g)\text{ 对所有 }g\in G_f\}.
\tag{6}
\]

这是 \(G_f\) 的子群。令 \(\bar G_f=G_f/P_f\)，则 \(W_f\) 唯一下降为
\(\bar W_f\)，并令 \(\bar t=tP_f\)。若 \(W_f(t)=0\)，则
\(\bar W_f(\bar t)=0\)。当 \(\bar G_f\) 为平凡群时，加权函数必须为常数；由于
\(V_f\ge1\)，这将迫使 \(W_f(t)>0\)，故未命中分支自动满足
\(|\bar G_f|>1\)。

这里的 \(P_f\) 是对加权 source spectrum 的稳定子，不是把未验证的 source row
数量简单当作周期。它使后续 Fourier 分母从 \(|G_f|-1\) 精确收紧到
\(|\bar G_f|-1\)。

## 3. 表示—对偶二分

在 source profile 已闭合后，目标分派按以下顺序进行。

### G 型支撑分离

若

\[
t\notin G_f,
\tag{7}
\]

有限商 \(U(4d')/G_f\) 中存在一个角色在 \(G_f\) 上恒等、在 \(tG_f\) 上非恒等。
因此没有任何 source-supported product 可以命中目标，输出

\[
\mathrm{G\_SOURCE\_SUPPORT\_SEPARATION}.
\]

这不是 Type II 空集的全局结论；raw 因子、外部 source 或其它参数纤维仍须独立处理。

### 加权命中

若 \(t\in G_f\) 且

\[
W_f(t)>0,
\tag{8}
\]

则存在 \(\mathbf u\) 和 owner assignment 使
\[
h=\prod_q q^{u_q}\equiv-1\pmod{4d'},
\qquad h\mid N_f.
\]

取该 \(\mathbf u\) 的任一 owner 见证，令

\[
K'=\frac{h+1}{4d'},\qquad
B'=\frac{K'p+A}{h},\qquad
C'=\frac{d'}A.
\tag{9}
\]

与目标共同整除关系给出 \(h\mid K'p+A\)，并且

\[
B'-A=\frac{K'(p-4Ad')+2A}{h}>0.
\tag{10}
\]

所以 \((A,C',K')\) 是直接 Type II 证书；owner assignment 保留了来源标签。只有
需要把它登记为从旧层 \(D\) 出发的递归边时，才另外检查
\(h\equiv-1\pmod{4D}\)、E1--E5 和严格下降势。

### 加权 Fourier 缺口

若 \(t\in G_f\) 但 \(W_f(t)=0\)，对 \(\bar\chi\in\widehat{\bar G_f}\) 定义未归一化
Fourier 系数

\[
\widehat{\bar W}_f(\bar\chi)
=\sum_{\bar g\in\bar G_f}
\bar W_f(\bar g)\bar\chi(\bar g).
\tag{11}
\]

有限群正交关系给出精确恒等式

\[
\sum_{\bar\chi\ne1}
\overline{\bar\chi(\bar t)}
\widehat{\bar W}_f(\bar\chi)
=-V_f.
\tag{12}
\]

因此存在非平凡角色 \(\bar\chi_*\) 使

\[
\boxed{
-\operatorname{Re}\!\left(
\overline{\bar\chi_*(\bar t)}
\widehat{\bar W}_f(\bar\chi_*)\right)
\ge\frac{V_f}{|\bar G_f|-1}.
}
\tag{13}
\]

规范角色按左端递减、角色阶递增、固定群坐标字典序选择。式 (13) 是带 owner
权重的稳定子 Fourier 对偶证书；它比只对去重支撑计数的 Fourier 门保留更多
source capacity 信息。

在独立 owner 模型中，(11) 还可逐 q 分解为

\[
\boxed{
\widehat W_f(\bar\chi)
=\prod_{\eta_q>0}
\left(1+\sum_{j=1}^{\eta_q}
\omega_q(j)\bar\chi(qP_f)^j\right).
}
\tag{14}
\]

若有 owner 兼容限制，则将每个 q 因子替换为完整 assignment 表的有限和；(12)--(13)
不变。

## 4. Fourier 到 F/G 与 q 容量的 typed 拉回

令 \(\Delta_f\) 为当前目标纤维 source relation/difference subgroup。对 (13) 中的
\(\bar\chi_*\) 必须先执行 source-SNF、角色阶和算术相位门：

1. \(\bar\chi_*|_{\Delta_f}=1\) 而 \(\bar\chi_*(\bar t)\ne1\)：输出
   \(\mathrm{G\_SUPPORT\_SEPARATION}\)，不产生 q demand；
2. \(\bar\chi_*|_{\Delta_f}\ne1\)，但阶筛、SNF 或
   \(\gamma\equiv-p4^{-1}\pmod{q^j}\) 失败：输出
   \(\mathrm{SOURCE\_RELATION\_FOURIER\_LIFT\_OBSTRUCTED}\) 或
   \(\mathrm{FOURIER\_PHASE\_OWNER\_NONIDENTIFIED}\)；
3. 只有角色通过这些门，才产生带 q 层的 F 型请求。

对固定 \(q,j\)，定义目标 owner 槽

\[
\mathcal O_{q,j}(f)
=\{s_a=Da:a\in\mathcal S,\
v_q(N_a)\ge j,\ v_q(N_f)\ge j\}.
\tag{15}
\]

因 \(q\nmid4\)，任意 \(s_a\in\mathcal O_{q,j}(f)\) 满足

\[
q^j\mid N_a-N_f=4(s_a-s_f),
\qquad
s_a\equiv s_f\pmod{q^j}.
\tag{16}
\]

因此所有第 \(j\) 层 owner 槽位于同一 q 进残类。若通过 (1)--(3) 的 F 型角色产生
\(R_{q,j}\) 个独立请求、每个 owner 的重复度上限为 \(\mu\)，则有必要条件

\[
\boxed{
R_{q,j}\le\mu\,|\mathcal O_{q,j}(f)|.
}
\tag{17}
\]

若 (17) 失败，输出严格的
\(\mathrm{Q\_ADIC\_TARGET\_OWNER\_CAPACITY\_DEFICIT}\)；若通过，仍须继续检查
source-switch、范围、标记解和稳定子商。式 (13) 本身只提供可拉回的对偶角色，
不虚构 \(R_{q,j}\) 的正下界。

## 5. 证明

式 (5) 按指数向量分组，故 (8) 当且仅当存在 owner-labeled 的 \(h\) 命中目标；
(9)--(10) 是 Type II 正规形恒等式。式 (6) 的稳定子定义保证 \(W_f\) 在
\(P_f\)-coset 上常值，所以 \(\bar W_f\) 和 \(\bar t\) 定义良好。

若 \(W_f(t)=0\)，Fourier 反演在 \(\bar t\) 处给出

\[
0=\frac1{|\bar G_f|}
\sum_{\bar\chi}
\widehat{\bar W}_f(\bar\chi)
\overline{\bar\chi(\bar t)}.
\]

平凡角色项为 \(V_f\)，移项即 (12)。共有 \(|\bar G_f|-1\) 个非平凡角色，取
左端最大者得到 (13)。独立 owner 时，群代数乘积直接给出 (14)。

最后，(16) 是两个共同 q 整除式相减并使用 \(q\nmid4\)；所有 owner 因而落在同一
残类，重复度为 \(\mu\) 时装箱上界即 (17)。SNF、相位和 F/G 分派沿用各自的必要
接口，不能由 Fourier 幅度跳过。证毕。

## 6. 三个算术控制

### \(p=409,D=8\)：目标在源群中但加权谱缺口

标准来源为 \(a=4,8\)，严格目标取 \(f=(4,2)\)：

\[
N_{8,4}=537=3\cdot179,\qquad
N_{8,8}=665=5\cdot7\cdot19,
\]

\[
N_f=409+4\cdot2\cdot4=441=3^2\cdot7^2.
\]

所以 \(\eta_3=\eta_7=1\)，owner 均为 1，且

\[
G_f=\langle3,7\rangle=U(16),\qquad
\operatorname{supp}(W_f)=\{1,3,7,21\}\bmod16
=\{1,3,5,7\}.
\]

目标 \(t=15\) 在 \(G_f\) 中但 \(W_f(t)=0\)，而加权稳定子为
\(P_f=\{1,7\}\)，所以 \(|G_f/P_f|=4\)，且 \(V_f=4\)。
用 \(3\)（四阶）和 \(15=-1\)（二阶）坐标标记角色
\(\chi_{1,1}(3)=i,\chi_{1,1}(15)=-1\)，有

\[
\widehat W_f(\chi_{1,1})=2+2i,\qquad
-\operatorname{Re}\bigl(\overline{\chi_{1,1}(15)}
\widehat W_f(\chi_{1,1})\bigr)=2
\ge\frac43.
\]

这是“\(-1\) 属于源生成群”却没有 source-supported adapter 的严格 F 型 Fourier
缺口；不能用群生成性替代整数指数谱命中。

### \(p=57399241,D=41\)：owner multiplicity 的 G 分离

取 \(f=(1,1)\)，标准来源 \(a=1,41\)。共同 q 只有 \(q=5\)，且
\(\omega_5(1)=2\)，因此

\[
G_f=\langle5\bmod4\rangle=\{1\},\qquad
W_f(1)=1+2=3,\qquad t=3\notin G_f.
\]

该分支输出 G 型支撑分离，而不是把两个 5 owner 当作两个独立乘法块或 q demand；
它也说明 owner multiplicity 与去重支撑是不同数据。

### \(p=5113,D=6\)：加权谱直接命中

取 active source rows \(a=3,6\)，目标 \(f=(1,1)\)。有

\[
\eta_7=\eta_{17}=1,\qquad
W_f(3)=2,\qquad W_f(1)=2,\qquad t=3.
\]

选择 \(h=7\) 给出 \(K'=2,B'=1461\) 的直接 Type II；若同时保留两个 owner
source blocks，则 \(h=119\) 还满足旧层 \(h\equiv-1\pmod{24}\)，可作为严格
source-switch 候选。

## 7. 研究边界

该桥新增了一个带 owner multiplicity 的表示—对偶对象，并证明其在加权稳定子商上
具有显式 Fourier 缺口下界；它把可提升 Fourier 角色的 q 层容量输入写成 (17)。
它仍不证明 (13) 中规范角色一定通过 SNF/相位门，也不证明所有目标纤维的
\(R_{q,j}\) 有足够正下界。因此全称目标仍需把不可提升角色、owner capacity deficit
和 raw/F/G 终端接入同一个良基势；本卡不把任一局部负证书宣称为原猜想反例。

窄复现：

~~~bash
python3 reproductions/type_ii_target_fiber_owner_weighted_fourier_capacity_bridge.py --verify
~~~
