---
kind: claim
claim_id: type-I-overflow-qadic-obstruction-transfer
title: overflow 双对偶支撑阻碍的逐素数幂支付分解
statement: 对 verified overflow pn=4Md+1、M=kp+r 和旧支撑 A|M，若 q^a||A，则 d 通道可支付的旧支撑层数恰为 min(a,v_q(d)+v_q(k+1))，r 通道恰为 min(a,v_q(r)+v_q(dn-1))；相应未支付高度分别为 (a-v_q(d)-v_q(k+1))_+ 与 (a-v_q(r)-v_q(dn-1))_+。此外 q|d 强制 dn-1 为 q-进单位，q|r 强制 k+1 为 q-进单位。该账本精确解释局部支撑失败，但不提供跨状态相位、容量超载或递归边。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-support-preserving-dual-criterion
  - type-I-overflow-determinant-fixed-n-dual-support-conflict
topics:
- type-I
- overflow
- determinant
- q-adic
- charged-support
- dual-carrier
- support-obstruction
- proof-boundary
- proof-program
sources:
  - claim: type-I-overflow-support-preserving-dual-criterion
    role: dual-support-divisibility-filter
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: joined-support-debt-replay
  - result: reproductions/type-i-representation-dual-capacity-selector-results.json
    role: typed-reset-debt-fields
visibility: public
last_checked: '2026-08-03'
---

# overflow 双对偶支撑阻碍的逐素数幂支付分解

## 1. 设定

设 verified overflow 满足

\[
pn=4Md+1,
\qquad M=kp+r,
\qquad 1\le r<p,
\]

并令旧 charged support \(A\mid M\)。固定一个素数幂

\[
q^a\parallel A.
\]

由 \(A\mid M\) 和 \(p\nmid M\)，有 \(q\ne p\)；又由

\[
pn\equiv1\pmod {q^a}
\]

得到 \(p,n\) 都是模 \(q^a\) 的单位。

## 2. d 通道的支付层

旧支撑在 d 图表中需要

\[
q^a\mid d(p-r).
\]

因为

\[
p-r=(k+1)p-M,
\]

且 \(q^a\mid M\)，所以截断到旧支撑的高度有

\[
\min\{a,v_q(p-r)\}
=
\min\{a,v_q(k+1)\}.
\tag{1}
\]

因此 \(d\) 通道由载体 \(d\) 和余数标签 \(k+1\) 共同支付的层数恰为

\[
P_d(q)=\min\{a,v_q(d)+v_q(k+1)\},
\]

未支付的精确高度为

\[
O_d(q)=a-P_d(q)
=\bigl(a-v_q(d)-v_q(k+1)\bigr)_+.
\tag{2}
\]

将 (2) 对所有 \(q^a\parallel A\) 相乘，正好得到

\[
\mathcal O_d
=\frac{A/\gcd(A,d)}{\gcd(A/\gcd(A,d),k+1)}.
\]

## 3. r 通道的支付层

同理，r 图表的旧支撑条件是

\[
q^a\mid r(p-d).
\]

由 \(pn\equiv1\pmod {q^a}\)，有

\[
p(dn-1)\equiv d-p=-(p-d)\pmod {q^a}.
\]

由于 \(p\) 是单位，

\[
\min\{a,v_q(p-d)\}
=
\min\{a,v_q(dn-1)\}.
\tag{3}
\]

所以 r 通道的支付层数和未支付高度分别为

\[
P_r(q)=\min\{a,v_q(r)+v_q(dn-1)\},
\]

\[
O_r(q)=\bigl(a-v_q(r)-v_q(dn-1)\bigr)_+.
\tag{4}
\]

将 (4) 对所有 \(q^a\parallel A\) 相乘，得到现有双对偶判据中的
\(\mathcal O_r\)。

## 4. 方向性单位推论

该分解还给出两个不能交换方向的局部事实：

- 若 \(q\mid d\)，则 \(dn-1\equiv-1\pmod q\)，所以 \(v_q(dn-1)=0\)。r 通道的
  这些支撑层只能由 \(r\) 支付；
- 若 \(q\mid r\)，因为 \(q\mid M=kp+r\) 且 \(q\ne p\)，有 \(q\mid k\)，从而
  \(k+1\equiv1\pmod q\)。d 通道的这些支撑层只能由 \(d\) 支付。

因此阻碍不是一个无方向的“缺少整除”：每个旧 \(q\)-层都带有载体支付和余数支付两种
来源，且当一个载体含 q 时，另一通道的余数支付被强制关闭。

## 5. 聚焦回执

验证器
`reproductions/type_i_overflow_qadic_obstruction_transfer.py --verify`
从冻结的 12 个 overflow receipt 重算 24 个双通道，并逐个 \(q^a\parallel A\) 检查：

1. determinant 余数的截断赋值等式 (1)、(3)；
2. 支付层与未支付高度的公式 (2)、(4)；
3. 两个方向性单位推论；
4. 逐素数幂账本的乘积与直接 \(\mathcal O_d,\mathcal O_r\) 完全一致。

输出结果保留每一行的 `carrier_height`、`residue_height`、`paid_height_capped` 和
`obstruction_height`，可直接作为后续跨状态容量或 alternate-source 搜索的 typed 输入。

统一 selector 进一步对每个双载体 RESET 重算

\[
\operatorname{Debt}_t
=\frac{\operatorname{lcm}(A,t)}{\gcd(\operatorname{lcm}(A,t),K_t)}.
\]

当 $t=d$ 时它精确等于

\[
\frac{A/\gcd(A,d)}{\gcd(A/\gcd(A,d),k+1)},
\]

当 $t=r$ 时精确等于

\[
\frac{A/\gcd(A,r)}{\gcd(A/\gcd(A,r),dn-1)}.
\]

因此 `support_debt.value=1` 与旧支撑整除完全等价；但它仍不是充分的递归条件，
还必须同时满足严格 support gain、正 canonical chart 和外层势下降。聚焦的 24 个
双通道中 8 条 verified edge 的 debt 为 1，16 条拒绝通道的 debt 逐行保留（其中
个别 debt=1 行仍因其它 E 条件失败）。

## 6. 逻辑边界

支付分解是状态内的精确算术恒等式。它没有证明：

- 不同 overflow 状态的余数标签形成嵌套 \(q\)-进相位胞；
- 阻碍高度落入有界标签区间并满足有界重复度；
- 某个阻碍因子自动给出 Type I/II、非空 marked 状态或 E1--E5 边；
- 丢弃旧支撑后的 reset 具有全局良基势。

还有一个不能省略的相位边界：\(O_d(q),O_r(q)\) 只记录未支付层数，并不确定
去掉 q 进赋值后的单位残数。真实反例如
[overflow 双通道 q 缺陷的单位相位非识别反例](type-I-overflow-qadic-dual-unit-phase-nonidentification.md)
表明，同一状态中两个通道可以有相同缺陷高度但不同单位相位；因此相位树容量必须
额外保存单位残数或显式仿射映射，不能仅按本卡的高度字段合并。

当前相位分派已覆盖赋值不等的缺口：
[不等赋值加权相位正规形](type-I-overflow-dual-valuation-asymmetry.md)证明这时先按
加权首层分裂处理，并记录 \(v_q(2p-r-d)=\min(v_q(k+1),v_q(dn-1))\)；赋值相等时
才进入 \(2p-r-d\) 的共同前缀判据。这个分派仍不等价于 source-switch 或递归边。

因此本卡是“表示—对偶—容量”选择器中的局部对偶账本，不是全称选择器证明。

## 复现

```bash
python3 reproductions/type_i_overflow_qadic_obstruction_transfer.py --verify
```

结果文件为
`reproductions/type-i-overflow-qadic-obstruction-transfer-results.json`。
