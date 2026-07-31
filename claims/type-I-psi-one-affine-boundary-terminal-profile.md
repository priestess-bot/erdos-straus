---
kind: claim
claim_id: type-I-psi-one-affine-boundary-terminal-profile
title: 完整 Reach 的仿射边界终端菜单闭合四个状态余项
statement: 对完整 Psi_0=1 F 谱在内部缺口、双秩前瞻和跨图表后留下的四个状态余项，穷尽完整形式 Reach，并从每个节点 (A,B,m) 的 A、B、m、|A-R|、|B-R| 取合法外部 gap 因子，再完整核验 Type I/II 平方除子谱。四态共 254 节点、609 边、298 个逐态 gap、39 个命中，四态全部得到原素数的直接证书；新增首命中分别来自 m、|A-R|、B、m，故冻结 483 态不再需要状态外固定 gap 回退。该结果是四态有限正信号，形式边仍不是递降，仿射边界菜单的全称非空性仍未证明。
claim_status: computationally_reproduced
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-I-f-bounded-fourier-certificate
  - type-I-formal-ranked-pruning-and-external-gap-selector
  - type-I-coprime-factor-normal-form
  - type-II-coprime-factor-normal-form
topics:
  - type-I
  - type-II
  - F-state
  - Psi-one
  - formal-target-pair
  - complete-reach
  - affine-boundary
  - external-gap
  - finite-selector
  - proof-boundary
sources:
  - claim: type-I-psi-one-full-spectrum-terminal-descent-boundary
    role: four-frozen-state-input
  - claim: type-I-formal-ranked-pruning-and-external-gap-selector
    role: raw-transition-and-direct-terminal-interface
visibility: public
last_checked: '2026-07-31'
---

# 完整 Reach 的仿射边界终端菜单闭合四个状态余项

## 1. 严格限定的候选菜单

固定形式可达节点

\[
v=(A,B,m),
\qquad A+B=Rm,
\qquad(A,B)=1.
\tag{1}
\]

定义五个仿射边界量

\[
\mathcal X_R(v)=
\{A,B,m,|A-R|,|B-R|\}\setminus\{0\}.
\tag{2}
\]

这里 \(A,B\) 是旧 external-gap 菜单。其余三项来自形式迁移分子
\(m+t\) 和 \(B+Rt\) 的端点 \(t=0,-1\)，其中交换 \(A,B\) 给出对称的
\(A-R\)。这些端点不冒充合法迁移；它们只生成待独立核验的缺口候选。

对每个 \(X\in\mathcal X_R(v)\) 及 \(h\mid X\)，只保留

\[
h\equiv3\pmod4,
\qquad3\le h\le p-2,
\qquad\frac{h}{(h,K)}>1.
\tag{3}
\]

令 \(x_h=(p+h)/4\)，再完整枚举 \(d\mid x_h^2\)，检查

\[
h\mid px_h+d
\tag{4}
\]

或

\[
d\le x_h,
\qquad h\mid x_h+d.
\tag{5}
\]

式 (4)、(5) 的命中分别作为原素数的 Type I、Type II 直接终端。形式节点和形式边只
负责产生 \(h\)，不进入证书的正确性证明。

## 2. 四个完整 Reach 余项

输入是完整 483 态审计在状态局部菜单后留下的四项。新菜单的精确结果为：

| \((p,R)\) | Reach 节点/边 | 候选/命中 gap | 规范首来源 | 首命中 |
|---:|---:|---:|---|---|
| \((37793809,35)\) | \(20/35\) | \(28/3\) | \(43\mid m=2715622\) | Type I，\(d=8789857\) |
| \((78268369,8895)\) | \(6/6\) | \(9/2\) | \(19\mid|326-8895|=8569\) | Type I，\(d=1361\) |
| \((174600409,20631)\) | \(200/518\) | \(199/23\) | \(19\mid B=20615\) | Type I，\(d=4200193\) |
| \((278505049,231)\) | \(28/50\) | \(62/11\) | \(15\mid m=60\) | Type I，\(d=2066\) |

合计为

\[
254\text{ 个节点},\quad609\text{ 条边},\quad
298\text{ 个逐态候选},\quad39\text{ 个直接命中}.
\tag{6}
\]

特别地，最后两张证书正是旧状态外回退中的 gap \(19,15\)，但现在两者都由同一状态的
完整 Reach 及固定菜单 (2) 产生。因此冻结样本的优先级可写成

\[
328\longrightarrow475\longrightarrow479
\longrightarrow483,
\tag{7}
\]

其中最后一步只对四个余项穷尽完整 Reach 和 (2)，不再追加全局 gap 上界 \(127\) 或固定
集合 \(\{15,19\}\)。

## 3. 证明边界与可证伪的下一命题

式 (1)--(5) 定义了一个无歧义的有限候选生成器，表中每张证书也都独立验真。但
“四项全中”仍只是冻结有限事实，没有证明

\[
\forall S\ \exists v\in\operatorname{Reach}(S)\
\ \exists X\in\mathcal X_R(v)\ \exists h\mid X:
\operatorname{Term}_p(h).
\tag{8}
\]

式 (8) 的量词必须逐状态使用全部起点的可达域；不能改成每个见证、每个汇 SCC 或一个
统一 \(h\)。此外，(2) 不得在遇到反例后继续追加临时表达式。只要找到一个核心可实现的
\(\Psi_0=1\) F 状态，穷尽其完整 Reach 与五类边界量后仍无终端，便应判定这条具体命题
失败。

即使 (8) 成立，它返回的也是原素数直接证书，不把形式迁移升级为合法递降边。其价值是
把最后的全局小缺口补丁改成状态内、可证伪且由迁移代数固定的候选菜单。

## 4. 复现

```bash
python3 reproductions/type_i_psi_one_affine_boundary_terminal_profile.py
python3 reproductions/type_i_psi_one_affine_boundary_terminal_profile.py --verify
```

结果文件：

```text
reproductions/type-i-psi-one-affine-boundary-terminal-profile-results.json
```

脚本与结果 SHA-256 分别为
`f8d3aabe2da41865f42d4c5809c7a5abf8ccfdd058686a1816d9452790347759`、
`ca986e77a01cf7c8f571c082553f5d18fca143e3b19c70062cda796e4ec3726e`。
