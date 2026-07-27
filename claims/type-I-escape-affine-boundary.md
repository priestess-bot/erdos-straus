---
kind: claim
claim_id: type-I-escape-affine-boundary
title: 深层 AC 条件逃逸进程的统一固定缺口 Type I 边界
statement: 对 p(t)=245044800t+1，在任意固定合法缺口 m 上，不存在对全部参数成立的常数或非恒定仿射 Type I 除子 d(t)|((p(t)+m)/4)^2。精确地，令 S=61261200，T=(m+1)/4，E=gcd(S,T)，则任何非恒定仿射候选为 d=a((S/E)t+T/E)，其中 a|E^2，且必须满足 m|S/E、a=-4E^2(T/E) modm；常数候选须 d|E^2、d=-T modm。前者和后者均强制 m|S。完整扫描 S 的720个除子中72个合法缺口，共检查434个非恒定和434个常数候选，均无命中。
claim_status: computationally_reproduced
topics:
- type-I
- affine-rigidity
- conditional-boundary
- factorization
- short-certificate
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-divisor-criterion
- paper: ventas2026
  locator: Theorems 2.1--2.3
  role: FCT-external-source-subfamily-context
visibility: public
last_checked: '2026-07-25'
---

# 深层 AC 条件逃逸进程的统一固定缺口 Type I 边界

## 定理

令

\[
p(t)=Nt+1,\qquad N=245044800=4S,\qquad S=61261200. \tag{1}
\]

固定一个合法缺口 \(m\equiv3\pmod4\)，并写

\[
x(t)=\frac{p(t)+m}{4}=St+T,
\qquad T=\frac{m+1}{4},
\qquad E=(S,T), \tag{2}
\]

\[
x(t)=E(ut+v),\qquad u=\frac SE,\quad v=\frac TE. \tag{3}
\]

则没有正的常数或非恒定仿射整数函数 \(d(t)\)，能对所有参数同时满足

\[
d(t)\mid x(t)^2,\qquad m\mid p(t)x(t)+d(t). \tag{4}
\]

也就是说，该进程没有任何统一、固定缺口的 Type I 除子证书。

## 有限化

首先 \((E,m)=1\)：若某素数同时整除 \(E\) 与 \(m\)，则它整除
\(4T-m=1\)，矛盾。

对非恒定仿射 \(d(t)\)，统一仿射 Type I 刚性给出唯一形状

\[
d(t)=a(ut+v),\qquad a\mid E^2. \tag{5}
\]

将其代入 (4)，得到充要条件

\[
m\mid u,\qquad a\equiv-4E^2v\pmod m. \tag{6}
\]

由于 \((E,m)=1\)，第一式等价于 \(m\mid S\)。因此所有可能的固定缺口
已压缩为 \(S\) 的有限因子。

若 \(d(t)=d\) 是常数，则 \(d\mid E^2\)，因为
\(\gcd_{t\ge0}x(t)^2=E^2\)。将 \(p(t)x(t)+d\) 的三个系数模 \(m\) 化简：

\[
p(t)x(t)+d
=4S^2t^2+S(4T+1)t+T+d. \tag{7}
\]

而 \(4T+1=m+2\)。由于 \(m\) 是奇数，(7) 对全部 \(t\) 成立也强制
\(m\mid S\)，随后仅剩

\[
d\equiv-T\pmod m. \tag{8}
\]

故常数和仿射两种情况都被同一有限因子枚举穷尽。

## 精确审计

\[
S=2^4\cdot3^2\cdot5^2\cdot7\cdot11\cdot13\cdot17
\]

有 720 个正因子。其中 \(m\equiv3\pmod4\) 的合法固定缺口有 72 个。对每个
缺口，完整枚举 \(E^2\) 的正因子，并检验 (6) 与 (8)：

| 项目 | 数目 |
|---|---:|
| \(S\) 的正因子 | 720 |
| 合法固定缺口状态 | 72 |
| 非恒定仿射候选 \(a\) | 434 |
| 常数候选 \(d\) | 434 |
| 非恒定仿射 Type I 命中 | 0 |
| 常数 Type I 命中 | 0 |

`reproductions/type_i_escape_affine_boundary.py` 还会对每个理论命中在
\(t=0,1,2,3\) 上独立以整数整除复核；本次没有命中。重建：

```bash
python3 reproductions/type_i_escape_affine_boundary.py
python3 -m unittest tests/test_type_i_escape_affine_boundary.py -q
```

## 与 FCT 和 Type II 边界的关系

三项 ceiling-FCT 的确定性构造等价于外部 source Type I 子类，因而属于这里的
非恒定仿射固定缺口候选。故该结果也排除它沿 (1) 的任何统一固定模板接回。

此前的 [深层 AC 逃逸的仿射射线边界](type-II-ac-escape-affine-ray-boundary.md)
只排除了统一仿射 Type II 原始 AC 射线。本卡补上 Type I：该条件性逃逸进程现在
同时不含这两类统一仿射短证书。

## 范围

本结论不排除随参数变化的缺口、非仿射因子、Type II 的非仿射证书，或任何严格递降。
尤其不能从条件性可采纳进程推断 Erdős--Straus 猜想存在反例。它只说明正向桥必须
真正利用参数依赖的非线性因子，或构造不被固定首分母标记束缚的提升。
