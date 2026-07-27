---
kind: claim
claim_id: odd-distance-even-source-fixed-first-tail-completeness
title: 奇距离偶源固定首项的两尾完备性
statement: 在奇距离偶源状态中，若保留源端首分母 dM，则任意正整数两尾分解 4/(p-c)=1/(dM)+1/u+1/v 等价于 (ru-M)(rv-M)=M^2。按 u<=v 取 e=ru-M，恰得到 e|M^2、e<=M、e=-M mod r。因此平方尾条件穷尽所有固定首项的三项源解。
claim_status: established
topics:
- type-I
- descent
- even-source
- egyptian-fractions
- divisor-residues
- rigidity
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-certificate-reconstruction
visibility: public
last_checked: '2026-07-25'
---

# 奇距离偶源固定首项的两尾完备性

在奇距离偶源状态

\[
p-c=d(1+cr),\qquad 4M=rp+1,\qquad (r,M)=1
\]

中，首项 \(1/(dM)\) 被标记提升保留。由源端恒等式，

\[
\frac4{p-c}-\frac1{dM}=\frac rM. \tag{1}
\]

因此任意保留该首项的三项源解都等价于

\[
\frac rM=\frac1u+\frac1v. \tag{2}
\]

清分母后有标准的完全因式分解

\[
(ru-M)(rv-M)=M^2. \tag{3}
\]

反之，(3) 的任意正因子对恢复 (2)。将分母排序为 \(u\le v\)，并令

\[
e=ru-M,
\]

则

\[
e\mid M^2,\qquad e\le M,\qquad e\equiv-M\pmod r, \tag{4}
\]

且

\[
u=\frac{M+e}{r},\qquad v=\frac{M(M+e)}{re}. \tag{5}
\]

这正是平方尾参数化。它说明固定 \(dM\) 时，平方尾不是一类候选，而是全部正整数
两尾分解的精确编码。

故有限积集型状态的高次 \(M^L\) 残数不可能通过“改写后两尾”补救；任何正向构造至少
要改变源端首分母、改变标记提升所保留的坐标，或使用不同的多步机制。

## 重建

式 (3) 是直接整数恒等式；现有偶源完整参数化可由下列复现交叉检查：

~~~bash
python3 -m unittest tests/test_short_certificate.py -q
python3 -m unittest tests/test_type_ii_h19_tail_exponent_rigidity.py -q
~~~
