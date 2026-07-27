---
kind: claim
claim_id: type-II-private-product-state
title: Type II 碰撞诱导私有积集状态与一孔同余陷阱
statement: 对有限规范移位扇，将每个 N_s=p+4s 的碰撞素因子剥离为 N_s=E_sR_s。完整射线失败等价于 R_s 的除子残数积集避开 E_s 的每个诱导目标 -e^{-1}。若 R_s 的生成支撑恰比其积集多一个诱导目标 f，则 p=E_s f^2 mod M_s。对前十四移位、p<=10^7 的 1792 条共同失败状态，1641 条所有诱导目标均在私有支撑外；其中 1141 条私有积集已饱和为整个支撑，只有 3 条触发一孔陷阱。
claim_status: established
topics:
- type-II
- factorization
- divisor-residues
- collision-state
- product-set
- congruence
- proof-program
sources:
- paper: grynkiewicz_marchan_ordaz2009
  locator: subsequence-product framework
  role: product-set-language
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-certificate-context
visibility: public
last_checked: '2026-07-25'
---

# Type II 碰撞诱导私有积集状态与一孔同余陷阱

## 碰撞诱导目标

固定有限规范移位扇 \(\mathcal S\)，并令 \(\mathcal P\) 为所有差
\(s-t\;(s\ne t)\) 的素因子集合。对一条移位 \(s=a^2c\)，写

\[
M=4ac,\qquad N=p+4s=ER, \tag{1}
\]

其中 \(E\) 只含 \(\mathcal P\)-素因子，\(R\) 不含它们。令

\[
\Pi_E=\{e\bmod M:e\mid E\},\qquad
\Pi_R=\{r\bmod M:r\mid R\},\qquad
K_R=\langle q\bmod M:q\mid R\rangle. \tag{2}
\]

所有素因子都与 \(M\) 互素。完整 Type II 射线失败
\(-1\notin\Pi_E\Pi_R\) 等价于

\[
F_E\cap\Pi_R=\varnothing,\qquad
F_E=\{-e^{-1}\pmod M:e\in\Pi_E\}. \tag{3}
\]

因此 \(F_E\cap K_R\) 的元素不是普通的未命中残数，而是私有积集在自己的生成支撑
内部必须缺失的指定目标；\(F_E\setminus K_R\) 则是支撑外约束。这给出一个不依赖
模数外素因子数的有限状态：

\[
\bigl(\Pi_E,\ K_R,\ \Pi_R,\ F_E\cap K_R\bigr). \tag{4}
\]

## 私有一孔同余陷阱

**引理。** 若存在 \(f\in F_E\) 使

\[
K_R\setminus\Pi_R=\{f\}, \tag{5}
\]

记 \(E_0=E\bmod M\)。则

\[
p\equiv E_0f^2\pmod M. \tag{6}
\]

**证明。** 设 \(P_R=R\bmod M\)。补因子映射

\[
x\longmapsto P_Rx^{-1} \tag{7}
\]

同时保持 \(K_R\) 与 \(\Pi_R\)，故保持 (5) 的单点补集。因此 \(f\) 是 (7) 的不动点，
从而 \(P_R=f^2\)。再由 \(N=ER\equiv p\pmod M\)，得到

\[
p\equiv E_0P_R=E_0f^2\pmod M,
\]

即 (6)。证毕。

当 \(E=1\)、\(f=-1\) 时，(6) 正是
`type-II-support-critical-congruence-trap` 的 \(p\equiv1\pmod M\)。
这里的形式允许有限碰撞因子存在，故适用于多移位的私有状态。

## 前十四规范移位的审计

取 \(s=1,\ldots,14\)。碰撞素数为

\[
\{2,3,5,7,11,13\}.
\]

在 \(p\le10^7\) 的 128 个共同失败素数上，14 条射线给出 1,792 个状态：

| 私有状态 | 数量 |
|---|---:|
| 所有诱导目标均在 \(K_R\) 外 | 1641 |
| 所有诱导目标均在 \(K_R\) 内 | 102 |
| 两者混合 | 49 |
| 全支撑外且 \(\Pi_R=K_R\) | 1141 |
| 触发 (5) 的私有一孔 | 3 |

同一审计扩展至前 19 条规范移位时，\(p\le10^7\) 的 45 个共同失败点给出：

| 扇 | 状态数 | 全支撑外 | 其中 \(\Pi_R=K_R\) | 私有一孔 |
|---:|---:|---:|---:|---:|
| \(H=14\) | 1792 | 1641 | 1141 | 3 |
| \(H=19\) | 855 | 747 | 510 | 0 |

所以增至 19 条后，主型仍是全诱导目标支撑外，且多数状态仍在私有支撑内完全饱和；
这不是前十四移位的偶然统计形状。

例如

\[
p=3{,}169{,}681,\quad s=5,\quad M=20,
\]

有

\[
E=3^2,\qquad R=17\cdot20717,\qquad F_E=\{11,13,19\}.
\]

私有支撑中只有 \(13\) 是诱导目标，且
\(K_R\setminus\Pi_R=\{13\}\)。引理给出

\[
p\equiv9\cdot13^2\equiv1\pmod {20},
\]

与该素数一致。

运行：

```bash
python3 reproductions/type_ii_private_product_state.py \
  --limit 10000000 --base-shift-bound 14 \
  --output reproductions/type-ii-private-product-state-h14-10m-results.json
```

会保存每个状态的碰撞与私有分解、诱导目标、支撑大小、积集缺陷及一孔同余核验。
把命令行的 `--base-shift-bound` 改为 19 可复现第二张表。

## 对后续势函数的限制

一孔状态可被 (6) 压入明确同余类，但只占本审计的 3 条。主残余是 1,641 条
全诱导目标支撑外状态，其中 1,141 条已经有 \(\Pi_R=K_R\)：私有积集在支撑内
没有任何孔可供补因子对合或 Kneser 膨胀利用。任何只追踪私有积集的小孔数、积集大小
或补因子轨道的势函数，都无法处理这一主型。

下一步必须利用 \(R_s\) 在不同移位间两两互素而 \(p+4s\) 又具有固定差值的双重约束，
并研究这些私有素因子的逐项残数分布。把 (6) 当作全覆盖机制，或仅由
\(p\bmod M\) 的字符值试图导出矛盾，都会遗漏主残余。
