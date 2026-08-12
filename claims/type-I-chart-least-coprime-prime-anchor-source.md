---
kind: claim
claim_id: type-I-chart-least-coprime-prime-anchor-source
title: 任意 Type I 图表的最小互素素数一步锚源与 d=1 raw 门消除
statement: >-
  设 R>=3、K>=1，并令 q_* 为不整除 RK(R-1) 的最小素数。则
  (U,V,m)=(q_*,R(q_*-1)-q_*,q_*-1) 是正 primitive formal source，q_* 是相对
  K 的严格超容量素数，且唯一 shift t=1 的 raw 边无约分地一步到达
  (1,R-1,1)。若 L=floor(log_2(RK(R-1)))，则 q_* 位于前 L+1 个素数内并满足
  q_*<=RK(R-1)+1，故 source 与验证菜单均只有输入位长的线性规模。该构造只提供确定性的
  chart-local source/path receipt，不能制造 persistent parent 或 fresh root。应用到完整乘积
  d=1 饱和行时，原 universal p-source 失败类 b≡0 (mod p) 可改用 q_* 到达同一
  complete-excess anchor；此时 p-free 门自动通过，目标 cofactor 精确为
  c=least_positive_residue(a^{-1},p)=least_positive_residue(2g,p)<p-1，故高支撑
  residual capacity 严格下降。于是 raw-p
  失败不再是该 action family 的算术余项；仍需真实 parent、typed/terminal-first 与
  selector adapter 才能登记 verified edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-formal-full-excess-cycle-or-hit-reduction
  - type-I-overflow-full-product-d-one-p-adic-regeneration-countdown
  - type-I-overflow-full-product-d-one-complete-excess-capacity-map
  - type-I-raw-universal-p-parent-root-policy-boundary
  - denominator-escape-state-contract
topics:
  - type-I
  - formal-source
  - raw-path
  - universal-source
  - least-coprime-prime
  - d-one
  - complete-excess-bundle
  - residual-capacity
  - bounded-certificate
  - proof-boundary
sources:
  - claim: type-I-formal-full-excess-cycle-or-hit-reduction
    role: complete-raw-transition-semantics
  - claim: type-I-overflow-full-product-d-one-p-adic-regeneration-countdown
    role: normalized-d-one-residue-and-capacity-map
  - claim: type-I-raw-universal-p-parent-root-policy-boundary
    role: source-provenance-and-root-policy-boundary
  - reproduction: reproductions/type_i_chart_least_coprime_prime_anchor_source.py
    role: focused-one-step-source-and-d-one-raw-gate-receipts
visibility: public
last_checked: '2026-08-12'
---

# 任意 Type I 图表的最小互素素数一步锚源与 \(d=1\) raw 门消除

## 1. 一个不依赖行列式素数的一步源

设

\[
R\ge3,
\qquad
K\ge1,
\tag{1}
\]

并取任意满足

\[
q\text{ 为素数},
\qquad
q\nmid RK
\tag{2}
\]

的 \(q\)。定义

\[
\boxed{
(U,V,m)=\bigl(q,\ R(q-1)-q,\ q-1\bigr).
}
\tag{3}
\]

### 定理 1（互素素数一步锚源）

式 (3) 是正 primitive formal source，且其唯一 \(q\)-raw 边无 gcd 约分地到达

\[
\boxed{(1,R-1,1)}.
\tag{4}
\]

**证明。** 首先

\[
V=(q-1)R-q\ge R-2>0,
\tag{5}
\]

并且

\[
U+V=R(q-1)=Rm.
\tag{6}
\]

由 (2)，

\[
(U,V)=(q,-R)=1,
\tag{7}
\]

所以 source primitive。又因 \(q\nmid K\) 且 \(q\mid U\)、\(q\nmid V\)，有

\[
\nu_q(UV)=1>0=\nu_q(K),
\tag{8}
\]

故 \(q\) 是完整 raw 定义允许的严格超容量标签。raw shift 是唯一的
\(1\le t<q\) 且 \(t\equiv-m\pmod q\)；由 \(m=q-1\) 得

\[
t=1.
\tag{9}
\]

因此未约分输出为

\[
\left(
\frac Uq,
\frac{V+R}{q},
\frac{m+1}{q}
\right)
=(1,R-1,1).
\tag{10}
\]

目标两坐标互素，所以 gcd reduction 也是 \(1\)。证毕。

这个公式不使用 \(4K=pR+1\)，也不要求 \(q\) 是该图表的行列式素数。条件
\(q\mid RK+1\) 只是 (2) 的一个方便充分条件，不参与 shift 或恒等式；下节为避免
source 标签与 anchor cargo 重合，会采用稍强的规范选择。

## 2. 确定性选择与位长界

定义

\[
\boxed{
q_\star:=\min\{q:q\text{ 为素数且 }q\nmid RK(R-1)\}.
}
\tag{11}
\]

这是只依赖图表 \((R,K)\) 的确定性选择，而不是在看到某个期望 raw endpoint 后倒推的
自由标签。额外避开 \(R-1\) 还保证该 source 标签不与随后 anchor 的超额块
\(Q\mid R-1\) 重合。令

\[
L:=\lfloor\log_2(RK(R-1))\rfloor.
\tag{12}
\]

若前 \(L+1\) 个素数都整除 \(RK(R-1)\)，它们的乘积也整除 \(RK(R-1)\)，但该乘积至少为
\(2^{L+1}>RK(R-1)\)，矛盾。所以 \(q_\star\) 位于前 \(L+1\) 个素数内。

另取 \(RK(R-1)+1\) 的任一素因子 \(r\)。必有 \(r\nmid RK(R-1)\)，故

\[
q_\star\le r\le RK(R-1)+1.
\tag{13}
\]

于是 \(q_\star\) 及 (3) 的全部整数只有

\[
O(\log R+\log K)
\tag{14}
\]

位；寻找 \(q_\star\) 时至多检查 \(L+1\) 个素数的整除性。这里声称的是有限菜单和
证书位长，不把一般整数分解假定为单位成本。

## 3. 这不是 fresh-root 许可

定理 1 只证明一张 chart-local actual raw receipt。它没有证明产生该图表的 charged
state 从哪里来，也没有给递归状态的解提升和势下降。因此：

1. 对已真实 persistent 的 state，(3)--(10) 可作为其内部 source/path provenance；
2. 对尚无 parent 的算术图表，不能在事后用 (3) 把它宣布为 fresh root；
3. 任何递归边仍须传播原 scope，重算 target 的 typed F/G/hit 与 terminal-first，
   并独立支付 E4--E5。

这与通用 \(p\)-parent 的 root-policy 边界一致。新增内容不是“每个 node 总能反向造一个
parent”，而是规范的 \(q_\star\) source 从任意合法图表直接到同一个 canonical anchor。

## 4. d=1 raw-p 失败类的严格容量出口

现在固定核心素数 \(p\equiv1\pmod {24}\)，并取完整乘积 \(d=1\) 饱和行

\[
A=\frac{pn-1}{4},
\qquad
R=(p-1)n-1,
\qquad
K=A(p-1).
\tag{15}
\]

沿用归一化参数

\[
\frac{p+1}{2}=ga,
\qquad
\frac{n+1}{2}=gb,
\qquad
(a,b)=1,
\tag{16}
\]

以及 complete-excess support 倍率

\[
E=(p-1)b-a.
\tag{17}
\]

原 universal \(p\)-source 失败恰为

\[
b\equiv0\pmod p
\quad\Longleftrightarrow\quad
p\mid R.
\tag{18}
\]

这时定理 1 的 \(q_\star\) 自动不同于 \(p\)、且不整除 \(Q\)，并仍一步到达旧 anchor
\((1,R-1,1)\)。完整超额块 \(Q\)、余块 \(\beta\) 和 carrier \(M=AE\) 全部与所选
source 标签无关，故同一 path-anchored complete-excess receipt 重新可用。

而且该类自动处于高支撑区。事实上写 \(n=kp-1\)，由
\(n\equiv p\equiv1\pmod4\) 得 \(k\equiv2\pmod4\)，所以

\[
n\ge2p-1,
\qquad
A=\frac{pn-1}{4}>B_p.
\tag{19}
\]

此外 (17)--(18) 给出

\[
E\equiv-a\not\equiv0,1\pmod p.
\tag{20}
\]

第一项说明 \(p\)-free bundle 门自动通过；第二项使用
\(1\le a\le(p+1)/2<p-1\)。canonical target cofactor 因而满足

\[
c\equiv-E^{-1}\equiv a^{-1}\equiv2g\pmod p.
\tag{21}
\]

取 \(1\le c<p\) 的标准代表，则

\[
\boxed{c=\langle2g\rangle_p<p-1.}
\tag{22}
\]

严格性也可直接看出：若 \(c=p-1\)，则 (21) 迫使 \(a=p-1\)，与 (20) 的范围矛盾。
结合 (19)，源与 target 的第一秩坐标同为零，而 residual capacity 从 \(p-1\) 严格降到
\(c\)。

因此，旧表中的 `raw p-source failure` 只是固定选择 \(q=p\) 的 adapter 门，不是
complete-excess action family 的数学 source 缺口。对一个已有真实 parent 的 (15)，
只要 \(q_\star\) receipt、typed reclassification、terminal-first、scope 和恒等
\(\operatorname{Sol}(4,p)\) lift 均进入同一内容地址宏，式 (22) 就支付 E5。

## 5. 聚焦回执与剩余边界

固定 \(p=73\) 的两张 raw-p 失败控制为：

- \(n=145\)：\(q_\star=5\)，目标容量 \(72\to2\)；
- 倒计时端点 \(n=9365182993\)：\(q_\star=11\)，目标容量同样为 \(72\to2\)。

下列无扫描回执重算 \(q_\star\) 的有界菜单、primitive 一步边和完整乘积容量出口：

```bash
python3 reproductions/type_i_chart_least_coprime_prime_anchor_source.py --verify
```

本定理消除了 \(d=1\) 倒计时末端两个旧门类中的 raw-source 类。另一个
\(p\)-free failure 类仍不能 canonical rechart；它需要沿真实 raw Reach 继续分派，
不能由本源定理修复。
