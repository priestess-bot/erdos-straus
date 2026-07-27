---
kind: claim
claim_id: type-I-tail-reverse-pminusone-boundary-500m
title: 五亿普通双尾遗漏的 p减一上半区桥边界
statement: 对p<=500000000的1717个普通Type II p-1双尾遗漏，完整枚举m<=215的78215张Type I正规形。p减一桥的唯一因子E=R+1以r=(R+1)/4整除((p-1)/4)^2精确测试后，1532点有p减一桥、185点没有。由于同一盒的1717点均有小侧上半区桥，185个p减一遗漏在该盒中必需使用非p减一的上半区偶源。因此p减一子选择器不是该有限盒的充分混合终端机制。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- type-II
- p-minus-one
- upper-half-source
- terminal-bridge
- selector-boundary
- finite-audit
- normal-form
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-and-Type-II-certificate-context
visibility: public
last_checked: '2026-07-28'
---

# 五亿普通双尾遗漏的 p 减一上半区桥边界

输入是完整 \(p\le5\cdot10^8\) 的 1,717 个普通 Type II \(p-1\) 双尾遗漏。对每个点，
完整枚举

\[
3\le m\le215,\qquad m\equiv3\pmod4
\]

中的每张 Type I 正规形。对固定正规形，\(p-1\) 源没有需要枚举的桥因子菜单：
[一般 p减一桥判据](type-I-normal-pminusone-upper-half-bridge.md)表明候选唯一为

\[
E=R+1=4r,
\qquad
r\mid\left(\frac{p-1}{4}\right)^2. \tag{1}
\]

命中时逐条重建 Type I 正规形、既约小侧因子对和两边单位分数恒等式。

## 结果

| 项目 | 数值 |
| --- | ---: |
| 普通双尾遗漏 | 1,717 |
| 穷尽的 Type I 正规形 | 78,215 |
| 检查的唯一 \(p-1\) 状态 | 78,215 |
| \(p-1\) 上半区桥命中 | 1,532 |
| \(p-1\) 桥遗漏 | 185 |

因此

\[
1717=1532_{p-1\ \mathrm{upper\!-!half}}+185_{\mathrm{no}\ p-1\ bridge\ in\ box}. \tag{2}
\]

首个遗漏是 \(p=297049\)；已知的最大首个一般偶源缺口点
\(p=493936249\) 也属于遗漏。相反，命中的 \(p-1\) 桥可在 \(B=1,2,3,4,5,6,8,9,13,14,17,18\)
等多个正规形坐标中出现，不能由固定小 \(B\) 菜单概括。

## 与上半区混合选择的关系

[替代正规形小侧剖面](type-I-tail-reverse-even-source-small-side-alternative-profile-500m.md)
已经在**同一** \(m\le215\) 盒中为全部 1,717 点提供小侧桥。结合 (2)，每个上述 185 点
在此盒内都有上半区偶源，但没有 \(p-1\) 源桥。因此，把
[上半区混合终端选择猜想](type-I-upper-half-mixed-terminal-selector-conjecture.md)的 Type I 分支
收缩成 \(p-1\) 分支在该完整有限模型中是错误的。

这不排除更大缺口上的 \(p-1\) 桥，也不反驳原混合终端选择引理；它精确排除的只是所述
有限正规形盒中的单一 \(p-1\) 子选择器。

重建命令：

~~~bash
python3 reproductions/type_i_tail_reverse_pminusone_profile_500m.py
python3 -m unittest tests/test_type_i_tail_reverse_pminusone_profile_500m.py -q
~~~
