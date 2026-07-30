---
kind: claim
claim_id: type-I-f-g-fourier-obstruction-certificate
title: F/G 状态的规范有限傅里叶障碍证书
statement: 在有限阿贝尔单位群中，G 型状态由商群分离角色给出；对目标位于生成子群但指数盒未命中的 F 型状态，目标缺失强制一个非平凡角色的有限傅里叶乘积至少达到平凡项的 1/(|H|-1)。这一结论对任意固定层 J 成立；归一化固定层因子不超过 1，因此规范角色还满足显式加权相位预算 sum_i min(1,nu_i^2 ||theta_i||^2) <= 60 log(|H|-1)。因此每个 G/F 状态都有可枚举的规范对偶证书，但该证书本身不等于跨状态容量矛盾。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- finite-fourier
- F-state
- G-state
- finite-abelian-groups
- target-fiber
- dual-certificate
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-target-context
visibility: public
last_checked: '2026-07-30'
---

# F/G 状态的规范有限傅里叶障碍证书

## 设置

令 $G=(\mathbb Z/R\mathbb Z)^\times$，令 $H\le G$ 为 $K$ 的素因子剩余类生成的有限阿贝尔子群。
取固定层 $J\subseteq H$、元素 $q_1,\ldots,q_r\in H$ 和预算
$\nu_i\ge0$。写

\[
D_{\nu}(u)=\sum_{z=-\nu}^{\nu}u^z,
\qquad
B_{\nu}=\prod_{i=1}^{r}(2\nu_i+1).
\]

对 $t\in H$，定义带固定层的表示数

\[
N_J(t)=\#\left\{(j,z):j\in J,\ -\nu_i\le z_i\le\nu_i,
\ j\prod_iq_i^{z_i}=t\right\}.
\]

当 $J=\{1\}$ 时，$N_J(-1)$ 正好是目标指数纤维
$\mathcal Z^-_{R,K}$ 的大小。

## F 型：目标缺失的非平凡谱证书

设 $t\in H$ 且 $N_J(t)=0$，并假设 $|H|>1$。对每个角色
$\chi\in\widehat H$ 定义

\[
A_J(\chi)=\left(\sum_{j\in J}\chi(j)\right)
\prod_{i=1}^{r}D_{\nu_i}(\chi(q_i)).
\]

有限群角色正交性给出精确公式

\[
\boxed{
N_J(t)=\frac1{|H|}\sum_{\chi\in\widehat H}
\overline{\chi(t)}A_J(\chi).}
\]

平凡角色的项为
$A_J(1)=|J|B_{\nu}$。由于左端为零，非平凡项满足

\[
\sum_{\chi\ne1}\overline{\chi(t)}A_J(\chi)=-|J|B_{\nu}.
\]

因此存在非平凡角色 \(\chi\ne1\) 使

\[
\boxed{
|A_J(\chi)|\ge\frac{|J|B_{\nu}}{|H|-1}.}
\]

特别地，在纯指数盒情形 $J=\{1\}$ 中，F 型目标缺失必产生
\[
\max_{\chi\ne1}\left|\prod_iD_{\nu_i}(\chi(q_i))\right|
\ge\frac{B_{\nu}}{|H|-1}.
\]

在固定的有限阿贝尔群表示下，可把所有满足该下界的角色按角色阶、再按
$|A_J(\chi)|$ 的降序作有限字典序选择，得到一个规范的 F 型 Fourier 证书。

## 规范编码与可验证载荷

固定素因子顺序 \(q_1<\cdots<q_r\)，令
\[
\phi:\mathbb Z^r\longrightarrow H,\qquad
\phi(z)=\prod_iq_i^{z_i},
\qquad
\Lambda=\ker\phi.
\]
取 \(\Lambda\) 的任意整数基矩阵 \(L\)。角色可以表示为一个
\(\theta\in(\mathbb Q/\mathbb Z)^r\)，满足
\[
L\theta\in\mathbb Z^r,\qquad
\chi_\theta(\phi(z))=e^{2\pi i\langle\theta,z\rangle}.
\]
用 Smith 正规形枚举这些有限阶相位。若 \(m=\operatorname{ord}(\chi_\theta)\)，
取分子向量
\[
a=(a_1,\ldots,a_r)\in\{0,\ldots,m-1\}^r,
\qquad
\theta_i=\frac{a_i}{m}\pmod1.
\]

于是一个 F 型证书可规范编码为
\[
\mathsf{FC}=
\bigl(m,\,-|A_J(\chi_\theta)|,\ a_1,\ldots,a_r\bigr),
\]
并按字典序最小化该元组（角色阶升序，谱幅度降序，随后相位分子升序）。
验证器只需检查：

1. \(L a\equiv0\pmod m\)，保证角色在 \(H\) 上良定义；
2. \(m/\gcd(m,a_1,\ldots,a_r)=m\)，保证记录的确是角色阶；
3. 用有限根单位的精确运算重建 \(A_J(\chi_\theta)\)，并检查
   \[
   |A_J(\chi_\theta)|\ge\frac{|J|B_\nu}{|H|-1};
   \]
4. 若需要近角色预算，检查
   \[
   \prod_i f_{\nu_i}(a_i/m)\ge\frac1{|H|-1}.
   \]

因此证书不依赖复数近似或角色枚举顺序；其有限阶分解
\(m=\prod_{\ell\mid m}\ell^{v_\ell(m)}\) 也可直接作为后续
\(q\)-进容量映射的输入。该编码仍只是状态内对偶证书；它没有自动保证不同状态选出的
角色共享同一素数阶分量。

## 任意固定层的近角色预算

下面的定量结论对任意非空固定层 \(J\subseteq H\) 成立。对每个坐标写

\[
\chi(q_i)=e^{2\pi i\theta_i},
\qquad
\delta_i=\|\theta_i\|_{\mathbb R/\mathbb Z}\in[0,1/2].
\]

令

\[
f_\nu(\theta)
=
\frac{|D_\nu(e^{2\pi i\theta})|}{2\nu+1}.
\]

则对所有 \(\nu\ge1\) 有一个统一的初等上界

\[
\boxed{
f_\nu(\theta)
\le
\exp\!\left(
-\frac1{60}
\min\{1,\nu^2\|\theta\|_{\mathbb R/\mathbb Z}^2\}
\right).
}
\tag{*}
\]

令归一化固定层因子
\[
g_J(\chi)=\frac{\left|\sum_{j\in J}\chi(j)\right|}{|J|}
\in[0,1].
\]
若上面选出的 F 型角色满足表示数缺失给出的下界，则
\[
g_J(\chi)\prod_i f_{\nu_i}(\theta_i)\ge\frac1{|H|-1}.
\]
这里 \(g_J(\chi)=0\) 不可能发生；否则该角色的 Fourier 项为零，不能满足前述下界。
由于 \(g_J(\chi)\le1\)，必有
\[
\prod_i f_{\nu_i}(\theta_i)
\ge\frac1{(|H|-1)g_J(\chi)}
\ge\frac1{|H|-1}.
\]
因此 F 型证书满足

\[
\prod_i f_{\nu_i}(\theta_i)\ge\frac1{|H|-1},
\]

则必有

\[
\boxed{
\sum_i\min\{1,\nu_i^2\delta_i^2\}
\le60\log(|H|-1).
}
\tag{**}
\]

这把“F 型目标缺失”转成了一个显式的近角色证书：大预算坐标中绝大多数
\(\chi(q_i)\) 必须靠近 1，除非其预算很小。它还没有说明这些近角色的幂必然
整除同一个标签差；那个算术拉回仍是跨状态桥的未解部分。固定层因子仍保留在规范
角色的选择和证书中，只是它的模长上界 \(g_J\le1\) 足以把相位预算推广到任意固定层。

### 有限阶分母推论

对规范角色令
\[
d_i=\operatorname{ord}\bigl(\chi(q_i)\bigr).
\]
若 \(\chi(q_i)\ne1\)，则其非零相位满足
\[
\delta_i=\left\|\theta_i\right\|_{\mathbb R/\mathbb Z}\ge\frac1{d_i}.
\]
因此相位预算进一步给出
\[
\boxed{
\sum_{\chi(q_i)\ne1}
\min\left\{1,\left(\frac{\nu_i}{d_i}\right)^2\right\}
\le60\log(|H|-1).
}
\tag{***}
\]
特别地，对任意 \(0<\eta\le1\)，低阶活跃坐标数满足
\[
\#\left\{i:\chi(q_i)\ne1,\ d_i\le\frac{\nu_i}{\eta}\right\}
\le\frac{60\log(|H|-1)}{\eta^2}.
\]
所以每个 F 型证书可分成两个可验证分支：少量低阶活跃素因子，或多数活跃坐标具有
\(d_i>\nu_i/\eta\) 的高阶相位。前一分支适合与有限阶商和 \(q\)-进容量结合，后一分支
则要求关系格或随机游走侧给出额外的短关系；这一步仍不是跨状态选择器定理。

### Fourier—关系格同一性

令关系格的对偶为
\[
\Lambda^*=\{y\in\mathbb R^r:\langle y,\lambda\rangle\in\mathbb Z
\text{ 对所有 }\lambda\in\Lambda\}.
\]
规范角色的相位向量 \(\theta\) 属于 \(\Lambda^*/\mathbb Z^r\)。取其逐坐标中心化代表
\[
y_i\in[-1/2,1/2],\qquad y_i\equiv\theta_i\pmod1.
\]
由于 \(\mathbb Z^r\subseteq\Lambda^*\)，有 \(y\in\Lambda^*\)；F 型角色非平凡则
\(y\ne0\)。因此每个 F 型状态都给出一个非零对偶格证书
\[
\boxed{
\operatorname{wd}_\nu(y)
=\sum_i\min\{1,\nu_i^2y_i^2\}
\le60\log(|H|-1).
}
\tag{****}
\]
该证书可由关系基矩阵 \(L\) 验证：检查 \(Ly\in\mathbb Z^r\)、中心化范围、
\(y\ne0\) 以及 (****)。若
\(\nu_i|y_i|\le1\) 对所有坐标成立，则 (****) 退化为标准加权二次短向量界
\(\sum_i\nu_i^2y_i^2\le60\log(|H|-1)\)；否则“宽坐标”集合
\(\{i:\nu_i|y_i|>1\}\) 的大小仍至多为 \(60\log(|H|-1)\)。

所以规范 Fourier 证书和规范关系格证书是同一个有限对象的两个投影。对 F 型或
\(H\) 内部非平凡角色，活跃坐标一旦选定即可从线性块分解提取逐状态的高载体高度；
尚未解决的是把该支撑/分母转成跨状态可重复的素数—颜色分组和联合容量需求。
外部 G 型分离角色在 \(H\) 上恒等，继续由支撑外分离证书处理。
固定层归一化因子 \(g_J(\chi)\) 还会把相位预算右端收紧为
\(60\log((|H|-1)g_J(\chi))\)，详见
[F 型固定层的 Fourier 谱余量约束](type-I-f-g-fixed-layer-spectral-slack.md)。

### 对偶宽度的盒分离充分条件

设 \(z_0\in\mathbb Z^r\) 满足 \(\phi(z_0)=t\)，并令
\[
\alpha_y=\operatorname{dist}\bigl(\langle y,z_0\rangle,\mathbb Z\bigr)
\in[0,1/2].
\]
若某个 \(0\ne y\in\Lambda^*\) 满足
\[
\boxed{
W_\nu(y)=\sum_i\nu_i|y_i|<\alpha_y,
}
\tag{*****}
\]
则
\[
(z_0+\Lambda)\cap B_\nu=\varnothing.
\]
事实上，任意 \(z\in B_\nu\) 都满足
\(|\langle y,z\rangle|\le W_\nu(y)<\alpha_y\)，而
\(\langle y,z\rangle\equiv\langle y,z_0\rangle\pmod1\) 对所有
\(z\in z_0+\Lambda\) 成立，二者不可能同时满足。于是 (*****) 是一个完全可验证的
F 型关系格分离证书。

该充分条件不声称覆盖所有 F 状态：截断宽度 (****) 可能很小，但未必满足未截断的
\(W_\nu(y)<\alpha_y\)。这正好划分出下一步的两类任务：小宽度分支直接得到格证书，
其余分支必须转入加法结构、有限阶商或跨状态容量。

### \((*)\) 的证明

置 \(m=2\nu+1\)、\(\delta=\|\theta\|\)。由几何级数和恒等式

\[
f_\nu(\theta)^2
=
1-\frac4{m^2}\sum_{d=1}^{m-1}(m-d)\sin^2(\pi d\delta).
\]

当 \(t=\nu\delta\le1/2\) 时，取 \(1\le d\le\nu\)，有
\(\pi d\delta\le\pi/2\) 且
\(\sin(\pi d\delta)\ge2d\delta\)。又 \(m\le3\nu\)，从而

\[
1-f_\nu(\theta)^2
\ge
\frac{16\delta^2}{m^2}
\sum_{d=1}^{\nu}(m-d)d^2
\ge\frac{16}{27}t^2.
\]

使用 \(\sqrt{1-x}\le e^{-x/2}\) 得
\(f_\nu(\theta)\le e^{-8t^2/27}\le e^{-\min(1,t^2)/60}\)。

当 \(t>1/2\) 时，几何级数的另一端给出

\[
f_\nu(\theta)
\le\frac1{m|\sin(\pi\delta)|}
\le\frac1{2m\delta}
\le\frac12
\le e^{-1/60}.
\]

两段合并得到 \((*)\)。对所有坐标相乘，再与
\(1/(|H|-1)\) 比较并取对数，即得 \((**)\)。

### 证明

对任意 $x,t\in H$，角色正交性为
\[
\mathbf 1_{x=t}=\frac1{|H|}\sum_{\chi\in\widehat H}\chi(x)\overline{\chi(t)}.
\]
将 $x=j\prod_iq_i^{z_i}$ 代入并对 $(j,z)$ 求和，得到精确公式。平凡角色给出
$|J|B_{\nu}$；对非平凡项应用三角不等式，若每一项都小于
$|J|B_{\nu}/(|H|-1)$，则其总和绝对值小于 $|J|B_{\nu}$，与上式矛盾。证毕。

## G 型：支撑外分离角色

若 $-1\notin H$，则有限商群 $G/H$ 的非单位元 $(-1)H$ 可由一个角色分离：存在
$\psi\in\widehat G$ 使

\[
\psi(h)=1\quad(h\in H),
\qquad
\psi(-1)\ne1.
\]

因此对所有指数向量 $z$，
$\psi(\prod_iq_i^{z_i})=1$，而目标 $-1$ 的值不为 $1$。这是一张精确的 G 型
支撑证书，不需要枚举有限指数盒。

## 逻辑边界

该卡把 G/F 障碍都变成有限、可枚举、可复核的对偶对象。F 型下界的规模可能只有
\(1/(|H|-1)\)，并不保证角色阶、导数或关系格长度足够小；因此它还不能单独推出
跨状态 $q$-进容量矛盾或算术下降。下一步必须把规范角色与素因子幂、模数差或标签碰撞
建立可计数的拉回映射。
