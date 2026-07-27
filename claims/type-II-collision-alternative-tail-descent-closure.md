---
kind: claim
claim_id: type-II-collision-alternative-tail-descent-closure
title: H19 碰撞标签状态的替代 Type II 尾部递降闭合
statement: 在 p<=10^9 的11个最小正碰撞重数 H19 状态中，2个在其已选碰撞标签证书缺口直接有标记尾部递降；其余9个虽然在该固定证书缺口失败，但完整枚举 p-1 的4倍数因子缺口后均找到另一张 Type II 双尾严格递降证书。因此这11个有限状态全部有严格递降出口；首个两碰撞状态 p=372271201 以替代缺口7递降至46533901。
claim_status: computationally_reproduced
topics:
- type-II
- descent
- collision-factor
- short-certificate
- alternative-certificate
- finite-audit
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-certificate-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-26'
---

# H19 碰撞标签状态的替代 Type II 尾部递降闭合

对固定碰撞标签证书的缩放首分母检验在 11 个状态中只命中 2 个，见
[固定缺口尾部递降边界](type-II-collision-label-tail-deflation-boundary.md)。这不应被
误读为素数本身没有递降：普通双尾去 \(p\) 允许从同一 \(p\) 重新选择缺口

\[
m=d-1,\qquad d\mid p-1,\qquad 4\mid d. \tag{1}
\]

对边界留下的九点，逐一穷尽 (1) 的全部候选；在每个 \(m\) 上精确分解
\(x=(p+m)/4\)，枚举 \(x^2\) 的全部除子并检查 Type II 条件。九点全部命中，故

\[
11=2_{\text{fixed-certificate descent}}+9_{\text{alternative-certificate descent}}. \tag{2}
\]

特别地，首个两碰撞压力点并不需要等待其 \(s=89\) 碰撞证书释放：

\[
p=372\,271\,201,quad m=7,quad d=8,quad
n=\frac{p+7}{8}=46\,533\,901. \tag{3}
\]

相应 Type II 除子为 \(47\)，其两条 \(p\)-尾分母同时除以 \(p\) 后严格重建
\(4/n\) 的一张解。

这只是 H19 后有限、已存储状态集的闭合。它没有证明每个核心素数都能在 \(p-1\) 的
因子缺口中选到 Type II 证书，也不能把“换证书后存在递降”误作一个尚未证明的全称
选择器。它的贡献是消除了这 11 个碰撞标签状态作为当前递降障碍的可能性。

## 重建

~~~bash
python3 reproductions/type_ii_collision_alternative_tail_descent.py
python3 -m unittest tests/test_type_ii_collision_alternative_tail_descent.py -q
~~~
