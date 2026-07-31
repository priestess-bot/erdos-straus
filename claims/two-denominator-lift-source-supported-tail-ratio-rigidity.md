---
kind: claim
claim_id: two-denominator-lift-source-supported-tail-ratio-rigidity
title: source-supported D-only 提升的固定尾比刚性与中心 Type I 等价
statement: 对核心素数 p、2<=n<p 及 D-only 双尾提升参数 D，若再有 D|n^2，则全部数据唯一消元为一张图表 4lambda=pk+1：替换坐标为 a=n lambda/h、a'=p lambda，标记尾方程恒为 k/lambda=1/b+1/c。因而该标记集非空当且仅当这张图表已有中心 Type I 命中；固定 (p,k,lambda) 后，任何只替换 distinguished coordinate 且保持同一双尾的 source-supported D-only 链都共享同一个尾投影，数值秩下降不会产生新的非空性。反向构造除 h|n^2 外还必须满足 h|n lambda。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - two-denominator-lift-d-only-marked-normal-form
  - type-I-general-b-centered-square-spectrum
  - marked-solution-descent-closure
topics:
  - descent
  - marked-solution
  - two-denominator-lift
  - divisor-parametrization
  - tail-ratio
  - type-I
  - rigidity
  - proof-boundary
sources:
  - claim: two-denominator-lift-d-only-marked-normal-form
    role: D-only-coordinate-and-marked-fiber-interface
  - claim: type-I-general-b-centered-square-spectrum
    role: centered-Type-I-hit-interface
  - claim: marked-solution-descent-closure
    role: marked-state-induction-contract
visibility: public
last_checked: '2026-07-31'
---

# source-supported \(D\)-only 提升的固定尾比刚性与中心 Type I 等价

## 1. 正向消元定理

固定核心素数

\[
p\equiv1\pmod {24},
\qquad 2\le n<p,
\qquad r=p-n,
\tag{1}
\]

并取

\[
D\in\mathcal D(p,n),
\qquad D\mid n^2,
\tag{2}
\]

其中 \(\mathcal D(p,n)\) 是
[D-only 标记正规形](two-denominator-lift-d-only-marked-normal-form.md)中的因子集合。令

\[
h=\frac{n^2}{D}.
\tag{3}
\]

因为 \(D<n^2\)，有 \(h>1\)。又由

\[
D\equiv np\pmod {4r}
\tag{4}
\]

以及 \((n,r)=(p,r)=1\)，先得到 \((D,r)=1\)。将 \(Dh=n^2\) 与 (4) 模
\(r\) 合并，并使用 \(p\equiv n\pmod r\)，可得

\[
h\equiv1\pmod r.
\]

所以

\[
k=\frac{h-1}{r}\in\mathbb N.
\tag{5}
\]

第二个 \(D\)-only 同余为

\[
\frac{(np)^2}{D}=p^2h\equiv np\pmod {4r}.
\tag{6}
\]

由于 \((p,4r)=1\)，消去 \(p\) 后得到 \(ph\equiv n\pmod {4r}\)。因此

\[
\lambda=\frac{ph-n}{4r}=\frac{pk+1}{4}\in\mathbb N,
\qquad
\boxed{4\lambda=pk+1}.
\tag{7}
\]

特别地，\(k\equiv3\pmod4\)、\(k\ge3\)，且

\[
(k,\lambda)=1
\tag{8}
\]

直接来自 \(4\lambda-pk=1\)。原 \(D\)-only 参数全部化为

\[
\boxed{
D=\frac{n^2}{h},\qquad
a=\frac{n\lambda}{h}=\frac{D\lambda}{n},\qquad
a'=p\lambda.}
\tag{9}
\]

标记非空判据中的量也同步简化为

\[
M=4a-n=Dk,
\qquad
S=na=D\lambda,
\qquad
g=(M,S)=D,
\tag{10}
\]

从而

\[
\boxed{\mu=k,\qquad\sigma=\lambda.}
\tag{11}
\]

## 2. 无冗余的反向参数化

反过来，固定正整数 \(k,\lambda\) 满足

\[
4\lambda=pk+1,
\tag{12}
\]

并取 \(2\le n<p\)。置

\[
h=4\lambda-nk=1+(p-n)k.
\tag{13}
\]

若且唯若满足以下两个整数条件

\[
\boxed{h\mid n^2,\qquad h\mid n\lambda,}
\tag{14}
\]

才可定义

\[
D=\frac{n^2}{h},
\qquad
a=\frac{n\lambda}{h}
\tag{15}
\]

并恢复一张 source-supported \(D\)-only 状态。事实上，由 \(h>1\) 有
\(0<D<n^2\)，而

\[
D-np=-4ra,
\qquad
\frac{(np)^2}{D}-np=p(ph-n)=4rp\lambda.
\tag{16}
\]

所以 \(D\in\mathcal D(p,n)\)，且 (9)--(11) 全部恢复。这个反向构造没有多余参数。

条件 \(h\mid n\lambda\) 不能从 \(h\mid n^2\) 删除。例如

\[
(p,n,k,\lambda,h)=(73,36,35,639,1296)
\]

满足 (12) 且 \(h=n^2\)，但 \(n\lambda/h=71/4\) 不是整数，因而不产生合法
\(D\)-only 状态。

## 3. 标记非空性就是原目标的中心 Type I 命中

由 (9) 有精确恒等式

\[
\boxed{
\frac4n-\frac1a
=\frac{k}{\lambda}
=\frac4p-\frac1{p\lambda}.}
\tag{17}
\]

定义固定图表的正尾集合

\[
\operatorname{Tail}(k,\lambda)=
\left\{(b,c)\in\mathbb N^2:
\frac1b+\frac1c=\frac{k}{\lambda}\right\}.
\tag{18}
\]

则 source-supported 标记集精确为

\[
W(p,n,D)=\{a\}\times\operatorname{Tail}(k,\lambda).
\tag{19}
\]

标准二尾因子化与 (11) 给出

\[
\operatorname{Tail}(k,\lambda)\ne\varnothing
\iff
\exists z>0:\quad
z\mid\lambda^2,\qquad z\equiv-\lambda\pmod k.
\tag{20}
\]

此时

\[
b=\frac{\lambda+z}{k},
\qquad
c=\frac{\lambda+\lambda^2/z}{k},
\tag{21}
\]

并且

\[
\frac4p=\frac1{p\lambda}+\frac1b+\frac1c.
\tag{22}
\]

式 (12) 正是同一素数的中心图表 \((R,K)=(k,\lambda)\)。若 (20) 中
\(z>\lambda\)，则互补因子 \(\lambda^2/z<\lambda\) 也满足同一个模 \(k\) 同余；
若 \(z<\lambda\) 则直接取 \(z\)。由于 \(k\ge3\)、\((k,\lambda)=1\)，不可能有
\(z=\lambda\)。所以 (20) 当且仅当存在规范中心除子

\[
d\mid\lambda^2,\qquad d<\lambda,\qquad
d\equiv-\lambda\pmod k.
\tag{23}
\]

因此得到严格等价链

\[
\boxed{
W(p,n,D)\ne\varnothing
\iff
\operatorname{Tail}(k,\lambda)\ne\varnothing
\iff
(k,\lambda)\text{ 中心 Type I 命中}.}
\tag{24}
\]

## 4. 固定尾比链的非推进定理

固定 \((p,k,\lambda)\) 后，让 \(n\) 遍历所有满足 (13)--(14) 的较小秩，并按
(15) 定义各自的 \(D_n,a_n\)。所有这些标记集的第一坐标虽然不同，但其尾投影严格相同：

\[
W(p,n,D_n)=\{a_n\}\times\operatorname{Tail}(k,\lambda).
\tag{25}
\]

任何只替换 distinguished coordinate、保持同一有序尾对 \((b,c)\) 的边，都是这些
集合之间在尾投影上的恒等双射。因此：

1. 若 (23) miss，则这整个固定图表类中的标记集全部为空；
2. 若 (23) hit，则 (20)--(22) 已经给出原 \(p\) 的直接 Type I 终端；
3. 即使 \(n\) 沿链严格下降，也没有降低真正的存在性核心
   \(\operatorname{Tail}(k,\lambda)\ne\varnothing\)。

所以 source-supported、固定 \((p,k,\lambda)\)、固定被替换坐标的同类 \(D\)-only
迭代不能提供新的 marked 非空闭包。这个结论不排除改变保留尾、旋转被替换坐标、切换
图表、Type II 或 support switch；恰恰相反，下一条有证明增量的 E4 边必须改变
既约尾比 \(k/\lambda\) 或离开双尾恒等类。

## 5. 两个精确边界

正例

\[
(p,n,D)=(73,33,9)
\]

给出

\[
(h,k,\lambda,a,a')=(121,3,55,15,4015).
\]

取 \(z=11\) 得 \((b,c)=(22,110)\)，所以

\[
(15,22,110)\longmapsto(4015,22,110).
\]

透明的空标记例为

\[
(p,n,D)=(73,64,64),
\qquad
(h,k,\lambda,a,a')=(64,7,128,128,9344).
\]

这里 \(z\mid128^2=2^{14}\) 的模 \(7\) 剩余只能是 \(1,2,4\)，而
\(-128\equiv5\pmod7\)。所以中心图表 miss，且 \(W(73,64,64)=\varnothing\)。

## 6. 证明边界与聚焦复现

本卡完成的是 source-supported 子类的消元与否定性分类，不是一般 \(D\)-only 状态的
全称分类。若 \(D\nmid n^2\)，不能引入整数 \(h=n^2/D\)，本定理不适用。

聚焦核验入口为

~~~bash
python3 reproductions/two_denominator_lift_source_supported_tail_rigidity.py
python3 reproductions/two_denominator_lift_source_supported_tail_rigidity.py --verify
~~~

结果文件为

~~~text
reproductions/two-denominator-lift-source-supported-tail-rigidity-results.json
~~~
