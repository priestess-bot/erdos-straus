---
kind: claim
claim_id: type-I-generalized-dyadic-standard-even-lift-boundary
title: 广义二进前驱的标准偶源分类与完整提升零边界
statement: 对广义二进偶前驱 n<p，标准解 (n/2,n,n) 的全部一分母保留提升按 E 与 2K、3K 的位置精确分成非正余量、缺口 2n-p 或 4n-p 的直接 Type I/II，以及保留大坐标 n 的 Type I 重图表；任何成功都已是原 p 的直接终端，不是新的 E4 递降边。另令 H=n^2/E，则 H 必为偶数，且 (n/2,(n+E)/2,(n+H)/2) 是显式 E-split 源解；它的两个两分母保留通道同样保留 n/2，成功仍只是直接缺口终端。冻结 483 个 Psi_0=1 F 状态的 3976 条原始表示去重为 1385 个前驱；完整检查 3792095 个标准一分母因子对与 2770 个 E-split 通道，命中均为零。该零结果是有限边界，不是全称障碍。
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

## 3. 483 态完整零审计

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
与 24 个 E-split 通道也全部失败。完整 Reach 后真正剩余的两态含 7 个前驱；其
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

## 4. 证明边界与下一问题

有限零结果不能外推为“所有 F 态的标准通道都失败”。相反，本页证明的全称部分只是：

1. 一分母保留或 E-split 一旦成功，就已经是直接 Type I/II 证书的重写；
2. 它们不能充当独立 E4 递降边；
3. 当前冻结 F 样本恰好全部失败。

若仍研究 E-split，最窄的新问题是：在 (8) 成功时，恢复的新图表是否必等于自然图表。
自然分支会回到 \(\alpha=nK/E\)；若能出现不同图表，它才可能暴露新的跨状态结构。

## 5. 复现

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
