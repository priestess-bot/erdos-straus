---
kind: claim
claim_id: type-I-root-capacity-strict-carry-eisenstein-small-norm-distance-gate
title: 严格 root carry 的 Eisenstein 小范数互补距离门
statement: >-
  对核心素数 p≡1 mod24 的 actual strict proper-root carry，沿用 canonical even
  complement n、距离 delta=p-n、符号 tau，以及 Eisenstein quotient norm t。令
  L(h,t)=floor(sqrt(4ht/3))。则总有 |s|<=L(h,t) 和
  |D+tau delta|<=L(h,t)。因而 c 为奇数时 delta<=L(h,t)-1；c 为偶数时
  delta<=floor((p L(h,t)-1)/(h-1))。所以只要相应上界不超过 (p-1)/2，canonical
  complement 自动落在 n>p/2 的 retained-standard-tail 域。特别地 t=1 的单位纤维
  有完全显式的距离盒。p=313,r=271 的 actual hard strict receipt 取
  (h,t,L,delta)=(543,1,26,15)，并精确达到偶 cofactor 分支的距离上界；但它的
  high-half tail selector 仍为空。因此小范数门是真实的 receipt-to-tail capacity map，
  不是短证书或全局出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-strict-carry-eisenstein-precofactor-quotient
  - type-I-root-capacity-strict-carry-complement-even-source-gate
topics:
  - type-I
  - root-capacity
  - strict-carry
  - eisenstein-integers
  - norm
  - small-norm
  - complement-distance
  - high-half-tail
  - capacity-map
  - proof-boundary
sources:
  - claim: type-I-root-capacity-strict-carry-eisenstein-precofactor-quotient
    role: exact-precofactor-eisenstein-norm
  - claim: type-I-root-capacity-strict-carry-complement-even-source-gate
    role: canonical-complement-and-high-half-tail-domain
  - reproduction: reproductions/type_i_root_capacity_strict_carry_eisenstein_small_norm_distance_gate.py
    role: fixed-strict-receipt-small-norm-distance-controls
visibility: public
last_checked: '2026-08-14'
---

# 严格 root carry 的 Eisenstein 小范数互补距离门

## 1. 设置

固定核心素数

\[
p\equiv1\pmod {24}
\]

的 actual strict proper-root carry。沿用其 maximal receipt 的 \(D,h\)，canonical
even complement \(n\)，以及

\[
\delta=p-n,
\qquad
\tau=
\begin{cases}
 1,&c\text{ 为奇数},\\
-1,&c\text{ 为偶数},
\end{cases}
\qquad
s=\frac{D-\tau\delta(h-1)}p.
\tag{1}
\]

于是 \(h=3u\ge3\)，且已建立的 pre-cofactor quotient 给出

\[
\alpha=D+\tau\delta-s\omega,
\qquad
N(\alpha)=ht,
\tag{2}
\]

其中 \(t\ge1\) 是实际 Eisenstein 商的范数。定义完全由 receipt 决定的整数半径

\[
\boxed{L(h,t):=\left\lfloor\sqrt{\frac{4ht}{3}}\right\rfloor.}
\tag{3}
\]

这里 \(3\mid h\)，所以根号内是整数有理数；定义 (3) 不需要分解 \(t\) 或搜索一个
tail divisor。

## 2. 范数给出的双坐标盒

令

\[
A=D+\tau\delta.
\tag{4}
\]

由 \(N(a+b\omega)=a^2-ab+b^2\) 与 (2)，有

\[
ht=N(A-s\omega)=A^2+As+s^2
=\left(A+\frac{s}{2}\right)^2+\frac{3s^2}{4}
=\left(s+\frac{A}{2}\right)^2+\frac{3A^2}{4}.
\tag{5}
\]

所以两个整数坐标都落在同一个显式盒内：

\[
\boxed{|s|\le L(h,t),\qquad |D+\tau\delta|\le L(h,t).}
\tag{6}
\]

这是来自 exact Eisenstein quotient 的结论。若只知道 (5) 的二次恒等式而不知道
\(t=N(\beta)\)，仍可写出相同不等式；(2) 的作用是保证 \(t\) 是 actual receipt 的
整范数坐标，而不是任意引入的二次型值。

## 3. 两个 cofactor parity 分支

### 奇 cofactor

若 \(c\) 为奇数，则 \(\tau=1\) 且 \(A=D+\delta>0\)。由 (6) 立刻得到

\[
\boxed{\delta\le L(h,t)-1.}
\tag{7}
\]

这里减去 1 使用 \(D\ge1\)。因此 odd-cofactor strict carry 的 canonical complement
\(n=p-\delta\) 在小 norm fiber 中必靠近 \(p\)。

### 偶 cofactor

若 \(c\) 为偶数，则 \(\tau=-1\)。式 (1) 改写为

\[
ps=D+\delta(h-1)>0.
\tag{8}
\]

结合 \(s\le L(h,t)\) 与 \(D\ge1\)，得到精确整数界

\[
\boxed{
\delta\le
\left\lfloor\frac{pL(h,t)-1}{h-1}\right\rfloor.}
\tag{9}
\]

同时 (6) 保留互补的近似式

\[
\boxed{|D-\delta|\le L(h,t).}
\tag{10}
\]

所以在 even-cofactor small-norm fiber 中，\(D\) 与 \(\delta\) 不能独立地大；它们
被约束在宽度 \(2L(h,t)\) 的对角带内，而 \(\delta\) 的绝对大小还受 (9) 限制。

## 4. 通向 high-half tail 的精确充分门

无论 parity 如何，canonical even complement 都满足

\[
n=p-\delta.
\tag{11}
\]

定义

\[
B_+(h,t)=L(h,t)-1,
\qquad
B_-(p,h,t)=\left\lfloor\frac{pL(h,t)-1}{h-1}\right\rfloor.
\tag{12}
\]

分别取 \(c\) 奇和 \(c\) 偶时的上界。若相应的 \(B_\tau\) 满足

\[
B_\tau\le\frac{p-1}{2},
\tag{13}
\]

则 (7) 或 (9) 推出

\[
\boxed{n=p-\delta>\frac p2.}
\tag{14}
\]

这不是 tail selector 本身。它只把该 receipt 强制送入已知的 retained-standard-tail
域；在那里仍须找到

\[
e\mid(pn)^2,
\qquad e\le pn,
\qquad e\equiv-pn\pmod {4n-p},
\tag{15}
\]

或使用另一条已经完整支付的 source/path 递降。因而 (13) 是一个 route selector，
不是 \(e\) 存在性的证明。

## 5. 单位纤维 sharp control

在 actual hard strict receipt

\[
p=313,
\qquad r=271,
\qquad h=543,
\qquad D=8,
\qquad c=n=298
\tag{16}
\]

中，有

\[
\delta=15,
\qquad \tau=-1,
\qquad s=26,
\qquad t=1.
\tag{17}
\]

故

\[
L(543,1)=\lfloor\sqrt{724}\rfloor=26,
\]

并且偶分支上界精确为

\[
\left\lfloor\frac{313\cdot26-1}{542}\right\rfloor=15=\delta.
\tag{18}
\]

这个最难的已知 strict control 因而不是被粗糙估计排除的特殊点，而是 (9) 的 sharp
unit-fiber 边界。它确实满足 (14)，但高半区 \(n=298\) 的 selector (15) 为空。
所以小 norm 与小距离不能被误读为已经给出短证书。

作为必要性边界，\(p=193,r=3\) 有 \(t=763\)、\(h=21\)、\(\delta=135\)；此时
\(B_-(193,21,763)=1408\)，不再提供非平凡的 high-half 强制。这个对照说明本卡只
收紧 small-norm fibers，不把任意 Eisenstein quotient 错称为距离递降。

## 6. 研究后果

这张容量图为 strict root route 给出一个新的有限入口：对固定 \((p,h,t)\)，canonical
complement distance 只须落在 (7) 或 (9) 的显式整数盒内。特别是 \(t=1\) 的所有
actual receipts 都有无需分解的窄距离菜单。下一步若要关闭该分支，必须把这个菜单与
tail residue (15) 的高阶指数盒、或 strict support-rebase 的真实 persistent path
结合；不能仅凭小 \(t\) 声称证书或全局递降。

## 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_strict_carry_eisenstein_small_norm_distance_gate.py --verify
```

该回执只重放三个 fixed actual strict receipts：`p=313` 的 sharp unit fiber、`p=73`
的 odd-cofactor 分支，以及 `p=193` 的非小-norm 边界；不扫描素数、root 参数、tail
divisor 或历史状态。
