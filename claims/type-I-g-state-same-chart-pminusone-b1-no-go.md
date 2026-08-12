---
kind: claim
claim_id: type-I-g-state-same-chart-pminusone-b1-no-go
title: G 图表排除同图表 p 减一的 B 等于一桥
statement: 设合法图表 4K=pR+1 的单位群上存在二次角色 chi，使 chi(q)=1 对所有 q|K 且 chi(-1)=-1。则任何要求 C|K 且 4C=-1 (mod R) 的同图表 p-1、B=1 桥都不存在。因而 R=7 的 Jacobi G 状态严格排除 E=8、C=5 (mod 7) 的固定 p-1 射线；这是一条局部无出口边界，不是全局递降或反例。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fixed-universal-pminusone-b1-rays
  - type-I-seven-p-plus-one-r7-b1-upper-bridge
  - type-I-g-separator-certificate-reconstruction
topics:
  - type-I
  - g-state
  - p-minus-one
  - b1
  - quadratic-character
  - strict-no-go
sources:
  - reproduction: reproductions/type_i_g_state_same_chart_pminusone_b1_no_go.py
    role: explicit-jacobi-controls-and-divisor-residue-check
visibility: public
last_checked: '2026-08-12'
---

# G 图表排除同图表 (p-1) 的 (B=1) 桥

## 引理

令 (p) 为核心素数，且

\[
4K=pR+1,
\qquad R\equiv3\pmod4,
\]

于是 ((K,R)=1)。假设存在单位群

\[
G=(\mathbb Z/R\mathbb Z)^\times
\]

上的二次角色

\[
\chi:G\longrightarrow\{\pm1\}
\]

满足

\[
\chi(q)=1\quad(q\mid K),
\qquad \chi(-1)=-1. \tag{1}
\]

若 (E=R+1) 属于固定 (p-1) 菜单，且同一图表存在 (B=1) 桥，则固定射线的
正规形条件要求某个正因子 (C\mid K) 满足

\[
4C\equiv-1\pmod R. \tag{2}
\]

但由 (1) 和 (C\mid K)，

\[
\chi(C)=1,
\qquad
\chi(4)=\chi(2)^2=1,
\]

故

\[
\chi(4C)=1,
\]

而 (2) 的右端给出

\[
\chi(4C)=\chi(-1)=-1,
\]

矛盾。因此不存在这样的 (C)，同图表 (p-1)、(B=1) 桥被严格排除。

这也适用于 Jacobi G 证书：取

\[
\chi(a)=\left(\frac aR\right).
\]

特别地，在 (R=7) 时，条件 (2) 是 (C\equiv5\pmod7)。所以只要
\((q/7)=1) 对每个 (q\mid(7p+1)/4)，就不可能命中此前的
[(R=7,E=8) (B=1) 上半区桥](type-I-seven-p-plus-one-r7-b1-upper-bridge.md)。

## 边界含义

这条结果只删除一个十分具体的同图表出口。它不排除：

- 同一 (R) 的 (B>1) 正规形；
- 改变 (R) 后的 determinant dual 或 support reset；
- Type II 因子对、外部 slab 碰撞和其它严格下降边。

因此它是当前全局出口目标中的**严格负向分派**：G 状态不能把同图表
(p-1,B=1) 桥当作备用终端，后续证明必须支付其它分支的证书或下降势。

## 显式控制

- (p=1801,R=7)：(K=3152=2^4\cdot197)，两个素因子都是模 7 二次剩余，
  而 (C\equiv5\pmod7) 的 (K)-除子不存在；
- (p=241,R=3)：(K=181)，其唯一素因子模 3 为 1，要求变成
  (C\equiv2\pmod3)，同样不存在。

这两个控制只验证引理在具体 G 图表上的算术收据，不声称对应素数没有其它
Erdős--Straus 表示。

## 复现

```bash
python3 reproductions/type_i_g_state_same_chart_pminusone_b1_no_go.py --verify
```
