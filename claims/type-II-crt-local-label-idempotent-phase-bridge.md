---
kind: claim
claim_id: type-II-crt-local-label-idempotent-phase-bridge
title: Type II CRT 局部标签到全局 Fourier 的幂等元桥
statement: 对两两互素的局部因子 h_i，局部标签只能先组成直和标签群并经 CRT 幂等元嵌入到 Z/hZ；把局部代表直接代入全局 h-角色在两个以上非平凡块时只有零频率与代表选择无关。幂等元桥给出规范的局部相位，并可继续送入有限阿贝尔源商的 SNF 提升门。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-same-modulus-source-switch-crt-criterion
  - type-II-raw-finite-abelian-source-lift-snf
topics:
  - type-II
  - CRT
  - local-label
  - Fourier
  - idempotent
  - source-switch
  - lift-compatibility
  - proof-boundary
sources:
  - claim: type-II-same-modulus-source-switch-crt-criterion
    role: local-source-crt-data
  - claim: type-II-raw-finite-abelian-source-lift-snf
    role: finite-abelian-source-character-gate
visibility: public
last_checked: '2026-08-05'
---

# Type II CRT 局部标签到全局 Fourier 的幂等元桥

## 1. 局部标签不是共同模数元素

令 \(h_1,\ldots,h_r>1\) 两两互素，并令

\[
h=\prod_{i=1}^{r}h_i.
\tag{1}
\]

一个来源参数只给出局部标签
\(x_i\in\mathbb Z/h_i\mathbb Z\)。这些标签自然组成

\[
\mathcal L=\bigoplus_{i=1}^{r}\mathbb Z/h_i\mathbb Z,
\tag{2}
\]

而不是 \(r\) 个有规范意义的 \(\mathbb Z/h\mathbb Z\) 元素。若直接选一个整数代表
\(\widetilde x_i\) 并写 \(e^{2\pi i k\widetilde x_i/h}\)，则把局部模数和全局模数
混在了一起；代表 \(\widetilde x_i+h_i\) 的替换会改变这个相位。

## 2. CRT 幂等元嵌入

置

\[
H_i=\frac h{h_i},
\qquad
t_i\equiv H_i^{-1}\pmod{h_i},
\qquad
E_i=H_i t_i.
\tag{3}
\]

则

\[
E_i\equiv1\pmod{h_i},
\qquad
E_i\equiv0\pmod{h_j}\quad(j\ne i).
\tag{4}
\]

由此得到规范 CRT 同构

\[
\Phi:\mathcal L\longrightarrow\mathbb Z/h\mathbb Z,
\qquad
\Phi(x_1,\ldots,x_r)=\sum_{i=1}^{r}E_i x_i\pmod h.
\tag{5}
\]

它与局部代表选择无关，并满足
\(\Phi(x)\equiv x_i\pmod{h_i}\)。对全局频率
\(k\in\mathbb Z/h\mathbb Z\)，全局角色

\[
\eta_k(y)=\exp\!\left(\frac{2\pi i ky}{h}\right)
\tag{6}
\]

拉回为

\[
\eta_k(\Phi(x_1,\ldots,x_r))
=
\prod_{i=1}^{r}
\exp\!\left(\frac{2\pi i k t_i x_i}{h_i}\right).
\tag{7}
\]

因此正确的局部相位不是 \(k x_i/h\)，而是
\(k t_i x_i/h_i\)。式 (7) 是把局部来源标签送入全局 Fourier 的唯一自然桥。

若真实源关系商 \(H\) 的指数为 \(E\)，则第 \(i\) 个局部角色的阶为

\[
\operatorname{ord}\!\left(
x_i\mapsto\exp\!\left(\frac{2\pi i k t_i x_i}{h_i}\right)
\right)
=\frac{h_i}{\gcd(h_i,k)},
\tag{7a}
\]

因为 \(t_i\) 与 \(h_i\) 互素。故任何提升到 \(H\) 的全局频率都必须满足

\[
\frac{h_i}{\gcd(h_i,k)}\mid E
\qquad(1\le i\le r).
\tag{7b}
\]

对两两互素的 \(h_i\)，这些条件的解集恰为

\[
\left\{
k\in\mathbb Z/h\mathbb Z:
\frac h{\gcd(h,E)}\mid k
\right\}
\simeq \mathbb Z/\gcd(h,E)\mathbb Z.
\tag{7c}
\]

因此 (7c) 是局部 CRT 版本的精确阶筛；通过它仍需继续检查源标签与锚点的 SNF
关系相容性。

## 3. 直接代入的严格障碍

若试图在局部群 \(\mathbb Z/h_i\mathbb Z\) 上使用“直接代入”相位

\[
\widetilde\eta_{k,i}(x_i)
=\exp\!\left(\frac{2\pi i k\widetilde x_i}{h}\right),
\tag{8}
\]

则它与代表选择无关，当且仅当

\[
\exp\!\left(\frac{2\pi i k h_i}{h}\right)=1
\iff
\frac h{h_i}\mid k.
\tag{9}
\]

若要求所有局部块都满足 (9)，则

\[
\operatorname{lcm}_{1\le i\le r}\frac h{h_i}\mid k.
\tag{10}
\]

当 \(r\ge2\) 且 \(h_i\) 两两互素时，左侧等于 \(h\)：每个 \(h_i\) 都出现在某个
\(h/h_j\)（取 \(j\ne i\)）中，故其最小公倍数包含全部互素因子。于是

\[
\boxed{
\text{两个以上互素局部块中，直接代入全局 }h\text{-角色只有 }k=0
\text{ 与代表选择无关。}
}
\tag{11}
\]

这说明把 \(a_i\bmod h_i\) 直接写成共同 \(\mathbb Z/h\mathbb Z\) Fourier 标签，
再把所得频率计入乘法容量，是一个严格的来源错误，而不是小的归一化问题。

## 4. 与带来源 CRT 及 SNF 的正确接线

在同模数 source-switch 中，局部来源给出

\[
a_i\in\mathbb Z/h_i\mathbb Z,
\qquad
a_0=\Phi(a_1,\ldots,a_r)\in\mathbb Z/h\mathbb Z.
\tag{12}
\]

这里 \(a_0\) 是 CRT 合并后的全局参数；只有 \(a_0\) 可以直接参与
\(\mathbb Z/h\mathbb Z\) 的 raw 残数 Fourier。若要保留每个局部来源的相位，则必须
使用式 (7) 的局部角色，随后把源单位、锚点和这些局部相位一起送入
有限阿贝尔源商的 SNF 系统。SNF 通过时得到真实源角色；失败时输出逐行整除或
关系组合的 LIFT_OBSTRUCTED 回执。

因此正确的处理顺序是：

1. 在 \(\bigoplus_i\mathbb Z/h_i\mathbb Z\) 中保留局部标签；
2. 用幂等元 (5) 合并为全局标签，或用 (7) 保留局部角色；
3. 对真实源单位和锚点执行 SNF 相容性检查；
4. 只有通过后才把 Fourier 系数送入 F/G 容量或 Type II source-switch。

## 5. \(p=97\) 的伪池化边界

取 \(h_1=11,h_2=13,h=143\)，局部标签

\[
(a_1,a_2)=(1\bmod11,\ 3\bmod13).
\]

幂等元为

\[
E_1=13\cdot13^{-1}\!\!\pmod{11}=78,
\qquad
E_2=11\cdot11^{-1}\!\!\pmod{13}=66,
\]

故全局 CRT 参数为

\[
a_0\equiv78\cdot1+66\cdot3\equiv133\pmod{143}.
\tag{13}
\]

若错误地把局部代表 \(1,3\) 直接当成 \(\mathbb Z/143\mathbb Z\) 标签，则它们在
代表替换 \(1\mapsto12\) 或 \(3\mapsto16\) 后相位改变；由 (11)，所有局部同时
代表无关的频率只能是 \(k=0\)。正确的全局标签是 \(133\)，而不是把 \(1,3\)
分别作为两个共同模数元素。对 \(U(24)\) 的真实源单位 \(11,13\)，再将局部/全局
相位送入 SNF（或先做指数 2 阶筛）会得到 LIFT_OBSTRUCTED；这正是该伪池化不能
直接升级为 Type II 的来源。

## 研究边界

幂等元桥解决局部 CRT 标签的规范化和代表选择问题，但不自动提供
\(\bigoplus_i\mathbb Z/h_i\mathbb Z\) 到真实单位源商的同态，也不证明 SNF 通过后有
统一短载体。后续仍需构造 raw 残数到源单位的有界标记，或证明标签/SNF 失败能产生
更小且可提升的 Type I/II 实例。
