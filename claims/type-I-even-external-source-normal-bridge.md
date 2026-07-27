---
kind: claim
claim_id: type-I-even-external-source-normal-bridge
title: 偶二次外源严格提升精确落入 Type I 正规形终端桥
statement: 对核心素数的任一完整平方因子外部源见证，令 q=4k-1、n=(qp+1)/(q+1)、K_0=kn。将其 Type I 证书正规化为 (A,B,C) 后，正规形参数恰满足 R=q、K=K_0，且最大尾反向选择器的桥因子为 E=n。因此 E|4K^2、E=1 mod R、E<=4K-2R；若 n 为偶数，则该外源见证不是仅有带标记严格递降，而是目标侧的偶源 Type I 终端桥。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- normal-form
- external-source
- even-source
- descent
- reverse-lift
- mixed-selector
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-certificate-context
- paper: ventas2026
  locator: Theorem 2.3
  role: quadratic-external-source-context
visibility: public
last_checked: '2026-07-28'
---

# 偶二次外源严格提升精确落入 Type I 正规形终端桥

## 定理

令 \(p\equiv1\pmod{24}\) 为素数，取

\[
k\mid\frac{p-1}{4},\qquad q=4k-1,\qquad
n=\frac{qp+1}{q+1},\qquad M=kn. \tag{1}
\]

设完整平方因子外部源选择到

\[
e\mid M^2,\qquad e\le M,\qquad e\equiv-M\pmod q. \tag{2}
\]

由二项尾构造的 Type I 证书是

\[
u=\frac{M+e}{q},\qquad
v=\frac{Mu}{e},\qquad
m=\frac{4e+1}{q},\qquad D=\frac{u^2}{e}. \tag{3}
\]

将 \((p,m,D)\) 正规化为 \(x=ABC\)、\(D=A^2C\)、\((A,B)=1\)，再置

\[
R=\frac{4B^2C+1}{m},\qquad H=AR-B,\qquad K=BCH. \tag{4}
\]

则

\[
R=q,\qquad K=M,\qquad E:=4K-nR=n. \tag{5}
\]

所以

\[
E\mid4K^2,\qquad E\equiv1\pmod R,\qquad E\le4K-2R. \tag{6}
\]

特别地，若 \(n\) 是偶数，则 (6) 正是 Type I 正规形最大尾反向选择器的偶源终端条件；
其源三元组是外源见证已有的

\[
\frac4n=\frac1M+\frac1u+\frac1v. \tag{7}
\]

## 证明

外源构造的目标三元组为

\[
\frac4p=\frac1{Mp}+\frac1u+\frac1v. \tag{8}
\]

证书正规形恢复的目标三元组为

\[
\frac4p=\frac1{ABC}+\frac1{ACH}+\frac1{pK}. \tag{9}
\]

构造中证书的首分母是 \(u\)、第二尾是 \(v\)、最大尾是 \(Mp\)，故正规化逐项恢复

\[
ABC=u,\qquad ACH=v,\qquad pK=Mp.
\]

于是 \(K=M\)。正规形恒等式 \(4K=pR+1\) 与 (1) 的

\[
4M=qp+1
\]

比较，得到 \(R=q\)。因此

\[
E=4K-nR=4M-nq=qp+1-nq=n. \tag{10}
\]

因 \(n\mid M\)，(10) 给出 \(E=n\mid4M^2=4K^2\)。又由
\((q+1)n=qp+1\) 得 \(n\equiv1\pmod q\)，即 \(E\equiv1\pmod R\)。最后

\[
4K-2R-E
=4kn-2q-n
=(4k-1)n-2q
=q(n-2)\ge0, \tag{11}
\]

因为严格外源分母满足 \(n\ge2\)。若 \(2\mid n\)，则 \(E\) 为偶数；而 (7) 中的
第一分母正是

\[
\frac{nK}{E}=K=M,
\]

故它与正规形最大尾反向的源完全一致，且可由偶数基底终止。

还可把奇偶性完全写在外部尺度上。令 \(B_p=(p-1)/4\)，则

\[
n=p-\frac{B_p}{k},
\]

所以由于 \(p\) 为奇数，

\[
2\mid n\quad\Longleftrightarrow\quad \frac{B_p}{k}\ \text{为奇数}. \tag{12}
\]

## 有限审计

对存储的十亿 H19 残余剖面，完整平方因子外源分支命中 \(660\) 条；上述正规化对每条
都成立。其中 \(120\) 条有偶数 \(n\)，直接进入本卡的终端桥，另有 \(540\) 条为奇源，
仍只是一条带标记严格提升。四个外源遗漏保持为

\[
35{,}840{,}809,\quad132{,}285{,}169,\quad141{,}326{,}089,\quad640{,}775{,}689.
\]

重建命令：

~~~bash
python3 reproductions/type_i_even_external_source_normal_bridge.py
python3 -m unittest tests/test_type_i_even_external_source_normal_bridge.py -q
~~~

## 范围

本结论只把已经选择到的完整平方因子外源见证运输为目标 Type I 正规形桥。它不证明每个
核心素数都存在某个 \(k,e\) 满足 (2)，也不把奇源的带标记严格提升误作无标记归纳。全称混合
选择引理仍需要选择普通 Type II 证书或这种偶桥因子的逐点机制。
