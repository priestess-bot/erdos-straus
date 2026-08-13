---
kind: claim
claim_id: type-I-root-capacity-stutter-provenance-dispatch
title: 根容量 stutter 范数因子的 provenance 三分派
statement: >-
  对 proper-root stutter 的范数 N=a^2-a(e-1)+(e-1)^2，任取 q|N。若 q|h 且
  q!=3，则 q|u（h=3u），无论 q|a,b 是否成立，都可使用根容量 q-source 的有限
  external-source 菜单；菜单命中给出显式 Type I 证书。若 q=3，则 q 不整除 u，
  是 h-支撑的唯一容量例外。若 q 不整除 h，则该因子没有被根容量强制的 source
  provenance；范数关系本身不保证一般 external-source 菜单非空。退化条件
  q|h、q|a 还严格推出 q|b 和 q|m，但不撤销 q 的容量菜单资格。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-eisenstein-support
  - type-I-root-capacity-prime-external-terminal-coupling
  - external-source-type-I-certificate
topics:
  - type-I
  - root-capacity
  - stutter
  - provenance
  - external-source
  - degenerate-factor
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-eisenstein-support
    role: norm-support-and-linear-degeneracy
  - claim: type-I-root-capacity-prime-external-terminal-coupling
    role: capacity-q-menu-and-certificate
  - claim: external-source-type-I-certificate
    role: generic-source-certificate-equivalence
  - reproduction: reproductions/type_i_root_capacity_stutter_provenance_dispatch.py
    role: focused-dispatch-controls
visibility: public
last_checked: '2026-08-14'
---

# 根容量 stutter 范数因子的 provenance 三分派

## 设置

沿用 proper-root stutter 记号

\[
M_0=\frac{p^2+p+1}{3},\qquad
u=(2r+1,M_0),\qquad h=3u,
\]

\[
b=e-1,\qquad a=em-h,\qquad N=a^2-ab+b^2,
\qquad h\mid N.
\]

Eisenstein 支撑引理给出：(q\mid N) 时，(q=3) 或 (q\equiv1\pmod3)。
本卡只处理这些素因子的来源类型，不声称菜单必命中。

## (h)-支撑因子的来源资格

设 (q\mid h) 且 (q\ne3)。因为 (M_0\equiv1\pmod3)，有
((u,3)=1)，从 (h=3u) 立即得到 (q\mid u)。因此根容量定理直接给出

\[
\rho=\langle p\rangle_q,\qquad i=q-\rho,
\]

以及有限菜单

\[
\mathcal T_{p,q}=\left\{t\mid\frac{p+i}{q}:
 t\equiv-pq^{-1}\pmod{4i}\right\}.
\]

任意 (t\in\mathcal T_{p,q}) 令 (m_*=qt)、(x=(p+m_*)/4)、(d=ix)，
便有 (d\mid x^2) 和 (m_*\mid px+d)，即显式 Type I 证书；Type I 不要求
(d\le x)。
这个推理只使用 (q\mid u)，不使用 (q\nmid a)。

### 退化子引理

若另外 (q\mid a)，则 (q\mid b) 和 (q\mid m)。事实上，
(N\equiv b^2\pmod q) 先给出 (q\mid b)；而 (a=em-h)、
(e=b+1\equiv1\pmod q)、(q\mid h) 再给出 (q\mid m)。这只说明 stutter
曲线在 q 处有共同因子，不能否定上面的容量来源菜单。非退化情况下 (q\nmid a)，
才可从 (pa\equiv-b\pmod q) 独立恢复同一个 p-余数；这是额外的范数桥，而不是
菜单的前提。

## 两个没有强制容量来源的类型

若 (q=3)，则 (3\nmid u)，因为 (M_0\equiv1\pmod3)。所以 3 可以出现在
(N) 或 (N/h) 中，却不是根容量 q-source 因子。

若 (q\nmid h)，则 q 不是当前根容量的支撑因子。此时范数关系不再把 q 识别为
(u) 的因子，因而没有被根容量强制的 source provenance；仍可用一般 external-source
条件独立搜索证书，但不能把这种搜索说成根容量分流的必然出口。若 q 同时整除 h
和 N/h，它仍属于第一类 h-支撑因子，不能按 quotient-only 处理。

## 对全局出口的含义

这次修正删除了一个过强的分支判断：退化 h-因子并不需要另造来源适配器，
它们已经属于现有 q-menu 的输入域。真正剩下的局部问题是：

1. 对每个 (q\mid h, q\ne3)，证明菜单命中，或给出菜单为空时的合法 Type I/II
   证书或可提升递降；
2. 处理 q=3 与 quotient-only 范数因子；
3. 把菜单命中接入 actual receipt 的 terminal-first、source path 和全局严格势。

因此本卡收紧了 global-exit 的类型接口，但没有声称完成全称“短证书或递降”引理。

## 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_stutter_provenance_dispatch.py --verify
```

脚本使用两个根容量菜单的正负控制、一个 q=3 退化曲线控制和一个非退化/商因子
曲线控制；抽象 stutter 元组不被宣称为 actual receipt。
