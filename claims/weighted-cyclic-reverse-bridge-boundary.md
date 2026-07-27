---
kind: claim
claim_id: weighted-cyclic-reverse-bridge-boundary
title: 首个共同递降逃逸点的加权循环三坐标反向桥接边界
statement: 对 p=2451289 的 21 张原始 Type II AC<=14 目标解，以及每个既约权重 0<r<s<=20，加权循环三坐标传输的精确逆像均不含严格整数源 2<=n<p。逆矩阵与最小公倍数判据穷尽了每个固定目标和权重的所有源，故这不是有界源搜索的阴性结果。
claim_status: computationally_reproduced
topics:
- descent
- weighted-transport
- type-II
- reverse-lift
- obstruction
- computation
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 2 and 4
  role: Type-II-certificate-reconstruction
visibility: public
last_checked: '2026-07-25'
---

# 首个共同递降逃逸点的加权循环三坐标反向桥接边界

## 三坐标反演

令 \(q=s-r\)，并把源和目标的倒数向量分别记为 \(t,t'\)。加权循环传输写为

\[
t'=\frac{n}{ps}(rI+qP)t,\qquad P^3=I, \tag{1}
\]

其中 \(P\) 循环移动三个坐标。由于

\[
(rI+qP)^{-1}
=\frac{r^2I-rqP+q^2P^2}{r^3+q^3}, \tag{2}
\]

固定目标三元组和既约权重 \(0<r<s\) 后，任意反向源必满足

\[
t_i=\frac{H_i}{n},\qquad
H=\frac{ps}{r^3+q^3}(r^2I-rqP+q^2P^2)t'. \tag{3}
\]

若任一 \(H_i\le0\)，不存在正源。否则将每个 \(H_i\) 约为 \(u_i/v_i\)，则
所有源分母都必须被

\[
L=\operatorname{lcm}(u_1,u_2,u_3) \tag{4}
\]

整除；反之 \(n=L\) 已给出整数源分母 \(n/H_i\)。因此存在严格源当且仅当
\(L<p\)（另排除 \(n=1\)）。这个判据完整决定固定目标、固定权重下的全部
\(2\le n<p\)，不需要枚举较小实例的埃及分数解。

## 压力点审计

取当前记录的首个共同真实递降逃逸点

\[
p=2{,}451{,}289.
\]

枚举其全部原始 Type II 射线

\[
1\le A,C\le14
\]

并按完整目标三元组去重，得到 21 张目标解。对每张解逐项应用 (3)--(4)，并对所有
既约权重

\[
0<r<s\le20
\]

审计。结果为

\[
\#\{\text{目标解}\}=21,\qquad
\#\{\text{严格加权循环反向源}\}=0. \tag{5}
\]

运行：

```bash
python3 reproductions/weighted_cyclic_reverse_bridge.py \
  --prime 2451289 --ac-bound 14 --weight-denominator-bound 20 \
  --output reproductions/weighted-cyclic-reverse-bridge-2451289-ac14-s20-results.json
```

输出逐证书保存 \(A,C,K\)、目标三元组及每个权重的全部反向命中列表。实现使用
`fractions.Fraction`，并在非空的校准例中重新代入两个埃及分数方程和正向传输：
\(p=31,r/s=1/2\) 恢复源 \(n=15,(4,120,120)\)；
\(p=2161,r/s=1/49\) 恢复完整重复尾审计的源
\(n=1103,(276,608856,608856)\)。

## 研究含义与范围

这严格扩展了只保留两个目标分母的反向桥接边界：这里三个坐标都允许改变，且反演已对
固定的循环零偏移传输穷尽所有严格源。它与重复尾刚性共同表明，继续在小权重循环混合
中调节参数，不能产生独立于 Type II 证书的新递降。

结论不排除 \(A,C>14\)、\(s>20\)、非循环矩阵、带偏移传输，或三项互异且携带额外
因子标记的源状态。后者才是这一方向仍有内容的最小扩展。
