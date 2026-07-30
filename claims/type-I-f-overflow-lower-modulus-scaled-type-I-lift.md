---
kind: claim
claim_id: type-I-f-overflow-lower-modulus-scaled-type-I-lift
title: 低模数盒内命中的缩放—模数交换提升判据
statement: 设 4K=pR+1、R=mt，且低模数 t 上有盒内目标除子 d|K^2、d<K、d=-K mod t。将 d 规范化为 d=B^2C、K=BCH、A=(B+H)/t，则它给出缩放分子 P=pm 的 Type I 解 (ABC,ACH,PK)。对 c|m，这三个分母可同时除以 c 当且仅当 c|A，等价于 d=-K mod ct；除后同一 d 成为分子 p(m/c)、模数 ct 的 Type I 正规形。故最大一步为 c=gcd(m,A)，完整提升到 p 当且仅当原模数 R 已盒内命中。原 R 为 F-box miss 时，任何始终重选 d_i|K^2、保持同一 K^2 除子格的有限链都不可能以这种方式闭合到 p。六个冻结 lower hit 的 50 个向量给出 25 对正规形，完整提升 0 对，仅 1 对可严格部分约去 c=3。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-f-overflow-balanced-lower-modulus-fiber-profile
  - type-I-general-b-centered-square-spectrum
  - type-I-f-overflow-lower-modulus-shared-gap-type-II-lift
topics:
  - type-I
  - F-state
  - lower-modulus
  - scaled-numerator
  - solution-lift
  - target-divisor
  - descent
  - negative-boundary
  - proof-program
sources:
  - claim: type-I-f-overflow-balanced-lower-modulus-fiber-profile
    role: lower-modulus-hit-input
  - claim: type-I-general-b-centered-square-spectrum
    role: centered-target-divisor-normalization
visibility: public
last_checked: '2026-07-30'
---

# 低模数盒内命中的缩放—模数交换提升判据

## 定理

设

\[
4K=pR+1,\qquad R=mt,
\tag{1}
\]

其中 \(p,m,t,R\) 都是正奇数，且 \(t>1\)。于是

\[
4K=(pm)t+1,\qquad (K,R)=1.
\tag{2}
\]

假设低模数 \(t\) 的原 \(K\)-指数盒内存在目标除子

\[
d\mid K^2,\qquad d<K,\qquad d\equiv-K\pmod t.
\tag{3}
\]

令

\[
g=(d,K),\qquad
B=\frac d g,\qquad
C=\frac{g^2}{d},\qquad
H=\frac K g.
\tag{4}
\]

则

\[
d=B^2C,\qquad K=BCH,\qquad (B,H)=1.
\tag{5}
\]

由 (3) 和 \((t,BC)=1\)，可定义

\[
A=\frac{B+H}{t},\qquad
f=\frac{4B^2C+1}{t}.
\tag{6}
\]

若记缩放分子 \(P=pm\)，则

\[
P=4ABC-f
\tag{7}
\]

并有显式三项分解

\[
\boxed{
\frac4P
=\frac1{ABC}+\frac1{ACH}+\frac1{PK}.
}
\tag{8}

而且

\[
(A,B)=1,\qquad B<H,\qquad 0<f<P.
\tag{8a}
\]
\]

对任意 \(c\mid m\)，下列条件等价：

\[
\begin{aligned}
&c\mid ABC\ \text{且}\ c\mid ACH;\\
&c\mid A;\\
&ct\mid B+H;\\
&d\equiv-K\pmod {ct}.
\end{aligned}
\tag{9}
\]

条件成立时，(8) 的三个分母都能同时除以 \(c\)，并得到

\[
\frac4{p(m/c)}
=\frac1{ABC/c}+\frac1{ACH/c}+\frac1{p(m/c)K}.
\tag{10}
\]

更精确地，令

\[
m'=\frac mc,\qquad t'=ct,\qquad A'=\frac Ac,
\qquad f'=\frac fc.
\tag{11}
\]

则同一个 \((B,C,H,d,K)\) 满足

\[
4K=(pm')t'+1,\qquad
p m'=4A'BC-f',
\tag{12}
\]

所以 (10) 仍是同一目标除子的 Type I 正规形，而不只是偶然可约的单位分数恒等式。

## 证明

式 (4)--(5) 是平方除子标准规范化。因为 \(BC\mid K\) 且 \((K,R)=1\)，有

\[
(BC,mt)=1.
\tag{13}
\]

由 \(d+K=BC(B+H)\) 和 (3) 可消去 \(BC\)，得到 \(t\mid B+H\)。同理，

\[
4d+1=4B^2C+1\equiv0\pmod t,
\]

故 (6) 中的 \(A,f\) 均为正整数。直接计算

\[
\frac1{ABC}+\frac1{ACH}
=\frac{B+H}{ABCH}
=\frac tK.
\]

再用 \(Pt+1=4K\)，便得到

\[
\frac tK+\frac1{PK}=\frac{Pt+1}{PK}=\frac4P,
\]

即 (8)。等式 (7) 也由同一计算直接恢复。

若某个素数同时整除 \(A,B\)，由 \(At=B+H\) 也会整除 \(H\)，与
\((B,H)=1\) 矛盾，故 \((A,B)=1\)。另外

\[
\frac dK=\frac BH<1,
\]

所以 \(B<H\)，并且

\[
t(P-f)=4BC(H-B)-2>0.
\]

这证明 (8a)，也说明 (8) 确实位于自然 Type I 正规形范围。

由于 \(c\mid m\) 且 \((m,BCH)=1\)，前两个分母同时被 \(c\) 整除，当且仅当
\(c\mid A\)。又 \(B+H=tA\)，所以这等价于 \(ct\mid B+H\)。利用
\((ct,BC)=1\) 和 \(d+K=BC(B+H)\)，再等价于 \(d\equiv-K\pmod {ct}\)，
得到 (9)。第三分母 \(PK=pmK\) 自动被每个 \(c\mid m\) 整除。

将 (8) 乘以 \(c\) 即得 (10)。因为 \(c\mid A,m\)，式 (7) 还推出
\(c\mid f\)；把 (2)、(7) 同时除去相应的 \(c\)，便得到 (11)--(12)。

## 最大约去量与固定支撑不可能性

一次可约去的最大因子精确为

\[
c_{\max}
=(m,A)=(m,AC)=(m,f)=\frac{(R,d+K)}t.
\tag{14}
\]

这里四个表达式的相等也不是额外假设。由 \((m,BCH)=1\) 先有
\((m,AC)=(m,A)\)。又由 \(P=pm=4ABC-f\)，模 \(m\) 有
\(f\equiv4ABC\)，而 \((m,4BC)=1\)，故 \((m,f)=(m,A)\)。最后

\[
d+K=BC(B+H)=BCtA
\]

给出

\[
(R,d+K)=(mt,BCtA)=t(m,A).
\]

完整回到原分子 \(p\) 当且仅当

\[
m\mid A
\iff mt=R\mid B+H
\iff d\equiv-K\pmod R.
\tag{15}
\]

所以，若原 \((K,R)\) 状态是 F-box miss，则低模数盒内命中不可能通过统一约去
\(m\) 直接提升到 \(p\)。这不是有限样本现象，而是定义层面的排除。

还可得到一个更强的链式边界。允许在中间模数

\[
t=t_0\mid t_1\mid\cdots\mid t_j=R
\]

反复重选任意 \(d_i\mid K^2\)。若最终一步仍使用 (9) 的统一缩放机制到达 \(p\)，
则最后的 \(d_j\) 必满足 \(d_j\equiv-K\pmod R\)。这与原 F-box miss 矛盾。因此：

\[
\boxed{
\text{只改变缩放因子和模数、始终保持同一 }K\text{ 支撑的 divisor-lattice 链，}
\text{不可能闭合原 F-box miss。}
}
\tag{16}
\]

要形成真正递降，必须改变 \(K\) 或其素因子支撑，或者转入独立的 Type II/外部源出口。

对单个正规形取 (14) 后，新的 \(m'=m/c_{\max}\)、\(A'=A/c_{\max}\) 互素，
所以同一 \(d\) 不能再次沿纯缩放方向前进；中间层若想继续，必须重选目标除子。

在当前低模数输入中还有

\[
p\equiv1\pmod4,\qquad m\equiv R\equiv3\pmod4,
\qquad t\equiv1\pmod4.
\tag{17}
\]

所以 \(P=pm\equiv3\pmod4\)，由 (7) 得缩放正规形的缺口

\[
f\equiv1\pmod4.
\tag{18}
\]

任意中间约去后的参数仍满足

\[
f'\equiv-pm'\pmod4,
\]

因此首分母保持整数。若完整约去 \(c=m\)，则最终缺口

\[
h=\frac fm\equiv3\pmod4
\]

正好是原 \(p\equiv1\pmod4\) 所需的合法 Type I 缺口；失败并非来自奇偶格式，而是
来自 (15) 的原模数目标未命中。

## 标记缩放解的精确边界

定义

\[
\operatorname{Sol}(pm)_{[m]}
=\{(X,Y,Z)\in\operatorname{Sol}(pm):m\mid X,Y,Z\}.
\]

逐坐标同乘、同除 \(m\) 给出双射

\[
\boxed{
\operatorname{Sol}(p)
\longleftrightarrow
\operatorname{Sol}(pm)_{[m]},
\qquad
(x,y,z)\longleftrightarrow(mx,my,mz).
}
\tag{19}
\]

因此，证明普通的 \(\operatorname{Sol}(pm)\ne\varnothing\) 并不比原问题更接近终点；
真正有用的是证明这个全分母可除的标记子集非空，而后者与 \(p\) 可解本身等价。

一个无需计算的边界例子说明“已有两个可除尾”仍不够。对
\(m\equiv3\pmod4\)，标准恒等式

\[
\frac4m
=\frac4{m+1}+\frac4{m(m+1)}
=\frac1{(m+1)/4}+\frac1{m(m+1)/2}+\frac1{m(m+1)/2}
\]

按 \(p\) 缩放后给出 \(4/(pm)\) 的解

\[
\left(
\frac{p(m+1)}4,
\frac{pm(m+1)}2,
\frac{pm(m+1)}2
\right).
\tag{20}
\]

后两项都被 \(m\) 整除，但当 \((p,m)=1\)、\(m>1\) 时第一项不被 \(m\) 整除，
所以 (20) 不能下除为 \(p\) 的三项解。这排除了“缩放实例可解”或“两个尾可除”作为
递降替代物。

## 六个 lower hit 的完整审计

复现脚本对冻结的六个 lower-modulus F-box hit 枚举原 \(K\)-指数盒中的全部目标向量，
并把互为逆向量的表示规范为同一个 \(d<K\)：

~~~text
lower_hit_count: 6
target_vector_count: 50
normal_form_count: 25
full_lift_count: 0
strict_partial_reduction_count: 1
no_reduction_count: 24
removable_factor_histogram: {1: 24, 3: 1}
~~~

零个完整提升也由 (15) 和原状态的 F-box miss 性质先验推出。唯一的严格部分约去发生在

\[
p=510725329,\quad R=555,\quad m=15,\quad t=37.
\]

目标向量对为

\[
(-1,-1,1,0),\qquad(1,1,-1,0),
\]

相对于素数顺序 \((13,29,67,2805461)\)。其正规参数为

\[
(A,B,C,H)=(12,67,2805461,377),\qquad (m,A)=3.
\]

因此可把缩放分子从 \(15p\) 严格降到 \(5p\)，同时把模数从 \(37\) 增至
\(111\)，但此时新 \(A'=4\) 与剩余缩放因子 \(5\) 互素，同一关系立即停止；它没有
给出 \(p\) 的解。

另一个边界代表是

\[
p=99151369,\quad R=3395,\quad m=35,\quad t=97,
\]

其中一个正规形为

\[
(A,B,C,H)=(280528,3093,1,27208123).
\]

这里 \((35,A)=1\)，所以只有第三分母自动含有 \(35\)，前两个分母无法同时下除。

## 结论边界

这条定理识别出一个真实但受限的“缩放因子下降”：低模数命中可以用
\(c=(m,A)\) 换取模数从 \(t\) 增长到 \(ct\)。然而原 F-box miss 精确排除了终点
\(ct=R\)。因此它不能作为现成的良基递降证明，反而证明了下一步必须引入至少一种新信息：

1. 改变 \(K\) 支撑的合法源状态转移；
2. 由中间模数产生不依赖固定 \(K^2\) 的 Type II 因子证书；
3. 对未能扩大的缩放因子建立跨状态容量收费。

## 复现

~~~bash
python3 reproductions/type_i_f_overflow_lower_modulus_scaled_type_i_lift.py
~~~

结果文件：

~~~text
reproductions/type-i-f-overflow-lower-modulus-scaled-type-i-lift-results.json
~~~

结果 SHA-256：

~~~text
720a2542cd2a6af338e153f4f3c064edd1d24f43e18c2eafdf5d2122df065190
~~~
