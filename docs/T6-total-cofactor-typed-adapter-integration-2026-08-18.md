# T6 total-cofactor typed adapter 接入记录

> 复核日期：2026-08-18
> 状态：`T6_GLOBAL_SELECTOR_TOTALITY = OPEN`
> 范围：为整体余因子 canonical 投影实现相对 E1--E5 verifier；不建立 actual reachability，
> 不把任何 fixture 注册为递归边。

## 已接入的相对合同

[`type_i_overflow_total_cofactor_typed_adapter.py`](../reproductions/type_i_overflow_total_cofactor_typed_adapter.py)
接受一个已重算的 Type-I `CHARGED` source、一个外部提供的 registration，以及绑定的
determinant receipt

\[
pn=4Md+1,\qquad R=4M-n,\qquad K=M(p-d),\qquad A\mid M.
\]

registration 必须引用同一个 `source_state_id`，并声明 persistent queue、parent receipt digest
和 terminal-first miss。verifier 只检查这些字段的存在性和相互绑定；它不访问一个实际队列，
也不会把 digest 的非空性解释为已经证明的 E1 来源。

对固定 \((p,A)\)，它构造

\[
C_A=(4A)^{-1}\pmod p,\qquad
K_A=AC_A,\qquad
R_A=\frac{4AC_A-1}{p},
\]

并分别重建 source 与 target 的全部 typed payload。命中中心平方盒时直接验证 Type-I 终端；
非命中时用有限单位群坐标判定 F/G：F 使用带版本的 Smith relation witness，G 使用 HNF
support lattice 的精确 dual character。两种类型都不得从 source 继承。

若 target 非 terminal，则 adapter 还验证

\[
\frac{K_S}{A}=C_A+pt,\qquad t>0,
\]

并以

\[
\left(\left\lfloor\frac{(p-1)^2}{4A}\right\rfloor,\frac KA,0,0\right)
\]

的严格第二坐标下降支付 Type-I `CHARGED` 的 `LOCAL_DROP`。\(t=0\) 必须拒绝为 canonical
stutter；transient source 或未登记 terminal-first miss 也必须拒绝。

## 已验证的边界控制

聚焦控制全部只是合同 fixture，不声称它们是在 terminal-first scheduler 中实际可达：

| 控制 | 结果 |
|---|---|
| \(p=73,(A,M,d,n)=(3,45,15,37)\) | F -> G，rank \((432,870,0,0)\to(432,67,0,0)\) |
| \(p=73,(22,220,18,217)\) | G -> F，rank \((58,550,0,0)\to(58,39,0,0)\) |
| \(p=73,(5,40,26,57)\) | F -> hit，终端分母 \((22,110,4015)\) |
| \(p=73,(3,3,6,1)\) | canonical stutter 被拒绝 |
| transient 或缺失 terminal-first miss | registration 被拒绝 |

## 对 T6 的实际影响

这一增量解决的是 O1 residual overflow 中的**序列化与重分类实现问题**：一旦未来的 selector
已经给出真实 persistent source registration 和 terminal-first miss，整体余因子分派不再缺少
通用 F/G/hit、state hash、scope 或 T5 ticket 的 reference implementation。

仍缺少的量词没有变化：必须证明每个 actual residual `A>1` overflow 要么先 terminal，
要么拥有这样的真实 registration 和 determinant receipt。adapter 不能制造 parent history，
也不能把 raw 或 transient checkpoint 升格为 persistent edge。因此
`GAP-O1-A-GT-ONE-OVERFLOW` 与 `T6_GLOBAL_SELECTOR_TOTALITY` 保持 `OPEN`。

## 复现

```bash
python3 reproductions/type_i_overflow_total_cofactor_typed_adapter.py --verify
python3 -m unittest tests/test_type_i_overflow_total_cofactor_typed_adapter.py
python3 reproductions/type_i_t6_selector_obligation_ledger.py --verify
```

相关的条件性数学 claim 见
[整体余因子 typed projection](../claims/type-I-overflow-total-cofactor-typed-projection-dispatch.md)，
全局缺口的 machine-readable 账本见
[T6 selector obligation ledger](T6-selector-obligation-ledger-2026-08-18.md)。
