---
kind: claim
claim_id: odd-distance-even-source-r-state-invariance
title: 奇距离偶源递降的 r 状态不变性
statement: 对固定核心素数 p，任意满足 p-c=d(1+cr)、dr=-1 mod4 的偶源兼容射线均有 M1=(rp+1)/4。因此尾部平方因子条件 e1|M1^2、e1<=M1、e1=-M1 mod r 只依赖于 r，不依赖于产生该 r 的距离 c 或源因子 d；同一 r 的所有射线同时命中或同时失败，并共享目标三元组与 Type I 证书。
claim_status: established
topics:
- type-I
- descent
- even-source
- state-compression
- divisor-residues
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-certificate-reconstruction
visibility: public
last_checked: '2026-07-25'
---

# 奇距离偶源递降的 r 状态不变性

对固定 \(p\)，任取奇距离偶源的兼容参数

\[
p-c=d(1+cr),\qquad dr\equiv-1\pmod4,\qquad
k=\frac{dr+1}{4},\qquad M_1=k(1+cr).
\]

由源端恒等式直接得到

\[
4M_1=(dr+1)(1+cr)=rp+1,\qquad
M_1=\frac{rp+1}{4}. \tag{1}
\]

故一旦 \(p,r\) 固定，\(M_1\) 已完全固定。尾部条件

\[
e_1\mid M_1^2,\qquad e_1\le M_1,\qquad e_1\equiv-M_1\pmod r \tag{2}
\]

只读取 \((r,M_1)\)，与表示该状态的 \(c,d\) 无关。任何满足 (2) 的 \(e_1\) 给出相同的
\(u,v\)、同一目标三元组 \((pM_1,u,v)\) 和同一 Type I 证书；不同射线仅有首项不同的源解。

因此偶源搜索应先按 \(r\) 合并，而不是将每个距离都当作独立尾部问题。第四压力点的
33 条兼容射线压缩为 22 个 \(r\) 状态：15 个字符型、6 个有限积集型、1 个命中；
其中 \(r=23\) 同时由距离 \(29,4037,6901\) 产生，但三者共享同一个失败尾部状态。

这仍不控制一般 \(p\) 的 \(r\) 状态数或状态大小；它只消除了同一 \(r\) 的完全重复，
并把下一步聚焦为不同 \(r\) 状态之间的关系。

第四压力点的首个命中实际上发生在最小可用的 \(r=15\) 状态，而非大尾模数，见
[第四压力点的最小偶源尾模数](type-II-h19-fourth-even-source-small-r-boundary.md)。

## 重建

~~~bash
python3 reproductions/type_ii_h19_fourth_even_source_r_state_profile.py
python3 -m unittest tests/test_type_ii_h19_fourth_even_source_r_state_profile.py -q
~~~
