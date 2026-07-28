---
kind: claim
claim_id: type-I-pminusone-global-exclusion-297049
title: 297049 的全正规形 p 减一 Type I 最大尾终端桥排除
statement: 对核心素数 p=297049，普通 Type II p-1 双尾选择器没有见证；并且对任意 Type I 正规形、任意缺口和任意 B，都不存在保持正规形前两项并以 n=p-1 为源的最大尾终端桥。证明性计算穷尽 t=(p-1)/4 的平方的 27 个除子 r、37557 个规范平方除子状态及包含全部 B,C,H 指数分配的 61851 个超集状态，目标剩余类命中为零。另一方面，p 有源 n=p-25、B=1 的 Type I 偶终端桥。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: independent_review
topics:
- type-I
- type-II
- p-minus-one
- terminal-bridge
- normal-form
- shifted-source
- selector-boundary
- exhaustive-computation
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-and-Type-II-certificate-context
visibility: public
last_checked: '2026-07-28'
---

# \(p=297049\) 的全正规形 \(p-1\) Type I 最大尾终端桥排除

## 精确结论

令 \(p=297049\)。在仓库的混合终端架构中，逐项成立：

1. \(p\) 没有普通 Type II \(p-1\) 双尾证书；
2. 跨任意 Type I 正规形、任意合法缺口及任意 \(B\)，\(p\) 没有保持正规形
   前两项、以 \(n=p-1\) 为源的最大尾终端桥；
3. \(p\) 有一张源为 \(n=p-25\) 的 \(B=1\) Type I 最大尾偶终端桥。

第二项中的“全局”只指这个单点上仓库已定义的**正规形最大尾终端桥**，不包含任意可能的
Type I 变换，也不排除其它 Type II 坐标。

## 有限量词的完备化

置

\[
t=\frac{p-1}{4}=74262=2\cdot3\cdot12377.
\]

由 [Type I 正规形的 \(p-1\) 桥判据](type-I-normal-pminusone-upper-half-bridge.md)，
任意这样的桥都强制

\[
R=4r-1,\qquad r\mid t^2,\qquad E=R+1=4r.
\]

因而只有

\[
\tau(t^2)=3^3=27
\]

个 \(r\) 状态。对每个状态定义

\[
K_r=pr-t=\frac{pR+1}{4}.
\]

若某个 Type I 正规形实现该源状态，则由
[源状态实现判据](type-I-normal-source-state-realization.md)，必存在正整数 \(B,C,H\) 使

\[
BCH=K_r,\qquad 4B^2C\equiv-1\pmod R. \tag{1}
\]

反向恢复不能止于检查 \(A\) 的整性与互素性。对命中的
\(d=B^2C\mid K_r^2\)，必须先规范化

\[
g=(d,K_r),\qquad B=\frac d g,\qquad
C=\frac{g^2}{d},\qquad H=\frac{K_r}{g}. \tag{2}
\]

逐素指数给出 \(B,C,H\in\mathbb N\)、\(BCH=K_r\)、\(B^2C=d\) 与
\((B,H)=1\)。由 \(4K_r=pR+1\) 有 \((K_r,R)=1\)，再结合目标同余可得
\(H\equiv-B\pmod R\)。若初始 \(H<B\)，交换 \(B,H\)；交换保持 \(C,K_r\) 与

\[
A=\frac{H+B}{R}
\]

不变，并因 \(H\equiv-B\pmod R\) 而保持平方除子的目标剩余类。目标分解的前两项仅仅
互换。\(H=B\) 会由互素性迫使 \(B=H=1\)，进而迫使 \(R\mid2\)，所以不可能。

定向到 \(H>B\) 后定义

\[
m=\frac{4B^2C+1}{R}. \tag{3}
\]

此时还要显式检查 \((A,B)=1\)、\(p=4ABC-m\) 以及

\[
R(p-m)=4BC(H-B)-2>0. \tag{4}
\]

由 \(m\equiv3\pmod4\) 可知 \(3\le m\le p-2\)，即缺口处于自然范围。实现对每个命中
还重建 Type I 除子证书，并以有理数精确检查目标与 \(p-1\) 源的两个三单位分数恒等式。
因此，穷尽全部有序分解 \(BCH=K_r\) 是不限制缺口、不限制 \(B\) 且不限制正规形的
有限超集枚举，但“命中”只有经过上述完整后处理才算有效见证。

## 两套精确枚举的交叉核验

计算对 27 个 \(r\) 保存了 \(K_r\) 的完整素因数分解，并分别精确枚举：

| 枚举对象 | 总数 | 目标同余命中 |
| --- | ---: | ---: |
| 规范化平方除子 \(d=B^2C\mid K_r^2\) | 37,557 | 0 |
| 全部有序分解 \(BCH=K_r\) | 61,851 | 0 |
| 各状态去重后的可达剩余类数之和 | 34,222 | 0 |

第一行用

\[
g=(d,K_r),\qquad B=\frac d g,\qquad
C=\frac{g^2}{d},\qquad H=\frac{K_r}{g}
\]

唯一恢复满足 \(\gcd(B,H)=1\) 的规范状态。第二行还包含 24,294 个非互素指数分配，
所以两行不是逐项一一对应；但它是更大的超集，且两种枚举对每个 \(r\) 得到完全相同的
可达 \(B^2C\bmod R\) 集合。目标类

\[
B^2C\equiv-r\pmod R
\]

在 27 个状态中全部缺失，故互素条件甚至没有成为障碍。这证明不存在所述 \(p-1\) 桥。

由于主审计是零命中，产物另存一个 \(p=73\) 的后处理正控：在 \(r=1,R=3,K=55\)
时，命中 \(d=275\) 先规范化为 \((B,C,H)=(5,11,1)\)，随后必须交换为
\((B,C,H)=(1,11,5)\)。它恢复

\[
(A,m)=(2,15),\qquad
\frac4{73}=\frac1{22}+\frac1{110}+\frac1{4015},
\]

且 \(15\) 位于自然范围；这条正控防止零命中掩盖定向代码的错误。

## 两个额外分支检查

普通 Type II \(p-1\) 双尾枚举检查了由 \(4\mid d\mid p-1\) 给出的八个缺口

\[
3,7,11,23,49507,99015,148523,297047,
\]

见证数为零。

移位分支取

\[
s=25,\quad n=297024,\quad R=19,\quad E=476,\quad
K=1410983,\quad (A,B,C)=(1046,1,71),\quad m=15.
\]

这些参数满足 \(E=sR+1\)、\(E\mid n^2/\gcd(E,4)\)、\(E\mid4K^2\) 及全部正规形条件。
精确回放为

\[
\frac4{297049}
=\frac1{74266}+\frac1{1475888218}+\frac1{419131089167},
\]

以及

\[
\frac4{297024}
=\frac1{880453392}+\frac1{74266}+\frac1{1475888218}.
\]

因此，在“普通 Type II \(p-1\) 双尾或 Type I 最大尾偶终端”这套架构内，该点确实强制
Type I 分支采用非零源距离。

## 证据与边界

- 实现：
  [`reproductions/type_i_pminusone_global_exclusion_297049.py`](../reproductions/type_i_pminusone_global_exclusion_297049.py)
- 逐状态产物：
  [`reproductions/type-I-pminusone-global-exclusion-297049.json`](../reproductions/type-I-pminusone-global-exclusion-297049.json)
- 精确回放与回归测试：
  [`tests/test_type_i_pminusone_global_exclusion_297049.py`](../tests/test_type_i_pminusone_global_exclusion_297049.py)

“这是该混合架构中首个必须移位的点”还依赖
[五亿 \(p-1\) 有限剖面](type-I-tail-reverse-pminusone-boundary-500m.md)对更小前缀的完整输入和
已存结果；本卡的单点全枚举所证明的是 \(p=297049\) 的跨正规形排除，不单独证明
“首个”的前缀量词。该有限排除也不是全称选择器定理，更不是 Erdős--Straus 反例。

~~~bash
python3 reproductions/type_i_pminusone_global_exclusion_297049.py
python3 -m unittest tests.test_type_i_pminusone_global_exclusion_297049 -v
~~~
