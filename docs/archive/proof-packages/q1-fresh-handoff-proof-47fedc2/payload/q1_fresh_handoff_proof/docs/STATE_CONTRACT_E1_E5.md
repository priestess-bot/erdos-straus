# Fresh-G-Handoff 的 E1--E5 状态合同实例化

## 1. Source state

```text
state_class          = type_ii_q_one_g_endpoint
equation_target      = 4/p
marked_solution_set  = Sol(p)
q                     = 1
gap                   = 3
first_denominator     = X=(p+3)/4
phase_rank            = 2
source_tree_scope     = type_ii_endpoint_only
```

`G` 只表示模 3 target fiber 为空；它不表示 `Sol(p)` 为空。

## 2. Target state

```text
state_origin          = q_one_full_carrier_phase_root_entry_v1
state_class           = type_i_full_carrier_low_root
source_tree_scope     = fresh_source_tree_only
normal_form           = type_i_full_carrier_low_root_v1
equation_target       = 4/p
marked_solution_set   = Sol(p)
R                     = R_X=(8X+1)/3
K                     = K_X=X(R_X-2)
absorbed_support      = 1
phase_rank            = 1
```

## 3. E1

必须同时保存：

- 输入确实是 ordinary `q=1 G` endpoint；
- root 是由 `p` 预声明的闭式函数，不读取 target factorization；
- fresh actual source
  
  \[
  (p,R_X(p-1)-p,p-1)
  \]
  
  满足 source equation 与 gcd；
- `q=p`、shift `1` 的 raw edge 重放到 `(1,R_X-1,1)`；
- target scope 是 `fresh_source_tree_only`。

## 4. E2

只允许由 `p` 计算：

\[
t=(p-1)/24,
\quad
X=(p+3)/4,
\quad
R_X=16t+3,
\quad
K_X=X(16t+1).
\]

不得用“先发现某个成功 target 再倒推 root”的规则。

## 5. E3

重算而非继承：

\[
4K_X=pR_X+1,
\quad
3\le R_X\le p-2,
\quad
X\mid K_X,
\quad
p\nmid K_X.
\]

还须重算 source 正性、互素性、shift 整除与 state digest。

不能继承旧 Type II 的 F/G witness 作为 Type I target classification。

## 6. E4

ordinary 版本有

\[
W_S=W_T=\operatorname{Sol}(p),
\]

故

\[
\Phi_{T\to S}=\mathrm{id}.
\]

这不是 constant map，也不使用“假设已有一个解”。集合即使为空，identity 仍为合法全域函数。

## 7. E5

phase prefix：

\[
2=q=1G,
\qquad1=\text{fresh Type I},
\qquad0=n<p.
\]

允许非终端：

```text
2 -> 1
1 -> 1
1 -> 0
```

禁止：

```text
1 -> 2   # nonterminal
```

若在 Type I tree 中发现 Type II certificate，只能作为 terminal leaf。

取 lexicographic prefix

\[
\Pi(S)=(2,1,0),
\qquad
\Pi(T_X)=(1,B_p,K_X),
\]

第一坐标严格下降。

## 8. 局部与全局的区别

该 E5 证明的是：

> 这条具名 phase root-entry 本身可以被赋予一个不回返的严格 rank。

它**没有**证明所有仓库 recursive edge 可以放进同一个全局势函数。后者仍是 T5。

## 9. nontrivial mark

当前 `v1` 不应直接用于非平凡 marked state。

若 mark `theta` 是 portable：

```text
W_S = W_T = W_{p,theta}
```

并能在 fresh target 中逐字重新序列化，则 E4 仍可取 identity。此时建议新建独立 normal form：

```text
type_i_full_carrier_low_root_mark_preserving_v1
```

而不是扩大原 `v1` 的语义。
