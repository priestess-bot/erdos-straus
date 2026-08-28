# SP-01：结构化 E1--E5 递降边的抽象良基归纳（正式版）

**状态：** OPEN_PROPOSITION
**性质：** 逻辑基础命题；所有前提均在本文显式给出。
**独立性：** 本文件完整定义状态、合法域、结果类型、势函数和 E1--E5/R，不依赖其他命题文件。

## 一、状态宇宙与两类义务

设 \(\mathscr U\) 是所有有限编码对象的集合。每个对象 \(S\in\mathscr U\) 带有：

1. 有限规范编码 \(\operatorname{enc}(S)\)；
2. 方程接口 \(\mathsf{Eq}(S)\)；
3. 方程解集
   \[
   \mathsf{Sol}(S)=\{w:w\text{ 满足 }\mathsf{Eq}(S)\};
   \]
4. owner、domain 和 schema 字段。

这些字段必须由规范对象重算；名称、标签和布尔字段本身不构成合法性证明。

对一个给定量词域 \(D\)，令

\[
\operatorname{Legal}_D(S)
\]

表示 \(S\) 满足该域的全部整数、结构和谱系条件，并定义 live-state 集合

\[
\mathscr S_D=\{S\in\mathscr U:\operatorname{Legal}_D(S)\}.
\]

必须区分两类义务：

\[
\mathsf{Obligation}(D)
=
\mathsf{Live}(D,S)
\;\uplus\;
\mathsf{Family}(D),
\]

其中：

* \(\mathsf{Live}(D,S)\) 表示已经给出了一个具体 \(S\in\mathscr S_D\)；
* \(\mathsf{Family}(D)\) 只询问 \(\mathscr S_D\) 是否为空，不产生一个哨兵状态。

## 二、固定七元势与字典序

固定七个总函数

\[
\pi_i:\mathscr S_D\longrightarrow\mathbb N,
\qquad i=1,\ldots,7,
\]

其中

\[
\mathbb N=\{0,1,2,\ldots\}.
\]

每个 \(\pi_i\) 必须在全部合法状态上有定义，由公共正规形计算，并由一个全局固定的
potential schema 决定；不能按边改变坐标含义、坐标顺序或计算算法。

定义

\[
\Pi(S)=
\bigl(\pi_1(S),\pi_2(S),\pi_3(S),\pi_4(S),
\pi_5(S),\pi_6(S),\pi_7(S)\bigr).
\]

对 \(a,b\in\mathbb N^7\)，定义

\[
a<_{\mathrm{lex}}b
\Longleftrightarrow
\bigvee_{j=1}^{7}
\left[
\left(\bigwedge_{i<j}a_i=b_i\right)
\land a_j<b_j
\right].
\]

由于首个不同坐标唯一，这等价于通常的有序七元组字典序；这里比较的是坐标序列，
不是坐标多重集。

为证明良基性，定义序数

\[
\varrho(S)=
\omega^6\pi_1(S)+\omega^5\pi_2(S)+\omega^4\pi_3(S)
+\omega^3\pi_4(S)+\omega^2\pi_5(S)+\omega\pi_6(S)+\pi_7(S).
\]

每个坐标为自然数，所以 \(\varrho(S)<\omega^7\)。Cantor 正规形唯一性给出

\[
\Pi(T)<_{\mathrm{lex}}\Pi(S)
\Longleftrightarrow
\varrho(T)<\varrho(S).
\]

因此

\[
T\prec S
\Longleftrightarrow
\Pi(T)<_{\mathrm{lex}}\Pi(S)
\]

是良基关系。不同状态可以有相同的 \(\Pi\) 值；相同值只表示它们之间不能凭 E5
构成严格下降边，不影响良基性。

## 三、结果类型和互斥性

live-state 结果是带标签的和类型：

\[
\mathsf{Result}(D,S)
=
\mathsf{TERMINAL}(s,c_{\mathrm{term}})
\;\uplus\;
\mathsf{SUCCESSOR}(T,c_{\mathrm{succ}}).
\]

FAMILY_EMPTY 不属于 \(\mathsf{Result}(D,S)\)，而属于域级证书：

\[
\mathsf{FamilyResult}(D)
=\mathsf{FAMILY\_EMPTY}(c_{\mathrm{empty}})
\;\uplus\;
\mathsf{NONEMPTY}(S,c_{\mathrm{live}}).
\]

标签只决定证书的解析方式；数学可靠性由下面的验证关系决定。

### 1. TERMINAL

设

\[
\operatorname{VerifyTerminal}(S,s,c)=1
\]

表示可靠终止验证器接受证书。要求

\[
\operatorname{VerifyTerminal}(S,s,c)=1
\Longrightarrow
s\in\mathsf{Sol}(S).
\]

终止谓词必须由证书定义：

\[
\operatorname{Terminal}(S)
\Longleftrightarrow
\exists s,c\;
\operatorname{VerifyTerminal}(S,s,c)=1.
\]

### 2. SUCCESSOR 与非终止门

定义

\[
\operatorname{VSucc}(S,T)
\Longleftrightarrow
\exists c\;
\operatorname{VerifySucc}(S,T,c)=1
\land
\neg\operatorname{Terminal}(S).
\]

也就是说：

\[
\boxed{
\operatorname{VSucc}(S,T)\Longrightarrow
\neg\operatorname{Terminal}(S).
}
\]

证书 \(c\) 不要求唯一；确定性要求的是给定 \(S\) 时 target \(T\) 唯一。若多个
证书证明同一个 \(T\)，它们仍代表同一条 selector 边。

### 3. FAMILY_EMPTY

域级空性验证器满足

\[
\operatorname{VerifyEmpty}(D,c)=1
\Longrightarrow
\forall S\in\mathscr U,\;
\neg\operatorname{Legal}_D(S).
\]

它不产生 \(S\in\mathscr S_D\)，更不产生一个满足
\(\mathsf{Sol}(S)=\varnothing\) 的状态哨兵。

因此：

* TERMINAL 与 SUCCESSOR 的互斥性来自非终止门；
* FAMILY_EMPTY 与 live-state 结果属于不同的类型，并且空性结论排除任何
  \(\mathsf{Live}(D,S)\)；
* 三种“闭合处置”可以在类型层表示为 TERMINAL、FAMILY_EMPTY、VERIFIED_SUCCESSOR，
  但不能把它们混成同一个状态集合。

## 四、E1--E5 与 R 的最小语义

### E1：actual occurrence and lineage

证书必须包含根初始化证书或已验证前驱序列：

\[
S_0\to S_1\to\cdots\to S_n=S.
\]

验证器逐步检查每个 source/target 编码相等，并从最终 source 的固定序列化 payload
解析所需整数的路径、字节范围和值。不能用另一个状态中的同值整数、owner 名、family
名或手工 occurred=true 替代。

### E2：deterministic projection

冻结规则 \(P\) 和 E1 绑定后，验证器自行计算

\[
T^\star=P(S,\text{E1 binding}),
\]

并要求

\[
\operatorname{enc}(T)=\operatorname{enc}(T^\star).
\]

“存在某个候选 target”不满足 E2。

### E3：common legal typing

验证器必须重新解析 target，按唯一公共 schema 计算正规形、owner、grammar 和
admission。producer 自报的 legal、owner 或 family 字段不具有证明力。

### E4：universal lift

必须给出绑定 source/target interface 的总映射

\[
\Lambda:\mathsf{Sol}(T)\to\mathsf{Sol}(S),
\]

并证明

\[
\forall t\in\mathsf{Sol}(T),\quad
\Lambda(t)\in\mathsf{Sol}(S).
\]

证明可以由可靠证明内核检查；不要求把全称命题误装成有限随机测试。

### E5：strict ticket

验证器从 source 和最终 target 的公共正规形重新计算同一个固定
\(\Pi\)，并要求

\[
\Pi(T)<_{\mathrm{lex}}\Pi(S).
\]

中间 checkpoint 的下降、局部参数下降或临时改变坐标顺序都不满足 E5。

### R：recursive re-entry

必须证明

\[
T\in\mathscr S_D
\]

且下一次选择使用同一个 selector contract、schema、grammar 和势函数。写入队列
本身不能证明 R。

## 五、待证明命题：正式存在性定理

假设对每个 \(S\in\mathscr S_D\)，恰有以下两种 live-state 情形之一：

\[
\operatorname{Terminal}(S)
\quad\dot\lor\quad
\exists!T\in\mathscr S_D,\operatorname{VSucc}(S,T).
\tag{A}
\]

这里的点号析取由
\(\operatorname{VSucc}(S,T)\Rightarrow\neg\operatorname{Terminal}(S)\)
保证；唯一性指 target \(T\)，不指证书。

再假设：

1. terminal verifier 可靠；
2. 每个 VSucc 证书通过 E1、E2、E3、E4、E5 和 R；
3. E5 使用上面固定的七个总函数和固定字典序。

则：

\[
\boxed{
\forall S\in\mathscr S_D,\qquad
\mathsf{Sol}(S)\ne\varnothing.
}
\tag{B}
\]

### 证明

令

\[
P(S)\;:\Longleftrightarrow\;\mathsf{Sol}(S)\ne\varnothing.
\]

在良基关系 \(\prec\) 上作良基归纳。固定任意 \(S\in\mathscr S_D\)，假设

\[
\forall U\in\mathscr S_D,\quad U\prec S\Longrightarrow P(U).
\]

由 (A)：

**情形一：** \(\operatorname{Terminal}(S)\)。
存在 \(s,c\) 使验证器接受；可靠性给出
\(s\in\mathsf{Sol}(S)\)，所以 \(P(S)\)。

**情形二：** \(\operatorname{VSucc}(S,T)\)。
由 R，\(T\in\mathscr S_D\)；由 E5，\(T\prec S\)。归纳假设给出
\(\mathsf{Sol}(T)\ne\varnothing\)。取任意
\(t\in\mathsf{Sol}(T)\)，由 E4 得
\(\Lambda(t)\in\mathsf{Sol}(S)\)，所以 \(P(S)\)。

两种情形均成立，故由良基归纳得到 (B)。其中 E1--E3 保证使用的是实际、确定且合法
绑定的对象；E4 完成解提升；E5 允许归纳；R 保证目标仍在归纳量词域内。

## 六、FAMILY_EMPTY 的正确加入方式

对域 \(D\)，定义域级命题

\[
Q(D):
\Longleftrightarrow
\forall S\in\mathscr U,\quad
\operatorname{Legal}_D(S)
\Longrightarrow
\mathsf{Sol}(S)\ne\varnothing.
\]

若

\[
\operatorname{VerifyEmpty}(D,c)=1,
\]

则

\[
\forall S\in\mathscr U,\quad
\neg\operatorname{Legal}_D(S),
\]

从而 \(Q(D)\) 真空成立。这里没有把任何无解对象加入
\(\mathscr S_D\)。因此点态存在性结论 (B) 仍只对 live-state 集合
\(\mathscr S_D\) 发表。

## 七、负控

以下构造必须拒绝：

1. **终止/后继同时命中：** 给出 terminal 解和 successor，若
   \(\operatorname{VSucc}\) 未检查非终止门，验证器必须失败；
2. **空哨兵：** 把一个 \(S_\varnothing\in\mathscr S_D\) 声明为
   FAMILY_EMPTY 且 \(\mathsf{Sol}(S_\varnothing)=\varnothing\)；
3. **单点 lift：** \(\mathsf{Sol}(T)=\{0,1\}\)、\(\mathsf{Sol}(S)=\{0\}\)，
   只证明 \(0\) 可提升而未证明 \(1\)；
4. **source swap：** 将 E1 绑定从 \(S_0\) 换成另一个方程接口不同的 source；
5. **target swap：** 将 E2 计算出的 \(T_0\) 替换为同 owner 但编码不同的 \(T_1\)；
6. **势坐标 swap：** 在不同边使用不同的 \((\pi_1,\ldots,\pi_7)\) 顺序；
7. **缺失 R：** 将 target 写入队列但 target 不属于 \(\mathscr S_D\)。

## 八、完成证据

命题从 OPEN_PROPOSITION 改为 ESTABLISHED 前，必须提交：

* 七个 \(\pi_i\) 的全局 schema、算法和语义；
* live-state 与 family-level 义务的类型定义；
* terminal verifier 可靠性证明；
* VSucc 非终止门和 target 唯一性证明；
* E1--E5/R 的结构字段与可靠验证规则；
* 正式良基归纳证明；
* 上述七类负控的可重放结果。

本命题是共享逻辑基础，不会单独关闭任何具体 F1、F2、F3 residual 或 T6。
