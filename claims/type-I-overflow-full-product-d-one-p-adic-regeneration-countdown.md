---
kind: claim
claim_id: type-I-overflow-full-product-d-one-p-adic-regeneration-countdown
title: 完整乘积 d=1 饱和高锚的 p 进再生倒计时与严格扩展秩
statement: >-
  固定核心素数 p≡1 (mod 24) 及完整乘积 d=1 饱和行
  A=(pn-1)/4、K=A(p-1)。令 alpha=(p+1)/2、v=(n+1)/2、
  g=gcd(alpha,v)、a=alpha/g、b=v/g，则其 complete-excess support 倍率精确为
  E=(p-1)b-a。raw p-source 失败、p-free 失败、d=1 canonical 再生分别等价于
  b≡0、-a、-a-1 (mod p)，其余两门通过的剩余类把目标容量从 p-1 严格降到
  c=least_positive_residue(-E^{-1},p)≤p-2。若 E≡1 (mod p)，写 s=(E-1)/p，
  则目标仍是 d=1 行，
  n'=En-s、b'=bE-as，且 g 与 a 不变；下一倍率满足
  E'-1=s[p+(p-1)(pb-a)]，故 v_p(E'-1)=v_p(E-1)-1。于是连续 canonical
  再生次数恰为初始 v_p(E-1)，不存在无限 d=1 stutter。把 eta=v_p(E-1)
  附加在 Lambda_p^sharp 之后，得到对所有原 Lambda_p^sharp-strict 边及这些再生边
  严格下降的良基秩。该结论在真实 persistent parent、两条 p 门、typed 重分类与
  terminal-first 均通过时支付 complete-excess 宏的 E5；它不覆盖两个门失败端点，
  也不是整个 G/Type I selector 的全局秩。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-full-product-d-one-complete-excess-capacity-map
  - type-I-high-support-bundle-carry-capacity-terminal-dispatch
  - type-I-overflow-unbounded-same-chart-promotion-persistence-boundary
  - type-I-high-anchor-cofactor-macro-e1-e4-admission
  - denominator-escape-state-contract
topics:
  - type-I
  - overflow
  - fixed-n
  - full-product
  - d-one
  - high-anchor
  - complete-excess-bundle
  - p-adic-countdown
  - residual-capacity
  - well-founded-descent
  - proof-boundary
sources:
  - claim: type-I-overflow-full-product-d-one-complete-excess-capacity-map
    role: exact-complete-excess-multiplier-and-two-p-gates
  - claim: type-I-high-support-bundle-carry-capacity-terminal-dispatch
    role: canonical-target-capacity-gate
  - claim: type-I-overflow-unbounded-same-chart-promotion-persistence-boundary
    role: exact-outer-support-rank-and-persistent-endpoint-boundary
  - reproduction: reproductions/type_i_overflow_d_one_p_adic_regeneration_countdown.py
    role: focused-countdown-capacity-and-gate-boundary-receipts
visibility: public
last_checked: '2026-08-12'
---

# 完整乘积 \(d=1\) 饱和高锚的 \(p\) 进再生倒计时与严格扩展秩

## 1. 归一化参数与四类剩余

固定

\[
p\equiv1\pmod {24},\qquad n>1,\qquad n\equiv1\pmod4,
\tag{1}
\]

并考虑完整乘积 \(d=1\) 饱和行

\[
A=\frac{pn-1}{4},\qquad
R=(p-1)n-1,\qquad
K=A(p-1).
\tag{2}
\]

已有 complete-excess 容量公式给出唯一的新 support

\[
M=AE,\qquad
E=\frac{((p-1)n-2)/2}
        {\gcd((p+1)/2,(n+1)/2)}>1.
\tag{3}
\]

令

\[
\alpha=\frac{p+1}{2},\qquad
v=\frac{n+1}{2},\qquad
g=(\alpha,v),\qquad
\alpha=ga,\qquad v=gb.
\tag{4}
\]

于是 \((a,b)=1\)。又因为

\[
\frac{(p-1)n-2}{2}=(p-1)v-\alpha,
\tag{5}
\]

式 (3) 化为

\[
\boxed{E=(p-1)b-a},
\qquad
E\equiv-a-b\pmod p.
\tag{6}
\]

这把旧的两条 \(p\)-门和 canonical stutter 压缩成四类互斥剩余：

\[
\begin{array}{c|c}
b\pmod p & \text{complete-excess 分派}\\ \hline
0 & \text{primitive raw }p\text{-source 门失败}\\
-a & p\text{-free bundle 门失败}\\
-a-1 & d=1\text{ canonical 再生}\\
\text{其它} & \text{目标 residual capacity 严格下降}.
\end{array}
\tag{7}
\]

前两行来自

\[
n=2gb-1,
\qquad
p\nmid g,
\qquad
p\nmid R\Longleftrightarrow b\not\equiv0\pmod p,
\tag{8}
\]

以及 \(p\nmid Q\Longleftrightarrow p\nmid E\)。第三行将在下一节证明。
这些特殊剩余确实互不相交：\(p\nmid a\)，而

\[
1\le a\le\alpha=\frac{p+1}{2}<p-1,
\tag{9}
\]

所以 \(a\not\equiv-1\pmod p\)。特别地，处于再生剩余类时，两条 \(p\)-门自动通过。

## 2. canonical target 的精确容量二分

先假设 \(p\nmid E\)，从而 support \(M=AE\) 的 canonical target 有定义。写

\[
c:=\frac{K_M}{M}\in\{1,\ldots,p-1\}.
\tag{10}
\]

由 \(4A\equiv-1\pmod p\) 和 \(4Mc\equiv1\pmod p\)，得到

\[
\boxed{c\equiv-E^{-1}\pmod p}.
\tag{11}
\]

这也是一般 high-support carry gate 在源容量 \(K/A=p-1\)、乘子 \(E\) 上的特化。
标准代表的唯一性给出

\[
\boxed{
c=p-1\Longleftrightarrow E\equiv1\pmod p.
}
\tag{12}
\]

因此若 \(E\not\equiv1\pmod p\)，则

\[
1\le c\le p-2<p-1=\frac KA.
\tag{13}
\]

当源 support 已在高支撑区 \(A>B_p\) 时，式 (13) 直接支付精确秩
\(\Lambda_p^\sharp=(\lfloor B_p/A\rfloor,K/A)\) 的第二坐标。若
\(A\le B_p\)，已有 \(M>p^2>B_p\) 则由第一坐标支付。这说明四类表最后一行不是
启发式改善，而是精确的算术 E5。

## 3. d=1 再生的精确递推

现在设

\[
E\equiv1\pmod p,
\qquad
s:=\frac{E-1}{p}.
\tag{14}
\]

由 (12)，target 仍有 \(c=p-1\)。定义

\[
\boxed{n'=En-s}.
\tag{15}
\]

则

\[
pn'=pEn-(E-1)=(pn-1)E+1=4AE+1=4M+1.
\tag{16}
\]

所以 target 不是一个没有结构的等容量 chart，而恰是下一条 \(d=1\) 饱和行：

\[
M=\frac{pn'-1}{4},\qquad
R_M=(p-1)n'-1,\qquad
K_M=M(p-1).
\tag{17}
\]

其归一化参数也有封闭递推。由 (4)、(14)--(15)，

\[
\frac{n'+1}{2}
=gbE-\alpha s
=g(bE-as).
\tag{18}
\]

令

\[
\boxed{b'=bE-as}.
\tag{19}
\]

由于 \(p\equiv1\pmod4\)，\(\alpha\) 为奇数，故

\[
(\alpha,p-1)=(\alpha,2)=1.
\tag{20}
\]

从而

\[
(a,b')=(a,bE)=(a,E)=(a,(p-1)b)=1.
\tag{21}
\]

式 (18)--(21) 证明

\[
\gcd\left(\alpha,\frac{n'+1}{2}\right)=g.
\tag{22}
\]

也就是说，再生过程严格保持 \(g\) 与 \(a\)，下一条 complete-excess 倍率仍可在同一
归一化坐标中写成

\[
E'=(p-1)b'-a.
\tag{23}
\]

## 4. p 进估值每步恰减一

由 \(E=1+ps\)，式 (19) 可重写为

\[
b'=b+s(pb-a).
\tag{24}
\]

把它代入 (23)，并使用
\((p-1)b-a-1=E-1=ps\)，得到核心恒等式

\[
\boxed{
E'-1
=s\bigl[p+(p-1)(pb-a)\bigr].
}
\tag{25}
\]

方括号中的因子满足

\[
p+(p-1)(pb-a)\equiv a\not\equiv0\pmod p,
\tag{26}
\]

所以它是一个 \(p\)-单位。因此

\[
\boxed{
\nu_p(E'-1)=\nu_p(s)=\nu_p(E-1)-1.
}
\tag{27}
\]

这给出了 canonical stutter 的精确倒计时，而不仅是“最终似乎会离开”的实验现象。
若初始

\[
\rho:=\nu_p(E-1),
\tag{28}
\]

则连续再生恰发生 \(\rho\) 次。中间任一仍满足 \(E\equiv1\pmod p\) 的节点都由
(7)--(9) 自动通过两条 \(p\)-门，所以倒计时不会在中途被门失败截断。第 \(\rho\)
次再生后到达 \(\nu_p(E-1)=0\) 的 \(d=1\) 行；在那里恰有三种结果：

1. 两门通过，当前行的下一次 complete-excess action 由 (13) 严格降容量；
2. \(b\equiv0\pmod p\)，raw \(p\)-source 门失败；
3. \(b\equiv-a\pmod p\)，\(p\)-free bundle 门失败。

所以不存在无限的 \(d=1\) complete-excess canonical stutter。后续的最小互素素数源
定理又消除了第 2 类的算术 source 缺口：它只是在固定 \(q=p\) 时失败，换用规范
\(q_\star\nmid RK\) 后仍到达同一 anchor，并且容量严格下降。第 3 类仍不是 terminal，
必须沿真实 \(p\)-peeling 后的 competing-excess Reach 继续处理；静默删除 \(p\)-block
会丢失来源回执。

## 5. 严格扩展秩及其作用域

对 charged canonical state \(H=(p,R_H,K_H;A_H)\)，定义

\[
\widehat\Lambda_p(H)=
\left(
\left\lfloor\frac{B_p}{A_H}\right\rfloor,
\frac{K_H}{A_H},
\eta(H)
\right),
\tag{29}
\]

其中 certified \(d=1\) 饱和正规形取

\[
\eta(H)=\nu_p(E_H-1),
\tag{30}
\]

其它状态取 \(\eta(H)=0\)。在自然数字典序下：

1. 低支撑 \(d=1\) action 因 \(A_H\le B_p<M\) 而严格降低第一坐标；
2. 高支撑非再生 action 因 \(p-1\to c\le p-2\) 而严格降低第二坐标；
3. 再生 action 的前两坐标保持为 \((0,p-1)\)，第三坐标由 (27) 严格减一；
4. 任一原本已严格降低 \(\Lambda_p^\sharp\) 的边仍严格降低 (29)，因为第三坐标不影响
   更早坐标的比较。

故 (29) 是“所有已有 \(\Lambda_p^\sharp\)-strict 边，加上上述 \(d=1\) 再生边”所成
子图上的严格良基秩。这个作用域不可删去：尚未逐一证明整个 G/Type I selector 中所有
保持前两坐标的其它 action 都不增加 \(\eta\)，所以 (29) 目前不是全图势函数。

## 6. E1--E5 的准确结论

以上第 1--5 节是无条件整数算术。要把某一步登记成真实递归边，source 仍必须是带
charged parent、内容地址和原样 scope 的 queued persistent state，并且：

1. primitive raw \(p\)-source 与 \(p\)-free complete-excess 两门通过；
2. path、完整超额块、lcm cargo 和 target 全部绑定到精确 source state ID；
3. target/checkpoint 独立重算 normal form、F/G/hit、state ID 与 terminal-first；
4. 标记集保持为图表无关的 \(\operatorname{Sol}(4,p)\)，用恒等映射提升；
5. E5 使用 (29)，而不是把 transient checkpoint 与 target 作伪比较。

这些 receipt 在每个 checkpoint 都重新具备时，倒计时链的每一步都有 E1--E5；若
terminal-first 命中则直接
返回短证书，不再入队。通用 raw parent 只提供 chart-local provenance，不能反向制造
fresh root policy。当前通用 typed serializer/verifier 尚未接入统一 selector，因此本卡
不把算术族批量升级成 `verified_edge`。

## 7. sharp 边界与聚焦回执

两个原门失败类在算术上都非空。固定 \(p=73\)：

- \(n=5325\) 经一次再生到 \(n'=1020794549\)，下一倍率满足
  \(E'\equiv0\pmod {73}\)，精确停在 \(p\)-free 门失败；
- \(n=16129\) 经一次再生到 \(n'=9365182993\)，下一归一化参数满足
  \(b'\equiv0\pmod {73}\)，精确停在 raw-source 门失败。

这两个控制只证明原分类的 sharp 边界真实存在，不证明它们已有 persistent 可达性。
其中 raw-source 类已由
[最小互素素数一步锚源](type-I-chart-least-coprime-prime-anchor-source.md) 条件性接回严格出口；
\(p\)-free 类的直接删块捷径则由
[p-block 来源丢失障碍](type-I-overflow-full-product-d-one-p-block-peeling-obstruction.md) 全称排除。
直接降容量、一次再生、两次再生和两个 sharp 端点由下列无扫描回执固定核验：

```bash
python3 reproductions/type_i_overflow_d_one_p_adic_regeneration_countdown.py --verify
```

本定理把旧的“\(d=1\) canonical stutter”严格消除。结合后续两卡，当前算术余项已经
进一步压缩为唯一的 \(p\)-free failure 类及其 peeled competing-excess Reach；所有实际
宏仍须补齐 typed persistence 接口。这里尚未给出该余类的 terminal 或更小分母 lift，
因而不是 G/Type I global exit 的最终证明。
