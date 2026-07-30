---
kind: claim
claim_id: type-I-f-overflow-shifted-external-lift-boundary
title: 多支持较小块平方终端的移位外部源提升边界
statement: 对多支持溢出分支的 253 个去重较小块平方终端源，完整枚举移位外部源族中 q=4k-1、d=p-4k(p-n)>0 的全部 k，并对每个源的全部因子 f 检查 n/f=-1 mod q、源/目标恒等式和 Type I 除子条件；共 1410064 个 k 循环，得到 0 个合法参数和 0 个目标素数命中。该结果只排除当前移位外部源族在这批终端上的覆盖，不排除其它源族、距离或选择器。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-overflow-square-terminal-lift-boundary
  - shifted-external-source-descent
topics:
- type-I
- F-state
- overflow-radius
- block-square
- shifted-external-source
- descent
- lift
- negative-boundary
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-lift-context
visibility: public
last_checked: '2026-07-30'
---

# 多支持较小块平方终端的移位外部源提升边界

## 审计范围

对[多支持较小块平方终端的奇数距离提升边界](type-I-f-overflow-square-terminal-lift-boundary.md)中的 253 个去重终端，记源为 \(n\)、目标素数为 \(p\)，并令 \(c=p-n\)。逐个枚举

\[
1\le k\le\left\lfloor\frac{p}{4c}\right\rfloor,\qquad q=4k-1,\qquad d=p-4kc>0.
\]

对每个 \(k\) 要求 \(d\mid kn\)，然后枚举 \(n\) 的全部正因子 \(f\)，保留

\[
\frac nf\equiv-1\pmod q.
\]

对保留参数逐项验证移位外部源定理的源/目标三项恒等式、范围条件以及

\[
D=dkfr^2\mid x^2,\qquad x=kfr,\qquad r=\frac{n/f+1}{q}.
\]

因此这不是只检查一个规范 \(k\) 或一个规范因子的抽样，而是对该参数族在这 253 个保存终端上的完整有限枚举。

## 结果

```text
candidate_count: 253
k_loop_count: 1410064
parameter_count: 0
hit_prime_count: 0
```

没有一个平方终端进入当前移位外部源提升族。因而此前“状态内偶终端”到“目标素数证书”之间的缺口，在已知奇数距离和移位外部源两个参数族上都被有限地确认。

## 逻辑边界

这是一个定向的计算负边界：

1. 它完整覆盖 \(k\) 和 \(f\) 的当前有限参数化，但不覆盖其它距离、非平方尾、一般 Type I/II 证书或新的良基下降；
2. 它不说明这些源 \(n\) 没有其它 Erdős--Straus 表示；
3. 它不把状态内平方终端升级为跨状态可提升链，也不构成全称选择器。

下一步应从 \(E=\min(U,V)^2\) 的因子分解和源块颜色出发构造新的距离/源族，或证明失败的提升条件会强制产生另一种短证书。

## 复现

```bash
python3 reproductions/type_i_f_overflow_shifted_external_lift.py
```

结果文件：

`reproductions/type-i-f-overflow-shifted-external-lift-results.json`

结果文件 SHA-256：

`873acd3a8604521dd1ffc2eb79f2f36cdbf32a41e031c872fd684baa174ef625`

