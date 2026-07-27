---
kind: concept
concept_id: short-certificate-descent
title: 短证书或递降计划
summary: 把核心素数的解改写为首分母缺口除子证书，并明确何种严格递降及可提升性足以通过强归纳解决猜想；现有参数化和模筛尚未提供这种强制机制。
topics:
- proof-program
- certificate
- descent
- divisor-parametrization
- computational-experiment
used_by:
- short-certificate-equivalence
- chamberland-type-II-equivalence
- bello-fab-window-reported
- marked-solution-descent-closure
- adaptive-external-source-descent
sources:
- bradford2024
- bello2026
- elsholtz_tao2013
- adaptive_divisor_clouds2026
visibility: public
last_checked: '2026-07-24'
---

# 短证书或递降计划

## 定义与直觉

对核心素数 \(p\equiv1\pmod{24}\)，把最小分母写为

\[
x=\frac{p+m}{4},\qquad m=4x-p\equiv3\pmod4.
\]

`short-certificate-equivalence` 给出了两种精确的 \((m,d)\) 除子证书。研究计划中的“短”必须指定为一个函数 \(H\)：直接分支要求 \(m\le H(p)\)。若不规定 \(H\)，则 \(m<p\) 的线性上界只是已有等价刻画，不能产生新结论。

Bhattacharjee 2026 的 moving-window saturation 将固定 \(J_0\) 表述为
\(H(p)=4J_0-1\) 的 Type II 版本；其 Conjecture 13.1 正是尚未证明的全覆盖命题，
不是已经完成的有限证书，见 adaptive_divisor_clouds2026。

## 无标记的强形式

设 \(\mathcal B\) 是已知可解的基例集合（例如非核心整数由经典恒等式处理，或经过独立验证的有限实例）。一个递降见证对 \(p\) 给出整数 \(n\) 与有限数据 \(w\)，满足：

\[
2\le n<p,
\]

且存在一个显式、可核验的映射

\[
L_{p,w}:\operatorname{Sol}(n)\longrightarrow\operatorname{Sol}(p).
\]

令归纳不变式为“所有 \(2\le r<p\) 的整数分母实例均可解”。若对每个核心素数 \(p\)，要么存在 \(m\le H(p)\) 的 I/II 证书，要么存在这样的递降见证，而递降链最终落入 \(\mathcal B\)，则 Erdős--Straus 猜想成立。

证明只用对分母 \(p\) 的强归纳：直接分支由证书恢复解；递降分支由归纳假设给出 \(n\) 的解，再施加 \(L_{p,w}\)。对于小于 \(p\) 的合数，先取一个素因子并缩放其解；对非核心素数使用经典恒等式。因此该不变式确实由核心素数步骤闭合。严格不等式 \(n<p\) 保证终止。

这是容易使用的**强闭包准则**，不是构造了递降映射。要完成原目标，缺少的正是对每个无短证书核心素数产生 \((n,w)\) 的统一算术规则。它还比归纳真正需要的条件更强：归纳只需一个可提升的源解，而非每个源解都可提升。

## 带标记解的闭包准则

更一般且恰当的表述见 marked-solution-descent-closure。它把归纳状态写成
\((n,\theta)\)，其中标签 \(\theta\) 指定一个待获得的子集
\(W_{n,\theta}\subseteq\operatorname{Sol}(n)\)。递降边只须给出

\[
W_{n,\theta}\longrightarrow W_{p,\theta'},\qquad n<p,
\]

并在较小状态递归地保证 \(W_{n,\theta}\) 非空。无标记映射
\(\operatorname{Sol}(n)\to\operatorname{Sol}(p)\) 正是取
\(W_{n,\theta}=\operatorname{Sol}(n)\) 的特例。

这一区分很重要：局部提升常只适用于带有特定因子条件的源解。标签甚至可以记录目标
\(p\)，但只要真实分母沿边严格下降，良基归纳仍然成立。新的全称难点因而更精确地变成：
为每个无短证书的 \(p\)，构造一个**可闭合**的较小标记状态，而不仅是发现一条偶然可提升的源解。

这个目标的逻辑强度取决于“短”的定量含义。若只允许自然范围
\(H(p)=p-2\)，则它与 Erdős--Straus 猜想（在核心素数上）等价：闭包准则给出
正向蕴含；反向则由猜想的解和 `short-certificate-equivalence` 直接产生一个
\(m\le p-2\) 的证书，甚至无需递降。所有此范围内的证书也已是 \(O(\log p)\) 位的
可核验证书。因此“证书有界”若仅指位长度，并没有降低问题难度。一个可独立检验的
目标必须指定非平凡数值界 \(H(p)<p-2\)，或提供一个此前未知的 \(L_{p,w}\)。

## 现有“提升”为什么不够

Bello-Hernández、Benito、Fernández的 Proposition 20 说明：若 \(k\) 对 \(\operatorname{fab}(n,a,b)\) 可采纳，则相同 \(k\) 对

\[
n_1=n+4abk
\]

仍可采纳。这是把**已有证书**沿同余类上提的机制；逆向也只能在已知同一 \((a,b,k)\) 证书时把它移回较小代表元。它并未从任意 \(\operatorname{Sol}(n)\) 构造 \(\operatorname{Sol}(p)\)，更没有为未检测的 \(p\) 自动产生 \((a,b,k)\)。因此它可用于有限模筛，不能单独充当上面的递降分支。

固定有限参数的同余覆盖还面临该文 Theorem 8 所指出的刚性障碍。这解释了为何“反复提升少数模板”不能闭合全称命题。

对最自然的 \(m=3\) 源分母 \(n=(p+3)/4\)，上述平移甚至有一个立即的同余障碍：
若 \(p=24t+1\) 且 `fab` 平移 \(n\mapsto n+4abk\) 恰到达 \(p\)，则
\(4abk=p-n=18t\)。故 \(t\) 为奇数时不可能，\(t\) 为偶数时也必须满足
\(abk=9t/2\)，见 `gap-three-fab-translation-obstruction`。这进一步表明平移筛
不能直接充当 \(m=3\) 的统一递降。

## 可检验的子目标

1. 找到并证明一个非平凡函数 \(H(p)\)，使所有核心素数都有 \(m\le H(p)\) 的证书；或
2. 对没有这种证书的 \(p\)，构造真正的 \(n<p\) 和解提升映射；或
3. 证明某个候选短界或递降规则失败，从而排除该路线。

`reproductions/short_certificate.py` 精确枚举 \(m=3,7,\ldots\) 的最小可用缺口。它用于给候选 \(H\) 和递降规则寻找反例、记录保持者及因子结构，不将有限数据解释为统一界。

其中 \(m=3\) 已有完全的素因子判据，见 `gap-three-criterion`：它把第一层未覆盖对象明确压缩为 \((p+3)/4\) 的所有素因子均为 \(1\pmod3\) 的素数。后续研究应对这一残余集推出新的小缺口证书或真正递降，而不是重复搜索 \(m=3\)。

固定缺口 \(m=7\) 也有三个无需分解的模类切片：\(p\equiv3,5,6\pmod7\) 时，
`gap-seven-congruence-certificates` 分别取 \(d=1,2x,2\)。故五分支的共同残余若再
剔除这条分支，必落在 \(p\equiv1,2,4\pmod7\)；这只改变筛常数，不构成全称覆盖。
更一般地，`fixed-divisor-gap-template-obstruction` 说明任意有限个这种“固定缺口 +
由 \(x\) 的公共小因子产生的固定除子”分支都能被同一 Dirichlet 素数列避开。因此
后续必须研究因子依赖的内部除子、可变参数射线或真实递降，而不是继续堆叠有限模表。

2026 的 `linear_ratio_ansatz2026` 把同一边界推广到一个看似更宽的比例族：
固定 \(x=(p+a)/4\) 并令另外两个分母满足 \(z/y=ps/r\)。其整数性对固定
\((a,r,s)\) 仍只是有限模测试；`linear-ratio-ansatz-type-I-translation` 将其精确译为
缺口 \(m=a\) 的 Type I 证书，除子为 \(d=rx/s\)。原稿的有限覆盖障碍有效地说明：
有限个原始三元组会被 \(p\equiv1\) 的一条 Dirichlet 素数列同时避开。因此该方向补充了
明确的同余族，未提供真正递降或有限全覆盖。

另一个可严格闭合的单步分支从 \(n=(3p+1)/4\) 出发。若 \(n\) 含
\(2\pmod3\) 素因子，`three-p-plus-one-descent-certificate` 显式给出
\((n,qr,nr)\mapsto(np,qr,nr)\) 的严格提升；同一构造还恢复
\(m=(4q+1)/3=O(\sqrt p)\) 的 Type I 证书。它的失败条件是 \(n\) 的所有
素因子皆为 \(1\pmod3\)，并有相对密度零的筛界，见
`three-p-plus-one-density-one-descent`。这提供了可用于状态图的真实下降边，
但未给出残余集上的统一选择器。

这条递降可沿外部源参数自适应扩张。adaptive-external-source-descent 令
\(k\mid(p-1)/4\)、\(q=4k-1\)、\(n=(qp+1)/(q+1)\)。若
\(n\) 有因子 \(f\equiv-1\pmod q\)，则标记源解
\((kn,kfr,knr)\) 严格提升为 \((knp,kfr,knr)\)，其中
\(r=(n/f+1)/q\)。同一数据给出正规形 \((r,1,kf)\) 的 Type I 证书及
\(m\le4\sqrt p/3+1/3\)。\(k=1\) 恢复原来的 \(q=3\) 分支，而核心素数
恒允许的 \(k=2,3,6\) 再给出 \(q=7,11,23\) 的分支。它仍要求某个因子残数，
所以是实际递降机制的扩展，不是对所有残余 \(p\) 的选择器。

外部源直接证书还有一个不同的变量因子坐标：
`type-I-rp-plus-one-external-factor-ray` 证明，任意 \(r\equiv3\pmod4\) 的
\(rp+1\) 若有 \(q\equiv-1\pmod r\) 的奇因子，就给出外部源 Type I 证书，
且缺口 \(m\le(p-1)/4\)。反向地，每个外部源都唯一恢复为
\(rp+1=4qt\) 的这种因子射线。故外部源的无穷难点应表述为变量 \(r\) 的因子
选择器，而不是固定 source 窗口的覆盖猜想。

对恒可选的 \(k=1,2,3,6\)，对应 \(q=3,7,11,23\) 都是 \(3\pmod4\) 素数。
分支失败会把各自的源分母 \(n_q\) 的素因子压入模 \(q\) 的半大小横截面。
four-external-source-descents-density 因而把四条真实递降共同残余压到
\(O(X/(\log X)^3)\)，比单独 q=3 分支的 \(3/2\) 维界更薄。它仍是密度结论，
不能替代共同残余上的逐点选择器。

shifted-external-source-descent 还允许 \(p\equiv d\pmod{4k}\) 的非零平移：
若 \(n=((4k-1)p+d)/(4k)\) 有 \(n=f((4k-1)r-1)\) 的因子形状，且
\(d\mid kn\)，则 \((kn,kfr,knr)\) 提升为 \((knp/d,kfr,knr)\)，并恢复
正规形 \((dr,1,kf/d)\) 的 Type I 证书。例如 \(p=2473,k=7,d=9\) 给出不同于
展示出的 \(d=1\) 见证的参数化递降；该平移族仍没有相对于完整
\(d=1\) 自适应族的全局覆盖定理，也尚未给出共同残余上的统一参数选择。
shifted-external-polynomial-ray 给出严格的有限分离：\(d=5,r=15,s=6\) 产生
\(p=31849\) 的缺口 \(71\) 递降边，而完整 \(d=1\) 自适应族在该素数上失败。
平移因此确实增加了标记图，但仍未给出共同残余上的统一参数选择。

`mixed-factor-external-source-descent` 则在 \(d=1\) 时放宽了源分解中的因子位置：
对 \(n=((4k-1)p+1)/(4k)\)，原分支要求 \(f\mid n\)、\(f\equiv-1\pmod{4k-1}\)；
新分支只要求 \(g\mid kn\)、\(g\le n\) 和同一残数条件。它保留显式的
\((kn,u,v)\to(knp,u,v)\) 提升并恢复 Type I 证书
\(m=(4kg+1)/(4k-1)\)、\(D=u^2/(kg)\)。例如 \(p=97,k=2,n=85,g=34\) 是旧族
不命中而新族命中的严格扩张例。然而新条件只保证 \(m\le p-2\)，没有平方根级界，
也尚未给出所有核心素数的参数选择。

更完整地，`quadratic-factor-external-source-descent` 穷尽固定 \(k\) 时保留
\(M=kn\) 的全部二项尾：它只需 \(e\mid M^2\)、\(e\le M\)、
\(e\equiv-M\pmod{4k-1}\)，便以 \((M,u,v)\to(Mp,u,v)\) 提升，并恢复
\(m=(4e+1)/(4k-1)\) 的 Type I 证书。这严格包含 \(e=kg\) 的混合因子情形；
\(p=409,k=6,e=63\) 给出缺口 \(11\)。因此该源上的剩余问题已有精确因子形式，
但跨全部允许 \(k\) 的选择器仍未知。

`shifted-quadratic-factor-external-source-descent` 将这一完整尾项参数化推广到
\(p\equiv d\pmod{4k}\) 的非零平移：若 \(d\mid M=kn\)，则目标替换为
\(M\mapsto Mp/d\)。此时因 \(q\) 未必与 \(M\) 互素，因子和互补因子的模条件都必须
显式检查；另有 \(d\mid e\) 才恢复 Type I 证书。它统一了零平移平方因子族与旧的
`shifted-external-source-descent` 子族，例如 \(p=8329,k=160,d=9\) 给出缺口 \(31\)。

其中 \(n=p-1\) 的平移扇可完全降维。对任意 \(d\mid p-1\)、\(d\equiv1\pmod4\)，
令 \(s=(p-1)/d\)、\(r=s-1\)、\(k=(p-d)/4\)，则相应平移源必为已知可解的
\(p-1\)。`p-minus-one-source-descent` 证明其完整平方尾选择恰化为
\(e_1\mid(ks)^2\) 与一个同余 \(e_1\equiv-ks\pmod r\)；第二个尾项同余由
\((r,ks)=1\) 自动给出。它因此提供从统一较小源 \(p-1\) 出发的严格提升扇，而非
另一个特殊充分条件。该扇在有限范围命中许多点，但因子选择仍未被全称强制。

同一降维实际上适用于任意奇数距离的偶源。若 $c$ 为正奇数、$p-c=ds$、
$s=1+cr$，且 $dr\equiv-1\pmod4$，则 $k=(dr+1)/4$ 给出源 $p-c<p$ 的完整扇；
其平方尾仍只需 $e_1\mid(ks)^2$ 和 $e_1\equiv-ks\pmod r$。这把所有满足上述
因子条件的平移源 $p-c$ 精确合并为 `odd-distance-even-source-descent`。例如
$p=73,c=3$ 命中而 $p-1$ 扇不命中，说明该状态图确有新边；然而 $c,d,e_1$ 的
全称选择器仍然缺失。

若允许保留的第一源分母是 \(A=an/b\) 而不要求它为 \(n\) 的整数倍，
scaled-source-descent-rigidity 证明缩放提升 \(A\mapsto Ap/d\) 的既约比例分母
仍只能有 \(b\mid4\)。所以除旧的 \(b=1\) 外，只需研究 \(b=2,4\) 两种比例源；
它们在 \(d=1\) 时均被奇偶性排除，但非零平移确有新边。具体地，
\(p=80809,A=67n/2,d=7\) 给出缺口 \(71\) 的 Type I 证书，且不属于此前
固定 \(M=kn\) 的完整尾项空间。

另一条脱离缩放模型的路线来自偶数源的非标准分裂。even-split-source-descent 完整参数化
\(4/n=1/(n/2)+1/a+1/b\) 的所有二项尾；标准点 \((n/2,n,n)\) 被既有障碍排除，
但 \(p=5209,n=2680,e=80\) 的非标准点能将 \(1380\) 替换为 \(481624140\)，
并给出缺口 \(151\) 的 Type I 证书。这表明“偶数源无效”的结论只适用于标准解，
而不适用于完整因子分裂族。

even-standard-two-tail-descent 给出另一条互补的偶数机制：仍从无条件标准源
\((n/2,n,n)\) 出发，但只保留其中一个大分母 \(n\)，并把 \(n/2\) 与另一个 \(n\)
同时重组为目标的两项。固定 \(p,n\) 时，全部这种提升由
\((4n-p)u-pn\) 和其互补因子分解 \((pn)^2\) 精确参数化。它不与“保留两项”的障碍
冲突；例如 \(21169\) 通过 \(n=12198,e=342\)，而 \(48409\) 通过
\(n=27764,e=1262\) 得到严格边和相应的 Type I 证书。这两个数此前正属于固定
\(M=kn\) 平方因子尾项留下的有限残余。该参数化依旧没有强制每个 \(p\) 存在一组
\((n,e)\)，所以它扩展状态图而不闭合全称递降。

three-divisible-standard-two-tail-descent 给出第三条无条件标准源的对应机制：从
\((n/3,2n,2n)\) 只保留一个 \(2n\)，并按 \((8n-p)u-2np\) 的互补因子重组其余两项。
由于在 \(p/2<n<p\) 时被保留分母 \(2n>p\)，它不受上述偶数大尾的 \(m>p/3\) 限制；
例如 \(p=8329,n=4620,e=168\) 给出缺口 \(2423<p/3\)。这严格绕开了
three-divisible-standard-source-lift-obstruction 所排除的“两项保留、一项替换”模板，
但与其它参数化一样，尚未证明每个核心素数均可选择到满足因子条件的 \(n,e\)。
其窗口不能随意下探：`three-divisible-tail-window-localization` 证明，
\(p/4<n<p/2\) 的同一因子选择与偶数标准源 \(2n\) 完全相同，\(p/8<n<p/4\) 则
退化为首分母 \(2n\) 的直接证书。因此 \(p/2<n<p\) 恰是这条三倍数大尾相对于已有分支
的非冗余区间。
更进一步，`standard-tail-type-I-coordinate-equivalence` 表明两条标准大尾在自然范围内
恰是 Type I 证书的第二分母窗口：偶数源对应 \(p/2<y<p\) 的偶数 \(y\)，三倍数源对应
\(p<y<2p\) 且 \(6\mid y\)。故它们是高效的目标证书搜索坐标，而不是在目标因子条件
失败后仍可单独闭合的归纳选择器。
对两条标准大尾族的精确扫描也给出直接的有限边界：在 \(p\le10^4\) 的 143 个核心
素数中，它们的并集只命中 126 个，并共同遗漏 17 个具体素数，见
standard-tail-descent-finite-audit。因此其高有限命中率不能替代全称选择器；后续递降
必须利用非标准源、不同的提升形状，或直接转向剩余集的证书构造。

affine-standard-tail-type-I-descent 进一步统一这两条大尾机制：当目标首分母、被保留
大尾和 Type I 除子写为 \(x=at,y=bt,d=ht\) 时，唯一的兼容关系就是
\(p(a+b)=4abt-h\)。偶数源典型地落在 \(a<b<3a\)，三倍数源则落在
\(3a<b<7a\)；后者正允许缺口进入 \(p/3\) 以下。因而下一步的选择器问题可改写为：
能否对每个剩余核心素数构造满足这些整除、奇偶和秩不等式的 \((a,b,h,t)\)，而不必
先在整个 \((pn)^2\) 因子格中盲搜。这个重新参数化仍不是覆盖性证明。

把 \(m=3\)、\((p+1)/2\)、\(p+4\)、\(4p+1\) 以及上述新分支同时施加，
`five-branch-sieve-residual` 将共同残余压到
\(O(X/(\log X)^{7/2})\)。其中 \(2521\) 还能由 \(p+2\) 的 source-2 分支直接处理：
`p-plus-two-external-source-certificate` 取 \(m=87\)。加入该第六条分支后，
`six-branch-sieve-residual` 给出更薄的
\(O(X/(\log X)^4)\) 共同残余。再加入 \(p+6\) 的 source-6 分支：若其因子残数不全
落入两个明确的模 \(24\) 子群之一，则 `p-plus-six-external-source-certificate` 给出
\(d=6x\) 的 Type I 证书。`seven-branch-sieve-residual` 将共同残余进一步压为
\(O(X/(\log X)^{9/2})\)。它仍有具体元素（例如 \(5569\)），所以这是研究目标的缩小，
而不是闭合证明。

`three-p-plus-four-internal-type-I-certificate` 首次明确控制一个真正的内部 Type I
切片：若 \(3p+4\) 有因子 \(m\equiv-p\pmod{48}\)，则正规形
\((A,B)=(4,3)\) 给出 \(m\le(3p+4)/41\) 的证书。它既非外部源的 \(B=1\) 面，
也非几何 lcm 边界的 \(A=1\) 面；例如 \(p=2521\) 取 \(m=23\) 得
\((A,B,C)=(4,3,53)\)。更强地，所需目标残数模 \(48\) 没有平方根，故互补的两类
素因子之积即为证书因子；失败时所有素因子只能落在有限个 8 类横截面之一。由此
`eight-branch-sieve-residual` 将共同残余再压为
\(O(X/(\log X)^5)\)。组合因子确实给出额外覆盖（如 \(p=1297,m=95\)），
但该筛界仍不构成全称选择器。

这一内部方向还能沿 \((A,B)=(2^a,3)\) 延伸：
`three-p-plus-power-two-internal-type-I-ray` 对每个 \(A=2^a\ge4\) 使用
\(m\mid3p+A\)、\(m\equiv-p\pmod{12A}\)，并有
\(m\le(3p+A)/(11A-3)\)。每条固定射线的失败同样把其移位数的素因子压入一半
单位残数类。于是 `power-two-internal-rays-superlog-residual` 证明：加入前 \(L\) 条
射线后的共同残余为 \(O_L(X/(\log X)^{(L+9)/2})\)；逃过全部射线的集合对任意
固定对数幂都满足相应上界。这里 \(L\) 随所要求的幂而定，故这仍不是一个有限覆盖，
也不蕴含残余为空。

更一般地，`wide-internal-type-I-factor-ray` 对任何 \(4\mid A\)、奇数
\(B\ge3\)、\((A,B)=1\)、\(A>2B\) 给出一条 \(Bp+A\) 的内部 Type I 射线：
目标因子满足 \(m\equiv-p\pmod{4AB}\) 时，其余因子自动至少为 \(A-B>B\)，故
\(m\le p-2\)。例如 \((A,B)=(12,5)\) 在 \(p=1033\) 给出
\((m,x,d)=(167,300,720)\)。它把因子分支扩展到 \(B>3\) 的内部区域；失败仍只产生
半大小残数横截面，因而是补充性的筛分支，而不是全称选择器。

另一个独立的变量因子方向固定缺口而不固定除子：
`fixed-gap-type-II-factor-ray` 说明，对每个素数 \(q\equiv3\pmod4\)，若
\((p+q)/4\) 含 \(-1\pmod q\) 因子，便有 \((A,B)=(1,B)\) 的 Type II 证书。
它在幂二射线残余中覆盖了大量具体点，例如 \(p=5569\) 由 \(q=7\) 覆盖。
每条这样的射线也贡献半维筛损失；与幂二 Type I 射线合用时，
`variable-factor-rays-superlog-residual` 给出 \(L+J\) 条射线的
\(O(X/(\log X)^{(L+J+9)/2})\) 界。变量 \(B\) 是关键，故这不是被固定除子模板
障碍排除的有限同余覆盖。

`gap-residue-reachability` 进一步给出任意固定缺口的统一语言：Type I 只需 \(x^2\) 的某个除子落在固定残数 \(-4^{-1}\)，Type II 只需落在 \(-x\)。两个独立的平方根级 Type I/II 子族分别来自 `(p+1)/2` 和 \(p+4\) 的 \(3\pmod4\) 素因子；`four-p-plus-one-type-ii-certificate` 还从 \(4p+1\) 的此类素因子构造一条（通常非平方根级）Type II 证书。真正的难点因而位于这些因子筛残余集与 \(m=3\) 残余集的交集。

除子格的边界也已完全分类：Type I 的 \(d=1,x^2\) 和 Type II 的 \(d=x\)
都不可能；Type I 的 \(d=x\) 与 Type II 的 \(d=1\) 分别精确化为 \(m\mid p+1\)、
\(m\mid p+4\)。因此在两条平方根级家族都失败时，后续直接搜索必须控制真正的内部
除子，不能从这些端点再获得新证书。

`external-source-type-I-certificate` 将 Ventas 的外部源条件 \(m\mid p+i\)、\(4i\mid p+m\) 精确译为 Type I 证书；它包含 \(i=1\) 的 \(p+1\) 分支，并允许用可变的 \(i\) 搜索额外的缺口。这里的“source”是围绕同一个 \(p\) 的因子搜索坐标，而不是一个较小分母实例；故它不能被误称为递降。

它还精确刻画 Type I 的一个子空间：外部源存在当且仅当证书除子可写成
\(d=ix\)，即 \(x\mid d\)。因此“强制外部源”不是重新表述全部猜想，而是要求在
Type I 证书中找到包含完整 \(x\) 因子的除子；一般除子 \(d\mid x^2\) 并不具有此性质。

## 一个必要的反例检查：纯缩放不能提升

最自然的候选提升会把一个较小实例 \(n\) 的分母三元组按同一比例 \(\lambda\)
放大。它对严格递降不可能有效。更强地，diagonal-lift-rigidity 说明：若三个输出
分母分别按与源解无关的比例 \(\lambda_1,\lambda_2,\lambda_3\) 缩放，并要求这个
公式对整个正实解曲面成立，则恒等式已经强制
\(\lambda_1=\lambda_2=\lambda_3=p/n\)。因此下述共同缩放障碍实际上排除了所有
这样的坐标对角全域提升。更准确地，若 \(2\le n<p\)、\(p\) 为素数，且

\[
\frac4n=\frac1u+\frac1v+\frac1w,
\]

则不存在正有理数 \(\lambda\)，使 \(\lambda u,\lambda v,\lambda w\) 都是整数且

\[
\frac4p=\frac1{\lambda u}+\frac1{\lambda v}+\frac1{\lambda w}.
\]

第二个等式强制 \(\lambda=p/n\)。由于 \(p>n\) 且 \(p\) 为素数，
\(\gcd(p,n)=1\)；分母整数性于是强制 \(n\mid u,v,w\)。写
\(u=nu'\)、\(v=nv'\)、\(w=nw'\)，原方程化为

\[
4=\frac1{u'}+\frac1{v'}+\frac1{w'},
\]

但右侧至多为 \(3\)，矛盾。故任何成功的 \(L_{p,w}\) 都不能只是把三个分母
作共同尺度变换；它必须利用输入解的非平凡因子结构，或直接从新的证书数据重组分母。
这条结论不排除一般的解提升，只排除了最容易被误当成递降的那一种。

这一障碍甚至允许逐坐标的常数平移：coordinatewise-affine-lift-rigidity 证明，若
\((a,b,c)\mapsto(\alpha_1a+\beta_1,\alpha_2b+\beta_2,\alpha_3c+\beta_3)\) 要在整个
正实源解曲面上成立，则微分恒等式强制所有 \(\beta_i=0\)、所有
\(\alpha_i=p/n\)。所以真正尚存的全域候选至少必须耦合不同输入坐标；真正尚存的带标记
候选还可依赖于源解的因子数据。

缺口 \(m=3\) 的自然递降候选也有更强的障碍。令 \(n=(p+3)/4\)，即
\(p=4n-3\)。若一个提升保留 \(\operatorname{Sol}(n)\) 中的两个分母，只替换第三个
\(a\)，则替换值被强制为

\[
a'=\frac{npa}{np-12(n-1)a}.
\]

对每个核心素数 \(p=24t+1\)，`gap-three-two-denominator-lift-obstruction` 证明这个量
不可能是正整数。故该递降必须至少同时改变两个分母；这不是对一般提升的否定，
却排除了直接沿 \(m=3\) 保留两项的最短尝试。

还有一个不依赖缺口选择的邻近偶数障碍。令 \(n=p-r\)，其中 \(r\) 为任意奇数，则
\(n\) 偶且有无条件源解 \((n/2,n,n)\)。对全部 \(1\le r\le p-2\)，
even-predecessor-two-denominator-lift-obstruction 证明：从该源解保留任意两个
分母并替换第三项也不可能提升到 \(p\)。因此“取一个已知可解的邻近偶数，再只改一项”
不是补足短证书残余集的路线；若从偶数实例递降，至少须使用非标准源解或同时重组两项。

同样，所有 \(n\equiv3\pmod4\) 的经典标准解
\[
\frac4n=\frac1{(n+1)/4}+\frac2{n(n+1)/2}
\]
也不能保留任意两个分母、只替换另一项来提升到核心 \(p\)，见
`three-mod-four-standard-source-lift-obstruction`。因此对所有无条件可解的两类基本源
（偶数与 \(3\pmod4\)），最短的二分母保留策略都已排除；这不排除它们的非标准源解，
也不排除只保留一个分母或重组全部三项。

这一保留也须谨慎理解。Subramanian 2026 的非标准平方尾
\[
\frac4n=\frac1{(n+1)/4}+\frac1{(n+1)^2/4}+\frac1{n(n+1)^2/4}
\quad(n\equiv3\pmod4)
\]
并不属于上述重复尾；但 `three-mod-four-nonstandard-source-lift-obstruction` 证明它的
三个坐标也都不能在保留另外两项时单独替换而提升到核心 \(p\)。所以该新恒等式没有留下
额外的二分母保留递降分支。未排除的空间仍是非标准因子标记、一分母保留，或真正耦合的
多坐标重组。

Subramanian 的另一条 \(n\equiv5\pmod8\) 双尾
\[
\frac4n=\frac1{(n+3)/4}+\frac1{n(n+3)/8}+\frac1{n(n+3)/4}
\]
也不能补上这个缺口。对核心目标有 \(p-n\equiv4\pmod8\)；
`five-mod-eight-nonstandard-source-lift-obstruction` 表明这使两个大尾的替换值无正性，
而首项的替换分母与所需分子至多共享因子 \(3\)，却必为 \(5\pmod8\)。因而该恒等式的
每一个 \(n<p\) 实例都没有二分母保留的单项提升。至此，两个来自新稿的非标准无条件源
也均未产生这种递降；这仍不触及一分母或耦合提升。

该稿在 \(4\mid n\) 时使用的平方尾
\[
\frac4{4t}=\frac1{t+1}+\frac1{(t+1)^2}+\frac1{t(t+1)^2}
\]
也需要单独处理，因为它不是通常的偶数重复尾 \((n/2,n,n)\)。
`four-divisible-nonstandard-source-lift-obstruction` 证明其每一个 \(n<p\) 源解同样
不能通过保留两项、只替换一项提升到核心 \(p\)。证明中，尾项的候选分母或为负，或在
\(p=4t+1\) 时与所需分子互素；首项的整除性则强制某个小于 \(p\) 的正数整除 \(p\)。
因此 Subramanian 给出的三类非标准无条件源均未提供这种最短递降边，仍须转向一分母保留
或真正耦合的变换。

第三类标准源 \(3\mid n\) 也有同样的完整障碍。其恒等式
\[
\frac4n=\frac1{n/3}+\frac2{2n}
\]
中，不论替换 \(n/3\) 还是一个 \(2n\)，`three-divisible-standard-source-lift-obstruction`
都证明不能保留另外两项提升到核心 \(p\)。因此这些最容易获得的源解类别都不能提供所需的
二分母保留递降；尚存的正向选择包括非标准源解、只保留一个分母或三项同时重组。

这个障碍并不扩展到所有自然源缺口。一般地，若 \(2\le n<p\) 的源解含有 \(a\)，保留
其余两项的提升只需 \(D=np-4(p-n)a>0\) 且 \(D\mid npa\)，见
two-denominator-lift-criterion。例如
\(4/33=1/15+1/22+1/110\) 真能提升为
\(4/73=1/4015+1/22+1/110\)。因此一个可行递降不必重组两项或三项；真正缺少的是
对每个残余 \(p\) 的源实例和可用坐标选择器。

事实上，保留**一个**源分母而同时重组另两个分母有精确的部分提升判据。若源解含有
\(c\)，令 \(R=4c-p\)、\(S=pc\)，则寻找 \(4/p=1/u+1/v+1/c\) 等价于寻找
\(e\mid S^2\)，使 \(R\) 同时整除 \(S+e\) 和 \(S+S^2/e\)，见
`one-denominator-lift-factor-criterion`。这确实能产生部分解提升，但尚未证明每个
相关源实例都有可用 \(c\)，也尚未给出能递归保证一个可用 \(c\) 存在的标记状态图，因而未闭合递降。
若 \(\gcd(R,S)=1\)，第二个同余由第一个自动推出；对 \(p\nmid c\) 的奇素数目标，
这正是标准源分支的情形。因此局部因子选择已压缩为一个可检验同余，但这不提供
所需因子 \(e\) 的全称存在性。

还要排除一个表面上的捷径：当保留分母满足 \(p/4<c<p/2\) 时，目标方程的其余两个
分母必大于 \(c\)，故 \(c\) 已是目标首分母。令 \(m=4c-p\)，此一分母提升便与缺口
\(m\) 的 Type I/II 证书严格等价，见
`middle-coordinate-lift-certificate-equivalence`。例如可总是从偶数 \(2c<p\) 的
标准解出发，但是否成功仍完全等价于直接找到目标证书；它不构成短证书失败后的递降。
因此此路线若要产生新内容，必须保留 \(c\ge p/2\) 的非首目标分母，或同时改变全部三个分母。

`type-I-coprime-factor-normal-form` 给出全体 Type I 证书的精确坐标：
\(x=ABC\)、\(d=A^2C\)、\(\gcd(A,B)=1\)、\(m\mid Bp+A\)。因此外部源正是
\(B=1\)。相对的 \(A=1\) 面恰为
`geometric-lcm-boundary-type-I-equivalence` 的
\(z=p\operatorname{lcm}(x,y)\) 几何模式，也是 Bradford--Ionascu 2015 的边界搜索所
聚焦的子类。\(p=2521\) 没有这一面的 Type I 证书，却有 Type II 证书和内部
\((A,B)=(4,3)\) 的 Type I 证书；故两面都不是全体 Type I 覆盖，余下的 Type I
搜索必须控制真正的互素参数对 \((A,B)\)。

Type II 也有平行的正规形：\(x=ABC\)、\(d=A^2C\)、\(\gcd(A,B)=1\)、
\(A\le B\)、\(m\mid A+B\)，见 `type-II-coprime-factor-normal-form`。令
\(K=(A+B)/m\)，它还给出
\[
(4ACK-1)(4B-1)=4Kp+1-4A(CK-1).
\]
当 \(C=K=1\) 时这退化为 \(4p+1=(4A-1)(4B-1)\)，即已知的
`four-p-plus-one-type-ii-certificate` 分支。故剩余的 Type II 难点可明确定位为
\(C>1\) 或 \(K>1\) 的内部参数，而不是这个因子分支的重复。
等价地，\(q=4ACK-1\) 必须整除 \(Kp+A\)，且商就是 \(B\)；这给出一个可测试的
小 \((A,C,K)\) 因子覆盖问题，而非递降映射。
还可固定 \((A,C)\) 而令 \(K\) 随 \(p\) 变化：此时
\(q\mid Kp+A\) 精确等价于 \(q\mid p+4A^2C\)，其中
\(q\equiv-1\pmod{4AC}\)。这把每条 \((A,C)\) 射线化为一个移位整数的因子残数问题。
在 \(p\le2\cdot10^8\) 的精确审计中，\(\max(A,C)\le14\) 已覆盖全部
\(1{,}383{,}890\) 个核心素数，见 `type-II-ac-ray-audit`；半径 11 在先前
\(p\le10^8\) 审计中漏掉 \(84{,}525{,}841\)。由于 \(K\) 未被固定，
`type-II-finite-template-obstruction` 不直接否定“存在全局 \(A,C\) 界”的可能性；
但该全称界目前仍未证明。若其全局界为 \(B\)，
`type-II-raw-ray-certificate` 还给出缺口
\(m\le p/3+4B/3\)，所以它会完成一个严格小于自然范围的短证书分支。
同一射线的序条件对 \(p\ge4B^3\) 自动成立；因此其真正的无穷难点是强制
有限组移位数 \(p+4A^2C\) 出现指定的因子剩余类，而非恢复出的 \(A\le B'\)。
不要求 \(A,C\) 有界时，type-II-ac-rays-superlog-residual 进一步表明：任取有限组
\(A^2C\) 互异的射线，每条失败各增加半个筛维；因而逃过所有 \(AC\) 射线的集合是
任意对数幂稀薄。这把该直接证书方向的共同残余大幅压缩，却不能把解析稀薄性升级为
逐点因子存在。
试图再用有限阿贝尔群结构把每条失败射线压成“真子群加短异常”也有严格边界：
`divisor-residue-subgroup-exception-boundary` 由 Kneser 定理证明稳定子群分解中群外项
至多为商群阶减二，但同时在 \((\mathbb Z/4q\mathbb Z)^\times\) 中构造了真实除子残数
序列，使相对于任何不含 \(-1\) 的子群都必须保留
\(\varphi(4q)/2-2\) 个异常项。因此次线性异常的普适分类为假；可行的增强版必须把
循环商中的双向临界算术级数列为独立主型，再研究这些主型能否在多条移位射线上同时出现。
一个可先行剥离的极端主型是“生成子群中恰只漏掉 \(-1\)”：
`type-II-support-critical-congruence-trap` 用全因子积与补因子配对证明它强制
\(p\equiv1\pmod {4AC}\)。这给出了多射线之间可累积的确定性同余限制，但尚未覆盖
缺失集有两个或更多元素的普遍失败。
对支撑内的多孔失败，`type-II-support-defect-orbit-constraint` 进一步给出完整的
补因子轨道约束：非平凡两孔只能是 \(\{-1,-p\}\)，奇孔强制一个缺失平方根
\(\rho^2\equiv p\pmod {4AC}\)。它把下一步明确为研究这些轨道如何在不同移位数间
不相容；但 \(-1\) 尚未进入生成子群的支撑外失败是独立主型，不能被这项结论掩盖。
对后者，`type-II-target-outside-support-quadratic-separation` 给出完全的第一道
代数划分：若 \(-1\notin K U(4AC)^2\)，就有一个消去全部素因子残数的二次特征，
并强制 \(\chi(p)=1\)；真正无法用二次特征剥离的是
\(-1\in K U(4AC)^2\) 的平方饱和核。更进一步，令 \(H_M\) 为核心素数允许残数；
分离特征在核心类上真正非平凡当且仅当 \(H_M\not\subset K U(4AC)^2\)。由于这类
特征仍可随 \(K\) 变化，下一步必须检查多条射线能否迫使有限个独立字符，或直接研究
平方饱和核。
其中“每条射线固定一个二次字符”已经有具体反例：
type-II-fixed-quadratic-character-boundary 在 \(M=80\) 给出两个实际核心失败，
其可用活跃字符互不相交。固定模数的有限字符并仍成立，却只重写已有的半横截面条件；
\(\chi(p)=1\) 由因子积自动推出，故此步骤本身不能增加筛维。
平方饱和也不是终点。type-II-two-power-character-depth-sieve 定义
\(\nu=\max\{d:-1\in K U(4AC)^{2^d}\}\)，并把深度 \(\nu\) 的支撑外失败压入
相对大小 \(2^{-(\nu+1)}\) 的高阶字符核。故若多条射线都已知深度至少 \(s\)，每条
可提供 \(1-2^{-(s+1)}\) 而非半个筛维；这仍是分层条件结论，未排除深度零和支撑内层。
但 type-II-character-product-congruence-compatibility-boundary 排除了一个看似自然的
跨射线路线：任意有限个字符核都同时含有 \(p\equiv1\) 的总积同余类，故
\(\chi_j(p)=1\) 的合取没有矛盾。要推进，必须使用各个移位数的逐因子分布或真正的
跨移位因子关联，不能只压缩为 \(p\) 的角色值。

贪心分解也不能代替这样的选择器。`greedy-one-step-terminal-obstruction` 给出核心素数
\(p=73\) 的精确反例：首步 \(1/19\) 后余项为 \(3/1387\)，而二项因子式要求
\(1387^2\) 有一个 \(2\pmod3\) 因子；实际所有正因子都为 \(1\pmod3\)。因此把
“不断作贪心分解”与“在所需的第三项处必能二项收尾”混为一谈，不能构成递降证明。
Roy 2026 的 HGDD 预印本正因这一终端断言而被审计为已反驳的负面记录。

另一种看似绕过因子条件的 LCM 除子格贪心也没有给出递降。Audige 2026 令
\(T=4L_n/n\)、\(L_n=\operatorname{lcm}(1,\ldots,n)\)，并声称总能将 \(T\) 写为
三个 \(L_n\) 的除子之和。`audige-divisor-lattice-completion-equivalence` 证明该断言
本身等价于存在三个分母都整除 \(L_n\) 的受限三项分解；\(T\) 为整数和 \(1\mid L_n\)
并不推出它。该稿的后续分割论证又以这个尚未建立的局部完成为输入，故不能提供本计划的
全称证书或递降边。

其中 Xu 所谓 tame 解恰为 \(K=1\) 的 Type II 切片：恢复的两个非首分母是
\(pACK,pBCK\)，它们同时整除 \(px\) 当且仅当 \(K=1\)，见
`type-II-tame-k-one-equivalence`。因此 tame/wild 的划分并不覆盖全部 Type II
证书空间；Xu-wild 只排除 \(K=1\)，仍可能存在 \(K>1\) 或 Type I 证书。
但 `type-II-finite-template-obstruction` 证明任何固定有限**三参数**模板集都会被一个
\(p\equiv1\pmod M\) 的 Dirichlet 素数列避开。因此固定 \((A,C,K)\) 窗口的完全覆盖只能是
计算现象；若走这条路线，至少 \(K\) 必须随 \(p\) 增长（如上述因子射线），或必须结合新的递降机制。

更细地说，合法外部源自动满足 \(i<p\)，因为 \(4i\le p+m\le2p-2\)。但其公式
\[
\left(x,\frac{x(p+i)}m,\frac{px(p+i)}{im}\right),\qquad x=\frac{p+m}{4},
\]
不读取 \(\operatorname{Sol}(i)\) 的任何元素。它由 \((p,i,m)\) 直接构造 \(p\) 的解；
若把它写成一个忽略输入的常值映射 \(\operatorname{Sol}(i)\to\operatorname{Sol}(p)\)，其数学内容仍只是已得到的证书，不能在外部源条件失败时产生新的递降见证。

第一条平方根级族还能用上界筛提升到“相对密度一的核心素数”结论，见 `p-plus-one-density-one-certificate`。这解释了为何它在大范围搜索中有效，却也强调密度结论不提供对每个残余素数的递降。

## 目标引理的逻辑边界

`short-certificate-descent-completeness-boundary` 给出一个必须保持清楚的界限：若
短界取自然范围 \(H(p)=p-2\)，则“对每个核心素数都有短证书或可闭合的严格递降”
与 Erdős--Straus 猜想本身等价。因而这不是一个可由现有参数化自动推出的辅助引理；
证明它已经是完整的证明。若取更强的 \(H(p)<p-2\)，该方案仍蕴含猜想，但它是严格更强的
研究目标，必须提供新的因子强制或新的标记解提升选择器。
