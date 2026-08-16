---
kind: claim
claim_id: type-I-q-one-full-carrier-d-one-c-eight-qstar-103-low-gate-odd-carry-rays
title: q=1 容量八 q-star=103 low gate 的奇 carry 射线参数化
statement: >-
  在实际 q_star=103 的 c=8 high-R source 中，固定 source defect
  D_s=gcd(V,M) 与 low direct capacity c in {1,...,7}。则每个 high-q low-gate
  prime 都唯一写成 q_t=2p(t+1)+eta_{s,c}，其 carry quotient 同时为
  lambda_t=64D_s(t+1)+sigma_{s,c}，其中 t>=0，sigma_{s,c} 是
  p sigma=79c+32D_s (mod 64D_s) 的唯一非零最小正剩余，
  eta_{s,c}=(p sigma_{s,c}-79c)/(32D_s) 是正奇数。反之，某个 t>=0
  给出实际 high-q low gate 当且仅当 q_t 为素数且 q_t divides G_c(lambda_t)。
  因而每个 fixed source/c pair 的 seven-gate residual 不是一般 carry 参数空间，
  而是一条从显式起点开始的奇素数--四次因子射线；q_t divides V 还给出其有限的
  source-local t interval。该结论不为 t 给出全局上界，不证明任何射线为空，也不支付
  terminal、typed admission 或 E5。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-full-carrier-qstar-103-rough-selection-criterion
  - type-I-q-one-full-carrier-d-one-c-eight-high-q-shared-defect-rigidity
  - type-I-q-one-full-carrier-d-one-c-eight-low-gate-quartic-carry-parameterization
topics:
  - type-I
  - q-one
  - full-carrier
  - c-eight
  - q-star-103
  - low-gate
  - carry-ray
  - quartic
  - proof-boundary
sources:
  - claim: type-II-q-one-full-carrier-qstar-103-rough-selection-criterion
    role: actual-q-star-implies-s-equals-86-mod-103
  - claim: type-I-q-one-full-carrier-d-one-c-eight-high-q-shared-defect-rigidity
    role: D_s-residue-table-and-high-q-defect-rigidity
  - claim: type-I-q-one-full-carrier-d-one-c-eight-low-gate-quartic-carry-parameterization
    role: G_c-forward-and-reverse-low-gate-equivalence
  - reproduction: reproductions/type_i_q_one_full_carrier_d_one_c_eight_qstar_103_low_gate_odd_carry_rays.py
    role: CRT-threshold-table-and-odd-ray-control
visibility: public
last_checked: '2026-08-17'
---

# q=1 容量八 \(q_\star=103\) low gate 的奇 carry 射线参数化

## 1. \(q_\star=103\) 把 defect 与 source 尺寸绑定

保留容量八 high-\(R\) source 的记号

\[
p=48s+1,\qquad K=8M,\qquad D=D_s=(V,M),
\tag{1}
\]

并只考虑实际 \(q_\star=103\) 宏的输入。其必要条件为

\[
s\equiv86\pmod {103}.
\tag{2}
\]

共享缺陷刚性给出

\[
D=
11^{[s\equiv6\ (11)]}
41^{[s\equiv30\ (41)]}
149^{[s\equiv55\ (149)]}.
\tag{3}
\]

将 (2) 与 (3) 中出现的因子逐个作 CRT，得到下表。这里的 \(s_D\) 是满足
相应已出现 defect 条件的最小 \(s\ge86\)；未出现的 defect 条件只会进一步缩小
可行集，因而不影响下界。

\[
\begin{array}{c|r|r|r}
D&s_D&48s_D+1&32D\\
\hline
1&86&4\,129&32\\
11&292&14\,017&352\\
41&1\,219&58\,513&1\,312\\
149&13\,167&632\,017&4\,768\\
451&13\,888&666\,625&14\,432\\
1\,639&59\,208&2\,841\,985&52\,448\\
6\,109&89\,902&4\,315\,297&195\,488\\
67\,199&5\,123\,718&245\,938\,465&2\,150\,368
\end{array}
\tag{4}
\]

因此每个实际 \(q_\star=103\) source 都满足

\[
\boxed{p>32D.}
\tag{5}
\]

若 \(\ell\in\{11,41,149\}\) 整除 \(D\)，由 (3) 分别有
\(p\equiv3,6,108\pmod\ell\)。故

\[
(p,64D)=1.
\tag{6}
\]

## 2. 奇 raw prime 强制一条 \(64D\) carry 类

设 \(q>2(p-1)\) 是一个实际 \(V\)-side strict raw prime，且其 a-side direct
capacity 是

\[
1\le c\le7.
\tag{7}
\]

四次 carry 参数化中的整数满足

\[
p\lambda=32Dq+79c.
\tag{8}
\]

因为 \(q\) 是奇数，

\[
32Dq\equiv32D\pmod {64D}.
\]

由 (6) 定义唯一剩余

\[
\boxed{
\sigma_{s,c}\equiv p^{-1}(79c+32D)\pmod {64D},
\qquad 1\le\sigma_{s,c}<64D.
}
\tag{9}
\]

这里 \(\sigma_{s,c}\ne0\)：若 \(D>1\)，\(64D\mid79c+32D\) 会推出
\(D\mid79c\)，这与 \(D\) 的素因子及 \(c\le7\) 矛盾；若 \(D=1\)，直接检查
\(c=1,\ldots,7\) 即可。

另一方面，\(q\ge2p-1\) 以及 (5) 给出

\[
\lambda
\ge64D+\frac{79c-32D}{p}
>64D-1.
\tag{10}
\]

所以整数 \(\lambda\) 至少为 \(64D\)。结合 (9)，存在唯一 \(t\ge0\) 使

\[
\boxed{
\lambda=\lambda_t:=64D(t+1)+\sigma_{s,c}.
}
\tag{11}
\]

特别地，(9) 模 \(16\) 正好恢复
\(\lambda_t\equiv-c\pmod {16}\)，但 (11) 比该旧同余强得多。

令

\[
\boxed{
\eta_{s,c}:=\frac{p\sigma_{s,c}-79c}{32D}.
}
\tag{12}
\]

由 (9)，该数是整数且为奇数；又 \(p\ge4129>79c\) 与
\(\sigma_{s,c}\ge1\) 给出 \(\eta_{s,c}>0\)。代入 (8)、(11)，实际 prime 必为

\[
\boxed{
q=q_t:=2p(t+1)+\eta_{s,c}.
}
\tag{13}
\]

所以 \(q_t\) 从一开始就为奇数且 \(q_t>2p>2(p-1)\)。

## 3. 与四次因子条件的精确等价

设

\[
G_c(X)=
X^4-4cX^3-27334c^2X^2
+2471436c^3X-59657719c^4.
\tag{14}
\]

前一张四次参数化卡已经证明：在固定 source 上，满足 (8) 的 high prime 是实际
low gate 当且仅当它整除 \(G_c(\lambda)\)。由 (11)--(13)，这在本范围内变成

\[
\boxed{
\begin{aligned}
&\text{存在 capacity 为 }c\text{ 的 actual high-}q\text{ low gate}\\
\Longleftrightarrow\quad&
\exists\,t\ge0:
\quad q_t\text{ 是素数，且 }q_t\mid G_c(\lambda_t).
\end{aligned}}
\tag{15}
\]

反向方向并未遗漏 strictness：若右侧成立，(8) 恢复；四次恒等式给出
\(q_t\mid4V\)，而 \(q_t\) 为奇数，故 \(q_t\mid V\)。又 \(q_t>2(p-1)\) 与
\(D=(V,M)\mid11\cdot41\cdot149\) 排除 \(q_t\mid M\)，所以
\(v_{q_t}(V)>v_{q_t}(K)\)，它正是所需的 strict raw 标签。

每个 fixed source/c pair 还得到一个有限但随 source 增长的候选区间。因为 (15) 的
\(q_t\) 整除 \(V\)，必有

\[
0\le t\le
\left\lfloor\frac{V-\eta_{s,c}}{2p}\right\rfloor-1.
\tag{16}
\]

这把 low gate 的后续研究压缩为七条明确的“线性 prime ray 命中四次因子”问题，
而不是继续把 \(q\bmod p\) 当作独立的七项菜单。

## 4. 非 low 控制

已有 actual high-\(q\) raw control

\[
s=116,\quad p=5569,\quad D=11,\quad
q=578581,\quad c=4202,\quad\lambda=36630
\tag{17}
\]

不在本卡的 \(c\le7\)、\(q_\star=103\) 范围内，但仍检验奇 carry 的代数重建：

\[
\sigma=22,\qquad \eta=-595,\qquad t=51,
\tag{18}
\]

\[
36630=64\cdot11\cdot(51+1)+22,
\qquad
578581=2\cdot5569\cdot(51+1)-595.
\tag{19}
\]

并且 \(q\mid G_{4202}(36630)\)。该控制只验证 (8) 的 parity-refined affine
重建；因 \(\eta<0\)，它不能替代 low-gate 范围内 \(\eta_{s,c}>0\) 的证明。

## 5. 边界

(15) 没有给出 \(t\) 的全局上界，(16) 的长度仍随 \(V/p\) 增长。它也没有证明
任何 \(q_t\) 必为合数，或某个 \(q_t\) 一定命中 \(G_c(\lambda_t)\)。因此该卡不关闭
seven-gate residual，不构造 terminal，不证明 split capacity 小于 \(8\)，也不提供
typed E1--E5 或 G/Type I global exit。

它的实质作用是给出下一步因子研究的精确量词：若要排空或命中一个 low gate，必须处理
(15) 的七条 odd affine rays；只检查 \(\lambda\equiv-c\pmod {16}\)、或只罗列
\(q\bmod p\) 的七个剩余，均不足以描述 actual high-\(q\) 候选。

聚焦复核：

~~~bash
PYTHONPATH=reproductions python3 \
  reproductions/type_i_q_one_full_carrier_d_one_c_eight_qstar_103_low_gate_odd_carry_rays.py --verify
~~~

复现器只重放八行 CRT 下界、56 个固定 ray 起点以及一个已有 raw control；不扫描
\(s\)、素数、\(V\) 的因子或历史 certificate。
