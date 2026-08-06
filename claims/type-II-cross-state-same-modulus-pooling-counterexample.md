---
kind: claim
claim_id: type-II-cross-state-same-modulus-pooling-counterexample
title: Type II 同模数跨状态积集池化的严格反例
statement: 即使两条 Type II 规范射线使用同一模数 M，不同移位的除子残数积集也不能直接合并。具体地，核心素数 p=97、M=24 的两条射线 s=6=1^2*6 与 s=18=3^2*2 分别有 N_1=p+4s=121、N_2=p+4s=169，完整除子残数集分别为 {1,11} 与 {1,13}，二者都不含 -1=23 mod24；但跨状态混乘 11*13=23 mod24。该混合命中不对应任何单条射线的 Type II 证书，因此直接把同模数状态的 Kneser 积集池化会产生伪证书。只有额外证明 source-switch、标记解提升或共同整数因子来源后，跨状态容量才可使用。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-qadic-height-kneser-block-bridge
  - type-II-shared-selector-kneser-target-fiber-terminal
topics:
- type-II
- cross-state
- same-modulus
- product-set
- Kneser
- counterexample
- source-switch
- proof-program
sources:
  - claim: type-II-qadic-height-kneser-block-bridge
    role: single-state-block-boundary
  - claim: type-II-shared-selector-kneser-target-fiber-terminal
    role: target-residue-criterion
visibility: public
last_checked: '2026-08-04'
---

# Type II 同模数跨状态积集池化的严格反例

## 反例数据

取核心素数

\[
p=97\equiv1\pmod{24},
\qquad M=24.
\]

同一 \(M=4ac\) 下有两条合法平方自由规范射线：

\[
\begin{array}{c|c|c|c}
s&a&c&N=p+4s=p+aM\\ \hline
6&1&6&121=11^2\\
18&3&2&169=13^2
\end{array}
\]

这里 \(6\) 和 \(2\) 都是平方自由，且分别满足
\(s=a^2c\)。因为 \(M<p\)，两条 \(N\) 都与 \(M\) 互素。

## 各状态都失败

第一条射线的全部除子为 \(1,11,121\)，所以

\[
\Pi_{24}(121)=\{1,11\}.
\]

第二条射线的全部除子为 \(1,13,169\)，所以

\[
\Pi_{24}(169)=\{1,13\}.
\]

目标残数为

\[
-1\equiv23\pmod{24}.
\]

因此

\[
23\notin\Pi_{24}(121),
\qquad
23\notin\Pi_{24}(169).
\]

按规范 Type II 射线的残数判据，两条射线各自都没有直接 Type II 命中。

## 跨状态伪命中

但若把两个状态的积集直接池化，则

\[
11\cdot13=143\equiv23\pmod{24}.
\]

于是

\[
-1\in\Pi_{24}(121)\Pi_{24}(169),
\]

尽管 \(-1\) 不在任一单状态积集内。这个乘积使用了 \(11\mid N_1\) 和
\(13\mid N_2\) 两个不同整数的因子，不能重建为一个 \(h\mid N_i\) 且
\(h\equiv-1\pmod{24}\) 的 Type II 证书。

## 结论

该反例排除以下未经证明的推理：

\[
\text{同一模数}
\;+\;
\text{各状态 Kneser 积集}
\Longrightarrow
\text{可将积集直接相乘并命中目标}.
\]

因此，跨状态容量必须至少附带下列之一：

1. 同一个整数因子同时属于多个状态，并保留其来源标签；
2. 一个已证明的 source-switch/alternate 恒等式，把混合因子重新组合为单个合法状态；
3. 一个标记解集提升定理，证明混合残数命中可回译为 Type I/II 证书；
4. 一个不依赖伪积集命中的严格下降势。

本反例不表示 \(p=97\) 没有 Erdős--Straus 分解；它只否定跨状态积集无条件池化。
它也说明上一张 q-height/Kneser 桥必须保持“单状态”量词，不能直接把
\(\kappa_q\) 在不同移位的商群中相加。
