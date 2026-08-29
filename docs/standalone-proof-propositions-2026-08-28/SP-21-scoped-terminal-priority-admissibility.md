# SP-21：scope-bound terminal-first 准入的健全性

**状态：** OPEN_PROPOSITION
**优先级：** P0，共享合同阻塞。
**已建立子结论：** 有限冻结 policy 的抽象 successor safety theorem 已建立。
**仍开放：** concrete policy registry、外部 authority、actual source、common admission 与
independent executable replayer。
**Canonical proof：** SP-21-ABSTRACT-SAFETY-PROOF-2026-08-29.md。
**原始提交归档：** docs/archive/proof-submissions/2026-08-29/SP-21-submitted-proof-2026-08-29.md。
**独立性：** 本文件完整定义状态、动作策略、scope MISS、terminal、verified successor
和剩余证明目标；不以仓库的现有 schema、代码或其他 SP 文件作为逻辑前提。

## 1. 对象与策略

令 \(\mathscr S\) 是有限编码状态的集合。每个 \(S\in\mathscr S\) 带有一个方程接口
\(\mathsf{Eq}(S)\) 和解集 \(\mathsf{Sol}(S)\)。固定有限有序 selector policy

\[
\mathcal P=(A_0,A_1,\ldots,A_N).
\]

每个 action \(A_i\) 都有固定 kind：

\[
K_i\in\{\mathsf{terminal},\mathsf{producer},\mathsf{reject}\},
\]

固定 subject 的 replay 是确定且终止的，输出分别属于：

\[
r_i(S)\in
\begin{cases}
\{\mathsf{MISS},\mathsf{HIT}(c)\},&K_i=\mathsf{terminal},\\
\{\mathsf{FALSE},\mathsf{TRUE}(T)\},&K_i=\mathsf{producer},\\
\{\mathsf{REJECT}(\rho)\},&K_i=\mathsf{reject}.
\end{cases}
\]

terminal hit 的 certificate 必须可靠：

\[
r_i(S)=\mathsf{HIT}(c)
\Longrightarrow
c\in\mathsf{Sol}(S).
\]

policy 的规范编码必须包含动作顺序、每个谓词、实现/证明标识、owner/domain、
branch index 与 subject binding。producer 本身不能修改该编码。

## 2. Reach 与 Scope Clearance

定义 action 的唯一继续条件：

\[
\operatorname{Pass}_i(S)
\Longleftrightarrow
\begin{cases}
r_i(S)=\mathsf{MISS},&K_i=\mathsf{terminal},\\
r_i(S)=\mathsf{FALSE},&K_i=\mathsf{producer},\\
\bot,&K_i=\mathsf{reject}.
\end{cases}
\]

selected action \(A_j\) 的实际可达性是

\[
\operatorname{Reach}_{\mathcal P,j}(S)
\Longleftrightarrow
\forall i<j,\ \operatorname{Pass}_i(S).
\tag{1}
\]

令 \(\operatorname{PriorClear}_{\mathcal P,j}(S)\) 表示所有 earlier terminal 输出
MISS、所有 earlier producer 输出 FALSE，且相应 record 完整、有序并绑定同一个
source/policy/action index。还要定义：

\[
\operatorname{NoRejectBefore}_{\mathcal P,j}
\Longleftrightarrow
\forall i<j,\ K_i\ne\mathsf{reject}.
\]

于是 canonical relation 是

\[
\boxed{
\operatorname{Reach}_{\mathcal P,j}(S)
\Longleftrightarrow
\operatorname{PriorClear}_{\mathcal P,j}(S)
\land
\operatorname{NoRejectBefore}_{\mathcal P,j}.}
\tag{2}
\]

此前只写 PriorClear 的版本不够：earlier reject 会停止 selector，即使此前没有
terminal 或 producer action。

合法 clearance 的类型固定为

\[
\mathsf{MISS\_HIGHER\_PRIORITY\_POLICY\_COMPLETE},
\qquad
\mathsf{coverage}=
\mathsf{REGISTERED\_HIGHER\_PRIORITY\_ONLY},
\qquad
\mathsf{global\_exhaustion}=\mathrm{false}.
\tag{3}
\]

它不等价于 \(\mathsf{Sol}(S)=\varnothing\)，也不等价于所有未注册 terminal family
都 MISS。

## 3. 已建立的抽象安全定理

若 selected producer \(A_j\) 对 \((S,T,\Lambda)\) 已独立满足 E1--E5、R 和

\[
\forall u\in\mathsf{Sol}(T),\quad
\Lambda(u)\in\mathsf{Sol}(S),
\tag{4}
\]

则：

\[
\boxed{
\begin{aligned}
\operatorname{Reach}_{\mathcal P,i}(S)
\land r_i(S)=\mathsf{HIT}(c)
&\Longrightarrow \mathsf{SelectorTerminal}_{\mathcal P}(S,c),\\
\operatorname{Reach}_{\mathcal P,j}(S)
\land r_j(S)=\mathsf{TRUE}(T)
\land\mathsf{EdgeOK}_j(S,T,\Lambda)
\land\mathsf{LiftOK}(S,T,\Lambda)
&\Longrightarrow
\mathsf{VerifiedSuccessor}^{\mathrm{safe}}_{\mathcal P,j}(S,T).
\end{aligned}}
\tag{5}
\]

有限前缀归纳证明其选定 index 唯一。第一行使用 terminal certificate 的可靠性；第二行
使用 Reach、producer 的 TRUE 输出和独立 edge/lift 义务。完整证明见 canonical proof。

未注册或明确 later 的 terminal certificate 即使存在，也不改变前缀 replay、selected
edge 或 (4)。这只证明 safety，不证明全局 solver completeness；后者仍需要各 family
totality 与 T5 良基归纳。

## 4. 具体 policy 必须证明的内容

为使 abstract theorem 成为 T6-compatible concrete instance，仍必须证明：

1. 每个与 selected producer guard 重叠、且 coordinator 声明为 prior 的 terminal action，
   都在 \(A_j\) 之前；
2. 每个不在 \(A_j\) 前的 registered terminal action，要么与 producer guard 不交，
   要么是显式 later action；
3. policy digest、action identities、owner/domain、branch index 与 replayer 由 producer
   外部 authority 固定；
4. selected target 只能经 common admission 和 re-entry 进入 persistent selector；
5. scope clearance 与 MISS_COMPLETE 是不相交的 serialized types；
6. independent prefix replayer 不执行 selected producer，也不接受 producer 自报的
   prior-MISS 断言。

## 5. q=1 负控

\[
p=21169,\qquad
X=\frac{p+3}{4}=5293=67\cdot79
\]

是 ordinary \(q=1,G\)。M23 的完整有限 factor-pair terminal actions均 MISS，但 gap 31
存在

\[
\frac4{21169}
=\frac1{5300}+\frac1{3619899}+\frac1{19185464700}.
\]

所以 M23 scope clearance 不能写成 MISS_COMPLETE；gap 31 未被列入 M23 也不能否定
其 terminal certificate。这个控制只证明 scope/global 区分的必要性，不授予任何
actual source 或 successor authority。

## 6. 完成证据

本 dossier 从 OPEN_PROPOSITION 改为 ESTABLISHED 前，必须交付：

* concrete coordinator-owned finite policy 与 priority/overlap theorem；
* external authority binding、actual source occurrence 和 source-bound clearance；
* independent executable prefix replayer；
* common admission、queue/re-entry 与 selected producer 的完整 E1--E5 receipts；
* policy mutation、action reorder、earlier reject、earlier true producer、later-terminal
  global-miss relabel、source swap、queue bypass 的可重放负控。

本文件不证明某个 concrete producer guard 非空，不证明 SP-22、F1/F2/F3/T6 totality，
也不改变 Erdős--Straus 猜想的状态。
