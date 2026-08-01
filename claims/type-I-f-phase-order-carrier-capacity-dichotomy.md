---
kind: claim
claim_id: type-I-f-phase-order-carrier-capacity-dichotomy
title: 冻结 F 状态的相位阶—载体高度二分与容量边界
statement: 在冻结的 45 个双方向 F 型相位需求状态中，逐活跃方向同时记录角色阶 d、K 指数 b=v_q(K) 和规范源块高度 h。90 个方向中 78 个来自非空相位投影且 d=2；其余 12 个方向全部属于 6 个空投影状态，且 d>2h。对 81 个同色 (p,q,label) 组，选定块的高度满足严格模数差整除和 q 进容量上界，未出现容量超载。因此在这组证据中，角色阶债务只形成状态内空投影证书，尚未形成跨状态 q 进需求；该结论是冻结数据的计算复现，不是所有 F 状态的全称定理。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-two-direction-phase-demand-map
  - type-I-linear-multi-active-fourier-carrier-vector
  - type-I-cross-state-q-adic-capacity-bound
topics:
- type-I
- F-state
- finite-fourier
- phase-order
- carrier
- q-adic
- capacity
- proof-boundary
- proof-program
sources:
  - claim: type-I-f-two-direction-phase-demand-map
    role: frozen-phase-and-carrier-input
  - claim: type-I-cross-state-q-adic-capacity-bound
    role: same-label-capacity-bound
visibility: public
last_checked: '2026-08-01'
---

# 冻结 F 状态的相位阶—载体高度二分与容量边界

## 1. 字典字段

对相位需求回执中的每个选定活跃方向，记

\[
q,
\qquad b=v_q(K),
\qquad \theta=\frac{u}{d}\pmod1,
\qquad h=v_q(tR+1),
\]

其中 \(d\) 取约分后角色 \(\exp(2\pi i\theta)\) 的阶，\(t\in\{s,a\}\) 是高度优先
选择的线性块标签。保存的有限债务是

\[
\mathsf D_{\mathrm{ord}}(q)
=\min\left\{1,\left(\frac{b}{d}\right)^2\right\}.
\]

另记单活跃模型的诊断余量

\[
\Delta_{\mathrm{sa}}=d-2b.
\]

只有在已知单活跃循环商且没有其它坐标相位抵消时，
\(\Delta_{\mathrm{sa}}>0\) 才等价于有限盒缺口；在多活跃状态中，它不能单独推出
目标缺失或载体超额。

## 2. 冻结数据的精确分裂

输入是
`reproductions/type-i-f-two-direction-phase-demand-results.json`，其 SHA-256 为

```text
27e15c714b238cc580b313b70c691c96b1759ab6b022bd12808429ec082265ea
```

结果文件 `reproductions/type-i-f-phase-weighted-carrier-dictionary-results.json` 的
SHA-256 为

```text
8d4eb0b21b32f14372b17c8a8f6599701f756f2e9461234c24d8b36b688708c7
```

聚焦脚本
`reproductions/type_i_f_phase_weighted_carrier_dictionary.py` 输出：

| 字段 | 数值 |
|---|---:|
| F 状态数 | 45 |
| 活跃方向数 | 90 |
| 空相位投影状态 | 6 |
| 非空投影方向 | 78 |
| 非空投影方向的角色阶 | 全部为 2 |
| 空投影中的高阶方向 | 12 |
| 同色容量组 | 81 |
| 容量超载组 | 0 |

因此高阶相位债务并未与跨状态容量混合出现：它全部落在已由空二维投影给出的状态内
F 证书中。非空投影分支只留下阶二相位，不能仅凭角色阶再收费一次。

## 3. 同色载体容量

对同一核心素数、同一活跃素数 \(q\) 和同一块标签 \(t\) 的方向，若两条记录的模数
不同，则块刚性给出

\[
q^{\min(h_i,h_j)}\mid (tR_i+1,tR_j+1)
\quad\Longrightarrow\quad
q^{\min(h_i,h_j)}\mid R_i-R_j.
\]

当 \(q\) 为奇素数且 \(R_i\equiv R_j\equiv3\pmod4\) 时，还可以使用
\((R_i-R_j)/4\) 作为整数坐标。对每个同色组，跨状态容量引理给出

\[
\sum_i h_i
\le \frac{M}{q-1}+H,
\]

其中 \(M\) 是该坐标区间长度，\(H=\max_i h_i\)。脚本逐对检查整除关系，并逐组检查
该上界；81 组全部通过。

这一步证明的是**实际块高度**的容量约束，而不是相位阶债务的容量约束。相位阶
\(d\) 只有在另有定理把它映到同一标签、同一模数差或一个有界重复度的外部载体时，才
能加入上述账本。

## 4. 对统一选择器的结论

本卡给出当前最窄的桥梁边界：

\[
\boxed{
\text{高阶相位}\Rightarrow\text{状态内空投影证书},
\qquad
\text{阶二相位}\Rightarrow\text{实际载体容量输入};
}
\]

但尚未得到

\[
\text{角色阶债务}\Rightarrow\text{跨状态 }q\text{-进超载}.
\]

所以不能把 \(\mathsf D_{\mathrm{ord}}\) 与 \(h\) 相加、相乘或互相替换。下一步若要
推进全称选择器，必须构造额外的相位—载体匹配定理，例如：高阶角色在非空投影分支中
强制一个带方向的新素数层，或证明相位缺口只能由一个合法的 support-switch/marked
状态支付。否则本卡只应作为 typed `analysis_evidence`，不升级为递归边。

## 5. 复现

```bash
python3 reproductions/type_i_f_phase_weighted_carrier_dictionary.py --verify
```

结果文件为
`reproductions/type-i-f-phase-weighted-carrier-dictionary-results.json`。
