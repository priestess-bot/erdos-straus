---
kind: claim
claim_id: type-II-h19-fourth-even-source-quadratic-character-profile
title: H19 十亿第四压力点平方尾障碍的二次角色化
statement: 对 p=640775689 的23条偶源平方尾子群--字符型失败射线，每一条都存在由 r 的素数 CRT 分量上的 Legendre 角色乘积构成的二次角色，该角色在 M1 的所有素因子上取1、在目标 -M1 mod r 上取-1；没有高阶角色余项。因此此压力点的字符型分支可完全化为显式二次角色兼容性问题。
claim_status: computationally_reproduced
topics:
- type-I
- type-II
- descent
- even-source
- quadratic-characters
- subgroup
- divisor-residues
- finite-audit
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-divisor-criterion
visibility: public
last_checked: '2026-07-25'
---

# H19 十亿第四压力点平方尾障碍的二次角色化

对 [平方尾子群--积集分流](type-II-h19-fourth-even-source-subgroup-profile.md) 中的每条
子群--字符型失败射线，令 \(S\) 是 \(r\) 的某些互异素因子组成的集合，并定义

\[
\chi_S(u)=\prod_{\ell\in S}\left(\frac{u}{\ell}\right). \tag{1}
\]

逐条穷尽 \(r\) 的 CRT 二次角色后，23 条失败全部存在 \(S\) 使

\[
\chi_S(q)=1\quad(q\mid M_1),\qquad
\chi_S(-M_1)=-1. \tag{2}
\]

因此这些射线的平方尾目标不可能由 \(M_1^2\) 的除子达到，且分离不需要高阶角色。

| 子群--字符型射线 | 二次角色可分离 | 高阶角色余项 |
|---:|---:|---:|
| 23 | 23 | 0 |

例如距离 \(c=6901\) 的 \(r=23\) 射线由单个 Legendre 角色
\(\left(\frac{\cdot}{23}\right)\) 分离。唯一子群指数为 \(24\) 的
\(c=2103\) 射线也已有二次分离支撑 \(\{3,37\}\)。

这不是对一般偶源扇的二次角色定理；它只说明当前压力点的字符分支可直接转化为 23 组
有限的二次同余约束。下一步应检验这些约束能否在同一个 \(p\) 的兼容射线间长期共同维持，
而不是预先引入更高阶角色技术。

## 重建

~~~bash
python3 reproductions/type_ii_h19_fourth_even_source_quadratic_character_profile.py
python3 -m unittest tests/test_type_ii_h19_fourth_even_source_quadratic_character_profile.py -q
~~~
