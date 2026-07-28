---
kind: claim
claim_id: type-I-pminusone-box-miss-global-audit-500m
title: 五亿有限盒 p 减一遗漏的全正规形全局审计
statement: 对五亿普通 Type II 双尾遗漏中在 m<=215 正规形盒内没有 p-1 Type I 最大尾桥的185个素数，完整穷尽每点全部 r|((p-1)/4)^2、全部 B 和全部自然缺口后，164点存在更大自然缺口上的 p-1 桥，21点在全正规形意义下仍无 p-1 桥。计算共检查15411个强制状态，并为164个命中保存两侧精确单位分数证书，为21个遗漏保存逐状态目标剩余类缺失摘要。
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
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-and-Type-II-certificate-context
visibility: public
last_checked: '2026-07-28'
---

# 五亿有限盒 \(p-1\) 遗漏的全正规形全局审计

## 结论及严格范围

[五亿 \(p-1\) 有限盒边界](type-I-tail-reverse-pminusone-boundary-500m.md)在
\(p\le5\cdot10^8\) 的 1,717 个普通 Type II \(p-1\) 双尾遗漏中，找到 1,532 个
\(m\le215\) 的 \(p-1\) Type I 最大尾桥，留下 185 个**盒内遗漏**。本审计只以这 185 点为
输入，但对每个输入点移除缺口和 \(B\) 的上界，得到

\[
185=164_{\text{存在某个全局 }p-1\text{ 桥}}
   +21_{\text{不存在任何全正规形 }p-1\text{ 桥}}. \tag{1}
\]

因此，在原 1,717 个普通双尾遗漏中，恰有 1,696 点有 \(p-1\) Type I 最大尾桥；余下
21 点在仓库的**正规形最大尾 \(p-1\) 架构**内全局失败。这不是对全部
\(p\le5\cdot10^8\) 素数重新进行的全局审计，也不排除其它 Type I 变换或其它 Type II 坐标。

21 个全局 \(p-1\) 遗漏为

\[
\begin{gathered}
297049,\ 3942409,\ 13782409,\ 36583369,\ 40944649,\\
62588089,\ 64214329,\ 72148729,\ 96530569,\ 171292489,\\
222416329,\ 257483209,\ 259423609,\ 297640249,\ 319207849,\\
335420089,\ 357834409,\ 401991529,\ 405660649,\ 459147049,\\
477015289.
\end{gathered} \tag{2}
\]

它们才是后续研究自适应移位源 \(s>1\) 的正确有限训练集。

## 输入冻结

唯一运行输入是
[`type-i-tail-reverse-pminusone-profile-500m-results.json`](../reproductions/type-i-tail-reverse-pminusone-profile-500m-results.json)
的 `p_minus_one_misses` 字段。脚本同时守卫：

- 前缀上界为 \(5\cdot10^8\)，来源盒为 \(m\le215\)；
- 普通双尾遗漏数为 1,717，盒内 \(p-1\) 命中数为 1,532；
- 输入恰有 185 个严格递增且互异的核心素数；
- 换行分隔素数列表的 SHA-256 为
  `e4a723da32b70ee8aed0236f66a6d61803181e0e1db1fd8767b830e81a0f7ccf`。

因而本计算不重新扫描五亿前缀；它严格复用已经冻结的 185 点边界集合。

## 全部正规形量词为何有限

对一个输入素数置

\[
t=\frac{p-1}{4}.
\]

由 [Type I 正规形的 \(p-1\) 桥判据](type-I-normal-pminusone-upper-half-bridge.md)，任意以
\(p-1\) 为源的最大尾桥都强制

\[
r\mid t^2,\qquad R=4r-1,\qquad E=R+1=4r,
\qquad K=pr-t=\frac{pR+1}{4}. \tag{3}
\]

因此，穷尽 \(r\mid t^2\) 就穷尽了所有可能的源模数，而不需要预先限制缺口或正规形。
185 点一共有

\[
\sum_p\tau(t_p^2)=15411 \tag{4}
\]

个强制状态；本计算逐个检查了全部 15,411 个状态，没有对命中点提前终止。

为避免直接分解最高达到 83 比特的 \(K\)，对每个 \(r\mid t^2\) 使用唯一平方正规化

\[
t=\alpha\beta\gamma,\qquad
r=\beta^2\gamma,\qquad
(\alpha,\beta)=1.
\]

于是

\[
K=\beta\gamma(\beta p-\alpha). \tag{5}
\]

\(\beta\gamma\) 的素因数已经包含在 \(t\) 的分解中，只需另外分解小于 \(2^{56}\) 的仿射因子
\(\beta p-\alpha\)。每个结果都通过素性和素因子幂乘积重新验证。

## 平方除数命中与正规形恢复

固定一个 \((p,r,R,K)\)。由
[源状态实现判据](type-I-normal-source-state-realization.md)，一般正规形命中必须存在

\[
BCH=K,\qquad 4B^2C\equiv-1\pmod R. \tag{6}
\]

写 \(d=B^2C\)，则 \(d\mid K^2\)，且因 \(4r\equiv1\pmod R\)，目标类等价于

\[
d\equiv-r\pmod R. \tag{7}
\]

反过来，对任意命中的 \(d\mid K^2\)，令

\[
g=(d,K),\qquad B=\frac d g,\qquad
C=\frac{g^2}{d},\qquad H=\frac K g. \tag{8}
\]

逐素指数立即给出 \(B,C,H\in\mathbb N\)、\(BCH=K\)、\(B^2C=d\) 及
\((B,H)=1\)。又因 \((K,R)=1\)，式 (7) 推出

\[
H\equiv-B\pmod R,
\]

所以 \(A=(B+H)/R\) 为整数，且 \((A,B)=1\)。这证明平方除数测试不仅是必要条件；经过
规范化后，它足以恢复互素正规形。

还必须保留自然缺口守卫。若初始 \(H<B\)，交换 \(B,H\)。因为
\(H\equiv-B\pmod R\)，交换保持 \(B^2C\) 的目标剩余类，同时保持 \(A,C,K\) 不变；目标
分解的前两个分母只是互换。相等情形会由 \((B,H)=1\) 强制 \(B=H=1\)，进而迫使
\(R\mid2\)，故不可能。定向到 \(H>B\) 后令

\[
m=\frac{4B^2C+1}{R}.
\]

由

\[
R(p-m)=4BC(H-B)-2>0 \tag{9}
\]

以及 \(m\equiv3\pmod4\)，得到严格自然范围 \(3\le m\le p-2\)。每张命中证书还重新检查
\(p=4ABC-m\)、目标 Type I 除子同余及

\[
\frac4p=\frac1{ABC}+\frac1{ACH}+\frac1{pK},\qquad
\frac4{p-1}=\frac1{(p-1)K/E}+\frac1{ABC}+\frac1{ACH} \tag{10}
\]

的精确 `Fraction` 恒等式。

## 目标缺失的精确核验

全部状态合计有

| 对象 | 数量 |
| --- | ---: |
| 强制 \(r\) 状态 | 15,411 |
| 平方除数候选 \(d\mid K^2\) | 112,657,233 |
| 有序 \(B,C,H\) 指数分配 | 178,245,405 |
| 平衡 MITM 两侧条目 | 1,417,964 |
| 目标剩余类可达状态 | 511 |

实现没有物化上亿个平方除数。将 \(K^2\) 的素幂菜单确定性地平衡拆成左右两块。因
\((K,R)=1\)，对每个左除数 \(d_L\)，右侧必须命中唯一要求的剩余类

\[
d_R\equiv-rd_L^{-1}\pmod R. \tag{11}
\]

这与全笛卡尔积枚举严格等价。对 21 个全局遗漏，结果文件展开了全部 1,323 个强制状态，
逐状态保存 \(K\) 的分块素因数分解、左右候选数、右侧实际剩余类集合哈希、所需剩余类集合
哈希及交集数零。测试从这些素因数分解重新生成两侧集合并再次验证交集为空。

## 证据文件

- 实现：
  [`reproductions/type_i_pminusone_box_miss_global_audit_500m.py`](../reproductions/type_i_pminusone_box_miss_global_audit_500m.py)
- 164 张命中证书及 21 点逐状态缺失摘要：
  [`reproductions/type-i-pminusone-box-miss-global-audit-500m-results.json`](../reproductions/type-i-pminusone-box-miss-global-audit-500m-results.json)
- 输入、完整量词、证书和 MITM 缺失重放：
  [`tests/test_type_i_pminusone_box_miss_global_audit_500m.py`](../tests/test_type_i_pminusone_box_miss_global_audit_500m.py)

单点 \(p=297049\) 的完整有序三因子枚举见
[297049 全局排除](type-I-pminusone-global-exclusion-297049.md)，它与本审计的首个全局遗漏一致。
本卡的主要新增结论是：原来 185 个盒内遗漏中，164 个只是需要更大的自然缺口；真正迫使
\(p-1\) 源失效的点只有上述 21 个。

~~~bash
python3 reproductions/type_i_pminusone_box_miss_global_audit_500m.py
python3 -m unittest tests.test_type_i_pminusone_box_miss_global_audit_500m -v
~~~
