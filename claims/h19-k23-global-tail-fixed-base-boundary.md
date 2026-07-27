---
kind: claim
claim_id: h19-k23-global-tail-fixed-base-boundary
title: H19-k23 全局尾的固定规范基底覆盖边界
statement: 对 H19-k23 的14条进程，令G=gcd(A,C_i-1)=165600。全部72个满足4q|G的全局普通尾m=4q-1均不存在全参数固定规范基底选择器：若u=(p+m)/(m+1)=at+b_i，g=gcd(a,b_1,...,b_14)，则F=(qg)^2整除每个x^2，但对每个全局尾都存在一条进程和一个参数周期状态，使任何d|F都不能同时满足d<=x及d=-x (mod m)。这排除固定除子基底的全进程证明路线，不排除依赖u的变量因子、子进程选择或仅素数参数的选择器。
claim_status: established
topics:
- type-II
- descent
- affine-progressions
- factor-support
- fixed-divisor
- h19
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-criterion
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 全局尾的固定规范基底覆盖边界

令 14 条残存进程为 \(p=At+C_i\)，并记

\[
G=\gcd(A,C_1-1,\ldots,C_{14}-1)=165\,600. \tag{1}
\]

因此全局可用的普通尾恰由 \(4q\mid G\) 给出，数目为 72。对其中一个尾
\(m=4q-1\)，写

\[
u_i(t)=\frac{At+C_i+m}{4q}=at+b_i,
\qquad g=\gcd(a,b_1,ldots,b_{14}). \tag{2}
\]

则 \(qg\mid x=qu_i(t)\) 对每一条进程、每一个参数成立，故

\[
F=(qg)^2mid x^2. \tag{3}
\]

反过来，若固定整数 \(D\) 对所有参数都整除 \(x^2\)，则对同一分支比较相邻参数可知
\(D\mid\gcd_t x(t)^2=(q\gcd(a,b_i))^2\)，再在全部分支取交，得到 \(D\mid F\)。
所以 (3) 的全部除子已穷尽全参数的固定平方除子，而不是某个预先选定的小基底。

对每个 \(d\mid F\)，只保留 \(d\le x\) 且

\[
d\equiv-x=-qu_i(t)\pmod m. \tag{4}
\]

的候选。目标剩余只随 \(t\bmod m/\gcd(a,m)\) 变化；因此对每条分支检查这个完整周期即可
精确决定是否覆盖所有非负参数。

## 完整边界

脚本枚举了 (1) 的所有 72 个四倍数约数、每个 \(F\) 的全部除子，以及每条分支的完整
最小周期。结果为

\[
72_{\text{global tails}}=0_{\text{fixed-base full covers}}
+72_{\text{tails with an uncovered periodic state}}. \tag{5}
\]

例如当前纯全局链的几个关键尾在分支 \(v\equiv0\pmod{29}\) 已有如下固定基底缺口：

| \(m\) | 未覆盖参数状态 | 目标 \(-x\pmod m\) |
|---:|---:|---:|
| 31 | \(t\equiv0\pmod{31}\) | 11 |
| 39 | \(t\equiv0\pmod{39}\) | 38 |
| 95 | \(t\equiv0\pmod{95}\) | 41 |

这里的参数状态未必给出素数 \(p\)，所以 (5) 不能被误读为“该尾对所有素数参数失败”。
它严格排除的只是更强、也更直接的全参数固定除子证明。要继续推进，必须利用 \(u\) 的
变量素因子、在参数空间中细分进程，或改用不同递降模型。

重建命令：

~~~bash
python3 reproductions/h19_k23_global_tail_fixed_base_boundary.py
python3 -m unittest tests/test_h19_k23_global_tail_fixed_base_boundary.py -q
~~~
