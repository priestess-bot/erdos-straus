---
kind: claim
claim_id: type-I-root-capacity-stutter-transverse-general-quadratic-type-II-fan
title: 横向 stutter 的一般 A 型二次移位 Type II 终端扇
statement: >-
  对核心素数 p≡1 mod24 的 terminal-first 后 actual proper-root stutter receipt，令
  D=mp+1-h 且 D|ph+1。取 p+3 的奇除数 A0、偶数 K>A0、gcd(A0,K)=1，及奇素数
  q|D。若 q|m A0^2+K(K-A0)，则 q|((K-A0)p-A0)(Kp+A0)。在正支
  q|Kp+A0 上，若 q≡3K-A0 mod 4A0K，则 q 自动整除 D*=D/gcd(D,h^2-1)，且
  s=(q+A0)/K、C=(p+s)/(4A0q) 为正整数，3≤s≤p-2；
  4/p=1/(A0qC)+1/(pA0CK)+1/(pqCK) 是一张 Type II 证书。A0=1 正好恢复
  既有偶 K 二次移位扇；本扇不保证任何 actual residual 命中移位、正支或剩余类，
  也不处理负支。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-general-endpoint-divisor-gate
  - type-I-root-capacity-stutter-transverse-quadratic-shift-type-II-fan
  - type-II-raw-ray-certificate
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
  - claim: type-I-root-capacity-general-endpoint-divisor-gate
    role: actual-stutter-D-and-ph-plus-one-divisor-gate
  - claim: type-I-root-capacity-stutter-transverse-quadratic-shift-type-II-fan
    role: A-zero-equals-one-special-slice
  - claim: type-II-raw-ray-certificate
    role: Type-II-raw-ray-certificate-reconstruction
  - claim: short-certificate-equivalence
    role: direct-Type-II-certificate-verifier
  - reproduction: reproductions/type_i_root_capacity_stutter_transverse_general_quadratic_type_ii_fan.py
    role: q-local-general-A-shift-and-Type-II-fixed-controls
visibility: public
last_checked: '2026-08-14'
---

# 横向 stutter 的一般 \(A_0\) 型二次移位 Type II 终端扇

## 1. 设置

固定核心素数

\[
p\equiv1\pmod {24}.
\]

在 terminal-first 后，设一个 actual proper-root stutter receipt 仍存在。沿用

\[
D=mp+1-h,
\qquad
D\mid ph+1,
\qquad
D_*=\frac{D}{(D,h^2-1)}.
\tag{1}
\]

这里的 \(A_0\) 是 Type II raw-ray 坐标，和根容量中可能出现的其他 \(A\) 无关。
取

\[
A_0\mid p+3,
\qquad
A_0\ \text{为奇数},
\qquad
K>A_0,
\qquad
K\equiv0\pmod2,
\qquad
(A_0,K)=1,
\tag{2}
\]

以及一个奇素数 \(q\mid D\)。本卡只在一般二次移位

\[
q\mid mA_0^2+K(K-A_0)
\tag{3}
\]

命中时分流。式 (3) 在 \(A_0=1\) 时就是已有的
\(q\mid m+K(K-1)\)。

## 2. 一般二次移位的线性因子扇

由 \(q\mid D\) 和 (1)，有

\[
h\equiv mp+1\pmod q,
\qquad
mp^2+p+1\equiv0\pmod q.
\tag{4}
\]

将第二式乘以 \(A_0^2\)，再使用 (3)，得到

\[
\begin{aligned}
\bigl(Kp+A_0\bigr)\bigl((K-A_0)p-A_0\bigr)
 &=K(K-A_0)p^2-A_0^2p-A_0^2\\
 &\equiv-A_0^2(mp^2+p+1)\\
 &\equiv0\pmod q.
\end{aligned}
\tag{5}
\]

因此

\[
\boxed{
q\mid mA_0^2+K(K-A_0)
\Longrightarrow
q\mid\bigl(Kp+A_0\bigr)\bigl((K-A_0)p-A_0\bigr).}
\tag{6}
\]

本卡只处理正支

\[
q\mid Kp+A_0.
\tag{7}
\]

由 (2) 及下面的剩余类条件可得 \((q,K)=1\)。又 \(q\nmid p\)，因为
\(q\mid D\mid ph+1\)；若 \(q\mid A_0\)，(7) 会推出 \(q\mid K\)，矛盾。
所以 \((q,A_0K)=1\)。将 (3)、(4)、(7) 联立，另有精确的高度余数

\[
\boxed{A_0h\equiv K\pmod q.}
\tag{8}
\]

## 3. 正支的 Type II 证书

再假设

\[
q\equiv3K-A_0\pmod {4A_0K}.
\tag{9}
\]

定义

\[
s=\frac{q+A_0}{K},
\qquad
C=\frac{p+s}{4A_0q}.
\tag{10}
\]

由 (9)，有

\[
s\equiv3\pmod {4A_0},
\qquad s\ge3.
\tag{11}
\]

又 \(A_0\) 为奇数且 \(A_0\mid p+3\)，而 \(p\equiv1\pmod4\)，故

\[
4A_0\mid p+3.
\tag{12}
\]

另一方面，(7) 给出

\[
K(p+s)=Kp+q+A_0\equiv0\pmod q.
\tag{13}
\]

因为 \((q,K)=1\)，有 \(q\mid p+s\)。再由 (11)--(12) 及
\((q,4A_0)=1\)，得到 \(C\in\mathbb Z_{>0}\)。

还须核对自然缺口范围。若 \(q=Kp+A_0\)，将 (9) 模 \(K\) 化简会给出
\(K\mid2A_0\)。由 (2) 只能有 \((K,A_0)=(2,1)\)，但此时
\(2p+1\equiv3\pmod8\)，与 (9) 要求的 \(5\pmod8\) 矛盾。因此 \(q\) 是
奇数 \(Kp+A_0\) 的真因子，其商至少为 \(3\)。所以

\[
s\le\frac p3+\frac{4A_0}{3K}
<\frac p3+\frac43
\le p-2.
\tag{14}
\]

最后，由 (9) 有 \(q=Ks-A_0\ge3K-A_0>A_0\)。令

\[
x=A_0qC,
\qquad d=A_0^2C.
\tag{15}
\]

则 \(d\mid x^2\)、\(d\le x\)，且

\[
x+d=A_0C(q+A_0)=A_0CKs.
\tag{16}
\]

故 \((s,d)\) 是一张 Type II 除子证书。等价地，raw-ray 的生成模数为

\[
4A_0CK-1=\frac{Kp+A_0}{q},
\tag{17}
\]

其 \(B\)-坐标恰为 \(q\)。恢复得到

\[
\boxed{
\frac4p=
\frac1{A_0qC}+
\frac1{pA_0CK}+
\frac1{pqCK}.}
\tag{18}
\]

## 4. 该正支自动横向

由 (9)--(11)，

\[
q=Ks-A_0\ge3K-A_0>K+A_0.
\tag{19}
\]

若 \(q\mid h-1\)，(8) 会给出 \(K\equiv A_0\pmod q\)；若
\(q\mid h+1\)，则给出 \(K\equiv-A_0\pmod q\)。两种情况分别与

\[
0<K-A_0<q,
\qquad
0<K+A_0<q
\tag{20}
\]

矛盾。因此

\[
\boxed{q\nmid h^2-1,\qquad q\mid D_*.}
\tag{21}
\]

所以虽然输入只需 \(q\mid D\)，正支 terminal 实际总是读取真正的横向 residual。
取 \(A_0=1\) 时，(3)、(6)、(9)、(18) 恰恢复已有偶 \(K\) 二次移位扇。

## 5. 固定局部控制

取

\[
(p,A_0,K,q,m,h)=(1297,5,6,13,6,9).
\tag{22}
\]

它满足 \(p\equiv1\pmod{24}\)、\(5\mid p+3\)、

\[
13\mid6\cdot1297+5,
\qquad
13\mid6\cdot5^2+6(6-5),
\qquad
13\equiv3\cdot6-5\pmod {120}.
\tag{23}
\]

局部 stutter 同余也有

\[
13\mid6\cdot1297+1-9,
\qquad
13\mid1297\cdot9+1,
\qquad
5\cdot9\equiv6pmod {13}.
\tag{24}
\]

这里 \(s=3,C=5\)，所以

\[
\frac4{1297}=
\frac1{325}+
\frac1{194550}+
\frac1{505830}.
\tag{25}
\]

这是 \(A_0>1\) 的局部 terminal control；它只检验 (3)--(18) 的算术，**不**把
\((22)\) 冒充 actual root receipt。复现器同时重放 \(A_0=1\) 的 \(K=6\) 行。

## 6. 边界

本扇没有证明：

* actual \(D_*\) 必有奇素因子命中某个一般二次移位；
* 命中 (3) 的素因子必落在正支而非 \(((K-A_0)p-A_0)\) 负支；
* 所需 \((A_0,K)\) 有统一界；
* 未命中时存在另一张 Type I/II 证书或带 identity lift 的严格递降。

它因而是 terminal-first 菜单的严格扩张，而不是 G/Type I global exit 或 global
potential 的证明。菜单未命中的 actual transverse residual 仍须进入新 provenance
adapter 或可验证的递降构造。

## 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_stutter_transverse_general_quadratic_type_ii_fan.py --verify
```

脚本只验证一个 \(A_0=1\) 回收控制与一个 \(A_0=5\) 的新局部控制、因子式和恢复后的
Type II 分母；它不扫描素数、根层、分母或历史 selector，也不把局部控制当作 actual
receipt。
