---
kind: claim
claim_id: type-I-root-capacity-stutter-m-three-biquadratic-norm-reduction
title: actual proper-root stutter 的 m=3 双二次范数约化
statement: >-
  对核心素数 p≡1 mod24 的 terminal-first 后 actual proper-root stutter receipt，若
  m=3，写 h=3u、a=3A，则 e=u+A，且
  D=(3u^2-u+1)/A、p=(D+3u-1)/3。这里 gcd(A,u)=1、A≡3 mod24、
  A≥27、u≥2A+6，并同时有 A|(3u^2-u+1) 与 u|(7A^2+A+1)。令
  r=(7A^2+A+1)/u，则 k=(u+r-A-2)/3。等价地，这一分支同时落在
  discriminant -11 与 -27 的两条正定二次范数方程上。进一步令
  B=(e-1)/3、k=3 kappa，则 gcd(a,e-1)=3、kappa≡7 mod24，且每个
  固定 kappa 的 primitive fiber 满足 A|9(27 kappa^2+8 kappa+1)。特别地
  actual m=3 receipt 必有 k≡21 mod72、k≥93 与 W-eta≥13。若
  d=(W-eta,k)，则 d|(p^2-p+1)、gcd(d,h(p^2+p+1)D)=1，且其 natural gap
  s_d 满足 d|(s_d^2+s_d+1)。若 d>1，则其 natural fan cofactor 必有 C_d>=40，且
  natural gap 满足 s_d<=(p-40)/39。若进一步 s_d=3，则 d=13，且 whole-d
  primitive quotient q=n/d 必满足 q≡13 mod24、q>=2893，且其 primitive coordinates
  满足
  tau>sigma（等价于 W-eta>eta+1）与 A<rho。
  所以 d 是 Phi_6(p) carrier，不是 root-height
  Phi_3(p) carrier。kappa 有一个 canonical q≡7 mod12 素因子；它确定地落入
  q|u 的 root-supported、q|d 的 Phi_6 cancellation，或两者皆不整除的 primitive
  quotient-only residual 三类之一。在 terminal-first 的 m=3 slice 中，5|D* 当且仅当
  v_5(3u^2-u+1)>=v_5(A)+2；这强制 p≡11、h≡9、u≡3 (mod 25)，且若该 5-residual
  高于最小层或进入 complete-excess multiplier，则原始 root 坐标为 11 (mod 25)。
  在唯一 minimal leaf 中，L_5=D_*/5 含有非 5 的 pure-T carrier；但其任一非平凡
  除子均不能命中 general-A_0 positive whole-divisor Type II terminal fan。
  其中每个 pure-T 素因子也不能进入 reflected negative ray。
  对任意真因子 1<J|L_5，D/J 虽给出严格的 formal cofactor，却不可能是同一
  (A,K,R-h) 的 canonical maximal receipt；L_5 的素因子因而严格分成已有
  endpoint q-excess（可重放 raw child，但无 persistent E1 root-policy）与容量内
  饱和两类。前一类的一步 raw deflation 精确给出 strict support cofactor
  \(p-\ell\)。更精确地，该 child 在 complete-excess 意义下必精确分流为单侧
  bundle，或两个 p-free 完整超额块的 atomic split；后者的 high-support rank
  stutter 恰等价于另一侧 multiplier \(F_y\equiv\ell\pmod p\)。这仍不能以因子删除
  冒充 E1 rebase；若该 stutter 出现，其 canonical residual \(D_y\) 还必须同时通过
  两个 root-receipt divisor gate 和一个显式模 \(p\) 同余。上述结果仍不支付 persistent
  provenance、priority 或 typed target。
  更一般地，m=3 的 D 因子不命中 native raw Type II menu。
  该约化不证明这些互锁 divisor fibers 为空，不构造
  terminal 或 E1--E5 successor，也不闭合 QC1、TR1 或 T6。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-finite-curve-constraint
  - type-I-root-capacity-stutter-actual-small-root-exclusion
  - type-I-root-capacity-stutter-positive-definite-norm-bound
  - type-I-root-capacity-stutter-complementary-eisenstein-coordinate-gap
  - type-I-root-capacity-stutter-eisenstein-support
  - type-I-root-capacity-stutter-primitive-quotient-normalization
  - type-I-root-capacity-stutter-transverse-residual-capacity-map
  - type-I-root-capacity-stutter-transverse-root-residue-low-gap-descent
  - type-I-root-capacity-stutter-transverse-overlap-valuation-alignment
  - type-I-root-capacity-stutter-transverse-overlap-complete-excess-valuation-classification
  - type-I-root-capacity-stutter-c-side-m-localization
  - type-I-root-capacity-stutter-transverse-composite-divisor-positive-quadratic-type-II-fan
  - type-I-root-capacity-stutter-transverse-native-raw-type-II-menu
  - type-I-root-capacity-stutter-transverse-negative-branch-bezout-reflection-terminal
  - type-I-root-capacity-strict-carry-support-rebase
  - type-I-root-capacity-strict-carry-universal-raw-word-policy-boundary
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
  - type-I-path-anchored-atomic-split-complete-excess-admission
topics:
  - type-I
  - root-capacity
  - stutter
  - m-three
  - quadratic-norm
  - divisor-fiber
  - eisenstein-quotient
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-finite-curve-constraint
    role: actual-stutter-linear-identities
  - claim: type-I-root-capacity-stutter-actual-small-root-exclusion
    role: actual-mod-three-parity-and-low-coefficient-bounds
  - claim: type-I-root-capacity-stutter-complementary-eisenstein-coordinate-gap
    role: complementary-gap-whole-d-identities-and-natural-fan-bounds
  - claim: type-I-root-capacity-stutter-eisenstein-support
    role: oddness-of-the-actual-Eisenstein-quotient
  - claim: type-I-root-capacity-stutter-primitive-quotient-normalization
    role: common-factor-normalization-and-primitive-system
  - claim: type-I-root-capacity-stutter-transverse-residual-capacity-map
    role: actual-D-star-to-original-root-coordinate-interface
  - claim: type-I-root-capacity-stutter-transverse-root-residue-low-gap-descent
    role: terminal-first-positive-q-equals-five-pruning
  - claim: type-I-root-capacity-stutter-transverse-overlap-valuation-alignment
    role: p-minus-one-overlap-excess-height
  - claim: type-I-root-capacity-stutter-transverse-overlap-complete-excess-valuation-classification
    role: p-minus-one-minimal-leaf-complete-excess-classification
  - claim: type-I-root-capacity-stutter-c-side-m-localization
    role: exact-C-side-versus-T-side-carrier-split-at-m-equals-three
  - claim: type-I-root-capacity-stutter-transverse-composite-divisor-positive-quadratic-type-II-fan
    role: whole-divisor-positive-ray-terminal-conditions
  - claim: type-I-root-capacity-stutter-transverse-native-raw-type-II-menu
    role: native-raw-ray-terminal-conditions
  - claim: type-I-root-capacity-stutter-transverse-negative-branch-bezout-reflection-terminal
    role: reflected-negative-ray-terminal-conditions
  - claim: type-I-root-capacity-strict-carry-support-rebase
    role: canonical-receipt-required-for-a-real-support-rebase
  - claim: type-I-root-capacity-strict-carry-universal-raw-word-policy-boundary
    role: actual-root-endpoint-raw-occurrence-without-persistent-E1-policy
  - claim: type-I-bottom-sink-scc-complete-excess-bundle-selector
    role: complete-excess-lcm-support-and-high-support-rank-admission
  - claim: type-I-path-anchored-atomic-split-complete-excess-admission
    role: two-sided-complete-excess-arithmetic-kernel-and-exact-rank-gate
visibility: public
last_checked: '2026-08-19'
---

# actual proper-root stutter 的 \(m=3\) 双二次范数约化

## 1. 范围

固定一个 terminal-first 后仍未终止的 actual proper-root stutter receipt：

\[
p\equiv1\pmod {24},\qquad h=3u<p,\qquad 3\nmid u,
\]

\[
a=em-h,\qquad pa+(e-1)=eh,
\qquad a^2-a(e-1)+(e-1)^2=hk,
\]

并额外假设

\[
\boxed{m=3.}
\tag{1}
\]

本卡只约化这个固定 \(m\) slice。所有 `actual`、maximal-receipt、terminal-first 和
source/path 前提都保留；反过来，下面的整数方程本身不恢复这些回执条件。

## 2. 精确坐标重写

actual 的模 \(3\) 分流在 \(m\equiv0\pmod3\) 时给出 \(3\mid a\)。写

\[
a=3A,\qquad h=3u.
\tag{2}
\]

由 \(a=3e-h\) 立刻得到

\[
\boxed{e=u+A.}
\tag{3}
\]

令 \(D=mp+1-h=3p+1-3u\)。将 (2)--(3) 代入
\(pa+(e-1)=eh\)，得到

\[
3Ap=3u^2+3Au-u-A+1.
\tag{4}
\]

将右边拆成 \((3u^2-u+1)+A(3u-1)\)，便有

\[
\boxed{
AD=3u^2-u+1,
\qquad
3p=D+3u-1.
}
\tag{5}
\]

因此 \(m=3\) 的全部整数曲线条件先压成

\[
\boxed{
A\mid3u^2-u+1,
\qquad
D=\frac{3u^2-u+1}{A},
\qquad
p=u+\frac{D-1}{3}.
}
\tag{6}
\]

原来的 \(eD=ph+1\) 在这些坐标中也可直接重放：

\[
ph+1=u(D+3u-1)+1
=uD+(3u^2-u+1)=(u+A)D=eD.
\tag{7}
\]

这说明 (5) 不是丢弃 \(D\)-receipt 的形式重参数化，而是原始两个线性 stutter
等式在 \(m=3\) 的精确合并。

## 3. cyclotomic 根条件给出的第二除子门

由 (7)，任何同时整除 \(e\) 与 \(h\) 的素数也会整除 \(ph+1\)，而后者模该素数
为 \(1\)。所以 \((e,h)=1\)。结合 (3) 和 \(h=3u\)，得到

\[
\boxed{(A,u)=1.}
\tag{8}
\]

在模 \(u\) 下，(5) 给出 \(AD\equiv1\)，且
\(3p\equiv D-1\)。因为 \(3A\) 在模 \(u\) 下可逆，

\[
p\equiv\frac{1-A}{3A}\pmod u.
\tag{9}
\]

将其代入 \(u\mid p^2+p+1\)，再乘以 \(9A^2\)，得到

\[
\boxed{u\mid7A^2+A+1.}
\tag{10}
\]

反过来，若 (5) 使 \(p\) 为整数、\((A,u)=1\)、\(3\nmid u\)，并且 (10) 成立，
则 (9) 的同一计算反向给出 \(u\mid p^2+p+1\)。在额外保留
\(p\equiv1\pmod3\) 时，便恢复 \(3u\mid p^2+p+1\)。所以 (5) 和 (10) 是
这个 slice 的两条精确算术 divisor gates，而非只取其一的必要筛选。
特别地，固定 \(A\) 时，\(u\) 必为 \(7A^2+A+1\) 的正除子；固定 \(u\) 时，
\(A\) 必为 \(3u^2-u+1\) 的正除子。这给出双向的有限 divisor fiber，而不是
对 \(p\) 或分母的范围扫描。

## 4. actual proper-root 范围

actual 根端点使 \(a\) 为奇数，故 \(A\) 为奇数。既有低系数排除给出
\(a(m-1)\ge30\)，于是

\[
\boxed{A\ge5.}
\tag{11}
\]

另一方面，互补坐标满足

\[
\eta=e-1-a=u-2A-1\ge5,
\]

所以

\[
\boxed{u\ge2A+6.}
\tag{12}
\]

proper-root 的 \(h<p\) 与 (5) 等价于

\[
D>6u+1.
\tag{13}
\]

故

\[
A=\frac{3u^2-u+1}{D}
<\frac{3u^2-u+1}{6u+1}<\frac u2.
\tag{14}
\]

式 (12) 比 (14) 更强，但 (13)--(14) 显示这个小 \(m\) slice 的 `D` carrier
仍然处在严格的 \(u\)-尺度之外。最后，\(D=3p+1-3u\equiv1\pmod3\)，
而 \(eD=ph+1\equiv1\pmod3\)，所以

\[
\boxed{u+A=e\equiv1\pmod3.}
\tag{15}
\]

## 5. 两个范数与 quotient 大小

定义第二个整数商

\[
r:=\frac{7A^2+A+1}{u}.
\tag{16}
\]

将 (2)--(3) 代入 Eisenstein 范数，可得

\[
\begin{aligned}
hk
&=9A^2-3A(u+A-1)+(u+A-1)^2\\
&=u^2-Au-2u+7A^2+A+1\\
&=u(u+r-A-2).
\end{aligned}
\]

因此

\[
\boxed{k=\frac{u+r-A-2}{3}.}
\tag{17}
\]

这两个 gate 也有自然的二次范数解释。令

\[
\omega_{11}^2-\omega_{11}+3=0,
\qquad
\vartheta_{27}^2-\vartheta_{27}+7=0.
\]

相应范数分别为

\[
N_{11}(x+y\omega_{11})=x^2+xy+3y^2,
\qquad
N_{27}(x+y\vartheta_{27})=x^2+xy+7y^2.
\]

于是 (5) 和 (10) 精确成为

\[
\boxed{
AD=N_{11}(1-u\omega_{11}),
\qquad
ur=N_{27}(1+A\vartheta_{27}).
}
\tag{18}
\]

它们的判别式分别为 \(-11\) 与 \(-27\)。例如，对任一不等于 \(11\) 的奇素数
\(q\mid D\)，(5) 表明 \(-11\) 是模 \(q\) 的平方；等价地
\[
\left(\frac{-11}{q}\right)=\left(\frac q{11}\right)=1,
\]
所以 \(q\bmod11\) 是二次剩余。这个局部限制并不自动给出 Type I/II certificate，但它把
\(m=3\) 的 transverse carrier 从一般因子问题变成一对互锁的二次范数问题。

## 6. 与 Eisenstein difference carrier 的严格分离

令

\[
\mathfrak d=(W-\eta,k),
\qquad g=(D,\mathfrak d).
\]

已有的 shifted-resultant identity 给出 \(g\mid\chi(m)\)，其中

\[
\chi(X)=X^4-6X^3+12X^2-9X+3.
\]

在本卡的 \(m=3\) slice，\(\chi(3)=3\)。另一方面
\(3\nmid\mathfrak d\)。故

\[
\boxed{(D,\mathfrak d)=1.}
\tag{19}
\]

因此非平凡 Eisenstein difference carrier 即使存在，也不会经由 \(D\) 转化成已经有
actual receipt provenance 的 transverse carrier。这一分离解释了为什么把 factor-level
quotient cancellation 直接重命名为 \(D_*\)-edge 在本 slice 中不可能成立。

此外，\(D(p+e)=3p^2+p+1\)，所以 \(D\) 的 native polynomial 是

\[
3X^2+X+1,
\qquad \operatorname{disc}=-11.
\tag{20}
\]

它在 \(\mathbb Q\) 上不可约。现有 even-\(K\) terminal fan 使用的是
\(K(K-1)X^2-X-1\) 的整数线性因子分解；它不能把 (20) 作为同一个
linear-factor instance。这个结论只排除该既有 factorization mechanism 的直接套用，
不排除某个 \(D\) 因子额外命中其它 terminal menu。

### 6.1 \(m=3\) transverse overlap 的精确二分

本节需要明确区分两个不同坐标。令 \(\varrho\) 为 root-capacity 的原始参数，

\[
u=\gcd(2\varrho+1,M_0),
\qquad
M_0=\frac{p^2+p+1}{3},
\]

而 (16) 的

\[
r_{27}=\frac{7A^2+A+1}{u}
\]

只是 \(-27\) 范数门的商。下述结论**不**把 \(\varrho\) 与 \(r_{27}\) 识别。

令

\[
D_H=(D,h^2-1),
\qquad
D_*=\frac{D}{D_H}.
\tag{20a}
\]

在 \(m=3\) 时 \(D=3p+1-h\)。因为 \(p,h\) 都是奇数且 \(3\mid h\)，有

\[
D\ \text{为奇数},
\qquad
D\equiv1\pmod3.
\tag{20b}
\]

置 \(b_-=(D,h-1)\)、\(b_+=(D,h+1)\)。直接模 \(b_-\)、\(b_+\) 重放
\(D=3p+1-h\) 与 \(D\mid ph+1\)，分别得到

\[
b_-\mid3,
\qquad
b_+\mid5.
\tag{20c}
\]

由 (20b)，\(b_-=1\)；又 \(D\) 为奇数，所以 \(D_H=b_+\)。因此

\[
\boxed{D_H\in\{1,5\}.}
\tag{20d}
\]

更精确地，

\[
\boxed{
D_H=5
\quad\Longleftrightarrow\quad
p\equiv1\pmod5,\quad u\equiv3\pmod5.}
\tag{20e}
\]

事实上，若 \(5\mid(D,h+1)\)，则 \(3u=h\equiv-1\pmod5\)，故
\(u\equiv3\pmod5\)；再由 \(D=3p+1-3u\) 得 \(p\equiv1\pmod5\)。
反向代入这两个同余便有 \(5\mid(D,h+1)\)，再用 (20d) 即得。

proper-root 条件 \(h<p\) 还给出

\[
D-(2p+1)=p-h>0.
\tag{20f}
\]

因此

\[
\boxed{
D_*>\frac{2p+1}{5};
\qquad
D_H=1\Longrightarrow D_*>2p+1.}
\tag{20g}
\]

横向 residual capacity map 的真正接口是

\[
D_*\mid m+2\varrho=2\varrho+3.
\tag{20h}
\]

结合 (20g)，得到实际 root 坐标的高区下界

\[
\boxed{
\varrho>\frac{p-7}{5};
\qquad
D_H=1\Longrightarrow\varrho\ge p.}
\tag{20i}
\]

这是一条 actual transverse scale/orientation 结论。它没有给出 \(D_*\) 的 terminal
residue、source consumption、全域 lift 或 T5 ticket，因而不构成 TR1；其作用是排除把
\(r_{27}\) 代入 (20h) 的错误，并把未来的 adapter 限定在真实高-root 输入上。

### 6.2 \(m=3\) 的 general-\(A_0\) low-gap factor gate 已完全分类

这里的 \(A_0\) 是 Type II raw-ray 的参数，不是本卡的 stutter 坐标 \(A\)。令

\[
\mathcal G=\{3,7,11,23\},\qquad
F_s^+=sh-1,\qquad F_s^-=s(h-1)+1,
\]

先取已有 root-residue low-gap adapter 的任一**正根**输入：\(A_0\mid p+3\) 为奇数，
\(q\mid D_*\) 是奇素数、\(q\nmid A_0\)，且其 root residue
\(K=\langle A_0h\rangle_q\) 满足该 adapter 的条件

\[
q+A_0=sK,\qquad s\in\mathcal G,
\qquad s\equiv3\pmod {4A_0}.
\tag{20j-0}
\]

因该 adapter 还要求 \(K>A_0\)，有
\(q=sK-A_0\ge s(A_0+1)-A_0>s\)。由 \(K\equiv A_0h\pmod q\) 与 (20j-0)，有

\[
q\mid A_0(sh-1),
\qquad\text{从而}\qquad q\mid F_s^+.
\tag{20j-1}
\]

这一步对任意允许的 \(A_0\) 都成立，不把它限制为 \(1\)。下文还会处理同一
general-\(A_0\) quadratic fan 的 negative linear factor 在这个 low-gap 形状下的情形。

确实，令

\[
\Delta_s=3s^2-s+1.
\]

有限曲线恒等式 \(Da=3+h(h-1)\) 给出

\[
\Delta_s+F_s^+F_s^-=s^2Da.
\tag{20j}
\]

因为 \(q\mid D_*\mid D\) 且 \(q>s\)，(20j-1) 的正根命中强制
\(q\mid\Delta_s\)。四个固定整数分解为

\[
\Delta_3=25,\qquad
\Delta_7=141=3\cdot47,\qquad
\Delta_{11}=353,\qquad
\Delta_{23}=1565=5\cdot313.
\tag{20k}
\]

其中 \(353\) 与 \(313\) 都是素数（分别只需试除不超过 \(17\) 的素数）。条件
\(s\equiv3\pmod {4A_0}\) 在 \(s=3,7,11,23\) 时分别只允许
\(A_0\) 为任意奇数、\(1\)、\(1\)、或 \(1,5\)。逐项再用
\(q+A_0\equiv0\pmod s\)：当 \(s=7\) 时 \(3+1,47+1\) 都不被 \(7\)
整除；当 \(s=11\) 时 \(353+1\) 不被 \(11\) 整除；当 \(s=23\) 时
\(A_0=1\) 给出 \(5+1,313+1\not\equiv0\pmod {23}\)，而 \(A_0=5\) 时
\(q\nmid A_0\) 排除 \(q=5\)，且 \(313+5\not\equiv0\pmod {23}\)。因此

\[
\boxed{\text{任一 positive low-gap root-residue 输入都满足 }(s,q)=(3,5).}
\tag{20l}
\]

若 \(5\mid F_3^+=3h-1\)，则
\(h\equiv2\pmod5\)。又 \(5\mid D\) 与 \(D=3p+1-h\) 给出
\(p\equiv2\pmod5\)。因为 \(5\nmid A_0\)、\(A_0\mid p+3\)，令

\[
C=\frac{p+3}{20A_0},
\qquad
K=\frac{A_0+5}{3}.
\]

因为 \(p\equiv1\pmod4\)，\(C\) 是正整数；\(K\) 则由 (20j-0) 给出。已有正根
构造在这里具体成为

\[
\boxed{
\frac4p=
\frac1{5A_0C}+
\frac1{pA_0CK}+
\frac1{5pCK}.}
\tag{20m}
\]

所以 terminal-first 后不可能保留任何允许 \(A_0\) 的 positive low-gap gate。

再取同一 general-\(A_0\) quadratic fan 的一个 low-gap **negative** specialization。
这次不假设正根的 \(K=\langle A_0h\rangle_q\)：令 \(A_0\mid p+3\) 为奇数，
\(K>A_0\) 为偶数、\((A_0,K)=1\)，\(q\mid D_*\) 为奇素数，并满足

\[
q+A_0=sK,\qquad s\in\mathcal G,
\qquad s\equiv3\pmod {4A_0}.
\tag{20m-1}
\]

再假设它落在 negative linear factor，

\[
q\mid((K-A_0)p-A_0).
\tag{20m-1a}
\]

因为 \(q\mid D_*\mid D\mid ph+1\)，有 \(q\nmid p\)。若 \(q\mid A_0\)，
(20m-1a) 会给出 \(q\mid K\)，与 \((A_0,K)=1\) 矛盾；故 \(q\nmid A_0\)。
又 \(q=sK-A_0>s\)，并由 \(p^{-1}\equiv-h\pmod q\)、(20m-1a) 得

\[
K-A_0\equiv-A_0h\pmod q,
\qquad
K\equiv A_0(1-h)\pmod q.
\tag{20m-2}
\]

因 \(Da=3+h(h-1)\) 且 \(q\mid D\)，这也重放 general-\(A_0\) quadratic shift：

\[
3A_0^2+K(K-A_0)
\equiv A_0^2\bigl(3+(1-h)(-h)\bigr)
\equiv0\pmod q.
\tag{20m-2a}
\]

将它代回 \(q+A_0=sK\)，得到

\[
q\mid A_0\bigl(s(h-1)+1\bigr),
\qquad\text{从而}\qquad q\mid F_s^-.
\tag{20m-3}
\]

由 (20j) 又有 \(q\mid\Delta_s\)。从 (20k) 到 (20l) 的逐项枚举只使用
\(q\mid\Delta_s\)、\(q\nmid A_0\)、\(s\equiv3\pmod {4A_0}\) 与
\(q+A_0\equiv0\pmod s\)，所以在这里同样给出 \((s,q)=(3,5)\)。若
\(5\mid F_3^-=3h-2\)，则
\(h\equiv-1\pmod5\)，同一 \(D\) 关系给出 \(p\equiv1\pmod5\)。此时

\[
5\mid(p-1,h+1,m+2).
\tag{20n}
\]

它正是已有 \(p-1,h+1,m+2\) overlap，而不是新的 pure-\(T\) transverse
branch；若 \(5\) 的更高赋值仍留在 \(D_*\)，那只是该 overlap 的既有 excess
情形。特别地，取 \(A_0=1\) 时才有 \(K=(5+1)/3=2\)、\(L=1\)，恰恢复此前的
\(A_0=1\) negative branch。故可准确总结为

\[
\boxed{
\begin{array}{l}
\text{terminal-first 的 actual }m=3\text{ stutter 不保留任何允许 }A_0\text{ 的 positive low-gap exit};\\
\text{其 general-}A_0\text{ negative low-gap specialization 至多是 }(s,q)=(3,5)\text{ 的既有 overlap}.
\end{array}}
\tag{20o}
\]

这是一个 fixed low-gap family exhaustion，不证明 \(D_*\) 的其它因子命中 terminal，
也不构造 TR1 的全称 E1--E5 adapter。

### 6.3 terminal-first 后 \(q=5\) transverse residual 的精确 \(5\)-进管

上一节留下的 \((s,q)=(3,5)\) negative overlap 不能仅按“\(5\mid D_*\)”
记录：在本 \(m=3\) slice 中，它等价于一个精确的 \(-11\) norm \(5\)-进条件。令

\[
F(X)=3X^2-X+1,
\qquad
\nu=v_5(A),
\qquad
\delta=v_5(D).
\tag{20p}
\]

则在本卡的 terminal-first actual scope 内有

\[
\boxed{
5\mid D_*
\quad\Longleftrightarrow\quad
v_5\bigl(F(u)\bigr)\ge\nu+2.}
\tag{20q}
\]

**证明。** 若 \(5\mid D_*\)，则 \(5\mid D\)，而 \(AD=F(u)\)。模 \(5\)
的两个根恰为

\[
F(u)\equiv0\pmod5
\quad\Longleftrightarrow\quad
u\equiv3\ \hbox{或}\ 4\pmod5.
\tag{20r}
\]

若 \(u\equiv4\pmod5\)，则 \(h=3u\equiv2\pmod5\)，并由
\(D=3p+1-h\) 得 \(p\equiv2\pmod5\)。此时

\[
5\mid3h-1,
\qquad
K=\langle h\rangle_5=2,
\qquad
\frac{5+1}{K}=3,
\tag{20s}
\]

正是第 6.2 节的 \(A_0=1\) positive low-gap Type II terminal。它已被
terminal-first 排除。因此必有 \(u\equiv3\pmod5\)，从而

\[
h\equiv-1\pmod5,
\qquad
p\equiv1\pmod5,
\qquad
D_H=5.
\tag{20t}
\]

因为 \(D_H\) 恰为 \(5\)，\(5\mid D_*\) 等价于 \(\delta\ge2\)；再由
\(D=F(u)/A\)，这正是 (20q) 的右端。反过来，若该右端成立，则
\(25\mid D\)。若 \(u\equiv4\pmod5\)，则 \(h\equiv2\pmod5\)，所以
\(5\nmid h^2-1\) 且 \(5\mid D_*\)；于是 (20s) 的 positive terminal 再次与
terminal-first 矛盾。故
(20t) 成立、\(D_H=5\)，于是 \(5\mid D/D_H=D_*\)。证毕。

这里的 \(u\equiv3\pmod5\) 根是 simple root，因为

\[
F'(3)=17\equiv2\pmod5.
\tag{20u}
\]

令 \(\alpha_j\) 为唯一满足

\[
F(\alpha_j)\equiv0\pmod {5^j},
\qquad
\alpha_j\equiv3\pmod5
\tag{20v}
\]

的剩余类。Hensel 提升和 (20q) 给出更精确的等价式

\[
\boxed{
5\mid D_*
\quad\Longleftrightarrow\quad
u\equiv\alpha_{\nu+2}\pmod {5^{\nu+2}}.}
\tag{20w}
\]

前几层为

\[
\alpha_1=3\pmod5,
\qquad
\alpha_2=3\pmod {25},
\qquad
\alpha_3=53\pmod {125}.
\tag{20x}
\]

特别地，任何未被 terminal-first 吃掉的 \(q=5\) transverse residual 都满足

\[
\boxed{
p\equiv11\pmod {25},
\qquad
h\equiv9\pmod {25},
\qquad
u\equiv3\pmod {25},}
\tag{20y}
\]

并且

\[
v_5(p-1)=v_5(h+1)=v_5(m+2)=1,
\qquad
v_5(D_*)=\delta-1=v_5(F(u))-\nu-1.
\tag{20z}
\]

令

\[
t=v_5(D_*)=\delta-1,
\qquad
\tau=v_5(T),
\tag{20za}
\]

这个 \(q=5\) branch 的原始 root 坐标还满足一个精确等价式：

\[
\boxed{
\varrho\equiv11\pmod {25}
\quad\Longleftrightarrow\quad
\tau\ge2.}
\tag{20zb}
\]

事实上，(20h) 先给出 \(\varrho\equiv1\pmod5\)，写

\[
\varrho=1+5c.
\tag{20zc}
\]

由 (20y) 的 \(p\equiv11\pmod {25}\)，直接在 \(T\) 的定义中计算

\[
2T=2p^2\varrho-(p+1)
\equiv5(1+2c)\pmod {25}.
\]

故 \(25\mid T\) 当且仅当 \(c\equiv2\pmod5\)，这正是 (20zb)。再由
\(5^t\mid T\)，有 \(\tau\ge t\)。于是唯一尚未被这个 root-coordinate
收缩覆盖的 \(q=5\) 情形有精确的最小 leaf 正规形

\[
\boxed{
\varrho\not\equiv11\pmod {25}
\quad\Longleftrightarrow\quad
t=\tau=1.}
\tag{20zd}
\]

并令 \(E\) 为该 actual maximal receipt 的 complete-excess multiplier，
\(\zeta=v_5(R-h)\)。由 (20z) 的 \(b=v_5(p-1)=1\) 与已有
\(p-1,h+1,m+2\) complete-excess 分型，(20zd) 的 minimal leaf 还必满足

\[
\boxed{5\nmid E,\qquad\zeta=2.}
\tag{20ze}
\]

反之，若 \(5\mid E\)，该分型给出 \(\tau=b+t=t+1\ge2\)，故自动落入
\(\varrho\equiv11\pmod {25}\) 的已定向支。这样，所有 \(t\ge2\) 或
complete-excess \(5\)-branch 都已被压到同一个 root-residue class；剩下的仅是
\(t=\tau=1\)、non-excess 的 actual leaf。

最后一个指数仍由已有 overlap capacity map 支付，即
\(5^t\mid T\)，而 actual residual map 至少给出
\(5\mid2\varrho+3\)，故 \(\varrho\equiv1\pmod5\)。这些是同一个
\(q=5\) residual 的 norm、receipt 与原始 root 坐标三种描述；其中
\(\varrho\) 仍不是 (16) 的 \(r_{27}\)。

本节只把唯一 low-gap negative overlap 压缩为一条可无限提升的局部同余管；它没有
证明该管为空，也没有给出 terminal、source consumption 或 E1--E5 adapter。因此
TR1、QC1 与 T6 的状态均不改变。

### 6.4 最小 \(q=5\) leaf 强制一个非平凡 pure-\(T\) cofactor

上一节的 minimal leaf 还不能被当作“只剩同一个 \(5\)”的局部残余。事实上，在整个
\(q=5\) branch（不只 minimal leaf）中，C-side 与 transverse carrier 精确分离为

\[
\boxed{D_C=5,\qquad D_T=D_*.}
\tag{20zf}
\]

**证明。** \(m=3\) 时，C-side localization 给出

\[
D_C\mid\operatorname{lcm}(m,m+2)=15.
\tag{20zg}
\]

另一方面 \(D\equiv1\pmod3\)，故 \(3\nmid D_C\)。由 (20z)，
\(v_5(D)\ge2\) 而 \(v_5(C)=v_5(p-1)=1\)，所以 \(5\mid D_C\)。
于是 (20zg) 强制 \(D_C=5\)。再用 (20t) 的 \(D_H=5\)，便得到
\(D_T=D/D_C=D/5=D_*\)。证毕。

现在专门回到 (20zd) 的 minimal leaf，定义

\[
L_5=\frac{D_*}{5}.
\tag{20zh}
\]

由于 \(t=v_5(D_*)=1\)，有 \((L_5,5)=1\)。而 (20g) 给出

\[
L_5>\frac{2p+1}{25}>1
\tag{20zi}
\]

（核心素数 \(p\ge73\)），所以可取一个奇素数 \(\ell\mid L_5\)。它不是另一份
模糊的 C-side 因子：由 (20zf)、\(D_H=5\)、actual C/T split 及 (20h)，有

\[
\boxed{
\ell\mid\gcd\bigl(T,\ 2\varrho+3,\ h^2-h-2\varrho\bigr),
\qquad
\ell\nmid (p^2-1)(h^2-1)m(m+2)(m-1).}
\tag{20zj}
\]

这里 \(\ell\nmid p^2-1\) 来自 \(D_C=5\)，\(\ell\nmid h^2-1\) 来自
\(D_H=5\)，而 \(m=3\)、\(\ell\ne3,5\) 排除余下三个小 \(m\)-side 因子。
第一组整除式分别来自 \(D_T\mid T\)、\(D_T\mid h^2-h-2\varrho\) 与
\(D_*\mid2\varrho+3\)。

因此 minimal \(q=5\) leaf 不是一个单独的 overlap dead end：它**必定**携带至少一个
非 \(5\) 的 actual pure-\(T\) prime carrier。这个 carrier 仍未被证明命中 terminal
menu 或拥有 E1--E5 adapter；但未来的 TR1 证明可以且必须在 \(\ell\) 上进行
physicalization，不能只反复处理已经完全分账的 \(5\) overlap。

### 6.5 \(L_5\) 的所有非平凡除子均避开 general-\(A_0\) positive terminal fan

上一节产生的 pure-\(T\) cofactor 看似可以立刻送入 general-\(A_0\) quadratic
Type II fan 的正支。这里必须先排除一个更强的事实：在 minimal leaf 内，**没有**
\(L_5\) 的非平凡除子能满足该正支的完整 terminal congruence。令

\[
Q>1,\qquad Q\mid L_5.
\tag{20zk}
\]

则不存在 odd \(A_0\mid p+3\)、even \(K>A_0\) 与 \((A_0,K)=1\)，使得

\[
Q\mid Kp+A_0,
\qquad
Q\equiv3K-A_0\pmod {4A_0K}.
\tag{20zl}
\]

按照 whole-divisor positive fan，(20zl) 若成立就会给出一张 direct Type II
terminal；本节证明它在这个 leaf 中实际上没有输入。

**证明。** 令

\[
s=\frac{Q+A_0}{K},
\qquad
C_0=\frac{p+s}{4A_0Q}.
\tag{20zm}
\]

由 (20zl) 有

\[
Q=Ks-A_0,
\qquad
s\equiv3\pmod {4A_0},
\qquad
s\ge3,
\tag{20zn}
\]

且 \(C_0\) 是正整数。又 \(Q\mid D\mid ph+1\)，将
\(Q\mid Kp+A_0\) 乘以 \(h\) 后得到

\[
A_0h\equiv K\pmod Q.
\tag{20zo}
\]

由 (20zl) 的最小正剩余，\(Q\ge3K-A_0>K\)。故可唯一写成

\[
A_0h=\alpha Q+K,
\qquad \alpha\in\mathbb Z_{\ge0}.
\tag{20zp}
\]

现在写 \(L_5=Qj\)。minimal leaf 的 \(D_H=5\)、\(D_*=5L_5\) 与
\(t=1\) 给出

\[
D=25Qj.
\tag{20zq}
\]

另一方面 (20zm) 给出 \(p=4A_0QC_0-s\)。将它和 (20zp) 代入
\(D=3p+1-h\)，并先乘以 \(A_0\)，得到

\[
\bigl(12A_0^2C_0-\alpha-25A_0j\bigr)Q
=3A_0s+K-A_0.
\tag{20zr}
\]

右端为正。记左侧括号为 \(\beta\in\mathbb Z_{>0}\)，再代入
\(Q=Ks-A_0\)，便得到只含 terminal 参数的刚性方程

\[
\boxed{
(\beta K-3A_0)s=K+A_0(\beta-1).}
\tag{20zs}
\]

它的正整数解在 (20zn) 和 \(K>A_0\) 下极少。若 \(\beta\ge5\)，则

\[
3(\beta K-3A_0)-\bigl(K+A_0(\beta-1)\bigr)
=(3\beta-1)K-\beta A_0-8A_0>0,
\]

其中最后一步使用 \(K\ge A_0+1\)。这与 \(s\ge3\) 矛盾。剩余
\(\beta=1,2,3,4\) 分别给出

\[
\begin{array}{c|c}
\beta&\text{(20zs) 的等价式}\\
\hline
1&(s-1)K=3A_0s\\
2&(2s-1)K=A_0(3s+1)\\
3&(3s-1)K=A_0(3s+2)\\
4&(4s-1)K=3A_0(s+1).
\end{array}
\tag{20zt}
\]

由于 \(s=3+4A_0n\)，第一行要求 \(s-1\mid3A_0\)：当 \(s=3\) 时这会要求
\(2\mid3A_0\)，而 \(s\ge4A_0+3\) 时有 \(s-1>3A_0\)，故无解。第二行中
\(\gcd(2s-1,3s+1)\mid5\)，第三行中
\(\gcd(3s-1,3s+2)\mid3\)，第四行中
\(\gcd(4s-1,s+1)\mid5\)。所以当 \(s\ge4A_0+3\) 时，(20zt) 每一行的
左侧去除该公因子后仍大于右侧所能提供的 \(A_0\) 或 \(3A_0\) 因子；只需检查
\(s=3\)。此时第二行给出

\[
(A_0,K,Q)=(1,2,5),
\tag{20zu}
\]

第三行给出 \(8K=11A_0\)，与 \(A_0\) 为奇数、\(K\) 为偶数矛盾；第四行给出
\(11K=12A_0\)。结合 \((A_0,K)=1\)，后者唯一给出

\[
(A_0,K,Q)=(11,12,25).
\tag{20zv}
\]

但 (20zh) 已有 \((L_5,5)=1\)，故 (20zu)、(20zv) 的 \(Q=5\) 和 \(Q=25\)
都不可能整除 \(L_5\)。矛盾，证毕。

这条 no-go 同时覆盖 \(Q=\ell\) 的素数选择和任意复合 \(Q\mid L_5\)，也允许
unbounded 的 gap \(s\)；因此它不是此前 fixed-low-gap 枚举的重述。它只排除了
一个明确的 direct Type II terminal family。native raw-ray、其它 Type I/II 图表、
general-\(A_0\) 负支以及带 E1--E5 的 actual adapter 都仍未处理，TR1 与 T6 的状态
不变。

### 6.6 \(m=3\) 的 native raw Type II menu 实际为空

这个 no-go 不需要进入 \(q=5\) leaf。对任一 \(m=3\) actual receipt，由 (5) 与
\(h=3u\) 直接有

\[
h^2-h+3=3(3u^2-u+1)=3AD,
\qquad\text{故}\qquad D\mid h^2-h+3.
\tag{20zw}
\]

反设某个 \(Q\mid D\) 命中 native raw menu。按该 menu 的定义，存在
\(c\in\mathbb Z_{>0}\) 使

\[
Q=4hc-1.
\tag{20zx}
\]

令

\[
N=\frac{h^2-h+3}{Q}\in\mathbb Z_{>0}.
\tag{20zy}
\]

模 \(h\) 使用 (20zx) 得 \(N\equiv-3\pmod h\)，故可写

\[
N=ah-3,
\qquad a\in\mathbb Z_{>0}.
\tag{20zz}
\]

将 (20zx)、(20zz) 代回 (20zy) 的分子，严格消去常数项后有

\[
h^2-h+3=(ah-3)(4hc-1)
\quad\Longrightarrow\quad
(4ac-1)h=a+12c-1.
\tag{20zza}
\]

但 \(a,c\ge1\) 时

\[
4(4ac-1)-(a+12c-1)
=(16c-1)a-12c-3\ge0.
\tag{20zzb}
\]

所以 (20zza) 强制 \(h\le4\)。另一方面 (11)--(12) 已给
\(h=3u\ge48\)，矛盾。因此

\[
\boxed{\mathcal M_{\mathrm{raw}}(p,h,D)=\varnothing
\quad\text{在所有 actual }m=3\text{ proper-root receipts 中成立}.}
\tag{20zzc}
\]

这不与一般 native raw menu 的存在性冲突：它使用的是本 slice 特有的
\(D\mid h^2-h+3\)。结论只排除该 Type II terminal chart；其它 terminal 图表和
所有 E1--E5 physicalization 义务保持开放。

### 6.7 minimal leaf 的 pure-\(T\) prime 不会进入 reflected negative ray

上一节排除了 positive quadratic fan 与 native raw menu；还须检查已有 negative-root
terminal 的反射子类。令 \(\ell\mid L_5\) 为任一素数。则不存在正整数
\(s\ge3,\lambda,c\) 满足

\[
\ell=s(\lambda+1)-1,
\qquad
\lambda p\equiv1\pmod\ell,
\qquad
\ell\equiv-1\pmod {4s(s-1)}.
\tag{20zzd}
\]

后一个同余正是 reflected negative ray 的 terminal 条件；当 \(s\) 取已有
low-gap set 时，这一结论特别排除了完整的 Bezout-reflection Type II certificate。

**证明。** 由最后一个同余与第一式，可写

\[
\lambda+1=4c(s-1),
\qquad
\ell=4sc(s-1)-1.
\tag{20zze}
\]

因为 \(\ell\mid D\mid ph+1\) 且 \(\lambda p\equiv1\pmod\ell\)，有

\[
h\equiv-\lambda\pmod\ell.
\tag{20zzf}
\]

这里 \(0<\lambda<\ell\)，而
\(\ell-\lambda=(s-1)(\lambda+1)=4c(s-1)^2\)。故存在
\(\alpha\in\mathbb Z_{\ge0}\) 使

\[
h=\alpha\ell+4c(s-1)^2.
\tag{20zzg}
\]

又由于 \(\ell\) 为素数且 \(\lambda\not\equiv0\pmod\ell\)，由 (20zzd) 得

\[
B:=\frac{(s-1)p+s}{\ell}\in\mathbb Z_{>0}.
\tag{20zzh}
\]

事实上，将分子乘以 \(\lambda\) 后模 \(\ell\) 化简，恰得到
\((s-1)+s\lambda=\ell\)。写 \(L_5=\ell j\)，由
\(D=25L_5\)、(20zzg) 及

\[
p=\frac{\ell B-s}{s-1}
\tag{20zzi}
\]

可得

\[
\bigl(3B-\alpha(s-1)-25j(s-1)\bigr)\ell
=2s+1+4c(s-1)^3.
\tag{20zzj}
\]

右端为正，故左括号可记为 \(\beta\in\mathbb Z_{>0}\)。再用 (20zze) 消去
\(\ell\)，得到

\[
4c(s-1)\bigl(\beta s-(s-1)^2\bigr)=\beta+2s+1.
\tag{20zzk}
\]

括号必须为正，因而 \(\beta\ge s-1\)。写
\(\beta=s-1+r\)、\(r\ge0\)，(20zzk) 化为

\[
4c(s-1)\bigl(s(r+1)-1\bigr)=3s+r.
\tag{20zzl}
\]

左端减右端关于 \(r\) 严格递增，且在 \(r=0\) 时至少为

\[
4(s-1)^2-3s>0
\qquad(s\ge3).
\tag{20zzm}
\]

所以 (20zzl) 无正整数解，矛盾，证毕。

该引理不说 \(\ell\) 必须落入某一 negative root；它只证明一旦尝试用 reflected
negative ray 消费它，就必然失败。non-reflection negative branch、其它 Type I/II
chart 以及 actual E1--E5 adapter 仍是下一步的实质问题。

### 6.8 \(L_5\) 真因子只能制造 formal strictness，不能删除 actual receipt

最小叶看起来还留下一个诱人的形式操作。任取

\[
1<J\mid L_5,
\tag{20zzn}
\]

并写

\[
\widetilde D_J=\frac{D}{J},
\qquad
\widetilde E_J=EJ.
\tag{20zzo}
\]

因为此处 \(D=25L_5=3p+1-h<3p\)，有

\[
1<J\le L_5<\frac{3p}{25}<p.
\tag{20zzp}
\]

又 \(p\nmid D\)，故 \(p\nmid J\)。所以 (20zzo) 保持所有容易检查的整数门：

\[
R-h=\widetilde E_J\widetilde D_J,
\qquad
\widetilde D_J\mid K,
\qquad
\widetilde D_J\mid ph+1,
\qquad
p\nmid\widetilde E_J.
\tag{20zzq}
\]

原 receipt 是 stutter，故 \(D\equiv1-h=-(h-1)\pmod p\)。形式 cofactor 因而为

\[
\widetilde c_J
:=
\left\langle
\widetilde D_J(h-1)^{-1}
\right\rangle_p
=
\left\langle-J^{-1}\right\rangle_p.
\tag{20zzr}
\]

由 (20zzp)，\(J\not\equiv1\pmod p\)，故

\[
\boxed{1\le\widetilde c_J\le p-2.}
\tag{20zzs}
\]

也就是说，删去 \(J\) 的确会产生一个**形式上的**严格 cofactor。关键是它不能
被误当作同一 endpoint 的 actual strict carry。

为此固定该 endpoint 的原始 \((A,K,z)\)，其中 \(z=R-h\)，并重放唯一的
maximal complete-excess normalisation

\[
Q_{\rm ex}
=
\prod_{\nu_\ell(z)>\nu_\ell(K)}
\ell^{\nu_\ell(z)},
\qquad
\beta=\frac z{Q_{\rm ex}},
\qquad
D=\beta(A,Q_{\rm ex}),
\qquad
E=\frac{Q_{\rm ex}}{(A,Q_{\rm ex})}.
\tag{20zzt}
\]

取任意素数 \(\ell\mid J\)，并记

\[
a_\ell=\nu_\ell(A),
\qquad
k_\ell=\nu_\ell(K),
\qquad
b_\ell=\nu_\ell(z).
\tag{20zzu}
\]

同一固定 endpoint 的 canonical \(D\)-指数只能是

\[
\nu_\ell(D)=
\begin{cases}
b_\ell,&b_\ell\le k_\ell,\\
a_\ell,&b_\ell>k_\ell.
\end{cases}
\tag{20zzv}
\]

但 \(\nu_\ell(\widetilde D_J)<\nu_\ell(D)\)。因此

\[
\boxed{
\widetilde D_J
\text{ 不可能是同一 }(A,K,z)\text{ 的 canonical maximal receipt}.}
\tag{20zzw}
\]

这不是单靠唯一性措辞的结论：在第一行，形式删除把一个尚在 \(K\) 容量内的
\(\ell\)-指数错误地移入 multiplier；在第二行，它把 canonical \((A,Q_{\rm ex})\)
留下的指数再删去。两种情形都直接违反 (20zzv)。所以 (20zzq) 中的整除式即使全部
成立，也不能为 complete-excess bundle 或 strict support rebase 提供 E1 receipt。

这还给出 minimal leaf 的一个可操作、但严格条件性的来源二分：

\[
\ell\mid L_5,\quad
\begin{cases}
\ell\nmid E
&\Longrightarrow\
\nu_\ell(z)=\nu_\ell(D)\le\nu_\ell(K),\\
\ell\mid E
&\Longrightarrow\
\nu_\ell(z)>\nu_\ell(K).
\end{cases}
\tag{20zzx}
\]

第一行由 (20zzv) 的第一种情形给出，第二行由
\(\nu_\ell(E)>0\) 只能出现在第二种情形给出。故前一类 pure-\(T\) prime 在当前
endpoint 甚至没有 raw overcapacity；它若要参与 TR1，必须来自不同的 raw
occurrence 或新 adapter。后一类则已有 endpoint-level overcapacity，但仍不能使用
\(\widetilde D_J\)。

这里不再需要把 root endpoint 的 raw occurrence 当作未知输入。已有 universal
raw-word 定理从 universal_p_source_v1 出发，先到 \((1,R-1)\)，再经两段
规范 capacity-peeling 到达 \((h,z,1)\)。因此若 \(\ell\mid E\)，则可在该
已回放 word 后追加唯一 shift
\(t=\ell-1\)，并有无额外 gcd 约分的 actual raw child

\[
(z,h,1)
\longmapsto
\left(
\frac z\ell,\
\frac{h+R(\ell-1)}\ell,\
1
\right)
=
\left(
\frac z\ell,\
R-\frac z\ell,\
1
\right).
\tag{20zzy}
\]

这里 \((z/\ell,R-z/\ell)=1\) 来自 \((z,R)=(z,h)=1\)。所以
\(\ell\mid E\) 时的缺口已不再是 raw occurrence，而是 universal root word 只能标为
analysis evidence：它由当前 target chart 反向确定，尚不支付 target-independent
persistent origin、scope 或 terminal-first miss。后继仍须重新计算 full receipt、typed
target、全域 lift 与 T5 ticket；当前没有证明 (20zzy) 给出 terminal 或 E1--E5 edge。

### 6.9 actual raw deflation 的严格 support cofactor

上一节的 (20zzy) 不是把 \(D\) 除以 \(\ell\) 的替代记号。它改变了 raw node，
因而应在 child 上重新计算完整超额块。这个重算恰好给出一个严格的 canonical
support target。

仍令

\[
M_{\rm ex}=\operatorname{lcm}(A,Q_{\rm ex})=AE,
\tag{20zzz}
\]

并取一个素数

\[
\ell\mid(E,L_5).
\tag{20zza}
\]

第 6.4 节的 pure-\(T\) 分裂给出 \(\ell\nmid p^2-1\)。由于
\(K=A(p-1)\)，若

\[
a=\nu_\ell(A)=\nu_\ell(K),
\qquad
b=\nu_\ell(z),
\tag{20zzb}
\]

则 \(\ell\mid E\) 与 canonical receipt 的逐赋值规则等价于 \(b>a\)。
对 (20zzy) 的 child 记

\[
x=\frac z\ell,
\qquad
Q_x=
\prod_{\nu_q(x)>\nu_q(K)}q^{\nu_q(x)},
\qquad
M_x=\operatorname{lcm}(A,Q_x).
\tag{20zzc}
\]

除 \(\ell\) 外，各个素数在 \(x\) 与 \(z\) 中的赋值完全相同。对 \(\ell\)，
\(\nu_\ell(x)=b-1\)：若 \(b-1>a\)，它仍在 \(Q_x\) 中；若 \(b-1=a\)，
它退出 \(Q_x\) 但恰由 \(A\) 承担。两种情形都给

\[
\nu_\ell(M_x)=b-1=\nu_\ell(M_{\rm ex})-1.
\tag{20zzd}
\]

逐素数合并，得到没有选择余地的恒等式

\[
\boxed{
M_x=\frac{M_{\rm ex}}{\ell}
=A\frac E\ell.}
\tag{20zze}
\]

这里 \(E/\ell>1\)：否则 \(E=\ell\)，但 stutter 有 \(E\equiv1\pmod p\)，
而 (20zzp) 给出 \(1<\ell<p\)，矛盾。因此 \(M_x>A>B_p\)。

原 root chart 满足 \(4A\equiv-1\pmod p\)，而 stutter 又有
\(E\equiv1\pmod p\)。所以 child 的 canonical lcm support cofactor 精确为

\[
\begin{aligned}
c_x
&=
\left\langle(4M_x)^{-1}\right\rangle_p\\
&=
\left\langle-\ell E^{-1}\right\rangle_p
=p-\ell.
\end{aligned}
\tag{20zzf}
\]

特别地

\[
\boxed{
\Lambda_p^\sharp:
(0,p-1)\longmapsto(0,p-\ell)
\quad\text{严格下降}.}
\tag{20zzg}
\]

故 \(\ell\mid(E,L_5)\) 子支的真正障碍不是 E5，也不是 raw move 或 lcm target
的算术唯一性。若能把 (20zzy) 的 child 作为现有单侧 complete-excess 或双色
atomic admission 的实际 occurrence，并补齐 persistent origin、scope、terminal-first
与 typed normal form，那么 (20zze)--(20zzg) 已经支付其 strict support/rank
部分。当前并未证明 child 满足这些 admission 的其余前提；尤其不能从
\(M_x\) 的严格性反推 E1--E4 或全域 lift。

### 6.10 excess-\(\ell\) raw child 的单侧/双色穷尽与精确 split stutter 门

第 6.9 节只重算了 child 的 \(x=z/\ell\) 一侧。这里证明：在 minimal leaf 中，
这个实际 raw child 不会落在 complete-excess 语法之外。仍固定

\[
\ell\mid(E,L_5),
\qquad
x=\frac z\ell,
\qquad
y=R-x,
\tag{20zz-child-1}
\]

并以相对于同一个 \(K\) 的 maximal complete-excess normalisation 定义

\[
x=Q_x\beta_x,
\qquad
g_x=(A,Q_x),
\qquad
E_x=\frac{Q_x}{g_x},
\qquad
D_x=\beta_xg_x,
\tag{20zz-child-2}
\]

以及 \(y=Q_y\beta_y\) 的同类对象。第 6.9 节的逐赋值讨论实际上给出更强的
完整恒等式

\[
\boxed{
E_x=\frac E\ell,
\qquad
D_x=D,
\qquad
\operatorname{lcm}(A,Q_x)=A\frac E\ell.}
\tag{20zz-child-3}
\]

确实，在 \(\ell\) 外所有赋值不变。若
\(a=\nu_\ell(A)=\nu_\ell(K)\)、\(b=\nu_\ell(z)>a\)，则 child 的赋值为
\(b-1\)。当 \(b-1>a\) 时，完整 \(\ell^{b-1}\) 块仍属于 \(Q_x\)；当
\(b-1=a\) 时，它完全退出 \(Q_x\)，转而留在 \(\beta_x\)。两种情形都使
\(D_x\) 的 \(\ell\)-赋值保持为 \(a\)，而 \(E_x\) 的 \(\ell\)-赋值比原来
少一。逐素数合并即得 (20zz-child-3)。

由第 6.9 节已知 \(E/\ell>1\)，所以

\[
Q_x>1,
\qquad
\beta_x\mid K.
\tag{20zz-child-4}
\]

还须排除双色 schema 中可能出现的 \(p\)-block。原端点 primitive，故
\((z,R)=(z,h)=1\)，于是

\[
(x,y)=(x,R)=1.
\tag{20zz-child-5}
\]

proper-root receipt 有 \(p\nmid E\)，而 stutter 给出
\(D\equiv1-h\pmod p\)、\(E\equiv1\pmod p\)。因此

\[
R=h+ED\equiv1\pmod p,
\qquad
x\equiv(1-h)\ell^{-1}\pmod p.
\tag{20zz-child-6}
\]

若 \(p\mid y\)，由 (20zz-child-6) 必有

\[
\ell\equiv1-h\pmod p.
\tag{20zz-child-7}
\]

这里 \(1<h<p\)、\(1<\ell<p\)，故 (20zz-child-7) 强制
\(\ell=p+1-h\)。但 \(\ell\mid L_5\mid D\)，且

\[
D-(p+1-h)=2p.
\tag{20zz-child-8}
\]

于是 \(\ell\mid2p\)，这不可能：\(\ell\) 是 odd pure-\(T\) prime、
\(\ell<p\)，并且 \(p\nmid D\)（\(D\equiv1-h\not\equiv0\pmod p\)）。故

\[
\boxed{p\nmid xy.}
\tag{20zz-child-9}
\]

同样，\(y=h+(\ell-1)x\equiv h\pmod\ell\)，而 \((h,D)=1\)、\(\ell\mid D\)，
所以 \(\ell\nmid y\)。这个事实以后排除了把 \(\ell\) 同时记到两种颜色。

现在有一个无需搜索的穷尽。若

\[
y\beta_x\mid K,
\tag{20zz-child-10}
\]

则 (20zz-child-2)、(20zz-child-4)--(20zz-child-5) 给出

\[
Q_x>1,
\qquad
x=Q_x\beta_x,
\qquad
y\beta_x\mid K,
\qquad
(Q_x,y\beta_x)=1,
\qquad
p\nmid Q_x.
\tag{20zz-child-11}
\]

并且 \(Q_x\nmid K\)、\(Q_x<R\)。这正是单侧 complete-excess receipt 的全部
**算术** kernel；其 canonical support 是 (20zz-child-3)，cofactor 已精确为
\(p-\ell\)，故在原 high-support root 的 \(\Lambda_p^\sharp\) 下严格。

反之，若 (20zz-child-10) 失败，则

\[
\boxed{Q_y>1.}
\tag{20zz-child-12}
\]

因为若 \(Q_y=1\)，maximal definition 给 \(y\mid K\)；再由
\((y,\beta_x)=1\) 及 \(\beta_x\mid K\)，便会推出 \(y\beta_x\mid K\)，矛盾。
结合 (20zz-child-5)、(20zz-child-9)，此时

\[
Q_x,Q_y>1,
\qquad
p\nmid Q_xQ_y,
\qquad
\beta_x\beta_y\mid K.
\tag{20zz-child-13}
\]

所以 raw child 落入 path-anchored atomic split 的完整**算术** kernel，而非一个
未分类的第三种 residual。

最后可把 split 的 E5 问题压成一个单一同余。令

\[
F_y=\frac{Q_y}{(A,Q_y)}>1.
\tag{20zz-child-14}
\]

由于 \((Q_x,Q_y)=1\) 且 \(E_x\mid Q_x\)，其 canonical joined support 为

\[
\begin{aligned}
M_{\rm split}
&=\operatorname{lcm}(A,Q_x,Q_y)\\
&=A\frac E\ell\,F_y.
\end{aligned}
\tag{20zz-child-15}
\]

其中 \(p\nmid F_y\) 由 (20zz-child-9) 给出。用 \(4A\equiv-1\pmod p\) 及
\(E\equiv1\pmod p\)，split target 的 canonical cofactor 是

\[
c_{\rm split}
=\left\langle(4M_{\rm split})^{-1}\right\rangle_p
=\left\langle-\ell F_y^{-1}\right\rangle_p.
\tag{20zz-child-16}
\]

原 root 的 high-support cofactor 为 \(p-1\)，故精确有

\[
\boxed{
c_{\rm split}=p-1
\quad\Longleftrightarrow\quad
F_y\equiv\ell\pmod p.}
\tag{20zz-child-17}
\]

因此 split 分支一旦通过其 source/target 准入，除 (20zz-child-17) 这一显式
congruence 外都自动严格支付 E5；若该同余不成立，则
\(c_{\rm split}\le p-2\)。这把此前模糊的“child 可能还要重新分块”收缩为：

\[
\boxed{
\begin{array}{ll}
\text{single-side:}&\text{算术 kernel 完整，且 cofactor }p-\ell;\\
\text{atomic split:}&\text{算术 kernel 完整，唯一 rank stutter 门为 }
F_y\equiv\ell\pmod p.
\end{array}}
\tag{20zz-child-18}
\]

这不是 E1--E5 edge 的声明。当前 universal root word 仍只提供 target-derived
`analysis_evidence` raw occurrence；两种分支都仍须由一个已入队 source 支付
persistent origin、scope、terminal-first priority、typed target/normal form 与全域 lift。
本节只证明：在这些合同义务之外，minimal leaf 的 excess-\(\ell\) child 已不存在
另一种未分类的 complete-excess arithmetic obstruction。

### 6.11 split stutter 的 root-receipt divisor gate

第 6.10 节没有排除唯一的 split rank-stutter 同余

\[
F_y\equiv\ell\pmod p.
\tag{20zz-gate-1}
\]

但它可以进一步压成只读取原 root receipt 和 \(y\)-side canonical residual 的三重门。
在 split 分支中置

\[
g_y=(A,Q_y),
\qquad
D_y=\beta_yg_y,
\qquad
F_y=\frac{Q_y}{g_y}.
\tag{20zz-gate-2}
\]

按 complete-excess 的定义，\(\beta_y\mid K\)、\(g_y\mid A\mid K\)，而
\((\beta_y,g_y)=1\)，故 \(D_y\mid K\)。又 \(D\mid x\)、\(D_y\mid y\) 和
(20zz-child-5) 给出

\[
(D,D_y)=1,
\qquad
DD_y\mid K,
\qquad
\boxed{D_y\mid\frac KD.}
\tag{20zz-gate-3}
\]

这里并未把两个 residual 的互素性当作额外假设：它直接来自同一 primitive raw child
的两侧。

再从 \(\ell y=(\ell-1)R+h\)、\(pR=4K-1\) 与 \(ph+1=eD\) 得到精确恒等式

\[
\begin{aligned}
p\ell y
&=(\ell-1)(4K-1)+ph\\
&=4(\ell-1)K+eD-\ell.
\end{aligned}
\tag{20zz-gate-4}
\]

两侧前两项均被 \(D_y\) 整除，所以 \(D_y\mid eD-\ell\)。又
\(\ell\mid D\) 而 \((D_y,\ell)=1\)，于是

\[
\boxed{D_y\mid\frac{eD}{\ell}-1.}
\tag{20zz-gate-5}
\]

若再假设 (20zz-gate-1)，则由 (20zz-child-6) 和 \(y=F_yD_y\) 有

\[
\ell^2D_y
\equiv
\ell y
\equiv
\ell+h-1
\pmod p.
\tag{20zz-gate-6}
\]

再用 stutter 的 \(D\equiv1-h\pmod p\) 并约去 \(\ell\)，可把它写成更接近
原 residual 的等价式

\[
\boxed{\ell D_y\equiv1-\frac D\ell\pmod p.}
\tag{20zz-gate-6a}
\]

事实上 \(\ell\) 是 \(L_5\) 的 odd prime，故 \(\ell\ge7\)；又
\(D/\ell<3p/\ell<p\)，并且 \(D/\ell=25(L_5/\ell)>1\)。所以
(20zz-gate-6a) 还有唯一的正整数 lifted form

\[
\boxed{
\ell D_y=p+1-\frac D\ell+pn_y,
\qquad n_y\in\mathbb Z_{\ge0}.}
\tag{20zz-gate-6b}
\]

最后，\(F_y\mid Q_y\mid y\)，而第 6.10 节已经证明 \(\ell\nmid y\)。由于
\(1<\ell<p\)，(20zz-gate-1) 唯一地写成

\[
\boxed{F_y=\ell+ps,\qquad s\in\mathbb Z_{\ge1}.}
\tag{20zz-gate-7}
\]

其中 \(s=0\) 会给 \(F_y=\ell\mid y\)，已被 \(y\equiv h\not\equiv0\pmod\ell\)
排除。综上，任何 actual split stutter 都必须同时满足

\[
\boxed{
D_y\mid
\gcd\!\left(\frac KD,\ \frac{eD}{\ell}-1\right),
\qquad
\ell D_y\equiv1-\frac D\ell\pmod p,
\qquad
F_y=\ell+ps\ (s\ge1).}
\tag{20zz-gate-8}
\]

这是一个 root-receipt divisor gate，而不是 stutter 的排空定理：目前没有证明
(20zz-gate-8) 无解，也没有从它构造 terminal、macro suffix 或 persistent edge。
它的价值在于把 split 的剩余问题从任意的 \(Q_y\) 因子化，缩到一个与 \(D\) 互素、
同时受两个原始 divisor gate 和一个模 \(p\) 线性余数约束的 \(D_y\)。

## 7. 根支撑强制的 primitive \(m=3\) quotient fiber

这里还有一个比 (15) 更强的 actual-only 收缩。因为 \(h=3u\mid p^2+p+1\)，
而 \(3\nmid u\)，\(u\) 的任一素因子 \(q\) 都满足 \(q\ne3\)。若
\(p\equiv1\pmod q\)，则 \(p^2+p+1\equiv3\pmod q\)，矛盾；故 \(p\) 在
模 \(q\) 下的乘法阶恰为 \(3\)，从而 \(q\equiv1\pmod3\)。因此

\[
\boxed{u\equiv1\pmod3.}
\tag{21}
\]

式 (15) 随即给出 \(3\mid A\)。结合 \(A\) 为奇数和 (11)，有

\[
\boxed{A\equiv3\pmod6,\qquad A\ge9.}
\tag{22}
\]

令 \(b=e-1\)，并写 \(g=(a,b)\)。这里 \(3\mid b\) 而 \(9\mid a\)，
所以 \(3\mid g\)。实际 primitive-quotient normalization 给出 \(g\mid m=3\)，
故

\[
\boxed{g=(a,e-1)=3.}
\tag{23}
\]

置

\[
B=\frac{e-1}{3},\qquad \kappa=\frac{k}{3}.
\]

primitive system 在本 slice 中精确成为

\[
\boxed{
(A,B)=1,qquad
u=3B+1-A,qquad
A^2-AB+B^2=u\kappa,qquad
pA+B=(3B+1)u.
}
\tag{24}
\]

因为 \(3\mid A\) 而 \((A,B)=1\)，有 \(3\nmid B\)。将 (24) 的范数式模
\(3\) 化简，并使用 \(u\equiv1\pmod3\)，得到 \(\kappa\equiv1\pmod3\)。actual
Eisenstein quotient \(k\) 为奇数，故

\[
\boxed{\kappa\equiv1\pmod6.}
\tag{25}
\]

同一范数式还给出

\[
\boxed{(A,\kappa)=1.}
\tag{25a}
\]

事实上，若素数 \(q\) 同时整除 \(A\) 和 \(\kappa\)，则 (24) 的范数式模 \(q\)
强制 \(q\mid B\)，与 \((A,B)=1\) 矛盾。

为得到一个不依赖 \(p\) 范围的 fixed-\(\kappa\) fiber，令
\(\rho=B-A\)。由 \(a<e\)、\((A,B)=1\) 和 (12)，有 \(\rho\ge2\)，并且 (24) 写成

\[
u=2A+3\rho+1,
\qquad
A^2+A\rho+\rho^2=(2A+3\rho+1)\kappa.
\tag{26}
\]

最后一个 (24) 方程模 \(A\) 给出第一条整除门

\[
A\mid9\rho^2+5\rho+1.
\tag{27}
\]

定义

\[
\lambda:=\frac{9\rho^2+5\rho+1}{A}.
\]

将 \(pA+B=(3B+1)u\) 展开后，得到精确的线性重写

\[
\boxed{p=6A+15\rho+4+\lambda.}
\tag{27a}
\]

因为 \(u=2A+3\rho+1\) 为奇数，\(\rho\) 为偶数。又由 \(3\mid A\)、(27) 和
\(p\equiv1\pmod3\)，依次得到

\[
\rho\equiv1\pmod3,
\qquad
\lambda\equiv0\pmod3.
\]

故 \(9\mid9\rho^2+5\rho+1\)。令 \(\rho=1+3z\) 后模 \(9\) 化简，得到
\(z\equiv2\pmod3\)。再结合 \(\rho\) 为偶数，以及 \(A,\lambda\) 都为奇数，便有

\[
\rho\equiv16\pmod {18},
\qquad
\lambda\equiv3\pmod6.
\tag{27b}
\]

核心模 \(8\) 条件还会收紧 \(A\)。由 (27a) 直接整理为

\[
\begin{aligned}
A(p-1)
={}&(A-3)(6A+21-\rho)+\rho(\rho+2)\\
&+8(2A\rho+\rho^2+8).
\end{aligned}
\tag{27c}
\]

这里 \(\rho(\rho+2)\) 被 \(8\) 整除，而 \(6A+21-\rho\) 为奇数。因为
\(p\equiv1\pmod8\) 且 \(A\) 为奇数，(27c) 强制 \(A\equiv3\pmod8\)。与 (22) 合并，

\[
\boxed{A\equiv3\pmod {24},\qquad A\ge27.}
\tag{27d}
\]

把 (26) 模 \(8\) 化简，并使用 \(A\equiv3\pmod8\) 与 \(\rho\) 为偶数，得到

\[
A^2+A\rho+\rho^2
\equiv7(2A+3\rho+1)\pmod8.
\]

右边括号就是 \(u\)，且 \(u\) 为奇数。由 (26) 可约去它，故

\[
\kappa\equiv7\pmod8.
\]

与 (25) 合并后，

\[
\boxed{\kappa\equiv7\pmod {24}.}
\tag{27e}
\]

而 (26) 模 \(A\) 给出 \(\rho^2\equiv\kappa(3\rho+1)\pmod A\)。代入 (27) 后，

\[
A\mid(27\kappa+5)\rho+(9\kappa+1).
\tag{28}
\]

不需要对 \(27\kappa+5\) 取逆：把 (27) 乘以它的平方，再用 (28) 消去 \(\rho\)，
便得到 resultant gate

\[
\boxed{A\mid9\bigl(27\kappa^2+8\kappa+1\bigr).}
\tag{29}
\]

实际上 (28) 与 \(u=2A+3\rho+1\) 还给出更有方向性的 cross-parameter bridge：

\[
\boxed{(27\kappa+5)u\equiv2\pmod A.}
\tag{29a}
\]

所以 \((A,27\kappa+5)=1\)，并且 fixed-\(\kappa\) 时 \(u\) 的模 \(A\) 类已被
确定。这条桥与 \(A\mid3u^2-u+1\) 联立后也重新给出 (29) 的同一 \(-11\) 判别式
约束。

所以固定 \(\kappa\) 后，\(A\) 是一个显式固定整数的除子，随后 (26) 至多给出两个
整数 \(\rho\)。这是一条 exact finite divisor fiber，不是对 \(p\)、\(u\) 或分母的扫描。

还有一个可直接排除的低 quotient 带。把 (26) 视为 \(\rho\) 的二次方程，其判别式必须是
平方：

\[
\Delta_\kappa
=-3A^2+2A\kappa+9\kappa^2+4\kappa.
\tag{30}
\]

由 (27e)，唯一小于 \(31\) 的正 \(\kappa\) 是 \(7\)。但
\(\Delta_7=-3A^2+14A+469<0\) 对所有 \(A\ge27\) 成立。故

\[
\boxed{
m=3\text{ 的 actual proper-root stutter 必满足 }
k\equiv21\pmod {72},\qquad k=3\kappa\ge93.
}
\tag{31}
\]

这排除了 \(m=3\) 与既有 \(k=3\) fiber 的交集，并排除了唯一更小的允许
\(k=21\) 子纤维；它并不排空 \(\kappa\ge31\) 的无界参数域。

### 7.1 bare difference gap 不能很小

回到已有的 complementary coordinates，并置

\[
\gamma:=W-\eta.
\]

已建立的 actual 坐标不等式给出 \(\gamma>0\) 与 \((\eta,W)=1\)。在本 slice 中
\(\eta=u-2A-1=3\rho\)。因为 \(\rho\) 为偶数，\(\eta\) 为偶数；而
\(k=e\eta-aW\) 为奇数、\(a=3A\) 为奇数，所以 \(W\) 及 \(\gamma\) 都为奇数。
再由 \((\eta,W)=1\)，有

\[
(\gamma,3\rho)=1.
\tag{31a}
\]

将 \(W=3\rho+\gamma\) 代入 \(k=e\eta-aW\)，得到

\[
\boxed{\kappa=3\rho^2+\rho-A\gamma.}
\tag{31b}
\]

结合 \(A\equiv3\pmod8\) 与 \(\kappa\equiv7\pmod8\)，这还给出

\[
\gamma\equiv\rho^2+3\rho+3\pmod8.
\tag{31c}
\]

设 \(c=\gamma\)。把 (31b) 代回 (26)，便把 \(A\) 压到

\[
(2c+1)A^2-
\bigl(6\rho^2+(1-3c)\rho-c\bigr)A-
\rho(9\rho^2+5\rho+1)=0.
\tag{31d}
\]

因此其判别式必须为平方。直接展开为

\[
\begin{aligned}
\Delta_c={}&36\rho^4+(36c+48)\rho^3
+(9c^2+22c+21)\rho^2\\
&+(6c^2+6c+4)\rho+c^2.
\end{aligned}
\tag{31e}
\]

令 \(L_c=6\rho^2+(3c+4)\rho\)。则

\[
\Delta_c-L_c^2
=(5-2c)\rho^2+(6c^2+6c+4)\rho+c^2.
\tag{31f}
\]

这足以不用搜索排除所有小的允许差距。对于 \(c=1\)，右边是
\(3\rho^2+16\rho+1\)，严格介于 \(0\) 与 \(2L_1+1\) 之间；故
\(\Delta_1\) 严格介于 \(L_1^2\) 与 \((L_1+1)^2\) 之间。

由 (27b) 与 (31c)，若 \(c=5,7,11\)，则分别有

\[
\rho\equiv34,52,16\pmod {72}.
\tag{31g}
\]

当 \(c=5\) 时，(31f) 的右边为
\(R_5=-5\rho^2+184\rho+25\)。在唯一的小代表 \(\rho=34\) 处，
\(0<R_5=501<2L_5+1\)；当 \(\rho\ge106\) 时，
\(R_5<0<R_5+2L_5-1=7\rho^2+222\rho+24\)。故 \(\Delta_5\) 总在
相邻平方之间。类似地，当 \(c=7\) 时

\[
R_7=-9\rho^2+340\rho+49<0,
\qquad
R_7+2L_7-1=3\rho^2+390\rho+48>0
\]

对全部 \(\rho\ge52\) 成立，也排除平方。

最后 \(c=11\) 时

\[
R_{11}=-17\rho^2+796\rho+121.
\]

在 \(\rho=16\) 处有
\(2L_{11}+1<R_{11}=8505<4L_{11}+4\)；在剩余的
\(\rho=88,160\) 处有 \(-2L_{11}+1<R_{11}<0\)；而对
\(\rho\ge232\)，有

\[
-4L_{11}+4<R_{11}<-2L_{11}+1,
\]

其中左侧严格不等式等价于
\(R_{11}+4L_{11}-4=7\rho^2+944\rho+117>0\)。这些区间都严格夹在
相邻平方之间。于是 (31d) 不可能在 \(c=1,5,7,11\) 有整数根。

由 (31a)，\(\gamma\) 是不被 \(3\) 整除的正奇数；以上恰排除了小于 \(13\) 的全部
可能值。因此

\[
\boxed{W-\eta=\gamma\ge13.}
\tag{31h}
\]

这是一条 actual coordinate-gap 强化，而不是 terminal：它没有强制
\((\gamma,k)>1\)，所以不能把下节的 \(d\)-cancellation 误写成每个 receipt 都存在的出口。

## 8. whole \(d\)-carrier 的 \(\Phi_6(p)\) 定向

继续令

\[
d=(\gamma,k).
\]

已有 whole-\(d\) identities 给出

\[
d\mid\eta+1,\qquad d\mid a^2-a+1,\qquad (a,d)=1,
\qquad h\equiv p+a\pmod d,
\tag{32}
\]

且 \(d\) 为奇数并满足 \(3\nmid d\)。但 \(m=3\) 坐标有额外的 exact identity

\[
h=3u=2a+3(\eta+1).
\tag{33}
\]

故 (32) 给出 \(h\equiv2a\pmod d\)，与 \(h\equiv p+a\pmod d\) 比较后得到

\[
p\equiv a\pmod d.
\]

因此

\[
\boxed{d\mid p-a,\qquad d\mid p^2-p+1.}
\tag{34}
\]

再结合 whole-\(d\) 的 \(e\equiv a\pmod d\)，actual receipt 的相关坐标在这个 carrier
上满足

\[
\boxed{
p\equiv a\equiv e,\qquad
h\equiv2p,\qquad
\delta=p-h\equiv-p,\qquad
D\equiv p+1
\pmod d.
}
\tag{34a}
\]

这里 \(p\) 在模 \(d\) 下是单位；又 \(d\) 为奇数，所以

\[
\boxed{(d,p^2+p+1)=1,\qquad(d,h)=1.}
\tag{35}
\]

特别地，写 \(v=(p^2+p+1)/h\)，还有 \((d,v)=1\)。

而 \(\gcd(p^2-p+1,p+1)\mid3\)，故

\[
\boxed{(d,D)=1.}
\tag{36}
\]

这在本 slice 中独立重新导出了 (19)，并给出更精确的原因：\(d\) 是
\(\Phi_6(p)=p^2-p+1\) 的实际 carrier，严格避开 root-height 的
\(\Phi_3(p)=p^2+p+1\) 以及 \(D\)-carrier。

已有 natural gap 定义满足 \(s_d\equiv a-h\pmod d\)。由 (33)--(34)，

\[
s_d\equiv\delta\equiv-p\pmod d,
\qquad
\boxed{d\mid s_d^2+s_d+1.}
\tag{37}
\]

这把 whole-\(d\) Type II fan 的 gap 定向成 \(\Phi_3(s_d)\) root。它仍未证明该
fan 必命中，所以 (37) 是下一条 identity-lifted terminal/adaptor 引理的输入，不能直接当作
terminal 或 E1--E5 edge。

### 8.1 \(m=3\) 的 whole-\(d\) branch 排除 \(C_d=7\)

现在额外假设 \(d>1\)，并使用既有 natural fan cofactor

\[
C_d=\frac{p+s_d}{4d}\ge7.
\]

为避免与 (27) 中 fixed-\(\kappa\) fiber 的 \(\lambda\) 混淆，本节起将 natural-gap
商系数记为 \(\ell\)。若 \(C_d=7\)，写

\[
\eta+1=d\sigma,
\qquad
s_d=\ell d-a.
\tag{37a}
\]

第二式是 general natural-gap identity 在 \(m=3\) 的专化。其 parity gate 给出
\(\ell\equiv0\pmod2\)。又 \(d\equiv1\pmod3\)、\(\eta=3\rho\)、
\(a\equiv0\pmod3\) 及 \(p\equiv1\pmod3\) 分别给出

\[
\sigma\equiv1\pmod3,
\qquad
\ell\equiv0\pmod3.
\tag{37b}
\]

由 (27b) 的 \(\rho\) 偶性，\(\eta=3\rho\) 为偶数；又 \(d\) 为奇数，故
\(\sigma=(\eta+1)/d\) 为奇数。于是实际上

\[
\boxed{\sigma\equiv1\pmod6.}
\tag{37b-1}
\]

因为 \(s_d>0\) 且 \(a>0\)，还有 \(\ell>0\)。

在 \(C_d=7\) 时，(37a) 化为

\[
p=(28-\ell)d+a,
\qquad
h=2a+3d\sigma,
\tag{37c}
\]

而 \(h<p\)、\(1\le s_d\le4d\) 强制

\[
a+3d\sigma<(28-\ell)d,
\qquad
(\ell-4)d\le a<\ell d.
\tag{37d}
\]

由 (37b)--(37d)，唯一可能的 \((\sigma,\ell)\) 是

\[
\begin{array}{c|c}
\sigma&\ell\\
\hline
1&6,12,18,24\\
7&6.
\end{array}
\tag{37e}
\]

把 (37c) 代回 \(pa+(e-1)=eh\)，其中 \(e=a+d\sigma\)，得到每一行共同的
二次门

\[
a^2+(5\sigma-28+\ell)ad-a+3\sigma^2d^2-d\sigma+1=0.
\tag{37f}
\]

三行 \((\sigma,\ell)=(1,18),(1,24),(7,6)\) 已由 (37d) 直接矛盾：
前两行分别要求 \(a<7d,a<d\)，但 gap bound 要求 \(a\ge14d,a\ge20d\)；最后一行
要求 \(a<d\)，但 gap bound 要求 \(a\ge2d\)。

对 \((1,6)\)，(37f) 是

\[
f_{1,6}(a)=a^2-17ad-a+3d^2-d+1=0.
\]

此时 \(2d\le a<6d\)，而
\(f'_{1,6}(a)=2a-17d-1<0\)；同时
\(f_{1,6}(2d)=-27d^2-3d+1<0\)。故这一行也不可能。

唯一留下的 \((1,12)\) 行满足

\[
f_{1,12}(a)=a^2-11ad-a+3d^2-d+1=0,
\tag{37g}
\]

并有 \(8d\le a<12d\)、\(h=2a+3d\)、\(\delta=13d-a\)。利用 (37g)，

\[
\delta^2+\delta+1=d(166d-15a+14).
\tag{37h}
\]

第 8 节已证明 \((h,d)=1\)，而 actual root gate 给出
\(h\mid\delta^2+\delta+1\)。故存在正整数 \(q\) 使

\[
166d-15a+14=q(2a+3d).
\tag{37i}
\]

由 \(a\ge8d\) 和 \(d>1\)，右边商严格小于 \(3\)，所以 \(q\in\{1,2\}\)。
若 \(q=1\)，则 \(17a=163d+14\)；代入 (37g) 并乘以 \(17^2\) 后得到

\[
-3045d^2-1114d+247=0,
\]

这对正 \(d\) 不可能。若 \(q=2\)，则 \(19a=160d+14\)；同样代入得到

\[
-6757d^2-1847d+291=0,
\]

也不可能。因此 \(C_d=7\) 无 actual \(m=3\) whole-\(d\) receipt，结合既有
\(C_d\ge7\)，有

\[
\boxed{d>1\quad\Longrightarrow\quad C_d\ge8\quad(m=3).}
\tag{37j}
\]

于是既有 canonical-gap bound 在这个 slice 中收紧为

\[
\boxed{s_d\le\frac{p-8}{7}.}
\tag{37k}
\]

这仍只压缩 Type II fan 的 cofactor/gap；它没有证明某个
\(t\mid dC_d\) 满足 \(t\equiv-1\pmod{s_d}\)，所以不能作为 terminal 或 selector edge。

### 8.2 actual cofactor 的同余锁与 \(C_d\ge25\)

继续固定 \(d>1\)，令 \(C=C_d\)，并保留 (37a) 的 \(\ell\)。由
\(p+s_d=4Cd\) 与 \(s_d=\ell d-a\)，有

\[
p-a=(4C-\ell)d.
\tag{37l}
\]

另一方面，(27d) 给出 \(a=3A\equiv9\pmod {24}\)，而 \(p\equiv1\pmod {24}\)。
所以右侧为 \(16\pmod {24}\)。设 \(M=4C-\ell\)。因为 \(d\) 为奇数，
\(Md\equiv16\pmod {24}\) 先强制 \(8\mid M\)。写 \(M=8M_0\)；再模 \(3\)
使用 \(d\equiv1\pmod3\)，便有

\[
2M_0\equiv1\pmod3,
\qquad
\boxed{4C-\ell\equiv16\pmod {24}.}
\tag{37m}
\]

结合 \(\ell\equiv0\pmod6\)，这还给出

\[
\boxed{C\equiv1\pmod3.}
\tag{37n}
\]

同时，(37d) 在一般 \(C\) 下成为

\[
(\ell-4)d\le a<\ell d,
\qquad
a<(4C-\ell-3\sigma)d.
\]

所以任何非空参数区间都满足

\[
2\ell+3\sigma<4C+4,
\qquad
\ell>0,
\qquad
\sigma\equiv1\pmod3.
\tag{37o}
\]

由第 8.1 节已有的 \(C\ge8\) 和 (37n)，若 \(C<22\)，只需处理
\(C=10,13,16,19\)。式 (37b-1)、(37m)--(37o) 分别将它们压缩为

\[
\begin{array}{c|c}
C&\text{唯一仍可能的 }(\ell,\sigma)\\
\hline
10&\varnothing\\
13&(12,1),(12,7)\\
16&(24,1)\\
19&(12,1),(12,7),(12,13),(36,1).
\end{array}
\tag{37p}
\]

这里 \(C=10\) 时 \(\ell\equiv0\pmod {24}\) 强制 \(\ell\ge24\)，却与
\(2\ell+3\sigma<44\) 矛盾。其余各行仍服从由原线性 stutter equation 给出的
一般二次门

\[
F_{C,\sigma,\ell}(a):=
a^2+(5\sigma-4C+\ell)ad-a+3\sigma^2d^2-d\sigma+1=0.
\tag{37q}
\]

对 \(C=13\)，\(8d\le a<12d\)：\(\sigma=1\) 时 \(F\) 递减且
\(F(8d)=-213d^2-9d+1<0\)，而 \(\sigma=7\) 时 \(F>0\)。对 \(C=16\)，
\(20d\le a<24d\)：\(\sigma=1\) 时 \(F<0\)。对 \(C=19\) 的
\(\ell=12\) 行，\(8d\le a<12d\)：\(\sigma=1,7\) 时 \(F<0\)，
\(\sigma=13\) 时 \(F>0\)。这些符号断言只用 \(d>1\)；例如
\(C=19,\sigma=7\) 的递减起点值为 \(-21d^2-15d+1<0\)。

只剩 (37p) 的 \((C,\ell,\sigma)=(19,36,1)\)。此时

\[
32d\le a<36d,
\qquad
F=a^2-35ad-a+3d^2-d+1,
\]

且 \(\delta=37d-a\)、\(h=2a+3d\)。由 \(h\mid\delta^2+\delta+1\) 以及
\((h,d)=1\)，存在正整数 \(q\) 使

\[
1366d-39a+38=q(2a+3d).
\tag{37r}
\]

左侧至多为 \(118d+38\)，右侧至少为 \(67d\)，故 \(q<3\)。若 \(q=2\)，则
\(43a=1360d+38\)，这与 \(a\ge32d\) 和奇数 \(d>1\) 矛盾。若 \(q=1\)，则
\(41a=1363d+38\)。把它代回 \(F=0\) 并乘以 \(41^2\)，得到

\[
-93093d^2-8506d+1567=0,
\]

这对正 \(d\) 不可能。因此所有 \(C<22\) 的情形均被排除，故

\[
\boxed{d>1\quad\Longrightarrow\quad C_d\ge22\quad(m=3).}
\tag{37s}
\]

第一个仍与 (37n) 相容的 cofactor 是 \(C=22\)。此时 (37m)、(37o) 和
(37b-1) 只留下

\[
(\ell,\sigma)=(24,1),(24,7),(24,13).
\]

在 \(20d\le a<24d\) 上，\(\sigma=1\) 时 (37q) 递减且
\(F(20d)=-777d^2-21d+1<0\)，\(\sigma=13\) 时 \(F>0\)。剩下的
\(\sigma=7\) 满足

\[
F=a^2-29ad-a+147d^2-7d+1,
\qquad
\delta=43d-a,
\qquad
h=2a+21d.
\]

由同一 \(h\mid\delta^2+\delta+1\) gate，存在正整数 \(q\) 使

\[
1702d-57a+50=q(2a+21d).
\tag{37s-1}
\]

左侧至多为 \(562d+50\)，右侧至少为 \(61d\)，故 \(q\le9\)。若 \(q\le4\)，
则 (37s-1) 直接给出 \(a>24d\)。因此 \(5\le q\le9\)。令

\[
P_q=57+2q,
\qquad
R_q=1702-21q,
\qquad
a=\frac{R_qd+50}{P_q}.
\]

代回 \(F=0\) 后，\(P_q^2F\) 依次为

\[
\begin{array}{c|c}
q&P_q^2F\\
\hline
5&107321d^2-75872d+3639\\
6&30067d^2-84521d+3811\\
7&-42693d^2-93142d+3991\\
8&-110959d^2-101735d+4179\\
9&-174731d^2-110300d+4375.
\end{array}
\tag{37s-2}
\]

前两行在所需的奇数 \(d>1\) 上严格为正：第一行从 \(d=1\) 起递增且值为
\(35088\)，第二行从 \(d=3\) 起递增且值为 \(20851\)。后三行从 \(d=1\) 起
严格递减且已经为负。因此 \(C=22\) 也不可能。与 (37n) 合并，得到更强的

\[
\boxed{d>1\quad\Longrightarrow\quad C_d\ge25\quad(m=3).}
\tag{37s-3}
\]

最后，\(s_d\equiv3\pmod4\) 与 \(1\le s_d\le4d\) 给出 \(4d-s_d\ge1\)。因此

\[
p-(C_d-1)s_d=C_d(4d-s_d)\ge C_d.
\]

由 (37s-3) 立即有

\[
p-24s_d=
\bigl[p-(C_d-1)s_d\bigr]+(C_d-25)s_d\ge25,
\]

从而

\[
\boxed{s_d\le\frac{p-25}{24}.}
\tag{37t}
\]

这仍是 actual gap/capacity 收缩。它没有令 natural fan 必命中，不能构造 terminal 或
E1--E5 edge。

### 8.2.1 完整二次门再排除 \(25\le C_d<37\)

上一节只用了 \(C\ge25\) 后的同余锁。现在重新使用完整二次门 (37q)，可排除紧随其后的
四个允许 cofactor。令

\[
x=\frac ad,\qquad
f_{C,\ell,\sigma}(x)
=x^2+(5\sigma-4C+\ell)x+3\sigma^2.
\tag{37t-1}
\]

因为 \(d>1\) 为奇数且 \(d\equiv1\pmod3\)，有 \(d\ge7\)。由 (37q)，

\[
F_{C,\sigma,\ell}(a)
=d^2f_{C,\ell,\sigma}(x)-d(x+\sigma)+1.
\tag{37t-2}
\]

对 \(C\in\{25,28,31,34\}\)，式 (37m)、(37o) 和
\(\sigma\equiv1\pmod6\) 给出的全部可能行如下。表中负号栏满足
\(f_{C,\ell,\sigma}(x)<0\) 于整个区间
\(\ell-4\le x<\ell\)；正号栏满足 \(f_{C,\ell,\sigma}(x)\ge87\)。

\[
\begin{array}{c|c|c|c}
C&\ell& f<0& f\ge87\\
\hline
25&12&1,7&13,19,25\\
25&36&1&7\\
28&24&1,7&13,19\\
28&48&1&\varnothing\\
31&12&1,7&13,19,25,31\\
31&36&1,7&13\\
34&24&1,7,13&19,25\\
34&48&1,7&13
\end{array}
\tag{37t-3}
\]

这是纯手算的二次区间表：例如每一行只需检查 \(f\) 的两个端点和其唯一顶点。负号栏使
\(F<0\)；正号栏则由 \(d\ge7\)、\(x+\sigma<61\) 给出

\[
F\ge49\cdot87-7\cdot61+1>0.
\tag{37t-4}
\]

故表中各行均与 \(F=0\) 矛盾。唯一未列入 (37t-3) 的允许行是

\[
(C,\ell,\sigma)=(31,60,1).
\tag{37t-5}
\]

此时 \(56d\le a<60d\)，且 (37x) 化为

\[
3718d-63a+62=q(2a+3d).
\tag{37t-6}
\]

左边必须为正，而其最大值小于 \(2(2a+3d)\)；所以正整数 \(q\) 只能为 \(1\)。
于是

\[
65a=3715d+62,
\tag{37t-7}
\]

但右边模 \(5\) 为 \(2\)，矛盾。至此 \(C=25,28,31,34\) 全部被排除。结合
\(C\equiv1\pmod3\) 与 (37s-3)，得到

\[
\boxed{d>1\quad\Longrightarrow\quad C_d\ge37\quad(m=3).}
\tag{37t-8}
\]

又 \(s_d\equiv3\pmod4\) 保证 \(4d-s_d\ge1\)。因此

\[
p-36s_d
=C_d(4d-s_d)+(C_d-37)s_d
\ge37,
\]

从而有更强的 natural-gap bound

\[
\boxed{s_d\le\frac{p-37}{36}.}
\tag{37t-9}
\]

这仍是 actual cofactor/gap 收缩，不断言 natural fan 必命中。

### 8.3 whole-\(d\) residual 的 primitive norm kernel

上面的低 cofactor 排除还没有用尽 actual quotient content。令

\[
n:=\frac{\delta^2+\delta+1}{h},
\qquad
q:=\frac nd,
\qquad
\tau:=\frac\gamma d,
\qquad
k_0:=\frac kd.
\tag{37u}
\]

既有 whole-\(d\) alignment 保证这些都是正整数，并给出

\[
\tau=\sigma\delta-aq,
\qquad
qk_0=\sigma^2+\sigma\tau+\tau^2,
\qquad
(\sigma,\tau)=1.
\tag{37v}
\]

第二式模 \(\sigma\) 为 \(qk_0\equiv\tau^2\pmod\sigma\)，而第一式模
\(\sigma\) 为 \(\tau\equiv-aq\pmod\sigma\)。因此

\[
\boxed{(\sigma,aqk_0)=1.}
\tag{37w}
\]

特别地 \((\sigma,A)=1\)，因为 \(a=3A\) 且 \(\sigma\equiv1\pmod6\)。若写

\[
\mu:=4C_d-\ell-3\sigma,
\]

则 \(\delta=\mu d-a\)、\(h=2a+3d\sigma\)，且用 (37q) 消去 \(a^2\) 后，
\(h\mid\delta^2+\delta+1\) 的全部内容精确成为

\[
\boxed{
\bigl[(\mu^2-3\sigma^2)d-(\mu+2\sigma)a+\mu+\sigma\bigr]
=q(2a+3d\sigma).
}
\tag{37x}
\]

这正是 (37r) 和 (37s-1) 中出现的整数商；它不是一个可自由选择的 divisibility
witness。式 (37q)、(37v)、(37w)、(37x) 将 \(m=3,d>1\) 的剩余问题压成一组
互锁的 primitive Diophantine constraints。它仍没有把 Eisenstein factor quotient 变成
ordinary state，也没有给出 E1 provenance、E4 lift 或 T5 ticket。

### 8.3.1 fixed-cofactor primitive kernel 的二次消元

这组 kernel 还给出一个不依赖 \(p\) 范围的 exact finite reduction。令

\[
M=4C_d-\ell,
\qquad
\mathcal D=M\tau-\bigl(\sigma^2+5\sigma\tau+3\tau^2\bigr).
\tag{37x-0}
\]

由 \(a\gamma=\eta(\eta+1)-k\)、\(\eta+1=d\sigma\) 与 (37u)，有

\[
a\tau=\sigma^2d-\sigma-k_0.
\tag{37x-0a}
\]

把它代入 (37q) 并乘以 \(\tau^2\)，得到只含 \(d\) 的精确二次方程

\[
\boxed{
\begin{aligned}
0={}&-\sigma^2\mathcal D\,d^2\\
&+\bigl[(\sigma+k_0)(\mathcal D-\sigma^2+3\tau^2)
-\sigma\tau(\sigma+\tau)\bigr]d\\
&+(\sigma+k_0)^2+\tau(\sigma+k_0)+\tau^2.
\end{aligned}}
\tag{37x-0b}
\]

其常数项严格为正，所以它不可能退化为零多项式。由
\(C_d\equiv1\pmod3\)、(37m) 与 \(\ell>0\)，有 \(\ell\equiv0\pmod {12}\)，
故 \(\ell\ge12\)。固定 \(C_d\) 后，(37m)、(37o) 使
\(\ell,\sigma\) 只有有限多个可能值；又由 (37x-0a) 和
\(a\ge(\ell-4)d\)，有

\[
0<\tau<\frac{\sigma^2}{\ell-4}.
\tag{37x-0c}
\]

最后 \(k_0\mid\sigma^2+\sigma\tau+\tau^2\) 由 (37v) 给出。因此每个固定
\(C_d\) 的 actual whole-\(d\) packet 至多留下有限个
\((\ell,\sigma,\tau,k_0,d)\)：对每个已定的前四元组，(37x-0b) 至多给出两个
整数 \(d\)。这是 exact Diophantine reduction，不断言这些有限 packet 实际可达，
也不提供 natural-fan hit。

### 8.3.2 primitive norm kernel 排除 \(C_d=37\)

现在假设 \(C=37\)。由 (37m)、(37o) 与
\(\sigma\equiv1\pmod6\)，所有可能的 \((\ell,\sigma)\) 为

\[
\begin{array}{c|c}
\ell&\sigma\\
\hline
12&1,7,13,19,25,31,37\\
36&1,7,13,19,25\\
60&1,7
\end{array}
\tag{37x-1}
\]

对这些有限行再次检查 (37t-1) 的端点和顶点，得到

\[
\begin{array}{c|c|c}
\ell&f<0&f\ge27\\
\hline
12&1,7&19,25,31,37\\
36&1,7&13,19,25\\
60&1&7
\end{array}
\tag{37x-1a}
\]

唯一未列入两栏的是 \((\ell,\sigma)=(12,13)\)。负号栏在相应区间有
\(f<0\)，正号栏有 \(f\ge27\)。
前者给出 \(F<0\)；后者由 \(d\ge7\) 与 \(x+\sigma<67\) 给出

\[
F\ge49\cdot27-7\cdot67+1>0.
\tag{37x-2}
\]

因此只须处理

\[
C=37,\qquad \ell=12,\qquad \sigma=13.
\tag{37x-3}
\]

写 \(a=8d+t\)。由 \(a\) 为奇数、\(a\equiv9\pmod {24}\) 及
\(d\equiv1\pmod3\)，有

\[
0<t<4d,\qquad t\equiv1\pmod {24}.
\tag{37x-4}
\]

在 (37q) 中代入这条线得到

\[
F=t^2-(55d+1)t+3d^2-21d+1.
\tag{37x-5}
\]

在 \(0\le t<4d\) 上，这个二次式对 \(t\) 严格递减；又 \(d\ge7\) 时
\[
F(0)=3d^2-21d+1>0,
\]
而
\[
F\!\left(\frac d{18}\right)
=-\frac{17}{324}d^2-\frac{379}{18}d+1<0.
\]
所以若 \(F=0\)，必有

\[
\boxed{0<t<\frac d{18}.}
\tag{37x-6}
\]

这时 \(\eta+1=d\sigma=13d\)。由
\(k=e\eta-aW\)、\(e=a+\eta+1\) 与 \(W=\eta+\gamma\) 直接得到 complementary identity
\[
a\gamma=\eta(\eta+1)-k.
\]
结合 (37u)，得到

\[
a\tau=169d-13-k_0,
\qquad
\tau t=(169-8\tau)d-13-k_0.
\tag{37x-7}
\]

因 \(k_0>0\)、\(a\ge8d\)、\(\tau\) 为奇数且 \((13,\tau)=1\)，

\[
\tau\in\{1,3,5,7,9,11,15,17,19,21\}.
\tag{37x-8}
\]

另一方面，(37v) 给出

\[
qk_0=N_\tau:=\tau^2+13\tau+169,
\qquad
k_0\le N_\tau.
\tag{37x-9}
\]

若 \(\tau\le19\)，由 (37x-6)--(37x-7) 有

\[
\left(169-\frac{145}{18}\tau\right)d
<13+N_\tau.
\tag{37x-10}
\]

相应的数值界为

\[
\begin{array}{c|ccccccccc}
\tau&1&3&5&7&9&11&15&17&19\\
\hline
N_\tau&183&217&259&309&367&433&589&679&777\\
d<&2&2&3&3&4&6&13&22&50
\end{array}
\tag{37x-11}
\]

而 (37x-6) 与 \(t\ge1\) 已给出 \(d>18\)。所以
\(\tau\le15\) 不可能。若 \(\tau=17\)，则 \(d=19\) 且 \(t=1\)；若
\(\tau=19\)，则同样 \(t=1\)。但 (37x-5) 在 \(t=1\) 时成为

\[
3d^2-76d+1=0,
\]

其判别式 \(5764\) 严格位于 \(75^2\) 与 \(76^2\) 之间，故两种情形均不可能。

最后，若 \(\tau=21\)，则 (37x-7) 给出

\[
d=21t+13+k_0.
\tag{37x-12}
\]

这里 \(k_0\mid N_{21}=883\)，故 \((k_0,6)=1\)。由
\(t\equiv1\pmod {24}\) 得右端模 \(6\) 只能为 \(3\) 或 \(5\)，
却与 \(d\equiv1\pmod6\) 矛盾。因此 \(C=37\) 也不可能。结合
\(C\equiv1\pmod3\) 和 (37t-8)，有

\[
\boxed{d>1\quad\Longrightarrow\quad C_d\ge40\quad(m=3).}
\tag{37x-13}
\]

同样地

\[
p-39s_d
=C_d(4d-s_d)+(C_d-40)s_d
\ge40,
\]

所以

\[
\boxed{s_d\le\frac{p-40}{39}.}
\tag{37x-14}
\]

这仍只收缩 actual natural fan，不蕴涵 terminal hit 或 physical successor。

### 8.4 即使加入 cofactor congruence lock，\(\Phi_6\) envelope 也不会强制 fan hit

上一节的结论不能被错误加强为“所有满足已使用的 \(\Phi_6\) carrier package 和
cofactor congruence lock 的整数都命中 natural fan”。事实上，下面给出一个完全手算的
formal countermodel：

\[
p=4729,\qquad d=13,\qquad s=3,\qquad C=91,
\qquad \ell=12,\qquad a=153.
\tag{37y}
\]

这里 \(4729\equiv1\pmod {24}\)，且因 \(\sqrt {4729}<69\)，逐一排除不超过
\(67\) 的素数后可知 \(4729\) 为素数。并且

\[
p+s=4732=4dC,\qquad
s\equiv-p\pmod d,\qquad
s\equiv3\pmod4,
\qquad
s=\ell d-a,\qquad
p-a=(4C-\ell)d,
\tag{37z}
\]

\[
13\mid4729^2-4729+1,
\qquad
13\mid3^2+3+1.
\tag{37aa}
\]

它还满足

\[
C\ge40,\qquad s\le\frac{p-40}{39},\qquad
C\equiv1\pmod3,\qquad
4C-\ell\equiv16\pmod {24},
\tag{37ab}
\]

并有 \(a\equiv9\pmod {24}\)、\(\ell\equiv0\pmod6\)。但 natural fan 的完整因子
\(x=dC=1183=7\cdot13^2\) 的除子只有

\[
1,7,13,91,169,1183,
\]

它们模 \(3\) 全部为 \(1\)，没有一个为 \(-1\)。故

\[
\nexists\,t\mid1183\quad t\equiv-1\pmod {3}.
\tag{37ac}
\]

这个六元组没有被声称为 actual stutter receipt：它没有重建 \(A,u,\rho,\kappa\)、
(37q) 的 double-norm gate、(37v)--(37x) 的 primitive kernel、maximality 或 E1
provenance。因此它不反驳 O2、T6 或任何
actual terminal theorem。它严格说明的是，任何想从

\[
d\mid\Phi_6(p),\qquad
d\mid\Phi_3(s_d),\qquad
C_d\ge40,
\qquad
4C_d-\ell\equiv16\pmod {24}
\]

**单独**推导 natural-fan hit 的证明都会失败；下一条全称引理必须使用尚未消费的
actual double-norm gates、receipt-capacity 或构造一条新的 physical adapter。

### 8.5 natural gap \(s_d=3\) 的 exact \(13\)-adic double-norm core

formal packet (37y) 说明单凭 \(\Phi_6/\Phi_3\) envelope 不能排除 \(s_d=3\)。但在
actual \(m=3\) receipt 中，这个 gap 不能保留任意的 \((d,\ell,\sigma)\)。以下给出它由
两张范数门和 whole-\(d\) primitive kernel 强制出的精确必要核。

继续假设 \(d>1\) 且

\[
s_d=3.
\tag{37ad}
\]

由 (37) 立刻有 \(d\mid3^2+3+1=13\)，故

\[
\boxed{d=13.}
\tag{37ae}
\]

再由 \(s_d=\ell d-a\)、\(a=3A\) 和 \(A\equiv3\pmod {24}\)，得到

\[
\ell\equiv12\pmod {24},
\qquad
\ell=12t,
\qquad
A=52t-1,
\qquad
t\equiv1\pmod6.
\tag{37af}
\]

这里 \(t>0\)。事实上 \(a=13\ell-3\)，而 \(a\equiv9\pmod {24}\) 给出
\(\ell\equiv12\pmod {24}\)；随后 \(A=13\ell/3-1\)，再用
\(A\equiv3\pmod {24}\) 即得 \(t\equiv1\pmod6\)。

另一方面，(26) 的 \(\eta=3\rho\) 与 (37a) 给出

\[
3\rho+1=13\sigma.
\tag{37ag}
\]

把它与 (27b) 的 \(\rho\equiv16\pmod {18}\) 联立。若
\(\rho=16+18n\)，则 (37ag) 模 \(13\) 强制 \(n\equiv8\pmod {13}\)。
正性因而给出唯一的参数化

\[
\boxed{
\rho=160+234z,
\qquad
\sigma=37+54z,
\qquad z\in\mathbb Z_{\ge0}.
}
\tag{37ah}
\]

特别地，这里不是一般 whole-\(d\) 分析中仅有的
\(\sigma\equiv1\pmod6\)，而是实际 \(m=3\) root gate 强制的
\(\sigma\equiv37\pmod {54}\)。

设

\[
u=2A+3\rho+1=104t+702z+479.
\tag{37ai}
\]

除了已有的 \(A\mid9\rho^2+5\rho+1\) 外，(26) 还给出一个对称的第二除子门。恒等式

\[
4(A^2+A\rho+\rho^2)
=(2A-\rho-1)(2A+3\rho+1)
+(7\rho^2+4\rho+1)
\tag{37aj}
\]

与 \(u\mid A^2+A\rho+\rho^2\) 及 \(u\) 为奇数等价地给出

\[
\boxed{u\mid7\rho^2+4\rho+1.}
\tag{37ak}
\]

由于 \(13\mid k=3\kappa\)，写 \(\kappa=13K\)。把 (37af)--(37ai) 代入两张
范数门，得到两个显式整数商

\[
\begin{aligned}
\lambda
&:=\frac{9\rho^2+5\rho+1}{A}
=\frac{492804z^2+675090z+231201}{52t-1},\\
K
&:=\frac{A^2+A\rho+\rho^2}{13u}\\
&=\frac{208t^2+936tz+632t+4212z^2+5742z+1957}
{104t+702z+479}.
\end{aligned}
\tag{37al}
\]

二者都必须是正整数；并且 (27e) 给出

\[
\boxed{K\equiv19\pmod {24}.}
\tag{37am}
\]

最后保留 whole-\(d\) 的 primitive content。写
\(\gamma=13\tau\)；由 \(k=3\kappa=39K\)、
\(k=\eta(\eta+1)-a\gamma\) 及 \(d=(\gamma,k)=13\)，有

\[
\boxed{
\begin{aligned}
(156t-3)\tau&=13\sigma^2-\sigma-3K,\\
3qK&=\sigma^2+\sigma\tau+\tau^2,\\
(\sigma,\tau)&=1,
\qquad
(\tau,3K)=1,
\end{aligned}}
\tag{37an}
\]

其中 \(q>0\) 是 (37u) 的 \(n/d\) 商。第二个互素条件正是
\(d=(13\tau,39K)=13\) 的 exactness，而不是把 \(13\mid k\) 作为松弛条件。

相应的核心素数和 cofactor 也不再自由：令 \(C=C_d\)，则

\[
\boxed{
p=312t+3510z+2398+\lambda=52C-3,
\qquad
52C=312t+3510z+2401+\lambda,
}
\tag{37ao}
\]

其中 \(p\) 仍须为核心素数，且既有结论保留

\[
C\ge40,
\qquad C\equiv1\pmod6,
\qquad
\lambda\equiv43-26z\pmod {52}.
\tag{37ap}
\]

最后一个同余只是 (37ao) 的可整除性重写；它不是新的 terminal predicate。

该核也精确描述 gap-\(3\) natural linear fan 的剩余。此时
\(x=dC=13C\)，所以

\[
\left\{\zeta\mid x:\ \zeta\equiv-1\pmod3\right\}=\varnothing
\quad\Longleftrightarrow\quad
\text{every prime divisor of }C\text{ is }1\pmod3.
\tag{37aq}
\]

左侧一旦失败，(54u) 已给出 direct Type II terminal；反向则因为
\(13\equiv1\pmod3\)、\(C\equiv1\pmod3\) 而成立。因此，\(s_d=3\) 的真正
remaining problem 不是 \(d\mid\Phi_3(s_d)\) 或 cofactor lower bound，而是：
是否能从 (37af)--(37an) 排除 (37aq)，或在它成立时构造不依赖 quotient rechart 的
actual E1--E5 adapter。

本节只给出 actual receipt 的一向 Diophantine reduction。它不声称任一满足
(37af)--(37ap) 的整数包可重建 maximal receipt，更不证明该核为空、natural fan 必命中
或 T6 的任何出口。

### 8.5.1 primitive quotient \(q\) 不能提供 gap-\(3\) fan residue

仍在 (37ad) 的 actual packet 中。由 (37ah)，有
\(\sigma\equiv1\pmod9\)；由 (37am)，有 \(K\equiv1\pmod3\) 且 \(K\) 为奇数。
再由 (31a) 前的 parity conclusion，\(\gamma\) 为奇数，故
\(\tau=\gamma/13\) 也为奇数。把这些信息代入 (37an) 的第二式。

首先 \((\tau,3K)=1\) 给出 \(3\nmid\tau\)。模 \(3\) 化简

\[
3qK=\sigma^2+\sigma\tau+\tau^2
\tag{37ar}
\]

可知 \(\tau\equiv1\pmod3\)：若 \(\tau\equiv-1\pmod3\)，右侧即为
\(1-1+1\not\equiv0\pmod3\)。写 \(\tau=1+3w\)，并使用
\(\sigma\equiv1\pmod9\)，则

\[
\sigma^2+\sigma\tau+\tau^2\equiv3\pmod9.
\tag{37as}
\]

因为 \(3\parallel3K\)，(37ar)--(37as) 给出 \(3\nmid q\)。另一方面，等式右侧为
奇数，而 \(3K\) 也为奇数，所以 \(q\) 为奇数。由 (37w)，\((q,\sigma)=1\)。若素数
\(r\mid q\)，则 \(r\ne3\)，且模 \(r\) 有

\[
\left(\tau\sigma^{-1}\right)^2+\tau\sigma^{-1}+1\equiv0\pmod r.
\tag{37at}
\]

其中 \(\tau\sigma^{-1}\ne1\)，否则会推出 \(r=3\)。故它在
\(\mathbb F_r^\times\) 中有阶 \(3\)，从而 \(r\equiv1\pmod3\)。此外，若一个素数同时
整除 \(\tau\) 与 \(q\)，则 (37ar) 模该素数会强制它整除 \(\sigma\)，与
\((\sigma,\tau)=1\) 矛盾。还可把 (37an) 的第一式模 \(4\) 化简：
\(156t-3\equiv1\pmod4\)、\(K\equiv3\pmod4\) 及 \(\sigma^2\equiv1\pmod4\)
给出

\[
\tau\equiv-\sigma\pmod4.
\tag{37at-1}
\]

因此 (37ar) 模 \(4\) 的右侧为 \(1-1+1\equiv1\pmod4\)，而
\(3K\equiv1\pmod4\)，从而 \(q\equiv1\pmod4\)。于是

\[
\boxed{
\tau\equiv1\pmod6,
\qquad
q\equiv1\pmod {12},
\qquad
(\tau,q)=1,
\qquad
r\mid q\Longrightarrow r\equiv1\pmod3.
}
\tag{37au}
\]

这不是把 \(q\) 识别为 \(13C\) 的除子，也不是新的 terminal。它只排除了一个常见但
无效的尝试：不能从 primitive quotient \(q\) 本身抽取 \(\zeta\equiv-1\pmod3\) 来完成
gap-\(3\) natural fan。因而 (37aq) 成立时，尚未解决的工作确实是 \(C\) 的因子结构或一条
新的 actual E1--E5 adapter。

### 8.5.2 \(q=1\) primitive leaf 的全称排空

上节的 \(q\equiv1\pmod {12}\) 仍允许 \(q=1\)。这一最小 leaf 实际上与两张范数门不相容。
若 \(q=1\)，则 (37u) 给出

\[
\frac{\delta^2+\delta+1}{h}=n=d=13.
\tag{37av}
\]

由 \(h=2a+3d\sigma=2a+39\sigma\)，有

\[
\delta^2+\delta+1=26a+507\sigma.
\tag{37aw}
\]

另一方面，(27a)、(37ag) 与 \(h=6A+9\rho+3\) 给出

\[
\delta=p-h=6\rho+1+\lambda=26\sigma-1+\lambda.
\tag{37ax}
\]

又因为 \(a=3A\)，把 (37ag) 代入 \(\lambda=(9\rho^2+5\rho+1)/A\)，得到

\[
a\lambda=507\sigma^2-13\sigma+1.
\tag{37ay}
\]

将 (37ax) 代入 (37aw) 可写成

\[
26a
=676\sigma^2+(52\lambda-533)\sigma+\lambda^2-\lambda+1.
\tag{37az}
\]

先证明 \(\lambda<21\)。若 \(\lambda\ge21\)，则
\(\delta\ge26\sigma+20\)，故由 (37aw)

\[
a\ge\frac{676\sigma^2+559\sigma+421}{26}.
\tag{37ba}
\]

但 (37ay) 同时给出

\[
a\le\frac{507\sigma^2-13\sigma+1}{21}.
\tag{37bb}
\]

两个界不相容，因为左边分子乘 \(21\) 后减去右边分子乘 \(26\) 等于

\[
1014\sigma^2+12077\sigma+8815>0.
\tag{37bc}
\]

而 (27b) 的 \(\lambda\equiv3\pmod6\) 与 \(\lambda>0\) 于是只留下
\(\lambda\in\{3,9,15\}\)。将 (37ay) 代入 (37az)，令其两边之差为

\[
F_\lambda(\sigma):=
\lambda\bigl[676\sigma^2+(52\lambda-533)\sigma+\lambda^2-\lambda+1\bigr]
-26(507\sigma^2-13\sigma+1).
\tag{37bd}
\]

则必须有 \(F_\lambda(\sigma)=0\)。但三个仅余多项式分别为

\[
\begin{array}{c|c}
\lambda&F_\lambda(\sigma)\\
\hline
3&-11154\sigma^2-793\sigma-5\\
9&-7098\sigma^2-247\sigma+631\\
15&-3042\sigma^2+4043\sigma+3139.
\end{array}
\tag{37be}
\]

前两行对 \(\sigma\ge1\) 严格为负；第三行从 \(\sigma=2\) 起严格递减且
\(F_{15}(2)=-943\)。而 (37ah) 给出 \(\sigma\ge37\)，故三行均不可能为零。结合
(37au) 的 \(q\equiv1\pmod {12}\)，排除 \(q=1\) 后得到

\[
\boxed{
\text{actual }m=3,\ d>1,\ s_d=3
\quad\Longrightarrow\quad q\ge13.
}
\tag{37bf}
\]

这是一条 family-empty proof，只排空 gap-\(3\) core 的 \(q=1\) primitive leaf。它不对
\(q>1\) 建立 terminal 或 E1--E5 successor，也不把 (37bf) 提升为 QC1 或 T6 的闭合。

### 8.5.3 \(q=13\) primitive leaf 的全称排空

下一允许值 \(q=13\) 也可由同一 exact core 排除。此时
\(n=dq=169\)，故 (37ax) 与 \(h=2a+39\sigma\) 给出

\[
338a
=676\sigma^2+(52\lambda-6617)\sigma+\lambda^2-\lambda+1.
\tag{37bg}
\]

先有 \(\lambda<255\)。否则 \(\delta\ge26\sigma+254\)，从而

\[
a\ge
\frac{676\sigma^2+6643\sigma+64771}{338}.
\tag{37bh}
\]

但 (37ay) 给出 \(a\le(507\sigma^2-13\sigma+1)/255\)。这与 (37bh) 矛盾，
因为其交叉相减为

\[
1014\sigma^2+1698359\sigma+16516267>0.
\tag{37bi}
\]

现在使用 (37ap) 的 \(\lambda\equiv43-26z\pmod {52}\)。若 \(z\) 为偶数，则
\(\lambda\equiv43\pmod {52}\)；若 \(z\) 为奇数，则
\(\lambda\equiv17\pmod {52}\)。结合 \(0<\lambda<255\) 与
\(\lambda\equiv3\pmod6\)，只剩

\[
z\equiv0\pmod2\Longrightarrow\lambda=147,
\qquad
z\equiv1\pmod2\Longrightarrow\lambda\in\{69,225\}.
\tag{37bj}
\]

把 (37ay) 代入 (37bg)，记

\[
\begin{aligned}
G_\lambda(\sigma):={}&
\lambda\bigl[676\sigma^2+(52\lambda-6617)\sigma+\lambda^2-\lambda+1\bigr]\\
&-338(507\sigma^2-13\sigma+1).
\end{aligned}
\tag{37bk}
\]

则 \(G_\lambda(\sigma)=0\) 是必要条件。三个剩余多项式及其实际范围如下：

\[
\begin{array}{c|c|c}
\lambda&G_\lambda(\sigma)&\text{applicable }\sigma\\
\hline
69&-124722\sigma^2-204607\sigma+323479&\sigma\ge91\\
147&-71994\sigma^2+155363\sigma+3154723&\sigma\ge37\\
225&-19266\sigma^2+1148069\sigma+11339887&\sigma\ge91.
\end{array}
\tag{37bl}
\]

第一行从 \(\sigma=1\) 起严格为负。第二行从 \(\sigma=2\) 起递减，且
\(G_{147}(37)=-89656632\)；第三行从 \(\sigma=91\) 起递减，且
\(G_{225}(91)=-43727580\)。故 (37bj) 的每个可能性都矛盾，进而

\[
\boxed{q\ne13.}
\tag{37bm}
\]

结合 (37au)、(37bf) 以及 \(r\mid q\Rightarrow r\equiv1\pmod3\)，若
\(1<q<37\)，唯一尚未排除的 \(q\equiv1\pmod {12}\) 数是 \(25\)，但它含有
\(5\equiv2\pmod3\) 的素因子。因此这个 actual gap-\(3\) core 必满足

\[
\boxed{q\ge37.}
\tag{37bn}
\]

这仍只是在 proper-root receipt 内排除两个 primitive leaves。它没有对
\(q\ge37\) 构造 terminal、actual successor 或 physical E1--E5 adapter。

### 8.5.4 \(q\)-residual 的统一二次 normal form

前两节的比较并不依赖 \(q=1\) 或 \(q=13\)。一般地，由
\(n=dq=13q\)、(37ax) 与 \(h=2a+39\sigma\)，所有剩余 packet 都满足

\[
26qa
=676\sigma^2+(52\lambda-26-507q)\sigma+\lambda^2-\lambda+1.
\tag{37bo}
\]

配合 (37ay)，消去 \(a\) 后得到一条必要的二次曲线

\[
\boxed{
\begin{aligned}
\mathcal G_{q,\lambda}(\sigma):={}&
\lambda\bigl[
676\sigma^2+(52\lambda-26-507q)\sigma+\lambda^2-\lambda+1
\bigr]\\
&-26q(507\sigma^2-13\sigma+1)=0.
\end{aligned}}
\tag{37bp}
\]

这条曲线还有一个统一的 upper slope bound：

\[
\boxed{\lambda<\frac{39q+3}{2}.}
\tag{37bq}
\]

事实上，反设 \(\lambda\ge(39q+3)/2\)。由 (37ax) 可得

\[
26qa\ge
676\sigma^2+(507q+52)\sigma+\frac{1521q^2+156q+7}{4}.
\tag{37br}
\]

另一方面，(37ay) 给出

\[
a\le\frac{2(507\sigma^2-13\sigma+1)}{39q+3}.
\tag{37bs}
\]

将 (37br) 与 (37bs) 交叉相乘，左减右为

\[
\begin{aligned}
&2028\sigma^2+(19773q^2+4225q+156)\sigma\\
&\qquad+\frac{59319q^3+10647q^2+533q+21}{4}>0,
\end{aligned}
\tag{37bt}
\]

矛盾，故 (37bq) 成立。再用 (37au) 的 \(q\equiv1\pmod {12}\) 和
\(\lambda\equiv3\pmod6\)，可写成更便于枚举 divisor fibers 的整型界

\[
\lambda\le\frac{39q-9}{2}.
\tag{37bu}
\]

因此尚未排空的 \(s_d=3\) actual packet 必同时满足

\[
\begin{gathered}
q\ge457,\qquad q\equiv1\pmod {12},\qquad
\sigma=37+54z,\qquad z\ge0,\\
\lambda>0,\qquad
\lambda\equiv3\pmod6,\qquad
\lambda\equiv43-26z\pmod {52},\qquad
\lambda\le\frac{39q-9}{2},\\
\mathcal G_{q,\lambda}(\sigma)=0,\qquad
a=\frac{507\sigma^2-13\sigma+1}{\lambda}=156t-3,\qquad
t>0,\quad t\equiv1\pmod6.
\end{gathered}
\tag{37bv}
\]

它仍须同时通过 (37al)、(37an) 的 \(K,\tau\) exactness；因此 (37bv) 是
Diophantine residual 的必要 normal form，不是对 actual receipts 的反向构造。
要关闭这个 residual，仍需要一条全称无限下降、一个 new terminal mechanism，或
带完整 E1--E5 的 physical adapter。

### 8.5.5 未消费 \(-27\) 范数门的 \(u\)-bridge

(37bv) 尚未使用 \(u\mid7\rho^2+4\rho+1\) 的完整商。定义

\[
S:=\frac{7\rho^2+4\rho+1}{u}\in\mathbb Z_{>0}.
\tag{37bw}
\]

由 \(\rho\equiv7\pmod9\)，分子恰为 \(3\pmod9\)；又 \(u\equiv1\pmod3\) 且
二者均为奇数。因此

\[
S\equiv3\pmod6.
\tag{37bx}
\]

把 \(3\rho+1=13\sigma\) 代入 (37bw)，有

\[
9uS=1183\sigma^2-26\sigma+4.
\tag{37by}
\]

另一方面，(37ay) 和 \(3u=2a+39\sigma\) 给出

\[
3\lambda u
=2(507\sigma^2-13\sigma+1)+39\lambda\sigma
=1014\sigma^2+(39\lambda-26)\sigma+2.
\tag{37bz}
\]

用 \(7\) 倍 (37bz) 减去 \(6\) 倍 (37by)，消去二次项，得到 exact linear bridge

\[
\boxed{
(273\lambda-26)\sigma-10
=u(21\lambda-54S).
}
\tag{37ca}
\]

左侧严格为正，故

\[
0<S<\frac{7\lambda}{18}.
\tag{37cb}
\]

同一 \(S\) 还把 \(q\)-quotient 与第二范数商直接耦合。由
\(\delta^2+\delta+1=39qu\)、(37ax) 与 (37bw)，有

\[
\boxed{
3u(91q-12S)
=(364\lambda-78)\sigma+7\lambda^2-7\lambda-9.
}
\tag{37cc}
\]

右侧严格为正；令

\[
R_{q,S}:=91q-12S,
\]

则

\[
\boxed{
R_{q,S}>0,
\qquad
R_{q,S}\equiv7\pmod {12}.
}
\tag{37cd}
\]

这里的结论只针对这个**复合 defect 整数本身**；它并不推出一个
\(7\pmod {12}\) 的素因子（例如 \(55\equiv7\pmod {12}\)）。\(R_{q,S}\) 也尚未证明整除
\(u\)、\(d\)、\(D_*\) 或 \(\kappa\)。因此它目前不是可直接消费的 source carrier，
更不是 terminal 或 E1--E5 adapter。它的价值在于把原先彼此独立的 \(q\)-residual 与
\(-27\) norm quotient 合成了单个 \(7\pmod {12}\) composite defect equation。

### 8.5.6 primitive \(\tau\)-bridge 的小 \(q\) 区间排空

除了 \(u\)-bridge，还可把 (37an) 的两个 primitive identities 与 (37ay) 直接
耦合。定义

\[
\theta:=\lambda-39\tau.
\]

由 (37an) 的第一式和 (37ay)，有

\[
\begin{aligned}
a\theta
&=a\lambda-39a\tau\\
&=(507\sigma^2-13\sigma+1)
-39(13\sigma^2-\sigma-3K)\\
&=26\sigma+1+117K>0.
\end{aligned}
\tag{37ce}
\]

又由 \(\lambda\equiv3\pmod6\) 和 \(\tau\equiv1\pmod6\)，有
\(\theta\equiv0\pmod6\)。式 (37ce) 模 \(13\) 化简为
\(a\theta\equiv1\pmod {13}\)；而 \(a=156t-3\equiv-3\pmod {13}\)，故

\[
\boxed{\theta\equiv30\pmod {78},\qquad \theta\ge30.}
\tag{37cf}
\]

将此与 (37bu) 联立，得到

\[
39\tau+30\le\lambda\le\frac{39q-9}{2}.
\]

因为 \(q\) 为奇数，遂有

\[
\boxed{q\ge2\tau+3,\qquad \tau\le\frac{q-3}{2}.}
\tag{37cg}
\]

这里的 \(\theta\) 还保留了 \(z\) 的一个实际 parity mark。由 \(t\equiv1\pmod6\)、
\(K\equiv19\pmod {24}\) 与 \(\sigma=37+54z\)，将 (37ce) 模 \(24\) 化简为

\[
9\theta\equiv18+12z\pmod {24}.
\]

因此 \(z\) 偶时 \(\theta\equiv18\pmod {24}\)，而 \(z\) 奇时
\(\theta\equiv6\pmod {24}\)。再与 (37cf) 联立，得到精确的两支：

\[
\boxed{
\begin{array}{c|c|c}
z\bmod2&\sigma\text{ 的下界}&\theta\text{ 的同余与下界}\\
\hline
0&\sigma\ge37&\theta\equiv186\pmod {312},\quad\theta\ge186\\
1&\sigma\ge91&\theta\equiv30\pmod {312},\quad\theta\ge30.
\end{array}}
\tag{37cg-1}
\]

在第一支，将 \(\theta\ge186\) 代回 (37bu)，并再次使用 \(q\) 为奇数，给出

\[
\boxed{z\equiv0\pmod2\Longrightarrow q\ge2\tau+11,
\qquad \tau\le\frac{q-11}{2}.}
\tag{37cg-2}
\]

另一方面，从 (37an) 消去 \(K\)：

\[
q(13\sigma^2-\sigma-a\tau)=\sigma^2+\sigma\tau+\tau^2.
\]

乘以 \(\lambda=39\tau+\theta\)，再使用 (37ay)，得到必要二次式

\[
\boxed{
\begin{aligned}
\mathcal H_{q,\tau,\theta}(\sigma):={}&
\bigl[39\tau-(13q-1)\theta\bigr]\sigma^2\\
&+\bigl[26q\tau+39\tau^2+\theta(q+\tau)\bigr]\sigma\\
&+q\tau+39\tau^3+\theta\tau^2=0.
\end{aligned}}
\tag{37ch}
\]

这条式子可一次排除此前未处理的一段完整 \(q\) 区间。写 (37ch) 的三个系数为
\(A,B,C\)。在两支中都可使用 (37cg) 与 (37bu)，因此

\[
\begin{aligned}
B&<52q^2,\\
C&=q\tau+\lambda\tau^2<5q^3.
\end{aligned}
\tag{37ci}
\]

例如，直接代入 \(\tau\le(q-3)/2\)、\(\lambda\le(39q-9)/2\) 即得

\[
\begin{aligned}
B&\le26q\frac{q-3}{2}
+39\frac{(q-3)^2}{4}
+\frac{39q-9}{2}\frac{3q-3}{2}<52q^2,\\
C&\le q\frac{q-3}{2}
+\frac{39q-9}{2}\frac{(q-3)^2}{4}<5q^3.
\end{aligned}
\]

现在反设 \(37\le q\le433\)。若 \(z\) 为偶数，则 (37cg-2) 与
\(\theta\ge186\) 给出

\[
A\le-\frac{4797q+57}{2}.
\tag{37cj}
\]

又 \(\sigma\ge37\)，故

\[
\mathcal H'_{q,\tau,\theta}(\sigma)
<52q^2-37(4797q+57).
\tag{37ck}
\]

右侧在 \([37,433]\) 上递减，且其在 \(q=37\) 的值为
\(-6498014\)。所以 \(\mathcal H\) 在 \(\sigma\ge37\) 上严格递减；同时

\[
\mathcal H_{q,\tau,\theta}(37)
<F_0(q):=5q^3+1924q^2-\frac{1369(4797q+57)}2.
\tag{37cl}
\]

函数 \(F_0\) 严格凸，且

\[
F_0(37)=-118643016,
\qquad
F_0(433)=-655172130.
\]

因此这一个 parity 支不可能有 \(37\le q\le433\) 的解。

若 \(z\) 为奇数，则 (37cg-1) 给出 \(\sigma\ge91\)，而 (37cf)、(37cg) 给出

\[
A\le-\frac{741q+57}{2}.
\tag{37cm}
\]

于是

\[
\mathcal H'_{q,\tau,\theta}(\sigma)
<52q^2-91(741q+57).
\tag{37cn}
\]

该右侧同样在 \([37,433]\) 上递减，且其在 \(q=37\) 的值为
\(-2428946\)。故 \(\mathcal H\) 在 \(\sigma\ge91\) 上严格递减，且

\[
\mathcal H_{q,\tau,\theta}(91)
<F_1(q):=5q^3+4732q^2-\frac{8281(741q+57)}2.
\tag{37co}
\]

函数 \(F_1\) 也严格凸，其端点值为

\[
F_1(37)=-107024724,
\qquad
F_1(433)=-35616222.
\]

凸函数在闭区间上不超过其两个端点值的较大者，故第二支也矛盾。于是
\(37\le q\le433\) 完全排空。由 \(q\equiv1\pmod {12}\)，先有 \(q\ge445\)；但
\(445=5\cdot89\)，而 (37au) 已证明 \(q\) 的每个素因子都是 \(1\pmod3\)，所以
\(q\ne445\)。最终得到

\[
\boxed{
\text{actual }m=3,\ d>1,\ s_d=3
\quad\Longrightarrow\quad q\ge457.
}
\tag{37cp}
\]

这是一条 uniform Diophantine exclusion：它没有对 \(q\ge457\) 构造 terminal，
也没有把 quotient parameter 变成 actual source carrier。因此 QC1、TR1 与 T6 的
状态均不因 (37cp) 改变。

### 8.5.7 primitive norm 的 high-gap orientation

式 (37ch) 还蕴含一个不依赖有限 \(q\) 区间的 actual coordinate orientation。将其按
\(q\) 收集，定义

\[
\mathscr D:=13\theta\sigma^2-(26\tau+\theta)\sigma-\tau.
\]

则 (37ch) 等价于

\[
\boxed{
q\mathscr D=\lambda(\sigma^2+\sigma\tau+\tau^2)>0.
}
\tag{37cq}
\]

由 (37cg)，\(q-2\tau>0\)。从 (37cq) 减去 \(2\tau\mathscr D\)，并用
\(\lambda=39\tau+\theta\)，得到

\[
\begin{aligned}
(q-2\tau)\mathscr D={}&
-\bigl(26\theta\tau-39\tau-\theta\bigr)\sigma^2\\
&+(91\tau^2+3\theta\tau)\sigma\\
&+39\tau^3+(\theta+2)\tau^2.
\end{aligned}
\tag{37cr}
\]

反设 \(\tau\le\sigma\)。令

\[
E:=26\theta\tau-39\tau-\theta.
\]

由 \(\theta\ge30\)、\(\tau\ge1\)，有

\[
E-(132+4\theta)\tau
=(22\theta-171)\tau-\theta>0.
\tag{37cs}
\]

而 \(\tau\le\sigma\) 时，(37cr) 右边的全部正项不超过

\[
(132+4\theta)\tau\sigma^2:
\]

\[
\begin{aligned}
91\tau^2\sigma&\le91\tau\sigma^2,\\
3\theta\tau\sigma&\le3\theta\tau\sigma^2,\\
39\tau^3&\le39\tau\sigma^2,\\
(\theta+2)\tau^2&\le(\theta+2)\tau\sigma^2.
\end{aligned}
\]

式 (37cs) 因而使 (37cr) 的右边严格为负；但左边严格为正，矛盾。因此

\[
\boxed{\tau>\sigma.}
\tag{37ct}
\]

在 actual coordinates 中，这等价于

\[
\gamma=13\tau>13\sigma=\eta+1.
\]

另一方面，(31b) 与 \(\kappa=13K>0\) 给出

\[
A\gamma=3\rho^2+\rho-13K<\rho(3\rho+1)=\rho(\eta+1).
\]

所以

\[
\boxed{\gamma>\eta+1,\qquad A<\rho.}
\tag{37cu}
\]

又 \(\sigma\equiv\tau\equiv1\pmod6\)，故 \(\tau\ge\sigma+6\)。与
(37cg-1)、(37bu) 合并还给出 parameter-scale 下界

\[
\boxed{
z\equiv0\pmod2\Longrightarrow q\ge2\sigma+23,
\qquad
z\equiv1\pmod2\Longrightarrow q\ge2\sigma+15.
}
\tag{37cv}
\]

### 8.5.8 \(-11\) gate 排除 low-\(t\)，并强制 large-scale primitive residual

仍固定 \(d=13,s_d=3\)，并保留 (37af)、(37ah)、(37al)、(37an) 与 (37ce)。
先由

\[
\lambda=\frac{9\rho^2+5\rho+1}{A}\in\mathbb Z
\tag{37cw-0}
\]

排除最小的两个允许 \(t\)。若 \(t=1\)，则 \(A=51\)，故
\(17\mid9\rho^2+5\rho+1\)。该二次式的判别式为
\(-11\equiv6\pmod {17}\)，而 \(6\) 不是模 \(17\) 的平方，矛盾。若 \(t=7\)，
则 \(A=363=3\cdot11^2\)，故 \(121\mid9\rho^2+5\rho+1\)。但

\[
36(9\rho^2+5\rho+1)=(18\rho+5)^2+11.
\]

右侧若为 \(0\pmod {121}\)，模 \(11\) 先给出 \(11\mid18\rho+5\)，使平方项为
\(0\pmod {121}\)，右侧反而为 \(11\pmod {121}\)。因此，因
\(t>0\) 且 \(t\equiv1\pmod6\)，有

\[
\boxed{t\ge13.}
\tag{37cw}
\]

另一方面，(37cu) 的 \(0<A<\rho\)、\(u=2A+3\rho+1>3\rho\) 与 (37al) 给出

\[
13K=\frac{A^2+A\rho+\rho^2}{u}
<\frac{3\rho^2}{3\rho}=\rho.
\]

由于 \(3\rho+1=13\sigma\)，所以

\[
\boxed{K<\frac{\sigma}{3}.}
\tag{37cx}
\]

代回 (37ce) 得

\[
a\theta=26\sigma+1+117K<65\sigma+1.
\tag{37cy}
\]

偶 \(z\) 支有 \(\theta\ge186\)，故由 \(a=156t-3\)、
\(\sigma=37+54z\) 及 (37cw)，

\[
4836\cdot13<494+585z,
\]

所以 \(z\ge108\)。奇 \(z\) 支有 \(\theta\ge30\)，同理得到

\[
780\cdot13<416+585z,
\]

所以 \(z\ge17\)。即

\[
\boxed{
z\equiv0\pmod2\Longrightarrow z\ge108,\ \sigma\ge5869;
\qquad
z\equiv1\pmod2\Longrightarrow z\ge17,\ \sigma\ge955.
}
\tag{37cz}
\]

还有一个精确的模 \(24\) 改进。由 (37an) 的第一式和
\(3\rho+1=13\sigma\)，有 \(A\tau=\sigma\rho-K\)。写
\(\tau=\sigma+6w\)、\(X=\rho-A\)，则 (37ct) 给出 \(w>0\)，并且

\[
K=\sigma X-6Aw.
\tag{37da}
\]

由 \(A\equiv3\pmod {24}\)、\(\rho\equiv16+18z\pmod {24}\)、
\(\sigma\equiv13+6z\pmod {24}\) 及 \(K\equiv19\pmod {24}\)，有

\[
w\equiv
\begin{cases}
3\pmod4,&z\equiv0\pmod2,\\
1\pmod4,&z\equiv1\pmod2.
\end{cases}
\tag{37db}
\]

事实上 \(\sigma X\equiv1\pmod {24}\) 于偶支、\(\sigma X\equiv13\pmod {24}\)
于奇支。两支的 \(w\) 都是奇数，且 \(\sigma w\equiv3\pmod4\)、
\(\sigma^2\equiv1\pmod {24}\)。于是 (37an) 的第二式化为

\[
qK=\sigma^2+6\sigma w+12w^2\equiv1+18+12\equiv7\pmod {24}.
\]

因 \(19^{-1}\equiv19\pmod {24}\)，故

\[
\boxed{q\equiv13\pmod {24}.}
\tag{37dc}
\]

最后由 (37cx) 和 \(3qK=\sigma^2+\sigma\tau+\tau^2\)，

\[
q>\sigma+\tau+\frac{\tau^2}{\sigma}
\ge3\sigma+18+\frac{36}{\sigma}.
\tag{37dd}
\]

将 (37cz)--(37dd) 合并，并在各支取大于右端的最小 \(13\pmod {24}\) 整数，得到

\[
\boxed{
\begin{array}{c|c|c|c}
z\bmod2&z&\sigma&q\\
\hline
0&\ge108&\ge5869&\ge17629\\
1&\ge17&\ge955&\ge2893
\end{array}}
\qquad\text{and hence}\qquad
\boxed{q\ge2893.}
\tag{37de}
\]

这把 whole-\(d\) gap-three residual 限定到严格的大尺度 actual high-\(\gamma\) sector。
它仍不说明 \(q\) 或 \(\gamma\) 的因子出现在 \(u,d,D_*\) 或 \(\kappa\)，也不把 \(q\)
变成 rational source carrier；因此不产生 terminal、source provenance 或 E1--E5 adapter，
QC1、TR1 与 T6 的状态均不因本节改变。

### 8.5.9 high-gap \(D_*\) 不能直接作为既有 odd-distance even-source 的距离

在这个精确 residual 中，actual transverse carrier \(D_*\) 也有一个看似自然的
smaller-source 解释，但它不满足既有 `odd-distance-even-source-descent` 的参数前提。先由
(37ao)、\(h=3u\) 与 \(u=2A+3\rho+1\)，有

\[
p-2h=\lambda-6A-3\rho-2.
\tag{37df}
\]

由 (37cu) 的 \(0<A<\rho\) 及 (37cw-0)，

\[
\lambda>\frac{9\rho^2+5\rho+1}{\rho}>9\rho+5,
\qquad
6A+3\rho+2<9\rho+2.
\]

所以

\[
\boxed{p>2h.}
\tag{37dg}
\]

回到 (20d) 的 actual dichotomy。若 \(D_H=1\)，则 (20g) 已给出
\(D_*=D>2p+1\)，因而 \(D_*\) 根本不能作为一个满足 \(0<c<p\) 的 source
distance。若 \(D_H=5\)，令

\[
c:=D_*=\frac{3p+1-h}{5},
\qquad
n:=p-c=\frac{2p+h-1}{5}.
\tag{37dh}
\]

由 (20b)，\(D\) 为奇数；故此时 \(c\) 为正奇数、\(n\) 为正偶数，且由 (37dg)

\[
c-\frac p2=\frac{p+2-2h}{10}>0,
\qquad
0<n<c.
\tag{37di}
\]

但是 `odd-distance-even-source-descent` 的首个参数条件已经要求

\[
n=d_0(1+cr_0)
\]

其中 \(d_0,r_0\) 都为正整数。这是该扇的首个必要参数条件；故必有
\(n\ge c+1\)，与 (37di) 矛盾。因此

\[
\boxed{
\begin{array}{c|c}
D_H&\text{以 }c=D_*\text{ 调用既有 odd-distance even-source fan 的结果}\\
\hline
1&D_*>p,\ \text{不在允许距离范围}\\
5&0<p-D_*<D_*,\ \text{首个因子参数已不可能}
\end{array}}
\tag{37dj}
\]

这是针对 actual \(D_*\) 的一个 family no-go，而不是 \(D_*\) 本身为空，也不排除其它
距离、marked lift、三分母 lift、direct terminal 或新的 E1--E5 adapter。特别地，TR1
仍保持开放；后续的 \(D_*\) 物理化不能只是把它重命名为现成的 odd-distance even-source。

## 9. 一个 canonical \(7\pmod {12}\) quotient carrier

式 (24) 还决定了 \(\kappa\) 的素因子类型。若奇素数 \(q\mid\kappa\)，则
\(q\nmid A\) 由 (25a) 给出；同样 \(q\nmid B\)，因为否则 (24) 的范数式模 \(q\)
会给出 \(q\mid A\)。故可令 \(z=BA^{-1}\pmod q\)，并由 (24) 得

\[
z^2-z+1\equiv0\pmod q.
\]

这里 \(q\ne3\)，且 \(z\) 既不为 \(1\) 也不为 \(-1\)，所以 \(z\) 的阶恰为 \(6\)。
因此

\[
\boxed{q\mid\kappa\Longrightarrow q\equiv1\pmod6.}
\tag{38}
\]

另一方面 (27e) 给出 \(\kappa\equiv3\pmod4\)，故 \(\kappa\) 至少有一个
\(3\pmod4\) 的素因子。结合 (38)，这样的素因子必为 \(7\pmod {12}\)。于是

\[
\boxed{
q_\star:=\min\{q:q\mid\kappa,\ q\equiv7\pmod {12}\}
\quad\text{is well-defined.}
}
\tag{39}
\]

这给出一个不依赖任意选择的 O2 carrier，并且第 8 节把它精确拆成三路。若
\(q_\star\mid u\)，它已有 actual root-height occurrence，属于既有 root-supported source 的
输入类型；若 \(q_\star\mid d\)，则它自动不整除 \(u\)，而是 whole-\(d\)
\(\Phi_6(p)\) cancellation 与 natural Type II fan 的因子；若两者都不整除，则它是严格的
primitive quotient-only residual，必须通过 QC1 的 physicalization 或 TR1 的独立出口处理。
第三路是否还整除 \(v=(p^2+p+1)/h\)，仍由 primitive-normalization 的 \(q\mid e\) 或
\(B\equiv(p+1)A\pmod q\) 分流精确决定；本卡没有抹去该信息。三路互斥且穷尽，但第二路的
fan 是否命中仍未证明，故它们都尚未产生 terminal 或 E1--E5 edge。

## 10. 边界与下一命题

本卡没有证明 (5)、(10)、(11)--(15) 的正整数解为空，也没有证明这些解能成为 actual
maximal receipt。更没有从 (18) 构造 Type I/II certificate、source replay、all-solution
lift 或 T5 ticket。

它把 \(m=3\) 的真正局部目标固定为：在 \(\kappa\ge31\) 的 fixed-\(\kappa\) fibers 上，
分别处理 root-supported \(q_\star\)、whole-\(d\) 的 \(\Phi_6(p)\) terminal fan，和
\(q_\star\nmid ud\) 的 primitive quotient-only residual。特别地，后两者不能再被错误地
重命名为 \(D\)-carrier。需要证明某一 terminal fan 必命中，或构造一个不依赖 quotient
rechart 的 actual E1--E5 adapter。没有完成这一步前，QC1、TR1 和
`T6_GLOBAL_SELECTOR_TOTALITY` 都保持 `OPEN`。
