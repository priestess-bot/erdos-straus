---
kind: claim
claim_id: type-I-linear-half-block-kneser-square-terminal-profile
title: 平方终端半块的 Kneser 缺陷与二进逃逸剖面
statement: 在冻结的 253 个多支持平方终端候选中，均可写为 p=a+s+asR、R=3 mod 8、a=s=3 mod 4，令 G=(aR+1)/2、H=(sR+1)/2、K=GH、X=A_R(G)、Y=A_R(H)、T=Stab_{H_R(K)}(XY)。253 个状态全部为 F 型，且 |XT|+|YT|-|T| <= |H_R(K)|/2-4；没有 Kneser 临界等号。稳定子阶只有 1 或 2（245 与 8 个状态），其中 119 个满足 -1 in <2 mod R>，134 个属于复合模数的二进逃逸分支；对全部 253 行，用 {2} 加至多 3 个 K 素因子即可生成 H_R(K)，二进逃逸分支的最小附加素因子数分布为 108、24、2。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- linear-source
- half-block
- kneser
- stabilizer
- two-adic
- square-terminal
- finite-spectrum
- boundary
- proof-program
sources:
- claim: type-I-linear-half-block-square-terminal-bridge
  role: half-block-square-terminal-interface
- claim: type-I-linear-two-block-kneser-f-obstruction
  role: F-type-Kneser-necessary-condition
- claim: type-I-linear-two-adic-kneser-terminal-selector
  role: two-adic-escape-interface
visibility: public
last_checked: '2026-07-30'
---

# 平方终端半块的 Kneser 缺陷与二进逃逸剖面

## 冻结对象

输入是多支持溢出分支中已经去重的 253 个平方终端
\((p,R,\operatorname{source},E)\)。每一行都恢复为线性源

\[
p=a+s+asR,
\qquad
G=\frac{aR+1}{2},
\qquad
H=\frac{sR+1}{2},
\qquad
K=GH.
\]

冻结样本满足

\[
R\equiv3\pmod 8,
\qquad
a\equiv s\equiv3\pmod4.
\]

对每行精确计算

\[
X=\mathcal A_R(G),
\quad
Y=\mathcal A_R(H),
\quad
XY=\mathcal A_R(K),
\quad
T=\operatorname{Stab}_{\mathcal H_R(K)}(XY).
\]

环境子群阶由 (K) 的素因子支撑的 CRT 对数格精确恢复；稳定子只需在有限积集
\(XY\) 中检查，因为 (1\in XY)。

## 结果

结果文件
`reproductions/type-i-f-square-half-block-kneser-profile-results.json` 的 SHA-256 为

```text
680d290b79ab9ca4cc6a4d8940c3aa5ad4ef7884a115153c82bb85bba36042c3
```

得到：

```text
candidate_count: 253
unique_R_count: 195
all_target_in_generated_subgroup: true
all_kneser_inequalities_valid: true
stabilizer_size_histogram: {"1": 245, "2": 8}
kneser_equality_count: 0
minimum_kneser_slack: 4
minus_one_in_<2 mod R>: 119
two_adic_escape: 134
full_support_rank_with_two_histogram: {"0": 87, "1": 138, "2": 26, "3": 2}
two_adic_escape_full_support_rank: {"1": 108, "2": 24, "3": 2}
```

这里的 `kneser_slack` 定义为

\[
\operatorname{slack}
=\frac{|\mathcal H_R(K)|}{2}
-\bigl(|XT|+|YT|-|T|\bigr).
\]

因此所有 253 行都满足严格的 F 型半密度缺陷，且没有一行处于 Kneser 临界等号。
119 行满足 \(-1\in\langle2\bmod R\rangle\)；其余 134 行全部来自复合 (R)，
是二进子群不能提供反足点的逃逸分支。96 个素数 (R) 全部属于前 119 行，另有
23 个复合 (R) 也属于前一分支。更精确地，在 134 个逃逸状态中，108 个只需加入一个
K 的素因子、24 个需加入两个、2 个需加入三个，即可使 \(\{2\}\) 与这些素因子
生成整个 \(\mathcal H_R(K)\)。

## 含义与边界

该剖面支持如下有限分流：

\[
\begin{array}{c}
\text{半块平方终端}\
\downarrow\\
\begin{cases}
-1\in\langle2\rangle:\text{二进逃逸已关闭，剩余是严格 Kneser 缺陷};\\
-1\notin\langle2\rangle:\text{复合模数二进逃逸，仍只需至多三个额外素因子生成元}.
\end{cases}
\end{array}
\]

它没有证明所有线性状态都具有这些奇偶型式，也没有把低秩支撑生成元转化为有限盒
目标命中或算术递降。下一步的理论问题是解释最小缺陷 4 及稳定子阶至多 2 是否来自
半块的二进端点结构，并把这组规范的低秩支撑需求接入跨状态容量收费。

这里的“最小缺陷 4”只属于冻结样本，不能表述为一般半块定理。小范围反例
\(p=241\)、\(R=11\)、\((a,s)=(3,7)\) 已给出同类 F 状态的 Kneser 等号；因此
后续证明不能依赖一个统一的正缺陷下界。

该反例的显式数据为
\[
G=17,\quad H=39,\quad K=663=3\cdot13\cdot17,
\quad X=\{1,6\},\quad Y=\{1,2,3,6\},
\]
其中 \(\mathcal H_{11}(K)=\mathbb Z_{11}^{\times}\)、\(T=\{1\}\)，故
\(|X|+|Y|-1=5=|\mathcal H_{11}(K)|/2\)，而
\(XY=\{1,2,3,4,5,6,7\}\) 与其反足集不交。

## 复现

```text
python3 reproductions/type_i_f_square_half_block_kneser_profile.py
```

脚本锁定输入平方终端结果的 SHA-256，并逐行检查半块谱分解、F 型反足点缺失、
稳定子闭合和 Kneser 不等式。
