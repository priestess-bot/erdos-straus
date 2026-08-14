---
kind: claim
claim_id: type-II-q-one-full-carrier-d-one-regeneration-completion
title: q=1 full-carrier 的 d=1 再生刚性与两步 complete-excess 收口
statement: >-
  设 ordinary q=1 G full-carrier root 的第二-anchor fixed-n 宏已产生 persistent
  d=1 receiver A=(pn-1)/4、R=(p-1)n-1、K=A(p-1)，且其 immediate
  complete-excess multiplier E 满足 E=1 (mod p)。则奇 t 分支不可能发生再生；
  偶 t=2s 分支必有 q_*=23、g=gcd((p+1)/2,(n+1)/2)=1、j=20、n=5p-4，且
  E=(5p^2-9p+2)/2、v_p(E-1)=1。唯一再生后的 d=1 行满足 b'=3/4 (mod p)、
  E'=-5/4 (mod p)，所以 raw p-source 门和 p-free bundle 门都通过，且
  E' 不等于 1 (mod p)；其下一 complete-excess canonical target 的容量
  c=4*5^(-1) (mod p) 属于 {1,...,p-2}。因此每个该类 immediate receiver
  最多经历两条 strict complete-excess relay：直接严格降容量，或恰好一次
  p-adic 再生后严格降容量。它不处理容量下降后的一般 Type I target，也不构成
  全局 selector 或 Erdős--Straus 猜想的证明。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-full-carrier-d-one-p-free-gate-exclusion-relay
  - type-II-q-one-full-carrier-second-anchor-fixed-n-macro
  - type-I-overflow-full-product-d-one-p-adic-regeneration-countdown
  - type-I-overflow-full-product-d-one-complete-excess-capacity-map
  - denominator-escape-state-contract
topics:
  - type-II
  - q-one
  - full-carrier
  - type-I
  - d-one
  - complete-excess
  - p-adic-regeneration
  - residual-capacity
  - strict-relay
  - well-founded-descent
  - proof-boundary
sources:
  - claim: type-II-q-one-full-carrier-d-one-p-free-gate-exclusion-relay
    role: immediate-postmacro-receiver-and-first-strict-relay
  - claim: type-I-overflow-full-product-d-one-p-adic-regeneration-countdown
    role: exact-d-one-regeneration-recurrence
  - reproduction: reproductions/type_ii_q_one_full_carrier_d_one_regeneration_completion.py
    role: finite-odd-contradiction-and-two-step-even-receipt
visibility: public
last_checked: '2026-08-15'
---

# q=1 full-carrier 的 d=1 再生刚性与两步 complete-excess 收口

## 1. 问题只剩 immediate receiver 的再生支

固定已有 q=1 full-carrier 第二-anchor fixed-(n) 宏的一个 persistent
postmacro receiver。沿用前卡的记号：

\[
p\equiv1\pmod {24},\qquad n>1,\qquad n\equiv1\pmod4,
\tag{1}
\]

\[
A=\frac{pn-1}{4},\qquad R=(p-1)n-1,\qquad K=A(p-1).
\tag{2}
\]

令

\[
\alpha=\frac{p+1}{2}=ga,\qquad
v=\frac{n+1}{2}=gb,\qquad
g=(\alpha,v),
\tag{3}
\]

则 complete-excess multiplier 是

\[
E=(p-1)b-a\equiv-a-b\pmod p.
\tag{4}
\]

前卡已排除该 **immediate** receiver 的 p-free 门失败。若
\(E\not\equiv1\pmod p\)，其 canonical target 的容量已经严格从 \(p-1\)
降到至多 \(p-2\)。所以本卡只须关闭唯一余下的情况

\[
E\equiv1\pmod p
\quad\Longleftrightarrow\quad
\alpha+v+g\equiv0\pmod p.
\tag{5}
\]

这里的第二个等价式来自把 \(a+b\equiv-1\pmod p\) 乘回 \(g\)；由于
\(g\mid\alpha<p\)，\(p\nmid g\)。

## 2. 奇支：再生被一个有限的精确矛盾排除

设 \(t\) 为奇数。固定-(n) 宏给出

\[
p=24t+1,\qquad L=\frac{5p+7}{6},\qquad pn=4L\delta+1,
\tag{6}
\]

以及唯一整数 \(j\) 满足

\[
14\delta+3=jp,\qquad1\le j\le13,
\qquad21n=5jp+7j-15.
\tag{7}
\]

由 (7) 及 \(p=24t+1\)，有

\[
\alpha=12t+1,\qquad
v=\frac{20jt+2j+1}{7},
\tag{8}
\]

并且

\[
3(7v)-5j\alpha=j+3.
\tag{9}
\]

因此 \(g\mid j+3\)，特别是 \(g\le16\)。将 (5) 乘以 \(42\)，再用
\(p=24t+1\) 消去 \(t\)，得到再生的必要条件

\[
\boxed{p\mid N:=7j+42g+27.}
\tag{10}
\]

但 \(N\le790\)，故 \(p\le790\)。又奇支的 \(t\ge3\)，所以只须对
\(t\in\{3,5,\ldots,31\}\) 的精确有限列表检查 \(24t+1\)；其中的素数恰为

\[
73,\ 313,\ 409,\ 457,\ 601.
\tag{11}
\]

由 \(jp\equiv3\pmod {14}\) 定出 \(j\)，再由 (7)--(8) 定出 \(n,g\)。下表不是
范围实验，而是 (10) 强加的小于 \(790\) 的全部算术候选：

| \(p\) | \(t\) | \(j\) | \(n\) | \(g\) | \(N\) | \(N\bmod p\) |
|---:|---:|---:|---:|---:|---:|---:|
| 73 | 3 | 1 | 17 | 1 | 76 | 3 |
| 313 | 13 | 9 | 673 | 1 | 132 | 132 |
| 409 | 17 | 1 | 97 | 1 | 76 | 76 |
| 457 | 19 | 5 | 545 | 1 | 104 | 104 |
| 601 | 25 | 11 | 1577 | 1 | 146 | 146 |

每一行都与 (10) 矛盾。因此：

\[
\boxed{\text{奇 }t\text{ 的 immediate q=1 receiver 从不发生 }d=1\text{ 再生。}}
\tag{12}
\]

表中包含所有核心素数超集；其中即使有一行不满足更早的 \(q=1\) rail 条件，保留它也只会
加强排除，并不把附加假设偷渡到这里。

## 3. 偶支：再生只能是一个刚性正规形

令 \(t=2s\)。宏的强制 excess prime \(q_\star\) 与 remainder 的闭式为

\[
p=48s+1,\qquad q_\star\mid6s-1,\qquad
3q_\star\delta-4=jp,
\tag{13}
\]

其中

\[
1\le j<3q_\star<p,\qquad j\equiv2\pmod3,
\qquad4n=jp+4-j.
\tag{14}
\]

所以

\[
\alpha=24s+1,\qquad v=6js+1,
\qquad4v-j\alpha=4-j.
\tag{15}
\]

从而 \(g\mid j-4\)。另一方面，(5) 乘以 \(8\) 后给出

\[
j\equiv12+8g\pmod p.
\tag{16}
\]

写 \(j=12+8g-kp\)。因为 \(1\le j<p\)，\(g\le\alpha=(p+1)/2\)，且
\(12+8g-j\) 是 \(p\) 的倍数但严格大于 \(-p\)，有 \(0\le k\le4\)。再由
\(g\mid\alpha\) 得 \(p\equiv-1\pmod g\)；联立 \(g\mid j-4\) 与 (16) 得

\[
g\mid k+8.
\tag{17}
\]

这里 \(g\) 是奇数且 \(3\nmid g\)，因为 \(g\mid24s+1\)。五个 \(k\) 的可能性是：

| \(k\) | 由 (17) 得到的 \(g\) | 对 \(j=12+8g-kp\) 的后果 |
|---:|---|---|
| 0 | \(g=1\) | \(j=20\) |
| 1 | \(g=1\) | \(j=20-p<0\) |
| 2 | \(g\in\{1,5\}\) | \(j\le52-2p<0\) |
| 3 | \(g\in\{1,11\}\) | \(j\le100-3p<0\) |
| 4 | \(g=1\) | \(j=20-4p<0\) |

故只剩

\[
\boxed{g=1,\qquad j=20,\qquad n=5p-4.}
\tag{18}
\]

将 (18) 代回 \(pn=4(9s q_\star)\delta+1\)，精确化简为

\[
q_\star\delta=8(40s+1).
\tag{19}
\]

而 \(q_\star\mid6s-1\)，并且 \(q_\star\) 为奇素数，所以 (19) 蕴含
\(q_\star\mid40s+1\)。最后

\[
20(6s-1)-3(40s+1)=-23,
\tag{20}
\]

强制

\[
\boxed{q_\star=23.}
\tag{21}
\]

这不是对 \(q_\star=23\) 的事后拟合：它是再生假设的必要结论。

## 4. 恰好一次再生，下一条边严格降容量

由 (18)，\(a=(p+1)/2\)、\(b=(5p-3)/2\)。式 (4) 于是成为

\[
E=\frac{5p^2-9p+2}{2},\qquad
E-1=p\frac{5p-9}{2}.
\tag{22}
\]

因为 \(p\ge73\)，右侧第二因子不被 \(p\) 整除，故

\[
\boxed{\nu_p(E-1)=1.}
\tag{23}
\]

此外 \(b\equiv-3/2\pmod p\)，而 \(-a\equiv-1/2\pmod p\)，所以初始再生行的
raw \(p\)-source 门和 p-free bundle 门本身也都通过。

令 \(u=(E-1)/p\)。一般 d=1 再生递推保持 \(g=1\)，并给出

\[
b'=bE-au.
\tag{24}
\]

将 (22) 代入模 \(p\) 后，

\[
b'\equiv\frac34\pmod p,
\qquad
E'=(p-1)b'-a\equiv-\frac54\pmod p.
\tag{25}
\]

因此 \(b'\not\equiv0,-a\pmod p\)：再生后的 raw \(p\)-source 门和 p-free
bundle 门均通过。又 \(E'\not\equiv1\pmod p\)，因为这会要求 \(p\mid9\)。所以第二个
complete-excess target 不可能再生，且其唯一 canonical capacity 为

\[
c\equiv-{E'}^{-1}\equiv4\cdot5^{-1}\pmod p,
\qquad1\le c\le p-2.
\tag{26}
\]

初始再生行本身也自动通过两条 \(p\) 门；所以两次 relay 都可取实际 universal
\(p\)-source。第一条边由 (23) 将 \(p\)-adic 坐标从 \(1\) 降到 \(0\)，第二条由
(26) 将容量从 \(p-1\) 严格降到 \(c\)。结合非再生情形的立即容量下降，得到：

\[
\boxed{
\text{每个 immediate q=1 postmacro }d=1\text{ receiver 在至多两条 strict relay 后}
\text{离开再生支。}}
\tag{27}
\]

## 5. 边界

式 (27) 只关闭 q=1 宏产生的 immediate d=1 receiver 的再生尾部。第二条容量下降边的
target 通常已不是 q=1 image；它随后是否有 terminal certificate、短证书或全局可选的
strict successor，仍是一般 Type I selector 的问题。本卡没有证明 global exit，更没有
证明 Erdős--Straus 猜想。

聚焦重放：

```bash
python3 reproductions/type_ii_q_one_full_carrier_d_one_regeneration_completion.py --verify
```

它只重放 (10) 的五行有限矛盾、两个实际偶支 q=1 再生正规形，以及 \(p=193\) 的完整
两步 source/bundle/capacity 回执；它不作素数范围扫描或终端枚举。
