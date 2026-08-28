# SP-07：C8/H4 actual atomic closure

**状态：** OPEN_PROPOSITION
**研究任务：** 对容量八和四步原子变换的全部实际输入构造互斥、穷尽、可递归的终端或严格后继。
**独立性：** 本文件重新定义 C8/H4 parent、capacity 和 atomic 分类；不使用本文未定义的假设。

## 1. 背景与定义

固定素数 \(p\equiv1\pmod{24}\)。状态是带规范编码和 parent 谱系的整数元组
\((p,R,K,A,C,\lambda)\)，满足

\[
4K=pR+1,\qquad K=AC,\qquad A\mid K.
\]

容量八 parent 定义为 \(C=8\) 且 \(\lambda\) 从根或已验证前驱到达当前编码。
所谓四步 parent 是由一个待构造的四步整数 word
\[
w=(F_1,F_2,F_3,F_4)
\]
从 actual source 产生的状态；证明者必须在同一证明中公布每个 \(F_i\) 的公式、
定义域、终端检查和中间编码。H4 只是该四步 word 的简称。

terminal certificate 是 \(4/p\) 的正整数三分母解；terminal-first 是一个明确列出的
有限有序检查列表。actual parent 必须有可重放规范 payload、父谱系和该列表的全部 MISS。
persistent 表示 parent 或 target 满足固定合法性谓词并可由同一选择规则再次消费。

raw occurrence 是 parent 编码中由固定路径解析出的整数 witness。由它计算一个有限
target capacity。容量八 outgoing
按固定优先级分为：

1. terminal hit；
2. optional double-low refinement，即两个明确计算的容量都在 \(\{1,\ldots,7\}\)；
3. second-full-excess OTHER fallback。

atomic target 的 target-local 分类分为：

* TERMINAL：中心 hit；
* F：中心 hit 为空且 \(-1\) 在 target support subgroup 中；
* G：中心 hit 为空且 \(-1\) 不在该 subgroup 中。

F/G 是算术分类名，不自动代表合法 persistent 分类。

这里的 support subgroup 有严格定义：若 target 的有限 support 素数集合为
\(\mathcal Q(T)\)，且 \(R_T\) 是 target 的奇数模数，则
\[
U_{R_T}=(\mathbb Z/R_T\mathbb Z)^\times,\qquad
\langle\mathcal Q(T)\rangle
\]
表示由 \(\mathcal Q(T)\) 在 \(U_{R_T}\) 中的剩余类生成的子群；center hit
是一个由 target payload 明确计算的有限证书集合 \(\mathcal Z(T)\subseteq U_{R_T}\)。
若证明者使用“clean-q、capacity-one 四步子域”，必须把 clean-q 写成具体
gcd/valuation 条件，并把 capacity-one 写成 \(C=1\)；该子域不因名称而为空。

## 2. 可独立使用的算术事实

对某个 C8 \(q_\star=103\) source 子域，定义两条候选整数射线
\[
s_+(v)=189+721v,\quad p_+(v)=9073+34608v,
\]
\[
s_-(v)=704+721v,\quad p_-(v)=33793+34608v.
\]
对相应 \(s=s_\pm(v)\)，定义
\[
q_\star(s)=
\begin{cases}
\min\{q:q\text{ 为素数},\ q\ge7,\ q\mid 6s-1\},
&\text{该集合非空},\\
\infty,&\text{该集合为空}.
\end{cases}
\]
条件 \(q_\star=103\) 精确等价于
\[
103\mid6s-1,\qquad
\ell\nmid6s-1\ \text{对每个素数 }7\le\ell<103.
\]
本命题需要的更强 roughness gate 另行定义为
\[
\operatorname{Rough}_{103}(s)
\Longleftrightarrow
q_\star=103\ \text{且}\ 25\nmid6s-1.
\]
因此 \(25\nmid6s-1\) 是额外的 5-adic 条件，不能被误当作
\(q_\star=103\) 的定义。ordinary-q1-G 定义为
\[
X=(p+3)/4
\]
的每个素因子都为 \(1\pmod3\)。若采用两条射线，必须同时从头证明核心素性、
roughness、ordinary-q1-G 和 parent 谱系；这些条件不是由射线名称自动得到的。
在 second-full-excess fallback 中，若

\[
75C\equiv64\pmod p,\qquad p\ge4129,
\]

则 \(C\notin\{1,\ldots,8,p-1\}\)，故
\(9\le C\le p-2\)。这只证明容量范围，不证明 source actualness。

## 3. 待证明命题

对每一个 actual 容量八或四步 parent 及其每个非 terminal arm，证明以下命题：

\[
\boxed{
\text{parent terminal hit}
\ \lor\
\text{deterministic OTHER target}
\ \lor\
\text{FAMILY\_EMPTY},
}
\]

并且对每个 atomic target：

\[
\boxed{
\text{center hit}
\ \lor\
(-1\in\langle\text{support}\rangle)
\ \lor\
(-1\notin\langle\text{support}\rangle),
}
\]

三者必须对应 TERMINAL、F successor、G successor，且每个 successor
都必须具备：

* actual parent-bound E1；
* deterministic atomic target map/E2；
* 固定 schema、分类、合法语法、admission/E3；
* 对应 equation interface 的 universal E4；
* parent-to-final fixed N\(^7\) E5；
* common re-entry。

## 4. 容量八与四步 word 之间的边界

四步 word 的 clean-q \(C=1\) 子域必须在同一证明中证明为空，且该证明只能关闭
这个精确子域。非 atomic 四步输出、其他容量八 arm、double-low optional branch
仍需分别处理。
C8 的 OTHER fallback 不能依赖 double-low 命中；double-low 只能是同一 MISS
输入上的可选替代。

## 5. 必须证明的独立性

* parent trace 不能由 p 重新生成；
* scheduler 的 terminal MISS 不能来自 caller 字段；
* atomic target 必须重新计算 support subgroup；
* F/G 独立验证器不得调用后继构造函数的内部结论；
* 四步/容量八两个构造函数若不同，必须有不同的规范规则编码；
* target terminal schedule 与 source schedule 必须分别绑定。

## 本文件中的 E-stage 词义

E1 绑定 actual parent 与 raw occurrence；E2 重算 atomic target；
E3 重新通过固定 schema、分类函数、语法和准入谓词；E4 是全称解集 lift；
E5 是固定 \(\mathbb N^7\) 的 parent-to-final 严格下降；R 是 common selector re-entry。
七个势坐标必须是全部合法状态上的固定总函数，算法和顺序在证明中公布。
F/G 分类和 capacity bound 本身都不授予任何 E-stage。

## 6. 控制与完成证据

至少保留一个 TERMINAL、一个 F、一个 G 和一个 malformed/nonactual control。
每个控制都要说明是数学实例还是实际 persistent state。最终交付需包含完整 leaf
分割、E1--E5 证书、独立 replay 和固定准入 trace；仅证明容量
\(9\le C\le p-2\) 不算完成。
