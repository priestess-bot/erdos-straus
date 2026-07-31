---
kind: claim
claim_id: type-I-formal-ranked-pruning-and-external-gap-selector
title: 形式目标对的双秩剪枝、一步终端前瞻与外部缺口选择器
statement: 对互素正整数形式对 A+B=Rm，任一满足 v_q(AB)>v_q(K) 的素数 q 都定义唯一的约分形式迁移；m>1 时该迁移严格降低 m，m=1 时可分别只保留严格降低 min(A,B) 或 max(A,B) 的边，从而得到两个良基有向无环图。被任一秩拒绝的一步后继可以用于直接 Type I/II 终端核验，但不能作为递归边。对冻结的 55 个 Psi_0=1 F 状态，两个秩加一步外部缺口前瞻分别闭合 53 和 52 个状态，并集闭合 54 个；唯一余项 (p,R)=(16002529,27) 由候选外部因子 Q=11 或 47 作为新模数后的中心谱 Type I 命中闭合，故该冻结分支 55/55 均得到独立验真的直接证书。形式迁移尚无合法后继状态与解提升，所以这个有限闭合不是全称递降定理。
claim_status: computationally_reproduced
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-I-f-psi-one-nearest-fiber-escape-boundary
  - type-I-f-qadic-numerator-lift-rigidity-and-gcd-reduction
  - type-I-general-b-centered-square-spectrum
  - type-I-coprime-factor-normal-form
  - type-II-coprime-factor-normal-form
  - type-I-formal-target-pair-descent-cycle-boundary
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - F-state
  - formal-target-pair
  - q-adic
  - well-founded-pruning
  - terminal-first
  - external-gap
  - cross-chart
  - finite-selector
  - proof-boundary
sources:
  - claim: type-I-f-psi-one-nearest-fiber-escape-boundary
    role: frozen-Psi-one-input
  - claim: type-I-f-qadic-numerator-lift-rigidity-and-gcd-reduction
    role: formal-transition-input
  - claim: type-I-general-b-centered-square-spectrum
    role: centered-cross-chart-terminal
  - claim: denominator-escape-state-contract
    role: legal-edge-acceptance-boundary
visibility: public
last_checked: '2026-07-31'
---

# 形式目标对的双秩剪枝、一步终端前瞻与外部缺口选择器

## 1. 任意超高素数的形式迁移

固定

\[
4K=pR+1,
\qquad
A+B=Rm,
\qquad
(A,B)=1,
\tag{1}
\]

并设素数 \(q\) 满足

\[
v_q(AB)>v_q(K).
\tag{2}
\]

交换 \(A,B\) 后可设 \(q\mid A\)。由互素性得 \(q\nmid B\)。若 \(q\mid R\)
或 \(q\mid m\)，把 (1) 模 \(q\) 化简都会推出 \(q\mid B\)，故

\[
q\nmid BRm.
\tag{3}
\]

于是存在唯一的 \(1\le t<q\) 满足

\[
t\equiv-m\pmod q.
\tag{4}
\]

定义

\[
A_0=\frac Aq,
\qquad
B_0=\frac{B+Rt}{q},
\qquad
m_0=\frac{m+t}{q}.
\tag{5}

它们是正整数且 \(A_0+B_0=Rm_0\)。令 \(g=(A_0,B_0)\)。由原始互素性和
\(q\nmid R\) 可得 \((g,R)=1\)，再由 \(g\mid Rm_0\) 得 \(g\mid m_0\)。所以

\[
T_q(A,B,m)=
\left(\frac{A_0}{g},\frac{B_0}{g},\frac{m_0}{g}\right)
\tag{6}
\]

仍是正互素形式对。这里不要求 \(q\mid K\)：新支撑素数和旧支撑的超额层都属于
同一个公式。

若 \(m>1\)，则

\[
m'\le\frac{m+t}{q}\le\left\lceil\frac mq\right\rceil<m.
\tag{7}
\]

若 \(m=1\)，则 \(t=q-1\)、\(g=1\)，且无序形式为

\[
\{A,R-A\}\longmapsto\{A/q,R-A/q\}.
\tag{8}
\]

式 (1)--(8) 是一般整数恒等式；它尚未给出另一个带目标方程和解提升的合法 F/G 状态。

## 2. 两个良基剪枝与安全的一步前瞻

在无序形式对上定义两个字典秩

\[
\rho_{\min}(A,B,m)=(m,\min(A,B)),
\qquad
\rho_{\max}(A,B,m)=(m,\max(A,B)).
\tag{9}
\]

它们都取值于字典序良基集 \(\mathbb N_{>0}^2\)。对每一个秩分别保留所有严格下降的
(6) 边。由 (7)，\(m>1\) 的全部形式边都被保留；在 \(m=1\) 层只保留使相应第二
坐标下降的边。因此每个剪枝图都是有限起点上的有向无环图。

这两个图不需要合并成一个共同势。选择器可以独立运行两次并接受任一直接终端。
对于从已访问节点出发但不降低当前秩的边，只允许构造其一步后继并执行终端核验：

\[
S\longrightarrow T,\quad \rho(T)\not<\rho(S),\quad
\operatorname{Term}(T)=\text{hit}
\quad\Longrightarrow\quad
\text{返回独立验真的根素数证书}.
\tag{10}
\]

式 (10) 没有把 \(S\to T\) 登记为递归边；若 \(T\) 不直接命中，就必须停止该分支。
此外，任何形式对搜索之前都应先对整个 \((p,R,K)\) 执行状态级中心谱扫描，而不是
只检查当前 \((A,B)\)。

## 3. 外部因子的精确缺口终端

从终端检查范围中的任一坐标 \(X\) 取

\[
Q\mid X,
\qquad
Q\equiv3\pmod4,
\qquad
\frac{Q}{(Q,K)}>1,
\qquad
3\le Q\le p-2.
\tag{11}
\]

条件 \(Q/(Q,K)>1\) 只负责从外部分母产生有限候选；证书本身由下面的标准完整判据
独立验真。令

\[
x=\frac{p+Q}{4}.
\tag{12}
\]

完整枚举 \(d\mid x^2\)：

\[
\begin{array}{ll}
\text{Type I:}&Q\mid px+d,\\
\text{Type II:}&d\le x\text{ 且 }Q\mid x+d.
\end{array}
\tag{13}

Type I 命中时可取

\[
y=\frac{px+d}{Q},
\qquad
z=\frac{pxy}{d};
\tag{14}
\]

Type II 命中时可取

\[
y=\frac{p(x+d)}{Q},
\qquad
z=\frac{xy}{d}.
\tag{15}
\]

直接通分给出

\[
\frac4p=\frac1x+\frac1y+\frac1z.
\tag{16}
\]

所以 (13) 的命中不依赖形式边是否合法；形式闭包只承担候选生成作用。

与 (11) 的外部候选互补，若候选缺口本身满足 \(M\mid K\)，则
\(pR\equiv-1\pmod M\) 可把 (13) 精确拉回为

\[
4dR^2\equiv-1\pmod M
\quad\text{或}\quad
4dR\equiv1\pmod M.
\]

这对复合 \(M\) 也成立，但仍必须保留 \(M\equiv3\pmod4\)、\(M\le p-2\) 与
\(d\mid x_M^2\)。冻结 55 态的完整内部菜单只闭合 37 态，因此它是
`terminal-first` 的另一条直接叶，不替代本卡的外部前瞻。见
[K 内部缺口的 R 坐标残数拉回](internal-support-gap-residue-pullback.md)。

## 4. 把同一个 Q 切换为中心谱模数

若 (11)--(13) 未命中，还可以把 \(Q\) 当作新模数并令

\[
K_Q=\frac{pQ+1}{4}.
\tag{17}
\]

完整检查

\[
D\mid K_Q^2,
\qquad
D<K_Q,
\qquad
D\equiv-K_Q\pmod Q.
\tag{18}

对自然缺口 \(h=(4D+1)/Q\)，式 (18) 是同一素数 \(p\) 的一般 \(B\) Type I
中心谱命中。其显式正规化为

\[
G=(D,K_Q),\quad B=D/G,\quad C=G/B,\quad H=K_Q/G,
\quad A=(B+H)/Q.
\tag{19}

于是 \(D=B^2C\)、\(K_Q=BCH\)。在 (13) 中以真实缺口 \(h\) 替换原缺口变量
\(Q\) 后，对应的直接 Type I 除子为 \(A^2C\)。
这一步返回原素数的直接证书，不需要跨状态解提升。

## 5. 冻结 \(\Psi_0=1\) 家族的完整结果

输入是已哈希锁定的 55 个 F 状态、140 个正向最短见证。先只允许 \(q\mid K\) 的
形式边，得到基线：

\[
282\text{ 个节点},\qquad153\text{ 条边},\qquad129\text{ 个汇点},
\tag{20}
\]

全部边严格降低 \(m\)，最长轨道为 5。再允许 (2) 中的所有超高素数，结果为：

| 模式 | 递归节点 | 保留边 | 被拒绝边 | 一步新后继 | 终端范围 | 命中状态 |
|---|---:|---:|---:|---:|---:|---:|
| \(\rho_{\min}\) | 4924 | 12421 | 1172 | 798 | 5722 | 53/55 |
| \(\rho_{\max}\) | 5086 | 10571 | 3651 | 849 | 5935 | 52/55 |

两个模式的命中并集为 54/55，唯一余项是

\[
(p,R)=(16{,}002{,}529,27).
\tag{21}

它在两个终端范围中产生的全部不同候选为

\[
Q\in\{7,11,23,47,67,103,251,1423,1607,2819,22471\}.
\tag{22}

把 (22) 逐个送入 (17)--(18)，恰有两个模数命中。按中心除子递增取规范首证书：

\[
Q=11,\quad K_Q=44{,}006{,}955,\quad D=657,
\tag{23}

\[
Q=47,\quad K_Q=188{,}029{,}716,\quad D=5299.
\tag{24}

对 (23)，式 (19) 给出

\[
(A,B,C,H)=(18268,3,73,200945),
\quad h=239,
\quad x=4{,}000{,}692,
\tag{25}
\]

直接 Type I 除子为

\[
A^2C=24{,}361{,}547{,}152,
\tag{26}

并得到逐项验真的解

\[
(x,y,z)=
(4{,}000{,}692, 267{,}973{,}017{,}980, 704{,}222{,}573{,}589{,}195).
\tag{27}

因此这批冻结状态的有限选择器覆盖率为

\[
\boxed{55/55}.
\tag{28}

复现入口为
`reproductions/type_i_f_psi_one_formal_transition_closure.py`，结果文件为
`reproductions/type-i-f-psi-one-formal-transition-closure-results.json`。脚本对每张返回
证书直接核对 (16)，并对冻结输入、基线规模、覆盖率、唯一余项和两个规范跨图表命中
设置断言。

## 6. 证明边界与下一条全称引理

这里必须分开三种结论：

1. 式 (1)--(16) 及两个秩的良基性是一般整数定理；
2. 式 (20)--(28) 是冻结 55 态的完整有限证据；
3. “每个核心素数都能沿该菜单命中”仍未证明。

特别地，形式边缺少合法状态合同中的目标方程、标记解、反向提升和边级验收回执，仍只
能登记为 `analysis_evidence`。有限 55/55 的真正推进是：它把外部分母从单纯障碍变成了
一个经证书验证的候选生成器，并把全称缺口压缩为下面的析取：

\[
\boxed{
\begin{array}{l}
\text{对任意 terminal-first 后仍未闭合的 }\Psi_0=1\text{ 状态，两个良基剪枝}\

\text{或其源可达一层 SCC 产生周期表示格盒交、}K\text{ 支撑乘子桥、外部}\

\text{缺口 Type I/II、中心谱跨图表命中，或产生满足}\

\text{完整 E1--E5 与解提升合同的合法 support switch。}
\end{array}}
\tag{29}

完整超高图的汇点现已证明等价于同状态 Type I，但纯外部周期在
\(R\equiv3\pmod8\) 时普遍存在，不能单独算作出口。因此证明 (29) 仍需要周期外的
terminal-first 与源可达信息；证明该析取才能把本卡升级为全称短证书或递降引理。
