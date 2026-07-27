---
kind: claim
claim_id: type-I-rp-plus-one-external-factor-ray
title: rp 加一因子射线给出四分之一范围 Type I 证书
statement: 对核心素数 p 和任意 r=3 mod4，若 rp+1 有奇因子 q=-1 mod r，则令 i=(q+1)/r、m=(p+i)/q；m 是 3 mod4 的自然缺口，满足 m<=(p-1)/4，且 m|(p+i)、4i|(p+m)。故该数据给出一张 Type I 除子证书。反之，每张外部源 Type I 证书唯一给出 r=3 mod4、q|rp+1 与 rp+1=4qt 的这种因子射线正规形。
claim_status: established
topics:
- type-I
- certificate
- external-source
- factorization
- ray
- short-certificate
- proof-program
sources:
- paper: ventas2026
  locator: "Theorem 2.3"
  role: external-source-context
- paper: bradford2024
  locator: "Proposition 1"
  role: Type-I-certificate-reconstruction
visibility: public
last_checked: '2026-07-24'
---

# \(rp+1\) 因子射线给出四分之一范围 Type I 证书

## 定理

令 \(p\equiv1\pmod {24}\) 为素数，且令 \(r\equiv3\pmod4\) 是正整数。
假设 \(rp+1\) 有一个奇因子

\[
q\equiv-1\pmod r. \tag{1}
\]

定义

\[
i=\frac{q+1}{r},\qquad m=\frac{p+i}{q}. \tag{2}
\]

则 \(i,m\) 为正整数，并且

\[
m\equiv3\pmod4,\qquad 3\le m\le\frac{p-1}{4},\qquad
m\mid p+i,\qquad4i\mid p+m. \tag{3}
\]

因此 \(m\) 与 \(d=ix\)、\(x=(p+m)/4\) 给出一张外部源 Type I
除子证书。

反向地，任一外部源见证 \((i,m)\) 令

\[
q=\frac{p+i}{m},\qquad t=\frac{p+m}{4i},\qquad
r=\frac{q+1}{i}, \tag{4}
\]

便唯一满足

\[
r\equiv3\pmod4,\qquad rp+1=4qt,\qquad q\equiv-1\pmod r. \tag{5}
\]

故外部源 Type I 子空间可等价地看作所有 \(r\equiv3\pmod4\) 的移位数
\(rp+1\) 上的因子残数选择问题。

## 证明

由 (1) 写 \(q=ri-1\)。又 \(q\mid rp+1\)，所以

\[
rp+1=4qt
\]

对某个正整数 \(t\) 成立：左边被 \(4\) 整除，且 \(q\) 为奇数。
在模 \(q\) 下，\(ri\equiv1\)；将 \(rp+1\equiv0\pmod q\) 乘以 \(i\)，
得到 \(p+i\equiv0\pmod q\)，故 (2) 中 \(m\) 为整数。

再由 \(q=ri-1\) 和 \(rp+1=4qt\)，

\[
p(q+1)=i(rp+1)=4iqt.
\]

代入 \(q+1=ri\) 并除以 \(q\)，即得 \(p+m=4it\)，从而
\(4i\mid p+m\)。外部源证书结论由
`external-source-type-I-certificate` 立即恢复。

为证界，\(q\) 是奇数且 \(q\equiv-1\pmod r\)，故
\(q\ge2r-1\ge5\)。从 \(rp+1=4qt\) 得
\[
i=\frac{q+1}{r}\le\frac p4+\frac5{4r}\le\frac p4+\frac5{12}.
\]
因而
\[
m=\frac{p+i}{q}\le\frac{p+p/4+5/12}{5}<\frac p4+1.
\]
又 \(m\) 为整数且 \(m\equiv-p\equiv3\pmod4\)，于是
\(m\le(p-1)/4\) 且 \(m\ge3\)。

反向方向中，外部源条件令 \(q,t\) 都为正整数。恒等式
\[
p(q+1)=i(4qt-1)
\]
来自 \(p+i=mq\) 和 \(p+m=4it\)。因 \(i<p\)，素数 \(p\) 不整除
\(i\)，所以 \(p\mid4qt-1\)。令 \(r=(4qt-1)/p\)，上式给出
\(r=(q+1)/i\)；再由 \(4qt=rp+1\) 看出 \(r\equiv3\pmod4\)，并得到
(5)。所有量均由 \((i,m)\) 唯一决定。

## 与递降和筛法的关系

当 \(r=3\) 时，此射线与 `three-p-plus-one-descent-certificate` 的
\((3p+1)/4\) 因子机制相邻，但不是同一张证书。例如
\(p=193,q=5\) 给出 \((i,m)=(2,39)\)；而 \(p=73,q=11\) 给出
\((i,m)=(4,7)\)。

若固定一个素数 \(r\equiv3\pmod4\)，只要 \(rp+1\) 有奇素因子
\(\ell\equiv-1\pmod r\)，便可取 \(q=\ell\)。这给出一条局部密度
\(1/(r-1)\) 的充分覆盖射线；有限多个不同 \(r\) 可进入上界筛。
但固定有限射线仍只给密度结论。当前难点是使 \(r\) 随 \(p\) 选择，或把该
因子条件接入一个真正可闭合的递降状态，而非把有限射线扩充误作全称证明。

## 复现

`external_source_factor_ray_normal_form` 和
`external_source_factor_ray_witness` 实现 (4)--(5) 的双向检查。运行：

\[
\texttt{python3 -m unittest tests.test_external_source -v}.
\]
