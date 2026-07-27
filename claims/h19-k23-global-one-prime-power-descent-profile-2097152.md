---
kind: claim
claim_id: h19-k23-global-one-prime-power-descent-profile-2097152
title: H19-k23 全局重写的一新增素因子幂递降剖面
statement: 在 H19-k23 二百万层全局重写的9,825条记录中，最终有5,128条规范支持度一的全局 Type II 证书；它们均给出严格双尾递降。所选证书的唯一非基底素因子指数分布为 5056 条一次、70 条二次、1 条三次、1 条四次。对其中46条，完整枚举同一最终尾的所有基底因子和所有非基底素数后，不存在任何非基底指数恰为一的 Type II 证书。因此同尾的一新增因子选择器不能普遍限制为 d=b*ell，必须允许 ell 的正幂。
claim_status: computationally_reproduced
topics:
- type-II
- descent
- p-minus-one
- global-tail-menu
- factor-support
- prime-powers
- computation
- h19
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-criterion
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 全局重写的一新增素因子幂递降剖面

本条只处理二百万层 H19-k23 审计中需要全局尾重写的 \(9\,825\) 条记录，不把它外推为
全体 \(4\,466\,959\) 个实际素数的命题。全局尾 \(m=4q-1\) 都满足
\(m+1\mid p-1\)。故一旦有 Type II 除子

\[
d\mid x^2,\qquad d\le x,\qquad d\equiv-x\pmod m,
\qquad x=\frac{p+m}{4},
\tag{1}
\]

就由双尾去 \(p\) 得到严格源

\[
n=\frac{p+m}{m+1}<p. \tag{2}
\]

在 68 条原为支持度二的行向后尾重写后，最终支持度一记录共有

\[
5\,128=5\,087_{\text{原一支持}}+41_{\text{二支持后移}}. \tag{3}
\]

脚本逐行完整分解 (1) 的 \(d\)，并相对该尾的规范基底 \(\mathcal B_m\) 记其唯一非基底
素数为 \(\ell\)。其指数剖面为

| \(v_\ell(d)\) | 1 | 2 | 3 | 4 |
|---:|---:|---:|---:|---:|
| 记录数 | 5,056 | 70 | 1 | 1 |

所有 5,128 条都以精确有理数重建 (1) 及 (2)，且该 \(\ell\) 均整除
\(u=(p+m)/(m+1)\)。所以这些不是单纯的因子统计，而是可核验的严格递降见证。

## 一次幂选择器的同尾边界

对每条选中高幂记录，进一步穷尽同一个最终尾的全部

\[
b\mid x^2,\qquad \operatorname{supp}(b)\subseteq\mathcal B_m,
\]

以及每个非基底素数 \(\ell\mid x\)，直接检查

\[
d=b\ell\le x,\qquad d\equiv-x\pmod m. \tag{4}
\]

结果为

\[
5\,082_{\text{存在一次幂证书}}+
46_{\text{不存在一次幂证书}}=5\,128. \tag{5}
\]

因此 46 条中的每一条在其**最终选定的全局尾**上都不能用 \(d=b\ell\) 替代；一个有效的
同尾自适应选择器必须允许 \(b\ell^e\) 的 \(e>1\)。这不排除这些点可能在另一个尾有一次幂
证书，也不表示所有核心素数都由一素数幂证书覆盖。

它把正向目标从“选一个新素数”修正为：

\[
\text{在某个自适应全局尾上，选 } \ell^e\mid u^2
\text{ 及基底部分，使 (1) 成立。} \tag{6}
\]

固定有限素数支持已由
[有限非基底素数支持障碍](h19-k23-global-tail-finite-support-menu-obstruction-2097152.md)
排除，故 \(\ell\) 和必要时的 \(e\) 都必须从实际因子化中无界地选择。

可复现命令：

~~~bash
python3 reproductions/h19_k23_global_one_prime_power_descent_profile.py \
  --global-input reproductions/h19-k23-full-global-tail-closure-2097152.json \
  --reroute-input reproductions/h19-k23-global-tail-one-support-closure-2097152.json \
  --output reproductions/h19-k23-global-one-prime-power-descent-profile-2097152.json
python3 -m unittest tests/test_h19_k23_global_one_prime_power_descent_profile.py -q
~~~
