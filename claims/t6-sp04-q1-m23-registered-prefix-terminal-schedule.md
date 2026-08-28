---
kind: claim
claim_id: t6-sp04-q1-m23-registered-prefix-terminal-schedule
title: SP-04 q=1 根的 M23 全除子 registered-prefix terminal schedule
statement: >-
  对满足 p≡1 (mod 4)、p 为素数且 23≤p−2 的 p，固定 B=23，逐 gap 枚举
  m=3,7,11,15,19,23 中每个
  x_m^2 的全部正除子，并按 gap、divisor、Type-I-before-Type-II 的固定顺序检查
  Bradford 两类条件，所得 schedule 有唯一最早 terminal hit；若全 miss，结论严格为
  MISS_REGISTERED_PRIORITY_COMPLETE、REGISTERED_PRIORITY_ONLY、next_unchecked_gap=27、
  global_exhaustion=false。该命题不声称自然 gap 全域穷尽、source 谱系、E1--E5、producer
  admission、Gate 4/5、F1/F2/F3、T6 或 Erdős--Straus 猜想闭合。
claim_status: established
proof_provenance: mixed
review_status: internal_review
topics:
  - T6
  - F1
  - SP-04
  - q-one
  - Bradford
  - terminal-first
  - registered-prefix
  - divisor-enumeration
  - proof-boundary
sources:
  - document: docs/standalone-proof-propositions-2026-08-28/SP-04-q1-m23-terminal-schedule.md
    role: complete mathematical proof and scope boundary
  - reproduction: reproductions/sp04_q1_m23/sp04_constructor.py
    role: factorization/exponent-product construction
  - reproduction: reproductions/sp04_q1_m23/sp04_verifier.py
    role: independent divisor-pair replay and precedence verifier
  - data: reproductions/sp04_q1_m23/verification_report.txt
    role: exact control and mutation report
  - test: tests/test_t6_sp04_q1_m23_package.py
    role: package replay, archive hash and boundary controls
visibility: public
last_checked: '2026-08-28'
---

# SP-04 q=1 根的 \(M_{23}\) 全除子 registered-prefix schedule

## 结论

固定

\[
M_{23}=\{3,7,11,15,19,23\},\qquad x_m=(p+m)/4.
\]

对每个 \(m\) 的 \(x_m^2\) 枚举全部正除子 \(d\)，检查

\[
\mathcal I_m(p)=\{d:d\mid x_m^2,\ m\mid px_m+d\},
\]

\[
\mathcal{II}_m(p)=\{d:d\mid x_m^2,\ d\le x_m,\ m\mid x_m+d\}.
\]

Type-I/II 命中分别按标准重建式给出三项分母，并用精确交叉乘法验证
\(4xyz=p(yz+xz+xy)\)。有限字典序
\((m,d,\mathrm I)<(m,d,\mathrm{II})\) 保证唯一 earliest hit；全 miss 只表示六个
registered gaps 的两类集合均为空。

## 独立重放与控制

constructor 以完整因子分解和指数笛卡尔积生成除子；independent verifier 不导入
constructor，而逐个扫描 \(1\le k\le x_m\)，用互补除子重建 \(x_m^2\) 的完整 divisor
lattice。两份 transcript 逐行一致（831 rows），素性 transcript 逐行一致（884 rows）。

精确 earliest controls 为：

| \(p\) | earliest |
|---:|---|
| 73 | \((m,d,\tau)=(7,1,\mathrm{II})\) |
| 241441 | \((11,27,\mathrm{II})\) |
| 2689 | \((15,26,\mathrm I)\) |
| 12721 | \((19,7,\mathrm{II})\) |
| 1201 | \((23,34,\mathrm I)\) |
| 2521 | \((23,8,\mathrm{II})\) |
| 21169 | six-gap MISS |

\(p=21169\) 的 gap 31、\(d=1\) Type-II 证书

\[
\frac4{21169}
=\frac1{5300}+\frac1{3619899}+\frac1{19185464700}
\]

证明六层 miss 不能升级为 terminal-universe miss。

## 权限和项目边界

该 claim 只关闭 registered-prefix schedule 的数学覆盖与独立复现。证据包的 source
binding 是 p-only control payload，不是实际递归 source lineage；没有授予
MISS_COMPLETE、generic E1、producer、E2--E5、common admission、queue、re-entry 或
任何 F1/F2/F3/T6 权限。legacy production terminal registry 仍保持
complete_schedules=0，当前 Gate 4/5、F1、F2、F3 和 T6 状态不变。
