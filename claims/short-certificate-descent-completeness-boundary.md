---
kind: claim
claim_id: short-certificate-descent-completeness-boundary
title: 短证书或可闭合递降在自然范围内等价于原猜想
statement: 设 H(p)=p-2。存在一个对每个核心素数 p=1 mod24 都给出 Type I/II 证书 m<=H(p) 或到较小带标记解状态的可闭合严格提升边的证明方案，当且仅当 Erdős--Straus 猜想在全部核心素数上成立。对任意更强的数值界 H(p)<p-2，这类方案仍是原猜想的充分条件，但不再由原猜想形式上推出。
claim_status: established
topics:
- descent
- certificate
- proof-program
- logical-boundary
sources:
- paper: bradford2024
  locator: "Propositions 1--4 (Type II proof not fully written out in the paper)"
  role: certificate-statement-context
- paper: elsholtz_tao2013
  locator: "Section 2"
  role: type-classification
visibility: public
last_checked: '2026-07-24'
---

# 短证书或可闭合递降在自然范围内等价于原猜想

## 定义

记核心素数集合为

\[
\mathcal P=\{p:\ p\text{ 为素数且 }p\equiv1\pmod{24}\}.
\]

给定函数 \(H\)，称一个**\(H\)-闭合方案**为如下数据及其证明：每个
\(p\in\mathcal P\) 的根状态有秩 \(p\) 且标记集为 \(\operatorname{Sol}(p)\)；
每个状态或者有一个显式标记解，或者有一条到严格较小秩状态的显式全域提升边。根状态的
显式解若由直接分支给出，必须来自缺口 \(m\le H(p)\) 的 Type I 或 Type II 证书。

“闭合”意为每条下降边的源标记状态同样包含在该规则中。因此不能把某个偶然找到的
\(n<p\) 的解称为递降，除非它在这个良基状态图中确实可获得。

## 定理

取自然缺口界

\[
H_0(p)=p-2.
\]

则下列两项等价：

1. 存在一个 \(H_0\)-闭合方案；
2. 对每个 \(p\in\mathcal P\)，方程 \(4/p=1/a+1/b+1/c\) 有正整数解。

后者正是约化到核心素数后的 Erdős--Straus 猜想。

## 证明

设 (1) 成立。每条提升边都严格降低分母秩，故
`marked-solution-descent-closure` 的良基归纳表明每个根标记集
\(\operatorname{Sol}(p)\) 非空。这就是 (2)。

反设 (2) 成立。对任意 \(p\in\mathcal P\)，取一个解并按分母排序。
`short-certificate-equivalence` 将它转换为一张 Type I 或 Type II 除子证书，且其
缺口满足

\[
3\le m\le p-2=H_0(p).
\]

故可对每个根直接取这张证书，完全不使用递降边，得到一个 \(H_0\)-闭合方案。这证明
(2) 蕴含 (1)。

最后，若 \(H(p)<p-2\)，同样的良基归纳仍给出“\(H\)-闭合方案蕴含原猜想”。但从原猜想
得到的证书只保证自然范围 \(m\le p-2\)，并不保证较强界，因此反向蕴含不能由上述论证
推出。

## 对当前目标的含义

所以，若“有界”仅指所有证书固有的 \(O(\log p)\) 位长度，或者指
\(m\le p-2\)，要求的“短证书或递降”引理就是原猜想的等价表述，尚未解决。
要使它成为有区分度的研究目标，必须明确给出真短界（例如
\(m\le p/3+O(1)\)）或给出此前未知的、在残余集上可闭合的严格递降选择器。
