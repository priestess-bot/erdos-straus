---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-nonminimal-d-lift-finite-phase-exclusion
title: H4 q0 re-entry 的非最小 D-lift 有限 phase 排除与最小残数边界
statement: >-
  在 actual q=1 high C=2 19-phase H4 q0>1 re-entry 中，令
  delta_d=2d(4d^2-2d+1)。若 p>delta_d 且 D>delta_d，则 D=delta_d+kp、
  ph-q+1=ell D，其中 k,ell>=1、k ell<=2d-1，且
  p=(2d ell delta_d-(2d-1))/(4d^2-1-2d k ell)。因此非最小 D-lift 被 31 个
  phase selector、d|abs(1536-a(p)) 的有限三元组 (d,k,ell) 完全参数化。对 213 个
  selector/divisor pairs 的 109 个 odd (u,d) supermenu pairs 作精确枚举，得到 233378 个
  三元组、137 个整 p 值、89 个 p>delta_d 值、7 个素数，且没有一个属于 actual
  p=912u+769,u mod119 in U31 phase progression；故 actual phase 中不存在
  p>delta_d,D>delta_d 的 q0 re-entry。另一方面，p>delta_d 的最小分支 D=delta_d
  在 d=1 (mod 3) 时不可能：其整除性会强制 0=1 (mod 3)。所以未关闭部分只能在
  p<=delta_d，或 p>delta_d、D=delta_d、d not equal to 1 (mod 3)；仍须叠加
  q-lock、p-adic/root、terminal、typed 与 atomic guards。
claim_status: established
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-d-residue-gate
  - type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
  - type-II-q-one-c-two-19-phase-fourth-anchor-terminal-gate
topics:
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - q0-reentry
  - divisor-gate
  - finite-sieve
  - source-provenance
  - carrier-d
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-d-residue-gate
    role: exact-D-residue-and-divisor-normal-form
  - claim: type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
    role: d-divides-selector-Delta-and-finite-phase-divisor-domain
  - claim: type-II-q-one-c-two-19-phase-fourth-anchor-terminal-gate
    role: exact-31-residual-phase-progressions-and-selector
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_q0_reentry_nonminimal_d_lift_finite_phase_exclusion.py
    role: exact-nonminimal-lift-phase-screen
visibility: public
last_checked: '2026-08-16'
---

# H4 \(q_0\) re-entry 的非最小 \(D\)-lift 筛

## 1. \(D>\delta_d\) 化为有界三元组

保留 actual H4 \(q_0>1\) re-entry 的 \(D\) 残数门，写

\[
\delta_d=2d(4d^2-2d+1),
\qquad
A:=ph-q+1=2dp-q+1.
\tag{1}
\]

现在设

\[
p>\delta_d,
\qquad D>\delta_d.
\tag{2}
\]

由 \(D\equiv\delta_d\pmod p\)、\(D\mid A\) 以及 \(A<2dp\)，唯一可写成

\[
D=\delta_d+kp,
\qquad
A=\ell D,
\qquad k,\ell\ge1.
\tag{3}
\]

将 \(q=(p+1)/(2d)\) 代入，得到

\[
2dA=(4d^2-1)p+(2d-1).
\tag{4}
\]

故 (3) 的精确重排为

\[
\boxed{
p\bigl(4d^2-1-2dk\ell\bigr)
=2d\ell\delta_d-(2d-1).
}
\tag{5}
\]

右边为正数，所以左边系数也为正。因而

\[
\boxed{k\ell\le2d-1,\qquad1\le\ell\le2d-1,}
\tag{6}
\]

并且每个候选素数被固定三元组唯一决定：

\[
\boxed{
p=
\frac{2d\ell\delta_d-(2d-1)}
     {4d^2-1-2dk\ell}.
}
\tag{7}
\]

因此这不是对增长的 H4 endpoint 或分母的搜索。对固定 carrier \(d\)，所有
nonminimal lift 已压缩成 \(k\ell\le2d-1\) 的有限整数菜单。

## 2. 31-selector 的精确 phase screen

实际 phase 只保留 31 个 \(u\bmod119\) 类，

\[
p=912u+769,
\qquad d\mid\lvert1536-a(p)\rvert.
\tag{8}
\]

对每个 selector 仅枚举 \(\lvert1536-a\rvert\) 的奇除子；偶 \(d\) 不可能整除奇数
\(w=(p+1)/2\)。再以 (6)--(7) 计算候选 \(p\)，并逐项重放 (8)、
\(2d\mid p+1\)、\(q>1\) 与 \(A=\ell D\)。回执的 exact count 为：

| 项目 | 数量 |
|---|---:|
| selector/divisor pairs | 213 |
| odd \((u,d)\) supermenu pairs | 109 |
| \((u,d,k,\ell)\) triples | 233,378 |
| (7) 给出的整 \(p\) | 137 |
| 满足 \(p>\delta_d\) 的候选 | 89 |
| 其中素数 | 7 |
| 属于实际 phase progression 的素数 | 0 |

### 命题 1（非最小 lift 排除）

在 actual 19-phase domain 中，(2) 不可能成立。

**证明。** (3)--(7) 给出完全的有限参数化。上表的 exact screen 对每个可能
\((u,d,k,\ell)\) 重建 \(p,q,D,A\)，没有任何 phase prime 通过所有必要整除式。\(\square\)

这里的 finite screen 是必要条件的 supermenu：它没有把任一静态 \((u,d)\) 对误称为
actual H4 payload；空结果因此可以安全地排除 actual re-entry 的 nonminimal 分支。

## 3. 最小 \(D\) 分支的模 \(3\) 障碍

仍设 \(p>\delta_d\)，若不在命题 1 的分支中，则只能有

\[
D=\delta_d=2dS_d,
\qquad S_d:=4d^2-2d+1.
\tag{9}
\]

由 \(D\mid A\)，特别有 \(S_d\mid A\)。将 (4) 模 \(S_d\) 约化，得到

\[
\boxed{
2(d-1)p+(2d-1)\equiv0\pmod {S_d}.
}
\tag{10}
\]

若 \(d\equiv1\pmod3\)，则

\[
S_d\equiv0\pmod3,
\qquad2(d-1)\equiv0\pmod3,
\qquad2d-1\equiv1\pmod3,
\tag{11}
\]

与 (10) 矛盾。因此：

\[
\boxed{
p>\delta_d,\quad D=\delta_d
\Longrightarrow d\not\equiv1\pmod3.
}
\tag{12}
\]

这包含但不替代已有 original carrier \(d=1\) 的全域排除：该特例连
\(p\le\delta_1\) 的可能性也已由直接 divisor argument 关闭。

## 4. 最小分支的 17 条 phase-supermenu 射线

当 \(d\not\equiv1\pmod3\) 时，\(S_d=4d^2-2d+1\) 与
\(4d^2-1\) 互素。事实上

\[
\begin{aligned}
\bigl(4d^2-1,4d^2S_d\bigr)
&=\bigl(2(d-1),S_d\bigr)\\
&=1,
\end{aligned}
\tag{13}
\]

其中最后一步使用 \(S_d\equiv3\pmod{d-1}\) 以及 \(3\nmid(d-1)\)。因此 \(D=\delta_d\)
的整除式给出唯一的 \(p\)-残数：

\[
\boxed{
p\equiv r_d:=-\,(2d-1)(4d^2-1)^{-1}
\pmod {m_d},
\qquad m_d:=4d^2S_d.
}
\tag{14}
\]

把 (14) 与每个 19-phase progression

\[
p\equiv912u+769\pmod {108528},
\qquad u\bmod119\in\mathcal U_{31},
\tag{15}
\]

作 Chinese remainder 合并。109 个 odd \((u,d)\) supermenu pairs 中，54 个被
\(d\equiv1\pmod3\) 排除，38 个 CRT 不相容，留下精确的 17 条射线。表中 \(P_0\)
是严格大于 \(\delta_d\) 的最小正代表，所有同类候选为 \(P_0+jL\)（\(j\ge0\)）。

| \(u\) | \(a\) | \(d\) | \(\delta_d\) | \(P_0\) | \(L\) |
|---:|---:|---:|---:|---:|---:|
| 8 | 2027 | 491 | 946,002,826 | 21,825,643,340,223,073 | 25,204,943,598,881,424 |
| 15 | 431 | 17 | 38,182 | 2,037,302,065 | 2,071,908,048 |
| 15 | 431 | 65 | 2,180,230 | 7,606,503,424,129 | 7,690,020,046,800 |
| 15 | 431 | 221 | 86,155,966 | 36,836,988,351,409 | 60,777,175,407,312 |
| 19 | 583 | 953 | 6,920,554,486 | 86,864,347,723,922,785 | 357,886,731,102,773,712 |
| 26 | 317 | 53 | 1,179,886 | 311,085,986,017 | 3,393,342,696,912 |
| 27 | 127 | 1409 | 22,370,149,126 | 1,339,790,592,759,223,105 | 1,710,376,324,992,128,976 |
| 34 | 925 | 611 | 1,823,300,986 | 13,275,607,028,084,881 | 60,452,098,437,429,744 |
| 43 | 963 | 191 | 55,597,426 | 155,640,750,101,761 | 576,235,296,372,624 |
| 57 | 830 | 353 | 351,398,086 | 1,153,439,502,130,609 | 6,731,097,805,762,512 |
| 78 | 1096 | 11 | 10,186 | 2,025,421,441 | 6,080,064,144 |
| 83 | 1723 | 11 | 10,186 | 4,120,233,457 | 6,080,064,144 |
| 83 | 1723 | 17 | 38,182 | 557,367,745 | 2,071,908,048 |
| 85 | 1894 | 179 | 45,754,906 | 430,576,893,658,129 | 444,429,115,233,936 |
| 104 | 260 | 11 | 10,186 | 1,974,328,465 | 6,080,064,144 |
| 104 | 260 | 29 | 191,806 | 297,290,411,905 | 301,836,662,736 |
| 117 | 2046 | 17 | 38,182 | 853,354,609 | 2,071,908,048 |

这 17 条是 necessary supermenu rays，而不是已存在的 H4 receipts；尤其不能由表中
\(P_0\) 的 primality 或 compositeness 推断整条 progression 的可达性或不可达性。

## 5. 更新后的未关闭边界

结合命题 1 与 (12)，任何仍未由 terminal/strict macro、q-lock countdown/root-fan 或
typed/atomic guard 截获的 actual \(q_0>1\) re-entry 必须满足

\[
\boxed{
p\le\delta_d
\quad\text{或}\quad
\bigl(p>\delta_d,\ D=\delta_d,\ d\not\equiv1\pmod3\bigr).
}
\tag{16}
\]

式 (16) 是 source-provenance 的缩窄，不是全局出口：它尚未排除有限低 \(p\) 区域，
也未处理最小 \(D\) 的其余两个模 \(3\) 类，更没有自动支付 Type I action 的
terminal-first、typed、serializer、atomic 或 persistent E1--E5 合同。

## 6. 定向复现

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_q0_reentry_nonminimal_d_lift_finite_phase_exclusion.py --verify
```

回执只枚举 (6) 的固定三元组，并对 (7) 的整数候选作精确 primality 与 phase-congruence
检查；随后重建 (14)--(15) 的 17 条 CRT 射线。不扫描 prime ranges、分母、Reach graph
或 H4 predecessor history。
