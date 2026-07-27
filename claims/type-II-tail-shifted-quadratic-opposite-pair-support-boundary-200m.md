---
kind: claim
claim_id: type-II-tail-shifted-quadratic-opposite-pair-support-boundary-200m
title: 两亿平移平方尾的反向除子对支持度边界
statement: 对两亿范围65条最小偏移平移平方尾射线，完整枚举所有兼容k及完整尾后，最小反向普通除子对支持度分布为1:7、2:24、3:26、4:4、5:3、6:1。故单素因子选择器只命中7条、至多双素因子选择器只命中31条；p=6294649的该最小偏移射线至少需要6个不同的有符号素因子坐标。
claim_status: computationally_reproduced
topics:
- type-I
- descent
- external-source
- divisor-residues
- factorization
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--3
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 两亿平移平方尾的反向除子对支持度边界

对每条已闭合的最小偏移射线，令完整尾为 $f\mid L^2$ 且
$f\equiv-L\pmod t$。将 $f/L$ 写成最简有符号指数商 $a/b$，则

$$
a,b\mid L,\qquad a\equiv-b\pmod t.
\tag{1}
$$

定义此对的支持度为 $a/b$ 的素因子分解中指数非零的不同素数数目。这正是
[反向普通除子对判据](shifted-quadratic-tail-opposite-divisor-pair.md)的有符号指数盒坐标数，
并非另一种近似搜索。

对两亿范围65条零偏移遗漏的最小可用偏移，完整枚举该偏移所有兼容
$k\mid(p-s)/4$，并对每个 $k$ 完整枚举已验证的 $f\mid L^2$。最小支持度分布为

$$
1:7,\qquad2:24,\qquad3:26,\qquad4:4,\qquad5:3,\qquad6:1.
\tag{2}
$$

所以单坐标反向对只覆盖 $7/65$ 条，至多两坐标只覆盖 $31/65$ 条。即使限制到25条
在最小偏移上平方尾必要的射线，其分布仍为

$$
2:2,\qquad3:15,\qquad4:4,\qquad5:3,\qquad6:1.
\tag{3}
$$

另一方面，普通除子残数集超过单位群一半即强制含有反向对。这个半密度充分条件在65条
射线中直接闭合42条，在25条平方必要射线中仍闭合7条；其余23条才是真正的低密度压力集。
因此它提供了可推广的第一层选择器，但不能取代多坐标指数盒分析。
把环境进一步缩小到 $L$ 的素因子实际生成的单位子群也没有增加命中：同样仍为42条。
对失败射线，计算在该子群大小已严格超过普通除子残数数目的两倍时终止，故这不是因大群
枚举截断而漏报的潜在半密度命中。

最强的有限范围反例是

$$
p=6{,}294{,}649,\quad s=25,\quad k=65{,}569,\quad t=10{,}491,
$$

其最小支持度为6；一条最短见证的有符号坐标为

$$
5\cdot7\cdot17\equiv-(19\cdot29\cdot37)\pmod{10{,}491}.
\tag{4}
$$

两边均为 $L$ 的普通除子。该射线的完整尾因子为
$f=481{,}828{,}025$，故 (4) 由实际的严格递降证书实现，而不是抽象单位群构造。

这排除的是在这些**最小偏移射线**上限制为至多五种素因子坐标的内层选择器；它不排除
更大偏移存在低支持度见证，也不证明任意 $L,t$ 的支持度无界。其作用是把下一步理论
目标准确定位为多坐标有界指数乘积盒，而不是单因子、双因子或饱和子群判据。

可复现命令：

~~~bash
python3 reproductions/type_ii_tail_shifted_quadratic_opposite_pair_profile.py
python3 -m unittest tests/test_type_ii_tail_shifted_quadratic_opposite_pair_profile_200m.py -q
~~~
