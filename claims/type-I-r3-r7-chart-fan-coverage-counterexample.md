---
kind: claim
claim_id: type-i-r3-r7-chart-fan-coverage-counterexample
title: 核心素数 p=241 的 R=3/7 Type-I 图表扇区不足反例
statement: 对核心素数 p=241，完整枚举 R=3 与 R=7 的有限目标指数纤维都不含 -1；因此固定有限 Type-I 图表扇区不能单独覆盖核心状态。该缺口由同一 p 的直接 Type-II 正规形 (A,C,K,B,h)=(1,1,2,69,7) 填补：h=4ACK-1、h | p+4A^2C、h | Kp+A 且 B>A。该反例证明全局选择器必须保留 Type-I 空纤维到 Type-II admission 的跨路线边，而不能把 R=3/7 的 Fourier/容量缺口当作递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-target-fiber-neighbor-terminal
  - type-I-fg-role-snf-terminal-dispatch
  - type-II-hall-fiber-arithmetic-closure-trichotomy
  - type-II-owner-exact-flow-negative-certificate-relay
topics:
  - type-I
  - type-II
  - chart-fan
  - target-fiber
  - coverage
  - strict-counterexample
  - arithmetic-certificate
  - proof-program
sources:
  - claim: type-I-target-fiber-neighbor-terminal
    role: exact-finite-target-fiber-definition
  - claim: type-II-hall-fiber-arithmetic-closure-trichotomy
    role: Type-II-normal-form-check
  - reproduction: reproductions/type_i_r3_r7_chart_fan_coverage_counterexample.py
    role: p241-empty-fibers-and-Type-II-rescue
visibility: public
last_checked: '2026-08-09'
---

# 核心素数 p=241 的 R=3/7 Type-I 图表扇区不足反例

## 1. 两个完整目标纤维

取 p=241，p ≡ 1 (mod 24)。

### R=3

K_3=(3p+1)/4=181.

181 是素数且 181 ≡ 1 (mod 3)。因此指数盒只有 z in {-1,0,1}，所有允许的
残数都是 181^z ≡ 1 (mod 3)，而目标 -1 ≡ 2 (mod 3) 不出现。这里目标纤维
不是被截断搜索漏掉，而是完整有限盒中的空集。

### R=7

K_7=(7p+1)/4=422=2*211.

在指数盒 z_1,z_2 in {-1,0,1} 中，2^{z_1}211^{z_2} ≡ 2^{z_1} (mod 7)，
因为 211 ≡ 1 (mod 7)。可得残数集合 {1,2,4}，不含 -1 ≡ 6 (mod 7)。
所以 R=7 的完整目标纤维也为空。

这给出严格的图表扇区负证书：

    Z^-_(3,K_3) = empty,     Z^-_(7,K_7) = empty.

## 2. Type-II 交叉路线的直接补偿

取 Type-II 正规形参数

    (A,C,K,B,h) = (1,1,2,69,7).

逐项检查：

    h = 4*A*C*K - 1 = 7,
    p + 4*A^2*C = 241 + 4 = 245 = 35*7,
    K*p + A = 2*241 + 1 = 483 = 69*7,
    B = 69 > A.

所以这是一个直接 Type-II 短证书，而非从两个空 Type-I 纤维拼出的伪容量。

## 3. 选择器含义

该反例强制以下路由顺序：

1. 对每个固定 R 先完整枚举目标指数纤维；空集要保留 exact empty receipt；
2. 不能把不同 R 的空纤维合并为一个 Fourier/流缺口，也不能由空纤维推出递降；
3. 空纤维必须把控制权交给 Type-II source universe/admission 菜单，或交给另一条
   Type-I 图表；
4. 只有 Type-II 的来源合同、物理 q 流和 E1--E5 通过后，才可登记短证书或严格
   可提升递降。

## 4. 证明

式 (1) 直接来自两个有限指数盒的逐项残数枚举；负指数在单位群中取逆，不会产生
新的残数。式 (3) 验证 Type-II 正规形的因子、整除和大小条件，故给出直接证书。
因此 R=3,7 的 Type-I 空纤维与 Type-II 命中可以同时存在，固定这两个图表扇区的
全称覆盖命题为假。证毕。

## 研究边界

该反例不否定 Type-I/Type-II 统一选择器；它否定的是“有限几个固定 Type-I 图表
空纤维可以自动代表所有核心状态”的简化假设。下一步必须证明图表扇区到 Type-II
source admission 的完备跨路线覆盖，或给出一个由空纤维直接产生的可提升后继；空纤维
本身不是容量单位，也不是递降证明。
