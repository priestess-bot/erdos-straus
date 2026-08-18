# T6 proper-root 最小缺口审计

> 复核日期：2026-08-17
>
> 文档角色：局部参数化与开放量词审计，不是 T6 closure claim。
>
> 结论：`PROPER_ROOT_SELECTOR_TOTALITY = OPEN`。

## 1. Scope

只考虑已经通过 actual source/path、terminal-first 和 canonical maximal
complete-excess 检验的 proper-root stutter receipt。沿用

\[
D=mp+1-h,\qquad eD=ph+1,\qquad a=em-h,
\]

\[
b=e-1,\qquad N=a^2-ab+b^2=hk,
\]

其中

\[
p\equiv1\pmod {24},\qquad h=3u,\qquad (u,6)=1,
\qquad h\mid p^2+p+1,\qquad 2\le h<p.
\]

本页不假设这种 actual receipt 存在，也不把满足部分整数等式的抽象元组当作 actual
state。

## 2. \(k=1\) 的精确参数化与 actual 全称排除

先只使用 \(k=1\) 和 stutter 整数等式。此时

\[
h=N=a^2-a(e-1)+(e-1)^2,
\qquad h=em-a.
\tag{1}
\]

两式相减并除以 \(e\)，得到

\[
m=\frac{(a+1)^2}{e}+e-a-2.
\tag{2}
\]

所以

\[
\boxed{e\mid(a+1)^2.}
\tag{3}
\]

令 \(g=(e,a+1)\)。写 \(e=gx\)、\(a+1=gy\) 且 \((x,y)=1\)。由 (3)
有 \(x\mid g\)，故存在正整数 \(d\) 使

\[
\boxed{e=dx^2,\qquad a=dxy-1,\qquad (x,y)=1.}
\tag{4}
\]

范围 \(1\le a<e\) 强制 \(1\le y\le x\)。代回 (2) 得

\[
\boxed{m=d(x^2-xy+y^2)-1.}
\tag{5}
\]

另一方面，\(p\) 为整数恰要求

\[
a\mid e(h-1)+1.
\]

在模 \(a=dxy-1\) 下有 \(e\equiv xy^{-1}\)。又由 (1)
\(h\equiv(e-1)^2\pmod a\)。乘以可逆的 \(y^3\) 后，整数门精确化为

\[
\boxed{
dxy-1\mid x^3-2x^2y+y^3
=(x-y)(x^2-xy-y^2).
}
\tag{6}
\]

令 \(Q=x^2-xy+y^2\)。给定满足 (4)--(6) 的参数，抽象候选有闭式

\[
h=d^2x^2Q-dx(x+y)+1,\qquad
p=\frac{d^3x^4Q-d^2x^3(x+y)+1}{dxy-1}.
\tag{7}
\]

恢复。反向地，每个 \(k=1\) 抽象整数 stutter 都有上述参数化。

### 2.1 对角子类已严格排除

若 \(y=x\)，由 \((x,y)=1\) 得 \(x=y=1\)，从而 \(a=e-1\) 且

\[
h=a^2.
\]

actual root 有 \(h=3u\)、\(3\nmid u\)，所以 \(v_3(h)=1\)；一个被 3 整除的平方却有
偶数 3-adic 赋值。故 actual \(k=1\) 候选必须满足

\[
\boxed{1\le y<x.}
\tag{8}
\]

### 2.2 Actual 奇偶与模 3 必要条件

actual root 有 \(a,h\) 为奇数，所以

\[
\boxed{dxy\equiv0\pmod2.}
\tag{9}
\]

当 \(k=1\) 时 \(3\nmid k\)。既有 3-adic 分流强制

\[
m\equiv1\pmod3,
\qquad
a\equiv e\equiv2\pmod3.
\]

代入 (4) 后等价于

\[
\boxed{
d\equiv2\pmod3,\qquad 3\nmid x,\qquad 3\mid y.
}
\tag{10}
\]

由于 \(a\) 为奇数且 \(a\equiv2\pmod3\)，有 \((a,24)=1\)。所以在 \(p\) 已由
(7) 恢复为整数后，核心同余 \(p\equiv1\pmod {24}\) 精确等价于

\[
\boxed{
d^3x^4Q-d^2x^3(x+y)-dxy+2\equiv0\pmod {24}.
}
\tag{11}
\]

这些只是必要的局部条件；相应模系统并不自动为空。

### 2.3 Actual \(k=1\) 域已严格为空

actual root 条件补上了抽象参数化中缺失的全称排除。令

\[
g_0=(a,e-1),\qquad a=g_0A,\qquad e-1=g_0B,
\qquad H=A^2-AB+B^2.
\]

若 \(k=1\)，则 \(h=N=g_0^2H\)。由 \(pa+e-1=eh\) 得

\[
A^2(p^2+p+1)
=H\left[e^2g_0^2H+eg_0(A-2B)+1\right].
\]

而 actual root 有 \(g_0^2H=h\mid p^2+p+1\)，所以方括号必须被 \(g_0^2\)
整除；它模 \(g_0\) 却等于 1。故 \(g_0=1\)。

令 \(P_2=x^2-xy-y^2\)。式 (6) 与两个恒等式

\[
x(dxy-1)-y(dx^2-1)=y-x,
\qquad
(dx^2-1)-(dxy-1)=dx(x-y)
\]

于是给出

\[
(dxy-1,x-y)=(a,e-1)=1,
\qquad a\mid P_2.
\]

actual 模 3 条件精确强制 \(d\equiv2\pmod3\)、\(3\nmid x\)、\(3\mid y\)，
所以 \(d\ge2,y\ge3,x>y\)。由此 \(P_2\) 不可能为零或负，故

\[
P_2=c(dxy-1),\qquad c>0.
\]

保持同一 \(d,c\) 的两步 Vieta 下降

\[
L=dc+1,\qquad q=x-Ly,\qquad r=y-Lq
\]

把每个 \(y>1\) 的互素正解严格送到

\[
0<r<q<y<x,
\]

并保持

\[
x^2-Lxy-y^2+c=q^2-Lqr-r^2+c=0.
\]

下降终点 \(y=1\) 强制 \(c=1\)。但此时
\(P_2\equiv x^2\equiv1\pmod3\)，而 \(a=dxy-1\equiv2\pmod3\)，矛盾。因此

\[
\boxed{
\forall S\in\mathcal S_{\mathrm{pr}},\qquad k(S)\ne1.
}
\tag{QC0-empty}
\]

完整证明与无有限扫描的符号核验见
[actual proper-root stutter 的 k=1 全称排除](../claims/type-I-root-capacity-stutter-k-one-universal-exclusion.md)。
这只清空 \(k=1\) 子域；actual maximality、terminal-first 与 source/path 条件不再需要
逐项过滤一个已经不存在的候选。

## 3. 两种 carrier 不可混同

proper-root residual 同时出现两类结构上不同的因子。

### 3.1 Eisenstein quotient carrier

\[
k=\frac Nh,\qquad 1\le k<\frac p4,
\]

且 \(k\) 的素因子只可能是 3 或 \(1\pmod3\)。当 \(k>1\) 时，形式上可构造

\[
R_k\equiv-p^{-1}\pmod {4k},\qquad
K_k=\frac{pR_k+1}{4},\qquad k\mid K_k.
\]

但 \(q\mid k\) 只带有 quotient algebra；它不自动对应 actual source/path 中的 charged
occurrence，也没有给出 \(W_T\to W_S\) 的 E4 lift。

### 3.2 Transverse receipt carrier

令

\[
D_*=\frac{D}{(D,h^2-1)}.
\]

已有 actual-receipt 定理给出

\[
1<D_*\mid\gcd(T/u,m+2r),
\]

以及

\[
(D_*,pM_0(2r+1)(m-1))=1.
\]

因此 \(q\mid D_*\) 确实来自 actual \(D\)，但它恰好没有现有 root-capacity menu 所需的
\(q\mid u\) provenance。现有 low-gap、正根、反射和 overlap 分派都只有条件性覆盖；
一般 \(L>1\) negative-root pure-\(T\) 分支，以及不命中这些有限多项式门的分支，仍没有
terminal 或 E1--E5 edge。

所以 \(q\mid k\) 与 \(q\mid D_*\) 不能互相替换：前者有 Eisenstein quotient 结构但缺
physical occurrence，后者有 receipt occurrence 但缺可消费的 source provenance。

### 3.3 \(k=3\) 的窄 fiber 收缩

当 \(k=3\) 时，actual \(3\)-adic 条件强制 \((a,e-1)=3\)。写

\[
A=\frac a3,\qquad B=\frac{e-1}{3},\qquad
d=\frac{(3A+2)^2-3}{3B+1},
\]

则 \(1\le A<B\)、\(d\equiv1\pmod3\)，并有 fixed-\(d\) 的有限除子门

\[
4\le d\le3A-2,
\qquad
A\mid3d^2+d-1.
\]

所以每个固定 \(d\) 只留下有限个 \(A\) 候选，然后 \(B,m,p\) 均可由闭式重建。
对偶地令 \(\rho=B-A\)，则同一 primitive system 还等价地给出

\[
A\mid3\rho^2+\rho-1,
\qquad
3(A+\rho)+1\mid9\rho^2-6\rho-2,
\]

所以固定 \(\rho\) 也是有限 divisor fiber。再写 \(j=m-\rho\)，则

\[
A\mid9j^2+7j+1,
\qquad
\rho(3j+1)+j=3A(A-j+1),
\]

故固定 \(j\) 同样只留下有限个 \(A\)-divisor，再由该等式唯一恢复 \(\rho\)。这一步
从旧的 \(A\mid3(9j^2+7j+1)\) 中消去了多余的因子 \(3\)；它仍不提供 \(j\) 的全局界。
共享的 \(A=1\) fiber 唯一恢复 \(\rho=6\)、\(p=939\)，非核心；这与已有的
\((m,a)=(6,3)\) small-root 排除行相同，用于交叉验证而不另计一个 closure。\(d\)、
\(\rho\) 与 \(j\) 都没有全局上界，这不是 \(k=3\) 的全称排空，更不是 QC1 的
physicalization。完整约化见
[\(k=3\) primitive fiber reduction](../claims/type-I-root-capacity-stutter-k-three-primitive-fiber-reduction.md)。
一个看似自然的同-\(M\) Vieta 递降也已被精确排除：第一 primitive equation 的另一
\(B\)-根恰为 \(j\)，但它若要通过第二整数门，就会强制 \(j=A-1\)，最终只剩失败的
\((A,j)=(3,2)\) 残余。故该 companion 不能成为 integer target；它是路线障碍而不是
QC1 closure，详见
[Vieta companion obstruction](../claims/type-I-root-capacity-stutter-k-three-vieta-companion-obstruction.md)。

## 4. 最小开放量词

令 \(\mathcal S_{\mathrm{pr}}\) 表示所有实际可达、terminal-first 后仍非终端的
proper-root stutter states，并定义

\[
\operatorname{Exit}(S)\iff
\operatorname{terminal}(S)
\ \lor\
\exists T\;\bigl(
E1(S,T)\land E2(T)\land E3(T)\land E4(T\to S)
\land\Pi_{T5}(T)<\Pi_{T5}(S)
\bigr).
\]

该子域的 T6 目标就是

\[
\boxed{
\forall S\in\mathcal S_{\mathrm{pr}},\quad \operatorname{Exit}(S).
}
\tag{PR-T6}
\]

按 quotient 路线，\(k=1\) 分支已经由 (QC0-empty) 全称排空，所以

\[
\forall S\in\mathcal S_{\mathrm{pr}},\ k(S)=1
\Longrightarrow\operatorname{Exit}(S),
\tag{QC0}
\]

现已真空成立。唯一仍开放的 quotient-carrier 量词是

\[
\forall S\in\mathcal S_{\mathrm{pr}},\ k(S)>1
\Longrightarrow
\left[
\operatorname{terminal}(S)\ \lor\
\exists q\mid k(S)\ \exists T\;
\operatorname{PhysicalE1toE5}(S,q,T)
\right].
\tag{QC1}
\]

按 transverse 路线，一个同样足够但尚未证明的局部引理是

\[
\forall S\in\mathcal S_{\mathrm{pr}},\quad
\operatorname{terminal}(S)\ \lor\
\exists q\mid D_*(S)\ \exists T\;
\operatorname{PhysicalE1toE5}(S,q,T).
\tag{TR1}
\]

这里 `PhysicalE1toE5` 必须包括 actual source replay、确定 target、target normal form、
全域 solution lift 和 T5 ticket；“\(q\) 较小”“\(q\mid K_q\)”或一条 q-adic 同余均不够。

## 5. 已知路线障碍

现有 Dirichlet--CRT no-go 已证明：只读取 low-gap negative-root 的同一个 \(q\)，并不断
添加有限多个固定条件 \(q\mid p+r\)，不能在 q-local 层全称关闭该负支。它不构造 actual
receipt 反例，但说明 (TR1) 不能由有限 fixed-gap same-carrier 菜单推出。下一步至少要读取
可变 gap、不同 carrier、多因子结构，或 canonical maximality 的额外非局部数据。

另一个具体纠偏是：T6-V1 中的
\(p=20\,065\,847\,377,m=6768,a=141,k=3\) 线索既不满足 actual root
divisibility，又被 gap-3 Type II terminal 抢占；详见
[数值线索审计](../claims/type-I-root-capacity-stutter-t6-numeric-clue-preemption.md)。它不能充当
(QC1) 或 (TR1) 的 actual 控制。

## 6. 结论边界

本页严格完成了 \(k=1\) 的参数化与 actual 全称排除；\(k=3\) 现有
fixed-\(d\)、fixed-\(\rho\)、fixed-\(j\) 三个有限 fiber 坐标，并排除了保持
\(A,M\) 的直接 Vieta companion。它们收紧整数曲线和后续候选路线，但不 physicalize
\(q\mid k\)，也不为 \(q\mid D_*\) 构造全称 successor。(PR-T6) 的 quotient 剩余仍
精确位于 \(k>1\) 的 (QC1)。因此 (QC0) 已闭合，但 proper-root 子域和 T6 仍保持开放。
