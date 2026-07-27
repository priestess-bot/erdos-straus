---
kind: claim
claim_id: type-II-h19-pressure-even-source-overflow-profile
title: H19 十亿压力偶源尾的最小 Type I 溢出剖面
statement: 在十亿 H19 剖面的四个标准递降压力点上，首个小 r 偶源状态的全部平方尾命中分别有5、18、12、12个；每个状态均含有目标除子溢出 B=1 的 Type I 正规形。故这些实际补救不需要目标除子相对其首分母的素因子指数溢出，但此有限事实不构成变量 r 的零溢出选择器定理。
claim_status: computationally_reproduced
topics:
- type-I
- even-source
- normal-form
- overflow
- selector
- finite-audit
- pressure-family
- h19
sources:
- paper: bradford2024
  locator: Proposition 1
  role: even-source-descent
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization
visibility: public
last_checked: '2026-07-26'
---

# H19 十亿压力偶源尾的最小 Type I 溢出剖面

设兼容偶源尾状态满足

\[
M=\frac{rp+1}{4},\qquad e\mid M^2,\qquad e\equiv-M\pmod r.
\]

令

\[
g=\frac{4e+1}{r},\qquad x=\frac{M+e}{r}=\frac{p+g}{4}.
\]

因为 \((r,M)=1\) 且 \(e\mid M^2\)，有 \((r,e)=1\)。由 \(rx=M+e\) 得
\(M\equiv rx\pmod e\)，进而 \(e\mid x^2\)。又 \(4e+1=rg\) 给出
\(e\equiv-1/4\pmod g\)。所以每个偶源尾因子都是缺口 \(g\) 的合法 Type I 目标除子。
它诱导的精确正规形溢出为

\[
B(e;x)=\frac{e}{(e,x)}.
\]

这把偶源尾的选择转成可比较的状态势量：在固定 \((p,r)\) 上，对所有尾命中取最小 \(B\)。

对十亿 H19 剖面中四个标准递降压力点的首个小 \(r\) 状态，精确枚举结果如下：

| (p) | (r) | 尾命中数 | 最小 (B) | 取到 (B=1) 的个数 |
| ---: | ---: | ---: | ---: | ---: |
| 35,840,809 | 103 | 5 | 1 | 1 |
| 132,285,169 | 31 | 18 | 1 | 2 |
| 141,326,089 | 31 | 12 | 1 | 2 |
| 640,775,689 | 15 | 12 | 1 | 4 |

因此四个已知压力补救均有零溢出尾。它比“存在小 \(r\) 命中”更精确，但绝不能外推为全称：
固定 \(r\) 上界已知会遗漏 H19 残余，而当前审计仅覆盖四个被标准递降遗漏的压力点。

下一条可能的正向定理应是变量状态的：长期逃过标准递降时，是否必存在某个兼容 \(r\) 使
最小尾溢出 \(B=1\)，或至少使 \(B\) 的素支撑/大小受控到可构造递降。这一问题保留了
距离可增长的自由度，也比固定距离或固定 \(r\) 的选择器更符合现有边界。

可复现命令：

~~~bash
python3 reproductions/type_ii_h19_pressure_even_source_overflow_profile.py \
  --input reproductions/type-ii-h19-pressure-small-r-1b-results.json \
  --output reproductions/type-ii-h19-pressure-even-source-overflow-profile-1b-results.json
python3 -m unittest tests/test_type_ii_h19_pressure_even_source_overflow_profile.py -q
~~~
