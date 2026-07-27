---
kind: claim
claim_id: h19-k23-m63-global-tail-replacement-1048576
title: H19-k23 非全局 m=63 尾的全局尾替换
statement: 在1048576层 H19-k23 的m=27替代尾规范缺陷审计中，全部6条首尾缺口m=63记录可改由全局可用的m=71或m=79普通 Type II 双尾证书闭合，规范支持缺陷仍至多2。14条进程的共同p-1因子为G=165600；64<m+1<=96的全部全局候选恰为72,80,92,96，对应m=71,79,91,95。替换后全部5081条m=27替代记录只使用全局尾31,35,39,47,59,71,79,91,95，精确缺陷分布为2420条0、2630条1、31条2、零遗漏。
claim_status: computationally_reproduced
topics:
- type-II
- descent
- p-minus-one
- affine-progressions
- factor-support
- h19
sources:
- paper: bradford2024
  locator: Proposition 2
  role: ordinary-Type-II-tail-context
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 非全局 \(m=63\) 尾的全局尾替换

对 14 条进程 \(p=At+C_i\)，一个普通双尾分母 \(d=m+1\) 对每条进程、每个参数
都可用，当且仅当

\[
d\mid G:=\gcd(A,C_1-1,\ldots,C_{14}-1). \tag{1}
\]

这里精确计算得

\[
G=165\,600=2^5\cdot3^2\cdot5^2\cdot23. \tag{2}
\]

故在非全局 \(m=63\) 之后、到已有末端 \(m=95\) 为止，全部全局普通尾候选是

\[
72,80,92,96\mid G,
\qquad m=71,79,91,95. \tag{3}
\]

这不是选择性的列表：它是 (1) 的完整约数枚举。

## 六条替换

规范支持缺陷审计中有六条首尾为 \(m=63\) 的 \(m=27\) 替代记录。按 (3) 依次检查
全局尾，并重新穷尽规范基底下的零、一、二新增素因子除子，结果如下。

| \(p\) | 原 \(m=63\) 缺陷 | 首个全局替换尾 | 新缺陷 | 替换除子 |
|---:|---:|---:|---:|---:|
| 508413877101691201 | 2 | 71 | 0 | 729 |
| 1048100016305102401 | 1 | 71 | 1 | 1028 |
| 132377066501040001 | 1 | 71 | 1 | 1676 |
| 131928382120896001 | 1 | 71 | 2 | 1911564 |
| 1573755934151361601 | 1 | 79 | 1 | 3225800 |
| 1442610094472107201 | 1 | 71 | 1 | 2196 |

第五条在 \(m=71\) 没有缺陷至多二的除子，但在紧随其后的全局 \(m=79\) 命中；其余五条
在 \(m=71\) 已命中。故不存在留下的非全局尾例外。

## 纯全局链

将这六条替换并入 [规范支持缺陷审计](h19-k23-m27-canonical-support-defect-1048576.md)，
全部 5,081 条记录仅使用

\[
\{31,35,39,47,59,71,79,91,95\} \tag{4}
\]

这些全局可用尾，且

\[
5\,081=2\,420_{\delta=0}+2\,630_{\delta=1}+31_{\delta=2}
+0_{\text{misses}}. \tag{5}
\]

这是有限 H19-k23 样本上的纯全局尾闭合，不是对任意核心素数或任意参数的证明。它的价值在于
把下一步理论问题从“处理某个分支特有尾”收缩为：能否在固定的全局尾菜单中证明规范缺陷
至多二，或在更深样本中找到首个失效点。

重建命令：

~~~bash
python3 reproductions/h19_k23_m63_global_tail_replacement.py \\
  --input reproductions/h19-k23-canonical-tail-support-defect-1048576.json \\
  --output reproductions/h19-k23-m63-global-tail-replacement-1048576.json
python3 -m unittest tests/test_h19_k23_m63_global_tail_replacement.py -q
~~~
