---
kind: claim
claim_id: two-source-affine-tail-rigidity
title: 双外部源仿射尾倍率的刚性障碍
statement: 令 p(t) 为非恒定正仿射进程，k!=l 为使 n_j=((4j-1)p+1)/(4j) 整值的静态尺度。不存在非恒定正整值仿射 c(t) 与正整值 v(t)，使 4/n_k=1/(k n_k)+1/(c(t)n_l)+1/v(t) 对全部参数成立。结合固定倍率障碍，这排除该双源单尾模板的全部仿射倍率；唯一的有理比例例外会给出 v=l n_l/(4l-1)，但它永不为整数。
claim_status: established
topics:
- descent
- external-source
- multisource
- rigidity
- affine-arithmetic
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: external-source-descent-context
visibility: public
last_checked: '2026-07-25'
---

# 双外部源仿射尾倍率的刚性障碍

## 定理

令 \(p(t)\) 是非恒定正整值仿射函数，取两个不同的正尺度 \(k\ne l\)，并令

\[
q_j=4j-1,\qquad
n_j(t)=\frac{q_jp(t)+1}{4j}. \tag{1}
\]

假设 \(n_k,n_l\) 在整个进程上皆为整数。不存在非恒定、最终为正的整值仿射函数
\(c(t)\)，以及正整数函数 \(v(t)\)，使

\[
\frac4{n_k(t)}
=\frac1{k n_k(t)}
+\frac1{c(t)n_l(t)}
+\frac1{v(t)} \tag{2}
\]

对每个充分大的参数 \(t\) 成立。

## 证明

记

\[
M(t)=k n_k(t)=\frac{q_kp(t)+1}{4},
\qquad
N(t)=n_l(t)=\frac{q_lp(t)+1}{4l},
\qquad q=q_k. \tag{3}
\]

由 (2) 必有

\[
v(t)=\frac{c(t)M(t)N(t)}{D(t)},
\qquad D(t)=c(t)qN(t)-M(t). \tag{4}
\]

\(M,N\) 是不成比例的一次式。若 \(c\) 非恒定，则 \(D\) 是二次式。对
\(\mathbb Q[t]\) 作带余除法；如果 \(D\) 不整除 \(cMN\)，余项次数小于二。
沿每个使商多项式具有固定分数部的参数同余类，余项除以无界的 \(D(t)\) 趋于零，
却又等于整数减去该固定分数部，只能恒为零。因此

\[
D\mid cMN\quad\text{于 }\mathbb Q[t]. \tag{5}
\]

若 \(c\) 不与 \(M\) 成比例，则 \(D\) 在 \(c,M,N\) 的任一零点都不为零：
在 \(c\) 或 \(N\) 的零点，\(D=-M\)；在 \(M\) 的零点，\(D=cqN\)。
所以 \((D,cMN)=1\)，与 (5) 矛盾。

故只能有 \(c=\lambda M\)，其中 \(\lambda\in\mathbb Q_{>0}\)。此时

\[
D=M(\lambda qN-1). \tag{6}
\]

第二个一次因子与 \(N\) 互素；由 (5) 它必须与 \(M\) 成比例。写

\[
\lambda qN-1=\mu M. \tag{7}
\]

比较 (3) 中 \(p\) 的系数和常数，唯一得到

\[
\lambda=\frac{l}{k-l},\qquad
\mu=\frac{q_l}{k-l}. \tag{8}
\]

正性迫使 \(k>l\)。把 (8) 代回 (4)：

\[
v(t)=\frac{\lambda}{\mu}N(t)
=\frac{l\,n_l(t)}{4l-1}. \tag{9}
\]

但是

\[
4l\,n_l(t)-(4l-1)p(t)=1, \tag{10}
\]

故 \((n_l(t),4l-1)=1\)；又 \((l,4l-1)=1\)。于是
\(4l-1\nmid l n_l(t)\)，和 \(v(t)\in\mathbb N\) 矛盾，证毕。

## 与固定倍率的合并

[固定尾分母的双源严格提升刚性障碍](two-source-fixed-tail-rigidity.md) 已排除
\(c(t)=c\) 为固定正整数的情形。本定理排除所有非恒定仿射倍率。因此最直接的双源
模板

\[
(k n_k,\ c(t)n_l,\ v(t))
\]

在仿射层面没有任何严格提升边；多源路线若要继续，必须同时改变两个尾结构、使用
非仿射因子，或离开单尾形式 (2)。

## 符号交叉核对

`reproductions/two_source_affine_tail_rigidity.py` 在 H19-k23 的一个代表性
静态进程及尺度集

\[
\{1,2,3,4,5,6,8,9,10,12,15,23\}
\]

上检查 132 个有序尺度对。66 个 \(k>l\) 对具有 (8) 所给的正有理比例例外；
每一个都由 (9) 的非整数尾排除。重建：

```bash
python3 reproductions/two_source_affine_tail_rigidity.py
python3 -m unittest tests/test_two_source_affine_tail_rigidity.py -q
```

## 范围

该结果不排除两条或三条尾分母同时依赖多个来源的耦合，不排除非仿射选择器，也不排除
新的非线性提升恒等式。它只把“让第二来源以仿射倍率充当单条尾”这一最自然升级完整排除。
