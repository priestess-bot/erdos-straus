---
kind: claim
claim_id: type-II-q-one-full-carrier-d-one-zero-k-capacity-ray-classification
title: q=1 full-carrier d=1 偶支零 k 容量射线的三相刚性
statement: >-
  设 ordinary q=1 G full-carrier 的 fixed-n 宏后 d=1 算术正规形处于
  偶 t=2s 分支，令 q_* 是 fixed-n 宏的强制 excess prime，j、g 采用既有正规形，
  c 是其 p-free complete-excess target 的 residual capacity，并由
  cj+8g=12c+kp 定义整数 k。则 q_* 整除显式 annihilator
  Gamma(c,k,g)=112c+81k-72g。特别地，若 k=0，则全部可能性恰为
  (c,j,g,q_*,s)=(2,8,1,19,16 mod 19)、(8,11,1,103,86 mod 103) 或
  (56,11,7,103,86 mod 721)。第一条是既有 19 相位；后两条都有显式 ordinary
  q=1 macro 实现：p=157393 给出 c=8，p=4129 给出 c=56。后续的 gap-7
  terminal-first 排除说明 c=56 不会成为 persistent queue；c=8 仍不自动给出
  strict edge。该结果把偶支中唯一 j 不随 s 增长的容量层从一般 c 压缩到三个明确相位，
  并证明 103 射线不是形式空集。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-full-carrier-second-anchor-fixed-n-macro
  - type-II-q-one-full-carrier-d-one-p-free-gate-exclusion-relay
  - type-II-q-one-full-carrier-d-one-capacity-two-rigidity
  - type-I-overflow-full-product-d-one-complete-excess-capacity-map
  - denominator-escape-state-contract
topics:
  - type-II
  - q-one
  - full-carrier
  - type-I
  - d-one
  - residual-capacity
  - q-star
  - capacity-ray
  - finite-rigidity
  - proof-boundary
sources:
  - claim: type-II-q-one-full-carrier-d-one-p-free-gate-exclusion-relay
    role: even-branch-j-g-and-q-star-normal-form
  - claim: type-II-q-one-full-carrier-d-one-capacity-two-rigidity
    role: existing-q-star-19-realization-on-the-c-two-ray
  - reproduction: reproductions/type_ii_q_one_full_carrier_d_one_zero_k_capacity_ray.py
    role: exact-three-shape-modular-phase-and-q-star-103-realization-receipt
visibility: public
last_checked: '2026-08-17'
---

# q=1 full-carrier d=1 偶支零 \(k\) 容量射线的三相刚性

## 1. 偶支的统一容量等式

固定 ordinary \(q=1\) G full-carrier 的 fixed-\(n\) macro，并暂时只记录其宏后
\(d=1\) receiver 的算术正规形；本卡尚未在 root 层施加 terminal-first sieve。令
\(t=2s\)。沿用既有 fixed-\(n\) 宏和 p-free relay 的记号：

\[
p=48s+1,\qquad
q_\star\mid6s-1,\qquad
3q_\star\delta-4=jp,
\tag{1}
\]

\[
1\le j<3q_\star<p,\qquad j\equiv2\pmod3,
\tag{2}
\]

\[
\alpha=24s+1,\qquad v=6js+1,\qquad
g=(\alpha,v),\qquad g\mid j-4.
\tag{3}
\]

因此 \(g\) 为奇数、\(3\nmid g\)，且 \(p\equiv-1\pmod g\)。令 p-free
complete-excess target 的 residual capacity 为 \(c\)。既有容量同余

\[
c(12-j)\equiv8g\pmod p
\tag{4}
\]

等价于存在唯一整数 \(k\) 使

\[
\boxed{cj+8g=12c+kp.}
\tag{5}
\]

本卡只分类这个严格等式中的零层 \(k=0\)。它是唯一使 (5) 中的 \(j\) 不随参数
\(s\) 线性增长的层。

## 2. \(q_\star\) annihilator

由 (1)，\(q_\star\) 同时整除 \(6s-1\) 与 \(jp+4\)。因为 \(q_\star\ne2,3\)，有

\[
p=48s+1=8(6s-1)+9\equiv9\pmod{q_\star}.
\tag{6}
\]

所以 \(q_\star\mid9j+4\)。把它乘以 \(c\)，再用 (5)，得到

\[
\begin{aligned}
c(9j+4)
 &=9(12c+kp-8g)+4c\\
 &=112c+9kp-72g\\
 &\equiv112c+81k-72g\pmod{q_\star}.
\end{aligned}
\tag{7}
\]

因此对**每一个**偶支容量面都有可直接重算的必要条件

\[
\boxed{
q_\star\mid\Gamma(c,k,g):=112c+81k-72g.}
\tag{8}
\]

式 (8) 是对容量三卡中 \(q_\star\mid1239\) 恒等式的统一形式；它没有使用
\(q_\star\) 是最小 excess prime，也没有假设 complete-excess target 已有 terminal。

## 3. 零 \(k\) 的完整分类

令 \(k=0\)。式 (5) 化为

\[
8g=c(12-j).
\tag{9}
\]

左侧为正，故 \(j<12\)。结合 (2)，只有

\[
j\in\{2,5,8,11\}.
\tag{10}
\]

再用 \(g\mid j-4\)、\(g\) 为奇数且 \(3\nmid g\)，得到下表：

\[
\begin{array}{c|c|c|c}
j&g&c=8g/(12-j)&\text{结果}\\ \hline
2&1&4/5&\text{不是整数}\\
5&1&8/7&\text{不是整数}\\
8&1&2&\text{保留}\\
11&1&8&\text{保留}\\
11&7&56&\text{保留}.
\end{array}
\tag{11}
\]

因此零 \(k\) 层恰有三个容量形状：

\[
\boxed{(c,j,g)\in\{(2,8,1),(8,11,1),(56,11,7)\}.}
\tag{12}
\]

## 4. 三个强制相位

将 (12) 代入 (8)，其 annihilator 分别为

\[
\begin{array}{c|c|c}
(c,j,g)&\Gamma(c,0,g)&\text{允许的 }q_\star\\ \hline
(2,8,1)&152=2^3\cdot19&19\\
(8,11,1)&824=2^3\cdot103&103\\
(56,11,7)&5768=2^3\cdot7\cdot103&7\text{ 或 }103.
\end{array}
\tag{13}
\]

第一、二行使用 \(q_\star\ne2,3\) 即给出唯一 prime。第三行还需使用
\(7\mid g\mid24s+1\)，即

\[
s\equiv2\pmod7.
\tag{14}
\]

若第三行有 \(q_\star=7\)，(1) 又会给 \(s\equiv6\pmod7\)，矛盾。因此该行也有

\[
q_\star=103.
\tag{15}
\]

最后由 \(q_\star\mid6s-1\) 得到

\[
\begin{array}{c|c}
(c,j,g,q_\star)&s\text{ 的必要同余}\\ \hline
(2,8,1,19)&s\equiv16\pmod{19}\\
(8,11,1,103)&s\equiv86\pmod{103}\\
(56,11,7,103)&s\equiv86\pmod{721}.
\end{array}
\tag{16}
\]

第三行的模 \(721=7\cdot103\) 同时满足 (14)；它不是把两个独立的相位条件混同。

## 5. \(q_\star=103\) 射线的显式实现

两个 \(q_\star=103\) 射线都不是仅由同余保留下来的形式候选。下表的每一行直接满足
(1)--(5)，并由 fixed-\(n\) macro、full-product fold 与 complete-excess canonical
chart 重放：

\[
\begin{array}{c|c|c|c|c|c|c|c}
p&s&X=12s+1&q_\star&\delta&n&(j,g)&c\\ \hline
4129&86&1033&103&147&11353&(11,7)&56\\
157393&3279&19^2\cdot109&103&5603&432829&(11,1)&8.
\end{array}
\tag{17}
\]

两行的 \(X\) 的全部素因子均为 \(1\pmod3\)，故它们确为 ordinary \(q=1\) G
root 的算术输入。以第一行为例，

\[
3\cdot103\cdot147-4=11\cdot4129,\qquad
4\cdot11353=11\cdot4129+4-11,
\tag{18}
\]

第二行同样满足

\[
3\cdot103\cdot5603-4=11\cdot157393,\qquad
4\cdot432829=11\cdot157393+4-11.
\tag{19}
\]

因此 \(c=8,56\) 的 103 射线不能由“ordinary \(q=1\) 条件会使它们全空”的路线
关闭。随后新增的 [容量五十六 gap-7 terminal-first 排除]
(type-II-q-one-full-carrier-d-one-capacity-fifty-six-gap-seven-terminal-preemption.md)
说明 \(c=56\) 的根会在 macro 前终止；故它保留为算术宏实现，而不再是 persistent
selector 的候选。\(c=8\) 仍须独立执行 terminal-first、typed classification 与一般
Type I selector。

## 6. 作用域

容量 \(c=2\) 的第一行与既有 \(q_\star=19\) 高相位入口相容。容量 \(8\) 和 \(56\)
的两行已有 (17) 的算术 macro receipt；\(c=56\) 已由后续 gap-7 卡排除为
terminal-first 后的持久队列状态，\(c=8\) 则尚未给出全称 Type I/II terminal、可提升
递降或一般 selector。对 \(c=8\) 而言，后续的
[第二完整 excess 增容障碍](type-I-q-one-full-carrier-d-one-c-eight-second-full-excess-carry-obstruction.md)
进一步证明它的确定性 full-excess continuation 反而使 capacity 从 \(8\) 增大，故下一步
不能重复这条 bundle 路线。

此外，本卡不分类 \(k\ne0\) 的容量面；对这些层，\(j\) 的 \(s\)-依赖仍需与
\(\Gamma(c,k,g)\)、\(j<3q_\star\) 及真实 complete-excess provenance 一起处理。
因此该结论是一张可复用容量映射，而不是 G/Type I global exit。

聚焦复核：

~~~bash
python3 reproductions/type_ii_q_one_full_carrier_d_one_zero_k_capacity_ray.py --verify
~~~

复现器只重放 (11)、(13)、(16) 和三个已指定的实际 macro receipt；不做素数范围扫描、
terminal 搜索或对 103 射线的全称 selector 声称。
