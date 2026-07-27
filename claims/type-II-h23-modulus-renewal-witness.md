---
kind: claim
claim_id: type-II-h23-modulus-renewal-witness
title: H23 模数扩张使一私有因子模型重新出现可采纳分支
statement: H=22 的规范 Type II 一私有素因子模型在 Q_22=77597520 的二层模三剥离后无安全分支；但其安全剩余类 r=529 在 Q_23=23Q_22 下有 CRT 提升 R=1474353409。R 对 H=23 全部射线仍一层安全，且 R mod 23=3 使第 5 条移位的强制因子从 3 变为 69。在二层分支 n=3m 中得到的 24 条线性型没有覆盖素数，故该简化模型在 H23 恢复可采纳分支。依 Dickson/Schinzel 素数元组猜想，这给出条件性的 H23 共同逃逸族；它不构成原猜想的反例或无条件否定。
claim_status: computationally_reproduced
topics:
- type-II
- canonicalization
- multishift
- factorization
- admissibility
- obstruction
- proof-program
sources:
- paper: chamberland2026
  locator: "Theorem 1"
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-25'
---

# H23 模数扩张使一私有因子模型重新出现可采纳分支

## 结论的精确位置

令前 \(H\) 条规范移位的联合模数为

\[
Q_H=\operatorname{lcm}\left(24,\{4a_sc_s:1\leq s\leq H\}\right).
\]

在 \(H=22\)，已有精确枚举证明：所有一层安全剩余类经 \(n=3m+j\) 的二层剥离后，
每个分支都被至少一个有限素数覆盖。这个结论只使用

\[
Q_{22}=77\,597\,520.
\]

第 23 条规范移位的模数引入新的素数 \(23\)，从而

\[
Q_{23}=1\,784\,742\,960=23Q_{22}.
\]

取 H22 的安全剩余类 \(r=529\)，并取唯一满足

\[
R\equiv529\pmod {Q_{22}},\qquad R\equiv3\pmod {23}
\]

的代表元

\[
R=1\,474\,353\,409\pmod {Q_{23}}.
\]

直接有限域检查给出：

| 层级 | 剩余类 | 二层分支 | 覆盖素数 |
|---|---:|---:|---|
| H22 | \(529\bmod Q_{22}\) | \(j=0\) | \(23\) |
| H22 | \(529\bmod Q_{22}\) | \(j=1\) | \(23\) |
| H22 | \(529\bmod Q_{22}\) | \(j=2\) | \(3,23\) |
| H23 | \(R\bmod Q_{23}\) | \(j=0\) | 无 |

这里的“无”是对应 \(p\) 和全部 23 个强制因子余商，共 24 条线性型的精确可采纳性；
它不是声称这些线性型已经无条件同时取到素数。

## 新素数如何改变状态

对第 5 条移位，H22 中的强制因子是 \(3\)。CRT 提升后，

\[
\gcd(Q_{23},R+4\cdot5)=69=3\cdot23.
\]

因而旧状态里用于覆盖二层分支的素数 \(23\)，在 H23 中已被吸收到这条移位的固定因子。
这正是固定模数闭合不能向下一次模数扩张直接归纳的具体机制。

执行

```bash
python3 reproductions/type_ii_prime_cofactor_renewal_witness.py
```

会重建 CRT、所有射线的一层安全性、第 5 条移位的强制因子 \(69\)，以及 H23 的
可采纳性检查。测试文件为
`tests/test_type_ii_prime_cofactor_renewal_witness.py`。

## 研究含义

这排除了一个过强的归纳设想：“只要某个固定 \(Q_H\) 的二层分支为零，继续添加射线就会
永久为零”。可行的状态量至少需要包含：

1. 每条旧移位的强制因子及其来源素数；
2. 模数扩张时哪些覆盖素数被转移进这些强制因子；
3. 新移位的残数约束，以及私有余商分解允许的复杂度。

下一步不应继续寻找另一个固定 \(H\) 的零分支，而应定义这种带来源标记的状态转移，
并证明每次重启都会消耗一个可度量资源，或可构造能从更小标记状态提升的严格递降边。

## 范围

该见证仅针对“每个剥离后的余商为一个素数”的简化模型。即使采用 Dickson/Schinzel
把可采纳线性型转成无穷素数元组，也只是该模型的条件性逃逸，不能推出
Erdős--Straus 猜想有反例，也不替代对真实多因子余商状态的分析。
