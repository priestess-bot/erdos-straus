---
kind: claim
claim_id: h19-k23-global-tail-pressure-extension-2097152
title: H19-k23 全局尾规范基底压力集的二百万层扩展
statement: H19-k23 的2,097,152层审计含4,466,959条实际素数记录，均有普通双尾递降且均能在72尾全局菜单闭合。9,825条全局重写记录经后移后全部降至至多一个新增素因子，其中9,803条可进一步降至规范基底零缺陷，余22条在完整72尾菜单中均无规范基底零缺陷证书。先前1,048,576层的12条压力记录全部保留，新增10条，因此压力集不是固定的12个例外。
claim_status: computationally_reproduced
topics:
- type-II
- descent
- p-minus-one
- global-tail-menu
- canonical-base
- pressure-set
- h19
- computation
sources:
- paper: bradford2024
  locator: Proposition 2
  role: ordinary-Type-II-tail-context
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 全局尾规范基底压力集的二百万层扩展

将共享选择器的每条残存进程从 \(2^{20}\) 扩展到 \(2^{21}=2\,097\,152\) 个参数层，得到

\[
4\,466\,959
\]

条实际素数记录。确定性 64 位素性检验、完整因子分解和全部合法除子检查均成功；最小共享
缺口仍不超过 \(99\)，没有共享选择器遗漏。普通 Type II 双尾闭合亦无遗漏：

\[
4\,466\,959
=4\,457\,153_{\text{shared-gap}}
+9\,806_{\text{alternative}}+0_{\text{misses}}. \tag{1}
\]

把这些记录放入共同因子 \(165600\) 给出的完整 72 尾全局菜单后，

\[
4\,466\,959
=4\,457\,134_{\text{direct global}}
+9\,825_{\text{rewritten global}}+0_{\text{misses}}. \tag{2}
\]

重写部分的首次规范缺陷为

\[
9\,825=4\,670_{\delta=0}+5\,087_{\delta=1}+68_{\delta=2}. \tag{3}
\]

全部 68 条二缺陷记录均可严格后移到一个至多一缺陷的全局尾，故

\[
9\,825=4\,697_{\delta=0}+5\,128_{\delta=1}. \tag{4}
\]

对后者逐条穷尽严格更大的全局尾的零缺陷证书；若仍失败，再穷尽完整 72 尾菜单。结果是

\[
9\,825=9\,803_{\text{base-only}}+22_{\text{pressure}}. \tag{5}
\]

22 条压力记录都仍有已核验的一新增素因子证书，但对每一条，72 个全局尾均不存在相对于
该尾规范基底的零缺陷证书。它们的当前尾与原共享缺口分布为

\[
11_{31}+6_{35}+3_{39}+1_{59}+1_{71}=22, \tag{6}
\]

\[
21_{\text{shared }27}+1_{\text{shared }51}=22. \tag{7}
\]

比较上一层的 12 条压力记录可得：旧集合是新集合的真子集，新增十条，分别落在
\(m=31,35,39,59,71\) 的当前尾。因此“压力集只是有限且固定的 12 个异常点”已经被这次
严格扩展否定。它不证明压力集无界，也不产生原猜想的反例；它只排除了以一份固定、有限的
例外清单结束全局尾方案的研究策略。

当前正向问题因而更清楚：需要一个能处理不断出现的一新增因子压力记录的结构引理，或一条
把它们归约为真正可提升的下降状态的机制。继续增加静态规范基底、固定尾或有限变量因子
模板都不能替代该引理。

可复现命令：

~~~bash
python3 reproductions/h19_k23_shared_selector_audit.py \
  --parameter-limit 2097152 --gap-cap 239 --workers 14 --compact \
  --output reproductions/h19-k23-shared-selector-audit-2097152.json
python3 reproductions/h19_k23_shared_selector_tail_descent_closure.py \
  --input reproductions/h19-k23-shared-selector-audit-2097152.json \
  --output reproductions/h19-k23-shared-selector-tail-descent-2097152.json
python3 reproductions/h19_k23_full_global_tail_closure.py \
  --input reproductions/h19-k23-shared-selector-tail-descent-2097152.json \
  --output reproductions/h19-k23-full-global-tail-closure-2097152.json
python3 reproductions/h19_k23_global_tail_one_support_closure.py \
  --input reproductions/h19-k23-full-global-tail-closure-2097152.json \
  --output reproductions/h19-k23-global-tail-one-support-closure-2097152.json
python3 reproductions/h19_k23_global_tail_base_only_descent.py \
  --input reproductions/h19-k23-full-global-tail-closure-2097152.json \
  --one-support reproductions/h19-k23-global-tail-one-support-closure-2097152.json \
  --output reproductions/h19-k23-global-tail-base-only-descent-2097152.json
~~~
