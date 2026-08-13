---
kind: claim
claim_id: type-I-overflow-full-product-d-one-a-one-regeneration-return-digit-normal-form
title: a=1 regeneration 终类首位判别与根容量饱和边界
statement: >-
  对 a=1 的 ordinary d=1 regeneration 链，令 F_i=(p-1)b_i-1，
  rho=nu_p(F_0-1)，omega=(F_0-1)/p^rho (mod p)。每次 regeneration 都保留这个
  首个非零 p-adic digit，故末次 multiplier 满足 F_rho=1+omega (mod p)：
  omega=-1 恰为 p-free failure，omega=-2 恰为 raw-source failure，其余类给严格
  capacity。rho=1 且末态 p-free 时，末前参数唯一写成 b_0=2p^2m-p-2；末态进入既有
  a=1 root interface，根 h=p+1 的对侧容量精确为
  D=3gcd(2r+1,(p^2+p+1)/3)。该 D 可以等于 p^2+p+1，因此 O(p^2) 上界不能强化为
  immediate D 的真因子下降或统一小量界。endpoint s=1 的静态 receipt 方程也允许
  饱和，但现有控制只有 formal raw parent，尚未通过 target-independent root policy；
  真实 admitted lineage
  是否排除饱和仍是开放的 provenance 问题。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-full-product-d-one-p-adic-regeneration-countdown
  - type-I-overflow-full-product-d-one-p-free-peeled-small-anchor
  - type-I-overflow-full-product-d-one-a-one-single-endpoint-stutter-guarded-relay
  - type-I-raw-universal-p-parent-root-policy-boundary
  - denominator-escape-state-contract
topics:
  - type-I
  - overflow
  - full-product
  - d-one
  - a-one
  - p-adic-regeneration
  - terminal-digit
  - p-free-failure
  - capacity-boundary
  - provenance
  - proof-boundary
sources:
  - claim: type-I-overflow-full-product-d-one-p-adic-regeneration-countdown
    role: exact-regeneration-recurrence-and-countdown
  - claim: type-I-overflow-full-product-d-one-p-free-peeled-small-anchor
    role: a-one-root-interface
  - claim: type-I-overflow-full-product-d-one-a-one-single-endpoint-stutter-guarded-relay
    role: endpoint-relay-normal-form-and-provenance-contract
  - claim: type-I-raw-universal-p-parent-root-policy-boundary
    role: formal-parent-versus-admitted-root-policy-boundary
  - reproduction: reproductions/type_i_regeneration_return_digit_normal_form.py
    role: digit-classification-saturated-root-and-static-endpoint-controls
visibility: public
last_checked: '2026-08-13'
---

# \(a=1\) regeneration 终类首位判别与根容量饱和边界

## 1. 首个非零 \(p\)-进数字决定终类

在 \(a=1\) 的 ordinary \(d=1\) 行中，令

\[
F_i=(p-1)b_i-1.
\tag{1}
\]

若 \(F_i\equiv1\pmod p\)，写

\[
q_i=\frac{F_i-1}{p}.
\tag{2}
\]

既有 regeneration 递推为

\[
b_{i+1}=b_iF_i-q_i,
\tag{3}
\]

\[
\boxed{F_{i+1}-1=q_iU_i,\qquad
U_i=p+(p-1)(pb_i-1)\equiv1\pmod p.}
\tag{4}
\]

设

\[
\rho=\nu_p(F_0-1),
\qquad
\omega=\frac{F_0-1}{p^\rho}\pmod p.
\tag{5}
\]

由 (2)--(4) 归纳得到

\[
\boxed{
\frac{F_i-1}{p^{\rho-i}}\equiv\omega\pmod p,
\qquad 0\le i\le\rho.}
\tag{6}
\]

因此末次非 regeneration multiplier 满足

\[
\boxed{F_\rho\equiv1+\omega\pmod p.}
\tag{7}
\]

同时
\[
b_\rho\equiv-F_\rho-1\pmod p,
\]
所以终类精确为

\[
\begin{array}{c|c}
\omega\pmod p & \text{末次类别}\\ \hline
-1 & F_\rho\equiv0,\ b_\rho\equiv-1:\ p\text{-free failure};\\
-2 & F_\rho\equiv-1,\ b_\rho\equiv0:\ raw-source failure;\\
\text{其它} & c=\langle-(1+\omega)^{-1}\rangle_p\le p-2:\ strict.
\end{array}
\tag{8}
\]

这把原先需要逐步追踪的末态分类压缩成 \(F_0-1\) 的首个非零 \(p\)-进数字。它是
全称整数算术；组合进 endpoint macro 时仍须重放每个 checkpoint 的 typed/priority
回执与最终 E5。

## 2. \(\rho=1\) 的 p-free return 正规形

现在设 \(\rho=1\) 且 \(\omega=-1\)。末前行必须满足

\[
b_0\equiv-p-2\pmod {p^2}.
\tag{9}
\]

由于 \(b_0\) 为正奇数，唯一写成

\[
\boxed{b_0=2p^2m-p-2,\qquad m\ge1.}
\tag{10}
\]

此时

\[
F_0=2p^3m-2p^2m-p^2-p+1,
\tag{11}
\]

\[
q=\frac{F_0-1}{p}=2p^2m-2pm-p-1\equiv-1\pmod p.
\tag{12}
\]

做一次 regeneration 后，

\[
b_*=b_0F_0-q=2pr-1,
\tag{13}
\]

其中

\[
r=\frac{
4m^2p^4-4m^2p^3-4mp^3-4mp^2+4mp+2m+p^2+3p+2}{2}.
\tag{14}
\]

末态 multiplier 为

\[
F_*=(p-1)b_*-1=pu,
\tag{15}
\]

且

\[
u\equiv-2m-3\pmod p.
\tag{16}
\]

所以当 \(2m+3\not\equiv0\pmod p\) 时，末态恰含一层 \(p\)；否则仍使用完整的
\(p^e\) peeling 公式。这一末态就是上一卡的 \(a=1\) root interface。

## 3. 根容量的精确公式

令

\[
N=p^2+p+1.
\tag{17}
\]

从末态 anchor 剥尽 \(p^e\)，再沿主侧容量剥离到 \(h=p+1\)。其对侧容量为

\[
D=(R-p-1,K)=(N,K).
\tag{18}
\]

使用

\[
K=CT,\qquad
C=\frac{p^2-1}{2},\qquad
T=p^2r-\frac{p+1}{2},
\tag{19}
\]

以及

\[
(N,C)=3,\qquad
\left(\frac N3,\frac C3\right)=1,
\tag{20}
\]

可得

\[
D=3\left(T,\frac N3\right).
\tag{21}
\]

模 \(N/3\) 有

\[
2T\equiv-(p+1)(2r+1).
\tag{22}
\]

而 \(2\) 与 \(p+1\) 都在模 \(N/3\) 下可逆，故

\[
\boxed{
D=3\gcd\left(2r+1,\frac{p^2+p+1}{3}\right).}
\tag{23}
\]

## 4. \(D\) 可以饱和整个根盒

取

\[
m=\frac{p-1}{3},
\tag{24}
\]

这对每个核心素数都是整数。把 \(p=3m+1\) 代入 (14)，直接因式分解得

\[
\boxed{
2r+1=\frac N3\left(108m^4-36m^2-8m+7\right).}
\tag{25}
\]

因此 (23) 给出

\[
\boxed{D=N=p^2+p+1.}
\tag{26}
\]

又由 (16)，\(u\equiv-7/3\not\equiv0\pmod p\)，所以末态确实只有一层 \(p\)。
固定控制 \(p=73,m=24\) 给出 \(D=N=5403\)。

这严格否定以下加强：根容量总是真因子、总是 \(O(p)\)、或 \(D/N\) 总会严格下降。
它只作用于一般 ordinary-regeneration-return 类；不能无条件反推该行来自某个真实
endpoint relay。

式 (26) 只否定 immediate 根容量的真下降，不是否定稍深的 endpoint-first 菜单。
固定 \(p=73,m=24\) 控制继续沿容量轨道会在短后缀出现严格算术出口；因此本卡没有
证明 fixed-menu no-go，也不声称饱和根会形成循环。

## 5. Endpoint \(s\equiv1\) 的 provenance 边界

如果一个 endpoint multiplier 写成

\[
E_0=1+p(1+pt),
\tag{27}
\]

源参数为 \(b=2pr_0-1\)，则 checkpoint 在一次 regeneration 后落入 p-free failure
的兼容条件为

\[
\boxed{t\equiv2r_0\pmod p.}
\tag{28}
\]

因此 endpoint congruence 本身并不排除 (26)。事实上 \(p=73\) 有一个完整的静态
endpoint receipt 控制：

\[
r_0=21\,164\,451,\qquad h=451\,141\,437\,368,
\tag{29}
\]

\[
R-h=3\cdot5\,337\,477\,005\,573,
\quad
(A,5\,337\,477\,005\,573)=1,
\quad h\cdot3\mid K.
\tag{30}
\]

这里 \(E_0=5\,337\,477\,005\,573\equiv1+73\pmod {73^2}\)，checkpoint 的
首位为 \(\omega=-1\)，最终根容量精确为 \(5403=N\)。

但 (29)--(30) 不能写成已 admitted 的 path endpoint。通用 raw-parent 构造可以给它
一个可重放 formal parent；既有合同同时明确说明，formal reverse parent 不能替代
target-independent named root policy、scope 和 persistent lineage。规范 anchor 容量轨道
也不经过这个 \(h\)。所以当前正确状态是

\[
\boxed{
\text{raw-parent replayable，root-policy/admission 未证。}}
\tag{31}
\]

这把下一缺口定位成 Reach/provenance 定理：要么证明所有 admitted endpoint lineages
排除根容量饱和，要么构造一个真正 admitted 的饱和 receipt。继续只从局部剩余类、
静态 endpoint 方程或 \(O(p^2)\) 上界推断 immediate 严格下降已经不够；若要排除任意
固定菜单，还需独立构造保持完整菜单前缀的参数族。

## 6. 聚焦回执

```bash
python3 reproductions/type_i_regeneration_return_digit_normal_form.py --verify
```

脚本只核对 (6)--(8) 的固定首位控制、\(p=73,m=24\) 的饱和 ordinary return，以及
(29)--(31) 的静态 endpoint-compatible 控制；它明确不把最后一项升级为 path-admitted
receipt，也不扫描 selector history 或历史结果。
