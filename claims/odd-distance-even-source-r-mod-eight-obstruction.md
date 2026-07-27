---
kind: claim
claim_id: odd-distance-even-source-r-mod-eight-obstruction
title: 核心偶源递降的 r 模八必要条件
statement: 对 p=1 mod24 的奇距离偶源参数 p-c=d(1+cr)、c 为奇数、dr=-1 mod4，必有 r=7 mod8。因此 r=3 mod8 的状态不可能含有兼容偶源，不论平方尾是否命中。
claim_status: established
topics:
- type-I
- descent
- even-source
- congruences
- state-compression
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-certificate-reconstruction
visibility: public
last_checked: '2026-07-25'
---

# 核心偶源递降的 \(r\) 模八必要条件

令 \(p\equiv1\pmod{24}\)，并有奇距离偶源参数

\[
p-c=d(1+cr),\qquad c\equiv1\pmod2,\qquad dr\equiv-1\pmod4. \tag{1}
\]

由标准恒等式，\(d\equiv1\pmod4\)、\(r\equiv3\pmod4\)，且

\[
M_1=\frac{(cr+1)(dr+1)}4=\frac{rp+1}{4}. \tag{2}
\]

其中 \((dr+1)/2\) 是偶数，故 \(M_1\) 是偶数。于是 \(8\mid rp+1\)。又
\(p\equiv1\pmod8\)，所以

\[
r+1\equiv rp+1\equiv0\pmod8,
\]

即

\[
r\equiv7\pmod8. \tag{3}
\]

因此对于核心类，原本写作 \(r\equiv3\pmod4\) 的搜索可无损缩小为
\(r\equiv7\pmod8\)。这只消除了不可能的源端状态；它不保证其余状态存在同余因子对，
也不保证 \(M_1^2\) 的平方尾命中。

第四压力点的全枚举提供交叉核对：\(r=3,11\) 均无兼容源，\(r=7\) 首次出现源，
而 \(r=15\) 首次尾部成功。十亿四点的首成功 \(r=103,31,31,15\) 也全为
\(7\pmod8\)。

## 重建

~~~bash
python3 reproductions/type_ii_h19_pressure_small_r_profile.py
python3 reproductions/type_ii_h19_fourth_even_source_small_r_boundary.py
python3 -m unittest tests/test_type_ii_h19_pressure_half_factor_pairs.py -q
~~~
