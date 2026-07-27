---
kind: claim
claim_id: type-I-target-divisor-overflow
title: Type I 目标除子的溢出因子与正规形精确对应
statement: 固定 p,m,x=(p+m)/4。若 e|x^2 且 e=-1/4 mod m，写 e 的每个素数指数相对 x 的超额之积为 B(e;x)=prod_q q^max(v_q(e)-v_q(x),0)。则存在唯一 A,C 使 x=ABC、gcd(A,B)=1、e=B^2C；相应 d=x^2/e=A^2C 是 Type I 证书。反过来每个 Type I 正规形给出这种 e，且其 B 正是该溢出因子。
claim_status: established
topics:
- type-I
- normal-form
- divisor-residues
- product-sets
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-divisor-certificate-equivalence
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization
visibility: public
last_checked: '2026-07-25'
---

# Type I 目标除子的溢出因子与正规形精确对应

## 定理

令 \(p\equiv1\pmod {24}\)，\(m\equiv3\pmod4\)，并记

\[
x=\frac{p+m}{4},\qquad t=-\frac14\pmod m.
\]

设 \(e\mid x^2\) 且 \(e\equiv t\pmod m\)。定义 \(e\) 相对于 \(x\) 的溢出因子

\[
B(e;x)=\prod_q q^{\max\{v_q(e)-v_q(x),0\}}. \tag{1}
\]

则唯一存在正整数 \(A,C\)，使

\[
x=ABC,\qquad (A,B)=1,\qquad e=B^2C. \tag{2}
\]

并且 \(d=x^2/e=A^2C\) 是 Type I 证书。反过来，任意 Type I 正规形
\(x=ABC,(A,B)=1,d=A^2C\) 的互补除子 \(e=x^2/d\) 满足 (2)，其 \(B\) 正是 (1)。

更直接地，令 \(g=(e,x)\)，则

\[
A=\frac{x}{g},\qquad B=\frac{e}{g},\qquad C=\frac{g^2}{e}. \tag{3}
\]

特别地，\(B\) 是目标除子离“整除 \(x\)”还差的精确商，而不是人为选定的参数。

因此，在固定 \((p,m)\) 下，最小正规形 \(B\) 与满足 \(e\equiv-1/4\pmod m\) 的
平方除子中最小的溢出因子完全相同。

## 证明

逐素数写 \(v_q(x)=a\)、\(v_q(e)=r\)，其中 \(0\le r\le2a\)。令

\[
b=\max\{r-a,0\},\qquad c=r-2b,\qquad \alpha=a-b-c. \tag{4}
\]

若 \(r\le a\)，则 \((b,c,\alpha)=(0,r,a-r)\)；若 \(r>a\)，则
\((b,c,\alpha)=(r-a,2a-r,0)\)。故三者均非负，且

\[
a=\alpha+b+c,\qquad r=2b+c. \tag{5}
\]

令 \(A,B,C\) 分别取指数 \(\alpha,b,c\) 的素因子积，即得 (2)。每个 \(b>0\)
都强制 \(\alpha=0\)，所以 \((A,B)=1\)。其唯一性由 (3) 给出。

公式 (3) 来自逐素数的 \(g\) 指数 \(\min\{r,a\}\)；上述两种情形同时说明
\(B\mid g\)，所以 \(C=g/B=g^2/e\) 为整数。再由 \(e=B^2C\) 与 \(x=ABC\) 得

\[
d=\frac{x^2}{e}=A^2C.
\]

因为 \(e\equiv-1/4\pmod m\)，它正是 Bradford Type I 判据的互补除子形式，故 \(d\)
为证书。反向等式直接成立。

## 研究意义

\(B=1\) 当且仅当目标残数已在普通除子集 \(\operatorname{Div}(x)\) 中命中；
\(B>1\) 精确记录为了命中而必须把哪些素因子指数提升到超过 \(x\) 的程度。故“小 \(B\)”
不是一个任意参数现象，而是有限阿贝尔群中受控平方除子溢出的选择问题。

等价地，关键选择问题是：能否找到 \(e\mid x^2\)、\(e\equiv-1/4\pmod m\)，使
\(e/(e,x)\) 很小。它把跨缺口研究直接接到 \(x\) 与目标平方除子共有的碰撞因子上。

## 一私有因子的精确代价

设窗口状态可写成

\[
x=Er^b,\qquad (E,r)=1,
\]

其中 \(r\) 是私有素因子。任意平方除子有唯一形状 \(e=ar^i\)，其中
\(a\mid E^2\)、\(0\le i\le2b\)。由 (3) 或直接分解最大公因子，得到

\[
B(e;x)=\frac{a}{(a,E)}r^{\max\{i-b,0\}}. \tag{6}
\]

这把 [私有平移首达判据](type-I-private-translate-index.md) 的可达性精确提升为代价：
若目标在 \(a r^i\) 处首次到达，\(i\) 决定私有部分是否需要溢出，而
\(a/(a,E)\) 记录固定碰撞部分仍未被普通除子吸收的代价。

特别地，若某个目标表示满足 \(a\mid E\)，则：

- \(i\le b\) 给出 \(B=1\) 的外部 source 证书；
- \(b<i\le2b\) 给出溢出 \(B=r^{i-b}\) 的 Type I 证书；
- \(i>2b\) 时该私有幂不属于 \(x^2\)，不能给出证书。

因此首达指数 \(\delta\) 本身不足以证明低溢出闭合：还必须控制实现该平移的固定部分
\(a\) 的溢出。反过来，(6) 给出一个正确的窗口势函数候选，即对全部
\(ar^i\equiv-1/4\pmod m\) 取右端的最小值；它恰是该状态的最小正规形 \(B\)，而非
一个启发式复杂度。

这给出一条可攻克的方向：在跨缺口碰撞状态中，证明长期不命中普通除子集会迫使目标
在低溢出积集命中，或使溢出因子的素支撑/大小增长到可导出新的证书或带标记递降的程度。
该定理本身不控制这种增长，因而不蕴含 Erdős--Straus 猜想。

## 机械核验

`short_certificate.type_i_normal_form_from_target_divisor` 将目标除子逐项归一化为
\((A,B,C)\)，并在 `tests/test_short_certificate.py` 中对 \(p\le10000,m\le107\) 的每张
Type I 证书核验 \(e=B^2C\) 与 \(B=e/(e,x)\)。
