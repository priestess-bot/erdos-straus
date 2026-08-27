---
kind: claim
claim_id: t6-q-one-finite-bradford-prefix-through-23-partition-v1
title: q=1 根的有限 Bradford 自然前缀全除子分割定理 v1
statement: >-
  Let p be a prime congruent to 1 modulo 4 and let B be a fixed integer with
  3 <= B <= p-2 and B congruent to 3 modulo 4. For every natural gap
  m=3,7,...,B, put x_m=(p+m)/4 and enumerate every positive divisor of
  x_m^2. Testing the complete Bradford Type I and Type II congruences in the
  fixed order (m, divisor, Type I before Type II) yields a finite canonical
  screen: a nonempty hit set has a unique earliest terminal certificate, and
  an empty hit set proves exactly the registered-prefix miss through B. Hence
  every supplied source domain is the disjoint union of its earliest-hit
  leaves and its prefix-miss residual. At B=23, the actual parentless ordinary
  q=1 G owner domain is partitioned by the six gaps 3,7,11,15,19,23 into
  terminal leaves and D_23. This is not a complete terminal-universe theorem:
  gaps from 27 onward are outside the conclusion, global_exhaustion is false,
  and p=21169 satisfies the arithmetic D_23 guard but has a gap-31 Type II
  certificate. Membership of an authenticated p=21169 source in D_23 remains
  conditional on separately supplying that source in D_G.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - short-certificate-equivalence
topics:
  - T6
  - q-one
  - terminal-first
  - Bradford
  - finite-prefix
  - divisor-enumeration
  - source-partition
  - proof-boundary
sources:
  - claim: short-certificate-equivalence
    role: complete Type I/II divisor parametrization and reconstruction
  - claim: type-I-type-II-gap-23-two-box-classification
    role: complete gap-23 classification and the p=21169 six-gap MISS control
  - review: docs/audits/T6_Q1_GAP23_TWO_BOX_INDEPENDENT_REVIEW_2026-08-27.md
    role: independent review of the single-gap theorem and p=21169 control
  - data: reproductions/short-certificate-results.json
    role: exact p=21169 gap-31 Type II anti-global control
visibility: public
last_checked: '2026-08-27'
---

# q=1 根的有限 Bradford 自然前缀全除子分割定理 v1

## 1. 一般有限前缀

令 \(p\equiv1\pmod4\) 为素数，固定

\[
3\le B\le p-2,
\qquad B\equiv3\pmod4,
\]

并定义自然前缀

\[
M_B=\{3,7,\ldots,B\}.
\tag{1}
\]

对每个 \(m\in M_B\)，令

\[
x_m=\frac{p+m}{4}.
\tag{2}
\]

由 \(m<p\)、\(p\) 为素数以及 \(4x_m=p+m\)，有

\[
\gcd(p,m)=\gcd(x_m,m)=\gcd(x_m,p)=1.
\tag{3}
\]

定义两个完整的单-gap 命中集合

\[
\mathcal B_m^{\rm I}(p)
=\{d:d\mid x_m^2,\ m\mid px_m+d\},
\tag{4}
\]

\[
\mathcal B_m^{\rm II}(p)
=\{d:d\mid x_m^2,\ d\le x_m,\ m\mid x_m+d\}.
\tag{5}
\]

这里的“完整”只指：在固定 \(m\) 上检查 \(x_m^2\) 的每个正除子，并同时检查
Type I 与 Type II；它不包含 \(M_B\) 之外的 gap。

## 2. 全 divisor screen 的完备性

写出 \(x_m\) 的完整素因子分解

\[
x_m=\prod_{i=1}^r\ell_i^{a_i}.
\tag{6}
\]

则 \(x_m^2\) 的正除子恰为

\[
d=\prod_{i=1}^r\ell_i^{e_i},
\qquad 0\le e_i\le2a_i.
\tag{7}
\]

因此有限笛卡尔积 (7) 既不遗漏除子，也不重复除子。对其中每个 \(d\)，条件
(4)--(5) 是精确整数判定。

若 \(d\in\mathcal B_m^{\rm I}(p)\)，令

\[
y=\frac{px_m+d}{m},
\qquad
z=\frac{p(x_m+p x_m^2/d)}{m}.
\tag{8}
\]

第一项由 (4) 为整数。又 \(d\equiv-px_m\pmod m\)，结合 (3) 得

\(\gcd(d,m)=1\)。将 \(x_m+p x_m^2/d\) 乘以 \(d\)，所得

\[
d x_m+p x_m^2=x_m(d+px_m)
\]

被 \(m\) 整除，所以 (8) 的 \(z\) 也是整数。直接代入得到

\[
\frac4p=\frac1{x_m}+\frac1y+\frac1z.
\tag{9}
\]

若 \(d\in\mathcal B_m^{\rm II}(p)\)，令

\[
y=\frac{p(x_m+d)}m,
\qquad
z=\frac{p(x_m+x_m^2/d)}m.
\tag{10}
\]

同理，\(d\equiv-x_m\pmod m\) 给出 \(\gcd(d,m)=1\)，而

\[
d x_m+x_m^2=x_m(d+x_m)
\]

被 \(m\) 整除，故 (10) 为整数并满足 (9)。条件 \(d\le x_m\) 是 Type II
反向参数化中的精确界。

反方向由 `short-certificate-equivalence` 给出：固定首分母 gap \(m\) 的每张有序
Type I 或 Type II 解都会恢复一个分别属于 (4) 或 (5) 的除子。因此，对每个
\(m\in M_B\)，(6)--(7) 的全枚举命中当且仅当该注册 Bradford family 在该 gap
命中。

## 3. 唯一 earliest-hit 分割

令

\[
\mathcal H_B(p)=
\{(m,d,\tau):m\in M_B,
\ d\in\mathcal B_m^\tau(p),
\ \tau\in\{\mathrm I,\mathrm{II}\}\}.
\tag{11}
\]

按以下 key 严格全序排列：先比较 \(m\)，再比较 \(d\)，最后在相同 \((m,d)\)
处规定 Type I 先于 Type II。因为 \(M_B\) 与每个 divisor lattice 都有限，
\(\mathcal H_B(p)\) 有限。若它非空，则存在唯一最小元素

\[
h_B(p)=\min\mathcal H_B(p),
\tag{12}
\]

并由 (8) 或 (10) 唯一确定规范 terminal 输出。若它为空，则精确结论只是

\[
\forall m\in M_B,\qquad
\mathcal B_m^{\rm I}(p)=
\mathcal B_m^{\rm II}(p)=\varnothing.
\tag{13}
\]

现在令 \(\mathcal D\) 是任意 supplied source domain，并要求每个
\(S\in\mathcal D\) 都绑定满足
\(p(S)\equiv1\pmod4\)、\(B\le p(S)-2\) 的根素数 \(p(S)\)。
定义 earliest-hit leaves

\[
\mathcal T_h=
\{S\in\mathcal D:h_B(p(S))=h\}
\tag{14}
\]

以及 prefix residual

\[
\mathcal D_B=
\{S\in\mathcal D:\mathcal H_B(p(S))=\varnothing\}.
\tag{15}
\]

有限全序集非空时有唯一最小元素，空时满足 (13)，故

\[
\boxed{
\mathcal D=
\left(\coprod_h\mathcal T_h\right)
\coprod\mathcal D_B.
}
\tag{16}
\]

式 (16) 是集合论上的互斥、穷尽分割；它不建立 \(\mathcal D\) 的 source actualness，
也不授予任一 schedule、issuer、E1 或 queue 权限。

## 4. q=1、B=23 的专门化

令 \(\mathcal D_G\) 表示 supplied source 已另行证明为 actual、parentless、ordinary
\(q=1\) G root，且 common owner 为 `type_ii_relation_g_endpoint` 的精确 owner-domain。
本命题不从字符串 label 推导这些前提。

取

\[
M_{23}=\{3,7,11,15,19,23\},
\tag{17}
\]

并记

\[
\mathcal D_{23}
=\left\{S\in\mathcal D_G:
\mathcal B_m^{\rm I}(p(S))=
\mathcal B_m^{\rm II}(p(S))=\varnothing
\text{ for every }m\in M_{23}\right\}.
\tag{18}
\]

则 (16) 给出

\[
\boxed{
\mathcal D_G=
\left(\coprod_{h\text{ over }M_{23}}\mathcal T_h\right)
\coprod\mathcal D_{23}.
}
\tag{19}
\]

所以把 future phase-root producer 的 source domain 收紧到 \(\mathcal D_{23}\) 不会删除
原 \(\mathcal D_G\) 中的其它 source：每个被排除的 source 都必须携带 (12) 的直接
terminal certificate。反之，仅把 owner 命名为“terminal-first survivor”而不提供
(6)--(13) 的 replay，不能引用 (19)。

## 5. 精确控制

下面各行都使用完整 divisor screen；表中的 hit 是该 prime 在 \(M_{23}\) 中的 earliest
hit。

| \(p\) | \(M_{23}\) 结果 | 规范控制 |
|---:|---|---|
| \(241441\) | terminal | gap 11, Type II, \(x=60363,d=27\)；历史 \(d=1083\) 也命中但不先于 \(d=27\) |
| \(12721\) | terminal | gap 19, Type II, \(x=3185,d=7\)；否定把 \([3,7,11,23]\) 宣称为 through-23 natural prefix |
| \(1201\) | terminal | gap 23, Type I, \(x=306,d=34\) |
| \(2521\) | terminal | gap 23, Type II, \(x=636,d=8\) |
| \(21169\) | arithmetic \(\mathcal D_{23}\) guard | gaps \(3,7,11,15,19,23\) 的两类 screen 全 MISS |

最后一行只证明：若一个已认证的 \(p=21169\) source 被另行供应在
\(\mathcal D_G\) 中，则它属于 \(\mathcal D_{23}\)；本命题本身不供应该 source
membership。这个算术 guard 也不是全局 miss。仓库的精确控制给出

\[
p=21169,\qquad m=31,\qquad x=5300,\qquad d=1,
\]

以及 Type II terminal

\[
\frac4{21169}
=\frac1{5300}
+\frac1{3619899}
+\frac1{19185464700}.
\tag{20}
\]

因此 \(B=23\) schedule 必须记录 `next_unchecked_gap=27`、
`coverage_semantics=REGISTERED_PRIORITY_ONLY` 和 `global_exhaustion=false`。

## 6. 证明边界

本命题建立一般有限 Bradford 前缀的全 divisor coverage、规范 precedence 与 source-set
分割，并给出 \(B=23\) 的 q=1 数学实例。它不证明：

- \(\mathcal D_G\) 的 actualness 或 V5/V6/V7 authority；
- \(M_{23}\) 是所有可能或所有已知 terminal templates 的全集；
- gaps \(27,31,\ldots,p-2\) MISS；
- 一个 production COMPLETE schedule、E1--E5、producer admission 或 re-entry；
- Gate 4、Gate 5、F1、F2、F3、T6 或 Erdős--Straus 猜想闭合。

若将“complete terminal schedule”解释成全部自然 Bradford range，
`short-certificate-equivalence` 表明其 HIT 等价于
\(\operatorname{Sol}(p)\ne\varnothing\)，其语义 MISS 则是候选反例而不能继续伪装成普通
prefix MISS。本命题只支持 versioned registered-prefix 语义。
