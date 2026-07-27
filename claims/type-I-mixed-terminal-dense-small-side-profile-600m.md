---
kind: claim
claim_id: type-I-mixed-terminal-dense-small-side-profile-600m
title: 五亿至六亿连续区间的 Type I 回退全部可选上半区偶源
statement: 对500000000<p<=600000000的621951个核心素数，621704个具有普通 Type II p-1 双尾证书。余下247个在m<=215的完整 Type I 正规形盒内均有小侧a<b的偶源桥，等价地均有n≥(p+1)/2的偶源；其中205个首次存储桥已经小侧，42个首次桥为大侧但均由替代正规形释放。故这个连续有限区间的混合终端闭合可强化为“普通双尾或上半区偶源”。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- type-II
- terminal-bridge
- even-source
- upper-half-source
- divisor-pairs
- finite-audit
- mixed-selector
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-and-Type-II-certificate-context
visibility: public
last_checked: '2026-07-28'
---

# 五亿至六亿连续区间的 Type I 回退全部可选上半区偶源

从[五亿至六亿连续核心区间的混合终端闭合](type-I-mixed-terminal-dense-600m.md)取出全部
247 条普通 Type II \(p-1\) 双尾遗漏。每条存储的 Type I 终端桥先以精确整数和有理数
重建：正规形、桥因子、目标三元组和源三元组均须成立。写

\[
L=2K,\qquad\frac EL=\frac ab,\qquad(a,b)=1.
\]

若首次桥有 \(a>b\)，就完整枚举同一有限盒

\[
3\le m\le215,\qquad m\equiv3\pmod4
\]

中的所有 Type I 正规形及严格偶源最大尾反向提升，保留 \(a<b\) 的替代桥。按
[小侧简化引理](type-I-normal-even-source-small-side-simplification.md)，这正等价于源

\[
n\ge\frac{p+1}{2}.
\]

## 结果

| 项目 | 数值 |
| --- | ---: |
| 区间内核心素数 | 621,951 |
| 普通 Type II \(p-1\) 双尾 | 621,704 |
| Type I 回退记录 | 247 |
| 首次桥已为小侧 | 205 |
| 首次桥为大侧 | 42 |
| 大侧记录的替代小侧桥 | 42 |
| 小侧遗漏 | 0 |
| 替代搜索的正规形 | 2,430 |
| 替代搜索的严格反向边 | 6,561 |

所以该区间有精确分流

\[
621{,}951
=621{,}704_{\mathrm{ordinary\ Type\ II\ tail}}
+247_{\mathrm{Type\ I\ upper\!-!half\ source}}.
\]

首个需要重选正规形的点为 \(p=500{,}019{,}529\)。它的首次桥来自

\[
(m,A,B,C)=(71,30489,1,4100)
\]

且为大侧 \((a,b)=(165148,87425)\)，源仅为 \(27{,}744{,}864\)。在另一张正规形

\[
(m,A,B,C)=(95,478946,1,261)
\]

中，桥 \(E=12\) 给出 \((a,b)=(2,458351235)\) 与源
\(n=500{,}019{,}528\)，即 \(p-1\)。这说明“首次偶源”不能代表最终的源深度，必须允许
跨正规形重选。

## 范围

这是一个连续有限区间和明确 \(m\le215\) 正规形盒的可复现实验。它不证明所有核心素数
都有 Type I 正规形，也不提供统一缺口界；因此“普通双尾或上半区偶源”在这里是被支持的
强化研究目标，不是全称定理。

重建命令：

~~~bash
python3 reproductions/type_i_mixed_terminal_dense_small_side_profile.py
python3 -m unittest tests/test_type_i_mixed_terminal_dense_small_side_profile.py -q
~~~
