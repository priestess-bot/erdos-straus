---
kind: claim
claim_id: h19-k23-m31-m35-selector-boundary
title: H19-k23 的 m=31 未命中到 m=35 因子支持边界
statement: 在524288层 H19-k23 原m=27替代记录的723个m=31单新增素数选择器未命中中，全部14条进程仍满足36|p-1和13|(p+35)/36。m=35的固定因子3^4*13^2零命中；387条由固定基底加一个新增素数幂给出Type II双尾，2条需两个不同新增素因子，余334条在完整m=35扫描中失败而首次转到m=39,47,59,63,71,79，频数为164,116,45,3,4,2。
claim_status: computationally_reproduced
topics:
- type-II
- descent
- divisor-selection
- factor-support
- p-minus-one
- h19
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-certificate-context
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 的 \(m=31\) 未命中到 \(m=35\) 因子支持边界

取前一层 \(m=31\) 单新增素数选择器未命中的 723 条原 \(m=27\) 替代记录。14 条
残存仿射进程都满足

\[
36\mid p-1,\qquad 13\mid u=\frac{p+35}{36}. \tag{1}
\]

故 \(m=35=4\cdot9-1\) 是所有这些点共同可尝试的普通双尾缺口。令

\[
x=9u.
\]

与 \(m=31\) 情形相同，\(m=35\) 的 Type II 双尾证书等价于

\[
1\le d\le9u,\qquad d\mid81u^2,\qquad d\equiv-9u\pmod {35}. \tag{2}
\]

这里 \(x\) 与 \(35\) 互素：若 \(r\mid(x,35)\)，则 \(r\mid u\)，而
\(p=36u-35\equiv u\pmod r\)，将迫使小素因子 \(r\) 整除较大的素数 \(p\)。

## 固定基底与支持度

由 (1)，固定因子

\[
H_{35}=3^4\cdot13^2=13\,689\mid81u^2. \tag{3}
\]

先允许 \(d\mid H_{35}\)，再允许

\[
d=h\ell^e,\qquad h\mid H_{35},\quad \ell\notin\{3,13\},\quad
\ell^e\mid(u/13)^2, \tag{4}
\]

最后允许两个不同新增素数的乘积

\[
d=h\ell_1^{e_1}\ell_2^{e_2}. \tag{5}
\]

所有候选仍须满足 (2)。这是逐层增加新增素因子支持度的完整有限审计，不是把
因子分解启发式当作定理。

## 524,288 层边界

固定基底在这 723 条条件性残余上恰为零命中。随后得到

\[
723=387_{\text{one new prime}}+2_{\text{two new primes}}+334_{\text{no }m=35}. \tag{6}
\]

两条需要两个不同新增素因子的 \(m=35\) 点为

\[
p=322\,146\,572\,356\,569\,601,\qquad
p=539\,103\,246\,196\,075\,201. \tag{7}
\]

其余 334 条的第一次成功尾缺口为

\[
164_{39}+116_{47}+45_{59}+3_{63}+4_{71}+2_{79}. \tag{8}
\]

因此，单新增素数机制在 \(m=35\) 层不是全称的，但只出现两个双新增因子例外；334 个
剩余则同时排除了固定、一新与二新支持度的 \(m=35\) 选择器。这个结论只覆盖给定的
有限闭包产物，不能推出任意参数下的统一支持度界。

重建命令：

~~~bash
python3 reproductions/h19_k23_m31_m35_selector_profile.py \
  --input reproductions/h19-k23-shared-selector-tail-descent-524288.json \
  --output reproductions/h19-k23-m31-m35-selector-profile-524288.json
python3 -m unittest tests/test_h19_k23_m31_m35_selector_profile.py -q
~~~
