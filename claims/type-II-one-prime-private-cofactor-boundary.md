---
kind: claim
claim_id: type-II-one-prime-private-cofactor-boundary
title: 十四规范移位的一私有素因子模型被模三覆盖阻断
statement: 对规范移位 s=1,...,14，令 Q=lcm(24,{4a_sc_s})=240240，并写 p=Qn+r。令 D_s=gcd(Q,r+4s)、L_s(n)=(Qn+r+4s)/D_s。若 r 是核心残数、每条射线在假设 N_s=D_s*L_s 且 L_s 为素数时仍失败，则共有 616 个允许 r；对每一个，它们的 15 条线性型 p,L_1,...,L_14 在模三上总有一条为零。故该线性型族不可采纳；除有限小值外，不能同时令 p 与所有 L_s 均为素数。任何足够大的共同失败点若落在这些安全残数类，至少一个 N_s 除去其同余强制因子后的商必为合数。
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
- paper: linnik1944
  locator: least-prime theorem in arithmetic progressions
  role: arithmetic-progression-context
- paper: chamberland2026
  locator: "Theorem 1"
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-24'
---

# 十四规范移位的一私有素因子模型被模三覆盖阻断

## 极简私有因子模型

取规范移位

\[
\mathcal S=\{1,2,\ldots,14\},
\]

并令每个 $s=a_s^2c_s$ 为平方自由规范表示。其射线模数的最小公倍数为

\[
Q=\operatorname{lcm}\bigl(24,\{4a_sc_s:s\in\mathcal S\}\bigr)=240240. \tag{1}
\]

固定一个核心残数 $r$，即

\[
r\equiv1\pmod {24},\qquad \gcd(r,Q)=1,
\]

并写

\[
p=Qn+r.
\]

对每个 $s$，有固定整除因子

\[
D_s=\gcd(Q,r+4s)\mid p+4s, \tag{2}
\]

及整系数线性商

\[
L_s(n)=\frac{Q}{D_s}n+\frac{r+4s}{D_s},\qquad
p+4s=D_sL_s(n). \tag{3}
\]

这里研究的只是最乐观的反覆盖模型：假定每个 $L_s(n)$ 都是一个素数。因为
$D_s$ 与相应射线模数互素，$L_s$ 模该模数的残数由 $rD_s^{-1}$ 唯一确定；可用
完整除子残数集精确判定这个“固定部分乘一个素数”的分解是否仍避开 $-1$。

## 有限可采纳性审计

枚举模 $Q$ 的全部 $5760$ 个核心残数。共有 $616$ 个残数能让十四条射线都通过上述
一私有素因子的避靶测试。对每个这样的 $r$，检查 15 条线性型

\[
Qn+r,\quad L_1(n),\ldots,L_{14}(n). \tag{4}
\]

结果是：每一个安全 $r$ 都被素数 $3$ 覆盖，即对任意 $n\pmod3$，(4) 中至少一条
为零模 3。没有一个安全残数给出可采纳的线性型族：

\[
\#\{\text{安全 }r\}=616,\qquad
\#\{\text{安全且可采纳 }r\}=0. \tag{5}
\]

这是严格有限检查。对 15 条线性型，只须检查不超过 15 的素数：对于更大的素数，
每条非退化线性型至多贡献一个根，15 个根不可能覆盖整个有限域。脚本还显式处理一条
线性型恒为零模某素数的退化情形。

```bash
python3 reproductions/type_ii_prime_cofactor_boundary.py \
  --base-shift-bound 14 \
  --output reproductions/type-ii-prime-cofactor-boundary-results.json
```

可重建所有残数、避靶检查和覆盖素数直方图；输出中模 3 的计数为 616。

## 含义和边界

由于每个安全残数类的某条 $L_s$ 总被 3 整除，当 $n$ 足够大时它不可能仍等于素数
3。因此不存在无穷个目标素数使 $p$ 和全部十四个一私有素因子 $L_s$ 同时为素数。

这不是十四射线的覆盖定理，也不排除 Erdős--Straus 的共同残余。实际失败点可以让
某个 $L_s$ 继续分解成两个或更多私有素因子；例如已有有限共同残余正表现出这种较丰富
的因子结构。该结论只排除了最简单的“每条移位只剩一个新的素因子”的逃逸模型。

它提供下一层可执行的目标：在模 3 强制出现的额外因子剥离后，递归追踪新的商的残数
乘积集，判断这条局部覆盖是否最终强制某个 Type II 因子，或是否继续产生真正的多因子
逃逸族。
