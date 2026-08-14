---
kind: claim
claim_id: type-I-root-capacity-stutter-transverse-quadratic-shift-type-II-fan
title: 横向 stutter 二次移位的偶 K Type II 终端扇
statement: >-
  对核心素数 p≡1 mod24 的 terminal-first 后 actual proper-root stutter receipt，令
  D*=D/gcd(D,h^2-1)、m=(D+h-1)/p。任取偶数 K≥2 和奇素数 q|D*。若
  q|m+K(K-1)，则 q|((K-1)p-1)(Kp+1)。在正支 q|Kp+1 上，若再有
  q≡3K-1 mod4K，则 s=(q+1)/K 与 C=(p+s)/(4q) 为正整数，3≤s≤p-2，且
  4/p=1/(qC)+1/(KpC)+1/(KpqC) 是一张 Type II 证书。K=2 恰恢复此前的
  m+2、2p+1、q≡5 mod8 分支；该扇不保证任何 D* 素因子命中某个移位或正支，
  也不处理 ((K-1)p-1) 负支。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-transverse-residual-capacity-map
  - type-II-coprime-factor-normal-form
  - short-certificate-equivalence
topics:
  - type-I
  - type-II
  - root-capacity
  - stutter
  - transverse-residual
  - quadratic-shift
  - terminal-dispatch
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-transverse-residual-capacity-map
    role: actual-D-star-transverse-residual-input
  - claim: type-II-coprime-factor-normal-form
    role: Type-II-normal-form-and-reconstruction
  - claim: short-certificate-equivalence
    role: direct-Type-II-certificate-verifier
  - reproduction: reproductions/type_i_root_capacity_stutter_transverse_quadratic_shift_type_ii_fan.py
    role: q-local-shift-and-Type-II-fixed-controls
visibility: public
last_checked: '2026-08-14'
---

# 横向 stutter 二次移位的偶 \(K\) Type II 终端扇

## 1. 设置

固定核心素数

\[
p\equiv1\pmod {24}.
\]

在 terminal-first 后，设一个 actual proper-root stutter receipt 仍存在。沿用

\[
D=mp+1-h,\qquad D\mid ph+1,\qquad
D_*=\frac{D}{(D,h^2-1)}.
\tag{1}
\]

取偶数 \(K\ge2\)，以及一个奇素数 \(q\mid D_*\)。本卡只在额外的二次移位条件

\[
q\mid m+K(K-1)
\tag{2}
\]

成立时分流。它不是说每个 \(D_*\) 都会碰到某个这样的移位。

## 2. 二次移位的线性因子扇

由 \(q\mid D\) 与 (1)，有

\[
h\equiv mp+1\pmod q.
\tag{3}
\]

代入 (2) 后，

\[
h\equiv1-K(K-1)p\pmod q.
\tag{4}
\]

又 \(q\mid ph+1\)，所以

\[
K(K-1)p^2-p-1\equiv0\pmod q.
\tag{5}
\]

左侧有精确分解

\[
\boxed{
K(K-1)p^2-p-1
=\bigl((K-1)p-1\bigr)(Kp+1).
}
\tag{6}
\]

因此

\[
\boxed{
q\mid m+K(K-1)
\Longrightarrow
q\mid\bigl((K-1)p-1\bigr)(Kp+1).
}
\tag{7}
\]

在正支 \(q\mid Kp+1\) 上，(4) 还给出

\[
\boxed{h\equiv K\pmod q.}
\tag{8}
\]

后面的终端剩余类会有 \(q\ge3K-1>K+1\)，故 (8) 自动使
\(q\nmid h^2-1\)。换言之，这确实是与 \(h\pm1\) overlap 不同的横向支；
这里不把它误并入 \(p\pm1\) 分流。

## 3. 正支的偶 \(K\) Type II 证书

再假设

\[
q\mid Kp+1,
\qquad
q\equiv3K-1\pmod {4K}.
\tag{9}
\]

定义

\[
s=\frac{q+1}{K},
\qquad
C=\frac{p+s}{4q}.
\tag{10}
\]

由 (9)，\(s\equiv3\pmod4\) 且 \(s\ge3\)。又 \((q,K)=1\)，并且

\[
K(p+s)=Kp+q+1\equiv0\pmod q,
\tag{11}
\]

所以 \(q\mid p+s\)。由于 \(p\equiv1\pmod4\)、\(s\equiv3\pmod4\)，
\(C\) 是正整数。

还需核对自然缺口范围。若 \(q=Kp+1\)，当 \(K\ge4\) 时它同时模 \(K\)
同余于 \(1\) 和 \(-1\)，矛盾；当 \(K=2\) 时会给出 \(s=p+1\equiv2\pmod4\)，
也与 (9) 矛盾。因此 \(q\) 是奇数 \(Kp+1\) 的真因子，其商至少为 \(3\)。于是

\[
s=\frac{q+1}{K}
\le\frac{p}{3}+\frac4{3K}
\le\frac{p+2}{3}
\le p-2.
\tag{12}
\]

令

\[
x=qC=\frac{p+s}{4},
\qquad d=C.
\tag{13}
\]

则

\[
d\mid x^2,\qquad d\le x,\qquad
s\mid x+d=C(q+1).
\tag{14}
\]

所以 \((s,d)\) 是 Type II 除子证书；在互素正规形中它是

\[
(A,B,C)=(1,q,C),
\qquad
\frac{A+B}{s}=K.
\tag{15}
\]

标准恢复给出显式分母

\[
\boxed{
\frac4p=
\frac1{qC}+
\frac1{KpC}+
\frac1{KpqC}.
}
\tag{16}
\]

## 4. 与已有 \(K=2\) 分支的关系

令 \(K=2\)。式 (7) 正好成为

\[
q\mid m+2
\Longrightarrow q\mid(p-1)(2p+1),
\]

而 (9) 的剩余类正是 \(q\equiv5\pmod8\)。式 (10)--(16) 因而完全恢复
`type-I-root-capacity-stutter-transverse-residual-local-terminal-dispatch` 中的
\(2p+1\) Type II 证书。

\(K=4\) 给出 \(4p+1\) 的一个可重叠 Type II 图表；它不应被记为对既有
\(4p+1\) 分支的额外覆盖。例如 \(K=6\) 的正支呈现为

\[
q\mid6p+1,
\qquad q\equiv17\pmod{24},
\]

并仍由同一公式给出 \(K=6\) 证书。这里仅说明 terminal chart 的可用性，
不声称它与仓库中其他终端家族的覆盖互不相交。

固定 \(q\)-局部控制 \((p,K,q)=(337,6,17)\) 有

\[
s=3,\qquad C=5,
\qquad
\frac4{337}=\frac1{85}+\frac1{10110}+\frac1{171870}.
\tag{17}
\]

复现器还以 \((97,2,5)\) 和 \((1009,4,11)\) 检查 \(K=2,4\)。这些是局部
同余与证书控制，不冒充完整 actual stutter receipt。

## 5. 边界

此扇只关闭同时满足 (2)、正支和 (9) 的残余素因子。它没有证明：

* \(D_*\) 必有素因子整除某个 \(m+K(K-1)\)；
* 命中 (2) 的素因子必落在 \(Kp+1\) 而非 \(((K-1)p-1)\)；
* 所需的偶 \(K\) 有统一界；
* 未命中时存在可提升的严格下降。

所以这是一条新的条件 Type II terminal dispatch，不是 G/Type I global exit 或
global potential 的证明。负支及未命中横向 residual 仍须以 actual receipt
provenance 构造新的证书或 identity lift。

## 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_stutter_transverse_quadratic_shift_type_ii_fan.py --verify
```

脚本只验证三个固定 \(q\)-局部移位控制、因子分解和恢复后的 Type II 分母；它不扫描
素数、根层、分母或历史 selector，也不把局部控制当作 actual receipt。
