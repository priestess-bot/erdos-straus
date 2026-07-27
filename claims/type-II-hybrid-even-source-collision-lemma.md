---
kind: claim
claim_id: type-II-hybrid-even-source-collision-lemma
title: 标准源、偶源与 Type II 射线的联合有限碰撞引理
statement: 令 p=1 mod24，B=(p-1)/4，n_k=p-B/k（k|B），m_c=p-c（c 为正奇数），r_s=p+4s。则 gcd(n_k,m_c) 整除 (4k-1)c+1，gcd(m_c,r_s) 整除 c+4s，且对 c!=d 有 gcd(m_c,m_d) 整除 |c-d|。结合已有标准源--射线和射线--射线界，任何有限的尺度、奇距离和移位集的全部公因子都来自显式有限常数的素因子；剥离它们后，各对象的私有部分两两互素。
claim_status: established
topics:
- descent
- external-source
- even-source
- type-II
- factorization
- gcd
- collision
- proof-program
sources:
- paper: bradford2024
  locator: "Propositions 1 and 3"
  role: external-source-and-certificate-context
visibility: public
last_checked: '2026-07-25'
---

# 标准源、偶源与 Type II 射线的联合有限碰撞引理

## 记号与结论

令 \(p\equiv1\pmod {24}\)，

\[
B=\frac{p-1}{4},\qquad
n_k=p-\frac Bk,\qquad
m_c=p-c,\qquad
r_s=p+4s,
\]

其中 \(k\mid B\)、\(c\) 为正奇数、\(s\ge1\)。除已有的
[多源--射线有限碰撞分解](multisource-descent-collision-lemma.md) 外，混合第二层偶源时有

\[
\gcd(n_k,m_c)\mid(4k-1)c+1, \tag{1}
\]
\[
\gcd(m_c,r_s)\mid c+4s, \tag{2}
\]
\[
\gcd(m_c,m_d)\mid |c-d|\quad(c\ne d). \tag{3}
\]

所以对任何有限尺度集 \(K\)、奇距离集 \(C\)、移位集 \(S\)，把下列常数的全部素因子
从所有相应的 \(n_k,m_c,r_s\) 中剥离：

1. \(|k-\ell|/\gcd(k,\ell)\)；
2. \(|4s(4k-1)-1|\)；
3. \(|s-t|\)；
4. \((4k-1)c+1\)；
5. \(c+4s\)；
6. \(|c-d|\)。

剩下的私有部分两两互素。该有限碰撞集合只依赖 \(K,C,S\)，不依赖 \(p\)。

## 证明

由 \(4kn_k=(4k-1)p+1\)，若 \(g\mid n_k\) 且 \(g\mid m_c=p-c\)，则

\[
(4k-1)p+1-(4k-1)(p-c)=(4k-1)c+1
\]

被 \(g\) 整除，得到 (1)。同样，若 \(g\mid p-c\) 且 \(g\mid p+4s\)，则

\[
(p+4s)-(p-c)=c+4s
\]

给出 (2)；两个偶源之差直接给出 (3)。已有引理分别给出标准源--标准源、
标准源--射线、射线--射线三类界。任意两个对象的公因子因而都只含上述六类常数中的
素因子；剥离全部这些素因子便得到两两互素的私有部分。

注意这是一条**状态压缩**引理。集合 \(K,C,S\) 增长时碰撞素数集也可增长，故它不提供
固定参数的全称选择器，也不自动构造任何 Type I/II 因子。

## 十亿压力点审计

对 H19 完整平方因子递降遗漏的四个点，取其已验证的偶源距离
\((7,3,3,34091)\)，再将 \(s=1,\ldots,19\) 与每点的纯新 Type II 备用射线一同纳入：

| \(p\) | \(c\) | 备用 \(s\) | 备用新因子 | \(\gcd(p-c,p+4s)\) |
|---:|---:|---:|---:|---:|
| 35,840,809 | 7 | 45 | 31,139 | 1 |
| 132,285,169 | 3 | 27 | 107 | 1 |
| 141,326,089 | 3 | 63 | 83 | 1 |
| 640,775,689 | 34,091 | 45 | 359 | 1 |

逐点将 \(c+4s\) 和所有射线差的素因子剥离后，偶源与 20 条射线的私有部分全都两两互素。
因此该压力集没有“偶源与其备用新因子射线共享大公因子”的桥接现象。特别是第四点的长距离
偶源与 \(s=45\) 的 \(359\) 因子射线也互素；要证明选择器，必须使用剥离后私有因子的
除子残数、证书同余或一个真正的状态递降，而不能只搜索共享因子。

重建：

~~~bash
python3 reproductions/type_ii_h19_hybrid_even_source_collision.py
python3 -m unittest tests/test_type_ii_h19_hybrid_even_source_collision.py -q
~~~

该审计依赖
[二层自适应偶源严格递降闭合](type-II-h19-adaptive-even-source-descent.md) 与
[短证书或严格递降混合闭合](type-II-h19-hybrid-short-or-descent.md) 的存储见证。
