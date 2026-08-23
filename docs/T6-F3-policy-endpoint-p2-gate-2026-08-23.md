# T6-F3 policy endpoint 的 \(p^2\) gate 复核

> 日期：2026-08-23
> 基线：`c851bd213936b3bc8b3103b469292c139d229e97`
> 结论：`POLICY_ENDPOINT_P2_NORMAL_FORM = ESTABLISHED`；
> `B5 = OPEN_MINIMAL_RESIDUAL`；`F3 = OPEN`。

## 1. 修正的对象边界

现有 \(m=3\) claim 中有两个不同 multiplier：

1. 第一次 excess-\(\ell\) atomic child 的
   \[
   L_1=(E/\ell)F_y.
   \]
2. 对该 child 执行非空 \(p\)-free policy 后，在新 endpoint 重新 maximal-normalize
   得到的
   \[
   L_\omega=M_\omega/\mathcal A.
   \]

`(20zz-factor-21/23)` 的书面前提是 \(L_1=1+p^2\chi_1\)，其变量 \(D_y\) 也属于
第一次 child。它不能作为 \(L_\omega\) 的 actual-source gate。已有 \(a=1\) 固定控制还
显示，第一次 multiplier 可满足 \(p^2\) stutter，而后续 endpoint 的 canonical cofactor
已经严格下降；所以通用 \(d=1\) relay 不保持这个二阶同余。

这里否定的是“把旧公式引用为 \(L_\omega\) gate”这一对象映射，不是否定旧公式本身。

## 2. 新的 endpoint 坐标

对 policy 最终 primitive \(p\)-free node \(u+v=R\)，相对原 \(K\) 唯一重算

\[
u=E_uD_u,\qquad v=E_vD_v.
\]

逐素数 complete-excess 定义给出

\[
D_u,D_v\mid K,\qquad D_uD_v\mid K,
\]

\[
D_u\mid pE_vD_v+1,\qquad D_v\mid pE_uD_u+1,
\]

以及

\[
\boxed{L_\omega=E_uE_v.}
\]

所以正确的二阶门是

\[
E_uE_v=1+p^2\chi,\qquad
E_uR-E_u^2D_u-D_v=p^2\chi D_v.
\]

这套坐标把 actual divisor source、canonical maximality 和 \(p^2\) congruence 放在
同一个 endpoint 上，不再混用前一节点的 residual。

## 3. 两个 policy 分支

### 3.1 Full-capacity

若 \(\mathcal W_y\not\equiv\delta\pmod p\)，policy 到达

\[
u=(y,K)=D_yJ_y\mid K.
\]

因此该 endpoint 非终止时必是单侧 complete-excess。若

\[
R-u=(1+p^2\chi)d,
\]

令

\[
c=(pu+1)/d,\quad m=(d+u-1)/p,\quad w=K/(ud),\quad R=1+p\tau,
\]

则

\[
\tau=m+p\chi d,\qquad 4uw=c+p+p^3\chi,\qquad
p+c\mid mc^2-c+1.
\]

特别地 \(4u\mid c+p+p^3\chi\)，且 small-endpoint theorem 强制

\[
u^2\ge p.
\]

这些是比单独 \(L_\omega\equiv1\pmod{p^2}\) 更强、可直接从 source 重算的 divisor
gates，但尚未排空。

### 3.2 Short \(Q_{\rm pf}\)

若 \(\mathcal W_y\equiv\delta\pmod p\)，policy 到达

\[
u=y/Q_{\rm pf},\qquad v=x+(Q_{\rm pf}-1)u.
\]

selected side 的 complete-excess 赋值可以从 \(y,K,Q_{\rm pf}\) 唯一更新；companion
\(v\) 可能丢失旧 block 或产生新 block，所以必须重新计算。若一侧 multiplier 为 1，
交换后回到单侧系统；真正剩余的是

\[
E_u,E_v>1,\qquad E_uE_v=1+p^2\chi
\]

的 path-anchored atomic receipt。

## 4. Checkpoint 与 E1--E5

| 项目 | 当前结论 |
|---|---|
| second-child tie-break | 算术上确定：full word / 最小 safe prime / 两个 bad occurrences |
| literal non-repeat | 已证：选中坐标严格缩小，canonical support 在非终止时严格增大 |
| E1 | 仅对已保存 persistent source path 且全部 priority-prefix miss 的子域成立 |
| E2 | endpoint maximal blocks 与 canonical target 唯一 |
| E3 | OPEN：缺实际 serializer、owner、normalizer、target-family receipt |
| E4 | target 被 validator 接受后由 \(\operatorname{Sol}(p)\) 恒等映射支付 |
| E5 | \(L_\omega\not\equiv1\pmod p\) 时严格；\(p^2\) residual 没有 ticket |

raw node 不重复并不等于 T5 下降。若 \(L_\omega=1+p^2\chi\)，parent 与 arithmetic
checkpoint 的 high-support local rank 都是 \((0,p-1)\)；它只能是 macro internal
checkpoint，不能作为 standalone successor 入队。

## 5. 当前最小缺口

1. 证明 full-capacity 的单侧 factor-pair 系统为空、terminal，或给出最终严格 guarded
   macro。
2. 证明 short-word two-sided 系统为空、terminal，或给出最终严格 atomic macro。
3. 从所有 actual proper-root states 全称构造 persistent source path 与 priority-prefix
   receipts；现有结论只是 source-bound。
4. 接入 E3 serializer/owner/F1 grammar，并证明所有 target recursive closure。
5. 单独处理 pure-dyadic multiplier 和 \(m=3,q=5\) 以外的 proper-root slices。

因此不能升级 B5、F3、T6 或 Erdos--Straus 猜想。

## 6. 聚焦重放

```bash
python3 reproductions/type_i_t6_f3_policy_endpoint_p2_gate.py --verify
python3 -m unittest tests.test_type_i_t6_f3_policy_endpoint_p2_gate -v
```

复现器只核对一个 two-sided \(p^2\) control、一个实际 p-free one-sided endpoint control
和一个同 chart 重新规范化时 multiplier 同余并非不变量的控制；第三项不是
\(\omega_{\rm pf}\) 路径证据。脚本不扫描素数、参数、selector history 或证书菜单。
