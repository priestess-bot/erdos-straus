# SP-09：high-support \(C>1\) empty-improvement 二分

**状态：** OPEN_PROPOSITION
**研究任务：** 对规范高支撑 \(2\le C\le p-1\) 状态的 empty-improvement 补集给出全称闭合。
**独立性：** 本文件自包含定义 source、candidate、势函数和闭合判据，前提只来自本文定义。

## 1. 背景

固定 \(p\equiv1\pmod{24}\) 素数，令
\(B_p=(p-1)^2/4\)。状态是带规范编码和 parent 谱系的
\((p,R,K,A,C,\phi)\)，满足

\[
4K=pR+1,\qquad R>p,\qquad K=AC,\qquad A>B_p,\qquad 2\le C\le p-1.
\]

actual 表示 \(\phi\) 从根或已验证前驱到当前编码；terminal-first-surviving 表示
一个在证明中完整列出的有限 terminal predicate 列表全部 MISS。协议相位固定为
\[
\mathrm{CHARGED}>\mathrm{PRE}>\mathrm{ABSORB}>\mathrm{RESET},
\]
并作为规范状态字段进入固定势函数。
terminal 是 \(4/p\) 的正整数三分母解，FAMILY_EMPTY 是对当前参数域无合法元组的
全称证明。

同一 chart 的“improvement candidate”是一个由 source 规范编码、合法 divisor
occurrence 和确定映射产生的 target，其最终合法 endpoint 的 cofactor
严格小于 \(C\)，且 target 仍满足统一状态方程。定义
\(\mathcal I(S)\) 为所有符合这些条件的 source-bound candidates 的集合。

注意：形式上存在 \(c\mid C\) 并不等于 source 中存在可消费的 raw occurrence；
bounded carry、中间对象或 transient rechart 也不自动成为 candidate。

## 2. 待证明命题

对每个上述状态 \(S\)，证明：

\[
\boxed{
\mathcal I(S)\ne\varnothing
\Longrightarrow
\text{按唯一规则选出一个 strict successor 或 terminal};
}
\]

\[
\boxed{
\mathcal I(S)=\varnothing
\Longrightarrow
\text{S 有 direct terminal、family-empty 证明，或进入更低 protocol/outer-rank domain}.
}
\]

第二个蕴含是本命题的核心。禁止把 empty improvement 写成“再试一次同样 carry”；
必须给出真正的 terminal、empty 或已定义的 phase/protocol drop。

## 3. 必须使用的固定势

定义一个固定
\[
\Pi(S)=(\rho,\Phi,\Psi,r_1,r_2,r_3,r_4)\in\mathbb N^7
\]
及其字典序。这里
\(\rho,\Phi,\Psi,r_1,r_2,r_3,r_4\) 必须是在全部合法状态上定义的七个固定总函数，
并在证明中公布各自算法和语义；不能按边改变。任何 successor 必须证明
\(\Pi(T)<_{\mathrm{lex}}\Pi(S)\)，比较 source 与最终 admitted target，
而不是 source 与中间 carry 对象。

若 proposed target 进入 ABSORB，必须明确 phase order；若从 ABSORB 回到
CHARGED，除非 outer \(\rho\) 严格下降，否则该边不合格。

## 4. 已知障碍必须纳入命题

证明者必须处理以下反例机制：

* 任意长的 \(C=2\) carry stutter；
* 任何保持某个辅助整数不变、或只用 total cofactor 重新参数化的变换，都必须直接
  证明最终 cofactor 和固定势下降，不能因变换名称而假设下降；
* 令 \(\operatorname{spf}(C)\) 为 \(C\) 的最小素因子；
  \(A\mapsto A\operatorname{spf}(C)\) 的 arithmetic saturation 不一定来自合法
  determinant occurrence；
* full q-excess block 指某个素数 \(q\) 在待消费整数中的指数严格超过其在 \(K\)
  中的指数所得完整 \(q\)-幂块；消费它可能 rechart，不能假设 same-chart；
* 外部 full-excess rechart 可能仍是 CHARGED overflow，不能凭 local drop 入队。

这些是需要被定理排除或吸收的情况，不是可忽略的实现细节。

## 本文件中的 E-stage 词义

E1 读取真实 source candidate occurrence；E2 固定唯一 improvement target；
E3 通过固定 target schema、分类规则和准入谓词；E4 对所有解给出 lift；
E5 比较最终 target 与 source 的固定 \(\mathbb N^7\) 势；R 证明 target re-entry。
候选集合为空不是 E1--E5 的替代品。

## 5. 完成证据

须给出：

1. \(\mathcal I(S)\) 的可计算定义和有限性；
2. candidate 之间的唯一 tie-break；
3. empty-improvement complement 的 terminal/empty/lower-protocol partition；
4. 每条实际 successor 的 E1--E5、固定 admission、re-entry；
5. 对 carry stutter、source swap、transient target、ABSORB upward edge 的反控。

若结果只得到“所定义候选集为空”，而没有补集分类，命题未完成。
