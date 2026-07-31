---
kind: claim
claim_id: type-I-generalized-dyadic-standard-even-lift-boundary
title: 广义二进前驱的标准偶源分类与完整提升零边界
statement: 对广义二进偶前驱 n<p，标准解 (n/2,n,n) 的全部一分母保留提升按 E 与 2K、3K 的位置精确分成非正余量、缺口 2n-p 或 4n-p 的直接 Type I/II，以及保留大坐标 n 的 Type I 重图表；任何成功都已是原 p 的直接终端，不是新的 E4 递降边。另令 H=n^2/E，并规范化 E=A^2C、H=B^2C、n=ABC。E-split 的两个尾替换分别等价于 Q_H=Ap-2(p-n)(A+B)>0、Q_H|n/2 或 Q_E=Bp-2(p-n)(A+B)>0、Q_E|n/2；成功时显式恢复 4K'=pR'+1 的中心 Type I 重图表，且 R'=R 当且仅当被替换尾是自然标记 alpha=nK/E。冻结 483 个 Psi_0=1 F 状态的 3976 条原始表示去重为 1385 个前驱；完整检查 3792095 个标准一分母因子对与 2770 个 E-split 通道，命中均为零。该零结果是有限边界，不是全称障碍。
claim_status: computationally_reproduced
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-I-generalized-dyadic-natural-lift-equivalence
  - one-denominator-lift-factor-criterion
  - two-denominator-lift-criterion
  - middle-coordinate-lift-certificate-equivalence
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - generalized-dyadic
  - even-predecessor
  - standard-even-source
  - E-split
  - solution-lift
  - finite-boundary
  - proof-boundary
sources:
  - claim: one-denominator-lift-factor-criterion
    role: complete-one-retained-coordinate-factorization
  - claim: two-denominator-lift-criterion
    role: E-split-tail-replacement
  - claim: type-I-generalized-dyadic-natural-lift-equivalence
    role: predecessor-arithmetic-and-natural-lift-boundary
visibility: public
last_checked: '2026-07-31'
---

# 广义二进前驱的标准偶源分类与完整提升零边界

## 1. 标准偶源的一分母通道没有新递降类型

设

\[
4K=pR+1,
\qquad
nR=4K-E,
\qquad
0<n<p,\qquad n\equiv0\pmod2,
\tag{1}
\]

其中 \(p\) 是奇素数、\(R>3\) 为奇数，且 \(E\) 是合法广义二进终端。较小方程有
标准解

\[
\frac4n=\frac1{n/2}+\frac1n+\frac1n.
\tag{2}
\]

保留一个源分母 \(c<p\) 时，令

\[
M=4c-p,\qquad S=pc.
\tag{3}
\]

[一分母提升判据](one-denominator-lift-factor-criterion.md)说明，成功当且仅当 \(M>0\)，
且存在无序因子对 \(ef=S^2\) 满足

\[
e\equiv f\equiv-S\pmod M.
\tag{4}
\]

条件 (4) 不读取源解的另外两个坐标；一旦命中，它已经显式恢复 \(4/p\) 的三分母解。
所以它是直接终端，而不是必须递归证明非空的标记边。

又因 \(p\nmid c\)，把规范因子写成 \(e=p^ad\)、\(d\mid c^2\)，则 \(c<p\) 与
\(e\le pc\) 排除 \(a=2\)，只剩：

- \(a=0\) 的 Type I 因子；
- \(a=1\)、\(d\le c\) 的 Type II 因子。

由 (1) 比较 \(n\) 与 \(p/2,p/4\)，并注意 \(E=2K,3K\) 都与
\(E\equiv1\pmod R\)、\(4K\equiv1\pmod R\) 矛盾，得到严格三分：

| \(E\) 的范围 | \(n\) 的范围 | 标准坐标通道 |
|---|---|---|
| \(E>3K\) | \(n<p/4\) | \(n/2,n\) 的余量均非正 |
| \(2K<E<3K\) | \(p/4<n<p/2\) | 只有 \(c=n\) 可行，正好是 gap \(4n-p\) 的直接 Type I/II |
| \(E<2K\) | \(n>p/2\) | \(c=n/2\) 是 gap \(2n-p\) 的直接 Type I/II；\(c=n\) 若成功，只是另一张首分母更小的 Type I 重图表 |

最后一格中 \(c=n>p/2\) 不可能属于 Type II：若 \(e=pd\)，重组出的另两个分母
都是 \(p\) 的倍数，故其倒数和至多 \(2/p\)，而 \(1/n<2/p\)，总和严格小于
\(4/p\)。因此这里只剩 Type I。

这给出一个无样本上界的结论：标准偶源的一分母通道可能产生直接证书，但永远不产生
第三种、独立于 Type I/II 的 E4 递降类型。

## 2. 一个普适的 E-split 显式源

由自然提升算术已有 \(E\mid n^2\)。记

\[
H=\frac{n^2}{E}.
\tag{5}
\]

事实上 \(H\) 必为偶数。令 \(u=v_2(4K)\)、\(e=v_2(E)\)、\(t=v_2(n)\)。
若 \(e<u\)，则 \(t=e\)；若 \(e>u\)，则 \(t=u\)，而合法二进条件
\(E\mid(2K)^2\) 给出 \(e\le2u-2\)；若 \(e=u\)，两个奇部相减给出
\(t\ge u+1\)。三种情形都有

\[
v_2(H)=2t-e\ge1.
\tag{6}
\]

写 \(n=2s,E=2x,H=2y\)，则 \(xy=s^2\)，从而

\[
\boxed{
\frac4n
=\frac1s+\frac1{s+x}+\frac1{s+y}
=\frac1{n/2}+\frac1{(n+E)/2}+\frac1{(n+H)/2}.
}
\tag{7}
\]

这比平凡解 (2) 使用了终端 \(E\) 的结构。若替换 \((n+T)/2\) 并保留另两项，
其中 \(T\in\{E,H\}\)，[两分母提升判据](two-denominator-lift-criterion.md)化为

\[
D_T=n(2n-p)-2(p-n)T>0,
\qquad
D_T\mid\frac{np(n+T)}2.
\tag{8}
\]

成功时新分母为 \(np(n+T)/(2D_T)\)。但 (7) 的两个通道都保留 \(n/2\)，所以
(8) 一旦成功，仍精确嵌入 gap \(2n-p\) 的一分母完整因子空间。它提供显式候选源，
却仍不是新递降类型。

## 3. E-split 命中的规范中心重图表

令

\[
\delta=p-n=\frac{E-1}{R}.
\tag{9}
\]

因为 \(EH=n^2\)，存在唯一的互素正规化

\[
E=A^2C,\qquad H=B^2C,\qquad n=ABC,\qquad(A,B)=1.
\tag{10}
\]

由 \(E,H\) 都是偶数可知 \(C\) 为偶数。记 \(S=A+B\)，则 E-split 两个尾为

\[
c_E=\frac{n+E}{2}=\frac{ACS}{2},
\qquad
c_H=\frac{n+H}{2}=\frac{BCS}{2}.
\tag{11}
\]

### 3.1 替换 H-tail

替换 \(c_H\)、保留 \(n/2,c_E\) 时，定义

\[
Q_H=Ap-2\delta S.
\tag{12}
\]

式 (8) 的判别量恰为 \(D_H=BCQ_H\)。又
\(\gcd(Q_H,pS)=1\)，所以整除条件严格等价于

\[
\boxed{Q_H>0,\qquad Q_H\mid n/2.}
\tag{13}
\]

这里 \((A,S)=1\)、\(S\le n<p\) 及 \((p,\delta)=1\) 给出
\((Q_H,pS)=1\)。又由 \(\delta R=A^2C-1\) 得 \((A,\delta)=1\)，所以
\((Q_H,\delta)=1\)。在 (13) 下有 \(n\equiv0\)、\(p\equiv\delta\pmod {Q_H}\)，
将其代入 (12) 便得到 \(Q_H\mid A+2B\)。于是

\[
R'_H=\frac{A+2B}{Q_H},
\qquad
K'_H=\frac{nS}{2Q_H}
\tag{14}
\]

都是正整数，并且

\[
4K'_H=pR'_H+1.
\tag{15}
\]

式 (8) 恢复的新分母正是 \(pK'_H\)。保留的两项还满足

\[
\frac2n+\frac2{ACS}=\frac{R'_H}{K'_H},
\]

故成功输出是新图表 \((R'_H,K'_H)\) 上的中心 Type I 直接终端。

### 3.2 替换 E-tail

替换 E-tail 时直接计算得到

\[
Q_E=Bp-2\delta S.
\tag{16}
\]

此时 \(D_E=ACQ_E\)。与上一通道相同，\((Q_E,pS)=1\)，故命中当且仅当

\[
Q_E>0,\qquad Q_E\mid n/2,
\]

又因 \(B\mid n<p\) 且 \(p\) 为素数，有 \((B,\delta)=1\)，进而
\((Q_E,\delta)=1\)。由 \(p\equiv\delta\pmod {Q_E}\) 可得
\(Q_E\mid2A+B\)。成功时

\[
R'_E=\frac{2A+B}{Q_E},
\qquad
K'_E=\frac{nS}{2Q_E},
\qquad
4K'_E=pR'_E+1,
\tag{17}
\]

而被替换尾恢复为 \(pK'_E\)。所以这一通道同样只能产生中心 Type I 重图表，不会产生
Type II 或新的递归状态类型。

### 3.3 自然图表的精确等号条件

两条通道回到原图表的条件为

\[
\begin{aligned}
R'_H=R
&\iff A=B(R-2)
\iff c_H=\alpha=\frac{nK}{E},\\
R'_E=R
&\iff RB^2=A(2A+B)
\iff c_E=\alpha.
\end{aligned}
\tag{18}
\]

第一行结合 \((A,B)=1\) 还推出 \(B=1,A=R-2\)；第二行推出 \(B\mid2\)。方向也由

\[
\operatorname{sgn}(R-R'_H)=\operatorname{sgn}(B(R-2)-A),
\]

\[
\operatorname{sgn}(R-R'_E)=
\operatorname{sgn}(RB^2-A(2A+B))
\]

完全决定。因此 \(R'\ne R\) 精确等价于被替换尾不是自然标记；但即使如此，(15) 或
(17) 已经把它恢复成原 \(p\) 的直接 Type I 证书，而不是一条需要较小状态非空性的
E4 边。

## 4. 483 态完整零审计

输入为完整 F 谱中的 483 个 \(\Psi_0=1\) 状态。3976 条原始 \((j,a,b)\) 表示先按
逐态 \((E,n)\) 去重；否则变换 \((j,a,b)\mapsto(j+1,2a,b)\) 会给同一个前驱制造
虚假重数。去重后共有 1385 个前驱：

| 区间 | raw | 去重后 |
|---|---:|---:|
| \(E<2K\) | 3896 | 1351 |
| \(2K<E<3K\) | 30 | 17 |
| \(E>3K\) | 50 | 17 |

对每个正余量坐标，完整枚举 \((pc)^2\) 的无序因子对 \(e\le pc\)：

| 保留坐标 | 正余量前驱 | \(c^2\) 除子数 | 无序因子对 | 命中 |
|---|---:|---:|---:|---:|
| \(n/2\) | 1351 | 1021941 | 1533587 | 0 |
| \(n\) | 1368 | 1505216 | 2258508 | 0 |
| 合计 | - | - | 3792095 | 0 |

全部 483 态都至少有一个 \(n>p/2\) 候选，所以零命中不是因为提升正域为空。
自然因子 \(e=E\) 在 \(n/2\) 通道有 915 个可用候选，在 \(n\) 通道有 1368 个，
也全部失败。

对 (7) 则检查 1385 个源、2770 个尾替换，其中 2557 个满足 \(D_T>0\)，整除命中仍为
零。原四个状态局部余项含 88 条 raw 表示、12 个不同前驱；其 12274 个一分母因子对
与 24 个 E-split 通道也全部失败。旧坐标菜单的完整 Reach 后剩余两态含 7 个前驱；其
5825 个一分母因子对与 14 个 E-split 通道仍全部失败。

首个冻结反例为

\[
(p,R,K,E,n)=(67369,27,454741,28,67368).
\]

保留 \(n/2,n\) 分别完整检查 203、284 个因子对。它的 E-split 源是

\[
(33684,33698,81077388),
\]

两个正判别量的整除余数分别为 \(3840816\) 与 \(206280816\)，均非零。

实现另锁定了一个域外正例

\[
(p,R,K,E,n)=(97,15,364,676,52),
\]

其中 (7) 的自然通道确实给出

\[
(26,28,364)\longmapsto(26,35308,364).
\]

这确认审计器并非恒零；但该成功恰是已知自然标记 \(28\mapsto pK\)，并且当前图表
已有中心命中。

## 5. 证明边界与下一问题

有限零结果不能外推为“所有 F 态的标准通道都失败”。相反，本页证明的全称部分只是：

1. 一分母保留一旦成功，就已经是直接 Type I/II 证书的重写；E-split 成功更精确地是
   (14) 或 (17) 的中心 Type I 重图表；
2. 它们不能充当独立 E4 递降边；
3. 当前冻结 F 样本恰好全部失败。

若仍研究 E-split，最窄的新问题已由 (18) 化成：核心域中的命中是否必满足相应丢番图
等式。当前已知正例 \(p=97\) 满足 \(R'=R\)，冻结 483 态则没有 E-split 命中；仓库中
目前没有合法的 \(R'\ne R\) 成功例，因此“所有合法成功是否都自然”仍是开放问题。
即使核心域最终出现 \(R'\ne R\)，(14)--(17) 也已证明它应登记为直接 Type I
跨图表终端；真正的递降增量仍须来自不预先包含目标证书的合法状态映射。

## 6. 复现

```bash
python3 reproductions/type_i_psi_one_full_spectrum_standard_even_lift_audit.py
python3 reproductions/type_i_psi_one_full_spectrum_standard_even_lift_audit.py --verify
```

结果文件：

```text
reproductions/type-i-psi-one-full-spectrum-standard-even-lift-audit-results.json
```

脚本与结果 SHA-256 分别为
`ff3321e623cfbb576bfa9c49207477b57ccb6eea546fd3d6375f8d47fc08364d`、
`7fc0cf328fcd5bcd26ebea94efc90dd20dec9261a62ddd3579fece28c6cc3e61`。
