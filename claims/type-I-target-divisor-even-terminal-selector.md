---
kind: claim
claim_id: type-I-target-divisor-even-terminal-selector
title: Type I 目标除子与偶终端桥的双因子选择器
statement: 对核心素数p，令m为合法缺口、x=(p+m)/4。存在一张以最大尾反向提升到偶源的 Type I 正规形，当且仅当存在e|x^2与偶数E，使 e=-1/4 modm，R=(4e+1)/m，K=xR-e，且 E|4K^2、E=1 modR、E<=4K-2R。此时目标解为(1/x,1/(xK/e),1/(pK))，偶源n=(4K-E)/R的解为(1/(nK/E),1/x,1/(xK/e))。因此全称混合终端选择引理等价于：每个核心素数有普通 Type II双尾证书，或有这样一对目标侧因子(e,E)。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- normal-form
- terminal-bridge
- even-source
- divisor-residues
- factorization
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-divisor-certificate-context
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization-context
visibility: public
last_checked: '2026-07-28'
---

# Type I 目标除子与偶终端桥的双因子选择器

## 定理

令 \(p\equiv1\pmod {24}\) 为素数，\(m\equiv3\pmod4\)、\(3\le m\le p-2\)，并令

\[
x=\frac{p+m}{4}. \tag{1}
\]

则存在一张 Type I 正规形，并可保持其前两项反向提升到偶源，当且仅当存在正整数 \(e,E\)
满足

\[
e\mid x^2,\quad\quad e\equiv-4^{-1}\pmod m, \tag{2}
\]

以及

\[
R=\frac{4e+1}{m},\quad\quad K=xR-e, \tag{3}
\]

\[
E\mid4K^2,\quad\quad E\equiv1\pmod R,\quad\quad
2\mid E,\quad\quad E\le4K-2R. \tag{4}
\]

此时

\[
4K=pR+1,\quad\quad n=\frac{4K-E}{R},\quad\quad 2\le n<p,\quad\quad 2\mid n, \tag{5}
\]

并有显式目标和终端源解

\[
\frac4p=\frac1x+\frac1{xK/e}+\frac1{pK}, \tag{6}
\]

\[
\frac4n=\frac1{nK/E}+\frac1x+\frac1{xK/e}. \tag{7}
\]

因此所研究的全称混合终端选择引理可完全改写为：每个核心素数至少有普通 Type II
双尾证书或一组 \((m,e,E)\) 满足 (1)--(4)。

## 证明

由[目标除子的溢出因子与正规形精确对应](type-I-target-divisor-overflow.md)，(2) 唯一给出

\[
x=ABC,\quad\quad e=B^2C,
\]

的一张 Type I 正规形。其正规形参数满足

\[
R=\frac{4B^2C+1}{m}=\frac{4e+1}{m}.
\]

令 \(g=(e,x)\)。该正规形可取

\[
A=\frac{x}{g},\quad\quad B=\frac{e}{g},\quad\quad C=\frac{g^2}{e}.
\]

于是

\[
BCH
=BC(AR-B)
=xR-e=K. \tag{8}
\]

又由 (1)、(3) 有

\[
4K=4xR-4e=(p+m)R-4e=pR+1. \tag{9}
\]

所以正规形最大尾的偶源选择器正好给出 (4)--(7)：其原同余为
\(E\equiv4K\pmod R\)，但 (9) 将其化为 \(E\equiv1\pmod R\)。反向方向按同一正规形
恢复即可。证毕。

## 含义与边界

这个形式消除了 \((A,B,C)\) 作为**选择变量**的必要性：第一个因子 \(e\) 同时编码 Type I
证书与其全部溢出，第二个因子 \(E\) 编码偶终端桥。它仍然没有强制任何 \(m,e,E\) 存在，
所以不是猜想的证明；但它给出了与普通 Type II 尾分支并列的精确目标侧因子状态，可直接用于
研究跨缺口的实际素因子、碰撞标签与积集饱和。

对五亿至六亿连续审计中的全部 247 条 Type I 终端记录，测试均从保存的 \(B^2C\) 和 \(E\)
重建 (3)、(6)、(7)，不依赖原始正规形的其余信息。

可复现命令：

~~~bash
python3 -m unittest tests/test_type_i_target_divisor_terminal_selector.py -q
~~~
