# SP-02：有限递归证明系统中 constructor 的穷尽分类

**状态：** OPEN_PROPOSITION
**研究任务：** 对一个完全由有限关系给出的递归证明系统，构造无 UNKNOWN 项的 constructor 分类。
**独立性：** 本文件定义全部输入对象、关系、分类算法和证明目标；“constructor”只是一
个有限关系的名称，不指代外部程序、目录或未写出的调用图。

## 独立性声明

本命题是关于一张显式给出的有限关系表的条件定理。证明者拿到
\(\mathcal X,\mathcal C,\mathcal W\) 及下列关系的完整有限描述后，即可只用有限集合论
完成证明。若以后把某个具体系统实例化为该有限模型，实例化者另行证明其关系表完整；
这不是本命题的前提，也不是本命题的结论。

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
4. **selector totality**
   对每个 \(c\in\mathcal C_{\rm sel}\)、\(S\in\operatorname{Reach}\) 和
   \((S,w)\in\operatorname{Invoke}_c\)，在固定的规范 tie-break 后恰有一个输出：一个通过
   \(\operatorname{Terminal}_c\) 验证的 terminal，或一个通过
   \(\operatorname{Successor}_c\) 验证的 successor。因而相应 terminal 解或 target 编码唯一。
5. **control 无持久副作用**
   \[
   c\in\mathcal C_{\rm ctl}
   \Longrightarrow
   \operatorname{Successor}_c=\varnothing.
   \]
6. **constructor 集合封闭**
   所有可改变 \(\operatorname{Reach}\) 的关系都已包含在
   \(\{\operatorname{Successor}_c:c\in\mathcal C\}\) 中。
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
* 对上述六类不良构模型的负控；
* 至少一个同时含 root、terminal-only、active producer、control 和 unreachable
  constructor 的完整有限示例。

本命题是独立的有限关系定理。把它应用到任何具体系统时，必须另外把该系统完整抽象为
这里要求的有限关系，并证明抽象忠实；该实例化不属于本命题的隐藏前提。
