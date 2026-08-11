---
kind: claim
claim_id: type-I-high-support-c2-h1-direct-cofactor-obstruction
title: 最小高支撑 C=2 边界的 H1 direct-cofactor 全称阻碍
statement: 设 p≡1 (mod 24) 为核心素数，最小 C=2 高支撑图表为 H_2(p)=(p,2p-3,K_2;A_2)，其中 A_2=(p-1)(2p-1)/8、K_2=2A_2。其确定性 high-R complete-excess H1 bundle 唯一给出 Q=p-2、beta=2、M=A_2(p-2)。该 bundle 的 canonical overflow cofactor 数据严格为 r=(p-1)/4、C_M=p-1、d=1、s=1。于是 high-cofactor gate 所需 a=A_2/gcd(A_2,C_M)=2p-1 不整除 r；同时 rC_M=B_p<K_2，使候选相位比值 (rC_M-K_2)/(pA_2) 为负，形式 cofactor 图表的 R_T=p-2<p。故 H1 direct-cofactor macro 在每个此类边界上均于 E2 前被拒绝，不能读取唯一内部位 A_2→K_2。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-high-support-c2-boundary-carry-dyadic-capacity-transduction
  - type-I-high-anchor-cofactor-macro-e1-e4-admission
  - type-I-overflow-cofactor-r-chart-support
topics:
  - type-I
  - high-support
  - c2-boundary
  - high-anchor
  - complete-excess
  - direct-cofactor
  - gate-obstruction
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_high_support_c2_h1_direct_cofactor_obstruction.py
    role: symbolic-formula-and-core-prime-controls
visibility: public
last_checked: '2026-08-12'
---

# 最小高支撑 \(C=2\) 边界的 H1 direct-cofactor 全称阻碍

## 1. 边界与问题

固定核心素数

\[
p\equiv1\pmod {24}.
\]

最小高支撑 \(C=2\) 图表是

\[
A_2=\frac{(p-1)(2p-1)}8,
\qquad
R_2=2p-3,
\qquad
K_2=2A_2.
\tag{1}
\]

此前已知：在这个图表上，complete-excess bundle 的任何 canonical target
cofactor 都严格大于 \(2\)，所以该 bundle 家族没有 carry 下降。这里排除一个
不同的、此前不能由 carry 结论排除的后备：把 H1 的确定性 high-\(R\) bundle
交给 direct-cofactor 宏。

结论只量化 H1 的完整超额 bundle；它不量化其它 raw source、partial-excess
选择、非 H1 adapter、直接 Type I/II 终端或任意重新排列三个分母的映射。

## 2. H1 bundle 的闭式

令

\[
R_2-1=2(p-2).
\tag{2}
\]

有

\[
\gcd(p-2,p-1)=1,
\qquad
\gcd(p-2,2p-1)=\gcd(p-2,3)=1.
\tag{3}
\]

最后一个等式使用 \(p\equiv1\pmod3\)，故 \(p-2\equiv2\pmod3\)。又
\(p-2\) 是奇数，而

\[
v_2(K_2)=v_2(p-1)-2\ge1.
\tag{4}
\]

所以相对于 \(K_2\)，(2) 中唯一的完整超容量块恰为

\[
\boxed{Q=p-2,\qquad\beta=2.}
\tag{5}
\]

由 (3)，\((A_2,Q)=1\)，H1 carrier 因而为

\[
M=\operatorname{lcm}(A_2,Q)=A_2(p-2).
\tag{6}
\]

注意 \(p\nmid R_2\)，因为 \(R_2\equiv-3\pmod p\)，故这里没有偷偷绕过
high-\(R\) raw-source 的原始性条件。

## 3. overflow cofactor 的唯一数据

由

\[
8A_2\equiv1\pmod p
\tag{7}
\]

和 \(Q\equiv-2\pmod p\)，(6) 给出

\[
r\equiv M\equiv-\frac14\pmod p.
\]

其标准代表是

\[
\boxed{r=\frac{p-1}{4}.}
\tag{8}
\]

同样地，\(4M\equiv-1\pmod p\)。canonical overflow cofactor
\(C_M\in\{1,\ldots,p-1\}\) 满足 \(4MC_M\equiv1\pmod p\)，故

\[
\boxed{C_M=p-1,\qquad d=p-C_M=1.}
\tag{9}
\]

direct-cofactor 正规形中的

\[
s=\frac{4rd+1}{p}
\]

因此也固定为

\[
\boxed{s=1.}
\tag{10}
\]

这些是从 H1 receipt 唯一导出的数据，不是枚举选择的一个分支。

## 4. 三重 E2 阻碍

写 \(m=(p-1)/8\)。则

\[
A_2=m(2p-1),
\qquad C_M=8m,
\qquad \gcd(2p-1,8m)=1,
\]

从而

\[
g=\gcd(A_2,C_M)=m,
\qquad
a=\frac{A_2}{g}=2p-1.
\tag{11}
\]

direct-cofactor 宏的 support gate 要求 \(a\mid r\)。但

\[
0<r=\frac{p-1}{4}<2p-1=a,
\tag{12}
\]

所以 gate 严格失败。

同一失败还可由两个独立量看出。第一，

\[
rC_M=\frac{(p-1)^2}{4}=B_p,
\]

而

\[
K_2=\frac{(p-1)(2p-1)}4>B_p.
\]

故候选 direct phase 比值

\[
h=\frac{rC_M-K_2}{pA_2}<0,
\tag{13}
\]

不属于允许的 \(h\in\{0,1,2\}\) 相位。第二，若忽略 gate 形式地代入
direct cofactor 图表，(8)--(10) 给出

\[
R_T=4r-s=p-2<p.
\tag{14}
\]

它也不可能是该 high-anchor macro 所要求的高 target。

因此有全称结论

\[
\boxed{
\text{最小 }C=2\text{ 边界的 H1 direct-cofactor macro 永不准入。}
}
\tag{15}
\]

这里不能把 (14) 误登记为一条低图表递降：旧 charged support 的合法性正是由
\(a\mid r\) gate 支付，而 (12) 已经否定它。故 (15) 是 E2/provenance 障碍，
不是一个尚待补解提升的 candidate transition。

## 5. 对全局出口的含义

最小 \(C=2\) 边界现在已知同时排除：

1. complete-excess carry 下降；
2. complete-excess 无法读取唯一的 \(A_2\to K_2\) 内部位；
3. 由该位导出的自然 dyadic 标记及全部双尾保持 \(D\)-only 提升；
4. H1 direct-cofactor macro。

所以该边界的任何 terminal-first 未解决实例若存在，必须经真正不同的
support-preserving alternate、非 H1 source、paid reset，或改变保留尾/坐标语法的
全局解提升退出。这个结论不声称这种实例存在，也不声称已经证明 Erdős--Straus
猜想。

## 6. 聚焦复核

```bash
python3 reproductions/type_i_high_support_c2_h1_direct_cofactor_obstruction.py --verify
```

脚本只复核 (1)--(14) 的符号恒等式及 \(p=73,193,241,337\) 四个核心素数控制；
不运行历史范围扫描。
