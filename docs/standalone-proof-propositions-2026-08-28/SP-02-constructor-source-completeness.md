# SP-02：有限递归证明系统中 constructor 的穷尽分类

**状态：** ESTABLISHED（条件有限模型定理；不等于当前仓库 F1 闭合）
**研究任务：** 对一个完全由有限关系给出的递归证明系统，构造无 UNKNOWN 项的 constructor 分类。
**独立性：** 本文件定义全部输入对象、关系、分类算法和证明目标；“constructor”只是一
个有限关系的名称，不指代外部程序、目录或未写出的调用图。

## 独立性声明

本命题是关于一张显式给出的有限关系表的条件定理。证明者拿到
\(\mathcal X,\mathcal C,\mathcal W\) 及下列关系的完整有限描述后，即可只用有限集合论
完成证明。若以后把某个具体系统实例化为该有限模型，实例化者另行证明其关系表完整；
这不是本命题的前提，也不是本命题的结论。

本文件的结论是条件性的元引理：selector totality、control 无后继、状态改变关系注册表
完备性和跨 constructor 的后继标签唯一性都是良构模型的输入证书。证明不会从有限表本身
推导这些语义前提，也不会把它们转译成当前仓库源码的 constructor/source completeness。
因此本文件完成后，抽象 SP-02 可标为 `ESTABLISHED`，但 `U-A0-01`、F1、F2、F3 和 T6
的实际状态不变。

## 一、背景与定义：有限语义模型

固定以下有限集合：

\[
\mathcal X=\text{所有规范状态编码},
\qquad
\mathcal C=\text{所有 constructor 标识},
\qquad
\mathcal W=\text{所有有限 witness 编码}.
\]

每个 constructor \(c\in\mathcal C\) 由以下显式有限关系定义：

\[
\operatorname{Invoke}_c\subseteq\mathcal X\times\mathcal W,
\]

\[
\operatorname{Terminal}_c\subseteq
\mathcal X\times\mathcal W\times\mathcal S,
\]

\[
\operatorname{Successor}_c\subseteq
\mathcal X\times\mathcal W\times\mathcal X,
\]

其中 \(\mathcal S\) 是直接数学解的有限编码集合。所有关系均作为命题输入完整列出，
不是从程序名称或布尔字段推断。

以下约定消除“原始候选”和“实际输出”的歧义。若一个实现先产生 raw candidate 集，
必须先给出一个固定、可重放的 tie-break 函数 \(\tau\)，将每个非空 raw 输出集映射为
一个 canonical output；本命题中的 \(\operatorname{Terminal}_c\) 和
\(\operatorname{Successor}_c\) 是该 canonical、post-tie-break 关系。等价地，也可以
把 \(\tau\) 作为模型输入，并在所有下式中使用其选择后的关系。分类、Reach 和
\(P,Q\) 只看 canonical output，不把未选中的 raw candidate 当成实际 successor。

为使“constructor 集合封闭”成为可检查的输入条件，再给出有限的状态改变注册表

\[
\mathcal G\subseteq\mathcal C\times\mathcal X\times\mathcal W\times\mathcal X.
\]

它列出模型声称的全部 state-changing records；良构条件 6 要求

\[
\mathcal G=
\{(c,S,w,T):(S,w,T)\in\operatorname{Successor}_c\}.
\tag{G}
\]

\(\mathcal G\) 的“列出了全部外部状态改变”是模型的闭世界公理，不能从缺失的数据中
自动发现；算法只能检查给定注册表与 successor 表的一致性。

固定：

* 根状态集合 \(\mathcal R\subseteq\mathcal X\)；
* 合法状态谓词 \(\operatorname{Legal}\subseteq\mathcal X\)；
* terminal 解验证关系
  \(\operatorname{VerifySol}\subseteq\mathcal X\times\mathcal S\)；
* selector 调用集合
  \(\mathcal C_{\rm sel}\subseteq\mathcal C\)；
* control 调用集合
  \(\mathcal C_{\rm ctl}=\mathcal C\setminus\mathcal C_{\rm sel}\)。

定义实际可达集 \(\operatorname{Reach}\subseteq\mathcal X\) 为满足下列条件的最小集合：

\[
\mathcal R\cap\operatorname{Legal}\subseteq\operatorname{Reach},
\]

且若
\[
S\in\operatorname{Reach},\quad
(S,w,T)\in\operatorname{Successor}_c,\quad
c\in\mathcal C_{\rm sel},\quad
T\in\operatorname{Legal},
\]

则 \(T\in\operatorname{Reach}\)。

因为 \(\mathcal X\) 有限，\(\operatorname{Reach}\) 可由单调闭包在至多
\(|\mathcal X|\) 轮内计算。

## 二、系统良构条件

命题只量化满足以下条件的有限模型：

1. **终端可靠性**
   \[
   (S,w,s)\in\operatorname{Terminal}_c
   \Longrightarrow
   (S,s)\in\operatorname{VerifySol}.
   \]
   并假设 \(\operatorname{VerifySol}\) sound：
   \[
   (S,s)\in\operatorname{VerifySol}
   \Longrightarrow
   s\in\operatorname{Sol}(S).
   \]
2. **调用--输出绑定和后继合法性**
   \[
   (S,w,s)\in\operatorname{Terminal}_c
   \ \text{或}\
   (S,w,T)\in\operatorname{Successor}_c
   \Longrightarrow
   (S,w)\in\operatorname{Invoke}_c\ \text{且}\ S\in\operatorname{Legal},
   \]
   且每个 successor 输出还满足 \(T\in\operatorname{Legal}\)。
3. **同一次调用的 terminal preemption**
   对同一 \((c,S,w)\)，不能同时存在 terminal 和 successor 输出。
4. **selector totality（对 canonical post-tie-break 输出）**
   对每个 \(c\in\mathcal C_{\rm sel}\)、\(S\in\operatorname{Reach}\) 和
   \((S,w)\in\operatorname{Invoke}_c\)，canonical 输出恰有一个：一个通过
   \(\operatorname{Terminal}_c\) 验证的 terminal，或一个通过
   \(\operatorname{Successor}_c\) 验证的 successor。因而相应 terminal 解或 target
   编码唯一。若模型另有 raw candidate 表，唯一性只要求 tie-break 后的输出，不要求
   raw 集本身只有一项。
5. **control 无持久副作用**
   \[
   c\in\mathcal C_{\rm ctl}
   \Longrightarrow
   \operatorname{Successor}_c=\varnothing.
   \]
6. **constructor 集合封闭**
   显式注册表 \(\mathcal G\) 满足式 (G)，且模型声明不存在注册表之外的
   state-changing relation。前半项可由算法检查，后半项是待实例化系统另行证明的闭世界
   假设。
7. **后继标签唯一**
   对 \(c\ne c'\)，不存在 reachable \(S\)、witness \(w,w'\) 和 target \(T\)
   同时满足
   \[
   (S,w,T)\in\operatorname{Successor}_c,\qquad
   (S,w',T)\in\operatorname{Successor}_{c'}.
   \]

一个不满足 1--7 中任意一项的有限关系表称为**不良构模型**，被拒绝而不进入下述
分类定理的量词域。

## 三、四种处置的形式定义

对 \(c\in\mathcal C\)，定义：

\[
\operatorname{LiveDom}(c)
=
\{S\in\operatorname{Reach}:\exists w\;(S,w)\in\operatorname{Invoke}_c\}.
\]

分类标签集合为

\[
\mathcal K=
\{
\mathsf{ACTIVE\_PRODUCER},
\mathsf{TERMINAL\_ONLY},
\mathsf{NONRUNTIME\_CONTROL},
\mathsf{OBSOLETE\_OR\_UNREACHABLE}
\}.
\]

先定义总的诊断算法
\(\widehat\Delta:\mathcal C\to\mathcal K\cup\{\mathsf{UNKNOWN}\}\)，按以下有序分支返回：

\[
\widehat\Delta(c)=
\begin{cases}
\mathsf{OBSOLETE\_OR\_UNREACHABLE},
&\operatorname{LiveDom}(c)=\varnothing,\\
\mathsf{ACTIVE\_PRODUCER},
&\exists S\in\operatorname{LiveDom}(c),w,T:
(S,w,T)\in\operatorname{Successor}_c,\\
\mathsf{TERMINAL\_ONLY},
&\nexists S\in\operatorname{LiveDom}(c),w,T:
(S,w,T)\in\operatorname{Successor}_c
\text{ 且 }
\exists S\in\operatorname{LiveDom}(c),w,s:
(S,w,s)\in\operatorname{Terminal}_c,\\
\mathsf{NONRUNTIME\_CONTROL},
&c\in\mathcal C_{\rm ctl},\\
\mathsf{UNKNOWN},&\text{其余情形}.
\end{cases}
\]

在良构模型上，第四个分支只会在没有 terminal 或 successor 输出的 control 调用上出现；
若某个 selector 落入最后一项，则违反 selector totality。待证结论将表明最后一项
从不发生，于是 \(\Delta=\widehat\Delta\) 的值域可收紧为 \(\mathcal K\)。

## 四、待证明命题

证明：

1. 在每个良构有限模型中，\(\widehat\Delta(c)\ne\mathsf{UNKNOWN}\) 对所有
   \(c\in\mathcal C\) 成立；
2. 四个非 UNKNOWN 分类谓词两两互斥；
3. 四类的并集为 \(\mathcal C\)；
4. 每个从 \(\operatorname{Reach}\) 中 source 产生的 successor 都由一个且仅一个
   \(\mathsf{ACTIVE\_PRODUCER}\) constructor 关系产生；
5. control 和 unreachable constructor 不可能扩张
   \(\operatorname{Reach}\)；
6. 因而
   \[
   \boxed{
   \#\{c\in\mathcal C:\widehat\Delta(c)=\mathsf{UNKNOWN}\}=0.
   }
   \]

这里 UNKNOWN 是真实算法输出的失败标记，而不是预先从值域中删除的符号。

## 五、算法与复杂度

证明者必须给出：

1. 计算 \(\operatorname{Reach}\) 的有限闭包算法；
2. 对每个 \(c\) 枚举 \(\operatorname{LiveDom}(c)\) 的算法；
3. 按定义计算 \(\widehat\Delta(c)\) 的算法；
4. 以
   \[
   O(|\mathcal X|\,|\mathcal C|\,|\mathcal W|\,|\mathcal X|)
   \]
   或更精确上界证明算法终止。

## 六、必须拒绝的模型

以下任一情况使模型不良构，而不是产生第五类：

* 未列入 \(\mathcal C\) 的关系可以产生状态；
* 同一调用既 terminal 又 successor；
* 两个 constructor 对同一 reachable source 产生同一 target；
* control relation 产生可扩张 \(\operatorname{Reach}\) 的 successor；
* selector 在 reachable state 上无输出；
* terminal relation 的候选解不能通过 \(\operatorname{VerifySol}\)；
* successor target 不满足 \(\operatorname{Legal}\)。

## 七、完成证据

命题从 OPEN_PROPOSITION 改为 ESTABLISHED 前，需要：

* 四类互斥和穷尽的形式证明；
* \(\operatorname{Reach}\) 最小不动点证明；
* 分类算法的终止性和复杂度证明；
* 对上述七类不良构模型的负控；
* 至少一个同时含 root、terminal-only、active producer、control 和 unreachable
  constructor 的完整有限示例。

本命题是独立的有限关系定理。把它应用到任何具体系统时，必须另外把该系统完整抽象为
这里要求的有限关系，并证明抽象忠实；该实例化不属于本命题的隐藏前提。

---

## 八、SP-02 完整证明（2026-08-28）

### 8.1 结论的准确范围

本节证明的是一个**条件有限模型定理**。良构条件 4（selector totality）、条件 5
（control 无 successor）、条件 6（完整 state-change registry）和条件 7（跨 constructor
的后继标签唯一）都是定理的假设，而不是由仓库源码自动推出的结论。特别是，若删除
条件 4，单个有 live invocation 但无任何输出的 selector 就立即给出
\(\mathsf{UNKNOWN}\)；所以本证明不能单独把当前 F1 的 U-A0-01 清零。

同样，若输入提供 raw candidate 集，必须先用模型输入的固定 tie-break \(\tau\) 产生
canonical post-tie-break 关系。以下 \(P,Q,\operatorname{Reach}\) 和分类均只引用
canonical 关系；原始 guards 本身可以重叠，不承担互斥性。

### 8.2 有效分支规范化

对每个 \(c\in\mathcal C\)，记

\[
L(c)\iff \operatorname{LiveDom}(c)\ne\varnothing,
\]

\[
P(c)\iff
\exists S\in\operatorname{LiveDom}(c),w,T:
(S,w,T)\in\operatorname{Successor}_c,
\]

\[
Q(c)\iff
\exists S\in\operatorname{LiveDom}(c),w,s:
(S,w,s)\in\operatorname{Terminal}_c,
\qquad
K(c)\iff c\in\mathcal C_{\rm ctl}.
\]

首匹配算法的五个有效输出谓词是

\[
\begin{aligned}
E_{\rm O}(c)&\iff\neg L(c),\\
E_{\rm A}(c)&\iff L(c)\land P(c),\\
E_{\rm T}(c)&\iff L(c)\land\neg P(c)\land Q(c),\\
E_{\rm N}(c)&\iff L(c)\land\neg P(c)\land\neg Q(c)\land K(c),\\
E_{\rm U}(c)&\iff L(c)\land\neg P(c)\land\neg Q(c)\land\neg K(c).
\end{aligned}
\tag{21}
\]

它们分别等价于

\[
\begin{aligned}
E_{\rm O}(c)&\iff\widehat\Delta(c)=\mathsf{OBSOLETE\_OR\_UNREACHABLE},\\
E_{\rm A}(c)&\iff\widehat\Delta(c)=\mathsf{ACTIVE\_PRODUCER},\\
E_{\rm T}(c)&\iff\widehat\Delta(c)=\mathsf{TERMINAL\_ONLY},\\
E_{\rm N}(c)&\iff\widehat\Delta(c)=\mathsf{NONRUNTIME\_CONTROL},\\
E_{\rm U}(c)&\iff\widehat\Delta(c)=\mathsf{UNKNOWN}.
\end{aligned}
\]

因为 \(K(c)\) 是 \(\mathcal C_{\rm ctl}=\mathcal C\setminus\mathcal C_{\rm sel}\) 的特征
谓词，任意 \(c\) 必有 \(L(c)\) 或 \(\neg L(c)\)；在 \(L(c)\) 为真时，\(P(c)\) 或
\(\neg P(c)\)，再依次有 \(Q(c)\) 或 \(\neg Q(c)\)、\(K(c)\) 或 \(\neg K(c)\)。因此

\[
\boxed{
\mathcal C=
E_{\rm O}\mathbin{\dot\cup}E_{\rm A}
\mathbin{\dot\cup}E_{\rm T}
\mathbin{\dot\cup}E_{\rm N}
\mathbin{\dot\cup}E_{\rm U}
}.
\tag{22}
\]

至少一个布尔文字在每两个不同分支之间取相反值，所以五类两两互斥。这里的点号析取
是对**实际首匹配输出**而言；把四个未经前序否定的 raw guards 直接声称互斥是不正确的。

### 8.3 Reach 的最小不动点

定义

\[
\operatorname{Post}(A)=
\left\{
T\in\operatorname{Legal}:
\exists S\in A,\ c\in\mathcal C_{\rm sel},w,\\
(S,w,T)\in\operatorname{Successor}_c
\right\}.
\]

令

\[
A_0=\mathcal R\cap\operatorname{Legal},
\qquad
A_{i+1}=A_i\cup\operatorname{Post}(A_i).
\tag{23}
\]

这是递增序列。由于 \(\mathcal X\) 有限，至多发生
\(|\mathcal X|-|A_0|\) 次严格增长，故存在 \(j\le|\mathcal X|\) 使
\(A_j=A_{j+1}\)。令 \(A_\ast=A_j\)，则

\[
\mathcal R\cap\operatorname{Legal}\subseteq A_\ast,
\qquad
\operatorname{Post}(A_\ast)\subseteq A_\ast.
\tag{24}
\]

若 \(B\subseteq\mathcal X\) 也满足这两个闭包条件，则归纳得 \(A_i\subseteq B\)：
基步为 \(A_0\subseteq B\)；若 \(A_i\subseteq B\)，则
\(\operatorname{Post}(A_i)\subseteq\operatorname{Post}(B)\subseteq B\)，从而
\(A_{i+1}\subseteq B\)。所以 \(A_\ast\subseteq B\)，即

\[
\boxed{\operatorname{Reach}=A_\ast}.
\tag{25}
\]

由 (23) 的基集和每次只加入 \(\operatorname{Legal}\) 状态，另有
\(\operatorname{Reach}\subseteq\operatorname{Legal}\)。

条件 6 的可检查部分是显式注册表 \(\mathcal G\) 与 successor 表满足

\[
\mathcal G=
\{(c,S,w,T):(S,w,T)\in\operatorname{Successor}_c\}.
\tag{26}
\]

“不存在 \(\mathcal G\) 之外的外部状态改变”不能从缺失数据中发现，必须作为模型的闭世界
假设或由另一个实例化证明提供。

### 8.4 队列算法

预先建立 canonical successor 邻接索引

\[
\operatorname{Adj}[S]=
\{T\in\operatorname{Legal}:
\exists c\in\mathcal C_{\rm sel},w,\\
(S,w,T)\in\operatorname{Successor}_c\}.
\]

然后执行：

~~~text
Reach := R ∩ Legal
Q := 将 Reach 中所有状态各放入一次的队列
while Q 非空:
    S := Q.pop()
    for T in Adj[S]:
        if T 不在 Reach:
            将 T 加入 Reach
            Q.push(T)
return Reach
~~~

每个状态至多入队一次，每条已登记 successor 至多在其 source 出队时扫描一次。按
路径长度归纳，队列在第 \(i\) 层得到的状态恰为 \(A_i\) 的新增部分，因此返回值正是
(25) 的最小不动点。

### 8.5 UNKNOWN 不可达：充分条件与等价边界

先定义 constructor-level selector coverage 条件

\[
\mathrm{SC}_{\rm ctor}\iff
\forall c\in\mathcal C_{\rm sel},\quad
L(c)\Longrightarrow P(c)\lor Q(c),
\tag{27}
\]

其中 \(P(c),Q(c)\) 是 (21) 中按 constructor 聚合的谓词。直接按 (21) 可得

\[
\boxed{E_{\rm U}=\varnothing\quad\Longleftrightarrow\quad\mathrm{SC}_{\rm ctor}}
\tag{28}
\]

（左到右、右到左都只是对 (21) 的布尔重写）。另定义更强的逐调用条件

\[
\mathrm{SC}_{\rm call}\iff
\forall c\in\mathcal C_{\rm sel},\\
\forall S\in\operatorname{Reach},\\
\forall w,\quad
(S,w)\in\operatorname{Invoke}_c
\Longrightarrow P_{S,w}\lor Q_{S,w}.
\tag{29}
\]

显然 \(\mathrm{SC}_{\rm call}\Rightarrow\mathrm{SC}_{\rm ctor}\)，但反向一般不成立：
同一 constructor 可以有一个有输出的 live invocation 和另一个无输出的 live invocation。

良构条件 4 的 selector totality 正是 \(\mathrm{SC}_{\rm call}\) 的一个更强、带唯一 canonical output 的
输入证书。若反设某个 \(c\) 满足 \(E_{\rm U}(c)\)，则 \(L(c)\) 给出
\(S\in\operatorname{Reach}\) 与 \((S,w)\in\operatorname{Invoke}_c\)，而
\(\neg K(c)\) 给出 \(c\in\mathcal C_{\rm sel}\)。条件 4 对该调用保证恰有一个 terminal
或 successor：

* successor 输出立即推出 \(P(c)\)，与 \(\neg P(c)\) 矛盾；
* terminal 输出立即推出 \(Q(c)\)，与 \(\neg Q(c)\) 矛盾。

所以在满足条件 4 的良构模型中

\[
\boxed{
\#\{c\in\mathcal C:\widehat\Delta(c)=\mathsf{UNKNOWN}\}=0.
}
\tag{30}
\]

注意 (30) 是“给定 selector-totality 证书后的诊断引理”，不是从源码 census 自动
证明 SC；唯一 selector invocation 无输出的有限模型正是反例。

### 8.6 reachable successor 的 active-producer owner 唯一性

取

\[
S\in\operatorname{Reach},\qquad
(S,w,T)\in\operatorname{Successor}_c.
\]

由条件 2，\((S,w)\in\operatorname{Invoke}_c\)、\(S,T\in\operatorname{Legal}\)，故
\(S\in\operatorname{LiveDom}(c)\) 且 \(P(c)\) 成立。若 \(c\) 是 control，则条件 5
与 successor 存在矛盾，所以 \(c\in\mathcal C_{\rm sel}\)，从而

\[
\widehat\Delta(c)=\mathsf{ACTIVE\_PRODUCER}.
\tag{31}
\]

若另一个 \(c'\ne c\) 以另一个 witness \(w'\) 对同一 \(S,T\) 产生 successor，则违反
条件 7。因此

\[
\boxed{
\forall S\in\operatorname{Reach},T\in\mathcal X,\quad
\#\{c:\exists w\ (S,w,T)\in\operatorname{Successor}_c\}\le1.
}
\tag{32}
\]

这只保证 constructor owner 唯一，不保证同一 constructor 的 witness 唯一。

### 8.7 control 与 unreachable constructor 不扩张 Reach

若 \(c\in\mathcal C_{\rm ctl}\)，条件 5 给出
\(\operatorname{Successor}_c=\varnothing\)，故它没有 Reach 扩张边。若
\(\operatorname{LiveDom}(c)=\varnothing\)，而假设存在 reachable source 的 successor，
条件 2 会推出该 source 属于 \(\operatorname{LiveDom}(c)\)，矛盾。因此

\[
\operatorname{LiveDom}(c)=\varnothing
\Longrightarrow
\nexists S\in\operatorname{Reach},w,T:
(S,w,T)\in\operatorname{Successor}_c.
\tag{32}
\]

结合 (26) 的闭世界假设，不存在未登记的其它 Reach 扩张机制。

### 8.8 完整验证算法与复杂度

验证器先检查有限域、关系 tuple 类型、(26)、终端 soundness、调用绑定、source/target
合法性、canonical tie-break 输出、control 无 successor 和条件 7。对每个 reachable
selector invocation 检查 canonical 输出恰有一个；失败立即返回
REJECT_MALFORMED_MODEL，不产生分类结果。一个与证明逐项对应的实现顺序是：

~~~text
validate_domains_and_relation_keys()
validate_terminal_binding_and_VerifySol_soundness()
validate_successor_binding_and_Legal_targets()
validate_state_change_registry_G()
validate_terminal_successor_preemption()
Reach := least_fixed_point_by_queue()
for c in C:
    Live[c] := {S in Reach : exists w, (S,w) in Invoke_c}
    HasSucc[c] := exists S in Live[c], w, T:
                   (S,w,T) in Successor_c
    HasTerm[c] := exists S in Live[c], w, s:
                   (S,w,s) in Terminal_c
    if Live[c] is empty:
        label[c] := OBSOLETE_OR_UNREACHABLE
    elif HasSucc[c]:
        label[c] := ACTIVE_PRODUCER
    elif HasTerm[c]:
        label[c] := TERMINAL_ONLY
    elif c in C_ctl:
        label[c] := NONRUNTIME_CONTROL
    else:
        label[c] := UNKNOWN
~~~

由于 UNKNOWN 是真实的最后一个分支，验证器不得在输入阶段把它从枚举值域删除；
在满足 selector totality 的模型上，(29) 再证明该分支不可达。通过后按 (23) 或队列
算法计算 Reach，再按 (21) 输出标签。

记

\[
n=|\mathcal X|,\quad m=|\mathcal C|,\quad q=|\mathcal W|,\quad \sigma=|\mathcal S|,
\]

\[
N_I=\sum_c|\operatorname{Invoke}_c|,\quad
N_E=\sum_c|\operatorname{Successor}_c|,\quad
N_T=\sum_c|\operatorname{Terminal}_c|,
\quad N_V=|\operatorname{VerifySol}|,\quad N_G=|\mathcal G|.
\]

使用哈希索引时，建立关系索引、Reach 闭包、LiveDom/输出计数、分类和闭包注册表检查
的总输入时间为

\[
\boxed{
O(n+m+N_I+N_E+N_T+N_V+N_G).
}
\tag{33}
\]

稠密上界为

\[
N_I\le mnq,\qquad
N_E\le mn^2q,\qquad
N_T\le mnq\sigma,\qquad
N_V\le n\sigma.
\]

若要写成题目给出的粗界
\(O(|\mathcal C||\mathcal W||\mathcal X|^2)\)，还必须显式假设

\[
\sigma=O(n),\qquad N_V+N_G=O(mqn^2).
\tag{34}
\]

只假设 \(N_T=O(mqn^2)\) 不足以控制 \(N_V\) 或 \(N_G\)。在 (34) 下 (33) 才退化为

\[
O(mqn^2).
\tag{35}
\]

所有循环遍历有限表，且队列每个状态只入队一次，故算法终止。

### 8.9 完整有限良构示例

取

\[
\mathcal X=\{r,a,z,b\},\quad
\operatorname{Legal}=\{r,a,z\},\quad
\mathcal R=\{r\},
\]

\[
\mathcal W=\{w_p,w_t,w_k,w_u\},\quad
\mathcal S=\{s_\ast\},\quad
\mathcal C=\{p,t,k,u\},
\]

\[
\mathcal C_{\rm sel}=\{p,t,u\},\qquad
\mathcal C_{\rm ctl}=\{k\},\qquad
\operatorname{VerifySol}=\{(a,s_\ast)\}.
\]

非空 canonical 关系只有

\[
\begin{array}{c|c|c|c}
c&\operatorname{Invoke}_c&\operatorname{Terminal}_c&\operatorname{Successor}_c\\\hline
p&\{(r,w_p)\}&\varnothing&\{(r,w_p,a)\}\\
t&\{(a,w_t)\}&\{(a,w_t,s_\ast)\}&\varnothing\\
k&\{(r,w_k)\}&\varnothing&\varnothing\\
u&\{(z,w_u)\}&\varnothing&\{(z,w_u,z)\}.
\end{array}
\]

令 \(\mathcal G\) 恰为上表的两条 successor record。于是

\[
A_0=\{r\},\qquad A_1=\{r,a\},\qquad
\operatorname{Reach}=\{r,a\}.
\]

相应

\[
\operatorname{LiveDom}(p)=\{r\},\\
\operatorname{LiveDom}(t)=\{a\},\\
\operatorname{LiveDom}(k)=\{r\},\\
\operatorname{LiveDom}(u)=\varnothing.
\]

所以

\[
\widehat\Delta(p)=\mathsf{ACTIVE\_PRODUCER},\quad
\widehat\Delta(t)=\mathsf{TERMINAL\_ONLY},\quad
\widehat\Delta(k)=\mathsf{NONRUNTIME\_CONTROL},\quad
\widehat\Delta(u)=\mathsf{OBSOLETE\_OR\_UNREACHABLE}.
\]

该例同时含 root、terminal-only、active producer、control 和带静态 successor 的
unreachable constructor，并满足所有良构条件。

### 8.10 七个负控

以下每次只对上例作一项修改；验证器都应在分类前拒绝：

| 控制 | 单独修改 | 违反项 |
|---|---|---|
| NC-1 | 在 \(\mathcal G\) 增加未出现在 successor 表的 rogue record | 条件 6 的 (26) |
| NC-2 | 给 \(t\) 同一调用同时增加 successor，保留 terminal | canonical preemption/唯一输出 |
| NC-3 | 让另一个 constructor 从 reachable \(r\) 产生同一 target \(a\) | 条件 7 |
| NC-4 | 给 control \(k\) 增加 successor | 条件 5 |
| NC-5 | 给 reachable selector invocation 增加 Invoke 但不增加输出 | 条件 4/SC |
| NC-6 | 增加无法通过 \(\operatorname{VerifySol}\) 的 terminal | 条件 1 与 VerifySol soundness |
| NC-7 | 让 successor target 为非法状态 \(b\) | 条件 2 |

另有一个 tie-break 边界控制：允许 raw 表中多个候选，但给出确定的 \(\tau\) 后只将其
canonical 选择写入三张关系表；这不应被错误拒绝。反过来，若 canonical 输出仍有
两个不同 target 且没有 \(\tau\) 选择，则条件 4 失败。

### 8.11 最终定理与当前项目边界

综合 (22)、(25)、(29)、(31) 和 (32)，对任何满足条件 1--7、且 \(\mathcal G\) 完备性
声明真实成立的有限模型：

\[
\forall c\in\mathcal C,\qquad
\widehat\Delta(c)\in
\left\{
\begin{array}{l}
\mathsf{ACTIVE\_PRODUCER},\\
\mathsf{TERMINAL\_ONLY},\\
\mathsf{NONRUNTIME\_CONTROL},\\
\mathsf{OBSOLETE\_OR\_UNREACHABLE}
\end{array}
\right\},
\]

四个实际输出类两两互斥、并集为 \(\mathcal C\)，每个 reachable successor 的 constructor
owner 至多一个，control 和 unreachable constructor 不扩张 Reach，且

\[
\boxed{
\#\{c\in\mathcal C:
\widehat\Delta(c)=\mathsf{UNKNOWN}\}=0.
}
\tag{36}
\]

这个结果可以把抽象 SP-02 从 OPEN_PROPOSITION 改为 ESTABLISHED（条件定理），但
不能修改当前仓库的

~~~text
U-A0-01/U-A0-02/U-A0-03/U-A0-08
F1 = OPEN_MINIMAL_GAPS
F2 = OPEN
F3 = OPEN_MINIMAL_GAPS
T6 = OPEN
~~~

因为当前项目尚未给出完整 concrete finite abstraction、全 selector totality 证书、
全 state-change registry、全 constructor owner disjointness 和 faithful correspondence
的证明。SP-02 是这些实例化工作的逻辑基线，不是它们的替代品。
