---
kind: claim
claim_id: odd-distance-even-source-tail-gap-normalization
title: 奇距离偶源平方尾与 Type I 缺口的精确归一化
statement: 设 M=(rp+1)/4，若兼容 r-偶源的平方尾因子 e|M^2 满足 e=-M mod r，则 g=(4e+1)/r 和 x=(M+e)/r=(p+g)/4。反之 e=(rg-1)/4。因此给定兼容源时，平方尾命中与 Type I 缺口可互相恢复，余下的证书条件是相应 d e|x^2 整除。
claim_status: established
topics:
- type-I
- descent
- even-source
- tail
- normalization
- selector
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-certificate-reconstruction
visibility: public
last_checked: '2026-07-25'
---

# 奇距离偶源平方尾与 Type I 缺口的精确归一化

设 \(p\equiv1\pmod{24}\)、\(r\equiv7\pmod8\)，并写

\[
M=\frac{rp+1}{4}.
\]

兼容偶源的平方尾条件要求某个 \(e\mid M^2\) 满足

\[
e\equiv-M\pmod r.
\]

因为 \(4M\equiv1\pmod r\)，这等价于 \(4e+1\equiv0\pmod r\)。定义

\[
g=\frac{4e+1}{r}.
\]

则

\[
\frac{M+e}{r}
=\frac{rp+1+4e}{4r}
=\frac{p+g}{4}. \tag{1}
\]

右端正是 Type I 证书在缺口 \(g\) 的首分母。反向也无损：

\[
e=\frac{rg-1}{4}. \tag{2}
\]

若兼容因子对的另一参数为 \(d\)，完整源--目标提升还要求
\(de\mid x^2\)，其中 \(x=(p+g)/4\)；这正是恢复 Type I 除子
\(x^2/(de)\) 的整除条件。

所以后续选择器不必把“尾部残数命中”和“短 Type I 缺口”当作两种不同现象。可等价地
寻找一个 \(r\)、一个缺口 \(g\)，使 (2) 是 \(M^2\) 的合适因子并满足兼容因子对及
\(de\mid x^2\)。四个 H19 压力见证分别给出
\[
(r,g)=(103,983),(31,191),(31,11),(15,375).
\]

## 重建

~~~bash
python3 reproductions/type_ii_h19_pressure_tail_gap_normalization.py
python3 -m unittest tests/test_type_ii_h19_pressure_tail_gap_normalization.py -q
~~~
