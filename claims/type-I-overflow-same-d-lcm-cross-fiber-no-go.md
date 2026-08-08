---
kind: claim
claim_id: type-I-overflow-same-d-lcm-cross-fiber-no-go
title: overflow 同 d 纤维 lcm 的跨纤维强制与同图表禁闭
statement: 设两个不同的 overflow carrier M_1,M_2 具有同一核心素数 p 和 determinant 参数 d，令 r_d=-(4d)^(-1) (mod p)、g=gcd(M_1,M_2)、L=lcm(M_1,M_2)。则 L 仍在同一 d 纤维当且仅当 g=r_d (mod p)，一般 canonical 新参数满足 d_L=d*g*r_d^(-1) (mod p)。若该同 d 条件成立，overflow 不等式强制 L>(p+1)(p^2+1)/(4(p-d))>B_p=(p-1)^2/4。因此在正常 outer-rank 域 L<=B_p 内，任意不同同 d carrier 的 lcm 必须改变 d；跨纤维 source-map 必须重算新 d_L、E2 和 E1--E5，不能继承旧 carry。这是一个严格的 lcm transition 硬门，不是全局递降定理。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-e2-fixed-fiber-constancy
  - type-I-fg-physical-carry-arc-lift-interface
  - type-I-marked-support-accumulation-rechart-saturation
topics:
  - type-I
  - overflow
  - lcm
  - cross-fiber
  - determinant
  - carry
  - E2
  - source-map
  - outer-rank
  - proof-boundary
sources:
  - claim: type-I-overflow-e2-fixed-fiber-constancy
    role: fixed-d-fiber-residue
  - claim: type-I-fg-physical-carry-arc-lift-interface
    role: carry-recomputation-boundary
  - claim: type-I-marked-support-accumulation-rechart-saturation
    role: outer-rank-domain
visibility: public
last_checked: '2026-08-09'
---

# overflow 同 \(d\) 纤维 lcm 的跨纤维强制与同图表禁闭

## 1. 两个同纤维 carrier

固定素数 \(p\)、\(0<d<p\)，并令

\[
C=p-d,
\qquad
r=r_d=[-(4d)^{-1}]_p\in\{1,\ldots,p-1\}.
\tag{1}
\]

设 \(M_1\ne M_2\) 都是 verified overflow carrier，即

\[
pn_i=4dM_i+1,
\qquad
4M_i-n_i>p
\quad(i=1,2).
\tag{2}
\]

由 (2) 模 \(p\)，两者都满足

\[
M_i\equiv r\pmod p.
\tag{3}
\]

令

\[
g=(M_1,M_2),
\qquad
L=[M_1,M_2]=\frac{M_1M_2}{g}.
\tag{4}
\]

因为 \(p\nmid M_1M_2\)，所以 \(g\) 和 \(L\) 都是模 \(p\) 的单位。由 (3)--(4) 有

\[
L\equiv r^2g^{-1}\pmod p.
\tag{5}
\]

## 2. lcm 的 determinant 参数公式

由 (1) 和 (5)，\(L\) 满足同一个 \(d\)-纤维的模 \(p\) 方程
\(4dL\equiv-1\pmod p\) 当且仅当

\[
\boxed{g\equiv r\pmod p.}
\tag{6}
\]

更一般地，\(L\) 的唯一 canonical determinant 参数 \(d_L\in\{1,\ldots,p-1\}\) 定义为

\[
4d_LL\equiv-1\pmod p.
\tag{7}
\]

由 \(L^{-1}\equiv gr^{-2}\pmod p\) 和
\(d\equiv-4^{-1}r^{-1}\pmod p\)，得到

\[
\boxed{
d_L\equiv d\,g\,r^{-1}\pmod p.
}
\tag{8}
\]

所以 \(g\not\equiv r\) 时，lcm transition 必然改变 determinant 参数；不能沿用原
\((p,d)\) 纤维的 E2 或相位表。

### 证明

式 (5) 直接由 \(M_1M_2/g\) 取模 \(p\) 得到。将 (5) 代入
\(4dL\equiv-1\) 并使用 \(4dr\equiv-1\)，得到
\(-rg^{-1}\equiv-1\)，即 (6)。式 (8) 则是
\(-\,(4L)^{-1}\) 的直接化简。证毕。

## 3. 同 \(d\) lcm 的严格 outer-rank 禁闭

现在假设 (6) 成立。写

\[
M_i=g u_i.
\tag{9}
\]

由 \(M_i\equiv r\pmod p\) 和 \(g\equiv r\pmod p\)，有

\[
u_i\equiv1\pmod p.
\tag{10}
\]

因 \(M_1\ne M_2\)，\(u_1\ne u_2\)，从而

\[
\max(u_1,u_2)\ge p+1.
\tag{11}
\]

令 \(M_{\min}=g\min(u_1,u_2)\)。由 overflow 条件 (2)：

\[
4M_i-\frac{4dM_i+1}{p}>p
\quad\Longrightarrow\quad
\boxed{
M_i>\frac{p^2+1}{4(p-d)}.
}
\tag{12}
\]

而

\[
L=g u_1u_2=M_{\min}\max(u_1,u_2),
\]

所以由 (11)--(12)

\[
L>
\frac{(p+1)(p^2+1)}{4(p-d)}
\ge
\frac{(p+1)(p^2+1)}{4(p-1)}.
\tag{13}
\]

最后，

\[
(p+1)(p^2+1)-(p-1)^3
=4p^2-2p+2>0,
\]

故

\[
\boxed{
L>\frac{(p-1)^2}{4}=B_p.
}
\tag{14}
\]

这证明了：

\[
\boxed{
M_1\ne M_2,\ \text{同一 }(p,d)\text{ overflow},\
L\le B_p
\Longrightarrow d_L\ne d.
}
\tag{15}
\]

同 \(d\) 的 lcm 只能落在高载体外部域，不能成为正常 outer-rank 内的同图表支撑
升级。这个禁闭与“单个 carrier 把 support \(A\) 提升到 \(M\)”不同：后者没有
把两个不同 carrier 做 lcm，仍可使用已有同图表 support-promotion 合同。

## 4. 统一选择器的跨纤维硬门

对两个同 \(d\) 状态尝试合并支持时，选择器必须先计算 \((g,r,L,d_L)\)：

1. 若 \(L>B_p\)，输出 LCM_HIGH_CARRIER_BOUNDARY，进入 high-carrier、固定-\(n/s\)
   或其它 overflow 分支；不能登记 normal same-chart edge。
2. 若 \(L\le B_p\)，由 (15) 自动得到 \(d_L\ne d\)，输出
   CROSS_FIBER_DETERMINANT_RESET，并重新计算 \(R_L,K_L,C_L\)、E2 短弧、source
   标签、SNF/CRT 和 E1--E5；旧纤维的 carry 只作为 provenance，不能作为新门的证明。
3. 只有新参数的完整物理 transition、E2 和 E1--E5 全部通过，才能把该 lcm 变成
   verified_edge；有限群上 \(d_L\) 的公式本身不等于整数递降。

这把现有 cross-fiber source-map 缺口缩成一个明确的输入：必须记录 lcm 的完整 gcd
因子谱（至少足以得到 \(g\bmod p\)），而仅保存各行的 \(\Theta_a(M)\) 不够。

## 5. 精确控制

取

\[
p=73,\qquad d=1,\qquad r=18,\qquad B_p=1296.
\]

有三条 verified overflow carrier：

\[
\begin{array}{c|c|c}
M&n=(4M+1)/73&4M-n\\ \hline
1332&73&5255\\
2646&145&10439\\
675&37&2663
\end{array}
\]

第一对 \(M_1=1332,M_2=2646\) 满足

\[
g=18\equiv r\pmod{73},
\qquad
L=195804>B_p,
\qquad
d_L=1.
\]

它正好落在定理的“同 \(d\) 只能高载体”分支。第二对
\(M_1=675,M_2=2646\) 满足

\[
g=27\not\equiv18\pmod{73},
\qquad
L=66150>B_p,
\qquad
d_L=38\ne1.
\]

后一行展示公式 (8) 的真实 determinant reset，即使 lcm 仍在同一个核心素数上，
也不能把旧 \(d=1\) carry 复用到新 chart。

这些数据只验证跨纤维硬门，不构成猜想反例；其它固定-\(n\)、固定-\(s\)、Type I/II
或 support promotion 出口仍可独立存在。

