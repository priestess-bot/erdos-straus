---
kind: claim
claim_id: type-II-h19-affine-square-uniform-audit
title: H19-k23 残存进程的完整统一仿射平方除子审计
statement: H19-k23 模二十九分裂的18条可采纳进程中，v=12 的整条进程 p=1552726375200n+664398295201 有平方专用统一 Type II 证书：取缺口 m=191，x=(p+m)/4=9048N，N=42902475n+18357601，d=7569N；这里 7569|9048^2、7569 不整除9048、191|9048+7569。其余17条进程对全部统一非恒定仿射平方除子 d=a x/E（E=gcd(S,T)，a|E^2，a<=E）均无自然范围未来缺口证书。
claim_status: computationally_reproduced
topics:
- type-II
- arithmetic-progression
- affine-rigidity
- square-divisor
- certificate
- conditional-boundary
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-criterion
visibility: public
last_checked: '2026-07-25'
---

# H19-k23 残存进程的完整统一仿射平方除子审计

## 审计对象与有限化

[H19-k23 模二十九出口分类](type-II-h19-external-scale-k23-branching.md) 的 18 条
条件性残存进程写作

\[
p=Pn+C.
\]

给定未来自然 Type II 缺口 \(m\)，令

\[
x=\frac{p+m}{4}=Sn+T,\qquad S=\frac P4,\qquad T=\frac{C+m}{4},
\qquad E=\gcd(S,T).
\]

[统一仿射平方除子刚性](type-II-affine-uniform-divisor-rigidity.md) 表明，全部参数上有效的
非恒定仿射平方除子只能是

\[
d=a\frac{x}{E},\qquad a\mid E^2,\qquad a\le E. \tag{1}
\]

固定缺口还要求 \(m\mid E+a\)。由于 \(E\mid T\)，有

\[
m\equiv-C\pmod {4E}. \tag{2}
\]

另一方面 \(m\mid E+a\) 和 \(a\le E\) 给出 \(m\le2E<4E\)。故固定 \(E\mid S\)
至多允许一个正缺口：它就是 \((-C)\bmod4E\)，若该代表元满足自然范围、\(E=\gcd(S,T)\)
及 \(m\equiv3\pmod4\)。这使每条进程的审计成为完整有限枚举，而不是给缺口设置人工上界。

## 一个平方专用整进程证书

在 \(v\equiv12\pmod {29}\) 的残存进程，

\[
p=1\,552\,726\,375\,200n+664\,398\,295\,201.
\]

取

\[
m=191,\qquad
x=388\,181\,593\,800n+166\,099\,573\,848
=9048N,
\]

其中

\[
N=42\,902\,475n+18\,357\,601,
\qquad d=7569N.
\]

直接有

\[
7569\mid9048^2,\qquad7569\nmid9048,\qquad
191\mid9048+7569.
\]

所以 \(d\mid x^2\)，但一般 \(d\nmid x\)，且两条 Type II 整除式对所有参数成立：

\[
191\mid x+d,\qquad191\mid x+\frac{x^2}{d}.
\]

从而每个落在该进程上的素数都由

\[
\frac4p=
\frac1x+
\frac1{p(x+d)/191}+
\frac1{p(x+x^2/d)/191}
\]

得到 Type II 表示。这是 [固定因子陷阱边界](type-II-h19-external-scale-fixed-trap-boundary.md)
所漏掉的 \(a\nmid E\) 平方专用情形。

## 完整结果与边界

对其余 17 条进程，脚本逐一穷尽全部合格 \(E\) 的唯一候选缺口和 (1) 的所有可能
\(a\)。空进程合计检查了 12,360 个固定因子状态与 45,594 个最短侧候选；没有命中。
命中进程在第 65 个合格 \(E\) 和第 207 个候选即给出上述见证，故无需继续枚举其它
见证来证明该整条进程已闭合。

这将 H19-k23 的条件性残存数由 18 降至 17，但不处理非仿射除子、参数相关缺口、
多源耦合或其它严格递降。特别是，它不能支持“平方专用仿射族已闭合全部状态树”的外推。

运行

```bash
python3 reproductions/type_ii_h19_affine_square_uniform_audit.py
python3 -m unittest tests/test_type_ii_h19_affine_square_uniform_audit.py -q
```

可重建全部进程、空结果和平方专用证书。
