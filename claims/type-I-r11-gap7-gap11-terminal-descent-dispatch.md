---
kind: claim
claim_id: type-I-r11-gap7-gap11-terminal-descent-dispatch
title: R=11 固定尾与 gap 7/11 的终端-递降联合 dispatch
statement: 设 p=24h+1 为核心素数，N=22h+1，u=3h+1，q=2h+1。按顺序检查：(i) R=11 固定 pK 尾的 divisor box；(ii) u 是否有模 7 二次非剩余素因子；(iii) -1 是否属于 signed-ratio box R_11(3q)。第一项命中给出直接 Type I terminal；第二项命中给出显式 gap-7 Type II terminal 及严格两尾递降到 u=(p+7)/8；第三项命中给出显式 gap-11 Type II terminal 及严格两尾递降到 q=(p+11)/12。三项全未命中当且仅当：N 属于 R=11 固定尾的两个精确残余因子类，u 的每个素因子均为模 7 二次剩余，且 -1 不属于 R_11(3q)。该 dispatch 是原始 p 的 terminal-first/strict-descent 子选择器，不依赖 G raw source receipt，也不声称其残余为空。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-r11-fixed-tail-residual-classification
  - type-I-g-anchor-r11-adaptive-divisor-terminal
  - type-II-factor-pair-carrier-strict-descent
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - terminal-first
  - strict-descent
  - R11
  - gap-seven
  - gap-eleven
  - factorization
  - proof-boundary
sources:
  - claim: type-I-g-anchor-r11-fixed-tail-residual-classification
    role: exact-first-branch-residual
  - claim: type-II-factor-pair-carrier-strict-descent
    role: gap-seven-and-gap-eleven-lift
  - reproduction: reproductions/type_i_r11_gap7_gap11_joint_dispatch.py
    role: branch-and-boundary-controls
visibility: public
last_checked: '2026-08-12'
---

# \(R=11\) 固定尾与 gap \(7/11\) 的联合 dispatch

## 1. 三条原始 \(p\) 路由

令

\[
p=24h+1,
\qquad
N=22h+1,
\qquad
u=3h+1,
\qquad
q=2h+1.
\tag{1}
\]

注意两个适合严格递降的恒等式

\[
\frac{p+7}{8}=u,
\qquad
\frac{p+11}{12}=q,
\tag{2}
\]

以及

\[
x_7=\frac{p+7}{4}=2u,
\qquad
x_{11}=\frac{p+11}{4}=3q.
\tag{3}
\]

以下三项按 terminal-first 顺序检查。

1. 若某个 \(d\mid N^2\) 满足 \(d\equiv7,8,10\pmod {11}\)，则 \(R=11\)
   的固定第三分母 \(p(3N)\) 构造给出原始 \(p\) 的直接 Type I terminal。
2. 若某个素数 \(r\mid u\) 是模 \(7\) 二次非剩余，则构造 gap \(7\) 的
   Type II terminal，且严格递降到 \(u\)。
3. 若

\[
-1\in\mathcal R_{11}(3q),
\tag{4}
\]

   则构造 gap \(11\) 的 Type II terminal，且严格递降到 \(q\)。

这里 \(\mathcal R_m(X)\) 是 \(X\) 的完整 signed-ratio box；因而 (4) 是有限、
由 \(3q\) 的素因子分解可重算的条件，而不是截断搜索。

## 2. gap \(7\) 的显式严格递降

假设 \(r\mid u\) 是模 \(7\) 二次非剩余。于是

\[
-r\pmod7\in\{1,2,4\}.
\tag{5}
\]

从下表按 \(-r\) 选择 \((a,b)\)：

\[
\begin{array}{c|ccc}
-r\pmod7&1&2&4\\ \hline
(a,b)&(1,1)&(2,1)&(1,2).
\end{array}
\tag{6}
\]

令

\[
A=a,
\qquad B=br,
\qquad C=\frac{2u}{abr},
\qquad K=\frac{A+B}{7}.
\tag{7}
\]

由于 \(r\ne2,7\)，(6) 保证 \(C\) 为正整数、\((A,B)=1\)、\(A\le B\)，且
\(A/B\equiv-1\pmod7\)。所以 \(K\) 是正整数，\(ABC=2u=x_7\)，而

\[
A+B=7K.
\tag{8}
\]

由 \(8\mid p-1\)，factor-pair identity 给出

\[
\boxed{
\frac4u=
\frac1{ABC}+\frac1{ACK}+\frac1{BCK},
\qquad
\frac4p=
\frac1{ABC}+\frac1{pACK}+\frac1{pBCK}.}
\tag{9}
\]

故第二条同时给出直接 Type II certificate、全域可提升公式和严格势支付
\(u<p\)。这里的 \(u\) 不是附带参数，而正是 (2) 中的递归目标分母。

## 3. gap \(11\) 的显式严格递降

条件 (4) 等价于存在两两互素的正整数 \(A,B,C\)，使

\[
ABC=3q,
\qquad
\frac AB\equiv-1\pmod {11}.
\tag{10}
\]

这是 signed-ratio exponent vector 的正、负和零部分分别放入 \(A,B,C\) 得到的。
交换 \(A,B\) 不改变同余，故可取 \(A\le B\)。定义

\[
K=\frac{A+B}{11}.
\tag{11}
\]

则 \(K>0\)，且 \(x_{11}=ABC\)、\(A+B=11K\)。又 \(12\mid p-1\)，所以

\[
\boxed{
\frac4q=
\frac1{ABC}+\frac1{ACK}+\frac1{BCK},
\qquad
\frac4p=
\frac1{ABC}+\frac1{pACK}+\frac1{pBCK}.}
\tag{12}
\]

这是第三条的 E4 显式两尾 lift，E5 是普通自然数秩 \(q<p\)。

## 4. 精确共同残余

R=11 固定尾未命中的精确分类给出：第一条失败，当且仅当 \(N\) 属于

\[
\begin{array}{ll}
\text{(QR11)}&\text{所有 }\ell\mid N\text{ 都是模 }11\text{ 二次剩余};\\
\text{(2,6,1)}&N=\ell_2\ell_6D,\quad
 \ell_2\equiv2,\ \ell_6\equiv6\pmod {11},\\
&\ell_2,\ell_6\text{ 各仅出现一次，且每个 }s\mid D\text{ 满足 }s\equiv1\pmod {11}.
\end{array}
\tag{13}
\]

第二条失败，当且仅当 \(u\) 的每个素因子均属于

\[
\operatorname{QR}_7=\{1,2,4\}\pmod7,
\tag{14}
\]

因为 \(2\) 本身是模 \(7\) 二次剩余，且 gap \(7\) 的完整因子对判据正是
\(x_7=2u\) 有一个二次非剩余素因子。特别地，(14) 自动推出
\(p\pmod7\in\{1,2,4\}\)，所以旧的三条固定 mod-7 certificate 不会被遗漏。

因此三条都失败的**充要**条件是 (13)、(14)，再加上

\[
\boxed{-1\notin\mathcal R_{11}(3q).}
\tag{15}
\]

这把当前联合残余压成三条互相独立、可复核的因子条件；其中前两条已是精确素因子
半群描述，第三条是完整有限 signed-ratio box，而不是未说明的搜索余项。

## 5. 四个固定控制与边界

| \(p\) | \(h\) | dispatch 结果 |
|---:|---:|---|
| \(313\) | \(13\) | \(N=7\cdot41\)，第一条直接 Type I terminal。 |
| \(241\) | \(10\) | \(N=13\cdot17\) 落在 (2,6,1)，但 \(u=31\equiv3\pmod7\)；第二条严格递降到 \(31\)。 |
| \(337\) | \(14\) | \(N=3\cdot103\) 落在 (QR11)，且 \(u=43\equiv1\pmod7\)；第三条以 \((A,B,C,K)=(1,87,1,8)\) 严格递降到 \(29\)。 |
| \(1201\) | \(50\) | \(N=3\cdot367\) 属 (QR11)，\(u=151\equiv4\pmod7\)，且 \(-1\notin\mathcal R_{11}(303)\)；这是三路共同残余。 |

最后一行只否定这张有限 dispatch 的全称覆盖。\(p=1201\) 在其它 terminal-first
菜单中可以被关闭，故它不是 Erdős--Straus 反例，也不否定继续加入新的严格递降路由。

复现：

```bash
python3 reproductions/type_i_r11_gap7_gap11_joint_dispatch.py --verify
```
