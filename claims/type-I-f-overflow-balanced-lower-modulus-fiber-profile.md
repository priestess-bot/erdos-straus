---
kind: claim
claim_id: type-I-f-overflow-balanced-lower-modulus-fiber-profile
title: 端点下降的更小模数 F/G 盒分流
statement: 对来自原 F 型见证的 R 因子修复候选严格端点下降，令 t=R/m、H_t=<q mod t:q|K>，并令 C_t 为原 K 指数盒在模 t 的像。原见证关系沿 (Z/RZ)^×→(Z/tZ)^× 约化，所以 -1 必恒在 H_t；低模数 G 分支结构性不可能。因而实际只有两分：-1 在 C_t 时是有限盒命中；-1 在 H_t\C_t 时是有限盒外的 F 型关系障碍。冻结的 48 个严格端点下降中得到 6、42 个；33 个模数虽有 2^j=-1 (mod t)，但二进预算可行数为 0。这只是 t\equiv1 (mod 4) 的对偶接口，不能直接视为原素数 p 的合法 Type I gap 证书。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-f-overflow-balanced-endpoint-descent
topics:
- type-I
- F-state
- G-state
- relation-lattice
- finite-box
- quotient
- descent
- support-escape
- proof-program
sources:
- claim: type-I-f-overflow-balanced-endpoint-descent
  role: smaller-modulus-input
visibility: public
last_checked: '2026-07-30'
---

# 端点下降的更小模数 F/G 盒分流

## 设置

沿用 \(R\)-因子修复分支。对一个严格端点下降，设

\[
R=mt,\qquad A=mu-1,\qquad B=mv+1,\qquad
\bar u=\frac{u}{g},\quad \bar v=\frac{v}{g},\quad g=(u,v),
\]

其中 \(t>1\)、\((v,t)=1\)，并且

\[
\frac{\bar u}{\bar v}\equiv-1\pmod t.
\tag{1}
\]

由于 \(R\equiv m\equiv3\pmod4\)，必有 \(t\equiv1\pmod4\)。又原状态满足
\((K,R)=1\)，所以 \(K\) 的所有素因子都是模 \(t\) 的单位。

写

\[
K=\prod_{i=1}^r q_i^{\nu_i},\qquad
H_t=\langle q_1,\ldots,q_r\rangle\le(\mathbb Z/t\mathbb Z)^\times,
\]

并定义原有限指数盒的目标纤维

\[
\mathcal C_t=\left\{\prod_i q_i^{z_i}\bmod t:
                 -\nu_i\le z_i\le\nu_i\right\}.
\tag{2}
\]

这里 \(\mathcal C_t\) 是带重数的指数向量像；同一个残数可以由多个盒内向量表示。

## 支撑约化与精确二分

若原端点来自 F 型见证 \(z=(z_i)\)，则
\[
\prod_iq_i^{z_i}\equiv-1\pmod R.
\]
因为 \(t\mid R\)，约化同态立即给出
\[
\prod_iq_i^{z_i}\equiv-1\pmod t,
\]
从而 \(-1\in H_t\)。这条约化与端点是否保持 \(K\)-支撑无关，只依赖于原 F
见证仍由 \(K\) 的素因子组成；因此任何这种严格端点下降都不能产生低模数 G 分离。

一般地，若暂时不假设输入来自 F 见证，目标残数 \(-1\) 相对于 \(H_t\) 与
\(\mathcal C_t\) 有三种互斥情形：

\[
\boxed{
\begin{array}{ll}
\text{quotient-G:}&-1\notin H_t,\\
\text{quotient-F-hit:}&-1\in\mathcal C_t,\\
\text{quotient-F-miss:}&-1\in H_t\setminus\mathcal C_t.
\end{array}}
\tag{3}
\]

第一种情形是支撑分离：有限阿贝尔群对偶性给出一个角色
\(\chi:(\mathbb Z/t\mathbb Z)^\times\to\mathbb C^\times\)，在 \(H_t\) 上恒等而
\(\chi(-1)\ne1\)。第二种情形给出一个满足原 \(K\)-指数预算的更小模数目标向量。第三种
情形说明目标仍在 \(K\)-支撑生成子群内，但所有原预算内表示都失败，因而是关系格/Fourier
意义上的有限盒外障碍。

端点式 (1) 只说明 \(-1\) 在加入 \(\bar u,\bar v\) 的扩展支撑中出现；对于本卡的
原 F 输入，上一段的约化论证进一步强制 \(-1\in H_t\)。因此实际审计只需区分
F-box hit 与 F-box miss，而不把外部素因子误记为低模数 G 型命中。

## 与算术提升的边界

因为 \(t\equiv1\pmod4\)，\(t\) 不是原 Type I 缺口的合法 \(3\pmod4\) 模数。故三分
中的 quotient-F-hit 仍需一个额外的奇偶/终端提升，quotient-F-miss 仍需把关系格
证书接到广义 \(2^j\) 终端、普通 Type II 或跨状态容量；quotient-G 只是一张更小模数
的对偶分离证书。三分本身不证明 \(p\) 已有 Type I/II 短证书，也不构成严格可提升
递降。

## 冻结审计

复现脚本同时计算 \(H_t\) 的生成闭包和盒 (2) 的精确重数。结果文件：

~~~text
reproductions/type-i-f-overflow-r-modulus-repair-results.json
~~~

最新结果 SHA-256：

~~~text
c656c91ebb02a33e8d1f5c78db70ce14ac5fbc2decc0db99e05bcbcc1fbee22f
~~~

严格端点下降的 48 个候选给出：

~~~text
strict_balanced_reduction_count: 48
lower_modulus_f_box_hit_count: 6
lower_modulus_f_box_miss_count: 42
lower_modulus_g_count: 0 (structurally excluded)
lower_modulus_order_two_target_count: 33
lower_modulus_dyadic_budget_admissible_count: 0
forward: 4 / 20 / 0
reverse: 2 / 22 / 0
~~~

在这 48 个样本中 \(K\) 全部为奇数，所以二进终端接口的预算
\(v_2(2K)=1\)。33 个更小模数满足某个最小 \(j>0\) 使
\(2^j\equiv-1\pmod t\)，但最小 \(j\ge2\)，没有一个满足预算；
其余 15 个模数没有这样的二进幂。因而盒内命中并没有被误记为已经完成的
广义 \(2^j\) 终端。

六个盒命中样本的 \((p,R,m,t)\) 为

~~~text
(57399241,155,31,5)
(99151369,3395,35,97)
(242042089,771,3,257)
(366108649,1379,7,197)
(475619929,5915,7,845)
(510725329,555,15,37)
~~~

每个命中都还需检查 \(t\) 上的奇偶终端或把该关系提升回合法 \(3\bmod4\) 缺口；42 个
盒外样本已经进一步重建为规范关系格证书，见[端点下降 F-box miss 的更小模数关系格证书](type-I-f-overflow-lower-modulus-relation-lattice.md)；
这仍不是“没有目标”的证明。

## 复现

~~~bash
python3 reproductions/type_i_f_overflow_r_modulus_repair.py
~~~
