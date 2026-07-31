---
kind: claim
claim_id: type-I-formal-external-slab-collision-absorption-rechart
title: 单新支撑 q-slab 的双碰撞终端与容量吸收图表族
statement: 设核心图表 4K=pR+1 的一个形式表示只留下单个 K 外素数幂 Q=q^e，写成 X=Qa、Y=b、(X,Y)=1、ab|K、X+Y=Rm，并令 L=XY。对任意 T|(X+Y)，4L|(p+T) 直接给出 gap T 的 Type II 证书，4L|(pT+1) 则直接给出以 T 为模数的中心 Type I 命中及其自然 gap 证书。若 q!=p，对任意 Q|M|L 都有 M-indexed 规范图表 pR_M=-1 (mod 4M)、1<=R_M<4M，使 M|K_M；在隔离的 absorption-only 阶段中，R_M<R 给出 W=Sol(p) 上恒等提升且严格降 R 的 rechart，在未受限全局图中则仍只是 candidate_transition。特别地，R_Q!=R，故要么下降，要么 Q>R/4。该析取不覆盖 q=p、其它外部坐标或 large-slab 分支，下降也不可能保留全部旧 K。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-formal-reach-odd-combination-box-rigidity
  - type-I-general-b-centered-square-spectrum
  - type-I-coprime-factor-normal-form
  - type-II-coprime-factor-normal-form
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - F-state
  - formal-target-pair
  - external-slab
  - q-adic
  - capacity
  - support-switch
  - rechart
  - well-founded-potential
  - proof-boundary
sources:
  - claim: type-I-formal-reach-odd-combination-box-rigidity
    role: external-slab-output-interface
  - claim: denominator-escape-state-contract
    role: support-switch-and-phase-contract
visibility: public
last_checked: '2026-07-31'
---

# 单新支撑 \(q\)-slab 的双碰撞终端与容量吸收图表族

## 1. 单外部 slab

固定核心素数 \(p\equiv1\pmod {24}\) 和一张目标图表

\[
4K=pR+1,
\qquad R\equiv3\pmod4.
\tag{1}
\]

设形式表示格或 Reach 组合留下一个外部素数幂

\[
Q=q^e,
\qquad e\ge1,
\qquad q\nmid K,
\tag{2}
\]

并给出正整数 \(a,b,m\)，使

\[
X=Qa,
\qquad Y=b,
\qquad (X,Y)=1,
\qquad ab\mid K,
\qquad X+Y=Rm.
\tag{3}
\]

记

\[
S=X+Y=Rm,
\qquad L=XY=Qab.
\tag{4}
\]

式 (3) 是本卡的全部 slab 输入。它不声称每个 F/G 状态都能产生这样的单外部表示，
也不覆盖 \(q\mid K\) 的单坐标指数溢出，或剥离 \(q\) 后仍留下其它盒外坐标的组合。

## 2. \(\operatorname{Div}(S)\) 上的两类直接碰撞

任取正因子 \(T\mid S\)，并令

\[
U=\min(X,Y),
\qquad V=\max(X,Y).
\tag{5}
\]

由 (3) 有 \((U,V)=1\) 且 \(U<V\)。存在以下两个独立终端。

### 2.1 Type II 碰撞

若

\[
4L\mid p+T,
\tag{6}
\]

令 \(C=(p+T)/(4L)\)。则

\[
p=4UVC-T,
\qquad T\mid U+V.
\tag{7}
\]

式 (6) 与 \(p\equiv1\pmod4\) 给出 \(T\equiv3\pmod4\)。又有

\[
T\le U+V\le2UV\le2UVC.
\]

等号 \(T=2UVC\) 会迫使 \(U=V=C=1,T=2\)，与 \(T\equiv3\pmod4\) 矛盾。
所以 \(p=4UVC-T>T\)，从而 \(3\le T\le p-2\)。由 Type II 互素因子正规形，
\((U,V,C)\) 直接给出 gap \(T\) 的 Type II 证书。

### 2.2 跨图表中心 Type I 碰撞

若

\[
4L\mid pT+1,
\tag{8}
\]

定义

\[
C=\frac{pT+1}{4L},
\qquad J=\frac ST,
\qquad K_T=UVC,
\qquad D_T=U^2C.
\tag{9}
\]

则

\[
4K_T=pT+1,
\qquad D_T\mid K_T^2,
\qquad D_T<K_T.
\tag{10}
\]

因为 \(T\mid U+V\) 且 \((U,V)=1\)，模 \(T\) 下 \(V\) 可逆，并有

\[
\frac {D_T}{K_T}=\frac UV\equiv-1\pmod T.
\tag{11}
\]

所以 \(D_T\equiv-K_T\pmod T\)，即新图表的中心 Type I 盒命中。这里 \(D_T\) 是
新图表的中心平方除子，不是最终自然 gap 的 Bradford 除子。更显式地，令

\[
h=\frac{4U^2C+1}{T}.
\tag{12}
\]

则 \(h\) 为正整数，且

\[
p=4JUC-h,
\qquad Up+J=Vh,
\qquad (J,U)=1.
\tag{13}
\]

此外

\[
T(p-h)=4UC(V-U)-2>0.
\tag{14}
\]

因此 \(h\equiv3\pmod4\)、\(3\le h\le p-2\)，而 \((J,U,C)\) 是一张完整的
Type I 互素正规形。对应于自然 gap \(h\) 的实际证书除子是

\[
d_h=J^2C\mid(JUC)^2,
\]

不是 \(D_T\)。这是原素数的直接终端，不是递降边。

若 \((p,4L)=1\)，两种碰撞还可精确写成 \(4L\) 上的两个剩余类：

\[
T\equiv-p\pmod {4L},
\qquad
T\equiv-p^{-1}\pmod {4L}.
\tag{15}
\]

## 3. 规范部分容量吸收图表

以下再假设 \(q\ne p\)。由于 \(ab\mid K\) 且 \(p\nmid K\)，任取

\[
Q\mid M\mid L
\tag{16}
\]

都有 \((p,4M)=1\)。定义唯一代表

\[
1\le R_M<4M,
\qquad pR_M\equiv-1\pmod {4M},
\tag{17}
\]

以及

\[
K_M=\frac{pR_M+1}{4}.
\tag{18}
\]

模 \(4\) 化简 (17) 得 \(R_M\equiv3\pmod4\)，而模 \(M\) 立即给出

\[
\boxed{M\mid K_M.}
\tag{19}
\]

所以对每个给定的 \(M\)，(17) 是把该 slab 子积注入新 \(K\) 容量的唯一同 \(p\)
图表。\(M\) 本身只形成由 (16) 索引的容量梯，并没有规范选择规则。若

\[
R_M<R,
\tag{20}
\]

则它可在预先隔离的 `external_capacity_absorption` 阶段中登记为
`isolated_verified_rechart`：

| 合同项 | 核验 |
|---|---|
| E1 | (16)--(20) 给出正性、互素、模类和整除 |
| E2 | 后继为 \((p,R_M,K_M)\)，并从其完整因子分解重新生成目标纤维 |
| E3 | 重算 \(4K_M=pR_M+1\)、\(M\mid K_M\) 及新图表的 hit/F/G 类型 |
| E4 | 两端都取 \(W=\operatorname{Sol}(p)\)，提升映射为恒等映射 |
| E5 | 该隔离阶段只允许 (20) 的边，势函数 \(R\in\mathbb N\) 严格下降 |

这里必须重算新状态，不能把旧图表的指数见证、Fourier 角色或缺陷向量直接搬过去。
这一 E5 只对隔离的吸收阶段成立；若同时允许使 \(R\) 增大的反向因子转移，便会产生
二环，不能把两种定向混写成一个良基系统。在完整 phase 状态机尚未定义时，该输出在
未受限的全局递降图中只能标为 `candidate_transition`，不能直接并入主递降闭包。

## 4. 小 slab 析取、\(q=p\) 与容量损失

在 (17) 中取 \(M=Q\)。若 \(R_Q=R\)，则 (18) 给出 \(Q\mid K\)，与 (2) 矛盾。
所以

\[
R_Q<R
\quad\text{或}\quad
R<R_Q<4Q.
\tag{21}
\]

特别地，

\[
\boxed{4Q\le R\Longrightarrow R_Q<R.}
\tag{22}
\]

因此单外部 slab 至少给出如下无样本析取：两类碰撞直接终端；否则，小外部幂
\(Q\le R/4\) 可进入规范容量吸收；剩余困难被压到 \(Q>R/4\) 的 large-slab 分支。

若 \(q=p\)，则任意同 \(p\) 图表都满足

\[
4K'=pR'+1\equiv1\pmod p,
\]

故 \(p\nmid K'\)。所以本节的 \(M\)-injection 不能吸收这个外部坐标；这不排除其它
同 \(p\) 终端、坐标重组或不同类型的状态边。

这一分支下，前两种 slab 碰撞本身也为空：由 \((X,Y)=1\) 可知 \(p\nmid Y\)，故
\(p\nmid S\) 及 \(p\nmid T\)；但 (6) 模 \(p\) 会要求 \(p\mid T\)，而 (8) 模
\(p\) 会给出 \(0\equiv1\)，均不可能。此时当然也不能使用 (15) 中的 \(p^{-1}\)。

下降图表也不能保留全部旧容量。若某个同 \(p\) 图表满足 \(K'=cK\)，则

\[
pR'+1=c(pR+1).
\]

于是 \(p\mid c-1\)。写 \(c=1+pt\)，便有

\[
R'=R+4Kt.
\tag{23}
\]

当 \(c>1\) 时，(23) 严格增大 \(R\)。所以任何降 \(R\) 的 support switch 都必须
舍弃一部分旧 \(K\) 支撑或指数容量；(19) 只能声称吸收选定的 \(M\)，不能声称搬运
整个旧 slab 或旧 \(K\)。

## 5. 两个精确边界

聚焦核验给出两种互补行为。

| \((p,R)\) | \((X,Y)\) | \(L\) | 两碰撞 | 含 \(Q\) 的下降子积 |
|---:|---:|---:|---|---|
| \((178513,183)\) | \((13,170)\) | \(2210\) | 均空 | 仅 \(M=13,26\)；\(R_{13}=35\)、\(R_{26}=87\) |
| \((78268369,8895)\) | \((8243,652)\) | \(5374436\) | 均空 | 无；\(R_{8243}=10395>R\) |

第一例的完整子积满足 \(R_L=1543>R\)，说明下降会损失大部分 slab 容量。第二例对
所有 \(Q\mid M\mid L\) 都有 \(R_M>R\)，严格否定“总能保留某个含 \(Q\) 的容量
子积并降 \(R\)”这一更强命题。它不是 Erdos--Straus 猜想的反例；该素数仍可由其它
仿射边界 gap 直接终端。

## 6. 证明边界与下一接口

本卡把表示格留下的外部 slab 首次接到两个直接正规形及一个受控的良基 support switch，
但没有证明下列全称命题：

1. 每个 terminal-free F/G 状态都产生单外部 slab；
2. large-slab 必有 \(\operatorname{Div}(S)\) 碰撞；
3. 吸收后的新图表必为 hit，或必继续产生可下降 slab；
4. \(q=p\) 分支存在其它同目标修复。

因此下一步应为 large-slab 寻找其它 Reach slab、直接终端或新的 equation target，
并为真正的状态边给出全域解提升；否则 unrestricted rechart 只是在不同图表中重新编码
原短证书问题。

## 7. 聚焦复现

```bash
python3 reproductions/type_i_formal_external_slab_absorption_rechart.py
python3 reproductions/type_i_formal_external_slab_absorption_rechart.py --verify
```

结果文件：

```text
reproductions/type-i-formal-external-slab-absorption-rechart-results.json
```

脚本与结果 SHA-256 分别为
`a0cf9ab36e63630dbe42f54b69567840c22b03033b08f67e2a7f486473081555`、
`872a5dc39c3a4ffefe2b88354d11a5d1d423865717e4499ab6920a2e650dfc04`。
