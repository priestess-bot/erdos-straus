---
kind: claim
claim_id: fct-three-term-type-I-equivalence
title: 三项 ceiling-FCT 与外部 source Type I 证书的精确等价
statement: 对三项 ceiling-FCT 的正系数 c0,c1,c2，若 p=c2(c0c1-1)-c0 是核心素数且 4k=c1c2-1，则除以 k 后的三项 FCT 分解恰给出缺口 m=c2、首分母 x=kc0、除子 D=c0x 的 Type I 证书。反之，每张外部 source Type I 证书唯一恢复 c0=i、c1=((p+i)/m+1)/i、c2=m。故 FCT 的确定性三项构造与外部 source Type I 射线完全相同，不是无标记严格递降。
claim_status: established
topics:
- continued-fractions
- type-I
- external-source
- certificate
- equivalence
- proof-program
sources:
- paper: ventas2026
  locator: "Theorems 2.1--2.3"
  role: FCT-construction-context
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-certificate-reconstruction
visibility: public
last_checked: '2026-07-25'
---

# 三项 ceiling-FCT 与外部 source Type I 证书的精确等价

## 定理

取正整数 \(c_0,c_1,c_2\)，并定义

\[
p_0=c_0,\qquad p_1=c_0c_1-1,\qquad
p=c_2p_1-c_0,\qquad 4k=c_1c_2-1. \tag{1}
\]

设 \(4k\) 为正整数且 \(p\equiv1\pmod{24}\) 为素数。三项 ceiling-FCT 在除以
\(k\) 后给出

\[
\frac4p
=\frac1{kp_0}+\frac1{kp_0p_1}+\frac1{kp_1p}. \tag{2}
\]

令

\[
m=c_2,\qquad x=kc_0,\qquad D=c_0x. \tag{3}
\]

则 \((m,D)\) 是 (2) 的 Type I 除子证书。反过来，任取外部 source 证书

\[
m\mid p+i,\qquad4i\mid p+m,\qquad
x=\frac{p+m}{4}, \tag{4}
\]

令

\[
c_0=i,\qquad
c_1=\frac{(p+i)/m+1}{i},\qquad
c_2=m,\qquad
k=\frac xi. \tag{5}
\]

这些量皆为正整数，且 (1) 重建原来的 \(p,k\) 与分母。因此 (1)--(3) 和
(4)--(5) 互为双射。

## 证明

由 (1) 有

\[
c_1p+1
=c_1(c_2p_1-c_0)+1
=(c_1c_2-1)p_1
=4kp_1.
\]

故 (2) 的右侧等于

\[
\frac{c_1}{kp_1}+\frac1{kp_1p}
=\frac{c_1p+1}{kp_1p}
=\frac4p.
\]

又

\[
4x-p=(c_1c_2-1)c_0-(c_2p_1-c_0)=c_2=m, \tag{6}
\]

并且 \(D=c_0x\mid x^2\)，因为 \(x=kc_0\)。由
\(p+c_0=c_2p_1\) 可得

\[
\frac{px+D}{m}
=\frac{kc_0(p+c_0)}{c_2}
=kc_0p_1. \tag{7}
\]

另有 \(x^2/D=k\)，所以

\[
\frac{p(x+px^2/D)}m
=\frac{pk(c_0+p)}{c_2}
=kp_1p. \tag{8}
\]

这正是 Type I 的两条恢复分母。

反向地，(4) 给出 \(i\mid x\)，故 \(k=x/i\) 为整数。设
\(p_1=(p+i)/m\)。由于 \(m=4ki-p\)，模 \(i\) 有 \(m\equiv-p\)，而
\(p+i=mp_1\)。又 \(0<i\le x<p\)，所以 \((p,i)=1\)，从而
\(p_1\equiv-1\pmod i\)，故 (5) 中的 \(c_1\) 是正整数。直接计算：

\[
c_1m-1
=\frac{(p_1+1)m}{i}-1
=\frac{p+m}{i}
=4k, \tag{9}
\]

\[
c_2(c_0c_1-1)-c_0=mp_1-i=p. \tag{10}
\]

因此精确恢复 (1)，证毕。

## 独立审计

`reproductions/fct_type_i_equivalence.py` 用整数递推、外部 source 重建和精确有理数
恒等式验证该双射。在

\[
p\le5000,\qquad p\equiv1\pmod{24},\qquad1\le i\le32
\]

的审计中，76 个核心素数给出 386 个外部 source 见证；每一个都成功恢复 FCT
系数、三条分母及同一张 Type I 证书。代表性例子为

\[
(p,i,m)=(73,4,7),
\]

对应 \((c_0,c_1,c_2,k)=(4,3,7,5)\)，并给出

\[
\frac4{73}=\frac1{20}+\frac1{220}+\frac1{4015}.
\]

重建命令：

```bash
python3 reproductions/fct_type_i_equivalence.py
python3 -m unittest tests/test_fct_type_i_equivalence.py -q
```

## 研究含义与边界

Ventas 的三项 FCT 构造提供了有用的搜索坐标和外部整数 \(p+i\) 的因子视角，但其
确定性部分不超出外部 source Type I 证书的 \(x\mid D\) 子空间。特别地，它并没有
把任意一个较小分母实例的解无标记地提升到 \(p\)；所有成功仍等价于选出目标的特定
Type I 证书。

该文的 source 独立性、除子机会数与 Borel--Cantelli 推论只属于其随机模型，不能
推出对每个素数存在 (4)。因此 FCT 若要成为主证路线，必须额外证明一个确定性的、
随 \(p\) 自适应增长的外部 source 选择器，或产出不属于 (3) 的新提升恒等式。
