---
kind: claim
claim_id: type-II-ac-ray-audit
title: 有界 A,C、可变 K 的 Type II 因子射线在 5*10^8 内全覆盖
statement: 精确审计表明，对每个 p<=5*10^8 且 p=1 mod24，存在 1<=A,C<=14 和任意正整数 K，使 h=4ACK-1 整除 Kp+A、A<=(Kp+A)/h，且由此恢复的 Type II 证书有效。半径 11 在 p<=10^8 的审计中仅遗漏 p=84525841。等价的因子检查是 h|p+4A^2C 且 h 为 4AC 模下的负一残数。
claim_status: computationally_reproduced
topics:
- type-II
- factorization
- computation
- short-certificate
- proof-program
sources:
- paper: bradford2024
  locator: "Propositions 2 and 4 (statements; the paper leaves their proofs to the reader)"
  role: Type-II-certificate-statement-context
- paper: chamberland2026
  locator: "Theorem 1"
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-27'
---

# 有界 \(A,C\)、可变 \(K\) 的 Type II 因子射线在 \(5\cdot10^8\) 内全覆盖

## 精确代数

Type II 正规形的因子生成器记为

\[
h=4ACK-1.
\]

对固定的正整数 \(A,C,K\)，有精确等价

\[
h\mid Kp+A
\quad\Longleftrightarrow\quad
h\mid p+4A^2C. \tag{1}
\]

正向只需将 \(Kp+A\) 乘以 \(4AC\)，并使用
\(4ACK\equiv1\pmod h\)；反向则将右式乘以 \(K\)。因此，对固定
\((A,C)\)，所有可能的 \(K\) 可由 \(p+4A^2C\) 的因子穷举：

\[
h>1,\qquad h\equiv-1\pmod{4AC},\qquad
K=\frac{h+1}{4AC}. \tag{2}
\]

因 \(h\mid Kp+A\)，商 \(B=(Kp+A)/h\) 已自动为正整数。剩下的序条件可精确写为

\[
B-A=\frac{K(p-4A^2C)+2A}{h}\ge0. \tag{3}
\]

因此 \(p\ge4A^2C\) 时该条件自动成立；只有有限个较小 \(p\) 需要再检查。然后
\(m=(A+B)/K\)、\(d=A^2C\) 恢复并严格验证 Type II 证书。

互素条件不应加入 (3)：它只使 \((A,B,C)\) 成为唯一正规形，并非证书有效性的必要条件。
若 \(g=\gcd(A,B)>1\)，直接的 \(x=ABC,d=A^2C\) 仍已满足 Type II 条件；它只是可
重写为互素坐标 \(A/g,B/g,Cg^2\)。本审计保留这类冗余参数，以避免漏掉较小的
\(\max(A,C)\) 射线。

这里的关键区别是：\(A,C\) 被限制，但 \(K\) 没有被限制。故
type-II-finite-template-obstruction 关于固定有限三元组 \((A,C,K)\) 的结论
不能直接排除此路线。

## 有限审计

运行

```bash
python3 reproductions/type_ii_ac_ray.py --limit 500000000 --ac-bound 14 \
  --output reproductions/type-ii-ac-ray-500m-bound14-results.json
```

对全部 \(3{,}292{,}848\) 个 \(p\le5\cdot10^8\)、\(p\equiv1\pmod{24}\) 的素数，
半径 \(14\) 的结果为

\[
\#\{\text{命中}\}=3{,}292{,}848,\qquad \#\{\text{遗漏}\}=0. \tag{4}
\]

较早的 \(p\le10^8\) 审计中，半径 \(11\) 仅遗漏 \(84{,}525{,}841\)，而半径 \(14\)
已全覆盖。五亿范围继续保持同一记录保持者：

\[
p=84{,}525{,}841,\qquad
(A,C,K,h)=(1,14,30,1679),\qquad
(m,d)=(50343,14).
\]

在同一方向上，移动窗口的保持者 \(p=8{,}803{,}369\) 甚至有

\[
(A,C,K,h)=(1,3,3841,46091),\qquad (m,d)=(191,3),
\]

说明小 \(A,C\) 不意味着小 \(K\) 或固定小缺口。

脚本同时对每张接受的证书执行整数整除和有理数恒等式复核。边界 \(11\) 的独立输出在
`type-ii-ac-ray-1e8-results.json`；半径 \(14\) 的 \(10^8\)、\(2\cdot10^8\) 与
\(5\cdot10^8\) 输出分别在 `type-ii-ac-ray-1e8-bound14-results.json`、
`type-ii-ac-ray-2e8-bound14-results.json` 与
`type-ii-ac-ray-500m-bound14-results.json`。

## 不能推出的结论

该结果没有证明存在全局常数 \(B\)，使

\[
\forall p\equiv1\pmod{24}\ \exists\,A,C\le B,\ K\ge1
\]

满足 (1)--(3)。若这种全局 \(B\) 被证明，便会通过直接 Type II 证书解决目标猜想；
目前这只是一个明确而未证明的子目标。更精确地，对 \(p\ge4B^3\)，(3) 自动成立，
所以其无穷部分只是在有限组移位数 \(p+4A^2C\) 中强制一个
\(-1\pmod{4AC}\) 因子；\(p<4B^3\) 只是有限的边界检查。

它也不等同于固定有限 \((A,C,K)\) 模板覆盖：这里 \(K\) 随 \(p\) 增长，甚至在
\(A=C\) 很小的情形也可很大。因而既不能将有限审计提升为定理，也不能用已有的有限模板
避免定理直接否定它。
