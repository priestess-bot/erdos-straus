---
kind: claim
claim_id: h19-k23-global-tail-base-only-descent-1048576
title: H19-k23 全局尾菜单的规范基底压力集
statement: 在 H19-k23 的 1,048,576 层全局尾单新增因子闭合中，5,254 条重写记录有 5,242 条可在某个更大的全局尾使用规范基底零缺陷证书闭合；其余 12 条均来自共享缺口 27、当前尾 31、35 或 39，并在完整 72 尾全局菜单中均不存在规范基底零缺陷证书。
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

# H19-k23 全局尾菜单的规范基底压力集

先使用 [全局尾菜单的单新增因子有限闭合](h19-k23-global-tail-one-support-closure-1048576.md)
将全部 5,254 条重写记录降至规范缺陷 \(\delta\le1\)。其中

\[
2\,512_{\delta=0}+2\,742_{\delta=1}=5\,254. \tag{1}
\]

对 2,742 条仍为一缺陷的记录，依次测试所有严格更大的全局尾
\[
m+1\mid165600
\]
上的零缺陷规范证书。2,730 条成功，故

\[
5\,254=5\,242_{\text{base-only}}+12_{\text{pressure}}. \tag{2}
\]

这里的 5,242 条包括原有的 2,512 条基底证书和 2,730 条严格后移得到的基底证书。
每个后移证书都重新验算了平方根补全的 Type II 标准形，且新尾严格大于原尾。

对余下 12 条，不仅没有更大尾的零缺陷证书；还逐一穷尽了完整 72 尾菜单，均无任何规范
基底零缺陷证书。它们全部来自原共享缺口 \(27\)，当前全局尾的分布为

\[
9_{m=31}+1_{m=35}+2_{m=39}=12. \tag{3}
\]

因此这是一个真正的**规范基底压力集**，而非按尾递增顺序产生的偶然残余。每条压力记录
仍有已核验的一新增素因子证书；被排除的仅是“在某个全局尾完全不用新增素因子”的路线。

这项结论不意味着 12 个具体核心素数就是原猜想的困难反例，更不构成无限参数范围的结论。
它仅在 H19-k23、给定有限参数层、以及由最大仿射不变量定义的规范基底框架内成立。它把
下一步理论工作精确集中到两条路线：

1. 解释这 12 个压力记录的一新增因子为何必然可控或可提升；
2. 证明任意未来的一缺陷记录都会在某个尾进入基底闭合，或者识别新的无限压力类。

可复现命令：

~~~bash
python3 reproductions/h19_k23_global_tail_base_only_descent.py \
  --input reproductions/h19-k23-full-global-tail-closure-1048576.json \
  --one-support reproductions/h19-k23-global-tail-one-support-closure-1048576.json \
  --output reproductions/h19-k23-global-tail-base-only-descent-1048576.json
python3 -m unittest tests/test_h19_k23_global_tail_base_only_descent.py -q
~~~
