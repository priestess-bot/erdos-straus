---
kind: claim
claim_id: h19-k23-m35-m39-selector-boundary
title: H19-k23 的 m=35 未命中到 m=39 平滑基底边界
statement: 在524288层 H19-k23 原m=27替代记录的334个m=35支持度至多二的未命中中，全部14条进程满足40|p-1。允许m=39的完整2,5平滑基底扩展后，零条由基底独立闭合；155条由基底加一个新增素数幂闭合，9条需两个不同新增素因子，余170条在完整m=39扫描中失败而首次转到m=47,59,63,71,79，频数为116,45,3,4,2。
claim_status: computationally_reproduced
topics:
- type-II
- descent
- divisor-selection
- factor-support
- smooth-numbers
- h19
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-certificate-context
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 的 \(m=35\) 未命中到 \(m=39\) 平滑基底边界

考察前一层 \(m=35\) 固定、一新增和二新增支持度均未命中的 334 条记录。所有 14 条
仿射进程都满足

\[
40\mid p-1. \tag{1}
\]

故 \(m=39=4\cdot10-1\) 对每条都可用。令

\[
u=\frac{p+39}{40},\qquad x=10u.
\]

普通 Type II 双尾证书的精确条件为

\[
1\le d\le10u,\qquad d\mid100u^2,\qquad d\equiv-10u\pmod {39}. \tag{2}
\]

## 为什么须保留平滑基底扩展

这里 \(q=10\)，所以 \(q^2=2^2 5^2\)。与此前 \(u\) 具有固定额外因子的层不同，
\(u\) 本身的 \(2\) 与 \(5\) 进位也会进入 \(100u^2\)。因此先完整允许

\[
d=2^a5^b,\qquad
0\le a\le2+2v_2(u),\quad 0\le b\le2+2v_5(u), \tag{3}
\]

再按真正不同于 \(2,5\) 的新增素因子数目增加支持度。这个定义避免把基础素数的高次幂
错误归为“新因子”。

## 524,288 层边界

在 334 条输入中，(3) 本身零命中。加入一个新增素数幂后有 155 条命中；再允许两个
不同新增素因子后增加 9 条，得到

\[
334=155_{\text{one new prime}}+9_{\text{two new primes}}+170_{\text{no }m=39}. \tag{4}
\]

170 条的第一次成功尾缺口为

\[
116_{47}+45_{59}+3_{63}+4_{71}+2_{79}. \tag{5}
\]

故 \(m=39\) 同样否定了固定平滑基底选择器，却保留了强烈但有限的低支持度现象。
这不是对任意 H19 参数的支持度上界；170 个残余已经排除了本层的零、一、二新增素因子
模型。

重建命令：

~~~bash
python3 reproductions/h19_k23_m35_m39_selector_profile.py \
  --input reproductions/h19-k23-shared-selector-tail-descent-524288.json \
  --output reproductions/h19-k23-m35-m39-selector-profile-524288.json
python3 -m unittest tests/test_h19_k23_m35_m39_selector_profile.py -q
~~~
