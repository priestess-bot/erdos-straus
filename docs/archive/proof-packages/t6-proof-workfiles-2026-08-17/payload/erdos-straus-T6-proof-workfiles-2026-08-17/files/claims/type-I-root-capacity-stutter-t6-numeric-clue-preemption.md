---
kind: claim
claim_id: type-I-root-capacity-stutter-t6-numeric-clue-preemption
title: T6 proper-root 数值线索的 root-provenance 失败与 gap-3 终端抢占
statement: >-
  对 T6-V1 中记录的数值线索 p=20065847377、m=6768、a=141、k=3，
  将 proper-root quotient 恒等式反解得到唯一正整数候选
  u=46126129、h=138378387、e=20446、D=135805516669150，且
  N=a^2-a(e-1)+(e-1)^2=3h。然而
  p^2+p+1 除以 h 的余数为 39277161，故 h 不整除 p^2+p+1，u 也不可能是
  gcd(2r+1,(p^2+p+1)/3)；该线索不是 actual proper-root receipt。
  独立地，x=(p+3)/4=5016461845 含素因子 5=2 mod3，故 d=5 给出直接
  gap-3 Type II 证书并由 terminal-first 抢占。该审计只删除一个数值线索，
  不证明 actual proper-root stutter 域为空，也不关闭 T6。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-pair-root-divisor-gate
  - type-I-root-capacity-stutter-positive-definite-norm-bound
  - gap-three-criterion
  - short-certificate-equivalence
topics:
  - type-I
  - root-capacity
  - stutter
  - T6
  - numeric-control
  - terminal-first
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_root_capacity_stutter_t6_numeric_clue_preemption.py
    role: exact-reconstruction-root-divisibility-and-terminal-control
visibility: public
last_checked: '2026-08-17'
---

# T6 proper-root 数值线索的 root-provenance 失败与 gap-3 终端抢占

## 1. 被审核的线索

T6 技术备忘录记录了

\[
p=20\,065\,847\,377,\qquad m=6768,\qquad a=141,\qquad k=3.
\tag{1}
\]

它只被列为“未验证线索”。下面证明它不能提升为 actual proper-root stutter
receipt。

## 2. 唯一正根重建

沿用 parameter-pair root-divisor gate 的记号

\[
L=am=954288,\qquad s=m-a=6627.
\]

任一对应的 root height \(u>0\) 必满足

\[
9u^2+3(a-1)u+s=Lp.
\tag{2}
\]

式 (2) 的判别式为

\[
\Delta=689349505021230564=830270742^2,
\]

所以唯一正整数根为

\[
u=46126129.
\]

随后所有 stutter 参数都被强制为

\[
h=3u=138378387,
\qquad
e=\frac{a+3u}{m}=20446,
\]

\[
D=mp+1-h=135805516669150.
\tag{3}
\]

直接重算给出

\[
eD=ph+1,
\qquad
a=em-h,
\]

以及

\[
N=a^2-a(e-1)+(e-1)^2=415135161=3h.
\tag{4}
\]

因此 (1) 确实能重建抽象 quotient 曲线，且其形式商为 \(k=N/h=3\)。

## 3. Actual root provenance 失败

actual root endpoint 必须满足

\[
h\mid p^2+p+1,
\qquad
u=\gcd\!\left(2r+1,\frac{p^2+p+1}{3}\right)
\]

对某个真实 source 坐标 \(r\) 成立。但 (1)--(3) 给出

\[
p^2+p+1
=h\cdot 2909690159758+39277161.
\tag{5}
\]

余数非零，故 \(h\nmid p^2+p+1\)。特别地 \(u\) 不整除
\((p^2+p+1)/3\)，所以它不可能成为上述 gcd。这个失败发生在 source/root
provenance，早于 maximal complete-excess normalization 和 E1--E5。

## 4. Terminal-first 还会独立抢占

该素数还有一张直接 gap-3 Type II 证书。令

\[
x=\frac{p+3}{4}=5016461845=5\cdot1003292369,
\qquad d=5.
\]

则 \(d\mid x^2\)、\(d\le x\)，且 \(3\mid x+d\)。按短证书恢复式，

\[
(X,Y,Z)=
(
5016461845,
33553185951547689150,
33663655420825800263779096350
)
\]

满足

\[
\frac4p=\frac1X+\frac1Y+\frac1Z.
\tag{6}
\]

所以即使忽略 (5)，terminal-first 也会在进入 proper-root stutter 分支前终止该
\(p\)。

## 5. 边界

本卡只完成对 (1) 这一条数值线索的精确审计。它不说明其它参数是否产生 actual
proper-root stutter，也不把 Eisenstein quotient chart 变成 persistent successor，因而不
构成 T6 totality 或 Erdős--Straus 猜想的证明。

一般 (k=1) 的精确参数化与仍未完成的 quotient/transverse carrier 全称量词，另见
[T6 proper-root 最小缺口审计](../docs/T6-proper-root-minimal-gap-audit-2026-08-17.md)。

## 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_stutter_t6_numeric_clue_preemption.py --verify
```
