---
kind: claim
claim_id: type-II-single-new-factor-release
title: H19 新因子状态的单因子释放审计
statement: 在 p<=3*10^8、s<=200 的 H19 首次无旧私有因子 Type II 剖面中，260个含新因子的状态有223个首次即只含一个新因子；余下37个首次含两个或三个新因子的状态全部在后续移位中获得只含一个新因子的无旧私有证书，最迟s=96。因此该有限范围的全部新因子状态均可取单新因子证书。
claim_status: computationally_reproduced
topics:
- type-II
- multishift
- factorization
- new-factor
- transition
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-certificate-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-25'
---

# H19 新因子状态的单因子释放审计

## 问题

[首次无旧私有因子深度谱](type-II-source-free-transition-profile.md) 在三亿范围中给出
328 个 H19 残余的首次无复用 Type II 证书。其中 68 张仅用旧碰撞因子，260 张含有
新因子。这里仅对后者检验：若首张无复用证书需要多个新因子，单新因子是否会在后续
移位出现？

“单新因子”指证书因子 \(h\) 在 H19 旧来源素因子集以外的素因子重数之和为一；它可以
同时含有任意个旧碰撞因子，但不含旧私有因子。

## 三亿审计

运行：

    python3 reproductions/type_ii_single_new_factor_release.py \
      --input reproductions/type-ii-source-free-transition-h19-300m-results.json

在 260 个新因子状态中，223 个首次即为单新因子。余下 37 个的首张证书中，36 个有
两个新因子、1 个有三个新因子；完整后续扫描得到

\[
37\longrightarrow37,\qquad
\max\{\text{首个单新因子移位}\}=96. \tag{1}
\]

故全部 260 个新因子状态在 \(s\le96\) 可选择单新因子证书。最晚者仍为

\[
p=4{,}722{,}169,\qquad s=96,\qquad h=1151. \tag{2}
\]

唯一首张证书含三个新因子的点是

\[
p=113{,}509{,}489;
\]

它在 \(s=38\) 释放为 \(h=3\cdot5{,}405{,}221\) 的单新因子证书。

## 含义与边界

结合静态碰撞剥离，有限范围的 H19 残余已被压缩为两种单一出口：固定碰撞射线，或
只引入一个新因子的 Type II 证书。后者仍允许任意大的 \(k\)，因而这不支持固定尺度
选择器；例如 (2) 的 \(k=12\)，而其他单新因子见证可大得多。

这是有限选择规律，而不是新因子必然出现或必在固定深度出现的定理。下一条正向引理应
研究一个新素因子与碰撞残数如何共同满足 \(h\equiv-1\pmod{4ac}\)，或在失败时如何导出
真正可提升的递降。

## 重建

    python3 reproductions/type_ii_single_new_factor_release.py
    python3 -m unittest tests/test_type_ii_single_new_factor_release.py -q
