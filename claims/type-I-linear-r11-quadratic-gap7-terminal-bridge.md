---
kind: claim
claim_id: type-I-linear-r11-quadratic-gap7-terminal-bridge
title: R=11 线性 F 二次相位的 gap-7 Type II 终端桥
statement: 设 k>=0，M=13+154k 与 p=241+2856k 都是素数。则 p=1 mod24 有一个 R=11 的线性 Type I 图表，其中心指数盒是 F 型且具有非平凡二次 Fourier 角色；两块群像生成整个 U(11)，故没有两块群像的 source escape。该二次角色在目标 -1 与真实 raw 因子 7 上取同一负相位。独立地，7 整除 2p+1，故参数 (A,C,K,h)=(1,1,2,7) 直接给出 Type II 短证书 4/p=1/B+1/(2p)+1/(2pB)，其中 B=(2p+1)/7。该结果给出一个带 Fourier provenance 的显式候选参数列，不断言其中有无穷多个同时为素数的 k，也不把相位对齐当作整数 source-fiber lift。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-linear-two-block-source-map-completeness
  - type-I-f-g-fourier-obstruction-certificate
  - type-II-raw-ray-certificate
topics:
  - type-I
  - Type-II
  - linear-source
  - F-state
  - Fourier
  - quadratic-character
  - source-map
  - raw-terminal
  - gap-7
  - proof-program
sources:
  - claim: type-I-linear-two-block-source-map-completeness
    role: finite-two-block-source-map
  - claim: type-I-f-g-fourier-obstruction-certificate
    role: F-Fourier-certificate-context
  - claim: type-II-raw-ray-certificate
    role: raw-Type-II-terminal
visibility: public
last_checked: '2026-08-06'
---

# \(R=11\) 线性 F 二次相位的 gap-7 Type II 终端桥

## 1. 参数族与两块 source-map

令

\[
M_k=13+154k,\qquad
p_k=241+2856k,\qquad
s_k=7+84k.
\tag{1}
\]

设 \(k\ge0\) 且 \(M_k,p_k\) 都是素数。因为 \(2856\) 被 \(24\) 整除，

\[
p_k\equiv1\pmod{24}.
\tag{2}
\]

在 \(R=11\)、\(a=3\)、\(s=s_k\) 处，

\[
p_k=a+s+asR.
\tag{3}
\]

令 \(K=(p_kR+1)/4\)。直接计算给出

\[
sR+1=6M_k,\qquad aR+1=34,
\qquad
K=3\cdot17\cdot M_k.
\tag{4}
\]

由于 \(s,a\) 均为奇数，两个奇部实际线性块为

\[
U^\circ=3M_k,\qquad V^\circ=17.
\tag{5}
\]

模 \(11\) 下，

\[
U^\circ\equiv V^\circ\equiv6\pmod{11},
\qquad
\operatorname{ord}_{U(11)}(6)=10.
\tag{6}
\]

故

\[
L_{\rm blk}=\langle U^\circ,V^\circ\rangle=U(11)=H.
\tag{7}
\]

因此两块群像对任何目标纤维差分都闭合：没有
\(\mathrm{LINEAR\_BLOCK\_SOURCE\_ESCAPE}\)。这只说明
\(L_{\rm blk}=H\)，并不证明带标记 menu saturation、角色标签提升或实际整数
source-fiber lift。

## 2. 固定图表确为 F 型

以 \(2\) 为 \(U(11)\) 的原根。有

\[
3=2^8,\qquad17=2^9,\qquad M_k\equiv2=2^1\pmod{11}.
\tag{8}
\]

因为 \(K\) 平方自由，中心指数盒的对数像为

\[
\{8x+9y+z:x,y,z\in\{-1,0,1\}\}
=\{-4,-3,\ldots,4\}\pmod{10}.
\tag{9}
\]

它恰缺 \(5\)，而

\[
-1=2^5\pmod{11}.
\tag{10}
\]

所以 \(-1\in H\)，但中心指数盒没有目标表示；这个固定 \(R=11\) 图表是 F 型。

## 3. 二次相位和实际奇因子

令

\[
\chi_2(u)=\left(\frac{u}{11}\right).
\tag{11}
\]

这是 \(U(11)\) 唯一非平凡二次角色。由 (8)，

\[
\chi_2(3)=1,\qquad
\chi_2(17)=\chi_2(M_k)=-1.
\tag{12}
\]

因此三坐标盒在该角色上的 Fourier 系数绝对值为

\[
\left|(1+1+1)(-1+1-1)(-1+1-1)\right|=3.
\tag{13}
\]

尤其这给出一个实际的 \(q=2\) Fourier 相位，而不是从角色阶推测整数
\(2\)-进高度。由 (5)、(10) 与二次剩余表，

\[
\chi_2(U^\circ)=\chi_2(V^\circ)
=\chi_2(-1)=\chi_2(7)=-1.
\tag{14}
\]

同时

\[
p_k\equiv3\pmod7,
\qquad
7\mid p_k+4,
\qquad
7\mid 2p_k+1.
\tag{15}
\]

式 (14) 仅记录 \(7\) 与目标的二次相位对齐；它不构成整数 source-fiber lift，
也不把 Fourier 的 \(q=2\) 阶改写成 \(2\)-进载体。独立地，
\(7\mid2p_k+1\) 才是下节 raw 射线的整除条件；\(7\mid p_k+4\) 只解释
这里的 gap-7 命名，并不参与该射线。

## 4. 直接 Type II 终端

取 raw Type II 射线参数

\[
(A,C,K_0,h)=(1,1,2,7),
\qquad
B=\frac{2p_k+1}{7}=69+816k.
\tag{16}
\]

由 (15)，\(B\) 是正整数，且

\[
h=4ACK_0-1=7,\qquad h\mid K_0p_k+A.
\tag{17}
\]

又 \(B\ge69>1=A\)，所以 raw-ray 定理给出 Type II 短证书。直接化简也有

\[
\boxed{
\frac4{p_k}
=\frac1B+\frac1{2p_k}+\frac1{2p_kB}.
}
\tag{18}
\]

因此这种 F 图表不需要等待容量或递降：terminal-first 选择器应在其二次相位被继续
收费前，以 'direct_type_ii' 返回 (18)。

## 5. 两个定点实例

当 \(k=0\) 时，

\[
(M,p,K,B)=(13,241,663,69),
\]

\[
\frac4{241}
=\frac1{69}+\frac1{482}+\frac1{33258}.
\tag{19}
\]

当 \(k=6\) 时，

\[
(M,p,K,B)=(937,17377,47787,4965).
\tag{20}
\]

这两个实例只核验公式与素性，不支持关于 (1) 中同时素数参数有无穷多个的断言。

## 6. 边界

本卡证明的是一个明确的线性 F 子类被外部 raw gap-7 射线抢占。它不说明任意二次
Fourier 相位都有奇因子 \(7\)，不构造一般 source-map 的相位 lift，也不解决其它
F/G 状态的容量或 E1--E5 递降。
