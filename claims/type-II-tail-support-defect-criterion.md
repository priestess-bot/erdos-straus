---
kind: claim
claim_id: type-II-tail-support-defect-criterion
title: 普通 Type II 双尾选择器的支持度缺陷判据
statement: 设p=4q(u-1)+1为核心素数，m=4q-1，且m+1|p-1。给定一组基底素数B，将d|q^2u^2中B外不同素因子的个数定义为支持度。则最小支持度缺陷delta_B(p,m)等于使某个d<=qu、d=-qu (mod m)、d|q^2u^2成立的最小支持度；delta_B(p,m)<=k当且仅当相应基底除子乘至多k个非基底素数幂命中目标剩余类，并由此给出普通 Type II 双尾严格递降。
claim_status: established
topics:
- type-II
- descent
- divisor-selection
- factor-support
- potential-function
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-certificate-context
visibility: public
last_checked: '2026-07-26'
---

# 普通 Type II 双尾选择器的支持度缺陷判据

令

\[
m=4q-1,\qquad p=4q(u-1)+1,\qquad x=qu. \tag{1}
\]

假定 (p\equiv1\pmod{24}) 为素数；因此 (m+1=4q\mid p-1)，并且 (x=(p+m)/4)。
给定一组基底素数 (B)，把任意 (d\mid x^2=q^2u^2) 中不属于 (B) 的**不同**
素因子数记作

\[
\operatorname{supp}_B(d). \tag{2}
\]

定义支持度缺陷

\[
\delta_B(p,m)=
\min\left\{\operatorname{supp}_B(d):
1\le d\le x,\ d\mid x^2,\ d\equiv-x\pmod m\right\}, \tag{3}
\]

若集合为空则取 (\delta_B=\infty)。

## 判据

由于 (p) 为素数且 (p>m)，有 ((x,m)=1)：任意公共素因子同时整除
(u) 与 (m)，从 (p=4q(u-1)+1\equiv u\pmod m) 导出它整除 (p)，矛盾。
因此当 (d\equiv-x\pmod m) 时，补除子自动满足

\[
\frac{x^2}{d}\equiv-x\pmod m. \tag{4}
\]

故 (3) 中每个 (d) 都是普通 Type II 双尾除子，且双尾去 (p) 严格降至 (u)。

把 (x^2) 的素因子分解为基底部分和非基底部分。对每个非基底素数 \(\ell\)，允许的
非零幂为

\[
\ell,\ell^2,\ldots,\ell^{v_\ell(x^2)}. \tag{5}
\]

于是 (\delta_B\le k) 当且仅当目标剩余 \(-x\pmod m) 落入“基底所有除子剩余”与至多
(k) 个集合 (5) 的乘积集中，并满足大小界 (d\le x)。这给出一个有限、精确的
乘积集覆盖问题，而不是经验性因子标签。

## 与当前梯的关系

H19-k23 的 (m=27) 替代尾梯正是在阶段依赖的 (B) 下得到

\[
\delta_B\le2 \tag{6}
\]

的 2,710 条有限闭合。要把这种模式升级为证明，需要一个跨阶段引理：当某个当前缺口的
缺陷超过 2 时，必须在后续合法尾缺口降低缺陷或触发另一种严格递降。当前数据只验证了
该命题的有限实例，没有提供这种全称势能律。

重建命令：

~~~bash
python3 -m unittest tests/test_type_ii_tail_support_defect.py -q
~~~
