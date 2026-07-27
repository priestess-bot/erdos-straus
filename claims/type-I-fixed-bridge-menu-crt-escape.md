---
kind: claim
claim_id: type-I-fixed-bridge-menu-crt-escape
title: 十六桥模板的CRT无穷源侧逃逸
statement: 对五千万最终残余上使用的16个固定桥因子模板，考虑每个E=sR+1的全部正奇因子分解（包括R=1）。其源平方同余模数与24的最小公倍数为781779462544080。核心剩余p=73模该数与模数互素且避开全部128个必要同余p=s模Lambda(E)。故由Dirichlet等差数列素数定理，存在无穷多个p=1模24的素数对这16个桥模板均无源平方兼容状态；因而该固定桥菜单不能成为Erdos--Straus猜想的全称Type I选择器。
claim_status: established
topics:
- type-I
- source-state
- bridge
- congruence
- CRT
- Dirichlet-progressions
- obstruction
- selector
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 十六桥模板的 CRT 无穷源侧逃逸

令 \(\mathcal E\) 为[桥模板驱动审计](type-I-adaptive-bridge-menu-profile-50m.md)中的 16 个偶数 \(E\)。
对每个 \(E\)，考虑所有

\[
E=sR+1,\qquad s,R>0\text{ 为奇数}. \tag{1}
\]

这里特意包含 \(R=1\)，所以本结论不依赖计算选择器中为自然缺口而设置的 \(R\ge3\) 门槛。
按[源平方同余模数](type-I-source-square-congruence-modulus.md)，任何以该状态为桥的偶源
\(n=p-s\) 必须满足

\[
p\equiv s\pmod{\Lambda(E)}. \tag{2}
\]

16 个 \(E\) 的全部正奇状态共 128 个。令

\[
M=\operatorname{lcm}\left(24,\{\Lambda(E):(s,R)\text{ 满足 (1)}\}\right)
=781{,}779{,}462{,}544{,}080. \tag{3}
\]

## 定理

对所有 128 个状态，均有

\[
73\not\equiv s\pmod{\Lambda(E)}. \tag{4}
\]

并且

\[
73\equiv1\pmod{24},\qquad\gcd(73,M)=1. \tag{5}
\]

因此，Dirichlet 关于互素等差数列中素数的定理给出无穷多个素数

\[
p\equiv73\pmod M. \tag{6}
\]

它们全部是核心素数 \(p\equiv1\pmod{24}\)。对充分大的这类 \(p\)，每个固定模板的候选源
\(p-s\) 都为正偶数，但 (4) 违反必要条件 (2)。故这些 \(p\) 对 \(\mathcal E\) 的任何桥模板
都没有源平方兼容状态，更不可能通过后续的 \(K\) 因子对剩余条件。

## 证明

式 (2) 是源平方同余模数引理。程序逐一枚举 (1) 的 128 个状态，计算其 \(\Lambda(E)\)，并直接验证
(3)--(5)。因为每个 \(\Lambda(E)\mid M\)，类 (6) 中任意 \(p\) 在每一个所需模数上的余数均与 73
相同，故 (4) 逐状态推出 (2) 失败。最后由 (5) 和 Dirichlet 定理得到无穷多个素数项。

这比有限范围中的“未命中”更强：它证明这 16 个**固定**桥模板绝不可能成为全称 Type I 选择器，且
失败发生在任何 \(BC\mid K\) 的除子搜索之前。它不排除 (E) 或 (s) 随 (p) 自适应增长的选择律，
不排除菜单外的 Type I 状态，也不排除 Type II 或其他解提升递降机制。

可复现命令：

~~~bash
python3 reproductions/type_i_fixed_bridge_menu_crt_escape.py
python3 -m unittest tests/test_type_i_fixed_bridge_menu_crt_escape.py -q
~~~
