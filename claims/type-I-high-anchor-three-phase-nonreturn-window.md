---
kind: claim
claim_id: type-I-high-anchor-three-phase-nonreturn-window
title: 高锚点 charged r-图表的三相非回返窗口
statement: 设高锚点是 \(\operatorname{Ch}_p(A)=(R,K)\)，即 \(pR+1=4K\)、\(A\mid K\)、\(p<R<4A\)。若一个通过代数 gate 的 cofactor r-图表满足 \(1\le r,C<p\)、\(pR_r+1=4rC\) 且 \(\operatorname{lcm}(A,C)\mid rC\)，则 \(h=(rC-K)/(pA)=(R_r-R)/(4A)\) 是 \(0,1,2\) 三者之一。\(h=0\) 当且仅当 r-图表回返原 \((R,K)\)；\(h=1,2\) 均为严格非回返且 \(R_r>R\)。并且非回返至少将支撑放大 \(h+1\) 倍。故高锚点上的代数 non-return 不再是无界算术现象，而是两个可枚举相位；该局部分类本身不构成跨锚点良基递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-cofactor-r-chart-support
  - type-I-overflow-same-chart-support-promotion
  - type-I-fixed-high-anchor-return-one-shot-exhaustion
  - type-I-general-b-centered-square-spectrum
  - denominator-escape-state-contract
topics:
  - type-I
  - high-carrier
  - r-chart
  - nonreturn
  - charged-support
  - F-state
  - G-state
  - terminal-first
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_high_r_chart_p3793_audit.py
    role: G-parented h=1 local candidate and Type I terminal
  - reproduction: reproductions/type_i_high_r_chart_7393_nonreturn.py
    role: F-to-F h=1 local candidate and Type I terminal
  - reproduction: reproductions/type_i_high_r_chart_60913_h2_nonreturn.py
    role: G-to-G-to-F h=2 local candidate and Type I terminal
visibility: public
last_checked: '2026-08-06'
---

# 高锚点 charged r-图表的三相非回返窗口

## 1. 设置

令 \(p\equiv1\pmod4\) 为素数，且当前 charged 高锚点是其支撑
\(A\) 的 canonical chart：

\[
pR+1=4K,\qquad A\mid K,\qquad p<R<4A.
\tag{1}
\]

最后一个不等式不是额外假设，而是
\(R=\operatorname{canonical\_chart}(p,A)\) 的规范代表范围；高锚点条件是
\(R>p\)。特别地 \(A>p/4\)。又 \(p\nmid A\)：否则 \(p\mid K\)，这与
\(pR+1=4K\pmod p\) 矛盾。

设一个 complete-excess overflow 的余数图表给出

\[
1\le r,C<p,\qquad pR_r+1=4rC.
\tag{2}
\]

这里 \(r=M\bmod p\)、\(C=p-d\)，所以 (2) 就是通常的
cofactor \(r\)-chart。令 \(A_C=\operatorname{lcm}(A,C)\)。其 charged
target gate 是

\[
A_C\mid rC
\quad\Longleftrightarrow\quad
A\mid rC.
\tag{3}
\]

只讨论 (3) 已通过且 \(R_r>0\) 的情形；否则它不是当前相位中的
通过代数 gate 的 target chart。

这一 gate 已自动保证 target 是其支撑的 canonical chart。确实，令

\[
g=(A,C),\qquad A=ga,\qquad C=gc,\qquad (a,c)=1.
\tag{3a}
\]

则 \(A\mid rC\) 等价于 \(a\mid r\)。写 \(r=at\)，其中 \(1\le t<p\)，便有

\[
rC=A_Ct,\qquad 1\le R_r=\frac{4A_Ct-1}{p}<4A_C.
\tag{3b}
\]

所以 \(\operatorname{canonical\_chart}(p,A_C)=(R_r,rC)\)。这里和下文的
“回返”只指回返原图表 \((R,K)\)，不表示回到同一完整 charged state。

## 2. 三相引理

**引理。** 在 (1)--(3) 下，

\[
h:=\frac{rC-K}{pA}
=\frac{R_r-R}{4A}
\tag{4}
\]

是良定义的整数，并且

\[
\boxed{h\in\{0,1,2\}.}
\tag{5}
\]

此外，以下等价：

\[
\boxed{
h=0
\ \Longleftrightarrow\
(R_r,rC)=(R,K)
\ \Longleftrightarrow\
r\mid K\ \text{且}\ R<4r.
}
\tag{6}
\]

因此 \(h=1\) 或 \(h=2\) 时

\[
R_r=R+4Ah>R>p,
\tag{7}
\]

是严格的高锚点非回返。

### 证明

由 (1)、(2) 模 \(p\) 相减，\(p\mid rC-K\)。gate (3) 给出
\(A\mid rC\)，又 \(A\mid K\)，故 \(A\mid rC-K\)。因为
\((A,p)=1\)，分子被 \(pA\) 整除。再由两条 chart 方程相减，

\[
4(rC-K)=p(R_r-R),
\tag{8}
\]

得到 (4)。若 \(h\le-1\)，则

\[
R_r=R+4Ah\le R-4A<0,
\]

与 \(R_r>0\) 矛盾，故 \(h\ge0\)。另一方面，\(r,C\le p-1\) 给出

\[
R_r\le\frac{4(p-1)^2-1}{p}<4p-7.
\]

又 \(R_r\equiv3\pmod4\)，所以 \(R_r\le4p-9\)。若 \(h\ge3\)，由
\(R>p\)、\(A>p/4\) 有

\[
R_r=R+4Ah>p+3p=4p,
\]

矛盾。于是 (5) 成立。

当 \(h=0\) 时 (8) 给出 \(R_r=R\) 且 \(rC=K\)，所以回返原图表，并立即有
\(r\mid K\)、\(R=R_r<4r\)。反过来，若 \(r\mid K\) 且 \(R<4r\)，则

\[
\frac Kr\le p-\frac{p-1}{4r}<p,
\]

其中使用 \(R\le4r-1\)。式 (2) 与 \(4K\equiv4rC\equiv1\pmod p\) 给出
\(C\equiv K/r\pmod p\)；两者均在 \(1,\ldots,p-1\)，故 \(C=K/r\)，即
\(h=0\)。这证明 (6)，而 (7) 随即成立。证毕。

为避免与固定锚点回返卡中的符号混淆，这里使用的是正向非回返差
\((K_r-K)/p\)；该卡中的 return defect 则是它的相反数。

## 3. 相位支付的支撑放大

保留 (3a) 的记号，并写 \(K=AB\)。由 \(rC=A_Ct=Act\) 和 (4) 得到

\[
ct=B+ph.
\tag{9}
\]

若 \(h>0\)，则 \(ct=B+ph>ph\)，而 \(at=r<p\) 给出 \(t<p/a\)。因此

\[
 c>\frac{ph}{t}>ha,
\]

从而（\(c\) 为整数）

\[
\boxed{h>0\quad\Longrightarrow\quad c\ge ha+1\ge h+1,
\qquad A_C=Ac\ge(ha+1)A.}
\tag{10}
\]

特别地，\(h=1\) 至少使支撑翻倍，\(h=2\) 至少使它三倍；若 \(a>1\)，放大
更强。令 canonical 余量为

\[
n=4A-R,\qquad n_T=4A_C-R_r.
\]

由 (7) 得

\[
n_T=n+4A(c-h-1)\ge n.
\tag{10a}
\]

这里 \(h=0\) 时只用 \(c\ge1\)，而正相位时使用 (10)。余量保持相等的正相位
只能是 \((h,c,a)=(1,2,1)\) 或 \((2,3,1)\)；它们正是既有 fixed-\(n\) 支撑
\((h+1)A\) 的最小影子。更精确地，若 \(c=h+1\)，则 \(a=1\)，并且由
\(B=ct-ph\) 可得 \(c\mid(p-B)\)。因此 \(L=cA\mid A(p-B)\)，且

\[
R_L=R+4Ah=R_r,\qquad K_L=K_r.
\tag{10b}
\]

这种最小相位应分派给既有 fixed-\(n\) 支撑分支，而不是保留为新的相位递归边。因而
任一只由这类持久化 cofactor 边组成的固定 \(p\) 支撑循环都不能含正相位。这个支付
规律仍不能禁止 forgetful RESET、越过容量盒的跳跃或跨 \(p\) 调度，因而不是全局 E5 秩。

## 4. 回返窗口与筛选

对固定 \((p,R,K)\)，定义有限窗口

\[
\mathcal D_{p,R,K}
=\{t:1\le t<p,\ t\mid K,\ R<4t\}.
\tag{11}
\]

式 (6) 给出一个无需枚举 \(C\) 的精确筛：

\[
\text{cofactor r-chart 回返}
\quad\Longleftrightarrow\quad
r\in\mathcal D_{p,R,K}.
\tag{12}
\]

在 gate 已通过的高锚点上，其余通过代数 gate 的情形只能带有 \(h=1\) 或 \(h=2\)。
这严格加强了“只要 \(R_r\ne R\) 就记为另一分支”的粗分类：现在 non-return
分支有一个显式、至多二值的局部相位标签。

直接、无 RESET 的 cofactor 链现在还满足更强的一次性令牌：正相位至多发生一次，见
[高锚点 cofactor r-图表链的正相位一次性令牌](type-I-high-anchor-positive-phase-one-shot-token.md)。
再结合零相位的 \(\Omega(K/A)\) 支付和 identity-stutter 抑制，direct cofactor 宏步已有
显式的 token-Omega 良基秩，见
[高锚点 direct cofactor 宏步的 token-Omega 良基秩](type-I-high-anchor-direct-cofactor-lexicographic-rank.md)。
它仍不是全局 E5 秩，因为外部 complete-excess bundle、same-chart support promotion、
RESET 及跨 chart 调度不属于这条直接链。

## 5. G 型父状态并非阻断

同图表支撑升级保持 \((p,R,K)\) 不变，故保持 \(K\) 的素因子、中心盒与 F/G
分类不变。F 状态沿用其规范 signed witness；G 状态只需重算同一支撑外分离角色，
而标记集仍是图表无关的
\(W_S=W_T=\operatorname{Sol}(p)\) 与恒等提升。它正是
[同图表支撑升级](type-I-overflow-same-chart-support-promotion.md) 的 E4，
不能被误缩成“只允许 F”。

专用 high-\(R\) 回放现在显式实现了 Legendre 型 G 分离器。例如

\[
p=3793,\quad A=1811,\quad (R,K)=(7011,1811\cdot3671).
\]

因 \(19\mid7011\)，且

\[
\left(\frac{1811}{19}\right)
=\left(\frac{3671}{19}\right)=1,
\qquad
\left(\frac{-1}{19}\right)=-1,
\]

该 anchor 确为 G 型。但 root overflow 满足 \(1\to1811\le B_p\)，所以
G-aware 同图表回放给出完整 charged parent。其后续 cofactor 图表为

\[
(R_r,K_r;A_C)=(14255,13517304;3622),
\qquad h=1,
\]

并有 source/target 的规范 F 见证。故 G 不是这里的数学 no-go；先前 F-only
adapter 只是实现层的错误限制。

## 6. 全 F 的独立控制例

令

\[
p=7393,\quad A=2490,\quad (R,K)=(9863,18229290).
\]

root anchor、high overflow source 与 r-chart target 都是 F 型，且可重放同图表
parent。高 bundle 给出

\[
M=12278190=1660p+5810,\qquad C=6306,
\]

\[
A_C=2616990,\qquad (R_r,K_r)=(19823,36637860).
\]

这里

\[
\frac{K_r-K}{p}=2490=A,\qquad h=1,
\]

局部势严格为

\[
\left\lfloor\frac{13660416}{2490}\right\rfloor=5486
\quad>\quad
5=\left\lfloor\frac{13660416}{2616990}\right\rfloor.
\]

这是一条不依赖 G/F 语义扩张的 F-to-F non-return source-local candidate，
并完整通过局部 E1--E5；它仍不是 global verified edge。

## 7. 最小 \(h=2\) 的 G--G--F 控制例

最小 \(h=2\) 相位也确实出现，而不只是上界中的形式可能。专用回执给出

\[
p=60913,\qquad A=18647,\qquad (R,K)=(72259,1100378117).
\]

其 first high anchor 与 high overflow source 均为 CRT-parity G 型。高 bundle 的
cofactor 为

\[
M=1347394926,\qquad C=55941=3A,
\]

并给出 F 型 target

\[
(R_r,K_r;A_C)=(221435,3372067539;55941),\qquad h=2.
\]

这里 \(n=4A-R=2329\) 在 target 保持不变，正是 (10b) 的 \(L=3A\) 边界；局部
势严格为

\[
49743=\left\lfloor\frac{927567936}{18647}\right\rfloor
\quad>\quad
16581=\left\lfloor\frac{927567936}{55941}\right\rfloor.
\]

该路径完整通过局部 E1--E5 与 G/G/F 纤维证书，但仍仅登记为
`candidate_transition`。它由独立 terminal-first 证书关闭：

\[
\frac4{60913}
=\frac1{15230}+\frac1{132531460}+\frac1{8072888822980}.
\]

## 8. terminal-first 边界

上述三个素数均已由独立 Type I 正规形终止：

\[
\frac4{3793}
=\frac1{950}+\frac1{514900}+\frac1{1953015700},
\]

\[
\frac4{7393}
=\frac1{1850}+\frac1{1953865}+\frac1{5344621859650}.
\]

特别地，\(7393+4=13\cdot569\) 没有 \(3\pmod4\) 素因子，故旧的
\(p+4\) Type II 快筛不会终止它；这一行仍由 gap-7 Type I 证书优先关闭。
这些是结构正例而非未解核心余项，也说明任何 non-return 搜索都必须先运行
terminal-first dispatcher。

## 9. 下一缺口

三相引理、一次性 token 和零相位 \(\Omega(K/A)\) 秩现在已关闭 direct cofactor
子程序的非平凡循环；\(h=0,c=1\) 仅是 capability-aware macro cache 应抑制的 identity。
新的关键问题是 token 离开 canonical checkpoint 子图后的传播：same-chart promotion、
joined RESET 与整除单调 support 扩张可携带 spent token；support_reset_paid、forgetful
RESET、fresh-root/epoch 改变和非 canonical transient carrier 则必须 token_exit，并由
既有外层 E5、terminal 或新的 epoch-rank 支付。详见
[高锚点正相位 token 的 canonical checkpoint 传播合同](type-I-high-anchor-token-canonical-checkpoint-propagation.md)。
