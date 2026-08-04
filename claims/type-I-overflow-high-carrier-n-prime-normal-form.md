---
kind: claim
claim_id: type-I-overflow-high-carrier-n-prime-normal-form
title: 高载体 n=p overflow 的唯一 d=1 G-anchor 正规形
statement: 对核心素数 p=1 (mod 24)，若 verified overflow 满足 p*n=4*M*d+1、R_M=4*M-n>p、M>B_p=(p-1)^2/4 且 n=p，则 d=1、M=(p^2-1)/4。写 r=(p-1)/4，则唯一对偶规范图表为 (R_r,K_r)=(p-2,B_p)，其 anchor 超额块固定为 Q=(p-3)/2、beta=2。该分支被精确压到 G-anchor 分流，不自动给出保持旧支撑的递归边。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-high-carrier-p-plus-four-complement
  - type-I-overflow-d-one-p-minus-two-g-rechart
  - type-I-universal-p-source-capacity-anchor-orbit
topics:
- type-I
- overflow
- high-carrier
- n-equals-p
- d-one
- G-state
- anchor
- exact-normal-form
- proof-boundary
sources:
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: exact n=p normal-form classifier and verifier
  - result: reproductions/type-i-representation-dual-capacity-selector-results.json
    role: selector receipt
visibility: public
last_checked: '2026-08-04'
---

# 高载体 n=p overflow 的唯一 d=1 G-anchor 正规形

## 唯一算术形态

由 n=p 得

    M*d = (p^2-1)/4.

因为 p>3，

    (p^2-1)/4 < 2*((p-1)^2/4).

而 M>B_p，所以 d<2；正整数条件强制 d=1，并且

    M=(p^2-1)/4.

写 r=(p-1)/4。则 M=r*(p+1)、M mod p=r，规范对偶图表是

    R_r=p-2,    K_r=(p-1)^2/4=4*r^2.

并且

    R_r-1=p-3=2*Q,    Q=(p-3)/2,    gcd(Q,K_r)=1.

所以完整 G-anchor 超额块固定为 Q，beta=2。通用 p-source

    (U,V,m)=(p,(p-2)*(p-1)-p,p-1)

经 shift=1 到达 (1,p-3,1)=(1,Q*beta,1)。这是 source/path provenance 和规范化，
不是 E1--E5 递归边：G 图表的支撑内目标纤维为空，且 Q 通常不包含旧 charged support。

## 选择器边界

该分支应同时进入：

1. p+4 Type II 分流；有 3 (mod 4) 素因子时直接终端；
2. G-anchor 的 Q=(p-3)/2 complete-excess 分流；
3. 非支撑 Type I/II、跨状态容量或其它良基 support reset。

无 source provenance 的算术边界例子：

    (p,M,d,n)=(97,2352,1,97), (R_r,K_r)=(95,2304), Q=47.

这里 p+4=101 没有 3 (mod 4) 素因子，因此只是 G-anchor hard core，不是猜想反例。

复现：

    python3 reproductions/type_i_representation_dual_capacity_selector.py --verify
