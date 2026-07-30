---
kind: claim
claim_id: type-I-f-overflow-lower-modulus-shared-gap-type-ii-lift
title: 盒内命中的共享缺口 Type II 旁路提升
statement: 对六个端点下降后的 lower-modulus F-box hit，完整枚举原 K 指数盒内的所有 a/b=-1 (mod t) 表示，再枚举每个 a+b 的合法因子 m' 并独立检查 Type II 正规形。50 个表示、25 个不同和、101 个共享缺口候选中得到 4 张有效 Type II 证书，覆盖 p=57399241、242042089、475619929 三个素数；该流程是有限共享缺口接口，不是自动提升定理。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-overflow-balanced-lower-modulus-fiber-profile
  - type-II-coprime-factor-normal-form
topics:
- type-I
- F-state
- finite-box
- shared-gap
- type-II
- normal-form
- lift
- computational-audit
- proof-program
sources:
- claim: type-I-f-overflow-balanced-lower-modulus-fiber-profile
  role: lower-hit-input
- claim: type-II-coprime-factor-normal-form
  role: independent-Type-II-test
visibility: public
last_checked: '2026-07-30'
---

# 盒内命中的共享缺口 Type II 旁路提升

## 有限桥接流程

严格端点下降给出 \(t=R/m\equiv1\pmod4\)。对一个 lower-modulus F-box hit，取

\[
\frac ab=\prod_iq_i^{z_i},\qquad -\nu_i\le z_i\le\nu_i,\qquad
a\equiv-b\pmod t,\qquad (a,b)=1.
\]

令 \(S=a+b\)。若

\[
m'\mid S,\qquad m'\equiv3\pmod4,\qquad 3\le m'\le p-2,
\tag{1}
\]

则 \(m'\) 是一个**共享缺口候选**：它同时承载低模数表示的和，而不是说它已经是
Erdős--Straus 证书。设

\[
x'=\frac{p+m'}4.
\]

只有在独立找到互素 \(A\le B\)、\(C\ge1\) 使

\[
x'=ABC,\qquad m'\mid A+B,\qquad d=A^2C
\tag{2}
\]

时，Type II 正规形才给出有效除子证书。这里不要求 \(A,B\) 等于低模数表示的
\(a,b\)；事实上它们通常不相等，也不必整除同一个 \(x'\)。因此 (1) 是候选筛，(2)
是独立的提升检验。

## 冻结审计

复现脚本和结果：

~~~text
reproductions/type_i_f_overflow_lower_modulus_shared_gap_type_ii.py
reproductions/type-i-f-overflow-lower-modulus-shared-gap-type-ii-results.json
~~~

输入是六个 lower_modulus_classification=F_box_hit 的冻结记录，并从支撑边界输入恢复
\(K\) 的素因子分解。逐一枚举整个原指数盒，而不是只取脚本保存的最短向量。

~~~text
lower_hit_count: 6
representation_count: 50
unique_sum_count: 25
shared_gap_candidate_count: 101
type_ii_certificate_count: 4
prime_hit_count: 3
~~~

逐样本分流为：

| (p) | (t) | 盒内表示 | 不同和 | 共享缺口候选 | Type II 命中 |
|---:|---:|---:|---:|---:|---:|
| 57399241 | 5 | 34 | 17 | 63 | 1 |
| 99151369 | 97 | 2 | 1 | 0 | 0 |
| 242042089 | 257 | 6 | 3 | 6 | 1 |
| 366108649 | 197 | 2 | 1 | 0 | 0 |
| 475619929 | 845 | 4 | 2 | 30 | 2 |
| 510725329 | 37 | 2 | 1 | 2 | 0 |

命中表为：

| \(p\) | lower \(t\) | 共享缺口 \(m'\) | \((A,B,C)\) | \(d=A^2C\) |
|---:|---:|---:|---:|---:|
| 57399241 | 5 | 311 | (2, 32031, 224) | 896 |
| 242042089 | 257 | 31 | (2, 29, 1043285) | 4173140 |
| 475619929 | 845 | 295 | (1, 29726264, 4) | 4 |
| 475619929 | 845 | 1703 | (9, 733984, 18) | 1458 |

每张证书均独立验证 \(x'=ABC\)、\(d=A^2C\)、\(A\le B\)、\((A,B)=1\) 和
\(m'\mid A+B\)，并直接检查三个分母的整数性及
\(4/p=1/x'+1/y+1/z\)。其余三个素数
\(p=99151369,366108649,510725329\) 的全部共享缺口候选均未通过 Type II 检验。

## 严格边界

这不是“lower F-box hit 必有 Type II 提升”的证明。低模数表示只保证 \(t\mid a+b\)；
即使 \(m'\mid a+b\)，也不能推出 \(m'\mid A+B\) 或 \(A,B\mid x'\)。相反，审计中
仍有 101 个候选缺口而只有 4 张证书，说明独立 Type II 因子选择是实际瓶颈。该接口
的全称版本需要额外证明：对每个 lower hit，某个表示和 \(S\) 的合法因子必与 \(x'\)
的平方除子谱发生同缺口碰撞；当前数据不足以支持这一全称断言。

## 复现命令

~~~bash
python3 reproductions/type_i_f_overflow_lower_modulus_shared_gap_type_ii.py
~~~
