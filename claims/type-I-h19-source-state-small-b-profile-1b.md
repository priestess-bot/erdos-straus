---
kind: claim
claim_id: type-I-h19-source-state-small-b-profile-1b
title: H19偶桥源状态的最小B小菜单剖面
statement: 对H19十亿664条已选择的偶源状态，完整重枚举其所有Type I正规形实现并最小化B后，分布为B=1:647、B=2:12、B=4:2、B=7:2、B=13:1；因此该有限输入均有B≤13实现。p≡25 mod48的243条分布为B=1:237、B=2:4、B=4:2，均有B≤4实现。
claim_status: computationally_reproduced
topics:
- type-I
- normal-form
- descent
- source-state
- small-parameter
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# H19 偶桥源状态的最小 B 小菜单剖面

固定 H19 十亿源自由残余的664条已核验偶源状态，再按
[源状态实现判据](type-I-normal-source-state-realization.md) 完整枚举全部正规形，并以

$$
(B,C,A,m)
$$

字典序最小化。所得最小 $B$ 分布为

$$
664=647_{B=1}+12_{B=2}+2_{B=4}+2_{B=7}+1_{B=13}. \tag{1}
$$

故在这个独立的有限 H19 输入上，每条已选择的偶源状态都有 $B\le13$ 的正规形实现。
唯一需要 $B=13$ 的点为 $p=169588609$。

在 $p\equiv25\pmod{48}$ 的243条子类中，分布进一步收紧为

$$
243=237_{B=1}+4_{B=2}+2_{B=4}, \tag{2}
$$

即每条均有 $B\le4$ 实现。这里的重实现可能牺牲原先的短缺口：全664点的所选最小 $B$
形式中最大 $m=21\,544\,419$，所以 (1)--(2) 是低正规形因子复杂度的有限事实，不能误读为
统一短证书界或全称 $B$ 界。

这个 H19 菜单不能直接提升为跨样本候选：五亿普通尾压力集已经出现
$B=3,5,8,9,11,14,16,17$，见
[五亿偶源状态的最小B跨样本边界](type-I-tail-source-state-small-b-profile-500m.md)。
后续必须寻找依赖于源状态因子结构的菜单或势函数，而不是固定此五个数。

可复现命令：

~~~bash
python3 reproductions/type_i_h19_source_state_small_b_profile.py
python3 -m unittest tests/test_type_i_h19_source_state_small_b_profile.py -q
~~~
