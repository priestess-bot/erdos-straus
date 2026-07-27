---
kind: claim
claim_id: type-I-h19-affine-uniform-square-audit
title: H19-k23 残存进程的完整统一仿射 Type I 审计
statement: H19-k23 模二十九分裂的18条可采纳进程中，v 属于 {2,9,12,25} 的4条有统一仿射 Type I 证书，均取 m=87、E=3094，而 a 分别为 338、119、833、10829；最后一个 a>E，故严格属于 Type I 而不能由 Type II 覆盖。其余14条进程对所有正非恒定仿射除子 d=a x/E（a|E^2，无 a<=E 限制）均无自然范围统一 Type I 证书。
claim_status: computationally_reproduced
topics:
- type-I
- arithmetic-progression
- affine-rigidity
- square-divisor
- certificate
- conditional-boundary
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-divisor-criterion
visibility: public
last_checked: '2026-07-25'
---

# H19-k23 残存进程的完整统一仿射 Type I 审计

## 完整枚举空间

对 [H19-k23 模二十九出口分类](type-II-h19-external-scale-k23-branching.md) 的每条
\(p=Pn+C\)，令 \(x=(p+m)/4=Sn+T\)、\(E=\gcd(S,T)\)。
[统一仿射 Type I 刚性](type-I-affine-uniform-divisor-rigidity.md) 将全部正非恒定
统一仿射 Type I 除子化为

\[
d=a\frac{x}{E},\qquad a\mid E^2,
\]

并强制

\[
m\mid S/E,\qquad a\equiv-4E^2(T/E)pmod m. \tag{1}
\]

因此 \(m\mid S\)，不需要以数值方式截断未来缺口。每条进程恰有 564 个自然范围
\(m\equiv3\pmod4\) 候选；对每个候选，脚本用 (1) 在 \(E^2\) 的全部正除子中
选择 \(a\)，并核验二次同余的每个系数及恢复的单位分数恒等式。

## 四条整进程证书

下表中所有进程的公用步长为 \(P=1\,552\,726\,375\,200\)，并取
\(m=87,E=3094\)。每一行都表示该仿射进程中所有素数值的一张 Type I 证书。

| \(v\bmod29\) | \(C\) | \(a\) | 与 Type II 的关系 |
|---:|---:|---:|---|
| 2 | 128,975,407,201 | 338 | \(a\le E\)，但满足的是 Type I 同余 |
| 9 | 503,771,428,801 | 119 | \(a\le E\)，但满足的是 Type I 同余 |
| 12 | 664,398,295,201 | 833 | \(a\le E\)，另有 \(m=191\) 的 Type II 叶子 |
| 25 | 1,360,448,049,601 | 10,829 | \(a>E\)，严格为 Type I 专用 |

最后一行尤为关键：\(10829\mid3094^2\)，但 \(10829>3094\)，所以它不可能来自
任何要求 \(d\le x\) 的 Type II 证书。

## 余下边界

其余 14 条进程均完整检查 564 个缺口，合计 19,338 个最短侧平方因子残数候选后为空。
连同 [统一仿射平方 Type II 审计](type-II-h19-affine-square-uniform-audit.md)，原来的
18 条 H19-k23 条件性残存进程已有 4 条被无条件证书闭合，留下 14 条。

空结果不排除非仿射 Type I 除子、参数相关缺口、多源耦合或严格递降；它只是把这些
机制从“可能被一个整进程仿射叶子解决”的范围中精确分离出来。

运行

```bash
python3 reproductions/type_i_h19_affine_uniform_square_audit.py
python3 -m unittest tests/test_type_i_h19_affine_uniform_square_audit.py -q
```

可重建所有候选、四张证书及十四条空进程。
