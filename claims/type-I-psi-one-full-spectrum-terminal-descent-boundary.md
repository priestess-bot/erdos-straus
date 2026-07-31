---
kind: claim
claim_id: type-I-psi-one-full-spectrum-terminal-descent-boundary
title: 完整 F 谱中四百八十三个缺陷一状态的终端与提升边界
statement: 冻结的 200 个压力素数共有 2752 个 finite-exponent F 状态；完整枚举 13533050 个正向一层面点后，恰有 483 个 Psi_0=1 状态和 1615 条正向见证，旧 55 态是其真子集。内部缺口、双秩 accepted 闭包、一步 rejected 前瞻及跨图表中心谱依次把直接证书覆盖推进到 328、475、479 态，留下四个状态局部残余；它们分别由状态外 gap 43、19、19、15 的 Type I 证书闭合，所以该有限样本最终 483/483 有直接证书。另一方面，完整广义二进枚举在 483/483 态产生 3976 个较小偶前驱，但自然标记分母 alpha=nK/E 从不等于 n/2 或 n，且 F 分类使自然标记源为空；这些前驱均未满足 E4，不能计作证明闭合。该结果是冻结有限边界，不是全称选择器定理。
claim_status: computationally_reproduced
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-I-f-bounded-fourier-certificate
  - type-I-f-psi-one-nearest-fiber-escape-boundary
  - internal-support-gap-residue-pullback
  - type-I-formal-ranked-pruning-and-external-gap-selector
  - type-I-generalized-dyadic-natural-lift-equivalence
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - F-state
  - Psi-one
  - full-spectrum
  - terminal-first
  - formal-transition
  - cross-chart
  - generalized-dyadic
  - solution-lift
  - finite-selector
  - proof-boundary
sources:
  - claim: type-I-f-bounded-fourier-certificate
    role: frozen-full-F-spectrum
  - claim: type-I-formal-ranked-pruning-and-external-gap-selector
    role: ranked-formal-candidate-generator
  - claim: internal-support-gap-residue-pullback
    role: internal-direct-terminal
  - claim: type-I-generalized-dyadic-natural-lift-equivalence
    role: E4-boundary
visibility: public
last_checked: '2026-07-31'
---

# 完整 F 谱中 483 个缺陷一状态的终端与提升边界

## 1. 扩展样本与完整一层壳

输入是冻结的 200 个 \(B>1\) 压力素数的完整线性谱。其中 2752 个状态被精确分类为
`finite_exponent`：目标 \(-1\) 属于 \(K\) 支撑生成的子群，但原指数盒中没有目标表示，
因而都是 F 状态。

对每个

\[
K=\prod_iq_i^{\nu_i}
\]

逐坐标固定

\[
z_j=\nu_j+1,
\qquad |z_i|\le\nu_i\quad(i\ne j),
\tag{1}
\]

并直接核验 \(\prod_iq_i^{z_i}\equiv-1\pmod R\)。完整检查

\[
13{,}533{,}050
\]

个正向一层面点后，得到

\[
\boxed{483\text{ 个 }\Psi_0=1\text{ 状态， }1615\text{ 条正向见证}.}
\tag{2}
\]

此前平方终端链中的 55 态、140 条见证完整包含在 (2) 中，但只是这个集合的真子集。

## 2. 直接证书通道

每态依次运行：

1. 全部合法内部缺口 \(M\mid K\) 的 Type I/II 完整平方除子谱；
2. \((m,\min(A,B))\) 秩的 accepted 闭包与一步 rejected 后继终端检查；
3. 对称的 \((m,\max(A,B))\) 两层检查；
4. 双秩仍遗漏时，把外部候选 \(Q\) 作为新模数，完整检查 \(K_Q^2\) 中心谱。

形式边仍只生成候选；每次命中都重新恢复原素数的三个分母并精确验证单位分数恒等式。

| 通道 | 命中状态 |
|---|---:|
| 内部 \(M\mid K\) | 328 |
| min accepted 节点 | 430 |
| min 一步前瞻 | 392 |
| min 两范围并集 | 455 |
| max accepted 节点 | 441 |
| max 一步前瞻 | 384 |
| max 两范围并集 | 459 |
| 双秩并集 | 467 |
| 内部与双秩并集 | 475 |
| 再加跨图表中心谱 | 479 |

按实际优先级，累计覆盖为

\[
328\to468\to473\to473\to475\to479.
\tag{3}
\]

这里 max accepted 没有在 min 两层之后独占新增状态，max rejected 前瞻新增 2 态。完整内部
菜单共有 11406 个合法缺口、666 个规范命中；双秩终端范围的外部候选并集共有 29058 个
缺口、5166 个规范命中。

## 3. 跨图表独占命中

跨图表在内部与双秩遗漏中独占闭合四态。规范首命中为：

| 原 \((p,R)\) | 新模数 \(Q\) | 中心除子 \(D\) | 真实 Type I 缺口 |
|---:|---:|---:|---:|
| \((5596369,35)\) | 11 | 85 | 31 |
| \((37793809,623)\) | 31 | 8300 | 1071 |
| \((536944489,7367)\) | 19 | 869 | 183 |
| \((556685089,199)\) | 19 | 71466329 | 15045543 |

最小第一行明确否定了旧 55 态上观察到的“内部菜单或 min 外部直接缺口必命中”的外推：
在 \((5596369,35)\) 处，局部直接候选全部失败，只有把 \(Q=11\) 用作中心谱候选生成器
后才得到真实 gap 31 证书。

## 4. 四个状态局部残余

上述全部状态局部菜单仍遗漏

\[
\boxed{
(37793809,35),\quad
(78268369,8895),\quad
(174600409,20631),\quad
(278505049,231).}
\tag{4}
\]

它们不是猜想反例。对原素数执行独立的小缺口终端优先扫描，分别得到：

| \(p\) | gap | \(x=(p+\text{gap})/4\) | Type I 除子 \(d\) |
|---:|---:|---:|---:|
| 37793809 | 43 | 9448463 | 8789857 |
| 78268369 | 19 | 19567097 | 1361 |
| 174600409 | 19 | 43650107 | 4200193 |
| 278505049 | 15 | 69626266 | 2066 |

四张证书都从 \(d\mid x^2\)、gap\(\mid px+d\) 独立恢复并验真。因此对这个冻结样本，
在状态局部菜单后补固定缺口集合 \(\{15,19,43\}\) 即达到 483/483。这个有限闭合同时
暴露了当前形式候选生成器的不完备，不能解释为一个无样本上界的选择器。

## 5. 完整广义二进菜单为何仍是零分支

对 483 态完整枚举互素 \(a,b\mid2K\) 及所有合法 \(j\)，得到：

\[
483/483\text{ 态有较小偶前驱},
\qquad3976\text{ 个候选},
\qquad1385\text{ 个逐态不同的 }n.
\tag{5}
\]

每态规范首候选均有 \(j=1\)，全集最大 \(j=24\)，单态最多 60 个候选。特别地，(4) 的
四态分别有 3、15、60、10 个候选。

若只看未标记偶数 \(n\)，(5) 似乎会把全部状态闭合；这是错误计数。对每个候选，

\[
\alpha=\frac{nK}{E}
\]

确实都是整数，但 3976 个候选中

\[
\#\{\alpha=n/2\}=0,
\qquad
\#\{\alpha=n\}=0.
\tag{6}
\]

更强地，[自然标记提升等价](type-I-generalized-dyadic-natural-lift-equivalence.md)证明：
包含 \(\alpha\) 的源解非空，当且仅当 \(R/K\) 可分成两个单位分数，也就是当前图表已有
中心 Type I 除子。这里 483 态全是 F 状态，所以自然标记源全部为空。故 (5) 中所有对象
只能登记为 `unlifted_generalized_dyadic_candidate`，不能计入 (3) 的直接证书，也不满足
E4 递降合同。

## 6. 当前真正的下一步

这次扩展把主缺口进一步定位为：

1. 不再把“存在较小偶数 \(n\)”当作终点；它在完整样本中已经饱和，却没有推进 E4；
2. 对 (4) 优先研究不要求标记分母 \(nK/E\) 的一分母或两分母提升，或构造合法的换支撑
   图表；
3. 全称引理必须使用整个源可达域中的终端或合法边，不能要求汇 SCC 自身含证书；
4. 固定 \(\{15,19,43\}\)、479/483 或 483/483 都只是冻结有限现象。

## 7. 复现

```bash
python3 reproductions/type_i_psi_one_full_spectrum_terminal_descent_audit.py --workers 6
python3 reproductions/type_i_psi_one_full_spectrum_terminal_descent_audit.py --workers 6 --verify
```

结果文件：

```text
reproductions/type-i-psi-one-full-spectrum-terminal-descent-audit-results.json
```

脚本与结果 SHA-256 分别为
`fbd6bec0493a0216c68c2e96352f6e2e67b1bca455d55799c6f29f489968a7b5`、
`6cac496237cf87359a7e915a3f824a3837fe1ced070e06a4edff191aa773978c`。
