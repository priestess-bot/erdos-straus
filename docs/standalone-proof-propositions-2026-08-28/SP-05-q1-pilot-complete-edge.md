# SP-05：q=1 phase-root 首条完整活动边

**状态：** OPEN_PROPOSITION
**目标：** 将一个 ordinary q=1 G 根变成一条真正具备 E1--E5 和 re-entry 的非终止边。
**独立性：** 本文件重新定义根、投影、解集和证书；任何外部实现结果只能作为动机，不能作为前提。

## 0. 状态与证明术语

状态是一个有唯一规范编码的有限整数对象，至少包含 \(p,q,R,K\) 和 equation
interface \(4/p\)。根初始化器是一个从 \(p\) 唯一产生 source 状态、且不消费前驱的
可验证函数。actual source 是根初始化器的输出或一条逐步验证的 parent-target 链的末端；
persistent 表示该状态通过固定合法性谓词并可被同一选择器再次消费。

terminal certificate 是正整数 \((x,y,z)\) 满足
\[
\frac4p=\frac1x+\frac1y+\frac1z.
\]
terminal-first schedule 是有限有序 terminal 谓词列表，首个 HIT 必须先于任何后继构造。

本文件使用：

* E1：actual parent 谱系和 source 编码中 \(q=1\) 的整数位置；
* E2：由冻结公式唯一重算 target；
* E3：target 通过固定 schema、正规形、分类函数和合法性谓词；
* E4：对全部 target 解成立的 \(\mathsf{Sol}(T)\to\mathsf{Sol}(S)\) 映射；
* E5：一个全局固定 \(\Pi:\mathscr S\to\mathbb N^7\) 的严格字典序下降；
* R：target 仍属于 \(\mathscr S\) 并由相同选择器再次消费。

\(\Pi=(\pi_1,\ldots,\pi_7)\) 的每个坐标必须是全部合法状态上的总函数；证明必须
公布各坐标算法、语义和固定顺序。

## 1. 背景和状态定义

设 \(p=24t+1\) 是素数，并令

\[
X=6t+1=\frac{p+3}{4}.
\]

称根为 ordinary q=1 G，若 \(q=1\)，且 \(X\) 的每个素因子都同余
\(1\pmod3\)。字母 G 在本文中只表示这个明确的因子条件。
根状态 \(S\) 的方程接口是

\[
\mathsf{Eq}(S):\quad \frac4p,
\]

其解集为

\[
\mathsf{Sol}(S)=
\{(x,y,z)\in\mathbb N_{>0}^3:4/p=1/x+1/y+1/z\}.
\]

定义 phase-root 投影的整数

\[
R=16t+3,\qquad K=X(16t+1).
\]

直接计算给出

\[
4K=pR+1.
\]

并且若 \(M=R-1=16t+2\)，则 \(\gcd(M,K)=1\)：先有
\(\gcd(M,16t+1)=1\)，再用
\(\gcd(M,X)\mid 3M-8X=-2\) 和 \(X\) 为奇数。

根和 phase-root target 都表示同一个 \(4/p\) 解集；因此目标端的 universal lift
候选是恒等映射，但必须在最终证书中明确写出其定义域和值域。

## 2. source terminal-first 前提

在根端固定六个 gap

\[
\mathcal M_{23}=\{3,7,11,15,19,23\}
\]

对每个 \(m\) 令 \(x_m=(p+m)/4\)，并对每个 \(d\mid x_m^2\) 检查
\[
\mathrm{TypeI}(p,m,d)\Longleftrightarrow m\mid px_m+d,
\]
\[
\mathrm{TypeII}(p,m,d)\Longleftrightarrow
d\le x_m\land m\mid x_m+d.
\]
命中时必须用本文件第 0 节的 terminal 定义验证相应三分母公式。
只有六层全 MISS 的状态才能进入本命题的 producer 分支；任一命中都立即返回
terminal。这个前提是 registered-prefix 语义，不是“所有可能 terminal 都不存在”。

source occurrence 必须来自一个明确的根初始化谱系，并在 source 的规范有限编码中含有
精确整数 \(q=1\) 的字段位置。位置、值、父谱系和完整 source 编码必须同时绑定；不能由
数值 \(p\) 事后重建 parent。

## 3. 待证明命题

对每个满足上述根条件、六层 source schedule MISS 且实际初始化谱系成立的 \(S\)，证明
存在唯一 target \(T\) 和一条完整边 \(S\to T\)，满足：

1. **E1：** \(q=1\) occurrence 是 source 编码中真实存在的整数，且 branch、domain、
   parent/root initializer、terminal certificate 和 occurrence path 绑定到同一个 source；
2. **E2：** \(T\) 的整数编码由 \((p,t)\) 唯一计算为 \(R,K\)，不存在调用者提供的
   tie-break 或第二个 target；
3. **E3：** \(T\) 通过本文件第 0 节所要求的固定 schema、正规形、分类和合法性谓词；
4. **E4：** 对每个 \(u\in\mathsf{Sol}(T)\)，恒等映射
   \(\Lambda(u)=u\) 属于 \(\mathsf{Sol}(S)\)；
5. **E5：** 在一个固定的 \(\mathbb N^7\) 势
   \(\Pi=(\rho,\Phi,\Psi,r_1,r_2,r_3,r_4)\) 下，
   \(\Pi(T)<_{\mathrm{lex}}\Pi(S)\)，且比较的是 parent-to-final target；
6. **R：** \(T\) 重新进入同一状态宇宙，并不会停留在未完成的中间对象。

形式上，目标是：

\[
\boxed{
\forall S\in\mathscr S_{q=1,G}^{\mathrm{six\text{-}miss}},
\quad
\operatorname{Terminal}(S)
\lor
\exists!T\in\mathscr S:
S\to T\text{ 满足 E1--E5 与 R}.
}
\]

## 4. 需要分开的 target terminal

phase-root target 必须独立重放：

* 同一个 p-only 六层 Bradford predicate；
* target-specific anchor-sink 条件 \(R-1\mid K\)，其命中时的三分母候选为
  \((K/(R-1),K,pK)\)。

后者恒为 MISS，因为 \(\gcd(R-1,K)=1\)。若未来 target-specific terminal 命中，
必须在接受非终止 target 前返回 source solution 的 terminal lift。
source terminal certificate 不能直接改名成 target terminal certificate。

## 5. 完成证据

必须提供：

* root initializer 到 source 的完整谱系；
* 六层 terminal transcript 和 terminal-preemption 证明；
* \(R,K\) 的代数推导；
* target 分类函数、合法语法和准入谓词的统一定义；
* 恒等 E4 的全称证明；
* 固定 N\(^7\) 势的 parent-to-final 严格比较；
* target terminal、source swap、q-path swap、projection tie-break swap 的负控；
* 独立重放器，不能调用后继构造函数的“已验证”结论。

若只完成代数 \(R,K\) 或一个未完成中间对象，命题仍未完成。只有满足全部条件的
后继构造才能称为活动、已验证 producer。

## 6. 完整 terminal 边界包（2026-08-29）

已合并的 standalone package 给出一项对本命题至关重要、但不构成其闭合的结果：对每个
固定 \(p\)，先执行本文件的 \(M_{23}\) registered prefix，再枚举

\[
\left\lfloor p/4\right\rfloor+1\le x\le\left\lfloor3p/4\right\rfloor
\]

中的排序首分母，并对约分 residual \(a/b\) 穷尽

\[
(ay-b)(az-b)=b^2
\]

的正因子对。这是一个有限 complete terminal decision：其 `MISS_COMPLETE` 当且仅当
\(\mathsf{Sol}(4,p)=\varnothing\)。因此，对于 complete-terminal-first 语义，任何现实的
ordinary \(q=1,G\) nonterminal phase-root edge 都要求一个 Erdős--Straus 反例；再加上
actualness、admission、E1--E5 receipt 和 re-entry authority 后，才有条件性的唯一 edge。

这排除了把 six-gap registered MISS 重命名为 `MISS_COMPLETE` 的做法。特别地，
\(p=21169\) 是 ordinary \(q=1,G\) 且 \(M_{23}\) 全 MISS，但全局 fallback 在

\[
\frac4{21169}=\frac1{5300}+\frac1{3619899}+\frac1{19185464700}
\]

处 terminal-preempt。因此本命题仍是 OPEN_PROPOSITION；当前没有 actual complete-miss
source，也没有 production successor authority。完整证明、两套独立实现和控制位于
`reproductions/sp05_complete_terminal_decision/`，合并复查记录见
`SP-05-complete-terminal-package-review-2026-08-29.md`。这些文件是结果的证据与解释，
不是本 dossier 的隐藏前提。
