---
kind: claim
claim_id: type-II-h19-ac6-tail-deflation-profile
title: H19 十亿残余的半径六 AC 或 Type II 双尾严格递降闭合
statement: 对存储的 p<=10^9 的664个 H19 残余，647个有 max(A,C)<=6 的直接 AC Type II 证书；其余17个全部有 Type II 双尾缩减严格递降。最小双尾缺口分布为3:3、7:5、11:4、15:2、19:2、27:1，最大仅27。因此该固定剖面由“半径六直接证书或缺口至多27的双尾递降”闭合；这不是全称选择器定理。
claim_status: computationally_reproduced
topics:
- type-II
- ac-rays
- descent
- short-certificate
- finite-audit
- h19
sources:
- paper: bradford2024
  locator: Propositions 2 and 3
  role: Type-II-certificate-and-lift-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-prime-shape-context
visibility: public
last_checked: '2026-07-27'
---

# H19 十亿残余的半径六 AC 或 Type II 双尾严格递降闭合

对 H19 规范扇留下的 664 个残余，先检查半径

\[
\max(A,C)\le6
\]

的直接 AC Type II 证书。647 个直接命中。对余下17个，枚举 \(p-1\) 的所有四的倍数
\(m+1\)，并检查缺口 \(m\) 的 Type II 证书是否允许两个 \(p\)-可除尾同时缩减：

\[
\frac4p=\frac1x+\frac1{pY}+\frac1{pZ}
\quad\Longrightarrow\quad
\frac4n=\frac1x+\frac1Y+\frac1Z,\qquad
n=\frac{p+m}{m+1}<p. \tag{1}
\]

每一项均以精确有理数验证，故 (1) 是真实的严格递降，而不是只重写目标证书。

| 最小双尾缺口 \(m\) | 状态数 |
| ---: | ---: |
| 3 | 3 |
| 7 | 5 |
| 11 | 4 |
| 15 | 2 |
| 19 | 2 |
| 27 | 1 |

17 个半径六遗漏全部命中，最大最小缺口为27。于是固定十亿剖面满足

\[
\boxed{\text{半径六直接 AC 证书}\quad\text{或}\quad
\text{缺口 }m\le27\text{ 的 Type II 双尾严格递降}.} \tag{2}
\]

这条分流比 mixed-factor 版本更独立于外源因子支持。特别地，mixed 因子至少需要三种
素因子的边界点

\[
p=942{,}584{,}161
\]

仍有缺口 \(15\) 的双尾缩减，并严格降至

\[
n=\frac{p+15}{16}=58{,}911{,}511.
\]

因此三素因子现象是 mixed 选择器的真实边界，但不是该点唯一、更不是该点必需的递降机制。

范围仍是有限的：H19、十亿上界、半径6和缺口27没有被提升为全称界。一般证明需要说明
为何短证书失败会强制某个可控双尾缩减，或找到另一种对所有残余有效的出口。

可复现命令：

~~~bash
python3 reproductions/type_ii_h19_ac6_tail_deflation_profile.py \
  --input reproductions/type-ii-h19-residual-ac-profile-1b-results.json \
  --ac-bound 6 \
  --output reproductions/type-ii-h19-ac6-tail-deflation-profile-1b-results.json
python3 -m unittest tests/test_type_ii_h19_ac6_tail_deflation_profile.py -q
~~~
