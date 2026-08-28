# SP-06：post-G/C9 连续路径的总分派命题

**状态：** OPEN_PROPOSITION
**研究任务：** 构造并证明 q=1 G 根之后的一族有限整数变换对其全部定义域具有终端、空域或严格后继的总分派。
**独立性：** 本文件自定义 post-G 状态、路径字和闭合结果；每项前提均在本文明示。

## 1. 自包含背景

固定素数 \(p\equiv1\pmod{24}\)，定义
\(B_p=(p-1)^2/4\)。状态是带唯一规范编码的整数元组
\[
S=(p,R,K,A,\sigma,\lambda),
\]
其中 \(\sigma\) 是有限附加数据，\(\lambda\) 是父谱系。Type-I 算术条件为

\[
4K=pR+1,\qquad R>p,\qquad A\mid K,\qquad A>B_p.
\]

令 \(C=K/A\)。actual 表示 \(\lambda\) 从根初始化器或已验证前驱逐步到达当前规范
编码；persistent 表示状态满足一个在证明开始前固定的合法性谓词并可再次被同一
选择器消费。附加数据只有在固定正规形谓词验证后才有意义。

terminal certificate 是正整数三元组直接满足 \(4/p=1/x+1/y+1/z\)。
terminal-first schedule 是有限有序 terminal 谓词列表，首个 HIT 抢先；只有全部
MISS 才能执行非终止变换。

ordinary q=1 G 根定义为 \(p=24t+1\)、\(q=1\)，且
\[
X=(p+3)/4=6t+1
\]
的每个素因子都为 \(1\pmod3\)。

post-G 路径是一个待构造的有向有限词：

\[
G\to\text{full-carrier root}\to\text{first Type-I child}
\to\text{second anchor}\to d=1\text{ relay}\to C2/H4/C9.
\]

这行不是对外部路线的引用，而是五个未知映射的命名：
\[
F_G,\ F_{\mathrm{child}},\ F_{\mathrm{anchor}},\
F_{d=1},\ F_{\mathrm{out}}.
\]
本命题的存在量词要求证明者给出每个 \(F\) 的完整整数公式、定义域、终端分支、
唯一 tie-break 和输出正规编码。full-carrier 只表示 \(K\) 使用 source 规范编码中
全部被指定的素因子幂；first child 和 second anchor 分别表示第一次和第二次应用
相应公布映射；\(d=1\) relay 表示该映射的 divisor 参数固定为 1。
atomic 表示有限映射序列的中间对象不可持久化；overflow 表示 target 满足 \(R>p\)。

每个箭头都必须由一个确定整数投影给出；不能把“可能继续”当作边。
允许的最终结果只有：

* TERMINAL：给出 \(4/p\) 的直接三分母解；
* FAMILY_EMPTY：在当前精确 domain 上证明不存在该分支；
* VERIFIED_SUCCESSOR：具备 E1--E5 和 re-entry 的 persistent target。

为避免依赖未定义路线，C2、H4、C9 只是下列构造变量的名称：

* \(P_{2}(S)\)：归一化容量参数等于 2 的状态；
* \(P_{4}(S,w)\)：存在一个有限 word \(w=(F_1,\ldots,F_4)\)，每个 \(F_i\)
  是证明者必须构造并公布的整数映射，且每个中间对象有规范编码；
* \(P_{9}(S)\)：证明者必须构造并公布的有限余项方程族，其 \(R\)-参数取
  \(23,35,11\)。

因此本命题是构造存在命题：必须同时构造 \(F_i\)、\(P_2,P_4,P_9\)、所有 guard、
target 公式和证明证书。名称本身不携带任何结论。

## 2. 必须作为同一证明的子命题

以下每项都属于本命题，不是外部已知事实：

1. q=1 immediate \(C=1\) 子族为空；
2. \(P_2\) 中不满足证明者明列的 19-phase 同余条件的子域为空；
3. 低 post-G chart 要么终端化，要么有限次 support doubling 后进入 \(A>B_p\)
   overflow；
4. 四步 word 的 guard DAG 算术输出属于 atomic 或 overflow 形状；
5. \(P_9\) 中某个明确的 \(R=23\) 算术射线是固定尾 terminal，且射线公式必须在
   同一证明中公布。

这些事实必须在同一证明中完成，不能替代所有剩余 row 的 source coverage 或固定准入。

## 3. 待证明命题

对每个 actual ordinary q=1 G source 及其所有 post-G descendants，证明存在一个
确定、互斥、穷尽的分派：

\[
\boxed{
\mathscr S_{\mathrm{postG}}
=\mathscr T\ \dot\cup\ \mathscr E\ \dot\cup\ \mathscr V,
}
\]

其中 \(\mathscr T\) 是直接三分母 terminal states，\(\mathscr E\) 是由全称矛盾
证明为空的参数域，\(\mathscr V\) 是带完整 E1--E5/R 的 successor states。

分派必须覆盖：

* first child 的奇偶两支；
* second anchor 的所有由规范编码重算的分类；
* \(d=1\) relay 的 terminal 和 nonterminal 分支；
* C2/H4 atomic、overflow 和 C9 的所有 row；
* 已在同一证明中处理的固定尾 terminal 之外的其余 \(R=23,35,11\) 行；
* target terminal-first、公共合法性验证和最终 re-entry。

## 4. 证明结构

证明者应按以下顺序建立：

1. 给出 source domain 的 exact quantifier，不得只写“post-G survivor”；
2. 证明每个 guard leaf 互斥且穷尽；
3. 为每个 nonterminal leaf 给出 source occurrence、完整 parent 编码和 terminal certificate；
4. 给出唯一 target 映射和 canonical tie-break；
5. 从 target 规范编码重新计算分类值和合法性谓词，不继承构造器自报字段；
6. 给出 universal solution lift；
7. 用固定 \(\Pi\in\mathbb N^7\) 比较 source 与最终 target，而非 checkpoint；
8. 证明 target 再进入同一 domain。

## 5. 关键反控

~~~text
把 G root arithmetic formula 当作 post-G actual source；
把一个 \(P_9\) fixed-tail 结果外推到其他 R；
把四步/容量八中间对象当作 persistent target；
把 support-doubling 次数当作全局 E5；
遗漏 first-child parity 或 d=1 relay 分支；
target 分类不经固定分类函数；
terminal hit 与后继构造同时命中时让后继构造先执行。
~~~

## 本文件中的 E-stage 词义

E1 是 actual source、parent 和 occurrence 的可重放谱系；E2 是唯一 target map；
E3 是固定 schema、分类函数、合法语法与准入谓词；E4 是对全部目标解的 lift；E5 是固定
\(\mathbb N^7\) 势的 parent-to-final 严格下降；R 是 target 回到同一 selector domain。
七个势坐标必须是全部合法状态上的固定总函数，算法和顺序在证明中公布。
任何只给局部算术或字符串 label 的结果都不满足这些定义。

## 6. 完成证据

须交付一个逐 leaf 表格，列出 predicate、closure、E1--E5、re-entry 和反控；
所有 row 的 open count 为零；至少一条 nonterminal row 必须形成可独立重放的
VERIFIED_SUCCESSOR。只有这样才算证明本命题，而不是只增加一个局部整数恒等式。
