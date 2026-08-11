---
kind: claim
claim_id: type-I-type-II-mod-three-double-g-exit-obstruction
title: 模三双 G 出口的精确等价与小缺口严格反例
statement: >-
  对核心素数 p=24t+1，令 X=(p+3)/4=6t+1、N=(3p+1)/4=18t+1。
  p-1 Type II 的 q=1、m=3 端点为 G，当且仅当 X 的全部素因子均为
  1 mod 3；这也当且仅当 gap 3 没有 Type I/II 短证书。Type I 的
  R=3 中心图表为 G，当且仅当 N 的全部素因子均为 1 mod 3；这也当且
  仅当既有 (3p+1)/4 标记递降源集为空。两种 G 障碍可以同时发生：p=241
  给出最小控制。更强地，p=2521 同时为双 G，且 gaps 3,7,11,15,19
  均无 Type I/II 证书；其首个短证书为 gap 23 的 Type II 证书
  x=636,d=8。因此 q=1 G 不能仅由 R=3 伴随图表、(3p+1)/4 递降或
  固定到 gap 19 的小缺口扇全称闭合。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - gap-three-criterion
  - three-p-plus-one-descent-certificate
  - type-II-relation-reach-gcd-shadow-endpoint-descent
topics:
  - type-I
  - type-II
  - G-state
  - gap-three
  - mod-three
  - descent
  - strict-counterexample
  - selector
sources:
  - claim: gap-three-criterion
    role: exact-gap-three-certificate-equivalence
  - claim: three-p-plus-one-descent-certificate
    role: exact-R-three-marked-source-equivalence
  - reproduction: reproductions/type_i_type_ii_mod_three_double_g_exit_obstruction.py
    role: focused-double-G-and-first-terminal-verifier
visibility: public
last_checked: '2026-08-12'
---

# 模三双 G 出口的精确等价与小缺口严格反例

## 1. 两个规范模三状态

令

\[
p=24t+1,
\qquad
X=\frac{p+3}{4}=6t+1,
\qquad
N=\frac{3p+1}{4}=18t+1.
\tag{1}
\]

两数均为 \(1\pmod3\)，因而都与 3 互素。

Type II 的 \(q=1\) 端点具有

\[
m=3,\qquad x=X.
\tag{2}
\]

其源群是 \(X\) 的素因子在 \(U(3)=\{1,-1\}\) 中生成的群。目标为
\(-1\)。所以目标在源群外，当且仅当每个素因子 \(\ell\mid X\) 都满足

\[
\ell\equiv1\pmod3.
\tag{3}
\]

这正是该端点的 G 分类。另一方面，gap-three-criterion 已证明 gap 3 存在
Type I 或 Type II 证书，当且仅当 \(X\) 含有 \(2\pmod3\) 的素因子。因此

\[
\boxed{
q=1\text{ Type II 为 G}
\iff
\text{gap }3\text{ 无 Type I/II 证书}.}
\tag{4}
\]

再看 Type I 的 \(R=3\) 中心图表。由 \(4K=pR+1\) 得

\[
K=N.
\tag{5}
\]

中心目标同样是 \(-1\)，源群由 \(N\) 的素因子模 3 生成。因此

\[
R=3\text{ Type I 为 G}
\iff
\text{每个 }\ell\mid N\text{ 都有 }\ell\equiv1\pmod3.
\tag{6}
\]

three-p-plus-one-descent-certificate 又给出：其标记源集非空，当且仅当
\(N\) 含有 \(2\pmod3\) 的素因子。故

\[
\boxed{
R=3\text{ Type I 为 G}
\iff
W_p^{(3p+1)/4}=\varnothing.}
\tag{7}
\]

式 (4) 与 (7) 是两个不同线性型上的条件，不存在互补性。

## 2. 最小双 G 控制

取 \(p=241\)。此时

\[
X=61,
\qquad
N=181.
\tag{8}
\]

二者都是 \(1\pmod3\) 的素数，所以 (4)、(7) 同时给出 G。该素数仍由
gap 7 的 \(d=1\) Type II 证书终止；它说明双 G 不是猜想反例，但严格否定
“两个模三状态必有一个非 G”的候选出口。

## 3. 逃过前五个缺口的严格反例

取

\[
p=2521,
\qquad
X=631,
\qquad
N=1891=31\cdot61.
\tag{9}
\]

这里 \(631,31,61\) 均为 \(1\pmod3\)，故仍为双 G。对
\(m\in\{3,7,11,15,19\}\)，相应 \(x=(p+m)/4\) 及其平方除子剩余谱如下：

| \(m\) | \(x\) | \(\{d\bmod m:d\mid x^2\}\) | Type I 目标 | Type II 目标 |
|---:|---:|---|---:|---:|
| 3 | \(631\) | \(\{1\}\) | 2 | 2 |
| 7 | \(632=2^3\cdot79\) | \(\{1,2,4\}\) | 5 | 5 |
| 11 | \(633=3\cdot211\) | \(\{1,2,3,4,6,7,9\}\) | 10 | 5 |
| 15 | \(634=2\cdot317\) | \(\{1,2,4,8\}\) | 11 | 11 |
| 19 | \(635=5\cdot127\) | \(\{1,2,5,6,7,8,9,13,17\}\) | 10 | 11 |

Type I 目标是 \(-px\pmod m\)，Type II 目标是 \(-x\pmod m\)。表中两种
目标均不在相应完整平方除子谱内，所以五个缺口全部严格失败。

下一个缺口 \(m=23\) 有

\[
x=636,
\qquad
d=8\mid636^2,
\qquad
8<636,
\qquad
8\equiv-636\pmod {23}.
\tag{10}
\]

故它是一张 Type II 证书，并恢复

\[
\frac4{2521}
=\frac1{636}+\frac1{70588}+\frac1{5611746}.
\tag{11}
\]

因此 \(p=2521\) 的首个自然短证书恰在 gap 23。

## 4. 对全局出口的约束

该结果关闭三个过强的候选命题：

1. \(q=1\) Type II G 不强制 \(R=3\) Type I 非 G；
2. 双 G 不强制 gap 7 或 gap 11 命中；
3. 把固定缺口扇截到 19 仍不能承担 G 出口的全称量词。

它不排除自适应选择更大的缺口，也不构造真分母递降。正向定理必须读取比两个
模三生成子群更丰富的数据，例如跨模数除子谱、实际 Type I source，或一个具有
非循环全域提升公式的较小分母状态。

聚焦验证：

~~~bash
python3 reproductions/type_i_type_ii_mod_three_double_g_exit_obstruction.py --verify
~~~
