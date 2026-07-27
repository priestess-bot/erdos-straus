---
kind: claim
claim_id: boundary-short-gap-tail-deflation-100k
title: 五亿边界点十万短缺口盒中的规范尾递降边界
statement: 对p=477015289的所有3<=m<=100003、m=3 mod4，完整分解x=(p+m)/4、枚举d|x^2并逐张核验Type I/II证书。共得到125张Type I和86张Type II证书，首张在m=27；125张Type I全部不满足规范p尾去缩放的严格递降条件。因此在该完整十万短缺口盒中，直接证书很多，但没有保持前两项、去缩放p倍尾的严格递降。
claim_status: computationally_reproduced
topics:
- type-I
- type-II
- descent
- finite-audit
- boundary-case
sources:
- paper: bradford2024
  locator: Propositions 1--3
  role: Type-I-and-Type-II-certificate-context
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-27'
---

# 五亿边界点十万短缺口盒中的规范尾递降边界

继续考察当前压力点

$$
p=477{,}015{,}289.
$$

对每一个

$$
3\le m\le100{,}003,\qquad m\equiv3\pmod4,
$$

令 $x=(p+m)/4$，以试除法完整分解 $x$，再枚举所有 $d\mid x^2$。每个候选均显式核验
Type I 或 Type II 的三项单位分数恒等式；这覆盖了 25,001 个缺口而不是只检查已有的
证书路径。

结果如下：

| 项目 | 数值 |
|---|---:|
| Type I 证书数 | 125 |
| Type II 证书数 | 86 |
| 首个有证书缺口 | 27 |
| 可规范尾去缩放的 Type I 数 | 0 |

最后一行对每张 Type I 正规形 $x=ABC$ 计算

$$
R=\frac{4B^2C+1}{m},\qquad R+1\mid4BC(A+B). \tag{1}
$$

它正是“保持前两项、将 $p$-倍尾去缩放”存在严格源的充要条件。因此此边界精确说明：在
该宽短缺口盒中，**直接 Type I/II 证书并不是瓶颈**；125 张 Type I 证书没有一张能按
当前已知的规范尾形状读成严格递降。

这不排除 $m>100003$，也不排除改变保留项、由不同源解重组两尾，或新的提升机制。事实上，
该点在 $m=27$ 的两张非最短证书已通过“保留前两项、替换最大项”的不同形状严格降到偶数源，
见 [gap-27 的二分母保留严格递降](boundary-gap-27-reverse-two-tail-bridge.md)。所以本审计的
准确作用是排除规范 $p$-尾去缩放，而不是宣称短缺口盒完全没有递降。

可复现命令：

~~~bash
python3 reproductions/boundary_gap_certificate_landscape.py \
  --prime 477015289 --gap-cap 100003 \
  --output reproductions/type-i-boundary-short-gap-tail-100k-477015289-results.json
~~~
