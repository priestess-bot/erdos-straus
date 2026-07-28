---
kind: claim
claim_id: type-II-ac-rays-superlog-residual
title: Type II 的 AC 因子射线共同残余可达到任意对数幂稀薄
statement: 取任意有限个正整数对 (A_j,C_j)，且 A_j^2 C_j 两两不同。未被相应 Type II AC 射线 p+4A_j^2C_j 的负一因子残数条件覆盖的核心素数数量为 O_S(X/(log X)^(1+|S|/2))。因而逃过全部正整数 AC 射线的核心素数集合对每个固定 B>0 都是 O_B(X/(log X)^B)。这不蕴含该集合为空。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- sieve
- density
- certificate
- type-II
- factorization
- ray
- residual-set
- proof-program
sources:
- paper: shute2022
  locator: Section 5.5, Lemma 5.5.1 (printed p. 57)
  role: explicit-fixed-dimension-upper-bound-sieve
- paper: montgomery_vaughan2007
  locator: Chapter 11, Corollaries 11.19/11.21
  role: fixed-modulus-PNT-in-arithmetic-progressions
- paper: elsholtz_tao2013
  locator: "Appendix A, shifted-prime additive functions and sieve estimates"
  role: methodological-foundation
- paper: bradford2024
  locator: "Propositions 2 and 4 (statements; the paper leaves their proofs to the reader)"
  role: Type-II-certificate-statement-context
- paper: chamberland2026
  locator: "Theorem 1"
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-28'
---

# Type II 的 \(AC\) 因子射线共同残余可达到任意对数幂稀薄

## 定理

令

\[
\mathcal S=\{(A_j,C_j):1\le j\le L\}\subset\mathbb N^2
\]

为有限集，并假设

\[
A_i^2C_i\ne A_j^2C_j\quad(i\ne j). \tag{1}
\]

对每个 \((A,C)\in\mathcal S\)，考虑 Type II 的 \(AC\) 射线条件

\[
N_{A,C}(p)=p+4A^2C,\qquad
h>1,\quad h\mid N_{A,C}(p),\quad h\equiv-1\pmod{4AC}. \tag{2}
\]

令 \(R_{\mathcal S}(X)\) 计数满足 \(p\le X\)、\(p\equiv1\pmod{24}\) 的素数，
并要求对每个 \((A,C)\in\mathcal S\) 都不存在 (2) 中的因子 \(h>1\)。则

\[
R_{\mathcal S}(X)
\ll_{\mathcal S}
\frac{X}{(\log X)^{1+L/2}}. \tag{3}
\]

当 \(p\ge4A^2C\) 时，(2) 自动恢复一张合法 Type II 证书；所以忽略有限多个小
\(p\) 后，\(R_{\mathcal S}(X)\) 正是逃过这些 \(AC\) 射线的核心素数数目。

特别地，令 \(R_{AC,\infty}(X)\) 计数逃过所有正整数对 \((A,C)\) 的 Type II
射线的核心素数。对任意固定 \(B>0\)，有

\[
R_{AC,\infty}(X)\ll_B\frac{X}{(\log X)^B}. \tag{4}
\]

## 证书的因子对形式

令 \(h=4ACK-1\)，并由 (2) 定义

\[
K=\frac{h+1}{4AC},\qquad m=\frac{p+4A^2C}{h}. \tag{5}
\]

则

\[
p+4A^2C=hm,\qquad
B'=Km-A=\frac{Kp+A}{h}. \tag{6}
\]

若 \(p\ge4A^2C\)，则 \(B'\ge A\)。所以

\[
(m,x,d)=\left(m,AB'C,A^2C\right) \tag{7}
\]

是 Type II 证书。这是 `type-II-raw-ray-certificate` 的因子形式；(6) 还说明
证书缺口正是所选因子 \(h\) 的互补因子。

为验证第二个等式，代入 \(p=hm-4A^2C\)：

\[
Kp+A=Khm-A(h+1)+A=h(Km-A).
\]

又 \(p\equiv1\pmod4\)、\(h\equiv-1\pmod4\)，故 \(m\equiv3\pmod4\)。
因 \(h\) 不可能等于 \(N_{A,C}(p)\)（二者模 \(4\) 分别为 \(3,1\)），有 \(m>1\)，
从而 \(m\ge3\)。其余自然范围和序条件由

\[
B'-A=\frac{K(p-4A^2C)+2A}{h}\ge0
\]

给出。

## 失败的半大小横截面

固定一对 \((A,C)\)，设 \(p>4A^2C\)。此时

\[
\gcd(N_{A,C}(p),4AC)=1. \tag{8}
\]

令 \(G_{A,C}=(\mathbb Z/4AC\mathbb Z)^\times\)。其上的对合

\[
r\longmapsto-r^{-1} \tag{9}
\]

没有不动点：任意单位 \(r\) 都是奇数，故 \(r^2\equiv1\pmod4\)，不可能
\(r^2\equiv-1\pmod{4AC}\)。所以 \(G_{A,C}\) 被分解为等大的二元组。

若 \(N_{A,C}(p)\) 有两个素因子，其模 \(4AC\) 残数为同一对中的
\(r,-r^{-1}\)，则两者乘积给出一个 \(-1\pmod{4AC}\) 的因子，违反射线失败。
因此失败时，\(N_{A,C}(p)\) 的全部素因子残数包含在某个横截面

\[
T_{A,C}\subset G_{A,C},\qquad |T_{A,C}|=\frac12\varphi(4AC). \tag{10}
\]

这只是失败的必要条件；横截面内多个素因子的积仍可能给出 \(-1\)，故不能反向使用。

## 筛法证明

固定每个 \((A,C)\) 的横截面选择。令

\[
Q=\operatorname{lcm}\bigl(24,\{4A_jC_j:1\le j\le L\}\bigr). \tag{11}
\]

写 \(p=24t+1\)。除有限个整除 \(Q\) 或任一非零差

\[
4(A_i^2C_i-A_j^2C_j) \tag{12}
\]

的素数 \(\ell\) 外，筛去根

\[
24t+1\equiv0\pmod\ell, \tag{13}
\]

以及对每个满足 \(\ell\bmod4A_jC_j\notin T_{A_j,C_j}\) 的 \(j\)，筛去

\[
24t+1+4A_j^2C_j\equiv0\pmod\ell. \tag{14}
\]

(1) 保证 (14) 的根彼此不同；它们也不同于 (13) 的根。按模 \(Q\) 的可逆素数
类平均，(10) 表明每条 (14) 平均贡献一个禁根的 \(1/2\)。因此局部禁根的平均数为

\[
1+\frac L2. \tag{15}
\]

以下把这一平均值提升为上界筛所需的完整输入，而不是只引用筛积的启发式。

### 局部根、CRT 误差与筛维

记 \(\mathcal E\) 为所有整除

\[
Q\prod_{i<j}4\lvert A_i^2C_i-A_j^2C_j\rvert
\]

的素数的有限集合。取一个固定的阈值 \(y_{\mathcal S}>L+1\)，使其大于
\(\mathcal E\) 中所有素数。对 \(\ell>y_{\mathcal S}\)，令
\(\Omega_\ell\) 是 (13) 与所有适用 (14) 的根集，且令

\[
\nu(\ell)=\lvert\Omega_\ell\rvert
=1+\sum_{j=1}^{L}
 \mathbf 1_{\ell\bmod 4A_jC_j\notin T_{A_j,C_j}}. \tag{16}
\]

此处 \(\ell\nmid Q\)，所以每个出现的线性式都有唯一根；又由对
\(4(A_i^2C_i-A_j^2C_j)\) 的排除，这些根两两不同。特别地
\(0\le\nu(\ell)\le L+1<\ell\)。

设 \(Y=\lfloor(X-1)/24\rfloor\)，
\(\mathcal A_X=\{1,\ldots,Y\}\)。对只含大于 \(y_{\mathcal S}\) 的素因子的
平方自由数 \(d\)，把各 \(\Omega_\ell\) 由中国剩余定理合并为
\(\nu(d)=\prod_{\ell\mid d}\nu(\ell)\) 个模 \(d\) 的根。于是精确地有

\[
\lvert\mathcal A_{X,d}\rvert
=Y\frac{\nu(d)}d+r_d,
\qquad\lvert r_d\rvert\le\nu(d). \tag{17}
\]

这是上界筛的余项公式；它不使用 \(24t+1\) 的素数分布。

令 \(M_j=4A_jC_j\)。固定模数 \(Q\) 的算术级数素数定理及分部求和给出：对
每个 \((a,Q)=1\)，

\[
\sum_{\substack{\ell\le v\\ \ell\equiv a\pmod Q}}\frac1\ell
=\frac1{\varphi(Q)}\log\log v+O_Q(1). \tag{18}
\]

模 \(Q\) 的单位类投到模 \(M_j\) 的单位类时纤维大小相同，而横截面补集占
\(U(M_j)\) 的一半。因此由 (16)、(18)，

\[
\sum_{y_{\mathcal S}<\ell\le v}\frac{\nu(\ell)}\ell
=\left(1+\frac L2\right)\log\log v+O_{\mathcal S}(1). \tag{19}
\]

记 \(\kappa=1+L/2\)，并定义

\[
V(v)=\prod_{y_{\mathcal S}<\ell<v}
 \left(1-\frac{\nu(\ell)}\ell\right).
\]

因为 \(\sum_\ell\nu(\ell)^2/\ell^2<\infty\)（这里 \(\mathcal S\) 固定），
对数展开和 (19) 给出

\[
V(v)\asymp_{\mathcal S}(\log v)^{-\kappa}. \tag{20}
\]

增大一个只依赖 \(\mathcal S\) 的常数 \(K\ge1\) 后，所有
\(2\le w\le v\) 都满足

\[
\frac{V(w)}{V(v)}
\le K\left(\frac{\log v}{\log w}\right)^\kappa. \tag{21}
\]

故 (17)、(21) 正是固定筛维 \(\kappa\) 的基本上界筛假设。

### 显式上界筛收口

取

\[
D=X^{1/3},\qquad
b=\left\lceil9\kappa+10\log K+2\right\rceil,\qquad
z=D^{1/b}. \tag{22}
\]

则 \(b\ge9\kappa+1\)，且 Shute 的 Lemma 5.5.1 中筛积主项的相对误差至多
\(e^{9\kappa-b}K^{10}\le e^{-2}\)。该引理的组合系数绝对值不超过 \(1\)。由
(17) 及

\[
\nu(d)\le(L+1)^{\omega(d)}\le\tau_{L+1}(d),
\qquad
\sum_{d\le D}\tau_{L+1}(d)
\ll_{\mathcal S}D(1+\log D)^L, \tag{23}
\]

其截断余项为 \(O_{\mathcal S}(X^{1/3}(\log X)^L)\)。因此，令
\(S_{\mathcal S}(X,z)\) 为避开所有 \(y_{\mathcal S}<\ell<z\) 禁根的
\(t\in\mathcal A_X\) 数目，则

\[
\begin{aligned}
S_{\mathcal S}(X,z)
&\ll_{\mathcal S}YV(z)+X^{1/3}(\log X)^L\\
&\ll_{\mathcal S}\frac{X}{(\log X)^{1+L/2}}.
\end{aligned}\tag{24}
\]

忽略 \(p\le\max_j4A_j^2C_j\) 的有限项后，若 \(p=24t+1>z\) 且所有指定射线
均失败，前节的横截面必要条件使 \(t\) 避开上述每一个禁根。被首个禁根删去的只有
\(p\le z\) 的素数，数目 \(O(z)\)，已被 (24) 吸收。故对固定的一组横截面选择，
失败核心素数数目具有 (24) 的上界。横截面系统的数目是有限常数
\(\prod_j2^{\varphi(4A_jC_j)/2}\)；对它们求和即得 (3)。

最后，对任意 \(B>0\)，取

\[
\mathcal S_L=\{(1,C):1\le C\le L\},
\qquad L\ge2(B-1). \tag{25}
\]

它满足 (1)。逃过所有 \(AC\) 射线的集合包含于逃过 \(\mathcal S_L\) 的集合，故
(3) 推出 (4)。

## 边界

这一定理把 `type-II-ac-ray-saturation-conjecture` 的失败集压得极薄，但没有证明它为空。
在 (25) 中，\(L\) 依赖于所要求的固定对数幂，且隐含常数随 \(\mathcal S_L\) 变化；
一个无限集合仍可满足 (4)。因此它不能替代逐点因子选择器或真正的递降机制。

此外，`divisor-residue-subgroup-exception-boundary` 证明：不能指望把每条失败射线的
全部素因子残数普适压缩为“不含 \(-1\) 的真子群加 \(o(\varphi(4AC))\) 个异常项”。
偶阶循环商存在长度线性的 Kneser 临界序列。若要改进这里的半大小横截面，结构分类至少
还必须容纳这类双向算术级数，并利用不同移位射线之间的算术不相容性。

其中最尖锐的“支撑子群只漏掉 \(-1\)”主型现在可确定性剥离：
`type-II-support-critical-congruence-trap` 证明它强制
\(p\equiv1\pmod {4AC}\)，而有限多条此型射线同时出现时会强制相应模数最小公倍数的
同余一。它没有处理缺失集至少含两个元素的普通非临界失败，但提供了一条不依赖概率模型的
临界同余陷阱。

多孔支撑内失败也不是毫无结构。`type-II-support-defect-orbit-constraint` 证明：
若 \(-1\) 已在素因子残数生成子群中，缺失集在 \(x\mapsto px^{-1}\) 下成轨道；
非平凡两孔时只能缺 \(\{-1,-p\}\)，非平凡奇孔时 \(p\) 必为该射线模数的二次剩余。
但大多数有限审计失败属于 \(-1\) 不在生成子群的支撑外主型，故这不是对全部失败的分类。

支撑外主型亦可精确剥去一个平方商层：`type-II-target-outside-support-quadratic-separation`
证明，只有当 \(-1\in K U(4AC)^2\) 时，才没有一个消去 \(K\) 而取
\(-1\) 为负的二次特征。更精确地，只有核心残数子群
\(H_M\not\subset K U(4AC)^2\) 时，才有一个对 \(p\equiv1\pmod{24}\) 非平凡的
分离特征；否则 \(\chi(p)=1\) 可能只重复已知同余。所以即使进入核心活跃层，特征仍
可随 \(K\) 变化，不能把这一代数分解误报为固定新增筛维。

这种“随 \(K\) 变化”不是措辞上的小缺口：`type-II-fixed-quadratic-character-boundary`
给出 \(M=80\) 的两个实际失败，其可用核心活跃字符互不相交，故每条射线选一个固定
字符的强化式已失败。虽然固定模数下仍可取有限字符并，但每个核只是已有半大小横截面，
且 \(\chi(p)=1\) 已由素因子核条件推出；单靠此改写不增加本定理的筛指数。

不过“二次不可分”并非最终核。`type-II-two-power-character-depth-sieve` 按
\(-1\in K U(M)^{2^d}\) 的最大深度分层，给出阶 \(2^{d+1}\) 的字符核；若一组
射线都处于深度至少 \(s\) 的支撑外层，每条的条件性筛贡献提升到
\(1-2^{-(s+1)}\)。这是一条严格更强的分层残余界，但深度零及支撑内失败仍在本定理的
原始半大小边界中。
