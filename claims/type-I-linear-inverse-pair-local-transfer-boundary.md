---
kind: claim
claim_id: type-I-linear-inverse-pair-local-transfer-boundary
title: 逆元对 F 状态的已知源内因子转移边界
statement: 在七个完整线性谱中唯一两个非空的“素模数、两一次仿射因子且互为逆元”F 方向上，仿射块 L=aR+1 的任意非平凡因子都不满足已知固定 s 或变 s 源转移条件；在完整源状态图中枚举这些转移及合法坐标交换的前向闭包，(p,R)=(64214329,359) 只含根状态，(105295129,839) 只含7个状态，二者均未到达现有 B=1 目标模数。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- linear-source
- finite-exponent
- inverse-pair
- source-transfer
- local-closure
- negative-boundary
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-29'
---

# 逆元对 F 状态的已知源内因子转移边界

## 审计对象

线性源写成

\[
p=a+s+asR,\qquad L=aR+1,
\]

并令

\[
E=sR+1,\qquad K=\frac{pR+1}{4}.
\]

七谱中只有两条非空方向同时满足：(R) 为素数、(L) 有两个一次素因子、且这两个因子
互为模 (R) 的逆元。它们正是循环对数盒判据中的两条压力方向：

| (p) | (R) | ((a,s)) | (L) 的分解 | 现有目标 (R) |
| ---: | ---: | ---: | ---: | --- |
| 64,214,329 | 359 | (7154,25) | (19\cdot135173) | 19, 43, 119, 131 |
| 105,295,129 | 839 | (2,62713) | (23\cdot73) | 15, 35, 119, 143 |

## 仿射块因子不能直接进入已知转移

固定 (s) 转移要求一个非平凡因子 (dmid a)、(d\equiv1\pmod s)；变 (s) 转移要求

\[
d\mid s,\qquad d\equiv1\pmod a,
\]

然后分别把 (d) 从 (a) 或 (s) 移入 (L) 的线性表达式。审计对 (L) 的**所有**非平凡
因子逐项测试这些条件，而非只测试两个素因子。

两行都满足

\[
\gcd(a,L)=1,\qquad \gcd(s,L)=1,
\]

所以 (L) 的任意非平凡因子既不可能整除 (a)，也不可能整除 (s)。脚本还逐项验证了
模同余条件；两类可转移因子计数均为零。这说明长循环对数溢出不是把当前仿射块因子
直接“搬回”源坐标即可消除的。

## 完整源图的前向闭包

用完整线性源枚举器恢复每个 (p) 的所有有向状态，再加入三类已验证边：

1. 固定 (s)：(q\mid a, q\equiv1\pmod s)；
2. 变 (s)：(q\mid s, q\equiv1\pmod a)，并要求新 (R\equiv3\pmod4)；
3. 当 (a,s) 都为奇数时的坐标交换 ((a,s,R)\leftrightarrow(s,a,R))。

结果为：

| (p,R) | 完整状态数 | 根的出边 | 前向闭包状态数 | 闭包命中目标数 |
| --- | ---: | ---: | ---: | ---: |
| 64,214,329; 359 | 80 | 0 | 1 | 0 |
| 105,295,129; 839 | 95 | 5 | 7 | 0 |

第二行的五条根出边来自 (s=62713) 的因子，随后合流到

\[
(2,1,52647563)\longrightarrow(1,1,105295127).
\]

这条局部闭包仍没有进入已有目标模数集合。第一行甚至没有可用的前向边。

## 结论边界

该结果是两个具体 F 状态上的有限、可复核负边界：

- “仿射块因子属于某个模源的生成子群”不能推出已知源内转移可修复；
- “沿固定 (s)/变 (s) 因子转移反复重选”在这两条逆元对压力方向上没有产生目标证书；
- 它不否定 Erdős--Straus 猜想，也不排除新的 (R) 构造、一般 (B) 证书、Type II 证书或真正的
  严格递降。

因此下一步必须引入超出这三类局部边的机制：控制新的源模数、把长循环对数转成可验证的
正规形，或直接构造普通 Type II 证书。

## 复现

```bash
python3 reproductions/type_i_linear_inverse_pair_local_transfer_boundary.py
python3 -m unittest tests.test_type_i_linear_inverse_pair_local_transfer_boundary -q
```

结果文件：
[type-i-linear-inverse-pair-local-transfer-boundary-results.json](../reproductions/type-i-linear-inverse-pair-local-transfer-boundary-results.json)
