---
kind: claim
claim_id: type-I-q-one-full-carrier-d-one-c-eight-marker-local-character-nonexclusion
title: q=1 容量八唯一 marker 的四次--模 47 局部非排除定理
statement: >-
  在 q_star=103 的 c=8 double-low 零 carry marker
  (D,c,c_Sigma,epsilon,g_b)=(1,1,4,0,47) 中，必有两行之一：
  (q mod 47, lambda mod 752)=(1,111) 或 (38,751)。令
  P(X)=121X^4-396X^3+346X^2+4X-79，
  G(X)=X^4-4X^3-27334X^2+2471436X-59657719。二者有相同的
  S_4 分裂域 L，且 L 与 Q(zeta_47) 线性无交。因而对每个
  r in (Z/47Z)^* 和每个 ell mod 752，都有无穷多个素数 q 和正整数 lambda
  满足 q= r (mod 47)、lambda=ell (mod 752)、q does not divide lambda，且
  q divides G(lambda)；甚至可取 P 与 G 在 F_q 上完全分裂。特别地，上述两条
  marker 同余行与 q divides G(lambda) 本身绝不矛盾。故任何只使用四次整除条件
  及 q/lambda 的固定模 47、16 同余类的排除策略不能关闭 marker；必须额外使用
  p lambda=32q+79 的精确整数提升、source 因子分配、roughness、terminal 或 typed
  admission。该结论不构造 actual marker endpoint，不否定全局 exit，也不替代这些额外门。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-q-one-full-carrier-d-one-c-eight-double-low-split-overlap-bridge
  - type-I-q-one-full-carrier-d-one-c-eight-low-gate-complement-pfree-split-interface
  - type-I-q-one-full-carrier-d-one-c-eight-low-gate-quartic-carry-parameterization
  - type-I-q-one-full-carrier-d-one-c-eight-universal-source-non-p-separation
topics:
  - type-I
  - q-one
  - full-carrier
  - c-eight
  - q-star-103
  - marker
  - quartic
  - galois
  - chebotarev
  - proof-boundary
sources:
  - claim: type-I-q-one-full-carrier-d-one-c-eight-double-low-split-overlap-bridge
    role: unique-zero-carry-marker
  - claim: type-I-q-one-full-carrier-d-one-c-eight-low-gate-complement-pfree-split-interface
    role: exact-g-b-congruence-formula
  - claim: type-I-q-one-full-carrier-d-one-c-eight-low-gate-quartic-carry-parameterization
    role: P-and-G-low-gate-transport
  - claim: type-I-q-one-full-carrier-d-one-c-eight-universal-source-non-p-separation
    role: c-eight-source-factorization
  - reproduction: reproductions/type_i_q_one_full_carrier_d_one_c_eight_marker_local_character_nonexclusion.py
    role: exact-discriminant-cycle-and-marker-residue-certificates
visibility: public
last_checked: '2026-08-17'
---

# q=1 容量八唯一 marker 的四次--模 47 局部非排除定理

## 1. marker 实际留下的局部同余

保留 (q_\star=103) 的 (c=8) high-(R) source：

\[
p=48s+1,
\qquad
M=9s(176s+5)(3168s^2+24s-1).
\tag{1}
\]

double-low bridge 已把唯一零 carry 残余压成

\[
(D,c,C,\epsilon,g_b)=(1,1,4,0,47).
\tag{2}
\]

这里已有的互补支撑公式为

\[
g_b=(M,p^2+p-1-q).
\tag{3}
\]

因此 (2) 给出 (47\mid M) 和

\[
q\equiv p^2+p-1\pmod {47}.
\tag{4}
\]

记 (L_s=176s+5)、(E_s=3168s^2+24s-1)。模 (47) 有

\[
E_s\equiv19s^2+24s-1,
\qquad
\operatorname{disc}(E_s)\equiv41\pmod {47}.
\tag{5}
\]

(41) 不是模 (47) 的平方，且 (L_s\equiv0) 仅在
(s\equiv20\pmod {47})。故

\[
47\mid M
\quad\Longleftrightarrow\quad
s\equiv0\ \text{或}\ 20\pmod {47}.
\tag{6}
\]

(c=1,D=1) 的 low-gate 整数式和奇 carry 同余分别是

\[
p\lambda=32q+79,
\qquad
\lambda\equiv-1\pmod {16}.
\tag{7}
\]

将 (4)、(6)、(7) 合并，得到所有 marker 必须落在下表之一：

\[
\begin{array}{c|c|c|c|c}
s\pmod {47}&p\pmod {47}&q\pmod {47}&\lambda\pmod {47}&\lambda\pmod {752}\\
\hline
0&1&1&17&111\\
20&21&38&46&751
\end{array}
\tag{8}
\]

这是必要条件，尚未断言这两行能被 actual source 实现。

## 2. 四次域的显式 (S_4) 证书

令

\[
\begin{aligned}
P(X)&=121X^4-396X^3+346X^2+4X-79,\\
G(X)&=X^4-4X^3-27334X^2+2471436X-59657719.
\end{aligned}
\tag{9}
\]

前者是 (4V) 的 source 多项式，后者是 (c=1) carry 多项式。二者满足精确的
齐次化恒等式

\[
\boxed{\lambda^4P(79/\lambda)=-79G(\lambda).}
\tag{10}
\]

所以它们的根通过 (x\leftrightarrow79/x) 一一对应，因而具有同一个分裂域 (L)。

(P) 的判别式为

\[
\operatorname{disc}(P)
=-2^{12}5^3 11^3\cdot23\cdot163.
\tag{11}
\]

模 (19) 以首项归一化后，

\[
121^{-1}P(X)\equiv X^4-5X^3+6X^2+6X+5\pmod {19}
\tag{12}
\]

不可约；因此 (\operatorname{Gal}(L/\mathbb Q)) 含有一个四循环。模 (3) 又有

\[
P(X)\equiv(X+1)(X^3-X^2-X-1)\pmod3,
\tag{13}
\]

其中三次因子在 \(\mathbb F_3\) 无根，故不可约，给出一个三循环。式 (12) 也证明
(P) 在 \(\mathbb Q\) 不可约。传递的四元置换群同时含四循环和三循环只能是

\[
\boxed{\operatorname{Gal}(L/\mathbb Q)\cong S_4.}
\tag{14}
\]

## 3. 与模 47 cyclotomic 层的无交

(S_4) 的阿贝尔化为 (C_2)，故 (L) 唯一可能的非平凡阿贝尔子扩张是其二次
判别式域：

\[
L^{A_4}=\mathbb Q(\sqrt{-206195}).
\tag{15}
\]

而 \(\mathbb Q(\zeta_{47})\) 的唯一二次子域为

\[
\mathbb Q(\sqrt{-47}).
\tag{16}
\]

两者不同。由于交域既包含于阿贝尔 cyclotomic 域，又是 (L) 的阿贝尔子扩张，
遂有

\[
\boxed{L\cap\mathbb Q(\zeta_{47})=\mathbb Q.}
\tag{17}
\]

所以复合域的 Galois 群是

\[
\operatorname{Gal}(L\mathbb Q(\zeta_{47})/\mathbb Q)
\cong S_4\times(\mathbb Z/47\mathbb Z)^*.
\tag{18}
\]

## 4. Chebotarev 非排除结论

取任意 (r\in(\mathbb Z/47\mathbb Z)^*\)。在 (18) 中选择元素

\[
(1,r).
\tag{19}
\]

标准 Chebotarev 密度定理给出无穷多个不在有限坏素数集中的素数 (q)，其 Frobenius
就是 (19)。这些 (q) 同时满足

\[
q\equiv r\pmod {47},
\qquad
P\text{ 与 }G\text{ 在 }\mathbb F_q\text{ 上完全分裂}.
\tag{20}
\]

对任意 (\ell\pmod {752})，从 (G) 选择一个非零根 (\lambda_q\pmod q)。因为
((q,752)=1)，中国剩余定理产生正整数 (\lambda) 使

\[
\lambda\equiv\lambda_q\pmod q,
\qquad
\lambda\equiv\ell\pmod {752}.
\tag{21}
\]

于是 (q\nmid\lambda) 且 (q\mid G(\lambda))。因此已经证明更强的命题：

\[
\boxed{
\begin{gathered}
\forall r\in(\mathbb Z/47\mathbb Z)^*,\ \forall\ell\pmod {752},\\
\exists\ \text{无穷多 }(q,\lambda):\quad
q\equiv r\pmod {47},\quad
\lambda\equiv\ell\pmod {752},\quad
q\nmid\lambda,\quad q\mid G(\lambda).
\end{gathered}}
\tag{22}
\]

特别地，(8) 的两条局部 marker 行都无法和 (q\mid G(\lambda)) 矛盾。

## 5. 结论的精确边界与路线转向

式 (22) 只否定一个具体证明设想：不能仅由

\[
q\mid G(\lambda),\qquad
q\pmod {47},\qquad
\lambda\pmod {16\cdot47}
\tag{23}
\]

导出 marker 不可能。它并不产生实际 source，因而不涉及以下仍然必要的信息：

\[
p\lambda=32q+79\quad\text{作为整数等式},
\quad q>2(p-1),
\quad p=48s+1\text{ 为素数},
\tag{24}
\]

以及 (q_\star=103) roughness、(D=1) 的全部 residue 排除、(g_b=47) 的精确
因子分配、terminal-first 与 typed admission。

因此本结果要求停止继续尝试“模 (47) 角色 + 单个四次整除”矛盾。下一条有效路线必须
把 (24) 的精确提升同 source 因子分配或可提升递降结构联立；否则它无法触及实际 marker。

聚焦复核：

~~~bash
python3 reproductions/type_i_q_one_full_carrier_d_one_c_eight_marker_local_character_nonexclusion.py --verify
~~~

复现器只验证判别式、两组有限域 cycle 证书、四次变换和 marker 的两行 CRT；无穷素数
结论使用文中明确声明的标准 Chebotarev 定理，不由程序声称证明。
