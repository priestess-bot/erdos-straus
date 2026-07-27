---
kind: claim
claim_id: h19-k23-global-first-power-tail-reroute-2097152
title: H19-k23 全局尾的一新增素因子一次幂后移闭合
statement: 在 H19-k23 二百万层全局重写的最终5,128条一支持记录中，5,082条已在当前尾有 d=b*ell 形式的一次幂 Type II 证书；其余46条虽在当前尾不存在任何此类证书，却全部在某个严格更大的全局尾获得一次幂证书。因此该有限重写样本的所有一支持严格递降均可取唯一非基底素因子指数为1，代价是自适应地后移尾。
claim_status: computationally_reproduced
topics:
- type-II
- descent
- p-minus-one
- global-tail-menu
- factor-support
- prime-powers
- cross-tail
- computation
- h19
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-criterion
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 全局尾的一新增素因子一次幂后移闭合

[一素因子幂递降剖面](h19-k23-global-one-prime-power-descent-profile-2097152.md)
的 \(5\,128\) 条最终一支持记录中，72 条最初选中的除子带有
\(\ell^e,\ e>1\)。这并不自动说明跨尾选择器必须保留高幂。

对每条记录及其最终尾 \(m\)，完整枚举

\[
d=b\ell,\qquad
b\mid x^2,\quad \operatorname{supp}(b)\subseteq\mathcal B_m,\quad
\ell\notin\mathcal B_m,\quad
d\le x,\quad d\equiv-x\pmod m. \tag{1}
\]

其中 \(x=(p+m)/4\)、\(\mathcal B_m\) 为该尾的规范基底。结果分为：

\[
5\,128=5\,082_{\text{当前尾一次幂}}+
46_{\text{当前尾空}}. \tag{2}
\]

对后 46 条，不重复使用旧尾，而是在完整的有序 72 尾菜单中仅搜索严格更大的尾。每一条
都在一个后续尾命中 (1)：

\[
46=17_{47\to59}+7_{59,71,47\to79}+2_{71\to91}
+9_{\to95}+1_{35\to99}+7_{\to119}+3_{\to143}, \tag{3}
\]

式 (3) 只压缩地表示首个后续尾的频数；完整的旧尾到新尾对保存在复现产物中。所有新尾仍是
全局普通尾，故 \(m+1\mid p-1\)，脚本逐项重建 Type II 分母与

\[
n=\frac{p+m}{m+1}<p \tag{4}
\]

的严格双尾源。

所以在这 \(9\,825\) 条全局重写的最终一支持部分，实际得到

\[
\text{一新增素因子幂选择}
\quad\Longrightarrow\quad
\text{经自适应后移的一新增素因子一次幂选择}. \tag{5}
\]

这是一个完整的有限闭合，不是全称选择器定理；它不覆盖未写入该子样本的直接全局记录，也不证明
每个参数都能在 72 尾中找到一次幂因子。结合
[有限非基底素数支持障碍](h19-k23-global-tail-finite-support-menu-obstruction-2097152.md)，
其正向含义是：可优先研究**跨尾、一次幂、但素数无界自适应**的选择器，而不必先处理高幂。

可复现命令：

~~~bash
python3 reproductions/h19_k23_global_first_power_tail_reroute.py \
  --profile-input reproductions/h19-k23-global-one-prime-power-descent-profile-2097152.json \
  --output reproductions/h19-k23-global-first-power-tail-reroute-2097152.json
python3 -m unittest tests/test_h19_k23_global_first_power_tail_reroute.py -q
~~~
