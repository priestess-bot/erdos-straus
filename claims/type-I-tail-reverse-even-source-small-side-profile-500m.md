---
kind: claim
claim_id: type-I-tail-reverse-even-source-small-side-profile-500m
title: 五亿偶源终端桥的小侧普通除子对剖面
statement: 对五亿普通 Type II 双尾遗漏的1717条完整 Type I 偶源终端记录，按 E/(2K)=a/b 的既约普通除子对分类，1421条已选桥为小侧 a<b，296条为大侧 a>b。完整枚举每条大侧记录同一L=2K的全部互素普通除子对后，其中201条另有小侧桥，95条没有；故1622条在相同正规形状态中有小侧桥，95条是大侧指数残余。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- normal-form
- terminal-bridge
- even-source
- divisor-pairs
- factorization
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-and-divisor-certificate-context
visibility: public
last_checked: '2026-07-28'
---

# 五亿偶源终端桥的小侧普通除子对剖面

对[五亿普通尾遗漏的偶源反向二尾闭合](type-I-tail-reverse-even-source-closure-500m.md)的每条记录，
取 \(L=2K\)，并将桥因子比值既约化为

\[
\frac EL=\frac ab,\qquad (a,b)=1. \tag{1}
\]

按[小侧简化引理](type-I-normal-even-source-small-side-simplification.md)，\(a<b\) 的桥不再有独立的
大小预算。对每个已选 \(a>b\) 的状态，本审计穷尽所有

\[
a',b'\mid L,\qquad (a',b')=1,\qquad a'<b',\qquad
a'\equiv2b'\pmod R, \tag{2}
\]

并保留使 \(E'=La'/b'\) 为偶数的全部候选。

## 结果

| 类别 | 记录数 |
| --- | ---: |
| 已选桥已是小侧 \(a<b\) | 1,421 |
| 已选桥为大侧 \(a>b\) | 296 |
| 大侧状态另有小侧桥 | 201 |
| 同一 \((L,R)\) 内没有小侧桥的大侧残余 | 95 |
| 拥有小侧桥的总状态数 | 1,622 |

例如，\(p=372409\) 的已选大侧为

\[
(R,L,E,a,b)=(7,1303432,2080478,83,52).
\]

同一 \((L,R)\) 内却存在更小侧对

\[
(E',a',b')=(8,1,162929),
\]

它给出偶源 \(n=372408\)。相反，首个大侧残余 \(p=67369\) 的
\(L=2930552,R=87\) 已完整枚举而没有任何小侧对；它说明不能把大侧桥一概通过取另一对因子消去。

## 边界

结果的输入是已经选定的 1,717 条五亿终端记录。它不证明每个核心素数存在 Type I 正规形，
也不说明 95 条大侧残余在其它缺口、其它正规形或 Type II 分支中失败。其用途是将后续的
因子指数研究准确集中到这些不能在原状态内降为小侧的点。

重建命令：

~~~bash
python3 reproductions/type_i_tail_reverse_even_source_small_side_profile.py
python3 -m unittest tests/test_type_i_tail_reverse_even_source_small_side_profile.py -q
~~~
