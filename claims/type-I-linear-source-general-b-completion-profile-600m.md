---
kind: claim
claim_id: type-I-linear-source-general-b-completion-profile-600m
title: 六亿压力集的线性源一般 B Type I 有限闭合剖面
statement: 对权威冻结的1964个普通 Type II p-1 双尾遗漏，其中1717个来自p不超过五亿、247个来自五亿到六亿区间，按min(a,s)不超过sqrt((p-2)/3)的完备方案扫描至首个命中，并对每个实际审计的R以完整MITM判定所有d整除K平方且4d=-1模R的候选后，1964点全部获得自然一般B Type I最大尾桥。所选证书中1764张满足B=1、200张必须在该确定性顺序中使用B>1；最晚首达点为p=283319689且min(a,s)=587。这只是冻结有限压力集的闭合，不证明全称选择猜想。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: independent_review
topics:
- type-I
- type-II
- linear-source
- shifted-source
- general-b
- terminal-bridge
- target-square-divisor
- exhaustive-computation
- finite-audit
- selector-profile
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-and-Type-II-certificate-context
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization-context
visibility: public
last_checked: '2026-07-28'
---

# 六亿压力集的线性源一般 \(B\) Type I 有限闭合剖面

## 精确结论和范围

本审计冻结两个已经存在的普通 Type II \(p-1\) 双尾遗漏集合：

- \(p\le5\cdot10^8\) 的 1,717 点；
- \(5\cdot10^8<p\le6\cdot10^8\) 的 247 点。

两个集合交集为空，合并后恰有 1,964 个核心素数。对每一点寻找线性移位源

\[
p=a+s+asR,\quad s\equiv1\pmod2,\quad
R\ge3,\quad R\equiv3\pmod4, \tag{1}
\]

并令

\[
E=sR+1,\quad n=p-s=aE,\quad K=\frac{pR+1}{4}. \tag{2}
\]

目标侧不限制为 \(B=1\)，而是完整判定是否存在

\[
d\mid K^2,\quad 4d\equiv-1\pmod R. \tag{3}
\]

结果为

\[
1964=1964_{\text{线性源一般 }B\text{ 命中}}+0_{\text{遗漏}}. \tag{4}
\]

这是一项**有限压力集闭合**。输入不是六亿以内的全部核心素数，计算也没有证明
[线性上半区一般 \(B\) 混合终端选择猜想](type-I-linear-source-general-b-terminal-selector-conjecture.md)，
更没有证明 Erdős--Straus 猜想。

## 输入冻结

第一份输入为
[`type-i-tail-reverse-even-source-closure-500m-results.json`](../reproductions/type-i-tail-reverse-even-source-closure-500m-results.json)，
文件 SHA-256 为
`426ef578d796c7307505e87d16794d28569a91d8297693ec742bcf21873d4f77`；
其 1,717 个素数按换行分隔后的 SHA-256 为
`f3553871ba8b5e9ad256d1f647bd034dd305b9c192ea0295034da1585082252e`。

第二份输入为
[`type-i-mixed-terminal-dense-500m-600m-results.json`](../reproductions/type-i-mixed-terminal-dense-500m-600m-results.json)，
文件 SHA-256 为
`beca2d981fbccd4313f14f5f5ba81459afaae368bf377db066f26a8bbdc77ce0`；
其 247 个素数列表 SHA-256 为
`1856761ddad705b94e02a9ed62aa59c384b84597ff3ec193714abeb76c6257f2`。

按上述顺序拼接后的 1,964 点列表 SHA-256 为
`c6f389dc599898b9bfe182c10d3260033e6ebc2ad9061251b7fb8a7e1ef5ce40`。
程序还逐点检查 \(p\equiv1\pmod {24}\) 和素性，因此结果不能因输入文件中其它字段变化而
静默换用另一批素数。

## 线性源的完备平方根枚举

令

\[
u=\min(a,s),\quad v=\max(a,s).
\]

由式 (1) 得

\[
u^2\le as=\frac{p-a-s}{R}\le\frac{p-2}{3}, \tag{5}
\]

所以任意线性源都满足

\[
1\le u\le\left\lfloor\sqrt{\frac{p-2}{3}}\right\rfloor. \tag{6}
\]

固定 \(u\) 后又有

\[
p-u=v(1+uR). \tag{7}
\]

程序完整分解 \(p-u\)，按递增顺序枚举其全部正因子 \(q\)，保留

\[
q\equiv1\pmod u,\quad
R=\frac{q-1}{u}\equiv3\pmod4,\quad
v=\frac{p-u}{q}\ge u. \tag{8}
\]

若 \(v\) 为奇数，先取定向源 \((a,s)=(u,v)\)；若 \(u\) 为奇数且 \(u\ne v\)，再取
\((a,s)=(v,u)\)。这恢复全部以奇坐标作为 \(s\) 的定向线性源。目标可达性只依赖
\((p,R)\)，所以同一素数内重复出现的 \(R\) 只审计一次；若该 \(R\) 已完整失败，复用失败
结论不会丢失证书。若一个素数最终失败，程序才会扫描完式 (6) 的全部 \(u\)，并在结果中
展开保存全部唯一 \(R\) 审计。本次失败集合为空。

线性条件还自动给出

\[
s\le\frac{p-1}{4},\quad
n=p-s\ge\frac{3p+1}{4}, \tag{9}
\]

所以这些源不只是上半区偶源，而是位于最上四分之一区间。由 \(E\mid n\)，
[源平方正规分解](type-I-source-square-normal-factorization.md)中的源参数恒有
\(\beta=1\)。这与目标侧是否需要一般 \(B\) 是两个不同问题。

## 一般 \(B\) 的完整 MITM 判定

固定实际恢复的 \(R\)。程序精确分解 \(K\)，把 \(K^2\) 的全部素数幂菜单确定性地平衡
分为左右两块。因为 \((K,R)=1\)，左右除数 \(d_L,d_R\) 命中式 (3) 当且仅当

\[
d_R\equiv -4^{-1}d_L^{-1}\pmod R. \tag{10}
\]

两侧分别枚举所有除数，并比较右侧实际剩余类集合与左侧诱导的所需剩余类集合。因此每个
实际审计的 \(R\) 都是对**全部** \(d\mid K^2\) 的精确判定，不是小 \(B\)、小缺口或
因子个数截断。命中时选择最小的 \(d\)。互补因子 \(K^2/d\) 保持目标剩余类，故该最小
命中自动满足 \(d<K\)。

令

\[
g=(d,K),\quad
B_0=\frac d g,\quad C=\frac{g^2}{d},\quad H_0=\frac K g. \tag{11}
\]

则 \(B_0CH_0=K\)、\(B_0^2C=d\) 且 \((B_0,H_0)=1\)。若 \(H_0<B_0\)，程序交换
\(B_0,H_0\)，记定向后的值为 \(B,H\)。随后逐张检查

\[
A=\frac{B+H}{R},\quad
m=\frac{4B^2C+1}{R},\quad
3\le m\le p-2,\quad m\equiv3\pmod4, \tag{12}
\]

以及 \((A,B)=1\)、\(p=4ABC-m\)。每张证书最终用精确有理数重放

\[
\frac4p=\frac1{ABC}+\frac1{ACH}+\frac1{pK}, \tag{13}
\]

\[
\frac4n=\frac1{nK/E}+\frac1{ABC}+\frac1{ACH}. \tag{14}
\]

式 (14) 中 \(nK/E=aK\) 为整数，且所有 1,964 张证书的源正规化均重新得到
\(\beta=1\)。

## 搜索统计

确定性顺序在每个素数的首次命中后停止。累计统计为：

| 对象 | 数量 |
| --- | ---: |
| 输入核心素数 | 1,964 |
| 实际扫描的 \(u\) 值 | 3,597 |
| 枚举的 \(p-u\) 正因子 | 99,394 |
| 无序线性源候选 | 6,968 |
| 定向线性源候选 | 9,485 |
| 唯一 \(R\) 完整审计 | 6,656 |
| 审计中表示的 \(K^2\) 除子空间 | 3,638,456 |
| 递增直接枚举等价的首达前候选数 | 3,060,069 |
| MITM 两侧实际条目 | 202,644 |
| 成功点 | 1,964 |
| 失败点 | 0 |

所选见证进一步分为

\[
1964=1764_{B=1}+200_{B>1}, \tag{15}
\]

\[
1964=1091_{s=1}+873_{s>1}. \tag{16}
\]

这说明目标侧一般 \(B\) 在当前确定性选择中确实被使用。尤其，
[\(p=878089\) 的线性 \(B=1\) 全局反例](type-I-linear-shifted-source-counterexample-878089.md)
在本审计中由

\[
(a,s,R;A,B,C,H,m)=(4,3705,59;2,7,16669,111,55375)
\]

闭合。21 个全局 \(p-1\) 遗漏中线性 \(B=1\) 仍失败的
\(3942409,62588089,297640249,477015289\) 也全部由所选 \(B>1\) 线性证书闭合。
这不能推出未来所有压力点都只需线性源或有界 \(B\)。

首次命中所需的最大

\[
\min(a,s)=587
\]

唯一出现在 \(p=283319689\)。对应所选状态为

\[
(a,s,R)=(587,7661,63),\quad
(A,B,C,H,m)=(157051,11,41,9894202,315). \tag{17}
\]

结果还保存 \(a,s,R,K,A,B,C,H,m\) 各自的最大值及出现素数。全部所选见证按字段

~~~text
prime,a,s,R,K,matched_square_divisor,A,B,C,H,gap
~~~

组成 JSON 数组后，其规范 SHA-256 为
`461b9c7a816500fd9dc5ebff4e86f38352a0998667caf0f3a49b2f4270aadb7a`。

## 独立重放与证据文件

测试不调用生产实现的线性源恢复或 MITM 作为 oracle。它分别固定小 \(a\) 与小奇数 \(s\)，
从 \(s\mid p-a\) 和 \(a\mid p-s\) 两条定向通道恢复源状态；目标侧则直接枚举
\(K^2\) 的全部正因子。独立 oracle 至少覆盖：

- \(p=878089\)，并重现 54 个定向线性源、24 个不同 \(R\) 和 \(B=1\) 零命中；
- 合并输入的前 13 点；
- 21 个全局 \(p-1\) 遗漏；
- 最难首达点 \(p=283319689\)。

测试还逐张重放全部 1,964 个源与目标 `Fraction` 恒等式，并从 MITM 两侧素数幂菜单
重建所选 \(R\) 的完整笛卡尔积命中。

- 实现：
  [`type_i_linear_source_general_b_completion_profile_600m.py`](../reproductions/type_i_linear_source_general_b_completion_profile_600m.py)
- 结果：
  [`type-i-linear-source-general-b-completion-profile-600m-results.json`](../reproductions/type-i-linear-source-general-b-completion-profile-600m-results.json)
- 独立重放：
  [`test_type_i_linear_source_general_b_completion_profile_600m.py`](../tests/test_type_i_linear_source_general_b_completion_profile_600m.py)

~~~bash
python3 reproductions/type_i_linear_source_general_b_completion_profile_600m.py
python3 -m unittest tests.test_type_i_linear_source_general_b_completion_profile_600m -v
~~~
