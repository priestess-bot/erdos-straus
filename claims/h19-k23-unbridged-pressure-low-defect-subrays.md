---
kind: claim
claim_id: h19-k23-unbridged-pressure-low-defect-subrays
title: H19-k23 两条无固定桥压力进程各有无穷低缺陷选择器素数子射线
statement: H19-k23 两条没有固定因子外源桥的压力进程各含一条原始仿射子射线，使子射线的每个素数值都具有固定的动态 p-1 Type II 尾证书。第一条取 q=15、d=37845，支持缺陷为1；第二条取 q=8、d=1508258，支持缺陷为2。两条子射线由 Dirichlet 定理各含无穷多个核心素数。这证明动态低缺陷选择器在两个困难进程上都有非平凡无限子族，但不覆盖原进程的全部素数值。
claim_status: established
proof_provenance: mixed
review_status: independent_review
topics:
- type-II
- support-defect
- selector
- affine-progressions
- dirichlet
- h19
- pressure-family
sources:
- paper: bradford2024
  locator: Proposition 2
  role: ordinary-Type-II-tail-context
visibility: public
last_checked: '2026-07-27'
---

# 两条无固定桥压力进程的低缺陷子射线

令 \(P_1,P_2\) 为
[动态选择器接口](dynamic-low-defect-tail-or-external-exit-selector.md)中两条 H19-k23
压力进程的步长。现有 one-factor 周期细化给出

\[
P'_1=29P_1,\qquad P'_2=2089^2P_2.
\]

考虑子射线

\[
p'_1(n)=2\,220\,549\,727\,681\,245\,601+P'_1n,
\qquad
p'_2(n)=748\,375\,048\,866\,405\,601+P'_2n,
\qquad n\ge0.
\]

## 固定见证

对第一条子射线取

\[
q_1=15,\qquad m_1=59,\qquad
d_1=37\,845=3^2\cdot5\cdot29^2.
\]

对第二条子射线取

\[
q_2=8,\qquad m_2=31,\qquad
d_2=1\,508\,258=2\cdot19^2\cdot2089.
\]

对 \(i=1,2\)，置

\[
B_i(n)=\frac{p'_i(n)-1}{4},\qquad x_i(n)=B_i(n)+q_i.
\]

精确整数审计逐项验证

\[
q_i\mid B_i(0),\quad q_i\mid\frac{P'_i}{4},\quad
d_i\mid x_i(0)^2,\quad d_i\mid\frac{P'_i}{4},
\]

以及

\[
x_i(0)+d_i\equiv0\pmod{m_i},\qquad
\frac{P'_i}{4}\equiv0\pmod{m_i},\qquad
d_i\le x_i(0).
\]

因此对每个 \(n\ge0\)，都有

\[
q_i\mid B_i(n),\qquad
d_i\mid x_i(n)^2,\qquad
d_i\le x_i(n),\qquad
d_i\equiv-x_i(n)\pmod{m_i}. \tag{1}
\]

式 (1) 是普通 Type II 双尾判据。相对于 \(\operatorname{Supp}(q_i)\)，两个
固定除子的新增支持分别为

\[
\operatorname{Supp}(d_1)\setminus\operatorname{Supp}(q_1)=\{29\},
\qquad
\operatorname{Supp}(d_2)\setminus\operatorname{Supp}(q_2)=\{19,2089\}.
\]

故两条子射线上分别有 \(\delta(p,q)\le1\) 与 \(\delta(p,q)\le2\)。

## 无穷性与边界

两条子射线都满足 \(p'_i(0)\equiv1\pmod{24}\)、\(24\mid P'_i\) 且
\(\gcd(p'_i(0),P'_i)=1\)。Dirichlet 定理因而保证每条子射线含无穷多个素数，
这些素数全部是核心素数并由同一个固定见证满足选择器分支 T。

本文的周期细化论证本身只覆盖各自一个同余子族。后续审计已经找到不需要周期细化的
固定见证，并在
[两条原压力进程的全体低缺陷尾定理](h19-k23-unbridged-pressure-full-low-defect-rays.md)
中把两条原进程全部闭合；因此“其余素数值开放”只描述本文形成时的边界，不再是当前
知识库状态。

可复现命令：

~~~bash
python3 reproductions/h19_k23_unbridged_pressure_selector_subrays.py
python3 -m unittest tests/test_h19_k23_unbridged_pressure_selector_subrays.py -q
~~~
