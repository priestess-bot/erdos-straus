---
kind: claim
claim_id: type-II-ac-escape-affine-ray-boundary
title: 深层 AC 条件逃逸进程不存在统一仿射 Type II 射线
statement: 对深层 AC 条件逃逸进程 p(t)=245044800t+1，任取正整数 A,C。若 p(t)+4A^2C 有一个对全部 t 整除的非恒定仿射因子 h(t)，且 h(t)=-1 mod 4AC 对全部 t 成立，则存在固定余因子 L，使 L|245044800、L|(1+4A^2C)、4AC|245044800/L，且 (1+4A^2C)/L=-1 mod 4AC。完整枚举系数的1008个因子、896000个必需 AC 分解和58230个余因子情形，命中为零。故该进程没有任何统一仿射 Type II 原始 AC 射线证书。
claim_status: computationally_reproduced
topics:
- type-II
- ac-rays
- affine-rigidity
- conditional-boundary
- proof-program
sources:
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
- paper: bradford2024
  locator: Section 2, Type II divisor certificates
  role: ray-certificate-context
visibility: public
last_checked: '2026-07-25'
---

# 深层 AC 条件逃逸进程不存在统一仿射 Type II 射线

## 归约

令

\[
p(t)=Nt+1,\qquad N=245044800,
\]

并固定正整数 \(A,C\)。设某个非恒定正仿射式 \(h(t)\) 对每个整数 \(t\) 都整除

\[
p(t)+4A^2C=Nt+1+4A^2C. \tag{1}
\]

因为二者同为一次式，商在无穷多个 \(t\) 上有界，故必为固定正整数 \(L\)：

\[
Nt+1+4A^2C=Lh(t). \tag{2}
\]

若 \(h(t)\equiv-1\pmod {4AC}\) 对全部 \(t\) 成立，比较 (2) 的系数和常数得

\[
L\mid N,\qquad L\mid(1+4A^2C),\qquad
4AC\mid\frac NL,\qquad
\frac{1+4A^2C}{L}\equiv-1\pmod {4AC}. \tag{3}
\]

特别地，\(4AC\mid N\)。所以表面上无界的 \(A,C\) 搜索被压缩为 \(N\) 的有限因子
分解；这也包括固定因子和固定 \(K\) 的原始 AC 模板。

## 精确枚举

脚本枚举 \(L\mid N\)，再枚举 \(4AC\mid N/L\) 的每个模数及其全部 \(AC\) 分解，
最后检查 (3)：

| 项目 | 数量 |
|---|---:|
| \(N\) 的正因子 | 1,008 |
| 必需 AC 分解 | 896,000 |
| 同时整除两侧的 \(L\) 情形 | 58,230 |
| 仿射原始 AC 射线命中 | 0 |

重建：

    python3 reproductions/type_ii_ac_escape_affine_ray_boundary.py \
      --output reproductions/type-ii-ac-escape-affine-ray-boundary-results.json
    python3 -m unittest tests/test_type_ii_ac_escape_affine_ray_boundary.py -q

## 含义与边界

这排除的是特定条件进程上的统一一次因子证书，不排除随参数非线性变化的因子、
Type I 证书或可提升的严格递降。它也不是 Erdős--Straus 猜想的条件性反例。

因此，固定 AC 盒的逃逸状态不能仅靠添一条固定或仿射 AC 射线接回。正向方案必须利用
因子随参数的非线性变化，或构造真正以更小分母状态为源的提升边。
