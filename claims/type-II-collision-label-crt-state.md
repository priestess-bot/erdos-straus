---
kind: claim
claim_id: type-II-collision-label-crt-state
title: 带来源碰撞标签的 CRT 状态
statement: 对 H19 后的单新因子 Type II 因子 h=eq，若 e 的不同素因子 ell 都来自 H19 射线 p+4t，则目标移位 s 同时满足 s=t mod ell；这些来源标签合成为一个显式 CRT 类 s=r mod E，其中 E为碰撞素数积。并且 q=-e^{-1} mod4ac。对p=372271201的延迟释放链，该状态依次为(89,21,5 mod21)、(401,5,1 mod5)、(484,1,0 mod1)。
claim_status: established
topics:
- type-II
- multishift
- collision-factor
- congruence
- CRT
- state-transition
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-certificate-context
visibility: public
last_checked: '2026-07-25'
---

# 带来源碰撞标签的 CRT 状态

令 \(h=eq\) 是一张单新因子 Type II 证书，其中 \(e\) 的不同奇素因子集合为 \(L\)，
每个 \(\ell\in L\) 都整除某条 H19 射线 \(p+4t_\ell\)。若同一 \(\ell\) 也整除目标
\(p+4s\)，则

\[
s\equiv t_\ell\pmod\ell. \tag{1}
\]

所以相容的来源标签给出唯一 CRT 状态

\[
s\equiv r_L\pmod {E_L},\qquad E_L=\prod_{\ell\in L}\ell. \tag{2}
\]

另一方面，若 \(h\equiv-1\pmod {4ac}\)，则 \(e\) 与 \(4ac\) 互素，且新素因子满足

\[
q\equiv-e^{-1}\pmod {4ac}. \tag{3}
\]

式 (2)--(3) 将一个带碰撞的单新因子证书压缩为“来源 CRT 类、碰撞积、射线模数、
新素因子逆元类”的有限状态。它不保证这样的状态存在，也不说明 \(E_L\) 随移位增大而
单调变化。

## 延迟释放实例

对 \(p=372{,}271{,}201\) 的三层释放链，精确状态为：

| \(s\) | \(e\) | 来源 CRT 状态 |
|---:|---:|---|
| 89 | \(3\cdot7\) | \(s\equiv5\pmod{21}\) |
| 401 | \(5\) | \(s\equiv1\pmod5\) |
| 484 | \(1\) | \(s\equiv0\pmod1\) |

第一行的 \(3\) 来自 \(2\bmod3\) 的 H19 来源类，\(7\) 来自 \(5\bmod7\) 类；
第二行的 \(5\) 来自 \(1\bmod5\) 类。每一行的 \(q\) 也都满足 (3)。

这显示“碰撞重数”不是充分状态变量：释放同时改变来源类与 CRT 模数。将
\(21\to5\to1\) 解释为一般势能仍是开放问题，不能由此单例推出单调性。

## 十亿单碰撞核验

对 \(p\le10^9\) 的 H19 深度谱，全部 10 个最小碰撞重数恰为 1 的状态均满足
(1)--(3)；碰撞素数频数为 \(3:4,5:2,7:1,13:2,17:1\)。因此来源标签和反元残数
不是三亿样本中的偶然现象。不过这只是必要结构的精确复核，不能推出某个标签类必然
释放新因子；两碰撞点 \(p=372{,}271{,}201\) 仍表明碰撞积与释放深度都必须允许随状态变化。

重建：

~~~bash
python3 reproductions/type_ii_collision_label_crt.py
python3 -m unittest tests/test_type_ii_collision_label_crt.py -q
~~~
