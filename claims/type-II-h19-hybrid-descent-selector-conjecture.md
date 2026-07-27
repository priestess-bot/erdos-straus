---
kind: claim
claim_id: type-II-h19-hybrid-descent-selector-conjecture
title: H19 后标准或偶源严格递降选择器猜想
statement: 对每个未被 H19 直接 Type II 射线捕获的素数 p=1 mod24，猜想至少有一个出口成立：(A) 存在 k|(p-1)/4 与 e|[k((4k-1)p+1)/(4k)]^2，使 e=-k((4k-1)p+1)/(4k) mod(4k-1)；或 (B) 存在正奇数 c、p-c 的因子 d 与整数 r,e1，满足 (p-c)/d=1+cr、dr=-1 mod4、e1|[k(1+cr)]^2、e1=-k(1+cr) mod r，其中 k=(dr+1)/4。两种情形均给出到严格更小分母的显式提升；该选择器若成立则蕴含 Erdős--Straus 猜想。
claim_status: open
topics:
- descent
- external-source
- even-source
- type-II
- selector
- induction
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: certificate-and-descent-context
visibility: public
last_checked: '2026-07-25'
---

# H19 后标准或偶源严格递降选择器猜想

## 命题

令 \(p\equiv1\pmod{24}\) 是未被前 19 条规范 Type II 射线直接捕获的素数。提出如下析取
选择器。

**标准平方因子分支。** 存在

\[
k\mid\frac{p-1}{4},\qquad q=4k-1,\qquad
n=\frac{qp+1}{q+1},\qquad M=kn
\]

和 \(e\) 满足

\[
e\mid M^2,\qquad e\le M,\qquad e\equiv-M\pmod q. \tag{A}
\]

**奇距离偶源分支。** 存在正奇数 \(c<p\)、\(d\mid p-c\) 和正整数 \(r,e_1\)，使

\[
\frac{p-c}{d}=1+cr>1,\qquad dr\equiv-1\pmod4, \tag{B1}
\]

并在

\[
k=\frac{dr+1}{4},\qquad M_1=k(1+cr)
\]

下满足

\[
e_1\mid M_1^2,\qquad e_1\le M_1,\qquad
e_1\equiv-M_1\pmod r. \tag{B2}
\]

分支 (A) 是[平方因子外部源递降](quadratic-factor-external-source-descent.md)的完整条件；
(B1)--(B2) 是[奇数距离偶源递降](odd-distance-even-source-descent.md)的完整条件。
二者都给出显式 \(4/n\) 解并严格提升为 \(4/p\)，其中源分母 \(n<p\)。

## 为何足以证明猜想

若该选择器对所有 H19 残余素数成立，则对分母作强归纳。小于 \(p\) 的源分母已由归纳
假设有三项分解，而 (A) 或 (B) 的带标记提升将其变为 \(4/p\) 的分解。非核心素数的
既有同余构造与合数约化处理其余分母；H19 直接捕获剩余的核心素数。因此该选择器加上
已证的 H19 射线公式蕴含 Erdős--Straus 猜想。

关键点是这不是“若存在某个解则可递降”的循环陈述：(A) 和 (B) 都是有限因子分解和
同余条件，可独立检查并直接构造提升。

## 当前证据与边界

在存储的 \(p\le5\cdot10^8\) H19 残余剖面中，425 个状态均满足这个析取：
422 个满足 (A)，其余三个满足 (B)，所需距离为 \(7,3,3\)，见
[二层自适应偶源递降闭合](type-II-h19-adaptive-even-source-descent.md)。

这不支持把 \(k\) 或 \(c\) 固定。标准分支在五亿范围仍需要 \(k=98\)，且确有三个失败；
奇距离偶源扇即使允许所有距离也不能单独覆盖一般核心素数。更强的外部源逃逸审计还给出
不带 H19 直接出口的真实递降逃逸边界，见
[自适应外部源递降逃逸型](adaptive-external-source-escape-audit.md)。

十亿审计进一步发现 \(p=640{,}775{,}689\) 同时逃过标准分支和完整
\(c\le9999\) 偶源截断，却在 \(c=34091\) 首次满足 (B)。它也有
\(s=45,h=359\) 的纯新 Type II 证书。因此该析取选择器在十亿范围保持闭合，但不能以
固定小距离替代状态依赖的 (B) 或短证书分支，见
[第四压力点的偶源首释放](type-II-h19-fourth-even-source-release-boundary.md)。

所以待证的真正内容是：H19 射线的共同失败状态为何强制 (A) 或一个随状态变化的
\((c,d,r,e_1)\) 满足 (B1)--(B2)，或者为何其共同失败转而产生受限的新因子 Type II
证书；固定有限源表不能替代这一步。

十亿四点压力集的首个偶源尾参数为 \(r=103,31,31,15\)，均不超过 103，而相应距离并不
统一有界。这使一个更精确的中间猜想成为可能：共同失败若不走 (A)，则应强制某个受控
\(r\) 的 \(rp+1\) 出现满足 (B1)--(B2) 的因子对；目前这只是有限证据，见
[小 r 偶源尾选择剖面](type-II-h19-pressure-small-r-profile.md)。
这些状态已逐项重建为严格提升，故该析取在存储的十亿剖面上确实以 \(660+4\) 纯递降闭合，
见 [H19 十亿标准递降或受控 r 偶源递降闭合](type-II-h19-hybrid-small-r-descent.md)。
