---
kind: claim
claim_id: type-II-k2-adjacent-type-I-cross-chart-bridge
title: Type II 的 K 等于二切片与相邻 Type I 图表桥
statement: 设 p=1 mod24 为素数，3<=h<=p-2 且 h=3 mod4，令 L=2h-1、R'=2h+1、x=(p+h)/4、K'=(pR'+1)/4。则 K'=R'x-((h+1)/4)L，且 L|x 当且仅当 L|K'。若此整除成立，令 C_II=x/L、C_I=K'/(2L)、m=8C_I-p=8C_II-1，则 (1,L,C_II) 是缺口 h、K=2 的 Type II 正规形，而 (1,2,C_I,L) 是缺口 m、模数 R' 的 Type I 四元正规形；两者均显式给出 p 的单位分数解。若上游另行定义的规则从联合目标合同输出候选 h，本桥仍只在 L|x 时闭合；本卡不构造“合同到 h”的映射。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
- type-II-coprime-factor-normal-form
- type-I-coprime-factor-normal-form
topics:
- type-II
- type-I
- cross-chart
- adjacent-modulus
- normal-form
- divisor-certificate
- joint-obstruction
- proof-program
sources:
- claim: type-II-coprime-factor-normal-form
  role: Type-II-normal-form-and-reconstruction
- claim: type-I-coprime-factor-normal-form
  role: Type-I-normal-form-and-reconstruction
visibility: public
last_checked: '2026-07-30'
---

# Type II 的 \(K=2\) 切片与相邻 Type I 图表桥

## 定理

设 \(p\equiv1\pmod {24}\) 是素数，并取自然缺口候选

\[
3\le h\le p-2,
\qquad h\equiv3\pmod4.
\]

定义

\[
L=2h-1,
\qquad R'=2h+1=L+2,
\qquad x=\frac{p+h}{4},
\qquad K'=\frac{pR'+1}{4}. \tag{1}
\]

则这些量都是正整数，并有恒等式

\[
\boxed{
K'=R'x-\frac{h+1}{4}L
}. \tag{2}
\]

特别地，

\[
\boxed{L\mid x\quad\Longleftrightarrow\quad L\mid K'.} \tag{3}
\]

若 (3) 成立，令

\[
C_{\mathrm{II}}=\frac{x}{L},
\qquad
C_{\mathrm I}=\frac{K'}{2L},
\qquad
m=8C_{\mathrm I}-p. \tag{4}
\]

则 \(C_{\mathrm{II}},C_{\mathrm I},m\) 都是正整数，而且

\[
\boxed{
m=\frac{2p+1}{L}=8C_{\mathrm{II}}-1
}. \tag{5}
\]

此时同一个整除条件同时给出两张直接证书：

1. 缺口 \(h\) 的 Type II 互素正规形
   \[
   (A,B,C)=(1,L,C_{\mathrm{II}}),
   \qquad \frac{A+B}{h}=2; \tag{6}
   \]
2. 缺口 \(m\)、相邻模数 \(R'=2h+1\) 的 Type I 四元正规形
   \[
   (A,B,C,D)=(1,2,C_{\mathrm I},L). \tag{7}
   \]

这里“四元正规形”使用

\[
D=\frac{Bp+A}{m},
\qquad
A(4BCD-1)=(B+D)p \tag{8}
\]

的坐标次序。式 (6)--(7) 分别恢复单位分数恒等式

\[
\frac4p
=\frac1{LC_{\mathrm{II}}}
 +\frac1{2pC_{\mathrm{II}}}
 +\frac1{2pLC_{\mathrm{II}}}, \tag{9}
\]

\[
\frac4p
=\frac1{2C_{\mathrm I}}
 +\frac1{C_{\mathrm I}L}
 +\frac1{2pC_{\mathrm I}L}
=\frac1{K'/L}+\frac1{K'/2}+\frac1{pK'}. \tag{10}
\]

## 恒等式与整除等价

由 (1) 直接展开，

\[
\begin{aligned}
R'x-\frac{h+1}{4}L
&=\frac{(2h+1)(p+h)-(h+1)(2h-1)}4\\
&=\frac{p(2h+1)+1}{4}=K',
\end{aligned}
\]

即得 (2)。又

\[
\gcd(R',L)=\gcd(2h+1,2h-1)=1,
\]

所以把 (2) 模 \(L\) 化简为 \(K'\equiv R'x\pmod L\) 后，立刻得到 (3)。

由于 \(p\equiv1\pmod8\)、\(R'\equiv7\pmod8\)，有

\[
pR'+1\equiv0\pmod8,
\]

故 \(K'\) 为偶数。又 \(L\) 为奇数；因此 \(L\mid K'\) 自动加强为
\(2L\mid K'\)，从而 (4) 中的 \(C_{\mathrm I}\) 是正整数。

最后，由 \(R'-L=2\) 得

\[
8C_{\mathrm I}-p
=\frac{4K'}L-p
=\frac{pR'+1-pL}{L}
=\frac{2p+1}{L}. \tag{11}
\]

另一方面 \(p=4x-h=4LC_{\mathrm{II}}-h\)，故

\[
2p+1=8LC_{\mathrm{II}}-(2h-1)
=L(8C_{\mathrm{II}}-1),
\]

这证明 (5)。

## Type II 证书的逐项验证

对 (6)，有

\[
x=ABC=LC_{\mathrm{II}},
\qquad
d_{\mathrm{II}}=A^2C=C_{\mathrm{II}},
\qquad
\gcd(A,B)=1,
\qquad A\le B. \tag{12}
\]

正性显然，而且

\[
d_{\mathrm{II}}\mid x^2,
\qquad d_{\mathrm{II}}\le x,
\qquad
x+d_{\mathrm{II}}
=C_{\mathrm{II}}(L+1)
=2hC_{\mathrm{II}}. \tag{13}
\]

所以 \(h\mid x+d_{\mathrm{II}}\)。等价地，正规形同余为

\[
h\mid A+B=L+1=2h,
\qquad K_{\mathrm{II}}=\frac{A+B}{h}=2. \tag{14}
\]

这逐项满足 Type II 除子证书条件。将 (12)--(14) 代入标准恢复式，所得分母正是

\[
(x,y,z)
=(LC_{\mathrm{II}},\,2pC_{\mathrm{II}},\,2pLC_{\mathrm{II}}).
\]

式 (9) 也可直接由

\[
2p+L+1=2(p+h)=8x=8LC_{\mathrm{II}}
\]

核对。因为 \(x<p\)，只有后两个分母被 \(p\) 整除，故这确实是 Type II 解。

## 相邻 Type I 证书的逐项验证

对 (7)，令 \(H=AR'-B\)。由 \(R'=L+2\) 及 (4)，

\[
H=R'-2=L,
\qquad
K'=BC_{\mathrm I}H=2C_{\mathrm I}L. \tag{15}
\]

进一步，(5) 给出

\[
D=\frac{Bp+A}{m}
=\frac{2p+1}{m}=L. \tag{16}
\]

并且

\[
mR'=16C_{\mathrm I}+1=4B^2C_{\mathrm I}+1. \tag{17}
\]

这里 (17) 可由 \(4K'=pR'+1\)、\(R'=L+2\) 直接验证。于是

\[
A(4BC_{\mathrm I}D-1)
=8C_{\mathrm I}L-1
=4K'-1
=pR'
=(B+D)p, \tag{18}
\]

所以 (7) 确为 Type I 四元正规形，而非只有形式相似的四元组。

它对应的首分母与证书除子为

\[
x_{\mathrm I}=ABC=2C_{\mathrm I}=\frac{K'}L,
\qquad
d_{\mathrm I}=A^2C=C_{\mathrm I}. \tag{19}
\]

由 (5) 还有

\[
m=4x_{\mathrm I}-p=8C_{\mathrm I}-p
=8C_{\mathrm{II}}-1. \tag{20}
\]

因此 \(m\equiv7\pmod8\)，且 \(m>0\)。因 \(L\ge5\)，

\[
m=\frac{2p+1}{L}\le\frac{2p+1}{5}\le p-2,
\]

故 \(m\) 是自然范围内的合法缺口。最后，

\[
d_{\mathrm I}\mid x_{\mathrm I}^2,
\qquad
px_{\mathrm I}+d_{\mathrm I}
=C_{\mathrm I}(2p+1)
=mC_{\mathrm I}L, \tag{21}
\]

所以 Type I 的除法与同余条件全部成立。标准恢复给出

\[
(x_{\mathrm I},y_{\mathrm I},z_{\mathrm I})
=(2C_{\mathrm I},\,C_{\mathrm I}L,\,2pC_{\mathrm I}L)
=\left(\frac{K'}L,\frac{K'}2,pK'\right).
\]

式 (10) 的分子恒等式是

\[
pL+2p+1=pR'+1=4K'=8C_{\mathrm I}L.
\]

又 \(\gcd(p,K')=1\)，因为 \(4K'-pR'=1\)。故前两个分母不被 \(p\) 整除，
第三个分母被 \(p\) 整除；这确实是 Type I 解。

## 命中例：\(p=214729\)

取 \(h=19\)。此时

\[
L=37,\quad R'=39,\quad x=53687=37\cdot1451,
\]

以及

\[
K'=2093608=2\cdot37\cdot28292,
\qquad m=8\cdot1451-1=11607.
\]

两张正规形分别为

\[
(A,B,C)_{\mathrm{II}}=(1,37,1451),
\qquad
(A,B,C,D)_{\mathrm I}=(1,2,28292,37).
\]

它们恢复

\[
\frac4{214729}
=\frac1{53687}
 +\frac1{623143558}
 +\frac1{23056311646},
\]

以及

\[
\frac4{214729}
=\frac1{56584}
 +\frac1{1046804}
 +\frac1{449558352232}.
\]

这个素数还有一个原始 \(R=43\) 的二坐标平方终端状态：

\[
214729=7+711+7\cdot711\cdot43,
\]

\[
7\cdot43+1=2\cdot151,
\qquad
711\cdot43+1=2\cdot15287.
\]

在模 \(43\) 下，\(151\equiv15287\equiv22\)，且

\[
\operatorname{ord}_{43}(22)=14,
\qquad22^7\equiv-1\pmod {43}.
\]

所以其目标指数纤维投影为

\[
z_1+z_2\equiv7\pmod {14},
\qquad (\nu_1,\nu_2)=(1,1). \tag{22}
\]

## 同联合合同但桥失败：\(p=77017\)

该素数也有 \(R=43\) 的二坐标状态

\[
77017=7+255+7\cdot255\cdot43,
\]

其两个块为

\[
7\cdot43+1=2\cdot151,
\qquad
255\cdot43+1=2\cdot5483.
\]

同样有 \(151\equiv5483\equiv22\pmod {43}\)，所以它与 (22) 具有完全相同的
联合投影合同

\[
z_1+z_2\equiv7\pmod {14},
\qquad (\nu_1,\nu_2)=(1,1). \tag{23}
\]

但是对同一候选 \(h=19\)，

\[
x=19259\equiv19\pmod {37},
\qquad
K'=750916\equiv1\pmod {37}. \tag{24}
\]

因此 \(37\nmid x\) 且 \(37\nmid K'\)，本定理的两张指定正规形都不能构造。
这只证明该**相邻跨图表桥**在此失败；它不证明 \(p=77017\) 没有其它 Type I/II
证书或其它缺口的桥。

## 研究边界

式 (22)--(24) 给出关键量词边界：若上游另行定义的规则从联合障碍输出候选 \(h\)，
本桥还需要额外的

\[
L\mid x
\quad\Longleftrightarrow\quad
4L\mid p+h
\quad\Longleftrightarrow\quad
L\mid K' \tag{25}
\]

才把候选闭合为实际证书。相同的联合投影合同与同一个外部候选 \(h=19\) 不强制
(25)；本卡本身没有定义“联合合同 \(\mapsto h\)”的选择规则。

最后，本桥输出的是同一 \(p\) 的两张直接证书，不是从较小实例提升解的递降边。若要接入
“短证书或严格可提升递降”总目标，仍须另外证明：每个残余状态都能选择满足 (25) 的候选，
或在 (25) 失败时产生一个合法的新状态、解提升映射与严格下降势函数。
