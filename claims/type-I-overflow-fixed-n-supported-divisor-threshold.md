---
kind: claim
claim_id: type-I-overflow-fixed-n-supported-divisor-threshold
title: overflow 保持支撑的 fixed-n 折叠的最小素因子阈值与粗糙残余
statement: >-
  设 verified overflow 满足 pn=4Md+1、M=Ab、1<=d<p，并携带
  1<=A<=B_p=(p-1)^2/4 的 charged support。令 H=floor(B_p/A)，并约定
  spf(1)=infinity。则在既有 fixed-n 商模 p 折叠合同（其目标 support 定为折叠
  载体 L）内，所有保持旧 support 的折叠载体恰为 L=At，其中 t|bd、2<=t<=H；
  故这类完整 E1--E5 边存在当且仅当
  spf(bd)<=H，规范选择为 t=spf(bd)。若 d>1 而该菜单为空，则 bd 是 H-rough、
  d>=H+1，且必有 A>(p-1)/4。若还满足 M>B_p，则
  n>=nu_min(H+1,p-2)(p) 的既有高载体高度下界。因而 A>1 overflow 的
  fixed-n 保支撑残余不再是一般因子搜索，而是一个显式的高支撑粗糙数族；它不排除
  paid support reset、fixed-s、总余因子投影、直接终端或其它全局出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-fixed-n-quotient-fold-descent
  - type-I-overflow-high-carrier-height-staircase
  - type-I-overflow-total-cofactor-canonical-projection-persistence-rank
topics:
  - type-I
  - overflow
  - fixed-n
  - quotient-fold
  - charged-support
  - least-prime-factor
  - roughness
  - high-support
  - denominator-height
  - well-founded-descent
  - proof-boundary
sources:
  - claim: type-I-overflow-fixed-n-quotient-fold-descent
    role: complete-E1--E5-quotient-fold-contract
  - claim: type-I-overflow-high-carrier-height-staircase
    role: high-carrier-denominator-lower-bound
  - claim: type-I-overflow-total-cofactor-canonical-projection-persistence-rank
    role: strict-total-fold-and-persistence-boundary
  - reproduction: reproductions/type_i_overflow_fixed_n_supported_divisor_threshold.py
    role: focused-positive-and-rough-residual-receipts
visibility: public
last_checked: '2026-08-12'
---

# overflow 保持支撑的 fixed-\(n\) 折叠的最小素因子阈值与粗糙残余

## 设置

固定核心素数

\[
p\equiv1\pmod {24},
\qquad
B_p=\frac{(p-1)^2}{4}.
\tag{1}
\]

设一个已有 source/path/node 回执的 verified overflow 满足

\[
pn=4Md+1,
\qquad
M=Ab,
\qquad
1\le d<p,
\qquad
1\le A\le B_p.
\tag{2}
\]

这里 \(A\mid M\) 是当前 charged support，\(b=M/A\) 是余因子。记

\[
H:=\left\lfloor\frac{B_p}{A}\right\rfloor,
\qquad
\operatorname{spf}(x):=\text{\(x>1\) 的最小素因子},
\qquad
\operatorname{spf}(1):=\infty.
\tag{3}
\]

以下仅讨论既有 `overflow_fixed_n_quotient_fold_outer_rank_v1` 合同中的
**保持旧 support** 分支：目标 charged support 被定义为折叠载体 \(L\)，因而
\(A\mid L\)。这不是对未来所有可能 target-support 语义的分类，也不是把 \(A\)
丢弃后另行支付 reset 的分支。

## 精确候选集

令

\[
\mathcal F_{p,M,d;A}:=
\left\{
L:\ L\mid Md,\ A\mid L,\ A<L\le B_p,
\left\lfloor\frac{B_p}{L}\right\rfloor
<
\left\lfloor\frac{B_p}{A}\right\rfloor
\right\}.
\tag{4}
\]

那么有完全显式的恒等式

\[
\boxed{
\mathcal F_{p,M,d;A}
=
\{At:\ t\mid bd,\ 2\le t\le H\}.
}
\tag{5}
\]

事实上，\(A\mid L\) 唯一写成 \(L=At\)。由 \(Md=Abd\)，

\[
At\mid Md
\quad\Longleftrightarrow\quad
t\mid bd.
\tag{6}
\]

又 \(A<L\le B_p\) 等价于 \(2\le t\le H\)。剩余的严格 outer-rank
条件在这里是自动的。令 \(x=B_p/A\)，则 \(\lfloor x\rfloor=H\)。若
\(t\ge2\) 且 \(\lfloor x/t\rfloor\ge H\)，便有

\[
x\ge tH\ge2H\ge H+1,
\tag{7}
\]

这与 \(x<H+1\) 矛盾。因此

\[
\left\lfloor\frac{B_p}{At}\right\rfloor
<
\left\lfloor\frac{B_p}{A}\right\rfloor.
\tag{8}
\]

式 (5) 不再需要旧的正窗口 \(4L>n\)：商模 \(p\) 折叠已经处理全部长商。

## 最小素因子判据与规范边

因为任一大于一的 \(bd\) 除子的最小者正是 \(\operatorname{spf}(bd)\)，(5) 立刻给出

\[
\boxed{
\mathcal F_{p,M,d;A}\ne\varnothing
\quad\Longleftrightarrow\quad
\operatorname{spf}(bd)\le H.
}
\tag{9}
\]

当 (9) 成立时，取规范因子

\[
t_0=\operatorname{spf}(bd),
\qquad
L_0=At_0.
\tag{10}
\]

写

\[
\frac{bd}{t_0}=ph+\delta,
\qquad
h\ge0,
\qquad
1\le\delta<p.
\tag{11}
\]

由[固定-\(n\) 商模 \(p\) 折叠的完整外层秩递降](type-I-overflow-fixed-n-quotient-fold-descent.md)，

\[
(M_T,d_T,n_T;A_T)
=
(L_0,\delta,n-4L_0h;L_0)
\tag{12}
\]

是完整 E1--E5 的边：\(A\mid A_T\)，解提升仍是
\(\operatorname{Sol}(p)\) 上的恒等映射，而 (8) 严格支付 outer rank。
所以 (9) 是这个既有、目标 support 等于 \(L\) 的**全部保持支撑 fixed-\(n\)
折叠菜单**的存在性充要条件，而非一个只对正窗口有效的充分条件。

## 空菜单的粗糙残余与高度压缩

现在假设 \(d>1\) 且 (9) 失败。则

\[
\operatorname{spf}(bd)>H.
\tag{13}
\]

因此 \(b\) 与 \(d\) 的每一个素因子都大于 \(H\)，特别地

\[
\boxed{d\ge H+1.}
\tag{14}
\]

这个失败不可能发生在低 support。令

\[
c:=\frac{p-1}{4}.
\tag{15}
\]

若 \(A\le c\)，则 \(H\ge B_p/c=p-1\)。但 \(d>1\)、\(d<p\) 蕴含

\[
\operatorname{spf}(bd)\le\operatorname{spf}(d)\le d\le p-1\le H,
\tag{16}
\]

与 (13) 矛盾。故

\[
\boxed{d>1\ \text{且}\ \mathcal F_{p,M,d;A}=\varnothing
\quad\Longrightarrow\quad A>c.}
\tag{17}
\]

若进一步 \(M>B_p\)，则已有高载体高度阶梯可应用。由于 (14)、(17) 给出
\(H\le p-2\)，令

\[
j:=\min(H+1,p-2).
\tag{18}
\]

便有 \(d\ge j\)，从而

\[
\boxed{
n\ge \nu_j(p)
=j(p-2)+1+[j]_4.
}
\tag{19}
\]

这里 \([j]_4\) 是 \(j\) 模 \(4\) 的最小非负剩余。因而在高载体、\(d>1\)
分支中，无法作保持支撑 fixed-\(n\) 折叠并不是一般的“因子间隙”：它只能位于

\[
A>c,
\qquad
\operatorname{spf}(bd)>\left\lfloor\frac{B_p}{A}\right\rfloor,
\qquad
n\ge\nu_{\min(H+1,p-2)}(p).
\tag{20}
\]

这是一张显式的高支撑、\(H\)-rough、高分母残余地图。

## 与整体余因子投影的交界

式 (20) 只关闭保持旧 support 的 bounded fixed-\(n\) 菜单；它不应被误写为
全局无出口。设

\[
C:=p-d,
\qquad
\frac KA=bC.
\tag{21}
\]

在 source 是真实 persistent state、并且既有 typed total-cofactor adapter 的
persistence 门通过时，整体余因子投影的严格门恰为

\[
bC>p.
\tag{22}
\]

若 (22) 失败，\(p\nmid K/A\) 排除等号 \(bC=p\)，故

\[
bC<p.
\tag{23}
\]

此时 source 已是 support \(A\) 的 canonical projection；更精确地，若
\(C_A=\langle(4A)^{-1}\rangle_p\)，则 \(bC=C_A\)。所以在已经通过
persistence/typed 门的真实状态上，两个菜单同时不能严格下降的残余还必须满足

\[
\boxed{
A>c,
\quad \operatorname{spf}(bd)>H,
\quad d\ge H+1,
\quad b(p-d)=C_A<p.
}
\tag{24}
\]

这是一个精确的后续目标 normal form，不是完整的全局出口证明。

两个先前仅用于说明 bounded-divisor atlas 会空的算术控制，其实在 (22) 上都严格：

\[
\begin{array}{c|c|c|c}
p&A&b(p-d)&C_A\\ \hline
73&293&420&55\\
673&821&6838&108
\end{array}
\tag{25}
\]

相应 total-fold 余量分别为 \((420-55)/73=5\) 与
\((6838-108)/673=10\)。这些行仍没有 source/path 可达性断言，因此 (25) 只说明：
一旦未来的 persistent typed adapter 接纳同类来源，它们不是 (24) 的算术残余，不能
继续被当作全局选择器的硬反例。

## 有界合同的支撑饱和边界与无界闭合

同图表支撑升级已经严格关闭所有真实 persistent overflow 中 \(M>A\) 的行；因此，
在该边可以调用后，仍可能需要单独处理的 fixed-\(n\) 支撑保留分支只能有

\[
\boxed{M=A.}
\tag{26}
\]

这并不使 (9) 自动成立。此时 \(b=1\)，所以若 \(d>1\) 且 (9) 失败，便有

\[
\operatorname{spf}(d)>H,
\qquad
d\ge H+1.
\tag{27}
\]

既有商折叠合同唯一自然会尝试取完整因子 \(L=Ad=Md\)，其商为 \(1\)，从而会
算术上产生 \(d_T=1\)。但是 (27) 给出

\[
\boxed{L=Ad\ge A(H+1)>B_p,}
\tag{28}
\]

其中严格性来自 \(d\ge H+1\) 与 \(B_p<A(H+1)\)。故该载体**不在**当前
`overflow_fixed_n_quotient_fold_outer_rank_v1` 的有界、外层秩付费域中；不能把
“完整因子折到 \(d_T=1\)”误登记成现有 verified edge。

这种边界同时真实发生在两种 typed 类别中，而不只是某一 G 相位。以下是纯算术
normal-form 控制（不声称来源可达）：

\[
\begin{array}{c|c|c|c|c|c|c|c}
p&A&H&C=p-d&d&n&R&\text{target class}\\ \hline
73&97&13&54&19&101&287& G\\
73&56&23&44&29&89&135& F\\
97&79&29&66&31&101&215& G\\
97&70&32&44&53&153&127& F
\end{array}
\tag{29}
\]

四行均满足 \(pn=4Ad+1\)、\(R=4A-n>p\)、\(A\mid K=A(p-d)\)、
\(\operatorname{spf}(d)>H\)，并且 \(Ad>B_p\)。G 行的支撑子群不含 \(-1\)，
F 行的支撑子群含 \(-1\) 但中心盒内无命中。因而支撑饱和粗糙 normal form 既不能
由“它一定是 G”排除，也不能由“它一定已有 F witness”排除。

以上 no-go 的价值也必须精确表述：它只否定当前
`overflow_fixed_n_quotient_fold_outer_rank_v1` 的**有界**载体域，不能否定 charged
state contract 允许的无界 support。事实上，完整乘积 \(L=Md\) 的商恒为 \(1\)。在
真实 persistent source 与 typed target adapter 的准入前提下，[无界完整乘积商折叠]
(type-I-overflow-unbounded-full-product-quotient-fold.md) 以

\[
(M_T,d_T,n_T;A_T)=(Md,1,n;Md)
\tag{30}
\]

把每个 \(M=A,d>1\) 的 (27) 行送到严格 paid outer-rank target；虽然
\(Ad>B_p\)，但 \(\lfloor B_p/(Ad)\rfloor<\lfloor B_p/A\rfloor\)。因此 (29) 的四行
现在是新分支的正控制，而不是全局选择器的算术反例。

完整乘积支路唯一没有严格 support 增长的情况是 \(bd=1\)，亦即
\(M=A,d=1\)。这才是该支路保留下来的 sharp d=1 边界；它仍需要已有的 d=1 G
重图表、非支撑 Type I/II 终端或高支撑出口，不能由本有界阈值卡单独关闭。

## 聚焦复现

```bash
python3 reproductions/type_i_overflow_fixed_n_supported_divisor_threshold.py --verify
```

回执只重算两个规范保支撑折叠、两个 \(H\)-rough 空菜单控制、它们的高度下界以及
total-fold 算术余量，另核验四个支撑饱和 F/G normal-form 边界；不进行历史范围扫描。
