# SP-03：唯一准入、无绕过与全 target re-entry

**状态：** OPEN_PROPOSITION
**研究任务：** 证明递归证明程序只有一个持久准入路径，且每个非终止 target 都回到同一状态宇宙。
**独立性：** 本文件自定义全部对象和证明义务；前提只限本文明确给出的对象与假设。

## 背景与独立对象

设 \(\mathscr P\) 是所有允许持久化的状态，\(\mathscr Q\) 是持久队列。
系统有一个公共准入谓词 \(A(S)\)，一个公共分类器 \(\kappa(S)\)，以及一个唯一
的持久化操作 \(E(S)\)。任何状态只有在通过 \(A\) 后才能进入 \(\mathscr Q\)。

本文件中：

* producer 是从合法 source 提出临时后继的函数；
* projector 是从 source 和 witness 唯一计算 target 的纯函数；
* schema 是规范编码允许的字段集合和类型；
* grammar 是对规范 target 的可判定合法性谓词；
* owner 是由规范 target 唯一重算的分类值；
* admission 是同时检查 schema、grammar、owner、parent、terminal priority、全称解提升和势下降的谓词；
* E1 是 actual parent/occurrence 谱系；
* E2 是由 source 和 witness 唯一重算的 target 投影；
* E3 是公共 schema/grammar/owner/admission 的联合证明；
* E4 是对 target 全部解成立的 source 解提升；
* E5 是固定 \(\Pi:\mathscr P\to\mathbb N^7\) 的 parent-to-final 严格下降；
* R 是 target 属于 \(\mathscr P\) 且可由相同 selector contract 再次消费；
* terminal certificate 是一个可靠验证器接受后能给出 source 直接解的证书。
* registry 是在所有 producer 之外冻结、producer 无法修改的有限映射；
* queue token 是 source 编码、target 编码、parent 编码和一次性 nonce 的规范元组；
* actual source 是根初始化输出或一条逐步验证的 parent-target 链的末端。

每个 producer 输出一个临时 target \(T^\circ\)，而不是直接输出持久状态。公共 projector
\(\rho\) 将它映射为统一 envelope \(\rho(T^\circ)=T\)。公共分类器满足：

\[
\kappa(T)\in\{\text{terminal},\text{known family},\text{reject}\}.
\]

定义“绕过”包括：直接 append、隐藏缓存、异步发送、测试对象提升、替换
准入函数、使用另一种持久 target 类型，或在分类器之后再修改状态字段。

## 待证明命题

若能独立证明：

1. 所有 bootstrap 与 successor 入口都经过同一个 \(A\)；
2. 所有 producer 只能通过一个在 producer 之外冻结且不可由其修改的 registry 被调用；
3. 所有持久化写入都经过唯一 \(E\)，且 \(E\) 的调用者只能是 \(A\) 成功后的路径；
4. 所有非终止 target 都先经过同一个 \(\rho\) 和 \(\kappa\)；
5. \(\rho\) 保留 source lineage、equation interface，并允许 owner、grammar 和 \(\Pi\)
   从 target 规范编码重新计算；
6. \(A\) 拒绝缺 E1、E2、E3、E4、E5、R、parent 或 terminal certificate 的 target；

则：

\[
\boxed{
\operatorname{PersistedTargets}
\subseteq
\operatorname{Reenter}(\kappa)
\quad\text{且}\quad
\operatorname{QueueWrites}=\{E\}.
}
\]

若另外证明存在一个固定
\(\Pi:\mathscr P\to\mathbb N^7\) 且每条持久 successor 严格降低它，则公共 runtime
的每条持久 successor 都属于同一良基递归系统。

## 证明义务

证明者必须给出静态调用图和动态追踪定义，覆盖：

* 初始化、普通 successor、terminal、错误恢复和重启；
* list/deque/database/file/IPC 等所有潜在写入；
* target envelope 的 schema 封闭性；
* owner/grammar/admission 的重新计算，而不是继承 producer 的自报字段；
* queue token 的唯一性和不可伪造性；
* target re-entry 的终止性：不能在 \(\kappa\) 前无限 stutter。

## 反例控制

~~~text
直接调用 E 以外的 append；
把临时 target 当作持久 state；
修改 owner 后不重跑 grammar；
把 E3_pre_admission 布尔值换成 common E3；
从 checkpoint rank drop 直接入队；
给 queue token 加一位就绕过 parent-to-final E5；
把 terminal hit 作为普通 producer target。
~~~

## 完成证据

* 完整写入调用图及唯一写入点证明；
* 每类入口到 admission 的路径覆盖；
* 每个 target schema 到 \(\rho\to\kappa\) 的映射；
* queue/no-bypass 负控；
* source/projector/owner/grammar/lift/potential 变更会使旧 admission 失效；
* 独立重放至少一个 terminal、一个 reject 和一个 successor。

本命题不证明具体 producer 的数学 totality；它只证明共享持久化与递归重入合同。
