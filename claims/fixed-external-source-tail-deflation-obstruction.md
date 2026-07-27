---
kind: claim
claim_id: fixed-external-source-tail-deflation-obstruction
title: 固定外源直接证书的尾部递降有限性判据
statement: 设互素正整数s,m给出一张外源Type I直接证书：m=3 mod4，m|(p+s)，4s|(p+m)。令A=(p+m)/(4s)、B=(p+s)/m、q=(B+1)/s=(4A+1)/m。保持该证书前两项并把末项pAB缩为AB可形成严格递降，当且仅当q+1|(m+1)(s+1)。因此固定(s,m)至多给出有限多个这类严格递降；具体地p<=ms((m+1)(s+1)-1)-m-s。边界点p=477015289的(s,m)=(29,27)有q+1=609216，但(m+1)(s+1)=840，故其gap-27直接证书不能按此尾部去缩放。
claim_status: established
topics:
- type-I
- descent
- external-source
- obstruction
- parametrization
sources:
- paper: bradford2024
  locator: Propositions 1--3
  role: Type-I-certificate-context
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-27'
---

# 固定外源直接证书的尾部递降有限性判据

## 定理

设 $p\equiv1\pmod {24}$，并取正整数 $s,m$，满足

$$
(s,m)=1,\qquad m\equiv3\pmod4,\qquad m\mid p+s,\qquad4s\mid p+m.
$$

定义

$$
A=\frac{p+m}{4s},\qquad B=\frac{p+s}{m}.
$$

这给出外源 Type I 直接证书

$$
\frac4p=\frac1{sA}+\frac1{sAB}+\frac1{pAB}. \tag{1}
$$

再令

$$
q=\frac{B+1}{s}=\frac{4A+1}{m}. \tag{2}
$$

两个商在这里均为整数。保持 (1) 的前两项，并把第三分母 $pAB$ 缩为 $AB$，能得到严格源

$$
\frac4n=\frac1{sA}+\frac1{sAB}+\frac1{AB},\qquad
n=\frac{4AB}{q+1}<p, \tag{3}
$$

当且仅当

$$
q+1\mid(m+1)(s+1). \tag{4}
$$

特别地，对固定的一对 $(s,m)$，(4) 迫使

$$
q+1\le(m+1)(s+1),
$$

从而

$$
p=msq-m-s\le ms\bigl((m+1)(s+1)-1\bigr)-m-s. \tag{5}
$$

因此固定外源参数的直接证书无穷同余族，不可能通过这种“保持前两项、去缩放末尾”的方式提供
无穷严格递降族。

## 证明

由 $p=4sA-m=mB-s$ 得

$$
s(4A+1)=m(B+1). \tag{6}
$$

互素性给出 (2)。(1) 的 Type I 正规形为 $(A_0,B_0,C_0)=(s,1,A)$。将其代入
[Type I 正规尾部递降选择器](type-I-normal-tail-deflation-selector.md)，严格去缩放的条件是

$$
q+1\mid4A(s+1). \tag{7}
$$

但 $4A=mq-1$；模 $q+1$ 有 $q\equiv-1$，所以 (7) 等价于

$$
q+1\mid-(m+1)(s+1),
$$

即 (4)。此时选择器中的源分母化为 $n=4AB/(q+1)$，源三元组正是 (3)。其严格性也可由
该选择器保证；直接比较则为

$$
\frac np=\frac{(p+m)B}{p(B+s+1)}<1,
$$

其中不等式等价于 $p+s<p(s+1)$。

最后，由 $p=msq-m-s$ 和 (4) 的正整数界得到 (5)。

## 五亿边界点

在

$$
p=477{,}015{,}289,\qquad(s,m)=(29,27)
$$

处，[gap-27 外源同余直接证书族](gap-27-external-source-progression.md) 给出

$$
A=4{,}112{,}201,\qquad B=17{,}667{,}234,\qquad q=609{,}215.
$$

故 $q+1=609{,}216$，而 $(m+1)(s+1)=840$，(4) 失败。事实上该固定参数下任何此型严格
去缩放都必须满足 $p\le656{,}881$；这个五亿点不可能由该固定 $(29,27)$ 直接证书尾部
产生严格递降。

这不是“没有任何严格递降”的结论，只排除了从这张固定外源直接证书读取的一个具体提升形状。
它也不与该点已有的直接 Type I 证书矛盾；恰恰说明直接证书与可提升证书必须分别优化。
