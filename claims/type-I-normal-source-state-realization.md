---
kind: claim
claim_id: type-I-normal-source-state-realization
title: Type I源状态的正规形单残数因子对实现判据
statement: 给定偶源状态(p,n,E)，令s=p-n、R=(E-1)/s、K=(pR+1)/4，并假定E|n^2/gcd(E,4)。存在以该(n,E)为桥的Type I正规形反向边，当且仅当存在BC|K，令H=K/(BC)，满足R|(4B^2C+1)及gcd((H+B)/R,B)=1。此时H=-B modR自动成立，且A=(H+B)/R、m=(4B^2C+1)/R显式恢复正规形。
claim_status: established
topics:
- type-I
- normal-form
- descent
- reverse-lift
- factorization
- source-state
- selector
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# Type I 源状态的正规形单残数因子对实现判据

设 $p$ 为目标素数，$2\le n<p$ 为偶源，并令

$$
s=p-n,\qquad R=\frac{E-1}{s},\qquad K=\frac{pR+1}{4}. \tag{1}
$$

假定 (1) 中 $R,K$ 均为正整数，$E$ 为偶数，且

$$
E\mid\frac{n^2}{\gcd(E,4)}. \tag{2}
$$

## 定理

存在以给定 $(n,E)$ 为桥的 Type I 正规形最大尾反向边，当且仅当存在正整数 $B,C$，令

$$
BC\mid K,\qquad H=\frac K{BC}, \tag{3}
$$

满足

$$
R\mid4B^2C+1,\qquad
\gcd\left(\frac{H+B}{R},B\right)=1. \tag{4}
$$

此时令

$$
A=\frac{H+B}{R},\qquad m=\frac{4B^2C+1}{R}. \tag{5}
$$

便恢复正规形 $x=ABC$、$H=AR-B$，并有

$$
p=4ABC-m,\qquad
\frac4p=\frac1{ABC}+\frac1{ACH}+\frac1{pK}. \tag{6}
$$

同时其反向源为

$$
\frac4n=\frac1{nK/E}+\frac1{ABC}+\frac1{ACH}. \tag{7}
$$

## 证明

若正规形已给定，则 $K=BCH$，所以 (3) 成立；正规形定义给出 (4) 的第一项，而互素条件给出
第二项。反过来，第一项自动给出 $R\mid H+B$：令 $T=BC$，则

$$
4BT\equiv-1\pmod R.
$$

故 $T$ 在模 $R$ 下可逆。又 $4K\equiv1\pmod R$，所以

$$
4H\equiv4KT^{-1}\equiv T^{-1}\equiv-4B\pmod R.
$$

因 $R$ 为奇数，$H\equiv-B\pmod R$。于是 (3)--(5) 直接给出 $H=AR-B$ 和
$(4B^2C+1)=mR$。计算

$$
4ABC-m=\frac{4BCH-1}{R}=\frac{4K-1}{R}=p,
$$

从而恢复 (6)。又 $E=sR+1=4K-nR$，且 (2) 由
[归一化源平方等价](type-I-normal-source-square-bridge-equivalence.md) 等价于 $E\mid4K^2$。
于是偶源反向选择器给出 $E\mid nK$ 及 (7)。

## 含义

这一定理把“选择 Type I 正规形”转成在一个已知整数 $K$ 上选择因子对 $B,C$ 的一条同余：

$$
4B^2C\equiv-1\pmod R.
$$

第二个互补因子剩余自动成立，只有 $\gcd(A,B)=1$ 仍需单独检查。因此，外部尺度残余切换到
内部桥后的真正选择问题不再是开放的 $A,B,C,m$ 搜索，而是单一受限除子对的残数命中加互素性。
该判据已在 H19 $p\equiv25\pmod{48}$ 的28个外部纯剩余点上独立
枚举并逐项重建原正规形。

可复现命令：

~~~bash
python3 reproductions/type_i_normal_source_state_realization.py
python3 -m unittest tests/test_type_i_normal_source_state_realization.py -q
~~~
