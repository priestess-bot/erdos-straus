---
kind: claim
claim_id: type-I-h19-variable-even-scale-after-k6-1b
title: H19双固定尺度边界的全变量偶尺度外源审计
statement: H19十亿p=25 mod48残余中，k=2与k=6共同遗漏的71个点上，完整枚举每个k|(p-1)/4且n=((4k-1)p+1)/(4k)为偶数的尺度，以及每个g|kn、g<=n、g=-1 mod(4k-1)的混合因子，43个获得严格Type I偶源证书，28个仍遗漏。故该完整仿射混合因子偶源族在此有限输入上有精确分流71=43+28。
claim_status: computationally_reproduced
topics:
- type-I
- descent
- even-source
- external-source
- variable-scale
- factorization
- finite-audit
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-certificate-context
- paper: ventas2026
  locator: Theorem 2.3
  role: external-source-context
visibility: public
last_checked: '2026-07-27'
---

# H19 双固定尺度边界的全变量偶尺度外源审计

对固定核心素数 $p$，考察仿射外部源族

$$
q=4k-1,\qquad n=\frac{qp+1}{4k}.
$$

此 $n$ 为整数当且仅当 $k\mid(p-1)/4$。因此，对 [H19 k=2 子群边界后的
k=6 偶源释放](type-I-h19-k6-after-k2-boundary-1b.md) 所留下的71个点，完整枚举

$$
k\mid\frac{p-1}{4},\qquad n\equiv0\pmod2,
$$

以及每个满足

$$
g\mid kn,\qquad g\le n,\qquad g\equiv-1\pmod{4k-1}
$$

的混合因子。每个命中均从

$$
\frac4n=\frac1{kn}+\frac1u+\frac1v,
\qquad
u=\frac{k(n+g)}{4k-1},\quad v=\frac{nu}{g},
$$

重建，并同时以有理数恒等式和 Bradford 短证书逐项核验。结果为

$$
71=43_{\text{变量偶尺度终止}}+28_{\text{该族遗漏}}.
$$

选择的43条证书中最常见尺度为 $k=30$（10条）、$10$（7条）、$14$（6条）与
$18$（4条），这说明在此处变量尺度确实释放了固定 $2,6$ 无法覆盖的残数条件。
另一方面，28个遗漏已经排除了该**完整**终端偶源仿射混合因子族，而非仅排除一个有限尺度菜单。
它们仍不排除其他 Type I 正规形、非终端源、Type II 递降或猜想本身。

可复现命令：

~~~bash
python3 reproductions/type_i_h19_variable_even_scale_after_k6.py
python3 -m unittest tests/test_type_i_h19_variable_even_scale_after_k6.py -q
~~~
