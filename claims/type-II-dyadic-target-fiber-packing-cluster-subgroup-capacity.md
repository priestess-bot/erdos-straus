---
kind: claim
claim_id: type-II-dyadic-target-fiber-packing-cluster-subgroup-capacity
title: Type II 二进顶位装箱簇生成关系子群与容量候选
statement: 对最大二进深度目标类的去重源表示按 2^r 个符号盒分组。若最大符号簇含 m 个不同源像，则以簇内一个基点作差得到 m-1 个预算内、进入 L_d=2^{d+1}K 的非零关系；这些关系在循环 K=C_{2^a} 中生成阶至少 m 的子群，因而至少携带 ceil(log_2 m) 个二进层的关系容量候选。只有通过 source-closure、稳定子投影和 E1–E5 后，该候选才可转换为 Kneser/q 价格；否则只登记关系子群负载，不得重复收费。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-dyadic-target-fiber-top-class-packing-short-relation
  - type-II-dyadic-target-fiber-maximal-quotient-dedup
  - type-II-q-layer-prefix-kneser-price-certificate
  - type-II-cross-state-layered-rado-qcapacity-cut
  - type-II-stabilizer-kernel-source-box-lattice-criterion
topics:
  - type-II
  - dyadic
  - target-fiber
  - packing
  - relation-subgroup
  - q-adic-capacity
  - Kneser
  - source-closure
  - E1-E5
  - proof-program
sources:
  - claim: type-II-dyadic-target-fiber-top-class-packing-short-relation
    role: sign-cell-pair-and-budgeted-relation
  - claim: type-II-dyadic-target-fiber-maximal-quotient-dedup
    role: distinct-top-source-images
  - claim: type-II-q-layer-prefix-kneser-price-certificate
    role: relation-block-to-price-interface
  - claim: type-II-cross-state-layered-rado-qcapacity-cut
    role: cross-state-q-layer-capacity-gate
  - claim: type-II-stabilizer-kernel-source-box-lattice-criterion
    role: source-closure-and-stabilizer-gate
  - reproduction: reproductions/dyadic_target_fiber_max_depth.py
    role: cluster-subgroup-control
visibility: public
last_checked: '2026-08-09'
---

# Type II 二进顶位装箱簇生成关系子群与容量候选

## 设置

沿用二进目标纤维的加法记号。令 \(H\) 为有限阿贝尔群，令
\(K=\langle\kappa\rangle\simeq C_{2^a}\) 为核，令 \(\phi:\mathbb Z^r\to H\) 为源
指数同态，并令

\[
\mathcal B_\nu=\prod_{i=1}^r[-\nu_i,\nu_i]\cap\mathbb Z^r.
\]

固定二阶目标 \(t\) 和源像集 \(S=\phi(\mathcal B_\nu)\)，满足

\[
t\notin S,\qquad
F_t=\{k\in K:t+k\in S\}\ne\varnothing,\qquad
0\notin F_t.
\]

令

\[
d=\max_{k\in F_t}\operatorname{dep}_2(k),
\qquad
L_d=2^{d+1}K,
\qquad
F_t^{(d)}=\{k\in F_t:\operatorname{dep}_2(k)=d\}.
\]

定义最大深度去重表示集 \(\mathcal Z_d^{\mathrm{red}}\)：每个不同的源像
\(\phi(z)=t+k\), \(k\in F_t^{(d)}\)，只保留一个 \(z\in\mathcal B_\nu\)。

## 装箱簇定理

把每个坐标区间分为

\[
I_i^-=[-\nu_i,0],
\qquad
I_i^+=[1,\nu_i].
\]

设 \(C_\epsilon\) 是由这些区间产生的符号簇，最多有 \(2^r\) 个；令

\[
m=\max_\epsilon |C_\epsilon\cap\mathcal Z_d^{\mathrm{red}}|,
\qquad
m\ge
\left\lceil\frac{|\mathcal Z_d^{\mathrm{red}}|}{2^r}\right\rceil.
\]

若 \(m\ge2\)，取最大簇中的规范基点 \(z_0\)，并列出其余代表
\(z_1,\ldots,z_{m-1}\)。定义

\[
\Delta_j=z_j-z_0,
\qquad
\rho_j=\phi(\Delta_j).
\]

则：

\[
\boxed{
|\Delta_{j,i}|\le\nu_i,\qquad
\rho_j\in L_d\setminus\{0\},
\qquad
\rho_i\ne\rho_j\ (i\ne j).
}
\tag{1}
\]

令

\[
R_C=\langle\rho_1,\ldots,\rho_{m-1}\rangle\le L_d.
\]

则

\[
\boxed{|R_C|\ge m.}
\tag{2}
\]

在循环核 \(K=C_{2^a}\) 中，\(R_C\) 也是循环子群。若
\(|R_C|=2^\beta\)，则

\[
\boxed{
\beta\ge\lceil\log_2m\rceil,
\qquad
R_C=2^bK,\quad
b=a-\beta\ge d+1.
}
\tag{3}
\]

因此一个符号簇产生的不是单个孤立碰撞，而是一个带 \(m-1\) 个预算内生成向量、
至少 \(\lceil\log_2m\rceil\) 个二进层的关系子群候选。\(m=1\) 时输出
\(\mathrm{TOP\_CLASS\_CLUSTER\_BOUNDARY}\)，本引理不强制非零关系。

## 证明

同一符号簇中任意两个指数在每个坐标的同一半区间内，因此
\(|z_{j,i}-z_{0,i}|\le\nu_i\)。二者都属于最大深度层，所以

\[
\phi(z_j)=t+k_j,\qquad
\phi(z_0)=t+k_0,
\qquad
k_j,k_0\in F_t^{(d)}.
\]

最大深度去重引理给出

\[
\rho_j=k_j-k_0\in2^{d+1}K=L_d.
\]

保留的是不同源像，故 \(\rho_j\ne0\)；若
\(\rho_i=\rho_j\)，则 \(k_i-k_0=k_j-k_0\)，从而
\(k_i=k_j\)，与源像不同矛盾。这证明 (1)。

子群 \(R_C\) 含有单位元 \(0\) 和 \(m-1\) 个互不相同的
\(\rho_j\)，故 \(|R_C|\ge m\)，得到 (2)。由于 \(K\) 是二幂循环群，其所有子群
均为 \(2^bK\)。写 \(|R_C|=2^\beta\) 即得
\(b=a-\beta\)。又 \(R_C\le L_d=2^{d+1}K\)，所以 \(b\ge d+1\)；由
\(2^\beta\ge m\) 得 \(\beta\ge\lceil\log_2m\rceil\)。证毕。

## 关系子群到容量的受控接线

\(R_C\) 的阶下界本身是有限群事实，不等于整数 Type II 证书，也不等于可以把
\(|R_C|-1\) 直接加入 Hall/q 容量。要收费，必须通过一个关系闭合门：

1. **SOURCE_CLOSURE**：源关系格和参数纤维能实现一组保持来源标签的块，使
   \(R_C\) 的相应平移真实出现在当前乘积集；
2. **STABILIZER_PROJECTION**：在当前稳定子 \(T\) 下使用
   \(R_CT/T\)，先删除 \(R_C\cap T\) 已吸收的部分；
3. **Q/PRIMARY_COMPATIBILITY**：若映射到 q 或 \(\ell\)-primary 槽，必须通过分层
   Rado/Hall、shared-q 和 source-column 独立性；
4. **E1--E5**：来源记录、统一 CRT、范围、正规形和严格势下降全部通过。

若这些门通过，关系子群可作为一个真实 Kneser 价格候选

\[
\boxed{
\operatorname{price}_T(R_C)
=
|R_CT/T|-1.
}
\tag{4}
\]

若 \(T\cap R_C=\{0\}\)，则

\[
\operatorname{price}_T(R_C)=|R_C|-1\ge m-1.
\tag{5}
\]

若 \(R_C\le T\)，价格为零，但
\(\mathrm{DYADIC\_RELATION\_SUBGROUP\_ABSORBED}\) 记录了它已被
稳定子吸收；不能再次收费。若 SOURCE_CLOSURE、SNF 或 E1--E5 任一门失败，输出
\(\mathrm{DYADIC\_RELATION\_SUBGROUP\_LIFT\_OBSTRUCTED}\)，保留 \(R_C\)、关系生成元
及最小失败门，不把 (4) 当成已完成的整数容量。

## q 进与跨状态接口

对每个状态和最大深度层先构造 \(R_C\)。若 closure gate 进一步给出一个保持来源
标签的层 token 映射，把 \(R_C\) 的 \(\beta=\log_2|R_C|\) 个二进层候选送入某个
q/primary 请求子集 \(U\)，并令 \(n_C\) 是实际通过所有标签门后支付的独立 token 数，
则

\[
n_C\le
\min\!\left(
\beta,
\mathsf C_q(U),
\operatorname{rank}_{V_\ell}(U)
\right).
\]

这里的 \(\mathsf C_q(U)\) 是分层 q 容量上界，
\(\operatorname{rank}_{V_\ell}(U)\) 是真实源列秩；二者是支付 token 的必要上界，
而不是把 \(R_C\) 自动转换为 q 槽的存在性结论。没有这个带标签的映射时，只能
保留 \(R_C\) 和 \(\beta\) 作为关系候选，不能绕过 q 进层占用、源列秩或物理 owner
流门。
若多个状态的 \(R_C\) 投影到同一个 q 方向，先按商方向去重，再调用
\(\texttt{type-II-cross-state-layered-rado-qcapacity-cut}\)；跨状态相加只在来源标签分派和
纤维不交已经证明时进行。

如果 \(\operatorname{price}_T(R_C)\) 通过，关系子群给出一个 Kneser 价格；若不
通过，则仍保留 \(R_C\) 作为一个结构性缺口，交给前一层的 Fourier/SNF 或严格
下降分派。这个顺序避免把“关系存在”误写成“容量可支付”。

## 控制实例

取

\[
H=C_2\times C_{16},
\quad
g_1=(1,1),\quad g_2=(0,2),
\quad
\mathcal B=[-2,2]^2,
\quad
t=(1,0).
\]

最大深度为 \(d=0\)，顶位去重源像数为 6。符号簇中最大的一个含 3 个代表，例如

\[
z_0=(-1,-2),\qquad
z_1=(-1,-1),\qquad
z_2=(-1,0).
\]

因此

\[
\Delta_1=(0,1),\quad
\Delta_2=(0,2),
\qquad
\rho_1=(0,2),\quad
\rho_2=(0,4).
\]

它们生成

\[
R_C=\langle(0,2)\rangle=2K,
\qquad
|R_C|=8,
\qquad
\beta=3\ge\lceil\log_2 3\rceil=2.
\]

复现器还验证了严格商、单条短关系、顶层终端和 \(t\in K\) 固定点控制。

## 边界

该引理把“顶位表示过密”推进为“关系子群阶下界”，但不声称每个核心素数都存在
\(m\ge2\) 的最大簇，也不自动证明 SOURCE_CLOSURE 或 E1–E5。关系子群可能已被稳定子
吸收，或只能在抽象有限群中构造；这些情况必须分别记录为吸收或提升障碍，不能冒充
Type II 短证书或全局递降。

## 复现

~~~bash
python3 -m py_compile reproductions/dyadic_target_fiber_max_depth.py
python3 reproductions/dyadic_target_fiber_max_depth.py --verify
~~~

复现器的 \(\mathrm{cluster}\) 回执包括最大符号簇、全部预算内关系、生成子群阶、二进深度和
\(\lceil\log_2m\rceil\) 下界；\(\mathrm{packing\_pair}\) 则保留与上一引理兼容的单对回执。
