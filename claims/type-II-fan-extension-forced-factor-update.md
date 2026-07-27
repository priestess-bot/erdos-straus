---
kind: claim
claim_id: type-II-fan-extension-forced-factor-update
title: Type II 扇扩张的模数强制因子精确更新律
statement: 设旧扇模数为Q、残数为r，新扇模数Q'为Q的倍数，并取兼容提升R等于r模Q。对每条旧移位s，强制因子D_s=gcd(Q,r+4s)整除D'_s=gcd(Q',R+4s)，其各素数指数由两次最小值精确相减给出。因此新增模数素数可进入旧移位的强制因子，即使新增移位没有引入任何新的移位差碰撞素数。H22到H23中Q'=23Q，唯一改变的旧移位为s=5，D_5从3变为69；同时移位差碰撞素因子集合不变。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-II
- canonicalization
- multishift
- state-transition
- factorization
- forced-factors
- proof-program
sources:
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-28'
---

# Type II 扇扩张的模数强制因子精确更新律

## 状态与定理

令有限规范移位扇的联合模数为 (Q)，并在一个残数进程中写

\[
p=Qn+r.
\]

对一条旧移位 (s)，一私有余因子模型先从 (p+4s) 中抽取的强制因子是

\[
D_s(Q,r)=\gcd(Q,r+4s). \tag{1}
\]

扩张扇后，设

\[
Q\mid Q',\qquad R\equiv r\pmod Q, \tag{2}
\]

其中 (R) 是新模数下的一个兼容残数。令

\[
D'_s=\gcd(Q',R+4s). \tag{3}
\]

则对每条旧移位都有

\[
D_s\mid D'_s. \tag{4}
\]

更精确地，对任意素数 (ell)，

\[
v_\ell(D'_s)-v_\ell(D_s)
=\min\{v_\ell(Q'),v_\ell(R+4s)\}
-\min\{v_\ell(Q),v_\ell(r+4s)\}. \tag{5}
\]

因此某个新增的模数素数 (ell) 进入旧移位 (s) 的强制因子，当且仅当
右边为正；这取决于**提升后的**残数 (R)，不能由旧扇的状态单独决定。

## 证明

由 (2)，对每个 (ell) 有

\[
\min\{v_\ell(Q),v_\ell(r+4s)\}
=\min\{v_\ell(Q),v_\ell(R+4s)\}. \tag{6}
\]

这是因为两数之差被 (Q) 整除；在 (v_\ell(Q)) 以下它们的赋值相同，在该阈值以上
两边最小值都已饱和。式 (4) 随即由 (Q\mid Q') 得到，而对 (1)、(3) 分别取
(\ell)-进赋值并使用 (6)，便得到 (5)。

注意这与实际移位数的碰撞因子是不同的状态层。后者只能来自

\[
\gcd(p+4s,p+4u)\mid4(u-s), \tag{7}
\]

而 (5) 允许新模数素数改变旧移位的强制因子，即使它不整除任何新旧移位差。

## H22 到 H23 的见证

取既有 H22 安全残数与其 H23 CRT 提升

\[
Q_{22}=77{,}597{,}520,\quad r=529,\qquad
Q_{23}=23Q_{22}=1{,}784{,}742{,}960,\quad
R=1{,}474{,}353{,}409. \tag{8}
\]

对 22 条旧移位应用 (1)--(5)，唯一变化是

\[
D_5=\gcd(Q_{22},529+20)=3,\qquad
D'_5=\gcd(Q_{23},R+20)=69. \tag{9}
\]

故 (23) 被转入第 5 条旧移位的强制因子。另一方面，前 22 条与前 23 条移位的
差值碰撞素数集合完全相同；因此这次重启不是新的差值碰撞，而是模数增长与 CRT 提升
共同造成的状态更新。

## 研究含义

任何可归纳的 AC 多射线状态至少要同时保存：

1. 实际因子分解中的碰撞/私有来源标签；
2. 当前模数与残数进程的每条移位强制因子；
3. 扩张时的新模数素数及兼容残数提升。

仅保存第一层会漏掉 (9)，仅保存固定模数下的余商模型又会漏掉新扇带来的重启。该更新律
本身不强制 Type II 证书、Type I 桥或严格递降；它只是构造此类全称转移定理所需的精确状态规则。

可复现命令：

~~~bash
python3 reproductions/type_ii_fan_extension_forced_factor_update.py
python3 -m unittest tests/test_type_ii_fan_extension_forced_factor_update.py -q
~~~
