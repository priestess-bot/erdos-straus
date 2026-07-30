---
kind: claim
claim_id: type-I-short-relation-even-terminal
title: 短关系导致偶终端引理
statement: >-
  设 K=product_i q_i^{nu_i}、4K=1 mod R 且 R 为正奇数。若乘法核关系格 Lambda 含有非零
  lambda，满足 product_i q_i^{lambda_i}=1 mod R 且 |lambda_i|<=nu_i，则可定向 lambda
  使 rho=product_i q_i^{lambda_i}<1；此时 E=4K rho 是正的偶终端除子，满足 E|4K^2、
  E=1 mod R、E<=4K-4R，并给出 n=(4K-E)/R，且 n 为正的 4 的倍数、n<p（当
  4K=pR+1）。Verifier 在冻结的 291 个分色未解析 F 状态中均找到这样的关系并验证全部
  终端条件。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- F-state
- relation-lattice
- short-relation
- even-terminal
- finite-exponent
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-terminal-selector-context
visibility: public
last_checked: '2026-07-30'
depends_on:
  - type-I-target-divisor-even-terminal-selector
  - type-I-f-split-color-relation-certificate
---

# 短关系导致偶终端引理

## 设置

设 \(R\) 为正奇数，\(4K=pR+1\)，并写

\[
K=\prod_{i=1}^{r}q_i^{\nu_i}.
\]

令

\[
\Lambda=
\left\{\lambda\in\mathbb Z^r:
\prod_iq_i^{\lambda_i}\equiv1\pmod R\right\}
\]

为乘法核关系格。由于 \(4K\equiv1\pmod R\)，每个 \(q_i\) 都与 \(R\) 互素，故负指数在
模 \(R\) 的单位群中有意义。

## 引理

若存在非零 \(\lambda\in\Lambda\) 满足

\[
|\lambda_i|\le\nu_i\qquad(1\le i\le r),
\]

则存在一个合法偶终端 \(E\)，具体为

\[
\rho=\prod_iq_i^{\lambda_i}<1,
\qquad
U=K\rho,
\qquad
E=4U,
\qquad
n=\frac{4K-E}{R}.
\]

它满足

\[
E\mid4K^2,
\qquad
E\equiv1\pmod R,
\qquad
0<E\le4K-4R,
\qquad
0<n<p,
\qquad
4\mid n.
\]

## 证明

非零关系的有理数比值不可能等于 \(1\)，否则唯一分解会给出所有坐标为零。因此在
\(\lambda\) 与 \(-\lambda\) 中选取一个，使 \(\rho<1\)。反向取关系不改变坐标界。

由于 \(|\lambda_i|\le\nu_i\)，有

\[
U=\prod_iq_i^{\nu_i+\lambda_i},
\qquad
0\le\nu_i+\lambda_i\le2\nu_i.
\]

所以 \(U\) 是正整数且 \(U\mid K^2\)，从而 \(E=4U\mid4K^2\)。关系
\(\lambda\in\Lambda\) 给出 \(\rho\equiv1\pmod R\)，因此

\[
U\equiv K\pmod R,
\qquad
E=4U\equiv4K\equiv1\pmod R.
\]

又 \(U<K\)，且 \(K-U\) 是正的 \(R\) 的倍数，所以 \(K-U\ge R\)。于是

\[
E=4U\le4K-4R,
\qquad
n=\frac{4(K-U)}R
\]

是正的 \(4\) 的倍数。最后

\[
n<\frac{4K}{R}=p+\frac1R.
\]

由于 \(n\) 为整数，先得 \(n\le p\)；而 \(p\) 为奇素数、\(n\) 被 \(4\) 整除，故
\(n\ne p\)，从而 \(n<p\)。证毕。

## 冻结审计

复现脚本对完整 Fourier 输入和分色容量输入做哈希锁定，并在 291 个分色未解析 F 状态中
穷举原始指数盒内的非零核关系。每个状态均通过上述精确算术检查：

```text
record_count: 291
terminal_count: 291
relation ||lambda||_infinity: 1 -> 220, 2 -> 60, 3 -> 8, 4 -> 3
maximum ||lambda||_1: 9
```

运行：

```text
python3 reproductions/type_i_short_relation_even_terminal.py
```

结果文件：

```text
reproductions/type-i-short-relation-even-terminal-results.json
```

## 逻辑边界

这是一个状态内终端引理。它不提供目标平方除子 \(e\)，因此不能单独完成一般 Type I
选择器；它说明在目标纤维难以直接使用时，原始关系格中的短核关系本身也能产生偶终端。
冻结审计只覆盖 291 个状态，不是对所有核心素数存在短关系的全称证明，也不构成跨状态
容量矛盾或算术递降定理。
