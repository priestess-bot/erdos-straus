---
kind: claim
claim_id: mixed-factor-h19-uniform-affine-boundary
title: H19-k23 十四条残存进程的统一仿射混合因子递降边界
statement: 在 H19-k23 经统一仿射 Type I/II 证书削减后保留的14条进程上，对37个全程可用外部尺度 k（k|1800 或 k=23），不存在全参数仿射混合因子 g。精确地，若 n_k=F(un+v)，任何正非恒定仿射 g|k n_k 必为 g=b(un+v)，其中 b|kF；混合因子严格递降还要求 b<=F、(4k-1)|bu 与 (4k-1)|(bv+1)。14乘37个源的全部2394个 b 候选均未满足这些条件。
claim_status: computationally_reproduced
topics:
- descent
- external-source
- mixed-factor
- affine-rigidity
- arithmetic-progression
- conditional-boundary
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-certificate-and-lift-context
visibility: public
last_checked: '2026-07-25'
---

# H19-k23 十四条残存进程的统一仿射混合因子递降边界

## 统一仿射混合因子的正规形

固定外部尺度 \(k\)，令 \(q=4k-1\)。在一个进程参数 \(t\) 上，假设源分母全程为

\[
n_k(t)=F(ut+v),\qquad \gcd(u,v)=1. \tag{1}
\]

设正非恒定仿射 \(g(t)\) 对全部参数都满足

\[
g(t)\mid k n_k(t). \tag{2}
\]

则唯一有正整数 \(b\) 使

\[
g(t)=b(ut+v),\qquad bmid kF. \tag{3}
\]

事实上，将 \(g(t)\) 与 \(kn_k(t)\) 的一次系数交叉相消，得到 \(g(t)\) 整除一个
固定整数；非恒定正函数无界，故该固定整数只能为零，因而两者成比例。再取
\(ut+v\) 的值的最大公因子为一，得到 \(b\mid kF\)。

混合因子外部源严格提升还要求

\[
g(t)le n_k(t),\qquad g(t)equiv-1pmod q. \tag{4}
\]

由 (1)--(3)，(4) 与下列有限条件等价：

\[
b\le F,\qquad q\mid bu,\qquad q\mid bv+1. \tag{5}
\]

命中后，`mixed-factor-external-source-descent` 的恒等式给出从 \(n_k<p\) 到 \(p\)
的严格带标记提升；故 (5) 不是启发式筛选，而是该统一仿射子族的充要条件。

## 十四条剩余进程的完整结果

[统一仿射 Type I 审计](type-I-h19-affine-uniform-square-audit.md) 与
[统一仿射平方 Type II 审计](type-II-h19-affine-square-uniform-audit.md) 合并后，
H19-k23 树仅余 14 条进程。对每一条，以下 37 个尺度在全部参数上可用：

\[
\{k:k\mid1800\}\cup\{23\}.
\]

脚本对每个源提取 (1)，枚举所有 \(b\mid kF\) 且 \(b\le F\)，再精确检查 (5)。结果为：

| 项目 | 数目 |
|---|---:|
| 残存进程 | 14 |
| 每进程静态尺度 | 37 |
| 全部候选 \(b\) | 2,394 |
| 统一仿射混合因子命中 | 0 |

每个候选命中时还会逐项核验源单位分数恒等式与把首项替换为其 \(p\) 倍后的严格提升；
本次没有命中。

## 含义与边界

这排除了一个很具体但自然的递降桥：从一个固定外部源尺度上，使用一个随进程线性变化且
全程整除 \(kn_k\) 的混合因子。它不排除：

- 随参数非仿射的因子选择；
- 同时使用两个或多个源分母的因子关系；
- 新的源分母或其它 Type I/II 证书；
- 在子状态上才出现的严格递降。

因此下一步的桥接引理必须实质性使用多源关系或非仿射因子，而不能只是把单源
混合因子推广为一个冻结仿射模板。

运行

```bash
python3 reproductions/mixed_factor_h19_uniform_affine_boundary.py
python3 -m unittest tests/test_mixed_factor_h19_uniform_affine_boundary.py -q
```

可重建全部 2,394 个候选与零命中结果。
