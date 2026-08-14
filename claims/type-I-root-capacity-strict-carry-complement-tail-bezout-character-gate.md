---
kind: claim
claim_id: type-I-root-capacity-strict-carry-complement-tail-bezout-character-gate
title: 严格 root carry 互补偶源尾的 Bezout 归一化与二次字符障碍
statement: >-
  对 strict proper-root carry 的 canonical even complement n，在 retained-standard-tail
  域 R=4n-p>0 中，令 w=(Ec+1)/p。若 c 为偶数，取 a=E-4w；若 c 为奇数，取
  a=3E-4w。则 receipt multiplier 满足一个精确 Bezout 恒等式，并强制
  na=-1 (mod R)、pa=-4 (mod R)、pna^2=4 (mod R)。所以 tail selector
  e|(pn)^2、e=-pn (mod R) 等价于 ea^2=-4 (mod R)。对任意奇素数 q|R，
  对固定的 q|R，Legendre target 恒为 (-pn/q)=(-1/q)，不再读取 E、D、h 的
  二次角色；特别地，
  若 q=3 (mod 4) 且 n 的每个素因子都是模 q 二次剩余，则该 tail selector 必空。
  这给出 actual receipt 到 selector 的精确二次 character no-go，同时证明仅靠
  receipt 的二次信息不能强制高半区因子。p=73,r=3 由 q=71 触发该障碍；actual
  high-half control p=313,r=271 通过二次必要门却在模 293 的有限指数盒失败，表明
  二次障碍不是充分条件。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-strict-carry-complement-even-source-gate
  - type-I-root-capacity-strict-carry-support-rebase
topics:
  - type-I
  - root-capacity
  - strict-carry
  - even-source
  - tail-selector
  - bezout
  - quadratic-character
  - divisor-residue
  - obstruction
  - proof-boundary
sources:
  - claim: type-I-root-capacity-strict-carry-complement-even-source-gate
    role: canonical-even-complement-and-exact-tail-selector
  - claim: type-I-root-capacity-strict-carry-support-rebase
    role: actual-receipt-multiplier-and-strict-root-controls
  - reproduction: reproductions/type_i_root_capacity_strict_carry_complement_tail_bezout_character_gate.py
    role: fixed-bezout-character-and-exponent-box-controls
visibility: public
last_checked: '2026-08-14'
---

# 严格 root carry 互补偶源尾的 Bezout 归一化与二次字符障碍

## 1. 设置

固定 core prime \(p\equiv1\pmod {24}\) 的 strict proper-root receipt。沿用其
multiplier \(E\) 与 canonical cofactor

\[
1\le c\le p-2,
\qquad
c\equiv-E^{-1}\pmod p.
\tag{1}
\]

令

\[
w=\frac{Ec+1}{p}.
\tag{2}
\]

这是正整数。按前一张互补偶源卡，定义

\[
n=
\begin{cases}
c,&2\mid c,\\
p-c,&2\nmid c,
\end{cases}
\qquad
R=4n-p,
\qquad S=pn.
\tag{3}
\]

以下讨论 retained-standard-tail 有意义的 \(R>0\) 域，特别包括非平凡的
high-half 域 \(n>p/2\)。该 tail 的精确 selector 是

\[
e\mid S^2,\quad e\le S,\quad e\equiv-S\pmod R.
\tag{4}
\]

## 2. Receipt multiplier 给出的 Bezout 单位

定义一个由 receipt 决定的整数

\[
a=
\begin{cases}
E-4w,&2\mid c,\\
3E-4w,&2\nmid c.
\end{cases}
\tag{5}
\]

它满足下列两种精确恒等式：

\[
\begin{array}{c|c|c}
 & \text{关于 }p & \text{关于 }n\\
\hline
2\mid c & pa+ER=-4 & na+Rw=-1\\
2\nmid c & pa-ER=-4 & na-R(E-w)=-1.
\end{array}
\tag{6}
\]

**证明。** 若 \(2\mid c\)，有 \(n=c\)、\(R=4c-p\)。于是

\[
p(E-4w)+E(4c-p)=4(Ec-pw)=-4,
\]

以及

\[
c(E-4w)+(4c-p)w=Ec-pw=-1.
\]

若 \(2\nmid c\)，有 \(n=p-c\)、\(R=3p-4c\)。直接展开给出

\[
p(3E-4w)-E(3p-4c)=4(Ec-pw)=-4,
\]

和

\[
(p-c)(3E-4w)-(3p-4c)(E-w)=Ec-pw=-1.
\]

证毕。

因此在两种 parity 下都得到

\[
\boxed{
na\equiv-1\pmod R,
\qquad
pa\equiv-4\pmod R,
\qquad
Sa^2\equiv4\pmod R.}
\tag{7}
\]

特别地 \((a,R)=1\)。把 (4) 乘以可逆的 \(a^2\)，得到 root-aware 的完全等价改写

\[
\boxed{
e\equiv-S\pmod R
\Longleftrightarrow
ea^2\equiv-4\pmod R.}
\tag{8}
\]

这不是又一个充分条件：它精确重写了同一个 tail selector。它的价值是把 actual receipt
的 \(E\) 投影成一个明确的 modular inverse，从而可以逐 character 判断哪些 receipt
信息仍然存在。

## 3. 二次角色完全消去 receipt multiplier

令 \(q\) 是任意奇素数且 \(q\mid R\)。因为

\[
(R,pn)=1,
\tag{9}
\]

Legendre 符号均有定义。由 (7) 可得

\[
\left(\frac{S}{q}\right)=1,
\qquad
\boxed{
\left(\frac{-S}{q}\right)=\left(\frac{-1}{q}\right).}
\tag{10}
\]

所以即使 \(a\) 本身依赖 \(E\)，一旦 \(n,R\) 及其中的 \(q\) 已固定，selector
target 的二次类便不再读取 \(E\)、\(D\) 或 \(h\) 的二次角色。换言之，任何只试图从
actual receipt 提取二次 character 信息来强制 (4) 的策略，在到达既定 \(R\) 的二次商后
不会比 \(-1\) 获得更多目标信息；receipt 仍可通过选择 \(n,R\) 间接影响所用的模数。

这立即给出一个可检验的 no-go。

**二次字符障碍。** 若存在素数 \(q\mid R\) 满足

\[
q\equiv3\pmod4,
\qquad
\left(\frac{\ell}{q}\right)=1
\quad\text{对每个素数 }\ell\mid n,
\tag{11}
\]

则 (4) 无解。

的确，\(p\equiv4n\pmod q\)，所以 (11) 也给出 \((p/q)=1\)。因此 \(S^2\) 的
每个因子 \(e\) 都是模 \(q\) 的二次剩余；但 (10) 与 \(q\equiv3\pmod4\) 给出
\((-S/q)=-1\)，不可能有 \(e\equiv-S\pmod q\)。

这只是必要 no-go，不是充分判据。若 (11) 失败，selector 仍可能因更高阶 character、
有限指数范围或完整 CRT 同余而为空。

## 4. 固定 actual controls

### \(p=73,r=3\)：二次障碍解释 tail miss

该 actual strict root 有

\[
E=10583,
\qquad c=37,
\qquad w=5364,
\qquad n=36,
\qquad R=71.
\]

这里 \(c\) 为奇数，故 \(a=3E-4w=10293\)，并有

\[
73a-10583\cdot71=-4,
\qquad
36a-71(10583-5364)=-1.
\tag{12}
\]

虽然 \(n=36\) 属于中间带而非 high half，它已经给出一个干净的 actual receipt
character control。因为

\[
71\equiv3\pmod4,
\qquad
\left(\frac2{71}\right)=
\left(\frac3{71}\right)=1,
\tag{13}
\]

而 \(n=2^2 3^2\)，(11) 成立。故 retained-standard-tail 的 factor selector
无解，这不再只是 75 个因子的枚举事实。

### \(p=313,r=271\)：二次门通过但有限指数盒仍失败

这个 actual high-half strict control 有

\[
E=2077472563,
\quad c=n=298,
\quad w=1977913175,
\quad R=879=3\cdot293,
\quad S=2\cdot149\cdot313.
\tag{14}
\]

现在 \(a=E-4w=-5834180137\)，且

\[
313a+2077472563\cdot879=-4.
\tag{15}
\]

模 \(3\) 时，\(2\) 和 \(149\) 都是二次非剩余，故 (11) 不触发；模 \(293\) 时
\(-1\) 是二次剩余。这个 control 因而说明二次障碍不是充分条件。

事实上 \(2\) 是 \(\mathbb F_{293}^{\times}\) 的生成元，并有

\[
\log_2(149)=172,
\qquad
\log_2(313)=175,
\qquad
\log_2(-S)=\log_2(193)=202
\pmod {292}.
\tag{16}
\]

若 (4) 有解，某个 \(e=2^\alpha149^\beta313^\gamma\) 必满足

\[
\alpha+172\beta+175\gamma\equiv202\pmod {292},
\qquad
0\le\alpha,\beta,\gamma\le2.
\tag{17}
\]

这个 27 元指数盒为空，故 (4) 在该 actual high-half control 仍失败。它指出下一步
不能停在 Legendre 层，必须真正利用 higher-order/exponent-box 结构，或接入 \(D,h,Q\)
的赋值来源。

## 5. 对全局出口的影响

(6)--(10) 是 strict root receipt 通向小偶源 tail selector 的第一条精确代数桥。
它同时给出正、反两面信息：实际 \(E\) 可被序列化为 Bezout witness \(a\)，但二次层
完全丢失其区分力；(11) 能消去一部分 tail，但不会强制余下的 tail 命中。因而尚未得到
一个 universal \(n<p\) exit。

下一步应只研究两种仍可能带来实质进展的对象：

1. actual \(D\mid ph+1\) 与 \(D\mid K\) 是否限制 (17) 中可出现的 higher-order
   exponent box；
2. high-half 未命中是否能从 receipt valuation 直接回译为 Type I/II terminal 或
   support-rebase 的可注册 strict edge。

这比对任意 even source 扩大扫描更接近 strict-root global exit。

## 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_strict_carry_complement_tail_bezout_character_gate.py --verify
```

该回执只检查 (6)--(17) 的两个 actual root controls；不扫描素数、root 参数、分母或
历史 selector。
