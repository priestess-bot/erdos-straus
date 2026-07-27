---
kind: claim
claim_id: two-source-full-tail-size-obstruction
title: 双完整外部源尾的点态大小障碍
statement: 对核心素数 p、任一静态来源 n_k 和任意静态来源 n_l,n_m，保留项 1/(k n_k) 后的剩余倒数严格大于 1/(c n_l)+1/(d n_m)，其中 c,d 是任意正整数。因此 4/n_k 不可能写成 1/(k n_k)+1/(c n_l)+1/(d n_m)。该结论逐点成立，不要求倍率或尾分母随参数统一。
claim_status: established
topics:
- descent
- external-source
- multisource
- size-obstruction
- unit-fractions
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: external-source-descent-context
visibility: public
last_checked: '2026-07-25'
---

# 双完整外部源尾的点态大小障碍

## 定理

令 \(p\equiv1\pmod{24}\) 是素数。对任何使下式为整数的正尺度 \(j\)，记

\[
q_j=4j-1,\qquad
n_j=\frac{q_jp+1}{4j}. \tag{1}
\]

任取这样的 \(k,l,m\) 及正整数 \(c,d\)，都有

\[
\frac4{n_k}
\ne
\frac1{k n_k}+\frac1{c n_l}+\frac1{d n_m}. \tag{2}
\]

这不依赖于 \(c,d\) 如何随 \(p\) 或其它状态选择。

## 证明

由 (1) 也可写成

\[
n_j=p-\frac{p-1}{4j}.
\]

故 \(n_j\ge n_1=(3p+1)/4\)。于是任意两条完整来源尾的倒数和满足

\[
\frac1{c n_l}+\frac1{d n_m}
\le\frac1{n_l}+\frac1{n_m}
\le\frac8{3p+1}. \tag{3}
\]

另一方面，保留第一项后的准确残差为

\[
\frac4{n_k}-\frac1{k n_k}
=\frac{4k-1}{k n_k}
=\frac{4q_k}{q_kp+1}. \tag{4}
\]

而

\[
\frac{4q_k}{q_kp+1}>\frac8{3p+1}
\quad\Longleftrightarrow\quad
q_k(p+1)>2, \tag{5}
\]

后式因 \(q_k\ge3\) 而成立。式 (3) 和 (4) 不可能相等，故得到 (2)。

## 含义

这个障碍强于“固定或仿射尾倍率”限制：即使 \(c,d\) 每个参数点都重新选择，只要两条
尾仍是完整外部来源分母的正整数倍，大小已经不足以补足残差。

因此，多源双尾方案必须至少对某个来源作因子拆分、允许小于来源的分母，或使用不同于
保留 \(1/(k n_k)\) 的首项结构。它与
[双源仿射尾倍率刚性障碍](two-source-affine-tail-rigidity.md) 共同说明，来源之间的
可行耦合不能只是把整个 \(n_j\) 直接放入一条或两条尾。

## 有限交叉核对

`reproductions/two_source_full_tail_size_obstruction.py` 对
\(p\le10000\) 的 143 个核心素数和其全部 2,425 个静态尺度状态使用精确有理数核对
(5)。重建：

```bash
python3 reproductions/two_source_full_tail_size_obstruction.py
python3 -m unittest tests/test_two_source_full_tail_size_obstruction.py -q
```

## 范围

该结果不排除使用来源分母的真因子、同时混合其它分母、改变保留首项或非线性变换的递降。
它只排除最直接的“两条完整来源尾”构造。
