---
kind: claim
claim_id: type-II-h19-residual-ac-profile
title: H19 十亿残余的半径九直接 AC 证书剖面
statement: 对存储的 p<=10^9 的664个 H19 规范扇残余，完整枚举 max(A,C)<=9 的 AC Type II 射线且 K 不设界后，664个全部有直接 Type II 证书；最小半径分布为3:148、4:282、5:189、6:28、7:11、8:4、9:2。半径8遗漏165479161和633393601，故半径9在该固定样本内必要。这是有限直接证书闭合，不给出一般半径界。
claim_status: computationally_reproduced
topics:
- type-II
- ac-rays
- short-certificate
- finite-audit
- h19
sources:
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-prime-shape-context
- paper: bradford2024
  locator: Propositions 2 and 3
  role: Type-II-certificate-context
visibility: public
last_checked: '2026-07-26'
---

# H19 十亿残余的半径九直接 AC 证书剖面

令 H19 残余指前 19 条规范 Type II 射线均未命中的 \(p\le10^9\) 的核心素数。
对存储的全部 664 个残余，枚举

\[
h=4ACK-1\mid p+4A^2C,\qquad \max(A,C)\le9, \tag{1}
\]

其中 \(K\) 不设预先上界，而由 \(p+4A^2C\) 的完整因子分解恢复。每个候选均精确重建
Type II 三项单位分数证书并验证因子对恒等式。

| 最小半径 \(\max(A,C)\) | 残余数 |
| ---: | ---: |
| 3 | 148 |
| 4 | 282 |
| 5 | 189 |
| 6 | 28 |
| 7 | 11 |
| 8 | 4 |
| 9 | 2 |

因此 664 个点全由半径不超过 9 的直接 Type II AC 证书闭合。半径 8 仍遗漏恰好两点

\[
165{,}479{,}161,\qquad633{,}393{,}601.
\]

它们在半径 9 的最小见证均取 \((A,C)=(9,3)\)，分别可取

\[
(K,h,\operatorname{gap})=(9175,990899,167),\qquad
(15808,1707263,371). \tag{2}
\]

故半径 9 在这个固定十亿样本内确为必要。特别地，半径六结论不是整个 H19 残余集的规律：
它命中 647 个，遗漏 17 个；后者的最小半径为 \(7,8,9\)。这避免把针对高溢出同参数失败
状态的半径六补洞误读为全 H19 的统一界。

这个结果只是一个有限、直接的证书剖面，不证明所有 H19 残余、更不证明所有
\(p\equiv1\pmod {24}\) 都有固定半径的 AC 证书。事实上，已有有限 AC 模板的逃逸边界表明，
任何向全称命题的提升都必须控制随 \(p\) 变化的因子结构，而不能只固定有限条射线。
见 [有限 AC 射线集的仿射逃逸边界](type-II-ac-escape-affine-ray-boundary.md)。

可复现命令：

~~~bash
python3 reproductions/type_ii_h19_residual_ac_profile.py \
  --input reproductions/type-ii-source-free-transition-h19-1b-results.json \
  --ac-bound 9 \
  --output reproductions/type-ii-h19-residual-ac-profile-1b-results.json
python3 -m unittest tests/test_type_ii_h19_residual_ac_profile.py -q
~~~
