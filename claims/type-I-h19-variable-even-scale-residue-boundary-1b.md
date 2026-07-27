---
kind: claim
claim_id: type-I-h19-variable-even-scale-residue-boundary-1b
title: H19变量偶尺度剩余的纯除子剩余障碍
statement: H19十亿p=25 mod48分支中全变量偶尺度仿射混合因子族留下的28个点，对每个允许尺度k|(p-1)/4及其偶源n，去掉大小限制后完整枚举全部g|kn仍无g=-1 mod(4k-1)。共542个尺度剖面均为零命中。因此该28点的遗漏完全由除子剩余积集障碍造成，并非g<=n大小条件造成。
claim_status: computationally_reproduced
topics:
- type-I
- descent
- even-source
- external-source
- variable-scale
- divisor-residues
- finite-audit
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# H19 变量偶尺度剩余的纯除子剩余障碍

在 [全变量偶尺度审计](type-I-h19-variable-even-scale-after-k6-1b.md) 留下的28个点上，对每个
允许尺度

$$
k\mid\frac{p-1}{4},\qquad n=\frac{(4k-1)p+1}{4k}\equiv0\pmod2,
$$

原来的终止条件还要求

$$
g\mid kn,\qquad g\le n,\qquad g\equiv-1\pmod{4k-1}.
$$

这里去除唯一的大小条件 $g\le n$，枚举全部正除子 $g\mid kn$。28个点共有542个允许尺度，结果为

$$
\#\{(p,k,g):g\mid kn,\ g\equiv-1\pmod{4k-1}\}=0.
$$

所以该有限边界的遗漏早于终止大小界发生：每一个尺度的完整除子剩余积集都避开目标类
$-1$。这将后续理论任务明确为控制不同 $4k-1$ 模数下的因子残数生成，而不是设法放宽
混合因子的大小界。结论的范围仍严格限于该仿射、终端、偶源外部族。

可复现命令：

~~~bash
python3 reproductions/type_i_h19_variable_even_scale_residue_boundary.py
python3 -m unittest tests/test_type_i_h19_variable_even_scale_residue_boundary.py -q
~~~
