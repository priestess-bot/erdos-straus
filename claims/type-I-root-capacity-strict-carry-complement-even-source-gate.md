---
kind: claim
claim_id: type-I-root-capacity-strict-carry-complement-even-source-gate
title: 严格 root carry 的互补偶源三分与高半区单同余提升门
statement: >-
  对核心素数 p=1 (mod 24) 的 strict proper-root carry，令其 canonical
  cofactor 为 1<=c<=p-2，并以 c 的奇偶性规范地选取互补偶源
  n=c (2|c) 或 n=p-c (2∤c)，以及奇距离 delta=p-n。则 2<=n<p、n
  为偶数、delta 为奇数，并有显式源解 4/n=1/(n/2)+1/n+1/n。若 n<=p/4，
  该标准源的任一原坐标均不能保留到 4/p；若 p/4<n<p/2，唯一可保留的 n
  作为目标首分母，因而其一分母提升精确等价于 gap 4n-p 的直接 Type I/II
  证书；对本卡的坐标保留与奇距离机制，只有 n>p/2 是非平凡的
  canonical-complement source 域。在此高半区，
  保留一个 n 并重组另两项存在当且仅当存在 e|(pn)^2、e<=pn、
  e=-pn (mod 4n-p)，并由显式二项因子式给出 n<p 的标记提升。既有奇距离偶源扇也
  只有 n>p/2 才可能有 compatible ray。因此 strict root cofactor 本身不自动给出
  小分母递降；它把这一分支精确缩成高半区的两个独立有限 selector。实际 strict
  controls p=73,r=3 与 p=313,r=271 分别显示低半区与高半区的失败边界。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-strict-carry-support-rebase
  - odd-distance-even-source-descent
  - one-denominator-lift-factor-criterion
  - middle-coordinate-lift-certificate-equivalence
topics:
  - type-I
  - root-capacity
  - strict-carry
  - descent
  - even-source
  - canonical-complement
  - divisor-residue
  - certificate
  - proof-boundary
sources:
  - claim: type-I-root-capacity-strict-carry-support-rebase
    role: strict-root-cofactor-and-actual-controls
  - claim: odd-distance-even-source-descent
    role: complete-odd-distance-even-source-fan
  - claim: one-denominator-lift-factor-criterion
    role: exact-retained-denominator-tail-factorization
  - claim: middle-coordinate-lift-certificate-equivalence
    role: middle-band-certificate-collapse
  - reproduction: reproductions/type_i_root_capacity_strict_carry_complement_even_source_gate.py
    role: fixed-strict-root-and-high-half-construction-controls
visibility: public
last_checked: '2026-08-14'
---

# 严格 root carry 的互补偶源三分与高半区单同余提升门

## 1. 从 strict cofactor 规范地产生一个小偶源

固定一个 core prime

\[
p\equiv1\pmod {24}.
\]

设 actual proper-root strict carry 的 complete-excess support rebase cofactor 是

\[
1\le c\le p-2.
\tag{1}
\]

这里的 \(c\) 是

\[
c=\langle-E^{-1}\rangle_p,
\]

而不是任意选择的模 \(p\) 单位。定义其 canonical even complement 为

\[
n=
\begin{cases}
c,&2\mid c,\\
p-c,&2\nmid c,
\end{cases}
\qquad
\delta=p-n.
\tag{2}
\]

由于 \(p\) 为奇数，(1) 立即给出

\[
\boxed{2\le n<p,\qquad 2\mid n,\qquad 1\le\delta<p,\qquad
2\nmid\delta.}
\tag{3}
\]

因此 \(n\) 不需要任何猜测性 source solver：它总有标准偶源解

\[
\boxed{
\frac4n=\frac1{n/2}+\frac1n+\frac1n.}
\tag{4}
\]

这条观察本身没有把 (4) 提升到 \(p\)。下文精确划出何时这种由 strict carry
产生的 source 真正提供新的递降出口。

## 2. 保留标准坐标的三分

标准源 (4) 只有两个不同坐标：\(n/2\) 和 \(n\)。先问一个最弱的问题：
目标 \(4/p\) 的正三项分解能否保留其中的一个坐标？

### 低半区：没有坐标可保留

若

\[
n\le\frac p4,
\tag{5}
\]

则 \(n/2<n\le p/4\)。对任意 \(a\le p/4\)，有 \(1/a\ge4/p\)；等号会迫使
\(4\mid p\)，与 \(p\) 为奇素数矛盾。故 \(4/p\) 的正三项分解不可能含有
\(n/2\) 或 \(n\)。

\[
\boxed{n\le p/4\Longrightarrow
\text{标准偶源的原坐标不能被任何正 target 保留。}}
\tag{6}
\]

这只排除 coordinate-retaining maps；它不排除同时重组全部三个 source 坐标的其它
机制。

### 中间带：退化为直接证书

若

\[
\frac p4<n<\frac p2,
\tag{7}
\]

则 \(n/2<p/4\)，仍不能保留。若 target 保留 \(n\)，则

\[
\frac4p-\frac1n=\frac{4n-p}{pn}<\frac1n,
\tag{8}
\]

所以其余两个 target 分母都严格大于 \(n\)。因此 \(n\) 是 target 的首分母，
而

\[
m=4n-p
\tag{9}
\]

满足 \(3\le m\le p-2\)、\(m\equiv3\pmod4\)。由中间分母的一分母提升等价，
保留 \(n\) 的存在性精确等价于 gap \(m\) 的直接 Type I/II 除子证书：

\[
\boxed{
\frac p4<n<\frac p2
\Longrightarrow
\text{标准源的 retained-}n\text{ 分支不是独立递降，而是直接短证书。}}
\tag{10}
\]

### 高半区：两条 canonical-complement 直接机制的唯一非平凡域

只剩

\[
\boxed{n>\frac p2.}
\tag{11}
\]

此时保留一个 \(n\) 并重组标准源的另两项不再是首分母证书的重述。令

\[
R=4n-p,
\qquad S=pn.
\tag{12}
\]

有 \(R>0\)，且

\[
(R,S)=1.
\tag{13}
\]

事实上 \((R,p)=(4n,p)=1\)，而 \((R,n)=(p,n)=1\)，其中 \(n<p\) 且 \(p\)
为素数。

应用标准二项单位分数因式分解，以下命题等价：

1. 存在正整数 \(u,v\)，使
   \[
   \frac4p=\frac1n+\frac1u+\frac1v;
   \tag{14}
   \]
2. 存在正整数 \(e\)，使
   \[
   \boxed{
   e\mid S^2,\qquad e\le S,\qquad e\equiv-S\pmod R;}
   \tag{15}
   \]
3. 对这样的 \(e\)，有
   \[
   u=\frac{S+e}{R},
   \qquad
   v=\frac{S+S^2/e}{R}.
   \tag{16}
   \]

式 (13) 使第二个互补因子的同余自动成立。又 (4)、(14) 给出一个无需递归求解
\(n\) 的显式 strict marked lift：

\[
\boxed{
\left(\frac n2,n,n\right)
\in\operatorname{Sol}(n)
\quad\longmapsto\quad
(n,u,v)\in\operatorname{Sol}(p),
\qquad n<p.}
\tag{17}
\]

故 (15) 是由 strict root carry 的 high-half canonical complement 所需的一个精确、
有限、单同余 selector，而非仅仅的充分条件。

## 3. 与奇距离偶源扇的共同半区门

(2) 同时把 \(n\) 写成既有奇距离偶源扇的候选源 \(n=p-\delta\)。该扇若有
compatible ray，则某个正因子 \(a\mid n\) 满足

\[
\frac na=1+\delta r,
\qquad r\ge1.
\tag{18}
\]

因此 \(n/a\ge\delta+1\)，从而

\[
n>\delta
\Longleftrightarrow
n>\frac p2.
\tag{19}
\]

这给出没有扫描的必要条件：

\[
\boxed{
n\le p/2
\Longrightarrow
\text{canonical complement 的完整奇距离偶源扇没有 compatible ray。}}
\tag{20}
\]

所以 high half (11) 是两条由 canonical complement 自然诱导的 direct-lift
机制同时可能工作的唯一域：

| Root-complement 区域 | retained-standard-tail | odd-distance even-source fan |
|---|---|---|
| \(n\le p/4\) | 原坐标不可能保留 | 无 compatible ray |
| \(p/4<n<p/2\) | 退化为 gap \(4n-p\) 的直接证书 | 无 compatible ray |
| \(p/2<n<p\) | 精确门 (15) | 仍须额外满足 (18) 与平方尾门 |

这是一个 capacity map，不是全称 selector：高半区不会强迫 (15) 的因子，也不会强迫
(18) 的 ray。

## 4. 两个 actual strict-root 边界

该门与 actual root receipt 的连接不能只靠 \(c\) 的形式值。两个已固定的 actual
strict controls 给出互补边界。

### 低半区控制：\(p=73,r=3\)

actual receipt 有 \(E=10583\)、\(c=37\)，所以

\[
n=p-c=36,
\qquad \delta=37.
\]

这里 \(p/4<n<p/2\)，故 (20) 先排除奇距离扇；retained-\(n\) 分支即使成功也只是
gap \(4n-p=71\) 的直接证书。对 \(R=71,S=2628\)，(15) 的精确有序尾因子--同余
检查为空，所以这个固定控制不命中 retained-standard-tail gate。

### 高半区控制：\(p=313,r=271\)

actual hard-root strict receipt 有

\[
E=2077472563,
\qquad c=298,
\qquad n=298,
\qquad \delta=15.
\]

它已落在 (11)，却仍不自动给出 direct descent：

\[
R=879,
\qquad S=93274,
\]

而 (15) 的精确有序尾因子--同余检查为空。同时
\(298\) 的非平凡因子商为 \(298,149,2\)，没有一个等于 \(1\pmod {15}\)，故连
odd-distance fan 的 compatible ray 也不存在。

因此这个 actual high-half strict carry 是下述错误断言的反例：

\[
\text{``strict root carry 总能由其 canonical even complement 直接下降''}.
\]

它不反驳其它 source、其它保留坐标或 complete-excess support rebase 的高支撑秩下降；
它只精确限定了本卡的两条 direct source 机制。

### 非空构造控制

高半区门并非恒空。取 core prime \(p=21169\)、偶源 \(n=12198\) 与 \(e=342\)，有

\[
R=27623,
\qquad S=258219462,
\qquad e\mid S^2,
\qquad e\equiv-S\pmod R.
\]

式 (16) 给出

\[
\frac4{12198}=\frac1{6099}+\frac1{12198}+\frac1{12198}
\quad\Longrightarrow\quad
\frac4{21169}
=\frac1{12198}+\frac1{9348}+\frac1{7057998628}.
\tag{21}
\]

它验证 (15)--(17) 的构造性，但不是一个 actual root-complement 命中。

## 5. 对全局出口的精确影响

strict root carry 现有的 support-rebase 已给出条件性的高支撑良基秩下降；本卡另给出
一条真正以 \(n<p\) 为秩的 direct marked-lift 入口。要把它升级为全局出口，仍需证明：

\[
\text{每个未终止 strict root 至少满足一个短证书、(15)，或完整奇距离扇的尾门。}
\]

现有两条 actual control 已表明这不能从 strictness 或 cofactor parity 单独推出。下一步
有意义的数学目标是把 actual receipt 的 \(Q,E,D,h\) 赋值约束接到 high-half residue
\(e\equiv-pn\pmod {4n-p}\)，或证明低半区必先落入短证书，而不是扩大对任意 \(n\)
的扫描。

## 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_strict_carry_complement_even_source_gate.py --verify
```

该回执只重算两个 actual strict-root controls 与一个固定高半区正构造；不扫描素数、
根层、分母或历史 selector。
