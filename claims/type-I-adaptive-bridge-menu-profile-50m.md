---
kind: claim
claim_id: type-I-adaptive-bridge-menu-profile-50m
title: 五千万最终残余的桥模板驱动自适应移位闭合
statement: 对五千万p减一层残余的35个核心素数，固定16个偶桥因子E={58,352,414,676,722,928,1442,1540,2080,2576,2704,2800,3276,5540,5776,7776}。对每个E完整枚举E=sR+1的奇因子分解且R不小于3，并以p同余s模Lambda(E)筛选源，再完整枚举K=(pR+1)/4的B不大于7因子对。该选择器闭合全部35点；实际选中移位包含3、5、7、9、11、17、25、29以及105。此为有限桥菜单审计，不是全称选择器。
claim_status: computationally_reproduced
topics:
- type-I
- normal-form
- descent
- even-source
- source-state
- bridge
- congruence
- factorization
- selector
- shifted-source
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 五千万最终残余的桥模板驱动自适应移位闭合

取[五千万多层闭合](type-I-multitier-short-shift-closure-50m.md)中固定移位菜单之前的 35 个最终残余，
并固定桥菜单

\[
\mathcal E=\{58,352,414,676,722,928,1442,1540,2080,2576,2704,2800,
3276,5540,5776,7776\}. \tag{1}
\]

对每个 \(E\in\mathcal E\)，不预先固定移位；而是完整枚举

\[
E=sR+1,\qquad s,R\text{ 为正奇数},\qquad R\ge3. \tag{2}
\]

由[源平方同余模数](type-I-source-square-congruence-modulus.md)，只保留

\[
p\equiv s\pmod{\Lambda(E)}. \tag{3}
\]

再要求 \(4\mid pR+1\)，令 \(K=(pR+1)/4\)，穷尽 \(B\le7\) 与 \(BC\mid K\)，并以
[源状态实现判据](type-I-normal-source-state-realization.md)重建证书。

## 有限审计结果

该过程完整闭合全部 35 点：

\[
35=35_{\mathcal E,B\le7}. \tag{4}
\]

所选桥和移位的频数为：

| 项 | 频数 |
|---|---:|
| \(E=58,352,414,676,722,928,1442,1540\) | \(2,6,1,6,1,1,1,1\) |
| \(E=2080,2576,2704,2800,3276,5540,5776,7776\) | \(1,2,2,3,1,1,4,2\) |
| \(s=3,5,7,9,11,17,25,29,105\) | \(2,2,2,16,1,2,7,1,2\) |

尤其是两条 \(s=105\) 见证不在此前八移位搜索范围内。这表明先选桥 \(E\)、再从 \(E-1\) 的因子
自适应导出 \(s\)，确实探索了不同于静态移位菜单的状态空间。

这不是桥菜单在数学上“更小”或“更好”的证明：它有 16 个 \(E\) 模板，并且是从该有限残余中提取的。
其价值是把下一步选择律的变量明确为 \(E\) 的因子结构，而不再把移位集合当作原始对象。下一条
[固定桥菜单的 CRT 逃逸](type-I-fixed-bridge-menu-crt-escape.md)进一步证明这个固定菜单本身不可能全称覆盖。

可复现命令：

~~~bash
python3 reproductions/type_i_adaptive_bridge_menu_profile.py
python3 -m unittest tests/test_type_i_adaptive_bridge_menu_profile.py -q
~~~
