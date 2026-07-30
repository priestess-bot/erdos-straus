---
kind: claim
claim_id: type-I-linear-cross-label-independent-joint-capacity
title: 双标签独立颜色的联合 q 进除子容量
statement: 固定核心素数 p、两个线性标签 t_1,t_2、有限素数支持 Q 和模数窗口 I。对每个 q 允许 q 进高度独立选择两个块 t_1R+1、t_2R+1 中较高者，则联合高度乘积可由所有颜色分配的混合多除子对集合之和严格上界；该接口把独立颜色放宽容量转化为有限算术除子账本，但不说明关系格溢出必须支付这些层数。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-linear-multi-active-joint-divisor-capacity
sources:
- claim: type-I-linear-multi-active-joint-divisor-capacity
  role: same-block-joint-capacity-interface
topics:
- type-I
- linear-source
- multi-active
- q-adic
- capacity
- cross-state
- proof-program
visibility: public
last_checked: '2026-07-30'
---

# 双标签独立颜色的联合 q 进除子容量

## 设置

固定核心素数 (p)、两个标签 (t_1,t_2)、有限素数集合 (Q) 和窗口
(I=[R_{min},R_{max}]capmathbb Z)。假设所考虑的完整线性源状态满足

\[
B_j(R)=t_jR+1\mid p-t_j, j=1,2.
\]

写

\[
h_q^{(j)}(R)=v_q(B_j(R)).
\]

目标是控制允许每个 (q) 独立选择颜色的联合容量

\[
C_{\mathrm{ind}}(Q;I)=
\sum_{R\in I}
\prod_{q\in Q}\max\{h_q^{(1)}(R),h_q^{(2)}(R)\}.
\]

## 混合颜色层

给定颜色分配 (sigma:Q\to\{1,2\}) 和层向量
(\mathbf k=(k_q)_{q\in Q})，令

\[
Q_j(\sigma,\mathbf k)=
\prod_{q:\,\sigma(q)=j}q^{k_q},
, j=1,2,
\]

空乘积约定为 1。定义混合多除子对集合

\[
\mathcal D_{\sigma,\mathbf k}(p,t_1,t_2;I)
=
\left\{
(d_1,d_2):
\begin{array}{l}
d_j\mid (p-t_j)/Q_j(\sigma,\mathbf k),\\
Q_j(\sigma,\mathbf k)d_j\equiv1\pmod {t_j},\\
\displaystyle
\frac{Q_1d_1-1}{t_1}
=\frac{Q_2d_2-1}{t_2}\in I
\end{array}
\right\}.
\]

若 (Q_j\nmid(p-t_j))，对应集合为空。令

\[
N_{\sigma,\mathbf k}
=
\#\{R\in I:
h_q^{(\sigma(q))}(R)\ge k_q
\text{ 对所有 }q\in Q\}.
\]

对每个这样的 (R)，定义

\[
d_j=\frac{B_j(R)}{Q_j}.
\]

因为 (B_j(R)\mid p-t_j)，有 (d_j\mid(p-t_j)/Q_j)；因为
(B_j(R)\equiv1\pmod {t_j})，有 (Q_jd_j\equiv1pmod {t_j})；两个商都恢复同一个
(R)。因此映射 (R\mapsto(d_1,d_2)) 单射，得到严格层界

\[
N_{\sigma,\mathbf k}
\le
\left|\mathcal D_{\sigma,\mathbf k}(p,t_1,t_2;I)\right|.
\tag{1}
\]

层析恒等式给出

\[
\sum_{R\in I}\prod_{q\in Q}h_q^{(\sigma(q))}(R)
=
\sum_{k_q\ge1}N_{\sigma,\mathbf k}
\le
\sum_{k_q\ge1}
\left|\mathcal D_{\sigma,\mathbf k}(p,t_1,t_2;I)\right|.
\tag{2}
\]

## 独立颜色放宽容量

逐点使用

\[
\prod_{q\in Q}\max\{x_q,y_q\}
\le
\prod_{q\in Q}(x_q+y_q)
=
\sum_{\sigma:Q\to\{1,2\}}
\prod_{q\in Q}z_{q,\sigma(q)},
\]

其中 (z_{q,1}=x_q,z_{q,2}=y_q)。将 (2) 对全部 (2^{|Q|}) 个颜色分配求和，得到

\[
\boxed{
C_{\mathrm{ind}}(Q;I)
\le
\sum_{\sigma:Q\to\{1,2\}}
\sum_{k_q\ge1}
\left|\mathcal D_{\sigma,\mathbf k}(p,t_1,t_2;I)\right|.
}
\tag{3}
\]

这是一条严格的、颜色选择不变的联合 q 进容量上界。它比要求所有方向落在同一块
的容量更宽松；因此右端若仍小于某个联合需求，才可能形成真正稳健的容量矛盾。

## 对当前普适缺口的接口

普适联合容量审计使用的

\[
\sum_{(a,R,s)}\prod_{q\in Q}
\max\{v_q(aR+1),v_q(sR+1)\}
\]

正是左端的有限状态版本。公式 (3) 说明它可以进一步改写为混合多除子对的有限账本，
从而不依赖“某个颜色分配恰好被选中”这一任意诊断规则。

该主张仍不解决最后一步：关系格盒外向量的支持和符号尚未证明必须支付
\(\prod_qe_q\) 个联合层。这个映射若能建立，(3) 才能与当前 142/142 个多坐标组的
压力边界合并为跨状态选择器；否则应从同一联合向量构造严格可提升下降。
