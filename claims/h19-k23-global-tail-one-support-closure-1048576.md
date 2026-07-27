---
kind: claim
claim_id: h19-k23-global-tail-one-support-closure-1048576
title: H19-k23 全局尾菜单的单新增因子有限闭合
statement: 在 H19-k23 的 1,048,576 层全局尾闭合中，原有 5,254 条重写记录都可用 72 个全局尾中的一个规范 Type II 证书完成；2,512 条只用规范基底，2,742 条只需一个非基底素因子，零条需要两个或更多。原先的 40 条二缺陷记录均通过严格更大的全局尾重写为零或一缺陷。
claim_status: computationally_reproduced
topics:
- type-II
- descent
- p-minus-one
- global-tail-menu
- factor-support
- h19
- computation
sources:
- paper: bradford2024
  locator: Proposition 2
  role: ordinary-Type-II-tail-context
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 全局尾菜单的单新增因子有限闭合

全局闭合产物给出 \(5\,254\) 条需要从共享缺口改写到全局尾的记录。其中

\[
2\,497_{\delta=0}+2\,717_{\delta=1}+40_{\delta=2}=5\,254. \tag{1}
\]

这里的 \(\delta\) 是相对于该尾的规范全局基底，命中平方根补全除子所需的非基底素因子
个数。对每条 \(\delta=2\) 记录，按 72 个 \(m+1\mid165600\) 的全局尾严格递增枚举；
在每个尾上穷尽规范基底乘积与至多一个新增素因子的候选，并逐项复核平方根补全条件。

40 条均有成功的更大尾。将它们替换后，全部重写记录的分布为

\[
5\,254=2\,512_{\delta=0}+2\,742_{\delta=1}, \tag{2}
\]

无 \(\delta\ge2\) 记录。连同直接全局证书，有限层的完整闭合可写为

\[
2\,270\,418=2\,265\,164_{\text{direct global}}
+5\,254_{\text{rewritten, }\delta\le1}+0_{\text{misses}}. \tag{3}
\]

这次重写实际新增使用 \(119,143,183\) 三个全局尾；重写部分的完整尾频数为

\[
\begin{aligned}
&3730_{31}+734_{35}+279_{39}+280_{47}+153_{59}+45_{71}+13_{79}\\
&\quad+2_{91}+8_{95}+2_{99}+2_{119}+3_{143}+2_{159}+1_{183}=5\,254. \tag{4}
\end{aligned}
\]

40 条的迁移按 \((m_{\rm old},m_{\rm new},\delta_{\rm new})\) 汇总为

\[
\begin{array}{c|c}
(m_{\rm old},m_{\rm new},\delta_{\rm new}) & \text{条数}\\ \hline
(35,39,1),(35,47,0) & 1,1\\
(39,47,0),(39,47,1),(39,59,0),(39,59,1),(39,71,0),(39,95,1) & 2,8,2,1,1,1\\
(47,59,0),(47,59,1),(47,71,0),(47,95,1) & 6,2,1,1\\
(59,99,1) & 1\\
(71,79,0),(71,79,1),(71,143,1) & 2,1,3\\
(79,95,1),(79,119,1),(79,183,1) & 2,1,1\\
(91,95,1),(95,119,1) & 1,1.
\end{array} \tag{5}
\]

这是一个有限、确定性的支持度下降现象：每个原二缺陷实例至少有一个严格更大的全局尾使
\(\delta\le1\)。它**不是**“全局单新增因子选择器”的证明，原因有二：审计只覆盖给定的
1,048,576 层参数范围，且这里只处理了原有二缺陷记录，没有证明任意未来参数的任意失败
都会落入这种可下降的类别。当前可证明边界因此从“固定菜单内有限样本的 \(\delta\le2\)”
推进到“允许向后换尾时有限样本的 \(\delta\le1\)”。

可复现命令：

~~~bash
python3 reproductions/h19_k23_global_tail_one_support_closure.py \
  --input reproductions/h19-k23-full-global-tail-closure-1048576.json \
  --output reproductions/h19-k23-global-tail-one-support-closure-1048576.json
python3 -m unittest tests/test_h19_k23_global_tail_one_support_closure.py -q
~~~
