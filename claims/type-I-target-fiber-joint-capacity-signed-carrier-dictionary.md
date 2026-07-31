---
kind: claim
claim_id: type-I-target-fiber-joint-capacity-signed-carrier-dictionary
title: 目标纤维溢出与联合容量的带符号载体字典
statement: 在合法核心图表 4K=pR+1、x_R=(p+R)/4 中，设 P,Q 互素且 P/Q 模 R 为 -1，令 z_l=v_l(P)-v_l(Q)、L=PQ，并以 K 和 x_R 的赋值向量 nu、sigma 及联合预算 mu=max(nu,sigma) 计量。则 e_K(L)、e_x(L) 与共同过载 C(L) 分别精确等于 z 对 nu、sigma、mu 的盒外向量的整数编码；strict split 恰等价于 z 位于联合盒 B_mu 但同时越出 B_nu、B_sigma，共同过载则恰等价于 z 越出 B_mu。给定表示见证 z 后，溢出的正负部分还指出实际承载该 q 进需求的是 P 还是 Q；无符号 Pareto 向量本身不保留该方向。若两个任意目标表示在 K 外坐标完全相同、在 K 内逐坐标相距不超过 nu，则它们仍直接产生偶终端；联合盒内目标表示数超过显式分箱数时必有这种近邻对。对已经非空的完整目标纤维扩张生成元支撑时，旧坐标的 forced height 只能下降，新坐标的 forced height 恒为零；因此 sink-SCC 新标签不能自动制造单素数强制收费，必须保留多坐标 Pareto 价格或受限路径语言。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-target-fiber-fourier-overflow-generating-function
  - type-I-target-fiber-neighbor-terminal
  - type-I-source-word-joint-capacity-common-split-dichotomy
topics:
  - type-I
  - target-fiber
  - Fourier
  - Pareto
  - q-adic-capacity
  - common-overload
  - split-capacity
  - signed-carrier
  - near-pair
  - proof-program
sources:
  - claim: type-I-target-fiber-fourier-overflow-generating-function
    role: canonical-target-fiber-and-Pareto-interface
  - claim: type-I-target-fiber-neighbor-terminal
    role: in-box-neighbor-terminal
  - claim: type-I-source-word-joint-capacity-common-split-dichotomy
    role: joint-capacity-defects
visibility: public
last_checked: '2026-08-01'
---

# 目标纤维溢出与联合容量的带符号载体字典

## 1. 相位 -1 表示的指数坐标

固定合法核心图表

\[
p\equiv1\pmod {24},
\qquad p\text{ 为素数},
\qquad R\equiv3\pmod4,
\qquad 3\le R\le p-2,
\]

并记

\[
4K=pR+1,
\qquad
x_R=\frac{p+R}{4}.
\]

于是 \((Kx_R,R)=1\)。再取互素正整数 \(P,Q\)，满足

\[
(PQ,R)=1,
\qquad
P+Q\equiv0\pmod R.
\tag{1}
\]

于是 \(P/Q\equiv-1\pmod R\)。令有限素数集 \(\mathcal P\) 包含 \(P,Q,K,x_R\) 的全部
素因子，并定义

\[
z_\ell=v_\ell(P)-v_\ell(Q)
\qquad(\ell\in\mathcal P).
\tag{2}
\]

由于 \((P,Q)=1\)，每个素数至多出现在一侧，所以

\[
\boxed{|z_\ell|=v_\ell(PQ).}
\tag{3}
\]

若

\[
\phi(z)=\prod_{\ell\in\mathcal P}\ell^{z_\ell}\pmod R,
\tag{4}
\]

则 (1) 等价于

\[
\boxed{\phi(z)=-1.}
\tag{5}
\]

所以每个来源路径字产生的互素交叉目标对，不只是一项乘积 \(L=PQ\)，还规范产生目标
纤维中的一个带符号指数点 \(z\)。符号记录过量素数实际位于哪一个整数因子上。

## 2. 三种容量恰是三个盒外向量

记

\[
\nu_\ell=v_\ell(K),
\qquad
\sigma_\ell=v_\ell(x_R),
\qquad
\mu_\ell=\max(\nu_\ell,\sigma_\ell),
\tag{6}
\]

并对任意非负预算向量 \(h\) 定义

\[
\operatorname{ov}_h(z)_\ell=(|z_\ell|-h_\ell)_+,
\qquad
\operatorname{Enc}(e)=\prod_{\ell\in\mathcal P}\ell^{e_\ell}.
\tag{7}
\]

令 \(L=PQ\)。联合容量主张中的三个缺陷因子满足

\[
e_K(L)=\frac{L}{(L,K)},
\qquad
e_x(L)=\frac{L}{(L,x_R)},
\qquad
C(L)=\frac{L}{(L,\operatorname{lcm}(K,x_R))}.
\tag{8}
\]

逐素数使用 (3) 立即得到完整字典

\[
\boxed{
e_K(L)=\operatorname{Enc}(\operatorname{ov}_\nu(z)),
\quad
e_x(L)=\operatorname{Enc}(\operatorname{ov}_\sigma(z)),
\quad
C(L)=\operatorname{Enc}(\operatorname{ov}_\mu(z)).
}
\tag{9}
\]

这不是只比较素因子支撑；(9) 保留每个共同过载层的精确 \(q\)-进高度。

### 证明

以第一式为例，其 \(\ell\)-进指数为

\[
v_\ell(L)-\min(v_\ell(L),v_\ell(K))
=(|z_\ell|-\nu_\ell)_+.
\]

第二式相同。又因

\[
v_\ell(\operatorname{lcm}(K,x_R))
=\max(\nu_\ell,\sigma_\ell)=\mu_\ell,
\]

第三式也成立。证毕。

## 3. common 与 strict split 的目标纤维几何

令

\[
B_h=\{z\in\mathbb Z^{\mathcal P}:|z_\ell|\le h_\ell\ \forall\ell\}.
\tag{10}
\]

由 (9) 有

\[
\begin{aligned}
L\mid K&\iff z\in B_\nu,\\
L\mid x_R&\iff z\in B_\sigma,\\
L\mid\operatorname{lcm}(K,x_R)&\iff z\in B_\mu.
\end{aligned}
\tag{11}
\]

因此，在 \(L\nmid K\) 且 \(L\nmid x_R\) 的双 miss 域中，联合容量二分精确变成

\[
\boxed{
\begin{aligned}
C(L)>1
&\iff z\notin B_\mu,
&&\text{共同过载};\\
C(L)=1
&\iff z\in B_\mu\setminus(B_\nu\cup B_\sigma),
&&\text{strict split}.
\end{aligned}}
\tag{12}
\]

所以 strict split 不是“接近共同过载”的模糊状态，而是一个精确的三盒几何区域：它在
联合盒内，却同时位于两个单容量盒外。

逐坐标还有互补恒等式。若

\[
r_\nu=(|z_\ell|-\nu_\ell)_+,
\qquad
r_\sigma=(|z_\ell|-\sigma_\ell)_+,
\]

则

\[
\boxed{
\min(r_\nu,r_\sigma)=(|z_\ell|-\mu_\ell)_+,
\qquad
\max(r_\nu,r_\sigma)
=(|z_\ell|-\min(\nu_\ell,\sigma_\ell))_+.
}
\tag{13}
\]

第一式就是共同过载取两个缺陷逐坐标最小值；第二式则是缺陷并集。

## 4. 溢出符号给出实际整数载体

定义

\[
c_\ell^+=(z_\ell-\mu_\ell)_+,
\qquad
c_\ell^-=(-z_\ell-\mu_\ell)_+.
\tag{14}
\]

显然每个 \(\ell\) 至多有一个正方向，并且

\[
\operatorname{ov}_\mu(z)_\ell=c_\ell^++c_\ell^-.
\tag{15}
\]

由互素性还得到真正的整除载体：

\[
\boxed{
\begin{aligned}
c_\ell^+>0&\Longrightarrow
\ell^{\mu_\ell+c_\ell^+}\mid P,\\
c_\ell^->0&\Longrightarrow
\ell^{\mu_\ell+c_\ell^-}\mid Q.
\end{aligned}}
\tag{16}
\]

并且

\[
\boxed{C(L)=\prod_\ell\ell^{c_\ell^++c_\ell^-}.}
\tag{17}
\]

因此，一旦同时保留表示见证 \(z\)，一个正溢出坐标就不再只是抽象价格：它指向
\(P\) 或 \(Q\) 中的一个实际整数因子。式 (16) 给出从“表示--对偶”进入跨状态载体
计数的候选算术标签；它本身尚未给出共同载体区间、标签互异性或重复度上界。

## 5. 与 Fourier 生成函数的精确接口

这里必须先固定状态级或候选族级有限支撑 \(\mathcal P_0\)，它包含 \(K,x_R\) 以及所
量化全部来源路径或 bottom-SCC 表示中允许出现的素数。每个具体 \((P,Q)\) 的指数向量
都在 \(\mathcal P_0\) 上补零。下述“规范”或“选择不变”只相对于固定数据
\((R,\mathcal P_0,\mu)\) 成立；改变生成元支撑会改变整个目标纤维和 Pareto 前沿。

对该固定支撑、目标 \(-1\) 和预算 \(\mu\)，令
\(\mathcal F_{-1}^{(\mu)}(\mathbf T)\) 为已有的目标纤维溢出 Fourier 生成函数。其系数
定理说明

\[
[\mathbf T^e]\mathcal F_{-1}^{(\mu)}
=\#\{z:\phi(z)=-1,\operatorname{ov}_\mu(z)=e\}.
\tag{18}
\]

每个互素相位 \(-1\) 对 \((P,Q)\) 由 (2) 向

\[
e=\operatorname{ov}_\mu(z)
\tag{19}
\]

贡献一个正计数，而 (17) 正是该单项式的整数编码。于是：

1. 常数项 \(e=0\) 计数全部联合盒表示；
2. 其中 \(z\in B_\nu\cup B_\sigma\) 是直接 Type I/II 容量命中；
3. 余下的常数项正是 strict split；
4. 非零 Pareto 首层正是相对于固定支撑的选择不变共同过载需求。

这补上了此前两个分离接口之间的字典：Fourier 生成函数不是另一种“类似容量”的对象，
它的 Newton 支撑就是联合容量缺陷向量本身。

但 \(\mathcal F_{-1}^{(\mu)}(\mathbf T)\) 是无符号对象：\(z\) 与 \(-z\) 给出同一
单项式，却交换 \(P,Q\) 两侧，因而不能从无符号 Pareto 向量恢复 (14) 的方向。若要在
Fourier 层保留该方向，对每个特征 \(\chi\) 和
\(\lambda_{\ell,\chi}=\chi(\ell)\) 应改用

\[
\begin{aligned}
P^{\pm}_{\ell,\chi}(T_\ell^+,T_\ell^-)
={}&\sum_{n=-\mu_\ell}^{\mu_\ell}\lambda_{\ell,\chi}^n\\
&+\sum_{e\ge1}\lambda_{\ell,\chi}^{\mu_\ell+e}(T_\ell^+)^e
+\sum_{e\ge1}\lambda_{\ell,\chi}^{-\mu_\ell-e}(T_\ell^-)^e.
\end{aligned}
\tag{20}
\]

对 \(\prod_\ell P^{\pm}_{\ell,\chi}\) 作相同特征平均后，
\([(\mathbf T^+)^u(\mathbf T^-)^v]\) 才精确计数满足
\((c^+,c^-)=(u,v)\) 的目标表示。令 \(T_\ell^+=T_\ell^-=T_\ell\) 即退化回无符号
生成函数。反足对称仍会给出交换两侧的成对表示，但不再丢失每个见证自身的颜色。

若记 \(N_h=|\phi^{-1}(-1)\cap B_h|\)，则常数项中的 strict split 数还有精确公式

\[
\boxed{
N_{\rm split}=N_\mu-N_\nu-N_\sigma+N_{\min(\nu,\sigma)}.
}
\tag{21}
\]

这里使用了 \(B_\nu\cap B_\sigma=B_{\min(\nu,\sigma)}\)。

## 6. 盒外目标表示的近邻终端

原近邻终端并不需要两个表示分别位于 \(K\) 盒内。设 \(z,w\) 是同一有限素数支撑上的
两个不同目标表示：

\[
\phi(z)=\phi(w)=-1.
\tag{22}
\]

只要满足

\[
\boxed{
z_\ell=w_\ell\quad(\nu_\ell=0),
\qquad
|z_\ell-w_\ell|\le\nu_\ell\quad(\nu_\ell>0),
}
\tag{23}
\]

就仍然产生偶终端。

### 证明

交换 \(z,w\) 后令

\[
\rho=\prod_\ell\ell^{z_\ell-w_\ell}<1,
\qquad
U=K\rho.
\tag{24}
\]

式 (23) 使 \(K\) 外的指数差全部为零，并使每个 \(K\) 内指数

\[
\nu_\ell+z_\ell-w_\ell
\]

落在 \([0,2\nu_\ell]\)。所以 \(U\) 是正整数且 \(U\mid K^2\)。由 (22)，
\(\rho\equiv1\pmod R\)，故 \(U\equiv K\pmod R\)，而定向给出 \(U<K\)。因此

\[
E=4U,
\qquad
n=\frac{4(K-U)}R
\tag{25}
\]

与原近邻定理完全相同地满足 \(E\mid4K^2\)、\(E\equiv1\pmod R\) 及
\(0<n<p\)，且 \(n\) 为偶数。证毕。

### 联合盒装箱推论

现在假设 \(z,w\) 取自有限联合盒 \(B_\mu\)。把第 \(\ell\) 个整数区间
\([-\mu_\ell,\mu_\ell]\) 连续分成长度至多 \(\nu_\ell+1\) 的小段。小段数为

\[
N_\ell=\left\lceil
\frac{2\mu_\ell+1}{\nu_\ell+1}
\right\rceil.
\tag{26}
\]

当 \(\nu_\ell=0\) 时，每段只有一个整数，所以同一盒自动强制外部坐标相等；当
\(\nu_\ell>0\) 时，同段两点距离至多 \(\nu_\ell\)。鸽巢原理给出

\[
\boxed{
|\phi^{-1}(-1)\cap B_\mu|
>
\prod_{\ell\in\mathcal P}
\left\lceil\frac{2\mu_\ell+1}{\nu_\ell+1}\right\rceil
\Longrightarrow
\text{存在偶终端}.}
\tag{27}
\]

取 \(\mu=\nu\) 时，每个正预算坐标贡献两个分箱，(27) 退化为原来的
\(2^{\omega(K)}\) 阈值。新式允许表示落在 \(K\) 盒外，只要它们仍受联合容量盒控制。

## 7. 支撑扩张不能制造单坐标强制高度

设有限交换群 \(H\) 中有生成元支撑 \(I\)，目标

\[
y\in\langle g_i:i\in I\rangle
\tag{28}
\]

已经可表示。给每个坐标预算 \(b_i\ge0\)，定义完整目标纤维和盒外向量

\[
\mathcal F_I(y)
=\left\{z\in\mathbb Z^I:
\prod_{i\in I}g_i^{z_i}=y\right\},
\qquad
e_b(z)_i=(|z_i|-b_i)_+.
\tag{29}
\]

令 \(\mathcal D_I\) 为全部 \(e_b(z)\) 的 Pareto 极小集。单坐标强制高度为

\[
\boxed{
h_{I,i}^{\rm forced}
=\min_{e\in\mathcal D_I}e_i
=\min_{z\in\mathcal F_I(y)}(|z_i|-b_i)_+.
}
\tag{30}
\]

最后一个等号成立，因为对任意纤维点，都可在其下方选择一个 Pareto 极小向量；反向
不等式显然。

现在扩张到 \(J\supset I\)，允许任意新生成元，旧预算放宽为
\(b_i'\ge b_i\)，新预算只要求 \(b_j'\ge0\)。把旧表示嵌入为

\[
\iota:\mathcal F_I(y)\longrightarrow\mathcal F_J(y),
\qquad
z\longmapsto(z,0).
\tag{31}
\]

于是旧坐标 overflow 不增，而每个新坐标恰为零。得到一般单调性

\[
\boxed{
h_{J,i}^{\rm forced}\le h_{I,i}^{\rm forced}
\quad(i\in I),
\qquad
h_{J,j}^{\rm forced}=0
\quad(j\in J\setminus I).
}
\tag{32}
\]

这条结论的前提 \(\mathcal F_I(y)\ne\varnothing\) 不可删除。G 状态若只有加入新支撑后
才首次表示目标，(31) 不存在；若扩张后仍不可达，则应保留无穷支撑障碍，而不是赋
forced height。

### 7.1 p=2017 的完整纤维与路径静态严格不同

对

\[
(p,R,K,x_R)=(2017,207,2^2\cdot5\cdot17\cdot307,2^2\cdot139),
\tag{33}
\]

加入 sink 二循环标签 \(41,101\)，取支撑

\[
\mathcal P=\{2,5,17,307,139,41,101\}
\tag{34}
\]

和联合预算

\[
\mu=(2,1,1,1,1,0,0).
\tag{35}
\]

对每个坐标 \(q\in\mathcal P\)，都有一个模 \(207\) 的目标表示令 \(z_q=0\)：

\[
\begin{array}{c|c}
\text{避开的坐标}&\text{模 }207\text{ 的 }-1\text{ 表示}\\ \hline
2&5^{-1}307^2\cdot139\\
5&2^{-2}17^{-1}\cdot139\\
17,307,139,101&2^{-1}\cdot5\cdot41\\
41&2^{-1}\cdot5\cdot101^{-1}.
\end{array}
\tag{36}
\]

逐项有 \(307\equiv100\)、\(101^{-1}\equiv41\)，并可直接核对四行都等于
\(-1\pmod {207}\)。所以

\[
\boxed{h_q^{\rm forced}=0\qquad(q\in\mathcal P).}
\tag{37}
\]

再加入瞬态标签 \(103\) 时，(32) 还给 \(h_{103}^{\rm forced}=0\)，旧坐标仍为零。
这与来源路径语言中的 \(\texttt{MISS\_STATIC}(103)\) 不矛盾：路径字只量化完整目标
纤维的一个受限子集

\[
\mathcal Z_{\rm path}\subsetneq\mathcal F_{\mathcal P}(-1),
\tag{38}
\]

所以受限最小值可以严格大于完整纤维最小值。不能把 path-static \(103\) 直接当成完整
纤维的选择不变单 \(q\) 需求。

### 7.2 单坐标全零仍可有正的多坐标价格

取

\[
(p,R,K)=(214729,43,151\cdot15287).
\tag{39}
\]

两个生成元都同余 \(22\pmod {43}\)，其阶为 \(14\)，目标条件为

\[
z_1+z_2\equiv7\pmod {14},
\qquad
(b_1,b_2)=(1,1).
\tag{40}
\]

完整无符号 Pareto 集恰为

\[
\boxed{
\mathcal D
=\{(k,5-k):0\le k\le5\}.
}
\tag{41}
\]

因此两个单坐标 forced height 都为零，但对任意 \(w_1,w_2>0\)，

\[
\min_{e\in\mathcal D}w\cdot e
=5\min(w_1,w_2)>0.
\tag{42}
\]

正确的跨状态容量对象因而是完整多坐标 Pareto 价格。进一步按高度层定义

\[
a_{q,k}(e)=\mathbf1_{e_q\ge k}
\tag{43}
\]

后，可使用层依赖价格 \(\lambda_{q,k}\ge0\)；若存在已证明的实际载体容量
\(C_{q,k}\)，有限 LP 分离给出充分矛盾证书

\[
\sum_s\min_{e\in\mathcal D_s}
\sum_{q,k\le e_q}\lambda_{q,k}
>
\sum_{q,k}\lambda_{q,k}C_{q,k}.
\tag{44}
\]

式 (44) 的难点不是有限优化，而是把每一层 overflow 注入固定颜色、有限区间且重复度
受控的实际算术载体。没有这条映射时，LP 仍只是条件接口。

## 8. 边界与下一步

本字典完成了四项此前分离的局部工作：

1. 固定支撑上的规范 Fourier/Pareto 溢出与 \(K/x_R\) 联合容量逐坐标相同；
2. 每个带表示见证的正需求有实际整数侧 \(P\) 或 \(Q\) 的符号载体；
3. 联合盒中足够丰富的目标纤维仍由近邻机制直接终端；
4. 完整纤维的单坐标 forced height 在支撑扩张下只能下降，新坐标恒为零。

它仍没有提供跨状态全称容量矛盾。为此还必须证明：规范载体落在共同有限区间，且不同
状态的标签互异或重复度有统一上界。对一个素数 \(q\)，只有在固定支撑上证明强制高度

\[
h_q^{\rm forced}
=\min_{e\in\operatorname{Pareto}}e_q
\]

为正时，才得到选择不变的单 \(q\) 收费。式 (32)--(37) 进一步说明，单纯加入
sink-SCC 标签不可能制造这种收费。若该最小值为零，就不能用任意选定路径上的正过载
替代它；多坐标需求必须保留同一个全局价格向量、层化价格或完整 Pareto 集。

对 large-slab 因子层还要注意

\[
N_{\alpha,e}=\alpha p q^e+1\equiv1\pmod q.
\]

因此 slab 外素数 \(q\) 不可能由 \(N_{\alpha,e}\) 的尾因子本身支付；把 (16) 映入
跨层因子对容量时，只能把 \(\ell\ne q\) 的载体送入该尾坐标。纯 \(q\) 过载必须由
路径 ancestry、另一路径或另一表示中的 \(x_R\)-cover、carrier-swap 或合法换图表分支
处理；当前已经纯 \(q\) 过载的表示自身不可能再被 \(x_R\) 覆盖。
