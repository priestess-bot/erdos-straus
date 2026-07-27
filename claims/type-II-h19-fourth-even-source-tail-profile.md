---
kind: claim
claim_id: type-II-h19-fourth-even-source-tail-profile
title: H19 十亿第四压力点的源射线与平方尾分离
statement: 对 p=640775689 的完整奇距离偶源扇 c<=34091，恰有33条源端兼容射线、覆盖24个距离；但仅 c=34091 的 d=1253、r=15 射线有任何 M1^2 除子落入目标残数 -M1 mod r。该射线有122个不大于M1的平方尾除子，其中12个命中目标残数，最小为1406。故该压力点的首释放瓶颈在平方尾除子残数，而非源端射线兼容性。
claim_status: computationally_reproduced
topics:
- type-I
- type-II
- descent
- even-source
- divisor-residues
- boundary
- finite-audit
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-certificate-reconstruction
visibility: public
last_checked: '2026-07-25'
---

# H19 十亿第四压力点的源射线与平方尾分离

对

\[
p=640{,}775{,}689,\qquad 1\le c\le34{,}091,\qquad c\equiv1\pmod2
\]

的每个偶源 \(p-c\)，先只检查奇距离偶源定理的源端条件

\[
p-c=d(1+cr),\qquad dr\equiv-1\pmod4.
\]

这产生 33 条兼容射线，分布在 24 个不同距离。也就是说，首释放前并不缺少可提升源的
代数形状。

再对每条射线穷尽

\[
e_1\mid M_1^2,\qquad e_1\le M_1,\qquad e_1\equiv-M_1\pmod r.
\]

33 条射线中只有一条有命中：它恰在

\[
c=34{,}091,\quad d=1253,\quad r=15,\quad s=511{,}366,\quad
k=4699,\quad M_1=2{,}402{,}908{,}834.
\]

该 \(M_1^2\) 有 122 个不大于 \(M_1\) 的除子，其中 12 个落入目标残数；最小的
\(e_1=1406\)，从而恢复此前的严格递降证书。

因此，这个压力点将正向研究问题具体化为：在状态依赖的兼容源射线上，何种跨射线或
乘法结构会强制平方除子残数集命中 \(-M_1\bmod r\)。只扩大源端距离或仅证明存在兼容
\((d,r)\)，不足以推进该点。

其中 \(c,d\equiv1\pmod4\) 的一部分射线可由距离--源因子交换对称性合并；该对称性保持
\(M_1\) 和尾部命中数，却不覆盖实际成功的 \(c=34091\) 射线。因此它是状态压缩规则，
不是本压力点的充分机制，见
[奇距离偶源的距离--源因子交换对称性](odd-distance-even-source-exchange-symmetry.md)。

对 33 条射线进一步按 \(M_1\) 素因子生成子群分流后，32 条未命中中有 23 条是字符型、
9 条是受限指数积集型；因此这两类问题不能由同一条“因子数足够多”引理处理，见
[第四压力点平方尾的子群--积集分流](type-II-h19-fourth-even-source-subgroup-profile.md)。

更基本地，固定 \(p\) 时尾部状态只由 \(r\) 决定。这里 33 条射线仅有 22 个 \(r\) 状态，
故 11 条距离只是同一尾部问题的重复表示，见
[奇距离偶源的 r 状态不变性](odd-distance-even-source-r-state-invariance.md)。
其中首个命中 \(r=15\) 已是该点最小的可用尾模数，说明应优先扫描小 \(r\) 的因子对而非
直接扩大距离，见
[第四压力点的最小偶源尾模数](type-II-h19-fourth-even-source-small-r-boundary.md)。

## 重建

~~~bash
python3 reproductions/type_ii_h19_fourth_even_source_tail_profile.py
python3 -m unittest tests/test_type_ii_h19_fourth_even_source_tail_profile.py -q
~~~
