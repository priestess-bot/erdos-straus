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

---

# SP-21 完整证明

## 0. 结论与两处必要修正

SP-21 的核心结论是正确的：

> 递归 selector 的安全性只要求完整重放冻结 policy 中位于 selected producer 之前的动作，并独立验证 producer edge；它不要求穷尽所有可能的 terminal 公式，也不要求证明 (\mathsf{Sol}(S)=\varnothing)。

不过，原命题若把 (\mathsf{Terminal}(S,c)) 和 (\mathsf{VerifiedSuccessor}(S,T)) 理解为**实际 selector 输出**，还缺两个形式条件。

第一，earlier reject 没有被 (\operatorname{PriorClear}) 覆盖。取

[
\mathcal P=(R,A_j),
]

其中 (R) 是 reject action，且 (A_j) guard true。按原定义，前面没有 terminal 或 producer，所以 (\operatorname{PriorClear}_{\mathcal P,j}(S)) 真；但 selector 在 (R) 处已经拒绝，不可能选择 (A_j)。

第二，任意 earlier terminal HIT 不一定是实际输出。取

[
\mathcal P=(B,C,A_j),
]

其中 (B) 是 guard true 的 producer，(C) 是返回 (\mathsf{HIT}(c)) 的 terminal。虽然

[
\operatorname{Replay}(C,S)=\mathsf{HIT}(c),
]

selector 实际会先选择 (B)。因此：

* 若 (\mathsf{Terminal}(S,c)) 仅表示“(c) 是可靠 terminal certificate”，原第一行成立；
* 若它表示“selector 实际返回 (c)”，必须增加“此前所有动作均继续”的最小索引条件。

以下给出闭合后的精确定理。它保持原命题的 scope-bound 主张不变。

---

## 1. 冻结 policy、绑定和 selector 语义

对每个动作 (A_i)，记其类型为

[
K_i\in{\mathsf{terminal},\mathsf{producer},\mathsf{reject}}.
]

记

[
r_i(S)=\operatorname{Replay}(A_i,S).
]

动作输出类型为

[
r_i(S)\in
\begin{cases}
{\mathsf{MISS}}\cup{\mathsf{HIT}(c)},&
K_i=\mathsf{terminal},[2mm]
{\mathsf{FALSE}}\cup{\mathsf{TRUE}(T)},&
K_i=\mathsf{producer},[2mm]
{\mathsf{REJECT}(\rho)},&
K_i=\mathsf{reject}.
\end{cases}
]

其中 (\mathsf{TRUE}(T)) 同时表示 guard true 和规范候选 target (T)。

### 1.1 继续谓词

定义动作 (i) 对状态 (S) 的“继续”谓词

[
\operatorname{Pass}_i(S)
]

为

[
\operatorname{Pass}_i(S)
\iff
\begin{cases}
r_i(S)=\mathsf{MISS},&K_i=\mathsf{terminal},\
r_i(S)=\mathsf{FALSE},&K_i=\mathsf{producer},\
\bot,&K_i=\mathsf{reject}.
\end{cases}
]

因此，在题目给定的 reject 类型下，reject 永远是决定性动作，不存在“reject action 被调用但继续”的情况。

定义到达 (A_j) 的前缀条件

[
\operatorname{Reach}_{\mathcal P,j}(S)
\iff
\forall i<j,\quad \operatorname{Pass}_i(S).
]

再定义静态条件

[
\operatorname{NoRejectBefore}_{\mathcal P,j}
\iff
\forall i<j,\quad K_i\neq\mathsf{reject}.
]

在 replay record 完整且绑定有效时，有

[
\boxed{
\operatorname{Reach}*{\mathcal P,j}(S)
\iff
\operatorname{PriorClear}*{\mathcal P,j}(S)
\land
\operatorname{NoRejectBefore}_{\mathcal P,j}.}
\tag{1}
]

特别地，如果 (A_j) 已经被 selector 实际选择，那么
(\operatorname{NoRejectBefore}_{\mathcal P,j}) 自动成立；否则任何 earlier reject 都会使 (j) 不可达。

如果预期 reject action 也可以“不适用并继续”，其输出类型必须显式改成

[
\mathsf{REJECT}(\rho)\ \mid\ \mathsf{PASS},
]

并将该 (\mathsf{PASS}) 纳入 clearance。当前三种动作定义并不具有这一语义。

### 1.2 receipt 的完整覆盖

仅要求“每一条现存 record 都正确绑定”还不够；空 record 集也会真空满足该条件。合法 clearance receipt 必须满足

[
I_j^{tp}
========

{,i<j:K_i\in{\mathsf{terminal},\mathsf{producer}},},
]

并且：

[
{\operatorname{index}(R):R\in\operatorname{records}(\rho)}
==========================================================

I_j^{tp},
]

每个索引恰好出现一次，按递增索引编码。每条 record 必须绑定：

[
\bigl(
\operatorname{subjectID}(S),
\operatorname{policyID}(\mathcal P),
i,
\operatorname{actionID}(A_i),
r_i(S)
\bigr).
]

在纯数学证明中，可直接以规范编码作为
(\operatorname{subjectID}) 和 (\operatorname{policyID})，从而保持单射。实现若使用固定长度 hash，则还需要 hash 碰撞安全假设；单有 hash 字符串并不是无条件的数学单射证明。

---

## 2. 前缀分割引理

对前 (k) 个动作定义顺序执行 (\operatorname{Run}_k(S))。初始为

[
\operatorname{Run}_0(S)=\mathsf{CONTINUE}(0).
]

若已经停止，则保持该结果；若当前为 (\mathsf{CONTINUE}(i))，则检查 (r_i(S))：

[
\begin{array}{c|c}
r_i(S)&\text{下一结果}\ \hline
\mathsf{MISS}&\mathsf{CONTINUE}(i+1)\
\mathsf{HIT}(c)&\mathsf{TERMINAL}(i,c)\
\mathsf{FALSE}&\mathsf{CONTINUE}(i+1)\
\mathsf{TRUE}(T)&\mathsf{PRODUCER}(i,T)\
\mathsf{REJECT}(\rho)&\mathsf{REJECTED}(i,\rho).
\end{array}
]

### 引理 2.1：前缀唯一分割

对每个 (k)，(\operatorname{Run}_k(S)) 恰为以下四种情况之一：

[
\begin{aligned}
&\mathsf{CONTINUE}(k),
&&\text{且 }\forall i<k,\operatorname{Pass}_i(S);\
&\mathsf{TERMINAL}(i,c),
&&i<k,\ \forall h<i,\operatorname{Pass}_h(S),
r_i(S)=\mathsf{HIT}(c);\
&\mathsf{PRODUCER}(i,T),
&&i<k,\ \forall h<i,\operatorname{Pass}_h(S),
r_i(S)=\mathsf{TRUE}(T);\
&\mathsf{REJECTED}(i,\rho),
&&i<k,\ \forall h<i,\operatorname{Pass}_h(S),
r_i(S)=\mathsf{REJECT}(\rho).
\end{aligned}
]

而且结果唯一。

#### 证明

对 (k) 归纳。

当 (k=0) 时，只有 (\mathsf{CONTINUE}(0))。

假设结论对 (k) 成立。若 (\operatorname{Run}_k(S)) 已经是三种停止结果之一，则增加一个未执行动作不会改变最早决定结果。若为 (\mathsf{CONTINUE}(k))，则检查唯一确定的 (r_k(S))。由于动作输出构造互不相交，且 replay 确定，只能唯一落入表中的五种转移之一。于是得到 (k+1) 的结论。

策略前缀有限，每个 replay 终止，所以归纳过程终止。证毕。

### 推论 2.2：选择 producer 的精确条件

若 (A_j) 是 producer，且

[
r_j(S)=\mathsf{TRUE}(T),
]

则

[
\boxed{
\operatorname{Sel}*{\mathcal P}(S)=j
\iff
\operatorname{Reach}*{\mathcal P,j}(S).}
\tag{2}
]

结合式 (1)：

[
\boxed{
\operatorname{Sel}*{\mathcal P}(S)=j
\iff
\operatorname{PriorClear}*{\mathcal P,j}(S)
\land
\operatorname{NoRejectBefore}_{\mathcal P,j}
\land
r_j(S)=\mathsf{TRUE}(T).}
\tag{3}
]

这就是 scope-bound prefix replay 的完整 operational characterization。

---

## 3. terminal 与 successor 的健全性定理

为消除“terminal certificate”和“实际 terminal 输出”的歧义，定义

[
\mathsf{TerminalCert}(S,c)
\iff c\in\mathsf{Sol}(S),
]

以及

[
\mathsf{SelectorTerminal}*{\mathcal P}(S,c)
\iff
\exists i;
\bigl(
\operatorname{Sel}*{\mathcal P}(S)=i
\land r_i(S)=\mathsf{HIT}(c)
\bigr).
]

把 selected producer 的所有独立边义务记为

[
\begin{aligned}
\mathsf{EdgeOK}_j(S,T,\Lambda)
:={}&
\mathsf{E1}\land\mathsf{E2}\land\mathsf{E3}
\land\mathsf{E4}\land\mathsf{E5}\land\mathsf R\
&{}\land\mathsf{SourceOccurrence}
\land\mathsf{TargetProjection}
\land\mathsf{Typing}\
&{}\land\mathsf{T5Ticket}
\land\mathsf{Reentry}.
\end{aligned}
]

另外定义语义 lift：

[
\mathsf{LiftOK}(S,T,\Lambda)
\iff
\forall u\in\mathsf{Sol}(T),\quad
\Lambda(u)\in\mathsf{Sol}(S).
]

安全 successor 定义为

[
\begin{aligned}
\mathsf{VerifiedSuccessor}^{\mathrm{safe}}*{\mathcal P,j}(S,T)
\iff{}&
\operatorname{Sel}*{\mathcal P}(S)=j\
&{}\land r_j(S)=\mathsf{TRUE}(T)\
&{}\land\mathsf{EdgeOK}_j(S,T,\Lambda)\
&{}\land\mathsf{LiftOK}(S,T,\Lambda).
\end{aligned}
]

### 定理 3.1：scope-bound terminal-first 健全性

对任意 actual source (S)：

#### （一）任意 replay HIT 的 certificate 都可靠

[
\boxed{
\exists i<j:\ r_i(S)=\mathsf{HIT}(c)
\quad\Longrightarrow\quad
\mathsf{TerminalCert}(S,c).}
\tag{4}
]

#### （二）被到达的 terminal HIT 是实际 terminal 输出

[
\boxed{
\operatorname{Reach}*{\mathcal P,i}(S)
\land
r_i(S)=\mathsf{HIT}(c)
\quad\Longrightarrow\quad
\mathsf{SelectorTerminal}*{\mathcal P}(S,c).}
\tag{5}
]

#### （三）前缀 clearance 加独立 edge verification 推出安全 successor

[
\boxed{
\begin{aligned}
&
\operatorname{PriorClear}*{\mathcal P,j}(S)
\land
\operatorname{NoRejectBefore}*{\mathcal P,j}\
&\quad{}\land
r_j(S)=\mathsf{TRUE}(T)
\land
\mathsf{EdgeOK}*j(S,T,\Lambda)
\land
\mathsf{LiftOK}(S,T,\Lambda)\
&\qquad\Longrightarrow
\mathsf{VerifiedSuccessor}^{\mathrm{safe}}*{\mathcal P,j}(S,T).
\end{aligned}}
\tag{6}
]

#### （四）earlier terminal HIT 与 producer clearance 互斥

[
\boxed{
\left(
\exists i<j:\ r_i(S)=\mathsf{HIT}(c)
\right)
\land
\operatorname{PriorClear}_{\mathcal P,j}(S)
\Longrightarrow\bot.}
\tag{7}
]

#### 证明

式 (4) 直接来自 terminal HIT 可靠性假设：

[
r_i(S)=\mathsf{HIT}(c)
\Longrightarrow c\in\mathsf{Sol}(S).
]

对式 (5)，前缀分割引理说明 selector 到达 (i)，随后 (A_i) 返回 HIT，因此实际停止在 (i)；certificate 可靠性给出 (c\in\mathsf{Sol}(S))。

对式 (6)，由式 (1) 得

[
\operatorname{Reach}_{\mathcal P,j}(S).
]

再由 (r_j(S)=\mathsf{TRUE}(T)) 和式 (2)，selector 的最小决定索引为 (j)。其余合取项正是独立 edge verifier 和语义 lift，因此得到
(\mathsf{VerifiedSuccessor}^{\mathrm{safe}})。

对式 (7)，若某个 (i<j) 返回 HIT，则
(\operatorname{PriorClear}) 的第一项要求同一

[
(S,\operatorname{policyID},i,A_i)
]

的 replay 返回 MISS。确定性和 record 绑定排除了同一 replay 同时返回 HIT 和 MISS。证毕。

### 原命题框的准确解释

因此，原框在以下解释下成立：

[
\mathsf{Terminal}(S,c):=\mathsf{TerminalCert}(S,c).
]

若希望 (\mathsf{Terminal}) 表示 actual selector result，则第一行必须改成式 (5)，即增加前缀可达性，或规定 (i) 是最小决定索引。

第二行若希望表示 actual selected successor，则必须增加

[
\operatorname{NoRejectBefore}_{\mathcal P,j},
]

或直接把“selector 已到达 (A_j)”放入前提。

---

## 4. 为什么完全不需要 global exhaustion

定理 3.1 的证明只使用了：

[
{r_i(S):i<j},
\qquad
r_j(S),
\qquad
\mathsf{EdgeOK},
\qquad
\mathsf{LiftOK}.
]

证明中没有出现

[
\mathsf{Sol}(S)=\varnothing
]

或

[
\forall F\in\text{所有可能 terminal families},\quad F(S)=\mathsf{MISS}.
]

### 4.1 一个直接反模型

取 (j=0)，policy 的第一个动作就是 producer (A_0)，并取一个满足

[
\mathsf{Sol}(S)\neq\varnothing
]

的状态。此时

[
\operatorname{PriorClear}_{\mathcal P,0}(S)
]

真空成立。因此不存在一般推理规则

[
\operatorname{PriorClear}_{\mathcal P,j}(S)
\Longrightarrow
\mathsf{Sol}(S)=\varnothing.
]

### 4.2 未注册 terminal 的非干扰性

设 (F) 是未出现在 policy 前缀中的 terminal family，且它事实上能发现

[
c_0\in\mathsf{Sol}(S).
]

这不会改变任何 (r_i(S))、policy order、producer target 或 lift 映射。因此式 (6) 的所有前提和结论保持不变。

存在 (c_0) 只能说明：

[
\mathsf{Sol}(S)\neq\varnothing;
]

它不能否定

[
\forall u\in\mathsf{Sol}(T),\quad
\Lambda(u)\in\mathsf{Sol}(S).
]

换言之，source 还存在其他解并不会使 lift 失效。

若后来把 (F) 注册到一个新 policy 中，则完整 policy 编码改变，policy digest 也必须改变。旧 receipt 不能在新 policy 下复用；新 policy 必须重新进行 prefix replay。如果 (F) 被放在 (j) 之前，它必须被 replay；若被放在 (j) 之后，则它在新 policy 中是明确的 later action。

### 4.3 这里只证明 safety，不证明 solver completeness

式

[
\forall u\in\mathsf{Sol}(T),\quad
\Lambda(u)\in\mathsf{Sol}(S)
]

证明的是：

> 只要递归 target 给出解，就能可靠恢复 source 的解。

它不证明

[
\mathsf{Sol}(S)\neq\varnothing
\Longrightarrow
\mathsf{Sol}(T)\neq\varnothing.
]

因此，如果一个全局 solver 永久放弃 (S) 的其他分支且不回溯，那么总体完备性还需要反向存在性、等价 reduction 或公平回溯。SP-21 只建立 selector safety 和 policy fidelity；它没有声称 total solver completeness。

---

## 5. Goal-compatible terminal-first 定理

令外部 coordinator 给出注册动作间的优先关系

[
i\prec_C j
]

以及显式的 later 关系。对 terminal (A_i) 与 producer (A_j)，定义 guard overlap

[
\mathsf{Overlap}(i,j)
\iff
\exists S;
\bigl(
\mathsf{Predicate}*i(S)
\land
\mathsf{Guard}*{A_j}(S)
\bigr).
]

要求 manifest 满足：

[
\begin{aligned}
\text{G1:}\quad&
K_i=\mathsf{terminal}
\land i\prec_Cj
\land\mathsf{Overlap}(i,j)
\Longrightarrow i<j;[1mm]
\text{G2:}\quad&
K_i=\mathsf{terminal}
\land i\not<j\
&\qquad\Longrightarrow
\mathsf{Disjoint}(i,j)
\ \lor
j\prec_C i;[1mm]
\text{G3:}\quad&
\text{policy order、predicate、implementation/proof ID、}\
&\text{owner/domain、branch index、subject binding}\
&\text{均由 producer 外部 authority 固定；}[1mm]
\text{G4:}\quad&
\text{target 只能经 common admission 和 re-entry 入队；}[1mm]
\text{G5:}\quad&
\text{scope receipt 的编码类型与 global miss 类型不相交。}
\end{aligned}
]

还应要求 priority metadata 与实际顺序无冲突，例如 earlier action 不得同时标记为 later。

定义 coordinator-relative terminal-first 条件：

[
\begin{aligned}
\mathsf{TerminalFirst}_C(j,S)
\iff
\forall i,\quad&
K_i=\mathsf{terminal}
\land i\prec_Cj
\land\mathsf{Predicate}_i(S)\
&\Longrightarrow r_i(S)=\mathsf{MISS}.
\end{aligned}
]

### 定理 5.1：Goal-compatible scope-bound admission

若 G1–G5 成立，并且

[
\operatorname{PriorClear}*{\mathcal P,j}(S)
\land
\operatorname{NoRejectBefore}*{\mathcal P,j},
]

则

[
\mathsf{TerminalFirst}_C(j,S).
]

若进一步有

[
r_j(S)=\mathsf{TRUE}(T),
\quad
\mathsf{EdgeOK}_j(S,T,\Lambda),
\quad
\mathsf{LiftOK}(S,T,\Lambda),
]

并且 common admission/re-entry gate 接受相应 tickets，则 (T) 是 T6-compatible admitted successor。

#### 证明

取任意 coordinator 声明为 prior、且与 (A_j) 重叠的 terminal (A_i)。由 G1，

[
i<j.
]

由 (\operatorname{PriorClear})，

[
r_i(S)=\mathsf{MISS}.
]

所以所有 coordinator-declared prior overlapping terminals 均已清除。

由 G2，任何不在 (j) 前面的 registered terminal，要么与 producer guard 不交，要么被明确置为 later；不存在被静默遗漏的 prior terminal。

由 G3，producer 不能通过修改 policy、owner、branch index 或 replay implementation 伪造这一结论。

由定理 3.1，selector 选择 (A_j)，并得到安全 edge。G4 再保证 candidate target 不会绕过 common admission/re-entry。G5 保证 receipt 只表达 scope clearance。证毕。

这没有降低 terminal-first 要求，而是将其精确定义为：

[
\text{冻结 policy/coordinator 中全部 prior actions 已清除。}
]

它不把“所有可想象的 terminal 公式”错误地纳入一个不可冻结、不可完整编码的隐含宇宙。

---

## 6. independent prefix replayer

一个满足证明要求的 reference replayer 具有如下逻辑结构：

```text
replay_prefix(S, frozen_policy, j):
    validate canonical policy encoding
    validate external authority and policy identity

    records := []

    for i = 0, ..., j-1:
        spec := frozen_policy[i]
        out  := Replay(spec, canonical_encoding(S))

        append bound_record(
            subject_id = ID(S),
            policy_id  = ID(frozen_policy),
            index      = i,
            action_id  = spec.action_id,
            output     = out
        )

        match spec.kind, out:
            terminal, HIT(c):
                verify terminal certificate c against Eq(S)
                return TERMINAL(i, c, records)

            terminal, MISS:
                continue

            producer, TRUE(T0):
                return EARLIER_PRODUCER(i, T0, records)

            producer, FALSE:
                continue

            reject, REJECT(reason):
                return REJECTED(i, reason, records)

            otherwise:
                return INVALID_ACTION_OUTPUT

    assert record indices are exactly all terminal/producer indices < j

    return SCOPE_CLEAR(
        semantic =
          MISS_HIGHER_PRIORITY_POLICY_COMPLETE,
        coverage =
          REGISTERED_HIGHER_PRIORITY_ONLY,
        global_exhaustion = false,
        subject_id = ID(S),
        policy_id = ID(frozen_policy),
        selected_index = j,
        records = records
    )
```

这个 replayer 有以下已经由前缀分割引理证明的性质：

1. **终止性**：循环有限，且每个 earlier replay 终止。
2. **确定性**：固定 (S)、policy 和 (j) 时结果唯一。
3. **完整性**：只有所有 earlier terminal MISS、producer false 且没有 earlier reject 时才返回 scope clearance。
4. **健全性**：返回 scope clearance 必然推出式 (1) 的前缀可达性。
5. **subject/policy binding**：每条 record 都绑定同一 source、完整 policy identity、动作索引和动作 implementation ID。
6. **独立性**：它不执行 (A_j)，不调用 (A_j) 的 E1–E5/R verifier，也不接受 producer 提供的“前缀已经通过”断言。
7. **terminal authority separation**：它可以调用 earlier terminal action 自己的 certificate verifier，但该 verifier 不依赖 selected producer 的 edge 结论。

因此 replay proof 对 (A_j) 的 target、lift 和 edge tickets 是参数无关的；改变 E1–E5 verifier 的结果不会改变 prefix replay 输出。

---

## 7. 必须失败的负控

| 负控                                        | 必须拒绝的位置                                | 证明理由                                     |
| ----------------------------------------- | -------------------------------------- | ---------------------------------------- |
| earlier reject                            | prefix replayer                        | reject 无继续输出，因此 (j) 不可达                  |
| policy mutation                           | receipt/admission policy-ID check      | 完整规范编码改变；旧 receipt 绑定旧 policy            |
| action reorder                            | policy-ID 与 index/action-ID check      | 顺序属于规范编码；同一 action 在不同 index 的 record 无效 |
| later terminal 伪装 global miss             | receipt decoder/serializer             | scope 与 global 是不同 tagged constructors   |
| source swap                               | subject-ID、owner/domain、branch binding | record 对另一 canonical source 无效           |
| guard overlap 且遗漏 declared-prior terminal | manifest linter                        | 违反 G1/G2，不得生成 Goal-compatible ticket     |
| branch index swap                         | record/admission token                 | selected index 和 edge ticket 不一致         |
| queue bypass                              | common admission gate                  | 裸 target 没有 admission token，不得入队         |
| producer 自报 prior MISS                    | independent replayer boundary          | replayer只接受自己的规范重放结果                     |
| mixed-policy replay                       | per-record policy identity             | 不允许不同 record 绑定不同 policy digest          |

### scope/global 编码不混淆

应使用不相交的代数数据类型：

[
\begin{aligned}
\mathsf{Clearance}:={}&
\mathsf{ScopeClear}(
\mathsf{REGISTERED_HIGHER_PRIORITY_ONLY},
\mathsf{global=false},
\ldots)\
&\mid
\mathsf{GlobalMiss}(
\mathsf{GlobalExhaustionProof},
\ldots).
\end{aligned}
]

合法序列化器不得存在

[
\mathsf{ScopeClear}\longrightarrow\mathsf{MISS_COMPLETE}
]

的映射。decoder 必须拒绝以下不一致组合：

[
\begin{aligned}
&\mathsf{semantic}
=\mathsf{MISS_HIGHER_PRIORITY_POLICY_COMPLETE},\
&\mathsf{global_exhaustion}=\mathsf{true},
\end{aligned}
]

或

[
\mathsf{coverage}
\neq
\mathsf{REGISTERED_HIGHER_PRIORITY_ONLY}.
]

---

## 8. (q=1) 负控的完整有限证明

以下证明不依赖任何未定义的 Bradford 实现。它直接给出一个有限、确定、可靠的 divisor terminal screen。

### 8.1 固定 gap 的完整 divisor 判据

令

[
x_g=\frac{p+g}{4},
\qquad
D_g=p,x_g.
]

则

[
\frac4p-\frac1{x_g}
===================

# \frac{4x_g-p}{px_g}

\frac g{D_g}.
]

寻找另外两个单位分数等价于寻找

[
\frac g{D_g}=\frac1y+\frac1z.
]

对正整数 (y,z)，定义

[
a=gy-D_g,\qquad b=gz-D_g.
]

由于另一单位分数严格为正，有 (gy>D_g) 和 (gz>D_g)，故 (a,b>0)。并且

[
\begin{aligned}
ab
&=(gy-D_g)(gz-D_g)\
&=g^2yz-gD_g(y+z)+D_g^2\
&=D_g^2.
\end{aligned}
]

最后一步使用

[
gyz=D_g(y+z).
]

反之，若存在正因子 (a,b) 满足

[
ab=D_g^2,
\qquad
a\equiv b\equiv-D_g\pmod g,
]

则

[
y=\frac{a+D_g}{g},
\qquad
z=\frac{b+D_g}{g}
]

为正整数，并由反向展开得到

[
\frac g{D_g}=\frac1y+\frac1z.
]

因此：

[
\boxed{
\frac g{D_g}=\frac1y+\frac1z
\iff
\exists a\mid D_g^2:
\quad
a\equiv \frac{D_g^2}{a}\equiv-D_g\pmod g.}
\tag{8}
]

一个 terminal action 可以按递增顺序枚举 (D_g^2) 的全部因子。该过程有限、确定；HIT certificate 由式 (8) 保证可靠；没有候选时返回 MISS。

### 8.2 (p) 与 (X)

[
p=21169,
\qquad
p\equiv1\pmod4,
]

且

[
X=\frac{p+3}{4}=5293=67\cdot79.
]

如需独立验证 (p) 为素数，可使用 Pocklington certificate：

[
21168=2^4\cdot3^3\cdot7^2,
]

并取 witness (13)。直接模幂计算给出

[
\begin{aligned}
13^{21168}&\equiv1,\
13^{10584}&\equiv21168,\
13^{7056}&\equiv10710,\
13^{3024}&\equiv20207
\pmod{21169},
\end{aligned}
]

而

[
\gcd(21167,21169)
=================

# \gcd(10709,21169)

\gcd(20206,21169)
=1.
]

由于 (21168>\sqrt{21169})，该证书证明 (21169) 为素数。

### 8.3 (M_{23}) 的完整 scope MISS

对

[
M_{23}={3,7,11,15,19,23},
]

记

[
\mathcal R_g
============

{a\bmod g:a\mid D_g^2}.
]

由 (p) 和相应 (x_g) 的素因子分解，逐个枚举各素因子在 (D_g^2) 中允许的指数，即得：

[
\begin{array}{c|c|c|c}
g&x_g\text{ 的分解}&-D_g\bmod g&\mathcal R_g\ \hline
3&5293=67\cdot79
&2
&{1}\
7&5294=2\cdot2647
&5
&{1,2,4}\
11&5295=3\cdot5\cdot353
&2
&{1,3,4,5,9}\
15&5296=2^4\cdot331
&11
&{1,2,4,8}\
19&5297
&12
&{1,2,3,7,9,10,11,15,16}\
23&5298=2\cdot3\cdot883
&20
&{1,2,3,4,6,8,9,12,13,16,18}.
\end{array}
]

表中的小因子素性可由不超过各自平方根的有限试除复核。

每一行都有

[
-D_g\bmod g\notin\mathcal R_g.
]

因此甚至不存在满足第一个同余

[
a\equiv-D_g\pmod g
]

的因子，更不可能同时满足式 (8) 的两个同余。故六个完整 divisor terminal actions 全部返回 MISS：

[
\boxed{
\forall g\in M_{23},\qquad
\operatorname{Replay}(B_g,S_p)=\mathsf{MISS}.}
\tag{9}
]

这严格证明了 (M_{23}) screen 的 scope MISS。

### 8.4 gap (31)、(d=1) 的 HIT

取

[
g=31,
\qquad
x=x_{31}=\frac{21169+31}{4}=5300,
\qquad
D=px=112195700.
]

模 (31) 有

[
D\equiv4,\qquad -D\equiv27.
]

取

[
a=p=21169.
]

则

[
a\equiv27\equiv-D\pmod{31}.
]

令

[
b=\frac{D^2}{a}=p,x^2.
]

由于

[
x=5300\equiv-1\pmod{31},
]

有

[
b\equiv p x^2\equiv p\equiv27\equiv-D\pmod{31}.
]

所以式 (8) 命中。在标准归一化 (a=pd) 下，这正是

[
d=1.
]

对应

[
\begin{aligned}
y
&=\frac{a+D}{31}
=\frac{p(1+x)}{31}
=3619899,\
z
&=\frac{b+D}{31}
=x,y
=19185464700.
\end{aligned}
]

也可直接验证：

[
x+1=5301=31\cdot171,
]

所以

[
y=171p=3619899,
\qquad
z=5300y=19185464700.
]

于是

[
\begin{aligned}
\frac1y+\frac1z
&=\frac{x+1}{xy}\
&=\frac{31}{px},
\end{aligned}
]

从而

[
\begin{aligned}
\frac1x+\frac1y+\frac1z
&=\frac1x+\frac{31}{px}\
&=\frac{p+31}{px}\
&=\frac{4x}{px}\
&=\frac4p.
\end{aligned}
]

即

[
\boxed{
\frac4{21169}
=============

\frac1{5300}
+
\frac1{3619899}
+
\frac1{19185464700}.}
\tag{10}
]

因此

[
(5300,3619899,19185464700)\in\mathsf{Sol}(S_p).
]

### 8.5 两个错误结论均被严格否定

由式 (9)，冻结的 (M_{23}) policy prefix 可以合法产生 scope clearance。

由式 (10)，

[
\mathsf{Sol}(S_p)\neq\varnothing.
]

所以：

[
\boxed{
\mathsf{M23ScopeMiss}
\not\Rightarrow
\mathsf{MISS_COMPLETE}.}
]

同时，gap (31) 不在 (M_{23}) 中并不影响 certificate 的存在：

[
\boxed{
31\notin M_{23}
\not\Rightarrow
\text{gap-31 certificate 不存在}.}
]

若冻结顺序为

[
\mathcal P_{\mathrm{neg}}
=========================

(B_3,B_7,B_{11},B_{15},B_{19},B_{23},
A_{\mathrm{phase}},
B_{31}),
]

那么在六个 (B_g) 全部 MISS、没有 earlier reject 或 true producer、且
(A_{\mathrm{phase}}) guard true 时，selector 合法选择
(A_{\mathrm{phase}})。

later action (B_{31}) 确实能够 HIT，但它在冻结 policy 中位于 producer 之后。该事实：

* 不破坏 prefix priority；
* 不破坏 producer 的 E4 lift；
* 不把 scope clearance 变成错误；
* 只证明该 scope clearance 绝非 global miss。

---

## 9. 最终审定

可以成立的精确结论是：

[
\boxed{
\begin{aligned}
&\textbf{SP-21 safety theorem：ESTABLISHED；}\
&\textbf{原始未修正的 operational 表述：不成立。}
\end{aligned}}
]

必须写入正式命题的补丁是：

[
\operatorname{NoRejectBefore}_{\mathcal P,j}
]

或等价的

[
\operatorname{Reach}_{\mathcal P,j}(S),
]

以及 actual terminal 分支的最小决定索引条件。

在这些修正下，已经证明：

[
\boxed{
\begin{aligned}
&\operatorname{PriorClear}*{\mathcal P,j}(S)
\land
\operatorname{NoRejectBefore}*{\mathcal P,j}
\land
\operatorname{Guard}_{A_j}(S)\
&\qquad\land
\mathsf{EdgeOK}*j(S,T,\Lambda)
\land
\mathsf{LiftOK}(S,T,\Lambda)\
&\hspace{35mm}\Longrightarrow
\mathsf{VerifiedSuccessor}^{\mathrm{safe}}*{\mathcal P,j}(S,T).
\end{aligned}}
]

该证明不需要、也不推出

[
\mathsf{Sol}(S)=\varnothing,
]

不量化所有未注册 terminal families，不改变任何 family totality、T6 completeness 或猜想状态。

若“ESTABLISHED”状态还要求第 6 节所列的具体工程证据，则应分成：

[
\begin{aligned}
&\mathsf{SP21_THEOREM}
=\mathsf{ESTABLISHED},\
&\mathsf{SP21_CONCRETE_POLICY_INSTANCE}
=\mathsf{OPEN_EVIDENCE},
\end{aligned}
]

因为具体 producer 的完整 manifest、实现/证明 ID、外部 authority、common admission 实现和独立 replayer 二进制并未包含在题面中。理论证明、完整 (M_{23}) MISS 负控和 gap (31) HIT 负控则已经闭合。
