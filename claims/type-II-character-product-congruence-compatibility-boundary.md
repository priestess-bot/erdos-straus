---
kind: claim
claim_id: type-II-character-product-congruence-compatibility-boundary
title: Type II 多射线字符积同余的兼容性边界
statement: 对任意有限条 Type II AC 射线及每条射线任意指定的字符核或单位群子群 H_j，所有只保留总积条件 p mod 4A_jC_j belongs to H_j 的推理均不能推出矛盾：p=1 mod lcm(24,{4A_jC_j}) 同时满足所有条件，且 Dirichlet 定理给出无穷多个这样的核心素数。因此跨射线推进必须使用移位数 p+4A_j^2C_j 的实际素因子分布或其他非乘积信息。
claim_status: established
topics:
- type-II
- higher-order-characters
- congruence
- Dirichlet-theorem
- obstruction
- proof-program
sources:
- paper: linnik1944
  locator: least-prime theorem in arithmetic progressions
  role: arithmetic-progression-prime-existence-context
- paper: chamberland2026
  locator: "Theorem 1"
  role: Type-II-application-context
visibility: public
last_checked: '2026-07-24'
---

# Type II 多射线字符积同余的兼容性边界

## 定理

取任意有限射线集

\[
\mathcal S=\{(A_j,C_j):1\le j\le L\},\qquad M_j=4A_jC_j.
\]

对每个 \(j\)，任取单位群的子群 \(H_j\le U(M_j)\)，特别可以取任意二幂字符的核。
则总积同余条件

\[
p\bmod M_j\in H_j\qquad(1\le j\le L) \tag{1}
\]

有无穷多个核心素数解。

## 证明

令

\[
Q=\operatorname{lcm}(24,M_1,\ldots,M_L).
\]

每个子群 \(H_j\) 都含单位元，所以任意

\[
p\equiv1\pmod Q \tag{2}
\]

都满足 (1)，并且满足 \(p\equiv1\pmod{24}\)。因 \(\gcd(1,Q)=1\)，Dirichlet
算术级数定理给出无穷多个素数满足 (2)。

当一个 Type II 射线的素因子残数子群 \(K_j\) 包含在某个字符核 \(H_j\) 时，
\(N_j=p+4A_j^2C_j\equiv p\pmod{M_j}\) 的全因子积给出恰是 (1)。所以所有
\(\chi_j(p)=1\) 的结论也由同一个 \(p\equiv1\pmod Q\) 同时满足。

## 含义和严格限制

这不构造同时失败所有射线的素数：条件 (1) 遗忘了每个移位数
\(p+4A_j^2C_j\) 的**各个**素因子必须落在指定核内这一更强事实。
定理只证明，若论证最终只剩各移位数的总积或字符值，就不可能由有限条射线得出矛盾。

因此 type-II-two-power-character-depth-sieve 的高阶字符层必须与移位因子分布、
不同移位的公共素因子排斥、或新的证书/递降选择器结合；不能仅把
\(\chi_j(p)=1\) 的有限合取再作同余拼接。
