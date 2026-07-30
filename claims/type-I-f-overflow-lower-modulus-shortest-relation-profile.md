---
kind: claim
claim_id: type-I-f-overflow-lower-modulus-shortest-relation-profile
title: 端点下降 F-box miss 的最短关系与端点大小边界
statement: 对 42 个更小模数 F-box miss，用固定生成元顺序和邻居顺序的 Cayley 图 BFS 求得一个确定性最短 l1 关系向量。最短 l1 范围为 3--22，盒外层数范围为 1--19；33 个对应端点积大于 p/2，9 个逐一检查端点和的合法因子仍无 Type II 命中，固定 h=3t 探针为 0/42。该结果是规范 tie-break 下的诊断边界，不排除其它最短并列向量、非最短关系或因子重分配。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-overflow-balanced-lower-modulus-fiber-profile
  - type-I-f-overflow-balanced-endpoint-type-ii-boundary
topics:
- type-I
- F-state
- relation-lattice
- shortest-path
- endpoint
- type-II
- finite-audit
- overflow
sources:
- claim: type-I-f-overflow-balanced-lower-modulus-fiber-profile
  role: F-box-miss-input
- claim: type-I-f-overflow-balanced-endpoint-type-ii-boundary
  role: endpoint-criterion
visibility: public
last_checked: '2026-07-30'
---

# 端点下降 F-box miss 的最短关系与端点大小边界

## 规范最短关系

对每个 F-box miss，令 \(q_1,\ldots,q_r\) 按冻结因子分解顺序排列，在由
\(q_i^{\pm1}\) 生成的 Cayley 图上从单位元到 \(-1\bmod t\) 做 BFS。邻居依次采用
\(q_i\)、\(q_i^{-1}\)，因此得到一个可复现的最短 \(\ell^1\) 向量；若存在并列最短向量，
本卡只固定这个 tie-break，不把向量本身宣称为选择不变对象。

对该向量 \(z\)，取互素端点
\[
U=\prod_iq_i^{\max(z_i,0)},\qquad
V=\prod_iq_i^{\max(-z_i,0)}.
\]
盒外层数定义为
\[
\Delta(z)=\sum_i\bigl(|z_i|-\nu_i\bigr)_+.
\]

## 冻结审计

复现脚本：

~~~text
reproductions/type_i_f_overflow_lower_modulus_shortest_relation.py
~~~

结果文件：

~~~text
reproductions/type-i-f-overflow-lower-modulus-shortest-relation-results.json
~~~

输入结果 SHA-256：

~~~text
c656c91ebb02a33e8d1f5c78db70ce14ac5fbc2decc0db99e05bcbcc1fbee22f
~~~

统计为：

~~~text
state_count: 42
shortest_l1_min: 3
shortest_l1_max: 22
overflow_layers_min: 1
overflow_layers_max: 19
size_excluded_count: 33
small_product_count: 9
endpoint_type_ii_hit_count: 0
three_t_endpoint_hit_count: 0
~~~

其中 33 个状态满足 \(UV>p/2\)，由合法 Type II 缺口的大小界直接排除；余下 9 个
状态完整枚举 \(h\mid U+V\)、\(h\equiv3\pmod4\) 的端点对证书，命中为 0。固定
\(h=3t\) 的探针在 42 个状态中也全部失败。

## 解释边界

最短 \(\ell^1\) 长度是该有限生成集上的规范距离，但并列最短向量会随生成元顺序
改变。因而本卡不能把 33/9 的端点大小分流升级成所有关系的排除定理；真正选择不变
的容量接口仍应使用目标纤维上的 \(\Omega_w(t)\) 或 Pareto 溢出集合。

## 复现

~~~bash
python3 reproductions/type_i_f_overflow_lower_modulus_shortest_relation.py
~~~

---
