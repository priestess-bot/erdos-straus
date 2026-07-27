---
kind: claim
claim_id: type-II-support-critical-congruence-trap
title: Type II 支撑临界失败强制目标素数同余一
statement: 对固定 Type II AC 射线，若移位整数 N=p+4A^2C 的全部除子模 4AC 的残数恰为其素因子残数生成子群去掉 -1，则 p=1 mod 4AC；若有限多条射线同时满足该一孔支撑临界条件，则 p=1 mod 这些模数的最小公倍数。
claim_status: established
topics:
- type-II
- divisor-residues
- subgroup-structure
- critical-sequence
- congruence
- proof-program
sources:
- paper: grynkiewicz_marchan_ordaz2009
  locator: "subsequence-product framework; Theorem C"
  role: structural-context
- paper: chamberland2026
  locator: "Theorem 1"
  role: Type-II-application-context
visibility: public
last_checked: '2026-07-24'
---

# Type II 支撑临界失败强制目标素数同余一

## 定理

固定正整数 \(A,C\)，令

\[
M=4AC,\qquad N=p+4A^2C=p+AM,
\]

其中 \(\gcd(p,M)=1\)。把 \(N\) 的素因子按重数取模 \(M\)，得到单位群
\(U(M)\) 中的序列 \(S\)；记所有子序列乘积的集合为 \(\Pi(S)\)，记
\(K=\langle S\rangle\le U(M)\)。若

\[
\Pi(S)=K\setminus\{-1\}, \tag{1}
\]

则

\[
p\equiv1\pmod {4AC}. \tag{2}
\]

因此若有限多条 \(AC\) 射线都发生 (1)，则

\[
p\equiv1\pmod{\operatorname{lcm}_{(A,C)}(4AC)}. \tag{3}
\]

## 证明

令 \(P\) 为 \(S\) 全部项的乘积。它正是 \(N\bmod M\)。对任意子序列乘积
\(x\in\Pi(S)\)，取补子序列会给出

\[
x\longmapsto Px^{-1}. \tag{4}
\]

这是 \(\Pi(S)\) 上的双射，也是在 \(K\) 上的双射。因此它保持
\(K\setminus\Pi(S)\)。由 (1)，唯一缺失元素 \(-1\) 必为 (4) 的不动点：

\[
P(-1)^{-1}=-1,
\]

从而 \(P=1\)。所以 \(N\equiv1\pmod M\)。又 \(N\equiv p\pmod M\)，即得 (2)；
(3) 由中国剩余定理的最小公倍数表述立即得到。

## 意义和精确边界

这是对一类真正失败射线的确定性排除，而非密度估计。对固定有限射线集，(3) 还把
此型残余包含在一个固定算术级数中；素数定理的算术级数形式给出
\(O(X/(\varphi(Q)\log X))\)，其中 \(Q\) 是 (3) 的模数。

条件 (1) 不能删除。当 \(\lvert K\setminus\Pi(S)\rvert\ge2\) 时，补集只在
\(x\mapsto Px^{-1}\) 下封闭，通常不迫使 \(P=1\)。已有的 Kneser 临界序列边界
也表明，不能把所有失败统一压缩成这个一孔主型或真子群加次线性异常。

该主型并非空的：在 \(p=1489\)、\((A,C)=(2,2)\) 时，
\(M=16\)、\(N=1521=3^2 13^2\)，且
\(\Pi(S)=U(16)\setminus\{15\}\)。复现脚本在
\(p\le10^4\)、\(A,C\le5\) 的精确审计中找到 2,909 条失败射线，其中 5 条属于
此主型，全部满足 (2)。

## 复现

运行 python3 reproductions/divisor_residue_structure.py --audit-limit 10000 --ac-bound 5。

相应单元测试固定审计总数、首个例子和零反例。有限审计只核验实现，不替代上面的证明。
