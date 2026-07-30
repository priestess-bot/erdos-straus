---
kind: claim
claim_id: type-I-f-overflow-balanced-endpoint-descent
title: 盒外见证的端点平衡小模数表示下降
statement: 对 R 因子修复候选 m|gcd(R,B-1)，写 R=mt、A=mu-1、B=mv+1。则 u+v=t m_0。若 t>1 且 gcd(v,t)=1，令 g=gcd(u,v)，则约分后的 u/g、v/g 互素且 (u/g)/(v/g)=-1 (mod t)。这给出严格更小模数 t 上的目标有理表示；若约分端点均为 K 的素因子光滑，则得到同一关系格的支撑接口，但仍需检查有限指数盒，否则产生支撑逃逸标签。冻结审计的 149 个一级候选中有 48 个严格小模数表示下降，其中 41 个发生双端点支撑逃逸、7 个仅一端支撑逃逸、0 个两端都保持 K 支撑。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-f-overflow-r-modulus-repair
topics:
- type-I
- F-state
- relation-lattice
- rational-gap
- descent
- support-escape
- q-adic
- proof-program
sources:
- claim: type-I-f-overflow-r-modulus-repair
  role: balanced-endpoint-input
visibility: public
last_checked: '2026-07-30'
---

# 盒外见证的端点平衡小模数表示下降

## 引理

沿用 \(R\)-因子修复分支的记号。设

\[
\frac AB\equiv-1\pmod R,\qquad
m\mid\gcd(R,B-1),\qquad
m\equiv3\pmod4.
\]

令

\[
R=mt,\qquad
A=mu-1,\qquad
B=mv+1.
\tag{1}
\]

则 \(u,v\) 为非负整数，且由 \(A+B=Rm_0\) 得

\[
u+v=t\,m_0.
\tag{2}
\]

若 \(t>1\) 且 \(\gcd(v,t)=1\)，令 \(g=\gcd(u,v)\) 并写

\[
\bar u=\frac ug,\qquad \bar v=\frac vg.
\tag{3}
\]

则

\[
\gcd(\bar u,\bar v)=1,\qquad
\gcd(\bar v,t)=1,\qquad
\frac{\bar u}{\bar v}\equiv-1\pmod t.
\tag{4}
\]

因此，\((\bar u,\bar v,t)\) 是严格更小模数 \(t<R\) 上的目标有理表示。

## 证明

因为 \(m\mid R\) 且 \(m\mid B-1\)，而 \(R\mid A+B\)，所以
\[
A\equiv-B\equiv-1\pmod m,
\]
从而 (1) 中的 \(u\) 为整数。将 (1) 代入 \(A+B=Rm_0\) 得 (2)。

若 \(\gcd(v,t)=1\)，则 \(\gcd(g,t)=1\)，所以约分后的 \(\bar v\) 仍在
\((\mathbb Z/t\mathbb Z)^\times\) 中。由 (2) 除以 \(g\) 并模 \(t\) 取值，
\[
\bar u+\bar v\equiv0\pmod t,
\]
故 \(\bar u\bar v^{-1}\equiv-1\pmod t\)。因 \(t>1\) 且 \(m\ge3\)，有
\(t=R/m<R\)，得到严格小模数表示下降。

## 与关系格/状态下降的边界

这个下降首先发生在“端点表示”层，不自动是原 \(K\) 的有限指数盒见证。要把它
接回目标纤维，需要同时满足：

1. \(\bar u,\bar v\) 的全部素因子属于 \(K\) 的素因子支撑；
2. 对应指数向量落在所选有限盒内；
3. \(4K\equiv1\pmod t\) 能与新的状态参数或提升恒等式兼容。

若第 1 项失败，\(\bar u\) 或 \(\bar v\) 的 \(K\)-光滑分解残差就是一个明确的
支撑逃逸标签；它应进入 G 型外部角色、Type II 因子或新的标记下降，而不能被误记为
F 型目标纤维命中。若第 1 项成立但第 2 项失败，则得到小模数上的盒外关系，可继续
应用有理缺口分母桥。

## 冻结审计

对 \(R\)-因子修复分支的 149 个一级候选逐项检查 (1)--(4)，并以原 \(K\) 的素因子
支撑剥离 \(\bar u,\bar v\) 的残差：

~~~text
candidate_gap_count: 149
strict_balanced_reduction_count: 48
balanced_support_preserved_count: 0
balanced_external_support_count: 41
forward_strict_balanced_reduction_count: 24
reverse_strict_balanced_reduction_count: 24
~~~

结果字段位于：

~~~text
reproductions/type-i-f-overflow-r-modulus-repair-results.json
~~~

结果文件 SHA-256：

~~~text
c656c91ebb02a33e8d1f5c78db70ce14ac5fbc2decc0db99e05bcbcc1fbee22f
~~~

该边界把一级修复失败分成两个可证明的方向：

\[
\boxed{
\text{小模数且支撑保持的表示下降}
\quad\lor\quad
\text{小模数表示下降但端点支撑逃逸}.
}
\]

当前样本全部落入第二类，因此下一步不应把小模数表示直接当作 F 型命中，而应研究
支撑逃逸端点能否构造 G/Type II 短证书，或其外部素因子是否在跨状态中形成容量超载。

更细的下游分流见[端点下降的更小模数 F/G 盒分流](type-I-f-overflow-balanced-lower-modulus-fiber-profile.md)：
在严格下降的 48 个冻结样本中，6 个在更小模数 \(t\) 上重新命中原 \(K\)-指数盒，
42 个仍为 \(K\)-支撑内的盒外 F 型障碍，0 个转成更小模数的 G 型分离。由于
\(t\equiv1\pmod4\)，这三分仍是对偶/关系接口，不能直接当作合法 Type I 缺口。

## 复现

~~~bash
python3 reproductions/type_i_f_overflow_r_modulus_repair.py
~~~
