---
kind: claim
claim_id: type-II-small-shared-gap-explicit-fan
title: 缺口 3、7、11 的显式共享因子 Type II 扇
statement: 对每个核心素数 p>=73，缺口 m=3、7、11 分别自动具有共享因子 D=4、8、12。若 x_3=(p+3)/4 含有 2 mod3 素因子，或 p=3,5,6 mod7，或 p=7,8,10 mod11，则相应缺口另有显式 Type II 除子，因而共享除子残数选择器成立。三个分支都不命中时，必有 x_3 的全部素因子为 1 mod3、p=1,2,4 mod7，且 p=1,2,3,4,5,6,9 mod11。
claim_status: established
topics:
- type-II
- shared-divisor
- congruences
- small-gap
- factor-selection
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--2
  role: certificate-reconstruction
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-24'
---

# 缺口 \(3,7,11\) 的显式共享因子 Type II 扇

## 定理

令 \(p\equiv1\pmod {24}\) 为素数，\(p\ge73\)。下表中的每一行都给出
共享因子 \(D\mid p+m\)、\(D\equiv1\pmod m\)，以及一张 Type II 除子证书。

\[
\begin{array}{c|c|c|c}
\text{触发条件}&m&D&d\mid x^2,\ d\equiv-x\pmod m\\
\hline
x_3=(p+3)/4\text{ 有 }q\equiv2\pmod3&3&4&q\\
p\equiv3\pmod7&7&8&1\\
p\equiv5\pmod7&7&8&4\\
p\equiv6\pmod7&7&8&2\\
p\equiv7\pmod{11}&11&12&1\\
p\equiv8\pmod{11}&11&12&9\\
p\equiv10\pmod{11}&11&12&3
\end{array} \tag{1}
\]

所以只要 (1) 的任意一项成立，`type-II-shared-residue-selector-conjecture`
就在该素数上成立。

## 证明

先验证共享条件。写 \(p=24t+1\)。则

\[
\begin{array}{c|c|c}
m&p+m&\text{共享因子}\\
\hline
3&4(6t+1)&4\equiv1\pmod3\\
7&8(3t+1)&8\equiv1\pmod7\\
11&12(2t+1)&12\equiv1\pmod{11}.
\end{array} \tag{2}
\]

故每个缺口的共享因子条件都无条件满足；只需检查 Type II 目标。

对 \(m=3\)，有 \(x_3\equiv1\pmod3\)。若 \(q\mid x_3\) 且
\(q\equiv2\pmod3\)，则 \(d=q\mid x_3^2\)、\(d\le x_3\) 并且
\(d\equiv-x_3\pmod3\)。

对 \(m=7\)，

\[
x_7=\frac{p+7}{4}\equiv2p\pmod7,
\]

而 \(x_7=2(3t+1)\) 为偶数，故 \(2,4\mid x_7^2\)。逐项代入
\(p\equiv3,5,6\pmod7\)，分别得到

\[
-x_7\equiv1,4,2\pmod7.
\]

对 \(m=11\)，

\[
x_{11}=\frac{p+11}{4}=3(2t+1),\qquad x_{11}\equiv3p\pmod{11}.
\]

所以 \(1,3,9\mid x_{11}^2\)。当 \(p\equiv7,8,10\pmod {11}\) 时，

\[
-x_{11}\equiv1,9,3\pmod {11},
\]

恰给出表中的三项。所有列出的 \(d\) 都不超过相应 \(x\)，故都是合法 Type II
证书。

反过来，三个**显式**分支都不触发当且仅当

\[
\begin{aligned}
&\text{所有 }q\mid x_3\text{ 都满足 }q\equiv1\pmod3,\\
&p\equiv1,2,4\pmod7,\\
&p\equiv1,2,3,4,5,6,9\pmod {11}. \tag{3}
\end{aligned}
\]

这里 (3) 是这个显式扇的残余条件，不是三个缺口完整选择器的失败判据：
\(m=7,11\) 的非平凡除子仍可额外命中。

## 精确审计

```bash
python3 reproductions/type_ii_small_shared_gap_fan.py --limit 10000000
```

对 \(p\le10^7\) 的 \(82{,}887\) 个核心素数，表 (1) 的先后扇分别覆盖

\[
47{,}137,\quad17{,}731,\quad4{,}037
\]

个，合计 \(68{,}905\) 个，即 \(83.1313\%\)。剩余 \(13{,}982\) 个只表示
没有触发表 (1)，不表示原选择器失败。相比之下，允许 \(m=7,11\) 的一般除子后，
前三缺口的实际选择器覆盖率为 \(96.7124\%\)，见
`type-II-shared-divisor-fan-audit`。

## 下一步

该定理把跨缺口研究的第一个真残余压缩为 (3)。下一步不是尝试把 (3) 误称为矛盾，
而是分类其在 \(m=7,11\) 上由非平凡因子产生的额外命中，并研究这种因子模式能否与
后续缺口 \(15,19,\ldots\) 的失败同时长期维持。

第一层这种分类已由 `type-II-small-shared-gap-single-prime-fan` 完成：允许一个
指定残数素因子后，显式覆盖提高到 \(92.2000\%\)。剩余差额需要真正的多素因子乘积
分析，而不能再化约为单个素因子是否出现。
