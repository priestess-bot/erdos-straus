# Erdős–Straus 未闭合证明命题包

本目录把尚未闭合的证明缺口拆成可独立交给数学家、形式化验证器或软件审计者处理的命题。
它不把任何外部文件、代码、状态标签或实验结果当作命题前提。

## 阅读规则

每个 SP-*.md 都是一个自包含 dossier。命题文件必须独立给出：

1. 对象、符号和背景定义；
2. 精确量词和假设；
3. 待证明的结论；
4. 可以使用的基础事实；
5. 不能偷用的结论；
6. 允许的三种闭合结果：FAMILY_EMPTY、TERMINAL、VERIFIED_SUCCESSOR；
7. 证明完成时必须提交的证据。

目录中的导航标签只说明命题之间的工作分工，不是证明前提。任何外部文件名、
代码、版本记录、测试、证书或状态，均只可作为动机标签，不能替代命题正文里的定义和证明。

对于本质上是构造问题的 dossier，例如有限 transition family、四步整数 word 或
regeneration map，待构造的映射本身进入该文件的存在量词。证明者必须在同一 dossier
中给出公式、定义域、终端分支、target 公式和验证证据；不得以某个未给出的项目函数
作为隐含前提。

## 全局问题

研究对象是 Erdős–Straus 猜想：

\[
\forall\text{ prime }p\ge2,\quad
\exists x,y,z\in\mathbb N_{>0}:
\frac4p=\frac1x+\frac1y+\frac1z.
\]

本目录中的“递降”命题使用以下完全重新定义的抽象语言。一个状态 \(S\) 包含一个方程接口
\(\mathsf{Eq}(S)\)、一个有限整数编码和一个解集 \(\mathsf{Sol}(S)\)。一条可递归使用的边
\(S\to T\) 必须同时具备：

~~~text
E1  actual source occurrence and lineage
E2  deterministic target projection
E3  common legal persistent typing/admission
E4  universal solution-set lift Sol(T) -> Sol(S)
E5  strict decrease in one fixed well-founded N^7 potential
R   target re-enters the same selector domain
~~~

只证明一个整数恒等式、有限样本、局部 rank 下降、候选 divisor 或布尔字段为真，都不满足这
个定义。

## 命题目录

| ID | 独立命题 | 导航标签（非前提） | 目标闭合 |
|---|---|---|---|
| SP-01 | 结构化 E1--E5 边的抽象良基归纳 | 共享证明合同 | 为活动边提供逻辑基线 |
| SP-02 | 全 constructor/source 信号的穷尽分类（抽象条件模型） | F1 U-A0-01 | 给定良构有限表时 unknown = 0 |
| SP-03 | 唯一准入、无绕过和全 target re-entry | F1 U-A0-02/03/08 | F1 共享基础 |
| SP-04 | q=1 根的 \(M_{23}\) 全除子 terminal schedule | Gate 4 | 六层 registered-prefix schedule（已证明；尚未注册 production authority） |
| SP-05 | q=1 phase-root 首条完整活动边 | Gate 5 / F2 post-G | complete-terminal branch theorem 已证；现实 VERIFIED_SUCCESSOR 仍开放 |
| SP-06 | post-G/C9 连续路径总分派 | F2-POSTG | terminal/empty/successor 分割 |
| SP-07 | C8/H4 actual atomic closure | F2-C8 | atomic leaves 全闭合 |
| SP-08 | high-support \(C=1\) 的 \(R=3\)-G 分支 | F2-HIGH-SUPPORT-C1 | 无 upward ABSORB |
| SP-09 | high-support \(C>1\) empty-improvement 二分 | F2-HIGH-SUPPORT-CGT1 | terminal/empty/lower protocol |
| SP-10 | high-support noncanonical incoming grammar | F2-HIGH-SUPPORT-NONCANONICAL | source-bound normalizer |
| SP-11 | F3 high strict-carry | F3-HIGH-STRICT-CARRY | high successor 或 terminal |
| SP-12 | F3 high \(k=1\) Pell residual | F3-HIGH-STUTTER-K1 | nonrecurrence 或闭合出口 |
| SP-13 | F3 high odd \(k\ge3\) residual | F3-HIGH-STUTTER-ODD-KGE3 | high-only closure |
| SP-14 | QC1 \(q_\perp\) integer occurrence and deflation | F3-QC1 | occurrence/terminal dichotomy |
| SP-15 | TR1 \(D^\ast\) fresh occurrence | F3-TR1 | least fresh factor and final rank |
| SP-16 | \(m=3,q=5\) R1 source-path binding | F3-M3Q5-R1 | active source receipt |
| SP-17 | \(m=3,q=5\) nonminimal \(q=5\) | F3-M3Q5-NONMINIMAL | \(5\mid E\) / \(5\nmid E\) closure |
| SP-18 | \(m=3,q=5\) regeneration p-free failure | F3-M3Q5-REGENERATION | terminal or paid macro |
| SP-19 | \(p^2\) one-sided factor-pair leaf | F3-M3Q5-P2-ONE-SIDED | terminal/contradiction/successor |
| SP-20 | \(p^2\) genuine two-sided leaf | F3-M3Q5-P2-TWO-SIDED | strict source-forward final macro |
| SP-21 | scope-bound terminal-first 准入健全性 | 共享 P0 | abstract safety theorem 已证；submitted prototype 已复现，但 current-runtime instance 仍开放 |
| SP-22 | actual q=1,G scoped phase-root pilot | P1 q=1 | submitted pilot 已复现；第一条 current-selector actual E1--E5/R edge 仍开放 |

## 证明者交付格式

证明者只需阅读该命题文件。对任一命题，最终交付应包含：

~~~text
statement.md       完整证明或明确反证
definitions.md     若正文有扩展定义，必须再次自包含
verification.md    符号/整数/形式化核验说明
counterexamples.md 所有边界控制和失败尝试
~~~

本目录的 SP-*.md 已将这四部分压缩在一个自包含文件中；若证明过程中产生长篇材料，可在同一
命题目录下追加文件，但不得把另一个 SP-*.md 当作未声明的前提。

SP-02 的独立运行记录见 SP-02-VERIFICATION.md；该记录验证抽象有限模型和负控，不替代
具体仓库的 constructor/source 完备性证明。SP-04 的解包证据和独立重放记录位于
reproductions/sp04_q1_m23/，并通过 tests/test_t6_sp04_q1_m23_package.py 验证。
SP-05 的 complete-terminal decision 包位于 reproductions/sp05_complete_terminal_decision/；
它严格保持 SP-05 的 actual nonterminal-edge 命题为开放，因为 complete MISS 正是
Erdős--Straus 反例条件，而包本身不签发 actualness、admission 或 queue authority。
SP-21 的 abstract safety theorem 已在 SP-21-ABSTRACT-SAFETY-PROOF-2026-08-29.md 中
成立；其 concrete coordinator policy、authority、actual source 与 executable replayer
仍未交付，因此 SP-21 dossier 本身继续开放。
2026-08-29 submitted concrete closure v1 的 package/archive/review 已归档；它在声明的历史
基线可重放，但只形成 isolated pilot，因为内嵌签名 key 没有外部 provenance，base commit
也没有在运行时与 current checkout 比对。它不改变 SP-21、SP-22 或 20 个开放 dossier 的状态。
当前所有 dossier 的已解决部分、P0/P1/P2 分层和推荐执行链见
CURRENT-PROOF-PORTFOLIO-2026-08-29.md。

## 状态纪律

截至本次整理，20 个命题仍是 OPEN_PROPOSITION；SP-02 已补入条件有限模型的完整证明，
SP-04 已补入六层 registered-prefix schedule 的完整证明、两套独立实现和控制，二者状态均
为 ESTABLISHED。这里的 ESTABLISHED 只表示各自精确作用域内的命题成立，不表示当前仓库
的 concrete constructor/source、production terminal authority 或 F1/F2/F3/T6 已闭合。
SP-05 已有完整 terminal-decision 与条件 phase-root branch 的边界证明，但这不提供一条
实际 complete-miss source，因此仍属于上述 20 个 OPEN_PROPOSITION。SP-21、SP-22 是该边界
之后新增的 P0/P1 问题；SP-21 的抽象 safety theorem 已证，但 concrete instance 仍未证明，
SP-22 仍未证明。已归档的 scoped prototype 不能替代这些义务。
