# SP-21：scope-bound terminal-first 准入的健全性

**状态：** OPEN_PROPOSITION
**优先级：** P0，共享合同阻塞。
**研究任务：** 证明一个可递归 selector 只需完整重放其固定优先级中位于 selected
producer 之前的 terminal/producer actions；它不需要证明所有可能的三分母 terminal
公式都不存在。
**独立性：** 本文件完整定义状态、动作策略、scope MISS、terminal、verified successor
和证明目标；不以仓库的现有 schema、代码或 SP 文件作为逻辑前提。

## 1. 对象与策略

令 \(\mathscr S\) 是有限编码状态的集合。每个 \(S\in\mathscr S\) 带有一个方程接口
\(\mathsf{Eq}(S)\) 和解集 \(\mathsf{Sol}(S)\)。固定一个 selector policy

\[
\mathcal P=(A_0,A_1,\ldots,A_N),
\]

其中每个 \(A_i\) 都是一个有版本、规范编码、可独立重放的动作，且类型恰为以下之一：

1. terminal action：返回 HIT certificate 或 MISS；
2. producer action：返回 guard true 并给出一个候选 target，或 guard false；
3. reject action：返回一个不入队的稳定拒绝。

策略是有限有序表。其规范编码必须包含动作顺序、每个动作的谓词、实现/证明标识、
适用 owner/domain、以及 subject binding 规则。动作本身不得修改策略。

对一个固定 state \(S\)，令

\[
\operatorname{Replay}(A_i,S)
\]

表示从 \(S\) 的规范编码重新计算的唯一输出。若 terminal action 返回 HIT certificate
\(c\)，必须有

\[
c\in\mathsf{Sol}(S).
\]

若 producer action 被选择并返回 target \(T\)，则它必须另行通过 E1、E2、E3、E4、E5
和 R；本文件不把 policy replay 当作这些义务的替代。

## 2. policy-relative clearance

设 \(A_j\) 是一个 producer action。定义其前缀 clearance：

\[
\operatorname{PriorClear}_{\mathcal P,j}(S)
\]

当且仅当：

1. 对每个 \(i<j\) 的 terminal action，\(\operatorname{Replay}(A_i,S)\) 返回 MISS；
2. 对每个 \(i<j\) 的 producer action，\(\operatorname{Replay}(A_i,S)\) 返回 guard false；
3. 每个 replay record 与同一个 \(S\)、同一个 policy digest 和同一个动作索引绑定；
4. 任一 earlier terminal HIT 都立即终止，不再计算 \(A_j\)。

clearance receipt 的唯一合法语义是

\[
\mathsf{MISS\_HIGHER\_PRIORITY\_POLICY\_COMPLETE},
\]

并附带

\[
\mathsf{coverage}=
\mathsf{REGISTERED\_HIGHER\_PRIORITY\_ONLY},
\qquad
\mathsf{global\_exhaustion}=\mathrm{false}.
\]

它不等价于 \(\mathsf{Sol}(S)=\varnothing\)，也不等价于所有未注册 terminal
family 都 MISS。

## 3. 待证明命题

设 policy \(\mathcal P\) 满足：

1. 所有早于 \(A_j\) 的动作都可终止地、确定地重放；
2. 每个 earlier terminal HIT 都有可靠 certificate；
3. \(A_j\) 的 guard、source occurrence、target projection、typing、lift、T5 ticket
   和 re-entry 已由独立 verifier 建立；
4. \(A_j\) 的 target \(T\) 满足

\[
\forall u\in\mathsf{Sol}(T),\qquad
\Lambda(u)\in\mathsf{Sol}(S).
\]

则对每个 actual source \(S\)，选择器的前缀行为是互斥且可靠的：

\[
\boxed{
\begin{aligned}
&\exists i<j:\operatorname{Replay}(A_i,S)=\mathsf{HIT}(c)
&&\Longrightarrow \mathsf{Terminal}(S,c),\\
&\operatorname{PriorClear}_{\mathcal P,j}(S)
\land \operatorname{Guard}_{A_j}(S)
&&\Longrightarrow \mathsf{VerifiedSuccessor}(S,T).
\end{aligned}}
\]

特别地，第二行不需要假设

\[
\mathsf{Sol}(S)=\varnothing
\]

或所有 terminal formulas 均已枚举。未被当前 policy 注册的 terminal 解，即使存在，
也不会破坏 successor 的 E4 lift 或 selector 的正确性。

## 4. 必须补出的 Goal-compatible 部分

仅有上述抽象定理还不足以接入 T6。对于一个具体 producer，必须额外证明：

1. 所有能与该 producer guard 重叠、且 coordinator 声明为 prior 的 terminal actions，
   均位于 \(A_j\) 之前；
2. 任一未位于 \(A_j\) 前的 registered terminal action，要么 guard 与 \(A_j\) 不交，
   要么属于之后的明确策略位置；
3. policy digest、动作实现、owner scope、branch index 和 replay verifier 都由
   外部于 producer 的 authority 固定；
4. selected producer 的 target 仍走同一 common admission/re-entry path；
5. scope MISS 永远不得序列化为 MISS_COMPLETE。

这不是降低 terminal-first 要求。它把 terminal-first 的正确对象从“不可能穷尽的
terminal universe”改为“冻结 selector policy 中的全部 prior actions”。

## 5. q=1 必须保留的负控

令

\[
p=21169,\qquad X=(p+3)/4=5293=67\cdot79.
\]

该点是 ordinary \(q=1,G\)。对

\[
M_{23}=\{3,7,11,15,19,23\}
\]

的完整 Bradford divisor priority screen 可以得到 scope MISS；但 gap \(31\)、\(d=1\)
给出

\[
\frac4{21169}
=\frac1{5300}
+\frac1{3619899}
+\frac1{19185464700}.
\]

因此以下两种错误都必须拒绝：

1. 将 M23 scope MISS 改名为 MISS_COMPLETE；
2. 仅因 gap 31 在当前 policy 外，就声称该 certificate 不存在。

相反，若一个冻结 policy 确实把 phase-root producer 放在 M23 后、gap 31 前，则
scope-bound clearance 可以允许该 producer；其 successor 正确性来自独立 E1--E5，
不是来自“没有解”的断言。

## 6. 完成证据

本命题从 OPEN_PROPOSITION 改为 ESTABLISHED 前，需要：

* policy 的完整有限规范和动作顺序；
* prefix replay 的终止性、确定性和 subject/policy binding 证明；
* terminal HIT 的可靠性证明；
* scope-clearance 与 selected producer 的互斥/前序证明；
* scope-bound successor soundness 的形式证明；
* policy mutation、动作重排、later-terminal 伪 global miss、source swap、
  guard overlap 和 queue bypass 的负控；
* 一个 independent replayer，不导入 selected producer 的边验证结论。

本命题不证明某个具体 producer guard 非空，不证明 common admission，不证明任何 F2/F3
family totality，也不改变 T6 或 Erdős--Straus 猜想的状态。
