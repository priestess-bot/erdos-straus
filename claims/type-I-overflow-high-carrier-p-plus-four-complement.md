---
kind: claim
claim_id: type-I-overflow-high-carrier-p-plus-four-complement
title: 高载体 overflow 的 p+4 互补分流
statement: 设核心素数 p≡1 (mod 24) 的 verified overflow 满足 pn=4Md+1、R_M=4M-n>p、1≤d<p，并令 B_p=(p-1)^2/4。若 M>B_p，则精确边界为 n=p 或 n≥p+4。若 p+4 含素因子 q≡3 (mod 4)，取 m=q、x=(p+m)/4，则 m|p+4、m|x+1，并给出精确 Type II 恒等式 4/p=1/x+1/(p(x+1)/m)+1/(px(x+1)/m)。若 p+4 不含 q≡3 (mod 4) 因子，该分支只给出明确的 factor-filter hard core，不产生递归边或猜想反例。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-same-chart-support-promotion
  - type-I-overflow-high-carrier-fixed-n-R-descent
  - four-p-plus-one-type-ii-certificate
topics:
- type-I
- overflow
- high-carrier
- complement-boundary
- p-plus-four
- type-II
- terminal-selector
- proof-boundary
sources:
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: high-carrier complement classifier and exact Type II construction
  - result: reproductions/type-i-representation-dual-capacity-selector-results.json
    role: focused high-carrier replay
visibility: public
last_checked: '2026-08-04'
---

# 高载体 overflow 的 \(p+4\) 互补分流

## 1. 高载体必有大互补量

设

\[
pn=4Md+1,
\qquad R_M=4M-n>p,
\qquad B_p=\frac{(p-1)^2}{4},
\qquad M>B_p.
\]

由于 \(d\ge1\)，有

\[
Md=\frac{pn-1}{4}>B_p.
\tag{1}
\]

又 \(p\equiv1\pmod4\) 且 \(pn=4Md+1\)，故 \(n\equiv1\pmod4\)。如果

\[
n\le p-4,
\]

则

\[
Md=\frac{pn-1}{4}
\le \frac{p(p-4)-1}{4}<B_p;
\]

而 \(n=p\) 时

\[
Md=\frac{p^2-1}{4}=B_p+\frac{p-1}{2}>B_p,
\]

所以 \(n=p\) 恰好是允许的边界；下一种可能值才是 \(n\ge p+4\)。因此

\[
\boxed{M>B_p\Longrightarrow n=p\ \text{或}\ n\ge p+4.}
\tag{2}
\]

这是对高载体 determinant 残差的无条件补余项分类，不依赖固定-\(n\) 除子是否存在，
也不把 \(M>B_p\) 误写成已经闭合的 overflow 分支。

## 2. \(p+4\) 因子给出的终端

若 \(q\mid p+4\) 且 \(q\equiv3\pmod4\)，令

\[
m=q,
\qquad x=\frac{p+m}{4}.
\]

那么 \(x\) 是正整数。因为 \(q\mid p+4\) 且 \(q\) 为奇数，

\[
q\mid x+1=\frac{p+q+4}{4}.
\]

取

\[
y=\frac{p(x+1)}{q},
\qquad
z=\frac{px(x+1)}{q},
\]

直接计算得到

\[
\frac1x+\frac1y+\frac1z
=\frac1x+\frac{q}{p(x+1)}+\frac{q}{px(x+1)}
=\frac{4}{p}.
\]

所以该条件下是 `terminal_leaf`，无需先进入 overflow 递降。注意这里的条件是
“\(p+4\) 有一个 \(3\pmod4\) 素因子”，不能推广为所有核心素数的自动终端。

## 3. hard-core 边界

若 \(p+4\) 的所有素因子均为 \(1\pmod4\)，上述 \(p+4\) 家族没有可用的 \(q\)。
选择器保留 `analysis_evidence` 并明确缺失条件
`q_congruent_3_mod_4_factor`，后续仍须使用其它 Type I/II、alternate、容量或良基
support reset。一个不带来源可达性主张的算术边界例子是

\[
(p,M,d,n)=(97,2449,1,101),
\qquad B_{97}=2304,
\qquad p+4=101,
\]

其中 \(M>B_p\)、\(R_M=9695>p\)，但 \(101\equiv1\pmod4\)。此外
\((97,2352,1,97)\) 展示了允许的精确边界 \(n=p\)。这些例子只测试分流边界，
不构成 Erdos--Straus 猜想的反例，也不带 raw Reach/source provenance。

## 4. 聚焦回放

统一选择器新增
`overflow_high_carrier_p_plus_four_complement`，在 overflow 其它递降分支之前执行。
12 个冻结来源行中：

| 项目 | 数值 |
|---|---:|
| 高载体行 | 1 |
| 低载体不适用 | 11 |
| \(p+4\) Type II 终端 | 1 |
| factor-filter hard core | 0 |

唯一高载体来源行是

\[
(p,M,d,n)=(73,1518,28,2329),
\qquad B_{73}=1296,
\qquad p+4=77=7\cdot11,
\]

取 \(q=7\) 得 \(x=20\)，精确终端分母为

\[
(x,y,z)=(20,219,4380).
\]

复现：

```text
python3 reproductions/type_i_representation_dual_capacity_selector.py --verify
```

## 5. 逻辑边界

该分流真正推进的是高载体残差的量词分类和一个直接终端子族；它没有证明所有
\(p+4\) 都有 \(3\pmod4\) 因子，也没有关闭没有该因子的高载体 hard core。主目标仍需
在这类行上构造 alternate/容量证书或全局良基递降。
