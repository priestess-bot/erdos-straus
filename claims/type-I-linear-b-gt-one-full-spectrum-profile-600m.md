---
kind: claim
claim_id: type-I-linear-b-gt-one-full-spectrum-profile-600m
title: 两百个首达 B 大于一线性证书的完整谱重选剖面
statement: 对六亿冻结普通双尾遗漏闭合中首个确定性一般B证书取B>1的全部200个核心素数，完整枚举所有线性源诱导R并精确分类一般B目标谱，共得到10292个R状态、1018个命中、2752个有限指数障碍和6522个子群角色障碍。182个素数可在完整谱中重选到B=1，故“首达B>1”通常只是搜索顺序现象；18个素数无任何B=1命中。一般B命中唯一的仅7点，其中878089、26034649、57399241、283319689同时无B=1命中，构成更小的真实对抗核心集。该剖面仍是有限数据，不证明全称选择器。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- linear-source
- general-b
- b-equals-one
- reselection
- centered-spectrum
- subgroup-character
- finite-exponent
- exhaustive-computation
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 两百个首达 B 大于一线性证书的完整谱重选剖面

## 审计对象

[六亿压力集的线性源一般 B Type I 有限闭合剖面](type-I-linear-source-general-b-completion-profile-600m.md)
对 1,964 个冻结普通 Type II 双尾遗漏按确定性顺序在**首个**一般 \(B\) 命中处停止。其中有
200 个首证书的规范参数 \(B>1\)。这一事实本身不能说明该素数的完整线性源谱没有 \(B=1\)
命中。

本页对恰好这 200 个素数重新完整枚举

\[
p=a+s+asR,
\qquad s\equiv1\pmod2,
\qquad R\equiv3\pmod4, \tag{1}
\]

的所有不同 \(R\)。对每个

\[
K=\frac{pR+1}{4}, \tag{2}
\]

分别穷尽判定

\[
d\mid K^2,\qquad4d\equiv-1\pmod R \tag{3}
\]

的一般 \(B\) 目标，以及更严格的

\[
d\mid K,\qquad4d\equiv-1\pmod R \tag{4}
\]

的 \(B=1\) 目标。无 (3) 命中时再用精确单位群格证书区分 F 型与 G 型。

## 完整结果

200 个完整线性谱共含

\[
10{,}292\text{ 个不同 }R,
\qquad18{,}074\text{ 个有向源状态}. \tag{5}
\]

一般 \(B\) 分类为

| 类别 | 状态数 |
| --- | ---: |
| 命中 | 1,018 |
| 有限指数 F | 2,752 |
| 子群角色 G | 6,522 |

每个素数都保留至少一个命中，这是对原首证书的独立全谱重放。更重要的是，\(B=1\) 的完整谱
重选分裂为

\[
\boxed{200=182_{\text{存在 }B=1\text{ 重选}}+18_{\text{全谱无 }B=1\text{ 命中}}.} \tag{6}
\]

所以“第一次找到的证书取 \(B>1\)”在 91% 的此类压力点上只是枚举顺序的副产物，不能作为
真正 \(B>1\) 必需性的证据。

## 最小对抗核心

一般 \(B\) 命中唯一的素数仅有七个：

\[
67{,}369,\ 878{,}089,\ 13{,}782{,}409,\ 26{,}034{,}649,\
57{,}399{,}241,\ 152{,}498{,}329,\ 283{,}319{,}689. \tag{7}
\]

其中第一个、第三个和第六个仍有 \(B=1\) 命中。把 (7) 与“全谱无 \(B=1\)”相交，得到四点
真正对抗核心：

| (p) | 唯一命中 (R) | F 型 | G 型 | 首证书 (B) |
| ---: | ---: | ---: | ---: | ---: |
| 878,089 | 59 | 2 | 21 | 7 |
| 26,034,649 | 187 | 6 | 20 | 2,947 |
| 57,399,241 | 19 | 24 | 30 | 7 |
| 283,319,689 | 63 | 13 | 46 | 11 |

最后一行的首达最小坐标为 \(587\)，在原 1,964 点闭合中为全局最大值。它既不是 \(B=1\)
可重选点，也不是多命中点，因而是当前跨源选择理论最具信息量的单一压力实例。

## 含义与范围

这张完整谱审计把后续理论对象从“200 个首达 \(B>1\) 记录”缩小为：

1. 18 个全谱确实无 \(B=1\) 命中的线性压力点；
2. 其中 4 个一般 \(B\) 命中唯一的对抗核心；
3. 尤其是 \(p=283{,}319{,}689\) 的 \(1+13+46\) 全谱分裂。

它没有证明所有未来核心素数也会有一般 \(B\) 命中；也不能把有限的 18 点误读为全称
\(B>1\) 必需族。其作用是给跨源二次角色、私有层和反足点增长理论提供完整、非首达偏差的
压力基准。

## 复现

~~~bash
python3 reproductions/type_i_linear_b_gt_one_full_spectrum_profile_600m.py
python3 -m unittest tests.test_type_i_linear_b_gt_one_full_spectrum_profile_600m -v
~~~
