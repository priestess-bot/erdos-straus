---
kind: claim
claim_id: type-I-dyadic-pminusone-profile-100k
title: 十万前缀的完整二幂p减一桥因子对剖面
statement: 对p≤100009的1181个核心素数，穷尽每个由2≤t≤2v2(p-1)-2允许的二幂桥E=2^t，以及K=((2^t-1)p+1)/4的全部因子对BC|K。1087个获得p-1严格偶源最大尾边，94个遗漏；已选指数分布为t=2:605、3:332、4:116、5:22、6:8、8:2、9:2，最大允许指数22而最大实际选中9。故完整二幂p-1子族覆盖92.04%，但不能独立闭合该前缀。
claim_status: computationally_reproduced
topics:
- type-I
- normal-form
- descent
- even-source
- source-state
- factorization
- dyadic
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 十万前缀的完整二幂 p 减一桥因子对剖面

对每个 \(p\le100009\)、\(p\equiv1\pmod{24}\)，枚举所有由源平方条件允许的

\[
2\le t\le2v_2(p-1)-2,
\]

并在

\[
K_t=\frac{(2^t-1)p+1}{4}
\]

中穷尽所有 \(BC\mid K_t\)，以[二幂桥 p 减一源判据](type-I-dyadic-p-minus-one-factor-pair-selector.md)
检查严格偶源 \(n=p-1\) 边。

| 项目 | 数值 |
|---|---:|
| 核心素数 | 1,181 |
| 二幂 \(p-1\) 桥命中 | 1,087 |
| 遗漏 | 94 |
| 覆盖率 | 92.04% |
| 最大允许 \(t\) | 22 |
| 最大实际选中 \(t\) | 9 |

按最小选中指数，命中数为

\[
t=2:605,\quad3:332,\quad4:116,\quad5:22,\quad6:8,\quad8:2,\quad9:2.
\]

完整允许更高指数只比 \(t\le6\) 多释放 4 点；94 个遗漏的前五个为

\[
241,\ 2089,\ 3049,\ 4729,\ 5209.
\]

因此二幂 \(p-1\) 桥是强且高度结构化的分支，却不是全称选择器。特别地，继续增加可允许
二幂指数并不能消除主要残余；后续必须合并其他源距离、非二幂桥或不同保留坐标。

可复现命令：

~~~bash
python3 reproductions/type_i_dyadic_pminusone_profile_100k.py
python3 -m unittest tests/test_type_i_dyadic_pminusone_profile_100k.py -q
~~~
