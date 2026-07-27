---
kind: claim
claim_id: type-I-normal-source-state-b1-realization
title: Type I源状态的B等于1单除子剩余判据
statement: 在Type I源状态实现判据中，B=1分支存在当且仅当K有除子C满足4C=-1 modR；写H=K/C后H=-1 modR自动成立，且A=(H+1)/R、m=(4C+1)/R。H19十亿p=25 mod48外部纯剩余的28个点全部存在这样的B=1实现。
claim_status: established
topics:
- type-I
- normal-form
- descent
- factorization
- source-state
- divisor-residues
- selector
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# Type I 源状态的 B 等于 1 单除子剩余判据

在 [源状态的正规形因子对实现判据](type-I-normal-source-state-realization.md) 中取 $B=1$。
令 $K=CH$，则唯一需要选择的条件简化为

$$
C\mid K,\qquad 4C\equiv-1\pmod R. \tag{1}
$$

写 $H=K/C$ 后，因 $4K\equiv1\pmod R$，条件 (1) 自动推出 $H\equiv-1\pmod R$。
这给出下列等价：存在 $B=1$ 的正规形实现，当且仅当 $K$ 有一个满足 (1) 的除子 $C$。一旦选定
此除子，参数无需搜索：

$$
A=\frac{H+1}{R},\qquad m=\frac{4C+1}{R},\qquad
x=AC. \tag{2}
$$

因而

$$
p=4AC-m,\qquad
\frac4p=\frac1{AC}+\frac1{ACH}+\frac1{pK},
$$

并由源状态的归一化平方桥条件恢复严格偶源边。

对 H19 十亿 $p\equiv25\pmod{48}$ 的28个外部纯剩余点，完整枚举每个相应 $K$ 的因子对后，
28点全部存在这样的 $B=1$ 实现。故当前切换问题可以进一步写成：在外部尺度残数族完全失效时，
为何目标相关整数 $K$ 必有一个除子落入 (1) 的指定剩余类？这仍是有限证据，
不是全称定理。

可复现命令：

~~~bash
python3 reproductions/type_i_normal_source_state_realization.py
python3 -m unittest tests/test_type_i_normal_source_state_realization.py -q
~~~
