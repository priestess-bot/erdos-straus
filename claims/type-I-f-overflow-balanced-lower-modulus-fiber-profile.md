---
kind: claim
claim_id: type-I-f-overflow-balanced-lower-modulus-fiber-profile
title: 端点下降的更小模数 F/G 盒分流
statement: 对 R 因子修复候选的严格端点下降，令 t=R/m、H_t=<q mod t:q|K>，并令 C_t 为原 K 指数盒在模 t 的像。则 -1 相对于 H_t 与 C_t 有精确三分：-1 不在 H_t 时是更小模数的 G 型支撑分离；-1 在 C_t 时是有限盒命中；-1 在 H_t\C_t 时是有限盒外的 F 型关系障碍。冻结的 48 个严格端点下降中分别得到 0、6、42 个；33 个模数虽有 2^j=-1 (mod t)，但二进预算可行数为 0。这只是 t\equiv1 (mod 4) 的对偶接口，不能直接视为原素数 p 的合法 Type I gap 证书。
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

## 精确三分

对于目标残数 \(-1\)，有互斥且完备的三种情形：

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

端点式 (1) 只说明 \(-1\) 在加入 \(\bar u,\bar v\) 的扩展支撑中出现；它不强制 \(-1\)
属于 \(H_t\)。因此 (3) 正好把“双端点支撑逃逸”继续细分为 G 分离或 F 盒外，而不把
外部素因子误记为原 F 型命中。

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
f6da0544498862bceec95529cdef68f8202dc75042ee89b67d2d258be16ef809
~~~

严格端点下降的 48 个候选给出：

~~~text
strict_balanced_reduction_count: 48
lower_modulus_f_box_hit_count: 6
lower_modulus_f_box_miss_count: 42
lower_modulus_g_count: 0
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
盒外样本则是下一轮 Fourier/关系格容量输入，而非“没有目标”的证明。

## 复现

~~~bash
python3 reproductions/type_i_f_overflow_r_modulus_repair.py
~~~
