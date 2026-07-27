---
kind: claim
claim_id: type-II-fixed-quadratic-character-boundary
title: Type II 核心活跃二次特征的固定化边界
statement: 对固定模数 M，所有核心活跃的支撑外 Type II 失败都落在有限个固定二次特征核的并中；但这不单独增加 Type II 半横截面筛的局部筛维，因为每个特征核本身只是一个半大小目标自由横截面，且 chi(p)=1 已由全部素因子在该核中推出。并且在射线 (A,C)=(5,4)、M=80，两个实际核心失败 p=601 和 p=3169 分别只允许互异的活跃二次特征，故单一固定特征不能统一覆盖该射线的所有核心活跃失败。
claim_status: established
topics:
- type-II
- divisor-residues
- quadratic-character
- sieve
- obstruction
- proof-program
sources:
- paper: grynkiewicz_marchan_ordaz2009
  locator: "subsequence-product framework"
  role: structural-context
- paper: elsholtz_tao2013
  locator: "Appendix A, shifted-prime additive functions and sieve estimates"
  role: sieve-context
- paper: chamberland2026
  locator: "Theorem 1"
  role: Type-II-application-context
visibility: public
last_checked: '2026-07-24'
---

# Type II 核心活跃二次特征的固定化边界

## 固定有限并

令 \(M=4AC\)、\(G=U(M)\)，并令

\[
H_M=\{r\in U(M):r\equiv1\pmod{\gcd(M,24)}\}.
\]

定义只依赖 \(M\) 的有限集合

\[
\mathcal X_M^\ast=
\{\chi\in\operatorname{Hom}(G,\{\pm1\}):
\chi(-1)=-1,\ \chi|_{H_M}\ne1\}. \tag{1}
\]

若一个支撑外失败满足

\[
-1\notin KG^2,\qquad H_M\not\subset KG^2, \tag{2}
\]

则 type-II-target-outside-support-quadratic-separation 给出
\(\chi\in\mathcal X_M^\ast\)，使 \(K\subseteq\ker\chi\)。因此每个核心活跃失败
都落在有限个固定条件

\[
\{\text{全部素因子残数属于 }\ker\chi,\quad \chi(p)=1\},
\qquad \chi\in\mathcal X_M^\ast, \tag{3}
\]

的并中。

## 为什么这不自行增加筛维

在 (3) 中，\(\ker\chi\) 是不含 \(-1\) 的指数二子群，因而只是 Type II
半大小横截面中的一个特例。全部素因子已在 \(\ker\chi\) 内时，其乘积
\(N\equiv p\pmod M\) 也在其中，所以 \(\chi(p)=1\) 是同一条件的乘积推论，
不是第二个独立局部禁根。

因此把自适应特征改写成 (1) 的有限并，至多缩小固定射线的横截面选择常数；它不单独
把 type-II-ac-rays-superlog-residual 的每条射线半筛维提升为更大的指数。想获得新筛维，
必须证明不同射线的特征选择不能独立变化，或从平方饱和核取得额外限制。

## 单一固定特征的反例

对 \((A,C)=(5,4)\)，有 \(M=80\)。在
\(U(80)/U(80)^2\) 中取计算得到的基 \((3,7,11)\)。令
\(\chi_3\) 与 \(\chi_{11}\) 分别为在该基的第一个、第三个坐标上取负的二次特征。

精确因子审计显示：

| 核心素数 | 可用的核心活跃分离特征 |
|---|---|
| \(p=601\) | 仅 \(\chi_3\) |
| \(p=3169\) | 仅 \(\chi_{11}\) |

两者都是此射线的支撑外核心活跃失败。因此不存在一个固定二次特征，能覆盖该射线的
全部核心活跃失败。这否定了“每条射线选定一个字符即可统一处理”的最简单强化式；它不否定
有限个特征的并，也不否定更强的跨射线相容性定理。

## 复现

运行 python3 reproductions/divisor_residue_structure.py --audit-limit 10000 --ac-bound 5。
单元测试固定上述两个互斥特征集合，并检查审计输出中的交集为空。
