---
kind: claim
claim_id: type-I-f-overflow-balanced-endpoint-type-ii-boundary
title: 端点下降 F-box miss 的平衡端点 Type II 边界
statement: 对冻结的 42 个更小模数 F-box miss，令 U,V 为端点平衡关系约分后的互素端点。若某个 Type II 证书恰以 U,V 作为前两项，则它等价于存在合法 h|U+V 且 UV|(p+h)/4。精确审计中 41/42 个状态由 UV>p/2 的大小界排除，唯一未排除状态 p=509434249、t=41、(U,V)=(47,76) 只需检查 h=3,123，均未命中；所有 42 个 h=3t 探针也未命中。这是端点对分支的有限边界，不排除因子重分配或其它 Type II 形式。
claim_status: computationally_reproduced
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-f-overflow-balanced-lower-modulus-fiber-profile
  - type-II-coprime-factor-normal-form
topics:
- type-I
- type-II
- F-state
- endpoint
- size-bound
- finite-audit
- descent
sources:
- claim: type-I-f-overflow-balanced-lower-modulus-fiber-profile
  role: lower-modulus-F-miss-input
- claim: type-II-coprime-factor-normal-form
  role: exact-Type-II-normal-form
visibility: public
last_checked: '2026-07-30'
---

# 端点下降 F-box miss 的平衡端点 Type II 边界

## 端点正规化

对一个严格端点下降候选，记原端点平衡式为

\[
R=mt,\qquad A=mu-1,\qquad B=mv+1.
\]

令 \(g=(u,v)\)，并写

\[
U=u/g,\qquad V=v/g.
\]

则 \((U,V)=1\)，且前一层的端点关系给出

\[
U+V\equiv0\pmod t,
\qquad U/V\equiv-1\pmod t.
\tag{1}
\]

这里的 \((U,V)\) 是确定的平衡端点对，不依赖 F-box miss 关系格中最短向量的选取。

## 端点对 Type II 判据

固定素数 \(p\equiv1\pmod4\)。若一个 Type II 互素正规形的前两项恰为
\((\min(U,V),\max(U,V))\)，则按互素 Type II 正规形定理，它必须且只需满足：存在

\[
h\equiv3\pmod4,\quad 3\le h\le p-2,\quad h\mid U+V,
\tag{2}
\]

使

\[
x_h=\frac{p+h}{4},\quad UV\mid x_h.
\tag{3}
\]

若 (2)--(3) 成立，令 \(A=\min(U,V)\)、\(B=\max(U,V)\)、\(C=x_h/(UV)\)，则

\[
x_h=ABC,\quad (A,B)=1,\quad A\le B,\quad h\mid A+B,
\]

正是 Type II 证书的互素正规形。反向方向由同一定理的必要条件直接得到。

## 大小排除

对任意合法 \(h\le p-2\)，有

\[
x_h=\frac{p+h}{4}\le\frac{p-1}{2}<\frac p2.
\]

因此只要 \(UV>p/2\)，条件 \(UV\mid x_h\) 不可能成立，整个端点对分支无需枚举缺口。

## 冻结审计

复现脚本：

~~~text
reproductions/type_i_f_overflow_balanced_endpoint_type_ii.py
~~~

结果文件：

~~~text
reproductions/type-i-f-overflow-balanced-endpoint-type-ii-results.json
~~~

输入结果文件 SHA-256：

~~~text
c656c91ebb02a33e8d1f5c78db70ce14ac5fbc2decc0db99e05bcbcc1fbee22f
~~~

冻结统计为：

~~~text
state_count: 42
size_excluded_count: 41
small_product_count: 1
endpoint_type_ii_hit_count: 0
three_t_endpoint_hit_count: 0
~~~

唯一未被大小界排除的状态为

~~~text
p=509434249, orientation=reverse, t=41, (U,V)=(47,76), UV=3572
~~~

此时 \(U+V=123\)，合法因子缺口只有 \(h=3,123\)，两者均不满足
\(UV\mid(p+h)/4\)。对全部 42 个状态的固定探针 \(h=3t\) 也没有端点命中。

## 边界

该结果只封闭“固定平衡端点对”这一条 Type II 分支。它不排除：

- 将 F-box 关系格向量重新分配为另一对端点；
- 使用非最短关系或引入外部素因子；
- 其它 Type II、Type I 或严格可提升递降出口。

因此当前未闭合的全局桥仍是：把 F-box miss 的选择不变溢出价格映射到可收费的
\(q\)-进高度、合法 Type II 因子重分配，或严格下降势函数。

## 复现

~~~bash
python3 reproductions/type_i_f_overflow_balanced_endpoint_type_ii.py
~~~

---
